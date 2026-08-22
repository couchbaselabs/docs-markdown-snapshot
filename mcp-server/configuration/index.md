---
title: Configuration
description: Overview of the environment variable and command-line options
  available for configuring the Couchbase MCP Server.
pubDate: 2026-08-22T04:32:17.641Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/release/1.0/modules/configuration/pages/index.adoc
  xref: xref:mcp-server:configuration:index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/configuration/index.html)

# Configuration

> Overview of the environment variable and command-line options available for configuring the Couchbase MCP Server. 

The Couchbase MCP Server can be configured through environment variables or command line arguments set in your MCP client configuration. This allows you to customize server behavior, authentication, transport settings, and more.

## [](#configuration-topics)Configuration Topics

* **[Environment Variables & Command Line Arguments](environment-variables.md)**: Full reference of all configuration options, authentication examples, and transport settings.
* **[Read-Only Mode](read-only-mode.md)**: Control write access to your cluster. Enabled by default for safety.
* **[Streamable HTTP Transport Mode](streamable-http.md)**: Run the server in Streamable HTTP transport mode for multi-client access.
* **[OAuth](oauth-overview.md)**: Secure the Streamable HTTP endpoint with OAuth 2.1 JWT token verification and scope-based authorization.
* **[Disabling Tools](disabling-tools.md)**: Selectively disable individual tools via configuration.
* **[Elicitation/Confirmation for Tool Calls](elicitation-for-tools.md)**: Require user confirmation before executing specific tools.
* **[Logging](logging.md)**: Configure log level, output sinks (console/file), and file logging for supportability.