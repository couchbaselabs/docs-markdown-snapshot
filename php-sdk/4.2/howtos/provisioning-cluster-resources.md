[View original HTML](/php-sdk/4.2/howtos/provisioning-cluster-resources.html)

> Provisioning cluster resources is managed at the collection or bucket level, depending upon the service affected. Common use cases are outlined here, less common use cases are covered in the [API docs](https://docs.couchbase.com/sdk-api/couchbase-php-client/namespaces/couchbase.html). 

Unresolved include directive in modules/howtos/pages/provisioning-cluster-resources.adoc - include::7.5@sdk:shared:partial$flush-info-pars.adoc\[\]

The PHP SDK also comes with some convenience functionality for common Couchbase management requests.

Management operations in the SDK may be performed through several interfaces depending on the object:

* BucketManager — [Cluster::buckets()](https://docs.couchbase.com/sdk-api/couchbase-php-client/classes/Couchbase-Cluster.html#method%5Fbuckets)
* UserManager — [Cluster::users()](https://docs.couchbase.com/sdk-api/couchbase-php-client/classes/Couchbase-Cluster.html#method%5Fusers)
* QueryIndexManager — [Cluster::queryIndexes()](https://docs.couchbase.com/sdk-api/couchbase-php-client/classes/Couchbase-Cluster.html#method%5FqueryIndexes)
* AnalyticsIndexManager — [Cluster::analyticsIndexes()](https://docs.couchbase.com/sdk-api/couchbase-php-client/classes/Couchbase-Cluster.html#method%5FanalyticsIndexes)
* SearchIndexManager — [Cluster::searchIndexes()](https://docs.couchbase.com/sdk-api/couchbase-php-client/classes/Couchbase-Cluster.html#method%5FsearchIndexes)
* CollectionManager — [Bucket::collections()](https://docs.couchbase.com/sdk-api/couchbase-php-client/classes/Couchbase-Bucket.html#method%5Fcollections)
* ViewIndexManager — [Bucket::viewIndexes()](https://docs.couchbase.com/sdk-api/couchbase-php-client/classes/Couchbase-Bucket.html#method%5FviewIndexes)

|  | When using a Couchbase version earlier than 6.5, you must create a valid Bucket connection using Cluster::bucket(name) before you can use cluster level managers. |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |

|  | Since SDK 4.0 uses the Couchbase++ library rather than libcouchbase, some management APIs have not been fully implemented, in particular: AnalyticsIndexManager SearchIndexManager ViewIndexManager CollectionManager Any attempt to use them will raise an UnsupportedOperationException error. The APIs will be available in a future 4.x release. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#bucket-management)Bucket Management

The `BucketManager` interface may be used to create and delete buckets from the Couchbase cluster. It is instantiated through the `Cluster::buckets()` method.

```php
$connectionString = "couchbase://localhost";
$options = new ClusterOptions();
$options->credentials("Administrator", "password");
$cluster = new Cluster($connectionString, $options);

$bucketMgr = $cluster->buckets();
```

The `BucketSettings` class is used for creating and updating buckets, and for exposing information about existing buckets.

Unresolved include directive in modules/howtos/pages/provisioning-cluster-resources.adoc - include::7.5@sdk:shared:partial$flush-info-pars.adoc\[\]

Here is the list of parameters available:

| Name                                          | Description                                                                                                                                                                      | Can be updated                                                                           |
| --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| name() string                                 | The name of the bucket, required for creation.                                                                                                                                   | false                                                                                    |
| flushEnabled() boolean                        | Enables flushing to be performed on this bucket (see the [Flushing Buckets](#flushing-buckets) section below).                                                                   | true                                                                                     |
| enableReplicaIndexes() boolean                | Whether or not to replicate indexes.                                                                                                                                             | false                                                                                    |
| ramQuotaMb() int                              | How much memory should each node use for the bucket, required for creation.                                                                                                      | true                                                                                     |
| numReplicas() int                             | The number of replicas to use for the bucket.                                                                                                                                    | true                                                                                     |
| bucketType() string                           | The type of the bucket, required for creation.                                                                                                                                   | false                                                                                    |
| evictionPolicy string                         | The type of the eviction to use for the bucket, defaults to VALUE\_ONLY.                                                                                                         | true (note: changing will cause the bucket to restart causing temporary inaccessibility) |
| maxTtl() int                                  | The default maximum time-to-live to apply to documents in the bucket. (note: This option is only available for Couchbase and Ephemeral buckets in Couchbase Enterprise Edition.) | true                                                                                     |
| compressionMode() string                      | The compression mode to apply to documents in the bucket. (note: This option is only available for Couchbase and Ephemeral buckets in Couchbase Enterprise Edition.)             | true                                                                                     |
| ConflictResolutionType ConflictResolutionType | The conflict resolution type to apply to conflicts on the bucket, defaults to SEQUENCE\_NUMBER                                                                                   | false                                                                                    |

The following example creates a "hello" bucket:

```php
$settings = new BucketSettings("hello");
$settings->enableFlush(false);
$settings->enableReplicaIndexes(false);
$settings->setRamQuotaMb(150);
$settings->setNumReplicas(1);
$settings->setBucketType(BucketType::COUCHBASE);
$settings->conflictResolutionType(ConflictResolutionType::SEQUENCE_NUMBER);

$bucketMgr->createBucket($settings);
```

We can now get this bucket and update it to enable Flush:

```php
$settings = $bucketMgr->getBucket("hello");
$settings->enableFlush(true);

$bucketMgr->updateBucket($settings);
```

Once you no longer need to use the bucket, you can remove it:

```php
$bucketMgr->dropBucket("hello");
```

### [](#flushing-buckets)Flushing Buckets

Unresolved include directive in modules/howtos/pages/provisioning-cluster-resources.adoc - include::7.5@sdk:shared:partial$flush-info-pars.adoc\[\]

You can flush a bucket in the SDK by using the `flush()` method:

```php
$bucketMgr->flush("hello");
```

The `flush()` operation may fail if the bucket does not have [flush enabled](https://docs.couchbase.com/sdk-api/couchbase-php-client/classes/Couchbase-Management-BucketSettings.html#method%5FflushEnabled), in that case it will return an `BucketNotFlushableException`.

## [](#index-management)Index Management

Unresolved include directive in modules/howtos/pages/provisioning-cluster-resources.adoc - include::7.5@sdk:shared:partial$flush-info-pars.adoc\[\]

### [](#queryindexmanager)QueryIndexManager

The `QueryIndexManager` interface contains the means for managing indexes used for queries. It can be instantiated through the `Cluster::queryIndexes()` method.

```php
$options = new ClusterOptions();
$options->credentials("Administrator", "password");
$cluster = new Cluster("couchbase://localhost", $options);

$queryIndexMgr = $cluster->queryIndexes();
```

Unresolved include directive in modules/howtos/pages/provisioning-cluster-resources.adoc - include::7.5@sdk:shared:partial$flush-info-pars.adoc\[\]

The example below shows how to create a simple primary index, restricted to a named scope and collection, by calling the `createPrimaryIndex()` method. Note that you cannot provide a named scope or collection separately, both must be set for the `QueryIndexManager` to create an index on the relevant keyspace path.

Creating a primary index

```php
$options = new CreateQueryPrimaryIndexOptions();
$options->scopeName("tenant_agent_01");
$options->collectionName("users");
// Set this if you wish to use a custom name
// $options->indexName("custom_name");
$options->ignoreIfExists(true);

$queryIndexMgr->createPrimaryIndex("travel-sample", $options);
```

When a primary index name is not specified, the SDK will create the index as `#primary` by default. However, if you wish to provide a custom name, you can simply set an `indexName` property in the `CreatePrimaryQueryIndexOptions` class.

You may have noticed that the example also sets the `ignoreIfExists` boolean flag. When set to `true`, this optional argument ensures that an error is not thrown if an index under the same name already exists.

Creating a _secondary_ index follows a similar approach, with some minor differences:

Creating a secondary index

```php
$options = new CreateQueryIndexOptions();
$options->scopeName("tenant_agent_01");
$options->collectionName("users");

$queryIndexMgr->createIndex("travel-sample", "tenant_agent_01_users_email", ["preferred_email"], $options);
```

The `createIndex()` method requires an index name to be provided, along with the fields to create the index on. Like the _primary_ index, you can restrict a _secondary_ index to a named scope and collection by passing some options.

Indexes can easily take a long time to build if they contain a lot of documents. In these situations, it is more ideal to build indexes in the background. To achieve this we can use the `deferred` boolean option, and set it to `true`.

Deferring index creation

```php
// Create a deferred index
$createOpts = new CreateQueryIndexOptions();
$createOpts->scopeName("tenant_agent_01");
$createOpts->collectionName("users");
$createOpts->deferred(true);

$queryIndexMgr->createIndex("travel-sample", "tenant_agent_01_users_phone", ["preferred_phone"], $createOpts);

// Build any deferred indexes within `travel-sample`.tenant_agent_01.users
$deferredOpts = new BuildQueryIndexesOptions();
$deferredOpts->scopeName("tenant_agent_01");
$deferredOpts->collectionName("users");

$queryIndexMgr->buildDeferredIndexes("travel-sample", $deferredOpts);

// Wait for indexes to come online
$watchOpts = new WatchQueryIndexesOptions();
$watchOpts->scopeName("tenant_agent_01");
$watchOpts->collectionName("users");

$queryIndexMgr->watchIndexes("travel-sample", ["tenant_agent_01_users_phone"], 30000, $watchOpts);
```

To delete a query index you can use the `dropIndex()` or `dropPrimaryIndex()` methods. Which one you use depends on the type of query index you wish to drop from the database.

Deleting an index

```php
// Drop a primary index
$options = new DropQueryPrimaryIndexOptions();
$options->scopeName("tenant_agent_01");
$options->collectionName("users");

$queryIndexMgr->dropPrimaryIndex("travel-sample", $options);

// Drop a secondary index
$options = new DropQueryIndexOptions();
$options->scopeName("tenant_agent_01");
$options->collectionName("users");

$queryIndexMgr->dropIndex("travel-sample", "tenant_agent_01_users_email", $options);
```