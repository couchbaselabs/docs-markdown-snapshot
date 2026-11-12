---
title: Tools
description: Reference of the tools the Couchbase MCP Server for Operational
  Insights exposes, grouped by category, with how the server handles large query
  results.
pubDate: 2026-11-12T06:49:41.760Z
meta:
  component:
    title: Couchbase MCP Server Self-Managed
    version: "1.1"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/release/1.1/modules/learn-oi/pages/tools-oi.adoc
  xref: xref:mcp-server:learn-oi:tools-oi.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/current/learn-oi/tools-oi.html)

# Tools

> Reference of the tools the Couchbase MCP Server for Operational Insights exposes, grouped by category, with how the server handles large query results. 

The Couchbase MCP Server for Operational Insights exposes several tools across multiple categories. The list of supported tools is constantly evolving, so see the [README](https://github.com/couchbase/mcp-server-couchbase/blob/main/README.md#operational-insights-tools) for the latest set of tools. Each tool is available to LLMs through the MCP protocol.

The Operational Insights server supports only self-managed deployments. For the Couchbase Server tools, see [Couchbase Server Tools](../learn/tools.md).

## [](#server-status)Server Status

Tool for checking server status. It's shared with the Couchbase Server server, so it keeps its name without an `operational_insights_` prefix.

[Source](https://github.com/couchbase/mcp-server-couchbase/blob/main/src/cb%5Fmcp/tools/status.py)

| Tool                               | Description                                                                                                                                                                                                                                                                                                                                                                          |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| get\_server\_configuration\_status | Get the server status and configuration without connecting to the cluster. The tool reports read-only mode, the tools that are turned off or need confirmation, OAuth settings, the resolved logging configuration, and the audit logging counters. It shows the connection string and username in clear text. For the password and certificates, it shows only whether they're set. |

## [](#data-model-schema-discovery)Data Model & Schema Discovery

Tools for exploring databases, scopes, collections, and document schemas.

[Source](https://github.com/couchbase/mcp-server-couchbase/blob/main/src/cb%5Fmcp/tools/operational%5Finsights/metadata.py)

| Tool                                                | Description                                                                                                                                                                                                                                     |
| --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| operational\_insights\_get\_databases\_in\_cluster  | Get a list of all the databases in the cluster.                                                                                                                                                                                                 |
| operational\_insights\_get\_scopes\_in\_database    | Get a list of all the scopes in the specified database.                                                                                                                                                                                         |
| operational\_insights\_get\_collections\_in\_scope  | Get a list of all the collections in the specified scope, including the type of each collection: INTERNAL, EXTERNAL, or VIEW. To list only stored or linked collections, filter out the VIEW rows.                                              |
| operational\_insights\_get\_schema\_for\_collection | Infer the JSON schema of a collection with the ARRAY\_INFER\_SCHEMA function, by sampling up to sample\_size documents. The maximum is 10,000\. By default, the tool returns the structure only. Use num\_sample\_values to add example values. |

## [](#query-and-index)Query and Index

Tools for running SQL++ queries, managing async queries, and working with indexes. For how to limit or export large query results, see [Large Result Handling](../configuration-oi/large-results-oi.md). Read-only mode turns off `operational_insights_create_index` by default. All the other tools stay available in read-only mode, including `operational_insights_cancel_async_query`.

> [!IMPORTANT]
> The async query tools are stateful. The server keeps each query handle in the memory of one process, so a restart loses all handles. If you run more than one Operational Insights server behind a load balancer, route all requests for a handle to the same server. For symptoms and fixes, see [Async Query Issues](../configuration-oi/troubleshooting-oi.md#async-query-issues).

[Source (query)](https://github.com/couchbase/mcp-server-couchbase/blob/main/src/cb%5Fmcp/tools/operational%5Finsights/query.py) | [Source (index)](https://github.com/couchbase/mcp-server-couchbase/blob/main/src/cb%5Fmcp/tools/operational%5Finsights/index.py)

| Tool                                                  | Description                                                                                                                                                                                                                                                                                  |
| ----------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| operational\_insights\_list\_indexes                  | List the secondary indexes that users created, optionally filtered by database, scope, and collection. The tool does not list primary indexes, optimizer samples, or internal System indexes.                                                                                                |
| operational\_insights\_explain\_query                 | Get the query plan for a SQL++ statement with EXPLAIN, without running it. Pass the statement without the EXPLAIN keyword.                                                                                                                                                                   |
| operational\_insights\_run\_query\_sync               | Run a SQL++ statement and return its result rows, up to the size limit that you configure. The statement can be SELECT, DML, or DDL. To send a large result to object storage instead, use the copy\_to\_\* arguments. See [Large Result Handling](../configuration-oi/large-results-oi.md). |
| operational\_insights\_run\_query\_async              | Start a SQL++ query without waiting for it to finish. The tool returns a query\_handle and no rows. The query holds server resources until you discard its results or cancel it. It also supports the copy\_to\_\* arguments.                                                                |
| operational\_insights\_get\_async\_query\_results     | Check the status of an async query and get its results once it finishes. While the query runs, the tool returns ready: false and no rows. When the query finishes, the tool returns ready: true with the rows. Calling the tool again does not consume the results.                          |
| operational\_insights\_discard\_async\_query\_results | Free the results of a finished async query on the server. Fetching results does not free them. If the query is still running, the tool returns discarded: false, and you can cancel the query instead.                                                                                       |
| operational\_insights\_cancel\_async\_query           | Stop an async query that's still running. The query handle stops working. If the query already finished, the tool returns cancelled: false and keeps the handle, so you can discard the results. Available in read-only mode.                                                                |
| operational\_insights\_create\_index                  | Create a secondary index with CREATE INDEX. The tool supports composite indexes and array indexes.                                                                                                                                                                                           |

## [](#see-also)See Also

* [Overview](../get-started-oi/overview-oi.md)
* [Environment Variables & Command Line Arguments](../configuration-oi/environment-variables-oi.md)
* [Read-Only Mode](../configuration-oi/read-only-mode-oi.md)
* [Large Result Handling](../configuration-oi/large-results-oi.md)
* [Architecture](architecture-oi.md)
* [Couchbase Server Tools](../learn/tools.md)