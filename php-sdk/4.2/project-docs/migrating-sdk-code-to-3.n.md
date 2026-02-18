---
title: Migrating to SDK 3 API
description: The SDK API 3 (used in PHP SDK 3.x and 4.x) introduces breaking
  changes to the previous SDK API 2 APIs (used in PHP SDK 2.x) in order to
  provide a number of improvements. Collections and Scopes are introduced.
editUrl: https://github.com/couchbase/docs-sdk-php/edit/temp/4.2/modules/project-docs/pages/migrating-sdk-code-to-3.n.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/php-sdk/4.2/project-docs/migrating-sdk-code-to-3.n.html)

# Migrating to SDK 3 API

> The SDK API 3 (used in PHP SDK 3.x and 4.x) introduces breaking changes to the previous SDK API 2 APIs (used in PHP SDK 2.x) in order to provide a number of improvements. Collections and Scopes are introduced. The Document class and structure has been completely removed from the API, and the returned value is now `Result`. Retry behaviour is more proactive, and lazy bootstrapping moves all error handling to a single place. 

The current PHP SDK 4.2 is also based on the [SDK API 3.5 specification](#api-version), and offers an entirely new backend (Couchbase++) with better support for new features like Distributed ACID Transactions. We have increased the major version to reflect the importance of this implementation change as per [semantic versioning](https://semver.org/).

The intent of this migration guide is to provide detail information on the changes and what to look for while upgrading the SDK.

> [!NOTE]
> For the most part, migration from SDK API 2._x_ versions remains the same. The few 4.0-specific changes can be found at the end of this document. If you are an existing PHP SDK 3._x_ user considering migrating to SDK 4.0, you may wish to skip to the [SDK 4.0 specifics](#sdk4-specifics) below.

Unresolved include directive in modules/project-docs/pages/migrating-sdk-code-to-3.n.adoc - include::7.5@sdk:shared:partial$api-version.adoc\[\]

Unresolved include directive in modules/project-docs/pages/migrating-sdk-code-to-3.n.adoc - include::7.5@sdk:shared:partial$migration.adoc\[\]

Unresolved include directive in modules/project-docs/pages/migrating-sdk-code-to-3.n.adoc - include::7.5@sdk:shared:partial$migration.adoc\[\]

As an example here is a KeyValue document fetch:

```php
$getResult = $collection->get("key", (new GetOptionsl())->timeout(3000000));
```

Compare this to a SQL++ (formerly N1QL) query:

```php
$queryResult = $cluster->query("select 1=1", (new QueryOptions())->timeout(3000000));
```

Unresolved include directive in modules/project-docs/pages/migrating-sdk-code-to-3.n.adoc - include::7.5@sdk:shared:partial$migration.adoc\[\]

Unresolved include directive in modules/project-docs/pages/migrating-sdk-code-to-3.n.adoc - include::7.5@sdk:shared:partial$migration.adoc\[\]

Unresolved include directive in modules/project-docs/pages/migrating-sdk-code-to-3.n.adoc - include::7.5@sdk:shared:partial$migration.adoc\[\]

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

Instead of SDK API 2’s:

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

Most of the KV APIs have moved from bucket-level (in SDK API 2.x) to collection-level (in SDK API 3.x). For servers which don’t support collections, the application should obtain the default collection using the `bucket->defaultCollection()` function.

The following table describes the mappings from SDK API 2 KV to those of SDK API 3:

__Table 1\. KV changes__
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

__Table 2\. ClusterManager changes__
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

__Table 3\. BucketManager changes__
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

Unresolved include directive in modules/project-docs/pages/migrating-sdk-code-to-3.n.adoc - include::7.5@sdk:shared:partial$archive.adoc\[\]