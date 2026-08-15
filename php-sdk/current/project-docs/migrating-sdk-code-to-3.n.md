---
title: Migrating to SDK 3 API
description: The SDK API 3 (used in PHP SDK 3.x and 4.x) introduces breaking
  changes to the previous SDK API 2 APIs (used in PHP SDK 2.x) in order to
  provide a number of improvements. Collections and Scopes are introduced.
editUrl: https://github.com/couchbase/docs-sdk-php/edit/temp/4.5/modules/project-docs/pages/migrating-sdk-code-to-3.n.adoc
pubDate: 2026-08-15T04:37:50.554Z
link: xref:php-sdk:project-docs:migrating-sdk-code-to-3.n.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/php-sdk/current/project-docs/migrating-sdk-code-to-3.n.html)

# Migrating to SDK 3 API

> The SDK API 3 (used in PHP SDK 3.x and 4.x) introduces breaking changes to the previous SDK API 2 APIs (used in PHP SDK 2.x) in order to provide a number of improvements. Collections and Scopes are introduced. The Document class and structure has been completely removed from the API, and the returned value is now `Result`. Retry behaviour is more proactive, and lazy bootstrapping moves all error handling to a single place. 

The current PHP SDK 4.2 is also based on the [SDK API 3.5 specification](#api-version), and offers an entirely new backend (Couchbase++) with better support for new features like Distributed ACID Transactions. We have increased the major version to reflect the importance of this implementation change as per [semantic versioning](https://semver.org/).

The intent of this migration guide is to provide detail information on the changes and what to look for while upgrading the SDK.

> [!NOTE]
> For the most part, migration from SDK API 2._x_ versions remains the same. The few 4.0-specific changes can be found at the end of this document. If you are an existing PHP SDK 3._x_ user considering migrating to SDK 4.0, you may wish to skip to the [SDK 4.0 specifics](#sdk4-specifics) below.

This release of the SDK is written to version 3.9 of the SDK API specification (and matching the features available in Couchbase 8.0.1 and earlier). For most developers, just using the latest version will be all that matters, and few will need to look at another of our SDKs. Just for those few that do, the table below shows each Couchbase SDK release version that matches the API version (and a table that covers the earliest versions of the 3.x SDK API can be found in documentation for earlier versions of the SDK).

Whilst these two numbers match for the .NET SDK, this is not the case for the others, as version numbers for individual SDKs are bumped up in line with [Semantic Versioning](https://semver.org/) — check the [release notes](#sdk-release-notes) of each SDK for individual details.

__Table 1\. SDK API Versions__
|                                                                    | API 3.4   | API 3.5 | API 3.6 | API 3.7 | API 3.8      | API 3.9     |
| ------------------------------------------------------------------ | --------- | ------- | ------- | ------- | ------------ | ----------- |
| [.NET](../../../dotnet-sdk/current/hello-world/overview.md)        | 3.4       | 3.5     | 3.6     | 3.7     | 3.8          | 3.9         |
| [C (libcouchbase)](../../../c-sdk/current/hello-world/overview.md) | 3.3.3 ①   | N/A ②   | N/A ②   | N/A ②   | N/A ②        | N/A ②       |
| [C++](../../../cxx-sdk/current/hello-world/overview.md)            | \-        | \-      | 1.0     | 1.1     | 1.2          | 1.3 & 1.4   |
| [Go](../../../go-sdk/current/hello-world/overview.md)              | 2.6 & 2.7 | 2.8     | 2.9     | 2.10    | 2.11         | 2.12        |
| [Java](../../../java-sdk/current/hello-world/overview.md)          | 3.4 & 3.5 | 3.6     | 3.7     | 3.8     | 3.9 & 3.10   | 3.11 & 3.12 |
| [Kotlin](../../../kotlin-sdk/current/hello-world/overview.md)      | 1.1 & 1.2 | 1.3     | 1.4     | 1.5     | 3.9 & 3.10 ③ | 3.11 & 3.12 |
| [Node.js](../../../nodejs-sdk/current/hello-world/overview.md)     | 4.2       | 4.3     | 4.4     | 4.5     | 4.6          | 4.7         |
| [PHP](../hello-world/overview.md)                                  | 4.1       | 4.2     | 4.2.2   | 4.3     | 4.4          | 4.5         |
| [Python](../../../python-sdk/current/hello-world/overview.md)      | 4.1       | 4.2     | 4.3     | 4.4     | 4.5          | 4.6         |
| [Ruby](../../../ruby-sdk/current/hello-world/overview.md)          | 3.4       | 3.5     | 3.5.2   | 3.6     | 3.7          | 3.8         |
| [Rust](../../../rust-sdk/current/hello-world/overview.md)          | \-        | \-      | \-      | \-      | \-           | 1.0         |
| [Scala](../../../scala-sdk/current/hello-world/overview.md)        | 1.4 & 1.5 | 1.6     | 1.7     | 1.8     | 3.9 & 3.10 ③ | 3.11 & 3.12 |

| **1** | Excludes DNS SRV refresh support in Serverless Environments.                                                                                                                                              |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | For most purposes better productivity and functionality can be found in our [C++ SDK](../../../cxx-sdk/current/hello-world/overview.md).                                                                  |
| **3** | With the Java 3.9 release, the other JVM SDKs hosted in the Java SDK monorepo adopted common release versions. This includes a number of other artifacts, as can be seen referenced in the release notes. |

**SDK API 3.9**: Provides support for JWT based authentication, as well as mTLS Certs Refresh (without restart). Deprecates SDK support for MapReduce Views.

**SDK API 3.8**: Introduced alongside Couchbase Server 8.0, which adds support for 128 vBuckets on Magma. Server 8.0 introduced vector query using Global Secondary Indexes (GSI), the Query Service index — using either a fast Hyperscale index, or a composite index to combine scalar queries with semantic search.

**SDK API 3.7**: Introduced support for KV reads from preferred server groups. The .NET SDK has been updated to support the latest Transactions specification — and the library is now incorporated within the .NET SDK. A new `getMulti()` interface batch reads with read committed isolation. Additionally, the Java SDK now includes a Quarkus extension with GraalVM support.

**SDK API 3.6**: Introduced support for base 64 encoded vector types alongside Server 7.6.2 (and Capella). General Availability of our C++ SDK — now available as a supported, stand-alone SDK, this SDK is also the core of our Node.js, PHP, Python, and Ruby SDKs.

**SDK API 3.5**: Introduced support for Vector Search alongside Server 7.6 (and Capella). Adds scoped indexes to Search (for Vector Seach and traditional FTS). Read from Replica for Query and Sub-Doc operations. KV Range Scan for querying documents through the Data Service, even if you don't know the document IDs (for use cases that require relatively low concurrency and tolerate relatively high latency). Transactions now implemented as a native library in all SDKs (except libcouchbase).

**SDK API 3.4**: Introduced support for ARM v8 on Ubuntu 20.04, Transactions on Spring Data Couchbase, and compatibility with running in serverless environments, such as AWS λ. The `couchbase2://` connection string was introduced in Go 2.7, Java 3.5, Kotlin 1.2, and Scala 1.5, for Cloud Native Gateway with [Couchbase Autonomous Operator](../../../operator/current/overview.md) (from CAO 2.6.1).

**SDK API 3.3**: Introduced alongside Couchbase Server 7.1, adds Management API for Eventing and Index Management for Scopes & Collections; extends Bucket Management API to support Custom Conflict Resolution and Storage Options; adds new platform support for Linux Alpine OS, Apple M1, and AWS Graviton2; provides improved error messages for better error handling; and an upgraded Spark Connector that runs on Spark 3.0 & 3.1 Platform.

**SDK API 3.2**: Introduced alongside Couchbase Server 7.0, provides features in support of Scopes and Collections, extends capabilities around Open Telemetry API to instrument telemetry data, enhanced client side field level encryption to add an additional layer of security to protect sensitive data, adds new platform support such as Ubuntu 20.04 LTS.

**SDK API 3.1**: Introduced alongside Couchbase Server 6.6, focuses on Bucket Management API, adds capabilities around Full Text Search features such-as Geo-Polygon support, Flex Index, and Scoring.

**SDK API 3.0**: Introduced alongside Couchbase Server 6.5, is a major overhaul from its predecessor, has simplified surface area, removed long-standing bugs and deprecated/removed old API, introduces new programming languages Scala and Ruby, written in anticipation to support Scopes and Collections.

## [](#fundamentals)Fundamentals

Before this guide dives into the language-specific technical component of the migration, it is important to understand the high level changes first. As a migration guide, this document assumes you are familiar with the previous generation of the SDK and does not re-introduce SDK API 2 concepts. We recommend familiarizing yourself with the new SDK first by reading at least the [getting started guide](../hello-world/start-using-sdk.md), and browsing through the other chapters a little.

### [](#terminology)Terminology

The concept of a `Cluster` and a `Bucket` remain the same, but a fundamental new layer is introduced into the API: `Collections` and their `Scopes`. Collections are logical data containers inside a Couchbase bucket that let you group similar data just like a _Table_ does in a relational database — although documents inside a collection do not need to have the same structure. Scopes allow the grouping of collections into a namespace, which is very usfeul when you have multilpe tenants acessing the same bucket. Couchbase Server includes support for collections as a [developer preview](#6.5@server:developer-preview:preview-mode.adoc) in version 6.5, and as a first class concept of the programming model from [version 7.0.](../../../server/current/learn/data/scopes-and-collections.md)

Note that the SDKs include the feature from SDK 3.0, to allow easier migration.

In the previous SDK generation, particularly with the `KeyValue` API, the focus has been on the codified concept of a `Document`. Documents were read and written and had a certain structure, including the `id`/`key`, content, expiry (`ttl`), and so forth. While the server still operates on the logical concept of documents, we found that this model in practice didn't work so well for client code in certain edge cases. As a result we have removed the `Document` class/structure completely from the API. The new API follows a clear scheme: each command takes required arguments explicitly, and an option block for all optional values. The returned value is always of type `Result`. This avoids method overloading bloat in certain languages, and has the added benefit of making it easy to grasp APIs evenly across services.

As an example here is a KeyValue document fetch:

```php
$getResult = $collection->get("key", (new GetOptionsl())->timeout(3000000));
```

Compare this to a SQL++ (formerly N1QL) query:

```php
$queryResult = $cluster->query("select 1=1", (new QueryOptions())->timeout(3000000));
```

Since documents also fundamentally handled the serialization aspects of content, two new concepts are introduced: the `Serializer` and the `Transcoder`. Out of the box the SDKs ship with a JSON serializer which handles the encoding and decoding of JSON. You'll find the serializer exposes the options for methods like SQL++ queries and KeyValue subdocument operations,.

The KV API extends the concept of the serializer to the `Transcoder`. Since you can also store non-JSON data inside a document, the `Transcoder` allows the writing of binary data as well. It handles the object/entity encoding and decoding, and if it happens to deal with JSON makes uses of the configured `Serializer` internally. See the _Serialization and Transcoding_ section below for details.

### [](#what-to-look-out-for)What to look out for

The SDKs are more proactive in retrying with certain errors and in certain situations, within the timeout budget given by the user — as an example, temporary failures or locked documents are now being retried by default — making it even easier to program against certain error cases. This behavior is customizable in a `RetryStrategy`, which can be overridden on a per operation basis for maximum flexibility if you need it.

Note, most of the bootstrap sequence is now lazy (happening behind the scenes). For example, opening a bucket is not raising an error anymore, but it will only show up once you perform an actual operation. The reason behind this is to spare the application developer the work of having to do error handling in more places than needed. A bucket can go down 2ms after you opened it, so you have to handle request failures anyway. By delaying the error into the operation result itself, there is only one place to do the error handling. There will still be situations why you want to check if the resource you are accessing is available before continuing the bootstrap; for this, we have the diagnostics and ping commands at each level which allow you to perform those checks eagerly.

## [](#language-specifics)Language Specifics

Now that you are familiar with the general theme of the migration, the next sections dive deep into the specifics. First, installation and configuration are covered, then we talk about exception handling, and then each service (i.e. Key/Value, Query,…​) is covered separately.

### [](#installation-and-configuration)Installation and Configuration

The primary source of artifacts is [the installation page](#installation.adoc), where we publish links to pre-built binaries, as well as to source tarballs.

From 3.0 onwards, binaries are available for Windows with the OpenSSL dependency. Note, that OpenSSL DLLs are not distributed in the archive and must be installed separately (see the [official OpenSSL page](https://wiki.openssl.org/index.php/Binaries) for more details).

### [](#connection-lifecycle)Connection Lifecycle

Bootstrapping the SDK is staged now, so the application has to create a Cluster object first, and then open the Bucket and Collection if necessary.

As in SDK API 2.x there is no explicit shutdown, and all underlying connections still kept in the cache, for reusing in future requests. The connection idle time is controlled by the `couchbase.pool.max_idle_time_sec` PHP INI setting.

SDK API 3.x allows the performance of Queries on the Cluster level, so it is not necessary to open a bucket anymore.

SDK API 3.x does not allow the use of SASL PLAIN mechanism by default, instead it restricts to `SCRAM-SHA{1,256,512}`.

### [](#exception-handling)Exception Handling

SDK API 3.x actively uses `Exceptions` to signal errors. Instead of using single `\Couchbase\Exception`, as in SDK API 2.x, now we use a hierarchy of exceptions, which allows the handling of errors in a more reliable way:

```php
try {
  $collection->get("foo");
} catch (\Couchbase\KeyNotFoundException $ex) {
  $collection->upsert("foo", ["bar" => 42]);
}
```

Instead of SDK API 2's:

```php
try {
  $bucket->get("foo");
} catch (\Couchbase\Exception $ex) {
  if ($ex->getCode() == COUCHBASE_KEYNOTFOUND) {
    $bucket->upsert("foo", ["bar" => 42]);
  }
}
```

### [](#serialization-and-transcoding)Serialization and Transcoding

SDK API 3.x still relies on native types and supports the `json_encode` API from the standard `json.so` module (therefore it still has to be loaded before `couchbase.so`). But the `igbinary.so` transcoder is no longer supported.

> [!NOTE]
> The `json` module is a core extension from PHP 8.0.0\.

### [](#migrating-services)Migrating Services

#### [](#key-value)Key Value

Most of the KV APIs have moved from bucket-level (in SDK API 2.x) to collection-level (in SDK API 3.x). For servers which don't support collections, the application should obtain the default collection using the `bucket->defaultCollection()` function.

The following table describes the mappings from SDK API 2 KV to those of SDK API 3:

__Table 2\. KV changes__
| SDK API 2              | SDK API 3                                                   |
| ---------------------- | ----------------------------------------------------------- |
| Bucket->upsert         | Collection->upsert                                          |
| Bucket->get            | Collection->get                                             |
| \-                     | Collection->exists                                          |
| Bucket->getFromReplica | Collection->getAnyReplica and Collection.getAllReplicas     |
| Bucket->getAndLock     | Collection->getAndLock                                      |
| Bucket->getAndTouch    | Collection->getAndTouch                                     |
| Bucket->insert         | Collection->insert                                          |
| Bucket->upsert         | Collection->upsert                                          |
| Bucket->replace        | Collection->replace                                         |
| Bucket->remove         | Collection->remove                                          |
| Bucket->unlock         | Collection->unlock                                          |
| Bucket->touch          | Collection->touch                                           |
| Bucket->lookupIn       | Collection->lookupIn                                        |
| Bucket->mutateIn       | Collection->mutateIn                                        |
| Bucket->counter        | BinaryCollection->increment and BinaryCollection->decrement |
| Bucket->append         | BinaryCollection->append                                    |
| Bucket->prepend        | BinaryCollection->prepend                                   |

The `BinaryCollection` mentioned above could be retrieved from the regular collection object using the `$collection->binary()` method.

#### [](#query)Query

In SDK 3.x, the API for Query was improved and now it is more consistent with other endpoints.

> [!NOTE]
> In particular, `→rows()` is now a method rather than a property, and returns an array of fields to index with `['field-name']` instead of an object with custom property names for each field.

SDK API 2

```php
$query = N1qlQuery::fromString('SELECT airportname FROM `travel-sample` WHERE city=$city AND type=$type');
$query->namedParams(['city' => "Los Angeles", 'type' => "airport"]);
$result = $bucket->query($query);
foreach ($result->rows as $row) {
  printf("%s\n", $row->airportname);
}
```

SDK API 3

```php
$options = new QueryOptions();
$options->namedParameters(['city' => "Los Angeles", 'type' => "airport"]);
$result = $cluster->query('SELECT airportname FROM `travel-sample` WHERE city=$city AND type=$airport', $options);
foreach ($result->rows() as $row) {
  printf("%s\n", $row['airportname']);
}
```

#### [](#analytics)Analytics

Analytics queries in SDK API 3 have their own API entry point.

SDK API 2

```php
$query = AnalyticsQuery::fromString('SELECT * FROM dataset WHERE type = $type');
$query->namedParams(['type' => "airport"]);
$result = $bucket->query($query);
foreach ($result->rows as $row) {
  printf("%s\n", $row->airportname);
}
```

SDK API 3

```php
$options = new AnalyticsQueryOptions();
$options->namedParameters(['type' => "airport"]);
$result = $cluster->analyticsQuery('SELECT * FROM dataset WHERE type = $type', $options);
foreach ($result->rows() as $row) {
  printf("%s\n", $row['airportname']);
}
```

#### [](#search)Search

In SDK API 3, query options and index name has been extracted from the query object.

SDK API 2

```php
$queryPart = SearchQuery::matchPhrase("hop beer");
$query = new SearchQuery("beer-search", $queryPart);
$query->limit(3)->fields("name");

$result = $this->bucket->query($query);
foreach ($result->hits() as $hit) {
  printf("%s - %f\n", $hit->id, $hit->score);
}
```

SDK API 3

```php
$query = new MatchPhraseSearchQuery("hop beer");
$options = new SearchOptions();
$options->limit(3);
$result = $cluster->search("beer-search", $query, $options);
foreach ($result->rows() as $row) {
  printf("%s - %f\n", $row['id'], $row['score']);
}
```

#### [](#views)Views

> [!CAUTION]
> Views Service Deprecation
> 
> MapReduce Views has been deprecated since Couchbase Server 7.0, and is deprecated in the current PHP SDK. Use the SQL++ Query Service, which benefits from [Multi-Dimensional Scaling](../../../server/current/learn/services-and-indexes/services/services.md#services-and-multi-dimensional-scaling).
> 
> The guide below is for those migrating a Views application from the previous major release of the SDK (2.x API). However, the best advice is to migrate the app directly to the Query Service.
> 
> If you are provisioning Views on Couchbase Server for a legacy application, _they must run on a [couchstore](../../../server/current/learn/buckets-memory-and-storage/storage-engines.md#couchstore) bucket_.

The most noticeable change in the Views API for SDK API 3.x is the change of names for consistency control settings.

SDK API 2

```php
$query = ViewQuery::from('design_name', 'test');
$query->consistency(ViewQuery::UPDATE_BEFORE);
$res = $bucket->query($query);
foreach ($res->rows as $row) {
  printf("%s\n", $row->id);
}
```

SDK API 3

```php
$options = new ViewOptions();
$options->scanConsistency(ViewScanConsistency::REQUEST_PLUS);
$res = $bucket->viewQuery('design_name', 'test', $options);
foreach ($res->rows() as $row) {
  printf("%s\n", $row->id());
}
```

### [](#batching-with-multi-get-multi-options)Batching with Multi Get, Multi Options

This feature of the SDK API 2 was introduced to the PHP SDK in release 3.2.2 — see the API ref for [getMulti](https://docs.couchbase.com/sdk-api/couchbase-php-client/classes/Couchbase-Collection.html#method%5FgetMulti), [upsertMulti](https://docs.couchbase.com/sdk-api/couchbase-php-client/classes/Couchbase-Collection.html#method%5FupsertMulti), and [removeMulti](https://docs.couchbase.com/sdk-api/couchbase-php-client/classes/Couchbase-Collection.html#method%5FremoveMulti).

For earlier SDKs, see the [batching docs](../howtos/concurrent-async-apis.md) for use of process forks.

## [](#management-apis)Management APIs

In SDK API 2, the management APIs were centralized in the `ClusterManager` at the cluster level and the `BucketManager` at the bucket level. Since SDK API 3 provides more management APIs, they have been split up into their respective domains. For example, when in SDK API 2 you needed to remove a bucket you would call `ClusterManager.removeBucket` — you will now find it under `BucketManager.dropBucket`. And, creating a SQL++ index now lives in the `QueryIndexManager`, which is accessible through the `Cluster`.

The following tables provide a mapping from the SDK API 2 management APIs to those of SDK API 3:

__Table 3\. ClusterManager changes__
| SDK API 2                    | SDK API 3                    |
| ---------------------------- | ---------------------------- |
| ClusterManager->info         | removed                      |
| ClusterManager->listBuckets  | BucketManager->getAllBuckets |
| \-                           | BucketManager->getBucket     |
| ClusterManager->createBucket | BucketManager->createBucket  |
| ClusterManager->removeBucket | BucketManager->removeBucket  |
| ClusterManager->upsertUser   | UserManager->upsertUser      |
| ClusterManager->removeUser   | UserManager->dropUser        |
| ClusterManager->listUsers    | UserManager->getAllUsers     |
| ClusterManager->getUser      | UserManager->getUser         |

__Table 4\. BucketManager changes__
| SDK API 2                             | SDK API 3                               |
| ------------------------------------- | --------------------------------------- |
| BucketManager->info                   | removed                                 |
| BucketManager->flush                  | BucketManager->flushBucket              |
| BucketManager->listDesignDocuments    | ViewIndexManager->getAllDesignDocuments |
| BucketManager->getDesignDocument      | ViewIndexManager->getDesignDocument     |
| BucketManager->removeDesignDocument   | ViewIndexManager->dropDesignDocument    |
| BucketManager->insertDesignDocument   | ViewIndexManager->upsertDesignDocument  |
| BucketManager->upsertDesignDocument   | ViewIndexManager->upsertDesignDocument  |
| BucketManager->listN1qlIndexes        | QueryIndexManager->getAllIndexes        |
| BucketManager->createN1qlIndex        | QueryIndexManager->createIndex          |
| BucketManager->createN1qlPrimaryIndex | QueryIndexManager->createPrimaryIndex   |
| BucketManager->dropN1qlIndex          | QueryIndexManager->dropIndex            |
| BucketManager->dropN1qlPrimaryIndex   | QueryIndexManager->dropPrimaryIndex     |

## [](#sdk4-specifics)SDK 4.x specifics

PHP SDK 4.0 implements the SDK API 3 spec, so all the steps above also apply to a migration from a PHP SDK 2.x directly to PHP SDK 4.0.

Additionally, the PHP SDK 4.0 offers a new backend (Couchbase++) with support for [multi-document ACID transactions](../howtos/distributed-acid-transactions-from-the-sdk.md), as well as the capabilities required for upcoming features. You should be aware of the following considerations arising from this new backend implementation.

The following features are unsupported in 4.0\. They are available in 3.2, and will be available in a later 4.x release.

* [Response Time Availability](../concept-docs/response-time-observability.md)
* [Legacy durability](../concept-docs/durability-replication-failure-considerations.md#older-server-versions)
* Log forwarding
* Replica reads

In addition:

* `get` requests on locked documents now retry rather than fast-fail.
* The changes to [Client Settings](../ref/client-settings.md) can be found in the [API reference](https://docs.couchbase.com/sdk-api/couchbase-php-client-4.0.0/classes/Couchbase-ClusterOptions.html).
* The changes to [Connection Strings](../howtos/managing-connections.md#connection-strings) can be found in the [API reference](https://docs.couchbase.com/sdk-api/couchbase-php-client/classes/Couchbase-Cluster.html#method%5Fconnect).
* Because of the change to the backend Couchbase++ library, an Autoload is needed, as in [this imports example](../hello-world/start-using-sdk.md#imports). If you are managing your Autoloads with Composer, as recommended, this process should be trivial, and not require any additional manual addition of `require_once` statements throughout your codebase.

## [](#comparing-older-documentation)Comparing Older Documentation

You may want to visit documentation for older versions of the SDK, to help to understand application code that you are migrating. Versions that have reached end of life can be found in the [archive](https://docs-archive.couchbase.com/home/index.html). In the release notes pages of these older docs, you will also find links to the API reference for each no-longer-supported release.