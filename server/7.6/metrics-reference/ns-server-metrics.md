---
title: Cluster Manager Metrics
description: A list of the metrics provided by the Cluster Manager.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/metrics-reference/pages/ns-server-metrics.adoc
pubDate: 2026-03-18T03:49:18.767Z
link: xref:7.6@server:metrics-reference:ns-server-metrics.adoc[]
---

[View original HTML](/server/7.6/metrics-reference/ns-server-metrics.html)

# Cluster Manager Metrics

> A list of the metrics provided by the Cluster Manager. 

The following Cluster Manager metrics can be queried by means of the REST APIs described in [Statistics](../rest-api/rest-statistics.md).

Histograms

Note that each histogram metric will generate three time series, with the following suffixes:

* `_count`
* `_sum`
* `_bucket`

Please refer to [Prometheus Histograms and Summaries](https://prometheus.io/docs/practices/histograms/) for more information.

> [!TIP]
> * The x.y.z badge shows the Couchbase Server version the metric was added in.
> * The type / unit badge shows shows the Prometheus [type](https://prometheus.io/docs/tutorials/understanding%5Fmetric%5Ftypes/) and [unit](https://prometheus.io/docs/practices/naming/#base-units) (if present).

| audit\_queue\_length7.0.0gauge Current number of entries in the audit queue                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| audit\_unsuccessful\_retries7.0.0counter Failed attempts to audit                                                                                                |
| cm\_auth\_cache\_current\_items7.6.0gauge Current number of items available in cbauth auth cache                                                                 |
| cm\_auth\_cache\_hit\_total7.6.0counter Total number of cbauth auth cache hits                                                                                   |
| cm\_auth\_cache\_max\_items7.6.0gauge Maximum capacity of cbauth auth cache                                                                                      |
| cm\_auth\_cache\_miss\_total7.6.0counter Total number of cbauth auth cache misses                                                                                |
| cm\_auto\_failover\_count7.2.6gauge Number of auto-failovers                                                                                                     |
| cm\_auto\_failover\_enabled7.2.6gauge Indicates if auto-failover is enabled (1 = true, 0 = false)                                                                |
| cm\_auto\_failover\_max\_count7.2.6gauge Maximum number of auto-failovers before being disabled                                                                  |
| cm\_build\_streaming\_info\_total7.0.0counter Number of streaming requests processed                                                                             |
| cm\_client\_cert\_cache\_current\_items7.6.0gauge Current number of items available in cbauth client\_cert cache                                                 |
| cm\_client\_cert\_cache\_hit\_total7.6.0counter Total number of cbauth client\_cert cache hits                                                                   |
| cm\_client\_cert\_cache\_max\_items7.6.0gauge Maximum capacity of cbauth client\_cert cache                                                                      |
| cm\_client\_cert\_cache\_miss\_total7.6.0counter Total number of cbauth client\_cert cache misses                                                                |
| cm\_erlang\_port\_count7.6.0gauge The number of ports in use by the erlang VM                                                                                    |
| cm\_erlang\_port\_limit7.6.0gauge The maximum number of ports that the erlang VM can use                                                                         |
| cm\_erlang\_process\_count7.6.0gauge The number of processes in use by the erlang VM                                                                             |
| cm\_erlang\_process\_limit7.6.0gauge The maximum number of processes that the erlang VM can use                                                                  |
| cm\_failover\_total7.2.6counter Number of non-graceful failover results                                                                                          |
| cm\_gc\_duration\_seconds7.6.0histogram Time to perform erlang garbage collection                                                                                |
| cm\_graceful\_failover\_total7.2.6counter Number of graceful failover results                                                                                    |
| cm\_http\_requests\_seconds7.0.0histogram Number of bucket HTTP requests                                                                                         |
| cm\_http\_requests\_total7.0.0counter Total number of HTTP requests categorized                                                                                  |
| cm\_is\_balanced7.2.6gauge Indicates if cluster is balanced (1 = true, 0 = false). Only reported by the orchestrator node and only updated once every 30 seconds |
| cm\_logs\_total7.1.0counter Total number of logs logged                                                                                                          |
| cm\_memcached\_call\_time\_seconds7.0.0histogram Amount of time to call memcached                                                                                |
| cm\_memcached\_cmd\_total7.6.0gauge Total number of memcached commands                                                                                           |
| cm\_memcached\_e2e\_call\_time\_seconds7.0.0histogram End to end memcached call times                                                                            |
| cm\_memcached\_q\_call\_time\_seconds7.0.0histogram / seconds Memcached queue call times                                                                         |
| cm\_mru\_cache\_add\_time\_seconds7.0.0histogram / seconds Time to add to MRU cache                                                                              |
| cm\_mru\_cache\_flush\_time\_seconds7.0.0histogram / seconds Time to flush MRU cache                                                                             |
| cm\_mru\_cache\_lock\_time\_seconds7.0.0histogram / seconds Time to lock MRU cache                                                                               |
| cm\_mru\_cache\_lookup\_time\_seconds7.0.0histogram / seconds Time to perform a lookup in the MRU cache                                                          |
| cm\_mru\_cache\_lookup\_total7.0.0counter Total number of MRU cache lookups                                                                                      |
| cm\_mru\_cache\_take\_lock\_total7.0.0counter Total number of times MRU cache lock was obtained                                                                  |
| cm\_odp\_report\_failed7.0.0counter Number of failures to send on-demand pricing report                                                                          |
| cm\_outgoing\_http\_requests\_seconds7.0.0histogram / seconds Time taken for outgoing HTTP requests                                                              |
| cm\_outgoing\_http\_requests\_total7.0.0counter Total number of outgoing HTTP requests                                                                           |
| cm\_rebalance\_in\_progress7.2.6gauge Indicates if a rebalance is running (1 = true, 0 = false). Only reported by the orchestrator node.                         |
| cm\_rebalance\_progress7.2.6gauge / ratio Estimate of the rebalance progress (0 - 1) for each stage. Only reported by the orchestrator node.                     |
| cm\_rebalance\_total7.2.6counter Number of rebalance results                                                                                                     |
| cm\_request\_hibernates\_total7.0.0counter Number of times requests were hibernated                                                                              |
| cm\_request\_unhibernates\_total7.0.0counter Number of times requests were unhibernated                                                                          |
| cm\_rest\_request\_access\_forbidden\_total7.6.0counter Number of REST requests failing due inadequate permissions                                               |
| cm\_rest\_request\_auth\_failure\_total7.6.0counter Number of REST requests failing authentication                                                               |
| cm\_rest\_request\_enters\_total7.0.0counter Number of REST requests to enter ns\_server                                                                         |
| cm\_rest\_request\_failure\_total7.6.0counter Number of REST requests failing (see specific code)                                                                |
| cm\_rest\_request\_leaves\_total7.0.0counter Number of REST requests to exit ns\_server                                                                          |
| cm\_status\_latency\_seconds7.0.0histogram / seconds Latency time for status                                                                                     |
| cm\_up\_cache\_current\_items7.6.0gauge Current number of items available in cbauth up cache                                                                     |
| cm\_up\_cache\_hit\_total7.6.0counter Total number of cbauth up cache hits                                                                                       |
| cm\_up\_cache\_max\_items7.6.0gauge Maximum capacity of cbauth up cache                                                                                          |
| cm\_up\_cache\_miss\_total7.6.0counter Total number of cbauth up cache misses                                                                                    |
| cm\_user\_bkts\_cache\_current\_items7.6.0gauge Current number of items available in cbauth bkts cache                                                           |
| cm\_user\_bkts\_cache\_hit\_total7.6.0counter Total number of cbauth bkts cache hits                                                                             |
| cm\_user\_bkts\_cache\_max\_items7.6.0gauge Maximum capacity of cbauth bkts cache                                                                                |
| cm\_user\_bkts\_cache\_miss\_total7.6.0counter Total number of cbauth bkts cache misses                                                                          |
| cm\_uuid\_cache\_current\_items7.6.0gauge Current number of items available in cbauth uuid cache                                                                 |
| cm\_uuid\_cache\_hit\_total7.6.0counter Total number of cbauth uuid cache hits                                                                                   |
| cm\_uuid\_cache\_max\_items7.6.0gauge Maximum capacity of cbauth uuid cache                                                                                      |
| cm\_uuid\_cache\_miss\_total7.6.0counter Total number of cbauth uuid cache misses                                                                                |
| cm\_web\_cache\_hits\_total7.0.0counter Total number of web cache hits                                                                                           |
| cm\_web\_cache\_inner\_hits\_total7.0.0counter Total number of inner web cache hits                                                                              |
| cm\_web\_cache\_updates\_total7.0.0counter Total number of web cache updates                                                                                     |
| couch\_docs\_actual\_disk\_size7.0.0gauge / bytes Amount of disk space used by the Data Service                                                                  |
| couch\_views\_actual\_disk\_size7.0.0gauge / bytes Amount of disk space used by Views data                                                                       |
| sys\_allocstall7.0.0counter Number of alloc stalls                                                                                                               |
| sys\_cpu\_burst\_rate7.2.0Deprecated in 7.6.0gauge Rate at which CPUs overran their quota                                                                        |
| sys\_cpu\_cgroup\_seconds\_total7.2.4counter / seconds Number of CPU seconds utilized in the cgroup, by mode                                                     |
| sys\_cpu\_cgroup\_usage\_seconds\_total7.6.0counter / seconds Number of 'user' and 'system' CPU seconds utilized in the cgroup                                   |
| sys\_cpu\_cores\_available7.0.0gauge Number of available CPU cores in the control group                                                                          |
| sys\_cpu\_host\_cores\_available7.1.1gauge Number of available CPU cores in the host                                                                             |
| sys\_cpu\_host\_idle\_rate7.2.4Deprecated in 7.6.0gauge Idle CPU utilization rate in the host                                                                    |
| sys\_cpu\_host\_other\_rate7.2.4Deprecated in 7.6.0gauge Other (not idle/user/sys/irq/stolen) CPU utilization rate in the host                                   |
| sys\_cpu\_host\_seconds\_total7.2.1counter / seconds Number of CPU seconds utilized in the host, by mode                                                         |
| sys\_cpu\_host\_sys\_rate7.1.1Deprecated in 7.6.0gauge System CPU utilization rate in the host                                                                   |
| sys\_cpu\_host\_user\_rate7.1.1Deprecated in 7.6.0gauge User space CPU utilization rate in the host                                                              |
| sys\_cpu\_host\_utilization\_rate7.1.1Deprecated in 7.6.0gauge CPU utilization rate in the host                                                                  |
| sys\_cpu\_irq\_rate7.0.0Deprecated in 7.6.0gauge IRQ rate                                                                                                        |
| sys\_cpu\_stolen\_rate7.0.0Deprecated in 7.6.0gauge CPU stolen rate                                                                                              |
| sys\_cpu\_sys\_rate7.0.0Deprecated in 7.6.0gauge System CPU utilization rate in the control group                                                                |
| sys\_cpu\_throttled\_rate7.2.0Deprecated in 7.6.0gauge Rate at which CPUs were throttled                                                                         |
| sys\_cpu\_user\_rate7.0.0Deprecated in 7.6.0gauge User space CPU utilization rate in the control group                                                           |
| sys\_cpu\_utilization\_rate7.0.0Deprecated in 7.6.0gauge CPU utilization rate in the control group                                                               |
| sys\_disk\_queue7.2.4gauge Current disk queue length of the disk                                                                                                 |
| sys\_disk\_queue\_depth7.2.4gauge Maximum disk queue length of the disk                                                                                          |
| sys\_disk\_read\_bytes7.2.4counter Number of bytes read by the disk                                                                                              |
| sys\_disk\_read\_time\_seconds7.2.4counter Amount of time that the disk spent reading                                                                            |
| sys\_disk\_reads7.2.4counter Number of reads that the disk performed                                                                                             |
| sys\_disk\_time\_seconds7.2.4counter Amount of time that the disk spent performing IO                                                                            |
| sys\_disk\_write\_bytes7.2.4counter Number of bytes written by the disk                                                                                          |
| sys\_disk\_write\_time\_seconds7.2.4counter Amount of time that the disk spent writing                                                                           |
| sys\_disk\_writes7.2.4counter Number of writes that the disk performed                                                                                           |
| sys\_mem\_actual\_free7.0.0gauge / bytes Amount of system memory available, including buffers/cache                                                              |
| sys\_mem\_actual\_used7.0.0gauge / bytes Amount of system memory used, excluding buffers/cache                                                                   |
| sys\_mem\_cgroup\_actual\_used7.2.0gauge / bytes Amount of system memory used, excluding buffers/cache, in the control group                                     |
| sys\_mem\_cgroup\_limit7.2.0gauge / bytes System memory limit, in the control group                                                                              |
| sys\_mem\_cgroup\_used7.2.0gauge / bytes Amount of system memory used, including buffers/cache, in the control group                                             |
| sys\_mem\_free7.0.0gauge / bytes Amount of system memory free, excluding buffers/cache                                                                           |
| sys\_mem\_limit7.0.0Deprecated in 7.6.0gauge / bytes System memory limit                                                                                         |
| sys\_mem\_total7.0.0gauge / bytes Total amount of system memory                                                                                                  |
| sys\_mem\_used\_sys7.0.0gauge / bytes Amount of system memory used, including buffers/cache                                                                      |
| sys\_pressure\_share\_time\_stalled7.2.4gauge Percentage of time that tasks were stalled on a given resource                                                     |
| sys\_pressure\_total\_stall\_time\_usec7.2.4counter / microseconds Absolute stall time when tasks were stalled on a given resource                               |
| sys\_swap\_total7.0.0gauge / bytes Total amount of swap space                                                                                                    |
| sys\_swap\_used7.0.0gauge / bytes Amount of swap space used                                                                                                      |
| sysproc\_cpu\_seconds\_total7.2.4counter Amount of user CPU cycles used, by process                                                                              |
| sysproc\_cpu\_utilization7.0.0Deprecated in 7.6.0gauge CPU utilization rate, by process                                                                          |
| sysproc\_major\_faults\_raw7.0.0counter Number of major page faults, by process                                                                                  |
| sysproc\_mem\_resident7.0.0gauge / bytes Amount of resident memory used, by process                                                                              |
| sysproc\_mem\_share7.0.0gauge / bytes Amount of shared memory used, by process                                                                                   |
| sysproc\_mem\_size7.0.0gauge / bytes Amount of memory used, by process                                                                                           |
| sysproc\_minor\_faults\_raw7.0.0gauge Number of minor page faults, by process                                                                                    |
| sysproc\_page\_faults\_raw7.0.0gauge Number of page faults, by process                                                                                           |
| sysproc\_start\_time7.2.4counter OS specific time when process was started                                                                                       |