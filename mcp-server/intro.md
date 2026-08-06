---
title: Capella MCP Server
description: ""
editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/main/modules/ROOT/pages/intro.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:mcp-server::intro.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/intro.html)

# Capella MCP Server

Couchbase MCP Server is a self-hosted MCP Server that allows AI agents to connect to and interact with data in Couchbase clusters, whether hosted on Capella or self-managed. It provides tools across categories including Cluster Health, Data Schema, Key-Value, Query, and Performance — with safety controls via read-only mode and fine-grained tool disabling. It supports both `STDIO` and Streamable HTTP transports.

Couchbase distributes MCP Server as a Python Package Index (PyPI) package and via Docker. A Couchbase AI Data Plane license provides enterprise support for Couchbase MCP Server, and also includes use and enterprise support of Couchbase Agent Memory and Couchbase Agent Catalog.

> [!NOTE]
> For the complete MCP Server Documentation, see <https://mcp-server.couchbase.com/>.

![architecture v1.0](_images/architecture-v1.0.png) 

Figure 1\. MCP Server Architecture

## [](#tools)Tools

The server exposes several tools across multiple categories.

See the [Tools](https://mcp-server.couchbase.com/tools) page for full details.

| Category                      | Tools                                                                                                                                                                                                                                                              |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Cluster Setup & Health        | get\_server\_configuration\_status, test\_cluster\_connection, get\_cluster\_health\_and\_services                                                                                                                                                                 |
| Data Model & Schema Discovery | get\_buckets\_in\_cluster, get\_scopes\_in\_bucket, get\_collections\_in\_scope, get\_scopes\_and\_collections\_in\_bucket, get\_schema\_for\_collection                                                                                                           |
| Document KV Operations        | get\_document\_by\_id, upsert\_document\_by\_id, insert\_document\_by\_id, replace\_document\_by\_id, delete\_document\_by\_id                                                                                                                                     |
| Query and Indexing            | run\_sql\_plus\_plus\_query, explain\_sql\_plus\_plus\_query, list\_indexes, get\_index\_advisor\_recommendations                                                                                                                                                  |
| Query Performance Analysis    | get\_longest\_running\_queries, get\_most\_frequent\_queries, get\_queries\_not\_selective, get\_queries\_not\_using\_covering\_index, get\_queries\_using\_primary\_index, get\_queries\_with\_largest\_response\_sizes, get\_queries\_with\_large\_result\_count |

## [](#releases)Releases

The latest release is available on [PyPI](https://pypi.org/project/couchbase-mcp-server/) and [Docker Hub](https://hub.docker.com/r/couchbase/mcp-server).

See the [Release Notes](https://mcp-server.couchbase.com/product-notes/release-notes) for version history and details.