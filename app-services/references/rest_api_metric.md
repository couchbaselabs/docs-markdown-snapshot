---
title: Capella App Services Metrics API Reference
editUrl: https://github.com/couchbaselabs/docs-capella-app-services/edit/main/modules/ROOT/pages/references/rest_api_metric.adoc
pubDate: 2026-07-20T13:54:32.914Z
link: xref:app-services::references/rest_api_metric.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/app-services/references/rest_api_metric.html)

# Capella App Services Metrics API Reference

* Introduction
* Prometheus
  * getGet debugging and monitoring runtime stats in Prometheus Exposition format

[API docs by Redocly](https://redocly.com/redoc/)

# App Services Metrics API (4.0)

Download OpenAPI specification:

License: [Business Source License 1.1 (BSL)](https://github.com/couchbase/sync%5Fgateway/blob/master/LICENSE) 

[⬆️ Manage App Services with the App Services API](rest-api-introduction.html)

## [](#section/Introduction)Introduction

App Services manages access and synchronization between Couchbase Lite and Couchbase Capella. The App Services Metrics REST API returns App Services metrics, in Prometheus-compatible format, for performance monitoring and diagnostic purposes.

## [](#tag/Prometheus)Prometheus

Endpoints for use with Prometheus

## [](#tag/Prometheus/operation/get%5Fmetrics)Get debugging and monitoring runtime stats in Prometheus Exposition format 

Returns App Services statistics and other runtime variables in Prometheus Exposition format.

For detailed metrics descriptions, see [Prometheus Metrics](../manage/stats-monitoring-prometheus.html).

### Responses

**200** 

Successfully returned statistics. For details, see [Prometheus Metrics](/sync-gateway/current/stats-monitoring-prometheus.html).

get/metrics

Metrics API

https://{hostname}:4988/metrics

### Response samples 

* 200

Content type

text/plainapplication/jsontext/plain

Copy

# HELP go_gc_duration_seconds A summary of the wall-time pause (stop-the-world) duration in garbage collection cycles.
# TYPE go_gc_duration_seconds summary
go_gc_duration_seconds{quantile="0"} 3.2374e-05
go_gc_duration_seconds{quantile="0.25"} 3.6417e-05
go_gc_duration_seconds{quantile="0.5"} 7.9875e-05
go_gc_duration_seconds{quantile="0.75"} 0.000152499
go_gc_duration_seconds{quantile="1"} 0.001503708
go_gc_duration_seconds_sum 0.002018457
go_gc_duration_seconds_count 7
# HELP go_gc_gogc_percent Heap size target percentage configured by the user, otherwise 100. This value is set by the GOGC environment variable, and the runtime/debug.SetGCPercent function. Sourced from /gc/gogc:percent
# TYPE go_gc_gogc_percent gauge
go_gc_gogc_percent 100
...