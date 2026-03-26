---
title: Provisioning Cluster Resources
description: Provisioning cluster resources is managed at the collection or
  bucket level, depending upon the service affected.
editUrl: https://github.com/couchbase/docs-sdk-java/edit/temp/3.6/modules/howtos/pages/provisioning-cluster-resources.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.6@java-sdk:howtos:provisioning-cluster-resources.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/java-sdk/3.6/howtos/provisioning-cluster-resources.html)

# Provisioning Cluster Resources

> Provisioning cluster resources is managed at the collection or bucket level, depending upon the service affected. Common use cases are outlined here, less common use cases are covered in the [API docs](https://pkg.go.dev/github.com/couchbase/gocb/v2?tab=doc). 

The primary means for managing clusters is through the Couchbase Web UI which provides an easy to use interface for adding, removing, monitoring and modifying buckets. In some instances you may wish to have a programmatic interface. For example, if you wish to manage a cluster from a setup script, or if you are setting up buckets in test scaffolding.

The Java SDK also comes with some convenience functionality for common Couchbase management requests.

Management operations in the SDK may be performed through several interfaces depending on the object:

* BucketManager — [Cluster.buckets()](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/Cluster.html#buckets%28%29)
* UserManager — [Cluster.users()](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/Cluster.html#users%28%29)
* QueryIndexManager — [Cluster.queryIndexes()](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/Cluster.html#queryIndexes%28%29)
* AnalyticsIndexManager — [Cluster.analyticsIndexes()](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/Cluster.html#analyticsIndexes%28%29)
* SearchIndexManager — [Cluster.searchIndexes()](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/Cluster.html#searchIndexes%28%29)
* CollectionManager — [Bucket.collections()](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/Bucket.html#collections%28%29)
* ViewIndexManager — [Bucket.viewIndexes()](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/Bucket.html#viewIndexes%28%29)

> [!NOTE]
> When using a Couchbase version earlier than 6.5, you must create a valid Bucket connection using `Cluster.bucket(name)` before you can use cluster level managers.

## [](#bucket-management)Bucket Management

The `BucketManager` interface may be used to create and delete buckets from the Couchbase cluster. It is instantiated through the `Cluster.buckets()` method.

```java
Cluster cluster = Cluster.connect("localhost", "Administrator", "password");
BucketManager bucketMgr = cluster.buckets();
```

The `BucketSettings` object is used for creating or updating buckets, and for exposing information about existing buckets.

> [!WARNING]
> Note that any property that is not explicitly set when building the bucket settings will use the default value. In the case of the update, this is not necessarily the currently configured value, so you should be careful to set all properties to their correct expected values when updating an existing bucket configuration.

Here is the list of parameters available:

| Name                                          | Description                                                                                                                                                                      | Can be updated                                                                           |
| --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| name string                                   | The name of the bucket, required for creation.                                                                                                                                   | false                                                                                    |
| flushEnabled boolean                          | Enables flushing to be performed on this bucket (see the [Flushing Buckets](#flushing-buckets) section below).                                                                   | true                                                                                     |
| replicaIndexes boolean                        | Whether or not to replicate indexes.                                                                                                                                             | false                                                                                    |
| ramQuotaMB uint64                             | How much memory should each node use for the bucket, required for creation.                                                                                                      | true                                                                                     |
| numReplicas int                               | The number of replicas to use for the bucket.                                                                                                                                    | true                                                                                     |
| bucketType BucketType                         | The type of the bucket, required for creation.                                                                                                                                   | false                                                                                    |
| evictionPolicy EvictionPolicyType             | The type of the eviction to use for the bucket, defaults to VALUE\_ONLY.                                                                                                         | true (note: changing will cause the bucket to restart causing temporary inaccessibility) |
| maxExpiry time.Duration                       | The default maximum time-to-live to apply to documents in the bucket. (note: This option is only available for Couchbase and Ephemeral buckets in Couchbase Enterprise Edition.) | true                                                                                     |
| compressionMode CompressionMode               | The compression mode to apply to documents in the bucket. (note: This option is only available for Couchbase and Ephemeral buckets in Couchbase Enterprise Edition.)             | true                                                                                     |
| conflictResolutionType ConflictResolutionType | The conflict resolution type to apply to conflicts on the bucket, defaults to SEQUENCE\_NUMBER                                                                                   | false                                                                                    |

The following example creates a "hello" bucket:

```java
try {
	BucketSettings bucketSettings = BucketSettings.create("hello")
			.flushEnabled(false)
			.replicaIndexes(true)
			.ramQuotaMB(150)
			.numReplicas(1)
			.bucketType(BucketType.COUCHBASE)
			.conflictResolutionType(ConflictResolutionType.SEQUENCE_NUMBER);

	bucketMgr.createBucket(bucketSettings);
} catch (BucketExistsException e) {
	System.out.println("Bucket already exists");
}
```

We can now get this bucket and update it to enable Flush:

```java
BucketSettings settings = bucketMgr.getBucket("hello");
settings.flushEnabled(true);

bucketMgr.updateBucket(settings);
```

Once you no longer need to use the bucket, you can remove it:

```java
bucketMgr.dropBucket("hello");
```

### [](#flushing-buckets)Flushing Buckets

When a bucket is flushed, all content is removed. Because this operation is potentially dangerous it is disabled by default for each bucket. Bucket flushing may be useful in test environments where it becomes a simpler alternative to removing and creating a test bucket. You may enable bucket flushing on a per-bucket basis using the Couchbase Web Console or when creating a bucket.

You can flush a bucket in the SDK by using the `flushBucket` method:

```java
bucketMgr.flushBucket("hello");
```

The `Flush` operation may fail if the bucket does not have flush enabled, in that case it will return a `BucketNotFlushableException`.

## [](#collection-management)Collection Management

The CollectionManager interface may be used to create and delete scopes and collections from the Couchbase cluster. It is instantiated through the `Bucket.collections()` method. Refer to the [CollectionManager API documentation](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/manager/collection/CollectionManager.html) — and to its [Async counterpart](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/manager/collection/AsyncCollectionManager.html) — for further details.

```java
Cluster cluster = Cluster.connect("localhost", "scopeAdmin", "password");
Bucket bucket = cluster.bucket("travel-sample");
CollectionManager collectionMgr = bucket.collections();
```

You can create a scope:

```java
try {
  collectionMgr.createScope("example-scope");
}
catch (ScopeExistsException e) {
  System.out.println("Scope already exists");
}
```

You can then create a collection within that scope:

```java
CollectionSpec spec = CollectionSpec.create("example-collection", "example-scope");

try {
  collectionMgr.createCollection(spec);
}
catch (CollectionExistsException e) {
  System.out.println("Collection already exists");
}
catch (ScopeNotFoundException e) {
  System.out.println("The specified parent scope doesn't exist");
}
```

Finally, you can drop unneeded collections and scopes:

```java
try {
  collectionMgr.dropCollection(spec);
}
catch (CollectionNotFoundException e) {
  System.out.println("The specified collection doesn't exist");
}
catch (ScopeNotFoundException e) {
  System.out.println("The specified parent scope doesn't exist");
}

try {
  collectionMgr.dropScope("example-scope");
}
catch (ScopeNotFoundException e) {
  System.out.println("The specified scope doesn't exist");
}
```

Note that the most minimal permissions to create and drop a Scope or Collections is [Manage Scopes](../../../server/current/learn/security/roles.md#manage-scopes)along with [Data Reader](../../../server/current/learn/security/roles.md#data-reader)

You can create users with the appropriate RBAC programmatically:

```java
users.upsertUser(
  new User("scopeAdmin")
  .password("password")
  .displayName("Manage Scopes [travel-sample:*]")
  .roles(
    new Role("scope_admin", "travel-sample", "*", "*"),
    new Role("data_reader", "travel-sample", "*", "*")));
```

## [](#index-management)Index Management

In general, you will rarely need to work with Index Managers from the SDK. For those occasions when you do, index management operations can be performed with the following interfaces:

* QueryIndexManager — [Cluster.queryIndexes()](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/Cluster.html#queryIndexes%28%29)
* AnalyticsIndexManager — [Cluster.analyticsIndexes()](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/Cluster.html#analyticsIndexes%28%29)
* SearchIndexManager — [Cluster.searchIndexes()](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/Cluster.html#searchIndexes%28%29)
* ViewIndexManager — [Bucket.viewIndexes()](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/Bucket.html#viewIndexes%28%29)

You will find some of these described in the following section.

### [](#queryindexmanager)QueryIndexManager

The `QueryIndexManager` interface contains the means for managing indexes used for queries. It can be instantiated through the `Cluster.queryIndexes()` method.

```java
Cluster cluster = Cluster.connect("localhost", "Administrator", "password");
QueryIndexManager queryIndexMgr = cluster.queryIndexes();
```

Applications can use this manager to perform operations such as creating, deleting, and fetching _primary_ or _secondary_ indexes:

* A _Primary_ index is built from a document's key and is mostly suited for simple queries.
* A _Secondary_ index is the most commonly used type, and is suited for complex queries that require filtering on document fields.

> [!NOTE]
> To perform query index operations, the provided user must either be an _Admin_ or assigned the _Query Manage Index_ role. See the [Roles](../../../server/current/learn/security/roles.md#query-manage-index) page for more information.

The example below shows how to create a simple primary index, restricted to a named scope and collection, by calling the `createPrimaryIndex()` method. Note that you cannot provide a named scope or collection separately, both must be set for the `QueryIndexManager` to create an index on the relevant keyspace path.

Creating a primary index

```java
CreatePrimaryQueryIndexOptions opts = CreatePrimaryQueryIndexOptions.createPrimaryQueryIndexOptions()
		.scopeName("tenant_agent_01")
		.collectionName("users")
		// Set this if you wish to use a custom name
		// .indexName("custom_name") 
		.ignoreIfExists(true);

queryIndexMgr.createPrimaryIndex("travel-sample", opts);
```

When a primary index name is not specified, the SDK will create the index as `#primary` by default. However, if you wish to provide a custom name, you can simply set an `indexName` property in the `CreatePrimaryQueryIndexOptions` object.

You may have noticed that the example also sets the `ignoreIfExists` boolean flag. When set to `true`, this optional argument ensures that an exception is not thrown if an index under the same name already exists.

Creating a _secondary_ index follows a similar approach, with some minor differences:

Creating a secondary index

```java
try {
	CreateQueryIndexOptions opts = CreateQueryIndexOptions.createQueryIndexOptions()
			.scopeName("tenant_agent_01")
			.collectionName("users");

	queryIndexMgr.createIndex("travel-sample", "tenant_agent_01_users_email",
			Arrays.asList("preferred_email"), opts);
} catch (IndexExistsException e) {
	System.out.println("Index already exists");
}
```

The `createIndex()` method requires an index name to be provided, along with the fields to create the index on. Like the _primary_ index, you can restrict a _secondary_ index to a named scope and collection by passing some options.

Indexes can easily take a long time to build if they contain a lot of documents. In these situations, it is more ideal to build indexes in the background. To achieve this we can use the `deferred` boolean option, and set it to `true`.

Deferring index creation

```java
try {
	// Create a deferred index
	CreateQueryIndexOptions createOpts = CreateQueryIndexOptions.createQueryIndexOptions()
			.scopeName("tenant_agent_01")
			.collectionName("users")
			.deferred(true);

	queryIndexMgr.createIndex("travel-sample", "tenant_agent_01_users_phone",
			Arrays.asList("preferred_phone"), createOpts);

	// Build any deferred indexes within `travel-sample`.tenant_agent_01.users
	BuildQueryIndexOptions deferredOpts = BuildQueryIndexOptions.buildDeferredQueryIndexesOptions()
			.scopeName("tenant_agent_01")
			.collectionName("users");

	queryIndexMgr.buildDeferredIndexes("travel-sample", deferredOpts);

	// Wait for indexes to come online
	WatchQueryIndexesOptions watchOpts = WatchQueryIndexesOptions.watchQueryIndexesOptions()
			.scopeName("tenant_agent_01")
			.collectionName("users");

	queryIndexMgr.watchIndexes("travel-sample", Arrays.asList("tenant_agent_01_users_phone"), 
			Duration.ofSeconds(60), watchOpts);

} catch (IndexExistsException e) {
	System.out.println("Index already exists");
}
```

To delete a query index you can use the `dropIndex()` or `dropPrimaryIndex()` methods. Which one you use depends on the type of query index you wish to drop from the database.

Deleting an index

```java
DropPrimaryQueryIndexOptions primaryIndexOpts = DropPrimaryQueryIndexOptions.dropPrimaryQueryIndexOptions()
		.scopeName("tenant_agent_01")
		.collectionName("users");	

queryIndexMgr.dropPrimaryIndex("travel-sample", primaryIndexOpts);

// Drop a secondary index
DropQueryIndexOptions indexOpts = DropQueryIndexOptions.dropQueryIndexOptions()
		.scopeName("tenant_agent_01")
		.collectionName("users");	

queryIndexMgr.dropIndex("travel-sample", "tenant_agent_01_users_email", indexOpts);
```

## [](#views-management)Views Management

Views are stored in design documents. The SDK provides convenient methods to create, retrieve, and remove design documents. To set up views, you create design documents that contain one or more view definitions, and then insert the design documents into a bucket. Each view in a design document is represented by a name and a set of MapReduce functions. The mandatory map function describes how to select and transform the data from the bucket, and the optional reduce function describes how to aggregate the results.

In the SDK, design documents are represented by the `DesignDocument` and `View` objects. All operations on design documents are performed on the `ViewIndexManager` instance:

```java
Cluster cluster = Cluster.connect("localhost", "Administrator", "password");
Bucket bucket = cluster.bucket("travel-sample");
ViewIndexManager viewMgr = bucket.viewIndexes();
```

The following example upserts a design document with two views:

```java
Map<String, View> views = new HashMap<>();
views.put(
	"by_country",
	new View("function (doc, meta) { if (doc.type == 'landmark') { emit([doc.country, doc.city], null); } }")
);
views.put(
	"by_activity",
	new View(
		"function (doc, meta) { if (doc.type == 'landmark') { emit([doc.country, doc.city], null); } }",
		"_count")
);

DesignDocument designDocument = new DesignDocument("landmarks", views);
viewMgr.upsertDesignDocument(designDocument, DesignDocumentNamespace.DEVELOPMENT);
```

> [!WARNING]
> When you want to update an existing document with a new view (or a modification of a view's definition), you can use the `upsertDesignDocument` method.
> 
> However, this method needs the list of views in the document to be exhaustive, meaning that if you just create the new view definition as previously and add it to a new design document that you upsert, all your other views will be erased!
> 
> The solution is to perform a `getDesignDocument`, add your view definition to the DesignDocument's views list, then upsert it. This also works with view modifications, provided the change is in the `map` or `reduce` functions (just reuse the same name for the modified view), or for deletion of one out of several views in the document.

Note the use of `DesignDocumentNamespace.DEVELOPMENT`, the other option is `DesignDocumentNamespace.PRODUCTION`. This parameter specifies whether the design document should be created as development, or as production — with the former running over only a small fraction of the documents.

Now that we've created a design document we can fetch it:

```java
DesignDocument designDocument = viewMgr.getDesignDocument("landmarks", DesignDocumentNamespace.DEVELOPMENT);
System.out.print(designDocument);
```

We've created the design document using `DesignDocumentNamespace.DEVELOPMENT` and now want to push it to production, we can do this with:

```java
viewMgr.publishDesignDocument("landmarks");
```

To remove this design document:

```java
viewMgr.dropDesignDocument("landmarks", DesignDocumentNamespace.PRODUCTION);
```