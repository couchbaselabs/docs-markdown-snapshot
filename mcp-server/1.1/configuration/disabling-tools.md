---
title: Disabling Tools
description: Disable specific Couchbase MCP Server tools so they aren't loaded,
  discovered, or callable by the LLM.
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase MCP Server
    version: "1.1"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/release/1.1/modules/configuration/pages/disabling-tools.adoc
  xref: xref:1.1@mcp-server:configuration:disabling-tools.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/1.1/configuration/disabling-tools.html)

# Disabling Tools

> Disable specific Couchbase MCP Server tools so they aren't loaded, discovered, or callable by the LLM. 

You can disable specific tools to prevent the server from loading and exposing them to the MCP client. Disabled tools don't appear in tool discovery, the LLM can't invoke them, and disabling them cuts noise and unnecessary token consumption.

## [](#how-it-works)How It Works

> [!NOTE]
> The commands on this page start the operational server, which is the default. Adding `operational` to the command, as in `uvx couchbase-mcp-server operational`, gives the same result.

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
CB_MCP_DISABLED_TOOLS="upsert_document_by_id, delete_document_by_id"

# Command line
uvx couchbase-mcp-server --disabled-tools "upsert_document_by_id, delete_document_by_id"
```

### [](#file-path-one-tool-per-line)File Path (One Tool Per Line)

```bash
# Environment variable
CB_MCP_DISABLED_TOOLS=/path/to/disabled_tools.txt

# Command line
uvx couchbase-mcp-server --disabled-tools /path/to/disabled_tools.txt
```

File format example (`disabled_tools.txt`):

```text
# Write operations
upsert_document_by_id
delete_document_by_id

# Index advisor
get_index_advisor_recommendations
```

The server treats lines starting with `#` as comments and ignores them.

## [](#mcp-client-configuration-examples)MCP Client Configuration Examples

**Using comma-separated list:**

```json
{
  "mcpServers": {
    "couchbase": {
      "command": "uvx",
      "args": ["couchbase-mcp-server"],
      "env": {
        "CB_CONNECTION_STRING": "couchbases://your-connection-string",
        "CB_USERNAME": "username",
        "CB_PASSWORD": "password",
        "CB_MCP_DISABLED_TOOLS": "upsert_document_by_id,delete_document_by_id"
      }
    }
  }
}
```

**Using file path (recommended for many tools):**

```json
{
  "mcpServers": {
    "couchbase": {
      "command": "uvx",
      "args": ["couchbase-mcp-server"],
      "env": {
        "CB_CONNECTION_STRING": "couchbases://your-connection-string",
        "CB_USERNAME": "username",
        "CB_PASSWORD": "password",
        "CB_MCP_DISABLED_TOOLS": "/path/to/disabled_tools.txt"
      }
    }
  }
}
```

## [](#tools-the-server-disables-automatically)Tools the Server Disables Automatically

The server also turns off some tools on its own. Several tools reach Couchbase through administrative REST endpoints that Capella does not expose. The server does not load these tools when `CB_CONNECTION_STRING` points at a Capella cluster. This happens whether or not you set `CB_MCP_DISABLED_TOOLS`.

`get_server_configuration_status` reports these tools in the same list as the ones you turned off, and the server lists them in the startup log. For the tools this affects and the deployments each one supports, see [Tools Not Available on Capella](../learn/tools.md#tools-not-available-on-capella).

## [](#important-security-note)Important Security Note

> [!WARNING]
> Disabling tools alone doesn't prevent certain operations from happening.

The underlying database user's RBAC (Role-Based Access Control) permissions are the authoritative security control. For example, even if you disable `upsert_document_by_id` and `delete_document_by_id`, you can still make data modifications via the `run_sql_plus_plus_query` tool using SQL++ DML statements (INSERT, UPDATE, DELETE, MERGE) unless:

* `CB_MCP_READ_ONLY_MODE` is set to `true` (default),

**OR**

* The database user lacks the necessary RBAC permissions

> [!TIP]
> Best Practice
> 
> Always configure appropriate RBAC permissions on your Couchbase user credentials as the primary security measure. See [RBAC for Couchbase Server](https://docs.couchbase.com/server/current/manage/manage-security/manage-users-and-roles.html) or [RBAC for Capella](https://docs.couchbase.com/cloud/clusters/manage-database-users.html). Use tool disabling as an additional layer to guide LLM behavior and reduce the attack surface, not as the sole security control.