---
title: Cluster Manager Metrics
description: A list of the metrics provided by the Cluster Manager.
pubDate: 2026-08-18T04:50:45.818Z
antora:
  editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/metrics-reference/pages/ns-server-metrics.adoc
  xref: xref:cloud:metrics-reference:ns-server-metrics.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/metrics-reference/ns-server-metrics.html)

# Cluster Manager Metrics

> A list of the metrics provided by the Cluster Manager. 

> [!TIP]
> * The x.y.z badge shows the Couchbase Server version the metric was added in.
> * The type / unit badge shows shows the Prometheus [type](https://prometheus.io/docs/tutorials/understanding%5Fmetric%5Ftypes/) and [unit](https://prometheus.io/docs/practices/naming/#base-units) (if present).

`audit_queue_length`

7.0.0 gauge Current number of entries in the audit queue

`audit_unsuccessful_retries`

7.0.0 counter Failed attempts to audit

`cm_auth_cache_current_items`

7.6.0 gauge Current number of items available in cbauth auth cache

`cm_auth_cache_hit_total`

7.6.0 counter Total number of cbauth auth cache hits

`cm_auth_cache_max_items`

7.6.0 gauge Maximum capacity of cbauth auth cache

`cm_auth_cache_miss_total`

7.6.0 counter Total number of cbauth auth cache misses

`cm_auto_failover_count`

7.2.6 gauge Number of auto-failovers

`cm_auto_failover_enabled`

7.2.6 gauge Indicates if auto-failover is enabled (1 = true, 0 = false)

`cm_auto_failover_max_count`

7.2.6 gauge Maximum number of auto-failovers before being disabled

`cm_build_streaming_info_total`

7.0.0 counter Number of streaming requests processed

`cm_client_cert_cache_current_items`

7.6.0 gauge Current number of items available in cbauth client\_cert cache

`cm_client_cert_cache_hit_total`

7.6.0 counter Total number of cbauth client\_cert cache hits

`cm_client_cert_cache_max_items`

7.6.0 gauge Maximum capacity of cbauth client\_cert cache

`cm_client_cert_cache_miss_total`

7.6.0 counter Total number of cbauth client\_cert cache misses

`cm_erlang_port_count`

7.6.0 gauge The number of ports in use by the erlang VM

`cm_erlang_port_limit`

7.6.0 gauge The maximum number of ports that the erlang VM can use

`cm_erlang_process_count`

7.6.0 gauge The number of processes in use by the erlang VM

`cm_erlang_process_limit`

7.6.0 gauge The maximum number of processes that the erlang VM can use

`cm_failover_total`

7.2.6 counter Number of non-graceful failover results

`cm_gc_duration_seconds`

7.6.0 histogram Time to perform erlang garbage collection

`cm_graceful_failover_total`

7.2.6 counter Number of graceful failover results

`cm_http_requests_seconds`

7.0.0 histogram Number of bucket HTTP requests

`cm_http_requests_total`

7.0.0 counter Total number of HTTP requests categorized

`cm_is_balanced`

7.2.6 gauge Indicates if cluster is balanced (1 = true, 0 = false). Only reported by the orchestrator node and only updated once every 30 seconds

`cm_logs_total`

7.1.0 counter Total number of logs logged

`cm_memcached_call_time_seconds`

7.0.0 histogram Amount of time to call memcached

`cm_memcached_cmd_total`

7.6.0 gauge Total number of memcached commands

`cm_memcached_e2e_call_time_seconds`

7.0.0 histogram End to end memcached call times

`cm_memcached_q_call_time_seconds`

7.0.0 histogram / seconds Memcached queue call times

`cm_mru_cache_add_time_seconds`

7.0.0 histogram / seconds Time to add to MRU cache

`cm_mru_cache_flush_time_seconds`

7.0.0 histogram / seconds Time to flush MRU cache

`cm_mru_cache_lock_time_seconds`

7.0.0 histogram / seconds Time to lock MRU cache

`cm_mru_cache_lookup_time_seconds`

7.0.0 histogram / seconds Time to perform a lookup in the MRU cache

`cm_mru_cache_lookup_total`

7.0.0 counter Total number of MRU cache lookups

`cm_mru_cache_take_lock_total`

7.0.0 counter Total number of times MRU cache lock was obtained

`cm_odp_report_failed`

7.0.0 counter Number of failures to send on-demand pricing report

`cm_outgoing_http_requests_seconds`

7.0.0 histogram / seconds Time taken for outgoing HTTP requests

`cm_outgoing_http_requests_total`

7.0.0 counter Total number of outgoing HTTP requests

`cm_rebalance_in_progress`

7.2.6 gauge Indicates if a rebalance is running (1 = true, 0 = false). Only reported by the orchestrator node.

`cm_rebalance_progress`

7.2.6 gauge / ratio Estimate of the rebalance progress (0 - 1) for each stage. Only reported by the orchestrator node.

`cm_rebalance_total`

7.2.6 counter Number of rebalance results

`cm_request_hibernates_total`

7.0.0 counter Number of times requests were hibernated

`cm_request_unhibernates_total`

7.0.0 counter Number of times requests were unhibernated

`cm_rest_request_access_forbidden_total`

7.6.0 counter Number of REST requests failing due inadequate permissions

`cm_rest_request_auth_failure_total`

7.6.0 counter Number of REST requests failing authentication

`cm_rest_request_enters_total`

7.0.0 counter Number of REST requests to enter ns\_server

`cm_rest_request_failure_total`

7.6.0 counter Number of REST requests failing (see specific code)

`cm_rest_request_leaves_total`

7.0.0 counter Number of REST requests to exit ns\_server

`cm_status_latency_seconds`

7.0.0 histogram / seconds Latency time for status

`cm_up_cache_current_items`

7.6.0 gauge Current number of items available in cbauth up cache

`cm_up_cache_hit_total`

7.6.0 counter Total number of cbauth up cache hits

`cm_up_cache_max_items`

7.6.0 gauge Maximum capacity of cbauth up cache

`cm_up_cache_miss_total`

7.6.0 counter Total number of cbauth up cache misses

`cm_user_bkts_cache_current_items`

7.6.0 gauge Current number of items available in cbauth bkts cache

`cm_user_bkts_cache_hit_total`

7.6.0 counter Total number of cbauth bkts cache hits

`cm_user_bkts_cache_max_items`

7.6.0 gauge Maximum capacity of cbauth bkts cache

`cm_user_bkts_cache_miss_total`

7.6.0 counter Total number of cbauth bkts cache misses

`cm_uuid_cache_current_items`

7.6.0 gauge Current number of items available in cbauth uuid cache

`cm_uuid_cache_hit_total`

7.6.0 counter Total number of cbauth uuid cache hits

`cm_uuid_cache_max_items`

7.6.0 gauge Maximum capacity of cbauth uuid cache

`cm_uuid_cache_miss_total`

7.6.0 counter Total number of cbauth uuid cache misses

`cm_web_cache_hits_total`

7.0.0 counter Total number of web cache hits

`cm_web_cache_inner_hits_total`

7.0.0 counter Total number of inner web cache hits

`cm_web_cache_updates_total`

7.0.0 counter Total number of web cache updates

`couch_docs_actual_disk_size`

7.0.0 gauge / bytes Amount of disk space used by the Data Service

`couch_views_actual_disk_size`

7.0.0 gauge / bytes Amount of disk space used by Views data

`sys_allocstall`

7.0.0 counter Number of alloc stalls

`sys_cpu_burst_rate`

7.2.0 Deprecated in 7.6.0gauge Rate at which CPUs overran their quota

`sys_cpu_cgroup_seconds_total`

7.2.4 counter / seconds Number of CPU seconds utilized in the cgroup, by mode

`sys_cpu_cgroup_usage_seconds_total`

7.6.0 counter / seconds Number of 'user' and 'system' CPU seconds utilized in the cgroup

`sys_cpu_cores_available`

7.0.0 gauge Number of available CPU cores in the control group

`sys_cpu_host_cores_available`

7.1.1 gauge Number of available CPU cores in the host

`sys_cpu_host_idle_rate`

7.2.4 Deprecated in 7.6.0gauge Idle CPU utilization rate in the host

`sys_cpu_host_other_rate`

7.2.4 Deprecated in 7.6.0gauge Other (not idle/user/sys/irq/stolen) CPU utilization rate in the host

`sys_cpu_host_seconds_total`

7.2.1 counter / seconds Number of CPU seconds utilized in the host, by mode

`sys_cpu_host_sys_rate`

7.1.1 Deprecated in 7.6.0gauge System CPU utilization rate in the host

`sys_cpu_host_user_rate`

7.1.1 Deprecated in 7.6.0gauge User space CPU utilization rate in the host

`sys_cpu_host_utilization_rate`

7.1.1 Deprecated in 7.6.0gauge CPU utilization rate in the host

`sys_cpu_irq_rate`

7.0.0 Deprecated in 7.6.0gauge IRQ rate

`sys_cpu_stolen_rate`

7.0.0 Deprecated in 7.6.0gauge CPU stolen rate

`sys_cpu_sys_rate`

7.0.0 Deprecated in 7.6.0gauge System CPU utilization rate in the control group

`sys_cpu_throttled_rate`

7.2.0 Deprecated in 7.6.0gauge Rate at which CPUs were throttled

`sys_cpu_user_rate`

7.0.0 Deprecated in 7.6.0gauge User space CPU utilization rate in the control group

`sys_cpu_utilization_rate`

7.0.0 Deprecated in 7.6.0gauge CPU utilization rate in the control group

`sys_disk_queue`

7.2.4 gauge Current disk queue length of the disk

`sys_disk_queue_depth`

7.2.4 gauge Maximum disk queue length of the disk

`sys_disk_read_bytes`

7.2.4 counter Number of bytes read by the disk

`sys_disk_read_time_seconds`

7.2.4 counter Amount of time that the disk spent reading

`sys_disk_reads`

7.2.4 counter Number of reads that the disk performed

`sys_disk_time_seconds`

7.2.4 counter Amount of time that the disk spent performing IO

`sys_disk_write_bytes`

7.2.4 counter Number of bytes written by the disk

`sys_disk_write_time_seconds`

7.2.4 counter Amount of time that the disk spent writing

`sys_disk_writes`

7.2.4 counter Number of writes that the disk performed

`sys_mem_actual_free`

7.0.0 gauge / bytes Amount of system memory available, including buffers/cache

`sys_mem_actual_used`

7.0.0 gauge / bytes Amount of system memory used, excluding buffers/cache

`sys_mem_cgroup_actual_used`

7.2.0 gauge / bytes Amount of system memory used, excluding buffers/cache, in the control group

`sys_mem_cgroup_limit`

7.2.0 gauge / bytes System memory limit, in the control group

`sys_mem_cgroup_used`

7.2.0 gauge / bytes Amount of system memory used, including buffers/cache, in the control group

`sys_mem_free`

7.0.0 Deprecated in 8.0.0gauge / bytes Amount of system memory free, excluding buffers/cache

`sys_mem_free_sys`

8.0.0 gauge / bytes Amount of free system memory (not being used for anything including buffers/cache)

`sys_mem_limit`

7.0.0 Deprecated in 7.6.0gauge / bytes System memory limit

`sys_mem_total`

7.0.0 gauge / bytes Total amount of system memory

`sys_mem_used_sys`

7.0.0 gauge / bytes Amount of system memory used, including buffers/cache

`sys_pressure_share_time_stalled`

7.2.4 gauge Percentage of time that tasks were stalled on a given resource

`sys_pressure_total_stall_time_usec`

7.2.4 counter / microseconds Absolute stall time when tasks were stalled on a given resource

`sys_swap_total`

7.0.0 gauge / bytes Total amount of swap space

`sys_swap_used`

7.0.0 gauge / bytes Amount of swap space used

`sysproc_cpu_seconds_total`

7.2.4 counter Amount of user CPU cycles used, by process

`sysproc_cpu_utilization`

7.0.0 Deprecated in 7.6.0gauge CPU utilization rate, by process

`sysproc_major_faults_raw`

7.0.0 counter Number of major page faults, by process

`sysproc_mem_resident`

7.0.0 gauge / bytes Amount of resident memory used, by process

`sysproc_mem_share`

7.0.0 gauge / bytes Amount of shared memory used, by process

`sysproc_mem_size`

7.0.0 gauge / bytes Amount of memory used, by process

`sysproc_minor_faults_raw`

7.0.0 gauge Number of minor page faults, by process

`sysproc_page_faults_raw`

7.0.0 gauge Number of page faults, by process

`sysproc_start_time`

7.2.4 counter OS specific time when process was started