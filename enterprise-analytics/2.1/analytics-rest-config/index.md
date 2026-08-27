---
title: Analytics Configuration REST API
description: A description of the Configuration REST API for Couchbase Enterprise Analytics.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/analytics-rest-config/pages/index.adoc
  xref: xref:2.1@enterprise-analytics:analytics-rest-config:index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.1/analytics-rest-config/index.html)

# Analytics Configuration REST API

* getView Service-Level Parameters
* putModify Service-Level Parameters
* getView Node-Specific Parameters
* putModify Node-Specific Parameters

[API docs by Redocly](https://redocly.com/redoc/)

# Enterprise Analytics Configuration REST API (2.1)

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
* "abortTasksTimeout": 600000,
* "activeMemoryGlobalBudget": "64 MiB",
* "activeStopTimeout": 3600,
* "activeSuspendTimeout": 3600,
* "allowLoopbackRedirectRemoteLink": false,
* "analyticsBroadcastDcpStateMutationCount": 100000,
* "analyticsHttpRequestQueueSize": 256,
* "analyticsHttpThreadCount": 16,
* "authorizationCacheTtlSeconds": 5,
* "authorizationHaltOnLostCredentialsSeconds": 120,
* "awsAssumeRoleAsyncRefreshEnabled": true,
* "awsAssumeRoleDuration": 3600,
* "awsAssumeRolePrefetchTime": 300,
* "awsAssumeRoleStaleTime": 60,
* "azureRequestTimeout": 120,
* "bindAddress": null,
* "bindToHost": false,
* "cloudAccessPreemptiveRefreshIntervalSeconds": 30,
* "cloudAccessRefreshHaltTimeoutSeconds": 300,
* "cloudAccessTtlSeconds": 15,
* "cloudAcquireTokenTimeout": 100,
* "cloudEvictionPlanReevaluateThreshold": 50,
* "cloudMaxReadRequestsPerSecond": 1500,
* "cloudMaxWriteRequestsPerSecond": 250,
* "cloudProfilerLogInterval": 5,
* "cloudRequestsHttpConnectionAcquireTimeout": 120,
* "cloudRequestsHttpConnectionMaxIdleSeconds": 120,
* "cloudRequestsHttpConnectionMaxLifetimeSeconds": 3600,
* "cloudRequestsMaxHttpConnections": 1000,
* "cloudRequestsMaxPendingHttpConnections": 10000,
* "cloudStorageAllocationPercentage": 0.8,
* "cloudStorageCachePolicy": "selective",
* "cloudStorageDiskMonitorInterval": 120,
* "cloudStorageIndexInactiveDurationThreshold": 360,
* "cloudStorageS3ClientReadTimeout": -1,
* "cloudStorageS3ParallelDownloaderClientType": "string",
* "cloudStorageS3UseRoundRobinDnsResolver": false,
* "cloudStorageSweepThresholdPercentage": 0.9,
* "cloudWriteBufferSize": 8388608,
* "clusterConnectRetries": 5,
* "collectDcpStateFromNodesTimeout": 600,
* "compilerArrayindex": true,
* "compilerBatchLookup": true,
* "compilerCbo": true,
* "compilerColumnFilter": true,
* "compilerCopyToWriteBufferSize": 8388608,
* "compilerDisjunctionAsJoin": false,
* "compilerDisjunctionHashThreshold": -1,
* "compilerExtractCommonExpressionLimit": 100,
* "compilerExternalFieldPushdown": true,
* "compilerExternalscanmemory": "8 KiB",
* "compilerFramesize": "32 KiB",
* "compilerGroupmemory": "32 MiB",
* "compilerJoinmemory": "32 MiB",
* "compilerMaxVariableOccurrencesInlining": 128,
* "compilerMinGroupmemory": "512 KiB",
* "compilerMinJoinmemory": "512 KiB",
* "compilerMinSortmemory": "512 KiB",
* "compilerMinWindowmemory": "512 KiB",
* "compilerOptimizeExpressionMaxArgs": 200,
* "compilerOrderedFields": false,
* "compilerParallelism": 0,
* "compilerQueryplanshape": "zigzag",
* "compilerRuntimeMemoryOverhead": 5,
* "compilerSortmemory": "32 MiB",
* "compilerSortParallel": false,
* "compilerWindowmemory": "32 MiB",
* "copyToKvBucketWaitUntilReadyTimeout": 30,
* "coresMultiplier": 3,
* "dcpBufferAckWatermark": 20,
* "dcpChannelConnectAttemptTimeout": 120,
* "dcpChannelConnectTotalTimeout": 480,
* "dcpConnectionBufferSize": 0,
* "dcpForceSnappyCompression": false,
* "dcpIdleQueueFlushThresholdMillis": 100,
* "dcpMaxConnectionsPerKvNode": 128,
* "dcpMinWorkPerKvConnection": 8,
* "dcpNoopInterval": 120,
* "dcpStreamRequestIncludePurgeSeqnos": true,
* "dcpSupportSnappyCompression": true,
* "dcpTargetMaxWorkPerKvConnection": 64,
* "deadlockWatchdogHaltDelaySeconds": 120,
* "deadlockWatchdogPollSeconds": 300,
* "gcpImpersonateServiceAccountDuration": 900,
* "healthCheckStatusCodeEjecting": 503,
* "healthCheckStatusCodeNormal": 204,
* "ingestionMaxBootstrapIntervalSeconds": 480,
* "jobHistorySize": 10,
* "jobQueueCapacity": 4096,
* "jsonMaxDepth": 1000,
* "jsonMaxDocLength": 0,
* "jsonMaxNameLength": 50000,
* "jsonMaxNumberLength": 1000,
* "jsonMaxStringLength": "40 MiB",
* "jsonMaxTokenCount": 0,
* "jvmArgs": null,
* "kafkaMaxFetchBytes": 4194304,
* "maxActiveLinks": 100,
* "maxRedirectsLocal": 0,
* "maxRedirectsRemoteLink": 10,
* "maxWebRequestSize": 209715200,
* "metadataRegistrationTimeoutSecs": 1800,
* "netBufferCount": 1,
* "netThreadCount": 1,
* "nodeDeltaRecovery": true,
* "rebalanceEjectDelaySeconds": 0,
* "remoteLinkConnectTimeoutSeconds": 30,
* "remoteLinkRefreshAuthSeconds": 0,
* "remoteLinkSocketTimeoutSeconds": 60,
* "remoteLinkValidationMaxRetries": 0,
* "remoteStorageSizeMetricTtlMillis": 300000,
* "replicaInactivityTimeoutSeconds": 900,
* "replicaRecoveryWaitIntervalSeconds": 720,
* "replicaReportIntervalSeconds": 5,
* "requestsArchiveSize": 1000,
* "serializationReplacementsLogFrequency": 1800,
* "storageBuffercacheMaxopenfiles": 2147483647,
* "storageBuffercachePagesize": "128 KiB",
* "storageColumnBufferAcquireTimeout": 120000,
* "storageColumnBufferPoolMaxMemory": "string",
* "storageColumnBufferPoolMaxSize": 8000,
* "storageColumnBufferSize": "4 KiB",
* "storageCompressionBlock": "snappy",
* "storageDiskForceBytes": "16 MiB",
* "storageFormat": "column",
* "storageIoScheduler": "async",
* "storageMaxColumnsInZerothSegment": 5000,
* "storageMaxConcurrentFlushesPerPartition": 1,
* "storageMaxConcurrentMergesPerPartition": 1,
* "storageMaxScheduledMergesPerPartition": 8,
* "storageMemorycomponentFlushThreshold": 0.9,
* "storageMemorycomponentMaxScheduledFlushes": 0,
* "storageMemorycomponentNumcomponents": 2,
* "storageMemorycomponentPagesize": "128 KiB",
* "storagePageZeroWriter": "default",
* "storageWriteRateLimit": 0,
* "streamingSocketTimeoutSeconds": 0,
* "threaddumpFrequencySeconds": 300,
* "threaddumpLogLevel": "DEBUG",
* "traceCategories": null,
* "txnDatasetCheckpointInterval": 3600
}`

## [](#operation/put%5Fservice)Modify Service-Level Parameters 

Modifies service-level parameters, which apply to all nodes.

IMPORTANT: For the configuration changes to take effect, you must restart the Enterprise Analytics Service using the [Service Restart API](/enterprise-analytics/current/analytics-rest-admin/index.html#operation/restart%5Fservice).

##### Authorizations:

_AnalyticsManage_

##### Request Body schema: 

application/jsonapplication/x-www-form-urlencodedapplication/json

An object specifying one or more of the configurable service-level parameters.

| abortTasksTimeout                             | integer <int32\> Default: 600000 The maximum time to wait for tasks to be aborted, in milliseconds.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| --------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| activeMemoryGlobalBudget                      | string or integer Default: "64 MiB" The memory budget for the active runtime. Accepts either an integer number of bytes or a byte string (e.g. 64MiB).                                                                                                                                                                                                                                                                                                                                                                                       |
| activeStopTimeout                             | integer <int32\> Default: 3600 The maximum time (in seconds) to wait for a graceful stop of an active runtime.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| activeSuspendTimeout                          | integer <int32\> Default: 3600 The maximum time (in seconds) to wait for a graceful suspend of an active runtime.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| allowLoopbackRedirectRemoteLink               | boolean Default: false Allow remote link redirects to loopback addresses.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| analyticsBroadcastDcpStateMutationCount       | integer <int64\> Default: 100000 The number of processed mutations after which the DCP state is broadcast to storage.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| analyticsHttpRequestQueueSize                 | integer <int32\> Default: 256 The maximum number of HTTP requests to queue pending ability to execute.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| analyticsHttpThreadCount                      | integer <int32\> Default: 16 The number of threads to service HTTP requests.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| authorizationCacheTtlSeconds                  | integer <int32\> Default: 5 How long (in seconds) to cache user authorizations before checking with the authorization provider.                                                                                                                                                                                                                                                                                                                                                                                                              |
| authorizationHaltOnLostCredentialsSeconds     | integer <int32\> Default: 120 How long to wait (in seconds) when receiving 401 from the parent process for credentials to succeed before halting. (0 == no wait, -1 == wait forever)                                                                                                                                                                                                                                                                                                                                                         |
| awsAssumeRoleAsyncRefreshEnabled              | boolean Default: true Whether the AWS credential provider should fetch credentials asynchronously in the background. If true, threads are less likely to block when credentials are loaded, but additional resources are used to maintain the provider.                                                                                                                                                                                                                                                                                      |
| awsAssumeRoleDuration                         | integer <int32\> \[ 900 .. 43200 \] Default: 3600 AWS assuming role duration in seconds. Range from 900 seconds (15 minutes) to 43200 seconds (12 hours).                                                                                                                                                                                                                                                                                                                                                                                    |
| awsAssumeRolePrefetchTime                     | integer <int32\> Default: 300 The amount of time (in seconds), relative to STS token expiration, at which cached credentials are considered close to stale and should be updated. Prefetch updates will occur between the specified time and the stale time of the provider.                                                                                                                                                                                                                                                                 |
| awsAssumeRoleStaleTime                        | integer <int32\> Default: 60 The amount of time (in seconds), relative to STS token expiration, that the cached credentials are considered stale and must be updated.                                                                                                                                                                                                                                                                                                                                                                        |
| azureRequestTimeout                           | integer <int32\> Default: 120 Timeout (in seconds) for Azure client requests.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| bindAddress                                   | string or null Default: null The specific bind address to use. If not set, the wildcard address is used.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| bindToHost                                    | boolean Default: false If true, bind to the configured hostname instead of the wildcard address.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| cloudAccessPreemptiveRefreshIntervalSeconds   | integer <int32\> Default: 30 The interval (in seconds) at which to attempt to preemptively verify cloud access. If access is confirmed to be revoked, the process will halt. (0 == no preemptive refresh)                                                                                                                                                                                                                                                                                                                                    |
| cloudAccessRefreshHaltTimeoutSeconds          | integer <int32\> Default: 300 The length of time (in seconds) before the process will halt on failure to verify cloud access. (0 == wait forever)                                                                                                                                                                                                                                                                                                                                                                                            |
| cloudAccessTtlSeconds                         | integer <int32\> Default: 15 The length of time (in seconds) allowed to assume we still have write access to cloud resources.                                                                                                                                                                                                                                                                                                                                                                                                                |
| cloudAcquireTokenTimeout                      | integer <int32\> Default: 100 The waiting time (in milliseconds) if a requesting thread failed to acquire a token when the rate limit of cloud requests is exceeded. (min: 1, max: 5000)                                                                                                                                                                                                                                                                                                                                                     |
| cloudEvictionPlanReevaluateThreshold          | integer <int32\> Default: 50 The number of eviction events after which the eviction plan is re-evaluated.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| cloudMaxReadRequestsPerSecond                 | integer <int32\> Default: 1500 The maximum number of read requests per second (default 1500, 0 means unlimited).                                                                                                                                                                                                                                                                                                                                                                                                                             |
| cloudMaxWriteRequestsPerSecond                | integer <int32\> Default: 250 The maximum number of write requests per second (default 250, 0 means unlimited).                                                                                                                                                                                                                                                                                                                                                                                                                              |
| cloudProfilerLogInterval                      | integer <int32\> Default: 5 The interval (in minutes) at which to log cloud request statistics. Minimum is 1 minute. Note: enabling this logging may perturb the performance of cloud requests. (0 == disabled)                                                                                                                                                                                                                                                                                                                              |
| cloudRequestsHttpConnectionAcquireTimeout     | integer <int32\> Default: 120 The waiting time (in seconds) to acquire an HTTP connection before failing the request. (default 120 seconds)                                                                                                                                                                                                                                                                                                                                                                                                  |
| cloudRequestsHttpConnectionMaxIdleSeconds     | integer <int32\> Default: 120 The time (in seconds) after which an idle cloud connection will be closed. (0 == unlimited idle) **Available from Enterprise Analytics 2.1.1.**                                                                                                                                                                                                                                                                                                                                                                |
| cloudRequestsHttpConnectionMaxLifetimeSeconds | integer <int32\> Default: 3600 The time (in seconds) after which a cloud connection will no longer be reused. (0 == unlimited lifetime) **Available from Enterprise Analytics 2.1.1.**                                                                                                                                                                                                                                                                                                                                                       |
| cloudRequestsMaxHttpConnections               | integer <int32\> Default: 1000 The maximum number of HTTP connections to use concurrently for cloud requests per node. (default 1000)                                                                                                                                                                                                                                                                                                                                                                                                        |
| cloudRequestsMaxPendingHttpConnections        | integer <int32\> Default: 10000 The maximum number of HTTP connections allowed to wait for a connection per node. (default 10000)                                                                                                                                                                                                                                                                                                                                                                                                            |
| cloudStorageAllocationPercentage              | number <double\> Default: 0.8 The percentage of the total disk space that should be allocated for data storage when the selective caching policy is used. The remaining will act as a buffer for query workspace (i.e., for query operations that require spilling to disk). (default 80% of the total disk space)                                                                                                                                                                                                                           |
| cloudStorageCachePolicy                       | string Default: "selective" The caching policy for cloud storage data. Supported values: - selective — Only cache data that is likely to be reused; sweeps disk when storage thresholds are exceeded. - eager — Cache all data eagerly. - lazy — Cache data on first access.                                                                                                                                                                                                                                                                 |
| cloudStorageDiskMonitorInterval               | integer <int32\> Default: 120 The disk monitoring interval time (in seconds) that determines how often the system checks for pressure on disk space when using the selective caching policy. (default 120 seconds)                                                                                                                                                                                                                                                                                                                           |
| cloudStorageIndexInactiveDurationThreshold    | integer <int32\> Default: 360 The duration in minutes to consider an index is inactive. (default 360 or 6 hours)                                                                                                                                                                                                                                                                                                                                                                                                                             |
| cloudStorageS3ClientReadTimeout               | integer <int32\> Default: \-1 The read timeout (in seconds) for the S3 synchronous client. -1 means the SDK default.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| cloudStorageS3ParallelDownloaderClientType    | string The S3 client type used for parallel downloads. Defaults to crt when no custom endpoint is configured, and java otherwise (computed at startup).                                                                                                                                                                                                                                                                                                                                                                                      |
| cloudStorageS3UseRoundRobinDnsResolver        | boolean Default: false Enable round-robin DNS resolver for the S3 client.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| cloudStorageSweepThresholdPercentage          | number <double\> Default: 0.9 The percentage of the used storage space at which the disk sweeper starts freeing space by punching holes in stored indexes or by evicting them entirely, when the selective caching policy is used. (default 90% of the allocated space for storage)                                                                                                                                                                                                                                                          |
| cloudWriteBufferSize                          | integer <int32\> Default: 8388608 The write buffer size in bytes. (default 8MB, min 5MB)                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| clusterConnectRetries                         | integer <int32\> Default: 5 The number of times to retry connecting to the cluster controller.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| collectDcpStateFromNodesTimeout               | integer <int32\> Default: 600 The maximum time (in seconds) to wait to collect DCP state from all nodes.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| compilerArrayindex                            | boolean Default: true Enable/disable using array-indexes in queries.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| compilerBatchLookup                           | boolean Default: true Enable/disable batch point-lookups when running queries with secondary indexes.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| compilerCbo                                   | boolean Default: true Set the mode for cost based optimization.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| compilerColumnFilter                          | boolean Default: true Enable/disable the use of column min/max filters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| compilerCopyToWriteBufferSize                 | integer <int32\> Default: 8388608 The COPY TO write buffer size in bytes. (default 8MB, min 5MB).                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| compilerDisjunctionAsJoin                     | boolean Default: false Rewrite disjunctions to joins in query plans. **Available from Enterprise Analytics 2.1.1.**The default is false for clusters provisioned from 2.1.1 onwards. Clusters upgraded to 2.1.1 have this set to true to preserve pre-upgrade behavior.                                                                                                                                                                                                                                                                      |
| compilerDisjunctionHashThreshold              | integer <int32\> Default: \-1 The number of disjunctions after which a hash-based approach is used for evaluating OR operations. -1 disables the hash-based approach. **Available from Enterprise Analytics 2.1.1.**                                                                                                                                                                                                                                                                                                                         |
| compilerExtractCommonExpressionLimit          | integer <int32\> Default: 100 The maximum number of common expressions to extract. **Available from Enterprise Analytics 2.1.1.**The default is 100 for clusters provisioned from 2.1.1 onwards. Clusters upgraded to 2.1.1 have this set to 2147483647 (unlimited) to preserve pre-upgrade behavior.                                                                                                                                                                                                                                        |
| compilerExternalFieldPushdown                 | boolean Default: true Enable pushdown of field accesses to the external data-scan operator.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| compilerExternalscanmemory                    | string or integer Default: "8 KiB" The memory budget for an external scan operator instance in a partition. Accepts either an integer number of bytes or a byte string (e.g. 8KiB, 1MiB).                                                                                                                                                                                                                                                                                                                                                    |
| compilerFramesize                             | string or integer Default: "32 KiB" The page size for computation. Accepts either an integer number of bytes or a byte string (e.g. 32KiB).                                                                                                                                                                                                                                                                                                                                                                                                  |
| compilerGroupmemory                           | string or integer Default: "32 MiB" The memory budget for a group by operator instance in a partition. Accepts either an integer number of bytes or a byte string (e.g. 32MiB).                                                                                                                                                                                                                                                                                                                                                              |
| compilerJoinmemory                            | string or integer Default: "32 MiB" The memory budget for a join operator instance in a partition. Accepts either an integer number of bytes or a byte string (e.g. 32MiB).                                                                                                                                                                                                                                                                                                                                                                  |
| compilerMaxVariableOccurrencesInlining        | integer <int32\> Default: 128 Maximum occurrences of a variable allowed in an expression for inlining.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| compilerMinGroupmemory                        | string or integer Default: "512 KiB" The minimum memory budget for a group by operator instance in a partition. Accepts either an integer number of bytes or a byte string (e.g. 512KiB, 32MiB).                                                                                                                                                                                                                                                                                                                                             |
| compilerMinJoinmemory                         | string or integer Default: "512 KiB" The minimum memory budget for a join operator instance in a partition. Accepts either an integer number of bytes or a byte string (e.g. 512KiB, 32MiB).                                                                                                                                                                                                                                                                                                                                                 |
| compilerMinSortmemory                         | string or integer Default: "512 KiB" The minimum memory budget for a sort operator instance in a partition. Accepts either an integer number of bytes or a byte string (e.g. 512KiB, 32MiB).                                                                                                                                                                                                                                                                                                                                                 |
| compilerMinWindowmemory                       | string or integer Default: "512 KiB" The minimum memory budget for a window operator instance in a partition. Accepts either an integer number of bytes or a byte string (e.g. 512KiB, 32MiB).                                                                                                                                                                                                                                                                                                                                               |
| compilerOptimizeExpressionMaxArgs             | integer <int32\> Default: 200 Avoid costly O(N^2) expression optimization passes (e.g. constant folding, CSE) on large IN-list queries when the number of OR/AND function arguments is greater than or equal to the specified value. **Available from Enterprise Analytics 2.1.1.**The default is 200 for clusters provisioned from 2.1.1 onwards. Clusters upgraded to 2.1.1 have this set to 2147483647 (unlimited) to preserve pre-upgrade behavior.                                                                                      |
| compilerOrderedFields                         | boolean Default: false Enable/disable select order list.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| compilerParallelism                           | integer <int32\> Default: 0 The degree of parallelism for query execution. Zero means to use the storage parallelism as the query execution parallelism, while other integer values dictate the number of query execution parallel partitions. The system will fall back to use the number of all available CPU cores in the cluster as the degree of parallelism if the number set by a user is too large or too small.                                                                                                                     |
| compilerQueryplanshape                        | string Default: "zigzag" Set the mode for forcing the shape of the query plan (e.g., zigzag, leftdeep, rightdeep).                                                                                                                                                                                                                                                                                                                                                                                                                           |
| compilerRuntimeMemoryOverhead                 | integer <int32\> Default: 5 A percentage of the job's required memory to be added to account for runtime memory overhead.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| compilerSortmemory                            | string or integer Default: "32 MiB" The memory budget for a sort operator instance in a partition. Accepts either an integer number of bytes or a byte string (e.g. 32MiB).                                                                                                                                                                                                                                                                                                                                                                  |
| compilerSortParallel                          | boolean Default: false Enables/disables full parallel sort.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| compilerWindowmemory                          | string or integer Default: "32 MiB" The memory budget for a window operator instance in a partition. Accepts either an integer number of bytes or a byte string (e.g. 32MiB).                                                                                                                                                                                                                                                                                                                                                                |
| copyToKvBucketWaitUntilReadyTimeout           | integer <int32\> Default: 30 The number of seconds to wait for COPY TO KV bucket WaitUntilReady before timing out.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| coresMultiplier                               | integer <int32\> Default: 3 The factor to multiply by the number of cores to determine maximum query concurrent execution level.                                                                                                                                                                                                                                                                                                                                                                                                             |
| dcpBufferAckWatermark                         | integer <int32\> Default: 20 The integer percentage of DCP connection buffer size at which to acknowledge bytes consumed to the DCP producer as part of flow control.                                                                                                                                                                                                                                                                                                                                                                        |
| dcpChannelConnectAttemptTimeout               | integer <int32\> Default: 120 The maximum attempt time to connect to a DCP channel in seconds.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| dcpChannelConnectTotalTimeout                 | integer <int32\> Default: 480 The maximum time to wait to connect to a DCP channel in seconds.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| dcpConnectionBufferSize                       | integer <int32\> DCP connection buffer size in bytes. **Default:** Computed at startup — 10 MiB divided by the number of IO devices on the node when the JVM maximum heap is less than 8 GiB; otherwise 1% of the JVM maximum heap divided by the number of IO devices. A plain integer value in bytes may be specified to override this.                                                                                                                                                                                                    |
| dcpForceSnappyCompression                     | boolean Default: false Directs KV to snappy compress all values before sending to Analytics. This should only be enabled in specific circumstances, as it will increase memory and CPU use on data nodes. Only applicable if snappy compression support is enabled (dcpSupportSnappyCompression).                                                                                                                                                                                                                                            |
| dcpIdleQueueFlushThresholdMillis              | integer <int64\> Default: 100 The number of milliseconds before an empty DCP queue will trigger a flush of any pending incoming mutations to storage. (0 == flush instantly, negative value == never flush)                                                                                                                                                                                                                                                                                                                                  |
| dcpMaxConnectionsPerKvNode                    | integer <int32\> Default: 128 The maximum number of DCP connections to allow to each KV node for an ingestion (cluster-wide).                                                                                                                                                                                                                                                                                                                                                                                                                |
| dcpMinWorkPerKvConnection                     | integer <int32\> Default: 8 The minimum amount of work to allow per DCP connection for each ingestion connection. Work is (vbuckets \* streams), where one stream is used for each unique KV collection being ingested. When allocating connections, it will be attempted to keep work per connection above this number.                                                                                                                                                                                                                     |
| dcpNoopInterval                               | integer <int32\> Default: 120 The DCP NOOP interval (in seconds) used for dead connection detection.                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| dcpStreamRequestIncludePurgeSeqnos            | boolean Default: true Whether the DCP client should include the purge sequence number in stream requests, if supported by the producer.                                                                                                                                                                                                                                                                                                                                                                                                      |
| dcpSupportSnappyCompression                   | boolean Default: true Support receiving values from KV via DCP in snappy compressed form.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| dcpTargetMaxWorkPerKvConnection               | integer <int32\> Default: 64 The maximum amount of work to target per DCP connection for each ingestion connection. Work is (vbuckets \* streams), where one stream is used for each unique KV collection being ingested. The larger this number, the fewer DCP connections that will be attempted to be used.                                                                                                                                                                                                                               |
| deadlockWatchdogHaltDelaySeconds              | integer <int64\> Default: 120 The delay (in seconds) to wait for graceful shutdown due to deadlocked threads, before halting.                                                                                                                                                                                                                                                                                                                                                                                                                |
| deadlockWatchdogPollSeconds                   | integer <int64\> Default: 300 The frequency (in seconds) to scan for deadlocked threads.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| gcpImpersonateServiceAccountDuration          | integer <int32\> \[ 60 .. 3600 \] Default: 900 GCS impersonating service account duration in seconds. Range from 60 seconds (1 minute) to 3600 seconds (1 hour).                                                                                                                                                                                                                                                                                                                                                                             |
| healthCheckStatusCodeEjecting                 | integer <int32\> Default: 503 HTTP status code returned by the health check endpoint (GET :8095/api/v1/health) when the node is being rebalanced out of the cluster. This should indicate failure to upstream load balancers so that traffic is no longer routed to the node.                                                                                                                                                                                                                                                                |
| healthCheckStatusCodeNormal                   | integer <int32\> Default: 204 HTTP status code returned by the health check endpoint (GET :8095/api/v1/health) when the node is healthy and able to serve traffic. This should indicate success to upstream load balancers.                                                                                                                                                                                                                                                                                                                  |
| ingestionMaxBootstrapIntervalSeconds          | integer <int32\> Default: 480 The timeout (in seconds) to wait for remaining partitions to complete bootstrapping after at least one has bootstrapped, before aborting ingestion and triggering a reconnect.                                                                                                                                                                                                                                                                                                                                 |
| jobHistorySize                                | integer <int32\> Default: 10 The number of historical jobs to retain in memory.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| jobQueueCapacity                              | integer <int32\> Default: 4096 The maximum number of jobs to queue before rejecting new jobs.                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| jsonMaxDepth                                  | integer <int32\> Default: 1000 The maximum nesting depth for JSON objects. The depth is a count of objects and arrays that have not been closed, { and \[ respectively.                                                                                                                                                                                                                                                                                                                                                                      |
| jsonMaxDocLength                              | string or integer Default: 0 The maximum length of a JSON document. Accepts either an integer number of bytes or a byte string (e.g. 10MiB). 0 means no limit.                                                                                                                                                                                                                                                                                                                                                                               |
| jsonMaxNameLength                             | string or integer Default: 50000 The maximum length of a JSON field name. Accepts either an integer number of bytes or a byte string.                                                                                                                                                                                                                                                                                                                                                                                                        |
| jsonMaxNumberLength                           | string or integer Default: 1000 The maximum length of a JSON number. Accepts either an integer number of bytes or a byte string. 0 or less means no limit.                                                                                                                                                                                                                                                                                                                                                                                   |
| jsonMaxStringLength                           | string or integer Default: "40 MiB" The maximum length of a JSON string value. Accepts either an integer number of bytes or a byte string. 0 or less means no limit.                                                                                                                                                                                                                                                                                                                                                                         |
| jsonMaxTokenCount                             | integer <int64\> Default: 0 The maximum number of JSON tokens in a JSON object (0 or less is no limit). A token is a single unit of input, such as a number, a string, an object start or end, or an array start or end.                                                                                                                                                                                                                                                                                                                     |
| jvmArgs                                       | string or null Default: null JVM arguments to pass to the Analytics Driver. The default is undefined (null). Note that JVM arguments are generally not secure, and are exposed by [cbcollect\_info](/enterprise-analytics/current/cli/cbcollect-info-tool.html) and the [System Event](/server/7.6/learn/clusters-and-availability/system-events.html) log. To pass arguments opaquely, you may use [Java command-line argument files](https://docs.oracle.com/en/java/javase/11/tools/java.html#GUID-4856361B-8BFD-4964-AE84-121F5F6CF111). |
| kafkaMaxFetchBytes                            | integer <int32\> Default: 4194304 Maximum number of bytes fetched by a Kafka consumer in one request.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| maxActiveLinks                                | integer <int32\> Default: 100 The maximum number of links that can be active at any given time.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| maxRedirectsLocal                             | integer <int32\> Default: 0 The number of redirects to follow when communicating with the local cluster via HTTP(S).                                                                                                                                                                                                                                                                                                                                                                                                                         |
| maxRedirectsRemoteLink                        | integer <int32\> Default: 10 The number of redirects to follow when communicating with a remote link cluster via http for remote links not configured to prevent redirects.                                                                                                                                                                                                                                                                                                                                                                  |
| maxWebRequestSize                             | integer <int64\> Default: 209715200 The maximum accepted web request size in bytes.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| metadataRegistrationTimeoutSecs               | integer <int32\> Default: 1800 How long (in seconds) to wait for the metadata node to register with the cluster controller.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| netBufferCount                                | integer <int32\> Default: 1 The number of network buffers per thread.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| netThreadCount                                | integer <int32\> Default: 1 The number of network I/O threads.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| nodeDeltaRecovery                             | boolean Default: true Attempt to perform delta recovery when a node is recovered after a failover.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| rebalanceEjectDelaySeconds                    | integer <int32\> Default: 0 The delay (in seconds) before a node is ejected from the cluster during rebalance from the time that the health check API on that node will start reporting an error response. This is to allow adequate time for the node to removed from consideration by clients utilizing the health check API, to avoid failures on rebalance out; 0 == means no delay.                                                                                                                                                     |
| remoteLinkConnectTimeoutSeconds               | integer <int32\> Default: 30 The maximum time (in seconds) to wait for a remote link connection to establish. A value of 0 disables timeout; a value of -1 sets timeout to the system default.                                                                                                                                                                                                                                                                                                                                               |
| remoteLinkRefreshAuthSeconds                  | integer <int32\> Default: 0 The frequency at which permissions should be reevaluated for remote buckets/collections that may have been lost/restored for remote cluster versions at 7.0 or later; a value of 0 disables preemptive reevaluation.                                                                                                                                                                                                                                                                                             |
| remoteLinkSocketTimeoutSeconds                | integer <int32\> Default: 60 The maximum time (in seconds) to wait after establishing the connection for remote links; the maximum time of inactivity between two data packets. A value of 0 disables timeout; a value of -1 sets timeout to the system default.                                                                                                                                                                                                                                                                             |
| remoteLinkValidationMaxRetries                | integer <int32\> Default: 0 The number of times to retry on a remote link credential / config validation connection failure, i.e. on CREATE or ALTER LINK (0 == don't retry).                                                                                                                                                                                                                                                                                                                                                                |
| remoteStorageSizeMetricTtlMillis              | integer <int64\> Default: 300000 The length of time after which the remote storage size metric is recomputed.                                                                                                                                                                                                                                                                                                                                                                                                                                |
| replicaInactivityTimeoutSeconds               | integer <int32\> Default: 900 The number of seconds to wait before declaring a replica inactive while it is catching up.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| replicaRecoveryWaitIntervalSeconds            | integer <int32\> Default: 720 The number of seconds to wait for a failed replica to recover before suspending new writes.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| replicaReportIntervalSeconds                  | integer <int32\> Default: 5 The number of seconds to wait before sending a replicas report.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| requestsArchiveSize                           | integer <int32\> Default: 1000 The maximum number of archived requests to maintain.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| serializationReplacementsLogFrequency         | integer <int64\> Default: 1800 The frequency (in seconds) at which to debug-log serialization replacements.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| storageBuffercacheMaxopenfiles                | integer <int32\> Default: 2147483647 The maximum number of open files in the buffer cache.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| storageBuffercachePagesize                    | string or integer Default: "128 KiB" The page size for pages in the buffer cache. Accepts either an integer number of bytes or a byte string (e.g. 128KiB).                                                                                                                                                                                                                                                                                                                                                                                  |
| storageColumnBufferAcquireTimeout             | integer <int64\> Default: 120000 The maximum time in milliseconds to wait for acquiring a buffer from the column buffer pool.                                                                                                                                                                                                                                                                                                                                                                                                                |
| storageColumnBufferPoolMaxMemory              | string or integer The maximum memory allocated to the column buffer pool. Accepts either an integer number of bytes or a byte string (e.g. 512MiB). **Default:** 3% of the JVM maximum heap size, or 100 MiB for JVM heaps below \~3.3 GiB (computed at startup). A value of 0 restores the computed default.                                                                                                                                                                                                                                |
| storageColumnBufferPoolMaxSize                | integer <int32\> Default: 8000 The maximum number of buffers in the column buffer pool.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| storageColumnBufferSize                       | string or integer Default: "4 KiB" The size of each buffer in the column buffer pool. Accepts either an integer number of bytes or a byte string (e.g. 4KiB).                                                                                                                                                                                                                                                                                                                                                                                |
| storageCompressionBlock                       | string Default: "snappy" The default block compression scheme for storage (e.g., snappy, none).                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| storageDiskForceBytes                         | string or integer Default: "16 MiB" The number of bytes written before each disk force (fsync). Accepts either an integer number of bytes or a byte string (e.g. 16MiB).                                                                                                                                                                                                                                                                                                                                                                     |
| storageFormat                                 | string Default: "column" The default storage format (either row or column).                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| storageIoScheduler                            | string Default: "async" The I/O scheduler for LSM flush and merge operations (e.g., greedy, async).                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| storageMaxColumnsInZerothSegment              | string or integer Default: 5000 The maximum number of columns in the zero segment (page-zero). Accepts either an integer or a byte string.                                                                                                                                                                                                                                                                                                                                                                                                   |
| storageMaxConcurrentFlushesPerPartition       | integer <int32\> Default: 1 The maximum number of concurrently executed flushes per partition (0 means unlimited).                                                                                                                                                                                                                                                                                                                                                                                                                           |
| storageMaxConcurrentMergesPerPartition        | integer <int32\> Default: 1 The maximum number of concurrently executed merges per partition (0 means unlimited).                                                                                                                                                                                                                                                                                                                                                                                                                            |
| storageMaxScheduledMergesPerPartition         | integer <int32\> Default: 8 The maximum number of scheduled merges per partition (0 means unlimited).                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| storageMemorycomponentFlushThreshold          | number <double\> Default: 0.9 The memory usage threshold (as a fraction) at which memory components should be flushed.                                                                                                                                                                                                                                                                                                                                                                                                                       |
| storageMemorycomponentMaxScheduledFlushes     | integer <int32\> Default: 0 The maximum number of scheduled flush operations. 0 means that the value will be calculated as the number of partitions.                                                                                                                                                                                                                                                                                                                                                                                         |
| storageMemorycomponentNumcomponents           | integer <int32\> Default: 2 The number of memory components to be used per LSM index.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| storageMemorycomponentPagesize                | string or integer Default: "128 KiB" The page size for pages allocated to memory components. Accepts either an integer number of bytes or a byte string (e.g. 128KiB).                                                                                                                                                                                                                                                                                                                                                                       |
| storagePageZeroWriter                         | string Default: "default" The implementation to use for writing page-zero in storage components. Possible values: default, sparse, adaptive.                                                                                                                                                                                                                                                                                                                                                                                                 |
| storageWriteRateLimit                         | string or integer Default: 0 The maximum disk write rate for each storage partition. 0 or less disables the limit. Accepts either an integer number of bytes per second or a byte string (e.g. 100MiB).                                                                                                                                                                                                                                                                                                                                      |
| streamingSocketTimeoutSeconds                 | integer <int32\> Default: 0 The maximum time (in seconds) to wait for a response for streaming requests; the maximum time of inactivity between two data packets. A value of 0 disables timeout; a value of -1 sets timeout to the system default.                                                                                                                                                                                                                                                                                           |
| threaddumpFrequencySeconds                    | integer <int64\> Default: 300 The frequency (in seconds) at which to log diagnostic thread dumps.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| threaddumpLogLevel                            | string Default: "DEBUG" The log level at which to emit diagnostic thread dumps (e.g., DEBUG, INFO, WARN).                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| traceCategories                               | string or null Default: null A comma-separated list of trace categories to enable for diagnostic tracing. The default is undefined (null — no categories enabled).                                                                                                                                                                                                                                                                                                                                                                           |
| txnDatasetCheckpointInterval                  | integer <int32\> Default: 3600 The interval (in seconds) after which an Analytics collection is considered idle and persisted to disk.                                                                                                                                                                                                                                                                                                                                                                                                       |

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
* "abortTasksTimeout": 600000,
* "activeMemoryGlobalBudget": "64 MiB",
* "activeStopTimeout": 3600,
* "activeSuspendTimeout": 3600,
* "allowLoopbackRedirectRemoteLink": false,
* "analyticsBroadcastDcpStateMutationCount": 100000,
* "analyticsHttpRequestQueueSize": 256,
* "analyticsHttpThreadCount": 16,
* "authorizationCacheTtlSeconds": 5,
* "authorizationHaltOnLostCredentialsSeconds": 120,
* "awsAssumeRoleAsyncRefreshEnabled": true,
* "awsAssumeRoleDuration": 3600,
* "awsAssumeRolePrefetchTime": 300,
* "awsAssumeRoleStaleTime": 60,
* "azureRequestTimeout": 120,
* "bindAddress": null,
* "bindToHost": false,
* "cloudAccessPreemptiveRefreshIntervalSeconds": 30,
* "cloudAccessRefreshHaltTimeoutSeconds": 300,
* "cloudAccessTtlSeconds": 15,
* "cloudAcquireTokenTimeout": 100,
* "cloudEvictionPlanReevaluateThreshold": 50,
* "cloudMaxReadRequestsPerSecond": 1500,
* "cloudMaxWriteRequestsPerSecond": 250,
* "cloudProfilerLogInterval": 5,
* "cloudRequestsHttpConnectionAcquireTimeout": 120,
* "cloudRequestsHttpConnectionMaxIdleSeconds": 120,
* "cloudRequestsHttpConnectionMaxLifetimeSeconds": 3600,
* "cloudRequestsMaxHttpConnections": 1000,
* "cloudRequestsMaxPendingHttpConnections": 10000,
* "cloudStorageAllocationPercentage": 0.8,
* "cloudStorageCachePolicy": "selective",
* "cloudStorageDiskMonitorInterval": 120,
* "cloudStorageIndexInactiveDurationThreshold": 360,
* "cloudStorageS3ClientReadTimeout": -1,
* "cloudStorageS3ParallelDownloaderClientType": "string",
* "cloudStorageS3UseRoundRobinDnsResolver": false,
* "cloudStorageSweepThresholdPercentage": 0.9,
* "cloudWriteBufferSize": 8388608,
* "clusterConnectRetries": 5,
* "collectDcpStateFromNodesTimeout": 600,
* "compilerArrayindex": true,
* "compilerBatchLookup": true,
* "compilerCbo": true,
* "compilerColumnFilter": true,
* "compilerCopyToWriteBufferSize": 8388608,
* "compilerDisjunctionAsJoin": false,
* "compilerDisjunctionHashThreshold": -1,
* "compilerExtractCommonExpressionLimit": 100,
* "compilerExternalFieldPushdown": true,
* "compilerExternalscanmemory": "8 KiB",
* "compilerFramesize": "32 KiB",
* "compilerGroupmemory": "32 MiB",
* "compilerJoinmemory": "32 MiB",
* "compilerMaxVariableOccurrencesInlining": 128,
* "compilerMinGroupmemory": "512 KiB",
* "compilerMinJoinmemory": "512 KiB",
* "compilerMinSortmemory": "512 KiB",
* "compilerMinWindowmemory": "512 KiB",
* "compilerOptimizeExpressionMaxArgs": 200,
* "compilerOrderedFields": false,
* "compilerParallelism": 0,
* "compilerQueryplanshape": "zigzag",
* "compilerRuntimeMemoryOverhead": 5,
* "compilerSortmemory": "32 MiB",
* "compilerSortParallel": false,
* "compilerWindowmemory": "32 MiB",
* "copyToKvBucketWaitUntilReadyTimeout": 30,
* "coresMultiplier": 3,
* "dcpBufferAckWatermark": 20,
* "dcpChannelConnectAttemptTimeout": 120,
* "dcpChannelConnectTotalTimeout": 480,
* "dcpConnectionBufferSize": 0,
* "dcpForceSnappyCompression": false,
* "dcpIdleQueueFlushThresholdMillis": 100,
* "dcpMaxConnectionsPerKvNode": 128,
* "dcpMinWorkPerKvConnection": 8,
* "dcpNoopInterval": 120,
* "dcpStreamRequestIncludePurgeSeqnos": true,
* "dcpSupportSnappyCompression": true,
* "dcpTargetMaxWorkPerKvConnection": 64,
* "deadlockWatchdogHaltDelaySeconds": 120,
* "deadlockWatchdogPollSeconds": 300,
* "gcpImpersonateServiceAccountDuration": 900,
* "healthCheckStatusCodeEjecting": 503,
* "healthCheckStatusCodeNormal": 204,
* "ingestionMaxBootstrapIntervalSeconds": 480,
* "jobHistorySize": 10,
* "jobQueueCapacity": 4096,
* "jsonMaxDepth": 1000,
* "jsonMaxDocLength": 0,
* "jsonMaxNameLength": 50000,
* "jsonMaxNumberLength": 1000,
* "jsonMaxStringLength": "40 MiB",
* "jsonMaxTokenCount": 0,
* "jvmArgs": null,
* "kafkaMaxFetchBytes": 4194304,
* "maxActiveLinks": 100,
* "maxRedirectsLocal": 0,
* "maxRedirectsRemoteLink": 10,
* "maxWebRequestSize": 209715200,
* "metadataRegistrationTimeoutSecs": 1800,
* "netBufferCount": 1,
* "netThreadCount": 1,
* "nodeDeltaRecovery": true,
* "rebalanceEjectDelaySeconds": 0,
* "remoteLinkConnectTimeoutSeconds": 30,
* "remoteLinkRefreshAuthSeconds": 0,
* "remoteLinkSocketTimeoutSeconds": 60,
* "remoteLinkValidationMaxRetries": 0,
* "remoteStorageSizeMetricTtlMillis": 300000,
* "replicaInactivityTimeoutSeconds": 900,
* "replicaRecoveryWaitIntervalSeconds": 720,
* "replicaReportIntervalSeconds": 5,
* "requestsArchiveSize": 1000,
* "serializationReplacementsLogFrequency": 1800,
* "storageBuffercacheMaxopenfiles": 2147483647,
* "storageBuffercachePagesize": "128 KiB",
* "storageColumnBufferAcquireTimeout": 120000,
* "storageColumnBufferPoolMaxMemory": "string",
* "storageColumnBufferPoolMaxSize": 8000,
* "storageColumnBufferSize": "4 KiB",
* "storageCompressionBlock": "snappy",
* "storageDiskForceBytes": "16 MiB",
* "storageFormat": "column",
* "storageIoScheduler": "async",
* "storageMaxColumnsInZerothSegment": 5000,
* "storageMaxConcurrentFlushesPerPartition": 1,
* "storageMaxConcurrentMergesPerPartition": 1,
* "storageMaxScheduledMergesPerPartition": 8,
* "storageMemorycomponentFlushThreshold": 0.9,
* "storageMemorycomponentMaxScheduledFlushes": 0,
* "storageMemorycomponentNumcomponents": 2,
* "storageMemorycomponentPagesize": "128 KiB",
* "storagePageZeroWriter": "default",
* "storageWriteRateLimit": 0,
* "streamingSocketTimeoutSeconds": 0,
* "threaddumpFrequencySeconds": 300,
* "threaddumpLogLevel": "DEBUG",
* "traceCategories": null,
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
* "storageBuffercacheSize": "string",
* "storageMemorycomponentGlobalbudget": "string"
}`

