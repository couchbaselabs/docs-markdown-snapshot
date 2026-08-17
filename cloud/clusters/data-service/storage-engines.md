---
title: Storage Engines
description: "Capella supports two different backend storage engines: Magma and Couchstore."
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/data-service/storage-engines.adoc
  xref: xref:cloud:clusters:data-service/storage-engines.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/clusters/data-service/storage-engines.html)

# Storage Engines

> Capella supports two different backend storage engines: Magma and Couchstore. 

You can choose between the Couchstore or Magma storage engines at the bucket level [when creating a bucket](manage-buckets.md#add-bucket). A single Capella cluster can have a mix of Couchstore and Magma buckets.

The choice of which storage engine to use depends on your use case and the size of your dataset. When using Couchbase Server 8.0 or later, Magma is the recommended storage engine for most use cases.

Understanding the strengths and weaknesses of each backend storage engine helps you choose the one that best suits your requirements.

__Table 1\. Couchstore and Magma at a glance__
|                              | Couchstore | Magma [\[1\]](#quota-note)                  |
| ---------------------------- | ---------- | ------------------------------------------- |
| Minimum bucket memory quota  | 100 MiB    | 100 MiB (128 vBuckets)1 GiB (1024 vBuckets) |
| Minimum memory to data ratio | 10%        | 1%                                          |
| Maximum data per node        | 1.6 TiB    | 16 TiB                                      |

| [\[1\]](#quota-ref) | Magma's minimum memory requirement depends on the number of vBuckets. |
| ------------------- | --------------------------------------------------------------------- |

> [!IMPORTANT]
> XDCR between Magma and Couchstore
> 
> Only Couchbase Server 8.0 and later supports XDCR replication between buckets with different numbers of vBuckets. Couchstore buckets use 1024 vBuckets, while Magma buckets can use either 128 or 1024 vBuckets.
> 
> To create an XDCR replication from a bucket on a cluster using Couchbase Server 7.6 or earlier, you must use Magma with 1024 vBuckets or Couchstore.

## [](#storage-engine-magma)Magma

Magma is the default backend storage engine in Capella. Magma is optimized for high-performance applications with large datasets that exceed available memory capacity. Disk access performance depends on the underlying disk subsystems.

Magma can work with low amounts of memory for large datasets. For example, a node holding 5 TiB of data can use Magma with only 64 GiB RAM. This efficiency is from Magma's optimized disk access and memory management techniques.

Magma gives you the choice between 128 and 1024 vBuckets. If you allocate 1 GiB or more memory per node to your bucket, the 1024 vBucket option delivers better performance at scale.

### [](#when-to-use-magma)When to Use Magma

You should use Magma if:

* Your working set is much larger than the available memory, and you only rely on disk access speed.
* You need to store and access large amounts of data using the lowest amount of memory.
* Your applications make heavy use of transactions with persistence-based durability.

## [](#couchstore)Couchstore

Couchstore delivers high performance while efficiently using system resources where memory is sufficient. Couchstore is ideal for small datasets that fit entirely in-memory.

### [](#when-to-use-couchstore)When to Use Couchstore

You should use Couchstore if:

* You have a dataset with a working set that fits in available memory and exceeds 20% of the total dataset size.
* You're using an operational cluster with limited resources, such as low compute or storage.

## [](#migrating-a-couchstore-bucket-to-magma)Migrating a Couchstore Bucket to Magma

* Couchbase Server 7.6+
* Couchbase Server 7.2

Couchstore to Magma migration is only possible when the target Magma bucket has 1024 vBuckets. If your cluster in Capella uses Couchbase Server 7.6 or later, migrate your Couchstore buckets to Magma by making a [PUT - Migrate Buckets](../../management-api-reference/index.md#tag/Clusters/operation/putBucketStorageBackend) call to the Management API.

PUT - Migrate Buckets can migrate 1 or more Couchstore buckets to Magma while your cluster is running. The API runs a swap [rebalance](../scale-database.md#rebalance) of your cluster's Data Service nodes. Your cluster shows a rebalancing state during the operation.

Before using PUT - Migrate Buckets, check that the buckets you're migrating meet the [requirements for Magma](#magma-reqs). If the bucket fails to meet those requirements, the API call returns `"errorType": "MagmaBucketSizeTooSmall"`.

If your cluster in Capella uses Couchbase Server 7.2, you must create a new bucket with the Magma storage engine and then copy the data. To create a bucket with the Magma storage engine, follow the steps in [Create a Bucket](../../../server/current/manage/manage-buckets/create-bucket.md) and select Magma as the storage backend during bucket creation.

To copy the data, use [XDCR](../xdcr/xdcr.md) or [backup](../backup-restore.md) the Couchstore bucket and restore it to the new Magma bucket.

## [](#next-steps)Next Steps

* [Create a Bucket](manage-buckets.md#add-bucket)