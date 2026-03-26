---
title: Getting Bucket Information
description: information about buckets defined on the cluster can be retrieved,
  by means of the REST API.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/rest-api/pages/rest-buckets-summary.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:server:rest-api:rest-buckets-summary.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/rest-api/rest-buckets-summary.html)

# Getting Bucket Information

> information about buckets defined on the cluster can be retrieved, by means of the REST API. 

## [](#http-methods-and-uris)HTTP Methods and URIs

GET /pools/default/buckets

GET /pools/default/buckets/<bucket-name>

## [](#description)Description

`GET /pools/default/buckets` retrieves information about all buckets defined on the cluster. If the `<bucket-name>` path-parameter is added, only information about the specified bucket is retrieved.

## [](#curl-syntax)Curl Syntax

curl -X GET http://<ip-address-or-domain-name>:8091/pools/default/buckets/<bucket-name>

## [](#responses)Responses

Successful execution returns `200 OK`, and either an object containing information about the individual bucket specified by the path-parameter; or an array of such objects, each containing information about one of the buckets defined on the cluster.

Failure to authenticate returns `401 Unauthorized`. An incorrectly specified URI returns `404 Object Not Found`. If an internal error prevents successful execution, `500 Internal Server Error` is returned.

## [](#example)Example

The following example returns information about a single bucket named `travel-sample`. The example pipes the output to [jq](https://stedolan.github.io/jq/) to format the output. It also removes the `nodes` and `vBucketMap` lists which are not important for understanding the bucket's settings.

```bash
curl -X GET -u Administrator:password \
      http://localhost:8091/pools/default/buckets/travel-sample | \
      jq '.vBucketServerMap.vBucketMap = "<vBucketMap omitted>"
         | .nodes = "<node details omitted>"'
```

If successful, the call returns `200 OK`, and an object similar to the one shown in the following example.

The fields `historyRetentionCollectionDefault`, `historyRetentionCollectionBytes`, and `historyRetentionCollectionSeconds` are specific to Magma storage. When the bucket does not use Magma as its storage backend, these properties do not appear in the output.

```json
{
  "name": "travel-sample",
  "nodeLocator": "vbucket",
  "bucketType": "membase",
  "storageBackend": "magma",
  "uuid": "823f32a2b2abd57581230b39e31b7a34",
  "uri": "/pools/default/buckets/travel-sample?bucket_uuid=823f32a2b2abd57581230b39e31b7a34",
  "streamingUri": "/pools/default/bucketsStreaming/travel-sample?bucket_uuid=823f32a2b2abd57581230b39e31b7a34",
  "numVBuckets": 128,
  "bucketCapabilitiesVer": "",
  "bucketCapabilities": [
    "collections",
    "durableWrite",
    "tombstonedUserXAttrs",
    "subdoc.ReplaceBodyWithXattr",
    "subdoc.DocumentMacroSupport",
    "subdoc.ReviveDocument",
    "nonDedupedHistory",
    "dcp.IgnorePurgedTombstones",
    "preserveExpiry",
    "querySystemCollection",
    "mobileSystemCollection",
    "subdoc.ReplicaRead",
    "subdoc.BinaryXattr",
    "subdoc.AccessDeleted",
    "rangeScan",
    "dcp",
    "cbhello",
    "touch",
    "cccp",
    "xdcrCheckpointing",
    "nodesExt",
    "xattr"
  ],
  "collectionsManifestUid": "2",
  "vBucketServerMap": {
    "hashAlgorithm": "CRC",
    "numReplicas": 0,
    "serverList": [
      "[::1]:11210"
    ],
    "vBucketMap": "<vBucketMap Omitted>"
  },
  "localRandomKeyUri": "/pools/default/buckets/travel-sample/localRandomKey",
  "controllers": {
    "compactAll": "/pools/default/buckets/travel-sample/controller/compactBucket",
    "compactDB": "/pools/default/buckets/travel-sample/controller/compactDatabases",
    "purgeDeletes": "/pools/default/buckets/travel-sample/controller/unsafePurgeBucket",
    "startRecovery": "/pools/default/buckets/travel-sample/controller/startRecovery"
  },
  "nodes": "<Node details omitted>",
  "stats": {
    "uri": "/pools/default/buckets/travel-sample/stats",
    "directoryURI": "/pools/default/buckets/travel-sample/stats/Directory",
    "nodeStatsListURI": "/pools/default/buckets/travel-sample/nodes"
  },
  "authType": "sasl",
  "autoCompactionSettings": false,
  "rank": 0,
  "enableCrossClusterVersioning": false,
  "versionPruningWindowHrs": 720,
  "replicaNumber": 0,
  "threadsNumber": 3,
  "quota": {
    "ram": 209715200,
    "rawRAM": 209715200
  },
  "basicStats": {
    "quotaPercentUsed": 21.90842056274414,
    "opsPerSec": 0,
    "diskFetches": 0,
    "itemCount": 63321,
    "diskUsed": 119897122,
    "dataUsed": 119897122,
    "memUsed": 137835864,
    "vbActiveNumNonResident": 0
  },
  "evictionPolicy": "fullEviction",
  "durabilityMinLevel": "none",
  "storageQuotaPercentage": 50,
  "historyRetentionSeconds": 0,
  "historyRetentionBytes": 0,
  "historyRetentionCollectionDefault": true,
  "magmaKeyTreeDataBlockSize": 4096,
  "magmaSeqTreeDataBlockSize": 4096,
  "continuousBackupEnabled": false,
  "continuousBackupInterval": 2,
  "continuousBackupLocation": "",
  "conflictResolutionType": "seqno",
  "workloadPatternDefault": "undefined",
  "maxTTL": 0,
  "compressionMode": "passive",
  "expiryPagerSleepTime": 600,
  "memoryLowWatermark": 75,
  "memoryHighWatermark": 85,
  "durabilityImpossibleFallback": "disabled",
  "warmupBehavior": "background",
  "invalidHlcStrategy": "error",
  "hlcMaxFutureThreshold": 3900,
  "dcpConnectionsBetweenNodes": 1,
  "dcpBackfillIdleProtectionEnabled": true,
  "dcpBackfillIdleLimitSeconds": 720,
  "dcpBackfillIdleDiskThreshold": 90,
  "accessScannerEnabled": true,
  "encryptionAtRestInfo": {
    "dataStatus": "unencrypted",
    "dekNumber": 0,
    "issues": []
  },
  "encryptionAtRestKeyId": -1,
  "encryptionAtRestDekRotationInterval": 2592000,
  "encryptionAtRestDekLifetime": 31536000
}
```

## [](#see-also)See Also

* For an overview of buckets, see [Buckets](../learn/buckets-memory-and-storage/buckets.md).
* For introduction to scopes and collections, see [Scopes and Collections](../learn/data/scopes-and-collections.md).