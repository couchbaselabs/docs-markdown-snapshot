---
title: Sync Gateway Metrics API Reference
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.1/modules/rest-api/pages/rest_api_metric.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:sync-gateway:rest-api:rest_api_metric.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/current/rest-api/rest_api_metric.html)

# Sync Gateway Metrics API Reference

* Introduction
* Prometheus
  * getGet debugging and monitoring runtime stats in Prometheus Exposition format
* JSON
  * getGet all Sync Gateway statistics in JSON format
* Server
  * getCheck if API is available

[API docs by Redocly](https://redocly.com/redoc/)

# Sync Gateway Metrics REST API (4.1)

Download OpenAPI specification:

License: [Business Source License 1.1 (BSL)](https://github.com/couchbase/sync%5Fgateway/blob/master/LICENSE) 

[⬆️ Metrics REST API Overview](rest-api-metrics.html)

## [](#section/Introduction)Introduction

Sync Gateway manages access and synchronization between Couchbase Lite and Couchbase Server. The Sync Gateway Metrics REST API returns Sync Gateway metrics, in JSON or Prometheus-compatible formats, for performance monitoring and diagnostic purposes.

## [](#tag/Prometheus)Prometheus

Endpoints for use with Prometheus

## [](#tag/Prometheus/operation/get%5Fmetrics)Get debugging and monitoring runtime stats in Prometheus Exposition format 

Returns Sync Gateway statistics and other runtime variables in Prometheus Exposition format.

For detailed metrics descriptions, see [Prometheus Metrics](../manage/stats-monitoring-prometheus.html).

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Dev Ops
* External Stats Reader

### Responses

**200** 

Successfully returned statistics. For detailed metrics descriptions, see [Prometheus Metrics](../manage/stats-monitoring-prometheus.html).

get/metrics

Metrics API

{protocol}://{hostname}:4986/metrics

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

## [](#tag/JSON)JSON

Endpoints for use with JSON metrics

## [](#tag/JSON/operation/get%5F%5Fexpvar)Get all Sync Gateway statistics in JSON format 

This returns a snapshot of all metrics in Sync Gateway for debugging and monitoring purposes.

This includes per database stats, replication stats, and server stats.

For details, see [JSON Metrics](../manage/stats-monitoring-json.html).

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Dev Ops
* External Stats Reader

### Responses

**200** 

Successfully returned statistics. For details, see [JSON Metrics](../manage/stats-monitoring-json.html).

get/\_expvar

Metrics API

{protocol}://{hostname}:4986/\_expvar

### Response samples 

* 200

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "cmdline": { },
* "memstats": { },
* "cb": { },
* "mc": { },
* "syncGateway_changeCache": {
  * "maxPending": { },
  * "lag-tap-0000ms": { },
  * "lag-queue-0000ms": { },
  * "lag-total-0000ms": { },
  * "outOfOrder": { },
  * "view_queries": { }  
},
* "syncGateway_db": {
  * "channelChangesFeeds": { },
  * "channelLogAdds": { },
  * "channelLogAppends": { },
  * "channelLogCacheHits": { },
  * "channelLogRewrites": { },
  * "channelLogRewriteCollisions": { },
  * "document_gets": { },
  * "revisionCache_adds": { },
  * "revisionCache_hits": { },
  * "revisionCache_misses": { },
  * "revs_added": { },
  * "sequence_gets": { },
  * "sequence_reserves": { }  
},
* "syncgateway": {
  * "global": {
    * "resource_utilization": {
      * "admin_net_bytes_recv": 0,
      * "admin_net_bytes_sent": 0,
      * "error_count": 0,
      * "go_memstats_heapalloc": 0,
      * "go_memstats_heapidle": 0,
      * "go_memstats_heapinuse": 0,
      * "go_memstats_heapreleased": 0,
      * "go_memstats_pausetotalns": 0,
      * "go_memstats_stackinuse": 0,
      * "go_memstats_stacksys": 0,
      * "go_memstats_sys": 0,
      * "goroutines_high_watermark": 0,
      * "num_goroutines": 0,
      * "num_idle_kv_ops": 0,
      * "num_idle_query_ops": 0,
      * "process_cpu_percent_utilization": 0.1,
      * "node_cpu_percent_utilization": 0.1,
      * "process_memory_resident": 0,
      * "pub_net_bytes_recv": 0,
      * "pub_net_bytes_sent": 0,
      * "system_memory_total": 0,
      * "warn_count": 0,
      * "uptime": 0  
      }  
  },
  * "per_db": [
    * {
      * "cache": { },
      * "database": { },
      * "per_replication": { },
      * "collections": { },
      * "security": { }  
      }  
  ],
  * "per_replication": [
    * {
      * "$replication_id": {
        * "sgr_active": true,
        * "sgr_docs_checked_sent": 0,
        * "sgr_num_attachments_transferred": 0,
        * "sgr_num_attachment_bytes_transferred": 0,
        * "sgr_num_docs_failed_to_push": 0,
        * "sgr_num_docs_pushed": 0  
            }  
      }  
  ]  
}
}`

## [](#tag/Server)Server

Endpoints for managing the REST API

## [](#tag/Server/operation/get%5F%5Fping)Check if API is available 

Returns OK status if API is available.

### Responses

**200** 

Returned status

get/\_ping

Metrics API

{protocol}://{hostname}:4986/\_ping

### Response samples 

* 200

Content type

text/plain

Copy

OK