---
title: Tools
description: Reference of the tools the Couchbase MCP Server exposes for
  Couchbase Server, grouped by category, with the deployments each tool
  supports.
pubDate: 2026-11-12T06:49:41.760Z
meta:
  component:
    title: Couchbase MCP Server Self-Managed
    version: "1.1"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/release/1.1/modules/learn/pages/tools.adoc
  xref: xref:mcp-server:learn:tools.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/current/learn/tools.html)

# Tools

> Reference of the tools the Couchbase MCP Server exposes for Couchbase Server, grouped by category, with the deployments each tool supports. 

The Couchbase MCP Server exposes several tools across multiple categories. The list of supported tools is constantly evolving, so see the [README](https://github.com/couchbase/mcp-server-couchbase/blob/main/README.md#operational-tools) for the latest set of tools. Each tool is available to LLMs through the MCP protocol.

The tables in this page show the deployments that each tool supports. For the Operational Insights tools, see [Operational Insights Tools](../learn-oi/tools-oi.md).

## [](#mcp-server-status-and-configuration)MCP Server Status and Configuration

Tool for checking the server status and configuration.

[Source](https://github.com/couchbase/mcp-server-couchbase/blob/main/src/cb%5Fmcp/tools/status.py)

| Tool                               | Deployment               | Description                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| get\_server\_configuration\_status | Self-managed and Capella | Get the server status and configuration without connecting to the cluster. The tool reports read-only mode, the tools that are turned off or need confirmation, OAuth settings, the resolved logging configuration, and the audit logging counters. It shows the connection string and username in clear text. For the password and certificates, it shows only whether they're set. |

## [](#cluster-setup-health)Cluster Setup & Health

Tools for checking cluster connectivity, health, bucket configuration, and service statistics.

> [!IMPORTANT]
> Administrator Roles
> 
> Several tools in this category need an administrator role:
> 
> * `get_cluster_health_snapshot`, `get_cluster_tasks`, `get_cluster_query_vitals`, and `get_bucket_config` need the Read-Only Admin (`ro_admin`) role or a role with more privileges.
> * `get_cluster_system_events` needs the Full Admin or Cluster Admin role.
> 
> A database user without the required role gets a permission error from these tools.

> [!WARNING]
> Infrastructure Information
> 
> The tools in this category return details about your infrastructure. These details include node addresses, service topology, cluster membership, bucket configuration, and cluster events. The MCP client passes tool results to the LLM that it uses. If that LLM runs in a third-party service, you share this information with that third party.
> 
> Review what these tools return before you share it with a third-party LLM. To limit the exposure, turn off the tools you do not need with `CB_MCP_DISABLED_TOOLS`, or connect with a database user that does not have the administrator roles. See [Sharing Infrastructure Information with LLMs](../security/security.md#sharing-infrastructure-information-with-llms).

[Source (cluster)](https://github.com/couchbase/mcp-server-couchbase/blob/main/src/cb%5Fmcp/tools/operational/server.py) | [Source (Query Service)](https://github.com/couchbase/mcp-server-couchbase/blob/main/src/cb%5Fmcp/tools/operational/query%5Fadmin.py) | [Source (Index Service)](https://github.com/couchbase/mcp-server-couchbase/blob/main/src/cb%5Fmcp/tools/operational/index.py)

| Tool                                | Deployment               | Description                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------------------------------- | ------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| test\_cluster\_connection           | Self-managed and Capella | Check the cluster credentials by connecting to the cluster.                                                                                                                                                                                                                                                                                                                                                           |
| get\_cluster\_health\_and\_services | Self-managed and Capella | Actively ping the cluster services, using the SDK ping service, and report reachability, latency, and connection details. Filter to specific services with service\_types. The active ping needs KV, Query, or Search privileges, or the Cluster Admin role.                                                                                                                                                          |
| get\_client\_connectivity\_report   | Self-managed and Capella | Report the SDK's cached connection state per endpoint, using the SDK diagnostics service. The tool makes no network request, so it needs no role beyond the one the cluster connection already uses. It includes the connection status, addresses, and last activity, plus the overall cluster state.                                                                                                                 |
| get\_cluster\_health\_snapshot      | Self-managed only        | Get the health of the cluster as a whole from the Server APIs, including per-node service topology, cluster membership, and orchestrator node. Needs Server 7.6 or later and the ro\_admin role or a role with more privileges.                                                                                                                                                                                       |
| get\_cluster\_metrics               | Self-managed only        | Retrieve one or more cluster statistics over a historic time window in a single call, through the Management REST API. Needs Server 7.6 or later. Use discover\_tool\_input\_values to find valid metric names. The tool does not limit the number of metrics, the time window, or the nodes, so a broad request can return a large response.                                                                         |
| get\_cluster\_tasks                 | Self-managed only        | Get the tasks the cluster is handling, such as rebalance, index build, compaction, XDCR, and backup, to detect stuck or failed operations. Needs Server 7.6 or later and the ro\_admin role or a role with more privileges.                                                                                                                                                                                           |
| get\_cluster\_system\_events        | Self-managed only        | Get the cluster system events that took place, for root-cause correlation against a symptom's timeframe. The first call returns 50 records, up to a maximum of 500 per request. Use since\_time to page through earlier events. Needs Server 7.6 or later and the Full Admin or Cluster Admin role.                                                                                                                   |
| get\_cluster\_query\_vitals         | Self-managed only        | Get Query Service health and vitals, such as request rate, active and queued request counts, memory, and garbage collection. Needs Server 7.6 or later and the ro\_admin role or a role with more privileges.                                                                                                                                                                                                         |
| get\_index\_stats                   | Self-managed only        | Get per-index metrics from the Index Service for the whole cluster or for a specific index. The metrics include data size, item count, fragmentation percentage, and pending mutations. Filters narrow the result by bucket, scope, collection, and index. Needs Server 7.6 or later.                                                                                                                                 |
| get\_bucket\_config                 | Self-managed only        | Get the configuration and live state of one bucket, or of every bucket when you omit bucket\_name. The result includes the memory quota, replica count, eviction policy, durability level, storage backend, conflict resolution type, compaction settings, and basic statistics. The tool only reads, and it never changes a bucket. Needs Server 7.6 or later and the ro\_admin role or a role with more privileges. |

## [](#data-model-schema-discovery)Data Model & Schema Discovery

Tools for exploring buckets, scopes, collections, and document schemas. Tools that modify structure are turned off by default when `CB_MCP_READ_ONLY_MODE=true`.

[Source (discovery)](https://github.com/couchbase/mcp-server-couchbase/blob/main/src/cb%5Fmcp/tools/operational/server.py) | [Source (scopes and collections)](https://github.com/couchbase/mcp-server-couchbase/blob/main/src/cb%5Fmcp/tools/operational/collection%5Fmanagement.py)

| Tool                                      | Deployment               | Description                                                                                                                                                                                                          |
| ----------------------------------------- | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| get\_buckets\_in\_cluster                 | Self-managed and Capella | Get a list of all the buckets in the cluster.                                                                                                                                                                        |
| get\_scopes\_in\_bucket                   | Self-managed and Capella | Get a list of all the scopes in the specified bucket.                                                                                                                                                                |
| get\_collections\_in\_scope               | Self-managed and Capella | Get a list of all the collections in a specified scope and bucket.                                                                                                                                                   |
| get\_scopes\_and\_collections\_in\_bucket | Self-managed and Capella | Get a list of all the scopes and collections in the specified bucket.                                                                                                                                                |
| get\_schema\_for\_collection              | Self-managed and Capella | Infer the document structure for a collection. The optional num\_sample\_values argument sets how many example values the schema reports for each field. Set it to 0 to return the structure without example values. |
| create\_scope                             | Self-managed and Capella | Create a new scope in a bucket.                                                                                                                                                                                      |
| create\_collection                        | Self-managed and Capella | Create a new collection in a scope.                                                                                                                                                                                  |
| delete\_scope                             | Self-managed and Capella | Delete an existing scope.                                                                                                                                                                                            |
| delete\_collection                        | Self-managed and Capella | Delete an existing collection.                                                                                                                                                                                       |

## [](#document-kv-operations)Document KV Operations

Tools for reading and writing documents by ID. Read-only mode (`CB_MCP_READ_ONLY_MODE=true`) turns off the tools that modify data by default.

[Source](https://github.com/couchbase/mcp-server-couchbase/blob/main/src/cb%5Fmcp/tools/operational/kv.py)

| Tool                      | Deployment               | Description                                                                                                                                                                                                                                                            |
| ------------------------- | ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| get\_document\_by\_id     | Self-managed and Capella | Get a document by ID from a specified scope and collection.                                                                                                                                                                                                            |
| upsert\_document\_by\_id  | Self-managed and Capella | Insert or update a document by ID.                                                                                                                                                                                                                                     |
| insert\_document\_by\_id  | Self-managed and Capella | Insert a new document by ID. The tool fails if the document exists.                                                                                                                                                                                                    |
| replace\_document\_by\_id | Self-managed and Capella | Replace an existing document by ID. The tool fails if the document does not exist.                                                                                                                                                                                     |
| delete\_document\_by\_id  | Self-managed and Capella | Delete a document by ID.                                                                                                                                                                                                                                               |
| lookup\_subdocument       | Self-managed and Capella | Retrieve one or more paths (get, exists, count) from a document without fetching the whole document.                                                                                                                                                                   |
| mutate\_subdocument       | Self-managed and Capella | Mutate one or more paths in a document (upsert, insert, replace, remove, array\_append, array\_prepend, array\_insert, array\_add\_unique, counter). You can create parent paths that do not exist, except for array\_insert, which does not support creating parents. |

## [](#query-and-index)Query and Index

Tools for running SQL++ and vector queries, managing in-flight queries, listing indexes, getting index recommendations, and creating indexes. Tools that create, build, or drop indexes, and `delete_active_query`, are turned off by default when `CB_MCP_READ_ONLY_MODE=true`.

> [!IMPORTANT]
> `get_active_queries` and `delete_active_query` need an administrator role, as the tables show. `get_active_queries` returns the statements of requests that other users are running, so treat its output as sensitive before you share it with a third-party LLM.

[Source (query)](https://github.com/couchbase/mcp-server-couchbase/blob/main/src/cb%5Fmcp/tools/operational/query.py) | [Source (in-flight queries)](https://github.com/couchbase/mcp-server-couchbase/blob/main/src/cb%5Fmcp/tools/operational/query%5Fadmin.py) | [Source (index)](https://github.com/couchbase/mcp-server-couchbase/blob/main/src/cb%5Fmcp/tools/operational/index.py) | [Source (vector index)](https://github.com/couchbase/mcp-server-couchbase/blob/main/src/cb%5Fmcp/tools/operational/vector%5Findex.py) | [Source (vector query)](https://github.com/couchbase/mcp-server-couchbase/blob/main/src/cb%5Fmcp/tools/operational/vector%5Fsearch.py)

| Tool                                 | Deployment               | Description                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------ | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| run\_sql\_plus\_plus\_query          | Self-managed and Capella | Run a [SQL++ query](https://www.couchbase.com/sqlplusplus/) on a specified scope.                                                                                                                                                                                                                                                                                                                                          |
| explain\_sql\_plus\_plus\_query      | Self-managed and Capella | Get the execution plan for a statement, including operators such as scans, joins, and filters. The plan shows index usage, cost estimates, and data access paths, which helps with performance tuning.                                                                                                                                                                                                                     |
| get\_active\_queries                 | Self-managed only        | Get the in-flight query requests that are running on the cluster, including the elapsed time and the query statement. Needs Server 7.6 or later and the ro\_admin role or a role with more privileges.                                                                                                                                                                                                                     |
| delete\_active\_query                | Self-managed only        | Cancel a specific in-flight query request by ID. Needs Server 7.6 or later and the Full Admin or Cluster Admin role.                                                                                                                                                                                                                                                                                                       |
| run\_vector\_query                   | Self-managed and Capella | Run a vector similarity search against a GSI vector index and return the matching documents. Needs Server 8.0 or later. Needs an embedding provider. See [Environment Variables](../configuration/environment-variables.md).                                                                                                                                                                                               |
| list\_indexes                        | Self-managed and Capella | List all indexes in the cluster with their definitions, with optional filtering. The list includes both vector and non-vector indexes. Set return\_raw\_index\_stats=true to return the unprocessed index information.                                                                                                                                                                                                     |
| get\_index\_advisor\_recommendations | Self-managed and Capella | Get index recommendations from the Couchbase Index Advisor for a given SQL++ query.                                                                                                                                                                                                                                                                                                                                        |
| create\_index                        | Self-managed and Capella | Deprecated. Create a non-vector GSI index, deferred by default. Not applicable to vector indexes. The tool remains available with a deprecation warning. Use create\_query\_index instead.                                                                                                                                                                                                                                 |
| build\_index                         | Self-managed and Capella | Build all deferred indexes in a collection. The tool takes only the bucket, scope, and collection, so you cannot target one index by name. It applies to all index types, including vector indexes, and does nothing if the collection has no deferred indexes. The build runs asynchronously, so success means the build started, not that it finished. Use list\_indexes to see when the indexes reach the online state. |
| drop\_index                          | Self-managed and Capella | Drop an existing index. Applies to all index types, including vector indexes.                                                                                                                                                                                                                                                                                                                                              |
| create\_query\_index                 | Self-managed and Capella | Create a regular or vector index by running SQL++, rather than using the SDK index manager. Replaces create\_index.                                                                                                                                                                                                                                                                                                        |

## [](#search-operations)Search Operations

Tools for discovering, querying, and managing Search indexes, including vector search through the Search Service. Tools that modify indexes are turned off by default when `CB_MCP_READ_ONLY_MODE=true`.

Search tools support both scope-level indexes and cluster-level (legacy) indexes, which are the pre-7.6 index type. The Search roles that work with these tools are:

* **Search Admin**: the minimum role for all five Search index tools. It works for `list_search_indexes`, `get_search_index_definition`, `run_search`, `upsert_search_index`, and `drop_search_index`.
* **Search Reader**: works for `list_search_indexes`, `get_search_index_definition`, and `run_search`. It does not work for `upsert_search_index` or `drop_search_index`.
* **Full Admin**: works for all five Search index tools.

[Source (Search)](https://github.com/couchbase/mcp-server-couchbase/blob/main/src/cb%5Fmcp/tools/operational/fts.py) | [Source (vector search)](https://github.com/couchbase/mcp-server-couchbase/blob/main/src/cb%5Fmcp/tools/operational/vector%5Fsearch.py)

| Tool                           | Deployment               | Description                                                                                                                                                                                                                                                          |
| ------------------------------ | ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| list\_search\_indexes          | Self-managed and Capella | List Search indexes, optionally filtered by bucket and scope. With no filters, the tool returns cluster-level (legacy) indexes. With a bucket only, it returns scope-level indexes across all scopes. With a bucket and scope, it returns the indexes of that scope. |
| get\_search\_index\_definition | Self-managed and Capella | Get the full definition of a Search index, including the mappings, analyzers, and plan parameters.                                                                                                                                                                   |
| run\_search                    | Self-managed and Capella | Run a raw Search (FTS) query against a Search index, or get its execution plan with explain=true.                                                                                                                                                                    |
| upsert\_search\_index          | Self-managed and Capella | Create a new Search index, or update an existing one.                                                                                                                                                                                                                |
| drop\_search\_index            | Self-managed and Capella | Drop an existing Search index.                                                                                                                                                                                                                                       |
| run\_vector\_search            | Self-managed and Capella | Run a vector search using the Search Service, including hybrid vector-plus-scalar searches. Needs Server 7.6 or later. Needs an embedding provider. See [Environment Variables](../configuration/environment-variables.md).                                          |

## [](#query-performance-analysis)Query Performance Analysis

Tools for identifying slow queries, missing indexes, and optimization opportunities. These tools query `system:completed_requests`.

[Source](https://github.com/couchbase/mcp-server-couchbase/blob/main/src/cb%5Fmcp/tools/operational/query.py)

| Tool                                         | Deployment               | Description                                                                     |
| -------------------------------------------- | ------------------------ | ------------------------------------------------------------------------------- |
| get\_longest\_running\_queries               | Self-managed and Capella | Get the longest running queries by average service time.                        |
| get\_most\_frequent\_queries                 | Self-managed and Capella | Get the most frequently executed queries.                                       |
| get\_queries\_not\_selective                 | Self-managed and Capella | Get queries that are not selective.                                             |
| get\_queries\_not\_using\_covering\_index    | Self-managed and Capella | Get queries that do not use a covering index.                                   |
| get\_queries\_using\_primary\_index          | Self-managed and Capella | Get queries that use a primary index, which is a potential performance concern. |
| get\_queries\_with\_largest\_response\_sizes | Self-managed and Capella | Get queries with the largest response sizes.                                    |
| get\_queries\_with\_large\_result\_count     | Self-managed and Capella | Get queries with the largest result counts.                                     |

## [](#reference-data)Reference Data

Tools for finding the exact input values that other tools require, from reference data that ships with the server. These tools never touch the cluster, so they work offline and while the cluster is unreachable.

[Source](https://github.com/couchbase/mcp-server-couchbase/blob/main/src/cb%5Fmcp/tools/operational/reference.py)

| Tool                          | Deployment   | Description                                                                                                                                                                                                                                                            |
| ----------------------------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| discover\_tool\_input\_values | Self-managed | Find the exact input values that a specific tool requires by browsing or searching the bundled reference dataset. Today the dataset lists the metric names for get\_cluster\_metrics. The server does not load this tool when the connection string points at Capella. |

## [](#tools-not-available-on-capella)Tools Not Available on Capella

Most tools work with both self-managed Couchbase Server and Capella. The following ten tools need self-managed Couchbase Server. The server does not load these tools when the connection string points at Capella, so they do not appear in tool discovery and the LLM cannot call them. `get_server_configuration_status` reports the withheld tools, and the server lists them in the startup log. Where the server states a minimum version or role, the table lists it. See [Tools the Server Disables Automatically](../configuration/disabling-tools.md#tools-the-server-disables-automatically).

| Tool                           | Minimum Server Version | Required Role                                         |
| ------------------------------ | ---------------------- | ----------------------------------------------------- |
| get\_cluster\_health\_snapshot | 7.6                    | ro\_admin or a role with more privileges              |
| get\_cluster\_metrics          | 7.6                    | ro\_admin or a role with more privileges              |
| get\_cluster\_tasks            | 7.6                    | ro\_admin or a role with more privileges              |
| get\_cluster\_system\_events   | 7.6                    | Full Admin or Cluster Admin                           |
| get\_cluster\_query\_vitals    | 7.6                    | ro\_admin or a role with more privileges              |
| get\_index\_stats              | 7.6                    | query\_system\_catalog or a role with more privileges |
| get\_bucket\_config            | 7.6                    | ro\_admin or a role with more privileges              |
| get\_active\_queries           | 7.6                    | ro\_admin or a role with more privileges              |
| delete\_active\_query          | 7.6                    | Full Admin or Cluster Admin                           |
| discover\_tool\_input\_values  | None                   | None                                                  |

## [](#see-also)See Also

* [Overview](../get-started/overview.md)
* [Architecture](architecture.md)
* [Read-Only Mode](../configuration/read-only-mode.md)
* [Disabling Tools](../configuration/disabling-tools.md)
* [Environment Variables & Command Line Arguments](../configuration/environment-variables.md)
* [Troubleshooting Cluster Health Tools](../configuration/troubleshooting.md#cluster-health-tool-issues)
* [Operational Insights Tools](../learn-oi/tools-oi.md)