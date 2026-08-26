---
title: Provisioning Cluster Resources
description: Provisioning cluster resources is managed at the collection or
  bucket level, depending upon the service affected.
pubDate: 2026-08-26T04:30:42.267Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-ruby/edit/temp/3.8/modules/howtos/pages/provisioning-cluster-resources.adoc
  xref: xref:ruby-sdk:howtos:provisioning-cluster-resources.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ruby-sdk/current/howtos/provisioning-cluster-resources.html)

# Provisioning Cluster Resources

> Provisioning cluster resources is managed at the collection or bucket level, depending upon the service affected. Common use cases are outlined here, less common use cases are covered in the [API docs](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/Couchbase/Management.html). 

The primary means for managing clusters is through the Couchbase Web UI which provides an easy to use interface for adding, removing, monitoring and modifying buckets. In some instances you may wish to have a programmatic interface. For example, if you wish to manage a cluster from a setup script, or if you are setting up buckets in test scaffolding.

The Ruby SDK also comes with some convenience functionality for common Couchbase management requests.

> [!TIP]
> Managing Capella Clusters
> 
> This part of the SDK API predates the Capella Management API, and is only intended to work with self-managed Couchbase Server clusters.
> 
> Management of your Capella Operational cluster is available away from the Web UI with the [Capella Management API](../../../cloud/management-api-guide/management-api-intro.md).

Management operations in the SDK may be performed through several interfaces depending on the object:

* BucketManager — `Couchbase::Management::BucketManager` — see [API docs](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/Couchbase/Management/BucketManager.html).
* UserManager — `Couchbase::Management::UserManager` — see [API docs](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/Couchbase/Management/UserManager.html).
* QueryIndexManager — `Couchbase::Management::QueryIndexManager` — see [API docs](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/Couchbase/Management/QueryIndexManager.html).
* AnalyticsIndexManager — `Couchbase::Management::AnalyticsIndexManager` — see [API docs](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/Couchbase/Management/AnalyticsIndexManager.html).
* SearchIndexManager — `Couchbase::Management::SearchIndexManager` — see [API docs](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/Couchbase/Management/SearchIndexManager.html).
* CollectionManager — `Couchbase::Management::CollectionManager` — see [API docs](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/Couchbase/Management/CollectionManager.html).
* ViewIndexManager — `Couchbase::Management::ViewIndexManager` — see [API docs](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/Couchbase/Management/ViewIndexManager.html).

> [!NOTE]
> When using a Couchbase version earlier than 6.5, you must create a valid Bucket connection using `cluster.Bucket(name)` before you can use cluster level managers.

## [](#creating-and-removing-buckets)Creating and Removing Buckets

The [BucketManager](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/Couchbase/Management/BucketManager.html) interface may be used to create and delete buckets from the Couchbase cluster. It is instantiated through the `#create_bucket()` method.

> [!WARNING]
> Note that any property that is not explicitly set when building the bucket settings will use the default value. In the case of the update, this is not necessarily the currently configured value, so you should be careful to set all properties to their correct expected values when updating an existing bucket configuration.

See the [API docs](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/Couchbase/Management/BucketSettings.html) for a full list of settings options.

The following example creates a new bucket, adding settings including making it flushable:

```ruby
bucket_name = "new_bucket"

settings = Management::BucketSettings.new
settings.name = bucket_name
settings.ram_quota_mb = 100
settings.flush_enabled = true
measure("New bucket #{bucket_name.inspect} created") { cluster.buckets.create_bucket(settings) }
```

We can retrieve information on various settings:

```ruby
settings = cluster.buckets.get_bucket(bucket_name)
puts "Bucket #{bucket_name.inspect} settings:"
puts " * healthy?           : #{settings.healthy?}"
puts " * RAM quota          : #{settings.ram_quota_mb}"
puts " * number of replicas : #{settings.num_replicas}"
puts " * flush enabled:     : #{settings.flush_enabled}"
puts " * max TTL            : #{settings.max_expiry}"
puts " * compression mode   : #{settings.compression_mode}"
puts " * replica indexes    : #{settings.replica_indexes}"
puts " * eviction policy    : #{settings.eviction_policy}"

measure("Bucket #{bucket_name.inspect} flushed") { cluster.buckets.flush_bucket(bucket_name) }
```

As well as flushing the bucket.

## [](#flushing-buckets)Flushing Buckets

When a bucket is flushed, all content is removed. Because this operation is potentially dangerous it is disabled by default for each bucket. Bucket flushing may be useful in test environments where it becomes a simpler alternative to removing and creating a test bucket. You may enable bucket flushing on a per-bucket basis using the Couchbase Web Console or when creating a bucket.

You can flush a bucket in the SDK by using the `flush_bucket()` method.

