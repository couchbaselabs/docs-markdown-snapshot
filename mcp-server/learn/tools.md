---
title: Tools
description: Reference of the tools the Couchbase MCP Server exposes, grouped by category.
pubDate: 2026-08-22T04:32:17.641Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/release/1.0/modules/learn/pages/tools.adoc
  xref: xref:mcp-server:learn:tools.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/learn/tools.html)

# Tools

> Reference of the tools the Couchbase MCP Server exposes, grouped by category. 

The Couchbase MCP Server exposes several tools across multiple categories. The list of supported tools is constantly evolving so check the [GitHub readme](https://github.com/couchbase/mcp-server-couchbase?tab=readme-ov-file#featurestools) for the latest set of tools. Each tool is available to LLMs through the MCP protocol.

## [](#cluster-setup-health)Cluster Setup & Health

Tools for checking server status and cluster connectivity.

[Source](https://github.com/couchbase/mcp-server-couchbase/blob/main/src/cb%5Fmcp/tools/server.py)

| Tool                                | Description                                                                                                                                                                                      |  |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |  |
| get\_server\_configuration\_status  | Get the server status and configuration without connecting to the cluster — reports read-only mode, disabled/confirmation-required tools, OAuth settings, and the resolved logging configuration |  |
| test\_cluster\_connection           | Check the cluster credentials by connecting to the cluster                                                                                                                                       |  |
| get\_cluster\_health\_and\_services | Get cluster health status and list of all running services                                                                                                                                       |  |

## [](#data-model-schema-discovery)Data Model & Schema Discovery

Tools for exploring buckets, scopes, collections, and document schemas. Tools that modify structure are disabled by default when `CB_MCP_READ_ONLY_MODE=true`.

[Source](https://github.com/couchbase/mcp-server-couchbase/blob/main/src/cb%5Fmcp/tools/server.py)

| Tool                                      | Description                                                          |  |
| ----------------------------------------- | -------------------------------------------------------------------- |  |
| get\_buckets\_in\_cluster                 | Get a list of all the buckets in the cluster                         |  |
| get\_scopes\_in\_bucket                   | Get a list of all the scopes in the specified bucket                 |  |
| get\_collections\_in\_scope               | Get a list of all the collections in a specified scope and bucket    |  |
| get\_scopes\_and\_collections\_in\_bucket | Get a list of all the scopes and collections in the specified bucket |  |
| get\_schema\_for\_collection              | Infer the document structure for a collection                        |  |
| create\_scope                             | Create a new scope in a bucket                                       |  |
| create\_collection                        | Create a new collection in a scope                                   |  |
| delete\_scope                             | Delete an existing scope                                             |  |
| delete\_collection                        | Delete an existing collection                                        |  |

## [](#document-kv-operations)Document KV Operations

Tools for reading and writing documents by ID. Tools that modify data are disabled by default when `CB_MCP_READ_ONLY_MODE=true`.

[Source](https://github.com/couchbase/mcp-server-couchbase/blob/main/src/cb%5Fmcp/tools/kv.py)

| Tool                      | Description                                                                                                                                                                                             |  |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |  |
| get\_document\_by\_id     | Get a document by ID from a specified scope and collection                                                                                                                                              |  |
| upsert\_document\_by\_id  | Insert or update a document by ID                                                                                                                                                                       |  |
| insert\_document\_by\_id  | Insert a new document by ID (fails if document exists)                                                                                                                                                  |  |
| replace\_document\_by\_id | Replace an existing document by ID (fails if document does not exist)                                                                                                                                   |  |
| delete\_document\_by\_id  | Delete a document by ID                                                                                                                                                                                 |  |
| lookup\_subdocument       | Retrieve one or more paths (get, exists, count) from a document without fetching the whole document                                                                                                     |  |
| mutate\_subdocument       | Mutate one or more paths in a document (upsert, insert, replace, remove, array\_append, array\_prepend, array\_insert, array\_add\_unique, counter), optionally creating parent paths that do not exist |  |

## [](#query-and-indexing)Query and Indexing

Tools for running SQL++ queries, listing indexes, and getting index recommendations. Tools that create, build, or drop indexes are disabled by default when `CB_MCP_READ_ONLY_MODE=true`.

[Source (query)](https://github.com/couchbase/mcp-server-couchbase/blob/main/src/cb%5Fmcp/tools/query.py) | [Source (index)](https://github.com/couchbase/mcp-server-couchbase/blob/main/src/cb%5Fmcp/tools/index.py)

| Tool                                 | Description                                                                                                                                                                                                             |  |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |  |
| run\_sql\_plus\_plus\_query          | Run a [SQL++ query](https://www.couchbase.com/sqlplusplus/) on a specified scope                                                                                                                                        |  |
| explain\_sql\_plus\_plus\_query      | Provides information about the execution plan for the statement. This includes operators such as scans, joins, and filters; it aids in performance tuning by showing index usage, cost estimates, and data access paths |  |
| list\_indexes                        | List all indexes in the cluster with their definitions, with optional filtering. Set return\_raw\_index\_stats=true to return the unprocessed index information.                                                        |  |
| get\_index\_advisor\_recommendations | Get index recommendations from Couchbase Index Advisor for a given SQL++ query                                                                                                                                          |  |
| create\_index                        | Create a non-vector GSI index, deferred by default. Not applicable to vector indexes.                                                                                                                                   |  |
| build\_index                         | Build a deferred index. Applies to all index types, including vector indexes.                                                                                                                                           |  |
| drop\_index                          | Drop an existing index. Applies to all index types, including vector indexes.                                                                                                                                           |  |

## [](#query-performance-analysis)Query Performance Analysis

Tools for identifying slow queries, missing indexes, and optimization opportunities. These tools query `system:completed_requests`.

[Source](https://github.com/couchbase/mcp-server-couchbase/blob/main/src/cb%5Fmcp/tools/query.py)

| Tool                                         | Description                                                          |  |
| -------------------------------------------- | -------------------------------------------------------------------- |  |
| get\_longest\_running\_queries               | Get longest running queries by average service time                  |  |
| get\_most\_frequent\_queries                 | Get most frequently executed queries                                 |  |
| get\_queries\_not\_selective                 | Get queries that are not selective                                   |  |
| get\_queries\_not\_using\_covering\_index    | Get queries that do not use a covering index                         |  |
| get\_queries\_using\_primary\_index          | Get queries that use a primary index (potential performance concern) |  |
| get\_queries\_with\_largest\_response\_sizes | Get queries with the largest response sizes                          |  |
| get\_queries\_with\_large\_result\_count     | Get queries with the largest result counts                           |  |