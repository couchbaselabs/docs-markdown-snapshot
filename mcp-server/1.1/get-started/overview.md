---
title: Couchbase MCP Server for Couchbase Server
description: Couchbase MCP Server lets AI agents connect to Couchbase clusters,
  on Capella or self-managed. It provides tools for cluster health, schema
  discovery, key-value operations, and query performance. Read-only mode and
  fine-grained tool controls keep it safe to use.
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase MCP Server
    version: "1.1"
  topic_type: concept
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/release/1.1/modules/get-started/pages/overview.adoc
  xref: xref:1.1@mcp-server:get-started:overview.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/1.1/get-started/overview.html)

# Couchbase MCP Server for Couchbase Server

> Couchbase MCP Server lets AI agents connect to Couchbase clusters, on Capella or self-managed. It provides tools for cluster health, schema discovery, key-value operations, and query performance. Read-only mode and fine-grained tool controls keep it safe to use. 

Couchbase MCP Server is a self-hosted MCP Server that allows AI agents to connect to and interact with data in Couchbase clusters. Clusters can be hosted on Capella or self-managed. It provides tools across categories including Cluster Health, Data Schema, Key-Value, Query, and Performance. Safety controls include read-only mode and fine-grained tool disabling. It supports both STDIO and Streamable HTTP transports.

The Couchbase MCP server ships as a Python Package Index (PyPI) package and via Docker. Enterprise support for Couchbase MCP Server is available by licensing [Couchbase AI Data Plane](https://www.couchbase.com/downloads/?family=ai-data-plane). This license also entitles use and enterprise support of Couchbase Agent Memory and Couchbase Agent Catalog.

## [](#get-started)Get Started

To set up the server, see [Prerequisites](prerequisites.md), then follow the [Quick Start](quickstart.md).

## [](#tools)Tools

The server exposes several tools across multiple categories. The tools page lists which tools work on Capella and which need self-managed Couchbase Server.

See the [Tools](../learn/tools.md) page for full details.

| Category                                | Tools                                                                                                                                                                                                                                                                            |
| --------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **MCP Server Status and Configuration** | get\_server\_configuration\_status                                                                                                                                                                                                                                               |
| **Cluster Setup & Health**              | test\_cluster\_connection, get\_cluster\_health\_and\_services, get\_client\_connectivity\_report, get\_cluster\_health\_snapshot, get\_cluster\_metrics, get\_cluster\_tasks, get\_cluster\_system\_events, get\_cluster\_query\_vitals, get\_index\_stats, get\_bucket\_config |
| **Data Model & Schema Discovery**       | get\_buckets\_in\_cluster, get\_scopes\_in\_bucket, get\_collections\_in\_scope, get\_scopes\_and\_collections\_in\_bucket, get\_schema\_for\_collection, create\_scope, create\_collection, delete\_scope, delete\_collection                                                   |
| **Document KV Operations**              | get\_document\_by\_id, upsert\_document\_by\_id, insert\_document\_by\_id, replace\_document\_by\_id, delete\_document\_by\_id, lookup\_subdocument, mutate\_subdocument                                                                                                         |
| **Query and Index**                     | run\_sql\_plus\_plus\_query, explain\_sql\_plus\_plus\_query, get\_active\_queries, delete\_active\_query, run\_vector\_query, list\_indexes, get\_index\_advisor\_recommendations, create\_index, build\_index, drop\_index, create\_query\_index                               |
| **Search Operations**                   | list\_search\_indexes, get\_search\_index\_definition, run\_search, upsert\_search\_index, drop\_search\_index, run\_vector\_search                                                                                                                                              |
| **Query Performance Analysis**          | get\_longest\_running\_queries, get\_most\_frequent\_queries, get\_queries\_not\_selective, get\_queries\_not\_using\_covering\_index, get\_queries\_using\_primary\_index, get\_queries\_with\_largest\_response\_sizes, get\_queries\_with\_large\_result\_count               |
| **Reference Data**                      | discover\_tool\_input\_values                                                                                                                                                                                                                                                    |

## [](#learn-more)Learn More

Watch the following video for a guided tour of the server.

### [](#video-walkthrough)Video Walkthrough