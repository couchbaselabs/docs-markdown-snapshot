---
title: Index Service Metrics
description: A list of the metrics provided by the Index Service.
pubDate: 2026-08-18T04:50:45.818Z
antora:
  editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/metrics-reference/pages/index-service-metrics.adoc
  xref: xref:cloud:metrics-reference:index-service-metrics.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/metrics-reference/index-service-metrics.html)

# Index Service Metrics

> A list of the metrics provided by the Index Service. 

> [!TIP]
> * The x.y.z badge shows the Couchbase Server version the metric was added in.
> * The type / unit badge shows shows the Prometheus [type](https://prometheus.io/docs/tutorials/understanding%5Fmetric%5Ftypes/) and [unit](https://prometheus.io/docs/practices/naming/#base-units) (if present).

`index_avg_disk_bps`

7.2.0 gauge Sum of disk bytes written per second, of all indexes, located on this node

`index_avg_drain_rate`

7.0.0 gauge Average number of documents indexed per second, for this index

`index_avg_item_size`

7.0.0 gauge / bytes Average size of the indexed items, for this index

`index_avg_mutation_rate`

7.2.0 gauge Sum of mutation rates of all indexes, located on this node

`index_avg_resident_percent`

7.2.0 gauge Average resident percent across all indexes, located on this node

`index_avg_scan_latency`

7.0.0 gauge / Nanoseconds Average latency observed by the index scans, for this index

`index_cache_hits`

7.0.0 counter The number of times the required index page for both scan and mutations is found in memory, for this index

`index_cache_misses`

7.0.0 counter The number of times the required index page for both scan and mutations is NOT found in memory, for this index

`index_codebook_mem_usage`

7.7 counter / bytes Amount of memory used by codebook for this index, includes memory used for coarse codebook and quantization codebook

`index_codebook_train_duration`

7.7 counter / Nanoseconds Amount of time spent in training the codebook, for this index

`index_data_size`

7.0.0 gauge / bytes The approximate size of the valid uncompressed index data, for this index

`index_data_size_on_disk`

7.0.0 gauge / bytes The size of the valid compressed index data, for this index

`index_disk_bytes`

7.6.4 counter / bytes Number of bytes read from and written to disk, including insert, get, and delete operations

`index_disk_size`

7.0.0 gauge / bytes Total disk space taken up by this index, after compression. This includes index data files, checkpoints etc.

`index_frag_percent`

7.0.0 gauge Percentage of invalid index data, for this index

`index_heap_in_use`

7.0.0 gauge / bytes Total heap memory in use by indexer process in the node

`index_items_count`

7.0.0 gauge The actual number of items present in the latest index snapshot, for this index

`index_log_space_on_disk`

7.0.0 gauge / bytes The size of the index data files - including garbage, for this index

`index_memory_quota`

7.0.0 gauge / bytes Configured memory quota for the index service nodes

`index_memory_rss`

7.2.0 gauge / bytes Resident set size of the indexer process, running on this node

`index_memory_total_storage`

7.2.0 gauge / bytes Amount of memory used by the index memory allocator, on this node

`index_memory_used`

7.0.0 gauge / bytes The memory used by this index

`index_memory_used_storage`

7.2.0 gauge / bytes Amount of memory used by underlying index storage, on this node

`index_memory_used_total`

7.0.0 gauge / bytes Total memory used by the indexer process

`index_net_avg_scan_rate`

7.0.0 gauge Average index scan rate across all indexes, for this node

`index_num_diverging_replica_indexes`

8.0.0 gauge Number of index partitions with diverging replica item counts.

`index_num_docs_indexed`

7.0.0 counter Number of document updates (of type insert, modify, delete) observed by this index

`index_num_docs_pending`

7.0.0 gauge Number of pending updates that are yet to be received by index service, for this index

`index_num_docs_queued`

7.0.0 gauge Number of updates queued (but not yet processed) by index service, for this index

`index_num_indexes`

7.2.0 gauge Total number of indexes, located on this node

`index_num_items_flushed`

7.6.4 counter Number of documents written from memory to index storage

`index_num_requests`

7.0.0 counter Number of scan requests received by the index service, for this index

`index_num_rows_returned`

7.0.0 counter Number of rows/index entries returned as the scan result during index scans, for this index

`index_num_rows_scanned`

7.0.0 counter Number of rows/index entries read during the index scans, for this index

`index_num_storage_instances`

7.2.0 gauge Total number of storage instances, located on this node

`index_partn_is_diverging_replica`

8.0.0 gauge Set to '1' if the index partition has diverging replica item counts

`index_partn_items_count`

7.6.6 gauge The actual number of items present in the latest index snapshot, for this partition

`index_raw_data_size`

7.0.0 gauge / bytes Encoded, uncompressed size of the index data, for this index

`index_recs_in_mem`

7.0.0 gauge Number of index entries cached in memory, for this index

`index_recs_on_disk`

7.0.0 gauge Number of index entries stored on disk, which are not cached in memory, for this index

`index_resident_percent`

7.0.0 gauge Ratio of records in memory to total records, for this index

`index_scan_bytes_read`

7.0.0 counter / bytes Number of bytes read from the index storage during index scans, for this index

`index_scan_cache_hits`

8.0 counter Number of times the required index page for serving scan request is found in memory, for this index

`index_scan_cache_misses`

8.0 counter Number of times the required index page for serving scan request is NOT found in memory, for this index

`index_state`

7.6.6 gauge The current state of this index; CREATED: 0, READY: 1, INITIAL: 2, CATCHUP: 3, ACTIVE: 4, DELETED: 5, ERROR: 6, NIL: 7, SCHEDULED: 8, RECOVERED: 9\. Index is usable only in ACTIVE state

`index_storage_avg_item_size`

7.6.0 gauge / bytes Ratio of total item size and total records

`index_storage_bytes_incoming`

7.6.0 gauge / bytes Aggregated total of bytes that are added to the stores and intended to be written on disc

`index_storage_bytes_written`

7.6.0 gauge / bytes Aggregated total of bytes written to the disc(data and recovery)

`index_storage_cleaner_blk_read_bs`

7.6.0 gauge / bytes Total of number bytes read for cleaner log reads (both data and recovery)

`index_storage_cleaner_num_reads`

7.6.0 gauge Total of number of cleaner log reads (both data and recovery)

`index_storage_compression_ratio`

7.6.0 gauge / bytes Ratio of cumulative number of page bytes compressed and cumulative number of page bytes after compression

`index_storage_current_quota`

7.6.0 gauge / bytes Plasma's internally active memory quota for this node. It is tuned by memtuner.

`index_storage_heap_limit`

7.6.0 gauge / bytes Plasma's global heap limit for managed memory for this node

`index_storage_hvi_blk_read_bs`

8.0.0 gauge Total number of bytes that were read from disk into memory

`index_storage_hvi_blk_reads_bs_get`

8.0.0 gauge Total number of bytes that were read from disk into memory for index scans

`index_storage_hvi_blk_reads_bs_lookup`

8.0.0 gauge Total number of bytes that were read from disk into memory for lookups

`index_storage_hvi_buf_memused`

8.0.0 gauge Total Memory used by various reusable buffers

`index_storage_hvi_bytes_incoming`

8.0.0 gauge Total number of bytes that were added to the stores and intended to be written to disk

`index_storage_hvi_bytes_written`

8.0.0 gauge Total number of bytes that were written to disk

`index_storage_hvi_compacts`

8.0.0 gauge Total count of compaction operations performed

`index_storage_hvi_compression_ratio_avg`

8.0.0 gauge Ratio of data bytes to be compressed and data bytes after compression

`index_storage_hvi_fragmentation`

8.0.0 gauge The fraction of garbage data present on disk

`index_storage_hvi_memory_used`

8.0.0 gauge Total memory used by HVI indexes

`index_storage_hvi_num_reads`

8.0.0 gauge Total number of times a disk block is read into memory

`index_storage_hvi_num_reads_get`

8.0.0 gauge Total number of times a disk block was read into memory due to index scans

`index_storage_hvi_num_reads_lookup`

8.0.0 gauge Total number of times a disk block was read into memory due to lookups

`index_storage_hvi_resident_ratio`

8.0.0 gauge Ratio of cache mem used and cacheable size

`index_storage_hvi_total_disk_size`

8.0.0 gauge Total disk usage in bytes

`index_storage_hvi_total_used_size`

8.0.0 gauge Total number of disk bytes used. This size is eligible for cleanups in subsequent compactions.

`index_storage_items_count`

7.6.0 gauge Aggregated number of items that are currently in the stores

`index_storage_lookup_blk_reads_bs`

7.6.0 gauge / bytes Total number of bytes that were read from disc into memory for lookups

`index_storage_lookup_num_reads`

7.6.0 gauge Total number of LSS lookups for looking up items from stores

`index_storage_lss_blk_rdr_reads_bs`

7.6.0 gauge / bytes Total number of bytes that were read from disc into memory from the logs(both data and recovery) for index scans

`index_storage_lss_blk_read_bs`

7.6.0 gauge / bytes Total number of bytes that were read from disc into memory from the logs(both data and recovery)

`index_storage_lss_fragmentation`

7.6.0 gauge The fraction of garbage data present in the logs

`index_storage_lss_num_reads`

7.6.0 gauge Total number of times an LSS(both data and recovery) block is read from disk into memory

`index_storage_lss_used_space`

7.6.0 gauge / bytes Total number of bytes used by data and recovery logs

`index_storage_memory_stats_size_page`

7.6.0 gauge / bytes Aggregated number of bytes of memory currently in use by Plasma for page records

`index_storage_num_burst_visits`

7.6.0 gauge Aggregated total of pages visited during burst eviction

`index_storage_num_evictable`

7.6.0 gauge Aggregated total of the number of pages can be compressed

`index_storage_num_evicted`

7.6.0 gauge Aggregated total of the number of pages that were evicted and persisted to disc

`index_storage_num_pages`

7.6.0 gauge Aggregated number of pages that are currently in use

`index_storage_num_periodic_visits`

7.6.0 gauge Aggregated total of pages visited during periodic eviction

`index_storage_purges`

7.6.0 gauge Aggregated number of times various pages are compacted due to the MVCCPurger being triggered

`index_storage_reclaim_pending_global`

7.6.0 gauge / bytes Aggregated number of bytes across all plasma instances which have been freed but not yet returned to OS

`index_storage_resident_ratio`

7.6.0 gauge Ratio of cached records and total records

`index_storage_rlss_num_reads`

7.6.0 gauge Total number of times an LSS block was read into memory due to index scans

`index_total_data_size`

7.2.0 gauge / bytes Sum of data size of all indexes, located on this node

`index_total_disk_size`

7.2.0 gauge / bytes Sum of disk size of all indexes, located on this node

`index_total_drain_rate`

7.2.0 gauge Sum of drain rate of all indexes, located on this node

`index_total_mutation_queue_size`

7.0.0 gauge Total number of index updates queued in the mutation queues, on this node

`index_total_pending_scans`

7.0.0 gauge Sum of number of pending scans across all indexes, located on this node

`index_total_raw_data_size`

7.0.0 gauge / bytes Sum of encoded, uncompressed size of the index data across all indexes, located on this node

`index_total_requests`

7.2.0 counter Sum of number of requests received by all indexes, located on this node

`index_total_rows_returned`

7.2.0 counter Sum of number of rows returned during index scan across all indexes, located on this node

`index_total_rows_scanned`

7.2.0 counter Sum of number of rows scanned during index scans across all indexes, located on this node

`index_total_scan_duration`

7.0.0 counter / Nanoseconds Total time taken by the scans requests, for this index