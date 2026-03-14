---
title: Provisioning Cluster Resources
description: Provisioning cluster resources is managed at the collection or
  bucket level, depending upon the service affected.
editUrl: https://github.com/couchbase/docs-sdk-rust/edit/release/1.0/modules/howtos/pages/provisioning-cluster-resources.adoc
pubDate: 2026-03-14T03:37:27.095Z
link: xref:rust-sdk:howtos:provisioning-cluster-resources.adoc[]
---

[View original HTML](/rust-sdk/current/howtos/provisioning-cluster-resources.html)

# Provisioning Cluster Resources

> Provisioning cluster resources is managed at the collection or bucket level, depending upon the service affected. Common use cases are outlined here, less common use cases are covered in the [API docs](https://docs.couchbase.com/sdk-api/couchbase-rust-client/). 

The primary means for managing clusters is through the Couchbase Web UI which provides an easy to use interface for adding, removing, monitoring and modifying buckets. In some instances you may wish to have a programmatic interface. For example, if you wish to manage a cluster from a setup script, or if you are setting up buckets in test scaffolding.

The Rust SDK also comes with some convenience functionality for common Couchbase management requests.

> [!TIP]
> Managing Capella Clusters
> 
> This part of the SDK API predates the Capella Management API, and is only intended to work with self-managed Couchbase Server clusters.
> 
> Management of your Capella Operational cluster is available away from the Web UI with the [Capella Management API](../../../cloud/management-api-guide/management-api-intro.md).

## [](#bucket-management)Bucket Management

The `BucketManager` interface may be used to create and delete buckets from the Couchbase cluster.

`BucketSettings` is used for creating and updating buckets. `BucketSettings` is also used for exposing information about existing buckets.

> [!WARNING]
> Note that any property that is not explicitly set when building the bucket settings will use the default value. In the case of the update, this is not necessarily the currently configured value, so you should be careful to set all properties to their correct expected values when updating an existing bucket configuration.

Here is the list of parameters available for `BucketSettings`. The "Updatable" column indicates whether the parameter may only be specified when creating a bucket, or whether it may be updated after creation.

| Name                                    | Type                   | Description                                                                                                                                                                                             | Updatable                                                                                                                                                                                                                        |
| --------------------------------------- | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| name                                    | String                 | The name of the bucket, required for creation.                                                                                                                                                          | false                                                                                                                                                                                                                            |
| ram\_quota\_mb                          | u64                    | How much memory should each node use for the bucket, required for creation.                                                                                                                             | true                                                                                                                                                                                                                             |
| flush\_enabled                          | bool                   | Enables flushing to be performed on this bucket (see the [Flushing Buckets](#flushing-buckets) section below).                                                                                          | true                                                                                                                                                                                                                             |
| num\_replicas                           | u32                    | The number of replicas to use for the bucket.                                                                                                                                                           | true                                                                                                                                                                                                                             |
| evictionPolicy                          | EvictionPolicyType     | The type of the eviction to use for the bucket, defaults to ValueOnly.                                                                                                                                  | true (note: changing will cause the bucket to restart causing temporary inaccessibility)                                                                                                                                         |
| max\_expiry                             | Duration               | The default maximum time-to-live to apply to documents in the bucket. (note: This option is only available for Couchbase and Ephemeral buckets in Couchbase Enterprise Edition.)                        | true                                                                                                                                                                                                                             |
| compressionMode                         | CompressionMode        | The compression mode to apply to documents in the bucket. (note: This option is only available for Couchbase and Ephemeral buckets in Couchbase Enterprise Edition.)                                    | true                                                                                                                                                                                                                             |
| minimum\_durability\_level              | DurabilityLevel        | The durability level to be assigned to the bucket.                                                                                                                                                      | true                                                                                                                                                                                                                             |
| conflictResolutionType                  | ConflictResolutionType | The conflict resolution type to apply to conflicts on the bucket, defaults to SequenceNumber                                                                                                            | false                                                                                                                                                                                                                            |
| replica\_indexes                        | bool                   | Whether or not to replicate indexes.                                                                                                                                                                    | false                                                                                                                                                                                                                            |
| bucket\_type                            | BucketType             | The type of the bucket, required for creation.                                                                                                                                                          | false                                                                                                                                                                                                                            |
| storage\_backend                        | StorageBackend         | The storage backend to be assigned to and used by the bucket.                                                                                                                                           | true (note: additional steps required to migrate a bucket’s storage backend. See [Migrate a Bucket’s Storage Backend](https://docs.couchbase.com/server/current/manage/manage-buckets/migrate-bucket.html) for more information) |
| num\_vbuckets                           | u16                    | The number of vBuckets for this bucket.                                                                                                                                                                 | false                                                                                                                                                                                                                            |
| history\_retention\_collection\_default | bool                   | Whether a change history is made for the bucket. This parameter is ignored unless the storageBackend is set to magma.                                                                                   | true                                                                                                                                                                                                                             |
| history\_retention\_collection\_fault   | bool                   | Whether a change history is made for the bucket. This parameter is ignored unless the storageBackend is set to magma.                                                                                   | true                                                                                                                                                                                                                             |
| history\_retention\_bytes               | u64                    | Specifies the maximum size, in bytes, of the change history that is written to disk for all collections in this bucket when the value of history\_retention\_collection\_fault is true.                 | true                                                                                                                                                                                                                             |
| history\_retention\_duration            | Duration               | Specifies the maximum number of seconds to be covered by the change history that is written to disk for all collections in this bucket when the value of history\_retention\_collection\_fault is true. | true                                                                                                                                                                                                                             |

The following example creates a "hello" bucket:

```rust
let bucket_manager = cluster.buckets();

let bucket = BucketSettings::new("hello")
    .flush_enabled(false)
    .replica_indexes(false)
    .num_replicas(1)
    .bucket_type(BucketType::COUCHBASE)
    .conflict_resolution_type(ConflictResolutionType::SEQUENCE_NUMBER);

match bucket_manager.create_bucket(bucket, None).await {
    Ok(_) => println!("Bucket created successfully"),
    Err(e) => println!("Error: {e}"),
}
```

We can now get this bucket and update it to enable Flush:

```rust
match bucket_manager.get_bucket("hello", None).await {
    Ok(bucket) => {
        let bucket = bucket.flush_enabled(true);
        match bucket_manager.update_bucket(bucket, None).await {
            Ok(_) => println!("Bucket updated successfully"),
            Err(e) => println!("Error: {e}"),
        }
    }
    Err(e) => println!("Error: {e}"),
}
match bucket_manager.flush_bucket("hello", None).await {
    Ok(_) => println!("Bucket flushed successfully"),
    Err(e) => match e.kind() {
        couchbase::error::ErrorKind::BucketNotFlushable => {
            println!("Flushing is not enabled on this bucket")
        }
        _ => {
            println!("Error: {e}")
        }
    },
}
```

Once you no longer need to use the bucket, you can remove it:

```rust
match bucket_manager.drop_bucket("hello", None).await {
    Ok(_) => println!("Bucket dropped successfully"),
    Err(e) => println!("Error: {e}"),
}
```

### [](#flushing-buckets)Flushing Buckets

When a bucket is flushed, all content is removed. Because this operation is potentially dangerous it is disabled by default for each bucket. Bucket flushing may be useful in test environments where it becomes a simpler alternative to removing and creating a test bucket. You may enable bucket flushing on a per-bucket basis using the Couchbase Web Console or when creating a bucket.

You can flush a bucket in the SDK by using the `Flush` method:

```rust
match bucket_manager.get_bucket("hello", None).await {
    Ok(bucket) => {
        let bucket = bucket.flush_enabled(true);
        match bucket_manager.update_bucket(bucket, None).await {
            Ok(_) => println!("Bucket updated successfully"),
            Err(e) => println!("Error: {e}"),
        }
    }
    Err(e) => println!("Error: {e}"),
}
match bucket_manager.flush_bucket("hello", None).await {
    Ok(_) => println!("Bucket flushed successfully"),
    Err(e) => match e.kind() {
        couchbase::error::ErrorKind::BucketNotFlushable => {
            println!("Flushing is not enabled on this bucket")
        }
        _ => {
            println!("Error: {e}")
        }
    },
}
```

## [](#collection-management)Collection Management

The CollectionManager interface may be used to create and delete scopes and collections from the Couchbase cluster. It is instantiated through the `Bucket.collections()` method.

```rust
let collection_manager = bucket.collections();
```

You can create a scope:

```rust
match collection_manager.create_scope("my_scope", None).await {
    Ok(_) => println!("Scope created successfully"),
    Err(e) => match e.kind() {
        couchbase::error::ErrorKind::ScopeExists => {
            println!("Scope already exists");
        }
        _ => {
            println!("Error: {e}");
        }
    },
}
```

You can then create a collection within that scope:

```rust
let settings = CreateCollectionSettings::new()
    .max_expiry(MaxExpiryValue::InheritFromBucket)
    .history(false);

match collection_manager
    .create_collection("example-scope", "example_collection", settings, None)
    .await
{
    Ok(_) => println!("Collection created successfully"),
    Err(e) => match e.kind() {
        couchbase::error::ErrorKind::ScopeNotFound => {
            println!("Scope does not exist");
        }
        couchbase::error::ErrorKind::CollectionExists => {
            println!("Collection already exists");
        }
        _ => {
            println!("Error: {e}");
        }
    },
}
```

Finally, you can drop unneeded collections and scopes:

```rust
match collection_manager
    .drop_collection("example-scope", "example-collection", None)
    .await
{
    Ok(_) => println!("Collection dropped successfully"),
    Err(e) => match e.kind() {
        couchbase::error::ErrorKind::ScopeNotFound => {
            println!("Scope not found");
        }
        couchbase::error::ErrorKind::CollectionNotFound => {
            println!("Collection not found");
        }
        _ => {
            println!("Error: {e}");
        }
    },
}

[data-source-url=https://github.com/couchbase/docs-sdk-rust/blob/1fadb8abb6ef0c493ffce043e89ec74daea6c58e/modules/devguide/examples/src/cluster_resources.rs#L128-L138]
match collection_manager.drop_scope("example-scope", None).await {
    Ok(_) => println!("Scope dropped successfully"),
    Err(e) => match e.kind() {
        couchbase::error::ErrorKind::ScopeNotFound => {
            println!("Scope not found");
        }
        _ => {
            println!("Error: {e}");
        }
    },
}
```

Note that the most minimal permissions to create and drop a Scope or Collection is [Manage Scopes](../../../server/current/learn/security/roles.md#manage-scopes)along with [Data Reader](../../../server/current/learn/security/roles.md#data-reader).

You can create users with the appropriate RBAC programmatically:

```rust
let user_manager = cluster.users();
let user = User::new(
    "scope-admin",
    "display-name",
    vec![
        Role::new("scope_admin").bucket("travel-sample"),
        Role::new("data_reader").bucket("travel-sample"),
    ],
);
match user_manager
    .upsert_user(user.password("password"), None)
    .await
{
    Ok(_) => println!("User created successfully"),
    Err(e) => println!("Error: {e}"),
}
```

## [](#index-management)Index Management

In general, you will rarely need to work with Index Managers from the SDK.

For those occasions when you do, you will find some of these described in the following section.

### [](#queryindexmanager)QueryIndexManager

The `QueryIndexManager` interface contains the means for managing indexes used for queries.  
It can be accessed via `Collection.query_indexes()`.

```rust
let collection = cluster
    .bucket("travel-sample")
    .scope("tenant_agent_01")
    .collection("users");
let query_index_manager = collection.query_indexes();
```

Applications can use this manager to perform operations such as creating, deleting, and fetching _primary_ or _secondary_ indexes:

* A _Primary_ index is built from a document’s key and is mostly suited for simple queries.
* A _Secondary_ index is the most commonly used type, and is suited for complex queries that require filtering on document fields.

> [!NOTE]
> To perform query index operations, the provided user must either be an _Admin_ or assigned the _Query Manage Index_ role. See the [Roles](../../../server/current/learn/security/roles.md#query-manage-index) page for more information.

The example below shows how to create a simple primary index on the collection, by calling the `create_primary_index()` method.

Creating a primary index

```rust
match query_index_manager
    .create_primary_index(
        CreatePrimaryQueryIndexOptions::new()
            .index_name("custom_name")
            .ignore_if_exists(true),
    )
    .await
{
    Ok(_) => println!("Primary index created successfully"),
    Err(e) => println!("Error: {e}"),
}
```

When a primary index name is not specified, the SDK will create the index as `#primary` by default. However, if you wish to provide a custom name, you can simply pass an `indexName` argument to `CreatePrimaryIndexOptions`.

You may have noticed that the example also sets the `ignoreIfExists` boolean flag. When set to `true`, this optional argument ensures that an error is not thrown if an index under the same name already exists.

Creating a _secondary_ index follows a similar approach, with some minor differences:

Creating a secondary index

```rust
match query_index_manager
    .create_index("tenant_agent_01_users_email", vec!["preferred_email".to_string()], None)
    .await
{
    Ok(_) => println!("Secondary index created successfully"),
    Err(e) => match e.kind() {
        couchbase::error::ErrorKind::IndexExists => {
            println!("Index already exists");
        }
        _ => {
            println!("Error: {e}");
        }
    },
}
```

The `create_index()` method requires an index name to be provided, along with the fields to create the index on.

Indexes can easily take a long time to build if they contain a lot of documents. In these situations, it is more ideal to build indexes in the background. To achieve this we can use the `deferred` boolean option, and set it to `true`.

Deferring index creation

```rust
match query_index_manager
    .create_index(
        "tenant_agent_01_users_email",
        vec!["preferred_email".to_string()],
        CreateQueryIndexOptions::new().deferred(true),
    )
    .await
{
    Ok(_) => println!("Secondary index created successfully"),
    Err(e) => match e.kind() {
        couchbase::error::ErrorKind::IndexExists => {
            println!("Index already exists");
        }
        _ => {
            println!("Error: {e}");
        }
    },
}

match query_index_manager.build_deferred_indexes(None).await {
    Ok(_) => println!("Deferred indexes are being built"),
    Err(e) => println!("Error: {e}"),
}

match query_index_manager
    .watch_indexes(vec!["tenant_agent_01_users_phone".to_string()], None)
    .await
{
    Ok(_) => println!("All watched indexes are online"),
    Err(e) => println!("Error: {e}"),
}
```

To delete a query index you can use the `drop_index()` or `drop_primary_index()` methods. Which one you use depends on the type of query index you wish to drop from the cluster.

Deleting an index

```rust
match query_index_manager.drop_primary_index(None).await {
    Ok(_) => println!("Primary index dropped successfully"),
    Err(e) => println!("Error: {e}"),
}

match query_index_manager
    .drop_index("tenant_agent_01_users_email", None)
    .await
{
    Ok(_) => println!("Secondary index dropped successfully"),
    Err(e) => println!("Error: {e}"),
}
```