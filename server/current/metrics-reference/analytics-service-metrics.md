---
title: Analytics Service Metrics
description: A list of the metrics provided by the Analytics Service.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/metrics-reference/pages/analytics-service-metrics.adoc
  xref: xref:server:metrics-reference:analytics-service-metrics.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/metrics-reference/analytics-service-metrics.html)

# Analytics Service Metrics

> A list of the metrics provided by the Analytics Service. 

The following Analytics Service metrics can be queried by means of the REST APIs described in [Statistics](../rest-api/rest-statistics.md).

See [Analytics Service Metrics Cross Reference](analytics-service-metrics-cross-reference.md) if you are looking for a metric name you know from an alternative supported or legacy tool.

> [!TIP]
> * The x.y.z badge shows the Couchbase Server version the metric was added in.
> * The type / unit badge shows shows the Prometheus [type](https://prometheus.io/docs/tutorials/understanding%5Fmetric%5Ftypes/) and [unit](https://prometheus.io/docs/practices/naming/#base-units) (if present).

`cbas_active_links`

7.2.4gauge / numberNumber of active links.

`cbas_backup_requests_failed_total`

7.6.2counter / countTotal number of failed backup requests.

`cbas_backup_requests_total`

7.6.2counter / countTotal number of backup requests.

`cbas_direct_memory_used_bytes`

7.0.2gauge / bytesDirect memory used in bytes.

`cbas_disk_used_bytes`

7.6.0gauge / bytesDisk used in bytes.

`cbas_disk_used_bytes_total`

7.0.0Deprecated in 7.6.0gauge / bytesDisk used in bytes.

`cbas_driver_boot_timestamp_seconds`

7.6.0gauge / secondsAnalytics driver process boot timestamp in seconds since Unix epoch.

`cbas_driver_uptime_seconds_total`

7.6.1counter / secondsTotal driver uptime in seconds.

`cbas_extra_incoming_records_total`

7.6.6counter / countTotal number of incoming records that were processed multiple times due to DCP snapshot alignment.

`cbas_failed_to_parse_records_count`

7.0.0Deprecated in 7.6.0gauge / numberTotal number of records which failed to parse.

`cbas_failed_to_parse_records_total`

7.6.0counter / countTotal number of records which failed to parse.

`cbas_gc_count_total`

7.0.0counter / countTotal number of garbage collections.

`cbas_gc_time_milliseconds_total`

7.0.0Deprecated in 7.6.0counter / millisecondsTotal time of garbage collections in milliseconds.

`cbas_gc_time_seconds_total`

7.6.0counter / secondsTotal time of garbage collections in fractional seconds.

`cbas_heap_memory_committed_bytes`

7.1.0gauge / bytesHeap memory committed in bytes.

`cbas_heap_memory_max_bytes`

7.2.7gauge / bytesHeap memory max in bytes.

`cbas_heap_memory_used_bytes`

7.0.0gauge / bytesHeap memory used in bytes.

`cbas_http_requests_failed_total`

7.6.0counter / countTotal number of failed http requests, grouped by status code.

`cbas_http_requests_timeout_total`

7.6.2counter / countTotal number of HTTP requests timeouts.

`cbas_http_requests_total`

7.6.0counter / countTotal number of http requests.

`cbas_incoming_records_count`

7.0.0Deprecated in 7.6.0gauge / countTotal number of incoming records.

`cbas_incoming_records_total`

7.6.0counter / countTotal number of incoming records.

`cbas_io_reads_total`

7.0.0counter / countTotal number of IO reads.

`cbas_io_writes_total`

7.0.0counter / countTotal number of IO writes.

`cbas_jobs_total`

7.6.2counter / countTotal number of successful, failed, cancelled and rejected jobs.

`cbas_link_connect_failed_total`

7.6.2counter / countTotal number of link connect failures.

`cbas_link_disconnect_failed_total`

7.6.2counter / countTotal number of link disconnect failures.

`cbas_link_invalid_credentials_total`

7.6.2counter / countTotal number of link invalid credentials.

`cbas_pending_flush_ops`

7.0.0gauge / numberTotal number of pending flush operations.

`cbas_pending_merge_ops`

7.0.0gauge / numberTotal number of pending merge operations.

`cbas_pending_replicate_ops`

7.1.0gauge / numberTotal number of pending replication operations.

`cbas_pending_requests`

7.2.4gauge / numberNumber of pending requests.

`cbas_queued_http_requests_size`

7.6.0gauge / numberNumber of queued http requests.

`cbas_queued_jobs`

7.2.4gauge / numberNumber of queued jobs.

`cbas_rebalance_cancelled_total`

7.6.0counter / countTotal number of cancelled rebalances.

`cbas_rebalance_failed_total`

7.6.0counter / countTotal number of rebalance failures.

`cbas_rebalance_successful_total`

7.6.0counter / countTotal number of successful rebalances.

`cbas_requests_failed_total`

7.6.2counter / countTotal number of failed requests.

`cbas_requests_total`

7.2.4counter / countTotal number of received requests.

`cbas_running_jobs`

7.2.4gauge / numberNumber of running jobs.

`cbas_scan_consistency_timeout_total`

7.6.2counter / countTotal number of scan consistency timeouts.

`cbas_system_load_average`

7.0.0gauge / numberSystem work load.

`cbas_thread_count`

7.0.0gauge / numberNumber of threads in use.

`cbas_virtual_buffer_cache_used_pages`

7.0.0gauge / numberTotal number of used memory pages in the virtual buffer cache.

`cbas_wrapper_boot_timestamp_seconds`

7.6.0gauge / secondsAnalytics wrapper process boot timestamp in seconds since Unix epoch.

`cbas_wrapper_uptime_seconds_total`

7.6.1counter / secondsTotal wrapper uptime in seconds.