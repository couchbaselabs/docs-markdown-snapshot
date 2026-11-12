---
title: Architecture
description: Component breakdown and request flow for the Couchbase MCP Server's
  client-server-cluster topology.
pubDate: 2026-11-12T06:49:41.760Z
meta:
  component:
    title: Couchbase MCP Server Self-Managed
    version: "1.1"
  topic_type: concept
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/release/1.1/modules/learn/pages/architecture.adoc
  xref: xref:mcp-server:learn:architecture.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/current/learn/architecture.html)

# Architecture

> Component breakdown and request flow for the Couchbase MCP Server's client-server-cluster topology. 

The Couchbase MCP Server is a self-hosted bridge between AI agents and Couchbase. It follows a three-tier topology — **MCP Client → MCP Server → Couchbase Cluster**. The server exposes Couchbase capabilities as MCP tools, enforces authentication and safety controls, and talks to the cluster through the Couchbase Python SDK. Clients connect over one of two transports: `stdio` (local subprocess) or [Streamable HTTP](../configuration/streamable-http.md) (networked, multi-client).

This page covers the Couchbase Server (`operational`) server. For the components that both servers share, see [Architecture](../reference/common-architecture.md).

![Overview and request flow of the Couchbase MCP Server for Couchbase Server](../reference/_images/overview_and_flow.png) 

Figure 1\. Overview and Request Flow

## [](#how-it-works-a-quick-example)How It Works — A Quick Example

The following example illustrates a typical request. A shopper using a retailer's shop bot asks: "Show me fleece jackets that can be delivered tomorrow." The retailer's inventory lives in Couchbase, and the Couchbase MCP Server is already configured so the shop bot can query that data. It has the correct MCP access and the appropriate tools exposed by the server.

1. On receiving the prompt, the shop bot first determines where to look. Because it's integrated with the Couchbase MCP Server, it knows the data resides there.
2. It calls the schema tools first — retrieving the scopes, collections, and schemas — to discover which collection holds the jacket inventory. Rather than guessing field names, it reads the real structure of the data.
3. With the real collections and fields known, it generates a SQL++ query grounded in that schema — here, fetching the jacket documents filtered by one-day delivery.
4. It then makes a second tool call to run the SQL++ query. The Couchbase MCP Server executes it, fetches the relevant documents, and returns them to the shop bot over the MCP protocol.

Finally, the shop bot's LLM shapes the result into a natural-language answer for the shopper. Notably, the model never touches the database directly — every data access goes through the MCP server.

## [](#components-responsibilities)Components & Responsibilities

![Foundational elements of the Couchbase MCP Server for Couchbase Server](../reference/_images/architecture-v1.0.png) 

Figure 2\. Component Architecture

| Component                                    | Responsibility                                                                                                                                                                       | Learn more                                                                                           |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- |
| **MCP Client**                               | The AI agent or IDE (VS Code, Claude Desktop, Cursor, …) that discovers and invokes tools.                                                                                           | [Quick Start](../get-started/quickstart.md)                                                          |
| **Transport**                                | How the client reaches the server: stdio (local subprocess) or Streamable HTTP (networked, serves /mcp).                                                                             | [Streamable HTTP](../configuration/streamable-http.md)                                               |
| **MCP Server**                               | The server process (distributed via PyPI and Docker, built on the FastMCP SDK), running the operational (default) subcommand. Hosts the tools and enforces auth and safety controls. | [Overview](../get-started/overview.md)                                                               |
| **Tool layer**                               | The tools the server exposes — Cluster Health, Schema Discovery, Key-Value, Query and Index, Search, and Performance — split into read and write tools.                              | [Tools](tools.md)                                                                                    |
| **Safety controls**                          | Server-side gating of which tools load and run: read-only mode, disabled tools, and confirmation/elicitation.                                                                        | [Read-Only Mode](../configuration/read-only-mode.md) · [Security](../security/security.md)           |
| **OAuth resource server**                    | On Streamable HTTP, verifies client JWTs (signature via JWKS, plus iss/aud/scopes) and optionally publishes PRM for discovery/DCR.                                                   | [OAuth](../configuration/oauth-overview.md)                                                          |
| **Couchbase Python SDK**                     | The client library the server uses to perform KV operations and SQL++/Query against the cluster.                                                                                     | —                                                                                                    |
| **Couchbase Cluster**                        | Capella or self-managed Couchbase. **RBAC on the server's credentials is the authoritative data-access control.**                                                                    | [Security](../security/security.md)                                                                  |
| **Identity Provider / Authorization Server** | External service that authenticates users/agents and issues signed JWTs (exposes JWKS and issuer).                                                                                   | [OAuth](../configuration/oauth-overview.md)                                                          |
| **Reverse proxy / TLS**                      | For networked deployments, terminates TLS in front of the server so the connection encrypts traffic and tokens in transit.                                                           | [Securing the Endpoint with TLS](../configuration/streamable-http.md#securing-the-endpoint-with-tls) |
| **Logging / observability**                  | Structured logs with configurable level and sinks (stderr / file).                                                                                                                   | [Logging](../configuration/logging.md)                                                               |

## [](#network-path)Network Path

The MCP server connects to the Couchbase cluster using the Couchbase binary protocol via the Couchbase Python SDK, over `couchbase://` or `couchbases://` (TLS).

A few tools call Couchbase REST APIs directly instead of going through the SDK:

* The Cluster Manager, on port 8091 (or 18091 with TLS) — used by tools such as `get_cluster_metrics` and `get_cluster_tasks`.
* The Index Service, on port 9102 (or 19102 with TLS) — used by tools such as `get_index_stats`.

## [](#authentication-planes)Authentication Planes

The server has **two independent authentication planes**:

* **Client → Server**: secured with **OAuth** (Streamable HTTP only). Decides which client may connect and which tools it may call.
* **Server → Cluster**: uses your **cluster credentials** (Basic Auth or mTLS). Decides what data the server can actually touch.

They're enforced separately, and **cluster RBAC is the ultimate authority** over data access. For details, see [OAuth](../configuration/oauth-overview.md) and [Security](../security/security.md).

## [](#sql-readwrite-enforcement)SQL++ Read/Write Enforcement

In read-only mode, `run_sql_plus_plus_query` uses AST-based parsing via `lark-sqlpp` rather than regex matching, so regex-based evasion tricks that sometimes bypass simpler checks don't work against it. The check is deny-by-default: it permits only query (DQL) and utility statements. The check blocks all data modification (DML: INSERT, UPDATE, DELETE, MERGE and similar), structural modification (DDL: CREATE, DROP, ALTER and similar), and privilege changes (DCL: GRANT, REVOKE).

## [](#see-also)See Also

* [Overview](../get-started/overview.md)
* [Tools](tools.md)
* [OAuth](../configuration/oauth-overview.md)
* [Security](../security/security.md)
* [Streamable HTTP Transport Mode](../configuration/streamable-http.md)
* [Logging](../configuration/logging.md)