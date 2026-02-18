---
title: Set GSI Settings
description: To set the global secondary index settings use <code>POST
  /settings/indexes</code>.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/rest-api/pages/post-settings-indexes.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.6/rest-api/post-settings-indexes.html)

# Set GSI Settings

> To set the global secondary index settings use `POST /settings/indexes`. 

## [](#description)Description

This endpoint is used to update the global secondary index settings for the cluster. The request is handled and validated by the cluster manager and then delegated to all relevant index nodes automatically. All changes to the index settings via this method apply to all index nodes in the cluster. Parameters which are not specified are left unchanged, it is not necessary to specify all parameters in the body.

## [](#http-method-and-uri)HTTP Method and URI

```http
POST http://<host>:8091/settings/indexes
```

## [](#body-parameters)Body Parameters

All of the following parameters are passed in the request body as `application/x-www-form-urlencoded` data. The parameters are specified as key-value pairs (e.g `key=value`).

**Optional**

| Name                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Type                                                                         |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| enableShardAffinity    | Selects the [Index Rebalance Methods](../learn/clusters-and-availability/rebalance-and-index-service.md#index-rebalance-methods): false (default value): Index Service nodes rebuild indexes that are newly assigned to them during a rebalance. true: Couchbase Server moves a reassigned index’s files between Index Service nodes. In Couchbase Server versions 7.6.0 and 7.6.1, when you enabled file-based rebalance you could not choose which Index Service nodes would contain an index when using the CREATE INDEX statement. In Couchbase Server 7.6.2 and later, you can use the WITH <node> clause to set which node contains the index. You still cannot use the WITH <node> clause with ALTER INDEX after you enable file-based rebalance.                                                                                                                                                                                                                                                        | boolean                                                                      |
| indexerThreads         | Number of threads for the indexer process to use, this applies equally to all index nodes in the cluster regardless of the number of cores on each node. A value of 0 causes the indexer process to use one thread per CPU core on each individual node.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | integer                                                                      |
| logLevel               | Indexer logging level.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Possible values are: silent fatal error warn info verbose timing debug trace |
| maxRollbackPoints      | Maximum number of committed rollback points.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | integer                                                                      |
| memorySnapshotInterval | In-memory snapshotting interval in milliseconds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | integer                                                                      |
| numReplica             | The default number of index replicas to be created by the Index Service whenever CREATE INDEX is invoked. For further details, refer to {index-replication}\[Index Replication\].                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | integer                                                                      |
| redistributeIndexes    | When true, Couchbase Server redistributes indexes when rebalance occurs, in order to optimize performance. If false (the default), such redistribution does not occur. For further details, refer to [Rebalancing the Index Service](../learn/clusters-and-availability/rebalance-and-index-service.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | boolean                                                                      |
| stableSnapshotInterval | Persisted snapshotting interval in milliseconds.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | integer                                                                      |
| enablePageBloomFilter  | Whether Bloom filters are enabled for memory management. See [Per Page Bloom Filters](../learn/services-and-indexes/indexes/storage-modes.md#per-page-bloom-filters).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | boolean                                                                      |
| storageMode            | The storage mode to be used for all global secondary indexes in the cluster. [ENTERPRISE EDITION](https://www.couchbase.com/products/editions) In the Enterprise Edition of Couchbase Server, the options are plasma and memory\_optimized. A value of plasma sets the cluster-wide index storage mode to use the Plasma storage engine, which can utilize both memory and persistent storage for index maintenance and index scans. A value of memory\_optimized sets the cluster-wide index storage mode to use memory optimized global secondary indexes which can perform index maintenance and index scan faster at in-memory speeds. This setting can only be changed while there are no index nodes in the cluster. To change from standard GSI to memory optimized GSI or vice versa, you need to remove all the index service nodes in the cluster. [COMMUNITY EDITION](https://www.couchbase.com/products/editions) If you are using the Community Edition, the default (and only) value is forestdb. | Possible values are: plasma memory\_optimized forestdb                       |

## [](#response-codes)Response Codes

| Response Code | Description                                                                      |
| ------------- | -------------------------------------------------------------------------------- |
| 200           | Success. Settings are updated and the new settings are returned in the response. |
| 401           | Unauthorized.                                                                    |

## [](#sample-curl-command)Sample Curl Command

The following example sets the global secondary index settings.

```bash
curl -v -X POST http://127.0.0.1:8091/settings/indexes \
-u Administrator:password \
-d indexerThreads=4 \
-d logLevel=verbose \
-d maxRollbackPoints=2 \
-d storageMode=plasma \
-d redistributeIndexes=false \
-d numReplica=0 \
-d enablePageBloomFilter=false
```

## [](#sample-response)Sample Response

**200**

```json
{
  "redistributeIndexes": false,
  "numReplica": 0,
  "enablePageBloomFilter": false,
  "enableShardAffinity": false,
  "indexerThreads": 4,
  "memorySnapshotInterval": 200,
  "stableSnapshotInterval": 5000,
  "maxRollbackPoints": 2,
  "logLevel": "verbose",
  "storageMode": "plasma"
}
```

**401**

This response code returns an empty body.

## [](#disable-file-transfer-based-rebalance)Curl Command to Disable the File Transfer Based Rebalance

The following command disables the File Transfer Based Rebalance (`enableShardAffinity`) feature in the [Index Storage Mode](../manage/manage-settings/general-settings.md#index-storage-mode).

> [!NOTE]
> Shard Based Rebalance and Rebalance Based on File Transfer are synonyms for File-based Rebalance.

```bash
curl -X POST http://<host>:8091/settings/indexes -d enableShardAffinity=false -u Administrator:<password>
```