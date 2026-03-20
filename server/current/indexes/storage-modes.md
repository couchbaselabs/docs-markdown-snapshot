---
title: Index Storage Settings
description: "A Secondary Index can be saved in either of two ways:
  memory-optimized or standard."
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/indexes/pages/storage-modes.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:server:indexes:storage-modes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/indexes/storage-modes.html)

# Index Storage Settings

> A Secondary Index can be saved in either of two ways: memory-optimized or standard. 

Both standard and memory-optimized indexes implement multi-version concurrency control (MVCC) to provide consistent index scan results and high throughput.

## [](#memory-optimized-index-storage)Memory-Optimized Index Storage

[ENTERPRISE EDITION](https://www.couchbase.com/products/editions)

Memory-optimized index storage is supported by the Nitro storage engine, and is only available in Couchbase Server Enterprise Edition.

A memory-optimized index uses a lock-free skiplist to maintain the index and keeps all the index data in memory. A memory-optimized index has better latency for index scans and processes the mutations of the data much faster.

Memory-optimized indexes can be created for both Couchbase and Ephemeral buckets. See [Buckets](../learn/buckets-memory-and-storage/buckets.md).

Memory-optimized index storage allows high-speed maintenance and scanning, since the index is kept fully in memory at all times. A snapshot of the index is maintained on disk, to permit rapid recovery if node failures are experienced. To be consistently beneficial, memory-optimized index storage requires that all nodes running the Index Service have a memory quota sufficient for the number and size of their resident indexes, and for the frequency with which the indexes will be updated and scanned.

Memory-optimized index storage may be less suitable for nodes where memory is constrained, since whenever the Index Service memory quota is exceeded, indexes on the node can neither be updated nor scanned.

If indexer RAM usage goes above 75% of the Index Service memory quota, an [error notification](../manage/manage-settings/configure-alerts.md) is provided. If indexer RAM usage then goes above 95% of the Index Service memory quota, the indexer goes into the Paused mode on that node. Although the indexes remain in `Active` state, traffic is routed away from the node.

Before index operations can resume, memory must be freed. When the indexer RAM usage drops below 80% of the Index Service memory quota, the indexer goes into Active mode again on that node.

To resume indexing operations on a node where the Indexer has paused due to low memory, consider taking one or more of the following actions:

* Increase the index memory quota, to give indexes additional memory for request processing.
* Remove less important indexes from the node, to free up memory.
* Remove buckets with indexes. Removing a bucket automatically removes all the dependent indexes.
* Flush buckets that have indexes. Flushing a bucket deletes all data in a bucket. Even if there are pending updates not yet processed, flushing causes all indexes to drop their own data.  
Attempting to delete bucket data selectively during an out-of-memory condition does not succeed in decreasing memory usage. Without memory, such requested deletions cannot themselves be processed.

In cases where recovery requires an Index Service node to be restarted, the node’s resident memory-optimized indexes are rebuilt from the snapshots retained on disk. Following the node’s restart, these indexes remain in the `Warmup` state until all information has been read into memory: then, final updates are made with the indexes in `Active` state. Once a rebuilt index is available, queries with `consistency=request_plus` or `consistency=at_plus` fail, if the specified timestamp exceeds the last timestamp processed by given index. \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]However, queries with `consistency=unbounded` execute normally. For information on these settings, see [Index Availability and Performance](#services-and-indexes/indexes/index-replication.adoc).

## [](#standard-index-storage)Standard Index Storage

Standard is the default storage setting for Secondary Indexes: the indexes are saved on disk in a disk-optimized format that uses both memory and disk for index update and scanning. The performance of standard index storage depends on overall I/O performance.

In Couchbase Server version 7.0.2 and later, standard index storage supports indexes for both Couchbase buckets and Ephemeral buckets. This applies both to Couchbase Server Enterprise Edition and to Couchbase Server Community Edition. See [Buckets](../learn/buckets-memory-and-storage/buckets.md).

The standard global secondary index uses a B-Tree index and keeps the optimal working set of data in the buffer. This means the total size of the index can be much bigger than the amount of memory available in each index node.

[ENTERPRISE EDITION](https://www.couchbase.com/products/editions)

In Couchbase Server Enterprise Edition, standard index storage is supported by the Plasma storage engine. In this case, compaction is handled automatically.

Each plasma instance has a data log and a recovery log to run. The log is based on Log-Structured Storage (LSS). The data LSS contains index data, while the recovery LSS stores metadata required for recovery. If the index is created on a default scope and collection, plasma uses a pair of dedicated LSS. For non-default scope or collection, instances will use shared LSS.

The default threshold for the LSS Cleaner to run is 16MB per LSS. This means the LSS/Recovery cleaner will remove stale blocks only when the LSS used space exceeds 16MB. Plasma minimizes disk fragmentation by using hole punching on filesystems that support it. Once the cleaner trims the LSS, hole punching occurs in fixed 64MB granularity. This means that the disk log file must expand to at least 80MB (64MB + 16MB) before blocks can be reclaimed or hole punched.

In 8.0, we have made the hole punching granularity configurable. ([MB-65161](https://jira.issues.couchbase.com/browse/MB-65161) )

[COMMUNITY EDITION](https://www.couchbase.com/products/editions)

In Couchbase Server Community Edition, standard index storage is supported by the Forestdb storage engine. In this case, each index saved with the standard option has two write modes:

Circular Write Mode

Writes changes to the end of the index file, until the relative index fragmentation exceeds 65%. Block reuse is then triggered: new data is written into stale blocks where possible, rather than to the end of the file, so as to optimize I/O throughput. Full compaction runs in accordance with the value of the **Circular write mode with day + time interval trigger** setting: see [Index Fragmentation](../manage/manage-settings/configure-compact-settings.md#index-fragmentation). However, the index fragmentation data size is not significantly changed by compaction.

Append-only Write Mode

Writes changes to the end of the index file, invalidating existing pages within the index file, and requiring frequent, full compaction.

By default, Couchbase Server Community Edition uses Circular Write Mode for standard index storage. Append-only Write Mode is provided for backwards compatibility with previous versions.

Other storage settings are described in detail in [Configuring Auto-Compaction](../manage/manage-settings/configure-compact-settings.md).

## [](#changing-index-storage-settings)Changing Index Storage Settings

Settings are established at cluster initialization for all indexes on the cluster, across all buckets. Following cluster initialization, to change from one setting to the other, all nodes running the Index Service must be removed. If the cluster is single-node, uninstall and reinstall Couchbase Server. If the cluster is multi-node, and only some of the nodes host the Index Service, proceed as follows:

1. Identify the nodes running the Index Service.
2. Remove each of the nodes running the Index Service. As Index Service nodes are removed, so are the indexes they contain. In consequence, any ongoing queries fail.
3. Perform a rebalance.
4. Change the Index Storage Settings for the cluster.
5. Add new Index Service nodes, and confirm the revised storage mode.

For information on adding and removing nodes, and on rebalancing a cluster, see [Manage Nodes and Clusters](../manage/manage-nodes/node-management-overview.md).

## [](#plasma-memory-enhancements)Plasma Memory Enhancements

Couchbase Server provides the following enhancements for Plasma:

* [Per Page Bloom Filters](#per-page-bloom-filters)
* [In-Memory Compression](#in-memory-compression)

These are described below.

### [](#per-page-bloom-filters)Per Page Bloom Filters

A [Bloom filter](https://en.wikipedia.org/wiki/Bloom%5Ffilter) gives guidance as to whether a searched-for item resides on disk. By indicating that the item is not on disk, the filter prevents unnecessary on-disk searches.

If Bloom filters are enabled (which is the default), when a lookup occurs, and the correct Plasma page is located, the Bloom filter indicates either that the item is not on the page, or that it may be on the page. If the filter indicates that:

* The item is not on the page, then the item is not on disk, and no disk read need occur.
* The item may be on the page, then the item can continue to be searched for, and a disk read must therefore occur.

The consequent reduction in disk reads promotes the efficiency of mutation processing, when the mutations are insert heavy.

Bloom filters can be enabled or disabled by means of the Couchbase Web Console UI, or the REST API. See the information provided on establishing [General](../manage/manage-settings/general-settings.md) settings for the cluster.

From release 7.2.1 onward, Bloom filters for plasma back indexes are enabled by default. During an upgrade, mixed mode clusters with nodes that support bloom filters will enable it for back indexes, even if they was disabled in the past. Users must explicitly disable it again after a cluster setup, or a new node is added.  
Once bloom filters are disabled in mixed mode, adding a new 7.2.1+ node will not re-enable them.

### [](#in-memory-compression)In-Memory Compression

Plasma memory management routinely performs the compression of a subset of items. This frees memory, and due to the additional memory made available, keeps a greater number of items in memory overall. By keeping more items in memory, the need for disk reads is reduced, as are corresponding latencies.

The selection of items to be compressed occurs periodically. Only items that have already been flushed to disk are compressed. After compression, such items are principal candidates for subsequent ejection.

Disk flushing occurs every 10 minutes. Items not yet flushed to disk are not compressed, nor is any recently used item. In consequence, items most likely to be accessed remain uncompressed in memory, and are therefore accessible with the least latency. Items less likely to be accessed are retained in memory in compressed form, until their ejection. After ejection, they must be accessed through disk reads.

This new model of memory usage leads to higher residence ratios and greater access efficiency, at the cost of some additional CPU utilization, due to the more frequent performance of compression and decompression routines.

---

[1](#%5Ffootnoteref%5F1). In fact, queries in this case wait for a consistent snapshot to be available and time out, rather than fail immediately.