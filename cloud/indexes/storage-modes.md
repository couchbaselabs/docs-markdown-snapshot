---
title: Index Storage Settings
description: All indexes in Couchbase Capella use the Couchbase Plasma storage engine.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/indexes/pages/storage-modes.adoc
  xref: xref:cloud:indexes:storage-modes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/indexes/storage-modes.html)

# Index Storage Settings

> All indexes in Couchbase Capella use the Couchbase Plasma storage engine. 

Couchbase Capella indexes implement multi-version concurrency control (MVCC) to provide consistent index scan results and high throughput.

## [](#standard-index-storage)Index Storage

In Couchbase Capella, indexes are saved on disk, in a disk-optimized format that uses both memory and disk for index-update and scanning. The performance of standard index storage depends on overall I/O performance.

Couchbase Capella index storage supports indexes for both Couchbase buckets and Memory-only buckets. See [Manage Buckets](../clusters/data-service/manage-buckets.md).

The standard global secondary index uses a B-Tree index and keeps the optimal working set of data in the buffer. This means the total size of the index can be much bigger than the amount of memory available in each index node.

Standard index-storage is supported by the Plasma storage engine. Plasma is highly scalable and performant storage engine that's optimized specifically for indexes. Compaction is handled automatically.

## [](#plasma-memory-enhancements)Plasma Memory Enhancements

Couchbase Capella provides the following enhancements for Plasma:

* [Per Page Bloom Filters](#per-page-bloom-filters)
* [In-Memory Compression](#in-memory-compression)

These are described below.

### [](#per-page-bloom-filters)Per Page Bloom Filters

A [Bloom filter](https://en.wikipedia.org/wiki/Bloom%5Ffilter) gives guidance as to whether a searched-for item resides on disk. By indicating that the item is not on disk, the filter prevents unnecessary on-disk searches.

If Bloom filters are enabled (which is the default), when a lookup occurs, and the correct Plasma page is located, the Bloom filter indicates either that the item is not on the page, or that it may be on the page. If the filter indicates that:

* The item is not on the page, then the item is not on disk, and no disk read need occur.
* The item may be on the page, then the item can continue to be searched for, and a disk read must therefore occur.

The consequent reduction in disk reads promotes the efficiency of mutation processing, when the mutations are insert heavy.

### [](#in-memory-compression)In-Memory Compression

In Couchbase Capella, Plasma memory management routinely performs the compression of a subset of items. This frees memory, and due to the additional memory made available, keeps a greater number of items in memory overall. By keeping more items in memory, the need for disk reads is reduced, as are corresponding latencies.

The selection of items to be compressed occurs periodically. Only items that have already been flushed to disk are compressed. After compression, such items are principal candidates for subsequent ejection.

Disk flushing occurs every 10 minutes. Items not yet flushed to disk are not compressed, nor is any recently used item. In consequence, items most likely to be accessed remain uncompressed in memory, and are therefore accessible with the least latency. Items less likely to be accessed are retained in memory in compressed form, until their ejection. After ejection, they must be accessed through disk reads.

This new model of memory usage leads to higher residence ratios and greater access efficiency, at the cost of some additional CPU utilization, due to the more frequent performance of compression and decompression routines.