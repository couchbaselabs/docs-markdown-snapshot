---
title: Index Service Metrics
description: A list of the metrics provided by the Index Service.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/metrics-reference/pages/index-service-metrics.adoc
pubDate: 2026-08-13T05:04:50.295Z
link: xref:server:metrics-reference:index-service-metrics.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/metrics-reference/index-service-metrics.html)

# Index Service Metrics

> A list of the metrics provided by the Index Service. 

The following Index-Service metrics can be queried by means of the REST APIs described in [Statistics](../rest-api/rest-statistics.md).

See [Index Service Cross Reference](index-service-metrics-cross-reference.md) if you are looking for a metric name you know from an alternative supported or legacy tool.

> [!TIP]
> * The x.y.z badge shows the Couchbase Server version the metric was added in.
> * The type / unit badge shows shows the Prometheus [type](https://prometheus.io/docs/tutorials/understanding%5Fmetric%5Ftypes/) and [unit](https://prometheus.io/docs/practices/naming/#base-units) (if present).

`index_avg_disk_bps`

7.2.0gaugeSum of disk bytes written per second, of all indexes, located on this node

`index_avg_drain_rate`

7.0.0gaugeAverage number of documents indexed per second, for this index

`index_avg_item_size`

7.0.0gauge / bytesAverage size of the indexed items, for this index

`index_avg_mutation_rate`

7.2.0gaugeSum of mutation rates of all indexes, located on this node

`index_avg_resident_percent`

7.2.0gaugeAverage resident percent across all indexes, located on this node

`index_avg_scan_latency`

7.0.0gauge / NanosecondsAverage latency observed by the index scans, for this index

`index_cache_hits`

7.0.0counterThe number of times the required index page for both scan and mutations is found in memory, for this index

`index_cache_misses`

7.0.0counterThe number of times the required index page for both scan and mutations is NOT found in memory, for this index

`index_codebook_mem_usage`

7.7counter / bytesAmount of memory used by codebook for this index, includes memory used for coarse codebook and quantization codebook

`index_codebook_train_duration`

7.7counter / NanosecondsAmount of time spent in training the codebook, for this index

`index_data_size`

7.0.0gauge / bytesThe approximate size of the valid uncompressed index data, for this index

`index_data_size_on_disk`

7.0.0gauge / bytesThe size of the valid compressed index data, for this index

`index_disk_bytes`

7.6.4counter / bytesNumber of bytes read from and written to disk, including insert, get, and delete operations

`index_disk_size`

7.0.0gauge / bytesTotal disk space taken up by this index, after compression. This includes index data files, checkpoints etc.

`index_frag_percent`

7.0.0gaugePercentage of invalid index data, for this index

`index_heap_in_use`

7.0.0gauge / bytesTotal heap memory in use by indexer process in the node

`index_items_count`

7.0.0gaugeThe actual number of items present in the latest index snapshot, for this index

`index_log_space_on_disk`

7.0.0gauge / bytesThe size of the index data files - including garbage, for this index

`index_memory_quota`

7.0.0gauge / bytesConfigured memory quota for the index service nodes

`index_memory_rss`

7.2.0gauge / bytesResident set size of the indexer process, running on this node

`index_memory_total_storage`

7.2.0gauge / bytesAmount of memory used by the index memory allocator, on this node

`index_memory_used`

7.0.0gauge / bytesThe memory used by this index

`index_memory_used_storage`

7.2.0gauge / bytesAmount of memory used by underlying index storage, on this node

`index_memory_used_total`

7.0.0gauge / bytesTotal memory used by the indexer process

`index_net_avg_scan_rate`

7.0.0gaugeAverage index scan rate across all indexes, for this node

`index_num_diverging_replica_indexes`

8.0.0gaugeNumber of index partitions with diverging replica item counts.

`index_num_docs_indexed`

7.0.0counterNumber of document updates (of type insert, modify, delete) observed by this index

`index_num_docs_pending`

7.0.0gaugeNumber of pending updates that are yet to be received by index service, for this index

`index_num_docs_queued`

7.0.0gaugeNumber of updates queued (but not yet processed) by index service, for this index

`index_num_indexes`

7.2.0gaugeTotal number of indexes, located on this node

`index_num_items_flushed`

7.6.4counterNumber of documents written from memory to index storage

`index_num_requests`

7.0.0counterNumber of scan requests received by the index service, for this index

`index_num_rows_returned`

7.0.0counterNumber of rows/index entries returned as the scan result during index scans, for this index

`index_num_rows_scanned`

7.0.0counterNumber of rows/index entries read during the index scans, for this index

`index_num_storage_instances`

7.2.0gaugeTotal number of storage instances, located on this node

`index_partn_is_diverging_replica`

8.0.0gaugeSet to '1' if the index partition has diverging replica item counts

`index_partn_items_count`

7.6.6gaugeThe actual number of items present in the latest index snapshot, for this partition

`index_raw_data_size`

7.0.0gauge / bytesEncoded, uncompressed size of the index data, for this index

`index_recs_in_mem`

7.0.0gaugeNumber of index entries cached in memory, for this index

`index_recs_on_disk`

7.0.0gaugeNumber of index entries stored on disk, which are not cached in memory, for this index

`index_resident_percent`

7.0.0gaugeRatio of records in memory to total records, for this index

`index_scan_bytes_read`

7.0.0counter / bytesNumber of bytes read from the index storage during index scans, for this index

`index_scan_cache_hits`

8.0counterNumber of times the required index page for serving scan request is found in memory, for this index

`index_scan_cache_misses`

8.0counterNumber of times the required index page for serving scan request is NOT found in memory, for this index

`index_state`

7.6.6gaugeThe current state of this index; CREATED: 0, READY: 1, INITIAL: 2, CATCHUP: 3, ACTIVE: 4, DELETED: 5, ERROR: 6, NIL: 7, SCHEDULED: 8, RECOVERED: 9\. Index is usable only in ACTIVE state

`index_storage_avg_item_size`

7.6.0gauge / bytesRatio of total item size and total records

`index_storage_bytes_incoming`

7.6.0gauge / bytesAggregated total of bytes that are added to the stores and intended to be written on disc

`index_storage_bytes_written`

7.6.0gauge / bytesAggregated total of bytes written to the disc(data and recovery)

`index_storage_cleaner_blk_read_bs`

7.6.0gauge / bytesTotal of number bytes read for cleaner log reads (both data and recovery)

`index_storage_cleaner_num_reads`

7.6.0gaugeTotal of number of cleaner log reads (both data and recovery)

`index_storage_compression_ratio`

7.6.0gauge / bytesRatio of cumulative number of page bytes compressed and cumulative number of page bytes after compression

`index_storage_current_quota`

7.6.0gauge / bytesPlasma's internally active memory quota for this node. It is tuned by memtuner.

`index_storage_heap_limit`

7.6.0gauge / bytesPlasma's global heap limit for managed memory for this node

`index_storage_hvi_blk_read_bs`

8.0.0gaugeTotal number of bytes that were read from disk into memory

`index_storage_hvi_blk_reads_bs_get`

8.0.0gaugeTotal number of bytes that were read from disk into memory for index scans

`index_storage_hvi_blk_reads_bs_lookup`

8.0.0gaugeTotal number of bytes that were read from disk into memory for lookups

`index_storage_hvi_buf_memused`

8.0.0gaugeTotal Memory used by various reusable buffers

`index_storage_hvi_bytes_incoming`

8.0.0gaugeTotal number of bytes that were added to the stores and intended to be written to disk

`index_storage_hvi_bytes_written`

8.0.0gaugeTotal number of bytes that were written to disk

`index_storage_hvi_compacts`

8.0.0gaugeTotal count of compaction operations performed

`index_storage_hvi_compression_ratio_avg`

8.0.0gaugeRatio of data bytes to be compressed and data bytes after compression

`index_storage_hvi_fragmentation`

8.0.0gaugeThe fraction of garbage data present on disk

`index_storage_hvi_memory_used`

8.0.0gaugeTotal memory used by HVI indexes

`index_storage_hvi_num_reads`

8.0.0gaugeTotal number of times a disk block is read into memory

`index_storage_hvi_num_reads_get`

8.0.0gaugeTotal number of times a disk block was read into memory due to index scans

`index_storage_hvi_num_reads_lookup`

8.0.0gaugeTotal number of times a disk block was read into memory due to lookups

`index_storage_hvi_resident_ratio`

8.0.0gaugeRatio of cache mem used and cacheable size

`index_storage_hvi_total_disk_size`

8.0.0gaugeTotal disk usage in bytes

`index_storage_hvi_total_used_size`

8.0.0gaugeTotal number of disk bytes used. This size is eligible for cleanups in subsequent compactions.

`index_storage_items_count`

7.6.0gaugeAggregated number of items that are currently in the stores

`index_storage_lookup_blk_reads_bs`

7.6.0gauge / bytesTotal number of bytes that were read from disc into memory for lookups

`index_storage_lookup_num_reads`

7.6.0gaugeTotal number of LSS lookups for looking up items from stores

`index_storage_lss_blk_rdr_reads_bs`

7.6.0gauge / bytesTotal number of bytes that were read from disc into memory from the logs(both data and recovery) for index scans

`index_storage_lss_blk_read_bs`

7.6.0gauge / bytesTotal number of bytes that were read from disc into memory from the logs(both data and recovery)

`index_storage_lss_fragmentation`

7.6.0gaugeThe fraction of garbage data present in the logs

`index_storage_lss_num_reads`

7.6.0gaugeTotal number of times an LSS(both data and recovery) block is read from disk into memory

`index_storage_lss_used_space`

7.6.0gauge / bytesTotal number of bytes used by data and recovery logs

`index_storage_memory_stats_size_page`

7.6.0gauge / bytesAggregated number of bytes of memory currently in use by Plasma for page records

`index_storage_num_burst_visits`

7.6.0gaugeAggregated total of pages visited during burst eviction

`index_storage_num_evictable`

7.6.0gaugeAggregated total of the number of pages can be compressed

`index_storage_num_evicted`

7.6.0gaugeAggregated total of the number of pages that were evicted and persisted to disc

`index_storage_num_pages`

7.6.0gaugeAggregated number of pages that are currently in use

`index_storage_num_periodic_visits`

7.6.0gaugeAggregated total of pages visited during periodic eviction

`index_storage_purges`

7.6.0gaugeAggregated number of times various pages are compacted due to the MVCCPurger being triggered

`index_storage_reclaim_pending_global`

7.6.0gauge / bytesAggregated number of bytes across all plasma instances which have been freed but not yet returned to OS

`index_storage_resident_ratio`

7.6.0gaugeRatio of cached records and total records

`index_storage_rlss_num_reads`

7.6.0gaugeTotal number of times an LSS block was read into memory due to index scans

`index_total_data_size`

7.2.0gauge / bytesSum of data size of all indexes, located on this node

`index_total_disk_size`

7.2.0gauge / bytesSum of disk size of all indexes, located on this node

`index_total_drain_rate`

7.2.0gaugeSum of drain rate of all indexes, located on this node

`index_total_mutation_queue_size`

7.0.0gaugeTotal number of index updates queued in the mutation queues, on this node

`index_total_pending_scans`

7.0.0gaugeSum of number of pending scans across all indexes, located on this node

`index_total_raw_data_size`

7.0.0gauge / bytesSum of encoded, uncompressed size of the index data across all indexes, located on this node

`index_total_requests`

7.2.0counterSum of number of requests received by all indexes, located on this node

`index_total_rows_returned`

7.2.0counterSum of number of rows returned during index scan across all indexes, located on this node

`index_total_rows_scanned`

7.2.0counterSum of number of rows scanned during index scans across all indexes, located on this node

`index_total_scan_duration`

7.0.0counter / NanosecondsTotal time taken by the scans requests, for this index