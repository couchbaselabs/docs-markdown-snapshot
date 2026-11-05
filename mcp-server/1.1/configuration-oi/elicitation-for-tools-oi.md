---
title: Elicitation / Confirmation for Tool Calls
description: Require user confirmation before the LLM executes specific
  Couchbase MCP Server tools.
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase MCP Server
    version: "1.1"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/release/1.1/modules/configuration-oi/pages/elicitation-for-tools-oi.adoc
  xref: xref:1.1@mcp-server:configuration-oi:elicitation-for-tools-oi.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/1.1/configuration-oi/elicitation-for-tools-oi.html)

# Elicitation / Confirmation for Tool Calls

> Require user confirmation before the LLM executes specific Couchbase MCP Server tools. 

The `CB_MCP_CONFIRMATION_REQUIRED_TOOLS` environment variable enables user confirmation prompts for tools marked as requiring confirmation. This allows users to double-check the tool call before the LLM executes the actions.

## [](#how-it-works)How It Works

When a tool requires confirmation, the server sends an [elicitation](https://modelcontextprotocol.io/docs/concepts/elicitation) request to the client.

**Clients with elicitation support:**

1. Prompt the user for confirmation.
2. Send the user's response back to the server.

**Clients without elicitation support:** The tool executes **without confirmation**. The server logs this at `DEBUG` level only, so no warning appears at the default log level. When audit logging is on, the server records a `confirmation skipped` event (57491). See [Audit Events](audit-logging-oi.md#audit-events).

> [!IMPORTANT]
> Full functionality requires client support for [elicitation](https://modelcontextprotocol.io/clients).

## [](#configuration)Configuration

| Environment Variable                   | CLI Argument                   | Description                                                                                                 | Default |  |
| -------------------------------------- | ------------------------------ | ----------------------------------------------------------------------------------------------------------- | ------- |  |
| CB\_MCP\_CONFIRMATION\_REQUIRED\_TOOLS | \--confirmation-required-tools | Comma-separated list or file path of tool names that require elicitation/user confirmation before execution | None    |  |

## [](#supported-formats)Supported Formats

Both settings accept the same two formats.

### [](#comma-separated-list)Comma-Separated List

```bash
# Environment variable
CB_MCP_CONFIRMATION_REQUIRED_TOOLS="operational_insights_create_index, operational_insights_cancel_async_query"

# Command line
uvx couchbase-mcp-server operational-insights --confirmation-required-tools "operational_insights_create_index, operational_insights_cancel_async_query"
```

### [](#file-path-one-tool-per-line)File Path (One Tool Per Line)

```bash
# Environment variable
CB_MCP_CONFIRMATION_REQUIRED_TOOLS=/path/to/confirmation_required_tools.txt

# Command line
uvx couchbase-mcp-server operational-insights --confirmation-required-tools /path/to/confirmation_required_tools.txt
```

File format example (`confirmation_required_tools.txt`):

```text
# Index and async query management
operational_insights_create_index
operational_insights_cancel_async_query
```

The server treats lines starting with `#` as comments and ignores them.

## [](#mcp-client-configuration-examples)MCP Client Configuration Examples

**Using comma-separated list:**

```json
{
  "mcpServers": {
    "couchbase-oi": {
      "command": "uvx",
      "args": ["couchbase-mcp-server", "operational-insights"],
      "env": {
        "CB_OPERATIONAL_INSIGHTS_CONNECTION_STRING": "https://your-oi-endpoint",
        "CB_OPERATIONAL_INSIGHTS_USERNAME": "username",
        "CB_OPERATIONAL_INSIGHTS_PASSWORD": "password",
        "CB_MCP_CONFIRMATION_REQUIRED_TOOLS": "operational_insights_create_index,operational_insights_cancel_async_query"
      }
    }
  }
}
```

**Using file path (recommended for many tools):**

```json
{
  "mcpServers": {
    "couchbase-oi": {
      "command": "uvx",
      "args": ["couchbase-mcp-server", "operational-insights"],
      "env": {
        "CB_OPERATIONAL_INSIGHTS_CONNECTION_STRING": "https://your-oi-endpoint",
        "CB_OPERATIONAL_INSIGHTS_USERNAME": "username",
        "CB_OPERATIONAL_INSIGHTS_PASSWORD": "password",
        "CB_MCP_CONFIRMATION_REQUIRED_TOOLS": "/path/to/confirmation_required_tools.txt"
      }
    }
  }
}
```

## [](#important-limitations)Important Limitations

* Elicitation does not work with stateless mode. A confirmation prompt needs a session, and stateless mode keeps no session. The server refuses to start when you combine `--confirmation-required-tools` with `--stateless-http`. See [Stateless Mode and Workers](streamable-http-oi.md#stateless-mode-and-workers).
* Setting `CB_MCP_CONFIRMATION_REQUIRED_TOOLS` for a tool that **did not load** has no effect, as the tool is not available. A tool does not load if it's explicitly listed under the `disabled_tools` configuration, or if the server runs in **READ\_ONLY** mode and the tool is not a **READ\_ONLY** tool.

> [!WARNING]
> The confirmation\_required setting applies explicitly to tools, not to individual actions (such as read, update, or delete operations).
> 
> For example, if you enable confirmation\_required for the `operational_insights_create_index` tool, the MCP server prompts for confirmation only when the MCP client selects that specific tool. The server doesn't request confirmation if the client selects a different tool, such as `operational_insights_run_query_sync` to run a raw `CREATE INDEX` SQL++ statement directly.