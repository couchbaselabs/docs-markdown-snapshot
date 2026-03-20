---
title: Index Statistics API
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/rest-api/pages/rest-index-stats.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:rest-api:rest-index-stats.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/rest-api/rest-index-stats.html)

# Index Statistics API

## [](#%5Foverview)Overview

The Index Statistics REST API is provided by the Index service. This API enables you to get Index service statistics.

The API schemes and host URLs are as follows:

* <http://node:9102/>
* <https://node:19102/> (for secure access)

where `node` is the host name or IP address of a computer running the index service.

### [](#version-information)Version information

_Version_ : 7.2

### [](#produces)Produces

* `application/json`

## [](#%5Fpaths)Paths

This section describes the operations available with this REST API.

**Table of Contents**

* [Get Statistics for an Index Node](#%5Fget%5Fnode%5Fstats)
* [Get Statistics for Indexes in a Keyspace](#%5Fget%5Fkeyspace%5Fstats)
* [Get Statistics for an Index](#%5Fget%5Findex%5Fstats)

### [](#%5Fget%5Fnode%5Fstats)Get Statistics for an Index Node

GET /api/v1/stats

#### [](#description)Description

Returns statistics for an index node, and for all indexes on that node.

#### [](#%5Fget%5Fnode%5Fstats%5Fparameters)Parameters

| Type      | Name                     | Description                                                                | Schema  | Default |
| --------- | ------------------------ | -------------------------------------------------------------------------- | ------- | ------- |
| **Query** | **pretty** _optional_    | Whether the output should be formatted with indentations and newlines.     | boolean | "false" |
| **Query** | **redact** _optional_    | Whether keyspace and index names should be redacted in the output.         | boolean | "false" |
| **Query** | **skipEmpty** _optional_ | Whether empty, null, or zero statistics should be omitted from the output. | boolean | "false" |

#### [](#responses)Responses

| HTTP Code | Description                                                                                                                                                                | Schema                                       |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| **200**   | Success. Returns an object containing a nested indexer object, and usually one or more nested <keyspace>:<index> objects — one for each index found on the specified node. | [Node and Indexes](#%5Fnode%5Fand%5Findexes) |

**Node and Indexes**

| Name                              | Description                                                                                                                                                                                                                                                                                                                                      | Schema             |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------ |
| **indexer** _required_            | A nested object containing statistics for the current index node.                                                                                                                                                                                                                                                                                | [Node](#%5Fnode)   |
| **<keyspace>:<index>** _optional_ | A nested object containing statistics for an entire index. <keyspace> is the bucket, scope, and collection containing the index. <index> is the name of the index. If the [redact](#%5Fget%5Fnode%5Fstats%5Fparameters) query parameter was set to true, the keyspace and index names are replaced by the index instance ID for confidentiality. | [Index](#%5Findex) |

#### [](#security)Security

| Type      | Name                                           |
| --------- | ---------------------------------------------- |
| **basic** | **[Node Statistics](#%5Fnode%5Fstatistics)**   |
| **basic** | **[Index Statistics](#%5Findex%5Fstatistics)** |

#### [](#example-http-request)Example HTTP request

Request 1: Return statistics for an index node and format the output.

Curl request

```sh
curl -X GET -u Administrator:password \
"http://localhost:9102/api/v1/stats?pretty=true"
```

Request 2: Return statistics for an index node, omit empty results, and format the output.

Curl request

```sh
curl -X GET -u Administrator:password \
"http://localhost:9102/api/v1/stats?skipEmpty=true&pretty=true"
```

Request 3: Return statistics for an index node, omit empty results, redact index names, and format the output.

Curl request

```sh
curl -X GET -u Administrator:password \
"http://localhost:9102/api/v1/stats?skipEmpty=true&redact=true&pretty=true"
```

#### [](#example-http-response)Example HTTP response

Result of [request 1](#node-example-1).

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

Result of [request 2](#node-example-2).

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

Result of [request 3](#node-example-3).

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

### [](#%5Fget%5Fkeyspace%5Fstats)Get Statistics for Indexes in a Keyspace

GET /api/v1/stats/{keyspace}

#### [](#description-2)Description

Returns statistics for all indexes within a bucket, scope, or collection.

#### [](#%5Fget%5Fkeyspace%5Fstats%5Fparameters)Parameters

| Type      | Name                     | Description                                                                                                                                                                                                                                                                                                                                                  | Schema  | Default |
| --------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- | ------- |
| **Path**  | **keyspace** _required_  | The name of a keyspace. This must contain a bucket name, which may be followed by an optional scope name and an optional collection name, separated by dots. For example, bucket.scope.collection. If any part of the keyspace name contains a dot, that part of the keyspace name must be wrapped in backticks. For example, \`bucket.1\`.scope.collection. | string  |         |
| **Query** | **pretty** _optional_    | Whether the output should be formatted with indentations and newlines.                                                                                                                                                                                                                                                                                       | boolean | "false" |
| **Query** | **redact** _optional_    | Whether keyspace and index names should be redacted in the output.                                                                                                                                                                                                                                                                                           | boolean | "false" |
| **Query** | **skipEmpty** _optional_ | Whether empty, null, or zero statistics should be omitted from the output.                                                                                                                                                                                                                                                                                   | boolean | "false" |

> [!NOTE]
> If the [keyspace](#%5Fget%5Fkeyspace%5Fstats%5Fparameters) path parameter specifies just a bucket name, the response contains statistics for all indexes in all collections in all scopes within that bucket. If this parameter specifies a bucket name and a scope name, the response contains statistics for all indexes in all collections within that scope. Similarly, if this parameter specifies a bucket name, a scope name, and a collection, the response contains statistics for all indexes in that collection.
> 
> To get statistics for the indexes in the default collection in the default scope within a bucket only, you must specify the scope and collection explicitly. For example, `bucket._default._default`.

#### [](#responses-2)Responses

| HTTP Code | Description                                                                                                                                                                                                                                                                         | Schema                 |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| **200**   | Success. Returns an object containing one or more nested <keyspace>:<index> objects — one for each index found within the specified bucket, scope, or collection.                                                                                                                   | [Indexes](#%5Findexes) |
| **404**   | Not found. Returns the complete specified keyspace name, and the specified index name if provided. The keyspace name may be incorrect, the keyspace may contain no indexes, the index may not be located in the specified keyspace, or the index may be warming up after a restart. | string                 |

**Indexes**

| Name                              | Description                                                                                                                                                                                                                                                                                                                                          | Schema             |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| **<keyspace>:<index>** _required_ | A nested object containing statistics for an entire index. <keyspace> is the bucket, scope, and collection containing the index. <index> is the name of the index. If the [redact](#%5Fget%5Fkeyspace%5Fstats%5Fparameters) query parameter was set to true, the keyspace and index names are replaced by the index instance ID for confidentiality. | [Index](#%5Findex) |

#### [](#security-2)Security

| Type      | Name                                           |
| --------- | ---------------------------------------------- |
| **basic** | **[Index Statistics](#%5Findex%5Fstatistics)** |

#### [](#example-http-request-2)Example HTTP request

Request 4: Return statistics for all indexes in a scope, omit empty results, and format the output.

Curl request

```sh
curl -X GET -u Administrator:password \
"http://localhost:9102/api/v1/stats/travel-sample.inventory?pretty=true&skipEmpty=true"
```

Request 5: Return statistics for all indexes in a collection, omit empty results, and format the output.

Curl request

```sh
curl -X GET -u Administrator:password \
"http://localhost:9102/api/v1/stats/travel-sample.inventory.airline?pretty=true&skipEmpty=true"
```

#### [](#example-http-response-2)Example HTTP response

Result of [request 4](#keyspace-example-1).

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

Result of [request 5](#keyspace-example-2).

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

### [](#%5Fget%5Findex%5Fstats)Get Statistics for an Index

GET /api/v1/stats/{keyspace}/{index}

#### [](#description-3)Description

Returns statistics for an index.

#### [](#%5Fget%5Findex%5Fstats%5Fparameters)Parameters

| Type      | Name                     | Description                                                                                                                                                                                                                                                                                                                                                  | Schema  | Default |
| --------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- | ------- |
| **Path**  | **keyspace** _required_  | The name of a keyspace. This must contain a bucket name, which may be followed by an optional scope name and an optional collection name, separated by dots. For example, bucket.scope.collection. If any part of the keyspace name contains a dot, that part of the keyspace name must be wrapped in backticks. For example, \`bucket.1\`.scope.collection. | string  |         |
| **Path**  | **index** _required_     | The name of an index.                                                                                                                                                                                                                                                                                                                                        | string  |         |
| **Query** | **pretty** _optional_    | Whether the output should be formatted with indentations and newlines.                                                                                                                                                                                                                                                                                       | boolean | "false" |
| **Query** | **partition** _optional_ | Whether statistics for index partitions should be included.                                                                                                                                                                                                                                                                                                  | boolean | "false" |
| **Query** | **redact** _optional_    | Whether keyspace and index names should be redacted in the output.                                                                                                                                                                                                                                                                                           | boolean | "false" |
| **Query** | **skipEmpty** _optional_ | Whether empty, null, or zero statistics should be omitted from the output.                                                                                                                                                                                                                                                                                   | boolean | "false" |

> [!NOTE]
> In most cases, the [keyspace](#%5Fget%5Findex%5Fstats%5Fparameters) path parameter must specify the complete name of the keyspace containing the index. It may not omit the scope name or the collection name.
> 
> However, if the specified index is stored in the default collection in the default scope within a bucket, then the [keyspace](#%5Fget%5Findex%5Fstats%5Fparameters) path parameter may specify just the bucket name alone.

> [!TIP]
> It is not possible to specify an individual index partition in the path.

#### [](#responses-3)Responses

| HTTP Code | Description                                                                                                                                                                                                                                                                                             | Schema                                               |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| **200**   | Success. Returns an object containing one nested <keyspace>:<index> object. If the [partition](#%5Fget%5Findex%5Fstats%5Fparameters) query parameter was set to true, the returned object also contains one or more Partition-<num> objects — one for each index partition found on the specified node. | [Index and Partitions](#%5Findex%5Fand%5Fpartitions) |
| **404**   | Not found. Returns the complete specified keyspace name, and the specified index name if provided. The keyspace name may be incorrect, the keyspace may contain no indexes, the index may not be located in the specified keyspace, or the index may be warming up after a restart.                     | string                                               |

**Index and Partitions**

| Name                              | Description                                                                                                                                                                                                                                                                                                                                       | Schema             |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| **<keyspace>:<index>** _required_ | A nested object containing statistics for an entire index. <keyspace> is the bucket, scope, and collection containing the index. <index> is the name of the index. If the [redact](#%5Fget%5Findex%5Fstats%5Fparameters) query parameter was set to true, the keyspace and index names are replaced by the index instance ID for confidentiality. | [Index](#%5Findex) |
| **Partition-<num>** _optional_    | A nested object containing statistics. If the index is partitioned, this object contains statistics for one index partition, where <num> is the partition number. If the index is not partitioned, this object contains statistics for the entire index, and <num> is 0.                                                                          | [Index](#%5Findex) |

#### [](#security-3)Security

| Type      | Name                                           |
| --------- | ---------------------------------------------- |
| **basic** | **[Index Statistics](#%5Findex%5Fstatistics)** |

#### [](#example-http-request-3)Example HTTP request

Request 6: Return statistics for an index and format the output.

Curl request

```sh
curl -X GET -u Administrator:password \
"http://localhost:9102/api/v1/stats/travel-sample.inventory.route/idx_partn?pretty=true"
```

Request 7: Return statistics for an index, include partitions, and format the output.

Curl request

```sh
curl -X GET -u Administrator:password \
"http://localhost:9102/api/v1/stats/travel-sample.inventory.route/idx_partn?partition=true&pretty=true"
```

#### [](#example-http-response-3)Example HTTP response

Result of [request 6](#index-example-1).

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

Result of [request 7](#index-example-2).

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

## [](#%5Fdefinitions)Definitions

This section describes the properties returned by this REST API.

**Table of Contents**

* [Node](#%5Fnode)
* [Index](#%5Findex)

### [](#%5Fnode)Node

| Name                                         | Description                                                                                                                                                                                               | Schema                       |
| -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| **indexer\_state** _optional_                | Current state of the Index service on this node. **Example** : "Active"                                                                                                                                   | enum (Active, Pause, Warmup) |
| **memory\_quota** _optional_                 | Memory quota assigned to the Index service on this node by user configuration (bytes). **Default** : 268435456 **Maximum value** : 1099511992567 **Example** : 536870912                                  | integer (int64)              |
| **memory\_total\_storage** _optional_        | [ENTERPRISE EDITION](https://www.couchbase.com/products/editions) The total size allocated in the indexer across all indexes (bytes). This also accounts for memory fragmentation. **Example** : 71794688 | integer                      |
| **memory\_used** _optional_                  | Amount of memory used by the Index service on this node (bytes). **Example** : 360192000                                                                                                                  | integer                      |
| **total\_indexer\_gc\_pause\_ns** _optional_ | The total time the indexer has spent in GC pause since last startup (ns). **Example** : 309778455                                                                                                         | integer                      |

### [](#%5Findex)Index

| Name                                    | Description                                                                                                                                                                                                                                                           | Schema          |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| **avg\_array\_length** _optional_       | (Array indexes only.) The average number of items indexed per document.                                                                                                                                                                                               | integer         |
| **avg\_drain\_rate** _optional_         | Average number of items flushed from memory to disk storage per second.                                                                                                                                                                                               | integer         |
| **avg\_item\_size** _optional_          | Average size of the keys.                                                                                                                                                                                                                                             | integer         |
| **avg\_scan\_latency** _optional_       | Average time to serve a scan request (nanoseconds).                                                                                                                                                                                                                   | integer         |
| **cache\_hit\_percent** _optional_      | [ENTERPRISE EDITION](https://www.couchbase.com/products/editions) Percentage of memory accesses that were served from the managed cache.                                                                                                                              | integer         |
| **cache\_hits** _optional_              | Accesses to this index data from RAM.                                                                                                                                                                                                                                 | integer         |
| **cache\_misses** _optional_            | Accesses to this index data from disk.                                                                                                                                                                                                                                | integer         |
| **data\_size** _optional_               | The size of indexable data that is maintained for the index or partition (bytes). **Example** : 95728                                                                                                                                                                 | integer         |
| **disk\_size** _optional_               | Total disk file size consumed by the index or partition. **Example** : 889054                                                                                                                                                                                         | integer         |
| **docid\_count** _optional_             | (Array indexes only.) The number of documents currently indexed.                                                                                                                                                                                                      | integer         |
| **frag\_percent** _optional_            | Percentage fragmentation of the index. At small index sizes of less than a hundred kB, the static overhead of the index disk file will inflate the index fragmentation percentage.                                                                                    | integer         |
| **initial\_build\_progress** _optional_ | Percentage initial build progress for the index. When initial build is completed, the value is 100. For an index partition, the value is listed as 0. **Example** : 100                                                                                               | integer         |
| **items\_count** _optional_             | The number of items currently indexed. **Example** : 2155                                                                                                                                                                                                             | integer         |
| **last\_known\_scan\_time** _optional_  | Time of the last scan request received for this index (Unix timestamp in nanoseconds). This may be useful for determining whether this index is currently unused. This statistic is persisted to disk every 15 minutes, so it is preserved when the indexer restarts. | integer (int64) |
| **num\_docs\_indexed** _optional_       | Number of documents indexed by the indexer since last startup.                                                                                                                                                                                                        | integer         |
| **num\_docs\_pending** _optional_       | Number of documents pending to be indexed.                                                                                                                                                                                                                            | integer         |
| **num\_docs\_queued** _optional_        | Number of documents queued to be indexed.                                                                                                                                                                                                                             | integer         |
| **num\_items\_flushed** _optional_      | Number of items flushed from memory to disk storage.                                                                                                                                                                                                                  | integer         |
| **num\_pending\_requests** _optional_   | Number of requests received but not yet served by the indexer.                                                                                                                                                                                                        | integer         |
| **num\_requests** _optional_            | Number of requests served by the indexer since last startup.                                                                                                                                                                                                          | integer         |
| **num\_rows\_returned** _optional_      | Total number of rows returned so far by the indexer.                                                                                                                                                                                                                  | integer         |
| **num\_scan\_errors** _optional_        | Number of requests that failed due to errors other than timeout.                                                                                                                                                                                                      | integer         |
| **num\_scan\_timeouts** _optional_      | Number of requests that timed out, either waiting for snapshots or during scan in progress.                                                                                                                                                                           | integer         |
| **recs\_in\_mem** _optional_            | [ENTERPRISE EDITION](https://www.couchbase.com/products/editions) For standard index storage, this is the number of records in this index that are stored in memory. For memory-optimized index storage, this is the same as items\_count. **Example** : 2155         | integer         |
| **recs\_on\_disk** _optional_           | [ENTERPRISE EDITION](https://www.couchbase.com/products/editions) For standard index storage, this is the number of records in this index that are stored on disk. For memory-optimized index storage, this is 0.                                                     | integer         |
| **resident\_percent** _optional_        | [ENTERPRISE EDITION](https://www.couchbase.com/products/editions) Percentage of the data held in memory. **Example** : 100                                                                                                                                            | integer         |
| **scan\_bytes\_read** _optional_        | Number of bytes read by a scan since last startup.                                                                                                                                                                                                                    | integer         |
| **total\_scan\_duration** _optional_    | Total time spent by the indexer in scanning rows since last startup (nanoseconds).                                                                                                                                                                                    | integer         |

## [](#%5Fsecurityscheme)Security

The Index Statistics API supports admin credentials. Credentials can be passed via HTTP headers (HTTP basic authentication).

### [](#%5Fnode%5Fstatistics)Node Statistics

To get [Node statistics](#%5Fnode), users must have the Query System Catalog RBAC role.

_Type_ : basic

### [](#%5Findex%5Fstatistics)Index Statistics

To get [Index statistics](#%5Findex) for all indexes in a bucket, scope, or collection, users must have the Query System Catalog RBAC role, or the Query Manage Index RBAC role with permissions on that bucket, scope, or collection.

To get [Index statistics](#%5Findex) for an individual index, users must have the Query System Catalog RBAC role, or the Query Manage Index RBAC role with permissions on the bucket, scope, and collection containing that index.

_Type_ : basic

Refer to [Roles](../learn/security/roles.md) for more details.