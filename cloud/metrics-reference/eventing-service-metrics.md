---
title: Eventing Service Metrics
description: A list of the metrics provided by the Eventing Service.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/metrics-reference/pages/eventing-service-metrics.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/cloud/metrics-reference/eventing-service-metrics.html)

# Eventing Service Metrics

> A list of the metrics provided by the Eventing Service. 

> [!TIP]
> * The x.y.z badge shows the Couchbase Server version the metric was added in.
> * The type / unit badge shows shows the Prometheus [type](https://prometheus.io/docs/tutorials/understanding%5Fmetric%5Ftypes/) and [unit](https://prometheus.io/docs/practices/naming/#base-units) (if present).

| eventing\_analytics\_op\_exception\_count7.6.0counter The total number of analytics query exceptions                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| eventing\_bkt\_ops\_cas\_mismatch\_count7.0.0counter The total number of Key-Value CAS mismatches                                                       |
| eventing\_bucket\_op\_exception\_count7.0.0counter The total number of Key-Value exceptions                                                             |
| eventing\_dcp\_backlog7.0.0gauge The total number of events not yet processed by eventing function                                                      |
| eventing\_dcp\_delete\_msg\_counter7.0.0counter The total number of delete events processed by worker                                                   |
| eventing\_dcp\_deletion\_sent\_to\_worker7.0.0counter The total number of delete events sent to worker to be processed by OnDelete function             |
| eventing\_dcp\_deletion\_suppressed\_counter7.0.0counter The total number of suppressed delete events                                                   |
| eventing\_dcp\_expiry\_sent\_to\_worker7.0.0counter The total number of expiry events sent to worker to be processed by OnDelete function               |
| eventing\_dcp\_mutation\_sent\_to\_worker7.0.0counter The total number of insert or update events sent to worker to be processed by OnUpdate function   |
| eventing\_dcp\_mutation\_suppressed\_counter7.0.0counter The total number of suppressed inserts or updates events                                       |
| eventing\_dcp\_mutations\_msg\_counter7.0.0counter The total number of insert or update events processed by worker                                      |
| eventing\_n1ql\_op\_exception\_count7.0.0counter The total number of Query exceptions                                                                   |
| eventing\_on\_delete\_failure7.0.0counter The total number of failed OnDelete calls                                                                     |
| eventing\_on\_delete\_success7.0.0counter The total number of successful OnDelete calls                                                                 |
| eventing\_on\_update\_failure7.0.0counter The total number of failed OnUpdate calls                                                                     |
| eventing\_on\_update\_success7.0.0counter The total number of successful OnUpdate calls                                                                 |
| eventing\_timeout\_count7.0.0counter The total number of JavaScript executions exceeding execution timeout                                              |
| eventing\_timer\_callback\_failure7.0.0counter The total number of failed timer callback invocations                                                    |
| eventing\_timer\_callback\_missing\_counter7.0.0counter The total number of undefined timer callback functions                                          |
| eventing\_timer\_callback\_success7.0.0counter The total number of successful timer callback invocations                                                |
| eventing\_timer\_cancel\_counter7.0.0counter The total number of successful CancelTimer call                                                            |
| eventing\_timer\_context\_size\_exception\_counter7.0.0counter The total number of timer\_create\_failure due to payload exceeding timer\_context\_size |
| eventing\_timer\_create\_counter7.0.0counter The total number of successful CreateTimer call                                                            |
| eventing\_timer\_create\_failure7.0.0counter The total number of failed CreateTimer call                                                                |
| eventing\_timer\_msg\_counter7.0.0gauge The total number of timer callbacks processed                                                                   |