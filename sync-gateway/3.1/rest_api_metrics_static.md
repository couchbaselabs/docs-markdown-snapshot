---
title: Metrics REST API (Static Page)
description: Description of the Sync Gateway Metrics REST API, alternative
  representation as a static page
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.1/modules/ROOT/pages/rest_api_metrics_static.adoc
  xref: xref:3.1@sync-gateway::rest_api_metrics_static.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.1/rest_api_metrics_static.html)

# Metrics REST API (Static Page)

> Description of the Sync Gateway Metrics REST API, alternative representation as a static page  

Related _REST API_ topics: [Public REST API (Static Page)](rest%5Fapi%5Fpublic%5Fstatic.md) | [Admin REST API (Static Page)](rest%5Fapi%5Fadmin%5Fstatic.md)

## [](#overview)Overview

### Version information

_Version_ : 3.1

### Host information

{protocol}://{hostname}:4986

Metrics API

| Component    | Description                                                                   |
| ------------ | ----------------------------------------------------------------------------- |
| **protocol** | The protocol to use (HTTP or HTTPS) **Values:** http, https **Example:** http |
| **hostname** | The hostname to use **Example:** localhost                                    |

## [](#resources)Resources

This section describes the operations available with this REST API. The operations are grouped in the following categories.

[Default](#tag-Default)  
[Prometheus](#tag-Prometheus)  
[Server](#tag-Server)

### [](#tag-Default)Default

**Table of Contents**

[Get all Sync Gateway statistics](#get%5F%5Fexpvar)

#### [](#get%5F%5Fexpvar)Get all Sync Gateway statistics

GET /_expvar

##### [](#get%5F%5Fexpvar-description)Description

This returns a snapshot of all metrics in Sync Gateway for debugging and monitoring purposes.

This includes per database stats, replication stats, and server stats.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Dev Ops
* External Stats Reader

Produces

* application/javascript

##### [](#get%5F%5Fexpvar-responses)Responses

| HTTP Code | Description         | Schema                                                    |
| --------- | ------------------- | --------------------------------------------------------- |
| 200       | Returned statistics | [GetExpvar200Response](#get%5F%5Fexpvar%5F200%5Fresponse) |

### [](#tag-Prometheus)Prometheus

Endpoints for use with Prometheus

[Debugging/monitoring runtime stats in Prometheus Exposition format](#get%5Fmetrics)  
[Debugging/monitoring runtime stats in Prometheus Exposition format](#get%5Fmetrics)

#### [](#get%5Fmetrics)Debugging/monitoring runtime stats in Prometheus Exposition format

GET /_metrics

##### [](#get%5Fmetrics-description)Description

Returns Sync Gateway statistics and other runtime variables in Prometheus Exposition format.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Dev Ops
* External Stats Reader

Produces

* text/plain

##### [](#get%5Fmetrics-responses)Responses

| HTTP Code | Description                 | Schema |
| --------- | --------------------------- | ------ |
| 200       | Successfully returned stats | String |

#### [](#get%5Fmetrics)Debugging/monitoring runtime stats in Prometheus Exposition format

GET /metrics

##### [](#get%5Fmetrics-description)Description

Returns Sync Gateway statistics and other runtime variables in Prometheus Exposition format.

Required Sync Gateway RBAC roles:

* Sync Gateway Architect
* Sync Gateway Dev Ops
* External Stats Reader

Produces

* text/plain

##### [](#get%5Fmetrics-responses)Responses

| HTTP Code | Description                 | Schema |
| --------- | --------------------------- | ------ |
| 200       | Successfully returned stats | String |

### [](#tag-Server)Server

**Table of Contents**

[Check if API is available](#get%5F%5Fping)  
[Check if API is available](#head%5F%5Fping)

#### [](#get%5F%5Fping)Check if API is available

GET /_ping

##### [](#get%5F%5Fping-description)Description

Returns OK status if API is available.

Produces

* text/plain

##### [](#get%5F%5Fping-responses)Responses

| HTTP Code | Description     | Schema |
| --------- | --------------- | ------ |
| 200       | Returned status | String |

#### [](#head%5F%5Fping)Check if API is available

HEAD /_ping

##### [](#head%5F%5Fping-description)Description

Returns OK status if API is available.

##### [](#head%5F%5Fping-responses)Responses

| HTTP Code | Description         | Schema |
| --------- | ------------------- | ------ |
| 200       | Server is available |        |

## [](#models)Definitions

This section describes the properties consumed and returned by this REST API.

[ExpVars](#ExpVars)  
[GetExpvar200Response](#get%5F%5Fexpvar%5F200%5Fresponse)  
[GetExpvar200ResponseSyncGatewayChangeCache](#get%5F%5Fexpvar%5F200%5Fresponse%5FsyncGateway%5FchangeCache)  
[GetExpvar200ResponseSyncGatewayDb](#get%5F%5Fexpvar%5F200%5Fresponse%5FsyncGateway%5Fdb)  
[GetExpvar200ResponseSyncgateway](#get%5F%5Fexpvar%5F200%5Fresponse%5Fsyncgateway)  
[GetExpvar200ResponseSyncgatewayGlobal](#get%5F%5Fexpvar%5F200%5Fresponse%5Fsyncgateway%5Fglobal)  
[GetExpvar200ResponseSyncgatewayGlobalResourceUtilization](#get%5F%5Fexpvar%5F200%5Fresponse%5Fsyncgateway%5Fglobal%5Fresource%5Futilization)  
[GetExpvar200ResponseSyncgatewayPerDbInner](#get%5F%5Fexpvar%5F200%5Fresponse%5Fsyncgateway%5Fper%5Fdb%5Finner)  
[GetExpvar200ResponseSyncgatewayPerReplicationInner](#get%5F%5Fexpvar%5F200%5Fresponse%5Fsyncgateway%5Fper%5Freplication%5Finner)  
[GetExpvar200ResponseSyncgatewayPerReplicationInnerReplicationId](#get%5F%5Fexpvar%5F200%5Fresponse%5Fsyncgateway%5Fper%5Freplication%5Finner%5F%5Freplication%5Fid)

### [](#ExpVars)ExpVars

 Object

| Property                                |                                                                                 | Schema                                                                                                      |
| --------------------------------------- | ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **cmdline** _optional_                  | Built-in variables from the Go runtime, lists the command-line arguments        | Object                                                                                                      |
| **memstats** _optional_                 | Dumps a large amount of information about the memory heap and garbage collector | Object                                                                                                      |
| **cb** _optional_                       | Variables reported by the Couchbase SDK (go\_couchbase package)                 | Object                                                                                                      |
| **mc** _optional_                       | Variables reported by the low-level memcached API (gomemcached package)         | Object                                                                                                      |
| **syncGateway\_changeCache** _optional_ |                                                                                 | [GetExpvar200ResponseSyncGatewayChangeCache](#get%5F%5Fexpvar%5F200%5Fresponse%5FsyncGateway%5FchangeCache) |
| **syncGateway\_db** _optional_          |                                                                                 | [GetExpvar200ResponseSyncGatewayDb](#get%5F%5Fexpvar%5F200%5Fresponse%5FsyncGateway%5Fdb)                   |
| **syncgateway** _optional_              | Monitoring stats                                                                | [GetExpvar200ResponseSyncgateway](#get%5F%5Fexpvar%5F200%5Fresponse%5Fsyncgateway)                          |

### [](#get%5F%5Fexpvar%5F200%5Fresponse)GetExpvar200Response

 Object

| Property                                |                                                                                 | Schema                                                                                                      |
| --------------------------------------- | ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **cmdline** _optional_                  | Built-in variables from the Go runtime, lists the command-line arguments        | Object                                                                                                      |
| **memstats** _optional_                 | Dumps a large amount of information about the memory heap and garbage collector | Object                                                                                                      |
| **cb** _optional_                       | Variables reported by the Couchbase SDK (go\_couchbase package)                 | Object                                                                                                      |
| **mc** _optional_                       | Variables reported by the low-level memcached API (gomemcached package)         | Object                                                                                                      |
| **syncGateway\_changeCache** _optional_ |                                                                                 | [GetExpvar200ResponseSyncGatewayChangeCache](#get%5F%5Fexpvar%5F200%5Fresponse%5FsyncGateway%5FchangeCache) |
| **syncGateway\_db** _optional_          |                                                                                 | [GetExpvar200ResponseSyncGatewayDb](#get%5F%5Fexpvar%5F200%5Fresponse%5FsyncGateway%5Fdb)                   |
| **syncgateway** _optional_              | Monitoring stats                                                                | [GetExpvar200ResponseSyncgateway](#get%5F%5Fexpvar%5F200%5Fresponse%5Fsyncgateway)                          |

### [](#get%5F%5Fexpvar%5F200%5Fresponse%5FsyncGateway%5FchangeCache)GetExpvar200ResponseSyncGatewayChangeCache

 Object

| Property                        |                                                                      | Schema |
| ------------------------------- | -------------------------------------------------------------------- | ------ |
| **maxPending** _optional_       | Max number of sequences waiting on a missing earlier sequence number | Object |
| **lag-tap-0000ms** _optional_   | Histogram of delay from doc save till it shows up in Tap feed        | Object |
| **lag-queue-0000ms** _optional_ | Histogram of delay from Tap feed till doc is posted to changes feed  | Object |
| **lag-total-0000ms** _optional_ | Histogram of total delay from doc save till posted to changes feed   | Object |
| **outOfOrder** _optional_       | Number of out-of-order sequences posted                              | Object |
| **view\_queries** _optional_    | Number of queries to channels view                                   | Object |

### [](#get%5F%5Fexpvar%5F200%5Fresponse%5FsyncGateway%5Fdb)GetExpvar200ResponseSyncGatewayDb

 Object

| Property                                   |                                                                                                       | Schema |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------- | ------ |
| **channelChangesFeeds** _optional_         | Number of calls to db.changesFeed, i.e. generating a changes feed for a single channel.               | Object |
| **channelLogAdds** _optional_              | Number of entries added to channel logs                                                               | Object |
| **channelLogAppends** _optional_           | Number of times entries were written to channel logs using an APPEND operation                        | Object |
| **channelLogCacheHits** _optional_         | Number of requests for channel-logs that were fulfilled from the in-memory cache                      | Object |
| **channelLogRewrites** _optional_          | Number of times entries were written to channel logs using a SET operation (rewriting the entire log) | Object |
| **channelLogRewriteCollisions** _optional_ | Number of collisions while attempting to rewrite channel logs using SET                               | Object |
| **document\_gets** _optional_              | Number of times a document was read from the database                                                 | Object |
| **revisionCache\_adds** _optional_         | Number of revisions added to the revision cache                                                       | Object |
| **revisionCache\_hits** _optional_         | Number of times a revision-cache lookup succeeded                                                     | Object |
| **revisionCache\_misses** _optional_       | Number of times a revision-cache lookup failed                                                        | Object |
| **revs\_added** _optional_                 | Number of revisions added to the database (including deletions)                                       | Object |
| **sequence\_gets** _optional_              | Number of times the database's lastSequence was read                                                  | Object |
| **sequence\_reserves** _optional_          | Number of times the database's lastSequence was incremented                                           | Object |

### [](#get%5F%5Fexpvar%5F200%5Fresponse%5Fsyncgateway)GetExpvar200ResponseSyncgateway

 Object

| Property                        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Schema                                                                                                                                 |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| **global** _optional_           | Global Sync Gateway stats                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | [GetExpvar200ResponseSyncgatewayGlobal](#get%5F%5Fexpvar%5F200%5Fresponse%5Fsyncgateway%5Fglobal)                                      |
| **per\_db** _optional_          | This array contains stats for all databases declared in the config file -- see the [Sync Gateway Statistics Schema](./../stats-monitoring.html) for more details on the metrics collected and reported by Sync Gateway. The statistics for each {$db\_name} database are grouped into: cache related statistics collections statistics cbl\_replication\_push cbl\_replication\_pull database\_related\_statistics delta\_sync gsi\_views security\_related\_statistics shared\_bucket\_import per\_replication statistics for each replication\_id | [GetExpvar200ResponseSyncgatewayPerDbInner](#get%5F%5Fexpvar%5F200%5Fresponse%5Fsyncgateway%5Fper%5Fdb%5Finner)array                   |
| **per\_replication** _optional_ | An array of stats for each replication declared in the config file **Deprecated @ 2.8**: used only by inter-sync-gateway replications version 1.                                                                                                                                                                                                                                                                                                                                                                                                    | [GetExpvar200ResponseSyncgatewayPerReplicationInner](#get%5F%5Fexpvar%5F200%5Fresponse%5Fsyncgateway%5Fper%5Freplication%5Finner)array |

### [](#get%5F%5Fexpvar%5F200%5Fresponse%5Fsyncgateway%5Fglobal)GetExpvar200ResponseSyncgatewayGlobal

 Object

| Property                             |                            | Schema                                                                                                                                        |
| ------------------------------------ | -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| **resource\_utilization** _optional_ | Resource utilization stats | [GetExpvar200ResponseSyncgatewayGlobalResourceUtilization](#get%5F%5Fexpvar%5F200%5Fresponse%5Fsyncgateway%5Fglobal%5Fresource%5Futilization) |

### [](#get%5F%5Fexpvar%5F200%5Fresponse%5Fsyncgateway%5Fglobal%5Fresource%5Futilization)GetExpvar200ResponseSyncgatewayGlobalResourceUtilization

 Object

| Property                                          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Schema        |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| **admin\_net\_bytes\_recv** _optional_            | The total number of bytes received (since node start-up) on the network interface to which the Sync Gateway api.admin\_interface is bound.                                                                                                                                                                                                                                                                                                                                                                                                                                    | Integer       |
| **admin\_net\_bytes\_sent** _optional_            | The total number of bytes sent (since node start-up) on the network interface to which the Sync Gateway api.admin\_interface is bound.                                                                                                                                                                                                                                                                                                                                                                                                                                        | Integer       |
| **error\_count** _optional_                       | The total number of errors logged.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Integer       |
| **go\_memstats\_heapalloc** _optional_            | HeapAlloc is bytes of allocated heap objects. Allocated heap objects include all reachable objects, as well as unreachable objects that the garbage collector has not yet freed. Specifically, HeapAlloc increases as heap objects are allocated and decreases as the heap is swept and unreachable objects are freed. Sweeping occurs incrementally between GC cycles, so these two processes occur simultaneously, and as a result HeapAlloc tends to change smoothly (in contrast with the sawtooth that is typical of stop-the-world garbage collectors).                 | Integer       |
| **go\_memstats\_heapidle** _optional_             | HeapIdle is bytes in idle (unused) spans. Idle spans have no objects in them. These spans could be (and may already have been) returned to the OS, or they can be reused for heap allocations, or they can be reused as stack memory. HeapIdle minus HeapReleased estimates the amount of memory that could be returned to the OS, but is being retained by the runtime so it can grow the heap without requesting more memory from the OS. If this difference is significantly larger than the heap size, it indicates there was a recent transient spike in live heap size. | Integer       |
| **go\_memstats\_heapinuse** _optional_            | HeapInuse is bytes in in-use spans. In-use spans have at least one object in them. These spans an only be used for other objects of roughly the same size. HeapInuse minus HeapAlloc estimates the amount of memory that has been dedicated to particular size classes, but is not currently being used. This is an upper bound on fragmentation, but in general this memory can be reused efficiently.                                                                                                                                                                       | Integer       |
| **go\_memstats\_heapreleased** _optional_         | HeapReleased is bytes of physical memory returned to the OS. This counts heap memory from idle spans that was returned to the OS and has not yet been reacquired for the heap.                                                                                                                                                                                                                                                                                                                                                                                                | Integer       |
| **go\_memstats\_pausetotalns** _optional_         | PauseTotalNs is the cumulative nanoseconds in GC stop-the-world pauses since the program started. During a stop-the-world pause, all goroutines are paused and only the garbage collector can run.                                                                                                                                                                                                                                                                                                                                                                            | Integer       |
| **go\_memstats\_stackinuse** _optional_           | StackInuse is bytes in stack spans. In-use stack spans have at least one stack in them. These spans can only be used for other stacks of the same size. There is no StackIdle because unused stack spans are returned to the heap (and hence counted toward HeapIdle).                                                                                                                                                                                                                                                                                                        | Integer       |
| **go\_memstats\_stacksys** _optional_             | StackSys is bytes of stack memory obtained from the OS. StackSys is StackInuse, plus any memory obtained directly from the OS for OS thread stacks (which should be minimal).                                                                                                                                                                                                                                                                                                                                                                                                 | Integer       |
| **go\_memstats\_sys** _optional_                  | Sys is the total bytes of memory obtained from the OS. Sys is the sum of the XSys fields below. Sys measures the virtual address space reserved by the Go runtime for the heap, stacks, and other internal data structures. It's likely that not all of the virtual address space is backed by physical memory at any given moment, though in general it all was at some point.                                                                                                                                                                                               | Integer       |
| **goroutines\_high\_watermark** _optional_        | Peak number of go routines since process start.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Integer       |
| **num\_goroutines** _optional_                    | The total number of goroutines.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Integer       |
| **num\_idle\_kv\_ops** _optional_                 | The total number of idle kv operations.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Integer       |
| **process\_cpu\_percent\_utilization** _optional_ | The CPU utilization as percentage value \* 10\. The extra 10 multiplier is a mistake left for backwards compatibility. Please consider using node\_cpu\_percent\_utilization as of version 3.2\. The CPU usage calculation is performed based on user and system CPU time, but it does not include components such as iowait. The derivation means that the values of process\_cpu\_percent\_utilization and %Cpu, returned when running the top command, will differ.                                                                                                        | Float (float) |
| **node\_cpu\_percent\_utilization** _optional_    | The node CPU utilization as percentage value, since the last time this stat was called. The CPU usage calculation is performed based on user and system CPU time, but it does not include components such as iowait.                                                                                                                                                                                                                                                                                                                                                          | Float (float) |
| **process\_memory\_resident** _optional_          | The memory utilization (Resident Set Size) for the process, in bytes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Integer       |
| **pub\_net\_bytes\_recv** _optional_              | The total number of bytes received (since node start-up) on the network interface to which the Sync Gateway api.public\_interface is bound. By default, that is the number of bytes received on 127.0.0.1:4984 since node start-up                                                                                                                                                                                                                                                                                                                                            | Integer       |
| **pub\_net\_bytes\_sent** _optional_              | The total number of bytes sent (since node start-up) on the network interface to which Sync Gateway api.public\_interface is bound. By default, that is the number of bytes sent on 127.0.0.1:4984 since node start-up.                                                                                                                                                                                                                                                                                                                                                       | Integer       |
| **system\_memory\_total** _optional_              | The total memory available on the system in bytes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Integer       |
| **warn\_count** _optional_                        | The total number of warnings logged.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Integer       |
| **uptime** _optional_                             | The total uptime.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Integer       |

### [](#get%5F%5Fexpvar%5F200%5Fresponse%5Fsyncgateway%5Fper%5Fdb%5Finner)GetExpvar200ResponseSyncgatewayPerDbInner

 Object

| Property                        |  | Schema |
| ------------------------------- |  | ------ |
| **cache** _optional_            |  | Object |
| **database** _optional_         |  | Object |
| **per\_replication** _optional_ |  | Object |
| **collections** _optional_      |  | Object |
| **security** _optional_         |  | Object |

### [](#get%5F%5Fexpvar%5F200%5Fresponse%5Fsyncgateway%5Fper%5Freplication%5Finner)GetExpvar200ResponseSyncgatewayPerReplicationInner

 Object

| Property                        |  | Schema                                                                                                                                                               |
| ------------------------------- |  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **$replication\_id** _optional_ |  | [GetExpvar200ResponseSyncgatewayPerReplicationInnerReplicationId](#get%5F%5Fexpvar%5F200%5Fresponse%5Fsyncgateway%5Fper%5Freplication%5Finner%5F%5Freplication%5Fid) |

### [](#get%5F%5Fexpvar%5F200%5Fresponse%5Fsyncgateway%5Fper%5Freplication%5Finner%5F%5Freplication%5Fid)GetExpvar200ResponseSyncgatewayPerReplicationInnerReplicationId

 Object

| Property                                                |                                                                                                                                                                                                                                                                                                                     | Schema  |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **sgr\_active** _optional_                              | Whether the replication is active at this time. **Deprecated @ 2.8**: used only by inter-sync-gateway replications version 1.                                                                                                                                                                                       | Boolean |
| **sgr\_docs\_checked\_sent** _optional_                 | The total number of documents checked for changes since replication started. This represents the number of potential change notifications pushed by Sync Gateway. **Constraints**This is not necessarily the number of documents pushed, as a given target might already have the change. Used by versions 1 and 2. | Integer |
| **sgr\_num\_attachments\_transferred** _optional_       | The total number of attachments transferred since replication started. **Deprecated @ 2.8**: used only by inter-sync-gateway replications version 1.                                                                                                                                                                | Integer |
| **sgr\_num\_attachment\_bytes\_transferred** _optional_ | The total number of attachment bytes transferred since replication started. **Deprecated @ 2.8**: used only by inter-sync-gateway replications version 1.                                                                                                                                                           | Integer |
| **sgr\_num\_docs\_failed\_to\_push** _optional_         | The total number of documents that failed to be pushed since replication started. Used by versions 1 and 2.                                                                                                                                                                                                         | Integer |
| **sgr\_num\_docs\_pushed** _optional_                   | The total number of documents that were pushed since replication started. Used by versions 1 and 2.                                                                                                                                                                                                                 | Integer |

---

###### 

### [](#related-content)Related Content

[](#-2) 

API Topics

* [Public REST API](rest-api.md)
* [Admin REST API](rest-api-admin.md)
* [Metrics REST API](rest-api-metrics.md)

[](#-3) 

Reference

* [Bootstrap](configuration-schema-bootstrap.md)
* [Database](configuration-schema-database.md)
* [Database Security](configuration-schema-db-security.md)
* [Access Control](configuration-schema-access-control.md)
* [Import Filter](configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)

[](#-4) 

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)