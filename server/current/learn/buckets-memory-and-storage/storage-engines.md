---
title: Storage Engines
description: "Couchbase supports two different backend storage engines:
  Couchstore and Magma."
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/learn/pages/buckets-memory-and-storage/storage-engines.adoc
  xref: xref:server:learn:buckets-memory-and-storage/storage-engines.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/learn/buckets-memory-and-storage/storage-engines.html)

# Storage Engines

> Couchbase supports two different backend storage engines: Couchstore and Magma. These storage engines organize the data both on disk and in memory. This page explains how to choose a backend storage to suit your needs. 

## [](#storage-engine-magma)Magma

[ENTERPRISE EDITION](https://www.couchbase.com/products/editions)

Magma is designed for high performance with large datasets that do not fit in memory. It's ideal for use cases that rely primarily on data stored on disk. The performance of disk access is as good as the underlying disk sub-systems. For example, using NVMe SSDs gives better performance than spinning drives.

When you create a bucket using the Magma storage engine, you choose the number of [vBuckets](vbuckets.md) a bucket uses. Magma supports two vBucket configurations: 128 or 1024\. This choice affects the minimum memory quota for the bucket. The 128 vBucket configuration is the default for new buckets in Couchbase Server Enterprise Edition 8.0 and later. It has a minimum memory quota of 100 MiB per node.

> [!NOTE]
> Magma buckets with 128 vBuckets are only available in clusters that have fully migrated to Couchbase Server 8.0 or later.

Magma using 1024 vBuckets has a minimum memory quota of 1 GiB per node.

If you can allocate at least 1 GiB memory per node to your bucket, you should choose the 1024 vBucket option for Magma as you'll get better performance at scale. As your dataset grows, Magma has a minimum memory-to-data ratio of 1%. For example, a node with 5 TiB data in a Magma bucket must allocate at least 51 GiB of RAM for the bucket.

### [](#magma-performance-considerations)Magma Performance Considerations

When using Magma, consider the following performance optimizations:

* Make sure your data storage path for the bucket is on an SSD.
* When installing Couchbase Server on Linux, use the [XFS file system](https://en.wikipedia.org/wiki/XFS) for the data storage path. Magma is a disk-optimized storage engine, and its performance depends on the speed of the underlying disk and its filesystem.
* Set the bucket's ejection policy to Full to minimize memory use. See [Ejection](memory.md#ejection) for more information.

#### [](#magma-writer-thread-settings)Magma Writer Thread Settings

Couchbase Server lets you set the number of threads for reading and writing data to the disk. For higher I/O concurrency, consider increasing the number of reader and writer threads by setting the bucket's **Reader Thread Settings** and **Writer Thread Settings** to **Disk i/o optimized** for Magma buckets. This setting makes sure there are enough threads to sustain high read and write rates.

You can also tune the number and allocation of threads that Magma uses to compact and flush data to disk. If you notice that Magma's data compaction spikes CPU use, you can change the ratio of threads that compact data to the threads that flush data. See [Magma Flushing and Compaction Threads](storage-settings.md#magma-flushing-and-compaction-threads) for more information about these settings.

See [Data Settings](../../manage/manage-settings/general-settings.md#data-settings) to learn more about configuring thread settings for Magma buckets.

## [](#couchstore)Couchstore

Couchstore is the original storage engine for Couchbase Server. It's the only storage engine available in Couchbase Server Community Edition. Couchstore is designed for high performance with datasets that fit in memory. It has a minimum memory requirement of 100 MB per node, and a minimum memory-to-data ratio of 10%. If you have a small dataset whose working set (frequently accessed data) can fit in memory, then you should consider using Couchstore.

## [](#couchstore-verses-magma-at-a-glance)Couchstore verses Magma at a Glance

The following table summarizes the differences between Couchstore and Magma storage engines.

|                              | Couchstore | Magma 128 vBuckets                                         | Magma 1024 vBuckets |
| ---------------------------- | ---------- | ---------------------------------------------------------- | ------------------- |
| Minimum bucket memory quota  | 100 MiB    | 100 MiB                                                    | 1 GiB               |
| Minimum memory to data ratio | 10%        | 1%                                                         | 1%                  |
| Maximum data per node        | 3 TB       | 10 TB, but with much higher possibility of data imbalance. | 10 TB               |

## [](#which-storage-engine-should-you-use)Which Storage Engine Should You Use?

The choice of which storage engine to use depends on your use case and the size of your dataset. As of Couchbase Server 8.0, the Magma is the recommended storage engine for most use cases. The choice between 128 and 1024 vBuckets gives you flexibility when configuring your bucket.

When to choose Magma with 128 vBuckets

You should use the Magma backend with 128 vBuckets if any of the following are true:

* You want to minimize memory use and have a working dataset that does not fit in the available memory or is more than 20% of the total dataset. Magma with 128 vBuckets is more efficient in this case than Couchstore.
* You want to conserve memory as your dataset grows. Because Magma has a 1% memory-to-data ratio, its memory requirements grow more slowly than Couchstore's 10% memory-to-data ratio.
* You have a dataset size that's less than 100 GiB. With this small dataset size, the 128 vBucket configuration saves you memory verses the minimum 1 GiB memory required by the 1024 vBucket Magma configuration.
* You're configuring a POC or testing system and plan to use Magma with 1024 vBuckets in production.

When to choose Magma with 1024 vBuckets

You should use the Magma backend with 1024 vBuckets if any of the following are true:

* Your working set is larger than the available memory (or you expect it to outgrow memory), and you need high disk-access speed.
* You need to store and access large amounts of data (multiple terabytes) using a small amount of memory. In this case, the 1024 vBucket configuration is less likely to have data imbalance issues than the 128 vBucket configuration. Also, Magma with 1024 vBuckets uses less CPU for operations such as compaction verse the 128 vBucket configuration.
* Your applications make heavy use of transactions with persistence-based durability.
* Your dataset will grow beyond Couchstore's 3 TB limit.

When should you choose Couchstore?

You should use the Couchstore backend if any of the following are true:

* You're using Couchbase Server Community Edition which only supports the Couchstore storage engine.
* You have a dataset with a working set that fits into available memory and the working set is less than 20% of the total dataset.
* You're running Couchbase Server on low-end hardware.
* You're running the legacy [Views Reference](../views/views-intro.md) Service, which does not run on Magma storage.

## [](#migrating-between-storage-engines)Migrating between Storage Engines

You can migrate a bucket to use a different storage engine. Consider migrating a bucket if it no longer meets the criteria explained in the previous sections. For example, suppose you have a bucket using the Couchstore backend whose working dataset has grown to the point where it no longer fits in memory. In this case, you should migrate the bucket to use Magma as a storage backend.

To learn how to migrate a bucket's storage backend, see [Migrate a Bucket's Storage Backend](../../manage/manage-buckets/migrate-bucket.md).