---
title: Analytics Service Metrics
description: A list of the metrics provided by the Analytics Service.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/metrics-reference/pages/analytics-service-metrics.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.6@server:metrics-reference:analytics-service-metrics.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/metrics-reference/analytics-service-metrics.html)

# Analytics Service Metrics

> A list of the metrics provided by the Analytics Service. 

The following Analytics Service metrics can be queried by means of the REST APIs described in [Statistics](../rest-api/rest-statistics.md).

See [Analytics Service Metrics Cross Reference](analytics-service-metrics-cross-reference.md) if you are looking for a metric name you know from an alternative supported or legacy tool.

> [!TIP]
> * The x.y.z badge shows the Couchbase Server version the metric was added in.
> * The type / unit badge shows shows the Prometheus [type](https://prometheus.io/docs/tutorials/understanding%5Fmetric%5Ftypes/) and [unit](https://prometheus.io/docs/practices/naming/#base-units) (if present).

| cbas\_active\_links7.2.4gauge / number Number of active links.                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| cbas\_backup\_requests\_failed\_total7.6.2counter / count Total number of failed backup requests.                                                            |
| cbas\_backup\_requests\_total7.6.2counter / count Total number of backup requests.                                                                           |
| cbas\_direct\_memory\_used\_bytes7.0.2gauge / bytes Direct memory used in bytes.                                                                             |
| cbas\_disk\_used\_bytes7.6.0gauge / bytes Disk used in bytes.                                                                                                |
| cbas\_disk\_used\_bytes\_total7.0.0Deprecated in 7.6.0gauge / bytes Disk used in bytes.                                                                      |
| cbas\_driver\_boot\_timestamp\_seconds7.6.0gauge / seconds Analytics driver process boot timestamp in seconds since Unix epoch.                              |
| cbas\_driver\_uptime\_seconds\_total7.6.1counter / seconds Total driver uptime in seconds.                                                                   |
| cbas\_extra\_incoming\_records\_total7.6.6counter / count Total number of incoming records that were processed multiple times due to DCP snapshot alignment. |
| cbas\_failed\_to\_parse\_records\_count7.0.0Deprecated in 7.6.0gauge / number Total number of records which failed to parse.                                 |
| cbas\_failed\_to\_parse\_records\_total7.6.0counter / count Total number of records which failed to parse.                                                   |
| cbas\_gc\_count\_total7.0.0counter / count Total number of garbage collections.                                                                              |
| cbas\_gc\_time\_milliseconds\_total7.0.0Deprecated in 7.6.0counter / milliseconds Total time of garbage collections in milliseconds.                         |
| cbas\_gc\_time\_seconds\_total7.6.0counter / seconds Total time of garbage collections in fractional seconds.                                                |
| cbas\_heap\_memory\_committed\_bytes7.1.0gauge / bytes Heap memory committed in bytes.                                                                       |
| cbas\_heap\_memory\_max\_bytes7.2.7gauge / bytes Heap memory max in bytes.                                                                                   |
| cbas\_heap\_memory\_used\_bytes7.0.0gauge / bytes Heap memory used in bytes.                                                                                 |
| cbas\_http\_requests\_failed\_total7.6.0counter / count Total number of failed http requests, grouped by status code.                                        |
| cbas\_http\_requests\_timeout\_total7.6.2counter / count Total number of HTTP requests timeouts.                                                             |
| cbas\_http\_requests\_total7.6.0counter / count Total number of http requests.                                                                               |
| cbas\_incoming\_records\_count7.0.0Deprecated in 7.6.0gauge / count Total number of incoming records.                                                        |
| cbas\_incoming\_records\_total7.6.0counter / count Total number of incoming records.                                                                         |
| cbas\_io\_reads\_total7.0.0counter / count Total number of IO reads.                                                                                         |
| cbas\_io\_writes\_total7.0.0counter / count Total number of IO writes.                                                                                       |
| cbas\_jobs\_total7.6.2counter / count Total number of successful, failed, cancelled and rejected jobs.                                                       |
| cbas\_link\_connect\_failed\_total7.6.2counter / count Total number of link connect failures.                                                                |
| cbas\_link\_disconnect\_failed\_total7.6.2counter / count Total number of link disconnect failures.                                                          |
| cbas\_link\_invalid\_credentials\_total7.6.2counter / count Total number of link invalid credentials.                                                        |
| cbas\_pending\_flush\_ops7.0.0gauge / number Total number of pending flush operations.                                                                       |
| cbas\_pending\_merge\_ops7.0.0gauge / number Total number of pending merge operations.                                                                       |
| cbas\_pending\_replicate\_ops7.1.0gauge / number Total number of pending replication operations.                                                             |
| cbas\_pending\_requests7.2.4gauge / number Number of pending requests.                                                                                       |
| cbas\_queued\_http\_requests\_size7.6.0gauge / number Number of queued http requests.                                                                        |
| cbas\_queued\_jobs7.2.4gauge / number Number of queued jobs.                                                                                                 |
| cbas\_rebalance\_cancelled\_total7.6.0counter / count Total number of cancelled rebalances.                                                                  |
| cbas\_rebalance\_failed\_total7.6.0counter / count Total number of rebalance failures.                                                                       |
| cbas\_rebalance\_successful\_total7.6.0counter / count Total number of successful rebalances.                                                                |
| cbas\_requests\_failed\_total7.6.2counter / count Total number of failed requests.                                                                           |
| cbas\_requests\_total7.2.4counter / count Total number of received requests.                                                                                 |
| cbas\_running\_jobs7.2.4gauge / number Number of running jobs.                                                                                               |
| cbas\_scan\_consistency\_timeout\_total7.6.2counter / count Total number of scan consistency timeouts.                                                       |
| cbas\_system\_load\_average7.0.0gauge / number System work load.                                                                                             |
| cbas\_thread\_count7.0.0gauge / number Number of threads in use.                                                                                             |
| cbas\_virtual\_buffer\_cache\_used\_pages7.0.0gauge / number Total number of used memory pages in the virtual buffer cache.                                  |
| cbas\_wrapper\_boot\_timestamp\_seconds7.6.0gauge / seconds Analytics wrapper process boot timestamp in seconds since Unix epoch.                            |
| cbas\_wrapper\_uptime\_seconds\_total7.6.1counter / seconds Total wrapper uptime in seconds.                                                                 |