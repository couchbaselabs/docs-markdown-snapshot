[View original HTML](/python-sdk/4.4/project-docs/migrating-sdk-code-to-3.n.html)

> The SDK API 3 (used in Python SDK 3.x and 4.x) introduces breaking changes to the previous SDK API 2 APIs (used in Python SDK 2.x) in order to provide a number of improvements. Collections and Scopes are introduced. The Document class and structure has been completely removed from the API, and the returned value is now `Result`. Retry behaviour is more proactive, and lazy bootstrapping moves all error handling to a single place. Individual behaviour changes across services are explained here. 

The current Python SDK 4.0 is also based on the [SDK API 3.3 specification](compatibility.md#sdk3.3), and offers an entirely new backend (Couchbase++) with better support for new features like Distributed ACID Transactions. We have increased the major version to reflect the importance of this implementation change as per [semantic versioning](https://semver.org/).

Couchbase Python SDK 4.0, like the 3.2, 3.1, and 3.0 versions, conforms to the Couchbase 3.x SDK API. Couchbase Python SDK 4.0 is built upon Couchbase++, whereas 3.x releases were built upon LCB (libcouchbase)

|  | For the most part, migration from SDK API 2._x_ versions remains the same. The few 4.0-specific changes can be found at the end of this document. If you are an existing Python SDK 3._x_ user considering migrating to SDK 4.0, you may wish to skip to the [SDK 4.0 specifics](#sdk4-specifics) below. |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

This release of the SDK is written to version 3.7 of the SDK API specification (and matching the features available in Couchbase 7.6.6 and earlier). For most developers, just using the latest version will be all that matters, and few will need to look at another of our SDKs. Just for those few that do, the table below shows each Couchbase SDK release version that matches the API version (and a table that covers the earliest versions of the 3.x SDK API can be found in documentation for earlier versions of the SDK).

Whilst these two numbers match for the .NET SDK, this is not the case for the others, as version numbers for individual SDKs are bumped up in line with [Semantic Versioning](https://semver.org/) — check the [release notes](#sdk-release-notes) of each SDK for individual details.

__Table 1\. SDK API Versions__
|                                                                    | API 3.3       | API 3.4   | API 3.5 | API 3.6 | API 3.7 |
| ------------------------------------------------------------------ | ------------- | --------- | ------- | ------- | ------- |
| [.NET](../../../dotnet-sdk/current/hello-world/overview.md)        | 3.3           | 3.4       | 3.5     | 3.6     | 3.7     |
| [C (libcouchbase)](../../../c-sdk/current/hello-world/overview.md) | 3.3.0 - 3.3.2 | 3.3.3 ①   | N/A ②   | N/A ②   | N/A ②   |
| [C++](../../../cxx-sdk/current/hello-world/overview.md)            | \-            | \-        | \-      | 1.0     | 1.1     |
| [Go](../../../go-sdk/current/hello-world/overview.md)              | 2.5           | 2.6 & 2.7 | 2.8     | 2.9     | 2.10    |
| [Java](../../../java-sdk/current/hello-world/overview.md)          | 3.3           | 3.4 & 3.5 | 3.6     | 3.7     | 3.8     |
| [Kotlin](../../../kotlin-sdk/current/hello-world/overview.md)      | 1.0           | 1.1 & 1.2 | 1.3     | 1.4     | 1.5     |
| [Node.js](../../../nodejs-sdk/current/hello-world/overview.md)     | 4.1           | 4.2       | 4.3     | 4.4     | 4.5     |
| [PHP](../../../php-sdk/current/hello-world/overview.md)            | 4.0           | 4.1       | 4.2     | 4.2.2   | 4.3     |
| [Python](../../current/hello-world/overview.md)                    | 4.0           | 4.1       | 4.2     | 4.3     | 4.4     |
| [Ruby](../../../ruby-sdk/current/hello-world/overview.md)          | 3.3           | 3.4       | 3.5     | 3.5.2   | 3.6     |
| [Scala](../../../scala-sdk/current/hello-world/overview.md)        | 1.3           | 1.4 & 1.5 | 1.6     | 1.7     | 1.8     |

| **1** | Excludes DNS SRV refresh support in Serverless Environments.                                                                             |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | For most purposes better productivity and functionality can be found in our [C++ SDK](../../../cxx-sdk/current/hello-world/overview.md). |

**SDK API 3.7**: Introduced support for KV reads from preferred server groups. The .NET SDK has been updated to support the latest Transactions specification — and the library is now incorporated within the .NET SDK. A new `getMulti()` interface batch reads with read committed isolation. Additionally, the Java SDK now includes a Quarkus extension with GraalVM support.

**SDK API 3.6**: Introduced support for base 64 encoded vector types alongside Server 7.6.2 (and Capella). General Availability of our C++ SDK — now available as a supported, stand-alone SDK, this SDK is also the core of our Node.js, PHP, Python, and Ruby SDKs.

**SDK API 3.5**: Introduced support for Vector Search alongside Server 7.6 (and Capella). Adds scoped indexes to Search (for Vector Seach and traditional FTS). Read from Replica for Query and Sub-Doc operations. KV Range Scan for querying documents through the Data Service, even if you don’t know the document IDs (for use cases that require relatively low concurrency and tolerate relatively high latency). Transactions now implemented as a native library in all SDKs (except libcouchbase).

**SDK API 3.4**: Introduced support for ARM v8 on Ubuntu 20.04, Transactions on Spring Data Couchbase, and compatibility with running in serverless environments, such as AWS λ. The `couchbase2://` connection string was introduced in Go 2.7, Java 3.5, Kotlin 1.2, and Scala 1.5, for Cloud Native Gateway with [Couchbase Autonomous Operator](../../../operator/current/overview.md) (from CAO 2.6.1).

**SDK API 3.3**: Introduced alongside Couchbase Server 7.1, adds Management API for Eventing and Index Management for Scopes & Collections; extends Bucket Management API to support Custom Conflict Resolution and Storage Options; adds new platform support for Linux Alpine OS, Apple M1, and AWS Graviton2; provides improved error messages for better error handling; and an upgraded Spark Connector that runs on Spark 3.0 & 3.1 Platform.

**SDK API 3.2**: Introduced alongside Couchbase Server 7.0, provides features in support of Scopes and Collections, extends capabilities around Open Telemetry API to instrument telemetry data, enhanced client side field level encryption to add an additional layer of security to protect sensitive data, adds new platform support such as Ubuntu 20.04 LTS.

**SDK API 3.1**: Introduced alongside Couchbase Server 6.6, focuses on Bucket Management API, adds capabilities around Full Text Search features such-as Geo-Polygon support, Flex Index, and Scoring.

**SDK API 3.0**: Introduced alongside Couchbase Server 6.5, is a major overhaul from its predecessor, has simplified surface area, removed long-standing bugs and deprecated/removed old API, introduces new programming languages Scala and Ruby, written in anticipation to support Scopes and Collections.

## [](#fundamentals)Fundamentals

Before this guide dives into the language-specific technical component of the migration, it is important to understand the high level changes first. As a migration guide, this document assumes you are familiar with the previous generation of the SDK and does not re-introduce SDK API 2 concepts. We recommend familiarizing yourself with the new SDK first by reading at least the [getting started guide](../hello-world/start-using-sdk.md), and browsing through the other chapters a little.

### [](#terminology)Terminology

The concept of a `Cluster` and a `Bucket` remain the same, but a fundamental new layer is introduced into the API: `Collections` and their `Scopes`. Collections are logical data containers inside a Couchbase bucket that let you group similar data just like a _Table_ does in a relational database — although documents inside a collection do not need to have the same structure. Scopes allow the grouping of collections into a namespace, which is very usfeul when you have multilpe tenants acessing the same bucket. Couchbase Server includes support for collections as a [developer preview](#6.5@server:developer-preview:preview-mode.adoc) in version 6.5, and as a first class concept of the programming model from [version 7.0.](#7.1@server:learn:data/scopes-and-collections.adoc)

Note that the SDKs include the feature from SDK 3.0, to allow easier migration.

In the previous SDK generation, particularly with the `KeyValue` API, the focus has been on the codified concept of a `Document`. Documents were read and written and had a certain structure, including the `id`/`key`, content, expiry (`ttl`), and so forth. While the server still operates on the logical concept of documents, we found that this model in practice didn’t work so well for client code in certain edge cases. As a result we have removed the `Document` class/structure completely from the API. The new API follows a clear scheme: each command takes required arguments explicitly, and an option block for all optional values. The returned value is always of type `Result`. This avoids method overloading bloat in certain languages, and has the added benefit of making it easy to grasp APIs evenly across services.

As an example here is a KeyValue document fetch:

```python
from datetime import timedelta
from couchbase.cluster import Cluster
from couchbase.collection import GetOptions
cluster=Cluster("couchbases://10.192.1.104")
collection=cluster.default_collection()
get_result = collection.get("key", GetOptions(timeout=timedelta(seconds=3)))
```

Compare this to a SQL++ (formerly N1QL) query:

```python
query_result = cluster.query("select 1=1", QueryOptions(timeout=timedelta(seconds=3)))
```

Since documents also fundamentally handled the serialization aspects of content, two new concepts are introduced: the `Serializer` and the `Transcoder`. Out of the box the SDKs ship with a JSON serializer which handles the encoding and decoding of JSON. You’ll find the serializer exposes the options for methods like SQL++ queries and KeyValue subdocument operations,.

The KV API extends the concept of the serializer to the `Transcoder`. Since you can also store non-JSON data inside a document, the `Transcoder` allows the writing of binary data as well. It handles the object/entity encoding and decoding, and if it happens to deal with JSON makes uses of the configured `Serializer` internally. See the _Serialization and Transcoding_ section below for details.

### [](#what-to-look-out-for)What to look out for

The SDKs are more proactive in retrying with certain errors and in certain situations, within the timeout budget given by the user — as an example, temporary failures or locked documents are now being retried by default — making it even easier to program against certain error cases. This behavior is customizable in a `RetryStrategy`, which can be overridden on a per operation basis for maximum flexibility if you need it.

Note, most of the bootstrap sequence is now lazy (happening behind the scenes). For example, opening a bucket is not raising an error anymore, but it will only show up once you perform an actual operation. The reason behind this is to spare the application developer the work of having to do error handling in more places than needed. A bucket can go down 2ms after you opened it, so you have to handle request failures anyway. By delaying the error into the operation result itself, there is only one place to do the error handling. There will still be situations why you want to check if the resource you are accessing is available before continuing the bootstrap; for this, we have the diagnostics and ping commands at each level which allow you to perform those checks eagerly.

## [](#language-specifics)Language Specifics

Now that you are familiar with the general theme of the migration, the next sections dive deep into the specifics. First, installation and configuration are covered, then we talk about exception handling, and then each service (i.e. Key/Value, Query,…​) is covered separately.

### [](#installation-and-configuration)Installation and Configuration

The primary source of artifacts is [the installation page](#installation.adoc), where we publish links to pre-built binaries, as well as to source tarballs. Builds can be found on PyPi. Please see the [Release Notes](sdk-release-notes.md) for up-to-date information.

|  | Python SDK 3.x and 4.x have a minimum required Python version of 3.5, although we recommend running the latest fully supported version (i.e. at the time of writing Python 3.10) with the highest patch version available. |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Note that the transitive dependency list has changed. As a refresher, Python SDK API 2 depended on the following packages:

* **typing**

SDK API 3 depends on the following ones instead:

* **typing** (on Python<3.7)
* **typing-extensions** (on Python<3.8)
* **boltons**
* **pyrsistent**

Additionally these are supported optionally in SDK API 2 and SDK API 3.

* **Twisted**
* **gevent**

|  | If you are pulling in the SDK through a package manager (recommended), all mandatory dependencies will be resolved for you automatically. |
|  | ----------------------------------------------------------------------------------------------------------------------------------------- |

### [](#configuring-collections)Configuring Collections

The fundamental semantics of the `Bucket` from SDK API 2 are analogous to that of the `Collection` in SDK API 3.

```python
# SDK API 2 custom KV timeout
bucket = Bucket("couchbases://127.0.0.1/default")
bucket.timeout=5
```

```python
# SDK 3 equivalent
cluster=Cluster("couchbases://10.192.1.104")
collection=cluster.bucket("default").default_collection()
collection.timeout=5
```

The default settings can still be customized through either the connection string or [system properties](../ref/client-settings.md). The SDK has elaborate reflection logic in place to parse "flat" string values and apply them to the builder, which means that you can now configure more properties than in SDK API 2\. Note that the property paths have changed.

```python
# Will set the compression type to inout
Cluster.connect(
    "couchbases://127.0.0.1?compression=inout",ClusterOptions(PasswordAuthenticator(
    "user",
    "pass")))

# This is equivalent to
collection.compression = COMPRESS_INOUT
```

See the [configuration section](../ref/client-settings.md) for full specifics.

At the end of this guide you’ll find a [reference](#configurations-options-reference) that describes the SDK API 2 environment options and their SDK 3 equivalents where applicable.

### [](#authentication)Authentication

Since SDK API 2 supports Couchbase Server clusters older than 5.0, it had to support both Role-Based Access Control (RBAC) as well as bucket-level passwords. The minimum cluster version supported by SDK API 3 is Server 5.0, which means that only RBAC is supported. This is why you can set the username and password when directly connecting:

```python
# add convenience overload when available
Cluster.connect("couchbases://127.0.0.1", ClusterOptions(PasswordAuthenticator("username", "password")))
```

This is just a shorthand for:

```python
Cluster.connect(
    "couchbases://127.0.0.1",
    ClusterOptions(PasswordAuthenticator("username", "password")))
```

The reason why you can pass in a specific authenticator is that you can also use the same approach to configure certificate-based authentication:

```python
cert_dir=os.path.join(os.path.curdir,"cert_dir")

Cluster.connect("couchbases://127.0.0.1", ClusterOptions(
    CertAuthenticator(cert_path="cert.pem",
                      key_path="key.crt",
                      trust_store_path="trust_store.pem"
)))
```

## [](#connection-lifecycle)Connection Lifecycle

From a high-level perspective, bootstrapping and shutdown is very similar to SDK API 2.

`Collections` will be generally available with an upcoming Couchbase Server release, but the SDK already encodes it in its API to be future-proof. If you are using a Couchbase Server version which does not support `Collections`, always use the `default_collection()` method to access the KV API; it will map to the full bucket.

Also note, you will now find Query, Search, and Analytics at the `Cluster` level. This is where they logically belong. If you are using Couchbase Server 6.5 or later, you will be able to perform cluster-level queries even if no bucket is open. If you are using an earlier version of the cluster you must open at least one bucket, otherwise cluster-level queries will fail.

## [](#exception-handling)Exception Handling

How to _handle_ exceptions is unchanged from SDK API 2\. You should still use `try/catch` on the blocking APIs and the corresponding async methods on the other APIs. There have been changes made in the following areas:

* Exception hierarchy and naming.
* Proactive retry where possible.

### [](#exception-hierarchy)Exception Hierarchy

The exception hierarchy is now unified under a `CouchbaseException`.

## [](#key-value)Key Value

The Key/Value (KV) API is now located under the `Collection` interface, so even if you do not use collections, the `default_collection()` call needs to be opened in order to access it.

The following table describes the mappings from SDK API 2 KV to those of SDK API 3:

__Table 2\. KV Changes__
| SDK API 2                 | SDK API 3                                                       |
| ------------------------- | --------------------------------------------------------------- |
| Bucket.upsert             | Collection.upsert                                               |
| Bucket.get                | Collection.get                                                  |
| Bucket.exists             | Collection.exists                                               |
| Bucket.get\_from\_replica | Collection.get\_any\_replica and collection\_get\_all\_replicas |
| Bucket.get\_and\_lock     | Collection.get\_and\_lock                                       |
| Bucket.get\_and\_touch    | Collection.get\_and\_touch                                      |
| Bucket.insert             | Collection.insert                                               |
| Bucket.upsert             | Collection.upsert                                               |
| Bucket.replace            | Collection.replace                                              |
| Bucket.remove             | Collection.remove                                               |
| Bucket.unlock             | Collection.unlock                                               |
| Bucket.touch              | Collection.touch                                                |
| Bucket.lookup\_in         | Collection.lookup\_in                                           |
| Bucket.mutate\_in         | Collection.mutate\_in//// ////                                  |

In addition, the datastructure APIs have been renamed and moved:

__Table 3\. Datastructure API Changes__
| SDK API 2            | SDK API 3                |
| -------------------- | ------------------------ |
| Bucket.map\_add      | Collection.map\_add      |
| Bucket.map\_get      | Collection.map\_get      |
| Bucket.map\_remove   | Collection.map\_remove   |
| Bucket.map\_size     | Collection.map\_size     |
| Bucket.list\_get     | Collection.list\_get     |
| Bucket.list\_append  | Collection.list\_append  |
| Bucket.list\_remove  | Collection.list\_remove  |
| Bucket.list\_prepend | Collection.list\_prepend |
| Bucket.list\_set     | Collection.list\_set     |
| Bucket.list\_size    | Collection.list\_size    |
| Bucket.set\_add      | Collection.set\_add      |
| Bucket.set\_contains | Collection.set\_contains |
| Bucket.set\_remove   | Collection.set\_remove   |
| Bucket.set\_size     | Collection.set\_size     |
| Bucket.queue\_push   | Collection.queue\_push   |
| Bucket.queue\_pop    | Collection.queue\_pop    |

There are two important API changes:

* On the request side, overloads have been reduced and moved under a `Options` block
* On the response side, the return types have been unified.

The signatures now look very similar.

In SDK API 3, the `get` method returns a `GetResult`, and the `upsert` returns `MutationResult`.

Each of those results only contains the fields that the specific method can actually return, making it impossible to accidentally try to access the `expiry` on the `Result` after a mutation, for example.

Optional parameters are now accessible via `couchbase.options.OptionBlock` derivatives, or via named parameters (with the latter overriding the former).

All required params are still part of the method signature, making it clear what is required and what is not (or has default values applied if not overridden).

The timeout can be overridden on every operation and now takes a `datetime.timedelta` object from the Python standard library.

```python
# SDK 3 custom timeout
get_result = collection.get(
    "mydoc-id",
    GetOptions(timeout=timedelta(seconds=5)))
self.assertEquals("fish",get_result.content_as[str])
```

In SDK API 2, the `get_from_replica` method had a `ReplicaMode` argument which allowed to customize its behavior on how many replicas should be reached. We have identified this as a potential source of confusion and as a result split it up in two methods that simplify usage significantly. There is now a `get_all_replicas` method and a `get_any_replica` method.

* `get_all_replicas` asks the active node and all available replicas and returns the results as a stream.
* `get_any_replica` uses `get_all_replicas`, and returns the first result obtained.

Unless you want to build some kind of consensus bet(ween the different replica responses, we recommend `get_any_replica` for a fallback to a regular `get` when the active node times out.

### [](#query)Query

SQL++ querying is now available at the `Cluster` level instead of the bucket level, because you can also write SQL++ queries that span multiple buckets. Compare a simple SQL++ query from SDK 2 with its SDK 3 equivalent:

```python
# SDK 2 simple query
query_result = bucket.query("select * from `travel-sample` limit 10")
for row in query_result:
    value = row.value
```

```python
# SDK 3 simple query
query_result = cluster.query("select * from `travel-sample` limit 10")
for value in query_result:
    #...
    pass
```

The following shows how to do named and positional parameters in SDK API 2, and their SDK API 3 counterparts:

```python
# SDK 2 named parameters
bucket.query(
    "select * from bucket where type = $type",
    type="airport")

# SDK 2 positional parameters
bucket.query(
    "select * from bucket where type = $1",
    "airport")
```

```python
# SDK 3 named parameters
from couchbase.cluster import QueryOptions
cluster.query(
    "select * from bucket where type = $type",
    QueryOptions(named_parameters={"type": "airport"}))

# SDK 3 positional parameters
cluster.query(
    "select * from bucket where type = $1",
    QueryOptions(positional_parameters=["airport"]))
```

#### [](#analytics)Analytics

Analytics querying, like SQL++, is also moved to the `Cluster` level: it is now accessible through the `Cluster.analytics_query` method. As with the Query service, parameters for the Analytics queries have moved into the `AnalyticsOptions`:

```python
# SDK 3 simple analytics query
analytics_result = cluster.analytics_query("select * from dataset")
for value in analytics_result:
    #...
    pass
```

```python
from couchbase.cluster import AnalyticsOptions
# SDK 3 named parameters for analytics
cluster.analytics_query(
        "select * from dataset where type = $type",
        AnalyticsOptions(named_parameters={"type": 'airport'}))

# SDK 3 positional parameters for analytics
cluster.analytics_query(
    "select * from dataset where type = $1",
    AnalyticsOptions(positional_parameters=["airport"]))
```

## [](#management-apis)Management APIs

In SDK API 2, the management APIs were centralized in the `Admin` class at the cluster level and the `BucketManager` class at the bucket level. Since SDK API 3 provides more management APIs, they have been split up in their respective domains. So for example when in SDK API 2 you needed to remove a bucket you would call `Admin.bucket_remove` you will now find it under `BucketManager.drop_bucket`. Also, creating a SQL++ index now lives in the `QueryIndexManager`, which is accessible through the `Cluster`.

The following table provides a mapping from the SDK API 2 management APIs to those of SDK API 3:

__Table 4\. ClusterManager changes__
| SDK API 2            | SDK API 3                       |
| -------------------- | ------------------------------- |
| Admin.bucket\_create | BucketManager.create\_bucket    |
| Admin.bucket\_remove | BucketManager.drop\_bucket      |
| Admin.bucket\_update | BucketManager.update\_bucket    |
| Admin.buckets\_list  | BucketManager.get\_all\_buckets |
| Admin.bucket\_info   | BucketManager.get\_bucket       |
| Admin.user\_get      | UserManager.get\_user           |
| Admin.user\_remove   | UserManager.drop\_user          |
| Admin.user\_upsert   | UserManager.upsert\_user        |
| Admin.users\_get     | UserManager.get\_all\_users     |

__Table 5\. BucketManager changes__
| SDK API 2                                  | SDK API 3                                    |
| ------------------------------------------ | -------------------------------------------- |
| BucketManager.design\_create               | ViewIndexManager.upsert\_design\_document    |
| BucketManager.design\_delete               | ViewIndexManager.drop\_design\_document      |
| BucketManager.design\_get                  | ViewIndexManager.get\_design\_document       |
| BucketManager.design\_list                 | ViewIndexManager.get\_all\_design\_documents |
| BucketManager.design\_publish              | ViewIndexManager.publish\_design\_document   |
| BucketManager.n1ql\_index\_build\_deferred | QueryIndexManager.build\_deferred\_indexes   |
| BucketManager.n1ql\_index\_create          | QueryIndexManager.create\_index              |
| BucketManager.n1ql\_index\_create\_primary | QueryIndexManager.create\_primary\_index     |
| BucketManager.n1ql\_index\_drop            | QueryIndexManager.drop\_index                |
| BucketManager.n1ql\_index\_drop\_primary   | QueryIndexManager.drop\_primary\_index       |
| BucketManager.n1ql\_index\_list            | QueryIndexManager.get\_all\_indexes          |
| BucketManager.n1ql\_index\_watch           | QueryIndexManager.watch\_indexes             |

## [](#sdk4-specifics)SDK 4.x specifics

Python SDK 4.0 implements the SDK API 3 spec, so all the steps above also apply to a migration from a Python SDK 2.x directly to Python SDK 4.0.

Importantly, the Python SDK 4.0 has been substantially reworked to use a new backend (Couchbase++ instead of libcouchbase.) Though the API surfaces are intended to be compatible, any code that relies on undocumented or uncommitted internal details is not guaranteed to work. Key areas that have been reworked:

* The `couchbase_core` package has been removed. The 4.0 SDK provides appropriate import paths within the `couchbase` package (or possibly the `acouchbase`/`txcouchbase` packages if using one of the async APIs) for anything that is needed with respect to the APIs provided by the SDK.
* As there is a new backend, the previous `_libcouchbase` c-extension has been removed
* Remnants of the 2.x API in previous Python 3.x SDK versions have been removed or deprecated

  * Key items that have been **removed**:

    * The `ClassicAuthenticator` class
    * Key-value operations are no longer available with a `bucket` instance. Use a `collection` instance for key-value operations.
    * A `cluster` and `bucket` instance do not inherit from the same base class
    * The `Client` class has been removed
    * `Items` API
    * `Admin` cluster
  * Key items that have been **deprecated**:

    * Datastructure methods provided by the `collection` instance have been deprecated and replaced with their respective APIs (i.e. `CouchbaseList`, `CouchbaseMap`, `CouchbaseQueue` and `CouchbaseSet`)
    * `OperationResult` (deprecated, still available from `couchbase.result`)
    * `ValueResult` (deprecated, still available from `couchbase.result`)
* The 4.x version of the Python SDK significantly improves how the SDK handles the [Global Interpreter Lock (GIL)](https://docs.python.org/3/glossary.html#term-global-interpreter-lock). As part of the improvements, the `lockmode` cluster option has been deprecated as it is a no-op (i.e. has no functionality) and will be removed in a future version of the SDK. Also, the `unlock_gil` option is no longer available.

  * For details on how to use the 4.x SDK within the parallelism paradigms provided by the Python language see the [parallelism](https://docs.couchbase.com/sdk-api/couchbase-python-client/couchbase%5Fapi/parallelism.html) page in the API documentation.
* Import paths have been reorganized to follow consistent patterns. While the import paths that existed in 3.x SDK are mostly available (see previous points on removal of `couchbase_core` package), some paths are deprecated and will be removed in a future release.

  * All authenticators should be imported from `couchbase.auth`
  * All constants should be imported from `couchbase.constants`
  * All options should be imported from `couchbase.options`
  * All management options should be imported from `couchbase.management.options`
  * All results should be imported from `couchbase.result`
  * All exceptions should be imported from `couchbase.exceptions`
  * Enumerations and Classes related to operations should be imported from that operation’s path. For example, `QueryScanConsistency` should be imported from `couchbase.n1ql` (i.e. `from couchbase.n1ql import QueryScanConsistency`)
* Changes to the async APIs (`acouchbase` and `txcouchbase`):

  * While multi-operations (`get_multi`, `upsert_multi`, etc.) still exist for the `couchbase` API, they have been removed from the async APIs (`acouchbase` and `txcouchbase`) as each of the async APIs are built with libraries that have mechanisms to handle multi/bulk operations (`asyncio` has `asyncio.gather(…​)` and `Twisted` has `DeferredList(…​)`).
  * If using the `txcouchbase` API, the reactor that should be installed is the `asyncioreactor`. Therefore, the `txcouchbase` package _needs_ to be imported prior to importing the `reactor`. See example import below.

```python
# this is new with Python SDK 4.x, it needs to be imported prior to
# importing the twisted reactor
import txcouchbase

from twisted.internet import reactor
```

The new backend enables the capabilities required for many upcoming features. Key new features include:

* [multi-document ACID transactions](../howtos/distributed-acid-transactions-from-the-sdk.md)

In addition:

* `get` requests on locked documents now retry rather than fast-fail.
* The changes to [Connection Strings](../howtos/managing-connections.md#connection-strings) can be found documented in the [API reference](https://docs.couchbase.com/sdk-api/couchbase-python-client/couchbase%5Fapi/options.html#cluster).
* The [Logging](../howtos/collecting-information-and-logging.md) changes are not fully documented.

## [](#comparing-older-documentation)Comparing Older Documentation

You may want to visit documentation for older versions of the SDK, to help to understand application code that you are migrating. Versions that have reached end of life can be found in the [archive](https://docs-archive.couchbase.com/home/index.html). In the release notes pages of these older docs, you will also find links to the API reference for each no-longer-supported release.