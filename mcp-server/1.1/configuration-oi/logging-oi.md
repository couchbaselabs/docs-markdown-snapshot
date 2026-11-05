---
title: Logging
description: Configure log levels, output sinks, and file logging for the
  Couchbase MCP Server.
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase MCP Server
    version: "1.1"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/release/1.1/modules/configuration-oi/pages/logging-oi.adoc
  xref: xref:1.1@mcp-server:configuration-oi:logging-oi.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/1.1/configuration-oi/logging-oi.html)

# Logging

> Configure log levels, output sinks, and file logging for the Couchbase MCP Server. 

The MCP server emits structured logs to help you operate it and to give Couchbase support the diagnostic information needed to triage issues. You can configure the log level and choose one or more output sinks (console, file, or both). Logging applies to all transports — both `stdio` and Streamable HTTP.

## [](#log-levels)Log Levels

| Level   | Description                                                                                           |  |
| ------- | ----------------------------------------------------------------------------------------------------- |  |
| error   | An operation failed, or the server cannot reliably serve the next request.                            |  |
| warning | A threshold was crossed, a fallback was taken, or a deprecated path was used. Nothing is broken yet.  |  |
| info    | Lifecycle events, request envelopes (metadata only), config snapshots, and version info. **Default.** |  |
| debug   | Internal phase transitions and timing details. Verbose. Intended for debugging.                       |  |
| off     | No logs are emitted.                                                                                  |  |

The configured level is a **minimum threshold**: the server records events at that level and every level above it. For example, `warning` records `warning` and `error`.

> [!NOTE]
> If `CB_MCP_LOG_LEVEL` is set to an unrecognized value, the server prints an error message and falls back to `info`.

> [!WARNING]
> Setting `CB_MCP_LOG_LEVEL=off` disables all logging. The server produces no logs, so the diagnostic files required for product support aren't available.

## [](#configuration)Configuration

