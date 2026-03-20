---
title: Analytics Configuration REST API
description: A description of the Configuration REST API for Couchbase Enterprise Analytics.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/analytics-rest-config/pages/index.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:2.0@enterprise-analytics:analytics-rest-config:index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.0/analytics-rest-config/index.html)

# Analytics Configuration REST API

* getView Service-Level Parameters
* putModify Service-Level Parameters
* getView Node-Specific Parameters
* putModify Node-Specific Parameters

[API docs by Redocly](https://redocly.com/redoc/)

# Enterprise Analytics Configuration REST API (2.0)

Download OpenAPI specification:

This API enables you to configure Enterprise Analytics Service.

## [](#operation/get%5Fservice)View Service-Level Parameters 

Views service-level parameters, which apply to all nodes.

##### Authorizations:

_AnalyticsManage_

### Responses

**200** 

Success. Returns an object listing the configurable service-level parameters and their current values.

**401** 

Unauthorized. The user name or password may be incorrect.

Returns an object containing an error message. Refer to [Error Codes](/server/7.6/analytics/error-codes.html).

get/api/v1/config/service

The URL scheme, host, and port are as follows.

{scheme}://{host}:{port}/api/v1/config/service

### Response samples 

* 200
* 401

Content type

application/json

Copy

`{
* "analyticsHttpRequestQueueSize": 256,
* "analyticsHttpThreadCount": 16,
* "cloudAccessPreemptiveRefreshIntervalSeconds": 15,
* "cloudAccessRefreshHaltTimeoutSeconds": 120,
* "cloudAccessTtlSeconds": 15,
* "cloudMaxReadRequestsPerSecond": 1500,
* "cloudMaxWriteRequestsPerSecond": 250,
* "cloudRequestsHttpConnectionAcquireTimeout": 120,
* "cloudRequestsMaxHttpConnections": 1000,
* "cloudRequestsMaxPendingHttpConnections": 10000,
* "cloudStorageAllocationPercentage": 0.8,
* "cloudStorageDiskMonitorInterval": 120,
* "cloudStorageIndexInactiveDurationThreshold": 360,
* "cloudStorageSweepThresholdPercentage": 0.9,
* "cloudWriteBufferSize": 8388608,
* "compilerCbo": true,
* "compilerColumnFilter": true,
* "compilerCopyToWriteBufferSize": 8388608,
* "compilerExternalFieldPushdown": true,
* "compilerFramesize": 32768,
* "compilerGroupmemory": 33554432,
* "compilerJoinmemory": 33554432,
* "compilerRuntimeMemoryOverhead": 5,
* "compilerSortmemory": 33554432,
* "compilerWindowmemory": 33554432,
* "copyToKvBucketWaitUntilReadyTimeout": 30,
* "coresMultiplier": 3,
* "dcpChannelConnectAttemptTimeout": 120,
* "dcpChannelConnectTotalTimeout": 480,
* "dcpConnectionBufferSize": 1048576,
* "jobQueueCapacity": 4096,
* "jvmArgs": null,
* "kafkaMaxFetchBytes": 4194304,
* "maxRedirectsRemoteLink": 10,
* "maxWebRequestSize": 209715200,
* "rebalanceEjectDelaySeconds": 0,
* "remoteLinkConnectTimeoutSeconds": 30,
* "remoteLinkRefreshAuthSeconds": 0,
* "remoteLinkSocketTimeoutSeconds": 60,
* "remoteLinkValidationMaxRetries": 0,
* "remoteStorageSizeMetricTtlMillis": 300000,
* "requestsArchiveSize": 1000,
* "resultTtl": 86400000,
* "storageFormat": "column",
* "storageMaxConcurrentFlushesPerPartition": 1,
* "storageMaxConcurrentMergesPerPartition": 1,
* "storageMaxScheduledMergesPerPartition": 8,
* "storageMemorycomponentMaxScheduledFlushes": 0,
* "txnDatasetCheckpointInterval": 3600
}`

## [](#operation/put%5Fservice)Modify Service-Level Parameters 

Modifies service-level parameters, which apply to all nodes.

IMPORTANT: For the configuration changes to take effect, you must restart the Enterprise Analytics Service using the [Service Restart API](/server/7.6/analytics-rest-admin.html#restart%5Fcluster).

##### Authorizations:

_AnalyticsManage_

##### Request Body schema: 

application/jsonapplication/x-www-form-urlencodedapplication/json

An object specifying one or more of the configurable service-level parameters.

| analyticsHttpRequestQueueSize               | integer <int32\> Default: 256 The maximum number of HTTP requests to queue pending ability to execute.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| analyticsHttpThreadCount                    | integer <int32\> Default: 16 The number of threads to service HTTP requests.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| cloudAccessPreemptiveRefreshIntervalSeconds | integer <int32\> Default: 15 The interval at which to attempt to preemptively verify cloud access. If access is confirmed to be revoked, the process will halt. (0 == no preemptive refresh)                                                                                                                                                                                                                                                                                                                               |
| cloudAccessRefreshHaltTimeoutSeconds        | integer <int32\> Default: 120 The length of time before we will halt on failure to verify cloud access. (0 == wait forever)                                                                                                                                                                                                                                                                                                                                                                                                |
| cloudAccessTtlSeconds                       | integer <int32\> Default: 15 The length of time allowed to assume we have still have write access to cloud resources                                                                                                                                                                                                                                                                                                                                                                                                       |
| cloudMaxReadRequestsPerSecond               | integer <int32\> Default: 1500 The maximum number of read requests per second (default 1500, 0 means unlimited)                                                                                                                                                                                                                                                                                                                                                                                                            |
| cloudMaxWriteRequestsPerSecond              | integer <int32\> Default: 250 The maximum number of write requests per second (default 250, 0 means unlimited)                                                                                                                                                                                                                                                                                                                                                                                                             |
| cloudRequestsHttpConnectionAcquireTimeout   | integer <int32\> Default: 120 The waiting time (in seconds) to acquire an HTTP connection before failing the request. (default 120 seconds)                                                                                                                                                                                                                                                                                                                                                                                |
| cloudRequestsMaxHttpConnections             | integer <int32\> Default: 1000 The maximum number of HTTP connections to use concurrently for cloud requests per node. (default 1000)                                                                                                                                                                                                                                                                                                                                                                                      |
| cloudRequestsMaxPendingHttpConnections      | integer <int32\> Default: 10000 The maximum number of HTTP connections allowed to wait for a connection per node. (default 10000)                                                                                                                                                                                                                                                                                                                                                                                          |
| cloudStorageAllocationPercentage            | number <double\> Default: 0.8 The percentage of the total disk space that should be allocated for data storage when the 'selective' caching policy is used. The remaining will act as a buffer for query workspace (i.e., for query operations that require spilling to disk). (default 80% of the total disk space)                                                                                                                                                                                                       |
| cloudStorageDiskMonitorInterval             | integer <int32\> Default: 120 The disk monitoring interval time (in seconds) determines how often the system checks for pressure on disk space when using the 'selective' caching policy. (default 120 seconds)                                                                                                                                                                                                                                                                                                            |
| cloudStorageIndexInactiveDurationThreshold  | integer <int32\> Default: 360 The duration in minutes to consider an index is inactive. (default 360 or 6 hours)                                                                                                                                                                                                                                                                                                                                                                                                           |
| cloudStorageSweepThresholdPercentage        | number <double\> Default: 0.9 The percentage of the used storage space at which the disk sweeper starts freeing space by punching holes in stored indexes or by evicting them entirely, when the 'selective' caching policy is used. (default 90% of the allocated space for storage)                                                                                                                                                                                                                                      |
| cloudWriteBufferSize                        | integer <int32\> Default: 8388608 The write buffer size in bytes. (default 8MB, min 5MB)                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| compilerCbo                                 | boolean Default: true Set the mode for cost based optimization.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| compilerColumnFilter                        | boolean Default: true Enable/disable the use of column min/max filters.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| compilerCopyToWriteBufferSize               | integer <int32\> Default: 8388608 The COPY TO write buffer size in bytes. (default 8MB, min 5MB).                                                                                                                                                                                                                                                                                                                                                                                                                          |
| compilerExternalFieldPushdown               | boolean Default: true Enable pushdown of field accesses to the external data-scan operator.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| compilerFramesize                           | integer <int32\> Default: 32768 The page size (in bytes) for computation.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| compilerGroupmemory                         | integer <int32\> Default: 33554432 The memory budget (in bytes) for a group by operator instance in a partition.                                                                                                                                                                                                                                                                                                                                                                                                           |
| compilerJoinmemory                          | integer <int32\> Default: 33554432 The memory budget (in bytes) for a join operator instance in a partition.                                                                                                                                                                                                                                                                                                                                                                                                               |
| compilerRuntimeMemoryOverhead               | integer <int32\> Default: 5 A percentage of the job's required memory to be added to account for runtime memory overhead.                                                                                                                                                                                                                                                                                                                                                                                                  |
| compilerSortmemory                          | integer <int32\> Default: 33554432 The memory budget (in bytes) for a sort operator instance in a partition.                                                                                                                                                                                                                                                                                                                                                                                                               |
| compilerWindowmemory                        | integer <int32\> Default: 33554432 The memory budget (in bytes) for a window operator instance in a partition.                                                                                                                                                                                                                                                                                                                                                                                                             |
| copyToKvBucketWaitUntilReadyTimeout         | integer <int32\> Default: 30 The number of seconds to wait for COPY TO KV bucket WaitUntilReady before timing out.                                                                                                                                                                                                                                                                                                                                                                                                         |
| coresMultiplier                             | integer <int32\> Default: 3 The factor to multiply by the number of cores to determine maximum query concurrent execution level.                                                                                                                                                                                                                                                                                                                                                                                           |
| dcpChannelConnectAttemptTimeout             | integer <int32\> Default: 120 The maximum attempt time to connect to a DCP channel in seconds.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| dcpChannelConnectTotalTimeout               | integer <int32\> Default: 480 The maximum time to wait to connect to a DCP channel in seconds.                                                                                                                                                                                                                                                                                                                                                                                                                             |
| dcpConnectionBufferSize                     | integer <int32\> Default: 1048576 DCP connection buffer size (in bytes). If the JVM maximum heap size is less than 8GB, the default for this parameter is 10 MB divided by the number of IO Devices on the node. Otherwise, the default is 1% of the JVM maximum heap size divided by the number of IO Devices on the node.                                                                                                                                                                                                |
| jobQueueCapacity                            | integer <int32\> Default: 4096 The maximum number of jobs to queue before rejecting new jobs.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| jvmArgs                                     | string or null Default: null JVM arguments to pass to the Analytics Driver. The default is undefined (null). Note that JVM arguments are generally not secure, and are exposed by [cbcollect\_info](/server/7.6/cli/cbcollect-info-tool.html) and the [System Event](/server/7.6/learn/clusters-and-availability/system-events.html) log. To pass arguments opaquely, you may use [Java command-line argument files](https://docs.oracle.com/en/java/javase/11/tools/java.html#GUID-4856361B-8BFD-4964-AE84-121F5F6CF111). |
| kafkaMaxFetchBytes                          | integer <int32\> Default: 4194304 Maximum number of bytes fetched by a kafka consumer in one request.                                                                                                                                                                                                                                                                                                                                                                                                                      |
| maxRedirectsRemoteLink                      | integer <int32\> Default: 10 The number of redirects to follow when communicating with a remote link cluster via http for remote links not configured to prevent redirects.                                                                                                                                                                                                                                                                                                                                                |
| maxWebRequestSize                           | integer <int64\> Default: 209715200 The maximum accepted web request size in bytes.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| rebalanceEjectDelaySeconds                  | integer <int32\> Default: 0 The delay (in seconds) before a node is ejected from the cluster during rebalance from the time that the health check API on that node will start reporting an error response. This is to allow adequate time for the node to removed from consideration by clients utilizing the health check API, to avoid failures on rebalance out; 0 == means no delay.                                                                                                                                   |
| remoteLinkConnectTimeoutSeconds             | integer <int32\> Default: 30 The maximum time (in seconds) to wait for a remote link connection to establish. A value of 0 disables timeout; a value of -1 sets timeout to the system default.                                                                                                                                                                                                                                                                                                                             |
| remoteLinkRefreshAuthSeconds                | integer <int32\> Default: 0 The frequency at which permissions should be reevaluated for remote buckets/collections that may have been lost/restored for remote cluster versions at 7.0 or later; a value of 0 disables preemptive reevaluation.                                                                                                                                                                                                                                                                           |
| remoteLinkSocketTimeoutSeconds              | integer <int32\> Default: 60 The maximum time (in seconds) to wait after establishing the connection for remote links; the maximum time of inactivity between two data packets. A value of 0 disables timeout; a value of -1 sets timeout to the system default.                                                                                                                                                                                                                                                           |
| remoteLinkValidationMaxRetries              | integer <int32\> Default: 0 The number of times to retry on a remote link credential / config validation connection failure, i.e. on CREATE or ALTER LINK (0 == don't retry).                                                                                                                                                                                                                                                                                                                                              |
| remoteStorageSizeMetricTtlMillis            | integer <int64\> Default: 300000 The length of time after which remote storage size metric is recomputed.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| requestsArchiveSize                         | integer <int32\> Default: 1000 The maximum number of archived requests to maintain.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| resultTtl                                   | integer <int64\> Default: 86400000 Limits the amount of time results for asynchronous jobs should be retained by the system in milliseconds.                                                                                                                                                                                                                                                                                                                                                                               |
| storageFormat                               | string Default: "column" The default storage format (either row or column).                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| storageMaxConcurrentFlushesPerPartition     | integer <int32\> Default: 1 The maximum number of concurrently executed flushes per partition (0 means unlimited).                                                                                                                                                                                                                                                                                                                                                                                                         |
| storageMaxConcurrentMergesPerPartition      | integer <int32\> Default: 1 The maximum number of concurrently executed merges per partition (0 means unlimited).                                                                                                                                                                                                                                                                                                                                                                                                          |
| storageMaxScheduledMergesPerPartition       | integer <int32\> Default: 8 The maximum number of scheduled merges per partition (0 means unlimited).                                                                                                                                                                                                                                                                                                                                                                                                                      |
| storageMemorycomponentMaxScheduledFlushes   | integer <int32\> Default: 0 The maximum number of scheduled flush operations. 0 means that the value will be calculated as the number of partitions.                                                                                                                                                                                                                                                                                                                                                                       |
| txnDatasetCheckpointInterval                | integer <int32\> Default: 3600 The interval (in seconds) after which an Analytics collection is considered idle and persisted to disk.                                                                                                                                                                                                                                                                                                                                                                                     |

### Responses

**200** 

The operation was successful.

**400** 

Bad request. Unknown parameter or incorrect value.

**401** 

Unauthorized. The user name or password may be incorrect.

Returns an object containing an error message. Refer to [Error Codes](/server/7.6/analytics/error-codes.html).

put/api/v1/config/service

The URL scheme, host, and port are as follows.

{scheme}://{host}:{port}/api/v1/config/service

### Request samples 

* Payload

Content type

application/jsonapplication/x-www-form-urlencodedapplication/json

Copy

`{
* "analyticsHttpRequestQueueSize": 256,
* "analyticsHttpThreadCount": 16,
* "cloudAccessPreemptiveRefreshIntervalSeconds": 15,
* "cloudAccessRefreshHaltTimeoutSeconds": 120,
* "cloudAccessTtlSeconds": 15,
* "cloudMaxReadRequestsPerSecond": 1500,
* "cloudMaxWriteRequestsPerSecond": 250,
* "cloudRequestsHttpConnectionAcquireTimeout": 120,
* "cloudRequestsMaxHttpConnections": 1000,
* "cloudRequestsMaxPendingHttpConnections": 10000,
* "cloudStorageAllocationPercentage": 0.8,
* "cloudStorageDiskMonitorInterval": 120,
* "cloudStorageIndexInactiveDurationThreshold": 360,
* "cloudStorageSweepThresholdPercentage": 0.9,
* "cloudWriteBufferSize": 8388608,
* "compilerCbo": true,
* "compilerColumnFilter": true,
* "compilerCopyToWriteBufferSize": 8388608,
* "compilerExternalFieldPushdown": true,
* "compilerFramesize": 32768,
* "compilerGroupmemory": 33554432,
* "compilerJoinmemory": 33554432,
* "compilerRuntimeMemoryOverhead": 5,
* "compilerSortmemory": 33554432,
* "compilerWindowmemory": 33554432,
* "copyToKvBucketWaitUntilReadyTimeout": 30,
* "coresMultiplier": 3,
* "dcpChannelConnectAttemptTimeout": 120,
* "dcpChannelConnectTotalTimeout": 480,
* "dcpConnectionBufferSize": 1048576,
* "jobQueueCapacity": 4096,
* "jvmArgs": null,
* "kafkaMaxFetchBytes": 4194304,
* "maxRedirectsRemoteLink": 10,
* "maxWebRequestSize": 209715200,
* "rebalanceEjectDelaySeconds": 0,
* "remoteLinkConnectTimeoutSeconds": 30,
* "remoteLinkRefreshAuthSeconds": 0,
* "remoteLinkSocketTimeoutSeconds": 60,
* "remoteLinkValidationMaxRetries": 0,
* "remoteStorageSizeMetricTtlMillis": 300000,
* "requestsArchiveSize": 1000,
* "resultTtl": 86400000,
* "storageFormat": "column",
* "storageMaxConcurrentFlushesPerPartition": 1,
* "storageMaxConcurrentMergesPerPartition": 1,
* "storageMaxScheduledMergesPerPartition": 8,
* "storageMemorycomponentMaxScheduledFlushes": 0,
* "txnDatasetCheckpointInterval": 3600
}`

### Response samples 

* 400
* 401

Content type

application/json

Copy

`{
* "error": "string"
}`

## [](#operation/get%5Fnode)View Node-Specific Parameters 

Views node-specific parameters, which apply to the node receiving the request.

##### Authorizations:

_AnalyticsManage_

### Responses

**200** 

Success. Returns an object listing the configurable node-level parameters and their current values.

**401** 

Unauthorized. The user name or password may be incorrect.

Returns an object containing an error message. Refer to [Error Codes](/server/7.6/analytics/error-codes.html).

get/api/v1/config/node

The URL scheme, host, and port are as follows.

{scheme}://{host}:{port}/api/v1/config/node

### Response samples 

* 200
* 401

Content type

application/json

Copy

`{
* "jvmArgs": null,
* "storageBuffercacheSize": 0,
* "storageMemorycomponentGlobalbudget": 0
}`

## [](#operation/put%5Fnode)Modify Node-Specific Parameters 

Views node-specific parameters, which apply to the node receiving the request.

IMPORTANT: For the configuration changes to take effect, you must restart the node using the [Node Restart API](/server/7.6/analytics-rest-admin.html#restart%5Fnode), or restart the Enterprise Analytics Service using the [Service Restart API](/server/7.6/analytics-rest-admin.html#restart%5Fservice).

##### Authorizations:

_AnalyticsManage_

##### Request Body schema: 

application/jsonapplication/x-www-form-urlencodedapplication/json

An object specifying one or more of the configurable node-level parameters on this node.

| jvmArgs                            | string or null Default: null JVM arguments to pass to the Analytics Driver. The default is undefined (null). Node-specific JVM arguments are appended to service-level JVM arguments. If the same JVM argument appears in both the service-level arguments and the node-specific arguments, the node-specific argument takes priority. Note that JVM arguments are generally not secure, and are exposed by \[cbcollect\_info\] and the \[System Event\] log. To pass arguments opaquely, you may use [Java command-line argument files](https://docs.oracle.com/en/java/javase/11/tools/java.html#GUID-4856361B-8BFD-4964-AE84-121F5F6CF111). |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| storageBuffercacheSize             | integer The size of memory allocated to the disk buffer cache. The value should be a multiple of the buffer cache page size. The default is 1/4 of the allocated memory.                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| storageMemorycomponentGlobalbudget | integer The size of memory allocated to the memory components. The value should be a multiple of the memory component page size. The default is 1/4 of the allocated memory.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

### Responses

**200** 

The operation was successful.

**400** 

Bad request. Unknown parameter or incorrect value.

**401** 

Unauthorized. The user name or password may be incorrect.

Returns an object containing an error message. Refer to [Error Codes](/server/7.6/analytics/error-codes.html).

put/api/v1/config/node

The URL scheme, host, and port are as follows.

{scheme}://{host}:{port}/api/v1/config/node

### Request samples 

* Payload

Content type

application/jsonapplication/x-www-form-urlencodedapplication/json

Copy

`{
* "jvmArgs": null,
* "storageBuffercacheSize": 0,
* "storageMemorycomponentGlobalbudget": 0
}`

### Response samples 

* 400
* 401

Content type

application/json

Copy

`{
* "error": "string"
}`