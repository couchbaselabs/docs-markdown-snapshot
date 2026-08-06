---
title: Buckets and Clusters
description: The Couchbase Ruby SDK provides an API for managing a Couchbase
  cluster programmatically.
editUrl: https://github.com/couchbase/docs-sdk-ruby/edit/temp/3.7/modules/concept-docs/pages/buckets-and-clusters.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:3.7@ruby-sdk:concept-docs:buckets-and-clusters.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ruby-sdk/3.7/concept-docs/buckets-and-clusters.html)

# Buckets and Clusters

> The Couchbase Ruby SDK provides an API for managing a Couchbase cluster programmatically. 

The primary means for managing clusters is through the [Couchbase Web UI](../../../server/current/manage/manage-buckets/bucket-management-overview.md) which provides an easy to use interface for adding, removing, monitoring, and modifying buckets. In some instances you may wish to have a programmatic interface. For example, if you wish to manage a cluster from a setup script, or if you are setting up buckets in test scaffolding.

The SDK also comes with some convenience functionality for common Couchbase management requests — see the [Provisioning Cluster Resources](../howtos/provisioning-cluster-resources.md) guide.

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