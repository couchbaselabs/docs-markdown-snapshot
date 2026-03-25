---
title: Provisioning Cluster Resources
description: Provisioning cluster resources is managed at the collection or
  bucket level, depending upon the service affected.
editUrl: https://github.com/couchbase/docs-sdk-go/edit/release/2.12/modules/howtos/pages/provisioning-cluster-resources.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:go-sdk:howtos:provisioning-cluster-resources.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/go-sdk/current/howtos/provisioning-cluster-resources.html)

# Provisioning Cluster Resources

> Provisioning cluster resources is managed at the collection or bucket level, depending upon the service affected. Common use cases are outlined here, less common use cases are covered in the [API docs](https://pkg.go.dev/github.com/couchbase/gocb/v2?tab=doc). 

The primary means for managing clusters is through the Couchbase Web UI which provides an easy to use interface for adding, removing, monitoring and modifying buckets. In some instances you may wish to have a programmatic interface. For example, if you wish to manage a cluster from a setup script, or if you are setting up buckets in test scaffolding.

The Go SDK also comes with some convenience functionality for common Couchbase management requests.

> [!TIP]
> Managing Capella Clusters
> 
> This part of the SDK API predates the Capella Management API, and is only intended to work with self-managed Couchbase Server clusters.
> 
> Management of your Capella Operational cluster is available away from the Web UI with the [Capella Management API](../../../cloud/management-api-guide/management-api-intro.md).

Management operations in the SDK may be performed through several interfaces depending on the object:

* BucketManager — [Cluster.Buckets()](https://pkg.go.dev/github.com/couchbase/gocb/v2?tab=doc#Cluster.Buckets)
* UserManager — [Cluster.Users()](https://pkg.go.dev/github.com/couchbase/gocb/v2?tab=doc#Cluster.Users)
* QueryIndexManager — [Cluster.QueryIndexes()](https://pkg.go.dev/github.com/couchbase/gocb/v2?tab=doc#Cluster.QueryIndexes)
* AnalyticsIndexManager — [Cluster.AnalyticsIndexes()](https://pkg.go.dev/github.com/couchbase/gocb/v2?tab=doc#Cluster.AnalyticsIndexes)
* SearchIndexManager — [Cluster.SearchIndexes()](https://pkg.go.dev/github.com/couchbase/gocb/v2?tab=doc#Cluster.SearchIndexes)
* CollectionManager — [Bucket.Collections()](https://pkg.go.dev/github.com/couchbase/gocb/v2?tab=doc#Bucket.Collections)
* ViewIndexManager — [Bucket.ViewIndexes()](https://pkg.go.dev/github.com/couchbase/gocb/v2?tab=doc#Bucket.ViewIndexes)

> [!NOTE]
> When using a Couchbase version earlier than 6.5, you must create a valid Bucket connection using `cluster.Bucket(name)` before you can use cluster level managers.

## [](#bucket-management)Bucket Management

The `BucketManager` interface may be used to create and delete buckets from the Couchbase cluster. It is instantiated through the `Cluster.Buckets()` method.

```golang
	cluster, err := gocb.Connect("localhost", opts)
	if err != nil {
		panic(err)
	}

	// For Server versions 6.5 or later you do not need to open a bucket here
	b := cluster.Bucket("travel-sample")

	// We wait until the bucket is definitely connected and setup.
	// For Server versions 6.5 or later if we hadn't opened a bucket then we could use cluster.WaitUntilReady here.
	err = b.WaitUntilReady(5*time.Second, nil)
	if err != nil {
		panic(err)
	}

	bucketMgr := cluster.Buckets()
```

The `CreateBucketSettings` and `BucketSettings` structs are used for creating and updating buckets, `BucketSettings` is also used for exposing information about existing buckets.

> [!WARNING]
> Note that any property that is not explicitly set when building the bucket settings will use the default value. In the case of the update, this is not necessarily the currently configured value, so you should be careful to set all properties to their correct expected values when updating an existing bucket configuration.

Here is the list of parameters available:

| Name                                          | Description                                                                                                                                                                      | Can be updated                                                                           |
| --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| Name string                                   | The name of the bucket, required for creation.                                                                                                                                   | false                                                                                    |
| FlushEnabled boolean                          | Enables flushing to be performed on this bucket (see the [Flushing Buckets](#flushing-buckets) section below).                                                                   | true                                                                                     |
| ReplicaIndexDisabled boolean                  | Whether or not to replicate indexes.                                                                                                                                             | false                                                                                    |
| RAMQuotaMB uint64                             | How much memory should each node use for the bucket, required for creation.                                                                                                      | true                                                                                     |
| NumReplicas uint32                            | The number of replicas to use for the bucket.                                                                                                                                    | true                                                                                     |
| BucketType BucketType                         | The type of the bucket, required for creation.                                                                                                                                   | false                                                                                    |
| EvictionPolicy EvictionPolicyType             | The type of the eviction to use for the bucket, defaults to valueOnly.                                                                                                           | true (note: changing will cause the bucket to restart causing temporary inaccessibility) |
| MaxTTL time.Duration                          | The default maximum time-to-live to apply to documents in the bucket. (note: This option is only available for Couchbase and Ephemeral buckets in Couchbase Enterprise Edition.) | true                                                                                     |
| CompressionMode CompressionMode               | The compression mode to apply to documents in the bucket. (note: This option is only available for Couchbase and Ephemeral buckets in Couchbase Enterprise Edition.)             | true                                                                                     |
| ConflictResolutionType ConflictResolutionType | The conflict resolution type to apply to conflicts on the bucket, defaults to seqno                                                                                              | false                                                                                    |

The following example creates a "hello" bucket:

```golang
	err := bucketMgr.CreateBucket(gocb.CreateBucketSettings{
		BucketSettings: gocb.BucketSettings{
			Name:                 "hello",
			FlushEnabled:         false,
			ReplicaIndexDisabled: true,
			RAMQuotaMB:           150,
			NumReplicas:          1,
			BucketType:           gocb.CouchbaseBucketType,
		},
		ConflictResolutionType: gocb.ConflictResolutionTypeSequenceNumber,
	}, nil)
	if err != nil {
		panic(err)
	}
```

We can now get this bucket and update it to enable Flush:

```golang
	settings, err := bucketMgr.GetBucket("hello", nil)
	if err != nil {
		panic(err)
	}

	settings.FlushEnabled = true
	err = bucketMgr.UpdateBucket(*settings, nil)
	if err != nil {
		panic(err)
	}
```

Once you no longer need to use the bucket, you can remove it:

```golang
	err := bucketMgr.DropBucket("hello", nil)
	if err != nil {
		panic(err)
	}
```

### [](#flushing-buckets)Flushing Buckets

When a bucket is flushed, all content is removed. Because this operation is potentially dangerous it is disabled by default for each bucket. Bucket flushing may be useful in test environments where it becomes a simpler alternative to removing and creating a test bucket. You may enable bucket flushing on a per-bucket basis using the Couchbase Web Console or when creating a bucket.

You can flush a bucket in the SDK by using the `Flush` method:

```golang
	err := bucketMgr.FlushBucket("hello", nil)
	if err != nil {
		panic(err)
	}
```

The `Flush` operation may fail if the bucket does not have flush enabled, in that case it will return an `ErrBucketNotFlushable`.

## [](#collection-management)Collection Management

The `CollectionManager` interface may be used to create and delete scopes and collections from the Couchbase cluster. It is instantiated through the `Bucket.Collections()` method. Refer to the [CollectionManager API documentation](https://pkg.go.dev/github.com/couchbase/gocb/v2?tab=doc#Bucket.Collections)for further details.

```golang
opts := gocb.ClusterOptions{
	Authenticator: gocb.PasswordAuthenticator{
		Username: "scope_admin",
		Password: "password",
	},
}
cluster, err := gocb.Connect("localhost", opts)
if err != nil {
	panic(err)
}

bucket := cluster.Bucket("travel-sample")
collections := bucket.CollectionsV2()
```

You can create a scope:

```golang
err = collections.CreateScope("example-scope", nil)
if err != nil {
	if errors.Is(err, gocb.ErrScopeExists) {
		fmt.Println("Scope already exists")
	} else {
		panic(err)
	}
}
```

You can then create a collection within that scope:

```golang
err = collections.CreateCollection("example-scope", "example-collection", nil, nil)
if err != nil {
	if errors.Is(err, gocb.ErrCollectionExists) {
		fmt.Println("Collection already exists")
	} else {
		panic(err)
	}
}
```

Finally, you can drop unneeded collections and scopes:

```golang
err = collections.DropCollection("example-scope", "example-collection", nil)
if err != nil {
	panic(err)
}

err = collections.DropScope("example-scope", nil)
if err != nil {
	panic(err)
}
```

Note that the most minimal permissions to create and drop a Scope or Collection is [Manage Scopes](../../../server/current/learn/security/roles.md#manage-scopes)along with [Data Reader](../../../server/current/learn/security/roles.md#data-reader)

You can create users with the appropriate RBAC programmatically:

```golang
user := gocb.User{
	Username:    "scope_admin",
	DisplayName: "Scope Admin [travel-sample:*]",
	Password:    "password",
	Roles: []gocb.Role{
		{
			Name:   "scope_admin",
			Bucket: "travel-sample",
		},
		{
			Name:   "data_reader",
			Bucket: "travel-sample",
		},
	}}

err = users.UpsertUser(user, nil)
if err != nil {
	panic(err)
}
```

## [](#index-management)Index Management

In general, you will rarely need to work with Index Managers from the SDK. For those occasions when you do, index management operations can be performed with the following interfaces:

* QueryIndexManager — [Cluster.QueryIndexes()](https://pkg.go.dev/github.com/couchbase/gocb/v2?tab=doc#Cluster.QueryIndexes)
* AnalyticsIndexManager — [Cluster.AnalyticsIndexes()](https://pkg.go.dev/github.com/couchbase/gocb/v2?tab=doc#Cluster.AnalyticsIndexes)
* SearchIndexManager — [Cluster.SearchIndexes()](https://pkg.go.dev/github.com/couchbase/gocb/v2?tab=doc#Cluster.SearchIndexes)
* ViewIndexManager — [Bucket.ViewIndexes()](https://pkg.go.dev/github.com/couchbase/gocb/v2?tab=doc#Bucket.ViewIndexes)

You will find some of these described in the following section.

### [](#queryindexmanager)QueryIndexManager

The `QueryIndexManager` interface contains the means for managing indexes used for queries. It can be instantiated through the `Cluster.QueryIndexes()` method.

```golang
cluster, err := gocb.Connect("localhost", gocb.ClusterOptions{
	Authenticator: gocb.PasswordAuthenticator{
		Username: "Administrator",
		Password: "password",
	},
})
if err != nil {
	panic(err)
}

if err = cluster.WaitUntilReady(5*time.Second, nil); err != nil {
	panic(err)
}

queryIndexMgr := cluster.QueryIndexes()
```

Applications can use this manager to perform operations such as creating, deleting, and fetching _primary_ or _secondary_ indexes:

* A _Primary_ index is built from a document’s key and is mostly suited for simple queries.
* A _Secondary_ index is the most commonly used type, and is suited for complex queries that require filtering on document fields.

> [!NOTE]
> To perform query index operations, the provided user must either be an _Admin_ or assigned the _Query Manage Index_ role. See the [Roles](../../../server/current/learn/security/roles.md#query-manage-index) page for more information.

The example below shows how to create a simple primary index, restricted to a named scope and collection, by calling the `CreatePrimaryIndex()` function. Note that you cannot provide a named scope or collection separately, both must be set for the `QueryIndexManager` to create an index on the relevant keyspace path.

Creating a primary index

```golang
if err := queryIndexMgr.CreatePrimaryIndex("travel-sample",
	&gocb.CreatePrimaryQueryIndexOptions{
		ScopeName:      "tenant_agent_01",
		CollectionName: "users",
		// Set this if you wish to use a custom name
		// CustomName: "custom_name",
		IgnoreIfExists: true,
	},
); err != nil {
	if errors.Is(err, gocb.ErrIndexExists) {
		fmt.Println("Index already exists")
	} else {
		panic(err)
	}
}
```

When a primary index name is not specified, the SDK will create the index as `#primary` by default. However, if you wish to provide a custom name, you can simply set a `CustomName` property in the `CreatePrimaryQueryIndexOptions` struct.

You may have noticed that the example also sets the `IgnoreIfExists` boolean flag. When set to `true`, this optional argument ensures that an error is not thrown if an index under the same name already exists.

Creating a _secondary_ index follows a similar approach, with some minor differences:

Creating a secondary index

```golang
if err := queryIndexMgr.CreateIndex("travel-sample", "tenant_agent_01_users_email", []string{"preferred_email"},
	&gocb.CreateQueryIndexOptions{
		ScopeName:      "tenant_agent_01",
		CollectionName: "users",
	},
); err != nil {
	if errors.Is(err, gocb.ErrIndexExists) {
		fmt.Println("Index already exists")
	} else {
		panic(err)
	}
}
```

The `CreateIndex()` function requires an index name to be provided, along with the fields to create the index on. Like the _primary_ index, you can restrict a _secondary_ index to a named scope and collection by passing some options.

Indexes can easily take a long time to build if they contain a lot of documents. In these situations, it is more ideal to build indexes in the background. To achieve this we can use the `Deferred` boolean option, and set it to `true`.

Deferring index creation

```golang
// Create a deferred index
if err := queryIndexMgr.CreateIndex("travel-sample", "tenant_agent_01_users_phone", []string{"preferred_phone"},
	&gocb.CreateQueryIndexOptions{
		ScopeName:      "tenant_agent_01",
		CollectionName: "users",
		Deferred:       true,
	},
); err != nil {
	if errors.Is(err, gocb.ErrIndexExists) {
		fmt.Println("Index already exists")
	} else {
		panic(err)
	}
}

// Build any deferred indexes within `travel-sample`.tenant_agent_01.users
indexesToBuild, err := queryIndexMgr.BuildDeferredIndexes("travel-sample",
	&gocb.BuildDeferredQueryIndexOptions{
		ScopeName:      "tenant_agent_01",
		CollectionName: "users",
	},
)
if err != nil {
	panic(err)
}

// Wait for indexes to come online
if err = queryIndexMgr.WatchIndexes("travel-sample", indexesToBuild, time.Duration(30*time.Second),
	&gocb.WatchQueryIndexOptions{
		ScopeName:      "tenant_agent_01",
		CollectionName: "users",
	},
); err != nil {
	panic(err)
}
```

To delete a query index you can use the `DropIndex()` or `DropPrimaryIndex()` functions. Which one you use depends on the type of query index you wish to drop from the cluster.

Deleting an index

```golang
// Drop a primary index
if err := queryIndexMgr.DropPrimaryIndex("travel-sample",
	&gocb.DropPrimaryQueryIndexOptions{
		ScopeName:      "tenant_agent_01",
		CollectionName: "users",
	},
); err != nil {
	panic(err)
}

// Drop a secondary index
if err := queryIndexMgr.DropIndex("travel-sample", "tenant_agent_01_users_email",
	&gocb.DropQueryIndexOptions{
		ScopeName:      "tenant_agent_01",
		CollectionName: "users",
	},
); err != nil {
	panic(err)
}
```

## [](#views-management)Views Management

Views are stored in design documents. The SDK provides convenient methods to create, retrieve, and remove design documents. To set up views, you create design documents that contain one or more view definitions, and then insert the design documents into a bucket. Each view in a design document is represented by a name and a set of MapReduce functions. The mandatory map function describes how to select and transform the data from the bucket, and the optional reduce function describes how to aggregate the results.

In the SDK, design documents are represented by the `DesignDocument` and `View` structs. All operations on design documents are performed on the `ViewIndexManager` instance:

```golang
	cluster, err := gocb.Connect("localhost", opts)
	if err != nil {
		panic(err)
	}

	// For Server versions 6.5 or later you do not need to open a bucket here
	bucket := cluster.Bucket("travel-sample")

	// We wait until the bucket is definitely connected and setup.
	// For Server versions 6.5 or later if we hadn't opened a bucket then we could use cluster.WaitUntilReady here.
	err = bucket.WaitUntilReady(5*time.Second, nil)
	if err != nil {
		panic(err)
	}

	viewMgr := bucket.ViewIndexes()
```

The following example upserts a design document with two views:

```golang
	designDoc := gocb.DesignDocument{
		Name: "landmarks",
		Views: map[string]gocb.View{
			"by_country": {
				Map:    "function (doc, meta) { if (doc.type == 'landmark') { emit([doc.country, doc.city], null); } }",
				Reduce: "",
			},
			"by_activity": {
				Map:    "function (doc, meta) { if (doc.type == 'landmark') { emit(doc.activity, null); } }",
				Reduce: "_count",
			},
		},
	}

	err := viewMgr.UpsertDesignDocument(designDoc, gocb.DesignDocumentNamespaceDevelopment, nil)
	if err != nil {
		panic(err)
	}
```

> [!WARNING]
> When you want to update an existing document with a new view (or a modification of a view’s definition), you can use the `UpsertDesignDocument` method.
> 
> However, this method needs the list of views in the document to be exhaustive, meaning that if you just create the new view definition as previously and add it to a new design document that you upsert, all your other views will be erased!
> 
> The solution is to perform a `GetDesignDocument`, add your view definition to the DesignDocument’s views list, then upsert it. This also works with view modifications, provided the change is in the `map` or `reduce` functions (just reuse the same name for the modified view), or for deletion of one out of several views in the document.

Note the use of `DesignDocumentNamespaceDevelopment`, the other option is `DesignDocumentNamespaceProduction`. This parameter specifies whether the design document should be created as development, or as production — with the former running over only a small fraction of the documents.

Now that we’ve created a design document we can fetch it:

```golang
	ddoc, err := viewMgr.GetDesignDocument("landmarks", gocb.DesignDocumentNamespaceDevelopment, nil)
	if err != nil {
		panic(err)
	}
	fmt.Println(ddoc)
```

We’ve created the design document using `DesignDocumentNamespaceDevelopment` and now want to push it to production, we can do this with:

```golang
	err := viewMgr.PublishDesignDocument("landmarks", nil)
	if err != nil {
		panic(err)
	}
```

To remove this design document:

```golang
	err := viewMgr.DropDesignDocument("landmarks", gocb.DesignDocumentNamespaceProduction, nil)
	if err != nil {
		panic(err)
	}
```