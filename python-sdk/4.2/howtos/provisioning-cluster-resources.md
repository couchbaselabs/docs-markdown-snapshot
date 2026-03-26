---
title: Provisioning Cluster Resources
description: Provisioning cluster resources is managed at the collection or
  bucket level, depending upon the service affected.
editUrl: https://github.com/couchbase/docs-sdk-python/edit/temp/4.2/modules/howtos/pages/provisioning-cluster-resources.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:4.2@python-sdk:howtos:provisioning-cluster-resources.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-sdk/4.2/howtos/provisioning-cluster-resources.html)

# Provisioning Cluster Resources

> Provisioning cluster resources is managed at the collection or bucket level, depending upon the service affected. Common use cases are outlined here, less common use cases are covered in the [API docs](https://docs.couchbase.com/sdk-api/couchbase-python-client/). 

The primary means for managing clusters is through the Couchbase Web UI which provides an easy to use interface for adding, removing, monitoring and modifying buckets. In some instances you may wish to have a programmatic interface. For example, if you wish to manage a cluster from a setup script, or if you are setting up buckets in test scaffolding.

The Python SDK also comes with some convenience functionality for common Couchbase management requests.

Management operations in the SDK may be performed through several interfaces depending on the object:

* BucketManager — [Cluster.buckets()](https://docs.couchbase.com/sdk-api/couchbase-python-client-4.0.0/couchbase%5Fapi/couchbase%5Fcore.html#couchbase.cluster.Cluster.buckets)
* UserManager — [Cluster.users()](https://docs.couchbase.com/sdk-api/couchbase-python-client-4.0.0/couchbase%5Fapi/couchbase%5Fcore.html#couchbase.cluster.Cluster.users)
* QueryIndexManager — [Cluster.query\_indexes()](https://docs.couchbase.com/sdk-api/couchbase-python-client-4.0.0/couchbase%5Fapi/couchbase%5Fcore.html#couchbase.cluster.Cluster.query%5Findexes)
* AnalyticsIndexManager — [Cluster.analytics\_ndexes()](https://docs.couchbase.com/sdk-api/couchbase-python-client-4.0.0/couchbase%5Fapi/couchbase%5Fcore.html#couchbase.cluster.Cluster.query%5Findexes)
* SearchIndexManager — [Cluster.search\_indexes()](https://docs.couchbase.com/sdk-api/couchbase-python-client-4.0.0/couchbase%5Fapi/couchbase%5Fcore.html#couchbase.cluster.Cluster.query%5Findexes)
* CollectionManager — [Bucket.collections()](https://docs.couchbase.com/sdk-api/couchbase-python-client-4.0.0/couchbase%5Fapi/couchbase%5Fcore.html#couchbase.bucket.Bucket.collections)
* ViewIndexManager — [Bucket.view\_indexes()](https://docs.couchbase.com/sdk-api/couchbase-python-client-4.0.0/couchbase%5Fapi/couchbase%5Fcore.html#couchbase.bucket.Bucket.collections)

> [!NOTE]
> When using a Couchbase version earlier than 6.5, you must create a valid Bucket connection using `Cluster.bucket(name)` before you can use cluster level managers.

## [](#bucket-management)Bucket Management

The `BucketManager` interface may be used to create and delete buckets from the Couchbase cluster. It is instantiated through the `Cluster.buckets()` method.

```python
cluster = Cluster(
    "couchbase://your-ip",
    authenticator=PasswordAuthenticator(
        "Administrator",
        "password"))
# For Server versions 6.5 or later you do not need to open a bucket here
bucket = cluster.bucket("travel-sample")
collection = bucket.default_collection()

bucket_manager = cluster.buckets()
```

The `CreateBucketSettings` and `BucketSettings` classes are used for creating and updating buckets, `BucketSettings` is also used for exposing information about existing buckets.

> [!WARNING]
> Note that any property that is not explicitly set when building the bucket settings will use the default value. In the case of the update, this is not necessarily the currently configured value, so you should be careful to set all properties to their correct expected values when updating an existing bucket configuration.

Here is the list of parameters available:

| Name                       | Type                   | Description                                                                                                                                                                      | Can be updated                                                                           |
| -------------------------- | ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| name                       | str                    | The name of the bucket, required for creation.                                                                                                                                   | false                                                                                    |
| flush\_enabled             | bool                   | Enables flushing to be performed on this bucket (see the [Flushing Buckets](#flushing-buckets) section below).                                                                   | true                                                                                     |
| replica\_index             | bool                   | Whether or not to replicate indexes.                                                                                                                                             | false                                                                                    |
| ram\_quota\_mb             | int                    | How much memory should each node use for the bucket, required for creation.                                                                                                      | true                                                                                     |
| num\_replicas              | int                    | The number of replicas to use for the bucket.                                                                                                                                    | true                                                                                     |
| bucket\_type               | BucketType             | The type of the bucket, required for creation.                                                                                                                                   | false                                                                                    |
| eviction\_policy           | EvictionPolicyType     | The type of the eviction to use for the bucket, defaults to valueOnly.                                                                                                           | true (note: changing will cause the bucket to restart causing temporary inaccessibility) |
| max\_ttl                   | timedelta              | The default maximum time-to-live to apply to documents in the bucket. (note: This option is only available for Couchbase and Ephemeral buckets in Couchbase Enterprise Edition.) | true                                                                                     |
| compression\_mode          | CompressionMode        | The compression mode to apply to documents in the bucket. (note: This option is only available for Couchbase and Ephemeral buckets in Couchbase Enterprise Edition.)             | true                                                                                     |
| conflict\_resolution\_type | ConflictResolutionType | The conflict resolution type to apply to conflicts on the bucket, defaults to seqno                                                                                              | false                                                                                    |

The following example creates a "hello" bucket:

```python
try:
    bucket_manager.create_bucket(
        CreateBucketSettings(
            name="hello",
            flush_enabled=True,
            ram_quota_mb=100,
            num_replicas=0,
            bucket_type=BucketType.COUCHBASE,
            conflict_resolution_type=ConflictResolutionType.SEQUENCE_NUMBER))
```

We can now get this bucket and update it to enable Flush:

```python
bucket = bucket_manager.get_bucket("hello")
print(f"Found bucket: {bucket.name}")

bucket_manager.update_bucket(BucketSettings(name="hello", flush_enabled=True))
```

Once you no longer need to use the bucket, you can remove it:

```python
bucket_manager.drop_bucket("hello")
```

### [](#flushing-buckets)Flushing Buckets

When a bucket is flushed, all content is removed. Because this operation is potentially dangerous it is disabled by default for each bucket. Bucket flushing may be useful in test environments where it becomes a simpler alternative to removing and creating a test bucket. You may enable bucket flushing on a per-bucket basis using the Couchbase Web Console or when creating a bucket.

You can flush a bucket in the SDK by using the [flush\_bucket() method](https://docs.couchbase.com/sdk-api/couchbase-python-client/api/couchbase.html#flushing-clearing-the-bucket).

```python
bucket_manager.flush_bucket("hello")
```

The `flush_bucket()` operation may fail if the bucket does not have flush enabled, in that case it will return an `BucketNotFlushableException`.

## [](#collection-management)Collection Management

The CollectionManager interface may be used to create and delete scopes and collections from the Couchbase cluster. It is instantiated through the `Bucket.collections()` method. Refer to the [API documentation](https://docs.couchbase.com/sdk-api/couchbase-python-client/api/couchbase.html)for further details.

```python
bucket = cluster.bucket("travel-sample")
coll_manager = bucket.collections()
```

You can create a scope:

```python
try:
    coll_manager.create_scope("example-scope")
except ScopeAlreadyExistsException as ex:
    print(ex)
```

You can then create a collection within that scope:

```python
collection_spec = CollectionSpec(
    "example-collection",
    scope_name="example-scope")

try:
    collection = coll_manager.create_collection(collection_spec)
except CollectionAlreadyExistsException as ex:
    print(ex)
```

Finally, you can drop unneeded collections and scopes:

```python
try:
    coll_manager.drop_collection(collection_spec)
except CollectionNotFoundException as ex:
    print(ex)

[data-source-url=https://github.com/couchbase/docs-sdk-python/blob/b5a9b6f9298e8f60424fea12c5f98c32e04b465f/modules/howtos/examples/provisioning_resources_collections.py#L107-L110]
try:
    coll_manager.drop_scope("example-scope")
except ScopeNotFoundException as ex:
    print(ex)
```

Note that the most minimal permissions to create and drop a Scope or Collection is [Manage Scopes](../../../server/current/learn/security/roles.md#manage-scopes)along with [Data Reader](../../../server/current/learn/security/roles.md#data-reader).

You can create users with the appropriate RBAC programmatically:

```python
users = cluster.users()
user = User(username="scopeAdmin",
            password="password",
            display_name="Manage Scopes [travel-sample:*]",
            roles=[
                Role(name="scope_admin", bucket="travel-sample"),
                Role(name="data_reader", bucket="travel-sample")
            ])
users.upsert_user(user)
```

You can enumerate Scopes and Collections using the `CollectionManager.get_all_scopes()` method and the `Scope.collections` property.

```python
def get_scope(collection_mgr, scope_name):
    return next((s for s in collection_mgr.get_all_scopes()
                if s.name == scope_name), None)


def get_collection(collection_mgr, scope_name, coll_name):
    scope = get_scope(collection_mgr, scope_name)
    if scope:
        return next(
            (c for c in scope.collections if c.name == coll_name),
            None)

    return None
```

## [](#index-management)Index Management

In general, you will rarely need to work with Index Managers from the SDK. For those occasions when you do, index management operations can be performed with the following interfaces:

* QueryIndexManager — [Cluster.query\_indexes()](https://docs.couchbase.com/sdk-api/couchbase-python-client-4.0.0/couchbase%5Fapi/couchbase%5Fcore.html#couchbase.cluster.Cluster.query%5Findexes)
* AnalyticsIndexManager — [Cluster.analytics\_ndexes()](https://docs.couchbase.com/sdk-api/couchbase-python-client-4.0.0/couchbase%5Fapi/couchbase%5Fcore.html#couchbase.cluster.Cluster.query%5Findexes)
* SearchIndexManager — [Cluster.search\_indexes()](https://docs.couchbase.com/sdk-api/couchbase-python-client-4.0.0/couchbase%5Fapi/couchbase%5Fcore.html#couchbase.cluster.Cluster.query%5Findexes)
* ViewIndexManager — [Bucket.view\_indexes()](https://docs.couchbase.com/sdk-api/couchbase-python-client-4.0.0/couchbase%5Fapi/couchbase%5Fcore.html#couchbase.bucket.Bucket.collections)

You will find some of these described in the following section.

### [](#queryindexmanager)QueryIndexManager

The `QueryIndexManager` interface contains the means for managing indexes used for queries. It can be instantiated through the `Cluster.query_indexes()` method.

```python
cluster = Cluster(
    "couchbase://your-ip",
    authenticator=PasswordAuthenticator("Administrator", "password")
)

query_index_mgr = cluster.query_indexes()
```

Applications can use this manager to perform operations such as creating, deleting, and fetching _primary_ or _secondary_ indexes:

* A _Primary_ index is built from a document's key and is mostly suited for simple queries.
* A _Secondary_ index is the most commonly used type, and is suited for complex queries that require filtering on document fields.

> [!NOTE]
> To perform query index operations, the provided user must either be an _Admin_ or assigned the _Query Manage Index_ role. See the [Roles](../../../server/current/learn/security/roles.md#query-manage-index) page for more information.

The example below shows how to create a simple primary index, restricted to a named scope and collection, by calling the `create_primary_index()` method. Note that you cannot provide a named scope or collection separately, both must be set for the `QueryIndexManager` to create an index on the relevant keyspace path.

Creating a primary index

```python
query_index_mgr.create_primary_index("travel-sample", CreatePrimaryQueryIndexOptions(
    scope_name="tenant_agent_01",
    collection_name="users",
    # Set this if you wish to use a custom name
    # index_name="custom_name",
    ignore_if_exists=True
))
```

When a primary index name is not specified, the SDK will create the index as `#primary` by default. However, if you wish to provide a custom name, you can simply set a `index_name` property in the `CreatePrimaryQueryIndexOptions` class.

You may have noticed that the example also sets the `ignore_if_exists` boolean flag. When set to `True`, this optional argument ensures that an error is not thrown if an index under the same name already exists.

Creating a _secondary_ index follows a similar approach, with some minor differences:

Creating a secondary index

```python
try:
    query_index_mgr.create_index("travel-sample", "tenant_agent_01_users_email", ["preferred_email"], CreateQueryIndexOptions(
        scope_name="tenant_agent_01",
        collection_name="users"
    ))
except QueryIndexAlreadyExistsException:
    print("Index already exists")
```

The `create_index()` method requires an index name to be provided, along with the fields to create the index on. Like the _primary_ index, you can restrict a _secondary_ index to a named scope and collection by passing some options.

Indexes can easily take a long time to build if they contain a lot of documents. In these situations, it is more ideal to build indexes in the background. To achieve this we can use the `deferred` boolean option, and set it to `True`.

Deferring index creation

```python
try:
    # Create a deferred index
    query_index_mgr.create_index("travel-sample", "tenant_agent_01_users_phone", ["preferred_phone"], CreateQueryIndexOptions(
        scope_name="tenant_agent_01",
        collection_name="users",
        deferred=True
    ))

    # Build any deferred indexes within `travel-sample`.tenant_agent_01.users
    query_index_mgr.build_deferred_indexes("travel-sample", BuildDeferredQueryIndexOptions(
        scope_name="tenant_agent_01",
        collection_name="users"
    ))

    # Wait for indexes to come online
    query_index_mgr.watch_indexes("travel-sample", ["tenant_agent_01_users_phone"], WatchQueryIndexOptions(
        scope_name="tenant_agent_01",
        collection_name="users",
        timeout=timedelta(seconds=30)
    ))
except QueryIndexAlreadyExistsException:
    print("Index already exists")
```

To delete a query index you can use the `drop_index()` or `drop_primary_index()` methods. Which one you use depends on the type of query index you wish to drop from the database.

Deleting an index

```python
# Drop a primary index
query_index_mgr.drop_primary_index("travel-sample", DropPrimaryQueryIndexOptions(
    scope_name="tenant_agent_01",
    collection_name="users"
))

# Drop a secondary index
query_index_mgr.drop_index("travel-sample", "tenant_agent_01_users_email", DropQueryIndexOptions(
    scope_name="tenant_agent_01",
    collection_name="users"
))
```

## [](#views-management)Views Management

Views are stored in design documents. The SDK provides convenient methods to create, retrieve, and remove design documents. To set up views, you create design documents that contain one or more view definitions, and then insert the design documents into a bucket. Each view in a design document is represented by a name and a set of MapReduce functions. The mandatory map function describes how to select and transform the data from the bucket, and the optional reduce function describes how to aggregate the results.

In the SDK, design documents are represented by the `DesignDocument` and `View` classes. All operations on design documents are performed on the `ViewIndexManager` instance:

```python
cluster = Cluster(
    "couchbase://your-ip",
    authenticator=PasswordAuthenticator(
        "Administrator",
        "password"))

# For Server versions 6.5 or later you do not need to open a bucket here
bucket = cluster.bucket("travel-sample")

view_manager = bucket.view_indexes()
```

The following example upserts a design document with two views:

```python
design_doc = DesignDocument(
    name="landmarks",
    views={
        "by_country": View(
            map="function (doc, meta) { if (doc.type == 'landmark') { emit([doc.country, doc.city], null); } }"),
        "by_activity": View(
            map="function (doc, meta) { if (doc.type == 'landmark') { emit(doc.activity, null); } }",
            reduce="_count")})

view_manager.upsert_design_document(
    design_doc, DesignDocumentNamespace.DEVELOPMENT)
```

> [!WARNING]
> When you want to update an existing document with a new view (or a modification of a view's definition), you can use the `upsert_design_document` method.
> 
> However, this method needs the list of views in the document to be exhaustive, meaning that if you just create the new view definition as previously and add it to a new design document that you upsert, all your other views will be erased!
> 
> The solution is to perform a `get_design_document`, add your view definition to the DesignDocument's views list, then upsert it. This also works with view modifications, provided the change is in the `map` or `reduce` functions (just reuse the same name for the modified view), or for deletion of one out of several views in the document.

Note the use of `DesignDocumentNamespace.DEVELOPMENT`, the other option is `DesignDocumentNamespace.PRODUCTION`. This parameter specifies whether the design document should be created as development, or as production — with the former running over only a small fraction of the documents.

Now that we've created a design document we can fetch it:

```python
d_doc = view_manager.get_design_document(
    "landmarks", DesignDocumentNamespace.DEVELOPMENT)

print("Found design doc: {} w/ {} views.".format(d_doc.name, len(d_doc.views)))
```

We've created the design document using `DesignDocumentNamespace.DEVELOPMENT` and now want to push it to production, we can do this with:

```python
view_manager.publish_design_document("landmarks")
```

To remove this design document:

```python
#view_manager.drop_design_document(
#    "landmarks", DesignDocumentNamespace.DEVELOPMENT)
```