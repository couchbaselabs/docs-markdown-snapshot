---
title: Provisioning Cluster Resources
description: Provisioning cluster resources is managed at the collection or
  bucket level, depending upon the service affected.
editUrl: https://github.com/couchbase/docs-sdk-scala/edit/release/3.10/modules/howtos/pages/provisioning-cluster-resources.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.10@scala-sdk:howtos:provisioning-cluster-resources.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/scala-sdk/3.10/howtos/provisioning-cluster-resources.html)

# Provisioning Cluster Resources

> Provisioning cluster resources is managed at the collection or bucket level, depending upon the service affected. Common use cases are outlined here, less common use cases are covered in the [API docs](https://docs.couchbase.com/sdk-api/couchbase-scala-client/com/couchbase/client/scala/index.html). 

The primary means for managing clusters is through the Couchbase Web UI which provides an easy to use interface for adding, removing, monitoring and modifying buckets. In some instances you may wish to have a programmatic interface. For example, if you wish to manage a cluster from a setup script, or if you are setting up buckets in test scaffolding.

The Scala SDK also comes with some convenience functionality for common Couchbase management requests.

> [!TIP]
> Managing Capella Clusters
> 
> This part of the SDK API predates the Capella Management API, and is only intended to work with self-managed Couchbase Server clusters.
> 
> Management of your Capella Operational cluster is available away from the Web UI with the [Capella Management API](../../../cloud/management-api-guide/management-api-intro.md).

Management operations in the SDK may be performed through several interfaces depending on the object:

* BucketManager — [Cluster.buckets](https://docs.couchbase.com/sdk-api/couchbase-scala-client/com/couchbase/client/scala/Cluster.html#buckets:com.couchbase.client.scala.manager.bucket.BucketManager)
* UserManager — [Cluster.users](https://docs.couchbase.com/sdk-api/couchbase-scala-client/com/couchbase/client/scala/Cluster.html#users:com.couchbase.client.scala.manager.user.UserManager) — see the [User Management page](sdk-user-management-example.md)
* QueryIndexManager — [Cluster.queryIndexes](https://docs.couchbase.com/sdk-api/couchbase-scala-client/com/couchbase/client/scala/Cluster.html#queryIndexes:com.couchbase.client.scala.manager.query.QueryIndexManager)
* AnalyticsIndexManager — [Cluster.analyticsIndexes](https://docs.couchbase.com/sdk-api/couchbase-scala-client/com/couchbase/client/scala/Cluster.html#analyticsIndexes:com.couchbase.client.scala.manager.analytics.AnalyticsIndexManager)
* SearchIndexManager — [Cluster.searchIndexes](https://docs.couchbase.com/sdk-api/couchbase-scala-client/com/couchbase/client/scala/Cluster.html#searchIndexes:com.couchbase.client.scala.manager.search.SearchIndexManager)
* CollectionManager — [Bucket.collections](https://docs.couchbase.com/sdk-api/couchbase-scala-client/com/couchbase/client/scala/Bucket.html#collections:com.couchbase.client.scala.manager.collection.CollectionManager)
* ViewIndexManager — [Bucket.viewIndexes](https://docs.couchbase.com/sdk-api/couchbase-scala-client/com/couchbase/client/scala/Bucket.html#viewIndexes:com.couchbase.client.scala.manager.view.ViewIndexManager)

> [!NOTE]
> When using a Couchbase version earlier than 6.5, you must create a valid Bucket connection using `Cluster.bucket(name)` before you can use cluster-level managers.

## [](#bucket-management)Bucket Management

The `BucketManager` interface may be used to create and delete buckets from the Couchbase cluster.

The `CreateBucketSettings` and `BucketSettings` classes are used for creating and updating buckets. `BucketSettings` is also used for exposing information about existing buckets.

> [!WARNING]
> Note that any property that is not explicitly set when building the bucket settings will use the default value. In the case of the update, this is not necessarily the currently configured value, so you should be careful to set all properties to their correct expected values when updating an existing bucket configuration.

Here is the list of parameters available for `CreateBucketSettings` and `BucketSettings`. The "Updatable" column indicates whether the parameter may only be specified when creating a bucket, or whether it may be updated after creation.

| Name                   | Type                   | Description                                                                                                                                                                      | Updatable                                                                                |
| ---------------------- | ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| name                   | String                 | The name of the bucket, required for creation.                                                                                                                                   | false                                                                                    |
| flushEnabled           | boolean                | Enables flushing to be performed on this bucket (see the [Flushing Buckets](#flushing-buckets) section below).                                                                   | true                                                                                     |
| replicaIndexes         | boolean                | Whether or not to replicate indexes.                                                                                                                                             | false                                                                                    |
| ramQuotaMB             | int                    | How much memory should each node use for the bucket, required for creation.                                                                                                      | true                                                                                     |
| numReplicas            | int                    | The number of replicas to use for the bucket.                                                                                                                                    | true                                                                                     |
| bucketType             | BucketType             | The type of the bucket, required for creation.                                                                                                                                   | false                                                                                    |
| ejectionMethod         | EjectionMethod         | The type of the ejection to use for the bucket, defaults to ValueOnly.                                                                                                           | true (note: changing will cause the bucket to restart causing temporary inaccessibility) |
| maxTTL                 | int                    | The default maximum time-to-live to apply to documents in the bucket. (note: This option is only available for Couchbase and Ephemeral buckets in Couchbase Enterprise Edition.) | true                                                                                     |
| compressionMode        | CompressionMode        | The compression mode to apply to documents in the bucket. (note: This option is only available for Couchbase and Ephemeral buckets in Couchbase Enterprise Edition.)             | true                                                                                     |
| conflictResolutionType | ConflictResolutionType | The conflict resolution type to apply to conflicts on the bucket, defaults to SequenceNumber                                                                                     | false                                                                                    |

The following example creates a "hello" bucket:

```scala
val bucketManager: BucketManager = cluster.buckets

val result: Try[Unit] = bucketManager.create(
  CreateBucketSettings("hello", ramQuotaMB = 1024)
    .flushEnabled(false)
    .replicaIndexes(false)
    .numReplicas(1)
    .bucketType(BucketType.Couchbase)
    .conflictResolutionType(ConflictResolutionType.SequenceNumber))

result match {
  case Success(_) =>
  case Failure(err) => print(s"Failed with error $err")
}
```

We can now get this bucket and update it to enable Flush:

```scala
val result: Try[Unit] = bucketManager.getBucket("hello")
  .flatMap((bucket: BucketSettings) => {
    val updated = bucket.toCreateBucketSettings.flushEnabled(true)
    bucketManager.updateBucket(updated)
  })

// Result error-checking omitted for brevity
```

Once you no longer need to use the bucket, you can remove it:

```scala
val result: Try[Unit] = bucketManager.dropBucket("hello")

// Result error-checking omitted for brevity
```

### [](#flushing-buckets)Flushing Buckets

When a bucket is flushed, all content is removed. Because this operation is potentially dangerous it is disabled by default for each bucket. Bucket flushing may be useful in test environments where it becomes a simpler alternative to removing and creating a test bucket. You may enable bucket flushing on a per-bucket basis using the Couchbase Web Console or when creating a bucket.

You can flush a bucket in the SDK by using the `Flush` method:

```scala
val result: Try[Unit] = bucketManager.flushBucket("hello")

result match {
  case Success(_) =>
  case Failure(err: BucketNotFlushableException) =>
    print("Flushing not enabled on this bucket")
  case Failure(err) => print(s"Failed with error $err")
}
```

## [](#collection-management)Collection Management

The CollectionManager interface may be used to create and delete scopes and collections from the Couchbase cluster. It is instantiated through the `Bucket.collections()` method. Refer to the [CollectionManager and AsyncCollectionManager API documentation](https://docs.couchbase.com/sdk-api/couchbase-scala-client/com/couchbase/client/scala/manager/collection/index.html)for further details.

```scala
val collectionMgr = bucket.collections;
```

You can create a scope:

```scala
collectionMgr.createScope("example-scope") match {
  case Success(_) =>
    println("Created scope OK")
  case Failure(err: ScopeExistsException) =>
    println("scope already exists")
  case Failure(err) =>
    println(err)
}
```

You can then create a collection within that scope:

```scala
val spec = CollectionSpec("example-collection", "example-scope");

collectionMgr.createCollection(spec)  match {
  case Success(_) =>
    println("Created collection OK")
  case Failure(err: ScopeNotFoundException) =>
    println("scope not found")
  case Failure(err: CollectionExistsException) =>
    println("collection already exists")
  case Failure(err) =>
    println(err)
}
```

Finally, you can drop unneeded collections and scopes:

```scala
collectionMgr.dropCollection(spec)
match {
  case Success(_) =>
    println("Dropped collection OK")
  case Failure(err: ScopeNotFoundException) =>
    println("scope not found")
  case Failure(err: CollectionNotFoundException) =>
    println("collection not found")
  case Failure(err) =>
    println(err)
}

[data-source-url=https://github.com/couchbase/docs-sdk-scala/blob/40c5c0756ea54842b8060584b43285a19043c2a9/modules/devguide/examples/scala/CollectionManagerExample.scala#L110-L118]
collectionMgr.dropScope("example-scope")
match {
  case Success(_) =>
    println("Dropped scope OK")
  case Failure(err: ScopeNotFoundException) =>
    println("scope not found")
  case Failure(err) =>
    println(err)
}
```

Note that the most minimal permissions to create and drop a Scope or Collection is [Manage Scopes](../../../server/current/learn/security/roles.md#manage-scopes)along with [Data Reader](../../../server/current/learn/security/roles.md#data-reader).

You can create users with the appropriate RBAC programmatically:

```scala
val users = cluster.users
val user = User("scopeAdmin")
  .password("password")
  .roles(
    new Role("scope_admin", Some("travel-sample")),
    new Role("data_reader", Some("travel-sample")))
users.upsertUser(user).get
```

## [](#index-management)Index Management

In general, you will rarely need to work with Index Managers from the SDK. For those occasions when you do, index management operations can be performed with the following interfaces:

* QueryIndexManager — [Cluster.queryIndexes](https://docs.couchbase.com/sdk-api/couchbase-scala-client/com/couchbase/client/scala/Cluster.html#queryIndexes:com.couchbase.client.scala.manager.query.QueryIndexManager)
* AnalyticsIndexManager — [Cluster.analyticsIndexes](https://docs.couchbase.com/sdk-api/couchbase-scala-client/com/couchbase/client/scala/Cluster.html#analyticsIndexes:com.couchbase.client.scala.manager.analytics.AnalyticsIndexManager)
* SearchIndexManager — [Cluster.searchIndexes](https://docs.couchbase.com/sdk-api/couchbase-scala-client/com/couchbase/client/scala/Cluster.html#searchIndexes:com.couchbase.client.scala.manager.search.SearchIndexManager)
* ViewIndexManager — [Bucket.viewIndexes](https://docs.couchbase.com/sdk-api/couchbase-scala-client/com/couchbase/client/scala/Bucket.html#viewIndexes:com.couchbase.client.scala.manager.view.ViewIndexManager)

You will find some of these described in the following section.

### [](#queryindexmanager)QueryIndexManager

The `QueryIndexManager` interface contains the means for managing indexes used for queries.  
It can be accessed via `Cluster.queryIndexes`.

```scala
val cluster = Cluster.connect("localhost", "Administrator", "password").get
val queryIndexMgr = cluster.queryIndexes
```

Applications can use this manager to perform operations such as creating, deleting, and fetching _primary_ or _secondary_ indexes:

* A _Primary_ index is built from a document's key and is mostly suited for simple queries.
* A _Secondary_ index is the most commonly used type, and is suited for complex queries that require filtering on document fields.

> [!NOTE]
> To perform query index operations, the provided user must either be an _Admin_ or assigned the _Query Manage Index_ role. See the [Roles](../../../server/current/learn/security/roles.md#query-manage-index) page for more information.

The example below shows how to create a simple primary index, restricted to a named scope and collection, by calling the `createPrimaryIndex()` method. Note that you cannot provide a named scope or collection separately, both must be set for the `QueryIndexManager` to create an index on the relevant keyspace path.

Creating a primary index

```scala
val result: Try[Unit] = queryIndexMgr.createPrimaryIndex(
  "travel-sample",
  // Set this if you wish to use a custom name
  // indexName = Option("custom_name"),
  scopeName = Option("tenant_agent_01"),
  collectionName = Option("users"),
  ignoreIfExists = true
)
result match {
  case Success(_)   =>
  case Failure(err) => throw err
}
```

When a primary index name is not specified, the SDK will create the index as `#primary` by default. However, if you wish to provide a custom name, you can simply pass an `indexName` argument to `createPrimaryIndex()`.

You may have noticed that the example also sets the `ignoreIfExists` boolean flag. When set to `true`, this optional argument ensures that an error is not thrown if an index under the same name already exists.

Creating a _secondary_ index follows a similar approach, with some minor differences:

Creating a secondary index

```scala
val result: Try[Unit] = queryIndexMgr.createIndex(
  "travel-sample",
  "tenant_agent_01_users_email",
  Array("preferred_email"),
  scopeName = Option("tenant_agent_01"),
  collectionName = Option("users")
)
result match {
  case Success(_) =>
  case Failure(err: IndexExistsException) => println("Index already exists!")
  case Failure(err) => throw err
}
```

The `createIndex()` method requires an index name to be provided, along with the fields to create the index on. Like the _primary_ index, you can restrict a _secondary_ index to a named scope and collection.

Indexes can easily take a long time to build if they contain a lot of documents. In these situations, it is more ideal to build indexes in the background. To achieve this we can use the `deferred` boolean option, and set it to `true`.

Deferring index creation

```scala
// Create a deferred index
var result: Try[Unit] = queryIndexMgr.createIndex(
  "travel-sample",
  "tenant_agent_01_users_phone",
  Array("preferred_phone"),
  scopeName = Option("tenant_agent_01"),
  collectionName = Option("users"),
  deferred = Option(true)
)
result match {
  case Success(_) =>
  case Failure(err: IndexExistsException) => println("Index already exists!")
  case Failure(err) => throw err
}

// Build any deferred indexes within `travel-sample`.tenant_agent_01.users
result = queryIndexMgr.buildDeferredIndexes(
  "travel-sample",
  scopeName = Option("tenant_agent_01"),
  collectionName = Option("users")
)
result match {
  case Success(_)   =>
  case Failure(err) => throw err
}

// Wait for indexes to come online
result = queryIndexMgr.watchIndexes(
  "travel-sample",
  Array("tenant_agent_01_users_phone"),
  Duration("30 seconds"),
  scopeName = Option("tenant_agent_01"),
  collectionName = Option("users")
)
result match {
  case Success(_) =>
  case Failure(err: IndexExistsException) => println("Index already exists!")
  case Failure(err) => throw err
}
```

To delete a query index you can use the `dropIndex()` or `dropPrimaryIndex()` methods. Which one you use depends on the type of query index you wish to drop from the cluster.

Deleting an index

```scala
 // Drop a primary index
 var result: Try[Unit] = queryIndexMgr.dropPrimaryIndex(
   "travel-sample",
   scopeName = Option("tenant_agent_01"),
   collectionName = Option("users")
 )
 result match {
   case Success(_)   =>
   case Failure(err) => throw err
 }

 // Drop a secondary index
result = queryIndexMgr.dropIndex(
   "travel-sample",
   "tenant_agent_01_users_email",
   scopeName = Option("tenant_agent_01"),
   collectionName = Option("users")
 )
 result match {
   case Success(_)   =>
   case Failure(err) => throw err
 }
```

## [](#eventing-management)Eventing Management

## [](#view-management)View Management

Views are stored in design documents. The SDK provides convenient methods to create, retrieve, and remove design documents. To set up views, you create design documents that contain one or more view definitions, and then insert the design documents into a bucket. Each view in a design document is represented by a name and a set of MapReduce functions. The mandatory map function describes how to select and transform the data from the bucket, and the optional reduce function describes how to aggregate the results.

In the SDK, design documents are represented by the `DesignDocument` and `View` structs. All operations on design documents are performed on the `ViewIndexManager` instance:

```scala
val viewIndexManager: ViewIndexManager = bucket.viewIndexes
```

The following example upserts a design document with two views:

```scala
val view1 = View("function (doc, meta) { if (doc.type == 'landmark') { emit([doc.country, doc.city], null); } }")
val view2 = View("function (doc, meta) { if (doc.type == 'landmark') { emit(doc.activity, null); } }", reduce = Some("_count"))

val designDoc = DesignDocument("landmarks",
  Map("by_country" -> view1, "by_activity " -> view2))

viewIndexManager.upsertDesignDocument(designDoc, DesignDocumentNamespace.Development)
```

> [!WARNING]
> When you want to update an existing document with a new view (or a modification of a view's definition), you can use the `upsertDesignDocument` method.
> 
> However, this method needs the list of views in the document to be exhaustive, meaning that if you just create the new view definition as previously and add it to a new design document that you upsert, all your other views will be erased!
> 
> The solution is to perform a `getDesignDocument`, add your view definition to the DesignDocument's views list, then upsert it. This also works with view modifications, provided the change is in the `map` or `reduce` functions (just reuse the same name for the modified view), or for deletion of one out of several views in the document.

Note the use of `DesignDocumentNamespace.Development`, the other option is `DesignDocumentNamespace.Production`. This parameter specifies whether the design document should be created as development, or as production — with the former running over only a small fraction of the documents.

Now that we've created a design document we can fetch it:

```scala
val designDoc: Try[DesignDocument] =
  viewIndexManager.getDesignDocument("landmarks", DesignDocumentNamespace.Development)
```

We've created the design document using `DesignDocumentNamespace.Development` and now want to push it to production, we can do this with:

```scala
val publishResult = viewIndexManager.publishDesignDocument("landmarks")

// Result error-handling omitted for brevity
```

To remove this design document:

```scala
val dropResult = viewIndexManager.dropDesignDocument("landmarks", DesignDocumentNamespace.Production)
// Result error-handling omitted for brevity
```