[View original HTML](/server/7.6/analytics-rest-config/index.html)

## [](#overview)Overview

The Analytics Configuration REST API is provided by the Analytics service. This API enables you to configure Analytics nodes and clusters.

### Version information

**Version:** 7.6

### Host information

{scheme}://{host}:{port}

The URL scheme, host, and port are as follows.

| Component  | Description                                                                                 |
| ---------- | ------------------------------------------------------------------------------------------- |
| **scheme** | The URL scheme. Use https for secure access. **Values:** http, https                        |
| **host**   | The host name or IP address of a node running the Analytics Service. **Example:** localhost |
| **port**   | The Analytics Service REST port. Use 18095 for secure access. **Values:** 8095, 18095       |

## [](#resources)Resources

This section describes the operations available with this REST API.

[View Node-Specific Parameters](#get%5Fnode)  
[View Service-Level Parameters](#get%5Fservice)  
[Modify Node-Specific Parameters](#put%5Fnode)  
[Modify Service-Level Parameters](#put%5Fservice)

### [](#get%5Fnode)View Node-Specific Parameters

GET /analytics/config/node

#### [](#get%5Fnode-description)Description

Views node-specific parameters, which apply to the node receiving the request.

Produces

* application/json

#### [](#get%5Fnode-responses)Responses

| HTTP Code | Description                                                                                                                                                              | Schema        |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------- |
| 200       | Success. Returns an object listing the configurable node-level parameters and their current values.                                                                      | [Node](#Node) |
| 401       | Unauthorized. The user name or password may be incorrect. Returns an object containing an error message. Refer to [Error Codes](/server/7.6/analytics/error-codes.html). | Object        |

#### [](#get%5Fnode-security)Security

| Type         | Name                                          |
| ------------ | --------------------------------------------- |
| http (basic) | [Analytics Manage](#security-AnalyticsManage) |

#### [](#example-http-request)Example HTTP Request

curl request

```sh
curl -v -u Administrator:password \
     http://localhost:8095/analytics/config/node
```

#### [](#example-http-response)Example HTTP Response

Response 200

```json
{
  "jvmArgs" : null,
  "storageBuffercacheSize" : 325320704,
  "storageMemorycomponentGlobalbudget" : 325320704
}
```

### [](#get%5Fservice)View Service-Level Parameters

GET /analytics/config/service

#### [](#get%5Fservice-description)Description

Views service-level parameters, which apply to all nodes running the Analytics service.

Produces

* application/json

#### [](#get%5Fservice-responses)Responses

| HTTP Code | Description                                                                                                                                                              | Schema              |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------- |
| 200       | Success. Returns an object listing the configurable service-level parameters and their current values.                                                                   | [Service](#Service) |
| 401       | Unauthorized. The user name or password may be incorrect. Returns an object containing an error message. Refer to [Error Codes](/server/7.6/analytics/error-codes.html). | Object              |

#### [](#get%5Fservice-security)Security

| Type         | Name                                          |
| ------------ | --------------------------------------------- |
| http (basic) | [Analytics Manage](#security-AnalyticsManage) |

#### [](#example-http-request-2)Example HTTP Request

curl request

```sh
curl -v -u Administrator:password \
     http://localhost:8095/analytics/config/service
```

#### [](#example-http-response-2)Example HTTP Response

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

### [](#put%5Fnode)Modify Node-Specific Parameters

PUT /analytics/config/node

#### [](#put%5Fnode-description)Description

Views node-specific parameters, which apply to the node receiving the request.

IMPORTANT: For the configuration changes to take effect, you must restart the node using the [Node Restart API](/server/7.6/analytics-rest-admin.html#restart%5Fnode), or restart the Analytics cluster using the [Cluster Restart API](/server/7.6/analytics-rest-admin.html#restart%5Fcluster).

Consumes

* application/json
* application/x-www-form-urlencoded

Produces

* application/json

#### [](#put%5Fnode-parameters)Parameters

By default, the API accepts parameters using the `application/x-www-form-urlencoded` MIME type. You can specify the `application/json` MIME type using the `Content-Type` header of the PUT request.

Body Parameter

| Name             | Description                                                                              | Schema        |
| ---------------- | ---------------------------------------------------------------------------------------- | ------------- |
| **Body**optional | An object specifying one or more of the configurable node-level parameters on this node. | [Node](#Node) |

#### [](#put%5Fnode-responses)Responses

| HTTP Code | Description                                                                                                                                                              | Schema            |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------- |
| 200       | The operation was successful.                                                                                                                                            |                   |
| 400       | Bad request. Unknown parameter or incorrect value.                                                                                                                       | [Errors](#Errors) |
| 401       | Unauthorized. The user name or password may be incorrect. Returns an object containing an error message. Refer to [Error Codes](/server/7.6/analytics/error-codes.html). | Object            |

#### [](#put%5Fnode-security)Security

| Type         | Name                                          |
| ------------ | --------------------------------------------- |
| http (basic) | [Analytics Manage](#security-AnalyticsManage) |

#### [](#example-http-request-3)Example HTTP Request

curl request

```sh
curl -v -u Administrator:password -X PUT \
     -d storageBuffercacheSize=162660352 \
     http://localhost:8095/analytics/config/node
```

### [](#put%5Fservice)Modify Service-Level Parameters

PUT /analytics/config/service

#### [](#put%5Fservice-description)Description

Modifies service-level parameters, which apply to all nodes running the Analytics service.

IMPORTANT: For the configuration changes to take effect, you must restart the Analytics cluster using the [Cluster Restart API](/server/7.6/analytics-rest-admin.html#restart%5Fcluster).

Consumes

* application/json
* application/x-www-form-urlencoded

Produces

* application/json

#### [](#put%5Fservice-parameters)Parameters

By default, the API accepts parameters using the `application/x-www-form-urlencoded` MIME type. You can specify the `application/json` MIME type using the `Content-Type` header of the PUT request.

Body Parameter

| Name             | Description                                                                    | Schema              |
| ---------------- | ------------------------------------------------------------------------------ | ------------------- |
| **Body**optional | An object specifying one or more of the configurable service-level parameters. | [Service](#Service) |

#### [](#put%5Fservice-responses)Responses

| HTTP Code | Description                                                                                                                                                              | Schema            |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------- |
| 200       | The operation was successful.                                                                                                                                            |                   |
| 400       | Bad request. Unknown parameter or incorrect value.                                                                                                                       | [Errors](#Errors) |
| 401       | Unauthorized. The user name or password may be incorrect. Returns an object containing an error message. Refer to [Error Codes](/server/7.6/analytics/error-codes.html). | Object            |

#### [](#put%5Fservice-security)Security

| Type         | Name                                          |
| ------------ | --------------------------------------------- |
| http (basic) | [Analytics Manage](#security-AnalyticsManage) |

#### [](#example-http-request-4)Example HTTP Request

curl request

```sh
curl -v -u Administrator:password -X PUT \
     -d jobHistorySize=5 \
     http://localhost:8095/analytics/config/service
```

## [](#models)Definitions

This section describes the properties consumed and returned by this REST API.

[Errors](#Errors)  
[Node](#Node)  
[Service](#Service)

### [](#Errors)Errors

 Object

| Property          |                   | Schema |
| ----------------- | ----------------- | ------ |
| **error**required | An error message. | String |

### [](#Node)Node

 Object

| Property                                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Schema  |
| ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **jvmArgs**optional                            | JVM arguments to pass to the Analytics Driver. The default is undefined (null). Node-specific JVM arguments are appended to service-level JVM arguments. If the same JVM argument appears in both the service-level arguments and the node-specific arguments, the node-specific argument takes priority. Note that JVM arguments are generally not secure, and are exposed by [cbcollect\_info](/server/7.6/cli/cbcollect-info-tool.html) and the [System Event](/server/7.6/learn/clusters-and-availability/system-events.html) log. To pass arguments opaquely, you may use [Java command-line argument files](https://docs.oracle.com/en/java/javase/11/tools/java.html#GUID-4856361B-8BFD-4964-AE84-121F5F6CF111). **Nullable:** yes | String  |
| **storageBuffercacheSize**optional             | The size of memory allocated to the disk buffer cache. The value should be a multiple of the buffer cache page size. The default is 1/4 of the allocated Analytics Service memory.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Integer |
| **storageMemorycomponentGlobalbudget**optional | The size of memory allocated to the memory components. The value should be a multiple of the memory component page size. The default is 1/4 of the allocated Analytics Service memory.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Integer |

### [](#Service)Service

 Object

| Property                                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Schema          |
| --------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| **activeMemoryGlobalBudget**optional                | The memory budget (in bytes) for the active runtime. **Default:** 67108864                                                                                                                                                                                                                                                                                                                                                                                                                                      | Integer (int32) |
| **activeStopTimeout**optional                       | The maximum time (in seconds) to wait for a graceful stop of an active runtime. **Default:** 3600                                                                                                                                                                                                                                                                                                                                                                                                               | Integer (int32) |
| **activeSuspendTimeout**optional                    | The maximum time (in seconds) to wait for a graceful suspend of an active runtime. **Default:** 3600                                                                                                                                                                                                                                                                                                                                                                                                            | Integer (int32) |
| **analyticsBroadcastDcpStateMutationCount**optional | The number of processed mutations after which the DCP state is broadcast to storage **Default:** 10000                                                                                                                                                                                                                                                                                                                                                                                                          | Integer (int32) |
| **analyticsHttpRequestQueueSize**optional           | The maximum number of HTTP requests to queue pending ability to execute. **Default:** 256                                                                                                                                                                                                                                                                                                                                                                                                                       | Integer (int32) |
| **analyticsHttpThreadCount**optional                | The number of threads to service HTTP requests. **Default:** 16                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Integer (int32) |
| **bindAddress**optional                             | The bind address to use. **Nullable:** yes                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | String          |
| **bindToHost**optional                              | Bind to configured hostname instead of wildcard address. **Default:** false                                                                                                                                                                                                                                                                                                                                                                                                                                     | Boolean         |
| **clusterConnectRetries**optional                   | Number of attempts to contact CC before giving up. **Default:** 5                                                                                                                                                                                                                                                                                                                                                                                                                                               | Integer (int32) |
| **collectDcpStateFromNodesTimeout**optional         | The maximum time to wait to collect DCP state from all nodes in seconds. **Default:** 600                                                                                                                                                                                                                                                                                                                                                                                                                       | Integer (int32) |
| **compilerFramesize**optional                       | The page size (in bytes) for computation. **Default:** 32768                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Integer (int32) |
| **compilerGroupmemory**optional                     | The memory budget (in bytes) for a group by operator instance in a partition. **Default:** 33554432                                                                                                                                                                                                                                                                                                                                                                                                             | Integer (int32) |
| **compilerJoinmemory**optional                      | The memory budget (in bytes) for a join operator instance in a partition. **Default:** 33554432                                                                                                                                                                                                                                                                                                                                                                                                                 | Integer (int32) |
| **compilerParallelism**optional                     | The degree of parallelism for query execution. Zero means to use the storage parallelism as the query execution parallelism, while other integer values dictate the number of query execution parallel partitions. The system will fall back to use the number of all available CPU cores in the cluster as the degree of parallelism if the number set by a user is too large or too small. **Default:** 0                                                                                                     | Integer (int32) |
| **compilerSortParallel**optional                    | Enables or disables full parallel sort. **Default:** false                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Boolean         |
| **compilerSortmemory**optional                      | The memory budget (in bytes) for a sort operator instance in a partition. **Default:** 33554432                                                                                                                                                                                                                                                                                                                                                                                                                 | Integer (int32) |
| **compilerWindowmemory**optional                    | The memory budget (in bytes) for a window operator instance in a partition. **Default:** 33554432                                                                                                                                                                                                                                                                                                                                                                                                               | Integer (int32) |
| **coresMultiplier**optional                         | The factor to multiply by the number of cores to determine maximum query concurrent execution level. **Default:** 3                                                                                                                                                                                                                                                                                                                                                                                             | Integer (int32) |
| **dcpBufferAckWatermark**optional                   | The percentage of DCP connection buffer size at which to acknowledge bytes consumed to DCP producer. **Default:** 20 **Minimum:** 1 **Maximum:** 100                                                                                                                                                                                                                                                                                                                                                            | Integer (int32) |
| **dcpChannelReconnectRemoteIdleSeconds**optional    | Reconnect remote DCP channels that are idle for the specified number of seconds to ensure permissions have not been lost. A value of 0 disables reconnects on idle. **Default:** 120                                                                                                                                                                                                                                                                                                                            | Integer (int32) |
| **dcpConnectionBufferSize**optional                 | DCP connection buffer size (in bytes). If the JVM maximum heap size is less than 8GB, the default for this parameter is 10 MB divided by the number of IO Devices on the node. Otherwise, the default is 1% of the JVM maximum heap size divided by the number of IO Devices on the node.                                                                                                                                                                                                                       | Integer (int32) |
| **deadlockWatchdogHaltDelaySeconds**optional        | The delay (in seconds) to wait for graceful shutdown due to deadlocked threads, before halting. **Default:** 120                                                                                                                                                                                                                                                                                                                                                                                                | Integer (int32) |
| **deadlockWatchdogPollSeconds**optional             | The frequency (in seconds) to scan for deadlocked threads. **Default:** 300                                                                                                                                                                                                                                                                                                                                                                                                                                     | Integer (int32) |
| **jobHistorySize**optional                          | Limits the number of historical jobs remembered by the system to the specified value. **Default:** 10                                                                                                                                                                                                                                                                                                                                                                                                           | Integer (int32) |
| **jobQueueCapacity**optional                        | The maximum number of jobs to queue before rejecting new jobs. **Default:** 4096                                                                                                                                                                                                                                                                                                                                                                                                                                | Integer (int32) |
| **jvmArgs**optional                                 | JVM arguments to pass to the Analytics Driver. The default is undefined (null). Note that JVM arguments are generally not secure, and are exposed by [cbcollect\_info](/server/7.6/cli/cbcollect-info-tool.html) and the [System Event](/server/7.6/learn/clusters-and-availability/system-events.html) log. To pass arguments opaquely, you may use [Java command-line argument files](https://docs.oracle.com/en/java/javase/11/tools/java.html#GUID-4856361B-8BFD-4964-AE84-121F5F6CF111). **Nullable:** yes | String          |
| **logLevel**optional                                | The logging level. **Default:** "DEBUG"                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | String          |
| **maxWebRequestSize**optional                       | The maximum accepted web request size in bytes. **Default:** 52428800                                                                                                                                                                                                                                                                                                                                                                                                                                           | Integer (int32) |
| **netBufferCount**optional                          | Number of network buffers per input/output channel. **Default:** 1                                                                                                                                                                                                                                                                                                                                                                                                                                              | Integer (int32) |
| **netThreadCount**optional                          | Number of threads to use for Network I/O. **Default:** 1                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Integer (int32) |
| **rebalancePullDatasetSizeFrequency**optional       | The frequency at which the Analytics collection size is pulled from nodes during rebalance in seconds. **Default:** 5                                                                                                                                                                                                                                                                                                                                                                                           | Integer (int32) |
| **remoteLinkConnectTimeoutSeconds**optional         | The maximum time (in seconds) to wait for a remote link connection to establish. A value of 0 disables timeout; a value of -1 sets timeout to the system default. **Default:** 60                                                                                                                                                                                                                                                                                                                               | Integer (int32) |
| **remoteLinkSocketTimeoutSeconds**optional          | The maximum time (in seconds) to wait after establishing the connection for remote links; the maximum time of inactivity between two data packets. A value of 0 disables timeout; a value of -1 sets timeout to the system default. **Default:** 60                                                                                                                                                                                                                                                             | Integer (int32) |
| **requestsArchiveSize**optional                     | The maximum number of archived requests to maintain. **Default:** 50                                                                                                                                                                                                                                                                                                                                                                                                                                            | Integer (int32) |
| **resultSweepThreshold**optional                    | The duration within which an instance of the result cleanup should be invoked in milliseconds. **Default:** 60000                                                                                                                                                                                                                                                                                                                                                                                               | Integer (int32) |
| **resultTtl**optional                               | Limits the amount of time results for asynchronous jobs should be retained by the system in milliseconds. **Default:** 86400000                                                                                                                                                                                                                                                                                                                                                                                 | Integer (int32) |
| **storageBuffercacheMaxopenfiles**optional          | The maximum number of open files in the buffer cache. **Default:** 2147483647                                                                                                                                                                                                                                                                                                                                                                                                                                   | Integer (int32) |
| **storageBuffercachePagesize**optional              | The page size in bytes for pages in the buffer cache. **Default:** 131072                                                                                                                                                                                                                                                                                                                                                                                                                                       | Integer (int32) |
| **storageCompressionBlock**optional                 | The default compression scheme for the storage. **Default:** "snappy"                                                                                                                                                                                                                                                                                                                                                                                                                                           | String          |
| **storageMemorycomponentNumcomponents**optional     | The number of memory components to be used per LSM index. **Default:** 2                                                                                                                                                                                                                                                                                                                                                                                                                                        | Integer (int32) |
| **storageMemorycomponentPagesize**optional          | The page size in bytes for pages allocated to memory components. **Default:** 131072                                                                                                                                                                                                                                                                                                                                                                                                                            | Integer (int32) |
| **storageWriteRateLimit**optional                   | The maximum disk write rate for each storage partition in bytes per second. Disabled if the provided value is less than or equal to 0. **Default:** 0                                                                                                                                                                                                                                                                                                                                                           | Long (int64)    |
| **threaddumpFrequencySeconds**optional              | The frequency (in seconds) at which to log diagnostic thread dumps. **Default:** 300                                                                                                                                                                                                                                                                                                                                                                                                                            | Integer (int32) |
| **threaddumpLogLevel**optional                      | The log level at which to emit diagnostic thread dumps. **Default:** "DEBUG"                                                                                                                                                                                                                                                                                                                                                                                                                                    | String          |
| **traceCategories**optional                         | Categories for tracing. The default is the empty array — no categories. **Default:** \[\]                                                                                                                                                                                                                                                                                                                                                                                                                       | String array    |
| **txnDatasetCheckpointInterval**optional            | The interval (in seconds) after which an Analytics collection is considered idle and persisted to disk. **Default:** 3600                                                                                                                                                                                                                                                                                                                                                                                       | Integer (int32) |

## [](#security)Security

The Analytics Configuration REST API supports HTTP basic authentication. Pass your credentials through HTTP headers.

### [](#security-AnalyticsManage)Analytics Manage

Users must have one of the following RBAC roles:

* Full Admin
* Cluster Admin
* Analytics Admin

**Type:** http

For more information, see [Roles](../learn/security/roles.md).