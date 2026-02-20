---
title: Analytics Configuration REST API
description: A description of the Configuration REST API for Couchbase Analytics.
editUrl: https://github.com/couchbase/docs-analytics/edit/release/7.2/modules/analytics/pages/rest-config.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:analytics:rest-config.adoc[]
---

[View original HTML](/server/7.2/analytics/rest-config.html)

# Analytics Configuration REST API

## [](#%5Foverview)Overview

The Analytics Configuration REST API is provided by the Analytics service. This API enables you to configure Analytics nodes and clusters.

The API schemes and host URLs are as follows:

* <http://node:8095/>
* <https://node:18095/> (for secure access)

where `node` is the host name or IP address of a node running the Analytics service.

### [](#version-information)Version information

_Version_ : 7.2

### [](#consumes)Consumes

* `application/x-www-form-urlencoded`
* `application/json`

### [](#produces)Produces

* `application/json`

## [](#%5Fpaths)Paths

This section describes the operations available with this REST API.

* [View Service-Level Parameters](#%5Fget%5Fservice)
* [Modify Service-Level Parameters](#%5Fput%5Fservice)
* [View Node-Specific Parameters](#%5Fget%5Fnode)
* [Modify Node-Specific Parameters](#%5Fput%5Fnode)

### [](#%5Fget%5Fservice)View Service-Level Parameters

GET /analytics/config/service

#### [](#description)Description

Views service-level parameters, which apply to all nodes running the Analytics service.

#### [](#responses)Responses

| HTTP Code | Description                                                                                                                                        | Schema                 |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| **200**   | Success. Returns an object listing the configurable service-level parameters and their current values.                                             | [Service](#%5Fservice) |
| **401**   | Unauthorized. The user name or password may be incorrect. Returns an object containing an error message. Refer to [Error Codes](error-codes.html). | object                 |

#### [](#security)Security

| Type      | Name                                           |
| --------- | ---------------------------------------------- |
| **basic** | **[Analytics Manage](#%5Fanalytics%5Fmanage)** |

#### [](#example-http-request)Example HTTP request

Curl request

```sh
curl -v -u Administrator:password \
     http://localhost:8095/analytics/config/service
```

#### [](#example-http-response)Example HTTP response

Response 200

```json
{
  "activeMemoryGlobalBudget" : 67108864,
  "activeStopTimeout" : 3600,
  "activeSuspendTimeout" : 3600,
  "analyticsBroadcastDcpStateMutationCount" : 10000,
  "analyticsHttpRequestQueueSize" : 256,
  "analyticsHttpThreadCount" : 16,
  "bindAddress" : null,
  "bindToHost" : false,
  "clusterConnectRetries" : 5,
  "collectDcpStateFromNodesTimeout" : 600,
  "compilerFramesize" : 32768,
  "compilerGroupmemory" : 33554432,
  "compilerJoinmemory" : 33554432,
  "compilerParallelism" : 0,
  "compilerSortParallel" : false,
  "compilerSortmemory" : 33554432,
  "compilerWindowmemory" : 33554432,
  "coresMultiplier" : 3,
  "dcpBufferAckWatermark" : 20,
  "dcpChannelReconnectRemoteIdleSeconds" : 120,
  "dcpConnectionBufferSize" : 10485760,
  "deadlockWatchdogHaltDelaySeconds" : 120,
  "deadlockWatchdogPollSeconds" : 300,
  "jobHistorySize" : 10,
  "jobQueueCapacity" : 4096,
  "jvmArgs" : null,
  "logLevel" : "DEBUG",
  "maxWebRequestSize" : 209715200,
  "netBufferCount" : 1,
  "netThreadCount" : 1,
  "rebalancePullDatasetSizeFrequency" : 5,
  "remoteLinkConnectTimeoutSeconds" : 60,
  "remoteLinkSocketTimeoutSeconds" : 60,
  "requestsArchiveSize" : 50,
  "resultSweepThreshold" : 60000,
  "resultTtl" : 86400000,
  "storageBuffercacheMaxopenfiles" : 2147483647,
  "storageBuffercachePagesize" : 131072,
  "storageCompressionBlock" : "snappy",
  "storageMemorycomponentNumcomponents" : 2,
  "storageMemorycomponentPagesize" : 131072,
  "storageWriteRateLimit" : 0,
  "threaddumpFrequencySeconds" : 300,
  "threaddumpLogLevel" : "DEBUG",
  "traceCategories" : [ ],
  "txnDatasetCheckpointInterval" : 3600
}
```

### [](#%5Fput%5Fservice)Modify Service-Level Parameters

PUT /analytics/config/service

#### [](#description-2)Description

Modifies service-level parameters, which apply to all nodes running the Analytics service.

> [!IMPORTANT]
> For the configuration changes to take effect, you must restart the Analytics cluster using the [Cluster Restart API](rest-admin.html#%5Frestart%5Fcluster).

#### [](#parameters)Parameters

By default, the API accepts parameters using the `application/x-www-form-urlencoded` MIME type. You can specify the `application/json` MIME type using the `Content-Type` header of the PUT request.

| Type     | Name                   | Description                                                                    | Schema                 |
| -------- | ---------------------- | ------------------------------------------------------------------------------ | ---------------------- |
| **Body** | **Service** _optional_ | An object specifying one or more of the configurable service-level parameters. | [Service](#%5Fservice) |

#### [](#responses-2)Responses

| HTTP Code | Description                                                                                                                                        | Schema               |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| **200**   | The operation was successful.                                                                                                                      | No Content           |
| **400**   | Bad request. Unknown parameter or incorrect value.                                                                                                 | [Errors](#%5Ferrors) |
| **401**   | Unauthorized. The user name or password may be incorrect. Returns an object containing an error message. Refer to [Error Codes](error-codes.html). | object               |

#### [](#security-2)Security

| Type      | Name                                           |
| --------- | ---------------------------------------------- |
| **basic** | **[Analytics Manage](#%5Fanalytics%5Fmanage)** |

#### [](#example-http-request-2)Example HTTP request

Curl request

```sh
curl -v -u Administrator:password -X PUT \
     -d jobHistorySize=5 \
     http://localhost:8095/analytics/config/service
```

### [](#%5Fget%5Fnode)View Node-Specific Parameters

GET /analytics/config/node

#### [](#description-3)Description

Views node-specific parameters, which apply to the node receiving the request.

#### [](#responses-3)Responses

| HTTP Code | Description                                                                                                                                        | Schema           |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| **200**   | Success. Returns an object listing the configurable node-level parameters and their current values.                                                | [Node](#%5Fnode) |
| **401**   | Unauthorized. The user name or password may be incorrect. Returns an object containing an error message. Refer to [Error Codes](error-codes.html). | object           |

#### [](#security-3)Security

| Type      | Name                                           |
| --------- | ---------------------------------------------- |
| **basic** | **[Analytics Manage](#%5Fanalytics%5Fmanage)** |

#### [](#example-http-request-3)Example HTTP request

Curl request

```sh
curl -v -u Administrator:password \
     http://localhost:8095/analytics/config/node
```

#### [](#example-http-response-2)Example HTTP response

Response 200

```json
{
  "jvmArgs" : null,
  "storageBuffercacheSize" : 325320704,
  "storageMemorycomponentGlobalbudget" : 325320704
}
```

### [](#%5Fput%5Fnode)Modify Node-Specific Parameters

PUT /analytics/config/node

#### [](#description-4)Description

Views node-specific parameters, which apply to the node receiving the request.

> [!IMPORTANT]
> For the configuration changes to take effect, you must restart the node using the [Node Restart API](rest-admin.html#%5Frestart%5Fnode), or restart the Analytics cluster using the [Cluster Restart API](rest-admin.html#%5Frestart%5Fcluster).

#### [](#parameters-2)Parameters

By default, the API accepts parameters using the `application/x-www-form-urlencoded` MIME type. You can specify the `application/json` MIME type using the `Content-Type` header of the PUT request.

| Type     | Name                | Description                                                                              | Schema           |
| -------- | ------------------- | ---------------------------------------------------------------------------------------- | ---------------- |
| **Body** | **Node** _optional_ | An object specifying one or more of the configurable node-level parameters on this node. | [Node](#%5Fnode) |

#### [](#responses-4)Responses

| HTTP Code | Description                                                                                                                                        | Schema               |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| **200**   | The operation was successful.                                                                                                                      | No Content           |
| **400**   | Bad request. Unknown parameter or incorrect value.                                                                                                 | [Errors](#%5Ferrors) |
| **401**   | Unauthorized. The user name or password may be incorrect. Returns an object containing an error message. Refer to [Error Codes](error-codes.html). | object               |

#### [](#security-4)Security

| Type      | Name                                           |
| --------- | ---------------------------------------------- |
| **basic** | **[Analytics Manage](#%5Fanalytics%5Fmanage)** |

#### [](#example-http-request-4)Example HTTP request

Curl request

```sh
curl -v -u Administrator:password -X PUT \
     -d storageBuffercacheSize=162660352 \
     http://localhost:8095/analytics/config/node
```

## [](#%5Fdefinitions)Definitions

This section describes the properties consumed and returned by this REST API.

* [Service](#%5Fservice)
* [Node](#%5Fnode)

### [](#%5Fservice)Service

| Name                                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Schema           |
| ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| **activeMemoryGlobalBudget** _optional_                | The memory budget (in bytes) for the active runtime. **Default** : 67108864                                                                                                                                                                                                                                                                                                                                                                                                 | integer (int32)  |
| **activeStopTimeout** _optional_                       | The maximum time (in seconds) to wait for a graceful stop of an active runtime. **Default** : 3600                                                                                                                                                                                                                                                                                                                                                                          | integer (int32)  |
| **activeSuspendTimeout** _optional_                    | The maximum time (in seconds) to wait for a graceful suspend of an active runtime. **Default** : 3600                                                                                                                                                                                                                                                                                                                                                                       | integer (int32)  |
| **analyticsBroadcastDcpStateMutationCount** _optional_ | The number of processed mutations after which the DCP state is broadcast to storage **Default** : 10000                                                                                                                                                                                                                                                                                                                                                                     | integer (int32)  |
| **analyticsHttpRequestQueueSize** _optional_           | The maximum number of HTTP requests to queue pending ability to execute. **Default** : 256                                                                                                                                                                                                                                                                                                                                                                                  | integer (int32)  |
| **analyticsHttpThreadCount** _optional_                | The number of threads to service HTTP requests. **Default** : 16                                                                                                                                                                                                                                                                                                                                                                                                            | integer (int32)  |
| **bindAddress** _optional_                             | The bind address to use.                                                                                                                                                                                                                                                                                                                                                                                                                                                    | string           |
| **bindToHost** _optional_                              | Bind to configured hostname instead of wildcard address. **Default** : false                                                                                                                                                                                                                                                                                                                                                                                                | boolean          |
| **clusterConnectRetries** _optional_                   | Number of attempts to contact CC before giving up. **Default** : 5                                                                                                                                                                                                                                                                                                                                                                                                          | integer (int32)  |
| **collectDcpStateFromNodesTimeout** _optional_         | The maximum time to wait to collect DCP state from all nodes in seconds. **Default** : 600                                                                                                                                                                                                                                                                                                                                                                                  | integer (int32)  |
| **compilerFramesize** _optional_                       | The page size (in bytes) for computation. **Default** : 32768                                                                                                                                                                                                                                                                                                                                                                                                               | integer (int32)  |
| **compilerGroupmemory** _optional_                     | The memory budget (in bytes) for a group by operator instance in a partition. **Default** : 33554432                                                                                                                                                                                                                                                                                                                                                                        | integer (int32)  |
| **compilerJoinmemory** _optional_                      | The memory budget (in bytes) for a join operator instance in a partition. **Default** : 33554432                                                                                                                                                                                                                                                                                                                                                                            | integer (int32)  |
| **compilerParallelism** _optional_                     | The degree of parallelism for query execution. Zero means to use the storage parallelism as the query execution parallelism, while other integer values dictate the number of query execution parallel partitions. The system will fall back to use the number of all available CPU cores in the cluster as the degree of parallelism if the number set by a user is too large or too small. **Default** : 0                                                                | integer (int32)  |
| **compilerSortParallel** _optional_                    | Enables or disables full parallel sort. **Default** : false                                                                                                                                                                                                                                                                                                                                                                                                                 | boolean          |
| **compilerSortmemory** _optional_                      | The memory budget (in bytes) for a sort operator instance in a partition. **Default** : 33554432                                                                                                                                                                                                                                                                                                                                                                            | integer (int32)  |
| **compilerWindowmemory** _optional_                    | The memory budget (in bytes) for a window operator instance in a partition. **Default** : 33554432                                                                                                                                                                                                                                                                                                                                                                          | integer (int32)  |
| **coresMultiplier** _optional_                         | The factor to multiply by the number of cores to determine maximum query concurrent execution level. **Default** : 3                                                                                                                                                                                                                                                                                                                                                        | integer (int32)  |
| **dcpBufferAckWatermark** _optional_                   | The percentage of DCP connection buffer size at which to acknowledge bytes consumed to DCP producer. **Default** : 20 **Minimum value** : 1 **Maximum value** : 100                                                                                                                                                                                                                                                                                                         | integer (int32)  |
| **dcpChannelReconnectRemoteIdleSeconds** _optional_    | Reconnect remote DCP channels that are idle for the specified number of seconds to ensure permissions have not been lost. A value of 0 disables reconnects on idle. **Default** : 120                                                                                                                                                                                                                                                                                       | integer (int32)  |
| **dcpConnectionBufferSize** _optional_                 | DCP connection buffer size (in bytes). If the JVM maximum heap size is less than 8GB, the default for this parameter is 10 MB divided by the number of IO Devices on the node. Otherwise, the default is 1% of the JVM maximum heap size divided by the number of IO Devices on the node.                                                                                                                                                                                   | integer (int32)  |
| **deadlockWatchdogHaltDelaySeconds** _optional_        | The delay (in seconds) to wait for graceful shutdown due to deadlocked threads, before halting. **Default** : 120                                                                                                                                                                                                                                                                                                                                                           | integer (int32)  |
| **deadlockWatchdogPollSeconds** _optional_             | The frequency (in seconds) to scan for deadlocked threads. **Default** : 300                                                                                                                                                                                                                                                                                                                                                                                                | integer (int32)  |
| **jobHistorySize** _optional_                          | Limits the number of historical jobs remembered by the system to the specified value. **Default** : 10                                                                                                                                                                                                                                                                                                                                                                      | integer (int32)  |
| **jobQueueCapacity** _optional_                        | The maximum number of jobs to queue before rejecting new jobs. **Default** : 4096                                                                                                                                                                                                                                                                                                                                                                                           | integer (int32)  |
| **jvmArgs** _optional_                                 | JVM arguments to pass to the Analytics Driver. The default is undefined (null). Note that JVM arguments are generally not secure, and are exposed by [cbcollect\_info](../cli/cbcollect-info-tool.html) and the [System Event](../learn/clusters-and-availability/system-events.html) log. To pass arguments opaquely, you may use [Java command-line argument files](https://docs.oracle.com/en/java/javase/11/tools/java.html#GUID-4856361B-8BFD-4964-AE84-121F5F6CF111). | string           |
| **logLevel** _optional_                                | The logging level. **Default** : "DEBUG"                                                                                                                                                                                                                                                                                                                                                                                                                                    | string           |
| **maxWebRequestSize** _optional_                       | The maximum accepted web request size in bytes. **Default** : 52428800                                                                                                                                                                                                                                                                                                                                                                                                      | integer (int32)  |
| **netBufferCount** _optional_                          | Number of network buffers per input/output channel. **Default** : 1                                                                                                                                                                                                                                                                                                                                                                                                         | integer (int32)  |
| **netThreadCount** _optional_                          | Number of threads to use for Network I/O. **Default** : 1                                                                                                                                                                                                                                                                                                                                                                                                                   | integer (int32)  |
| **rebalancePullDatasetSizeFrequency** _optional_       | The frequency at which the Analytics collection size is pulled from nodes during rebalance in seconds. **Default** : 5                                                                                                                                                                                                                                                                                                                                                      | integer (int32)  |
| **remoteLinkConnectTimeoutSeconds** _optional_         | The maximum time (in seconds) to wait for a remote link connection to establish. A value of 0 disables timeout; a value of -1 sets timeout to the system default. **Default** : 60                                                                                                                                                                                                                                                                                          | integer (int32)  |
| **remoteLinkSocketTimeoutSeconds** _optional_          | The maximum time (in seconds) to wait after establishing the connection for remote links; the maximum time of inactivity between two data packets. A value of 0 disables timeout; a value of -1 sets timeout to the system default. **Default** : 60                                                                                                                                                                                                                        | integer (int32)  |
| **requestsArchiveSize** _optional_                     | The maximum number of archived requests to maintain. **Default** : 50                                                                                                                                                                                                                                                                                                                                                                                                       | integer (int32)  |
| **resultSweepThreshold** _optional_                    | The duration within which an instance of the result cleanup should be invoked in milliseconds. **Default** : 60000                                                                                                                                                                                                                                                                                                                                                          | integer (int32)  |
| **resultTtl** _optional_                               | Limits the amount of time results for asynchronous jobs should be retained by the system in milliseconds. **Default** : 86400000                                                                                                                                                                                                                                                                                                                                            | integer (int32)  |
| **storageBuffercacheMaxopenfiles** _optional_          | The maximum number of open files in the buffer cache. **Default** : 2147483647                                                                                                                                                                                                                                                                                                                                                                                              | integer (int32)  |
| **storageBuffercachePagesize** _optional_              | The page size in bytes for pages in the buffer cache. **Default** : 131072                                                                                                                                                                                                                                                                                                                                                                                                  | integer (int32)  |
| **storageCompressionBlock** _optional_                 | The default compression scheme for the storage. **Default** : "snappy"                                                                                                                                                                                                                                                                                                                                                                                                      | string           |
| **storageMemorycomponentNumcomponents** _optional_     | The number of memory components to be used per LSM index. **Default** : 2                                                                                                                                                                                                                                                                                                                                                                                                   | integer (int32)  |
| **storageMemorycomponentPagesize** _optional_          | The page size in bytes for pages allocated to memory components. **Default** : 131072                                                                                                                                                                                                                                                                                                                                                                                       | integer (int32)  |
| **storageWriteRateLimit** _optional_                   | The maximum disk write rate for each storage partition in bytes per second. Disabled if the provided value is less than or equal to 0. **Default** : 0                                                                                                                                                                                                                                                                                                                      | integer (int64)  |
| **threaddumpFrequencySeconds** _optional_              | The frequency (in seconds) at which to log diagnostic thread dumps. **Default** : 300                                                                                                                                                                                                                                                                                                                                                                                       | integer (int32)  |
| **threaddumpLogLevel** _optional_                      | The log level at which to emit diagnostic thread dumps. **Default** : "DEBUG"                                                                                                                                                                                                                                                                                                                                                                                               | string           |
| **traceCategories** _optional_                         | Categories for tracing. The default is the empty array — no categories.                                                                                                                                                                                                                                                                                                                                                                                                     | < object > array |
| **txnDatasetCheckpointInterval** _optional_            | The interval (in seconds) after which an Analytics collection is considered idle and persisted to disk. **Default** : 3600                                                                                                                                                                                                                                                                                                                                                  | integer (int32)  |

### [](#%5Fnode)Node

| Name                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Schema  |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **jvmArgs** _optional_                            | JVM arguments to pass to the Analytics Driver. The default is undefined (null). Node-specific JVM arguments are appended to service-level JVM arguments. If the same JVM argument appears in both the service-level arguments and the node-specific arguments, the node-specific argument takes priority. Note that JVM arguments are generally not secure, and are exposed by [cbcollect\_info](../cli/cbcollect-info-tool.html) and the [System Event](../learn/clusters-and-availability/system-events.html) log. To pass arguments opaquely, you may use [Java command-line argument files](https://docs.oracle.com/en/java/javase/11/tools/java.html#GUID-4856361B-8BFD-4964-AE84-121F5F6CF111). | string  |
| **storageBuffercacheSize** _optional_             | The size of memory allocated to the disk buffer cache. The value should be a multiple of the buffer cache page size. The default is 1/4 of the allocated Analytics Service memory.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | integer |
| **storageMemorycomponentGlobalbudget** _optional_ | The size of memory allocated to the memory components. The value should be a multiple of the memory component page size. The default is 1/4 of the allocated Analytics Service memory.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | integer |

### [](#%5Ferrors)Errors

| Name                 | Description       | Schema |
| -------------------- | ----------------- | ------ |
| **error** _required_ | An error message. | string |

## [](#%5Fsecurityscheme)Security

### [](#%5Fanalytics%5Fmanage)Analytics Manage

The Analytics Configuration REST API supports HTTP basic authentication. Credentials can be passed via HTTP headers.

Users must have one of the following RBAC roles:

* Full Admin
* Cluster Admin
* Analytics Admin

Refer to [Roles](../learn/security/roles.html) for more details.

_Type_ : basic