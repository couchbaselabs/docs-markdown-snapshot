---
title: XDCR Metrics
description: A list of the metrics provided by XDCR.
pubDate: 2026-08-18T04:50:45.818Z
antora:
  editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/metrics-reference/pages/xdcr-metrics.adoc
  xref: xref:cloud:metrics-reference:xdcr-metrics.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/metrics-reference/xdcr-metrics.html)

# XDCR Metrics

> A list of the metrics provided by XDCR. 

> [!TIP]
> * The x.y.z badge shows the Couchbase Server version the metric was added in.
> * The type / unit badge shows shows the Prometheus [type](https://prometheus.io/docs/tutorials/understanding%5Fmetric%5Ftypes/) and [unit](https://prometheus.io/docs/practices/naming/#base-units) (if present).

`xdcr_atr_txn_docs_filtered_total`

7.6.0 counter Total number of documents filtered and not replicated because the documents were ATR documents

`xdcr_binary_filtered_total`

7.6.0 counter Number of documents filtered that were binary documents

`xdcr_changes_left_total`

7.0.0 gauge Given the vBuckets of this node, the number of sequence numbers that need to be processed (either replicated or handled) before catching up to the high sequence numbers for the vBuckets

`xdcr_client_txn_docs_filtered_total`

7.6.0 counter Total number of documents filtered and not replicated because the documents were transaction client records

`xdcr_clog_crd_docs_written_total`

8.0.0 counter Number of CRDs written to the conflict bucket.

`xdcr_clog_docs_filtered_total`

8.0.0 counter Number of conflict records filtered.

`xdcr_clog_docs_written_total`

8.0.0 counter Total number of conflict docs written. This counter includes all three types of conflict doc - source doc, target doc and CRD for the conflict detected.

`xdcr_clog_eaccesses_total`

8.0.0 counter Number of EACCESS errors encountered while writing the conflict records to the conflict bucket. It is likely that something has gone wrong with the previliges of the user used for conflict writing

`xdcr_clog_fatal_resps_total`

8.0.0 counter Number of fatal errors encountered while writing the conflict records to the conflict bucket. It includes EINVAL and XATTR\_EINVAL.

`xdcr_clog_guardrail_hits_total`

8.0.0 counter Number of guardrail hit errors encountered while writing the conflict records to the conflict bucket. It includes resident ratio, data size and disk space guardrail errors.

`xdcr_clog_hibernated_count_total`

8.0.0 counter Number of docs which were identified as conflicts, but could not be logged because the conflict logger was hibernated.

`xdcr_clog_impossible_resps_total`

8.0.0 counter Number of errors which by design should not have been returned, encountered while writing the conflict records to the conflict bucket. It includes EEXISTS, ENOENT and LOCKED errors.

`xdcr_clog_not_my_vbs_total`

8.0.0 counter Number of NOT\_MY\_VBUCKET errors encountered while writing the conflict records to the conflict bucket. It mostly is an indicator of topology changes.

`xdcr_clog_nw_errors_total`

8.0.0 counter Number of network errors encountered while writing the conflict records to the conflict bucket.

`xdcr_clog_other_errors_total`

8.0.0 counter Number of unidentified errors encountered while writing the conflict records to the conflict bucket. One should turn on debug logging for the replication to catch the unknown response.

`xdcr_clog_pool_get_timedout_total`

8.0.0 counter Number of conflict records for which the conflict logger had trouble getting a connection to the conflict bucket.

`xdcr_clog_queue_full_total`

8.0.0 counter Number of docs which were identified as conflicts, but could not be logged because the logging queue was full.

`xdcr_clog_src_docs_written_total`

8.0.0 counter Number of source conflict docs written to the conflict bucket.

`xdcr_clog_status`

8.0.0 gauge Indicates if the conflict logger of the replication is running or hibernated or if it does not exist.

`xdcr_clog_tgt_docs_written_total`

8.0.0 counter Number of target conflict docs written to the conflict bucket.

`xdcr_clog_throttled_total`

8.0.0 counter Number of conflict records which were throttled due to resource management and hence not written to conflict bucket.

`xdcr_clog_tmpfails_total`

8.0.0 counter Number of TMPFAIL errors encountered while writing the conflict records to the conflict bucket. It indicates that the data service was temporarily busy and could not process the incoming write.

`xdcr_clog_unknown_collections_total`

8.0.0 counter Number of UNKNOWN\_COLLECTION errors encountered while writing the conflict records to the conflict bucket. It indicates that where was a change to the collections setup which affected the conflict writes.

`xdcr_clog_unknown_resps_total`

8.0.0 counter Number of unknown responses returned by the source KV while writing the conflict records to the conflict bucket. One should turn on debug logging for the replication to catch the unknown response.

`xdcr_clog_write_timedout_total`

8.0.0 counter Number of conflict records for which the write to conflict bucket was timed out.

`xdcr_data_replicated_bytes`

7.0.0 counter / bytes Amount of data replicated for a Replication

`xdcr_data_replicated_uncompress_bytes`

7.0.0 counter / bytes Theoretical amount of data replicated for a Replication if compression were not used

`xdcr_datapool_failed_gets_total`

7.0.0 counter The total number of failed GET() operation on a reusable datapool within XDCR for the purpose of avoiding garbage generation

`xdcr_dcp_datach_length_total`

7.0.0 gauge The number of items sent by the Data Service waiting for the XDCR Source Nozzle to ingest and process

`xdcr_dcp_dispatch_time_seconds`

7.0.0 gauge / seconds The rolling average amount of time it takes for a document to be received by XDCR from the Data Service, to the time it is queued up in the Target Nozzle ready to be sent

`xdcr_deletion_cloned_total`

7.2.1 counter The number of times a Source Deletion or Expiration is cloned to be written to multiple Target Namespaces

`xdcr_deletion_docs_written_total`

7.0.0 counter Number of Deletions written to Target

`xdcr_deletion_failed_cr_source_total`

7.0.0 counter Number of Deletions that failed Source-side Conflict Resolution

`xdcr_deletion_failed_cr_target_total`

7.1.0 counter Number of Deletions that failed Conflict Resolution at the Target

`xdcr_deletion_filtered_total`

7.0.0 counter Number of Deletions that were filtered Source-side

`xdcr_deletion_received_from_dcp_total`

7.0.0 counter Number of Deletions received from the Data Service

`xdcr_docs_cas_poisoned_total`

8.0.0 counter Total number of documents not replicated because cas is beyond acceptable drift threshold

`xdcr_docs_checked_total`

7.0.0 gauge Across vBuckets for this node, the sum of all sequence numbers that have been considered to be checkpointed

`xdcr_docs_cloned_total`

7.0.0 counter Number of Source Document Mutation cloned to be written to different Target Namespaces

`xdcr_docs_compression_skipped_total`

8.0.0 counter Total number of documents whose compression was skipped before replication, due to a larger snappy-compressed size

`xdcr_docs_failed_cr_source_total`

7.0.0 counter Number of documents (or tombstones) that were not replicated to the Target due to Conflict Resolution evaluated on the Source

`xdcr_docs_failed_cr_target_total`

7.1.0 counter Number of documents failed Conflict Resolution at the Target

`xdcr_docs_filtered_on_txn_xattr_total`

7.6.0 counter Total number of documents filtered and not replicated due to the presence of transaction related xattrs in it

`xdcr_docs_filtered_on_user_defined_filter_total`

7.6.0 counter Total number of documents filtered and not replicated because of user defined filter expressions

`xdcr_docs_filtered_total`

7.0.0 gauge Total number of documents filtered and not replicated due to any type of filtering

`xdcr_docs_opt_repd_total`

7.0.0 counter Number of Documents Optimistically Replicated to the Target Cluster

`xdcr_docs_processed_total`

7.0.0 gauge Number of Documents processed for a Replication

`xdcr_docs_received_from_dcp_total`

7.0.0 counter Number of Document Mutations received from the Data Service

`xdcr_docs_sent_with_poisonedCas_errorMode_total`

8.0.0 counter The total number of documents that failed the set\_with\_meta operation due to the set CAS exceeding the acceptable threshold on the target data service.

`xdcr_docs_sent_with_poisonedCas_replaceMode_total`

8.0.0 counter The total number of documents replicated to the target, where the target data service regenerated CAS values because the set CAS exceeded the acceptable threshold on the target's data service.

`xdcr_docs_sent_with_subdoc_delete_total`

7.6.6 counter The number of deletes issued using subdoc command instead of delete\_with\_meta to avoid cas rollback on target

`xdcr_docs_sent_with_subdoc_set_total`

7.6.6 counter The number of sets issued using subdoc command instead of set\_with\_meta to avoid cas rollback on target

`xdcr_docs_unable_to_filter_total`

7.0.0 gauge Number of Document Mutations that couldn't be filtered due to inability to parse the document through Advanced Filtering engine and were not replicated

`xdcr_docs_written_total`

7.0.0 counter Number of docs Document Mutations written/sent to the Target

`xdcr_expiry_docs_written_total`

7.0.0 counter Number of Expirations written to the Target

`xdcr_expiry_failed_cr_source_total`

7.0.0 counter Number of Expirations that failed Source-side Conflict Resolution

`xdcr_expiry_failed_cr_target_total`

7.1.0 counter Number of Expirations that failed Conflict Resolution at the Target

`xdcr_expiry_filtered_total`

7.0.0 counter Number of Expirations filtered Source-side

`xdcr_expiry_received_from_dcp_total`

7.0.0 counter Number of Expirations or documents with TTL received from the Data Service

`xdcr_expiry_stripped_total`

7.0.0 counter Number of Document Mutations replicated that had the TTL changed to 0 before writing to Target (Source is unmodified)

`xdcr_guardrail_data_size_total`

7.6.0 counter The number of writes that target rejected because each target data node is holding too much data

`xdcr_guardrail_disk_space_total`

7.6.0 counter The number of writes that target rejected because a data node is running out of disk space

`xdcr_guardrail_resident_ratio_total`

7.6.0 counter The number of writes that target rejected due to the target bucket being under the resident ratio threshold

`xdcr_hlv_pruned_at_merge_total`

7.6.6 counter Number of mutations with HLV pruned when it is merged with target document

`xdcr_hlv_pruned_total`

7.6.6 counter Number of mutations with HLV pruned

`xdcr_hlv_updated_total`

7.6.6 counter Number of mutations with HLV updated

`xdcr_import_docs_failed_cr_source_total`

7.6.6 counter Number of mobile import mutations failed Source side Conflict Resolution. This is only counted in LWW buckets when enableCrossClusterVersioning is true

`xdcr_import_docs_written_total`

7.6.6 counter Number of import mutations sent

`xdcr_mobile_docs_filtered_total`

7.6.0 counter Total number of documents filtered and not replicated because the documents were mobile records

`xdcr_num_checkpoints_total`

7.0.0 counter The number of times checkpoint operation has completed successfully since this XDCR process instance is made aware of this replication

`xdcr_num_failedckpts_total`

7.0.0 counter The number of times checkpoint operation has encountered an error since this XDCR process instance is made aware of this replication

`xdcr_number_of_replications_total`

8.0.0 gauge The total number of replications that exists to replicate to a particular target cluster

`xdcr_number_of_source_nodes_total`

8.0 gauge For a given source cluster, the number of data service nodes that it contains

`xdcr_number_of_source_replications_total`

8.0 gauge For a given source cluster, the total number of outbound replications to this cluster

`xdcr_pipeline_errors`

7.6.0 gauge The number of currently present errors for a specific Replication Pipeline

`xdcr_pipeline_status`

7.6.0 gauge The pipeline status for a specific pipeline, where it could be paused, running or, error

`xdcr_resp_wait_time_seconds`

7.0.0 gauge / seconds The rolling average amount of time it takes from when a MemcachedRequest is created to be ready to route to an outnozzle to the time that the response has been heard back from the target node after a successful write

`xdcr_seqno_adv_received_from_dcp_total`

7.6.0 counter The number of seqno advance events received from source data service

`xdcr_set_docs_written_total`

7.0.0 counter Number of Set operations successfully written to the Target

`xdcr_set_failed_cr_target_total`

7.1.0 counter Number of Set operations that failed Conflict Resolution at the Target

`xdcr_set_filtered_total`

7.0.0 counter Number of documents filtered that was of a DCP mutation

`xdcr_set_received_from_dcp_total`

7.0.0 counter Number of Sets received from the Data Service

`xdcr_size_rep_queue_bytes`

7.0.0 gauge / bytes Amount of data being queued to be sent in a Target Nozzle

`xdcr_source_sync_xattr_removed_total`

7.6.6 counter Number of mutations with source mobile extended attributes removed

`xdcr_system_events_received_from_dcp_total`

7.6.0 counter The number of system events received from source data service

`xdcr_target_eaccess_total`

7.6.0 counter The total number of EACCESS errors returned from the target node.

`xdcr_target_sync_xattr_preserved_total`

7.6.6 counter Number of mutations with target mobile extended attributes preserved

`xdcr_target_tmpfail_total`

7.6.0 counter The total number of TMPFAIL errors returned from the target node.

`xdcr_target_unknown_status_total`

7.6.0 counter The total number of writes to target data service that returned with a status code that XDCR cannot comprehend

`xdcr_throttle_latency_seconds`

7.0.0 gauge / seconds The rolling average of the latency time introduced due to bandwith throttler

`xdcr_throughput_throttle_latency_seconds`

7.0.0 gauge / seconds The rolling average of the latency time introduced due to throughput throttler

`xdcr_time_committing_seconds`

7.0.0 gauge / seconds The rolling average amount of time it takes for a checkpoint operation to complete

`xdcr_true_conflicts_detected_total`

8.0.0 counter Number of true conflicts detected when the conflict logging feature is turned on. Logging of all these conflicts to a conflict bucket is best-effort, based on the system's state.

`xdcr_wtavg_docs_latency_seconds`

7.0.0 gauge / seconds The rolling average amount of time it takes for the source cluster to receive the acknowledgement of a SET\_WITH\_META response after the Memcached request has been composed to be processed by the XDCR Target Nozzle

`xdcr_wtavg_meta_latency_seconds`

7.0.0 gauge / seconds The rolling average amount of time it takes once a getMeta command is composed to be sent to the time the request is handled once the target node has responded