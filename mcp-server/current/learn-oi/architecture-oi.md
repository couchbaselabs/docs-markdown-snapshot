---
title: Architecture
description: Component breakdown and request flow for the Couchbase MCP Server's
  Operational Insights topology.
pubDate: 2026-11-12T06:49:41.760Z
meta:
  component:
    title: Couchbase MCP Server Self-Managed
    version: "1.1"
  topic_type: concept
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/release/1.1/modules/learn-oi/pages/architecture-oi.adoc
  xref: xref:mcp-server:learn-oi:architecture-oi.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/current/learn-oi/architecture-oi.html)

# Architecture

> Component breakdown and request flow for the Couchbase MCP Server's Operational Insights topology. 

The Couchbase MCP Server for Operational Insights is a self-hosted bridge between AI agents and a Couchbase Operational Insights endpoint. It follows a three-tier topology — **MCP Client → MCP Server → Operational Insights Cluster**. The server exposes Operational Insights capabilities as MCP tools, enforces authentication and safety controls, and talks to the cluster through the couchbase-operational-insights Python SDK. Clients connect over one of two transports: `stdio` (local subprocess) or [Streamable HTTP](../configuration-oi/streamable-http-oi.md) (networked, multi-client).

> [!IMPORTANT]
> The Operational Insights MCP server supports only self-managed deployments. Capella-hosted Operational Insights is not supported.

This page covers the Operational Insights (`operational-insights`) server. For the components that both servers share, see [Architecture](../reference/common-architecture.md).

## [](#how-it-works-a-quick-example)How It Works — A Quick Example

The following example illustrates a typical request. An analyst asks: "Which databases do we have, and how many orders came in last month in the `sales` database?"

1. On receiving the prompt, the agent first discovers what's available by calling `operational_insights_get_databases_in_cluster`, then `operational_insights_get_scopes_in_database` and `operational_insights_get_collections_in_scope` for the `sales` database.
2. It calls `operational_insights_get_schema_for_collection` to infer the real structure of the orders collection, rather than guessing field names.
3. With the real schema known, it generates a SQL++ analytics query grounded in that schema.
4. It submits the query with `operational_insights_run_query_sync` (or, for a long-running query, `operational_insights_run_query_async` followed by `operational_insights_get_async_query_results`), and the server returns the results over the MCP protocol.

Finally, the agent's LLM shapes the result into a natural-language answer for the analyst. Notably, the model never touches the Operational Insights cluster directly — every data access goes through the MCP server.

## [](#components-responsibilities)Components & Responsibilities

| Component                                    | Responsibility                                                                                                                                                                      | Learn more                                                                                                 |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| **MCP Client**                               | The AI agent or IDE (VS Code, Claude Desktop, Cursor, …) that discovers and invokes tools.                                                                                          | [Quick Start](../get-started-oi/quickstart-oi.md)                                                          |
| **Transport**                                | How the client reaches the server: stdio (local subprocess) or Streamable HTTP (networked, serves /mcp).                                                                            | [Streamable HTTP](../configuration-oi/streamable-http-oi.md)                                               |
| **MCP Server**                               | The server process (distributed via PyPI and Docker, built on the FastMCP SDK), running the operational-insights subcommand. Hosts the tools and enforces auth and safety controls. | [Overview](../get-started-oi/overview-oi.md)                                                               |
| **Tool layer**                               | The tools the server exposes — database, scope, and collection discovery, schema inference, and query execution/management — split into read and write tools.                       | [Tools](tools-oi.md)                                                                                       |
| **Safety controls**                          | Server-side gating of which tools load and run: read-only mode, disabled tools, and confirmation/elicitation.                                                                       | [Read-Only Mode](../configuration-oi/read-only-mode-oi.md) · [Security](../security-oi/security-oi.md)     |
| **OAuth resource server**                    | On Streamable HTTP, verifies client JWTs (signature via JWKS, plus iss/aud/scopes) and optionally publishes PRM for discovery/DCR.                                                  | [OAuth](../configuration-oi/oauth-overview-oi.md)                                                          |
| **couchbase-operational-insights SDK**       | The client library the server uses to perform SQL++ query operations against the Operational Insights cluster.                                                                      | —                                                                                                          |
| **Operational Insights Cluster**             | A self-managed Couchbase Operational Insights deployment. **RBAC on the server's credentials is the authoritative data-access control.**                                            | [Security](../security-oi/security-oi.md)                                                                  |
| **Identity Provider / Authorization Server** | External service that authenticates users/agents and issues signed JWTs (exposes JWKS and issuer).                                                                                  | [OAuth](../configuration-oi/oauth-overview-oi.md)                                                          |
| **Reverse proxy / TLS**                      | For networked deployments, terminates TLS in front of the server so the connection encrypts traffic and tokens in transit.                                                          | [Securing the Endpoint with TLS](../configuration-oi/streamable-http-oi.md#securing-the-endpoint-with-tls) |
| **Logging / observability**                  | Structured logs with configurable level and sinks (stderr / file).                                                                                                                  | [Logging](../configuration-oi/logging-oi.md)                                                               |

## [](#network-path)Network Path

The MCP server connects to the Operational Insights cluster over HTTP(S) via the couchbase-operational-insights SDK, typically port 8095 (HTTP) or 18095 (HTTPS).

## [](#authentication-planes)Authentication Planes

The server has **two independent authentication planes**:

* **Client → Server**: secured with **OAuth** (Streamable HTTP only). Decides which client may connect and which tools it may call.
* **Server → Operational Insights Cluster**: uses your **Operational Insights cluster credentials** (Basic Auth or mTLS, set via `CB_OPERATIONAL_INSIGHTS_*` environment variables). Decides what data the server can actually touch.

They're enforced separately, and **RBAC on the Operational Insights cluster is the ultimate authority** over data access. For details, see [OAuth](../configuration-oi/oauth-overview-oi.md) and [Security](../security-oi/security-oi.md).

## [](#sql-readwrite-enforcement)SQL++ Read/Write Enforcement

In read-only mode, the server runs SQL++ statements with the server-side `readonly` query option, rather than client-side AST parsing. `COPY …​ TO` (export) statements are also blocked client-side.

## [](#see-also)See Also

* [Overview](../get-started-oi/overview-oi.md)
* [Tools](tools-oi.md)
* [OAuth](../configuration-oi/oauth-overview-oi.md)
* [Security](../security-oi/security-oi.md)
* [Streamable HTTP Transport Mode](../configuration-oi/streamable-http-oi.md)
* [Logging](../configuration-oi/logging-oi.md)