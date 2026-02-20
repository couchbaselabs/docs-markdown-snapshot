---
title: Buckets and Clusters
description: The Couchbase Ruby SDK provides an API for managing a Couchbase
  cluster programmatically.
editUrl: https://github.com/couchbase/docs-sdk-ruby/edit/temp/3.5/modules/concept-docs/pages/buckets-and-clusters.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:3.5@ruby-sdk:concept-docs:buckets-and-clusters.adoc[]
---

[View original HTML](/ruby-sdk/3.5/concept-docs/buckets-and-clusters.html)

# Buckets and Clusters

> The Couchbase Ruby SDK provides an API for managing a Couchbase cluster programmatically. 

Unresolved include directive in modules/concept-docs/pages/buckets-and-clusters.adoc - include::7.5@sdk:shared:partial$clusters-buckets.adoc\[\]

Management operations in the Ruby SDK may be performed through several interfaces depending on the object:

## [](#creating-and-removing-buckets)Creating and Removing Buckets

To create or delete a bucket, call the bucket manager with the `buckets` call on the cluster:

```ruby
options = Cluster::ClusterOptions.new
options.authenticate("Administrator", "password")
cluster = Cluster.connect("couchbase://localhost", options)

manager = cluster.buckets

settings = Management::BucketSettings.new
settings.name = "travel-sample"
settings.ram_quota_mb = 100
settings.flush_enabled = true
manager.create_bucket(settings)
```

This class is also used to expose information about an existing bucket (`manager.get_bucket(String)`) or to update an existing bucket (`manager.update_bucket(bucket_settings)`).

The default Collection & Default Scope will be used automatically.