---
title: Search API
description: The Search API supports the creation and management of indexes for
  <em>Full Text Search</em>.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/rest-api/pages/rest-fts.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:rest-api:rest-fts.adoc[]
---

[View original HTML](/server/current/rest-api/rest-fts.html)

# Search API

## [](#apis-in-this-section)APIs in this Section

For Full Text Search, REST endpoints can be reached on Search-Service nodes on port 8094, or on 18094 when using SSL.

For information on required roles and permissions, see [Roles](../learn/security/roles.md).

For a list of the methods and URIs covered by these pages in this section, see the tables below.

### [](#node-configuration)Node Configuration

| HTTP Method | URI              | Documented at                                                                 |
| ----------- | ---------------- | ----------------------------------------------------------------------------- |
| GET         | /api/cfg         | [Get Cluster Configuration](../fts-rest-nodes/index.md#getClusterConfig)      |
| POST        | /api/cfgRefresh  | [Refresh Node Configuration](../fts-rest-nodes/index.md#refreshClusterConfig) |
| POST        | /api/managerKick | [Replan Resource Assignments](../fts-rest-nodes/index.md#managerKick)         |
| GET         | /api/managerMeta | [Get Node Capabilities](../fts-rest-nodes/index.md#managerMeta)               |

### [](#node-diagnostics)Node Diagnostics

| HTTP Method | URI                         | Documented at                                                                           |
| ----------- | --------------------------- | --------------------------------------------------------------------------------------- |
| GET         | /api/diag                   | [Get Diagnostics](../fts-rest-nodes/index.md#getDiagnostics)                            |
| GET         | /api/log                    | [Get Node Logs](../fts-rest-nodes/index.md#getLogs)                                     |
| GET         | /api/runtime                | [Get Node Runtime Information](../fts-rest-nodes/index.md#getRuntimeInfo)               |
| GET         | /api/runtime/args           | [Get Node Runtime Arguments](../fts-rest-nodes/index.md#getRuntimeArgs)                 |
| POST        | /api/runtime/profile/cpu    | [Capture CPU Profiling Information](../fts-rest-nodes/index.md#captureCpuProfile)       |
| POST        | /api/runtime/profile/memory | [Capture Memory Profiling Information](../fts-rest-nodes/index.md#captureMemoryProfile) |

### [](#node-management)Node Management

| HTTP Method | URI             | Documented at                                                      |
| ----------- | --------------- | ------------------------------------------------------------------ |
| POST        | /api/runtime/gc | [Perform Garbage Collection](../fts-rest-nodes/index.md#performGC) |

### [](#node-monitoring)Node Monitoring

| HTTP Method | URI                         | Documented at                                                        |
| ----------- | --------------------------- | -------------------------------------------------------------------- |
| GET         | /api/runtime/stats          | [Get Runtime Statistics](../fts-rest-nodes/index.md#getRuntimeStats) |
| GET         | /api/runtime/stats/statsMem | [Get Memory Statistics](../fts-rest-nodes/index.md#getMemoryStats)   |

### [](#index-definition)Index Definition

| HTTP Method | URI                                                                | Documented at                                                                                          |
| ----------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| GET         | /api/bucket/{BUCKET\_NAME}/scope/{SCOPE\_NAME}/index               | [Get All Search Index Definitions (Scoped)](../fts-rest-indexing/index.md#g-api-scoped-index)          |
| GET         | /api/bucket/{BUCKET\_NAME}/scope/{SCOPE\_NAME}/index/{INDEX\_NAME} | [Get Index Definition (Scoped)](../fts-rest-indexing/index.md#g-api-scoped-index-name)                 |
| PUT         | /api/bucket/{BUCKET\_NAME}/scope/{SCOPE\_NAME}/index/{INDEX\_NAME} | [Create or Update an Index Definition (Scoped)](../fts-rest-indexing/index.md#p-api-scoped-index-name) |
| DELETE      | /api/bucket/{BUCKET\_NAME}/scope/{SCOPE\_NAME}/index/{INDEX\_NAME} | [Delete Index Definition (Scoped)](../fts-rest-indexing/index.md#d-api-scoped-index-name)              |

### [](#index-management)Index Management

| HTTP Method | URI                                                                                       | Documented at                                                                                              |
| ----------- | ----------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| POST        | /api/bucket/{BUCKET\_NAME}/scope/{SCOPE\_NAME}/index/{INDEX\_NAME}/ingestControl/{OP}     | [Set Index Ingestion Control (Scoped)](../fts-rest-indexing/index.md#p-api-scoped-ingestcontrol)           |
| POST        | /api/bucket/{BUCKET\_NAME}/scope/{SCOPE\_NAME}/index/{INDEX\_NAME}/planFreezeControl/{OP} | [Freeze Index Partition Assignment (Scoped)](../fts-rest-indexing/index.md#p-api-scoped-planfreezecontrol) |
| POST        | /api/bucket/{BUCKET\_NAME}/scope/{SCOPE\_NAME}/index/{INDEX\_NAME}/queryControl/{OP}      | [Stop Queries on an Index (Scoped)](../fts-rest-indexing/index.md#p-api-scoped-querycontrol)               |

### [](#index-monitoring-and-debugging)Index Monitoring and Debugging

| HTTP Method | URI                                                                       | Documented at                                                                                      |
| ----------- | ------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| GET         | /api/stats                                                                | [Get Indexing and Data Metrics for All Indexes](../fts-rest-indexing/index.md#g-api-stats)         |
| GET         | /api/stats/{INDEX\_NAME}                                                  | [Get Indexing and Data Metrics for an Index](../fts-rest-indexing/index.md#g-api-stats-index-name) |
| POST        | /api/stats/{INDEX\_NAME}/analyzeDoc                                       | [Analyze Document](../fts-rest-indexing/index.md#g-api-stats-index-name-analyzeDoc)                |
| GET         | /api/bucket/{BUCKET\_NAME}/scope/{SCOPE\_NAME}/index/{INDEX\_NAME}/status | [Get Index Status (Scoped)](../fts-rest-indexing/index.md#g-api-scoped-status)                     |

### [](#index-querying)Index Querying

| HTTP Method | URI                                                                             | Documented at                                                                                            |
| ----------- | ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| GET         | /api/index/{INDEX\_NAME}/count                                                  | [Get Document Count for an Index](../fts-rest-indexing/index.md#g-api-index-name-count)                  |
| POST        | /api/bucket/{BUCKET\_NAME}/scope/{SCOPE\_NAME}/index/{INDEX\_NAME}/pindexLookup | [Look up the Index Partition for a Document (Scoped)](../fts-rest-indexing/index.md#p-api-pindex-lookup) |
| POST        | /api/bucket/{BUCKET\_NAME}/scope/{SCOPE\_NAME}/index/{INDEX\_NAME}/query        | [Query a Search Index (Scoped)](../fts-rest-indexing/index.md#p-api-scoped-query)                        |

### [](#index-partition-definition)Index Partition Definition

| HTTP Method | URI                      | Documented at                                                                 |
| ----------- | ------------------------ | ----------------------------------------------------------------------------- |
| GET         | /api/pindex              | [Get Index Partition Information](../fts-rest-advanced/index.md#getPartition) |
| GET         | /api/pindex/{pindexName} | [Get Index Partition by Name](../fts-rest-advanced/index.md#getPartitionName) |

### [](#index-partition-querying)Index Partition Querying

| HTTP Method | URI                            | Documented at                                                                         |
| ----------- | ------------------------------ | ------------------------------------------------------------------------------------- |
| GET         | /api/pindex/{pindexName}/count | [Get Index Partition Document Count](../fts-rest-advanced/index.md#getPartitionCount) |
| POST        | /api/pindex/{pindexName}/query | [Query Index Partition](../fts-rest-advanced/index.md#queryPartition)                 |

### [](#fts-memory-quota)FTS Memory Quota

| HTTP Method | URI            | Documented at                                                           |
| ----------- | -------------- | ----------------------------------------------------------------------- |
| POST        | /pools/default | [Set FTS Memory Quota](../fts-rest-advanced/index.md#setFtsMemoryQuota) |

### [](#search-statistics)Search Statistics

| HTTP Method | URI                              | Documented at                                                                                                     |
| ----------- | -------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| GET         | /api/nsstats                     | [Get Query, Mutation, and Partition Statistics for the Search Service](../fts-rest-stats/index.md#g-api-nsstats)  |
| GET         | /api/nsstats/index/{INDEX\_NAME} | [Get Query, Mutation, and Partition Statistics for an Index](../fts-rest-stats/index.md#g-api-nsstats-index-name) |

### [](#active-queries)Active Queries

| HTTP Method | URI                          | Documented at                                                           |
| ----------- | ---------------------------- | ----------------------------------------------------------------------- |
| GET         | /api/query                   | [View Active Node Queries](../fts-rest-query/index.md#api-query)        |
| GET         | /api/query/index/{indexName} | [View Active Index Queries](../fts-rest-query/index.md#api-query-index) |
| POST        | /api/query/{queryID}/cancel  | [Cancel Active Queries](../fts-rest-query/index.md#api-query-cancel)    |

### [](#search-manager-options)Search Manager Options

| HTTP Method | URI                 | Documented at                                                                 |
| ----------- | ------------------- | ----------------------------------------------------------------------------- |
| GET         | /api/managerOptions | [Rebalance Based on File Transfer](../fts-rest-manage/index.md#put%5Foptions) |

## [](#legacy-apis)Legacy APIs

These endpoints are for legacy Search indexes and may be deprecated in a future release.

### [](#index-definition-legacy)Index Definition

| HTTP Method | URI                      | Documented at                                                                          |
| ----------- | ------------------------ | -------------------------------------------------------------------------------------- |
| GET         | /api/index               | [Get All Search Index Definitions](../fts-rest-indexing/index.md#g-api-index)          |
| GET         | /api/index/{INDEX\_NAME} | [Get Index Definition](../fts-rest-indexing/index.md#g-api-index-name)                 |
| PUT         | /api/index/{INDEX\_NAME} | [Create or Update an Index Definition](../fts-rest-indexing/index.md#p-api-index-name) |
| DELETE      | /api/index/{INDEX\_NAME} | [Delete Index Definition](../fts-rest-indexing/index.md#d-api-index-name)              |

### [](#index-management-legacy)Index Management

| HTTP Method | URI                                             | Documented at                                                                                       |
| ----------- | ----------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| POST        | /api/index/{INDEX\_NAME}/ingestControl/{OP}     | [Set Index Ingestion Control](../fts-rest-indexing/index.md#p-api-idx-name-ingestcontrol)           |
| POST        | /api/index/{INDEX\_NAME}/planFreezeControl/{OP} | [Freeze Index Partition Assignment](../fts-rest-indexing/index.md#p-api-idx-name-planfreezecontrol) |
| POST        | /api/index/{INDEX\_NAME}/queryControl/{OP}      | [Stop Queries on an Index](../fts-rest-indexing/index.md#p-api-idx-name-querycontrol)               |

### [](#index-querying-legacy)Index Querying

| HTTP Method | URI                            | Documented at                                                                |
| ----------- | ------------------------------ | ---------------------------------------------------------------------------- |
| POST        | /api/index/{INDEX\_NAME}/query | [Query a Search Index](../fts-rest-indexing/index.md#p-api-index-name-query) |