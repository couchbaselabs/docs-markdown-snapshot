---
title: Couchbase Search Statistics API
description: The Search Statistics REST API is provided by the Search Service.
  This API enables you to get statistics for the Search Service and your Search
  indexes.
editUrl: https://github.com/couchbaselabs/cb-swagger/edit/release/8.0/docs/modules/fts-rest-stats/pages/index.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:fts-rest-stats:index.adoc[]
---

[View original HTML](/server/current/fts-rest-stats/index.html)

# Couchbase Search Statistics API

## [](#overview)Overview

The Search Statistics REST API is provided by the Search service. This API enables you to get statistics for the Search Service and your Search indexes.

### Version information

**Version:** 8.0

### Host information

{scheme}://{host}:{port}

The URL scheme, host, and port are as follows.

| Component  | Description                                                                              |
| ---------- | ---------------------------------------------------------------------------------------- |
| **scheme** | The URL scheme. Use https for secure access. **Values:** http, https                     |
| **host**   | The host name or IP address of a node running the Search Service. **Example:** localhost |
| **port**   | The Search Service REST port. Use 18094 for secure access. **Values:** 8094, 18094       |

## [](#resources)Resources

This section describes the operations available with this REST API.

[Get Query, Mutation, and Partition Statistics for the Search Service](#g-api-nsstats)  
[Get Query, Mutation, and Partition Statistics for an Index](#g-api-nsstats-index-name)

### [](#g-api-nsstats)Get Query, Mutation, and Partition Statistics for the Search Service

GET /api/nsstats

#### [](#g-api-nsstats-description)Description

Gets query, mutation, document, partition, and compaction statistics for the Search Service and any Search indexes.

This endpoint returns statistics provided by the Cluster Manager. For additional statistics, including detailed partition information, see [Get Indexing and Data Metrics for All Indexes](../fts-rest-indexing/index.html#g-api-stats).

Produces

* application/json

#### [](#g-api-nsstats-responses)Responses

| HTTP Code | Description                                                                                                                                                                                                                                                       | Schema                          |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| 200       | The Search Service returns statistics from the nsstats endpoint for the entire cluster, and for each Search index. For each Search index, the names of the statistics are prefixed with the bucket name and index name, in the form BUCKET:INDEX:statistic\_name. | [Service Statistics](#allStats) |
| 400       | Object not found. The URI may be malformed.                                                                                                                                                                                                                       |                                 |
| 401       | Unauthorized. Failure to authenticate.                                                                                                                                                                                                                            |                                 |
| 403       | Forbidden. The user authenticates but does not have the appropriate permissions.                                                                                                                                                                                  |                                 |

#### [](#g-api-nsstats-security)Security

| Type         | Name                     |
| ------------ | ------------------------ |
| http (basic) | [Admin](#security-Admin) |

#### [](#g-api-nsstats-ex-response)Example HTTP Response

A successful response returns an object like [Response 200](#g-api-nsstats-ex-response-200), which contains statistics on 2 indexes, `travel-sample-index` and `color-test`.

If a user authenticates but does not have the appropriate permissions, the API returns a `403 Forbidden` response with an object similar to [Response 403](#g-api-nsstats-ex-response-403).

Response 200

```json
{
  "avg_queries_latency" : 4.174125,
  "batch_bytes_added" : 135958,
  "batch_bytes_removed" : 14750,
  "curr_batches_blocked_by_herder" : 6,
  "num_batches_introduced" : 8,
  "num_bytes_ram_quota" : 524288000,
  "num_bytes_used_disk" : 150712,
  "num_bytes_used_ram" : 501286800,
  "num_bytes_used_ram_c" : 799240,
  "num_files_on_disk" : 3,
  "num_gocbcore_dcp_agents" : 2,
  "num_gocbcore_stats_agents" : 4,
  "num_indexes" : 2,
  "num_knn_search_requests" : 0,
  "num_vector_indexes" : 2,
  "pct_cpu_gc" : 3.1540216503022397E-4,
  "pct_used_ram" : 95.61286926269531,
  "tot_batches_flushed_on_maxops" : 0,
  "tot_batches_flushed_on_timer" : 8,
  "tot_batches_merged" : 59,
  "tot_batches_new" : 14,
  "tot_bleve_dest_closed" : 2,
  "tot_bleve_dest_opened" : 4,
  "tot_grpc_listeners_closed" : 0,
  "tot_grpc_listeners_opened" : 1,
  "tot_grpc_queryreject_on_memquota" : 0,
  "tot_grpcs_listeners_closed" : 0,
  "tot_grpcs_listeners_opened" : 1,
  "tot_http_limitlisteners_closed" : 0,
  "tot_http_limitlisteners_opened" : 1,
  "tot_https_limitlisteners_closed" : 0,
  "tot_https_limitlisteners_opened" : 2,
  "tot_queryreject_on_memquota" : 0,
  "tot_remote_grpc" : 0,
  "tot_remote_grpc_ssl" : 0,
  "tot_remote_grpc_tls" : 0,
  "tot_remote_http" : 0,
  "tot_remote_http2" : 0,
  "tot_remote_http_ssl" : 0,
  "tot_rollback_full" : 0,
  "tot_rollback_partial" : 0,
  "total_bytes_query_results" : 383,
  "total_create_index_bad_request_error" : 0,
  "total_create_index_internal_server_error" : 0,
  "total_create_index_request" : 0,
  "total_create_index_request_ok" : 0,
  "total_delete_index_bad_request_error" : 0,
  "total_delete_index_internal_server_error" : 0,
  "total_delete_index_request" : 0,
  "total_delete_index_request_ok" : 0,
  "total_gc" : 64,
  "total_internal_queries" : 0,
  "total_knn_queries_rejected_by_throttler" : 0,
  "total_queries" : 1,
  "total_queries_bad_request_error" : 0,
  "total_queries_consistency_error" : 0,
  "total_queries_error" : 0,
  "total_queries_max_result_window_exceeded_error" : 0,
  "total_queries_partial_results_error" : 0,
  "total_queries_rejected_by_herder" : 0,
  "total_queries_search_in_context_error" : 0,
  "total_queries_slow" : 0,
  "total_queries_timeout" : 0,
  "total_queries_validation_error" : 0,
  "total_request_time" : 4188959,
  "travel-sample:travel-sample.inventory.travel-sample-index:avg_grpc_internal_queries_latency" : 0,
  "travel-sample:travel-sample.inventory.travel-sample-index:avg_grpc_queries_latency" : 0,
  "travel-sample:travel-sample.inventory.travel-sample-index:avg_internal_queries_latency" : 0,
  "travel-sample:travel-sample.inventory.travel-sample-index:avg_queries_latency" : 4.174125,
  "travel-sample:travel-sample.inventory.travel-sample-index:doc_count" : 28,
  "travel-sample:travel-sample.inventory.travel-sample-index:global_query_timer_count" : 0,
  "travel-sample:travel-sample.inventory.travel-sample-index:global_query_timer_mean_ns" : 0,
  "travel-sample:travel-sample.inventory.travel-sample-index:global_query_timer_median_ns" : 0,
  "travel-sample:travel-sample.inventory.travel-sample-index:global_query_timer_p80_ns" : 0,
  "travel-sample:travel-sample.inventory.travel-sample-index:global_query_timer_p99_ns" : 0,
  "travel-sample:travel-sample.inventory.travel-sample-index:grpc_query_timer_count" : 0,
  "travel-sample:travel-sample.inventory.travel-sample-index:grpc_query_timer_mean_ns" : 0,
  "travel-sample:travel-sample.inventory.travel-sample-index:grpc_query_timer_median_ns" : 0,
  "travel-sample:travel-sample.inventory.travel-sample-index:grpc_query_timer_p80_ns" : 0,
  "travel-sample:travel-sample.inventory.travel-sample-index:grpc_query_timer_p99_ns" : 0,
  "travel-sample:travel-sample.inventory.travel-sample-index:index_bgthreads_active" : false,
  "travel-sample:travel-sample.inventory.travel-sample-index:last_access_time" : "2025-10-09T13:27:20.847+00:00",
  "travel-sample:travel-sample.inventory.travel-sample-index:num_bytes_read_at_query_time" : 36,
  "travel-sample:travel-sample.inventory.travel-sample-index:num_bytes_used_disk" : 85176,
  "travel-sample:travel-sample.inventory.travel-sample-index:num_bytes_used_disk_by_root" : 19640,
  "travel-sample:travel-sample.inventory.travel-sample-index:num_bytes_used_disk_by_root_reclaimable" : 0,
  "travel-sample:travel-sample.inventory.travel-sample-index:num_bytes_written_at_index_time" : 11102,
  "travel-sample:travel-sample.inventory.travel-sample-index:num_file_merge_ops" : 0,
  "travel-sample:travel-sample.inventory.travel-sample-index:num_files_on_disk" : 2,
  "travel-sample:travel-sample.inventory.travel-sample-index:num_mem_merge_ops" : 1,
  "travel-sample:travel-sample.inventory.travel-sample-index:num_mutations_to_index" : 55667,
  "travel-sample:travel-sample.inventory.travel-sample-index:num_persister_nap_merger_break" : 1,
  "travel-sample:travel-sample.inventory.travel-sample-index:num_persister_nap_pause_completed" : 2,
  "travel-sample:travel-sample.inventory.travel-sample-index:num_pindexes_actual" : 1,
  "travel-sample:travel-sample.inventory.travel-sample-index:num_pindexes_target" : 1,
  "travel-sample:travel-sample.inventory.travel-sample-index:num_recs_to_persist" : 0,
  "travel-sample:travel-sample.inventory.travel-sample-index:num_root_filesegments" : 1,
  "travel-sample:travel-sample.inventory.travel-sample-index:num_root_memorysegments" : 0,
  "travel-sample:travel-sample.inventory.travel-sample-index:scoped_query_timer_count" : 1,
  "travel-sample:travel-sample.inventory.travel-sample-index:scoped_query_timer_mean_ns" : 4174166,
  "travel-sample:travel-sample.inventory.travel-sample-index:scoped_query_timer_median_ns" : 4174166,
  "travel-sample:travel-sample.inventory.travel-sample-index:scoped_query_timer_p80_ns" : 4174166,
  "travel-sample:travel-sample.inventory.travel-sample-index:scoped_query_timer_p99_ns" : 4174166,
  "travel-sample:travel-sample.inventory.travel-sample-index:timer_batch_store_count" : 0,
  "travel-sample:travel-sample.inventory.travel-sample-index:timer_data_delete_count" : 0,
  "travel-sample:travel-sample.inventory.travel-sample-index:timer_data_update_count" : 249,
  "travel-sample:travel-sample.inventory.travel-sample-index:timer_opaque_get_count" : 256,
  "travel-sample:travel-sample.inventory.travel-sample-index:timer_opaque_set_count" : 165,
  "travel-sample:travel-sample.inventory.travel-sample-index:timer_rollback_count" : 0,
  "travel-sample:travel-sample.inventory.travel-sample-index:timer_snapshot_start_count" : 0,
  "travel-sample:travel-sample.inventory.travel-sample-index:tot_seq_received" : 2156,
  "travel-sample:travel-sample.inventory.travel-sample-index:total_bytes_indexed" : 4173,
  "travel-sample:travel-sample.inventory.travel-sample-index:total_bytes_query_results" : 383,
  "travel-sample:travel-sample.inventory.travel-sample-index:total_compaction_written_bytes" : 19640,
  "travel-sample:travel-sample.inventory.travel-sample-index:total_grpc_internal_queries" : 0,
  "travel-sample:travel-sample.inventory.travel-sample-index:total_grpc_queries" : 0,
  "travel-sample:travel-sample.inventory.travel-sample-index:total_grpc_queries_error" : 0,
  "travel-sample:travel-sample.inventory.travel-sample-index:total_grpc_queries_slow" : 0,
  "travel-sample:travel-sample.inventory.travel-sample-index:total_grpc_queries_timeout" : 0,
  "travel-sample:travel-sample.inventory.travel-sample-index:total_grpc_request_time" : 0,
  "travel-sample:travel-sample.inventory.travel-sample-index:total_internal_queries" : 0,
  "travel-sample:travel-sample.inventory.travel-sample-index:total_knn_searches" : 0,
  "travel-sample:travel-sample.inventory.travel-sample-index:total_mutations_filtered" : 28,
  "travel-sample:travel-sample.inventory.travel-sample-index:total_queries" : 1,
  "travel-sample:travel-sample.inventory.travel-sample-index:total_queries_error" : 0,
  "travel-sample:travel-sample.inventory.travel-sample-index:total_queries_slow" : 0,
  "travel-sample:travel-sample.inventory.travel-sample-index:total_queries_timeout" : 0,
  "travel-sample:travel-sample.inventory.travel-sample-index:total_queries_to_actives" : 1,
  "travel-sample:travel-sample.inventory.travel-sample-index:total_queries_to_replicas" : 0,
  "travel-sample:travel-sample.inventory.travel-sample-index:total_request_time" : 4188959,
  "travel-sample:travel-sample.inventory.travel-sample-index:total_synonym_searches" : 0,
  "travel-sample:travel-sample.inventory.travel-sample-index:total_term_searchers" : 1,
  "travel-sample:travel-sample.inventory.travel-sample-index:total_term_searchers_finished" : 1,
  "vector-sample:vector-sample.color.color-test:avg_grpc_internal_queries_latency" : 0,
  "vector-sample:vector-sample.color.color-test:avg_grpc_queries_latency" : 0,
  "vector-sample:vector-sample.color.color-test:avg_internal_queries_latency" : 0,
  "vector-sample:vector-sample.color.color-test:avg_queries_latency" : 0,
  "vector-sample:vector-sample.color.color-test:doc_count" : 0,
  "vector-sample:vector-sample.color.color-test:global_query_timer_count" : 0,
  "vector-sample:vector-sample.color.color-test:global_query_timer_mean_ns" : 0,
  "vector-sample:vector-sample.color.color-test:global_query_timer_median_ns" : 0,
  "vector-sample:vector-sample.color.color-test:global_query_timer_p80_ns" : 0,
  "vector-sample:vector-sample.color.color-test:global_query_timer_p99_ns" : 0,
  "vector-sample:vector-sample.color.color-test:grpc_query_timer_count" : 0,
  "vector-sample:vector-sample.color.color-test:grpc_query_timer_mean_ns" : 0,
  "vector-sample:vector-sample.color.color-test:grpc_query_timer_median_ns" : 0,
  "vector-sample:vector-sample.color.color-test:grpc_query_timer_p80_ns" : 0,
  "vector-sample:vector-sample.color.color-test:grpc_query_timer_p99_ns" : 0,
  "vector-sample:vector-sample.color.color-test:index_bgthreads_active" : true,
  "vector-sample:vector-sample.color.color-test:last_access_time" : "",
  "vector-sample:vector-sample.color.color-test:num_bytes_read_at_query_time" : 0,
  "vector-sample:vector-sample.color.color-test:num_bytes_used_disk" : 65536,
  "vector-sample:vector-sample.color.color-test:num_bytes_used_disk_by_root" : 0,
  "vector-sample:vector-sample.color.color-test:num_bytes_used_disk_by_root_reclaimable" : 0,
  "vector-sample:vector-sample.color.color-test:num_bytes_written_at_index_time" : 0,
  "vector-sample:vector-sample.color.color-test:num_file_merge_ops" : 0,
  "vector-sample:vector-sample.color.color-test:num_files_on_disk" : 1,
  "vector-sample:vector-sample.color.color-test:num_mem_merge_ops" : 0,
  "vector-sample:vector-sample.color.color-test:num_mutations_to_index" : 1049,
  "vector-sample:vector-sample.color.color-test:num_persister_nap_merger_break" : 0,
  "vector-sample:vector-sample.color.color-test:num_persister_nap_pause_completed" : 2,
  "vector-sample:vector-sample.color.color-test:num_pindexes_actual" : 1,
  "vector-sample:vector-sample.color.color-test:num_pindexes_target" : 1,
  "vector-sample:vector-sample.color.color-test:num_recs_to_persist" : 0,
  "vector-sample:vector-sample.color.color-test:num_root_filesegments" : 0,
  "vector-sample:vector-sample.color.color-test:num_root_memorysegments" : 0,
  "vector-sample:vector-sample.color.color-test:scoped_query_timer_count" : 0,
  "vector-sample:vector-sample.color.color-test:scoped_query_timer_mean_ns" : 0,
  "vector-sample:vector-sample.color.color-test:scoped_query_timer_median_ns" : 0,
  "vector-sample:vector-sample.color.color-test:scoped_query_timer_p80_ns" : 0,
  "vector-sample:vector-sample.color.color-test:scoped_query_timer_p99_ns" : 0,
  "vector-sample:vector-sample.color.color-test:timer_batch_store_count" : 0,
  "vector-sample:vector-sample.color.color-test:timer_data_delete_count" : 0,
  "vector-sample:vector-sample.color.color-test:timer_data_update_count" : 0,
  "vector-sample:vector-sample.color.color-test:timer_opaque_get_count" : 256,
  "vector-sample:vector-sample.color.color-test:timer_opaque_set_count" : 131,
  "vector-sample:vector-sample.color.color-test:timer_rollback_count" : 0,
  "vector-sample:vector-sample.color.color-test:timer_snapshot_start_count" : 2,
  "vector-sample:vector-sample.color.color-test:tot_seq_received" : 0,
  "vector-sample:vector-sample.color.color-test:total_bytes_indexed" : 0,
  "vector-sample:vector-sample.color.color-test:total_bytes_query_results" : 0,
  "vector-sample:vector-sample.color.color-test:total_compaction_written_bytes" : 0,
  "vector-sample:vector-sample.color.color-test:total_grpc_internal_queries" : 0,
  "vector-sample:vector-sample.color.color-test:total_grpc_queries" : 0,
  "vector-sample:vector-sample.color.color-test:total_grpc_queries_error" : 0,
  "vector-sample:vector-sample.color.color-test:total_grpc_queries_slow" : 0,
  "vector-sample:vector-sample.color.color-test:total_grpc_queries_timeout" : 0,
  "vector-sample:vector-sample.color.color-test:total_grpc_request_time" : 0,
  "vector-sample:vector-sample.color.color-test:total_internal_queries" : 0,
  "vector-sample:vector-sample.color.color-test:total_knn_searches" : 0,
  "vector-sample:vector-sample.color.color-test:total_mutations_filtered" : 0,
  "vector-sample:vector-sample.color.color-test:total_queries" : 0,
  "vector-sample:vector-sample.color.color-test:total_queries_error" : 0,
  "vector-sample:vector-sample.color.color-test:total_queries_slow" : 0,
  "vector-sample:vector-sample.color.color-test:total_queries_timeout" : 0,
  "vector-sample:vector-sample.color.color-test:total_queries_to_actives" : 0,
  "vector-sample:vector-sample.color.color-test:total_queries_to_replicas" : 0,
  "vector-sample:vector-sample.color.color-test:total_request_time" : 0,
  "vector-sample:vector-sample.color.color-test:total_synonym_searches" : 0,
  "vector-sample:vector-sample.color.color-test:total_term_searchers" : 0,
  "vector-sample:vector-sample.color.color-test:total_term_searchers_finished" : 0
}
```

Response 403

```json
{
  "message" : "Forbidden. User needs one of the following permissions",
  "permissions" : [ "cluster.fts!read" ]
}
```

### [](#g-api-nsstats-index-name)Get Query, Mutation, and Partition Statistics for an Index

GET /api/nsstats/index/{INDEX_NAME}

#### [](#g-api-nsstats-index-name-description)Description

Gets query, mutation, document, partition, and compaction statistics for the Search index specified in the endpoint URL.

This endpoint returns statistics provided by the Cluster Manager. For additional statistics, including detailed partition information, see [Get Indexing and Data Metrics for an Index](../fts-rest-indexing/index.html#g-api-stats-index-name).

Produces

* application/json

#### [](#g-api-nsstats-index-name-parameters)Parameters

Path Parameters

| Name                    | Description                                                                                                                                                                                                                                                                                                       | Schema |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **INDEX\_NAME**required | The name of the Search index definition. You must use the fully qualified name for the index, which includes the bucket and scope. To view the full, scoped name for an index for use with this endpoint: Go to the **Search** tab in the Couchbase Server Web Console. Point to the **Index Name** for an index. | String |

#### [](#g-api-nsstats-index-name-responses)Responses

| HTTP Code | Description                                                                                                                                                                                             | Schema                          |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| 200       | The Search Service returns statistics from the nsstats endpoint for the specified index. Note that for a single index, the names of the statistics are not prefixed with the bucket name or index name. | [Index Statistics](#indexStats) |

#### [](#g-api-nsstats-index-name-security)Security

| Type         | Name                               |
| ------------ | ---------------------------------- |
| http (basic) | [Statistics](#security-Statistics) |

#### [](#g-api-nsstats-index-name-ex-response)Example HTTP Response

Response 200

```json
{
  "avg_grpc_internal_queries_latency" : 0,
  "avg_grpc_queries_latency" : 0,
  "avg_internal_queries_latency" : 0,
  "avg_queries_latency" : 4.174125,
  "doc_count" : 28,
  "global_query_timer_count" : 0,
  "global_query_timer_mean_ns" : 0,
  "global_query_timer_median_ns" : 0,
  "global_query_timer_p80_ns" : 0,
  "global_query_timer_p99_ns" : 0,
  "grpc_query_timer_count" : 0,
  "grpc_query_timer_mean_ns" : 0,
  "grpc_query_timer_median_ns" : 0,
  "grpc_query_timer_p80_ns" : 0,
  "grpc_query_timer_p99_ns" : 0,
  "index_bgthreads_active" : false,
  "last_access_time" : "2025-10-09T13:27:20.847+00:00",
  "num_bytes_read_at_query_time" : 36,
  "num_bytes_used_disk" : 85176,
  "num_bytes_used_disk_by_root" : 19640,
  "num_bytes_used_disk_by_root_reclaimable" : 0,
  "num_bytes_written_at_index_time" : 11102,
  "num_file_merge_ops" : 0,
  "num_files_on_disk" : 2,
  "num_mem_merge_ops" : 1,
  "num_mutations_to_index" : 55667,
  "num_persister_nap_merger_break" : 1,
  "num_persister_nap_pause_completed" : 2,
  "num_pindexes_actual" : 1,
  "num_pindexes_target" : 1,
  "num_recs_to_persist" : 0,
  "num_root_filesegments" : 1,
  "num_root_memorysegments" : 0,
  "scoped_query_timer_count" : 1,
  "scoped_query_timer_mean_ns" : 4174166,
  "scoped_query_timer_median_ns" : 4174166,
  "scoped_query_timer_p80_ns" : 4174166,
  "scoped_query_timer_p99_ns" : 4174166,
  "timer_batch_store_count" : 0,
  "timer_data_delete_count" : 0,
  "timer_data_update_count" : 249,
  "timer_opaque_get_count" : 256,
  "timer_opaque_set_count" : 165,
  "timer_rollback_count" : 0,
  "timer_snapshot_start_count" : 0,
  "tot_seq_received" : 2156,
  "total_bytes_indexed" : 4173,
  "total_bytes_query_results" : 383,
  "total_compaction_written_bytes" : 19640,
  "total_grpc_internal_queries" : 0,
  "total_grpc_queries" : 0,
  "total_grpc_queries_error" : 0,
  "total_grpc_queries_slow" : 0,
  "total_grpc_queries_timeout" : 0,
  "total_grpc_request_time" : 0,
  "total_internal_queries" : 0,
  "total_knn_searches" : 0,
  "total_mutations_filtered" : 28,
  "total_queries" : 1,
  "total_queries_error" : 0,
  "total_queries_slow" : 0,
  "total_queries_timeout" : 0,
  "total_queries_to_actives" : 1,
  "total_queries_to_replicas" : 0,
  "total_request_time" : 4188959,
  "total_synonym_searches" : 0,
  "total_term_searchers" : 1,
  "total_term_searchers_finished" : 1
}
```

## [](#models)Definitions

This section describes the properties consumed and returned by this REST API.

[Service Statistics](#allStats)  
[Cluster Statistics](#clusterStats)  
[Index Statistics](#indexStats)

### [](#allStats)Service Statistics

 Composite Schema

| All of …​ |                                       | Schema                              |
| --------- | ------------------------------------- | ----------------------------------- |
|           | Statistics for the entire cluster.    | [Cluster Statistics](#clusterStats) |
| and       | Statistics for a single Search index. | [Index Statistics](#indexStats)     |

#### Cluster Statistics

 Object

| Property                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Schema     |
| ---------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **avg\_queries\_latency**optional                                | The average latency of all Search queries run on the cluster, in milliseconds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | BigDecimal |
| **batch\_bytes\_added**optional                                  | The total number of bytes in batches that have not yet been added to the Search index. Batches are a data structure in the Search Service, used for processing data coming in from DCP and the Data Service to the documents in a Search index.                                                                                                                                                                                                                                                                                                     | Integer    |
| **batch\_bytes\_removed**optional                                | The total number of bytes in batches that have been added to the Search index. Use together with batch\_bytes\_added to understand when indexing operations complete. Batches are a data structure in the Search Service, used for processing data coming in from DCP and the Data Service to the documents in a Search index.                                                                                                                                                                                                                      | Integer    |
| **curr\_batches\_blocked\_by\_herder**optional                   | The difference between the number of batches that have been indexed (batch\_bytes\_removed) and batches that have not yet been indexed (batch\_bytes\_added). The Search Service blocks batch indexing until there is sufficient memory available on a node. This statistic appears on the Server Web Console dashboard as **DCP Batches Blocked**.                                                                                                                                                                                                 | Integer    |
| **num\_batches\_introduced**optional                             | The total number of batches introduced as part of indexing operations. Batches are a data structure in the Search Service, used for processing data coming in from DCP and the Data Service to the documents in a Search index.                                                                                                                                                                                                                                                                                                                     | Integer    |
| **num\_bytes\_ram\_quota**optional                               | The total number of bytes set as the maximum usable memory for the Search Service on the cluster. This statistic appears on the Server Web Console dashboard as **RAM Quota for Search**.                                                                                                                                                                                                                                                                                                                                                           | Integer    |
| **num\_bytes\_used\_disk**optional                               | The total number of bytes used on disk by Search indexes in the cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Integer    |
| **num\_bytes\_used\_ram**optional                                | The number of bytes used in memory by the Search Service. This statistic appears on the Server Web Console dashboard as **RAM Used by Search**.                                                                                                                                                                                                                                                                                                                                                                                                     | Integer    |
| **num\_bytes\_used\_ram\_c**optional                             | The number of bytes used in memory by the Search Service's C language processes. This amount is included as part of the total number of bytes used in memory, given by the num\_bytes\_used\_ram statistic.                                                                                                                                                                                                                                                                                                                                         | Integer    |
| **num\_files\_on\_disk**optional                                 | The total number of files on disk for all Search indexes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Integer    |
| **num\_gocbcore\_dcp\_agents**optional                           | The total number of Go SDK DCP agents used by the Search Service to establish DCP communication with the Data Service. The number of Go SDK DCP agents should be less than or equal to the number of Search index partitions on a node.                                                                                                                                                                                                                                                                                                             | Integer    |
| **num\_gocbcore\_stats\_agents**optional                         | The total number of Go SDK agent pairs, used to retrieve statistics from the Data Service, that are present on a node. Typically, the Search Service uses one agent pair for each bucket on a node.                                                                                                                                                                                                                                                                                                                                                 | Integer    |
| **num\_indexes**optional                                         | The number of Search indexes in the cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | BigDecimal |
| **num\_knn\_search\_requests**optional                           | The total number of [Vector Search](https://docs.couchbase.com/server/8.0/vector-search/vector-search.html) requests made across all Search indexes in the cluster.                                                                                                                                                                                                                                                                                                                                                                                 | Integer    |
| **num\_vector\_indexes**optional                                 | The number of Search indexes in the cluster that have vector/vector\_base64 fields.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | BigDecimal |
| **pct\_cpu\_gc**optional                                         | The percentage of CPU time spent by a Search index in garbage collection. Garbage collection involves cleanup actions like removing unnecessary index entries.                                                                                                                                                                                                                                                                                                                                                                                      | BigDecimal |
| **pct\_used\_ram**optional                                       | The percentage of the available RAM quota used by the Search Service. This statistic appears on the Server Web Console dashboard as **Pct RAM Used by Search**.                                                                                                                                                                                                                                                                                                                                                                                     | BigDecimal |
| **tot\_batches\_flushed\_on\_maxops**optional                    | The total number of batches executed due to the batch size being greater than the maximum number of operations per batch. Batches are a data structure in the Search Service, used for processing data coming in from DCP and the Data Service to the documents in a Search index. A batch is executed when it's flushed to disk.                                                                                                                                                                                                                   | Integer    |
| **tot\_batches\_flushed\_on\_timer**optional                     | The total number of batches executed at regular intervals.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Integer    |
| **tot\_batches\_merged**optional                                 | The number of batches that have been merged together before being sent to the disk write queue. Batches are a data structure in the Search Service, used for processing data coming in from DCP and the Data Service to the documents in a Search index. A batch is executed when it's flushed to disk.                                                                                                                                                                                                                                             | Integer    |
| **tot\_batches\_new**optional                                    | The number of new batches that have been freshly introduced into the system. Batches are a data structure in the Search Service, used for processing data coming in from DCP and the Data Service to the documents in a Search index.                                                                                                                                                                                                                                                                                                               | Integer    |
| **tot\_bleve\_dest\_closed**optional                             | The total number of times a Search index partition closed to new Search requests.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Integer    |
| **tot\_bleve\_dest\_opened**optional                             | The total number of times Search index partitions were created or reopened for new Search requests, or for ingesting data coming in from DCP. Opening a Search index partition creates a file lock for concurrent access requests.                                                                                                                                                                                                                                                                                                                  | Integer    |
| **tot\_grpc\_listeners\_closed**optional                         | The total number of gRPC listeners closed. gRPC listeners handle incoming connection requests to the Search Service. The Search Service uses gRPC to manage scatter-gather operations across nodes when there are multiple nodes running the Search Service in a cluster.                                                                                                                                                                                                                                                                           | Integer    |
| **tot\_grpc\_listeners\_opened**optional                         | The total number of gRPC listeners opened. gRPC listeners handle incoming connection requests to the Search Service. The Search Service uses gRPC to manage scatter-gather operations across nodes when there are multiple nodes running the Search Service in a cluster.                                                                                                                                                                                                                                                                           | Integer    |
| **tot\_grpc\_queryreject\_on\_memquota**optional                 | The total number of gRPC queries rejected because of the available memory quota for the Search Service being less than the estimated memory required for merging search results from all partitions. For more information about how to set the Search Service's quota, see [ftsMemoryQuota](https://docs.couchbase.com/server/8.0/fts/fts-advanced-settings-ftsMemoryQuota.html). The Search Service uses gRPC to manage scatter-gather operations across nodes when there are multiple nodes running the Search Service in a cluster.              | Integer    |
| **tot\_grpcs\_listeners\_closed**optional                        | The total number of gRPC SSL listeners closed. gRPC SSL listeners handle incoming SSL connection requests to the Search Service. The Search Service uses gRPC to manage scatter-gather operations across nodes when there are multiple nodes running the Search Service in a cluster.                                                                                                                                                                                                                                                               | Integer    |
| **tot\_grpcs\_listeners\_opened**optional                        | The total number of gRPC SSL listeners opened. gRPC SSL listeners handle incoming SSL connection requests to the Search Service. The Search Service uses gRPC to manage scatter-gather operations across nodes when there are multiple nodes running the Search Service in a cluster.                                                                                                                                                                                                                                                               | Integer    |
| **tot\_http\_limitlisteners\_closed**optional                    | The total number of HTTP limit listeners closed. HTTP limit listeners manage limits on incoming HTTP requests to the Search Service.                                                                                                                                                                                                                                                                                                                                                                                                                | Integer    |
| **tot\_http\_limitlisteners\_opened**optional                    | The total number of HTTP limit listeners opened. HTTP limit listeners manage limits on incoming HTTP requests to the Search Service.                                                                                                                                                                                                                                                                                                                                                                                                                | Integer    |
| **tot\_https\_limitlisteners\_closed**optional                   | The total number of HTTPS limit listeners closed. HTTPS limit listeners manage limits on incoming HTTPS requests to the Search Service.                                                                                                                                                                                                                                                                                                                                                                                                             | Integer    |
| **tot\_https\_limitlisteners\_opened**optional                   | The total number of HTTPS limit listeners opened. HTTPS limit listeners manage limits on incoming HTTPS requests to the Search Service.                                                                                                                                                                                                                                                                                                                                                                                                             | Integer    |
| **tot\_queryreject\_on\_memquota**optional                       | The total number of Search queries rejected because of the available memory quota for the Search Service being less than the estimated memory required for merging search results from all partitions. For more information about how to set the Search Service's quota, see [ftsMemoryQuota](https://docs.couchbase.com/server/8.0/fts/fts-advanced-settings-ftsMemoryQuota.html).                                                                                                                                                                 | Integer    |
| **tot\_remote\_grpc**optional                                    | The total number of remote gRPC requests made to the Search Service. A request is remote if it comes from a different node in the cluster.                                                                                                                                                                                                                                                                                                                                                                                                          | Integer    |
| **tot\_remote\_grpc\_ssl**optional                               | The total number of gRPC scatter-gather requests made to the Search Service over SSL. A request is remote if it comes from a different node in the cluster.                                                                                                                                                                                                                                                                                                                                                                                         | Integer    |
| **tot\_remote\_grpc\_tls**optional                               | This metric is deprecated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Integer    |
| **tot\_remote\_http**optional                                    | The total number of remote HTTP requests made to the Search Service. A request is remote if it comes from a different node in the cluster. Remote HTTP requests are deprecated. Use gRPC requests, instead.                                                                                                                                                                                                                                                                                                                                         | Integer    |
| **tot\_remote\_http2**optional                                   | The total number of remote HTTPS requests made to the Search Service. A request is remote if it comes from a different node in the cluster. Remote HTTP requests are deprecated. Use gRPC requests, instead.                                                                                                                                                                                                                                                                                                                                        | Integer    |
| **tot\_remote\_http\_ssl**optional                               | The total number of remote HTTP SSL requests made to the Search Service. A request is remote if it comes from a different node in the cluster. Remote HTTP requests are deprecated. Use gRPC requests, instead.                                                                                                                                                                                                                                                                                                                                     | Integer    |
| **tot\_rollback\_full**optional                                  | The total number of full rollbacks that occurred on a Search index partition. The Search Service only maintains a small number of index snapshots at one time. If the Search Service loses connection to the Data Service, the Search Service compares rollback sequence numbers when the connection is re-established. If the Search Service's index snapshots are too far ahead of the Data Service's rollback sequence number, the Search Service performs a full rollback operation on documents in the index.                                  | Integer    |
| **tot\_rollback\_partial**optional                               | The total number of partial rollbacks that occurred on a Search index partition. The Search Service only maintains a small number of index snapshots at one time. If the Search Service loses connection to the Data Service, the Search Service compares rollback sequence numbers when the connection is re-established. If the Search Service's index snapshots are too far ahead of the Data Service's rollback sequence number, the Search Service performs a partial rollback operation on documents in the index.                            | Integer    |
| **total\_bytes\_query\_results**optional                         | The size of all results returned for Search queries. This includes the size of all JSON sent.                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Integer    |
| **total\_create\_index\_bad\_request\_error**optional            | The total number of bad request errors returned for requests to create new Search indexes on the cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                           | Integer    |
| **total\_create\_index\_internal\_server\_error**optional        | The total number of internal server errors returned for requests to create new Search indexes on the cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                       | Integer    |
| **total\_create\_index\_request**optional                        | The total number of requests received by the Search Service for creating new Search indexes.                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Integer    |
| **total\_create\_index\_request\_ok**optional                    | The total number of requests received by the Search Service for creating new Search indexes that were successful.                                                                                                                                                                                                                                                                                                                                                                                                                                   | Integer    |
| **total\_delete\_index\_bad\_request\_error**optional            | The total number of bad request errors returned for requests to delete Search indexes on the cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                               | Integer    |
| **total\_delete\_index\_internal\_server\_error**optional        | The total number of internal server errors returned for requests to delete Search indexes on the cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                           | Integer    |
| **total\_delete\_index\_request**optional                        | The total number of requests received by the Search Service to delete Search indexes.                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Integer    |
| **total\_delete\_index\_request\_ok**optional                    | The total number of requests received by the Search Service to delete Search indexes that were successful.                                                                                                                                                                                                                                                                                                                                                                                                                                          | Integer    |
| **total\_gc**optional                                            | The total number of garbage collection events triggered by the Search Service. Garbage collection events include removing unnecessary index entries.                                                                                                                                                                                                                                                                                                                                                                                                | Integer    |
| **total\_internal\_queries**optional                             | The number of internal queries from the coordinating node for a Search query to other nodes running the Search Service. The Search Service uses gRPC to manage scatter-gather operations across nodes when there are multiple nodes running the Search Service in a cluster. The coordinating node is the Search node that receives the Search request and scatters it to all other Search index partitions on other nodes. The coordinating node applies filters to the results from all Search index partitions and returns the final result set. | Integer    |
| **total\_queries**optional                                       | The total number of Search queries per second across all Search indexes in the cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Integer    |
| **total\_queries\_bad\_request\_error**optional                  | The total number of bad request errors returned for Search queries on the cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Integer    |
| **total\_queries\_consistency\_error**optional                   | The total number of Search queries that encountered consistency errors on the cluster. For more information about consistency in Search queries, see [Search Request JSON Properties](https://docs.couchbase.com/server/8.0/search/search-request-params.html#ctl).                                                                                                                                                                                                                                                                                 | Integer    |
| **total\_queries\_error**optional                                | The total number of Search queries that encountered an error on the cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Integer    |
| **total\_queries\_max\_result\_window\_exceeded\_error**optional | The total number of Search queries that exceeded the [bleveMaxResultWindow](https://docs.couchbase.com/server/8.0/fts/fts-advanced-settings-bleveMaxResultWindow.html) setting.                                                                                                                                                                                                                                                                                                                                                                     | Integer    |
| **total\_queries\_partial\_results\_error**optional              | The total number of Search queries that could only return partial results. A Search query can return partial results if it times out before all partitions can respond.                                                                                                                                                                                                                                                                                                                                                                             | Integer    |
| **total\_queries\_rejected\_by\_herder**optional                 | The total number of queries rejected by the Search Service when the memory used approaches or exceeds the quota set for a query. For more information about how to set the Search Service's memory quota, see [ftsMemoryQuota](https://docs.couchbase.com/server/8.0/fts/fts-advanced-settings-ftsMemoryQuota.html). This statistic appears on the Server Web Console dashboard as **Rejected Queries**.                                                                                                                                            | Integer    |
| **total\_queries\_search\_in\_context\_error**optional           | The total number of Search queries that returned an error when running through the SearchInContext API. These errors are typically internal server errors.                                                                                                                                                                                                                                                                                                                                                                                          | Integer    |
| **total\_queries\_slow**optional                                 | The total number of Search queries that were added to the slow query log.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Integer    |
| **total\_queries\_timeout**optional                              | The total number of Search queries that timed out. You can set the timeout for a query with the [ctl object](https://docs.couchbase.com/server/8.0/search/search-request-params.html#ctl).                                                                                                                                                                                                                                                                                                                                                          | Integer    |
| **total\_queries\_validation\_error**optional                    | The total number of queries that encountered a validation error, when the query request included a validate property in the ctl object. For more information, see the [validate property](https://docs.couchbase.com/server/8.0/search/search-request-params.html#validate).                                                                                                                                                                                                                                                                        | Integer    |
| **total\_request\_time**optional                                 | The total time, in nanoseconds, spent processing Search queries across the cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Integer    |

### [](#indexStats)Index Statistics

 Object

| Property                                                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Schema           |
| ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| **BUCKET:INDEX:avg\_grpc\_internal\_queries\_latency**optional         | The average time taken for a Search query's scatter-gather requests between the coordinator and other nodes running the Search Service. The Search Service uses gRPC to manage scatter-gather operations across nodes when there are multiple nodes running the Search Service in a cluster. The coordinator is the Search node that receives the Search request and scatters it to all other Search index partitions on other nodes.                                                                                                                                                       | Integer          |
| **BUCKET:INDEX:avg\_grpc\_queries\_latency**optional                   | The average time taken for each Search query that uses gRPC, in milliseconds for the given Search index. The Search Service uses gRPC to manage scatter-gather operations across nodes when there are multiple nodes running the Search Service in a cluster.                                                                                                                                                                                                                                                                                                                               | Integer          |
| **BUCKET:INDEX:avg\_internal\_queries\_latency**optional               | The average latency, in milliseconds, for inter-node queries for the given Search index.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Integer          |
| **BUCKET:INDEX:avg\_queries\_latency**optional                         | The average latency, in milliseconds, for all Search queries on the given Search index. This statistic appears on the Server Web Console dashboard as **Search Query Latency**.                                                                                                                                                                                                                                                                                                                                                                                                             | Integer          |
| **BUCKET:INDEX:doc\_count**optional                                    | The total number of documents in the given Search index. This statistic appears on the Server Web Console dashboard as **Search Docs**.                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Integer          |
| **BUCKET:INDEX:global\_query\_timer\_count**optional                   | The number of Search query timer events received at the global query endpoint.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | BigDecimal       |
| **BUCKET:INDEX:global\_query\_timer\_mean\_ns**optional                | The mean runtime for Search queries received at the global query endpoint in nanoseconds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | BigDecimal       |
| **BUCKET:INDEX:global\_query\_timer\_median\_ns**optional              | The median runtime for Search queries received at the global query endpoint in nanoseconds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | BigDecimal       |
| **BUCKET:INDEX:global\_query\_timer\_p80\_ns**optional                 | The 80th percentile runtime for Search queries received at the global query endpoint in nanoseconds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | BigDecimal       |
| **BUCKET:INDEX:global\_query\_timer\_p99\_ns**optional                 | The 99th percentile runtime for Search queries received at the global query endpoint in nanoseconds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | BigDecimal       |
| **BUCKET:INDEX:grpc\_query\_timer\_count**optional                     | The number of Search query timer events received at the gRPC endpoint.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | BigDecimal       |
| **BUCKET:INDEX:grpc\_query\_timer\_mean\_ns**optional                  | The mean runtime for Search queries received at the gRPC endpoint in nanoseconds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | BigDecimal       |
| **BUCKET:INDEX:grpc\_query\_timer\_median\_ns**optional                | The median runtime for Search queries received at the gRPC endpoint in nanoseconds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | BigDecimal       |
| **BUCKET:INDEX:grpc\_query\_timer\_p80\_ns**optional                   | The 80th percentile runtime for Search queries received at the gRPC endpoint in nanoseconds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | BigDecimal       |
| **BUCKET:INDEX:grpc\_query\_timer\_p99\_ns**optional                   | The 99th percentile runtime for Search queries received at the gRPC endpoint in nanoseconds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | BigDecimal       |
| **BUCKET:INDEX:last\_access\_time**optional                            | The last date and time that a query ran against the given Search index.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Date (date-time) |
| **BUCKET:INDEX:num\_bytes\_read\_at\_query\_time**optional             | The total number of bytes read by all queries against the given Search index.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Integer          |
| **BUCKET:INDEX:num\_bytes\_used\_disk**optional                        | The total number of bytes used on disk by the given Search index. This statistic appears on the Server Web Console dashboard as **Search Disk Size**.                                                                                                                                                                                                                                                                                                                                                                                                                                       | Integer          |
| **BUCKET:INDEX:num\_bytes\_used\_disk\_by\_root**optional              | The total number of bytes used on disk by the root segment of the given Search index. The root segment includes all data for the Search index, excluding any segments that might be stale and will be removed by the persister or merger. Segments are stale when they're replaced by a new merged segment created by the merger. Stale segments are deleted when they're not used by any new queries. The num\_bytes\_used\_disk\_by\_root value will be less than the num\_bytes\_used\_disk value.                                                                                       | Integer          |
| **BUCKET:INDEX:num\_bytes\_used\_disk\_by\_root\_reclaimable**optional | The total number of bytes used on disk by the latest root index segment snapshot, which can potentially be reclaimed by a file merge operation. The root segment includes all data for the Search index, excluding any segments that might be stale and will be removed by the persister or merger. Segments are stale when they're replaced by a new merged segment created by the merger. Stale segments are deleted when they're not used by any new queries.                                                                                                                            | Integer          |
| **BUCKET:INDEX:num\_bytes\_written\_at\_index\_time**optional          | The total cumulative number of bytes written to disk as part of introducing segments, or files.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Integer          |
| **BUCKET:INDEX:num\_file\_merge\_ops**optional                         | The number of merge operations completed by the merger routine, over persisted files. Each Search index partition has a merger and a persister. The persister reads in-memory segments from the disk write queue and flushes them to disk. The merger consolidates flushed files from the persister and flushes the consolidated result to disk through the persister, while purging the smaller, older files. The persister and merger interact to continuously flush and merge new in-memory segments to disk.                                                                            | Integer          |
| **BUCKET:INDEX:num\_files\_on\_disk**optional                          | The total number of files on disk for the given Search index. This statistic appears on the Server Web Console dashboard as **Search Disk Files**.                                                                                                                                                                                                                                                                                                                                                                                                                                          | Integer          |
| **BUCKET:INDEX:num\_mem\_merge\_ops**optional                          | The number of merge operations completed by the merger routine, over in-memory segments. Each Search index partition has a merger and a persister. The persister reads in-memory segments from the disk write queue and flushes them to disk. The merger consolidates flushed files from the persister and flushes the consolidated result to disk through the persister, while purging the smaller, older files. The persister and merger interact to continuously flush and merge new in-memory segments to disk.                                                                         | Integer          |
| **BUCKET:INDEX:num\_mutations\_to\_index**optional                     | The DCP sequence numbers of changes that have not yet been indexed for the given Search index. This statistic appears on the Server Web Console dashboard as **Search Mutations Remaining**.                                                                                                                                                                                                                                                                                                                                                                                                | Integer          |
| **BUCKET:INDEX:num\_persister\_nap\_merger\_break**optional            | The number of times the persister was interrupted by the merger during a nap period. Each Search index partition has a merger and a persister. The persister reads in-memory segments from the disk write queue and flushes them to disk. The merger consolidates flushed files from the persister and flushes the consolidated result to disk through the persister, while purging the smaller, older files. The persister and merger interact to continuously flush and merge new in-memory segments to disk.                                                                             | Integer          |
| **BUCKET:INDEX:num\_persister\_nap\_pause\_completed**optional         | The number of times the persister completed its configured nap period before flushing content to disk, without being interrupted by the merger. Each Search index partition has a merger and a persister. The persister reads in-memory segments from the disk write queue and flushes them to disk. The merger consolidates the flushed files from the persister and flushes the consolidated result to disk through the persister, while purging the smaller, older files. The persister and merger interact to continuously flush and merge new in-memory segments to disk.              | Integer          |
| **BUCKET:INDEX:num\_pindexes\_actual**optional                         | The total number of partitions currently in the given Search index. This statistic appears on the Server Web Console dashboard as **Search Partitions**.                                                                                                                                                                                                                                                                                                                                                                                                                                    | Integer          |
| **BUCKET:INDEX:num\_pindexes\_target**optional                         | The total number of planned or expected partitions for the given Search index. This statistic appears on the Server Web Console dashboard as **Search Partitions Expected**.                                                                                                                                                                                                                                                                                                                                                                                                                | Integer          |
| **BUCKET:INDEX:num\_recs\_to\_persist**optional                        | The total number of entries, including terms, records, and dictionary rows, that have not yet been persisted to disk. This statistic appears on the Server Web Console dashboard as **Search Records to Persist**.                                                                                                                                                                                                                                                                                                                                                                          | Integer          |
| **BUCKET:INDEX:num\_root\_filesegments**optional                       | The total number of file segments in the root segment. The root segment includes all data for the Search index, excluding any segments that might be stale and will be removed by the persister or merger. This statistic appears on the Server Web Console dashboard as **Search Disk Segments**.                                                                                                                                                                                                                                                                                          | Integer          |
| **BUCKET:INDEX:num\_root\_memorysegments**optional                     | The total number of memory segments in the root segment. The root segment includes all data for the Search index, excluding any segments that might be stale and will be removed by the persister or merger. This statistic appears on the Server Web Console dashboard as **Search Memory Segments**.                                                                                                                                                                                                                                                                                      | Integer          |
| **BUCKET:INDEX:scoped\_query\_timer\_count**optional                   | The number of Search query timer events received at the scoped query endpoint.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | BigDecimal       |
| **BUCKET:INDEX:scoped\_query\_timer\_mean\_ns**optional                | The mean runtime for Search queries received at the scoped query endpoint in nanoseconds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | BigDecimal       |
| **BUCKET:INDEX:scoped\_query\_timer\_median\_ns**optional              | The median runtime for Search queries received at the scoped query endpoint in nanoseconds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | BigDecimal       |
| **BUCKET:INDEX:scoped\_query\_timer\_p80\_ns**optional                 | The 80th percentile runtime for Search queries received at the scoped query endpoint in nanoseconds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | BigDecimal       |
| **BUCKET:INDEX:scoped\_query\_timer\_p99\_ns**optional                 | The 99th percentile runtime for Search queries received at the scoped query endpoint in nanoseconds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | BigDecimal       |
| **BUCKET:INDEX:timer\_batch\_store\_count**optional                    | The total number of times batches were executed against the given Search index. Batches are a data structure in the Search Service, used for processing data coming in from DCP and the Data Service to the documents in a Search index. A batch is executed when it's flushed to disk.                                                                                                                                                                                                                                                                                                     | Integer          |
| **BUCKET:INDEX:timer\_data\_delete\_count**optional                    | The total number of delete operations received from DCP for the given Search index.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Integer          |
| **BUCKET:INDEX:timer\_data\_update\_count**optional                    | The total number of create or update operations received from DCP for the given Search index.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Integer          |
| **BUCKET:INDEX:timer\_opaque\_get\_count**optional                     | The total number of times the DCP consumer had to retrieve stored metadata to aid in reconnection for the given Search index. If the DCP connection closes, the Search Service can use this stored metadata to resume from the last stable point.                                                                                                                                                                                                                                                                                                                                           | Integer          |
| **BUCKET:INDEX:timer\_opaque\_set\_count**optional                     | The total number of times the DCP consumer updated stored metadata, based on changes to Snapshot markers or the failover log, for the given Search index.                                                                                                                                                                                                                                                                                                                                                                                                                                   | Integer          |
| **BUCKET:INDEX:timer\_rollback\_count**optional                        | The total number of DCP Rollback messages received for the given Search index.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Integer          |
| **BUCKET:INDEX:timer\_snapshot\_start\_count**optional                 | The total number of DCP Snapshot markers received for the given Search index. Snapshots contain a representation of document mutations on either a write queue or in storage.                                                                                                                                                                                                                                                                                                                                                                                                               | Integer          |
| **BUCKET:INDEX:tot\_seq\_received**optional                            | This metric is no longer used and will soon be deprecated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Integer          |
| **BUCKET:INDEX:total\_bytes\_indexed**optional                         | The rate, in bytes per second, of content indexed in the given Search index. This statistic appears on the Server Web Console dashboard as **Search Index Rate**.                                                                                                                                                                                                                                                                                                                                                                                                                           | Integer          |
| **BUCKET:INDEX:total\_bytes\_query\_results**optional                  | The size of results returned for Search queries on the given Search index. This includes the size of all JSON sent. This statistic appears on the Server Web Console dashboard as **Search Result Rate**.                                                                                                                                                                                                                                                                                                                                                                                   | Integer          |
| **BUCKET:INDEX:total\_compaction\_written\_bytes**optional             | The total number of bytes written to disk as a result of compaction operations on the given Search index. This statistic appears on the Server Web Console dashboard as **Search Compaction Rate**.                                                                                                                                                                                                                                                                                                                                                                                         | Integer          |
| **BUCKET:INDEX:total\_grpc\_internal\_queries**optional                | The total number of internal gRPC requests from the coordinating node for a Search query to other nodes running the Search Service, for the given Search index. The Search Service uses gRPC to manage scatter-gather operations across nodes when there are multiple nodes running the Search Service in a cluster. The coordinating node is the Search node that receives the Search request and scatters it to all other Search index partitions on other nodes. The coordinating node applies filters to the results from all Search index partitions and returns the final result set. | Integer          |
| **BUCKET:INDEX:total\_grpc\_queries**optional                          | The total number of queries, using gRPC for streaming, for the given Search index.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Integer          |
| **BUCKET:INDEX:total\_grpc\_queries\_error**optional                   | The total number of queries that resulted in an error that used gRPC for streaming on the given Search index.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Integer          |
| **BUCKET:INDEX:total\_grpc\_queries\_slow**optional                    | The total number of queries added to the slow query log that used gRPC for streaming on the given Search index.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Integer          |
| **BUCKET:INDEX:total\_grpc\_queries\_timeout**optional                 | The total number of queries that timed out that used gRPC for streaming on the given Search index.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Integer          |
| **BUCKET:INDEX:total\_grpc\_request\_time**optional                    | The total time, in nanoseconds, for internal scatter-gather requests. The Search Service uses gRPC to manage scatter-gather operations across nodes when there are multiple nodes running the Search Service in a cluster. The coordinating node is the Search node that receives the Search request and scatters it to all other Search index partitions on other nodes. The coordinating node applies filters to the results from all Search index partitions and returns the final result set.                                                                                           | Integer          |
| **BUCKET:INDEX:total\_internal\_queries**optional                      | The number of internal queries from the coordinating node for a Search query to other nodes running the Search Service, for the given Search index. The Search Service uses gRPC to manage scatter-gather operations across nodes when there are multiple nodes running the Search Service in a cluster. The coordinating node is the Search node that receives the Search request and scatters it to all other Search index partitions on other nodes. The coordinating node applies filters to the results from all Search index partitions and returns the final result set.             | Integer          |
| **BUCKET:INDEX:total\_knn\_searches**optional                          | The total number of [Vector Search](https://docs.couchbase.com/server/8.0/vector-search/vector-search.html) requests made to the given Search index.                                                                                                                                                                                                                                                                                                                                                                                                                                        | Integer          |
| **BUCKET:INDEX:total\_queries**optional                                | The total number of Search queries per second on the given Search index.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Integer          |
| **BUCKET:INDEX:total\_queries\_error**optional                         | The total number of Search queries on the given Search index that resulted in an error. This statistic appears on the Server Web Console dashboard as **Search Query Error Rate**.                                                                                                                                                                                                                                                                                                                                                                                                          | Integer          |
| **BUCKET:INDEX:total\_queries\_slow**optional                          | The total number of Search queries on the given Search index in the slow query log. Slow queries are any queries that take longer than 5 seconds to run. This statistic appears on the Server Web Console dashboard as **Search Slow Queries**.                                                                                                                                                                                                                                                                                                                                             | Integer          |
| **BUCKET:INDEX:total\_queries\_timeout**optional                       | The total number of Search queries on the given Search index that timed out. This statistic appears on the Server Web Console dashboard as **Search Query Timeout Rate**.                                                                                                                                                                                                                                                                                                                                                                                                                   | Integer          |
| **BUCKET:INDEX:total\_request\_time**optional                          | The total time, in nanoseconds, spent processing Search query requests for the given Search index.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Integer          |
| **BUCKET:INDEX:total\_term\_searchers**optional                        | The total number of term searchers for the given Search index. Every Search query requires 1 or more term searchers. More complex Search queries typically require more term searchers. Use this statistic to approximate how complex a query is. This statistic appears on the Server Web Console dashboard as **Term Searchers Start Rate**.                                                                                                                                                                                                                                              | Integer          |
| **BUCKET:INDEX:total\_term\_searchers\_finished**optional              | The total number of term searchers on the given Search index that have finished serving a Search query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Integer          |
| **BUCKET:INDEX:total\_vectors**optional                                | The total number of vectors inside the given Search index, across all indexed fields. If there are no vectors inside the Search index, the REST API does not return this statistic.                                                                                                                                                                                                                                                                                                                                                                                                         | Integer          |

## [](#security)Security

The Search REST APIs support HTTP basic authentication. Pass your credentials through HTTP headers.

### [](#security-Admin)Admin

You must have the **Full Admin**, **Cluster Admin**, or **Bucket Admin** role, with FTS Read permissions on the required bucket.

**Type:** http

### [](#security-Statistics)Statistics

You must have the **Search Admin** role, with Stats Read permissions on the required bucket.

**Type:** http

For more information, see [Roles](../learn/security/roles.md).