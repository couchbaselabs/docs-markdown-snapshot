---
title: Start Using the Python SDK
description: Get up and running quickly, installing the Couchbase Python SDK,
  and running our Hello World example.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-python/edit/temp/4.3/modules/hello-world/pages/start-using-sdk.adoc
  xref: xref:4.3@python-sdk:hello-world:start-using-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-sdk/4.3/hello-world/start-using-sdk.html)

# Start Using the Python SDK

> Get up and running quickly, installing the Couchbase Python SDK, and running our Hello World example. 

The Couchbase Python SDK allows Python applications to access a Couchbase cluster. It offers a traditional synchronous API as well as integration with _twisted_ and _asyncio_.

In this guide, you will learn:

* How to [connect to Couchbase Capella or Couchbase Server](#connect).
* How to [add and retrieve Documents](#add-and-retrieve-documents).
* How to [lookup documents](#sql-lookup) with the [SQL++ (formerly N1QL)](https://www.couchbase.com/products/n1ql) query language.

## [](#hello-couchbase)Hello Couchbase

We will go through the code sample step by step, but for those in a hurry to see it, here it is:

* Couchbase Capella Sample
* Local Couchbase Server

To connect to [Couchbase Capella](../../../home/cloud.md), be sure to get the correct endpoint as well as user, password, and bucket name. The certificate for connecting to Capella is included in the 4.1 Python SDK.

```python
from datetime import timedelta

# needed for any cluster connection
from couchbase.auth import PasswordAuthenticator
from couchbase.cluster import Cluster
# needed for options -- cluster, timeout, SQL++ (N1QL) query, etc.
from couchbase.options import (ClusterOptions, ClusterTimeoutOptions,
                               QueryOptions)


# Update this to your cluster
endpoint = "--your-instance--.dp.cloud.couchbase.com"
username = "username"
password = "Password!123"
bucket_name = "travel-sample"
# User Input ends here.

# Connect options - authentication
auth = PasswordAuthenticator(username, password)

# get a reference to our cluster
options = ClusterOptions(auth)
# Sets a pre-configured profile called "wan_development" to help avoid latency issues
# when accessing Capella from a different Wide Area Network
# or Availability Zone(e.g. your laptop).
options.apply_profile('wan_development')
cluster = Cluster('couchbases://{}'.format(endpoint), options)

# Wait until the cluster is ready for use.
cluster.wait_until_ready(timedelta(seconds=5))

# get a reference to our bucket
cb = cluster.bucket(bucket_name)

cb_coll = cb.scope("inventory").collection("airline")


def upsert_document(doc):
    print("\nUpsert CAS: ")
    try:
        # key will equal: "airline_8091"
        key = doc["type"] + "_" + str(doc["id"])
        result = cb_coll.upsert(key, doc)
        print(result.cas)
    except Exception as e:
        print(e)

# get document function


def get_airline_by_key(key):
    print("\nGet Result: ")
    try:
        result = cb_coll.get(key)
        print(result.content_as[str])
    except Exception as e:
        print(e)

# query for new document by callsign


def lookup_by_callsign(cs):
    print("\nLookup Result: ")
    try:
        inventory_scope = cb.scope('inventory')
        sql_query = 'SELECT VALUE name FROM airline WHERE callsign = $1'
        row_iter = inventory_scope.query(
            sql_query,
            QueryOptions(positional_parameters=[cs]))
        for row in row_iter:
            print(row)
    except Exception as e:
        print(e)


airline = {
    "type": "airline",
    "id": 8091,
    "callsign": "CBS",
    "iata": None,
    "icao": None,
    "name": "Couchbase Airways",
}

upsert_document(airline)

get_airline_by_key("airline_8091")

lookup_by_callsign("CBS")
```

```python
from datetime import timedelta

# needed for any cluster connection
from couchbase.auth import PasswordAuthenticator
from couchbase.cluster import Cluster
# needed for options -- cluster, timeout, SQL++ (N1QL) query, etc.
from couchbase.options import (ClusterOptions, ClusterTimeoutOptions,
                               QueryOptions)

# Update this to your cluster
username = "Administrator"
password = "password"
bucket_name = "travel-sample"
# User Input ends here.

# Connect options - authentication
auth = PasswordAuthenticator(
    username,
    password,
)

# Get a reference to our cluster
# NOTE: For TLS/SSL connection use 'couchbases://<your-ip-address>' instead
cluster = Cluster('couchbase://your-ip', ClusterOptions(auth))

# Wait until the cluster is ready for use.
cluster.wait_until_ready(timedelta(seconds=5))

# get a reference to our bucket
cb = cluster.bucket(bucket_name)

cb_coll = cb.scope("inventory").collection("airline")

# Get a reference to the default collection, required for older Couchbase server versions
cb_coll_default = cb.default_collection()

# upsert document function


def upsert_document(doc):
    print("\nUpsert CAS: ")
    try:
        # key will equal: "airline_8091"
        key = doc["type"] + "_" + str(doc["id"])
        result = cb_coll.upsert(key, doc)
        print(result.cas)
    except Exception as e:
        print(e)

# get document function


def get_airline_by_key(key):
    print("\nGet Result: ")
    try:
        result = cb_coll.get(key)
        print(result.content_as[str])
    except Exception as e:
        print(e)

# query for new document by callsign


def lookup_by_callsign(cs):
    print("\nLookup Result: ")
    try:
        inventory_scope = cb.scope('inventory')
        sql_query = 'SELECT VALUE name FROM airline WHERE callsign = $1'
        row_iter = inventory_scope.query(
            sql_query,
            QueryOptions(positional_parameters=[cs]))
        for row in row_iter:
            print(row)
    except Exception as e:
        print(e)


airline = {
    "type": "airline",
    "id": 8091,
    "callsign": "CBS",
    "iata": None,
    "icao": None,
    "name": "Couchbase Airways",
}

upsert_document(airline)

get_airline_by_key("airline_8091")

lookup_by_callsign("CBS")
```

As well as the Python SDK (see below), and a running instance of Couchbase Server, you will need to load up the Travel Sample Bucket using either the [Web interface](../../../server/7.6/manage/manage-settings/install-sample-buckets.md#install-sample-buckets-with-the-ui)or the [command line](../../../server/7.6/manage/manage-settings/install-sample-buckets.md#install-sample-buckets-with-the-cli).

The [Couchbase Capella free tier](https://cloud.couchbase.com/sign-up) version comes with the Travel Sample Bucket, and its Query indexes, loaded and ready.

## [](#quick-installation)Quick Installation

The SDK will run on [supported versions Python](#compatibility.adoc#python-version-compat). A more detailed guide in our [Installation page](../project-docs/sdk-full-installation.md) covers every supported platform, but this section should be enough to get up and running for _most_ [supported Operating Systems](#compatibility.adoc#platform-compatibility).

* macOS 12 & 13
* Red Hat & CentOS
* Debian & Ubuntu
* Windows

If you are running Catalina (macOS 10.15) — or have other detailed requirements — take a look at our [full installation guide](#project-pages:sdk-full-installation.adoc). Otherwise, read on for a quick install on macOS _Big Sur_ or _Monterey_.

The Python SDK has wheels are available on macOS for [supported versions of Python](#compatibility.adoc#python-version-compat).

First, make sure that your _brew_ package index is up-to-date:

```console
$ brew update
```

Install a compatible Python 3:

```console
$ brew install python3
```

Ensure that the Python installation can be called from the shell:

```console
$ echo 'export PATH="/usr/local/bin:"$PATH' >> ~/.zshrc
```

```console
$ source ~/.zshrc
```

Now, install the Python SDK:

```console
$ sudo -H python3 -m pip install couchbase
```

> [!NOTE]
> Starting with Python 3.11.5, macOS installers from python.org now use [OpenSSL 3.0](https://docs.python.org/3/whatsnew/3.11.html#notable-changes-in-3-11-5). If using a version prior to 4.1.9 of the Python SDK, a potential side-effect of this change is an `ImportError: DLL load failed while importing pycbc_core` error. Upgrade the SDK to a version >= 4.1.9 to avoid this side-effect. If unable to upgrade, a work-around is to set the `PYCBC_OPENSSL_DIR` environment variable to the path where the OpenSSL 1.1 libraries (`` libssl.1.1.dylib ` and `libcrypto.1.1.dylib ``) can be found.

Note, check that you have a [supported version of Python](#compatibility.adoc#python-version-compat). Suggestions for platforms with an outdated build chain, such as CentOS 7, can be found in our [Installation Guide](../project-docs/sdk-full-installation.md). Assuming you have an updated build environment, follow these steps.

The Python SDK has manylinux wheels available for [supported versions of Python](#compatibility.adoc#python-version-compat).

During first-time setup, install the prerequisites:

```console
$ sudo yum install gcc gcc-c++ git python3-devel python3-pip
```

Full details of prerequisites can be found [here](../project-docs/sdk-full-installation.md#requirements).

Now you can install the latest Python SDK (for older versions, see the [Release Notes page](../project-docs/sdk-release-notes.md)):

```console
$ python3 -m pip install couchbase
```

Note, check that you have a [supported version of Python](#compatibility.adoc#python-version-compat). Suggestions for platforms with an outdated build chain, such as Debian 9, can be found in our [Installation Guide](../project-docs/sdk-full-installation.md). Assuming you have an updated build environment, follow these steps.

The Python SDK has manylinux wheels available for [supported versions of Python](#compatibility.adoc#python-version-compat).

During first-time setup, install the prerequisites:

```console
$ sudo apt-get install git python3-dev python3-pip python3-setuptools build-essential
```

Full details of prerequisites can be found [here](../project-docs/sdk-full-installation.md#requirements).

Now you can install the latest Python SDK (for older versions, see the [Release Notes page](../project-docs/sdk-release-notes.md)):

```console
$ python3 -m pip install couchbase
```

Download and install Python from [python.org](https://www.python.org/downloads). Best practice is to use a Python virtual environment such as _venv_ or _pyenv_.

> [!TIP]
> Checkout the [pyenv-win](https://github.com/pyenv-win/pyenv-win) project to manage multiple versions of Python.

The Python SDK has wheels available on Windows for [supported versions of Python](#compatibility.adoc#python-version-compat).

```console
python -m pip install couchbase
```

> [!NOTE]
> Starting with Python 3.11.5, Windows builds from python.org now use [OpenSSL 3.0](https://docs.python.org/3/whatsnew/3.11.html#notable-changes-in-3-11-5). If using a version prior to 4.1.9 of the Python SDK, a potential side-effect of this change is an `ImportError: DLL load failed while importing pycbc_core` error. Upgrade the SDK to a version >= 4.1.9 to avoid this side-effect. If unable to upgrade, a work-around is to set the `PYCBC_OPENSSL_DIR` environment variable to the path where the OpenSSL 1.1 libraries (`libssl-1_1.dll` and `libcrypto-1_1.dll`) can be found.

The standard Python distributions for Windows include OpenSSL DLLs, as PIP and the inbuilt `ssl` module require it for correct operation. Prior to version 4.1.9 of the Python SDK, the binary wheels for Windows are built against OpenSSL 1.1\. Version 4.1.9 and beyond statically link against BoringSSL thus removing the OpenSSL requirement.

> [!NOTE]
> If you require a version that doesn't have a suitable binary wheel on PyPI, follow the [build instructions](https://github.com/couchbase/couchbase-python-client#alternative-installation-methods) on the GitHub repo.

If there are any problems, refer to the full [Installation page](../project-docs/sdk-full-installation.md).

## [](#prerequisites)Prerequisites

The following code samples assume:

* Couchbase Capella
* Local Couchbase Server

* You have signed up to [Couchbase Capella](https://cloud.couchbase.com/sign-up).
* You have created your own bucket, or loaded the Travel Sample dataset. Note, the Travel Sample dataset is installed automatically when deploying a Capella free tier cluster.
* A user is created with permissions to access the cluster (at least Application Access permissions). See the [Capella connection page](../../../cloud/get-started/run-first-queries.md#credentials) for more details.

> [!IMPORTANT]
> Couchbase Capella uses [Roles](../../../cloud/organizations/organization-projects-overview.md) to control user access to cluster resources. For the purposes of this guide, you can use the **Organization Owner** role automatically assigned to your account during installation of the Capella cluster. In a production scenario, we strongly recommend setting up users with more granular access roles as a best practice.

* [Couchbase Server](#7.6@server:getting-started/do-a-quick-install.adoc) is installed and accessible locally.
* You have created your own bucket, or loaded the Travel Sample dataset using the [Web interface](../../../server/7.6/manage/manage-settings/install-sample-buckets.md#install-sample-buckets-with-the-ui).
* A user is created with permissions to access your cluster (at least Application Access permissions). See [Manage Users, Groups and Roles](../../../server/7.6/manage/manage-security/manage-users-and-roles.md) for more details.

> [!IMPORTANT]
> Couchbase Server uses [Role Based Access Control (RBAC)](../../../server/7.6/learn/security/roles.md) to control access to resources. In this guide we suggest using the **Full Admin** role created during setup of your local Couchbase Server cluster. For production client code, you will want to use more appropriate, restrictive settings.

## [](#step-by-step)Step-by-Step

At this point we want to transition from the terminal to your code editor of choice.

Let's now create an empty file named `cb-test.py` and walk through adding code step-by-step.

Here are all the import statements that you will need to run the sample code:

```python
from datetime import timedelta

# needed for any cluster connection
from couchbase.auth import PasswordAuthenticator
from couchbase.cluster import Cluster
# needed for options -- cluster, timeout, SQL++ (N1QL) query, etc.
from couchbase.options import (ClusterOptions, ClusterTimeoutOptions,
                               QueryOptions)
```

### [](#connect)Connect

The basic connection details that you'll need are given below — for more background information, refer to the [Managing Connections page](../howtos/managing-connections.md#connection-strings).

* Couchbase Capella
* Local Couchbase Server

From version 4.0, the Python SDK includes Capella's standard certificates by default, so you don't need any additional configuration. You do need to enable TLS, which can be done by simply using `couchbases://` in the connection string as in this example.

```python
# Update this to your cluster
endpoint = "--your-instance--.dp.cloud.couchbase.com"
username = "username"
password = "Password!123"
bucket_name = "travel-sample"
# User Input ends here.

# Connect options - authentication
auth = PasswordAuthenticator(username, password)

# get a reference to our cluster
options = ClusterOptions(auth)
# Sets a pre-configured profile called "wan_development" to help avoid latency issues
# when accessing Capella from a different Wide Area Network
# or Availability Zone(e.g. your laptop).
options.apply_profile('wan_development')
cluster = Cluster('couchbases://{}'.format(endpoint), options)

# Wait until the cluster is ready for use.
cluster.wait_until_ready(timedelta(seconds=5))
```

When accessing Capella from a different Wide Area Network or Availability Zone, you may experience latency issues with the default connection settings. SDK 4.1 introduces a `wan_development` Configuration Profile, which provides pre-configured timeout settings suitable for working in high latency environments. Basic usage is shown in the example above, but if you want to learn more see [Constrained Network Environments](../ref/client-settings.md#constrained-network-environments).

> [!CAUTION]
> The Configuration Profiles feature is currently a [Volatile API](../../current/project-docs/compatibility.md#interface-stability) and may be subject to change.

```python
# Update this to your cluster
username = "Administrator"
password = "password"
bucket_name = "travel-sample"
# User Input ends here.

# Connect options - authentication
auth = PasswordAuthenticator(
    username,
    password,
)

# Get a reference to our cluster
# NOTE: For TLS/SSL connection use 'couchbases://<your-ip-address>' instead
cluster = Cluster('couchbase://your-ip', ClusterOptions(auth))

# Wait until the cluster is ready for use.
cluster.wait_until_ready(timedelta(seconds=5))
```

For developing locally on the same machine as Couchbase Server, your URI can be `couchbase://localhost`. For production deployments, you will want to use a secure server, with `couchbases://`.

Following successful authentication, add this code snippet to access your `Bucket`:

```python
# get a reference to our bucket
cb = cluster.bucket(bucket_name)
```

### [](#add-and-retrieve-documents)Add and Retrieve Documents

The Python SDK supports full integration with the [Collections](../concept-docs/collections.md) feature introduced in Couchbase Server 7.0\. **Collections** allow documents to be grouped by purpose or theme, according to a specified _Scope_.

Here we refer to the `users` collection within the `tenant_agent_00` scope from the Travel Sample bucket as an example, but you may replace this with your own data.

```python
cb_coll = cb.scope("inventory").collection("airline")
```

The code shows how you would use a named collection and scope.

> [!IMPORTANT]
> For Local Couchbase Server only
> 
> The `default_collection` must be used when connecting to a 6.6 cluster or earlier.
> 
> ```python
> # Get a reference to the default collection, required for older Couchbase server versions
> cb_coll_default = cb.default_collection()
> ```

Let's create a dictionary object in our application that we can add to our `travel-sample` bucket that conforms to the structure of a document of type `airline`.

```python
airline = {
    "type": "airline",
    "id": 8091,
    "callsign": "CBS",
    "iata": None,
    "icao": None,
    "name": "Couchbase Airways",
}
```

[Data operations](../howtos/kv-operations.md), such as storing and retrieving documents, can be done using simple methods on the `Collection` class such as `Collection.get` and `Collection.upsert`. Simply pass the key (and value, if applicable) to the relevant methods.

The following function will _upsert_ a document and print the returned [CAS](../howtos/concurrent-document-mutations.md) value:

```python


def upsert_document(doc):
    print("\nUpsert CAS: ")
    try:
        # key will equal: "airline_8091"
        key = doc["type"] + "_" + str(doc["id"])
        result = cb_coll.upsert(key, doc)
        print(result.cas)
    except Exception as e:
        print(e)
```

Call the `upsert_document()` function passing in our `airline` document:

```python
upsert_document(airline)
```

Now let's retrieve that document using a key-value operation. The following function runs a `get()` for a document key and either logs out the result or error in our console:

```python
# get document function


def get_airline_by_key(key):
    print("\nGet Result: ")
    try:
        result = cb_coll.get(key)
        print(result.content_as[str])
    except Exception as e:
        print(e)
```

Call the `get_airline_by_key` function passing in our valid document key `airline_8091`:

```python
get_airline_by_key("airline_8091")
```

### [](#sql-lookup)SQL++ Lookup

Couchbase SQL++ queries can be performed at the `Cluster` or `Scope` level by invoking `Cluster.query()` or `Scope.query()`.

Cluster level queries require you to specify the fully qualified keyspace each time (e.g. `travel-sample.inventory.airline`). However, with a Scope level query you only need to specify the Collection name — which in this case is `airline`:

```python
# query for new document by callsign


def lookup_by_callsign(cs):
    print("\nLookup Result: ")
    try:
        inventory_scope = cb.scope('inventory')
        sql_query = 'SELECT VALUE name FROM airline WHERE callsign = $1'
        row_iter = inventory_scope.query(
            sql_query,
            QueryOptions(positional_parameters=[cs]))
        for row in row_iter:
            print(row)
    except Exception as e:
        print(e)
```

We call the `lookup_by_callsign` function passing in our callsign `CBS`:

```python
lookup_by_callsign("CBS")
```

### [](#execute)Execute!

Now we can run our code using the following command:

```console
$ python3 cb-test.py
```

The results you should expect are as follows:

```console
Upsert CAS:
1598469741559152640

Get Result:
{'type': 'airline', 'id': 8091, 'callsign': 'CBS', 'iata': None, 'icao': None, 'name': 'Couchbase Airways'}

Lookup Result:
Couchbase Airways
```

## [](#next-steps)Next Steps

Now you're up and running, try one of the following:

* Our [Travel Sample Application](sample-application.md) demonstrates all the basics you need to know;
* Explore [Key Value Operations](../howtos/kv-operations.md) (CRUD) against a document database;
* Or [Query](../howtos/n1ql-queries-with-sdk.md) with our SQL-based SQL++ query language;
* Or read up on [which service fits your use case](../concept-docs/data-services.md).

### [](#additional-resources)Additional Resources

The API reference is generated for each release and the latest can be found [here](http://docs.couchbase.com/sdk-api/couchbase-python-client/).

Older API references are linked from their respective sections in the [Individual Release Notes](../project-docs/sdk-release-notes.md). Most of the API documentation can also be accessed via `pydoc`.

[Migration page](../project-docs/migrating-sdk-code-to-3.n.md) highlights the main differences to be aware of when migrating your code.

Couchbase welcomes community contributions to the Python SDK. The Python SDK source code is available on [GitHub](https://github.com/couchbase/couchbase-python-client).

### [](#troubleshooting)Troubleshooting

* Couchbase Server is designed to work in the same WAN or availability zone as the client application. If you're running the SDK on your laptop against a Capella cluster, see further information on:

  * Notes on [Constrained Network Environments](../ref/client-settings.md#constrained-network-environments).
  * [Network Requirements](../project-docs/compatibility.md#network-requirements).
  * If you have a consumer-grade router which has problems with DNS-SRV records review our [Troubleshooting Guide](../howtos/troubleshooting-cloud-connections.md#troubleshooting-host-not-found).
* Our [community forum](https://forums.couchbase.com/c/python-sdk/10) is a great source of help.