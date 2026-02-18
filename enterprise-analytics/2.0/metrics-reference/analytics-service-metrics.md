---
title: Analytics Service Metrics
description: A list of the metrics provided by the Analytics Service.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/metrics-reference/pages/analytics-service-metrics.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/enterprise-analytics/2.0/metrics-reference/analytics-service-metrics.html)

# Analytics Service Metrics

> A list of the metrics provided by the Analytics Service. 

> [!TIP]
> * The type / unit badge shows shows the Prometheus [type](https://prometheus.io/docs/tutorials/understanding%5Fmetric%5Ftypes/) and [unit](https://prometheus.io/docs/practices/naming/#base-units) (if present).

| cbas\_active\_linksgauge / number Number of active links.                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| cbas\_backup\_requests\_failed\_totalcounter / count Total number of failed backup requests.                                                          |
| cbas\_backup\_requests\_totalcounter / count Total number of backup requests.                                                                         |
| cbas\_direct\_memory\_used\_bytesgauge / bytes Direct memory used in bytes.                                                                           |
| cbas\_disk\_used\_bytesgauge / bytes Disk used in bytes.                                                                                              |
| cbas\_disk\_used\_bytes\_totalDeprecatedgauge / bytes Disk used in bytes.                                                                             |
| cbas\_driver\_boot\_timestamp\_secondsgauge / seconds Analytics driver process boot timestamp in seconds since Unix epoch.                            |
| cbas\_driver\_uptime\_seconds\_totalcounter / seconds Total driver uptime in seconds.                                                                 |
| cbas\_failed\_to\_parse\_records\_countDeprecatedgauge / number Total number of records which failed to parse.                                        |
| cbas\_failed\_to\_parse\_records\_totalcounter / count Total number of records which failed to parse.                                                 |
| cbas\_gc\_count\_totalcounter / count Total number of garbage collections.                                                                            |
| cbas\_gc\_time\_milliseconds\_totalDeprecatedcounter / milliseconds Total time of garbage collections in milliseconds.                                |
| cbas\_gc\_time\_seconds\_totalcounter / seconds Total time of garbage collections in fractional seconds.                                              |
| cbas\_heap\_memory\_committed\_bytesgauge / bytes Heap memory committed in bytes.                                                                     |
| cbas\_heap\_memory\_used\_bytesgauge / bytes Heap memory used in bytes.                                                                               |
| cbas\_http\_requests\_failed\_totalcounter / count Total number of failed http requests, grouped by status code.                                      |
| cbas\_http\_requests\_timeout\_totalcounter / count Total number of HTTP requests timeouts.                                                           |
| cbas\_http\_requests\_totalcounter / count Total number of http requests.                                                                             |
| cbas\_incoming\_bytes\_totalcounter / bytes Total size of incoming records.                                                                           |
| cbas\_incoming\_records\_countDeprecatedgauge / count Total number of incoming records.                                                               |
| cbas\_incoming\_records\_totalcounter / count Total number of incoming records.                                                                       |
| cbas\_io\_reads\_totalcounter / count Total number of IO reads.                                                                                       |
| cbas\_io\_writes\_totalcounter / count Total number of IO writes.                                                                                     |
| cbas\_jobs\_totalcounter / count Total number of successful, failed, cancelled and rejected jobs.                                                     |
| cbas\_link\_connect\_failed\_totalcounter / count Total number of link connect failures.                                                              |
| cbas\_link\_disconnect\_failed\_totalcounter / count Total number of link disconnect failures.                                                        |
| cbas\_link\_invalid\_credentials\_totalcounter / count Total number of link invalid credentials.                                                      |
| cbas\_pending\_flush\_opsgauge / number Total number of pending flush operations.                                                                     |
| cbas\_pending\_merge\_opsgauge / number Total number of pending merge operations.                                                                     |
| cbas\_pending\_replicate\_opsgauge / number Total number of pending replication operations.                                                           |
| cbas\_pending\_requestsgauge / number Number of pending requests.                                                                                     |
| cbas\_queued\_http\_requests\_sizegauge / number Number of queued http requests.                                                                      |
| cbas\_queued\_jobsgauge / number Number of queued jobs.                                                                                               |
| cbas\_rebalance\_cancelled\_totalcounter / count Total number of cancelled rebalances.                                                                |
| cbas\_rebalance\_failed\_totalcounter / count Total number of rebalance failures.                                                                     |
| cbas\_rebalance\_successful\_totalcounter / count Total number of successful rebalances.                                                              |
| cbas\_remote\_storage\_object\_copy\_requests\_totalcounter / count Total number of remote storage object COPY requests.                              |
| cbas\_remote\_storage\_object\_delete\_requests\_totalcounter / count Total number of remote storage object DELETE requests.                          |
| cbas\_remote\_storage\_object\_get\_requests\_totalcounter / count Total number of remote storage object GET requests.                                |
| cbas\_remote\_storage\_object\_multipart\_download\_requests\_totalcounter / count Total number of remote storage object multipart DOWNLOAD requests. |
| cbas\_remote\_storage\_object\_multipart\_upload\_requests\_totalcounter / count Total number of remote storage object multipart UPLOAD requests.     |
| cbas\_remote\_storage\_object\_write\_requests\_totalcounter / count Total number of remote storage object WRITE requests.                            |
| cbas\_remote\_storage\_objects\_list\_requests\_totalcounter / count Total number of remote storage objects LIST requests.                            |
| cbas\_remote\_storage\_size\_bytesgauge / bytes Total remote storage space used in bytes.                                                             |
| cbas\_requests\_failed\_totalcounter / count Total number of failed requests.                                                                         |
| cbas\_requests\_totalcounter / count Total number of received requests.                                                                               |
| cbas\_running\_jobsgauge / number Number of running jobs.                                                                                             |
| cbas\_scan\_consistency\_timeout\_totalcounter / count Total number of scan consistency timeouts.                                                     |
| cbas\_system\_load\_averagegauge / number System work load.                                                                                           |
| cbas\_thread\_countgauge / number Number of threads in use.                                                                                           |
| cbas\_virtual\_buffer\_cache\_used\_pagesgauge / number Total number of used memory pages in the virtual buffer cache.                                |
| cbas\_wrapper\_boot\_timestamp\_secondsgauge / seconds Analytics wrapper process boot timestamp in seconds since Unix epoch.                          |
| cbas\_wrapper\_uptime\_seconds\_totalcounter / seconds Total wrapper uptime in seconds.                                                               |