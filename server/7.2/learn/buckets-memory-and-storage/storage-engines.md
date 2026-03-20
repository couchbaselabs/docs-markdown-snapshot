---
title: Storage Engines
description: "Couchbase supports two different backend storage mechanisms:
  Couchstore and Magma."
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/learn/pages/buckets-memory-and-storage/storage-engines.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:learn:buckets-memory-and-storage/storage-engines.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/learn/buckets-memory-and-storage/storage-engines.html)

# Storage Engines

> Couchbase supports two different backend storage mechanisms: Couchstore and Magma. It is important to understand which backend storage is best suited to your requirements. 

## [](#couchstore)Couchstore

Couchstore is the original storage engine for Couchbase Server. It’s the only storage engine available in Couchbase Server Community Edition. Couchstore is designed for high performance with datasets that fit in memory. It has a minimum memory requirement of 100 MB per node, and a recommended minimum memory-to-data ratio of 10%. If you have a small dataset whose working set (frequently accessed data) can fit in memory, then you should consider using Couchstore.

## [](#storage-engine-magma)Magma

[ENTERPRISE EDITION](https://www.couchbase.com/products/editions)

Magma is designed for high performance with very large datasets that do not fit in memory. It is ideal for use cases that rely primarily on disk access. The performance of disk access will be as good as the underlying disk sub-systems — for example, using NVMe SSDs will give higher performance.

In order to get maximum performance from Magma for disk-oriented workloads, it is recommended to set the Writer Threads to `Disk i/o optimized`. This setting will ensure there are enough threads to sustain high write rates.

To learn more about Writer Thread settings, see [Data Settings](../../manage/manage-settings/general-settings.md#data-settings)

Magma can work with very low amounts of memory for large datasets: a minimum memory-to-data ratio of 1% is required. For example, if a node is holding 5 TB of data, Magma can be used with only 64 GB RAM.

__Table 1\. Magma Supported Services__
| Couchbase Version            | Services Supported                                      |
| ---------------------------- | ------------------------------------------------------- |
| **Version 7.1**              | Query, Index, XDCR, Backup                              |
| **Version 7.1.2 and Higher** | Search, Eventing, Analytics[\[1\]](#magma-support-note) |

| [1](#magma-support-ref) | If these services are required in versions prior to 7.1.2, Couchstore should be used. |
| ----------------------- | ------------------------------------------------------------------------------------- |

## [](#couchstore-and-magma-at-a-glance)Couchstore and Magma at a Glance

|                              | Couchstore | Magma                    |
| ---------------------------- | ---------- | ------------------------ |
| Minimum bucket memory quota  | 100 MB     | 1 GB[\[1\]](#quota-note) |
| Minimum memory to data ratio | 10%        | 1%                       |
| Maximum data per node        | 3 TB       | 10 TB                    |

| [1](#quota-ref) | Magma’s minimum memory requirement is higher at 1GB per node due to the more complex data structures it has to maintain. |
| --------------- | ------------------------------------------------------------------------------------------------------------------------ |

## [](#when-should-you-use-couchstore)When should you use Couchstore?

The choice of Couchstore or Magma is set at the bucket level [when the bucket is created](../../manage/manage-buckets/create-bucket.md). A single Couchbase cluster can have a mix of Couchstore and Magma buckets.

You should use the Couchstore backend if:

* You have a dataset with a working set that will fit into available memory (and the working set is > 20%).
* You are running the Couchbase server on low-end hardware.
* You are running a version prior to 7.1.2, and your bucket needs to support the Search, Eventing, or Analytics Service.
* You are running the legacy [MapReduce Views](../views/views-intro.md) Service, which will not run on Magma storage.

## [](#when-should-you-use-magma)When should you use Magma?

You should use the Magma backend if:

* Your working set is much larger than the available memory, and you need high disk-access speed.
* You need to store and access large amounts of data (several terabytes) using a small amount of memory.
* Your applications make heavy use of transactions with persistence-based durability.

## [](#migrating-a-couchstore-bucket-to-magma)Migrating a Couchstore Bucket to Magma

If you have an existing Couchstore bucket that you would like to migrate to Magma, create a new Magma bucket, and then copy the data to the Magma bucket.

To copy the data, either use [XDCR](../../xdcr-reference/xdcr-reference-intro.md) or [backup](../../manage/manage-backup-and-restore/manage-backup-and-restore.md) the Couchstore bucket and then _restore_ to the Magma bucket.