## [](#operation/put%5Fnode)Modify Node-Specific Parameters 

Views node-specific parameters, which apply to the node receiving the request.

IMPORTANT: For the configuration changes to take effect, you must restart the node using the [Node Restart API](/enterprise-analytics/current/analytics-rest-admin/index.html#operation/restart%5Fnode), or restart the Enterprise Analytics Service using the [Service Restart API](/enterprise-analytics/current/analytics-rest-admin/index.html#operation/restart%5Fservice).

##### Authorizations:

_AnalyticsManage_

##### Request Body schema: 

application/jsonapplication/x-www-form-urlencodedapplication/json

An object specifying one or more of the configurable node-level parameters on this node.

| jvmArgs                            | string or null Default: null JVM arguments to pass to the Analytics Driver. The default is undefined (null). Node-specific JVM arguments are appended to service-level JVM arguments. If the same JVM argument appears in both the service-level arguments and the node-specific arguments, the node-specific argument takes priority. Note that JVM arguments are generally not secure, and are exposed by \[cbcollect\_info\] and the \[System Event\] log. To pass arguments opaquely, you may use [Java command-line argument files](https://docs.oracle.com/en/java/javase/11/tools/java.html#GUID-4856361B-8BFD-4964-AE84-121F5F6CF111). |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| storageBuffercacheSize             | string or integer The size of memory allocated to the disk buffer cache. The value should be a multiple of the buffer cache page size. Accepts either an integer number of bytes or a byte string (e.g. 512MiB, 2GiB). **Default:** 1/4 of the JVM maximum heap size (computed at startup).                                                                                                                                                                                                                                                                                                                                                    |
| storageMemorycomponentGlobalbudget | string or integer The size of memory allocated to the memory components. The value should be a multiple of the memory component page size. Accepts either an integer number of bytes or a byte string (e.g. 512MiB, 2GiB). **Default:** 1/4 of the JVM maximum heap size (computed at startup).                                                                                                                                                                                                                                                                                                                                                |

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
* "storageBuffercacheSize": "string",
* "storageMemorycomponentGlobalbudget": "string"
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