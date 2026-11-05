---
title: Couchbase MCP Server for Operational Insights
description: Couchbase MCP Server lets AI agents connect to a self-managed
  Couchbase Operational Insights endpoint. It provides tools for database and
  schema discovery and running analytics queries. Read-only mode keeps it safe
  to use.
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase MCP Server
    version: "1.1"
  topic_type: concept
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/release/1.1/modules/get-started-oi/pages/overview-oi.adoc
  xref: xref:1.1@mcp-server:get-started-oi:overview-oi.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/1.1/get-started-oi/overview-oi.html)

# Couchbase MCP Server for Operational Insights

> Couchbase MCP Server lets AI agents connect to a self-managed Couchbase Operational Insights endpoint. It provides tools for database and schema discovery and running analytics queries. Read-only mode keeps it safe to use. 

Couchbase MCP Server is a self-hosted MCP Server that allows AI agents to connect to and interact with a Couchbase Operational Insights endpoint.

> [!IMPORTANT]
> The Operational Insights MCP server supports only self-managed deployments. Capella-hosted Operational Insights is not supported.

It provides tools for database, scope, and collection discovery, schema inference, and running and managing SQL++ queries — with safety controls via read-only mode. It supports both STDIO and Streamable HTTP transports.

The Couchbase MCP server ships as a Python Package Index (PyPI) package and via Docker. Enterprise support for Couchbase MCP Server is available by licensing [Couchbase AI Data Plane](https://www.couchbase.com/downloads/?family=ai-data-plane). This license also entitles use and enterprise support of Couchbase Agent Memory and Couchbase Agent Catalog.

## [](#get-started)Get Started

To set up the server, see [Prerequisites](prerequisites-oi.md), then follow the [Quick Start](quickstart-oi.md).

## [](#tools)Tools

The server exposes several tools across multiple categories.

See the [Tools](../learn-oi/tools-oi.md) page for full details.

| Category                          | Tools                                                                                                                                                                                                                                                                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Server Status**                 | get\_server\_configuration\_status                                                                                                                                                                                                                                                                                                                          |
| **Data Model & Schema Discovery** | operational\_insights\_get\_databases\_in\_cluster, operational\_insights\_get\_scopes\_in\_database, operational\_insights\_get\_collections\_in\_scope, operational\_insights\_get\_schema\_for\_collection                                                                                                                                               |
| **Query and Index**               | operational\_insights\_list\_indexes, operational\_insights\_explain\_query, operational\_insights\_run\_query\_sync, operational\_insights\_run\_query\_async, operational\_insights\_get\_async\_query\_results, operational\_insights\_discard\_async\_query\_results, operational\_insights\_create\_index, operational\_insights\_cancel\_async\_query |