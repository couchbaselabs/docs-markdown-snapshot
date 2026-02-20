---
title: Backup Service Metrics
description: A list of the metrics provided by the Backup Service.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/metrics-reference/pages/backup-service-metrics.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:metrics-reference:backup-service-metrics.adoc[]
---

[View original HTML](/server/7.2/metrics-reference/backup-service-metrics.html)

# Backup Service Metrics

> A list of the metrics provided by the Backup Service. 

The following Backup Service metrics can be queried by means of the REST APIs described in [Statistics](../rest-api/rest-statistics.md).

> [!TIP]
> * The x.y.z badge shows the Couchbase Server version the metric was added in.
> * The type / unit badge shows shows the Prometheus [type](https://prometheus.io/docs/tutorials/understanding%5Fmetric%5Ftypes/) and [unit](https://prometheus.io/docs/practices/naming/#base-units) (if present).

| backup\_data\_size7.0.0 gauge / bytes Repository backed up data size                                     |
| -------------------------------------------------------------------------------------------------------- |
| backup\_dispatched7.0.0 counter Number of tasks dispatched to be run                                     |
| backup\_location\_check7.0.0 counter Number of location checks performed                                 |
| backup\_task\_duration\_seconds7.0.0 histogram Histogram of the task duration                            |
| backup\_task\_orphaned7.0.0 counter Number of tasks that were triggered to run but the status is unknown |
| backup\_task\_run7.0.0 counter Number of tasks run                                                       |