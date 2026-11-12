---
title: Architecture
description: How the Couchbase MCP Server package is built, and what the
  Couchbase Server and Operational Insights servers share.
pubDate: 2026-11-12T06:49:41.760Z
meta:
  component:
    title: Couchbase MCP Server Self-Managed
    version: "1.1"
  topic_type: concept
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/release/1.1/modules/reference/pages/common-architecture.adoc
  xref: xref:mcp-server:reference:common-architecture.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/current/reference/common-architecture.html)

# Architecture

> How the Couchbase MCP Server package is built, and what the Couchbase Server and Operational Insights servers share. 

The Couchbase MCP Server is an implementation of the [Model Context Protocol](https://modelcontextprotocol.io/) that lets MCP-compatible clients, such as Claude Desktop, Cursor, and custom LLM agents, work with Couchbase. One package ships two MCP servers. Each server is a subcommand of the same `couchbase-mcp-server` command.

![One package with a shared core and two servers: operational for Couchbase Server](_images/one-package-two-servers.svg) 

Figure 1\. One Package, Two Servers

## [](#one-package-two-servers)One Package, Two Servers

| Subcommand            | Target                                                 | SDK                                       | Default HTTP Port |
| --------------------- | ------------------------------------------------------ | ----------------------------------------- | ----------------- |
| operational (default) | A Couchbase Server cluster, on Capella or self-managed | Couchbase Python SDK                      | 8000              |
| operational-insights  | A self-managed Couchbase Operational Insights cluster  | couchbase-operational-insights Python SDK | 8001              |

Each process loads only the SDK for its own subcommand. The `operational` subcommand is the default, so existing configurations keep working without changes.

Each server exposes its own set of tools, grouped in categories:

* The Couchbase Server tools cover cluster health, schema discovery, key-value operations, queries and indexes, Search, and query performance. See [Couchbase Server Tools](../learn/tools.md).
* The Operational Insights tools cover database and schema discovery, and SQL++ queries and indexes. See [Operational Insights Tools](../learn-oi/tools-oi.md).

For the component breakdown and request flow of each server, see [Couchbase Server Architecture](../learn/architecture.md) and [Operational Insights Architecture](../learn-oi/architecture-oi.md).

## [](#shared-components)Shared Components

Both servers use the same core for the following components. Each server adds only its own tools and its own SDK connection.

| Component     | What It Does                                                                                                        | Learn More                                                                                                                              |
| ------------- | ------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| FastMCP core  | Hosts the server, registers the tools, and handles the MCP protocol.                                                | [Couchbase Server](../learn/architecture.md) · [Operational Insights](../learn-oi/architecture-oi.md)                                   |
| Configuration | Reads settings from command-line arguments and environment variables.                                               | [Couchbase Server](../configuration/environment-variables.md) · [Operational Insights](../configuration-oi/environment-variables-oi.md) |
| Logging       | Writes operational logs to stderr, and optionally to rotating files.                                                | [Couchbase Server](../configuration/logging.md) · [Operational Insights](../configuration-oi/logging-oi.md)                             |
| Audit logging | Records tool calls, authorization denials, and guardrail blocks in a separate audit log.                            | [Couchbase Server](../configuration/audit-logging.md) · [Operational Insights](../configuration-oi/audit-logging-oi.md)                 |
| OAuth 2.1     | Verifies JWT bearer tokens on the Streamable HTTP transport, and enforces read and write scopes on every tool call. | [Couchbase Server](../configuration/oauth-overview.md) · [Operational Insights](../configuration-oi/oauth-overview-oi.md)               |
| Tool gating   | Controls which tools load. Read-only mode, turned-off tools, and confirmation prompts all use it.                   | [Couchbase Server](../configuration/read-only-mode.md) · [Operational Insights](../configuration-oi/read-only-mode-oi.md)               |

## [](#code-composition)Code Composition

A single codebase powers both servers, which ship together in one wheel and one container image. Each server is a service package that pairs a **ServerSpec** with a provider. The ServerSpec defines the tool set, the scopes, the default port, and the logging target. The provider manages the connection to the SDK. At startup, the shared `cb_mcp` core assembles these into a FastMCP instance.

The core builds the infrastructure features once and both servers use them. These features are tool gating, OAuth authentication, human confirmation, logging, and audit logging. Because the entry point loads only the spec and provider for the selected subcommand, a running process imports only the SDK it needs. Adding another server in the future needs only a new spec and provider, and the shared core does not change.

## [](#shared-security-model)Shared Security Model

Both servers follow the same security defaults:

* **Read-only by default**: `CB_MCP_READ_ONLY_MODE` defaults to `true`. Tools that modify data or structure are not registered in that mode.
* **Optional OAuth for the HTTP transport**: when configured, the server validates JWT bearer tokens from an external identity provider and enforces read and write scopes on every tool call. Both servers use the same scope labels, so one token works across both.
* **Credential isolation**: credentials live only in process memory and are never persisted.
* **Tool gating**: operators can hide tools entirely with `--disabled-tools`, or require human confirmation with `--confirmation-required-tools`.
* **Couchbase RBAC is the final control**: every call runs with the privileges of the configured credentials, regardless of read-only mode.

For the full security reference of each server, see [Couchbase Server Security](../security/security.md) and [Operational Insights Security](../security-oi/security-oi.md).

## [](#shared-observability)Shared Observability

Both servers write logs and audit records the same way. For the settings of each server, use the following pages:

* **Logging**: both servers log to `stderr` by default, with an optional `file` sink for rotating per-level log files. See [Couchbase Server Logging](../configuration/logging.md) and [Operational Insights Logging](../configuration-oi/logging-oi.md).
* **Audit logging**: both servers can record an audit trail in a separate log. See [Couchbase Server Audit Logging](../configuration/audit-logging.md) and [Operational Insights Audit Logging](../configuration-oi/audit-logging-oi.md).

## [](#distribution)Distribution

The server ships through several channels:

* **PyPI package**: `pip install couchbase-mcp-server`. MCP clients typically run it as a local `stdio` subprocess with `uvx`. It supports Python 3.11 to 3.14.
* **Docker image** (`couchbase/mcp-server`): published for tagged releases. It runs as a non-root user, defaults to read-only mode and the `stdio` transport, and exposes port 8000 (`operational`) and port 8001 (`operational-insights`) for the HTTP transport.
* **MCP Registry**: one `server.json` entry lists packages for both subcommands.

## [](#see-also)See Also

* [Overview](common-overview.md)
* [Couchbase Server Architecture](../learn/architecture.md)
* [Operational Insights Architecture](../learn-oi/architecture-oi.md)
* [Couchbase Server Security](../security/security.md)
* [Operational Insights Security](../security-oi/security-oi.md)
* [Release Notes](release-notes.md)