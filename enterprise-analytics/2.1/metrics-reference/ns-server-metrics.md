---
title: Cluster Manager Metrics
description: A list of the metrics provided by the Cluster Manager.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/metrics-reference/pages/ns-server-metrics.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:2.1@enterprise-analytics:metrics-reference:ns-server-metrics.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.1/metrics-reference/ns-server-metrics.html)

# Cluster Manager Metrics

> A list of the metrics provided by the Cluster Manager. 

> [!TIP]
> * The type / unit badge shows shows the Prometheus [type](https://prometheus.io/docs/tutorials/understanding%5Fmetric%5Ftypes/) and [unit](https://prometheus.io/docs/practices/naming/#base-units) (if present).

| audit\_queue\_lengthgauge Current number of entries in the audit queue                                                                                      |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| audit\_unsuccessful\_retriescounter Failed attempts to audit                                                                                                |
| cm\_auth\_cache\_current\_itemsgauge Current number of items available in cbauth auth cache                                                                 |
| cm\_auth\_cache\_hit\_totalcounter Total number of cbauth auth cache hits                                                                                   |
| cm\_auth\_cache\_max\_itemsgauge Maximum capacity of cbauth auth cache                                                                                      |
| cm\_auth\_cache\_miss\_totalcounter Total number of cbauth auth cache misses                                                                                |
| cm\_auto\_failover\_countgauge Number of auto-failovers                                                                                                     |
| cm\_auto\_failover\_enabledgauge Indicates if auto-failover is enabled (1 = true, 0 = false)                                                                |
| cm\_auto\_failover\_max\_countgauge Maximum number of auto-failovers before being disabled                                                                  |
| cm\_build\_streaming\_info\_totalcounter Number of streaming requests processed                                                                             |
| cm\_client\_cert\_cache\_current\_itemsgauge Current number of items available in cbauth client\_cert cache                                                 |
| cm\_client\_cert\_cache\_hit\_totalcounter Total number of cbauth client\_cert cache hits                                                                   |
| cm\_client\_cert\_cache\_max\_itemsgauge Maximum capacity of cbauth client\_cert cache                                                                      |
| cm\_client\_cert\_cache\_miss\_totalcounter Total number of cbauth client\_cert cache misses                                                                |
| cm\_erlang\_port\_countgauge The number of ports in use by the erlang VM                                                                                    |
| cm\_erlang\_port\_limitgauge The maximum number of ports that the erlang VM can use                                                                         |
| cm\_erlang\_process\_countgauge The number of processes in use by the erlang VM                                                                             |
| cm\_erlang\_process\_limitgauge The maximum number of processes that the erlang VM can use                                                                  |
| cm\_failover\_totalcounter Number of non-graceful failover results                                                                                          |
| cm\_gc\_duration\_secondshistogram Time to perform erlang garbage collection                                                                                |
| cm\_graceful\_failover\_totalcounter Number of graceful failover results                                                                                    |
| cm\_http\_requests\_secondshistogram Number of bucket HTTP requests                                                                                         |
| cm\_http\_requests\_totalcounter Total number of HTTP requests categorized                                                                                  |
| cm\_is\_balancedgauge Indicates if cluster is balanced (1 = true, 0 = false). Only reported by the orchestrator node and only updated once every 30 seconds |
| cm\_logs\_totalcounter Total number of logs logged                                                                                                          |
| cm\_memcached\_call\_time\_secondshistogram Amount of time to call memcached                                                                                |
| cm\_memcached\_cmd\_totalgauge Total number of memcached commands                                                                                           |
| cm\_memcached\_e2e\_call\_time\_secondshistogram End to end memcached call times                                                                            |
| cm\_memcached\_q\_call\_time\_secondshistogram / seconds Memcached queue call times                                                                         |
| cm\_mru\_cache\_add\_time\_secondshistogram / seconds Time to add to MRU cache                                                                              |
| cm\_mru\_cache\_flush\_time\_secondshistogram / seconds Time to flush MRU cache                                                                             |
| cm\_mru\_cache\_lock\_time\_secondshistogram / seconds Time to lock MRU cache                                                                               |
| cm\_mru\_cache\_lookup\_time\_secondshistogram / seconds Time to perform a lookup in the MRU cache                                                          |
| cm\_mru\_cache\_lookup\_totalcounter Total number of MRU cache lookups                                                                                      |
| cm\_mru\_cache\_take\_lock\_totalcounter Total number of times MRU cache lock was obtained                                                                  |
| cm\_odp\_report\_failedcounter Number of failures to send on-demand pricing report                                                                          |
| cm\_outgoing\_http\_requests\_secondshistogram / seconds Time taken for outgoing HTTP requests                                                              |
| cm\_outgoing\_http\_requests\_totalcounter Total number of outgoing HTTP requests                                                                           |
| cm\_rebalance\_in\_progressgauge Indicates if a rebalance is running (1 = true, 0 = false). Only reported by the orchestrator node.                         |
| cm\_rebalance\_progressgauge / ratio Estimate of the rebalance progress (0 - 1) for each stage. Only reported by the orchestrator node.                     |
| cm\_rebalance\_totalcounter Number of rebalance results                                                                                                     |
| cm\_request\_hibernates\_totalcounter Number of times requests were hibernated                                                                              |
| cm\_request\_unhibernates\_totalcounter Number of times requests were unhibernated                                                                          |
| cm\_rest\_request\_access\_forbidden\_totalcounter Number of REST requests failing due inadequate permissions                                               |
| cm\_rest\_request\_auth\_failure\_totalcounter Number of REST requests failing authentication                                                               |
| cm\_rest\_request\_enters\_totalcounter Number of REST requests to enter ns\_server                                                                         |
| cm\_rest\_request\_failure\_totalcounter Number of REST requests failing (see specific code)                                                                |
| cm\_rest\_request\_leaves\_totalcounter Number of REST requests to exit ns\_server                                                                          |
| cm\_status\_latency\_secondshistogram / seconds Latency time for status                                                                                     |
| cm\_up\_cache\_current\_itemsgauge Current number of items available in cbauth up cache                                                                     |
| cm\_up\_cache\_hit\_totalcounter Total number of cbauth up cache hits                                                                                       |
| cm\_up\_cache\_max\_itemsgauge Maximum capacity of cbauth up cache                                                                                          |
| cm\_up\_cache\_miss\_totalcounter Total number of cbauth up cache misses                                                                                    |
| cm\_user\_bkts\_cache\_current\_itemsgauge Current number of items available in cbauth bkts cache                                                           |
| cm\_user\_bkts\_cache\_hit\_totalcounter Total number of cbauth bkts cache hits                                                                             |
| cm\_user\_bkts\_cache\_max\_itemsgauge Maximum capacity of cbauth bkts cache                                                                                |
| cm\_user\_bkts\_cache\_miss\_totalcounter Total number of cbauth bkts cache misses                                                                          |
| cm\_uuid\_cache\_current\_itemsgauge Current number of items available in cbauth uuid cache                                                                 |
| cm\_uuid\_cache\_hit\_totalcounter Total number of cbauth uuid cache hits                                                                                   |
| cm\_uuid\_cache\_max\_itemsgauge Maximum capacity of cbauth uuid cache                                                                                      |
| cm\_uuid\_cache\_miss\_totalcounter Total number of cbauth uuid cache misses                                                                                |
| cm\_web\_cache\_hits\_totalcounter Total number of web cache hits                                                                                           |
| cm\_web\_cache\_inner\_hits\_totalcounter Total number of inner web cache hits                                                                              |
| cm\_web\_cache\_updates\_totalcounter Total number of web cache updates                                                                                     |
| couch\_docs\_actual\_disk\_sizegauge / bytes Amount of disk space used by the Data Service                                                                  |
| couch\_views\_actual\_disk\_sizegauge / bytes Amount of disk space used by Views data                                                                       |
| sys\_allocstallcounter Number of alloc stalls                                                                                                               |
| sys\_cpu\_burst\_rateDeprecatedgauge Rate at which CPUs overran their quota                                                                                 |
| sys\_cpu\_cgroup\_seconds\_totalcounter / seconds Number of CPU seconds utilized in the cgroup, by mode                                                     |
| sys\_cpu\_cgroup\_usage\_seconds\_totalcounter / seconds Number of 'user' and 'system' CPU seconds utilized in the cgroup                                   |
| sys\_cpu\_cores\_availablegauge Number of available CPU cores in the control group                                                                          |
| sys\_cpu\_host\_cores\_availablegauge Number of available CPU cores in the host                                                                             |
| sys\_cpu\_host\_idle\_rateDeprecatedgauge Idle CPU utilization rate in the host                                                                             |
| sys\_cpu\_host\_other\_rateDeprecatedgauge Other (not idle/user/sys/irq/stolen) CPU utilization rate in the host                                            |
| sys\_cpu\_host\_seconds\_totalcounter / seconds Number of CPU seconds utilized in the host, by mode                                                         |
| sys\_cpu\_host\_sys\_rateDeprecatedgauge System CPU utilization rate in the host                                                                            |
| sys\_cpu\_host\_user\_rateDeprecatedgauge User space CPU utilization rate in the host                                                                       |
| sys\_cpu\_host\_utilization\_rateDeprecatedgauge CPU utilization rate in the host                                                                           |
| sys\_cpu\_irq\_rateDeprecatedgauge IRQ rate                                                                                                                 |
| sys\_cpu\_stolen\_rateDeprecatedgauge CPU stolen rate                                                                                                       |
| sys\_cpu\_sys\_rateDeprecatedgauge System CPU utilization rate in the control group                                                                         |
| sys\_cpu\_throttled\_rateDeprecatedgauge Rate at which CPUs were throttled                                                                                  |
| sys\_cpu\_user\_rateDeprecatedgauge User space CPU utilization rate in the control group                                                                    |
| sys\_cpu\_utilization\_rateDeprecatedgauge CPU utilization rate in the control group                                                                        |
| sys\_disk\_queuegauge Current disk queue length of the disk                                                                                                 |
| sys\_disk\_queue\_depthgauge Maximum disk queue length of the disk                                                                                          |
| sys\_disk\_read\_bytescounter Number of bytes read by the disk                                                                                              |
| sys\_disk\_read\_time\_secondscounter Amount of time that the disk spent reading                                                                            |
| sys\_disk\_readscounter Number of reads that the disk performed                                                                                             |
| sys\_disk\_time\_secondscounter Amount of time that the disk spent performing IO                                                                            |
| sys\_disk\_write\_bytescounter Number of bytes written by the disk                                                                                          |
| sys\_disk\_write\_time\_secondscounter Amount of time that the disk spent writing                                                                           |
| sys\_disk\_writescounter Number of writes that the disk performed                                                                                           |
| sys\_mem\_actual\_freegauge / bytes Amount of system memory available, including buffers/cache                                                              |
| sys\_mem\_actual\_usedgauge / bytes Amount of system memory used, excluding buffers/cache                                                                   |
| sys\_mem\_cgroup\_actual\_usedgauge / bytes Amount of system memory used, excluding buffers/cache, in the control group                                     |
| sys\_mem\_cgroup\_limitgauge / bytes System memory limit, in the control group                                                                              |
| sys\_mem\_cgroup\_usedgauge / bytes Amount of system memory used, including buffers/cache, in the control group                                             |
| sys\_mem\_freegauge / bytes Amount of system memory free, excluding buffers/cache                                                                           |
| sys\_mem\_limitDeprecatedgauge / bytes System memory limit                                                                                                  |
| sys\_mem\_totalgauge / bytes Total amount of system memory                                                                                                  |
| sys\_mem\_used\_sysgauge / bytes Amount of system memory used, including buffers/cache                                                                      |
| sys\_pressure\_share\_time\_stalledgauge Percentage of time that tasks were stalled on a given resource                                                     |
| sys\_pressure\_total\_stall\_time\_useccounter / microseconds Absolute stall time when tasks were stalled on a given resource                               |
| sys\_swap\_totalgauge / bytes Total amount of swap space                                                                                                    |
| sys\_swap\_usedgauge / bytes Amount of swap space used                                                                                                      |
| sysproc\_cpu\_seconds\_totalcounter Amount of user CPU cycles used, by process                                                                              |
| sysproc\_cpu\_utilizationDeprecatedgauge CPU utilization rate, by process                                                                                   |
| sysproc\_major\_faults\_rawcounter Number of major page faults, by process                                                                                  |
| sysproc\_mem\_residentgauge / bytes Amount of resident memory used, by process                                                                              |
| sysproc\_mem\_sharegauge / bytes Amount of shared memory used, by process                                                                                   |
| sysproc\_mem\_sizegauge / bytes Amount of memory used, by process                                                                                           |
| sysproc\_minor\_faults\_rawgauge Number of minor page faults, by process                                                                                    |
| sysproc\_page\_faults\_rawgauge Number of page faults, by process                                                                                           |
| sysproc\_start\_timecounter OS specific time when process was started                                                                                       |