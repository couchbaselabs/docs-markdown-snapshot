---
title: Disabling Tools
description: Disable specific Couchbase MCP Server tools so they aren't loaded,
  discovered, or callable by the LLM.
pubDate: 2026-11-12T06:49:41.760Z
meta:
  component:
    title: Couchbase MCP Server Self-Managed
    version: "1.1"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/release/1.1/modules/configuration-oi/pages/disabling-tools-oi.adoc
  xref: xref:mcp-server:configuration-oi:disabling-tools-oi.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/current/configuration-oi/disabling-tools-oi.html)

# Disabling Tools

> Disable specific Couchbase MCP Server tools so they aren't loaded, discovered, or callable by the LLM. 

You can disable specific tools to prevent the server from loading and exposing them to the MCP client. Disabled tools don't appear in tool discovery, the LLM can't invoke them, and disabling them cuts noise and unnecessary token consumption.

## [](#how-it-works)How It Works

When you specify tools to disable, the server doesn't load those tools at startup. If you disable a tool, any attempt to call it from the client results in an error response indicating that the tool is unavailable.

## [](#configuration)Configuration

| Environment Variable     | CLI Argument      | Description                                                | Default |  |
| ------------------------ | ----------------- | ---------------------------------------------------------- | ------- |  |
| CB\_MCP\_DISABLED\_TOOLS | \--disabled-tools | Comma-separated list or file path of tool names to disable | None    |  |

## [](#supported-formats)Supported Formats

`CB_MCP_DISABLED_TOOLS` accepts either of these formats.

### [](#comma-separated-list)Comma-Separated List

```bash
# Environment variable
CB_MCP_DISABLED_TOOLS="operational_insights_create_index, operational_insights_cancel_async_query"

# Command line
uvx couchbase-mcp-server operational-insights --disabled-tools "operational_insights_create_index, operational_insights_cancel_async_query"
```

### [](#file-path-one-tool-per-line)File Path (One Tool Per Line)

```bash
# Environment variable
CB_MCP_DISABLED_TOOLS=/path/to/disabled_tools.txt

# Command line
uvx couchbase-mcp-server operational-insights --disabled-tools /path/to/disabled_tools.txt
```

File format example (`disabled_tools.txt`):

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
        "CB_MCP_DISABLED_TOOLS": "operational_insights_create_index,operational_insights_cancel_async_query"
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
        "CB_MCP_DISABLED_TOOLS": "/path/to/disabled_tools.txt"
      }
    }
  }
}
```

## [](#important-security-note)Important Security Note

> [!WARNING]
> Disabling tools alone doesn't prevent certain operations from happening.

The underlying database user's RBAC (Role-Based Access Control) permissions are the authoritative security control. For example, even if you disable `operational_insights_create_index`, you can still attempt index and structural changes via the `operational_insights_run_query_sync`/`operational_insights_run_query_async` tools using SQL++ DDL statements unless:

* `CB_MCP_READ_ONLY_MODE` is set to `true` (default), which runs SQL++ queries with the server-side `readonly` option,

**OR**

* The database user lacks the necessary RBAC permissions

> [!TIP]
> Best Practice
> 
> Always configure appropriate RBAC permissions on your Couchbase user credentials as the primary security measure. See [RBAC for Couchbase Server](https://docs.couchbase.com/server/current/manage/manage-security/manage-users-and-roles.html). Use tool disabling as an additional layer to guide LLM behavior and reduce the attack surface, not as the sole security control.