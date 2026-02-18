---
title: Provisioning Cluster Resources
description: Provisioning cluster resources is managed at the collection or
  bucket level, depending upon the service affected.
editUrl: https://github.com/couchbase/docs-sdk-nodejs/edit/temp/4.4/modules/howtos/pages/provisioning-cluster-resources.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/nodejs-sdk/4.4/howtos/provisioning-cluster-resources.html)

# Provisioning Cluster Resources

> Provisioning cluster resources is managed at the collection or bucket level, depending upon the service affected. Common use cases are outlined here, less common use cases are covered in the [API docs](https://docs.couchbase.com/sdk-api/couchbase-node-client/). 

The primary means for managing clusters is through the Couchbase Web UI which provides an easy to use interface for adding, removing, monitoring and modifying buckets. In some instances you may wish to have a programmatic interface. For example, if you wish to manage a cluster from a setup script, or if you are setting up buckets in test scaffolding.

The Node.js SDK also comes with some convenience functionality for common Couchbase management requests.

Management operations in the SDK may be performed through several interfaces depending on the object:

* BucketManager — [Cluster.buckets()](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/Cluster.html#buckets)
* UserManager — [Cluster.users()](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/Cluster.html#users)
* QueryIndexManager — [Cluster.queryIndexes()](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/Cluster.html#queryIndexes)
* AnalyticsIndexManager — [Cluster.analyticsIndexes()](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/Cluster.html#analyticsIndexes)
* SearchIndexManager — [Cluster.searchIndexes()](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/Cluster.html#searchIndexes)
* CollectionManager — [Bucket.collections()](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/Bucket.html#collections)
* ViewIndexManager — [Bucket.viewIndexes()](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/Bucket.html#viewIndexes)

> [!NOTE]
> When using a Couchbase version earlier than 6.5, you must create a valid Bucket connection using `cluster.bucket(name)` before you can use cluster level managers.

## [](#bucket-management)Bucket Management

The `BucketManager` interface may be used to create and delete buckets from the Couchbase cluster. It is instantiated through the `Cluster.buckets()` method.

```javascript
const bucketMgr = cluster.buckets()
```

The `CreateBucketSettings` and `BucketSettings` structs are used for creating and updating buckets, `BucketSettings` is also used for exposing information about existing buckets.

> [!WARNING]
> Note that any property that is not explicitly set when building the bucket settings will use the default value. In the case of the update, this is not necessarily the currently configured value, so you should be careful to set all properties to their correct expected values when updating an existing bucket configuration.

Here is the list of parameters available:

| Name                              | Description                                                                                                                                                                      | Can be updated                                                                           |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| name string                       | The name of the bucket, required for creation.                                                                                                                                   | false                                                                                    |
| flushEnabled boolean              | Enables flushing to be performed on this bucket (see the [Flushing Buckets](#flushing-buckets) section below).                                                                   | true                                                                                     |
| replicaIndex boolean              | Whether or not to replicate indexes.                                                                                                                                             | false                                                                                    |
| ramQuotaMB uint64                 | How much memory should each node use for the bucket, required for creation.                                                                                                      | true                                                                                     |
| numReplicas uint32                | The number of replicas to use for the bucket.                                                                                                                                    | true                                                                                     |
| bucketType BucketType             | The type of the bucket, required for creation.                                                                                                                                   | false                                                                                    |
| evictionPolicy EvictionPolicyType | The type of the eviction to use for the bucket, defaults to valueOnly.                                                                                                           | true (note: changing will cause the bucket to restart causing temporary inaccessibility) |
| maxTTL time.Duration              | The default maximum time-to-live to apply to documents in the bucket. (note: This option is only available for Couchbase and Ephemeral buckets in Couchbase Enterprise Edition.) | true                                                                                     |
| compressionMode CompressionMode   | The compression mode to apply to documents in the bucket. (note: This option is only available for Couchbase and Ephemeral buckets in Couchbase Enterprise Edition.)             | true                                                                                     |

The following example creates a "hello" bucket:

```javascript
await bucketMgr.createBucket({
  name: 'hello',
  flushEnabled: false,
  replicaIndex: false,
  ramQuotaMB: 200,
  numReplicas: 1,
  bucketType: couchbase.BucketType.Couchbase,
})
```

We can now get this bucket and update it to enable flush:

```javascript
var settings = await bucketMgr.getBucket('hello')
settings.flushEnabled = true

await bucketMgr.updateBucket(settings)
```

Once you no longer need to use the bucket, you can remove it:

```javascript
await bucketMgr.dropBucket('hello')
```

### [](#flushing-buckets)Flushing Buckets

When a bucket is flushed, all content is removed. Because this operation is potentially dangerous it is disabled by default for each bucket. Bucket flushing may be useful in test environments where it becomes a simpler alternative to removing and creating a test bucket. You may enable bucket flushing on a per-bucket basis using the Couchbase Web Console or when creating a bucket.

You can flush a bucket in the SDK by using the `flush` method:

```javascript
await bucketMgr.flushBucket('hello')
```

The `flush` operation may fail if the bucket does not have flush enabled, in that case it will return an error.

## [](#collection-management)Collection Management

The [CollectionManager](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/CollectionManager.html) interface may be used to create and delete scopes from the Couchbase cluster. It is instantiated through the `Bucket.collections()` method.

```javascript
const bucket = cluster.bucket('travel-sample')
const collectionMgr = bucket.collections()
```

You can create a scope:

```javascript
try {
  await collectionMgr.createScope('example-scope')
} catch (e) {
  if (e instanceof couchbase.ScopeExistsError) {
    console.log('The scope already exists')
  } else {
    throw e
  }
}
```

You can then create a collection within that scope:

```javascript
try {
  var collectionSpec = new couchbase.CollectionSpec({
    name: 'example-collection',
    scopeName: 'example-scope',
  })

  await collectionMgr.createCollection(collectionSpec)
} catch (e) {
  if (e instanceof couchbase.CollectionExistsError) {
    console.log('The collection already exists')
  } else if (e instanceof couchbase.ScopeNotFoundError) {
    console.log('The scope does not exist')
  } else {
    throw e
  }
}
```

Finally, you can drop unneeded collections and scopes:

```javascript
try {
  await collectionMgr.dropCollection('example-collection', 'example-scope')
} catch (e) {
  if (e instanceof couchbase.CollectionNotFoundError) {
    console.log('The collection does not exist')
  } else if (e instanceof couchbase.ScopeNotFoundError) {
    console.log('The scope does not exist')
  } else {
    throw e
  }
}

try {
  await collectionMgr.dropScope('example-scope')
} catch (e) {
  if (e instanceof couchbase.ScopeNotFoundError) {
    console.log('The scope does not exist')
  } else {
    throw e
  }
}
```

Note that the most minimal permissions to create and drop a Scope or Collection is [Manage Scopes](../../../server/current/learn/security/roles.md#manage-scopes)along with [Data Reader](../../../server/current/learn/security/roles.md#data-reader)

You can create users with the appropriate RBAC programmatically:

```javascript
const userMgr = clusterAdm.users()
const bucketAdm = clusterAdm.bucket('travel-sample')

await userMgr.upsertUser({
  username: 'scope_admin',
  password: 'password',
  displayName: 'JS Manage Scopes [travel-sample:*]',
  roles: [
    { name: 'scope_admin', bucket: 'travel-sample' },
    { name: 'data_reader', bucket: 'travel-sample' },
  ],
})
```

## [](#index-management)Index Management

In general, you will rarely need to work with Index Managers from the SDK. For those occasions when you do, index management operations can be performed with the following interfaces:

* QueryIndexManager — [Cluster.queryIndexes()](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/Cluster.html#queryIndexes)
* AnalyticsIndexManager — [Cluster.analyticsIndexes()](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/Cluster.html#analyticsIndexes)
* SearchIndexManager — [Cluster.searchIndexes()](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/Cluster.html#searchIndexes)
* ViewIndexManager — [Bucket.viewIndexes()](https://docs.couchbase.com/sdk-api/couchbase-node-client/classes/Bucket.html#viewIndexes)

You will find some of these described in the following section.

### [](#queryindexmanager)QueryIndexManager

The `QueryIndexManager` interface contains the means for managing indexes used for queries. It can be instantiated through the `Cluster.queryIndexes()` method.

```javascript
const cluster = await couchbase.connect('couchbase://localhost', {
  username: 'Administrator',
  password: 'password',
})
const queryIndexMgr = cluster.queryIndexes()
```

Applications can use this manager to perform operations such as creating, deleting, and fetching _primary_ or _secondary_ indexes:

* A _Primary_ index is built from a document’s key and is mostly suited for simple queries.
* A _Secondary_ index is the most commonly used type, and is suited for complex queries that require filtering on document fields.

> [!NOTE]
> To perform query index operations, the provided user must either be an _Admin_ or assigned the _Query Manage Index_ role. See the [Roles](../../../server/current/learn/security/roles.md#query-manage-index) page for more information.

The example below shows how to create a simple primary index, restricted to a named scope and collection, by calling the `createPrimaryIndex()` method. Note that you cannot provide a named scope or collection separately, both must be set for the `QueryIndexManager` to create an index on the relevant keyspace path.

Creating a primary index

```javascript
await queryIndexMgr.createPrimaryIndex('travel-sample', {
  scopeName: 'tenant_agent_01',
  collectionName: 'users',
  // Set this is you wish to use a custom name
  // indexName: 'custom_name',
  ignoreIfExists: true,
})
```

When a primary index name is not specified, the SDK will create the index as `#primary` by default. However, if you wish to provide a custom name, you can simply set an `indexName` property in the `CreatePrimaryQueryIndexOptions` class.

You may have noticed that the example also sets the `ignoreIfExists` boolean flag. When set to `true`, this optional argument ensures that an error is not thrown if an index under the same name already exists.

Creating a _secondary_ index follows a similar approach, with some minor differences:

Creating a secondary index

```javascript
try {
  await queryIndexMgr.createIndex(
    'travel-sample',
    'tenant_agent_01_users_email',
    ['preferred_email'],
    { scopeName: 'tenant_agent_01', collectionName: 'users' }
  )
} catch (IndexExistsError) {
  console.info('Index already exists')
}
```

The `createIndex()` method requires an index name to be provided, along with the fields to create the index on. Like the _primary_ index, you can restrict a _secondary_ index to a named scope and collection by passing some options.

Indexes can easily take a long time to build if they contain a lot of documents. In these situations, it is more ideal to build indexes in the background. To achieve this we can use the `deferred` boolean option, and set it to `true`.

Deferring index creation

```javascript
try {
  // Create a deferred index
  await queryIndexMgr.createIndex(
    'travel-sample',
    'tenant_agent_01_users_phone',
    ['preferred_phone'],
    { scopeName: 'tenant_agent_01', collectionName: 'users', deferred: true }
  )

  // Build any deferred indexes within `travel-sample`.tenant_agent_01.users
  await queryIndexMgr.buildDeferredIndexes('travel-sample', {
    scopeName: 'tenant_agent_01',
    collectionName: 'users',
  })

  // Wait for indexes to come online
  await queryIndexMgr.watchIndexes(
    'travel-sample',
    ['tenant_agent_01_users_phone'],
    30000, // milliseconds
    { scopeName: 'tenant_agent_01', collectionName: 'users' }
  )
} catch (IndexExistsError) {
  console.info('Index already exists')
}
```

To delete a query index you can use the `dropIndex()` or `dropPrimaryIndex()` methods. Which one you use depends on the type of query index you wish to drop from the cluster.

Deleting an index

```javascript
// Drop a primary index
await queryIndexMgr.dropPrimaryIndex('travel-sample', {
  scopeName: 'tenant_agent_01',
  collectionName: 'users',
})

// Drop a secondary index
await queryIndexMgr.dropIndex(
  'travel-sample',
  'tenant_agent_01_users_email',
  { scopeName: 'tenant_agent_01', collectionName: 'users' }
)
```

## [](#views-management)Views Management

Views are stored in design documents. The SDK provides convenient methods to create, retrieve, and remove design documents. To set up views, you create design documents that contain one or more view definitions, and then insert the design documents into a bucket. Each view in a design document is represented by a name and a set of MapReduce functions. The mandatory map function describes how to select and transform the data from the bucket, and the optional reduce function describes how to aggregate the results.

In the SDK, design documents are represented by the `DesignDocument` and `View` classes. All operations on design documents are performed on the `ViewIndexManager` instance:

```javascript
  const cluster = await couchbase.connect('couchbase://localhost', {
    username: 'Administrator',
    password: 'password',
  })
  const bucket = cluster.bucket('travel-sample')

  const viewMgr = bucket.viewIndexes()
```

The following example upserts a design document with two views:

```javascript
  let designDoc = new DesignDocument({
    name: 'dev_landmarks',
    views: {
      by_country: {
        map: "function (doc, meta) { if (doc.type == 'landmark') { emit([doc.country, doc.city], null); } }",
      },
      by_activity: {
        map: "function (doc, meta) { if (doc.type == 'landmark') { emit(doc.activity, null); } }",
        reduce: '_count',
      },
    },
  })

  await viewMgr.upsertDesignDocument(designDoc)
```

> [!WARNING]
> When you want to update an existing document with a new view (or a modification of a view’s definition), you can use the `upsertDesignDocument` method.
> 
> However, this method needs the list of views in the document to be exhaustive, meaning that if you just create the new view definition as previously and add it to a new design document that you upsert, all your other views will be erased!
> 
> The solution is to perform a `getDesignDocument`, add your view definition to the DesignDocument’s views list, then upsert it. This also works with view modifications, provided the change is in the `map` or `reduce` functions (just reuse the same name for the modified view), or for deletion of one out of several views in the document.

Note the use of `dev_` in the design document name. This specifies whether the design document should be created as development, or as production — with the former running over only a small fraction of the documents.

Now that we’ve created a design document we can fetch it:

```javascript
  designDoc = await viewMgr.getDesignDocument('dev_landmarks')
  console.info(
    'Found design doc:',
    designDoc.name,
    Object.keys(designDoc.views).length
  )
```

We’ve created the design document using `dev_` and now want to push it to production, we can do this with:

```javascript
  await viewMgr.publishDesignDocument('landmarks')
```

To remove this design document:

```javascript
  await viewMgr.dropDesignDocument('landmarks')
```