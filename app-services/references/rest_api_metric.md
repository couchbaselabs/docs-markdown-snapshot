---
title: Capella App Services Metrics API Reference
editUrl: https://github.com/couchbaselabs/docs-capella-app-services/edit/main/modules/ROOT/pages/references/rest_api_metric.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/app-services/references/rest_api_metric.html)

# Capella App Services Metrics API Reference

* Introduction
* Prometheus
  * getGet debugging and monitoring runtime stats in Prometheus Exposition format

[API docs by Redocly](https://redocly.com/redoc/)

# App Services Metrics API (4.0)

Download OpenAPI specification:

License: [Business Source License 1.1 (BSL)](https://github.com/couchbase/sync%5Fgateway/blob/master/LICENSE) 

[⬆️ Manage App Services with the App Services API](rest-api-introduction.html)

## [](#section/Introduction)Introduction

App Services manages access and synchronization between Couchbase Lite and Couchbase Capella. The App Services Metrics REST API returns App Services metrics, in Prometheus-compatible format, for performance monitoring and diagnostic purposes.

## [](#tag/Prometheus)Prometheus

Endpoints for use with Prometheus

## [](#tag/Prometheus/operation/get%5Fmetrics)Get debugging and monitoring runtime stats in Prometheus Exposition format 

Returns App Services statistics and other runtime variables in Prometheus Exposition format.

### Responses

**200** 

Successfully returned statistics. For details, see [Prometheus Metrics](/sync-gateway/current/stats-monitoring-prometheus.html).

get/metrics

Metrics API

https://{hostname}:4988/metrics

### Response samples 

* 200

Content type

application/json

Copy

`{
* "sgw_audit_num_audits_filtered_by_role": 0,
* "sgw_audit_num_audits_filtered_by_user": 0,
* "sgw_audit_num_audits_logged": 0,
* "sgw_cache_abandoned_seqs": 0,
* "sgw_cache_chan_cache_active_revs": 0,
* "sgw_cache_chan_cache_bypass_count": 0,
* "sgw_cache_chan_cache_channels_added": 0,
* "sgw_cache_chan_cache_channels_evicted_inactive": 0,
* "sgw_cache_chan_cache_channels_evicted_nru": 0,
* "sgw_cache_chan_cache_compact_count": 0,
* "sgw_cache_chan_cache_compact_time": 0,
* "sgw_cache_chan_cache_hits": 0,
* "sgw_cache_chan_cache_max_entries": 0,
* "sgw_cache_chan_cache_misses": 0,
* "sgw_cache_chan_cache_num_channels": 0,
* "sgw_cache_chan_cache_pending_queries": 0,
* "sgw_cache_chan_cache_removal_revs": 0,
* "sgw_cache_chan_cache_tombstone_revs": 0,
* "sgw_cache_current_skipped_seq_count": 0,
* "sgw_cache_high_seq_cached": 0,
* "sgw_cache_high_seq_stable": 0,
* "sgw_cache_non_mobile_ignored_count": 0,
* "sgw_cache_num_active_channels": 0,
* "sgw_cache_num_skipped_seqs": 0,
* "sgw_cache_pending_seq_len": 0,
* "sgw_cache_rev_cache_bypass": 0,
* "sgw_cache_rev_cache_hits": 0,
* "sgw_cache_rev_cache_misses": 0,
* "sgw_cache_revision_cache_num_items": 0,
* "sgw_cache_revision_cache_total_memory": 0,
* "sgw_cache_skipped_seq_cap": 0,
* "sgw_cache_skipped_seq_len": 0,
* "sgw_cache_view_queries": 0,
* "sgw_collection_doc_reads_bytes": 0,
* "sgw_collection_doc_writes_bytes": 0,
* "sgw_collection_import_count": 0,
* "sgw_collection_num_doc_reads": 0,
* "sgw_collection_num_doc_writes": 0,
* "sgw_collection_sync_function_count": 0,
* "sgw_collection_sync_function_exception_count": 0,
* "sgw_collection_sync_function_reject_access_count": 0,
* "sgw_collection_sync_function_reject_count": 0,
* "sgw_collection_sync_function_time": 0,
* "sgw_config_database_config_bucket_mismatches": 0,
* "sgw_config_database_config_collection_conflicts": 0,
* "sgw_database_compaction_attachment_start_time": 0,
* "sgw_database_compaction_tombstone_start_time": 0,
* "sgw_database_conflict_write_count": 0,
* "sgw_database_crc32c_match_count": 0,
* "sgw_database_dcp_caching_count": 0,
* "sgw_database_dcp_caching_time": 0,
* "sgw_database_dcp_received_count": 0,
* "sgw_database_dcp_received_time": 0,
* "sgw_database_doc_reads_bytes_blip": 0,
* "sgw_database_doc_writes_bytes": 0,
* "sgw_database_doc_writes_bytes_blip": 0,
* "sgw_database_doc_writes_xattr_bytes": 0,
* "sgw_database_high_seq_feed": 0,
* "sgw_database_http_bytes_written": 0,
* "sgw_database_num_attachments_compacted": 0,
* "sgw_database_num_doc_reads_blip": 0,
* "sgw_database_num_doc_reads_rest": 0,
* "sgw_database_num_doc_writes": 0,
* "sgw_database_num_idle_kv_ops": 0,
* "sgw_database_num_public_rest_requests": 0,
* "sgw_database_num_replications_active": 0,
* "sgw_database_num_replications_rejected_limit": 0,
* "sgw_database_num_replications_total": 0,
* "sgw_database_num_tombstones_compacted": 0,
* "sgw_database_public_rest_bytes_read": 0,
* "sgw_database_replication_bytes_received": 0,
* "sgw_database_replication_bytes_sent": 0,
* "sgw_database_sequence_assigned_count": 0,
* "sgw_database_sequence_get_count": 0,
* "sgw_database_sequence_incr_count": 0,
* "sgw_database_sequence_released_count": 0,
* "sgw_database_sequence_reserved_count": 0,
* "sgw_database_sync_function_count": 0,
* "sgw_database_sync_function_exception_count": 0,
* "sgw_database_sync_function_time": 0,
* "sgw_database_total_sync_time": 0,
* "sgw_database_warn_channel_name_size_count": 0,
* "sgw_database_warn_channels_per_doc_count": 0,
* "sgw_database_warn_grants_per_doc_count": 0,
* "sgw_database_warn_xattr_size_count": 0,
* "sgw_delta_sync_delta_cache_hit": 0,
* "sgw_delta_sync_delta_pull_replication_count": 0,
* "sgw_delta_sync_delta_push_doc_count": 0,
* "sgw_delta_sync_delta_sync_miss": 0,
* "sgw_delta_sync_deltas_requested": 0,
* "sgw_delta_sync_deltas_sent": 0,
* "sgw_gsi_views__count": 0,
* "sgw_gsi_views__error_count": 0,
* "sgw_gsi_views__time": 0,
* "sgw_replication_expected_sequence_len": 0,
* "sgw_replication_expected_sequence_len_post_cleanup": 0,
* "sgw_replication_processed_sequence_len": 0,
* "sgw_replication_processed_sequence_len_post_cleanup": 0,
* "sgw_replication_pull_attachment_pull_bytes": 0,
* "sgw_replication_pull_attachment_pull_count": 0,
* "sgw_replication_pull_max_pending": 0,
* "sgw_replication_pull_norev_send_count": 0,
* "sgw_replication_pull_num_pull_repl_active_continuous": 0,
* "sgw_replication_pull_num_pull_repl_active_one_shot": 0,
* "sgw_replication_pull_num_pull_repl_caught_up": 0,
* "sgw_replication_pull_num_pull_repl_since_zero": 0,
* "sgw_replication_pull_num_pull_repl_total_caught_up": 0,
* "sgw_replication_pull_num_pull_repl_total_continuous": 0,
* "sgw_replication_pull_num_pull_repl_total_one_shot": 0,
* "sgw_replication_pull_num_replications_active": 0,
* "sgw_replication_pull_replacement_rev_send_count": 0,
* "sgw_replication_pull_request_changes_count": 0,
* "sgw_replication_pull_request_changes_time": 0,
* "sgw_replication_pull_rev_error_count": 0,
* "sgw_replication_pull_rev_processing_time": 0,
* "sgw_replication_pull_rev_send_count": 0,
* "sgw_replication_pull_rev_send_latency": 0,
* "sgw_replication_push_attachment_push_bytes": 0,
* "sgw_replication_push_attachment_push_count": 0,
* "sgw_replication_push_doc_push_count": 0,
* "sgw_replication_push_doc_push_error_count": 0,
* "sgw_replication_push_propose_change_count": 0,
* "sgw_replication_push_propose_change_time": 0,
* "sgw_replication_push_write_processing_time": 0,
* "sgw_replication_push_write_throttled_count": 0,
* "sgw_replication_push_write_throttled_time": 0,
* "sgw_replication_sgr_conflict_resolved_local_count": 0,
* "sgw_replication_sgr_conflict_resolved_merge_count": 0,
* "sgw_replication_sgr_conflict_resolved_remote_count": 0,
* "sgw_replication_sgr_deltas_recv": 0,
* "sgw_replication_sgr_deltas_requested": 0,
* "sgw_replication_sgr_deltas_sent": 0,
* "sgw_replication_sgr_docs_checked_recv": 0,
* "sgw_replication_sgr_docs_checked_sent": 0,
* "sgw_replication_sgr_num_attachment_bytes_pulled": 0,
* "sgw_replication_sgr_num_attachment_bytes_pushed": 0,
* "sgw_replication_sgr_num_attachments_pulled": 0,
* "sgw_replication_sgr_num_attachments_pushed": 0,
* "sgw_replication_sgr_num_connect_attempts_pull": 0,
* "sgw_replication_sgr_num_connect_attempts_push": 0,
* "sgw_replication_sgr_num_docs_failed_to_pull": 0,
* "sgw_replication_sgr_num_docs_failed_to_push": 0,
* "sgw_replication_sgr_num_docs_pulled": 0,
* "sgw_replication_sgr_num_docs_purged": 0,
* "sgw_replication_sgr_num_docs_pushed": 0,
* "sgw_replication_sgr_num_handlers_panicked": 0,
* "sgw_replication_sgr_num_reconnects_aborted_pull": 0,
* "sgw_replication_sgr_num_reconnects_aborted_push": 0,
* "sgw_replication_sgr_push_conflict_count": 0,
* "sgw_replication_sgr_push_rejected_count": 0,
* "sgw_resource_utilization_admin_net_bytes_recv": 0,
* "sgw_resource_utilization_admin_net_bytes_sent": 0,
* "sgw_resource_utilization_error_count": 0,
* "sgw_resource_utilization_go_memstats_heapalloc": 0,
* "sgw_resource_utilization_go_memstats_heapidle": 0,
* "sgw_resource_utilization_go_memstats_heapinuse": 0,
* "sgw_resource_utilization_go_memstats_heapreleased": 0,
* "sgw_resource_utilization_go_memstats_pausetotalns": 0,
* "sgw_resource_utilization_go_memstats_stackinuse": 0,
* "sgw_resource_utilization_go_memstats_stacksys": 0,
* "sgw_resource_utilization_go_memstats_sys": 0,
* "sgw_resource_utilization_goroutines_high_watermark": 0,
* "sgw_resource_utilization_node_cpu_percent_utilization": 0,
* "sgw_resource_utilization_num_goroutines": 0,
* "sgw_resource_utilization_process_cpu_percent_utilization": 0,
* "sgw_resource_utilization_process_memory_resident": 0,
* "sgw_resource_utilization_pub_net_bytes_recv": 0,
* "sgw_resource_utilization_pub_net_bytes_sent": 0,
* "sgw_resource_utilization_system_memory_total": 0,
* "sgw_resource_utilization_uptime": 0,
* "sgw_resource_utilization_warn_count": 0,
* "sgw_security_auth_failed_count": 0,
* "sgw_security_auth_success_count": 0,
* "sgw_security_num_access_errors": 0,
* "sgw_security_num_docs_rejected": 0,
* "sgw_security_total_auth_time": 0,
* "sgw_shared_bucket_import_import_cancel_cas": 0,
* "sgw_shared_bucket_import_import_count": 0,
* "sgw_shared_bucket_import_import_error_count": 0,
* "sgw_shared_bucket_import_import_high_seq": 0,
* "sgw_shared_bucket_import_import_partitions": 0,
* "sgw_shared_bucket_import_import_processing_time": 0
}`