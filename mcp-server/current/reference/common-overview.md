---
title: Couchbase MCP Server
description: Couchbase MCP Server lets AI agents connect to Couchbase Server (on
  Capella or self-managed) or Operational Insights Enterprise. It provides a
  range of tools for cluster health, schema discovery, Query and Index, and
  more. Read-only mode and fine-grained tool controls keep it safe to use.
pubDate: 2026-11-12T06:49:41.760Z
meta:
  component:
    title: Couchbase MCP Server Self-Managed
    version: "1.1"
  topic_type: concept
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/release/1.1/modules/reference/pages/common-overview.adoc
  xref: xref:mcp-server:reference:common-overview.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/current/reference/common-overview.html)

# Couchbase MCP Server

> Couchbase MCP Server lets AI agents connect to Couchbase Server (on Capella or self-managed) or Operational Insights Enterprise. It provides a range of tools for cluster health, schema discovery, Query and Index, and more. Read-only mode and fine-grained tool controls keep it safe to use. 

Couchbase MCP Server is a self-hosted MCP Server that allows AI agents to connect to and interact with data in Couchbase Servers (whether hosted on Capella or self-managed) or Operational Insights Enterprise. It provides tools across categories including Cluster Health, Data Schema, Query, and more — with safety controls via read-only mode and fine-grained tool disabling. It supports both STDIO and Streamable HTTP transports with OAuth capabilities.

Couchbase MCP server is distributed as a Python Package Index (PyPI) package and via Docker. Enterprise support for Couchbase MCP Server is available by licensing [Couchbase AI Data Plane](https://www.couchbase.com/downloads/?family=ai-data-plane), which also entitles use and enterprise support of Couchbase Agent Memory and Couchbase Agent Catalog.

## [](#choose-your-server)Choose Your Server

One package ships two servers. Pick the one that matches the system you want your agents to work with. Each overview lists the tools of that server.

| Server               | Connects To                                        | Start Here                                                                                                 |
| -------------------- | -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Couchbase Server     | Couchbase Server, on Capella or self-managed       | [Overview and tools](../get-started/overview.md) · [Quick Start](../get-started/quickstart.md)             |
| Operational Insights | Operational Insights Enterprise, self-managed only | [Overview and tools](../get-started-oi/overview-oi.md) · [Quick Start](../get-started-oi/quickstart-oi.md) |

For how the two servers fit together, see [Architecture](common-architecture.md).

## [](#releases)Releases

The latest release is available on [PyPI](https://pypi.org/project/couchbase-mcp-server/) and [Docker Hub](https://hub.docker.com/r/couchbase/mcp-server).

See the [Release Notes](release-notes.md) for version history and details.

## [](#support-policy)Support Policy

Enterprise support for Couchbase MCP Server is available by licensing [Couchbase AI Data Plane](https://www.couchbase.com/downloads/?family=ai-data-plane), which also entitles use and enterprise support of Couchbase Agent Memory and Couchbase Agent Catalog.

## [](#learn-more)Learn More

Watch the following video for a guided tour of the server.

### [](#video-walkthrough)Video Walkthrough

## [](#see-also)See Also

* [Architecture](common-architecture.md)
* [Couchbase Server Overview](../get-started/overview.md)
* [Operational Insights Overview](../get-started-oi/overview-oi.md)
* [Registries](registries.md)
* [Release Notes](release-notes.md)