---
title: Couchbase MCP Server
description: Couchbase MCP Server lets AI agents connect to Couchbase clusters,
  on Capella or self-managed. It provides tools for cluster health, schema
  discovery, key-value operations, and query performance. Read-only mode and
  fine-grained tool controls keep it safe to use.
pubDate: 2026-08-22T04:32:17.641Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/release/1.0/modules/get-started/pages/overview.adoc
  xref: xref:mcp-server:get-started:overview.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/get-started/overview.html)

# Couchbase MCP Server

> Couchbase MCP Server lets AI agents connect to Couchbase clusters, on Capella or self-managed. It provides tools for cluster health, schema discovery, key-value operations, and query performance. Read-only mode and fine-grained tool controls keep it safe to use. 

Couchbase MCP Server is a self-hosted MCP Server that allows AI agents to connect to and interact with data in Couchbase clusters, whether hosted on Capella or self-managed. It provides tools across categories including Cluster Health, Data Schema, Key-Value, Query, and Performance — with safety controls via read-only mode and fine-grained tool disabling. It supports both STDIO and Streamable HTTP transports.

Couchbase MCP server is distributed as a Python Package Index (PyPI) package and via Docker. Enterprise support for Couchbase MCP Server is available by licensing [Couchbase AI Data Plane](https://www.couchbase.com/downloads/?family=ai-data-plane), which also entitles use and enterprise support of Couchbase Agent Memory and Couchbase Agent Catalog.

## [](#architecture)Architecture

![architecture v1.0](_images/architecture-v1.0.png) 

Figure 1\. Couchbase MCP Server Architecture

For the component breakdown and request flow, see [Architecture](../learn/architecture.md).

## [](#tools)Tools

The server exposes several tools across multiple categories.

See the [Tools](../learn/tools.md) page for full details.

| Category                          | Tools                                                                                                                                                                                                                                                              |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Cluster Setup & Health**        | get\_server\_configuration\_status, test\_cluster\_connection, get\_cluster\_health\_and\_services                                                                                                                                                                 |
| **Data Model & Schema Discovery** | get\_buckets\_in\_cluster, get\_scopes\_in\_bucket, get\_collections\_in\_scope, get\_scopes\_and\_collections\_in\_bucket, get\_schema\_for\_collection                                                                                                           |
| **Document KV Operations**        | get\_document\_by\_id, upsert\_document\_by\_id, insert\_document\_by\_id, replace\_document\_by\_id, delete\_document\_by\_id                                                                                                                                     |
| **Query and Indexing**            | run\_sql\_plus\_plus\_query, explain\_sql\_plus\_plus\_query, list\_indexes, get\_index\_advisor\_recommendations                                                                                                                                                  |
| **Query Performance Analysis**    | get\_longest\_running\_queries, get\_most\_frequent\_queries, get\_queries\_not\_selective, get\_queries\_not\_using\_covering\_index, get\_queries\_using\_primary\_index, get\_queries\_with\_largest\_response\_sizes, get\_queries\_with\_large\_result\_count |

## [](#releases)Releases

The latest release is available on [PyPI](https://pypi.org/project/couchbase-mcp-server/) and [Docker Hub](https://hub.docker.com/r/couchbase/mcp-server).

See the [Release Notes](../reference/release-notes.md) for version history and details.

## [](#support-policy)Support Policy

Enterprise support for Couchbase MCP Server is available by licensing [Couchbase AI Data Plane](https://www.couchbase.com/downloads/?family=ai-data-plane), which also entitles use and enterprise support of Couchbase Agent Memory and Couchbase Agent Catalog.

## [](#learn-more)Learn More

Watch the video below for a guided tour of the server.

### [](#video-walkthrough)Video Walkthrough