---
title: Data Service Metrics
description: A list of the metrics provided by the Data Service.
pubDate: 2026-08-18T04:50:45.818Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/metrics-reference/pages/data-service-metrics.adoc
  xref: xref:server:metrics-reference:data-service-metrics.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/metrics-reference/data-service-metrics.html)

# Data Service Metrics

> A list of the metrics provided by the Data Service. 

The following Data Service metrics can be queried by means of the REST APIs described in [Statistics](../rest-api/rest-statistics.md).

See [Data Service Metrics Cross Reference](data-service-metrics-cross-reference.md) if you are looking for a metric name you know from an alternative supported or legacy tool.

Histograms

Note that each histogram metric will generate three time series, with the following suffixes:

* `_count`
* `_sum`
* `_bucket`

Please refer to [Prometheus Histograms and Summaries](https://prometheus.io/docs/practices/histograms/) for more information.

> [!TIP]
> * The x.y.z badge shows the Couchbase Server version the metric was added in.
> * The type / unit badge shows shows the Prometheus [type](https://prometheus.io/docs/tutorials/understanding%5Fmetric%5Ftypes/) and [unit](https://prometheus.io/docs/practices/naming/#base-units) (if present).

`kv_audit_dropped_events`

7.0.0 counter The number of audit events dropped due to errors while trying to insert them to the audit trail

`kv_audit_enabled`

7.0.0 gauge Boolean value to indicate if audit is enabled or not

`kv_auth_cmds`

7.0.0 gauge The number of authentication commands

`kv_auth_errors`

7.0.0 gauge The number of failed authentication requests

`kv_auth_external_authentication_duration_seconds`

8.0.0 histogram / seconds Timing histogram for external authentication execution times

`kv_auth_external_authorization_duration_seconds`

8.0.0 histogram / seconds Timing histogram for external authorization execution times

`kv_auth_external_received`

8.0.0 gauge The number of received external authentication responses

`kv_auth_external_sent`

8.0.0 gauge The total number of requests sent to the external authentication provider

`kv_bg_batch_size`

7.0.0 histogram Batch size for background fetches

`kv_bg_load_seconds`

7.0.0 histogram / seconds Background fetches waiting for disk

`kv_bg_wait_seconds`

7.0.0 histogram / seconds Background fetches waiting in the dispatcher queue

`kv_clients`

7.6.0 gauge The number of references to the bucket

`kv_cmd_duration_seconds`

7.0.0 histogram / seconds Per-opcode histogram of time taken to execute operations

`kv_cmd_lookup`

7.0.0 counter The number of lookup operations. This includes operations such as Get, Gat, Getk, Getq, GetLocked, GetRandomKey, GetReplica, SubdocMultiLookup, SubdocGet and SubdocExists

`kv_cmd_lookup_10s_count`

7.0.0 gauge The number of lookup operations performed within the last 10 seconds. This aggregates operations like Get, Gat, Getk, Getq, and various Sub-Document lookups

`kv_cmd_lookup_10s_duration_seconds`

7.0.0 gauge / seconds The total duration of lookup operations performed over the last 10 seconds. This aggregates the time for operations like Get, Gat, Getk, Getq, and various Sub-Document lookups

`kv_cmd_mutation`

7.0.0 counter The number of mutation operations. This includes operations such as Add, Append, Decrement, Delete, Gat, Increment, Prepend, Replace, Set, Touch, and various Sub-Document mutations (e.g., SubdocArrayAddUnique, SubdocCounter, SubdocDelete, etc.)

`kv_cmd_mutation_10s_count`

7.0.0 gauge The number of mutation operations performed within the last 10 seconds. This includes operations like Add, Append, Delete, Replace, and various Sub-Document mutations

`kv_cmd_mutation_10s_duration_seconds`

7.0.0 gauge / seconds The total duration of mutation operations performed over the last 10 seconds. This includes time spent on operations like Add, Append, Delete, Replace, and various Sub-Document mutations

`kv_collection_data_size_bytes`

7.0.0 gauge / bytes Per-collection data size on disk for active vbuckets only

`kv_collection_history`

7.2.0 gauge Whether history (CDC) is enabled for each collection

`kv_collection_item_count`

7.0.0 gauge Per-collection item count for active vbuckets only

`kv_collection_maxTTL_seconds`

7.0.0 gauge / seconds Per-collection maxTTL (maximum expiry) if configured

`kv_collection_mem_used_bytes`

7.0.0 gauge / bytes Per-collection memory usage for active vbuckets only

`kv_collection_ops`

7.0.0 counter Per-collection counters of operations that perform store/get(read)/delete type operations against active vbuckets

`kv_conflicts_resolved`

7.2.0 counter Counter of all SetWithMeta/DelWithMeta conflict resolution results. The result may be that the incoming operation was: accepted as it is 'ahead', rejected as it is 'behind', or rejected as it appears identical (by metadata, not comparing document bodies)

`kv_conn_timeslice_yields`

7.6.0 counter The total number all clients in this bucket yield due to using their entire timeslice

`kv_conn_yields`

7.0.0 counter The total number all clients in this bucket yield due to consuming the number of ops allowed for the current timeslice

`kv_connection_structures`

7.0.0 gauge Current number of allocated connection structures

`kv_curr_connections`

7.0.0 gauge The current number of connections. This includes user, system and daemon connections

`kv_curr_connections_closing`

8.0.0 gauge The current number of connections currently closing down

`kv_curr_items`

7.0.0 gauge Count of alive (non-deleted) items in active vbuckets, including non-resident items

`kv_curr_items_tot`

7.0.0 gauge Total number of items

`kv_curr_temp_items`

7.0.0 gauge Number of temporary items in memory

`kv_current_external_client_connections`

7.6.5 gauge The current number of authenticated connections using the labelled SDK

`kv_daemon_connections`

7.0.0 gauge The number of server sockets currently in use

`kv_daemon_memory_allocated_bytes`

7.1.0 gauge / bytes Total amount of memory allocated (outside the context of a bucket)

`kv_daemon_memory_resident_bytes`

7.1.0 gauge / bytes Total amount of memory resident (outside the context of a bucket)

`kv_datatype_count`

7.0.2 gauge Count of items in memory with a given datatype combination

`kv_dcp_backoff`

7.0.0 gauge Number of times Consumer DCP connections (i.e., replica) have paused consuming items because memory usage is too high

`kv_dcp_connection_count`

7.0.0 gauge Current number of DCP connections (Consumers or Producers)

`kv_dcp_count`

7.0.0 gauge Current number of DCP connections

`kv_dcp_items_backfilled`

7.2.1 gauge Number of items pushed into the DCP stream ready queue from a backfill

`kv_dcp_items_remaining`

7.0.0 gauge Current total number of items remaining for to be sent for all outgoing DCP streams (approximate)

`kv_dcp_items_sent`

7.0.0 gauge Total number of items sent out by all _currently existing_ outgoing DCP streams, since each stream was created

`kv_dcp_max_running_backfills`

7.0.2 gauge Maximum number of backfills across all DCP connections

`kv_dcp_num_running_backfills`

7.0.2 gauge Total number of running backfills across all DCP connections

`kv_dcp_paused_count`

7.6.0 gauge Count of how many times the DCP connection has been paused

`kv_dcp_ready_queue_size_bytes`

7.1.0 gauge / bytes Estimated memory usage of items waiting to be sent across all _existing_ DCP connections

`kv_dcp_stream_count`

7.6.0 gauge Current number of Streams (Active or Passive)

`kv_dcp_total_data_size_bytes`

7.0.0 gauge / bytes Total data sent across all _existing_ DCP connections

`kv_dcp_total_uncompressed_data_size_bytes`

7.0.0 gauge / bytes Total equivalent uncompressed size of data sent across all _existing_ DCP connections

`kv_dcp_unpaused_count`

7.6.0 gauge Count of how many times the DCP connection has been unpaused

`kv_disk_seconds`

7.0.0 histogram / seconds time spent waiting for disk

`kv_domain_memory_used_bytes`

7.1.0 gauge / bytes Current memory used in KV for primary/secondary domain

`kv_ep_access_scanner_enabled`

7.0.0 gauge True if access scanner task is enabled

`kv_ep_access_scanner_last_runtime_seconds`

7.0.0 gauge / seconds Number of seconds that last Access Scanner task run took to complete.

`kv_ep_access_scanner_num_items`

7.0.0 gauge Number of items that last Access Scanner task run wrote to the Access Log.

`kv_ep_ahead_exceptions`

7.0.0 counter Total number of times a vbucket saw an item with a HLC CAS from too far in the future (indicating the clock is behind)

`kv_ep_allow_sanitize_value_in_deletion`

7.0.0 gauge Let EPE delete/prepare/del\_with\_meta prune any invalid body in the payload instead of failing

`kv_ep_alog_block_size`

7.0.0 gauge Logging block size.

`kv_ep_alog_max_stored_items`

7.0.0 gauge The maximum number of items the Access Scanner will hold in memory before commiting them to disk

`kv_ep_alog_resident_ratio_threshold`

7.0.0 gauge Resident ratio percentage above which we do not generate access log

`kv_ep_alog_sleep_time`

7.0.0 gauge Number of minutes between each sweep for the access log

`kv_ep_alog_task_time`

7.0.0 gauge Hour in GMT time when access scanner task is scheduled to run

`kv_ep_arena_memory_allocated_bytes`

7.6.0 gauge / bytes The total memory allocated from the engine's arena

`kv_ep_arena_memory_resident_bytes`

7.6.0 gauge / bytes The resident set size of the engine's arena

`kv_ep_backfill_mem_threshold`

7.0.0 gauge Memory usage threshold (percentage of bucket quota) after which backfill will be snoozed.

`kv_ep_behind_exceptions`

7.0.0 counter Total number of times a vbucket saw an item with a HLC CAS from too far in the past (indicating the clock is ahead)

`kv_ep_bfilter_enabled`

7.0.0 gauge Enable or disable the bloom filter

`kv_ep_bfilter_fp_prob`

7.0.0 gauge Bloomfilter: Allowed probability for false positives

`kv_ep_bfilter_key_count`

7.0.0 gauge Bloomfilter: Estimated key count per vbucket

`kv_ep_bfilter_residency_threshold`

7.0.0 gauge If resident ratio (during full eviction) were found less than this threshold, compaction will include all items into bloomfilter

`kv_ep_bg_fetch_avg_read_amplification_ratio`

7.0.0 gauge / ratio Average read amplification for all background fetch operations - ratio of read()s to documents fetched.

`kv_ep_bg_fetched`

7.0.0 counter Number of items fetched from disk

`kv_ep_bg_fetched_compaction`

7.1.5 counter The number of bgfetches which are triggered by compaction

`kv_ep_bg_load_avg_seconds`

7.0.0 gauge / seconds The average time for an item to be loaded from disk

`kv_ep_bg_load_seconds`

7.0.0 counter / seconds The total elapsed time for items to be loaded from disk

`kv_ep_bg_max_load_seconds`

7.0.0 gauge / seconds The longest load time when loading from disk

`kv_ep_bg_max_wait_seconds`

7.0.0 gauge / seconds The longest time in the queue waiting to be loaded from disk

`kv_ep_bg_meta_fetched`

7.0.0 counter Number of metadata fetches from disk

`kv_ep_bg_min_load_seconds`

7.0.0 gauge / seconds The shortest load time when loading from disk

`kv_ep_bg_min_wait_seconds`

7.0.0 gauge / seconds The shortest time in the queue waiting to be loaded from disk

`kv_ep_bg_num_samples`

7.0.0 gauge The number of samples included in the average

`kv_ep_bg_remaining_items`

7.0.0 gauge Number of remaining bg fetch items

`kv_ep_bg_remaining_jobs`

7.0.0 gauge Number of remaining bg fetch jobs

`kv_ep_bg_wait_avg_seconds`

7.0.0 gauge / seconds The average wait time for an item before it's serviced by the dispatcher

`kv_ep_bg_wait_seconds`

7.0.0 gauge / seconds The total elapse time for the wait queue

`kv_ep_blob_num`

7.0.0 gauge The number of blob objects in the cache

`kv_ep_blob_num_allocated_total`

7.6.0 counter The number of blob object allocations

`kv_ep_blob_num_freed_total`

7.6.0 counter The number of blob object deallocations

`kv_ep_bucket_quota_change_task_poll_interval`

7.0.0 gauge Time in seconds between the BucketQuotaChangeTask polling memory usage to attempt to reduce the bucket quota

`kv_ep_cache_size`

7.0.0 gauge Memory quota (in bytes) for this bucket.

`kv_ep_checkpoint_computed_max_size_bytes`

7.1.0 gauge / bytes Actual max size in bytes of a single Checkpoint

`kv_ep_checkpoint_consumer_limit_bytes`

7.6.2 gauge / bytes Max allocation allowed in all checkpoints (including the dcp consumer buffer quota)

`kv_ep_checkpoint_destruction_tasks`

7.0.0 gauge Number of tasks responsible for destroying closed unreferenced checkpoints.

`kv_ep_checkpoint_max_size`

7.0.0 gauge Max size (in bytes) of a single checkpoint. '0' for EPEngine auto-setup.

`kv_ep_checkpoint_memory_bytes`

7.0.0 gauge / bytes Memory of items in all checkpoints

`kv_ep_checkpoint_memory_pending_destruction_bytes`

7.1.0 gauge / bytes Memory of checkpoint structures awaiting destruction by a background task

`kv_ep_checkpoint_memory_quota_bytes`

7.1.0 gauge / bytes Max allocation allowed in all checkpoints

`kv_ep_checkpoint_memory_ratio`

7.0.0 gauge Max ratio of the bucket quota that can be allocated in checkpoints. The system enters a TempOOM phase if hit.

`kv_ep_checkpoint_memory_recovery_lower_mark`

7.0.0 gauge Fraction of the checkpoint quota (as computed by checkpoint\_memory\_ratio) that represents the target of checkpoint memory recovery. Memory recovery yields when reached.

`kv_ep_checkpoint_memory_recovery_lower_mark_bytes`

7.1.0 gauge Fraction of the checkpoint quota (as computed by checkpoint\_memory\_ratio) that represents the target of checkpoint memory recovery. Memory recovery yields when reached

`kv_ep_checkpoint_memory_recovery_upper_mark`

7.0.0 gauge Fraction of the checkpoint quota (as computed by checkpoint\_memory\_ratio) that triggers attempt of memory releasing from checkpoint.

`kv_ep_checkpoint_memory_recovery_upper_mark_bytes`

7.1.0 gauge Fraction of the checkpoint quota (as computed by checkpoint\_memory\_ratio) that triggers attempt of memory releasing from checkpoint

`kv_ep_checkpoint_remover_task_count`

7.0.0 gauge Number of concurrent tasks performing ItemExpel and CursorDrop/CheckpointRemoval

`kv_ep_chk_expel_enabled`

7.0.0 gauge Enable the ability to expel (remove from memory) items from a checkpoint. An item can be expelled if all cursors in the checkpoint have iterated past the item.

`kv_ep_chk_persistence_remains`

7.0.0 gauge Number of remaining vbuckets for checkpoint persistence

`kv_ep_clock_cas_drift_threshold_exceeded`

7.0.0 gauge ep\_active\_ahead\_exceptions + ep\_replica\_ahead\_exceptions

`kv_ep_collections_drop_compaction_delay`

7.0.0 gauge How many milliseconds before compaction runs following the drop of a collection

`kv_ep_collections_enabled`

7.0.0 gauge Enable the collections functionality, enabling the storage of collection metadata

`kv_ep_commit_num`

7.0.0 gauge Total number of write commits

`kv_ep_commit_time_seconds`

7.0.0 gauge / seconds Number of milliseconds of most recent commit

`kv_ep_commit_time_total_seconds`

7.0.0 gauge / seconds Cumulative milliseconds spent committing

`kv_ep_compaction_aborted`

7.1.0 gauge Counter of how many times compaction aborted, e.g. the vbucket is required to rollback, so compaction is aborted

`kv_ep_compaction_expire_from_start`

7.0.0 gauge Should compaction expire items that were logically deleted at the start of the compaction (true) or at the point in time at which they were visited (false)?

`kv_ep_compaction_expiry_fetch_inline`

7.0.0 gauge If compaction requires a bgfetch before attempting expiry to ensure it does not expire an older version of the document, true: fetch it in the compaction thread. false: queue a bgfetch for the bgfetcher task to complete

`kv_ep_compaction_failed`

7.1.0 gauge Counter of how many times compaction has failed, e.g. a system call error caused compaction to fail

`kv_ep_compaction_max_concurrent_ratio`

7.0.0 gauge Maximum number of CompactVBucketTask tasks which can run concurrently, as a fraction of the possible Writer task concurrency. Note that a minimum of 1, and a maximum of N-1 CompactVBucketTasks will be run (where N is the possible Writer task concurrency), to ensure both forward progress for Compaction and Flushing.

`kv_ep_concurrent_pagers`

7.0.0 gauge Number of eviction pager tasks to create when memory usage is high

`kv_ep_connection_cleanup_interval`

7.0.0 gauge How often connection manager task should release dead connections (in seconds).

`kv_ep_connection_manager_interval`

7.0.0 gauge How often connection manager task should be run (in seconds).

`kv_ep_continuous_backup_callback_count`

8.0.0 gauge Number of times the continuous backup metadata callback was run.

`kv_ep_continuous_backup_callback_time_seconds`

8.0.0 gauge / seconds Time spent in KV in the continuous backup metadata callback.

`kv_ep_continuous_backup_enabled`

7.0.0 gauge True if continouous backup is enabled.

`kv_ep_continuous_backup_interval`

7.0.0 gauge The continouous backup interval (in seconds).

`kv_ep_couchstore_file_cache_max_size`

7.0.0 gauge Maximum number of couchstore files that we will keep open. Default value is 30 \* 1024 (i.e. one file for each vBucket and 30 Buckets - the supported limit).

`kv_ep_couchstore_midpoint_rollback_optimisation`

7.0.0 gauge Should we have to rollback more than half of the seqnos seen by this vBucket we will instead rollback to 0 and re-stream from the active if set to true

`kv_ep_couchstore_mprotect`

7.0.0 gauge Enable couchstore to mprotect the iobuffer

`kv_ep_couchstore_tracing`

7.0.0 gauge Enable couchstore tracing

`kv_ep_couchstore_write_validation`

7.0.0 gauge Validate couchstore writes

`kv_ep_cross_bucket_ht_quota_sharing`

7.0.0 gauge Allow this Bucket's HashTable quota to be shared with other Buckets which have this setting enabled.

`kv_ep_cursors_dropped`

7.0.0 gauge Number of cursors dropped by the checkpoint remover

`kv_ep_data_read_failed`

7.0.0 gauge Total number of get failures

`kv_ep_data_traffic_enabled`

7.0.0 gauge True if we want to enable data traffic after warmup is complete

`kv_ep_data_write_failed`

7.0.0 gauge Total compaction and commit failures

`kv_ep_db_data_size_bytes`

7.0.0 gauge / bytes Total size of valid data in db files

`kv_ep_db_file_size_bytes`

7.0.0 gauge / bytes Total size of the db files

`kv_ep_db_history_file_size_bytes`

7.2.0 gauge / bytes The total size of all history currently stored by the bucket

`kv_ep_db_history_start_timestamp_seconds`

7.2.0 gauge / seconds The timestamp of the oldest document stored in the history window, oldest of all vbuckets

`kv_ep_db_prepare_size_bytes`

7.0.0 gauge / bytes Total size of SyncWrite prepares in db files

`kv_ep_dcp_backfill_byte_drain_ratio`

7.0.0 gauge What ratio of the dcp\_backfill\_byte\_limit must be drained for un-pausing a paused backfill

`kv_ep_dcp_backfill_byte_limit`

7.0.0 gauge Max bytes a connection can backfill into memory before backfill is paused

`kv_ep_dcp_backfill_idle_disk_threshold`

7.0.0 gauge The percentage of disk usage at which DCP backfills would be ended when no progress is made for dcp\_backfill\_idle\_limit\_seconds

`kv_ep_dcp_backfill_idle_limit_seconds`

7.0.0 gauge How long (in seconds) a DCP Backfill can be held open with no progress being made. When this limit is exceeded the stream is force ended (reason Slow) releasing the resources being held by the stream. The default value is 2x of dcp\_idle\_timeout

`kv_ep_dcp_backfill_idle_protection_enabled`

7.0.0 gauge When true, DCP backfills will be checked for progress. Any backfill which makes no progress for dcp\_backfill\_idle\_limit\_seconds will be subject to further checks. If the directory referenced by dbname is over dcp\_backfill\_idle\_disk\_threshold percent used and cancelling the backfill will free disk space, the scan cancels and the associated DCP stream will end with reason slow.

`kv_ep_dcp_backfill_in_progress_per_connection_limit`

7.0.0 gauge The maximum number of backfills each connection can have in-progress (i.e. KVStore snapshot open and reading data from)

`kv_ep_dcp_backfill_run_duration_limit`

7.0.0 gauge Maximum time (in ms) backfill task will run before yielding.

`kv_ep_dcp_checkpoint_dequeue_limit`

7.0.0 gauge The limit given to CheckpointManager::getNextItemsForDcp by ActiveStream

`kv_ep_dcp_consumer_buffer_ratio`

7.0.0 gauge Ratio of the BucketQuota that can be allocated by all DCP consumers for buffered messages

`kv_ep_dcp_consumer_flow_control_ack_ratio`

7.0.0 gauge Ratio of freed bytes in the DCP Consumer buffer that triggers a BufferAck message to the Producer

`kv_ep_dcp_consumer_flow_control_ack_seconds`

7.0.0 gauge Max seconds after which a Consumer acks all the remaining freed bytes, regardless of whether dcp\_consumer\_flow\_control\_ack\_ratio has kicked-in or not

`kv_ep_dcp_consumer_flow_control_enabled`

7.0.0 gauge Whether DCP Consumer on this node enable flow control

`kv_ep_dcp_enable_noop`

7.0.0 gauge Whether DCP Consumer connections should attempt to negotiate no-ops with the Producer

`kv_ep_dcp_idle_timeout`

7.0.0 gauge The maximum number of seconds between dcp messages before a connection is disconnected

`kv_ep_dcp_min_compression_ratio`

7.0.0 gauge Compression ratio to be achieved above which producer will ship documents as is

`kv_ep_dcp_noop_mandatory_for_v5_features`

7.0.0 gauge Forces clients to enable noop for v5 features

`kv_ep_dcp_noop_tx_interval`

7.0.0 gauge The time interval in seconds between noop messages being sent to the consumer

`kv_ep_dcp_oso_backfill_large_value_ratio`

7.0.0 gauge When considering out-of-seqno order (OSO) DCP backfill for a collection with 'large' mean value size, OSO will only be selected if the backfilling collection item count is less than this fraction of the vBucket item count. Whether the collection has 'small' or 'large' items depends on the value of 'dcp\_oso\_backfill\_mean\_item\_size\_threshold'.

`kv_ep_dcp_oso_backfill_small_item_size_threshold`

7.0.0 gauge When considering out-of-seqno order (OSO) DCP backfill for a collection, should the items in the collection be considered 'small' or 'large' and subsequently should backfill use 'dcp\_oso\_backfill\_small\_value\_collection\_ratio' or 'dcp\_oso\_backfill\_large\_value\_collection\_ratio' when deciding ot use OSO or not? Collections whoss mean on-disk value size is less than this parameter are considered 'small', otherwise they are considered 'large'

`kv_ep_dcp_oso_backfill_small_value_ratio`

7.0.0 gauge When considering out-of-seqno order (OSO) DCP backfill for a collection with 'small' mean value size, OSO will only be selected if the backfilling collection item count is less than this fraction of the vBucket item count. Whether the collection has 'small' or 'large' items depends on the value of 'dcp\_oso\_backfill\_mean\_item\_size\_threshold'.

`kv_ep_dcp_oso_max_collections_per_backfill`

7.0.0 gauge This is the maximum number of collections that a DCP stream can be filtering to be eligible for OSO

`kv_ep_dcp_producer_catch_exceptions`

7.0.0 gauge If true, ActiveStream will catch exceptions during item processing and close the stream's related connection (and thus all streams for that connection). If false, exception will be re-thrown.

`kv_ep_dcp_producer_processor_run_duration_us`

7.0.0 gauge The approximate maximum runtime in microseconds for ActiveStreamCheckpointProcessorTask

`kv_ep_dcp_producer_snapshot_marker_yield_limit`

7.0.0 gauge Not in use - replaced by dcp\_producer\_processor\_run\_duration\_us

`kv_ep_dcp_scan_byte_limit`

7.0.0 gauge Max bytes that can be read in a single backfill scan before yielding

`kv_ep_dcp_scan_item_limit`

7.0.0 gauge Max items that can be read in a single backfill scan before yielding

`kv_ep_dcp_takeover_max_time`

7.0.0 gauge Max amount of time for takeover send (in seconds) after which front end ops would return ETMPFAIL

`kv_ep_defragmenter_age_threshold`

7.0.0 gauge How old (measured in number of DefragmenterVisitor passes) must a document be to be considered for defragmentation.

`kv_ep_defragmenter_auto_lower_threshold`

7.0.0 gauge When mode is not static and scored fragmentation is above this value, a sleep time between defragmenter\_auto\_min\_sleep and defragmenter\_auto\_max\_sleep will be used

`kv_ep_defragmenter_auto_max_sleep`

7.0.0 gauge The maximum sleep that the auto controller can set

`kv_ep_defragmenter_auto_min_sleep`

7.0.0 gauge The minimum sleep that the auto controller can set

`kv_ep_defragmenter_auto_pid_d`

7.0.0 gauge The d term for the PID controller

`kv_ep_defragmenter_auto_pid_dt`

7.0.0 gauge The dt (interval) term for the PID controller. Value represents milliseconds

`kv_ep_defragmenter_auto_pid_i`

7.0.0 gauge The i term for the PID controller

`kv_ep_defragmenter_auto_pid_p`

7.0.0 gauge The p term for the PID controller

`kv_ep_defragmenter_auto_upper_threshold`

7.0.0 gauge When mode is auto\_linear and scored fragmentation is above this value, the defragmenter will use defragmenter\_auto\_min\_sleep

`kv_ep_defragmenter_chunk_duration`

7.0.0 gauge Maximum time (in ms) defragmentation task will run for before being paused (and resumed at the next defragmenter\_interval).

`kv_ep_defragmenter_enabled`

7.0.0 gauge True if defragmenter task is enabled

`kv_ep_defragmenter_interval`

7.0.0 gauge How often defragmenter task should be run (in seconds).

`kv_ep_defragmenter_num_moved`

7.0.0 gauge Number of items moved by the defragmentater task.

`kv_ep_defragmenter_num_visited`

7.0.0 gauge Number of items visited (considered for defragmentation) by the defragmenter task.

`kv_ep_defragmenter_sleep_time_seconds`

7.6.0 gauge / seconds The amount of time the defragmenter task will sleep before it is scheduled to run again.

`kv_ep_defragmenter_stored_value_age_threshold`

7.0.0 gauge How old (measured in number of DefragmenterVisitor passes) must a StoredValue be to be considered for defragmentation.

`kv_ep_defragmenter_sv_num_moved`

7.0.0 gauge Number of StoredValues moved by the defragmentater task.

`kv_ep_degraded_mode`

7.0.0 gauge True if the engine is either warming up or data traffic is disabled

`kv_ep_diskqueue_drain`

7.0.0 gauge Total drained items on disk queue

`kv_ep_diskqueue_fill`

7.0.0 gauge Total enqueued items on disk queue

`kv_ep_diskqueue_items`

7.0.0 gauge Total items in disk queue

`kv_ep_diskqueue_memory_bytes`

7.0.0 gauge / bytes Total memory used in disk queue

`kv_ep_diskqueue_pending`

7.0.0 gauge Total bytes of pending writes

`kv_ep_ephemeral_mem_recovery_enabled`

7.0.0 gauge Whether ephemeral memory recovery task is enabled. If disabled, ItemPager will carry out memory recovery for AutoDelete buckets.

`kv_ep_ephemeral_mem_recovery_sleep_time`

7.0.0 gauge Duration in milliseconds the EphemeralMemRecovery task will sleep between periodic executions.

`kv_ep_ephemeral_metadata_mark_stale_chunk_duration`

7.0.0 gauge Maximum time (in ms) ephemeral hash table cleaner task will run for before being paused (and resumed at the next ephemeral\_metadata\_purge\_interval).

`kv_ep_ephemeral_metadata_purge_age`

7.0.0 gauge Age in seconds after which Ephemeral metadata is purged entirely from memory. Purging disabled if set to -1.

`kv_ep_ephemeral_metadata_purge_interval`

7.0.0 gauge Time in seconds between automatic, periodic runs of the Ephemeral metadata purge task. Periodic purging disabled if set to 0.

`kv_ep_ephemeral_metadata_purge_stale_chunk_duration`

7.0.0 gauge Maximum time (in ms) ephemeral stale metadata purge task will run for before being paused (and resumed at the next ephemeral\_metadata\_purge\_interval).

`kv_ep_exp_pager_enabled`

7.0.0 gauge True if expiry pager task is enabled

`kv_ep_exp_pager_initial_run_time`

7.0.0 gauge Hour in GMT time when expiry pager can be scheduled for initial run

`kv_ep_exp_pager_stime`

7.0.0 gauge Number of seconds between expiry pager runs.

`kv_ep_expired_access`

7.0.0 gauge Number of times an item was expired on application access

`kv_ep_expired_compactor`

7.0.0 gauge Number of times an item was expired by the compactor

`kv_ep_expired_pager`

7.0.0 gauge Number of times an item was expired by the item pager

`kv_ep_expiry_pager_concurrency`

7.0.0 gauge Number of tasks which are created to scan for and delete expired items

`kv_ep_expiry_visitor_expire_after_visit_duration_ms`

7.0.0 gauge The time limit in milliseconds for processing expired items after visiting hash tables. After finding expired items during hash table traversal, the expiry pager will process them until this duration is reached before yielding.

`kv_ep_expiry_visitor_items_only_duration_ms`

7.0.0 gauge The time limit in milliseconds for processing items from the expired items list at the start of an expiry pager run. If the expired items list is not empty when the pager starts, it will only process items from this list for up to this duration before yielding.

`kv_ep_failpartialwarmup`

7.0.0 gauge If true then do not allow traffic to be enabled to the bucket if warmup didn't complete successfully

`kv_ep_flush_batch_max_bytes`

7.0.0 gauge Max size (in bytes) of a single flush-batch passed to the KVStore for persistence.

`kv_ep_flush_duration_total_seconds`

7.0.0 gauge / seconds Cumulative milliseconds spent flushing

`kv_ep_flusher_todo`

7.0.0 gauge Number of items currently being written

`kv_ep_flusher_total_batch_limit`

7.0.0 gauge Number of items that all flushers can be currently flushing. Each flusher has flusher\_total\_batch\_limit / num\_writer\_threads individual batch size. Individual batches may be larger than this value, as we cannot split Memory checkpoints across multiple commits.

`kv_ep_freq_counter_increment_factor`

7.0.0 gauge The increment factor of the ProbabilisticCounter being used for the frequency counter. The default value of 0.012 is set such that it allows an 8-bit ProbabilisticCounter to mimic a uint16 counter. See the comment on the ProbabilisticCounter class for more information.

`kv_ep_fsync_after_every_n_bytes_written`

7.0.0 gauge Perform a file sync() operation after every N bytes written. Disabled if set to 0.

`kv_ep_fusion_bytes_migrated_bytes`

8.0.0 counter / bytes Total number of bytes migrated over from the mounted source to the host volume.

`kv_ep_fusion_bytes_synced_bytes`

8.0.0 counter / bytes Total number of bytes synced to FusionLogStore.

`kv_ep_fusion_extent_merger_bytes_read_bytes`

8.0.0 counter / bytes Total number of bytes read in order to merge extents.

`kv_ep_fusion_extent_merger_reads`

8.0.0 counter / count Total number of read IOs issued in order to merge extents.

`kv_ep_fusion_file_map_mem_used_bytes`

8.0.0 gauge / bytes Total amount of memory consumed by file map.

`kv_ep_fusion_log_clean_bytes_read_bytes`

8.0.0 counter / bytes Total number of bytes read in order to clean the logs.

`kv_ep_fusion_log_clean_reads`

8.0.0 counter / count Total number of read IOs issued in order to clean the logs.

`kv_ep_fusion_log_store_garbage_size_bytes`

8.0.0 gauge / bytes Total size of the garbage data present on FusionLogStore.

`kv_ep_fusion_log_store_pending_delete_size_bytes`

8.0.0 gauge / bytes Total number of bytes not yet deleted from FusionLogStore.

`kv_ep_fusion_log_store_reads`

8.0.0 counter / count Total Number of read operations issued to FusionLogStore. The read maybe answered locally if there's a cache hit. This stats also includes ep\_fusion\_log\_store\_remote\_gets.

`kv_ep_fusion_log_store_remote_deletes`

8.0.0 counter / count Total number of DELETE operations issued to FusionLogStore.

`kv_ep_fusion_log_store_remote_gets`

8.0.0 counter / count Total number of GET operations issued to FusionLogStore.

`kv_ep_fusion_log_store_remote_lists`

8.0.0 counter / count Total number of LIST operations issued to FusionLogStore.

`kv_ep_fusion_log_store_remote_puts`

8.0.0 counter / count Total number of PUT operations issued to FusionLogStore.

`kv_ep_fusion_log_store_size_bytes`

8.0.0 gauge / bytes Total size of all the logs on FusionLogStore.

`kv_ep_fusion_logs_cleaned`

8.0.0 counter / count Total number of logs cleaned because their garbage size crossed the fragmentation threshold.

`kv_ep_fusion_logs_migrated`

8.0.0 counter / count Total number of logs migrated over from the mounted source to the host volume.

`kv_ep_fusion_migration_completed_bytes_bytes`

8.0.0 gauge / bytes Total number of bytes completed in the migration.

`kv_ep_fusion_migration_failures`

8.0.0 counter / count Total number of times migrating logs failed.

`kv_ep_fusion_migration_total_bytes_bytes`

8.0.0 gauge / bytes Total number of bytes in the migration.

`kv_ep_fusion_num_file_extents`

8.0.0 gauge / count Number of file extents on Fusion.

`kv_ep_fusion_num_files`

8.0.0 gauge / count Number of files on Fusion.

`kv_ep_fusion_num_log_segments`

8.0.0 gauge / count Number of log segments on Fusion.

`kv_ep_fusion_num_logs_mounted`

8.0.0 counter / count Number of logs mounted on Fusion for the purpose of extent migration.

`kv_ep_fusion_sync_failures`

8.0.0 counter / count Total number of times syncing data to Fusion failed.

`kv_ep_fusion_sync_session_completed_bytes_bytes`

8.0.0 gauge / bytes Total number of bytes completed in the sync session.

`kv_ep_fusion_sync_session_total_bytes_bytes`

8.0.0 gauge / bytes Total number of bytes in the sync session.

`kv_ep_fusion_syncs`

8.0.0 counter / count Total number of times data was synced to Fusion.

`kv_ep_fusion_total_file_size_bytes`

8.0.0 gauge / bytes Total size of all files on Fusion.

`kv_ep_getl_default_timeout`

7.0.0 gauge The default timeout for a getl lock in (s)

`kv_ep_getl_max_timeout`

7.0.0 gauge The maximum timeout for a getl lock in (s)

`kv_ep_history_retention_bytes`

7.0.0 gauge Max bytes of history a bucket should aim to retain on disk.

Continued on [page 2](data-service-metrics-2.md).