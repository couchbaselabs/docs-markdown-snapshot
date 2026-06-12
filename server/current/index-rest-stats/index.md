---
title: Index Statistics REST API
editUrl: https://github.com/couchbaselabs/cb-swagger/edit/release/8.0/docs/modules/index-rest-stats/pages/index.adoc
pubDate: 2026-06-12T16:31:57.907Z
link: xref:server:index-rest-stats:index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/index-rest-stats/index.html)

# Index Statistics REST API

## [](#overview)Overview

The Index Statistics REST API is provided by the Index service. This API enables you to get Index service statistics.

### Version information

**Version:** 8.0

### Host information

{scheme}://{host}:{port}

The URL scheme, host, and port are as follows.

| Component  | Description                                                                             |
| ---------- | --------------------------------------------------------------------------------------- |
| **scheme** | The URL scheme. Use https for secure access. **Values:** http, https                    |
| **host**   | The host name or IP address of a node running the Index Service. **Example:** localhost |
| **port**   | The Index Service REST port. Use 19102 for secure access. **Values:** 9102, 19102       |

## [](#resources)Resources

This section describes the operations available with this REST API.

[Get Statistics for an Index](#get%5Findex%5Fstats)  
[Get Statistics for Indexes in a Keyspace](#get%5Fkeyspace%5Fstats)  
[Get Statistics for an Index Node](#get%5Fnode%5Fstats)

### [](#get%5Findex%5Fstats)Get Statistics for an Index

GET /api/v1/stats/{keyspace}/{index}

#### [](#get%5Findex%5Fstats-description)Description

Returns statistics for an index.

Produces

* application/json

#### [](#get%5Findex%5Fstats-parameters)Parameters

Path Parameters

| Name                 | Description                                                                                                                                                                                                                                                                                                                                                  | Schema |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------ |
| **keyspace**required | The name of a keyspace. This must contain a bucket name, which may be followed by an optional scope name and an optional collection name, separated by dots. For example, bucket.scope.collection. If any part of the keyspace name contains a dot, that part of the keyspace name must be wrapped in backticks. For example, \`bucket.1\`.scope.collection. | String |
| **index**required    | The name of an index.                                                                                                                                                                                                                                                                                                                                        | String |

Query Parameters

| Name                  | Description                                                                                   | Schema  |
| --------------------- | --------------------------------------------------------------------------------------------- | ------- |
| **pretty**optional    | Whether the output should be formatted with indentations and newlines. **Default:** false     | Boolean |
| **partition**optional | Whether statistics for index partitions should be included. **Default:** false                | Boolean |
| **redact**optional    | Whether keyspace and index names should be redacted in the output. **Default:** false         | Boolean |
| **skipEmpty**optional | Whether empty, null, or zero statistics should be omitted from the output. **Default:** false | Boolean |

> [!NOTE]
> In most cases, the [keyspace](#get%5Findex%5Fstats-parameters) path parameter must specify the complete name of the keyspace containing the index. It may not omit the scope name or the collection name.
> 
> However, if the specified index is stored in the default collection in the default scope within a bucket, then the [keyspace](#get%5Findex%5Fstats-parameters) path parameter may specify just the bucket name alone.

> [!TIP]
> It is not possible to specify an individual index partition in the path.

#### [](#get%5Findex%5Fstats-responses)Responses

| HTTP Code | Description                                                                                                                                                                                                                                                                                        | Schema                           |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| 200       | Success. Returns an object containing one nested <keyspace>:<index> object. If the [partition](#get%5Findex%5Fstats-parameters) query parameter was set to true, the returned object also contains one or more Partition-<num> objects — one for each index partition found on the specified node. | [Index and Partitions](#PartIdx) |
| 404       | Not found. Returns the complete specified keyspace name, and the specified index name if provided. The keyspace name may be incorrect, the keyspace may contain no indexes, the index may not be located in the specified keyspace, or the index may be warming up after a restart.                |                                  |

#### [](#get%5Findex%5Fstats-security)Security

| Type         | Name                                          |
| ------------ | --------------------------------------------- |
| http (basic) | [Index Statistics](#security-IndexStatistics) |

#### [](#example-http-request)Example HTTP Request

Request 1: Return statistics for an index and format the output.

curl request

```sh
curl -X GET -u Administrator:password \
"http://localhost:9102/api/v1/stats/travel-sample.inventory.route/idx_partn?pretty=true"
```

Request 2: Return statistics for an index, include partitions, and format the output.

curl request

```sh
curl -X GET -u Administrator:password \
"http://localhost:9102/api/v1/stats/travel-sample.inventory.route/idx_partn?partition=true&pretty=true"
```

#### [](#example-http-response)Example HTTP Response

Result of [request 1](#index-example-1).

Response 200

```json
{
   "travel-sample:inventory:route:idx_partn": {
      "avg_drain_rate": 0,
      "avg_item_size": 41,
      "avg_scan_latency": 0,
      "cache_hit_percent": 100,
      "cache_hits": 12003,
      "cache_misses": 0,
      "data_size": 2495580,
      "disk_size": 2102624,
      "frag_percent": 64,
      "initial_build_progress": 100,
      "items_count": 12003,
      "last_known_scan_time": 0,
      "num_docs_indexed": 15778,
      "num_docs_pending": 0,
      "num_docs_queued": 0,
      "num_items_flushed": 15778,
      "num_pending_requests": 0,
      "num_requests": 0,
      "num_rows_returned": 0,
      "num_scan_errors": 0,
      "num_scan_timeouts": 0,
      "recs_in_mem": 15815,
      "recs_on_disk": 0,
      "resident_percent": 100,
      "scan_bytes_read": 0,
      "total_scan_duration": 0
   }
}
```

Result of [request 2](#index-example-2).

Response 200

```json
{
   "Partition-2": {
      "avg_drain_rate": 0,
      "avg_item_size": 41,
      "avg_scan_latency": 0,
      "cache_hit_percent": 100,
      "cache_hits": 3006,
      "cache_misses": 0,
      "data_size": 625087,
      "disk_size": 528728,
      "frag_percent": 65,
      "initial_build_progress": 0,
      "items_count": 3006,
      "last_known_scan_time": 0,
      "num_docs_indexed": 3926,
      "num_docs_pending": 0,
      "num_docs_queued": 0,
      "num_items_flushed": 3926,
      "num_pending_requests": 0,
      "num_requests": 0,
      "num_rows_returned": 0,
      "num_scan_errors": 0,
      "num_scan_timeouts": 0,
      "recs_in_mem": 4010,
      "recs_on_disk": 0,
      "resident_percent": 100,
      "scan_bytes_read": 0,
      "total_scan_duration": 0
   },
   "Partition-3": {
      "avg_drain_rate": 0,
      "avg_item_size": 41,
      "avg_scan_latency": 0,
      "cache_hit_percent": 100,
      "cache_hits": 2992,
      "cache_misses": 0,
      "data_size": 622348,
      "disk_size": 520536,
      "frag_percent": 64,
      "initial_build_progress": 0,
      "items_count": 2992,
      "last_known_scan_time": 0,
      "num_docs_indexed": 3933,
      "num_docs_pending": 0,
      "num_docs_queued": 0,
      "num_items_flushed": 3933,
      "num_pending_requests": 0,
      "num_requests": 0,
      "num_rows_returned": 0,
      "num_scan_errors": 0,
      "num_scan_timeouts": 0,
      "recs_in_mem": 3996,
      "recs_on_disk": 0,
      "resident_percent": 100,
      "scan_bytes_read": 0,
      "total_scan_duration": 0
   },
   "Partition-4": {
      "avg_drain_rate": 0,
      "avg_item_size": 41,
      "avg_scan_latency": 0,
      "cache_hit_percent": 100,
      "cache_hits": 3008,
      "cache_misses": 0,
      "data_size": 625267,
      "disk_size": 528728,
      "frag_percent": 65,
      "initial_build_progress": 0,
      "items_count": 3008,
      "last_known_scan_time": 0,
      "num_docs_indexed": 3965,
      "num_docs_pending": 0,
      "num_docs_queued": 0,
      "num_items_flushed": 3965,
      "num_pending_requests": 0,
      "num_requests": 0,
      "num_rows_returned": 0,
      "num_scan_errors": 0,
      "num_scan_timeouts": 0,
      "recs_in_mem": 4011,
      "recs_on_disk": 0,
      "resident_percent": 100,
      "scan_bytes_read": 0,
      "total_scan_duration": 0
   },
   "Partition-5": {
      "avg_drain_rate": 0,
      "avg_item_size": 41,
      "avg_scan_latency": 0,
      "cache_hit_percent": 100,
      "cache_hits": 2997,
      "cache_misses": 0,
      "data_size": 622878,
      "disk_size": 524632,
      "frag_percent": 64,
      "initial_build_progress": 0,
      "items_count": 2997,
      "last_known_scan_time": 0,
      "num_docs_indexed": 3954,
      "num_docs_pending": 0,
      "num_docs_queued": 0,
      "num_items_flushed": 3954,
      "num_pending_requests": 0,
      "num_requests": 0,
      "num_rows_returned": 0,
      "num_scan_errors": 0,
      "num_scan_timeouts": 0,
      "recs_in_mem": 3798,
      "recs_on_disk": 0,
      "resident_percent": 100,
      "scan_bytes_read": 0,
      "total_scan_duration": 0
   },
   "travel-sample:inventory:route:idx_partn": {
      "avg_drain_rate": 0,
      "avg_item_size": 41,
      "avg_scan_latency": 0,
      "cache_hit_percent": 100,
      "cache_hits": 12003,
      "cache_misses": 0,
      "data_size": 2495580,
      "disk_size": 2102624,
      "frag_percent": 64,
      "initial_build_progress": 100,
      "items_count": 12003,
      "last_known_scan_time": 0,
      "num_docs_indexed": 15778,
      "num_docs_pending": 0,
      "num_docs_queued": 0,
      "num_items_flushed": 15778,
      "num_pending_requests": 0,
      "num_requests": 0,
      "num_rows_returned": 0,
      "num_scan_errors": 0,
      "num_scan_timeouts": 0,
      "recs_in_mem": 15815,
      "recs_on_disk": 0,
      "resident_percent": 100,
      "scan_bytes_read": 0,
      "total_scan_duration": 0
   }
}
```

### [](#get%5Fkeyspace%5Fstats)Get Statistics for Indexes in a Keyspace

GET /api/v1/stats/{keyspace}

#### [](#get%5Fkeyspace%5Fstats-description)Description

Returns statistics for all indexes within a bucket, scope, or collection.

Produces

* application/json

#### [](#get%5Fkeyspace%5Fstats-parameters)Parameters

Path Parameters

| Name                 | Description                                                                                                                                                                                                                                                                                                                                                  | Schema |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------ |
| **keyspace**required | The name of a keyspace. This must contain a bucket name, which may be followed by an optional scope name and an optional collection name, separated by dots. For example, bucket.scope.collection. If any part of the keyspace name contains a dot, that part of the keyspace name must be wrapped in backticks. For example, \`bucket.1\`.scope.collection. | String |

Query Parameters

| Name                  | Description                                                                                   | Schema  |
| --------------------- | --------------------------------------------------------------------------------------------- | ------- |
| **pretty**optional    | Whether the output should be formatted with indentations and newlines. **Default:** false     | Boolean |
| **redact**optional    | Whether keyspace and index names should be redacted in the output. **Default:** false         | Boolean |
| **skipEmpty**optional | Whether empty, null, or zero statistics should be omitted from the output. **Default:** false | Boolean |

> [!NOTE]
> If the [keyspace](#get%5Fkeyspace%5Fstats-parameters) path parameter specifies just a bucket name, the response contains statistics for all indexes in all collections in all scopes within that bucket. If this parameter specifies a bucket name and a scope name, the response contains statistics for all indexes in all collections within that scope. Similarly, if this parameter specifies a bucket name, a scope name, and a collection, the response contains statistics for all indexes in that collection.
> 
> To get statistics for the indexes in the default collection in the default scope within a bucket only, you must specify the scope and collection explicitly. For example, `bucket._default._default`.

#### [](#get%5Fkeyspace%5Fstats-responses)Responses

| HTTP Code | Description                                                                                                                                                                                                                                                                         | Schema                     |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| 200       | Success. Returns an object containing one or more nested <keyspace>:<index> objects — one for each index found within the specified bucket, scope, or collection.                                                                                                                   | [Indexes](#PartIdxIndexes) |
| 404       | Not found. Returns the complete specified keyspace name, and the specified index name if provided. The keyspace name may be incorrect, the keyspace may contain no indexes, the index may not be located in the specified keyspace, or the index may be warming up after a restart. |                            |

#### [](#get%5Fkeyspace%5Fstats-security)Security

| Type         | Name                                          |
| ------------ | --------------------------------------------- |
| http (basic) | [Index Statistics](#security-IndexStatistics) |

#### [](#example-http-request-2)Example HTTP Request

Request 3: Return statistics for all indexes in a scope, omit empty results, and format the output.

curl request

```sh
curl -X GET -u Administrator:password \
"http://localhost:9102/api/v1/stats/travel-sample.inventory?pretty=true&skipEmpty=true"
```

Request 4: Return statistics for all indexes in a collection, omit empty results, and format the output.

curl request

```sh
curl -X GET -u Administrator:password \
"http://localhost:9102/api/v1/stats/travel-sample.inventory.airline?pretty=true&skipEmpty=true"
```

#### [](#example-http-response-2)Example HTTP Response

Result of [request 3](#keyspace-example-1).

Response 200

```json
{
   "travel-sample:inventory:airline:def_inventory_airline_primary": {
      "avg_item_size": 12,
      "avg_scan_latency": 2898606,
      "cache_hit_percent": 75,
      "cache_hits": 3,
      "cache_misses": 1,
      "data_size": 213281,
      "disk_size": 747993,
      "frag_percent": 79,
      "initial_build_progress": 100,
      "items_count": 187,
      "last_known_scan_time": 1620385003874921293,
      "memory_used": 12258,
      "num_requests": 4,
      "num_rows_returned": 748,
      "recs_in_mem": 187,
      "resident_percent": 100,
      "scan_bytes_read": 9016,
      "total_scan_duration": 12789504
   },
   "travel-sample:inventory:airport:def_inventory_airport_airportname": {
      "avg_item_size": 73,
      "data_size": 514569,
      "disk_size": 1664271,
      "frag_percent": 72,
      "initial_build_progress": 100,
      "items_count": 1968,
      "memory_used": 3880,
      "recs_on_disk": 1968
   },
   // ...
}
```

Result of [request 4](#keyspace-example-2).

Response 200

```json
{
   "travel-sample:inventory:airline:def_inventory_airline_primary": {
      "avg_item_size": 12,
      "avg_scan_latency": 2898606,
      "cache_hit_percent": 75,
      "cache_hits": 3,
      "cache_misses": 1,
      "data_size": 213281,
      "disk_size": 747993,
      "frag_percent": 79,
      "initial_build_progress": 100,
      "items_count": 187,
      "last_known_scan_time": 1620385003874921293,
      "memory_used": 12258,
      "num_requests": 4,
      "num_rows_returned": 748,
      "recs_in_mem": 187,
      "resident_percent": 100,
      "scan_bytes_read": 9016,
      "total_scan_duration": 12789504
   }
}
```

### [](#get%5Fnode%5Fstats)Get Statistics for an Index Node

GET /api/v1/stats

#### [](#get%5Fnode%5Fstats-description)Description

Returns statistics for an index node, and for all indexes on that node.

Produces

* application/json

#### [](#get%5Fnode%5Fstats-parameters)Parameters

Query Parameters

| Name                  | Description                                                                                   | Schema  |
| --------------------- | --------------------------------------------------------------------------------------------- | ------- |
| **pretty**optional    | Whether the output should be formatted with indentations and newlines. **Default:** false     | Boolean |
| **redact**optional    | Whether keyspace and index names should be redacted in the output. **Default:** false         | Boolean |
| **skipEmpty**optional | Whether empty, null, or zero statistics should be omitted from the output. **Default:** false | Boolean |

#### [](#get%5Fnode%5Fstats-responses)Responses

| HTTP Code | Description                                                                                                                                                                | Schema                       |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| 200       | Success. Returns an object containing a nested indexer object, and usually one or more nested <keyspace>:<index> objects — one for each index found on the specified node. | [Node and Indexes](#NodeIdx) |

#### [](#get%5Fnode%5Fstats-security)Security

| Type         | Name                                          |
| ------------ | --------------------------------------------- |
| http (basic) | [Index Statistics](#security-IndexStatistics) |
| http (basic) | [Node Statistics](#security-NodeStatistics)   |

#### [](#example-http-request-3)Example HTTP Request

Request 5: Return statistics for an index node and format the output.

curl request

```sh
curl -X GET -u Administrator:password \
"http://localhost:9102/api/v1/stats?pretty=true"
```

Request 6: Return statistics for an index node, omit empty results, and format the output.

curl request

```sh
curl -X GET -u Administrator:password \
"http://localhost:9102/api/v1/stats?skipEmpty=true&pretty=true"
```

Request 7: Return statistics for an index node, omit empty results, redact index names, and format the output.

curl request

```sh
curl -X GET -u Administrator:password \
"http://localhost:9102/api/v1/stats?skipEmpty=true&redact=true&pretty=true"
```

#### [](#example-http-response-3)Example HTTP Response

Result of [request 5](#node-example-1).

Response 200

```json
{
   "indexer": {
      "indexer_state": "Active",
      "memory_quota": 536870912,
      "memory_total_storage": 14708736,
      "memory_used": 290727936,
      "total_indexer_gc_pause_ns": 309778455
   },
   "travel-sample:def_airportname": {
      "avg_drain_rate": 0,
      "avg_item_size": 73,
      "avg_scan_latency": 0,
      "cache_hit_percent": 0,
      "cache_hits": 0,
      "cache_misses": 0,
      "data_size": 514623,
      "disk_size": 872448,
      "frag_percent": 56,
      "initial_build_progress": 100,
      "items_count": 1968,
      "last_known_scan_time": 0,
      "memory_used": 3498,
      "num_docs_indexed": 0,
      "num_docs_pending": 0,
      "num_docs_queued": 0,
      "num_items_flushed": 0,
      "num_pending_requests": 0,
      "num_requests": 0,
      "num_rows_returned": 0,
      "num_scan_errors": 0,
      "num_scan_timeouts": 0,
      "recs_in_mem": 0,
      "recs_on_disk": 1968,
      "resident_percent": 0,
      "scan_bytes_read": 0,
      "total_scan_duration": 0
   },
   "travel-sample:def_city": {
      "avg_drain_rate": 0,
      "avg_item_size": 59,
      "avg_scan_latency": 0,
      "cache_hit_percent": 0,
      "cache_hits": 0,
      "cache_misses": 0,
      "data_size": 1083447,
      "disk_size": 1138688,
      "frag_percent": 56,
      "initial_build_progress": 100,
      "items_count": 7380,
      "last_known_scan_time": 0,
      "memory_used": 16330,
      "num_docs_indexed": 0,
      "num_docs_pending": 0,
      "num_docs_queued": 0,
      "num_items_flushed": 0,
      "num_pending_requests": 0,
      "num_requests": 0,
      "num_rows_returned": 0,
      "num_scan_errors": 0,
      "num_scan_timeouts": 0,
      "recs_in_mem": 0,
      "recs_on_disk": 7380,
      "resident_percent": 0,
      "scan_bytes_read": 0,
      "total_scan_duration": 0
   },
   // ...
   }
}
```

Result of [request 6](#node-example-2).

Response 200

```json
{
   "indexer": {
      "indexer_state": "Active",
      "memory_quota": 536870912,
      "memory_total_storage": 14708736,
      "memory_used": 376973312,
      "total_indexer_gc_pause_ns": 72809334
   },
   "travel-sample:def_airportname": {
      "avg_item_size": 73,
      "data_size": 514623,
      "disk_size": 872448,
      "frag_percent": 56,
      "initial_build_progress": 100,
      "items_count": 1968,
      "memory_used": 3498,
      "recs_on_disk": 1968
   },
   "travel-sample:def_city": {
      "avg_item_size": 59,
      "data_size": 1083447,
      "disk_size": 1138688,
      "frag_percent": 56,
      "initial_build_progress": 100,
      "items_count": 7380,
      "memory_used": 16330,
      "recs_on_disk": 7380
   },
   // ...
}
```

Result of [request 7](#node-example-3).

Response 200

```json
{
   "10862128657611330848": {
      "avg_item_size": 73,
      "data_size": 514623,
      "disk_size": 872448,
      "frag_percent": 56,
      "initial_build_progress": 100,
      "items_count": 1968,
      "memory_used": 3498,
      "recs_on_disk": 1968
   },
   "1358505159407317360": {
      "avg_item_size": 59,
      "data_size": 1083447,
      "disk_size": 1138688,
      "frag_percent": 56,
      "initial_build_progress": 100,
      "items_count": 7380,
      "memory_used": 16330,
      "recs_on_disk": 7380
   },
   // ...
   "indexer": {
      "indexer_state": "Active",
      "memory_quota": 536870912,
      "memory_total_storage": 14708736,
      "memory_used": 376973312,
      "total_indexer_gc_pause_ns": 72809334
   }
}
```

## [](#models)Definitions

This section describes the properties consumed and returned by this REST API.

[Node and Indexes](#NodeIdx)  
[Nodes](#NodeIdxNode)  
[Node](#NodeIdxNodeIndexer)  
[Index and Partitions](#PartIdx)  
[Indexes](#PartIdxIndexes)  
[Partitions](#PartIdxPartitions)  
[Index](#PartIdxPartitionsIndex)

### [](#NodeIdx)Node and Indexes

 Composite Schema

| All of …​ |                   | Schema                     |
| --------- | ----------------- | -------------------------- |
|           | Node statistics.  | [Nodes](#NodeIdxNode)      |
| and       | Index statistics. | [Indexes](#PartIdxIndexes) |

#### Nodes

 Object

| Property            |                                                                   | Schema                      |
| ------------------- | ----------------------------------------------------------------- | --------------------------- |
| **indexer**required | A nested object containing statistics for the current index node. | [Node](#NodeIdxNodeIndexer) |

#### Node

 Object

| Property                                  |                                                                                                                                                                                                          | Schema       |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| **indexer\_state**optional                | Current state of the Index service on this node. **Values:** "Active", "Pause", "Warmup" **Example:** "Active"                                                                                           | String       |
| **memory\_quota**optional                 | Memory quota assigned to the Index service on this node by user configuration (bytes). **Default:** 268435456 **Maximum:** 1099511992567 **Example:** 536870912                                          | Long (int64) |
| **memory\_total\_storage**optional        | [ENTERPRISE EDITION](https://www.couchbase.com/products/editions) The total size allocated in the indexer across all indexes (bytes). This also accounts for memory fragmentation. **Example:** 71794688 | Integer      |
| **memory\_used**optional                  | Amount of memory used by the Index service on this node (bytes). **Example:** 360192000                                                                                                                  | Integer      |
| **total\_indexer\_gc\_pause\_ns**optional | The total time the indexer has spent in GC pause since last startup (ns). **Example:** 309778455                                                                                                         | Integer      |

### [](#PartIdx)Index and Partitions

 Composite Schema

| All of …​ |                             | Schema                           |
| --------- | --------------------------- | -------------------------------- |
|           | Index statistics.           | [Indexes](#PartIdxIndexes)       |
| and       | Index partition statistics. | [Partitions](#PartIdxPartitions) |

### [](#PartIdxIndexes)Indexes

 Object

| Property           |                                                                        | Schema                           |
| ------------------ | ---------------------------------------------------------------------- | -------------------------------- |
| additionalproperty | A nested object containing statistics for an index or index partition. | [Index](#PartIdxPartitionsIndex) |

> [!NOTE]
> By default, the name of the nested object has the form `<keyspace>:<index>`.
> 
> * `<keyspace>` is the bucket, scope, and collection containing the index.
> * `<index>` is the name of the index.
> 
> If the `redact` query parameter was set to `true`, the name of the nested object is replaced by the index instance ID for confidentiality.

#### Partitions

 Object

| Property           |                                                                        | Schema                           |
| ------------------ | ---------------------------------------------------------------------- | -------------------------------- |
| additionalproperty | A nested object containing statistics for an index or index partition. | [Index](#PartIdxPartitionsIndex) |

> [!NOTE]
> The name of the nested object has the form `Partition-<num>`.
> 
> * If the index is partitioned, this object contains statistics for one index partition, where `<num>` is the partition number.
> * If the index is not partitioned, this object contains statistics for the entire index, and `<num>` is `0`.

#### Index

 Object

| Property                             |                                                                                                                                                                                                                                                                      | Schema       |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| **avg\_array\_length**optional       | (Array indexes only.) The average number of items indexed per document.                                                                                                                                                                                              | Integer      |
| **avg\_drain\_rate**optional         | Average number of items flushed from memory to disk storage per second.                                                                                                                                                                                              | Integer      |
| **avg\_item\_size**optional          | Average size of the keys.                                                                                                                                                                                                                                            | Integer      |
| **avg\_scan\_latency**optional       | Average time to serve a scan request (nanoseconds).                                                                                                                                                                                                                  | Integer      |
| **cache\_hit\_percent**optional      | [ENTERPRISE EDITION](https://www.couchbase.com/products/editions) Percentage of memory accesses that were served from the managed cache.                                                                                                                             | Integer      |
| **cache\_hits**optional              | Accesses to this index data from RAM.                                                                                                                                                                                                                                | Integer      |
| **cache\_misses**optional            | Accesses to this index data from disk.                                                                                                                                                                                                                               | Integer      |
| **data\_size**optional               | The size of indexable data that's maintained for the index or partition (bytes). **Example:** 95728                                                                                                                                                                  | Integer      |
| **disk\_size**optional               | Total disk file size consumed by the index or partition. **Example:** 889054                                                                                                                                                                                         | Integer      |
| **docid\_count**optional             | (Array indexes only.) The number of documents currently indexed.                                                                                                                                                                                                     | Integer      |
| **frag\_percent**optional            | Percentage fragmentation of the index. TIP: At small index sizes of less than a hundred kB, the static overhead of the index disk file will inflate the index fragmentation percentage.                                                                              | Integer      |
| **initial\_build\_progress**optional | Percentage initial build progress for the index. When initial build is completed, the value is 100. For an index partition, the value is listed as 0. **Example:** 100                                                                                               | Integer      |
| **items\_count**optional             | The number of items currently indexed. **Example:** 2155                                                                                                                                                                                                             | Integer      |
| **last\_known\_scan\_time**optional  | Time of the last scan request received for this index (Unix timestamp in nanoseconds). This may be useful for determining whether this index is currently unused. This statistic is persisted to disk every 15 minutes, so it's preserved when the indexer restarts. | Long (int64) |
| **num\_docs\_indexed**optional       | Number of documents indexed by the indexer since last startup.                                                                                                                                                                                                       | Integer      |
| **num\_docs\_pending**optional       | Number of documents pending to be indexed.                                                                                                                                                                                                                           | Integer      |
| **num\_docs\_queued**optional        | Number of documents queued to be indexed.                                                                                                                                                                                                                            | Integer      |
| **num\_items\_flushed**optional      | Number of items flushed from memory to disk storage.                                                                                                                                                                                                                 | Integer      |
| **num\_pending\_requests**optional   | Number of requests received but not yet served by the indexer.                                                                                                                                                                                                       | Integer      |
| **num\_requests**optional            | Number of requests served by the indexer since last startup.                                                                                                                                                                                                         | Integer      |
| **num\_rows\_returned**optional      | Total number of rows returned so far by the indexer.                                                                                                                                                                                                                 | Integer      |
| **num\_scan\_errors**optional        | Number of requests that failed due to errors other than timeout.                                                                                                                                                                                                     | Integer      |
| **num\_scan\_timeouts**optional      | Number of requests that timed out, either waiting for snapshots or during scan in progress.                                                                                                                                                                          | Integer      |
| **recs\_in\_mem**optional            | [ENTERPRISE EDITION](https://www.couchbase.com/products/editions) For standard index storage, this is the number of records in this index that are stored in memory. For memory-optimized index storage, this is the same as items\_count. **Example:** 2155         | Integer      |
| **recs\_on\_disk**optional           | [ENTERPRISE EDITION](https://www.couchbase.com/products/editions) For standard index storage, this is the number of records in this index that are stored on disk. For memory-optimized index storage, this is 0.                                                    | Integer      |
| **resident\_percent**optional        | [ENTERPRISE EDITION](https://www.couchbase.com/products/editions) Percentage of the data held in memory. **Example:** 100                                                                                                                                            | Integer      |
| **scan\_bytes\_read**optional        | Number of bytes read by a scan since last startup.                                                                                                                                                                                                                   | Integer      |
| **total\_scan\_duration**optional    | Total time spent by the indexer in scanning rows since last startup (nanoseconds).                                                                                                                                                                                   | Integer      |

## [](#security)Security

The Index Statistics API supports admin credentials. Pass your credentials through HTTP headers (HTTP basic authentication).

### [](#security-NodeStatistics)Node Statistics

To get [Node statistics](#NodeIdxNodeIndexer), users must have the Query System Catalog RBAC role.

**Type:** http

### [](#security-IndexStatistics)Index Statistics

To get [Index statistics](#PartIdxPartitionsIndex) for all indexes in a bucket, scope, or collection, users must have the Query System Catalog RBAC role, or the Query Manage Index RBAC role with permissions on that bucket, scope, or collection.

To get [Index statistics](#PartIdxPartitionsIndex) for an individual index, users must have the Query System Catalog RBAC role, or the Query Manage Index RBAC role with permissions on the bucket, scope, and collection containing that index.

**Type:** http

For more information, see [Roles](../learn/security/roles.md).