---
title: Buckets and Clusters
description: The Couchbase Node.js SDK provides an API for managing a Couchbase
  cluster programmatically.
editUrl: https://github.com/couchbase/docs-sdk-nodejs/edit/temp/4.4/modules/concept-docs/pages/buckets-and-clusters.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/nodejs-sdk/4.4/concept-docs/buckets-and-clusters.html)

# Buckets and Clusters

> The Couchbase Node.js SDK provides an API for managing a Couchbase cluster programmatically. 

The primary means for managing clusters is through the [Couchbase Web UI](#7.1@server:manage:manage-buckets/bucket-management-overview.adoc) which provides an easy to use interface for adding, removing, monitoring, and modifying buckets. In some instances you may wish to have a programmatic interface. For example, if you wish to manage a cluster from a setup script, or if you are setting up buckets in test scaffolding.

The SDK also comes with some convenience functionality for common Couchbase management requests — see the [Provisioning Cluster Resources](../howtos/provisioning-cluster-resources.md) guide.

Management operations in the Node.js SDK may be performed through several interfaces depending on the object:

## [](#creating-and-removing-buckets)Creating and Removing Buckets

To create or delete a bucket, call the bucket manager with the `buckets()` call on the cluster:

```javascript
const bucketMgr = cluster.buckets()

bucketMgr.createBucket({
    name: 'my_bucket',
    flushEnabled: false,
    ramQuotaMB: 256,
    numReplicas: 1,
    replicaIndexes: false,
    bucketType: couchbase.BucketType.Couchbase,
    ejectionMethod: couchbase.EvictionPolicy.ValueOnly,
    maxTTL: 0,
    compressionMode: couchbase.CompressionMode.Passive,
})
```

The default Collection & Default Scope will be used automatically.

See [Provisioning Cluster Resources](../howtos/provisioning-cluster-resources.md) for more details.