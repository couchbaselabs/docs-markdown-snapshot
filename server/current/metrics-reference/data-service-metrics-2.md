---
title: Data Service Metrics
description: A list of the metrics provided by the Data Service (page 2).
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/metrics-reference/pages/data-service-metrics-2.adoc
pubDate: 2026-08-13T05:04:50.295Z
link: xref:server:metrics-reference:data-service-metrics-2.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/metrics-reference/data-service-metrics-2.html)

# Data Service Metrics

> A list of the metrics provided by the Data Service (page 2). 

Continued from [page 1](data-service-metrics.md).

> [!TIP]
> * The x.y.z badge shows the Couchbase Server version the metric was added in.
> * The type / unit badge shows shows the Prometheus [type](https://prometheus.io/docs/tutorials/understanding%5Fmetric%5Ftypes/) and [unit](https://prometheus.io/docs/practices/naming/#base-units) (if present).

`kv_ep_history_retention_seconds`

7.0.0gaugeSeconds of history the bucket should aim to retain on disk.

`kv_ep_hlc_drift_ahead_threshold_us`

7.0.0gaugeThe μs threshold of drift at which we will increment a vbucket's ahead counter.

`kv_ep_hlc_drift_behind_threshold_us`

7.0.0gaugeThe μs threshold of drift at which we will increment a vbucket's behind counter.

`kv_ep_hlc_drift_count`

7.0.0gaugeThe accumulated number of times the corresponding kv\_ep\_hlc\_drift\_count has been updated

`kv_ep_hlc_drift_seconds`

7.0.0gauge / secondsThe accumulated drift between this node's HLC and the remote node. For active vbucket's this represents the difference in CAS and local HLC for withMeta operations, for replica vbucket's this represents the difference in CAS and local HLC from DCP replication.

`kv_ep_hlc_max_future_threshold_us`

7.0.0gaugeThe acceptable μs threshold of drift at which we accept a new cas value.

`kv_ep_ht_item_memory_bytes`

7.1.0gauge / bytesThe total byte size of all items, no matter the vbucket's state, no matter if an item's value is ejected. Tracks the same value as ep\_total\_cache\_size

`kv_ep_ht_locks`

7.0.0gauge

`kv_ep_ht_resize_interval`

7.0.0gaugeInterval in seconds to wait between HashtableResizerTask executions.

`kv_ep_ht_size`

7.0.0gaugeThe initial and minimum number of slots in HashTable objects.

`kv_ep_ht_size_decrease_delay`

7.0.0gaugeDelay in seconds before decreasing the size of a HashTable following a previous resize.

`kv_ep_ht_temp_items_allowed_percent`

7.0.0gauge

`kv_ep_io_bg_fetch_read_count`

7.0.0gaugeAccumulated count of read system calls issued by BG fetches, only maintained by couchstore buckets

`kv_ep_io_compaction_read_bytes_bytes`

7.0.0gauge / bytesTotal number of bytes read during compaction

`kv_ep_io_compaction_write_bytes_bytes`

7.0.0gauge / bytesTotal number of bytes written during compaction

`kv_ep_io_document_write_bytes_bytes`

7.0.0gauge / bytesTotal number of bytes written. Only maintained by couchstore buckets and includes Couchstore B-Tree and other overheads

`kv_ep_io_total_read_bytes_bytes`

7.0.0gauge / bytesTotal number of bytes read

`kv_ep_io_total_write_bytes_bytes`

7.0.0gauge / bytesTotal number of bytes written

`kv_ep_item_begin_failed`

7.0.0gaugeNumber of times a transaction failed to start due to storage errors

`kv_ep_item_commit_failed`

7.0.0gaugeNumber of times a transaction failed to commit due to storage errors

`kv_ep_item_compressor_chunk_duration`

7.0.0gaugeMaximum time (in ms) item compression task will run for before being paused (and resumed at the next item\_compressor\_interval).

`kv_ep_item_compressor_interval`

7.0.0gaugeHow often the item compressor task should run (in milliseconds)

`kv_ep_item_compressor_num_compressed`

7.0.0gaugeNumber of items compressed by the item compressor task.

`kv_ep_item_compressor_num_visited`

7.0.0gaugeNumber of items visited (considered for compression) by the item compressor task.

`kv_ep_item_eviction_age_percentage`

7.0.0gaugeThe age percentage used when determining the age threshold in the learning\_age\_and\_mfu eviction policy.

`kv_ep_item_eviction_freq_counter_age_threshold`

7.0.0gauge

`kv_ep_item_eviction_initial_mfu_percentile`

7.0.0gaugePercentile of existing item MFU distribution to use to determine the MFU to give to new items (0 would insert new items with MFU equal to that of the coldest item present; 100 to that of hottest item present) for the upfront\_mfu\_only eviction strategy.

`kv_ep_item_eviction_initial_mfu_update_interval`

7.0.0gaugeTime between updates of the initial MFU given to new items (seconds)

`kv_ep_item_flush_expired`

7.0.0gaugeNumber of times an item is not flushed due to the expiry of the item

`kv_ep_item_flush_failed`

7.0.0gaugeNumber of times an item failed to flush due to storage errors

`kv_ep_item_freq_decayer_chunk_duration`

7.0.0gaugeMaximum time (in ms) itemFreqDecayer task will run for before being paused.

`kv_ep_item_freq_decayer_percent`

7.0.0gaugeThe percent that the frequency counter of a document is decayed when visited by item\_freq\_decayer.

`kv_ep_item_num`

7.0.0gaugeThe number of item objects allocated

`kv_ep_item_num_allocated_total`

7.6.0counterThe number of item object allocations

`kv_ep_item_num_freed_total`

7.6.0counterThe number of item object deallocations

`kv_ep_items_expelled_from_checkpoints`

7.0.0counterNumber of items expelled from checkpoints. Expelled refers to items that have been ejected from memory but are still considered to be part of the checkpoint.

`kv_ep_items_rm_from_checkpoints`

7.0.0counterNumber of items removed from closed unreferenced checkpoints

`kv_ep_key_value_size_bytes`

7.0.0gauge / bytesMemory used to store items metadata, keys and values in the system, no matter the vbucket's state

`kv_ep_magma_active_disk_usage_bytes`

7.2.0gauge / bytesCompressed disk size of latest version of the LSM Trees. This includes history

`kv_ep_magma_block_cache_hits`

7.1.0gaugeNumber of block cache hits

`kv_ep_magma_block_cache_mem_used_bytes`

7.1.0gauge / bytesMemory used by block cache. Accounts for allocated size of blocks that includes allocator internal fragmentation and any internal cache overheads due to auxilliary structures

`kv_ep_magma_block_cache_misses`

7.1.0gaugeNumber of block cache misses

`kv_ep_magma_bloom_filter_accuracy`

7.0.0gaugeMagma maintains a bloom filter per sstable in the LSMTree. The bloom filters are used to reduce IO in case of non-existent This config sets the accuracy of the bloom filters ie. (1 - accuracy) = false positive rate

`kv_ep_magma_bloom_filter_accuracy_for_bottom_level`

7.0.0gaugeThe bloom filters at the bottom level are used to avoid IO in case of non-existent keys. Also most of the data resides in the bottom level. This config allows for lowering of bloom filter accuracy of sstables residing in the lowermost level of the LSMTree.

`kv_ep_magma_bloom_filter_mem_used_bytes`

7.1.0gauge / bytesBloom filter memory usage in all versions of the LSM Trees

`kv_ep_magma_buffer_mem_used_bytes`

7.1.0gauge / bytesMemory usage for some buffers

`kv_ep_magma_bytes_incoming_bytes`

7.1.0gauge / bytesData written to key, seq, local index as part of the KV frontend writes.

`kv_ep_magma_bytes_outgoing_bytes`

7.1.0gauge / bytesTotal bytes returned via get (excluding bytes returned from sequence iterator)

`kv_ep_magma_bytes_per_read_ratio`

7.1.0gauge / ratioBytes read by get / number of Gets

`kv_ep_magma_checkpoint_disk_usage_bytes`

7.2.0gauge / bytesCheckpoint overhead

`kv_ep_magma_checkpoint_interval`

7.0.0gaugeFrequency of checkpoint interval; in seconds. A checkpoint provides a rollback point to which the data store can rollback to in the event of a failure.

`kv_ep_magma_checkpoint_threshold`

7.0.0gaugeThreshold of data written before a checkpoint is created; threshold is based on a fraction of the total data size. Checkpoints require data to be retained in order to provide rollback capability. If the amount of data written during a checkpoint interval is large, we need to do more frequent checkpoints to reduce space amplification.

`kv_ep_magma_compactions`

7.1.0gaugeCount of Magma compactions in key, seq and local index.

`kv_ep_magma_data_blocks_compressed_size`

7.2.0gaugeData blocks compressed size; actual size in storage

`kv_ep_magma_data_blocks_compression_ratio_ratio`

7.2.0gauge / ratioThe compression ratio calculated by dividing the uncompressed data size by the compressed data size

`kv_ep_magma_data_blocks_space_reduction_estimate_pct_ratio`

7.2.0gauge / ratioEstimated percentage of space savings in compressed data blocks (0-100)

`kv_ep_magma_data_blocks_uncompressed_size`

7.2.0gaugeData blocks uncompressed size

`kv_ep_magma_delete_frag_ratio`

7.0.0gaugeMagma compaction always removes duplicate keys but not all sstables are visited during compaction.. This is the minimum fragmentation ratio threshold for when a compaction will be triggerred.

`kv_ep_magma_delete_memtable_writecache`

7.0.0gaugeMagma uses a lazy update model to maintain the sequence index. It maintains a list of deleted seq #s that were deleted from the key Index.

`kv_ep_magma_drop_encryption_keys_compactions`

8.0.0gaugeCount of Magma compactions issued to drop older encryption keys.

`kv_ep_magma_enable_block_cache`

7.0.0gaugeThe block cache is an LRU policy driven cache that is used to maintain index blocks for the sstable's btrees.

`kv_ep_magma_enable_direct_io`

7.0.0gaugeUsing direct IO tells magma to bypass the file system cache when writing or reading sstables.

`kv_ep_magma_enable_group_commit`

7.0.0gaugeGroup Commit allows transactions in magma to be grouped together to reduce the number of WAL fsyncs. When a transaction is ready to fsync, if there are new transactions waiting to start, we stall the transaction waiting to fsync until there are no more transactions waiting to start for a given magma instance.

`kv_ep_magma_enable_memory_optimized_writes`

7.0.0gaugeWhen enabled, if copying a write batch into memtable results in exceeding the write cache quota, Magma avoids the copy and instead flushes the batch to disk on the writer thread itself. This tradeoffs an increase in write latency for reduced memory consumption and obeys quota limits. If copying a batch keeps us under the quota, Magma will to continue to copy and do the flush in background.

`kv_ep_magma_enable_upsert`

7.0.0gaugeWhen true, the kv\_engine will utilize Magma's upsert capabiltiy but accurate document counts for the data store or collections can not be maintained.

`kv_ep_magma_enable_wal`

7.0.0gaugeWAL ensures Magma's atomicity, durability. Disabling it is useful in performance analysis.

`kv_ep_magma_expiry_frag_threshold`

7.0.0gaugeAll compactions perform expiry but not all sstables are visited by compaction. Magma maintains an expiry histogram across the kvstore to help determine which range of sstables need to have compaction run on them because there are a significant number of expired items. The frag threshold is the number of expired keys vs keys in the data store.

`kv_ep_magma_expiry_purger_interval`

7.0.0gaugeMagma maintains statistics about expired documents to run compaction based on magma\_expiry\_frag\_threshold. This config determines the the expiry purger polling interval in seconds to trigger compaction on eligible sstables

`kv_ep_magma_filecount_compactions`

7.1.0gaugeNumber of compactions triggered by file count

`kv_ep_magma_flusher_thread_percentage`

7.0.0gaugePercentage of storage threads that are flusher threads (i.e. with a value of 20 we will allocate 4 (1/5th) of the storage threads to flushers and the remaining 16 (4/5ths) threads will be compactors).

`kv_ep_magma_flushes`

7.1.0gaugeNumber of write cache flushes performed

`kv_ep_magma_fragmentation_percentage`

7.0.0gaugeThe percentage of fragmentation a magma bucket aims to maintain. A 100 value will disable sequence tree compactions by setting the desired fragmentation percentage to 100%. Smaller compactions of the key and local indexes will still run.

`kv_ep_magma_fragmentation_ratio`

7.1.0gauge / ratioFragmentation on disk (excludes history)

`kv_ep_magma_fusion_log_checkpoint_interval`

7.0.0gaugeThe interval at which FusionFS should create a log checkpoint on the FusionMetadataStore and delete eligible logs from the FusionLogStore, in seconds.

`kv_ep_magma_fusion_logstore_fragmentation_threshold`

7.0.0gaugeThe threshold at which the fusion log store will perform garbage collection. This is a ratio between 0.0 and 1.0.

`kv_ep_magma_fusion_upload_interval`

7.0.0gaugeThe interval between kvstore syncs to fusion, in seconds.

`kv_ep_magma_gets`

7.1.0gaugeNumber of get operations

`kv_ep_magma_group_commit_max_sync_wait_duration_ms`

7.0.0gaugeWhen a transaction is about to stall because there are pending transactions waiting to start, if there already are transactions waiting and the oldest transaction has been waiting for magma\_group\_commit\_max\_sync\_wait\_duration ms or more, the current transaction will perform the fsync. When group commit is enabled and both magma\_group\_commit\_max\_sync\_wait\_duration and magma\_group\_commit\_max\_transaction\_count are set to 0, transactions will stall until there are no more transactions waiting to start. Unit is milliseconds.

`kv_ep_magma_group_commit_max_transaction_count`

7.0.0gaugeWhen a transaction is about to stall because there are pending transactions waiting to start, if there already are magma\_group\_commit\_max\_transaction\_count including the current transaction waiting, the current transaction will perform the fsync. When group commit is enabled and both magma\_group\_commit\_max\_sync\_wait\_duration and magma\_group\_commit\_max\_transaction\_count are set to 0, transactions will stall until there are no more transactions waiting to start.

`kv_ep_magma_heartbeat_interval`

7.0.0gaugeFrequency of heartbeat interval; in seconds. A heartbeat task is scheduled to provide cleanup and maintenance when magma is idle.

`kv_ep_magma_histogram_mem_used_bytes`

7.1.0gauge / bytesMemory usage for MagmaHistogramStats and file histograms

`kv_ep_magma_history_logical_data_size_bytes`

7.2.0gauge / bytesThe logical data size of history

`kv_ep_magma_history_logical_disk_size_bytes`

7.2.0gauge / bytesThe logical disk size of history

`kv_ep_magma_history_size_evicted_bytes`

7.2.0gauge / bytesHistory eviction bytes based on size

`kv_ep_magma_history_time_evicted_bytes`

7.2.0gauge / bytesHistory eviction bytes based on time

`kv_ep_magma_index_resident_ratio_ratio`

7.1.0gauge / ratioProportion of keyIndex (data+index blocks) and seqIndex (index blocks) in memory

`kv_ep_magma_initial_wal_buffer_size`

7.0.0gaugeThe WAL buffer is used to stage items to the write ahead log along with control information like begin and end transaction. This parameter refers to the initial WAL buffer size. The WAL buffer will adjust its size up to a maximum of 4MB or down to a minimum of 64KB depending on the transaction batch size with consideration for other magma components which consume memory such as the block cache, bloom filters, write cache and meta data overhead.

`kv_ep_magma_inserts`

7.1.0gaugeNumber of DocInsert operations

`kv_ep_magma_key_tree_data_block_size`

7.0.0gaugeMagma uses SSTables for storage. SSTables are made up of different types of blocks. Data blocks contain the bulk of the data and contain the key and metadata for each of the items in the block. Larger block sizes can decrease storage space by better block compression but they require more memory, cpu and io bandwidth to read and write them.

`kv_ep_magma_key_tree_index_block_size`

7.0.0gaugeMagma uses SSTables for storage. SSTables are made up of different types of blocks. Index blocks contain keys that help traverse the SSTable to locate the data item. Larger block sizes can decrease storage space by better block compression but they require more memory, cpu and io bandwidth to read and write them.

`kv_ep_magma_keyindex_filecount_compactions`

7.2.0gaugeNumber of compactions triggered by file count for the KeyIndex

`kv_ep_magma_keyindex_writer_compactions`

7.2.0gaugeNumber of compaction performed on the writer thread for the KeyIndex

`kv_ep_magma_logical_data_size_bytes`

7.1.0gauge / bytesThe logical data size, including history

`kv_ep_magma_logical_disk_size_bytes`

7.1.0gauge / bytesThe logical disk size, including history

`kv_ep_magma_lsmtree_object_mem_used_bytes`

7.1.0gauge / bytesMemory used by LSMTree objects

`kv_ep_magma_max_checkpoints`

7.0.0gaugeMaximum # of checkpoints retained for rollback.

`kv_ep_magma_max_default_storage_threads`

7.0.0gaugeIf the number of storage threads = 0, then we set the number of storage threads to this value and use magma\_flusher\_thread\_percentage to determine the ratio of flusher and compactor threads.

`kv_ep_magma_max_level_0_ttl`

7.0.0gaugeMaximum time (in seconds) that data is kept in level 0 before it is merged.

`kv_ep_magma_max_recovery_bytes`

7.0.0gaugeMaximum amount of data that is replayed from the WAL during magma recovery. When this threshold is reached magma, creates a temporary checkpoint to recover at. This is per kvstore and in bytes.

`kv_ep_magma_max_write_cache`

7.0.0gaugeMagma uses a common skiplist to buffer all items at the shard level called the write cache. The write cache contains items from all the kvstores that are part of the shard and when it is flushed, each kvstore will receive a few items each. Regardless of how much memory might be available, this would be the maximum amount that could be allocated.

`kv_ep_magma_mem_quota_low_watermark_ratio`

7.0.0gaugeFraction of memory quota used by magma as it's low water mark. Magma uses this low watermark to size it's write cache and block cache. This sizing includes bloom filters memory usage but bloom filter eviction is based on the memory quota

`kv_ep_magma_mem_quota_ratio`

7.0.0gaugeMagma total memory ratio of the Bucket Quota across all shards and Magma limit's it's memory usage to this value.

`kv_ep_magma_min_checkpoint_interval`

7.0.0gaugeMinimum interval between two checkpoints; in seconds. Prevents excessive creation of checkpoints.

`kv_ep_magma_min_value_block_size_threshold`

7.0.0gaugeMagma creates value blocks for values larger than this size. Value blocks only contain a single KV item and their reads/writes are optimised for lesser memory consumption as it avoids many value copies. For example, magma block compression is turned off for them as compression requires an output buffer as large as the input buffer. This is fine since for such large docs, per document Snappy compression already should give good enough space savings. This setting should be >= SeqIndex data block size or else it won't take effect.

`kv_ep_magma_per_document_compression_enabled`

7.0.0gaugeApply Snappy compression to each document when persisted (magma only)

`kv_ep_magma_read_ahead_buffer_mem_used_bytes`

7.1.0gauge / bytesMemory consumed by read ahead buffers. They are used for compactions and sequence iterators. This is included in BufferMemUsed

`kv_ep_magma_read_bytes_bytes`

7.1.0gauge / bytesTotal bytes read from disk as per Magma's manual accounting in various code paths

`kv_ep_magma_read_bytes_compact_bytes`

7.1.0gauge / bytesTotal bytes read from disk by compactors

`kv_ep_magma_read_bytes_get_bytes`

7.1.0gauge / bytesTotal bytes read from disk by gets

`kv_ep_magma_readamp_get_ratio`

7.1.0gauge / ratioBytes Read from disk by only Get threads / Bytes outgoing

`kv_ep_magma_readamp_ratio`

7.1.0gauge / ratioBytes read from disk / bytes outgoing. Bytes read from disk includes Gets and compactors (excluding WAL)

`kv_ep_magma_readio`

7.1.0gaugeNumber of read IOs performed

`kv_ep_magma_readioamp_ratio`

7.1.0gauge / ratioNumber of read IOs performed by GetDocs divided by the number of GetDocs

`kv_ep_magma_seq_tree_data_block_size`

7.0.0gaugeMagma uses SSTables for storage. SSTables are made up of different types of blocks. Data blocks contain the bulk of the data and contain the key, metadata and value for each of the items in the block. Larger block sizes can decrease storage space by better block compression but they require more memory, cpu and io bandwidth to read and write them. If this is less than magma\_min\_value\_block\_size\_threshold, Magma will internally auto configure the value block size to be as large as this.

`kv_ep_magma_seq_tree_index_block_size`

7.0.0gaugeMagma uses SSTables for storage. SSTables are made up of different types of blocks. Index blocks contain keys that help traverse the SSTable to locate the data item. Larger block sizes can decrease storage space by better block compression but they require more memory, cpu and io bandwidth to read and write them.

`kv_ep_magma_seqindex_data_compactions`

7.6.0gaugeCount of Magma compactions in seq index that compact the data level. This are already accounted in ep\_magma\_seqindex\_compactions hence not part of the magma\_compactions Prometheus stat family.

`kv_ep_magma_seqindex_delta_bytes_incoming_bytes`

7.6.0gauge / bytesData written to seq index delta levels as part of frontend update operations. This is already accounted in ep\_magma\_seqindex\_bytes\_incoming hence not part of Prometheus stat family magma\_bytes\_incoming.

`kv_ep_magma_seqindex_delta_write_bytes_bytes`

7.6.0gauge / bytesBytes written by Magma flushes, compactions of the seq index delta levels. This is already accounted into ep\_magma\_sequndex\_write\_bytes hence not part of the Prometheus stat family magma\_write\_bytes.

`kv_ep_magma_seqindex_filecount_compactions`

7.2.0gaugeNumber of compactions triggered by file count for the SeqIndex

`kv_ep_magma_seqindex_writer_compactions`

7.2.0gaugeNumber of compaction performed on the writer thread for the SeqIndex

`kv_ep_magma_sets`

7.1.0gaugeNumber of set operations (DocUpsert)

`kv_ep_magma_sync_every_batch`

7.0.0gaugeCouchstore generates a commit point at the end of every batch of items. During normal operation, Magma checkpoints are taken at every magma\_checkpoint\_interval. Many of the tests require more frequent checkpoints so this configuration parameter makes sure every batch generates a checkpoint. Each checkpoint generated in this way is a "Sync" checkpoint and isn't going to be useful for rollback as it only the latest checkpoint is a "Sync" checkpoiont. A "Rollback" checkpoint will be made instead if we set magma\_checkpoint\_interval to 0\. The "Rollback" checkpoints are stored in the checkpoint queue as potential rollback points. Should be used for testing only!

`kv_ep_magma_syncs`

7.1.0gaugeNumber of fsyncs performed

`kv_ep_magma_table_meta_mem_used_bytes`

7.1.0gauge / bytesMemory used by sstable metadata

`kv_ep_magma_table_object_mem_used_bytes`

7.1.0gauge / bytesMemory used by SSTable objects

`kv_ep_magma_tables`

7.1.0gaugeNumber of files used for tables

`kv_ep_magma_tables_created`

7.1.0gaugeNumber of table files created

`kv_ep_magma_tables_deleted`

7.1.0gaugeNumber of table files deleted

`kv_ep_magma_total_disk_usage_bytes`

7.1.0gauge / bytesCompressed size of all SSTables in all checkpoints, WAL and any other files on disk

`kv_ep_magma_total_mem_used_bytes`

7.1.0gauge / bytesTotal memory used by bloom filters, write cache, block cache and index blocks This account for all versions of the trees

`kv_ep_magma_tree_snapshot_mem_used_bytes`

7.6.0gauge / bytesMemory consumed by all LSMTree TreeSnapshots

`kv_ep_magma_ttl_compactions`

7.1.0gaugeNumber of time-to-live based compactions

`kv_ep_magma_wal_disk_usage_bytes`

7.1.0gauge / bytesDisk usage by the WAL

`kv_ep_magma_wal_mem_used_bytes`

7.1.0gauge / bytesTotal WAL memory used, including WAL buffer and any auxiliary memory

`kv_ep_magma_write_bytes_bytes`

7.1.0gauge / bytesBytes written by Magma flushes, compactions and WAL writes.

`kv_ep_magma_write_bytes_compact_bytes`

7.1.0gauge / bytesBytes written by Magma compactions.

`kv_ep_magma_write_cache_mem_used_bytes`

7.1.0gauge / bytesMemory usage of the write cache

`kv_ep_magma_write_cache_ratio`

7.0.0gaugeMemory is maintained across 3 magma components; Bloom filters, Block cache and Write cache. The least important of these is the write cache. If there is insufficent memory for the write cache, the write cache will grow to the size of the batch and then be immediately flushed and freed. If there is available memory, the write cache is limited to 20% of the available memory (after bloom filter and block cache get their memory up to magma\_max\_write\_cache (128MB). Bloom filters are the most important and are never paged out. Bloom filter memory can cause magma to go above the memory quota. To allevaite this, the bottom layer where the majority of bloom filter memory is, won't use bloom filters when OptimizeBloomFilterForMisses is on (which it is by default). The block cache grows each time the index sizes change. But its growth is bounded by the available memory or what's left over after the bloom filter memory is subtracted.

`kv_ep_magma_writer_compactions`

7.1.0gaugeNumber of compaction performed on the writer thread

`kv_ep_max_checkpoints`

7.0.0gaugeThe expected max number of checkpoints in each VBucket on a balanced system. Note: That is not a hard limit on the single vbucket. That is used (together with checkpoint\_memory\_ratio) for computing checkpoint\_max\_size, which triggers checkpoint creation.

`kv_ep_max_failover_entries`

7.0.0gaugemaximum number of failover log entries

`kv_ep_max_item_privileged_bytes`

7.0.0gaugeMaximum number of bytes allowed for 'privileged' (system) data for an item in addition to the max\_item\_size bytes

`kv_ep_max_item_size`

7.0.0gaugeMaximum number of bytes allowed for an item

`kv_ep_max_num_bgfetchers`

7.0.0gaugeMaximum number of bg fetcher objects (the number of concurrent bg fetch tasks we can run). 0 = auto-configure which means we use the same number as the number of reader threads (num\_reader\_threads).

`kv_ep_max_num_flushers`

7.0.0gaugeMaximum number of flusher objects (the number of concurrent flusher tasks we can run). 0 = auto-configure which means we use the same number as the number of shards (max\_num\_shards - for historic reasons). See also num\_writer\_threads.

`kv_ep_max_num_shards`

7.0.0gaugeMaximum mumber of shards (0 = auto-configure)

`kv_ep_max_num_workers`

7.0.0gaugeBucket Priority relative to other buckets

`kv_ep_max_size`

7.0.0gaugeMemory quota (in bytes) for this bucket.

`kv_ep_max_threads`

7.0.0gaugeMaximum number of threads of any single class (0 = automatically select based on core count)

`kv_ep_max_ttl`

7.0.0gaugeA maximum TTL (in seconds) that will apply to all new documents, documents set with no TTL will be given this value. A value of 0 means this is disabled

`kv_ep_max_vbuckets`

7.0.0gaugeMaximum number of vbuckets expected

`kv_ep_mem_freed_by_checkpoint_item_expel_bytes`

7.1.0gauge / bytesMemory recovered from Checkpoint by expelling clean items (i.e. items processed by all cursors) from the queue

`kv_ep_mem_freed_by_checkpoint_removal_bytes`

7.1.0gauge / bytesAmount of memory freed through ckpt removal

`kv_ep_mem_high_wat`

7.0.0gaugeThe bucket's memory used high watermark.

`kv_ep_mem_high_wat_percent`

7.0.0gaugeRatio of the Bucket Quota at which to place the high watermark. This is the maximum desired memory usage. This value should be lower than mutation\_mem\_ratio to avoid no memory errors.

`kv_ep_mem_low_wat`

7.0.0gaugeThe bucket's memory used low watermark.

`kv_ep_mem_low_wat_percent`

7.0.0gaugeRatio of the Bucket Quota at which to place the low watermark. This is the point to which to reduce the memory usage of the bucket after hitting the high watermark.

`kv_ep_mem_tracker_enabled`

7.0.0gaugeTrue if memory usage tracker is enabled

`kv_ep_mem_used_merge_threshold_percent`

7.0.0gaugeWhat percent of max\_data size should we allow the estimated total memory to lag by (EPStats::getEstimatedTotalMemoryUsed)

`kv_ep_meta_data_disk_bytes`

7.0.0gauge / bytesEstimate of how much metadata has been written to disk since startup

`kv_ep_meta_data_memory_bytes`

7.0.0gauge / bytesTotal memory used by meta data, including the key

`kv_ep_min_compression_ratio`

7.0.0gaugespecifies a minimum compression ratio below which storing the document will be stored as uncompressed.

`kv_ep_mutation_mem_ratio`

7.0.0gaugeRatio of the Bucket Quota that can be used before mutations return tmpOOMs

`kv_ep_not_locked_returns_tmpfail`

7.0.0gaugeControls which error code should be returned when attempting to unlock an item that is not locked. When value is true, the legacy temporary\_failure is used instead of not\_locked.

`kv_ep_num_access_scanner_runs`

7.0.0gaugeNumber of times we ran accesss scanner to snapshot working set

`kv_ep_num_access_scanner_skips`

7.0.0gaugeNumber of times accesss scanner task decided not to generate access log

`kv_ep_num_cas_regenerated`

8.0.0counterThe total number of CAS value regenerated

`kv_ep_num_checkpoints`

7.1.0gaugeThe number of checkpoint objects allocated

`kv_ep_num_checkpoints_allocated_total`

7.6.0counterThe number of checkpoint object allocations

`kv_ep_num_checkpoints_freed_total`

7.6.0counterThe number of checkpoint object deallocations

`kv_ep_num_checkpoints_pending_destruction`

7.6.0gaugeNumber of checkpoints detached from CM and owned by Destroyers

`kv_ep_num_eject_failures`

7.0.0counterNumber of items that could not be ejected

`kv_ep_num_expiry_pager_runs`

7.0.0counterNumber of times we ran expiry pager loops to purge expired items from memory/disk

`kv_ep_num_freq_decayer_runs`

7.0.0counterNumber of times we ran the freq decayer task because a frequency counter has become saturated

`kv_ep_num_invalid_cas`

8.0.0counterThe total number of invalid CAS values.

`kv_ep_num_non_resident`

7.0.0gaugeThe number of non-resident items

`kv_ep_num_not_my_vbuckets`

7.0.0counterNumber of times Not My VBucket exception happened during runtime

`kv_ep_num_pager_runs`

7.0.0counterNumber of times we ran pager loops to seek additional memory

`kv_ep_num_value_ejects`

7.0.0counterNumber of times item values got ejected from memory to disk

`kv_ep_num_workers`

7.0.0gaugeGlobal number of shared worker threads

`kv_ep_oom_errors`

7.0.0gaugeNumber of times unrecoverable OOMs happened while processing operations

`kv_ep_pager_sleep_time_ms`

7.0.0gaugeHow long in milliseconds the ItemPager will sleep for when not being requested to run

`kv_ep_paging_visitor_pause_check_count`

7.0.0gaugeExpected number of times the PagingVisitor will check the pause condition per vBucket

`kv_ep_pending_compactions`

7.0.0gaugeFor persistent buckets, the count of compaction tasks.

`kv_ep_pending_disk_ops_max_time_seconds`

8.0.0gauge / secondsThe longest time spent in a disk operation that is currently executing

`kv_ep_pending_ops`

7.0.0gaugeNumber of ops awaiting pending vbuckets

`kv_ep_pending_ops_max`

7.0.0gaugeMax ops seen awaiting 1 pending vbucket

`kv_ep_pending_ops_max_duration_seconds`

7.0.0gauge / secondsMax time (µs) used waiting on pending vbuckets

`kv_ep_pending_ops_total`

7.0.0counterTotal blocked pending ops since reset

`kv_ep_persist_vbstate_total`

7.0.0gaugeTotal VB persist state to disk

`kv_ep_persistent_metadata_purge_age`

7.0.0gaugeAge in seconds after which tombstones may be purged. Defaults to 3 days. Max of 60 days. If this is dynamically changed for a magma bucket then magma may not trigger compactions when it should, this can be avoided by running a full manual compaction after changing this parameter.

`kv_ep_primary_warmup_min_items_threshold`

7.0.0gaugeMark primary warm-up as complete when the number of values loaded by warm-up reaches this percentage of the available values. This is checked after evaluating primry\_warmup\_min\_memory\_threshold.

`kv_ep_primary_warmup_min_memory_threshold`

7.0.0gaugeMark primary warm-up as complete when bucket memory usage reaches this percentage of max\_data\_size. This is checked before evaluating primry\_warmup\_min\_items\_threshold.

`kv_ep_queue_size`

7.0.0gaugeNumber of items queued for storage

`kv_ep_range_scan_kv_store_scan_ratio`

7.0.0gaugeThe ratio for calculating how many RangeScans can exist, a ratio of total KVStore scans.

`kv_ep_range_scan_max_continue_tasks`

7.0.0gaugeThe maximum number of range scan tasks that can exist concurrently. Setting to 0 results in num\_auxio\_threads - 1 tasks

`kv_ep_range_scan_max_lifetime`

7.0.0gaugeThe maximum lifetime in seconds for a range-scan. Scans that don't complete before this limit are cancelled

`kv_ep_range_scan_read_buffer_send_size`

7.0.0gaugeThe size of a buffer used to store data read during the I/O phase of a range-scan-continue. Once the buffer size is >= to this value the data is sent to the connection

`kv_ep_retain_erroneous_tombstones`

7.0.0gaugewhether erroneous tombstones need to be retain during compaction. Erroneous tombstones are those that have invalid meta data in it. For example, a delete time of 0.

`kv_ep_rollback_count`

7.0.0gaugeNumber of rollbacks on consumer

`kv_ep_secondary_warmup_estimated_value_count`

8.0.0counterTo facilitate warm-up progress tracking this value represents how many values need to be loaded to reach 100% of values loaded. This counter is only initialised when warm-up reaches the "loading access log", "loading k/v pairs" or "loading data" state and the ratio of ep\_warmup\_value\_count and this provides insight into progress.

`kv_ep_secondary_warmup_min_items_threshold`

7.0.0gaugeStop secondary warm-up when the number of values loaded by warm-up reaches this percentage of the available values. This is checked after evaluating secondary\_warmup\_min\_memory\_threshold.

`kv_ep_secondary_warmup_min_memory_threshold`

7.0.0gaugeStop secondary warm-up when bucket memory usage reaches this percentage of max\_data\_size. This is checked before evaluating secondary\_warmup\_min\_items\_threshold.

`kv_ep_seqno_persistence_timeout`

7.0.0gaugeTimeout in seconds after which a pending SeqnoPersistence operation is temp-failed

`kv_ep_snapshot_read_bytes`

8.0.0gauge / bytesThe number of bytes read when copying/downloading snapshots

`kv_ep_startup_time_seconds`

7.0.0gauge / secondsSystem-generated engine startup time

`kv_ep_storedval_num`

7.0.0gaugeThe number of storedval objects allocated

`kv_ep_storedval_num_allocated_total`

7.6.0counterThe number of storedval object allocations

`kv_ep_storedval_num_freed_total`

7.6.0counterThe number of blob object deallocations

`kv_ep_storedval_size_allocated_total_bytes`

7.6.0counter / bytesThe total number of bytes ever allocated for storedval objects

`kv_ep_storedval_size_freed_total_bytes`

7.6.0counter / bytesThe total number of bytes ever freed by deallocated storedval objects

`kv_ep_sync_writes_max_allowed_replicas`

7.0.0gaugeThe maximum number of supported replicas for SyncWrites. Attempts to issue SyncWrites against a topology with more replicas than this setting will fail with DurabilityImpossible.

`kv_ep_tmp_oom_errors`

7.0.0counterNumber of times temporary OOMs happened while processing operations

`kv_ep_total_cache_size_bytes`

7.0.0gauge / bytesThe total byte size of all items, no matter the vbucket's state, no matter if an item's value is ejected. Tracks the same value as ep\_ht\_item\_memory

`kv_ep_total_deduplicated`

7.0.0gaugeTotal number of items de-duplicated when queued to CheckpointManager

`kv_ep_total_deduplicated_flusher`

7.2.0gaugeTotal number of items de-duplicated when flushed to disk

`kv_ep_total_del_items`

7.0.0gaugeTotal number of persisted deletions

`kv_ep_total_enqueued`

7.0.0gaugeTotal number of items queued for persistence

`kv_ep_total_new_items`

7.0.0gaugeTotal number of persisted new items

`kv_ep_total_persisted`

7.0.0gaugeTotal number of items persisted

`kv_ep_uncommitted_items`

7.0.0gaugeThe amount of items that have not been written to disk

`kv_ep_value_size_allocated_total_bytes`

7.6.0counter / bytesThe total number of bytes ever allocated for blob objects

`kv_ep_value_size_freed_total_bytes`

7.6.0counter / bytesThe total number of bytes ever freed by deallocated blob objects

`kv_ep_vb_total`

7.0.0gaugeTotal vBuckets (count)

`kv_ep_vbucket_del`

7.0.0gaugeNumber of vbucket deletion events

`kv_ep_vbucket_del_avg_walltime_seconds`

7.0.0gauge / secondsAvg wall time (µs) spent by deleting a vbucket

`kv_ep_vbucket_del_fail`

7.0.0gaugeNumber of failed vbucket deletion events

`kv_ep_vbucket_del_max_walltime_seconds`

7.0.0gauge / secondsMax wall time (µs) spent by deleting a vbucket

`kv_ep_vbucket_mapping_sanity_checking`

7.0.0gaugeAre vBucket mappings (key -> vBucket) checked by the server? This is a sanity checking mode which crc32 hashes the key to ensure that the client is supplying the expected vBucket for each key.

`kv_ep_warmup`

7.0.0gaugeIs Warmup of existing data enabled

`kv_ep_warmup_accesslog_load_batch_size`

7.0.0gaugeAccessLog loading operates in batches of this size (dictates the max number of keys issued to the KVStore::getMulti function)

`kv_ep_warmup_accesslog_load_duration`

7.0.0gaugeThe duration (in ms) after which warmup's LoadAccessLog phase will yield and re-schedule; allowing other tasks on the same thread pool to run.

`kv_ep_warmup_backfill_scan_chunk_duration`

7.0.0gaugeThe duration (in ms) after which warmup's backfill scans will yield and re-schedule; allowing other tasks on the same threads to run.

`kv_ep_warmup_backfill_task_shard_ratio`

7.0.0gaugeRatio controlling how many tasks that will be created in the KeyDump, LoadingKVPairs and LoadingData phases. This is a ratio using the number of shards as the denominator and least 1 task will be created per phase. A value of 0.0 will create tasks equal to the lower of #shards or #reader-threads, a value of 1.0 restores the orginal behaviour, 1 task per shard.

`kv_ep_warmup_dups`

7.0.0gaugeDuplicates encountered during warmup

`kv_ep_warmup_estimated_key_count`

7.1.0counterTo facilitate warm-up progress tracking this value represents how many keys need to be loaded to reach 100% keys loaded. This count is useful for progress tracking for Value Eviction buckets during the "loading keys" state and the ratio of ep\_warmup\_key\_count and this provides insight into progress. This value is the same for the estimated number of keys required to be loaded for secondary warmup, if secondary warmup is enabled.

`kv_ep_warmup_estimated_value_count`

7.1.0counterTo facilitate warm-up progress tracking this value represents how many values need to be loaded to reach 100% of values loaded. This counter is only initialised when warm-up reaches the "loading access log", "loading k/v pairs" or "loading data" state and the ratio of ep\_warmup\_value\_count and this provides insight into progress.

`kv_ep_warmup_key_count`

7.1.0counterNumber of keys warmed up

`kv_ep_warmup_oom`

7.0.0gaugeOOMs encountered during warmup

`kv_ep_warmup_status`

7.2.0gaugeThe current status of the warmup thread

`kv_ep_warmup_time_seconds`

7.0.0gauge / secondsTime (µs) spent by warming data during Primary warm-up

`kv_ep_warmup_value_count`

7.1.0counterNumber of values warmed up

`kv_ep_workload_monitor_enabled`

7.0.0gauge

`kv_ep_xattr_enabled`

7.0.0gauge

`kv_fusion_migration_rate_limit_bytes`

8.0.0gauge / bytesThe rate limit for fusion extent migration, in bytes per second.

`kv_fusion_sync_rate_limit_bytes`

8.0.0gauge / bytesThe rate limit for fusion sync uploads, in bytes per second.