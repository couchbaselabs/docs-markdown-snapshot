---
title: Configuration
description: Overview of the environment variable and command-line options
  available for configuring the Couchbase MCP Server.
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase MCP Server
    version: "1.1"
  topic_type: concept
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/release/1.1/modules/configuration-oi/pages/index-oi.adoc
  xref: xref:1.1@mcp-server:configuration-oi:index-oi.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/1.1/configuration-oi/index-oi.html)

# Configuration

> Overview of the environment variable and command-line options available for configuring the Couchbase MCP Server. 

You can configure the Couchbase MCP Server through environment variables or command line arguments set in your MCP client configuration. This allows you to customize server behavior, authentication, transport settings, and more.

## [](#configuration-topics)Configuration Topics

* **[Environment Variables & Command Line Arguments](environment-variables-oi.md)**: Full reference of all configuration options, authentication examples, and transport settings.
* **[Read-Only Mode](read-only-mode-oi.md)**: Control write access to your cluster. Enabled by default for safety.
* **[Streamable HTTP Transport Mode](streamable-http-oi.md)**: Run the server in Streamable HTTP transport mode for multi-client access.
* **[OAuth](oauth-overview-oi.md)**: Secure the Streamable HTTP endpoint with OAuth 2.1 JWT token verification and scope-based authorization.
* **[Disabling Tools](disabling-tools-oi.md)**: Selectively disable individual tools via configuration.
* **[Elicitation/Confirmation for Tool Calls](elicitation-for-tools-oi.md)**: Require user confirmation before executing specific tools.
* **[Logging](logging-oi.md)**: Configure log level, output sinks (console/file), and file logging for supportability.
* **[Audit Logging](audit-logging-oi.md)**: Record tool calls, authorization denials, and guardrail blocks in a separate audit log.
* **[Large Result Handling](large-results-oi.md)**: Limit the size of query results, or export a large result to object storage.