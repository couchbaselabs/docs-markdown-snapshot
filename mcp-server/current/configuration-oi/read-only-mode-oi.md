---
title: Read-Only Mode
description: Control write access to your Operational Insights cluster from the
  MCP server. Enabled by default for safety.
pubDate: 2026-11-12T06:49:41.760Z
meta:
  component:
    title: Couchbase MCP Server Self-Managed
    version: "1.1"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/release/1.1/modules/configuration-oi/pages/read-only-mode-oi.adoc
  xref: xref:mcp-server:configuration-oi:read-only-mode-oi.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/current/configuration-oi/read-only-mode-oi.html)

# Read-Only Mode

> Control write access to your Operational Insights cluster from the MCP server. Enabled by default for safety. 

The MCP server provides configuration options for controlling write operations, ensuring safe interaction between LLMs and your data. Use this mode to start in a safe default that prevents data mutations by not loading write-capable tools. See the [Security](../security-oi/security-oi.md) page for best practices. This mode is enabled by default.

## [](#tools-affected-by-read-only-mode)Tools Affected by Read-Only Mode

Read-only mode turns off the following tool when `CB_MCP_READ_ONLY_MODE` is `true` (the default):

| Tool                                 | Description                              |  |
| ------------------------------------ | ---------------------------------------- |  |
| operational\_insights\_create\_index | Create a secondary index on a collection |  |

`operational_insights_cancel_async_query` stays available in read-only mode. It stops a query that you started, and it does not change any data.

## [](#read-only-mode-recommended)Read-Only Mode (Recommended)

This is the primary server-side safety switch (`CB_MCP_READ_ONLY_MODE`) — defense-in-depth on top of database RBAC, which remains the authoritative boundary:

* **When `true` (default)**: `operational_insights_create_index` is not loaded. All the other tools stay available, including `operational_insights_cancel_async_query`. SQL++ queries run with the server-side `readonly` option, so the Operational Insights cluster itself rejects data and structure modifications. `COPY …​ TO` (export) statements are also blocked client-side, including an export that you request with the `copy_to_*` arguments.
* **When `false`**: All tools are loaded and available, and SQL++ queries run without the `readonly` option.

## [](#mode-behavior)Mode Behavior

| READ\_ONLY\_MODE | Result                                                                                                            |  |
| ---------------- | ----------------------------------------------------------------------------------------------------------------- |  |
| true (default)   | Read-only query and index operations. Index creation is turned off, and async query cancellation stays available. |  |
| false            | All query and index operations allowed.                                                                           |  |

> [!IMPORTANT]
> `CB_MCP_READ_ONLY_MODE=true` is the recommended safe default to prevent inadvertent data modifications by LLMs.

## [](#configuration-example)Configuration Example

To enable write operations:

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
        "CB_MCP_READ_ONLY_MODE": "false"
      }
    }
  }
}
```

## [](#security-guidelines)Security Guidelines

* Read-only mode is a **defense-in-depth feature**, not the primary security boundary.
* The authoritative control is **Couchbase RBAC**: You should configure database user permissions so that the credentials used by the MCP server do not have data modification privileges if you want strong guarantees. See [RBAC for Couchbase Server](https://docs.couchbase.com/server/current/manage/manage-security/manage-users-and-roles.html).

## [](#see-also)See Also

* [Tools](../learn-oi/tools-oi.md)
* [Disabling Tools](disabling-tools-oi.md)
* [Elicitation / Confirmation for Tool Calls](elicitation-for-tools-oi.md)
* [Troubleshooting Read-Only Mode](troubleshooting-oi.md#read-only-mode-issues)
* [Security](../security-oi/security-oi.md)