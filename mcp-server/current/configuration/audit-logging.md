---
title: Audit Logging
description: Record tool calls, authorization denials, and guardrail blocks in an audit log.
pubDate: 2026-11-12T06:49:41.760Z
meta:
  component:
    title: Couchbase MCP Server Self-Managed
    version: "1.1"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/release/1.1/modules/configuration/pages/audit-logging.adoc
  xref: xref:mcp-server:configuration:audit-logging.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/current/configuration/audit-logging.html)

# Audit Logging

> Record tool calls, authorization denials, and guardrail blocks in an audit log. 

The MCP server writes audit records separately from the `CB_MCP_LOG_*` operational logs. Audit logging is off by default. It applies to both `stdio` and Streamable HTTP transport modes. Authorization events occur only on Streamable HTTP.

## [](#enabling-audit-logging)Enabling Audit Logging

Set `CB_MCP_AUDIT_LOG_ENABLED=true`. By default, the server writes audit records to `stderr`, which is the `console` sink. Under `stdio`, the console sink never writes to `stdout`, because `stdout` carries the protocol messages.

To keep the records, add the `file` sink and set a path:

```bash
CB_MCP_AUDIT_LOG_ENABLED=true
CB_MCP_AUDIT_LOG_SINKS=console,file
CB_MCP_AUDIT_LOG_FILE_PATH=/var/log/couchbase-mcp/audit.log
```

If you list the `file` sink without a path, the server still starts. It drops the file sink and records an error.

## [](#configuration)Configuration