| Environment Variable                   | Description                                                                                                                                                                                                                                                                                                                                                                                          | Default                                |  |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |  |
| CB\_MCP\_LOG\_LEVEL                    | Minimum level to record. One of off, debug, info, warning, error.                                                                                                                                                                                                                                                                                                                                    | info                                   |  |
| CB\_MCP\_LOG\_SINKS                    | Where the server writes logs. One or more of stderr, file (comma-separated. The server writes to all listed sinks).                                                                                                                                                                                                                                                                                  | stderr                                 |  |
| CB\_MCP\_LOG\_FILE                     | File path used as the template for the per-level log files — the server inserts the level name before the extension (mcp\_server\_operational\_insights.log → mcp\_server\_operational\_insights.info.log, …). Used when you enable the file sink. The directory must already exist.                                                                                                                 | mcp\_server\_operational\_insights.log |  |
| CB\_MCP\_LOG\_MAX\_BYTES               | **Deprecated — use CB\_MCP\_LOG\_ROTATION\_MAX\_SIZE\_MB instead.** Still honored for backward compatibility. If you set both, CB\_MCP\_LOG\_ROTATION\_MAX\_SIZE\_MB takes priority, and a startup warning notes that the server ignores this variable. **Breaking change:** the server no longer accepts 0 — it logs a warning and falls back to the default instead of leaving rotation unbounded. | 1048576 (1 MB)                         |  |
| CB\_MCP\_LOG\_ROTATION\_MAX\_SIZE\_MB  | Maximum size in MB per log file before it rotates. Applies to all levels unless overridden per level — see [Per-Level Overrides](#per-level-overrides). 0 is not a valid value. The server logs a startup warning and falls back to the default instead of leaving rotation unbounded.                                                                                                               | 1 MB                                   |  |
| CB\_MCP\_LOG\_RETENTION\_BACKUP\_COUNT | Number of rotated backup files kept per level, in addition to the live file. Applies to all levels unless overridden per level — see [Per-Level Overrides](#per-level-overrides). Setting 0 keeps only the live file. Size-based rotation still applies.                                                                                                                                             | 1                                      |  |

### [](#per-level-overrides)Per-Level Overrides

Both the rotation size and the backup count can be overridden for an individual log level, taking priority over the global default for that level only:

| Log Level | Max Size Override                              | Backup Count Override                           |  |
| --------- | ---------------------------------------------- | ----------------------------------------------- |  |
| error     | CB\_MCP\_LOG\_ERROR\_ROTATION\_MAX\_SIZE\_MB   | CB\_MCP\_LOG\_ERROR\_RETENTION\_BACKUP\_COUNT   |  |
| warning   | CB\_MCP\_LOG\_WARNING\_ROTATION\_MAX\_SIZE\_MB | CB\_MCP\_LOG\_WARNING\_RETENTION\_BACKUP\_COUNT |  |
| info      | CB\_MCP\_LOG\_INFO\_ROTATION\_MAX\_SIZE\_MB    | CB\_MCP\_LOG\_INFO\_RETENTION\_BACKUP\_COUNT    |  |
| debug     | CB\_MCP\_LOG\_DEBUG\_ROTATION\_MAX\_SIZE\_MB   | CB\_MCP\_LOG\_DEBUG\_RETENTION\_BACKUP\_COUNT   |  |

A per-level override of `0` is invalid: the server logs a startup warning and that level inherits the global rotation size instead — it does not disable rotation.

A per-level backup-count override of `0` is valid: that level keeps only its live file, the same as the global `CB_MCP_LOG_RETENTION_BACKUP_COUNT` setting.

## [](#log-sinks)Log Sinks

The server supports two sinks, and you can enable more than one at a time:

* **`stderr`** (default) — logs are written to the console. MCP clients running the server over `stdio` typically capture this stream into their own log files.
* **`file`** — logs are written to disk.  
`CB_MCP_LOG_FILE` is the file path you provide. It may include a directory, for example, `/var/log/couchbase-mcp/mcp_server_operational_insights.log`, but the directory must already exist.  
It's a template, not the literal name written to disk. A separate file is written per log level, with the level name inserted just before the file extension: `/var/log/couchbase-mcp/mcp_server_operational_insights.log` produces `mcp_server_operational_insights.debug.log`, `mcp_server_operational_insights.info.log`, `mcp_server_operational_insights.warning.log`, and `mcp_server_operational_insights.error.log` in that directory (the error file also captures `CRITICAL`).  
The Operational Insights server uses its own default name, so it and the Operational server can write logs to the same directory without sharing files.  
Each file uses size-based rotation controlled by `CB_MCP_LOG_ROTATION_MAX_SIZE_MB` (default 1 MB) and `CB_MCP_LOG_RETENTION_BACKUP_COUNT` (default 1 backup per level), both of which can be overridden per level — see [Per-Level Overrides](#per-level-overrides). Each level occupies at most about `(backup count + 1) ×` the configured size on disk.

When `CB_MCP_LOG_SINKS` is not set, the server writes to `stderr` only.

## [](#startup-summary)Startup Summary

On every start, the server emits one `INFO` line reporting the **resolved** logging configuration — the level in effect, the active sinks, and the exact per-level file paths. It emits this line after applying defaults and discarding any invalid input. For example:

```none
2026-06-29T18:08:49+0530 - couchbase - INFO - Logging configured: level=INFO, sinks=stderr,file, log_files={'INFO': 'mcp_server_operational_insights.info.log', 'WARNING': 'mcp_server_operational_insights.warning.log', 'ERROR': 'mcp_server_operational_insights.error.log'}, max_bytes=1048576
```

When logging does not behave as expected, check this line first to confirm the level, sinks, and file paths actually in use. See [Troubleshooting → Logging Issues](troubleshooting-oi.md#logging-issues).

## [](#environment-system-info-file)Environment & System Info File

When the `file` sink is enabled, the server also writes the resolved environment and system information to `mcp_server_operational_insights_config.log.json` (derived from the `CB_MCP_LOG_FILE` base path) as pure JSON. The server captures this file at any configured log level, not just `debug`. It overwrites the file on every start, and the file never rotates. This means log rotation can no longer lose this diagnostic information, the way it previously could when the server captured it only in the `debug` log.

## [](#errors-warnings)Errors & Warnings

* **File logging disabled (default).** When the `file` sink is not explicitly enabled, the server emits the warning "File logging is disabled. Log files required for product support are not being generated." This is the default state, since the default sink is `stderr` — a reminder that you aren't saving your logs to disk for future support needs.
* **File sink errors.** When the `file` sink **is** enabled, the server raises an error if:
* the directory for the configured `CB_MCP_LOG_FILE` path **does not exist** — it does not create the directory structure for you.
* the path exists but the server **lacks write permission** for it.

## [](#sensitive-data-in-logs)Sensitive Data in Logs

To keep logs safe to share with support, the server never writes the following to any sink, at any log level:

* Credentials and passwords
* Tokens (bearer, JWT, OAuth) and signing secrets
* Certificates
* Connection strings with embedded credentials
* Document content

> [!WARNING]
> Some data can appear in logs depending on the configured log level:
> 
> * **Query text**: when `CB_MCP_LOG_LEVEL=debug`, the server logs the full SQL++ query.
> * **Document IDs**: the server logs document keys (DocIDs) in certain cases and at certain log levels.
> 
> Take this into account when choosing a log level and before sharing logs, especially if your query text or document keys may contain sensitive information.

## [](#example)Example

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
        "CB_MCP_LOG_LEVEL": "debug",
        "CB_MCP_LOG_SINKS": "stderr,file",
        "CB_MCP_LOG_FILE": "/path/to/folder/mcp-server.log",
        "CB_MCP_LOG_ROTATION_MAX_SIZE_MB": "2",
        "CB_MCP_LOG_RETENTION_BACKUP_COUNT": "1",
        "CB_MCP_LOG_DEBUG_RETENTION_BACKUP_COUNT": "10",
        "CB_MCP_LOG_DEBUG_ROTATION_MAX_SIZE_MB": "5",
        "CB_MCP_LOG_INFO_RETENTION_BACKUP_COUNT": "8",
        "CB_MCP_LOG_INFO_ROTATION_MAX_SIZE_MB": "2"
      }
    }
  }
}
```

## [](#see-also)See Also

* [Troubleshooting](troubleshooting-oi.md)
* [Environment Variables & Command Line Arguments](environment-variables-oi.md)
* [Security](../security-oi/security-oi.md)