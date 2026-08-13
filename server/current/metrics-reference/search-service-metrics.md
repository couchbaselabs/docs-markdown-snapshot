---
title: Search Service Metrics
description: A list of the metrics provided by the Search Service.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/metrics-reference/pages/search-service-metrics.adoc
pubDate: 2026-08-13T05:04:50.295Z
link: xref:server:metrics-reference:search-service-metrics.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/metrics-reference/search-service-metrics.html)

# Search Service Metrics

> A list of the metrics provided by the Search Service. 

The following Search Service metrics can be queried by means of the REST APIs described in [Statistics](../rest-api/rest-statistics.md).

> [!TIP]
> * The x.y.z badge shows the Couchbase Server version the metric was added in.
> * The type / unit badge shows shows the Prometheus [type](https://prometheus.io/docs/tutorials/understanding%5Fmetric%5Ftypes/) and [unit](https://prometheus.io/docs/practices/naming/#base-units) (if present).

`fts_avg_grpc_queries_latency`

7.2.0gauge / millisecondsAverage latency per query, using gRPC for streaming, for an index

`fts_avg_internal_queries_latency`

7.2.0gauge / millisecondsAverage latency of inter-node queries per unit time for an index

`fts_avg_queries_latency`

7.2.0gauge / millisecondsAverage latency of queries per unit time for an index

`fts_batch_bytes_added`

7.2.0counter / bytesTotal number of bytes from batches yet to be indexed.

`fts_batch_bytes_removed`

7.2.0counter / bytesTotal number of bytes from batches which have been indexed.

`fts_boot_timestamp_seconds`

7.5.0gauge / secondsThe time the service booted in fractional seconds since Unix epoch.

`fts_counter_cu_total`

7.5.0counter / secondsThe number of distinct operations recording Compute Units (CUs) with Regulator.

`fts_counter_ru_total`

7.5.0counter / secondsThe number of distinct operations recording Read Units (RUs) with Regulator.

`fts_counter_wu_total`

7.5.0counter / secondsThe number of distinct operations recording Write Units (WUs) with Regulator.

`fts_credit_cu_total`

7.5.0counter / secondsThe number of Compute Units (CUs) refunded.

`fts_credit_ru_total`

7.5.0counter / secondsThe number of Read Units (RUs) refunded.

`fts_credit_wu_total`

7.5.0counter / secondsThe number of Write Units (WUs) refunded.

`fts_curr_batches_blocked_by_herder`

7.2.0gaugeThe difference between the number of batches that have been indexed and the number of batches yet to be indexed

`fts_doc_count`

7.2.0counterNumber of documents in the index

`fts_global_query_timer_count`

8.0.0counterThe number of query timer events received at the global query endpoint

`fts_global_query_timer_mean_ns`

8.0.0gaugeMean runtime for queries received at the global query endpoint

`fts_global_query_timer_median_ns`

8.0.0gaugeMedian runtime for queries received at the global query endpoint

`fts_global_query_timer_p80_ns`

8.0.0gauge80th percentile runtime for queries received at the global query endpoint

`fts_global_query_timer_p99_ns`

8.0.0gauge99th percentile runtime for queries received at the global query endpoint

`fts_grpc_query_timer_count`

8.0.0counterThe number of query timer events received at the gRPC endpoint

`fts_grpc_query_timer_mean_ns`

8.0.0gaugeMean runtime for queries received at the gRPC endpoint

`fts_grpc_query_timer_median_ns`

8.0.0gaugeMedian runtime for queries received at the gRPC endpoint

`fts_grpc_query_timer_p80_ns`

8.0.0gauge80th percentile runtime for queries received at the gRPC endpoint

`fts_grpc_query_timer_p99_ns`

8.0.0gauge99th percentile runtime for queries received at the gRPC endpoint

`fts_meter_cu_total`

7.5.0counter / secondsThe number of Compute Units (CUs) recorded.

`fts_meter_ru_total`

7.5.0counter / secondsThe number of Read Units (RUs) recorded.

`fts_meter_wu_total`

7.5.0counter / secondsThe number of Write Units (WUs) recorded.

`fts_num_batches_introduced`

7.2.0counterTotal number of batches introduced as part of indexing.

`fts_num_bytes_ram_quota`

7.6.0gauge / bytesThe number of bytes allocated by the cluster manager as maximum usable memory for fts service

`fts_num_bytes_used_disk`

7.2.0gauge / bytesThe number of bytes used on disk by the index

`fts_num_bytes_used_disk_by_root`

7.2.0gauge / bytesThe number of bytes used on disk by the root segment

`fts_num_bytes_used_ram`

7.2.0gauge / bytesThe number of bytes used in memory

`fts_num_files_on_disk`

7.2.0gaugeThe number of files on disk for an index

`fts_num_indexes`

8.0.0gaugeNumber of search indexes in the cluster

`fts_num_knn_search_requests`

7.6.0counterTotal number of search requests with KNN

`fts_num_mutations_to_index`

7.2.0gaugeDCP sequence numbers yet to be indexed for an index

`fts_num_pindexes_actual`

7.2.0gaugeTotal number of pindexes currently

`fts_num_pindexes_target`

7.2.0gaugePlanned/expected number of pindexes

`fts_num_recs_to_persist`

7.2.0gaugeThe number of entries (terms, records, dictionary rows, etc) by Bleve not yet persisted to storage

`fts_num_root_filesegments`

7.2.0gaugeThe number of file segments in the root segment

`fts_num_root_memorysegments`

7.2.0gaugeThe number of memory segments in the root segment

`fts_num_vector_indexes`

8.0.0gaugeNumber of search indexes in the cluster that have vector/vector\_base64 fields

`fts_op_count_total`

7.5.0counter / secondsThe number of distinct operations recorded with Regulator.

`fts_pct_cpu_gc`

7.2.0gauge / percentThe percentage of CPU time spent by an index in garbage collection

`fts_pct_used_ram`

7.6.0gauge / percentThe percentage of RAM quota used by the fts service

`fts_reject_count_total`

7.5.0counter / secondsThe number of times Regulator instructed an operation to be rejected.

`fts_scoped_query_timer_count`

8.0.0counterThe number of query timer events received at the scoped query endpoint

`fts_scoped_query_timer_mean_ns`

8.0.0gaugeMean runtime for queries received at the scoped query endpoint

`fts_scoped_query_timer_median_ns`

8.0.0gaugeMedian runtime for queries received at the scoped query endpoint

`fts_scoped_query_timer_p80_ns`

8.0.0gauge80th percentile runtime for queries received at the scoped query endpoint

`fts_scoped_query_timer_p99_ns`

8.0.0gauge99th percentile runtime for queries received at the scoped query endpoint

`fts_throttle_count_total`

7.5.0counter / secondsThe number of times Regulator instructed an operation to throttle.

`fts_throttle_seconds_total`

7.5.0counter / secondsThe total time spent throttling (in seconds).

`fts_tot_batches_flushed_on_maxops`

7.2.0counterTotal number of batches executed due to the batch size being greater than the maximum number of operations per batch

`fts_tot_batches_flushed_on_timer`

7.2.0counterTotal number of batches executed at regular intervals

`fts_tot_bleve_dest_closed`

7.2.0counterTotal number of times Bleve destinations closed

`fts_tot_bleve_dest_opened`

7.2.0counterThe number of times Bleve destinations opened

`fts_tot_grpc_listeners_closed`

7.2.0counterTotal number of gRPC listeners closed

`fts_tot_grpc_listeners_opened`

7.2.0counterTotal number of gRPC listeners opened

`fts_tot_grpc_queryreject_on_memquota`

7.2.0counterTotal number of gRPC queries rejected due to the memory quota being lesser than the estimated memory required for merging search results from all partitions from the query

`fts_tot_grpcs_listeners_closed`

7.2.0counterTotal number of gRPC SSL listeners closed

`fts_tot_grpcs_listeners_opened`

7.2.0counterTotal number of gRPC SSL listeners opened

`fts_tot_http_limitlisteners_closed`

7.2.0counterTotal number of HTTP limit listeners closed

`fts_tot_http_limitlisteners_opened`

7.2.0counterTotal number of HTTP limit listeners opened

`fts_tot_https_limitlisteners_closed`

7.2.0counterTotal number of HTTPS limit listeners closed

`fts_tot_https_limitlisteners_opened`

7.2.0counterTotal number of HTTPS limit listeners opened

`fts_tot_queryreject_on_memquota`

7.2.0counterTotal number of queries rejected due to the memory quota being lesser than the estimated memory required for merging search results from all partitions from the query

`fts_tot_remote_grpc`

7.2.0counterTotal number of remote(i.e. different node) gRPC requests

`fts_tot_remote_grpc_ssl`

7.6.0counterTotal number of remote(i.e. different node) gRPC SSL requests when adding clients.

`fts_tot_remote_grpc_tls`

7.2.0counterTotal number of remote(i.e. different node) gRPC SSL requests when adding clients.

`fts_tot_remote_http`

7.2.0counterTotal number of remote(i.e. different node) HTTP requests

`fts_tot_remote_http2`

7.2.0counterTotal number of remote(i.e. different node) HTTP SSL requests

`fts_tot_remote_http_ssl`

7.6.0counterTotal number of remote(i.e. different node) HTTP SSL requests

`fts_total_bytes_indexed`

7.2.0gaugeRate of bytes indexed for an index

`fts_total_bytes_query_results`

7.2.0counter / bytesSize of results coming back from full text queries for search results, including the entire size of the JSON sent

`fts_total_compaction_written_bytes`

7.2.0counter / bytesNumber of bytes written to disk as a result of compaction

`fts_total_gc`

7.2.0counterThe number of garbage collection events triggered

`fts_total_grpc_internal_queries`

7.2.0counterThe number of internal gRPC requests from the co-ordinating node for the query to other nodes, for an index

`fts_total_grpc_queries`

7.2.0counterThe total number of queries, using gRPC for streaming, for an index

`fts_total_grpc_queries_error`

7.2.0counterThe number of queries that resulted in an error, using gRPC for streaming, for an index

`fts_total_grpc_queries_slow`

7.2.0counterThe number of queries in the slow query log, using gRPC for streaming, for an index

`fts_total_grpc_queries_timeout`

7.2.0counterThe number of queries that exceeded the timeout, using gRPC for streaming, for an index

`fts_total_internal_queries`

7.2.0counterThe number of internal queries from the co-ordinating node to other nodes, per unit time for an index

`fts_total_knn_searches`

7.6.0counterTotal bleve knn search operations

`fts_total_mutations_filtered`

8.0.0counterTotal number of mutations that qualify for any document filter in an index (in-memory only stat)

`fts_total_queries`

7.2.0counterThe number of full text queries per second for an index

`fts_total_queries_bad_request_error`

7.6.0counterThe number of FTS queries that resulted in an error due to a bad request

`fts_total_queries_consistency_error`

7.6.0counterThe number of FTS queries that resulted in an error due to a failure to meet consistency requirements

`fts_total_queries_error`

7.2.0counterThe number of FTS queries for an index that resulted in an error

`fts_total_queries_max_result_window_exceeded_error`

7.6.0counterThe number of FTS queries that resulted in an error due to exceeding the maximum result window

`fts_total_queries_partial_results_error`

7.6.0counterThe number of FTS queries that resulted in an error due to only partial results being returned

`fts_total_queries_rejected_by_herder`

7.2.0counterThe number of queries rejected by the app herder when the memory used exceeds the application's query quota

`fts_total_queries_search_in_context_error`

7.6.0counterThe number of FTS queries that resulted in an error while searching in context

`fts_total_queries_slow`

7.2.0counterThe number of FTS queries in the slow query log

`fts_total_queries_timeout`

7.2.0counterThe number of FTS queries for an index that exceeded the timeout

`fts_total_queries_to_actives`

8.0.0counterTotal number of searches served by the active partitions of an index on a node

`fts_total_queries_to_replicas`

8.0.0counterTotal number of searches served by the replica partitions of an index on a node

`fts_total_request_time`

7.2.0counter / nanosecondsTotal time spent processing query requests for an index

`fts_total_synonym_searches`

8.0.0counterTotal bleve synonym search operations

`fts_total_term_searchers`

7.2.0counterNumber of bleve term searchers

`fts_total_term_searchers_finished`

7.2.0counterTotal term searchers that have finished serving a query

`fts_total_vectors`

7.6.1gaugeThe total number of vectors indexed

`total_knn_queries_rejected_by_throttler`

7.6.4counterTotal number of http query requests with KNN rejected by the throttler