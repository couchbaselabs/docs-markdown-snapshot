---
title: Read-Only Mode
description: Control write access to your Couchbase cluster from the MCP server;
  enabled by default for safety.
pubDate: 2026-08-22T04:32:17.641Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/release/1.0/modules/configuration/pages/read-only-mode.adoc
  xref: xref:mcp-server:configuration:read-only-mode.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/configuration/read-only-mode.html)

# Read-Only Mode

> Control write access to your Couchbase cluster from the MCP server; enabled by default for safety. 

The MCP server provides configuration options for controlling write operations, ensuring safe interaction between LLMs and your database. Use this mode to start in a safe default that prevents data mutations by not loading write-capable tools; see the [Security](../security/security.md) page for best practices. This mode is enabled by default.

## [](#tools-affected-by-read-only-mode)Tools Affected by Read-Only Mode

The following tools are disabled when `CB_MCP_READ_ONLY_MODE` is `true` (the default):

| Tool                        | Description                            |  |
| --------------------------- | -------------------------------------- |  |
| upsert\_document\_by\_id    | Insert or update a document by ID      |  |
| insert\_document\_by\_id    | Insert a new document by ID            |  |
| replace\_document\_by\_id   | Replace an existing document by ID     |  |
| delete\_document\_by\_id    | Delete a document by ID                |  |
| mutate\_subdocument         | Mutate one or more paths in a document |  |
| run\_sql\_plus\_plus\_query | Run SQL++ queries that modify data     |  |
| create\_index               | Create a non-vector GSI index          |  |
| build\_index                | Build a deferred index                 |  |
| drop\_index                 | Drop an existing index                 |  |
| create\_scope               | Create a new scope                     |  |
| create\_collection          | Create a new collection                |  |
| delete\_scope               | Delete an existing scope               |  |
| delete\_collection          | Delete an existing collection          |  |

## [](#read-only-mode-recommended)Read-Only Mode (Recommended)

This is the primary server-side safety switch (`CB_MCP_READ_ONLY_MODE`) — defense-in-depth on top of database RBAC, which remains the authoritative boundary:

* **When `true` (default)**: All write operations are disabled. SQL++ queries that modify data are also blocked.
* **When `false`**: All tools are loaded and available. SQL++ write queries are allowed.

## [](#mode-behavior)Mode Behavior

| READ\_ONLY\_MODE | Result                                                  |  |
| ---------------- | ------------------------------------------------------- |  |
| true (default)   | Read-only KV and Query operations. All writes disabled. |  |
| false            | All KV and Query operations allowed.                    |  |

> [!IMPORTANT]
> `CB_MCP_READ_ONLY_MODE=true` is the recommended safe default to prevent inadvertent data modifications by LLMs.

## [](#configuration-example)Configuration Example

To enable write operations:

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
        "CB_MCP_READ_ONLY_MODE": "false"
      }
    }
  }
}
```

## [](#security-guidelines)Security Guidelines

* Read-only mode is a **defense-in-depth feature**, not the primary security boundary.
* The authoritative control is **Couchbase RBAC**: You should configure database user permissions so that the credentials used by the MCP server do not have data modification privileges if you want strong guarantees. See [RBAC for Couchbase Server](https://docs.couchbase.com/server/current/manage/manage-security/manage-users-and-roles.html) or [RBAC for Capella](https://docs.couchbase.com/cloud/clusters/manage-database-users.html).