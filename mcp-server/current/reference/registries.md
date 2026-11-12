---
title: Registries
description: Where the Couchbase MCP Server is listed for discovery and
  installation, including the MCP Registry and Docker MCP Catalog.
pubDate: 2026-11-12T06:49:41.760Z
meta:
  component:
    title: Couchbase MCP Server Self-Managed
    version: "1.1"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/release/1.1/modules/reference/pages/registries.adoc
  xref: xref:mcp-server:reference:registries.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/current/reference/registries.html)

# Registries

> Where the Couchbase MCP Server is listed for discovery and installation, including the MCP Registry and Docker MCP Catalog. 

The Couchbase MCP Server is listed on several MCP server registries. These registries make it easy to discover, install, and configure the server.

## [](#mcp-registry)MCP Registry

The [MCP Registry](https://registry.modelcontextprotocol.io/) is the official registry for MCP servers maintained by the MCP specification authors.

* **Package ID:** `io.github.couchbase/mcp-server-couchbase`
* **Packages:** PyPI (`couchbase-mcp-server`) and OCI (`docker.io/couchbase/mcp-server`)
* **Configuration:** Defined in [server.json](https://github.com/couchbase/mcp-server-couchbase/blob/main/server.json) at the repository root.
* **Operational Insights:** The `operational-insights` subcommand appears as an install option under the same listing as the operational server.

## [](#docker-mcp-catalog)Docker MCP Catalog

The [Docker MCP Catalog](https://docs.docker.com/ai/mcp-catalog-and-toolkit/catalog/) provides a curated listing of MCP servers available as Docker images.

* **Listing:** [Couchbase MCP Server on Docker MCP Catalog](https://hub.docker.com/mcp/server/couchbase/overview)
* **Image:** [mcp/couchbase](https://hub.docker.com/mcp/server/couchbase/overview)
* **Configuration:** Defined in the [Docker MCP Registry](https://github.com/docker/mcp-registry/blob/main/servers/couchbase/server.yaml).

## [](#glama-ai)Glama.ai

[Glama](https://glama.ai/mcp/connectors) provides an MCP server directory for AI agents and LLM applications, allowing users to easily find and connect to MCP servers for their AI projects.

* **Listing:** [Couchbase MCP Server on Glama](https://glama.ai/mcp/servers/couchbase/mcp-server-couchbase)