---
title: Query Service Metrics
description: A list of the metrics provided by the Query Service.
pubDate: 2026-08-18T04:50:45.818Z
antora:
  editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/metrics-reference/pages/query-service-metrics.adoc
  xref: xref:cloud:metrics-reference:query-service-metrics.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/metrics-reference/query-service-metrics.html)

# Query Service Metrics

> A list of the metrics provided by the Query Service. 

> [!TIP]
> * The x.y.z badge shows the Couchbase Server version the metric was added in.
> * The type / unit badge shows shows the Prometheus [type](https://prometheus.io/docs/tutorials/understanding%5Fmetric%5Ftypes/) and [unit](https://prometheus.io/docs/practices/naming/#base-units) (if present).

`n1ql_active_requests`

7.0.0 gauge Total number of active requests.

`n1ql_allocated_values`

7.6.0 counter The total number of values allocated in the query engine.

`n1ql_approx_vector_distance_func`

8.0.0 counter The number of APPROX\_VECTOR\_DISTANCE() calls made by statements.

`n1ql_at_plus`

7.0.0 counter Total number of N1QL requests with at\_plus index consistency.

`n1ql_audit_actions`

7.0.0 counter The total number of audit records sent to the server. Some requests cause more than one audit record to be emitted. Records in the output queue that have not yet been sent to the server are not counted.

`n1ql_audit_actions_failed`

7.0.0 counter The total number of audit records sent to the server that failed.

`n1ql_audit_requests_filtered`

7.0.0 counter The number of potentially auditable requests that cause no audit action to be taken.

`n1ql_audit_requests_total`

7.0.0 counter The total number of potentially auditable requests sent to the query engine.

`n1ql_boot_timestamp_seconds`

7.6.0 gauge / seconds The time the service booted in fractional seconds since Unix epoch.

`n1ql_bucket_reads`

7.6.0 gauge The total number of reads on the bucket.

`n1ql_bucket_retries`

7.6.0 gauge The total number of retries on the bucket.

`n1ql_bucket_writes`

7.6.0 gauge The total number of writes on the bucket.

`n1ql_bulk_get_errors`

7.2.4 counter Count of errors due to bulk get operations

`n1ql_cancelled`

7.0.0 counter Total number of cancelled requests.

`n1ql_cas_mismatch_errors`

7.2.4 counter Count of CAS mismatch errors

`n1ql_counter_cu_total`

7.6.0 counter / seconds The number of distinct operations recording Compute Units (CUs) with Regulator.

`n1ql_credit_cu_total`

7.6.0 counter / seconds The number of Compute Units (CUs) refunded.

`n1ql_credit_ru_total`

7.6.0 counter / seconds The number of Read Units (RUs) refunded.

`n1ql_credit_wu_total`

7.6.0 counter / seconds The number of Write Units (WUs) refunded.

`n1ql_curl_call_errors`

7.6.2 counter The number of CURL() calls made by statements that failed (returned an error).

`n1ql_curl_calls`

7.6.2 counter The number of CURL() calls made by statements.

`n1ql_cvi_request_timer_15m_rate`

8.0.0 gauge The 15m.rate latency of SQL++ Composite VECTOR requests.

`n1ql_cvi_request_timer_1m_rate`

8.0.0 gauge The 1m.rate latency of SQL++ Composite VECTOR requests.

`n1ql_cvi_request_timer_5m_rate`

8.0.0 gauge The 5m.rate latency of SQL++ Composite VECTOR requests.

`n1ql_cvi_request_timer_count`

8.0.0 gauge The number of SQL++ Composite VECTOR requests.

`n1ql_cvi_request_timer_max`

8.0.0 gauge The MAX latency of SQL++ Composite VECTOR requests.

`n1ql_cvi_request_timer_mean`

8.0.0 gauge The MEAN latency of SQL++ Composite VECTOR requests.

`n1ql_cvi_request_timer_mean_rate`

8.0.0 gauge The mean.rate latency of SQL++ Composite VECTOR requests.

`n1ql_cvi_request_timer_median`

8.0.0 gauge The MEDIAN latency of SQL++ Composite VECTOR requests.

`n1ql_cvi_request_timer_min`

8.0.0 gauge The MIN latency of SQL++ Composite VECTOR requests.

`n1ql_cvi_request_timer_p75`

8.0.0 gauge The 75% latency of SQL++ Composite VECTOR requests.

`n1ql_cvi_request_timer_p95`

8.0.0 gauge The 95% latency of SQL++ Composite VECTOR requests.

`n1ql_cvi_request_timer_p99`

8.0.0 gauge The 99% latency of SQL++ Composite VECTOR requests.

`n1ql_cvi_request_timer_p99point9`

8.0.0 gauge The 99.9% latency of SQL++ Composite VECTOR requests.

`n1ql_cvi_request_timer_stddev`

8.0.0 gauge The STDDEV latency of SQL++ Composite VECTOR requests.

`n1ql_deletes`

7.0.0 counter Total number of DELETE operations.

`n1ql_engine_error_count`

8.0.0 counter Total number of system-caused errors.

`n1ql_errors`

7.0.0 counter The total number of N1QL errors returned so far.

`n1ql_ffdc_manual`

7.6.6 counter The total number of ffdc captures triggered due to manual invocation of ffdc admin api

`n1ql_ffdc_memory_limit`

7.6.6 counter The total number of ffdc captures triggered due to free memory dropping below 10%

`n1ql_ffdc_memory_rate`

7.6.6 counter The total number of ffdc captures triggered due to memory usage rate increasing by 20% of the average memory usage over the past 2 hours

`n1ql_ffdc_memory_threshold`

7.6.6 counter The total number of ffdc captures triggered due to memory usage exceeding the 80% threshold

`n1ql_ffdc_plus_queue_full`

7.6.6 counter The total number of ffdc captures triggered due to the plus-request queue being full

`n1ql_ffdc_request_queue_full`

7.6.6 counter The total number of ffdc captures triggered due to the unbounded-request queue being full

`n1ql_ffdc_shutdown`

7.6.6 counter The total number of ffdc captures triggered due to shutdown processing exceeding 30 minutes

`n1ql_ffdc_sigterm`

7.6.6 counter The total number of ffdc captures triggered by a SIGTERM signal

`n1ql_ffdc_stalled_queue`

7.6.6 counter The total number of ffdc captures triggered due to no requests being processed when the queued requests exceed three times the number of servicers within the last 30 seconds

`n1ql_ffdc_total`

7.6.6 counter The total number of ffdc occurrences

`n1ql_fts_searches`

8.0.0 counter Total number of SQL++ FTS Searches.

`n1ql_fts_searches_svi`

8.0.0 counter Total number of SQL++ FTS Vetcor Searches.

`n1ql_hvi_request_timer_15m_rate`

8.0.0 gauge The 15m.rate latency of SQL++ Hyperscale VECTOR requests.

`n1ql_hvi_request_timer_1m_rate`

8.0.0 gauge The 1m.rate latency of SQL++ Hyperscale VECTOR requests.

`n1ql_hvi_request_timer_5m_rate`

8.0.0 gauge The 5m.rate latency of SQL++ Hyperscale VECTOR requests.

`n1ql_hvi_request_timer_count`

8.0.0 gauge The number of SQL++ Hyperscale VECTOR requests.

`n1ql_hvi_request_timer_max`

8.0.0 gauge The MAX latency of SQL++ Hyperscale VECTOR requests.

`n1ql_hvi_request_timer_mean`

8.0.0 gauge The MEAN latency of SQL++ Hyperscale VECTOR requests.

`n1ql_hvi_request_timer_mean_rate`

8.0.0 gauge The mean.rate latency of SQL++ Hyperscale VECTOR requests.

`n1ql_hvi_request_timer_median`

8.0.0 gauge The MEDIAN latency of SQL++ Hyperscale VECTOR requests.

`n1ql_hvi_request_timer_min`

8.0.0 gauge The MIN latency of SQL++ Hyperscale VECTOR requests.

`n1ql_hvi_request_timer_p75`

8.0.0 gauge The 75% latency of SQL++ Hyperscale VECTOR requests.

`n1ql_hvi_request_timer_p95`

8.0.0 gauge The 95% latency of SQL++ Hyperscale VECTOR requests.

`n1ql_hvi_request_timer_p99`

8.0.0 gauge The 99% latency of SQL++ Hyperscale VECTOR requests.

`n1ql_hvi_request_timer_p99point9`

8.0.0 gauge The 99.9% latency of SQL++ Hyperscale VECTOR requests.

`n1ql_hvi_request_timer_stddev`

8.0.0 gauge The STDDEV latency of SQL++ Hyperscale VECTOR requests.

`n1ql_index_scans`

7.0.0 counter Total number of secondary index scans.

`n1ql_index_scans_cvi`

8.0.0 counter Total number of Composite VECTOR index scans.

`n1ql_index_scans_fts`

7.2.4 counter Total number of index scans performed by FTS.

`n1ql_index_scans_gsi`

7.2.4 counter Total number of index scans performed by GSI.

`n1ql_index_scans_hvi`

8.0.0 counter Total number of Hyperscale VECTOR index scans.

`n1ql_index_scans_seq`

7.6.0 counter Total number of sequential scans.

`n1ql_inserts`

7.0.0 counter Total number of INSERT operations.

`n1ql_invalid_requests`

7.0.0 counter Total number of requests for unsupported endpoints.

`n1ql_load`

7.0.0 gauge The current utilization factor of the servicers on the query node.

`n1ql_load_factor`

7.6.0 gauge The total load factor of the query node.

`n1ql_mem_quota_exceeded_errors`

7.2.4 counter Count of memory quota exceeded errrors

`n1ql_meter_cu_total`

7.6.0 counter / seconds The number of Compute Units (CUs) recorded.

`n1ql_mutations`

7.0.0 counter Total number of document mutations.

`n1ql_node_memory`

7.6.0 gauge / bytes The total size of document memory in use, allocated from the node-wide document memory quota. This quota is defined only when node-quota and node-quota-val-percent settings are set.

`n1ql_node_rss`

7.6.1 gauge / bytes The resident set size (RSS) of the query node process.

`n1ql_op_count_total`

7.6.0 counter / seconds The number of distinct operations recorded with Regulator.

`n1ql_prepared`

7.0.0 counter Total number of prepared statements executed.

`n1ql_primary_scans`

7.0.0 counter Total number of primary index scans.

`n1ql_primary_scans_fts`

7.2.4 counter Total number of primary scans performed by FTS.

`n1ql_primary_scans_gsi`

7.2.4 counter Total number of primary scans performed by GSI.

`n1ql_primary_scans_seq`

7.6.0 counter Total number of primary sequential scans.

`n1ql_queued_requests`

7.0.0 gauge Total number of queued requests.

`n1ql_reject_count_total`

7.6.0 counter / seconds The number of times Regulator instructed an operation to be rejected.

`n1ql_request_time`

7.0.0 counter / nanoseconds Total end-to-end time to process all queries.

`n1ql_request_timer_15m_rate`

8.0.0 gauge The 15m.rate latency of SQL++ requests.

`n1ql_request_timer_1m_rate`

8.0.0 gauge The 1m.rate latency of SQL++ requests.

`n1ql_request_timer_5m_rate`

8.0.0 gauge The 5m.rate latency of SQL++ requests.

`n1ql_request_timer_count`

8.0.0 gauge The number of SQL++ requests.

`n1ql_request_timer_max`

8.0.0 gauge The MAX latency of SQL++ requests.

`n1ql_request_timer_mean`

8.0.0 gauge The MEAN latency of SQL++ requests.

`n1ql_request_timer_mean_rate`

8.0.0 gauge The mean.rate latency of SQL++ requests.

`n1ql_request_timer_median`

8.0.0 gauge The MEDIAN latency of SQL++ requests.

`n1ql_request_timer_min`

8.0.0 gauge The MIN latency of SQL++ requests.

`n1ql_request_timer_p75`

8.0.0 gauge The 75% latency of SQL++ requests.

`n1ql_request_timer_p95`

8.0.0 gauge The 95% latency of SQL++ requests.

`n1ql_request_timer_p99`

8.0.0 gauge The 99% latency of SQL++ requests.

`n1ql_request_timer_p99point9`

8.0.0 gauge The 99.9% latency of SQL++ requests.

`n1ql_request_timer_stddev`

8.0.0 gauge The STDDEV latency of SQL++ requests.

`n1ql_requests`

7.0.0 counter Total number of N1QL requests.

`n1ql_requests_1000ms`

7.0.0 counter Number of queries that take longer than 1000ms.

`n1ql_requests_250ms`

7.0.0 counter Number of queries that take longer than 250ms.

`n1ql_requests_5000ms`

7.0.0 counter Number of queries that take longer than 5000ms.

`n1ql_requests_500ms`

7.0.0 counter Number of queries that take longer than 500ms.

`n1ql_requests_cvi`

8.0.0 counter Total number of SQL++ GSI Composite VECTOR requests.

`n1ql_requests_gsi`

8.0.0 counter Total number of SQL++ GSI requests.

`n1ql_requests_hvi`

8.0.0 counter Total number of SQL++ GSI Hyperscale VECTOR requests.

`n1ql_requests_natural_ftssql`

8.0.0 counter Total number of SQL++ Natural Language FTSSQL requests.

`n1ql_requests_natural_jsudf`

8.0.0 counter Total number of SQL++ Natural Language JSUDF requests.

`n1ql_requests_natural_sql`

8.0.0 counter Total number of SQL++ Natural Language SQL requests.

`n1ql_requests_natural_total`

8.0.0 counter Total number of SQL++ Natural Language requests.

`n1ql_requests_search`

8.0.0 counter Total number of SQL++ FTS requests.

`n1ql_requests_svi`

8.0.0 counter Total number of SQL++ FTS VECTOR requests.

`n1ql_requests_vector`

8.0.0 counter Total number of SQL++ VECTOR requests.

`n1ql_result_count`

7.0.0 counter Total number of results (documents) returned by the query engine.

`n1ql_result_size`

7.0.0 counter / bytes Total size of data returned by the query engine.

`n1ql_scan_plus`

7.0.0 counter Total number of N1QL requests with request\_plus index consistency.

`n1ql_selects`

7.0.0 counter Total number of SELECT requests.

`n1ql_service_time`

7.0.0 counter / nanoseconds Time to execute all queries.

`n1ql_spills_order`

8.0.0 counter Number of order by operations that have spilled to disk.

`n1ql_svi_request_timer_15m_rate`

8.0.0 gauge The 15m.rate latency of SQL++ FTS VECTOR requests.

`n1ql_svi_request_timer_1m_rate`

8.0.0 gauge The 1m.rate latency of SQL++ FTS VECTOR requests.

`n1ql_svi_request_timer_5m_rate`

8.0.0 gauge The 5m.rate latency of SQL++ FTS VECTOR requests.

`n1ql_svi_request_timer_count`

8.0.0 gauge The number of SQL++ FTS VECTOR requests.

`n1ql_svi_request_timer_max`

8.0.0 gauge The MAX latency of SQL++ FTS VECTOR requests.

`n1ql_svi_request_timer_mean`

8.0.0 gauge The MEAN latency of SQL++ FTS VECTOR requests.

`n1ql_svi_request_timer_mean_rate`

8.0.0 gauge The mean.rate latency of SQL++ FTS VECTOR requests.

`n1ql_svi_request_timer_median`

8.0.0 gauge The MEDIAN latency of SQL++ FTS VECTOR requests.

`n1ql_svi_request_timer_min`

8.0.0 gauge The MIN latency of SQL++ FTS VECTOR requests.

`n1ql_svi_request_timer_p75`

8.0.0 gauge The 75% latency of SQL++ FTS VECTOR requests.

`n1ql_svi_request_timer_p95`

8.0.0 gauge The 95% latency of SQL++ FTS VECTOR requests.

`n1ql_svi_request_timer_p99`

8.0.0 gauge The 99% latency of SQL++ FTS VECTOR requests.

`n1ql_svi_request_timer_p99point9`

8.0.0 gauge The 99.9% latency of SQL++ FTS VECTOR requests.

`n1ql_svi_request_timer_stddev`

8.0.0 gauge The STDDEV latency of SQL++ FTS VECTOR requests.

`n1ql_temp_hwm`

8.0.0 counter High water mark for temp space use.

`n1ql_temp_space_errors`

7.6.0 counter Count of temp space related errors

`n1ql_temp_usage`

8.0.0 gauge Current temp space use.

`n1ql_tenant_kv_throttle_count`

7.6.0 gauge The total number of times KV has been throttled for queries on this tenant.

`n1ql_tenant_kv_throttle_seconds_total`

7.6.0 gauge / seconds The total amount of time KV has been throttled for queries on this tenant.

`n1ql_tenant_memory`

7.6.0 gauge / bytes The total size of document memory in use, allocated from the tenant-wide document memory quota.

`n1ql_tenant_reads`

7.6.0 gauge The total number of reads on the tenant.

`n1ql_tenant_retries`

7.6.0 gauge The total number of retries on the tenant.

`n1ql_tenant_writes`

7.6.0 gauge The total number of writes on the tenant.

`n1ql_throttle_count_total`

7.6.0 counter / seconds The number of times Regulator instructed an operation to throttle.

`n1ql_throttle_seconds_total`

7.6.0 counter / seconds The total time spent throttling (in seconds).

`n1ql_timeouts`

7.2.4 counter Count of request timeout errors

`n1ql_transaction_time`

7.0.0 counter / nanoseconds Total elapsed time of transactions so far.

`n1ql_transactions`

7.0.0 counter Total number of transactions.

`n1ql_unauthorized_users`

7.2.4 counter Count of unauthorized access errors

`n1ql_unbounded`

7.0.0 counter Total number of N1QL requests with not\_bounded index consistency.

`n1ql_updates`

7.0.0 counter Total number of UPDATE requests.

`n1ql_user_error_count`

8.0.0 counter Total number of user-caused errors.

`n1ql_vector_distance_func`

8.0.0 counter The number of VECTOR\_DISTANCE() calls made by statements.

`n1ql_warnings`

7.0.0 counter The total number of N1QL warnings returned so far.