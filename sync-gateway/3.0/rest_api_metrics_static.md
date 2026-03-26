---
title: Metrics REST API (Static Page)
description: Description of the Sync Gateway Metrics REST API, alternative
  representation as a static page
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.0/modules/ROOT/pages/rest_api_metrics_static.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.0@sync-gateway::rest_api_metrics_static.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.0/rest_api_metrics_static.html)

# Metrics REST API (Static Page)

> Description of the Sync Gateway Metrics REST API, alternative representation as a static page  

Related _REST API_ topics: [Public REST API (Static Page)](rest%5Fapi%5Fpublic%5Fstatic.md) | [Admin REST API (Static Page)](rest%5Fapi%5Fadmin%5Fstatic.md)

## [](#%5Fpaths)Paths

This resources section groups together the available API operations under functional categories.

* [Debugging/monitoring at runtime](#%5Fexpvar%5Fget)
* [Debugging/monitoring runtime stats in Prometheus format](#%5Fmetrics%5Fget)

### [](#%5Fexpvar%5Fget)Debugging/monitoring at runtime

GET /_expvar

#### [](#description)Description

The `Expvars` method returns Sync Gateways' numerous statistics, and other runtime variables, in JSON format. Making them readily available for debugging or performance monitoring purposes.

**See** : [Sync Gateway Statistics Schema](stats-monitoring.html) for more details on the metrics collected and reported by Sync Gateway.

_Sync Gateway Roles Required:_

– Sync Gateway Dev Ops – External Stats Reader

#### [](#responses)Responses

| HTTP Code | Description            | Schema                 |
| --------- | ---------------------- | ---------------------- |
| **200**   | OK - indicates success | [ExpVars](#%5Fexpvars) |

#### [](#tags)Tags

* Standard Output

### [](#%5Fmetrics%5Fget)Debugging/monitoring runtime stats in Prometheus format

GET /_metrics

#### [](#description-2)Description

The `_metrics` method returns Sync Gateway's statistics and other runtime variables in **Prometheus** format. This makes for a convenient feed for your debugging or performance monitoring purposes.

* For more details on the metrics collected and reported by Sync Gateway – see: [Sync Gateway Statistics Schema](stats-monitoring.html).
* For more details on Monitoring Sync Gateway using the `_metrics` feed – see: our blog on [Monitoring and Visualization of Couchbase Sync Gateway with Prometheus and Grafana](https://blog.couchbase.com/monitoring-and-visualization-of-couchbase-sync-gateway-with-prometheus-and-grafana/)

_Sync Gateway Roles Required:_

– Sync Gateway Dev Ops – External Stats Reader

#### [](#responses-2)Responses

| HTTP Code | Description            | Schema                 |
| --------- | ---------------------- | ---------------------- |
| **200**   | OK - indicates success | [Metrics](#%5Fmetrics) |

#### [](#tags-2)Tags

* Prometheus

## [](#%5Fdefinitions)Definitions

### [](#%5Fexpvars)ExpVars

| Name                                    | Description                                                                     | Schema                                                              |
| --------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **cb** _optional_                       | Variables reported by the Couchbase SDK (go\_couchbase package)                 | object                                                              |
| **cmdline** _optional_                  | Built-in variables from the Go runtime, lists the command-line arguments        | object                                                              |
| **mc** _optional_                       | Variables reported by the low-level memcached API (gomemcached package)         | object                                                              |
| **memstats** _optional_                 | Dumps a large amount of information about the memory heap and garbage collector | object                                                              |
| **syncGateway\_changeCache** _optional_ |                                                                                 | [syncGateway\_changeCache](#%5Fexpvars%5Fsyncgateway%5Fchangecache) |
| **syncGateway\_db** _optional_          |                                                                                 | [syncGateway\_db](#%5Fexpvars%5Fsyncgateway%5Fdb)                   |
| **syncgateway** _optional_              | Monitoring stats                                                                | [syncgateway](#%5Fexpvars%5Fsyncgateway)                            |

**syncGateway\_changeCache**

| Name                            | Description                                                          | Schema |
| ------------------------------- | -------------------------------------------------------------------- | ------ |
| **lag-queue-0000ms** _optional_ | Histogram of delay from Tap feed till doc is posted to changes feed  | object |
| **lag-tap-0000ms** _optional_   | Histogram of delay from doc save till it shows up in Tap feed        | object |
| **lag-total-0000ms** _optional_ | Histogram of total delay from doc save till posted to changes feed   | object |
| **maxPending** _optional_       | Max number of sequences waiting on a missing earlier sequence number | object |
| **outOfOrder** _optional_       | Number of out-of-order sequences posted                              | object |
| **view\_queries** _optional_    | Number of queries to channels view                                   | object |

**syncGateway\_db**

| Name                                       | Description                                                                                           | Schema |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------- | ------ |
| **channelChangesFeeds** _optional_         | Number of calls to db.changesFeed, i.e. generating a changes feed for a single channel.               | object |
| **channelLogAdds** _optional_              | Number of entries added to channel logs                                                               | object |
| **channelLogAppends** _optional_           | Number of times entries were written to channel logs using an APPEND operation                        | object |
| **channelLogCacheHits** _optional_         | Number of requests for channel-logs that were fulfilled from the in-memory cache                      | object |
| **channelLogRewriteCollisions** _optional_ | Number of collisions while attempting to rewrite channel logs using SET                               | object |
| **channelLogRewrites** _optional_          | Number of times entries were written to channel logs using a SET operation (rewriting the entire log) | object |
| **document\_gets** _optional_              | Number of times a document was read from the database                                                 | object |
| **revisionCache\_adds** _optional_         | Number of revisions added to the revision cache                                                       | object |
| **revisionCache\_hits** _optional_         | Number of times a revision-cache lookup succeeded                                                     | object |
| **revisionCache\_misses** _optional_       | Number of times a revision-cache lookup failed                                                        | object |
| **revs\_added** _optional_                 | Number of revisions added to the database (including deletions)                                       | object |
| **sequence\_gets** _optional_              | Number of times the database's lastSequence was read                                                  | object |
| **sequence\_reserves** _optional_          | Number of times the database's lastSequence was incremented                                           | object |

**syncgateway**

| Name                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Schema                                                         |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **global** _optional_           | Global Sync Gateway stats                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [global](#%5Fexpvars%5Fglobal)                                 |
| **per\_db** _optional_          | This array contains stats for all databases declared in the config file – see the [Sync Gateway Statistics Schema](stats-monitoring.html) for more details on the metrics collected and reported by Sync Gateway. The statistics for each {$db\_name} database are grouped into: \* cache related statistics \* cbl\_replication\_push \* cbl\_replication\_pull \* database\_related\_statistics \* delta\_sync \* gsi\_views \* security\_related\_statistics \* shared\_bucket\_import \* per\_replication statistics for each replication\_id | < [per\_db](#%5Fexpvars%5Fper%5Fdb) \> array                   |
| **per\_replication** _optional_ | An array of stats for each replication declared in the config file **Deprecated @ 2.8**: used only by inter-sync-gateway replications version 1.                                                                                                                                                                                                                                                                                                                                                                                                  | < [per\_replication](#%5Fexpvars%5Fper%5Freplication) \> array |

**global**

| Name                                 | Description                | Schema                                                                 |
| ------------------------------------ | -------------------------- | ---------------------------------------------------------------------- |
| **resource\_utilization** _optional_ | Resource utilization stats | [resource\_utilization](#%5Fexpvars%5Fglobal%5Fresource%5Futilization) |

**resource\_utilization**

| Name                                              | Schema  |
| ------------------------------------------------- | ------- |
| **admin\_net\_bytes\_recv** _optional_            | integer |
| **admin\_net\_bytes\_sent** _optional_            | integer |
| **error\_count** _optional_                       | integer |
| **go\_memstats\_heapalloc** _optional_            | integer |
| **go\_memstats\_heapidle** _optional_             | integer |
| **go\_memstats\_heapinuse** _optional_            | integer |
| **go\_memstats\_heapreleased** _optional_         | integer |
| **go\_memstats\_pausetotalns** _optional_         | integer |
| **go\_memstats\_stackinuse** _optional_           | integer |
| **go\_memstats\_stacksys** _optional_             | integer |
| **go\_memstats\_sys** _optional_                  | integer |
| **goroutines\_high\_watermark** _optional_        | integer |
| **num\_goroutines** _optional_                    | integer |
| **process\_cpu\_percent\_utilization** _optional_ | integer |
| **process\_memory\_resident** _optional_          | integer |
| **pub\_net\_bytes\_recv** _optional_              | integer |
| **pub\_net\_bytes\_sent** _optional_              | integer |
| **system\_memory\_total** _optional_              | integer |
| **warn\_count** _optional_                        | integer |

**per\_db**

| Name                            | Schema           |
| ------------------------------- | ---------------- |
| **cache** _optional_            | object           |
| **database** _optional_         | object           |
| **per\_replication** _optional_ | < object > array |
| **security** _optional_         | object           |

**per\_replication**

| Name                            | Schema                                                                 |
| ------------------------------- | ---------------------------------------------------------------------- |
| **$replication\_id** _optional_ | [$replication\_id](#%5Fexpvars%5Fper%5Freplication%5Freplication%5Fid) |

**$replication\_id**

| Name                                                    | Description                                                                                                                                                                                                                                                                                                         | Schema  |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **sgr\_active** _optional_                              | Whether the replication is active at this time. **Deprecated @ 2.8**: used only by inter-sync-gateway replications version 1.                                                                                                                                                                                       | boolean |
| **sgr\_docs\_checked\_sent** _optional_                 | The total number of documents checked for changes since replication started. This represents the number of potential change notifications pushed by Sync Gateway. **Constraints**This is not necessarily the number of documents pushed, as a given target might already have the change. Used by versions 1 and 2. | integer |
| **sgr\_num\_attachment\_bytes\_transferred** _optional_ | The total number of attachment bytes transferred since replication started. **Deprecated @ 2.8**: used only by inter-sync-gateway replications version 1.                                                                                                                                                           | integer |
| **sgr\_num\_attachments\_transferred** _optional_       | The total number of attachments transferred since replication started. **Deprecated @ 2.8**: used only by inter-sync-gateway replications version 1.                                                                                                                                                                | integer |
| **sgr\_num\_docs\_failed\_to\_push** _optional_         | The total number of documents that failed to be pushed since replication started. Used by versions 1 and 2.                                                                                                                                                                                                         | integer |
| **sgr\_num\_docs\_pushed** _optional_                   | The total number of documents that were pushed since replication started. Used by versions 1 and 2.                                                                                                                                                                                                                 | integer |

### [](#%5Fmetrics)Metrics

The Prometheus output is expected to by consumed only by a Prometheus server. For that reason its format is irrelevant, and a brief extract is show here for completeness and information only.

* For more details on the metrics collected and reported by Sync Gateway – see: [Sync Gateway Statistics Schema](stats-monitoring.html).
* For more details on Monitoring Sync Gateway using the `_metrics` feed – see: our blog on [Monitoring and Visualization of Couchbase Sync Gateway with Prometheus and Grafana](https://blog.couchbase.com/monitoring-and-visualization-of-couchbase-sync-gateway-with-prometheus-and-grafana/)

...
# HELP go_gc_duration_seconds A summary of the pause duration of garbage collection cycles.
# TYPE go_gc_duration_seconds summary
go_gc_duration_seconds{quantile="0"} 0.0001155
go_gc_duration_seconds{quantile="0.25"} 0.0001254
go_gc_duration_seconds{quantile="0.5"} 0.0001597
go_gc_duration_seconds{quantile="0.75"} 0.0001806
go_gc_duration_seconds{quantile="1"} 0.0049731
go_gc_duration_seconds_sum 0.006334
go_gc_duration_seconds_count 9
# HELP go_goroutines Number of goroutines that currently exist.
# TYPE go_goroutines gauge
go_goroutines 205
...

_Type_ : object

---

##### 

## [](#related-content)Related Content

###### [](#-2)

API Topics

* [Public REST API](rest-api.md)
* [Admin REST API](rest-api-admin.md)
* [Metrics REST API](rest-api-metrics.md)

###### [](#-3)

Reference

* [Bootstrap](configuration-schema-bootstrap.md)
* [Database](configuration-schema-database.md)
* [Database Security](configuration-schema-db-security.md)
* [Access Control](configuration-schema-access-control.md)
* [Import Filter](configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)