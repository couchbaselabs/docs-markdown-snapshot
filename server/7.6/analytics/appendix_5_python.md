---
title: "Appendix 5: Python UDFs"
description: A short guide and tutorial regarding the use of Python user-defined functions
editUrl: https://github.com/couchbase/docs-analytics/edit/release/7.6/modules/analytics/pages/appendix_5_python.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.6@server:analytics:appendix_5_python.adoc[]
---

[View original HTML](/server/7.6/analytics/appendix_5_python.html)

# Appendix 5: Python UDFs

## [](#function-authors-guide)Function Author’s Guide

Python UDFs in Analytics are designed first and foremost to give maximum freedom to the user, and as such almost any Python code can be bound as a function. However, to achieve the best performance and security, it is good to keep in mind how Analytics runs and utilizes your Python code.

### [](#security)Security

Python UDFs are run as the same user as the Couchbase Analytics process itself. To enable maximum flexibility for cases where specialized hardware (e.g. GPUs) might be needed for the function, no additional sandboxing or other code and process isolation techniques are used. This is similar to an unfenced external function in a traditional RDBMS.

Therefore any code that is part of a Library should be very carefully vetted for the possibility of misuse or accidental damage to the Couchbase cluster. Once a function is exposed from a library via `CREATE ANALYTICS FUNCTION` by an administrator with `cluster.analytics!manage`, it will become available to anyone with `cluster.analytics!select` to execute.

For the above reasons, Library uploads are highly privileged and correspondingly restricted, as well as the aforementioned restriction binding of those library artifacts into SQL++ for Analytics via `CREATE ANALYTICS FUNCTION`. Library uploads can only be accomplished via the loopback interface by an administrator with the privilege `cluster.admin.diag!write`.

### [](#execution-model)Execution Model

Analytics queries are deployed across the cluster as Hyracks jobs. A Hyracks job has a lifecycle that can be simplified for the purposes of UDFs to

* A pre-run phase which allocates resources, `open`
* The time during which the job has data flowing through it, `nextFrame`
* Cleanup and shutdown in `close`.

If a SQL++ for Analytics function is defined as a member of a class in the library, the class will be instantiated during `open`. The class will exist in memory for the lifetime of the query. Therefore if your function needs to reference files or other data that would be costly to load per-call, making it a member variable that is initialized in the constructor of the object will greatly increase the performance of the function.

For each function invoked during a query, there will be an independent instance of the function per data partition. This means that the function must not assume there is any global state or that it can assume things about the layout of the data. The execution of the function will be parallel to the same degree as the level of data parallelism in the cluster (e.g. the number of Analytics data partitions)

After initialization, the function bound in the SQL++ for Analytics function definition is called once per tuple during the query execution (i.e. `nextFrame`). Unless the function specifies `null-call` in the `WITH` clause, `NULL` values will be skipped.

At the close of the query, the function is torn down and not re-used in any way. All functions should assume that nothing will persist in-memory outside of the lifetime of a query, and any behavior contrary to this is undefined. Concretely, this means that the function should be free of side effects like writing files or editing state remotely. The query optimizer has no accommodation for this behavior, so any function that does this will have unpredictable behavior depending on how it is used in a query.

### [](#type-mappings)Type Mappings

Currently only a subset of types are supported in Python UDFs. The supported types are as follows:

* Integer types (int8,16,32,64)
* Floating point types (float, double)
* String
* Boolean
* Arrays, Sets (cast to lists)
* Objects (cast to dict)

Unsupported types can be cast to these in SQL++ for Analytics first in order to be passed to a Python UDF.

### [](#packaging)Packaging

Python UDFs need to be rolled into a [shiv](https://github.com/linkedin/shiv) package with all their dependencies. By default Couchbase Analytics will use its own integrated Python 3.9 interpreter. This can be changed in the cluster config using the `python.path` configuration variable.

The purpose of using `shiv` is so that the library can be uploaded with exactly the dependencies that are necessary, with the library itself. In this way every library has its own dependencies residing with it on the server. Thus, the possibility of conflicting versions of different packages is greatly reduced.

`shiv` targets the architecture, platform and Python version on which it is run. This will lead to issues if a library has dependencies that use native code (e.g. `numpy`), and the server has a different platform like Linux. `shiv` takes most arguments from pip, so the appropriate arguments to retrieve wheels for the correct target platform can be passed. For example, to target a Linux x86 platform for scikit-learn with Python 3.9, the command would look something like:

shiv -o lib.pyz --site-packages . --platform manylinux2010_x86_64 --python-version 39 --only-binary=:all: scikit-learn

The maximum allowed size of an uploaded library is determined by the `maxWebRequestSize` parameter value in the Analytics Service configuration. If the crafted library is very large (512MB or more), this limit may need to be reconfigured to a higher value.

## [](#tutorial)Tutorial

First, devise a function that you would like to use, `sentiment_mod.py`:

import os
from typing import Tuple
class sent_model:

    def __init__(self):
        good_words = os.path.join(os.path.dirname(__file__), 'good.txt')
        with open(good_words) as f:
            self.whitelist = f.read().splitlines()

    def sentiment(self, arg: Tuple[str])-> str:
        words = arg[0].split()
        for word in words:
            if word in self.whitelist:
                return 'great'

        return 'eh'

Furthermore, let’s assume 'good.txt' contains the following entries:

spam
eggs
ham

Now, in the module directory, execute `shiv` with all the dependencies of the module listed. This function doesn’t actually use scikit-learn here, but it’s just included as an example of a real module dependency. This command will wrap up the code that was just written, along with any dependencies it might have, so the server can keep all dependencies of each library separate from one another.

shiv -o lib.pyz --site-packages . scikit-learn

Then, deploy it with the library name `pylib` in the `Default` scope, or a scope of our choosing. This requires the permission `cluster.admin.diag!write`, which is normally only available to the role `Full Administrator`. This request must also originate locally from a node that is running Analytics. Upload requests from non-local origins are blocked for security purposes. See the [Analytics Library REST API](../analytics-rest-library/index.md) for complete details.

curl -X POST -u couchbase:couchbase -F "type=python" -F "data=@./lib.pyz" localhost:8095/analytics/library/Default/pylib

This request uploads and extracts the library across all nodes in the cluster, using a 2 phase commit protocol to ensure that each node has the complete library. Therefore it may take some time to return, dependent on the size of the uploaded library. Once a `200 OK` has been returned by the server, the upload is complete and the library is ready to use.

With the library deployed, you can define a function within it for use. For example, to expose the Python function `sentiment` in the module `sentiment_mod` in the class `sent_model`, the DDL would be as follows:

CREATE ANALYTICS FUNCTION sentiment(a)
  AS "sentiment_mod", "sent_model.sentiment" AT pylib;

By default, Analytics will treat all external functions as deterministic. It means the function must return the same result for the same input, irrespective of when or how many times the function is called on that input. This particular function behaves the same on each input, so it satisfies the deterministic property. This enables better optimization of queries including this function. If a function is not deterministic then it should be declared as such by using a `WITH` sub-clause:

CREATE ANALYTICS FUNCTION sentiment(text)
  AS "sentiment_mod", "sent_model.sentiment" AT pylib
  WITH { "deterministic": false }

With the function now defined, it can then be used as any other scalar Analytics function would be. See [User-Defined Functions](9%5Fudf.md) for details of the SQL++ for Analytics syntax for creating external functions.