| Environment Variable                         | CLI Argument                       | Default | Description                                                                                                                                |
| -------------------------------------------- | ---------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| CB\_MCP\_AUDIT\_LOG\_ENABLED                 | \--audit-log-enabled               | false   | Turns audit logging on.                                                                                                                    |
| CB\_MCP\_AUDIT\_LOG\_SINKS                   | \--audit-log-sinks                 | console | Comma-separated list of sinks. Allowed values are console and file.                                                                        |
| CB\_MCP\_AUDIT\_LOG\_FILE\_PATH              | \--audit-log-file-path             | None    | Path of the audit log file. Needed when file is one of the sinks. See [Retention and Per-Process Files](#retention-and-per-process-files). |
| CB\_MCP\_AUDIT\_LOG\_ROTATION\_MAX\_SIZE\_MB | \--audit-log-rotation-max-size-mb  | 10      | Size in MB that the live audit file can reach before the server rotates it. 0 turns size-based rotation off.                               |
| CB\_MCP\_AUDIT\_LOG\_ROTATION\_INTERVAL      | \--audit-log-rotation-interval     | 1d      | Age that the live audit file can reach before the server rotates it. 0 turns time-based rotation off. See [Log Rotation](#log-rotation).   |
| CB\_MCP\_AUDIT\_LOG\_RETENTION\_MAX\_BACKUPS | \--audit-log-retention-max-backups | 10      | Number of rotated backups to keep for each audit file, not counting the live file. 0 keeps none.                                           |
| CB\_MCP\_AUDIT\_LOG\_TOOL\_ARGS              | \--audit-log-tool-args             | false   | Includes tool arguments in audit records. See [Capturing Tool Arguments](#capturing-tool-arguments).                                       |
| CB\_MCP\_AUDIT\_LOG\_DISABLED\_EVENTS        | \--audit-log-disabled-events       | None    | Numeric event IDs to turn off, as a comma-separated list or a path to a file. See [Audit Events](#audit-events).                           |

## [](#log-rotation)Log Rotation

The server supports both time-based and size-based rotation of the audit file. The two settings are independent. The server rotates the file when either one falls due first.

Time-based rotation uses the format `<value><unit>`. The unit is `d` for 24 hours or `w` for 7 days. Examples are `1d`, `30d`, `1w`, and `8w`.

The server compresses rotated files with gzip and names them with the UTC rotation time. It keeps the number of backups that `CB_MCP_AUDIT_LOG_RETENTION_MAX_BACKUPS` sets. With `0`, the server keeps no backups and truncates the live file at each rotation.

Setting both the size and the interval to `0` gives a single file with no limit. If a value is unusable, the server falls back to the default and logs a warning at startup.

### [](#retention-and-per-process-files)Retention and Per-Process Files

Each server process writes its own audit file. The server inserts the hostname and process ID before the extension, so `audit.log` becomes `audit.myhost.1234.log`.

Under `stdio`, this is required. Each client starts its own server process, so several processes often run at once. Without per-process names, they would write to one file and interleave records.

Per-process files have consequences for retention that you need to plan for:

* **Retention applies to one file, not to the directory**: `CB_MCP_AUDIT_LOG_RETENTION_MAX_BACKUPS` bounds the rotated copies of the file that the running process owns. A process never prunes the files of another process. Nothing removes the files of processes that have exited.
* **Rotation happens only while a process runs**: A `stdio` session that lasts an hour never reaches a one-day interval, so the server never rotates its file. The file stays on disk as a single file after the client disconnects.
* **Files accumulate with the number of server starts**: Under `stdio`, this is normal use, not an error case. Every client session and every restart leaves a file behind. Total disk use grows over time, even when each file stays within its configured size.

To keep audit storage bounded:

* Size the volume for the number of sessions you expect, not for one file.
* Remove old `audit.**.log**` files with a scheduled job on the host, after you collect the records you need to keep.
* Forward records off the host with a log shipper if you need long retention. This also protects the records against local file deletion.
* Prefer the Streamable HTTP transport, where one long-lived process serves all clients. Rotation and retention then behave as configured, because the process lives long enough to apply them.

> [!CAUTION]
> Do not delete an audit file that a running server still has open. Collect or forward the records before you delete anything. Audit retention can be a compliance requirement, and you cannot recover a deleted file.

#### [](#reused-process-ids)Reused Process IDs

An operating system reuses process IDs, so a new server process can find an audit file that an earlier process with the same ID created. The server handles this. When it opens an existing file, it anchors the rotation interval to the last modification time of that file, not to the current time. The file from the earlier process is already past the rotation interval, so the server rotates it to a backup on the first record it writes. The server preserves the earlier records in the backup, and the new process starts a clean file. Two processes never append to the same file.

## [](#capturing-tool-arguments)Capturing Tool Arguments

By default, audit records exclude the following:

* Tool arguments
* Query text
* Document bodies
* Results
* Raw tokens

Set `CB_MCP_AUDIT_LOG_TOOL_ARGS=true` to add the tool arguments to each record. The server has no redaction. It writes argument values verbatim, including SQL++ text and the full document bodies that document-write tools receive.

> [!WARNING]
> Tool arguments can contain sensitive information. Keep audit files apart from the operational log files, and limit who can read them. Do not send audit records to the same destination as your operational logs.

## [](#audit-events)Audit Events

Each event has a numeric ID. The server records all events by default. You can turn off some of the events with `CB_MCP_AUDIT_LOG_DISABLED_EVENTS`. The tables show which ones. The server ignores an unknown ID and logs a warning.

For example, `CB_MCP_AUDIT_LOG_DISABLED_EVENTS=61490,61492` turns off the document read and index read events. The server always records write events, security events, and the `query` and `search` events. It refuses a request to turn them off and logs a warning.

### [](#event-id-blocks)Event ID Blocks

The IDs fall into three blocks. The Couchbase Server tools and the Operational Insights tools each have their own block for tool calls.

| Block Starts At | Covers                                                                                                                                        |
| --------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| 57344           | Events that both servers share: server lifecycle, sessions, authorization, and guardrails.                                                    |
| 61440           | Tool calls of the Couchbase Server tools. This page lists them.                                                                               |
| 65536           | Tool calls of the Operational Insights tools. See [Operational Insights Audit Logging](../configuration-oi/audit-logging-oi.md#audit-events). |

Some event names appear in more than one block. For example, `schema read` is 61489 for the Couchbase Server tools and 65585 for the Operational Insights tools. Write alert rules against the numeric ID, not the name.

Within a tool-call block, the ID range shows the kind of event:

| Offset From the Block Start | Kind of Event                   | Can Be Turned Off |
| --------------------------- | ------------------------------- | ----------------- |
| +48 to +63                  | Read                            | Yes               |
| +64 to +79                  | Single event (query and search) | No                |
| +80 to +95                  | Write                           | No                |

An event outside the read range cannot be turned off, but that no longer means the event is a write. The tables on this page show which events you can turn off.

### [](#server-session-authorization-and-guardrail-events)Server, Session, Authorization, and Guardrail Events

| ID    | Event                          | Description                                                                                                      | Can Be Turned Off |
| ----- | ------------------------------ | ---------------------------------------------------------------------------------------------------------------- | ----------------- |
| 57344 | server started                 | The MCP server started.                                                                                          | No                |
| 57345 | server stopped                 | The MCP server stopped cleanly.                                                                                  | No                |
| 57346 | server configuration           | The resolved configuration at startup, including read-only mode and the tools the server withheld or turned off. | No                |
| 57360 | session initialized            | An MCP client finished the initialize handshake.                                                                 | Yes               |
| 57376 | token rejected                 | The server rejected a bearer token during verification.                                                          | No                |
| 57377 | scope check denied             | The token did not carry a scope that the tool requires.                                                          | No                |
| 57488 | write blocked (read-only mode) | The server refused a SQL++ statement that modifies data or structure, because read-only mode is on.              | No                |
| 57490 | confirmation declined          | The user rejected the confirmation request for a tool that requires confirmation.                                | No                |
| 57491 | confirmation skipped           | A tool that requires confirmation ran without it, because the client does not support elicitation.               | No                |

A missing `server stopped` record means the server did not stop cleanly.

### [](#tool-call-events)Tool Call Events

Each tool call produces one record. Most categories have a read event and a write event, and the server classifies each call as one or the other. The `query` and `search` categories have one event each. See [Single-Event Categories](#single-event-categories).

| ID    | Event             | Description                                                                                               | Tools                                                                                                                                                                                                                                                                                    | Can Be Turned Off |
| ----- | ----------------- | --------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| 61488 | cluster read      | Reads cluster information, health, or statistics.                                                         | test\_cluster\_connection, get\_cluster\_health\_and\_services, get\_client\_connectivity\_report, get\_cluster\_metrics, get\_cluster\_tasks, get\_cluster\_health\_snapshot, get\_cluster\_system\_events, get\_cluster\_query\_vitals, get\_index\_stats, get\_bucket\_config         | Yes               |
| 61489 | schema read       | Reads buckets, scopes, collections, or schemas.                                                           | get\_buckets\_in\_cluster, get\_scopes\_in\_bucket, get\_collections\_in\_scope, get\_scopes\_and\_collections\_in\_bucket, get\_schema\_for\_collection                                                                                                                                 | Yes               |
| 61490 | document read     | Reads a document.                                                                                         | get\_document\_by\_id, lookup\_subdocument                                                                                                                                                                                                                                               | Yes               |
| 61492 | index read        | Reads index definitions or recommendations.                                                               | list\_indexes, get\_index\_advisor\_recommendations                                                                                                                                                                                                                                      | Yes               |
| 61493 | performance read  | Reads query performance data or in-flight requests.                                                       | get\_longest\_running\_queries, get\_most\_frequent\_queries, get\_queries\_with\_largest\_response\_sizes, get\_queries\_with\_large\_result\_count, get\_queries\_using\_primary\_index, get\_queries\_not\_using\_covering\_index, get\_queries\_not\_selective, get\_active\_queries | Yes               |
| 61495 | config read       | Reads the server configuration or reference data.                                                         | get\_server\_configuration\_status, discover\_tool\_input\_values                                                                                                                                                                                                                        | Yes               |
| 61507 | query             | Runs or explains a SQL++ query, or runs a vector query. One event for every call, whatever the call does. | run\_sql\_plus\_plus\_query, explain\_sql\_plus\_plus\_query, run\_vector\_query                                                                                                                                                                                                         | No                |
| 61510 | search            | Queries or manages Search indexes. One event for every call, whatever the call does.                      | run\_search, run\_vector\_search, list\_search\_indexes, get\_search\_index\_definition, upsert\_search\_index, drop\_search\_index                                                                                                                                                      | No                |
| 61520 | cluster write     | Changes the cluster.                                                                                      | No tool today                                                                                                                                                                                                                                                                            | No                |
| 61521 | schema write      | Creates or deletes scopes or collections.                                                                 | create\_scope, create\_collection, delete\_scope, delete\_collection                                                                                                                                                                                                                     | No                |
| 61522 | document write    | Creates, changes, or deletes a document.                                                                  | upsert\_document\_by\_id, insert\_document\_by\_id, replace\_document\_by\_id, delete\_document\_by\_id, mutate\_subdocument                                                                                                                                                             | No                |
| 61524 | index write       | Creates, builds, or drops an index.                                                                       | create\_index, create\_query\_index, build\_index, drop\_index                                                                                                                                                                                                                           | No                |
| 61525 | performance write | Cancels an in-flight query request.                                                                       | delete\_active\_query                                                                                                                                                                                                                                                                    | No                |
| 61527 | config write      | Changes the server configuration.                                                                         | No tool today                                                                                                                                                                                                                                                                            | No                |

The server records a tool that has no classification as a write. That record carries `unclassified: true`, and you cannot turn it off.

### [](#single-event-categories)Single-Event Categories

The `query` and `search` categories are each recorded as one event. The server does not record whether the operation read or wrote.

For queries, turn on `CB_MCP_AUDIT_LOG_TOOL_ARGS` to capture the statement text, after you read [Capturing Tool Arguments](#capturing-tool-arguments).

For search, a search query and a change to a Search index share one event ID. The `tool_name` field on each record identifies the tool that ran.

You cannot turn off either event. A single event covers the writes of its category as well as the reads, so turning it off would remove the record of a statement that modified data, or of a Search index being deleted.

Read-only mode is not affected. The server enforces it separately, and it does not depend on this classification.

## [](#record-format)Record Format

Records use JSON Lines format, with one record per line. The field names match Couchbase Server and Sync Gateway audit logs. The server omits any field that has no value.

| Field             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id                | Numeric event ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| name              | Event name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| description       | Event description.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| timestamp         | UTC time with millisecond precision, such as 2026-10-23T09:15:42.118Z.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| real\_userid      | The caller, as domain and user. The domain shows how the caller connected. oauth means Streamable HTTP with OAuth, and the user is the subject of the bearer token. anonymous means Streamable HTTP without OAuth, and the server cannot identify the caller. local means stdio, and the user is the operating system user that owns the process. In containers, that user is often root, so it does not identify a person. The server omits the field for events that no caller caused, such as server started. |
| server            | The MCP server version and host.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| cid               | A server-generated UUID4 that identifies one MCP request. Every record produced while handling that request shares the same cid, so you can join them. It's the only correlation value, and records contain no session identifier.                                                                                                                                                                                                                                                                               |
| outcome           | success, denied, blocked, or error.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| reason            | Present when the outcome is not success. The confirmation skipped record also carries a reason, although its outcome is success. Values are execution\_error and invalid\_arguments for tool calls, token\_invalid for a rejected token, missing\_scope when the token lacks a required scope, read\_only\_mode for a blocked write, confirmation\_declined for a declined confirmation, and confirmation\_unsupported for a skipped confirmation.                                                               |
| tool\_name        | The tool that the request called. Present on tool call and guardrail records.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| required\_scope   | The OAuth scope that the tool requires, read or write. Omitted on query and search records, because one event has no per-call class to derive it from. It's still present on refusal records.                                                                                                                                                                                                                                                                                                                    |
| ks                | The keyspace that the call targeted.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| cb\_userid        | The Couchbase user that the server connects as.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| client\_id        | The OAuth client ID from the token. Present on scope check denied records.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| scopes            | The scopes in the token of the caller. Present on scope check denied records.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| missing\_scopes   | The scopes that the tool needs and the token lacks. Present on refusals for a missing scope.                                                                                                                                                                                                                                                                                                                                                                                                                     |
| confirmation      | The result of the confirmation request, for a tool that requires confirmation.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| protocol\_version | The MCP protocol version that the client and server agreed on. Present on session initialized records.                                                                                                                                                                                                                                                                                                                                                                                                           |
| client\_name      | The name of the MCP client, such as Claude Desktop or Cursor. Present on session initialized records.                                                                                                                                                                                                                                                                                                                                                                                                            |
| client\_version   | The version of the MCP client. Present on session initialized records.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| args              | The tool arguments. Present only when CB\_MCP\_AUDIT\_LOG\_TOOL\_ARGS is true.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| unclassified      | true for a tool that has no classification. The server records the call as a write.                                                                                                                                                                                                                                                                                                                                                                                                                              |

### [](#example-records)Example Records

A document read that failed, from a `stdio` client:

```json
{
  "id": 61490,
  "name": "document read",
  "description": "A document read operation was requested through a tool",
  "timestamp": "2026-10-12T08:07:21.603Z",
  "real_userid": { "domain": "local", "user": "root" },
  "server": { "version": "1.0.2rc4", "host": "vm" },
  "cid": "ffbf8f99-a96e-4b65-8dfb-1c4e720ed5b7",
  "outcome": "error",
  "reason": "execution_error",
  "tool_name": "get_document_by_id",
  "required_scope": "read",
  "ks": "travel-sample.inventory.airline",
  "cb_userid": "test-user"
}
```

A write that the server denied because the token has only the read scope, from a Streamable HTTP client:

```json
{
  "id": 57377,
  "name": "scope check denied",
  "description": "A required OAuth scope was not granted by the presented token",
  "timestamp": "2026-08-05T09:15:02.101Z",
  "real_userid": { "domain": "oauth", "user": "agent-svc-7" },
  "server": { "version": "1.1.0", "host": "vm" },
  "cid": "req-7c19",
  "outcome": "denied",
  "client_id": "agent-svc-7",
  "scopes": ["couchbase-mcp:read"],
  "tool_name": "upsert_document_by_id",
  "required_scope": "write",
  "reason": "missing_scope"
}
```

## [](#reliability)Reliability

Audit logging never interferes with serving requests. If the server cannot write a record, the request still proceeds. The server counts the records it wrote, dropped, and failed to write, and reports the counts through the `get_server_configuration_status` tool.

Each sink writes through a bounded in-memory queue of 10,000 records and a background writer thread. When the queue is full, the server drops records and counts them. On shutdown, the server flushes the queue within a bounded wait. The server drops the records that are still queued when that wait expires, and counts them.

The `file` sink writes to the local filesystem only. The server has no syslog output and does not forward records to the Couchbase Server audit daemon.

## [](#see-also)See Also

* [Logging](logging.md)
* [Security](../security/security.md)
* [Operational Insights Audit Logging](../configuration-oi/audit-logging-oi.md)