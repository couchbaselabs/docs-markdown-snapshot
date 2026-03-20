---
title: Provisioning Cluster Resources
description: Provisioning cluster resources is managed at the collection or
  bucket level, depending upon the service affected.
editUrl: https://github.com/couchbase/docs-sdk-dotnet/edit/temp/3.6/modules/howtos/pages/provisioning-cluster-resources.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:3.6@dotnet-sdk:howtos:provisioning-cluster-resources.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/dotnet-sdk/3.6/howtos/provisioning-cluster-resources.html)

# Provisioning Cluster Resources

> Provisioning cluster resources is managed at the collection or bucket level, depending upon the service affected. Common use cases are outlined here, less common use cases are covered in the [API docs](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/index.html). 

The primary means for managing clusters is through the Couchbase Web UI which provides an easy to use interface for adding, removing, monitoring and modifying buckets. In some instances you may wish to have a programmatic interface. For example, if you wish to manage a cluster from a setup script, or if you are setting up buckets in test scaffolding.

The .NET SDK also comes with some convenience functionality for common Couchbase management requests.

Management operations in the SDK may be performed through several interfaces depending on the object:

* IBucketManager — [Cluster.Buckets](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.Cluster.html#Couchbase%5FCluster%5FBuckets)
* IUserManager — [Cluster.Users](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.Cluster.html#Couchbase%5FCluster%5FUsers)
* ICollectionQueryIndexManager — [Collection.QueryIndexes](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.Management.Query.ICollectionQueryIndexManager.html)
* IAnalyticsIndexManager — [Cluster.AnalyticsIndexes](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.Cluster.html#Couchbase%5FCluster%5FAnalyticsIndexes)
* ISearchIndexManager — [Cluster.SearchIndexes](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.Cluster.html#Couchbase%5FCluster%5FSearchIndexes)
* ICouchbaseCollectionManager — [Bucket.Collections](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.IBucket.html#Couchbase%5FIBucket%5FCollections)
* IViewIndexManager — [Bucket.ViewIndexes](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.IBucket.html#Couchbase%5FIBucket%5FViewIndexes)

> [!NOTE]
> When using a Couchbase version earlier than 6.5, you must create a valid Bucket connection using `Cluster.Bucket(name)` before you can use cluster level managers.

## [](#bucket-management)Bucket Management

The `IBucketManager` interface may be used to create and delete buckets from the Couchbase cluster. It is referenced via the `Cluster.Buckets` property.

```golang
var cluster = await Cluster.ConnectAsync("couchbase://your-ip", "Administrator", "password");
var bucketMgr = cluster.Buckets;
```

The `BucketSettings` object is used for creating or updating buckets, and for exposing information about existing buckets.

> [!WARNING]
> Note that any property that is not explicitly set when building the bucket settings will use the default value. In the case of the update, this is not necessarily the currently configured value, so you should be careful to set all properties to their correct expected values when updating an existing bucket configuration.

Here is the list of parameters available:

| Name                                          | Description                                                                                                                                                                             | Can be updated                                                                           |
| --------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Name string                                   | The name of the bucket, required for creation.                                                                                                                                          | false                                                                                    |
| FlushEnabled boolean                          | Enables flushing to be performed on this bucket (see the [Flushing Buckets](#flushing-buckets) section below).                                                                          | true                                                                                     |
| ReplicaIndexes boolean                        | Whether or not to replicate indexes.                                                                                                                                                    | false                                                                                    |
| RamQuotaMB Int64                              | How much memory should each node use for the bucket, required for creation.                                                                                                             | true                                                                                     |
| NumReplicas Int32                             | The number of replicas to use for the bucket.                                                                                                                                           | true                                                                                     |
| BucketType BucketType                         | The type of the bucket, required for creation.                                                                                                                                          | false                                                                                    |
| EvictionPolicy EvictionPolicyType             | The type of the eviction to use for the bucket, defaults to ValueOnly.                                                                                                                  | true (note: changing will cause the bucket to restart causing temporary inaccessibility) |
| MaxTTL Int32                                  | The default maximum time-to-live to apply to documents in the bucket. (note: This option is only available for Couchbase and Ephemeral buckets in Couchbase Server Enterprise Edition.) | true                                                                                     |
| CompressionMode CompressionMode               | The compression mode to apply to documents in the bucket. (note: This option is only available for Couchbase and Ephemeral buckets in Couchbase Server Enterprise Edition.)             | true                                                                                     |
| ConflictResolutionType ConflictResolutionType | The conflict resolution type to apply to conflicts on the bucket, defaults to SequenceNumber                                                                                            | false                                                                                    |

The following example creates a `hello` bucket:

```csharp
await bucketMgr.CreateBucketAsync(
    new BucketSettings{
        Name = "hello",
        FlushEnabled = false,
        RamQuotaMB = 100,
        NumReplicas = 0,
        BucketType = BucketType.Couchbase,
        ConflictResolutionType = ConflictResolutionType.SequenceNumber
    }
);
```

We can now get this bucket and update it to enable Flush:

```csharp
var settings = await bucketMgr.GetBucketAsync("hello");
settings.RamQuotaMB = 100;
settings.FlushEnabled = true;
settings.ConflictResolutionType = null;

await bucketMgr.UpdateBucketAsync(settings);
```

Once you no longer need to use the bucket, you can remove it:

```csharp
await bucketMgr.DropBucketAsync("hello");
```

### [](#flushing-buckets)Flushing Buckets

When a bucket is flushed, all content is removed. Because this operation is potentially dangerous it is disabled by default for each bucket. Bucket flushing may be useful in test environments where it becomes a simpler alternative to removing and creating a test bucket. You may enable bucket flushing on a per-bucket basis using the Couchbase Web Console or when creating a bucket.

You can flush a bucket in the SDK by using `FlushBucketAsync()`.

```csharp
await bucketMgr.FlushBucketAsync("hello");
```

The `Flush` operation may fail if the bucket does not have flush enabled, in that case it will return a `BucketIsNotFlushableException`.

## [](#collection-management)Collection Management

The CollectionManager interface may be used to create and delete scopes and collections from the Couchbase cluster. It can be referenced via the `Bucket.Collections` property. Refer to the [CollectionManager API documentation](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.Management.Collections.ICouchbaseCollectionManager.html)for further details.

```csharp
ICouchbaseCollectionManager collectionMgr = bucket.Collections;
```

You can create a scope:

```csharp
try {
    await collectionMgr.CreateScopeAsync("example-scope");
}
catch (ScopeExistsException) {
    Console.WriteLine("The scope already exists");
}
```

You can then create a collection within that scope:

```csharp
var spec = new CollectionSpec("example-scope", "example-collection");

try {
    await collectionMgr.CreateCollectionAsync(spec);
}
catch (CollectionExistsException) {
    Console.WriteLine("Collection already exists");
}
catch (ScopeNotFoundException) {
    Console.WriteLine("The specified parent scope doesn't exist");
}
```

Finally, you can drop unneeded collections and scopes:

```csharp
try {
    await collectionMgr.DropCollectionAsync(spec);
}
catch (CollectionNotFoundException) {
    Console.WriteLine("The specified collection doesn't exist");
}
catch (ScopeNotFoundException) {
    Console.WriteLine("The specified parent scope doesn't exist");
}

try {
    await collectionMgr.DropScopeAsync("example-scope");
}
catch (ScopeNotFoundException) {
    Console.WriteLine("The specified scope doesn't exist");
}
```

Note that the most minimal permissions to create and drop a Scope or Collection is [Manage Scopes](../../../server/current/learn/security/roles.md#manage-scopes)along with [Data Reader](../../../server/current/learn/security/roles.md#data-reader).

You can create users with the appropriate RBAC programmatically:

```csharp
ICluster clusterAdmin = await Cluster.ConnectAsync(
    "couchbase://your-ip", "Administrator", "password");
IUserManager users =  clusterAdmin.Users;

var user = new User("scopeAdmin") {
    Password = "password",
    DisplayName = "Manage Scopes [travel-sample:*]",
    Roles = new List<Role>() {
        new Role("scope_admin", "travel-sample"),
        new Role("data_reader", "travel-sample")}
};

await users.UpsertUserAsync(user);
```

You can enumerate Scopes and Collections using the `CollectionManager` and the properties of the `ScopeSpec` and `CollectionSpec` objects retrieved.

```csharp
var scopes = await collectionMgr.GetAllScopesAsync();
foreach (ScopeSpec scopeSpec in scopes) {
    Console.WriteLine($"Scope: {scopeSpec.Name}");
    
    foreach (CollectionSpec collectionSpec in scopeSpec.Collections) {
        Console.WriteLine($" - {collectionSpec.Name}");
    }
}
```

## [](#index-management)Index Management

In general, you will rarely need to work with Index Managers from the SDK. For those occasions when you do, index management operations can be performed with the following interfaces:

* ICollectionQueryIndexManager — [Collection.QueryIndexes](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.Management.Query.ICollectionQueryIndexManager.html)
* IAnalyticsIndexManager — [Cluster.AnalyticsIndexes](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.Cluster.html#Couchbase%5FCluster%5FAnalyticsIndexes)
* ISearchIndexManager — [Cluster.SearchIndexes](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.Cluster.html#Couchbase%5FCluster%5FSearchIndexes)
* IViewIndexManager — [Bucket.ViewIndexes](https://docs.couchbase.com/sdk-api/couchbase-net-client/api/Couchbase.IBucket.html#Couchbase%5FIBucket%5FViewIndexes)

You will find some of these described in the following section.

### [](#queryindexmanager)QueryIndexManager

The `ICollectionQueryIndexManager` interface contains the means for managing indexes used for queries. It’s referenced through the `Collection.QueryIndexes` property.

```csharp
var cluster = await Cluster.ConnectAsync("couchbase://your-ip", "Administrator", "password");
var bucket = await cluster.BucketAsync("travel-sample");
var scope = await bucket.ScopeAsync("tenant_agent_01");
var collection = await scope.CollectionAsync("users");

var queryIndexMgr = collection.QueryIndexes;
```

> [!NOTE]
> The `ICollectionQueryIndexManager` can only manage indexes in the keyspace it’s set on. You must create another Query Manager interface to manage indexes on a different keyspace.

Applications can use this manager to perform operations such as creating, deleting, and fetching _primary_ or _secondary_ indexes:

* A _Primary_ index is built from a document’s key and is mostly suited for simple queries.
* A _Secondary_ index is the most commonly used type, and is suited for complex queries that require filtering on document fields.

> [!NOTE]
> To perform query index operations, the provided user must either be an _Admin_ or assigned the _Query Manage Index_ role. See the [Roles](../../../server/current/learn/security/roles.md#query-manage-index) page for more information.

The following example shows how to create a primary index, by calling the `CreatePrimaryIndexAsync()` method.

Creating a primary index

```csharp
await queryIndexMgr.CreatePrimaryIndexAsync(
    new CreatePrimaryQueryIndexOptions()
        // Set this if you wish to use a custom name
        // .IndexName("custom_name")
        .IgnoreIfExists(true)
);
```

When a primary index name is not specified, the SDK creates the index as `#primary` by default. However, if you want to provide a custom name, you can set an `IndexName` property in the `CreatePrimaryQueryIndexOptions` class.

You may have noticed that the example also sets the `IgnoreIfExists` boolean flag. When set to `true`, this optional argument ensures that an error is not thrown if an index under the same name already exists.

Creating a _secondary_ index follows a similar approach, with some minor differences:

Creating a secondary index

```csharp
try
{
    await queryIndexMgr.CreateIndexAsync(
        "tenant_agent_01_users_email",
        new[] { "preferred_email" },
        new CreateQueryIndexOptions()
    );
}
catch (IndexExistsException)
{
    Console.WriteLine("Index already exists!");
}
```

The `CreateIndexAsync()` method requires an index name to be provided, along with the fields to create the index on.

Indexes can take a long time to build if they contain a lot of documents. In these situations, it’s ideal to build indexes in the background. To achieve this we can use the `Deferred` boolean option, and set it to `true`.

Deferring index creation

```csharp
try
{
    // Create a deferred index
    await queryIndexMgr.CreateIndexAsync(
        "tenant_agent_01_users_phone",
        new[] { "preferred_phone" },
        new CreateQueryIndexOptions()
            .Deferred(true)
    );

    // Build any deferred indexes within `travel-sample`.tenant_agent_01.users
    await queryIndexMgr.BuildDeferredIndexesAsync(
        new BuildDeferredQueryIndexOptions()
    );

    // Wait for indexes to come online
    TimeSpan duration = TimeSpan.FromSeconds(10);
    await queryIndexMgr.WatchIndexesAsync(
        new[] { "tenant_agent_01_users_phone" },
        duration,
        new WatchQueryIndexOptions()
    );
}
catch (IndexExistsException)
{
    Console.WriteLine("Index already exists!");
}
```

To delete a query index you can use the `DropIndexAsync()` or `DropPrimaryIndexAsync()` methods. Which one you use depends on the type of query index you want to drop from the cluster.

Deleting an index

```csharp
// Drop primary index
await queryIndexMgr.DropPrimaryIndexAsync(
    new DropPrimaryQueryIndexOptions()
);

// Drop secondary index
await queryIndexMgr.DropIndexAsync(
    "tenant_agent_01_users_email",
    new DropQueryIndexOptions()
);
```

## [](#view-management)View Management

Views are stored in design documents. The SDK provides convenient methods to create, retrieve, and remove design documents. To set up views, you create design documents that contain one or more view definitions, and then insert the design documents into a bucket. Each view in a design document is represented by a name and a set of MapReduce functions. The mandatory map function describes how to select and transform the data from the bucket, and the optional reduce function describes how to aggregate the results.

In the SDK, design documents are represented by the `DesignDocument` and `View` classes. All operations on design documents are performed on the `ViewIndexManager` instance:

```csharp
var cluster = await Cluster.ConnectAsync("couchbase://your-ip", "Administrator", "password");
var bucket = await cluster.BucketAsync("travel-sample");
var viewMgr = bucket.ViewIndexes;
```

The following example upserts a design document with two views:

```csharp
var views = new Dictionary<string, View>();
views.Add(
    "by_country",
    new View{ Map = "function (doc, meta) { if (doc.type == 'landmark') { emit([doc.country, doc.city], null); } }" }
);
views.Add(
    "by_activity",
    new View{ Map="function (doc, meta) { if (doc.type == 'landmark') { emit([doc.country, doc.city], null); } }",
    Reduce="_count" }
);

var designDocument = new DesignDocument { Name = "landmarks", Views = views };
await viewMgr.UpsertDesignDocumentAsync(designDocument, DesignDocumentNamespace.Development);
```

> [!WARNING]
> When you want to update an existing document with a new view (or a modification of a view’s definition), you can use the `UpsertDesignDocumentAsync` method.
> 
> However, this method needs the list of views in the document to be exhaustive, meaning that if you just create the new view definition as previously and add it to a new design document that you upsert, all your other views will be erased!
> 
> The solution is to perform a `GetDesignDocumentAsync`, add your view definition to the DesignDocument’s views list, then upsert it. This also works with view modifications, provided the change is in the `map` or `reduce` functions (just reuse the same name for the modified view), or for deletion of one out of several views in the document.

Note the use of `DesignDocumentNamespace.Development`, the other option is `DesignDocumentNamespace.Production`. This parameter specifies whether the design document should be created as development, or as production — with the former running over only a small fraction of the documents.

Now that we’ve created a design document we can fetch it:

```csharp
var designDocument = await viewMgr.GetDesignDocumentAsync("landmarks", DesignDocumentNamespace.Development);
Console.WriteLine($"Design Document: {designDocument.Name}");
```

We’ve created the design document using `DesignDocumentNamespace.Development` and now want to push it to production, we can do this with:

```csharp
await viewMgr.PublishDesignDocumentAsync("landmarks");
```

To remove this design document:

```csharp
await viewMgr.DropDesignDocumentAsync("landmarks", DesignDocumentNamespace.Production);
```