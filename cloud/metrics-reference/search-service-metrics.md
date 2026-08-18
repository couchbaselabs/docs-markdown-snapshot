---
title: Search Service Metrics
description: A list of the metrics provided by the Search Service.
pubDate: 2026-08-18T04:50:45.818Z
antora:
  editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/metrics-reference/pages/search-service-metrics.adoc
  xref: xref:cloud:metrics-reference:search-service-metrics.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/metrics-reference/search-service-metrics.html)

# Search Service Metrics

> A list of the metrics provided by the Search Service. 

> [!TIP]
> * The x.y.z badge shows the Couchbase Server version the metric was added in.
> * The type / unit badge shows shows the Prometheus [type](https://prometheus.io/docs/tutorials/understanding%5Fmetric%5Ftypes/) and [unit](https://prometheus.io/docs/practices/naming/#base-units) (if present).

`fts_avg_grpc_queries_latency`

7.2.0 gauge / milliseconds Average latency per query, using gRPC for streaming, for an index

`fts_avg_internal_queries_latency`

7.2.0 gauge / milliseconds Average latency of inter-node queries per unit time for an index

`fts_avg_queries_latency`

7.2.0 gauge / milliseconds Average latency of queries per unit time for an index

`fts_batch_bytes_added`

7.2.0 counter / bytes Total number of bytes from batches yet to be indexed.

`fts_batch_bytes_removed`

7.2.0 counter / bytes Total number of bytes from batches which have been indexed.

`fts_boot_timestamp_seconds`

7.5.0 gauge / seconds The time the service booted in fractional seconds since Unix epoch.

`fts_counter_cu_total`

7.5.0 counter / seconds The number of distinct operations recording Compute Units (CUs) with Regulator.

`fts_counter_ru_total`

7.5.0 counter / seconds The number of distinct operations recording Read Units (RUs) with Regulator.

`fts_counter_wu_total`

7.5.0 counter / seconds The number of distinct operations recording Write Units (WUs) with Regulator.

`fts_credit_cu_total`

7.5.0 counter / seconds The number of Compute Units (CUs) refunded.

`fts_credit_ru_total`

7.5.0 counter / seconds The number of Read Units (RUs) refunded.

`fts_credit_wu_total`

7.5.0 counter / seconds The number of Write Units (WUs) refunded.

`fts_curr_batches_blocked_by_herder`

7.2.0 gauge The difference between the number of batches that have been indexed and the number of batches yet to be indexed

`fts_doc_count`

7.2.0 counter Number of documents in the index

`fts_global_query_timer_count`

8.0.0 counter The number of query timer events received at the global query endpoint

`fts_global_query_timer_mean_ns`

8.0.0 gauge Mean runtime for queries received at the global query endpoint

`fts_global_query_timer_median_ns`

8.0.0 gauge Median runtime for queries received at the global query endpoint

`fts_global_query_timer_p80_ns`

8.0.0 gauge 80th percentile runtime for queries received at the global query endpoint

`fts_global_query_timer_p99_ns`

8.0.0 gauge 99th percentile runtime for queries received at the global query endpoint

`fts_grpc_query_timer_count`

8.0.0 counter The number of query timer events received at the gRPC endpoint

`fts_grpc_query_timer_mean_ns`

8.0.0 gauge Mean runtime for queries received at the gRPC endpoint

`fts_grpc_query_timer_median_ns`

8.0.0 gauge Median runtime for queries received at the gRPC endpoint

`fts_grpc_query_timer_p80_ns`

8.0.0 gauge 80th percentile runtime for queries received at the gRPC endpoint

`fts_grpc_query_timer_p99_ns`

8.0.0 gauge 99th percentile runtime for queries received at the gRPC endpoint

`fts_meter_cu_total`

7.5.0 counter / seconds The number of Compute Units (CUs) recorded.

`fts_meter_ru_total`

7.5.0 counter / seconds The number of Read Units (RUs) recorded.

`fts_meter_wu_total`

7.5.0 counter / seconds The number of Write Units (WUs) recorded.

`fts_num_batches_introduced`

7.2.0 counter Total number of batches introduced as part of indexing.

`fts_num_bytes_ram_quota`

7.6.0 gauge / bytes The number of bytes allocated by the cluster manager as maximum usable memory for fts service

`fts_num_bytes_used_disk`

7.2.0 gauge / bytes The number of bytes used on disk by the index

`fts_num_bytes_used_disk_by_root`

7.2.0 gauge / bytes The number of bytes used on disk by the root segment

`fts_num_bytes_used_ram`

7.2.0 gauge / bytes The number of bytes used in memory

`fts_num_files_on_disk`

7.2.0 gauge The number of files on disk for an index

`fts_num_indexes`

8.0.0 gauge Number of search indexes in the cluster

`fts_num_knn_search_requests`

7.6.0 counter Total number of search requests with KNN

`fts_num_mutations_to_index`

7.2.0 gauge DCP sequence numbers yet to be indexed for an index

`fts_num_pindexes_actual`

7.2.0 gauge Total number of pindexes currently

`fts_num_pindexes_target`

7.2.0 gauge Planned/expected number of pindexes

`fts_num_recs_to_persist`

7.2.0 gauge The number of entries (terms, records, dictionary rows, etc) by Bleve not yet persisted to storage

`fts_num_root_filesegments`

7.2.0 gauge The number of file segments in the root segment

`fts_num_root_memorysegments`

7.2.0 gauge The number of memory segments in the root segment

`fts_num_vector_indexes`

8.0.0 gauge Number of search indexes in the cluster that have vector/vector\_base64 fields

`fts_op_count_total`

7.5.0 counter / seconds The number of distinct operations recorded with Regulator.

`fts_pct_cpu_gc`

7.2.0 gauge / percent The percentage of CPU time spent by an index in garbage collection

`fts_pct_used_ram`

7.6.0 gauge / percent The percentage of RAM quota used by the fts service

`fts_reject_count_total`

7.5.0 counter / seconds The number of times Regulator instructed an operation to be rejected.

`fts_scoped_query_timer_count`

8.0.0 counter The number of query timer events received at the scoped query endpoint

`fts_scoped_query_timer_mean_ns`

8.0.0 gauge Mean runtime for queries received at the scoped query endpoint

`fts_scoped_query_timer_median_ns`

8.0.0 gauge Median runtime for queries received at the scoped query endpoint

`fts_scoped_query_timer_p80_ns`

8.0.0 gauge 80th percentile runtime for queries received at the scoped query endpoint

`fts_scoped_query_timer_p99_ns`

8.0.0 gauge 99th percentile runtime for queries received at the scoped query endpoint

`fts_throttle_count_total`

7.5.0 counter / seconds The number of times Regulator instructed an operation to throttle.

`fts_throttle_seconds_total`

7.5.0 counter / seconds The total time spent throttling (in seconds).

`fts_tot_batches_flushed_on_maxops`

7.2.0 counter Total number of batches executed due to the batch size being greater than the maximum number of operations per batch

`fts_tot_batches_flushed_on_timer`

7.2.0 counter Total number of batches executed at regular intervals

`fts_tot_bleve_dest_closed`

7.2.0 counter Total number of times Bleve destinations closed

`fts_tot_bleve_dest_opened`

7.2.0 counter The number of times Bleve destinations opened

`fts_tot_grpc_listeners_closed`

7.2.0 counter Total number of gRPC listeners closed

`fts_tot_grpc_listeners_opened`

7.2.0 counter Total number of gRPC listeners opened

`fts_tot_grpc_queryreject_on_memquota`

7.2.0 counter Total number of gRPC queries rejected due to the memory quota being lesser than the estimated memory required for merging search results from all partitions from the query

`fts_tot_grpcs_listeners_closed`

7.2.0 counter Total number of gRPC SSL listeners closed

`fts_tot_grpcs_listeners_opened`

7.2.0 counter Total number of gRPC SSL listeners opened

`fts_tot_http_limitlisteners_closed`

7.2.0 counter Total number of HTTP limit listeners closed

`fts_tot_http_limitlisteners_opened`

7.2.0 counter Total number of HTTP limit listeners opened

`fts_tot_https_limitlisteners_closed`

7.2.0 counter Total number of HTTPS limit listeners closed

`fts_tot_https_limitlisteners_opened`

7.2.0 counter Total number of HTTPS limit listeners opened

`fts_tot_queryreject_on_memquota`

7.2.0 counter Total number of queries rejected due to the memory quota being lesser than the estimated memory required for merging search results from all partitions from the query

`fts_tot_remote_grpc`

7.2.0 counter Total number of remote(i.e. different node) gRPC requests

`fts_tot_remote_grpc_ssl`

7.6.0 counter Total number of remote(i.e. different node) gRPC SSL requests when adding clients.

`fts_tot_remote_grpc_tls`

7.2.0 counter Total number of remote(i.e. different node) gRPC SSL requests when adding clients.

`fts_tot_remote_http`

7.2.0 counter Total number of remote(i.e. different node) HTTP requests

`fts_tot_remote_http2`

7.2.0 counter Total number of remote(i.e. different node) HTTP SSL requests

`fts_tot_remote_http_ssl`

7.6.0 counter Total number of remote(i.e. different node) HTTP SSL requests

`fts_total_bytes_indexed`

7.2.0 gauge Rate of bytes indexed for an index

`fts_total_bytes_query_results`

7.2.0 counter / bytes Size of results coming back from full text queries for search results, including the entire size of the JSON sent

`fts_total_compaction_written_bytes`

7.2.0 counter / bytes Number of bytes written to disk as a result of compaction

`fts_total_gc`

7.2.0 counter The number of garbage collection events triggered

`fts_total_grpc_internal_queries`

7.2.0 counter The number of internal gRPC requests from the co-ordinating node for the query to other nodes, for an index

`fts_total_grpc_queries`

7.2.0 counter The total number of queries, using gRPC for streaming, for an index

`fts_total_grpc_queries_error`

7.2.0 counter The number of queries that resulted in an error, using gRPC for streaming, for an index

`fts_total_grpc_queries_slow`

7.2.0 counter The number of queries in the slow query log, using gRPC for streaming, for an index

`fts_total_grpc_queries_timeout`

7.2.0 counter The number of queries that exceeded the timeout, using gRPC for streaming, for an index

`fts_total_internal_queries`

7.2.0 counter The number of internal queries from the co-ordinating node to other nodes, per unit time for an index

`fts_total_knn_searches`

7.6.0 counter Total bleve knn search operations

`fts_total_mutations_filtered`

8.0.0 counter Total number of mutations that qualify for any document filter in an index (in-memory only stat)

`fts_total_queries`

7.2.0 counter The number of full text queries per second for an index

`fts_total_queries_bad_request_error`

7.6.0 counter The number of FTS queries that resulted in an error due to a bad request

`fts_total_queries_consistency_error`

7.6.0 counter The number of FTS queries that resulted in an error due to a failure to meet consistency requirements

`fts_total_queries_error`

7.2.0 counter The number of FTS queries for an index that resulted in an error

`fts_total_queries_max_result_window_exceeded_error`

7.6.0 counter The number of FTS queries that resulted in an error due to exceeding the maximum result window

`fts_total_queries_partial_results_error`

7.6.0 counter The number of FTS queries that resulted in an error due to only partial results being returned

`fts_total_queries_rejected_by_herder`

7.2.0 counter The number of queries rejected by the app herder when the memory used exceeds the application's query quota

`fts_total_queries_search_in_context_error`

7.6.0 counter The number of FTS queries that resulted in an error while searching in context

`fts_total_queries_slow`

7.2.0 counter The number of FTS queries in the slow query log

`fts_total_queries_timeout`

7.2.0 counter The number of FTS queries for an index that exceeded the timeout

`fts_total_queries_to_actives`

8.0.0 counter Total number of searches served by the active partitions of an index on a node

`fts_total_queries_to_replicas`

8.0.0 counter Total number of searches served by the replica partitions of an index on a node

`fts_total_request_time`

7.2.0 counter / nanoseconds Total time spent processing query requests for an index

`fts_total_synonym_searches`

8.0.0 counter Total bleve synonym search operations

`fts_total_term_searchers`

7.2.0 counter Number of bleve term searchers

`fts_total_term_searchers_finished`

7.2.0 counter Total term searchers that have finished serving a query

`fts_total_vectors`

7.6.1 gauge The total number of vectors indexed

`total_knn_queries_rejected_by_throttler`

7.6.4 counter Total number of http query requests with KNN rejected by the throttler