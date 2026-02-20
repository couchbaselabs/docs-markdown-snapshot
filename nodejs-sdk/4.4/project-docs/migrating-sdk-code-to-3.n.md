---
title: Migrating to SDK API 3
description: The SDK API 3 (used in Node.js SDK 3.x and 4.x) introduces breaking
  changes to the previous SDK API 2 APIs (used in Node.js SDK 2.x) in order to
  provide a number of improvements. Collections and Scopes are introduced.
editUrl: https://github.com/couchbase/docs-sdk-nodejs/edit/temp/4.4/modules/project-docs/pages/migrating-sdk-code-to-3.n.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:4.4@nodejs-sdk:project-docs:migrating-sdk-code-to-3.n.adoc[]
---

[View original HTML](/nodejs-sdk/4.4/project-docs/migrating-sdk-code-to-3.n.html)

# Migrating to SDK API 3

> The SDK API 3 (used in Node.js SDK 3.x and 4.x) introduces breaking changes to the previous SDK API 2 APIs (used in Node.js SDK 2.x) in order to provide a number of improvements. Collections and Scopes are introduced. The Document class and structure has been completely removed from the API, and the returned value is now `Result`. Retry behavior is more proactive, and lazy bootstrapping moves all error handling to a single place. 

The current Node.js SDK 4.0 is also based on the [SDK API 3.2 specification](compatibility.md#sdk3.2), and offers an entirely new backend (couchbase++) with better support for upcoming features like Distributed ACID Transactions. We have increased the major version to reflect the importance of this implementation change as per [semantic versioning](https://semver.org/).

The intent of this migration guide is to provide detail information on the changes and what to look for while upgrading the SDK.

> [!NOTE]
> if you are an existing Node.js SDK 3._x_ user considering migrating to SDK 4.0, you may wish to skip to the [SDK 4.0 specifics](#sdk4-specifics) below.

This release of the SDK is written to version 3.6 of the SDK API specification (and matching the features available in Couchbase 7.6.2 and earlier). For most developers, just using the latest version will be all that matters, and few will need to look at another of our SDKs. Just for those few that do, the table below shows each Couchbase SDK release version that matches the API version (and a table that covers the earliest versions of the 3.x SDK API can be found in documentation for earlier versions of the SDK).

Whilst these two numbers match for the .NET SDK, this is not the case for the others, as version numbers for individual SDKs are bumped up in line with [Semantic Versioning](https://semver.org/) — check the [release notes](#sdk-release-notes) of each SDK for individual details.

__Table 1\. SDK API Versions__
|                                                                    | API 3.2   | API 3.3       | API 3.4   | API 3.5 | API 3.6 |
| ------------------------------------------------------------------ | --------- | ------------- | --------- | ------- | ------- |
| [.NET](../../../dotnet-sdk/current/hello-world/overview.md)        | 3.2       | 3.3           | 3.4       | 3.5     | 3.6     |
| [C (libcouchbase)](../../../c-sdk/current/hello-world/overview.md) | 3.2       | 3.3.0 - 3.3.2 | 3.3.3 ①   | N/A ②   | N/A ②   |
| [C++](../../../cxx-sdk/current/hello-world/overview.md)            | \-        | \-            | \-        | \-      | 1.0     |
| [Go](../../../go-sdk/current/hello-world/overview.md)              | 2.3 & 2.4 | 2.5           | 2.6 & 2.7 | 2.8     | 2.9     |
| [Java](../../../java-sdk/current/hello-world/overview.md)          | 3.2       | 3.3           | 3.4 & 3.5 | 3.6     | 3.7     |
| [Kotlin](../../../kotlin-sdk/current/hello-world/overview.md)      | \-        | 1.0           | 1.1 & 1.2 | 1.3     | 1.4     |
| [Node.js](../../current/hello-world/overview.md)                   | 3.2 & 4.0 | 4.1           | 4.2       | 4.3     | 4.4     |
| [PHP](../../../php-sdk/current/hello-world/overview.md)            | 3.2       | 4.0           | 4.1       | 4.2     | 4.2.2   |
| [Python](../../../python-sdk/current/hello-world/overview.md)      | 3.2       | 4.0           | 4.1       | 4.2     | 4.3     |
| [Ruby](../../../ruby-sdk/current/hello-world/overview.md)          | 3.2       | 3.3           | 3.4       | 3.5     | 3.5.2   |
| [Scala](../../../scala-sdk/current/hello-world/overview.md)        | 1.2       | 1.3           | 1.4 & 1.5 | 1.6     | 1.7     |

| **1** | Excludes DNS SRV refresh support in Serverless Environments.                                                                             |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | For most purposes better productivity and functionality can be found in our [C++ SDK](../../../cxx-sdk/current/hello-world/overview.md). |

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

```javascript
const result = await collection.get(key);
document = result.value;
```

Compare this to a SQL++ (formerly N1QL) query:

```javascript
async function queryNamed() {
  const query = `
    SELECT airportname, city FROM \`travel-sample\` 
    WHERE type=$TYPE 
      AND city=$CITY;
  `
  const options = { parameters: { TYPE: 'airport', CITY: 'Reno' } }

  try {
    let result = await cluster.query(query, options)
    console.log("Result:", result)
    return result
  } catch (error) {
    console.error('Query failed: ', error)
  }
}
```

Since documents also fundamentally handled the serialization aspects of content, two new concepts are introduced: the `Serializer` and the `Transcoder`. Out of the box the SDKs ship with a JSON serializer which handles the encoding and decoding of JSON. You’ll find the serializer exposes the options for methods like SQL++ queries and KeyValue subdocument operations,.

The KV API extends the concept of the serializer to the `Transcoder`. Since you can also store non-JSON data inside a document, the `Transcoder` allows the writing of binary data as well. It handles the object/entity encoding and decoding, and if it happens to deal with JSON makes uses of the configured `Serializer` internally. See the _Serialization and Transcoding_ section below for details.

### [](#what-to-look-out-for)What to look out for

The SDKs are more proactive in retrying with certain errors and in certain situations, within the timeout budget given by the user — as an example, temporary failures or locked documents are now being retried by default — making it even easier to program against certain error cases. This behavior is customizable in a `RetryStrategy`, which can be overridden on a per operation basis for maximum flexibility if you need it.

Note, most of the bootstrap sequence is now lazy (happening behind the scenes). For example, opening a bucket is not raising an error anymore, but it will only show up once you perform an actual operation. The reason behind this is to spare the application developer the work of having to do error handling in more places than needed. A bucket can go down 2ms after you opened it, so you have to handle request failures anyway. By delaying the error into the operation result itself, there is only one place to do the error handling. There will still be situations why you want to check if the resource you are accessing is available before continuing the bootstrap; for this, we have the diagnostics and ping commands at each level which allow you to perform those checks eagerly.

## [](#language-specifics)Language Specifics

Now that you are familiar with the general theme of the migration, the next sections dive deep into the specifics. First, installation and configuration are covered, then we talk about exception handling, and then each service (i.e. Key/Value, Query,…​) is covered separately.

## [](#installation-and-configuration)Installation and Configuration

The Node.js SDK 3._x_ and 4._x_ are available through `npm`, just like the previous generation. Please see the [Release Notes](sdk-release-notes.md) for up-to-date information.

The Node.js SDK 3.2 has the following dependencies:

```json
  "dependencies": {
    "bindings": "^1.5.0",
    "debug": "^4.3.2",
    "nan": "^2.15.0",
    "parse-duration": "^1.0.0",
    "prebuild-install": "^6.1.4"
  },
```

The Node.js SDK 4.0 additionally requires Node 12+ (the oldest supported maintenance LTS release).

### [](#connection-to-the-cluster)Connection to the Cluster

```javascript
const options = { username:"Administrator", password:"password"};
cluster = await couchbase.connect( "http://127.0.0.1", options);
bucket = cluster.bucket("travel-sample");
collection = bucket.scope("inventory").collection("airport");
```

Similar to SDK API 2, if you create your own `ClusterEnvironment` the SDK will not shut it down for you — you need to do this manually at the end of the program lifetime:

```javascript
cluster.close();
```

Connection String Url Query Parameters

```javascript
const options = { username:"Administrator", password:"password"};
cluster = await couchbase.connect( "http://127.0.0.1/?query_timeout=2000", options);
```

### [](#authentication)Authentication

Connecting with certificate-based authentication.

```javascript
// see sdk-examples/etc for creation of certificates
const here = process.cwd();
const truststorepath = here + "/" + '../etc/x509-cert/SSLCA/clientdir/trust.pem';
const certpath = here + "/" + '../etc/x509-cert/SSLCA/clientdir/client.pem';
const keypath = here + "/" + '../etc/x509-cert/SSLCA/clientdir'; // gets /client.key from cluster.bucket()

// Setup Cluster Connection Object
const options = {username: 'testuser', password: 'password'};
var cluster = new couchbase.Cluster(
    'couchbases://127.0.0.1/travel-sample' +
    '?truststorepath=' + truststorepath +
    '&certpath=' + certpath +
    '&keypath=' + keypath, options);
```

Please see the [documentation on certificate-based authentication](../howtos/sdk-authentication.md) for detailed information on how to configure this properly.

## [](#connection-lifecycle)Connection Lifecycle

From a high-level perspective, bootstrapping and shutdown is very similar to the SDK API 2._x_. One notable difference is that the `Collection` is introduced and that the individual methods like `bucket` immediately return, and do not throw an exception. Compare SDK API 2: the `openBucket` method would not work if it could not open the bucket.

The reason behind this change is that even if a bucket can be opened, a millisecond later it may not be available any more. All this state has been moved into the actual operation so there is only a single place where the error handling needs to take place. This simplifies error handling and retry logic for an application.

In SDK API 2, you connected, opened a bucket, performed a KV op, and disconnected like this:

```javascript
const cluster = new couchbase.Cluster("127.0.0.1");
cluster.authenticate("user", "pass");
const bucket = cluster.openBucket("travel-sample");

const getResult = bucket.get("airline_10");

cluster.close();
```

Here is the SDK API 3 equivalent:

```javascript
const options = { username:"Administrator", password:"password"};
cluster = await couchbase.connect( "http://127.0.0.1", options);
bucket = cluster.bucket("travel-sample");
collection = bucket.scope("inventory").collection("airport");

const getResult = await collection.get("airport_1254");

cluster.close();
```

`Collections` is generally available from Couchbase Server 7.0 release, but the SDK already encoded it in its API to be future-proof. If you are using a Couchbase Server version which does not support `Collections`, always use the `defaultCollection()` method to access the KV API; it will map to the full bucket.

> [!IMPORTANT]
> You’ll notice that `bucket(String)` returns immediately, even if the bucket resources are not completely opened. This means that the subsequent `get` operation may be dispatched even before the socket is open in the background. The SDK will handle this case transparently, and reschedule the operation until the bucket is opened properly. This also means that if a bucket could not be opened (say, because no server was reachable) the operation will time out. Please check the logs to see the cause of the timeout (in this case, you’ll see socket connect rejections).

Also note, you will now find Query, Search, and Analytics at the `Cluster` level. This is where they logically belong. If you are using Couchbase Server 6.5 or later, you will be able to perform cluster-level queries even if no bucket is open. If you are using an earlier version of the cluster you must open at least one bucket, otherwise cluster-level queries will fail.

## [](#serialization-and-transcoding)Serialization and Transcoding

In SDK API 2 the main method to control transcoding was through providing different `Document` instances (which in turn had their own transcoder associated), such as the `JsonDocument`. This only worked for the KV APIs though — Query, Search, Views, and other services exposed their JSON rows/hits in different ways. All of this has been unified in SDK API 3 under a single concept: serializers and transcoders.

By default, all KV APIs transcode to and from JSON — you can also provide Javascript objects which you couldn’t in the past.

```javascript
const  upsertResult = await collection.upsert("mydoc-id", { myvalue: "me"});
const getResult = await collection.get("mydoc-id");
console.log(getResult);
```

If you want to write binary data, you can use a `new RawBinaryTranscoder()`:

```javascript
const content = Buffer.from("some data to become binary");
const  upsertResult = await collection.upsert(
  "mydoc-id",
  content,
  {transcoder:new RawBinaryTranscoder()}
);
const getResult = await collection.get("mydoc-id");
console.log(getResult);
```

## [](#exception-handling)Exception Handling

How to _handle_ exceptions is unchanged from SDK API 2\. You should still use `try/catch` on the blocking APIs and the corresponding reactive/async methods on the other APIs. There have been changes made in the following areas:

* Exception hierarchy and naming.
* Proactive retry where possible.

### [](#exception-hierarchy)Exception hierarchy

The exception hierarchy is now flat and unified under a `CouchbaseError`. Each `CouchbaseError` has an associated `ErrorContext` which is populated with as much info as possible and then dumped alongside the stack trace if an error happens.

Here is an example of the error context if a SQL++ query is performed with an invalid syntax (i.e. `select 1= from`):

```none
Exception in thread "main" com.couchbase.client.core.error.ParsingFailedException: Parsing of the input failed {"completed":true,"coreId":1,"errors":[{"code":3000,"message":"syntax error - at from"}],"idempotent":false,"lastDispatchedFrom":"127.0.0.1:62253","lastDispatchedTo":"127.0.0.1:8093","requestId":3,"requestType":"QueryRequest","retried":11,"retryReasons":["ENDPOINT_TEMPORARILY_NOT_AVAILABLE","BUCKET_OPEN_IN_PROGRESS"],"service":{"operationId":"9111b961-e585-42f2-9cab-e1501da7a40b","statement":"select 1= from","type":"query"},"timeoutMs":75000,"timings":{"dispatchMicros":15599,"totalMicros":1641134}}
```

### [](#proactive-retry)Proactive Retry

One reason why the APIs do not expose a long list of exceptions is that the SDK now retries as many operations as it can if it can do so safely. This depends on the type of operation (idempotent or not), in which state of processing it is (already dispatched or not), and what the actual response code is if it arrived already. As a result, many transient cases — such as locked documents, or temporary failure — are now retried by default and should less often impact applications. It also means, when migrating to SDK API 3, you may observe a longer period of time until an error is returned by default.

> [!NOTE]
> Operations are retried by default as described above with the default `BestEffortRetryStrategy`.

## [](#migrating-services)Migrating Services

The following section discusses each service in detail and covers specific bits that have not been covered by the more generic sections above.

### [](#key-value)Key Value

The Key/Value (KV) API is now located under the `Collection` interface, so even if you do not use collections, the `defaultCollection()` needs to be opened in order to access it.

The following table describes the SDK API 2 KV calls and where they are now located in SDK API 3:

__Table 2\. KV API Changes__
| SDK API 2             | SDK API 3                                                 |
| --------------------- | --------------------------------------------------------- |
| bucket.upsert         | collection.upsert                                         |
| bucket.get            | collection.get                                            |
| bucket.exists         | collection.exists                                         |
| bucket.getFromReplica | collection.getAnyReplica and collection.getAllReplicas    |
| bucket.getAndLock     | collection.getAndLock                                     |
| bucket.getAndTouch    | collection.getAndTouch                                    |
| bucket.insert         | collection.insert                                         |
| bucket.upsert         | collection.upsert                                         |
| bucket.replace        | collection.replace                                        |
| bucket.remove         | collection.remove                                         |
| bucket.unlock         | collection.unlock                                         |
| bucket.touch          | collection.touch                                          |
| bucket.lookupIn       | collection.lookupIn                                       |
| bucket.mutateIn       | collection.mutateIn                                       |
| bucket.counter        | binarycollection.increment and binarycollection.decrement |
| bucket.append         | binarycollection.append                                   |
| bucket.prepend        | binarycollection.prepend                                  |

In addition, the datastructure APIs have been renamed and moved:

__Table 3\. Datastructure API Changes__
| SDK API 2          | SDK API 3        |
| ------------------ | ---------------- |
| bucket.mapAdd      | collection.map   |
| bucket.mapGet      | collection.map   |
| bucket.mapRemove   | collection.map   |
| bucket.mapSize     | collection.map   |
| bucket.listGet     | collection.list  |
| bucket.listAppend  | collection.list  |
| bucket.listRemove  | collection.list  |
| bucket.listPrepend | collection.list  |
| bucket.listSet     | collection.list  |
| bucket.listSize    | collection.list  |
| bucket.setAdd      | collection.set   |
| bucket.setContains | collection.set   |
| bucket.setRemove   | collection.set   |
| bucket.setSize     | collection.set   |
| bucket.queuePush   | collection.queue |
| bucket.queuePop    | collection.queue |

There are two important API changes:

* On the request side, overloads have been reduced and moved under a `Options` block
* On the response side, the return types have been unified.

The signatures now look very similar. The concept of the `Document` as a type is gone in SDK API 3 and instead you need to pass in the properties explicitly. This makes it very clear what is returned, especially on the response side.

Thus, the `get` method does not return a `Document` but a `GetResult` instead, and the `upsert` does not return a `Document` but a `MutationResult`. Each of those results only contains the field that the specific method can actually return, making it impossible to accidentally try to access the `expiry` on the `Document` after a mutation, for example.

Instead of having many overloads, all optional params are now part of the `Option` block. All required params are still part of the method signature, making it clear what is required and what is not (or has default values applied if not overridden).

The timeout can be overridden on every operation and now takes a `Duration` from java 8\. Compare SDK API 2 and SDK API 3 custom timeout setting:

```javascript
// SDK API 2 custom timeout
bucket.get("mydoc-id", 5000);
```

```javascript
// SDK API 3 custom timeout
const getResult = await collection.get( "airport_1254", {timeout : 2000});
```

In SDK API 2, the `getFromReplica` method had a `ReplicaMode` argument which allowed to customize its behavior on how many replicas should be reached. We have identified this as a potential source of confusion and as a result split it up in two methods that simplify usage significantly. There is now a `getAllReplicas` method and a `getAnyReplica` method.

* `getAllReplicas` asks the active node and all available replicas and returns the results as a stream.
* `getAnyReplica` uses `getAllReplicas`, and returns the first result obtained.

Unless you want to build some kind of consensus between the different replica responses, we recommend `getAnyReplica` for a fallback to a regular `get` when the active node times out.

> [!NOTE]
> Operations which cannot be performed on JSON documents have been moved to the `binarycollection`, accessible through `Collection.binary()`. These operations include `append`, `prepend`, `increment`, and `decrement` (previously called `counter` in SDK API 2). These operations should only be used against non-json data. Similar functionality is available through `mutateIn` on JSON documents.

### [](#query)Query

SQL++ querying is now available at the `Cluster` level instead of the bucket level, because you can also write SQL++ queries that span multiple buckets. Compare a simple SQL++ query from SDK API 2 with its SDK API 3 equivalent:

```javascript
// SDK API 2 simple query
queryResult = await bucket.query(
      couchbase.N1qlQuery.fromString('SELECT * FROM `travel-sample` WHERE city=$1 LIMIT 10'),
      [ 'Paris' ]);

queryResult.rows.forEach((row)=>{
      console.log(row);
   });
```

```javascript
// SDK API 3 simple query
const queryResult = await cluster.query("SELECT * FROM `travel-sample` WHERE city=$1 LIMIT 10", { parameters: ['Paris']});
queryResult.rows.forEach((row)=>{
   console.log(row);
});
```

Note that there is no `N1qlQuery.fromString` any more — and query parameters argument has been moved to the options parameter for consistency reasons. The following shows how to do named and positional parameters in SDK API 3:

```javascript
// SDK API 3 named parameters
const queryResultNamed = await cluster.query("SELECT * FROM `travel-sample` WHERE city=$CITY LIMIT 10", { parameters: {CITY:'Paris'}});
queryResultNamed.rows.forEach((row)=>{
   console.log(row);
});
// SDK API 3 positional parameters
const queryResultPositional = await cluster.query("SELECT * FROM `travel-sample` WHERE city=$1 LIMIT 10", { parameters: ['Paris']});
queryResultPositional.rows.forEach((row)=>{
   console.log(row);
});
```

Much of the non-row metadata has been moved into a specific `QueryMetaData` section:

It is no longer necessary to check for a specific error in the stream: if an error happened during processing it will throw an exception at the top level of the query. The reactive streaming API will terminate the rows' `Flux` with an exception as well as soon as it is discovered. This makes error handling much easier in both the blocking and non-blocking cases.

While in SDK API 2 you had to manually check for errors (otherwise you’d get an empty row collection):

```javascript
const queryResult = bucket.query(N1qlQuery.simple("select 1="));
if (!queryResult.errors.isEmpty()) {
  // errors contain [{"msg":"syntax error - at end of input","code":3000}]
}
```

In SDK API 3 the top level `query` method will throw an exception:

```none
Parsing of the input failed {"completed":true,"coreId":1,"errors":[{"code":3000,"message":"syntax error - at end of input"}],"idempotent":false,"lastDispatchedFrom":"127.0.0.1:51703","lastDispatchedTo":"127.0.0.1:8093","requestId":5,"requestType":"QueryRequest","retried":0,"service":{"operationId":"1c623a77-196a-4890-96cd-9d4f3f596477","statement":"select 1=","type":"query"},"timeoutMs":75000,"timings":{"dispatchMicros":13798,"totalMicros":70789}}
	at com.couchbase.client.java.AsyncUtils.block(AsyncUtils.java:51)
	at com.couchbase.client.java.Cluster.query(Cluster.java:225)
```

Not only does it throw a `CouchbaseError`, it also tries to map it to a specific exception type and include extensive contextual information for a better troubleshooting experience.

### [](#analytics)Analytics

Analytics querying, like SQL++, is also moved to the `Cluster` level: it is now accessible through the `Cluster.analyticsQuery` method. As with the Query service, parameters for the Analytics queries have moved into the `AnalyticsOptions`:

```javascript
// SDK API 3 simple analytics query
const analyticsResult = await cluster.analyticsQuery("select * from `travel-dataset` LIMIT 10");
analyticsResult.rows.forEach((row)=>{
   console.log(row);
});
```

```javascript
// SDK API 3 named parameters for analytics
const analyticsResult1 = await cluster.analyticsQuery(
  "select * from `travel-sample` where city = $CITY LIMIT 10",
  { parameters : { CITY : "Paris"}}
).catch((e)=>{console.log(e); throw e;});
analyticsResult1.rows.forEach((row)=>{
   console.log(row);
});

// SDK API 3 positional parameters for analytics
const analyticsResult2 = await cluster.analyticsQuery(
  "select * from `travel-sample` where city = $1 LIMIT 10",
  { parameters : [ "airport" ] }
);
analyticsResult2.rows.forEach((row)=>{
   console.log(row);
});
```

Also, errors will now be thrown as top level exceptions and it is no longer necessary to explicitly check for errors:

```java
// SDK API 2 error check
AnalyticsQueryResult analyticsQueryResult = b1.query(AnalyticsQuery.simple("select * from foo"));
if (!analyticsQueryResult.errors().isEmpty()) {
  // errors contain [{"msg":"Cannot find dataset foo in dataverse Default nor an alias with name foo! (in line 1, at column 15)","code":24045}]
}
```

### [](#search)Search

The Search API has changed a bit in SDK API 3 so that it aligns with the other query APIs. The type of queries have stayed the same, but all optional parameters moved into `SearchOptions`. Also, similar to the other query APIs, it is now available at the `Cluster` level.

Here is a SDK API 2 Search query with some options, and its SDK API 3 equivalent:

```javascript
//  SDK API 2 search query
const searchResult = bucket.query(
  "airports"",
  { indexName : "airport_view", limit:5, fields : [ "a", "b", "c"]}
  2000,
);
searchResult.rows.forEach((row)=>{
      console.log(row);
  });
}
```

```javascript
    // SDK API 3 search query
    const ftsQuery =  couchbase.SearchQuery.match("airport");
    const searchResult = await cluster.searchQuery(
      "hotels",
      ftsQuery,
      { timeout:2000,
        limit:5,
        fields : ["a", "b", "c"] },
      (err, res) => {
if(err) console.log(err);
if(res) console.log(res);
      }
    );
    searchResult.rows.forEach((row)=>{
       console.log(row);
    });
```

If you want to be absolutely sure that you didn’t get only partial data, you can check the error map:

```javascript
const ftsQuery =  couchbase.SearchQuery.match("airport");
const searchResult = await cluster.searchQuery(
  "hotels",
  ftsQuery,
  { timeout:2000,
    limit:5}
).catch((e)=>{console.log(e); throw e;});
console.log(searchResult);
if (searchResult.meta.status.failed == 0) {
  searchResult.rows.forEach((row)=>{
     console.log(row);
  });
}
```

### [](#views)Views

Views have stayed at the `Bucket` level, because it does not have the concept of collections and is scoped at the bucket level on the server as well. The API has stayed mostly the same, the most important change is that `staleness` is unified under the `ViewConsistency` enum.

__Table 4\. View Staleness Mapping__
| SDK API 2           | SDK API 3                         |
| ------------------- | --------------------------------- |
| Stale.TRUE          | QueryScanConsistency.NotBounded   |
| Stale.FALSE         | QuerywScanConsistency.RequestPlus |
| Stale.UPDATE\_AFTER | removed                           |

Compare this SDK API 2 view query with its SDK API 3 equivalent:

```javascript
// SDK API 2 view query
const query = async bucket.query(
  "design", "view", {limit:5, skip:2},
  10000
);
query.rows.forEach((row)=>{
      console.log(row);
  });
}
```

```javascript
// SDK API 3 view query
const viewResult = await bucket.viewQuery(
  "dev_airports",
  "airport_view",
  { limit:5, skip:2, timeout:10000 }
).catch((e)=>{console.log(e); throw e;});
viewResult.rows.forEach((row)=>{
   console.log(row);
});
```

### [](#management-apis)Management APIs

In SDK API 2, the management APIs were centralized in the `clustermanager` at the cluster level and the `bucketmanager` at the bucket level. Since SDK API 3 provides more management APIs, they have been split up in their respective domains. So for example when in SDK API 2 you needed to remove a bucket you would call `clustermanager.removeBucket` you will now find it under `bucketmanager.dropBucket`. Also, creating a SQL++ index now lives in the `queryindexmanager`, which is accessible through the `cluster`.

The following table provides a mapping from the SDK API 2 management APIs to those of SDK API 3:

__Table 5\. clustermanager changes__
| SDK API 2                   | SDK API 3                   |
| --------------------------- | --------------------------- |
| clustermanager.info         | removed                     |
| clustermanager.getBuckets   | bucketmanager.getAllBuckets |
| clustermanager.getBucket    | bucketmanager.getBucket     |
| clustermanager.hasBucket    | removed                     |
| clustermanager.insertBucket | bucketmanager.createBucket  |
| clustermanager.updateBucket | bucketmanager.updateBucket  |
| clustermanager.removeBucket | bucketmanager.dropBucket    |
| clustermanager.upsertUser   | usermanager.upsertUser      |
| clustermanager.removeUser   | usermanager.dropUser        |
| clustermanager.getUsers     | usermanager.getAllUsers     |
| clustermanager.getUser      | usermanager.getUser         |
| clustermanager.apiClient    | removed                     |

__Table 6\. bucketmanager changes__
| SDK API 2                              | SDK API 3                              |
| -------------------------------------- | -------------------------------------- |
| bucketmanager.info                     | removed                                |
| bucketmanager.flush                    | bucketmanager.flushBucket              |
| bucketmanager.getDesignDocuments       | viewindexmanager.getAllDesignDocuments |
| bucketmanager.getDesignDocument        | viewindexmanager.getDesignDocument     |
| bucketmanager.insertDesignDocument     | viewindexmanager.upsertDesignDocument  |
| bucketmanager.upsertDesignDocument     | viewindexmanager.upsertDesignDocument  |
| bucketmanager.removeDesignDocument     | viewindexmanager.dropDesignDocument    |
| bucketmanager.publishDesignDocument    | viewindexmanager.publishDesignDocument |
| bucketmanager.listN1qlIndexes          | queryindexmanager.getAllIndexes        |
| bucketmanager.createN1qlIndex          | queryindexmanager.createIndex          |
| bucketmanager.createN1qlPrimaryIndex   | queryindexmanager.createPrimaryIndex   |
| bucketmanager.dropN1qlIndex            | queryindexmanager.dropIndex            |
| bucketmanager.dropN1qlPrimaryIndex     | queryindexmanager.dropPrimaryIndex     |
| bucketmanager.buildN1qlDeferredIndexes | queryindexmanager.buildDeferredIndexes |
| bucketmanager.watchN1qlIndexes         | queryindexmanager.watchIndexes         |

### [](#encryption)Encryption

Due to a change in algorithms and API, SDK API 2 cannot read fields encrypted by SDK API 3\. Learn more in the [encryption guide](../howtos/encrypting-using-sdk.md#migrating-from-2).

## [](#sdk4-specifics)SDK 4.x specifics

Node.js SDK 4.0 implements the SDK API 3 spec, so all the steps above also apply to a migration from a Node.js SDK 2.x directly to Node.js SDK 4.0.

Additionally, the Node.js SDK 4.0 offers a new backend (Couchbase++) with support for [multi-document ACID transactions](../howtos/distributed-acid-transactions-from-the-sdk.md), as well as the capabilities required for upcoming features. You should be aware of the following considerations arising from this new backend implementation.

The following features are unsupported in 4.0\. They are available in 3.2, and will be available in a later 4.x release.

* [Response Time Availability](../concept-docs/response-time-observability.md)
* Log forwarding

In addition:

* The required minimum version of Node.js is now v12 (the oldest supported maintenance LTS release).
* Ping error entries are now typed.
* `get` requests on locked documents now retry rather than fast-fail.
* The changes to [Client Settings](../ref/client-settings.md) are documented in the [API reference](https://docs.couchbase.com/sdk-api/couchbase-node-client/interfaces/ConnectOptions.html).
* The changes to [Connection Strings](../howtos/managing-connections.md#connection-strings) are documented in the [API reference](https://docs.couchbase.com/sdk-api/couchbase-node-client/functions/connect.html).

## [](#comparing-older-documentation)Comparing Older Documentation

You may want to visit documentation for older versions of the SDK, to help to understand application code that you are migrating. Versions that have reached end of life can be found in the [archive](https://docs-archive.couchbase.com/home/index.html). In the release notes pages of these older docs, you will also find links to the API reference for each no-longer-supported release.