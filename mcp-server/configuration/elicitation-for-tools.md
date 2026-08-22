---
title: Elicitation / Confirmation for Tool Calls
description: Require user confirmation before the LLM executes specific
  Couchbase MCP Server tools.
pubDate: 2026-08-22T04:32:17.641Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/release/1.0/modules/configuration/pages/elicitation-for-tools.adoc
  xref: xref:mcp-server:configuration:elicitation-for-tools.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/configuration/elicitation-for-tools.html)

# Elicitation / Confirmation for Tool Calls

> Require user confirmation before the LLM executes specific Couchbase MCP Server tools. 

The `CB_MCP_CONFIRMATION_REQUIRED_TOOLS` environment variable enables user confirmation prompts for tools marked as requiring confirmation. This allows users to double-check the tool call before the LLM executes the actions.

## [](#how-it-works)How It Works

When a tool requires confirmation, the server sends an [elicitation](https://modelcontextprotocol.io/docs/concepts/elicitation) request to the client.

**Clients with elicitation support:**

1. Prompt the user for confirmation.
2. Send the user's response back to the server.

**Clients without elicitation support:** The tool executes **without confirmation**.

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
CB_MCP_CONFIRMATION_REQUIRED_TOOLS="delete_document_by_id, upsert_document_by_id"

# Command line
uvx couchbase-mcp-server --confirmation-required-tools "delete_document_by_id, upsert_document_by_id"
```

### [](#file-path-one-tool-per-line)File Path (One Tool Per Line)

```bash
# Environment variable
CB_MCP_CONFIRMATION_REQUIRED_TOOLS=/path/to/confirmation_required_tools.txt

# Command line
uvx couchbase-mcp-server --confirmation-required-tools /path/to/confirmation_required_tools.txt
```

File format example (`confirmation_required_tools.txt`):

```text
# Write operations
upsert_document_by_id
delete_document_by_id

# Replace operations
replace_document_by_id
```

Lines starting with `#` are treated as comments and ignored.

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
        "CB_MCP_CONFIRMATION_REQUIRED_TOOLS": "upsert_document_by_id,delete_document_by_id"
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
        "CB_MCP_CONFIRMATION_REQUIRED_TOOLS": "/path/to/confirmation_required_tools.txt"
      }
    }
  }
}
```

## [](#important-limitations)Important Limitations

* Setting `CB_MCP_CONFIRMATION_REQUIRED_TOOLS` for a tool that **did not load** has no effect, as the tool is not available. A tool does not load if it's explicitly listed under the `disabled_tools` configuration or if **READ\_ONLY** mode is enabled and the tool is not a **READ\_ONLY** tool.

> [!WARNING]
> The confirmation\_required setting applies explicitly to tools, not to individual actions (such as read, update, or delete operations).
> 
> For example, if confirmation\_required is enabled for the `delete_document_by_id` tool, the MCP server prompts for confirmation only when the MCP client selects that specific tool. No confirmation is requested if the client selects a different tool, such as `run_sql_plus_plus_query` to delete documents.