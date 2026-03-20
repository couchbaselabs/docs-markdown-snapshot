---
title: Buckets and Clusters
description: The Couchbase Java SDK provides an API for managing a Couchbase
  cluster programmatically.
editUrl: https://github.com/couchbase/docs-sdk-kotlin/edit/temp/1.3/modules/concept-docs/pages/buckets-and-clusters.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:1.3@kotlin-sdk:concept-docs:buckets-and-clusters.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/kotlin-sdk/1.3/concept-docs/buckets-and-clusters.html)

# Buckets and Clusters

> The Couchbase Java SDK provides an API for managing a Couchbase cluster programmatically. 

Unresolved include directive in modules/concept-docs/pages/buckets-and-clusters.adoc - include::7.5@sdk:shared:partial$clusters-buckets.adoc\[\]

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