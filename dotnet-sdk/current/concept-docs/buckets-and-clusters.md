---
title: Buckets and Clusters
description: The Couchbase .NET SDK provides an API for managing a Couchbase
  cluster programmatically.
editUrl: https://github.com/couchbase/docs-sdk-dotnet/edit/temp/3.8/modules/concept-docs/pages/buckets-and-clusters.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:dotnet-sdk:concept-docs:buckets-and-clusters.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/dotnet-sdk/current/concept-docs/buckets-and-clusters.html)

# Buckets and Clusters

> The Couchbase .NET SDK provides an API for managing a Couchbase cluster programmatically. 

The primary means for managing clusters is through the [Couchbase Web UI](../../../server/current/manage/manage-buckets/bucket-management-overview.md) which provides an easy to use interface for adding, removing, monitoring, and modifying buckets. In some instances you may wish to have a programmatic interface. For example, if you wish to manage a cluster from a setup script, or if you are setting up buckets in test scaffolding.

The SDK also comes with some convenience functionality for common Couchbase management requests — see the [Provisioning Cluster Resources](../howtos/provisioning-cluster-resources.md) guide.

Management operations in the .NET SDK may be performed through several interfaces depending on the object:

## [](#creating-and-removing-buckets)Creating and Removing Buckets

To create or delete a bucket, first get an `IBucketManager` instance from the `Buckets` property on the cluster:

```C#
IBucketManager manager = cluster.Buckets;

// create a bucket
var bucketSettings = new BucketSettings();
bucketSettings.Name = "mynewbucket";
bucketSettings.BucketType = BucketType.Couchbase;
bucketSettings.RamQuotaMB = 100;
await manager.CreateBucketAsync(bucketSettings);

// delete a bucket
await manager.DropBucketAsync("mynewbucket");
```

`IBucketManager` is also used to expose information about an existing bucket (`manager.GetBucketAsync(string)`) or to update an existing bucket (`manager.UpdateBucketAsync(BucketSettings)`).