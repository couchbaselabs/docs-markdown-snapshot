---
title: Search API
description: The Search API supports the creation and management of indexes for
  <em>Full Text Search</em>.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/rest-api/pages/rest-fts.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:rest-api:rest-fts.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/rest-api/rest-fts.html)

# Search API

## [](#apis-in-this-section)APIs in this Section

For Full Text Search, REST endpoints can be reached on Search-Service nodes on port 8094, or on 18094 when using SSL.

For information on required roles and permissions, see [Roles](../learn/security/roles.md).

For a list of the methods and URIs covered by these pages in this section, see the tables below.

### [](#index-definition)Index Definition

| HTTP Method | URI                    | Documented at                                             |
| ----------- | ---------------------- | --------------------------------------------------------- |
| GET         | /api/index             | [Index Definition](rest-fts-indexing.md#index-definition) |
| GET         | /api/index/{indexName} | [Index Definition](rest-fts-indexing.md#index-definition) |
| PUT         | /api/index/{indexName} | [Index Definition](rest-fts-indexing.md#index-definition) |
| DELETE      | /api/index/{indexName} | [Index Definition](rest-fts-indexing.md#index-definition) |

### [](#index-management)Index Management

| HTTP Method | URI                                           | Documented at                                             |
| ----------- | --------------------------------------------- | --------------------------------------------------------- |
| POST        | /api/index/{indexName}/ingestControl/{op}     | [Index Management](rest-fts-indexing.md#index-management) |
| POST        | /api/index/{indexName}/planFreezeControl/{op} | [Index Management](rest-fts-indexing.md#index-management) |
| POST        | /api/index/{indexName}/planQueryControl/{op}  | [Index Management](rest-fts-indexing.md#index-management) |

### [](#index-monitoring-and-debugging)Index Monitoring and Debugging

| HTTP Method | URI                               | Documented at                                                                         |
| ----------- | --------------------------------- | ------------------------------------------------------------------------------------- |
| GET         | /api/stats                        | [Index Monitoring And Debugging](rest-fts-indexing.md#index-monitoring-and-debugging) |
| GET         | /api/stats/{indexName}            | [Index Monitoring And Debugging](rest-fts-indexing.md#index-monitoring-and-debugging) |
| POST        | /api/stats/{indexName}/analyzeDoc | [Index Monitoring And Debugging](rest-fts-indexing.md#index-monitoring-and-debugging) |
| GET         | /api/query/index/{indexName}      | [Index Monitoring And Debugging](rest-fts-indexing.md#index-monitoring-and-debugging) |

### [](#index-querying)Index Querying

| HTTP Method | URI                          | Documented at                                         |
| ----------- | ---------------------------- | ----------------------------------------------------- |
| GET         | /api/index/{indexName}/count | [Index Querying](rest-fts-indexing.md#index-querying) |
| POST        | /api/index/{indexName}/query | [Index Querying](rest-fts-indexing.md#index-querying) |

### [](#node-configuration)Node Configuration

| HTTP Method | URI              | Documented at                                             |
| ----------- | ---------------- | --------------------------------------------------------- |
| GET         | /api/cfg         | [Node Configuration](rest-fts-node.md#node-configuration) |
| POST        | /api/cfgRefresh  | [Node Configuration](rest-fts-node.md#node-configuration) |
| POST        | /api/managerKick | [Node Configuration](rest-fts-node.md#node-configuration) |
| GET         | /api/managerMeta | [Node Configuration](rest-fts-node.md#node-configuration) |

### [](#node-diagnostics)Node Diagnostics

| HTTP Method | URI                         | Documented at                                         |
| ----------- | --------------------------- | ----------------------------------------------------- |
| GET         | /api/diag                   | [Node Diagnostics](rest-fts-node.md#node-diagnostics) |
| GET         | /api/log                    | [Node Diagnostics](rest-fts-node.md#node-diagnostics) |
| GET         | /api/runtime                | [Node Diagnostics](rest-fts-node.md#node-diagnostics) |
| GET         | /api/runtime/args           | [Node Diagnostics](rest-fts-node.md#node-diagnostics) |
| POST        | /api/runtime/profile/cpu    | [Node Diagnostics](rest-fts-node.md#node-diagnostics) |
| POST        | /api/runtime/profile/memory | [Node Diagnostics](rest-fts-node.md#node-diagnostics) |

### [](#node-management)Node Management

| HTTP Method | URI             | Documented at                                       |
| ----------- | --------------- | --------------------------------------------------- |
| POST        | /api/runtime/gc | [Node Management](rest-fts-node.md#node-management) |

### [](#node-monitoring)Node Monitoring

| HTTP Method | URI                         | Documented at                                       |
| ----------- | --------------------------- | --------------------------------------------------- |
| GET         | /api/runtime/stats          | [Node Monitoring](rest-fts-node.md#node-monitoring) |
| GET         | /api/runtime/stats/statsMem | [Node Monitoring](rest-fts-node.md#node-monitoring) |

### [](#index-partition-definition)Index Partition Definition

| HTTP Method | URI                      | Documented at                                               |
| ----------- | ------------------------ | ----------------------------------------------------------- |
| GET         | /api/pindex              | [Advanced](rest-fts-advanced.md#index-partition-definition) |
| GET         | /api/pindex/{pindexName} | [Advanced](rest-fts-advanced.md#index-partition-definition) |

### [](#index-partition-querying)Index Partition Querying

| HTTP Method | URI                            | Documented at                                             |
| ----------- | ------------------------------ | --------------------------------------------------------- |
| GET         | /api/pindex/{pindexName}/count | [Advanced](rest-fts-advanced.md#index-partition-querying) |
| POST        | /api/pindex/{pindexName}/query | [Advanced](rest-fts-advanced.md#index-partition-querying) |

### [](#fts-memory-quota)FTS Memory Quota

| HTTP Method | URI            | Documented at                                     |
| ----------- | -------------- | ------------------------------------------------- |
| POST        | /pools/default | [Advanced](rest-fts-advanced.md#fts-memory-quota) |