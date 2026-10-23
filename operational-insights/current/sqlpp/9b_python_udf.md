---
title: Python User-Defined Functions
description: Python User-Defined Functions (UDFs) let you extend SQL++ with code
  written in Python, running inside an isolated sandbox.
pubDate: 2026-10-23T04:31:18.652Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/sqlpp/pages/9b_python_udf.adoc
  xref: xref:enterprise-analytics:sqlpp:9b_python_udf.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/sqlpp/9b_python_udf.html)

# Python User-Defined Functions

> Python User-Defined Functions (UDFs) let you extend SQL++ with code written in Python, running inside an isolated sandbox. Use a Python UDF to bring a trained ML model into a query, or to implement logic that's difficult or impossible to express in SQL++. 

For the `CREATE FUNCTION` syntax that binds a Python function, see [Creating an External Function](9%5Fudf.md#create-external-function).

## [](#prerequisites)Prerequisites

Python UDFs require the separate `operational-insights-udf` add-on package, installed on every node. Without it, no node binds a socket for library uploads, so no node can evaluate a Python UDF.

Installing this package requires Docker on the host. Docker is not a declared dependency of the package, so the install fails if Docker is missing. The package installs the gVisor `runsc` runtime, and pulls and runs the `couchbase/operational-insights-udf` container image.

For installation, upgrade, and removal steps, see [Install the Python UDF Add-on](../install/install-udf-addon.md).

## [](#security)Security

Python UDFs run inside a restricted sandbox, isolated from the rest of the Operational Insights cluster. Inside the sandbox:

* 1 sandbox container runs per node, shared by every library on that node. It bind-mounts the applications directory read-only, so a function can read the files of every library on the node, even though only its own library's modules can be its entry point.
* The function has no network access.
* The function can write files within its own sandbox, though this is not recommended. It cannot reach any file system outside the sandbox.
* The sandbox container runs as the `couchbase` user.

Uploading a Python library requires the `cluster.admin.diag!write` privilege, normally reserved for the Full Administrator role, and is only possible over a local, restricted interface. Operational Insights blocks upload requests from non-local origins.

Creating a function from an uploaded library requires 2 privileges: `CREATE FUNCTION` on the scope where you create the function, and `USAGE` on the library. Operational Insights checks `USAGE` only when you create the function. Calling the function afterwards requires only `EXECUTE` on the function, even without `USAGE` on the library, and revoking `USAGE` from the function's creator does not affect functions they already created. For information about granting these privileges, see [GRANT Statement](5%5Fddl%5Fgrant%5Fstatement.md).

> [!IMPORTANT]
> Vet any code that's part of a library carefully. Once an administrator exposes a function from a library with `CREATE FUNCTION`, anyone with `EXECUTE` on that function can call it.

For an overview of the sandboxing technology that isolates Python UDFs, see [Security Considerations](../install/security-considerations.md).

## [](#execution-model)Execution Model

Operational Insights deploys queries across the cluster as parallel jobs. For the purposes of a Python UDF, a job's lifecycle has 3 phases:

* A pre-run phase that allocates resources, called `open`.
* The phase during which data flows through the job, called `nextFrame`.
* Cleanup and shutdown, called `close`.

If your function is a method on a class, Operational Insights instantiates the class during `open`, and the instance exists in memory for the lifetime of the query. If your function needs to reference files or other data that's costly to load per call, initialize it as a member variable in the class constructor instead of loading it on every call. This significantly improves performance.

Operational Insights runs an independent instance of the function per compute partition. Because of this, a function must not assume any global state, or make assumptions about how the data is laid out. The function runs in parallel to the same degree as the data parallelism of the cluster, that is, the number of compute partitions.

After initialization, Operational Insights calls the bound function once per tuple during query execution, and skips calling the function for `NULL` values by default. You can change this behavior with the `null-call` parameter. For details, see [Creating an External Function](9%5Fudf.md#create-external-function).

If a function raises an exception, Operational Insights logs a warning and returns `NULL` for that tuple, instead of failing the query.

At the end of the query, Operational Insights tears down the function instance and does not reuse it. A function should be free of side effects, such as writing files or editing remote state. The query optimizer does not account for such side effects, so a function that has them produces unpredictable results depending on how a query uses it.

## [](#type-mappings)Type Mappings

Python UDFs currently support only the following SQL++ types. Cast any other type to one of these before passing it to a Python UDF.

| SQL++ Type                                     | Python Type |
| ---------------------------------------------- | ----------- |
| Integer types (tinyint, smallint, int, bigint) | int         |
| Floating-point types (float, double)           | float       |
| string                                         | str         |
| boolean                                        | bool        |
| array, multiset                                | list        |
| object                                         | dict        |
| binary                                         | bytes       |
| null, missing                                  | None        |

A value a Python UDF returns maps back to SQL++ in a similar way: for example, a Python `int` comes back as a SQL++ `bigint`, and a `float` comes back as a `double`.

## [](#Packaging)Packaging a Python Library

Package a Python UDF, along with any dependencies that are not already available in the sandbox, using [shiv](https://github.com/linkedin/shiv). Packaging your code with shiv means each library carries exactly the dependencies it needs, alongside the code itself, which greatly reduces the chance of conflicting package versions between libraries.

The sandbox runs Python 3.11 on Debian 12 (bookworm, glibc 2.36). It uses either the x86\_64 or ARM64 architecture, matching the node it runs on. Besides the Python standard library, it ships with only `python3-msgpack` preinstalled. You need to bundle every other dependency your function requires, including common packages such as `numpy`, with shiv.

When you package dependencies with shiv, any binary wheel it pulls in must be a CPython 3.11 (`cp311`) Linux wheel built for the node's architecture, using a `manylinux` build tagged for glibc 2.36 or earlier, such as `manylinux2014` or `manylinux_2_17`. `musllinux`, macOS, and Windows wheels do not load in the sandbox. A pure-Python package, with no compiled extensions, works on either architecture. Avoid bundling dependencies that require a particular platform or architecture if you can avoid it, since these can behave unpredictably when the sandbox is updated.

The `maxWebRequestSize` parameter in the Analytics Service configuration determines the maximum size of an uploaded library. If your packaged library is 200 MB or larger, you might need to raise this value. Avoid using extremely large libraries, since this can slow performance.

## [](#tutorial)Tutorial

This tutorial packages a sentiment-analysis function, deploys it as a library, and binds it to a SQL++ function.

1. Create a file named `sentiment_mod.py`:  
```python  
import os  
class sent_model:  
    def __init__(self):  
        good_words = os.path.join(os.path.dirname(__file__), 'good.txt')  
        with open(good_words) as f:  
            self.whitelist = f.read().splitlines()  
    def sentiment(self, text: str) -> str:  
        for word in text.split():  
            if word in self.whitelist:  
                return 'great'  
        return 'eh'  
```  
In the same directory, create a file named `good.txt` containing:  
spam  
eggs  
ham
2. In the module directory, run shiv to bundle the code with its dependencies. This function does not use any external packages, but you would list them the same way if it did.  
```console  
shiv -o lib.pyz --site-packages .  
```
3. Deploy the packaged library, named `pylib`, to the `Default` scope. This requires the `cluster.admin.diag!write` privilege, normally available only to the Full Administrator role, and the request must go to a local Unix domain socket. Each node has its own socket, at `<install_path>/var/<node_uuid_prefix>_oi_lib.sock`, where `<node_uuid_prefix>` is the first 8 characters of that node's UUID.  
```console  
curl -u Administrator:password --unix-socket /opt/couchbase/var/1a2b3c4d_oi_lib.sock \
  -F "type=python" -F "data=@./lib.pyz" http://localhost/api/v1/library/Default/pylib  
```  
Operational Insights uploads and extracts the library to every node in the cluster using a 2-phase commit protocol, so the request can take some time to return, depending on the size of the library. Once the request returns a `200 OK` response with an empty `{}` body, the library is ready to use.
4. Expose the `sentiment` method on the `sent_model` class as a SQL++ function:  
```SQL++  
 CREATE FUNCTION sentiment(text)  
    AS "sentiment_mod", "sent_model.sentiment" AT pylib  
    WITH { "deterministic": false };  
```  
For details on this syntax, see [Creating an External Function](9%5Fudf.md#create-external-function).
5. Call `sentiment` like any other SQL++ function:  
```SQL++  
 SELECT VALUE sentiment("I bought spam and eggs");  
```  
Result  
[  
  "great"  
]

## [](#see-also)See Also

* [User-Defined Functions](9%5Fudf.md)
* [GRANT Statement](5%5Fddl%5Fgrant%5Fstatement.md)
* [Security Considerations](../install/security-considerations.md)