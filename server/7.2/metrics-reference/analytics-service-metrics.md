---
title: Analytics Service Metrics
description: A list of the metrics provided by the Analytics Service.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/metrics-reference/pages/analytics-service-metrics.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:metrics-reference:analytics-service-metrics.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/metrics-reference/analytics-service-metrics.html)

# Analytics Service Metrics

> A list of the metrics provided by the Analytics Service. 

The following Analytics Service metrics can be queried by means of the REST APIs described in [Statistics](../rest-api/rest-statistics.md).

> [!TIP]
> * The x.y.z badge shows the Couchbase Server version the metric was added in.
> * The type / unit badge shows shows the Prometheus [type](https://prometheus.io/docs/tutorials/understanding%5Fmetric%5Ftypes/) and [unit](https://prometheus.io/docs/practices/naming/#base-units) (if present).

| cbas\_active\_links7.2.4 gauge Number of active links.                                                              |
| ------------------------------------------------------------------------------------------------------------------- |
| cbas\_direct\_memory\_used\_bytes7.0.2 gauge Direct memory used in bytes.                                           |
| cbas\_disk\_used\_bytes\_total7.0.0 gauge Total disk used in bytes.                                                 |
| cbas\_failed\_to\_parse\_records\_count7.0.0 gauge Number of records which failed to parse.                         |
| cbas\_gc\_count\_total7.0.0 gauge Total number of garbage collections.                                              |
| cbas\_gc\_time\_milliseconds\_total7.0.0 gauge Total time of garbage collections in milliseconds.                   |
| cbas\_heap\_memory\_committed\_bytes7.1.0 gauge Heap memory committed in bytes.                                     |
| cbas\_heap\_memory\_max\_bytes7.2.7 gauge / bytes Heap memory max in bytes.                                         |
| cbas\_heap\_memory\_used\_bytes7.0.0 gauge Heap memory used in bytes.                                               |
| cbas\_incoming\_records\_count7.0.0 gauge Number of incoming records.                                               |
| cbas\_io\_reads\_total7.0.0 gauge Total number of IO reads.                                                         |
| cbas\_io\_writes\_total7.0.0 gauge Total number of IO writes.                                                       |
| cbas\_pending\_flush\_ops7.0.0 gauge Total number of pending flush operations.                                      |
| cbas\_pending\_merge\_ops7.0.0 gauge Total number of pending merge operations.                                      |
| cbas\_pending\_replicate\_ops7.1.0 gauge Total number of pending replication operations.                            |
| cbas\_pending\_requests7.2.4 gauge Number of pending requests.                                                      |
| cbas\_queued\_jobs7.2.4 gauge Number of queued jobs.                                                                |
| cbas\_requests\_total7.2.4 counter Total number of received requests.                                               |
| cbas\_running\_jobs7.2.4 gauge Number of running jobs.                                                              |
| cbas\_system\_load\_average7.0.0 gauge System work load.                                                            |
| cbas\_thread\_count7.0.0 gauge Number of threads in use.                                                            |
| cbas\_virtual\_buffer\_cache\_used\_pages7.0.0 gauge Total number of used memory pages in the virtual buffer cache. |