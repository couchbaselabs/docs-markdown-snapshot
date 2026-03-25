---
title: Buckets and Clusters
description: The Couchbase Java SDK provides an API for managing a Couchbase
  cluster programmatically.
editUrl: https://github.com/couchbase/docs-sdk-kotlin/edit/temp/3.9/modules/concept-docs/pages/buckets-and-clusters.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:3.9@kotlin-sdk:concept-docs:buckets-and-clusters.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/kotlin-sdk/3.9/concept-docs/buckets-and-clusters.html)

# Buckets and Clusters

> The Couchbase Java SDK provides an API for managing a Couchbase cluster programmatically. 

The primary means for managing clusters is through the [Couchbase Web UI](../../../server/current/manage/manage-buckets/bucket-management-overview.md) which provides an easy to use interface for adding, removing, monitoring, and modifying buckets. In some instances you may wish to have a programmatic interface. For example, if you wish to manage a cluster from a setup script, or if you are setting up buckets in test scaffolding.

The SDK also comes with some convenience functionality for common Couchbase management requests — see the [Provisioning Cluster Resources](#howtos:provisioning-cluster-resources.adoc) guide.

Management operations in the Java SDK may be performed through several interfaces depending on the object:

## [](#creating-and-removing-buckets)Creating and Removing Buckets

To create or delete a bucket, call the bucket manager with the `buckets()` call on the cluster:

```java
BucketManager manager = cluster.buckets();
bucketSettings = BucketSettings.create("myBucket");
manager.createBucket(bucketSettings);
```

This class is also used to expose information about an existing bucket (`manager.getBucket(string)`) or to update an existing bucket (`manager.updateBucket(bucketSettings)`).

The default Collection & Default Scope will be used automatically.