---
title: Pausing and Resuming a Replication
description: An XDCR replication can be paused and resumed by means of the REST API.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/rest-api/pages/rest-xdcr-pause-resume.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:rest-api:rest-xdcr-pause-resume.adoc[]
---

[View original HTML](/server/7.2/rest-api/rest-xdcr-pause-resume.html)

# Pausing and Resuming a Replication

> An XDCR replication can be paused and resumed by means of the REST API. 

## [](#http-method-and-uri)HTTP Method and URI

POST /settings/replications/<settingsURI>

## [](#description)Description

An XDCR replication is paused and resumed by configuring `pauseRequested`; which is one of the _XDCR advanced settings_ described in [Managing Advanced Settings](rest-xdcr-adv-settings.md).

The replication to be paused or resumed is specified by means of its `settingsURI`, which can be returned by using the `GET /pools/default/tasks` method and URI, described in [Getting Cluster Tasks](rest-get-cluster-tasks.md).

The Full Admin, Cluster Admin, or XDCR Admin role is required.

## [](#curl-syntax)Curl Syntax

curl -X POST http://<ip-address-or-domain-name>:8091/settings/replications/<settingsURI>
  -u <username>:<password>
  -d pauseRequested=[ true | false ]

The value of the `pauseRequested` flag can either be `true`, which means that the specified replication should be paused; or `false`, which means that the specified replication should _not_ be paused. The default value is `false`. If the established value is `false` and a value of `true` is then specified, an ongoing replication is paused. If the established value is `true` and a value of `false` is then specified, a paused replication is resumed. (Note that the operation is idempotent: specifying `true` when the established value is already `true`, or specifying `false` when the value is already `false`, has no effect.)

## [](#responses)Responses

Success returns `200 OK` and an object containing all current advanced settings.

If the boolean is incorrectly specified, `400 Bad Request` is returned, with the following error message: `{"pauseRequested": "The value must be a boolean" }`. If authentication is either not attempted or succeeds with inappropriate credentials, `403 Forbidden` is returned, with the following error message: `{"message": "Forbidden. User needs one of the following permissions", "permissions": ["cluster.bucket[travel-sample].xdcr!execute"]}`. If authentication is attempted but specified credentials are not matched, `401 Unauthorized` is returned.

If the `settingsURI` is incorrectly specified, `500 Internal Server Error` is returned, with the following error message: `requested resource not found`. Incorrect specification of the URI returns `404 Object Not Found`.

## [](#examples)Examples

The following example pauses the replication from the source bucket `travel-sample` to the target bucket `ts`. Output is piped to the [jq](https://stedolan.github.io/jq/) command, to facilitate readability.

curl -v -X POST \
http://localhost:8091/settings/replications/2b5dcd1b0101a9d52f31a802d8c4231e%2Ftravel-sample%2Fts \
-u Administrator:password \
-d pauseRequested=true | jq '.'

If execution is successful, the replication is paused, and the following object, containing all current advanced settings, is returned:

{
  "checkpointInterval": 600,
  "ckptSvcCacheEnabled": true,
  "colMappingRules": {},
  "collectionsExplicitMapping": false,
  "collectionsMigrationMode": false,
  "collectionsMirroringMode": false,
  "collectionsOSOMode": true,
  "compressionType": "Auto",
  "desiredLatency": 50,
  "docBatchSizeKb": 2048,
  "failureRestartInterval": 10,
  "filterBypassExpiry": false,
  "filterBypassUncommittedTxn": false,
  "filterDeletion": false,
  "filterExpiration": false,
  "filterExpression": "",
  "hlvPruningWindowSec": 259200,
  "jsFunctionTimeoutMs": 20000,
  "logLevel": "Info",
  "mergeFunctionMapping": {},
  "networkUsageLimit": 0,
  "optimisticReplicationThreshold": 256,
  "pauseRequested": true,
  "preReplicateVBMasterCheck": true,
  "priority": "High",
  "replicateCkptIntervalMin": 20,
  "retryOnRemoteAuthErr": true,
  "retryOnRemoteAuthErrMaxWaitSec": 3600,
  "sourceNozzlePerNode": 2,
  "statsInterval": 1000,
  "targetNozzlePerNode": 2,
  "type": "xmem",
  "workerBatchSize": 500
}

As the output indicates from the displayed value of `pauseRequested`, the replication has been paused.

The following example restarts the replication

curl -v -X POST \
http://localhost:8091/settings/replications/2b5dcd1b0101a9d52f31a802d8c4231e%2Ftravel-sample%2Fts \
-u Administrator:password \
-d pauseRequested=false | jq '.'

If execution is successful, the replication is restarted, and the following output is returned:

{
  "checkpointInterval": 600,
  "ckptSvcCacheEnabled": true,
  "colMappingRules": {},
  "collectionsExplicitMapping": false,
  "collectionsMigrationMode": false,
  "collectionsMirroringMode": false,
  "collectionsOSOMode": true,
  "compressionType": "Auto",
  "desiredLatency": 50,
  "docBatchSizeKb": 2048,
  "failureRestartInterval": 10,
  "filterBypassExpiry": false,
  "filterBypassUncommittedTxn": false,
  "filterDeletion": false,
  "filterExpiration": false,
  "filterExpression": "",
  "hlvPruningWindowSec": 259200,
  "jsFunctionTimeoutMs": 20000,
  "logLevel": "Info",
  "mergeFunctionMapping": {},
  "networkUsageLimit": 0,
  "optimisticReplicationThreshold": 256,
  "pauseRequested": false,
  "preReplicateVBMasterCheck": true,
  "priority": "High",
  "replicateCkptIntervalMin": 20,
  "retryOnRemoteAuthErr": true,
  "retryOnRemoteAuthErrMaxWaitSec": 3600,
  "sourceNozzlePerNode": 2,
  "statsInterval": 1000,
  "targetNozzlePerNode": 2,
  "type": "xmem",
  "workerBatchSize": 500
}

As the output indicates from the displayed value of `pauseRequested`, the replication has been restarted.

## [](#see-also)See Also

XDCR Advanced Settings are described in [Managing Advanced Settings](rest-xdcr-adv-settings.md).

The `settingsURI` is returned by using the `GET /pools/default/tasks` method and URI, described in [Getting Cluster Tasks](rest-get-cluster-tasks.md).

An overview of XDCR is provided in [Cross Data Center Replication (XDCR)](../learn/clusters-and-availability/xdcr-overview.md).