```ruby
flush_bucket(bucket_name, options = FlushBucketOptions.new)
```

The `flush_bucket()` operation may fail if the bucket does not have flush enabled, in which case it will return an `Error::BucketNotFlushable`.

## [](#collection-management)Collection Management

The CollectionManager interface may be used to create and delete scopes and collections from the Couchbase cluster. It is instantiated through the `Bucket.collections()` method. Refer to the [CollectionManager API documentation](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/Couchbase/Management/CollectionManager.html)for further details.

```ruby
options = Cluster::ClusterOptions.new
options.authenticate("scope_admin", "password")
cluster = Cluster.connect("couchbase://localhost", options)
bucket = cluster.bucket("travel-sample")
collections = bucket.collections
```

### [](#creating-and-deleting-scopes-and-collections)Creating and Deleting Scopes and Collections

You can create a scope:

```ruby
scopes = collections.get_all_scopes

if scopes.any? { |scope| scope.name == "example-scope" }
puts "Scope already exists"
else
    collections.create_scope("example-scope")
end
```

You can then create a collection within that scope:

```ruby
collection = Management::CollectionSpec.new {|spec|
    spec.name = "example-collection"
    spec.scope_name = "example-scope" }

collections.create_collection(collection)
```

Finally, you can drop unneeded collections and scopes:

```ruby
collections.drop_collection(collection)

collections.drop_scope("example-scope")
```

Note that the most minimal permissions to create and drop a Scope or Collection is [Manage Scopes](../../../server/current/learn/security/roles.md#manage-scopes)along with [Data Reader](../../../server/current/learn/security/roles.md#data-reader)

You can create users with the appropriate RBAC programmatically:

```ruby
user = Management::User.new {|user|
    user.username = "scope_admin"
    user.password = "password"
    user.display_name = "Manage Scopes [travel-sample:*]"
    user.roles = [
        Management::Role.new {|role|
            role.name = "scope_admin"
            role.bucket = "travel-sample"},
        Management::Role.new {|role|
            role.name = "data_reader"
            role.bucket = "travel-sample"}
    ]
}
users.upsert_user(user)
```

### [](#listing-the-scopes-and-collections-available)Listing the Scopes and Collections available

You can enumerate Scopes and Collections using the `CollectionManager.get_all_scopes()` method and the `Scope.collections` property.

```ruby
collections.get_all_scopes().each {|scope|
    puts "#{scope.name} :"
    scope.collections.each {|collection|
        puts "  * #{collection.name}"
    }
}
```

### [](#more-examples)More examples

There is a full example in the [Ruby SDK repo on GitHub](https://github.com/couchbase/couchbase-ruby-client/blob/master/examples/managing%5Fcollections.rb).

## [](#index-management)Index Management

In general,you will rarely need to work with Index Managers from the SDK. For those occasions when you do, please see the relevant API docs, linked [below](#further-reading-api-guides).

## [](#view-management)View Management

Views are stored in design documents. The SDK provides convenient methods to create, retrieve, and remove design documents. To set up views, you create design documents that contain one or more view definitions, and then insert the design documents into a bucket. Each view in a design document is represented by a name and a set of MapReduce functions. The mandatory map function describes how to select and transform the data from the bucket, and the optional reduce function describes how to aggregate the results.

In the SDK, design documents are represented by the `DesignDocument` and `View` classes. All operations on design documents are performed on the `ViewIndexManager` instance:

There is a full example in the [Ruby SDK repo on GitHub](https://github.com/couchbase/couchbase-ruby-client/blob/master/examples/managing%5Fview%5Findexes.rb).

## [](#further-reading-api-guides)Further Reading & API Guides

The [API Guide](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/Couchbase/Management.html) contains info on the following Management APIs:

* [BucketManager](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/Couchbase/Management/BucketManager.html) \-- `Couchbase::Management::BucketManager`
* [UserManager](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/Couchbase/Management/UserManager.html) — `Couchbase::Management::UserManager`
* [QueryIndexManager](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/Couchbase/Management/QueryIndexManager.html) — `Couchbase::Management::QueryIndexManager`
* [AnalyticsIndexManager](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/Couchbase/Management/AnalyticsIndexManager.html) — `Couchbase::Management::AnalyticsIndexManager`
* [SearchIndexManager](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/Couchbase/Management/SearchIndexManager.html) — `Couchbase::Management::SearchIndexManager`
* [CollectionManager](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/Couchbase/Management/CollectionManager.html) — `Couchbase::Management::CollectionManager`
* [ViewIndexManager](https://docs.couchbase.com/sdk-api/couchbase-ruby-client/Couchbase/Management/ViewIndexManager.html) — `Couchbase::Management::ViewIndexManager`.