---
title: Backup Service Metrics
description: A list of the metrics provided by the Backup Service.
pubDate: 2026-08-18T04:50:45.818Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/metrics-reference/pages/backup-service-metrics.adoc
  xref: xref:server:metrics-reference:backup-service-metrics.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/metrics-reference/backup-service-metrics.html)

# Backup Service Metrics

> A list of the metrics provided by the Backup Service. 

The following Backup Service metrics can be queried by means of the REST APIs described in [Statistics](../rest-api/rest-statistics.md).

Histograms

Note that each histogram metric will generate three time series, with the following suffixes:

* `_count`
* `_sum`
* `_bucket`

Please refer to [Prometheus Histograms and Summaries](https://prometheus.io/docs/practices/histograms/) for more information.

> [!TIP]
> * The x.y.z badge shows the Couchbase Server version the metric was added in.
> * The type / unit badge shows shows the Prometheus [type](https://prometheus.io/docs/tutorials/understanding%5Fmetric%5Ftypes/) and [unit](https://prometheus.io/docs/practices/naming/#base-units) (if present).

`backup_data_size`

7.0.0 gauge / bytes Repository backed up data size

`backup_dispatched`

7.0.0 counter Number of tasks dispatched to be run

`backup_location_check`

7.0.0 counter Number of location checks performed

`backup_request_duration_seconds`

8.0.0 histogram Histogram of the request duration

`backup_task_duration_seconds`

7.0.0 histogram Histogram of the task duration

`backup_task_orphaned`

7.0.0 counter Number of tasks that were triggered to run but the status is unknown

`backup_task_run`

7.0.0 counter Number of tasks run