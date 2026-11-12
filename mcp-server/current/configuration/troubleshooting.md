---
title: Troubleshooting
description: Common issues and fixes for the Couchbase MCP Server, covering
  connections, transport, OAuth, and logging.
pubDate: 2026-11-12T06:49:41.760Z
meta:
  component:
    title: Couchbase MCP Server Self-Managed
    version: "1.1"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/release/1.1/modules/configuration/pages/troubleshooting.adoc
  xref: xref:mcp-server:configuration:troubleshooting.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/current/configuration/troubleshooting.html)

# Troubleshooting

> Common issues and fixes for the Couchbase MCP Server, covering connections, transport, OAuth, and logging. 

Common issues that you might run into while using the Couchbase MCP Server and their solutions.

## [](#uvuvx-issues)uv/uvx Issues

If you see errors related to `uv` or `uvx`, check the following:

* **`uvx` not found**: Verify that `uv` is on your system PATH. Install uv following the [official instructions](https://docs.astral.sh/uv/getting-started/installation/). If installed via a package manager, verify it's on your PATH.
* Run `which uv` (macOS/Linux) or `where uv` (Windows) to find the path. You may need to provide the absolute path to `uv`/`uvx` in the `command` field of your MCP client configuration.
* **After updating source code**, run `uv sync` to update [dependencies](https://docs.astral.sh/uv/concepts/projects/sync/#syncing-the-environment). This is only required when running from source after pulling new changes.

## [](#connection-issues)Connection Issues

If you see errors related to connecting to the Couchbase cluster, check the following:

* **Check credentials**: Verify that your connection string, username, password, or certificate paths are correct.
* **Cluster accessibility**: Verify that the cluster is accessible from the machine running the MCP server. If using Couchbase Capella, verify that the machine's IP is [allowed](https://docs.couchbase.com/cloud/clusters/allow-ip-address.html) in the cluster settings — required only when connecting over the public Internet, not on a VPC or a private network to Capella.
* **Bucket permissions**: Check that the database user has proper permissions to access at least one bucket.
* **Connection string format**: Use `couchbases://` for Capella and TLS-enabled clusters, `couchbase://` for unencrypted local connections.
* Use `couchbase://` for unencrypted connections
* **Certificates for TLS**: If you're connecting with TLS enabled on non-Capella clusters, verify that you've configured the certificate correctly via `CB_CA_CERT_PATH`.

## [](#transport-mode-issues)Transport Mode Issues

If the MCP client is unable to communicate with the server, check the following based on your configured transport mode:

* **stdio**: Verify that you've configured the MCP client to launch the server as a subprocess. Check the client's server configuration for the correct command and arguments to start the server.
* **HTTP**: Check that the configured port is not in use. Verify that the URL ends with `/mcp`. Also check if the [client configuration](streamable-http.md) is set correctly.
* **Port conflicts**: If the default port 8000 is in use, set a different port with `CB_MCP_PORT` or `--port`.
* **Host binding**: By default, the server binds to `127.0.0.1` (localhost only). To allow external connections, set `CB_MCP_HOST=0.0.0.0` or `--host`.

## [](#cluster-health-tool-issues)Cluster Health Tool Issues

If a cluster health tool returns a permission error or is unavailable, review the following:

* **Permission denied for `get_cluster_health_snapshot`, `get_cluster_tasks`, `get_cluster_query_vitals`, `get_active_queries`, or `get_bucket_config`**: These tools need the `ro_admin` role or a role with more privileges.
* **Permission denied for `get_cluster_system_events` or `delete_active_query`**: These tools need the Full Admin or Cluster Admin role.
* **Permission denied for `get_cluster_health_and_services`**: The active ping needs KV, Query, or Search privileges, or the Cluster Admin role. `get_client_connectivity_report` makes no request to the cluster, so it needs no role beyond the one the connection already uses.
* **Tool missing from tool discovery**: The server does not load ten tools when the connection string points at Capella: `get_cluster_health_snapshot`, `get_cluster_metrics`, `get_cluster_tasks`, `get_cluster_system_events`, `get_cluster_query_vitals`, `get_index_stats`, `get_bucket_config`, `get_active_queries`, `delete_active_query`, and `discover_tool_input_values`. They also need Couchbase Server 7.6 or later. `get_server_configuration_status` reports the withheld tools, and the server lists them in the startup log.
* **REST-based tools fail with mTLS**: Tools that call REST APIs directly use basic authentication. They need `CB_USERNAME` and `CB_PASSWORD`, and they do not work with an mTLS-only configuration.
* **Earlier system events are missing**: `get_cluster_system_events` returns 50 records at first, and up to 500 per request. Use `since_time` to page through earlier events.
* **A bucket shows no configuration**: `get_bucket_config` returns an empty list when the connection lands on a node that never joined a cluster. This can happen when the connection string names a DNS or SRV record that points to a changing set of nodes. An empty list does not prove that the cluster has no buckets.

See [Cluster Setup & Health](../learn/tools.md#cluster-setup-health) for the full tool list.

## [](#vector-search-issues)Vector Search Issues

If the vector search tools fail or return unexpected results, review the following:

* **Embedding provider not configured**: Vector search needs an embedding provider. The vector search tools stay registered, and they return an error when you call them without one. Set `CB_MCP_EMBEDDING_MODEL_PROVIDER` and `CB_MCP_EMBEDDING_MODEL`, or the matching `--embedding-model-provider` and `--embedding-model` flags. See [Environment Variables](environment-variables.md).
* **Provider authentication fails**: Set `CB_MCP_EMBEDDING_MODEL_API_KEY` for `capella`, `openai`, `cohere`, and `voyage`. For `bedrock`, set the AWS key variables or rely on the default AWS credential chain. Bedrock also needs the optional extra, `couchbase-mcp-server[bedrock-embeddings]`.
* **Provider endpoint unreachable**: The `capella` provider requires `CB_MCP_EMBEDDING_MODEL_ENDPOINT`. For a local OpenAI-compatible server such as Ollama or vLLM, use the `openai` provider with `CB_MCP_EMBEDDING_MODEL_ENDPOINT`. Requests to the provider time out after 30 seconds.
* **Wrong model**: Use the same embedding model that produced the vectors in your index.
* **Server version**: `run_vector_query` needs Couchbase Server 8.0 or later and a GSI Composite or Hyperscale vector index. `run_vector_search` needs Couchbase Server 7.6 or later and the Search Service.
* **Data residency**: The server sends the search text of every vector search to the embedding provider. With a hosted provider, the provider is a third party.

## [](#read-only-mode-issues)Read-Only Mode Issues

If you're trying to perform write operations but they're not working as expected, check the following:

* Check whether `CB_MCP_READ_ONLY_MODE=true` (the default).
* When `CB_MCP_READ_ONLY_MODE=true`, KV write tools are not loaded and SQL++ write queries are blocked. Set `CB_MCP_READ_ONLY_MODE=false` to allow write operations.
* See [Read-Only Mode](read-only-mode.md) for the full behavior reference.

## [](#tool-disabling-issues)Tool Disabling Issues

If a tool you expect to be disabled is still executing, check the following:

* Verify that you've spelled tool names exactly as listed in the [Tools](../learn/tools.md) reference.
* If using a file path for `CB_MCP_DISABLED_TOOLS`, verify that the file exists and the server process can read it. If using Docker, verify that the file is included in the container and the path is correct.
* Remember that disabling tools alone does not prevent operations - RBAC is the authoritative security control. See [Security](../security/security.md).

## [](#elicitationtools-requiring-confirmation)Elicitation/Tools Requiring Confirmation

If the tool you expect to require confirmation is executing without it, check the following:

* Verify that the MCP client supports [Elicitation](https://modelcontextprotocol.io/docs/concepts/elicitation). If the client does not support it, the server executes the tools without requiring confirmation.
* Verify that you've spelled tool names exactly as listed in the [Tools](../learn/tools.md) reference.
* **The server fails to start with confirmation-required tools**: Elicitation cannot work in stateless mode, which has no session for the prompt. The server refuses to start when you combine `--confirmation-required-tools` with `--stateless-http`, or with `--workers` set to more than `1`. Turn off stateless mode and use one worker, or remove the confirmation requirement.
* If using a file path for `CB_MCP_CONFIRMATION_REQUIRED_TOOLS`, verify that the file exists and the server process can read it. If using Docker, verify that the file is included in the container and the path is correct.

## [](#environment-variable-issues)Environment Variable Issues

If you're setting environment variables but they do not seem to be taking effect, check the following:

* **Variables not taking effect**: Verify that you've set variables in the `env` block of your MCP client configuration, not as system environment variables (unless your client supports that).
* **CLI vs environment variable conflicts**: Command line arguments take priority over environment variables. If a setting is not behaving as expected, check if it's being overridden by a CLI argument.
* See [Environment Variables](environment-variables.md) for the full reference.

## [](#oauth-issues)OAuth Issues

OAuth applies only to the **Streamable HTTP** transport — it's ignored on `stdio`. For the full configuration reference, see [OAuth](oauth-overview.md).

### [](#quick-first-pass-diagnosis)Quick first-pass diagnosis

Before digging in, confirm these five things — a surprising number of OAuth issues are resolved here:

| # | Check                                                      | Expected                                                                                                                      |  |
| - | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |  |
| 1 | What transport is the server on?                           | Streamable HTTP (\--transport=http). OAuth is ignored on stdio                                                                |  |
| 2 | What does the startup log say about OAuth?                 | One of OAuth enabled …, OAuth disabled …, or OAuth settings provided but transport=…                                          |  |
| 3 | Does the PRM endpoint respond?                             | curl -s <http://<host>:<port>/.well-known/oauth-protected-resource/mcp> returns JSON (only when \--oauth-mcp-base-url is set) |  |
| 4 | Does an unauthenticated tool call return 401?              | A POST to /mcp with no token → 401 Unauthorized                                                                               |  |
| 5 | Decode a sample token and confirm iss, aud, exp, scope/scp | Values match what the server expects                                                                                          |  |

### [](#server-startup)Server startup

| Symptom                                                                                 | Meaning                                                                          | Fix                                                                                                                                                                                                                                                                       |  |
| --------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |  |
| **Incomplete OAuth configuration. To enable OAuth, set all of: …**                      | You set some but not all of the required JWT settings.                           | OAuth is all-or-nothing: set all of CB\_MCP\_OAUTH\_JWT\_ISSUER, CB\_MCP\_OAUTH\_JWT\_AUDIENCE, CB\_MCP\_OAUTH\_JWT\_JWKS\_URI, or none. The server refuses to start on partial config so OAuth never silently fails to enable.                                           |  |
| **…issuer must be a valid http(s) URL …**                                               | You enabled PRM (\--oauth-mcp-base-url) but the issuer is not a URL.             | With PRM, the issuer is published as the authorization-server URL and must be a valid http(s)://…. In token-only mode (no \--oauth-mcp-base-url), any plain string works.                                                                                                 |  |
| **Log: OAuth disabled (no … settings provided)**                                        | The server is running with no OAuth — all requests are accepted unauthenticated. | You passed none of the OAuth settings (a dropped shell line-continuation \\ is a frequent culprit), or set them in a different shell than the one you launched from. Verify with env \| grep CB\_MCP\_OAUTH in the same shell, or hardcode the values on one launch line. |  |
| **Log: OAuth settings provided but transport=stdio; …only honored for streamable-http** | OAuth flags were detected but the server started on stdio.                       | Add \--transport=http. OAuth applies only to Streamable HTTP.                                                                                                                                                                                                             |  |
| **Log: …MCP\_BASE\_URL set without any JWT settings; ignoring**                         | You asked for PRM but configured no token verifier.                              | Set the JWT settings. PRM is meaningless without a verifier — it advertises an authorization server but validates nothing.                                                                                                                                                |  |
| **/.well-known/oauth-protected-resource/mcp returns 404**                               | PRM is not mounted.                                                              | PRM is published only when \--oauth-mcp-base-url is set. Also confirm you include the /mcp suffix (per RFC 9728 the mount path is appended).                                                                                                                              |  |

### [](#401-unauthorized-token-validation)401 Unauthorized — token validation

Returned by the auth middleware before any tool runs. The log shows `Auth error returned: invalid_token (status=401)`. Decode the token and compare it against your server config.

| Symptom                                       | Meaning                          | Fix                                                                                                                                                                            |  |
| --------------------------------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |  |
| **audience mismatch (got 'X', expected 'Y')** | Token's aud ≠ \--oauth-audience. | Decode a sample token, copy the aud value verbatim, and set \--oauth-audience to match exactly (no trailing-slash differences). Some IdPs emit a different aud per grant type. |  |
| **issuer mismatch (got 'X', expected 'Y')**   | Token's iss ≠ \--oauth-issuer.   | Decode a token, copy iss verbatim, and match it. A trailing-slash difference is the most common cause.                                                                         |  |
| **token expired**                             | The exp claim is in the past.    | Mint a fresh token. If you suspect clock skew, run NTP on the server host — the server applies no leeway by default.                                                           |  |

### [](#403-forbidden-scope-enforcement)403 Forbidden — scope enforcement

Returned after JWT validation succeeds. The message names the required and missing scopes.

| Symptom                                                                     | Meaning                                                                                       | Fix                                                                                                                                     |  |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |  |
| **Tool 'X' requires scope(s) \['couchbase-mcp:read'\]; token is missing …** | The token does not carry the required scope.                                                  | Decode the token and check both the scope (space-separated string) and scp (array) claims. Mint a token that includes the needed scope. |  |
| **SQL++ tool rejected for a write-only token**                              | By design, couchbase-mcp:write permits KV mutations only. SQL++ is classified as a read tool. | If the agent must run SQL++, mint a token carrying **both** couchbase-mcp:read and couchbase-mcp:write.                                 |  |
| **SQL++ INSERT/UPDATE rejected even with both scopes**                      | Read-only mode is on, or the token lacks couchbase-mcp:write.                                 | Set CB\_MCP\_READ\_ONLY\_MODE=false (or \--read-only-mode=false) and confirm the token has both scopes.                                 |  |

### [](#couchbase-layer-errors-after-oauth-succeeds)Couchbase-layer errors (after OAuth succeeds)

These appear after the JWT validated and the scope check passed — they come from the Couchbase SDK or RBAC, not the OAuth layer.

| Symptom                                                             | Meaning                                                                         | Fix                                                                                                                                                                                                  |  |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |  |
| **AuthenticationException(<ec=6, …>) from the SDK**                 | CB\_USERNAME / CB\_PASSWORD do not authenticate against CB\_CONNECTION\_STRING. | Verify the cluster credentials directly — curl -u "$CB\_USERNAME:$CB\_PASSWORD" "<host>:8091/pools" should return 200. Check the connection scheme (couchbase:// vs couchbases://) and reachability. |  |
| **InvalidArgumentException(<message=The username must be a str.>)** | The server started without cluster credentials.                                 | Set CB\_CONNECTION\_STRING, CB\_USERNAME, and CB\_PASSWORD.                                                                                                                                          |  |
| **Reads succeed but writes fail**                                   | The Couchbase user lacks RBAC write permission on the target keyspace.          | RBAC is the ultimate authority — even a valid couchbase-mcp:write token cannot exceed the server's cluster credentials. Grant read/write (or equivalent) on the target bucket/scope.                 |  |

## [](#logging-issues)Logging Issues

The MCP server's own logging is configured at startup through environment variables or CLI flags — see [Logging](logging.md) for the full configuration reference. Every start emits one `INFO` **boot summary** line reporting the **resolved** configuration: the level in effect, which sinks are live, and the exact file paths being written. For example:

```none
2026-06-29T18:08:49+0530 - couchbase - INFO - Logging configured: level=INFO, sinks=stderr,file, log_files={'INFO': 'mcp_server.info.log', 'WARNING': 'mcp_server.warning.log', 'ERROR': 'mcp_server.error.log'}, max_bytes=1048576
```

When logging behaves unexpectedly, **read this line first** — then work through the following table.

| Symptom                                                                                          | Likely cause                                                                                                                                                                                                 | Fix                                                                                                                                                                                                                                                                                                            |  |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |  |
| **No log files anywhere**                                                                        | The file sink is not enabled — the default is stderr only.                                                                                                                                                   | Set CB\_MCP\_LOG\_SINKS=stderr,file (or \--log-sinks file). Confirm via the boot summary line.                                                                                                                                                                                                                 |  |
| **Files exist but one stays empty**                                                              | Each level's file is filtered to **exactly** its level, so an idle server may legitimately have an empty warning/error file.                                                                                 | This is expected. The info file should grow during normal use. If it does not, recheck the level and sinks in the boot line.                                                                                                                                                                                   |  |
| **A per-level file I expected is missing** (for example, no debug file, or no info/warning file) | That level is below the configured threshold — a file is created only for levels at or above CB\_MCP\_LOG\_LEVEL.                                                                                            | Lower the level to include it: \--log-level=debug produces all four files. At warning, only the warning \+ error files exist.                                                                                                                                                                                  |  |
| **Server logged "File logging is disabled…" warning**                                            | The file sink was not requested, so support files are not being persisted.                                                                                                                                   | Expected when running stderr\-only. Add file to \--log-sinks if you need persisted logs.                                                                                                                                                                                                                       |  |
| **I set a log level and nothing changed**                                                        | An invalid level value silently fell back to info.                                                                                                                                                           | Check the boot output for Ignored invalid log level …. Valid values are off/debug/info/warning/error.                                                                                                                                                                                                          |  |
| **A sink I configured is being ignored**                                                         | An unrecognized \--log-sinks token was dropped.                                                                                                                                                              | Look for Ignored invalid log sink value(s) … at startup. Valid tokens are stderr and file only.                                                                                                                                                                                                                |  |
| **I set a rotation size to 0 and got a warning**                                                 | 0 is not a valid rotation size — this applies to CB\_MCP\_LOG\_ROTATION\_MAX\_SIZE\_MB, any per-level override, and the deprecated CB\_MCP\_LOG\_MAX\_BYTES. Both variables route through the same resolver. | The server logs a warning and falls back to the 1 MB default. You can't disable rotation this way. To control disk usage, adjust CB\_MCP\_LOG\_RETENTION\_BACKUP\_COUNT and CB\_MCP\_LOG\_ROTATION\_MAX\_SIZE\_MB (globally or per level) instead — see [Per-Level Overrides](logging.md#per-level-overrides). |  |
| **Startup warning: CB\_MCP\_LOG\_MAX\_BYTES is deprecated**                                      | You're using the deprecated byte-based size variable.                                                                                                                                                        | Switch to CB\_MCP\_LOG\_ROTATION\_MAX\_SIZE\_MB (megabytes, not bytes). If both are set, the new variable wins and the old one is ignored.                                                                                                                                                                     |  |
| **ERROR lines I want to suppress keep appearing**                                                | ERROR cannot be raised away — only off silences it.                                                                                                                                                          | Set CB\_MCP\_LOG\_LEVEL=off to silence everything (understanding you lose error visibility too).                                                                                                                                                                                                               |  |
| **An ERROR line has no stack trace**                                                             | Stack traces are emitted at DEBUG, by design — ERROR stays a clean one-liner.                                                                                                                                | Re-run at \--log-level=debug to capture the traceback for the same failure.                                                                                                                                                                                                                                    |  |
| **No logs at all from the server**                                                               | Either \--log-level=off, or you're looking in the wrong place (the client captures stderr).                                                                                                                  | Confirm the boot line appears. For stdio clients, see the [Checking Logs](#checking-logs) section later in this page for client log locations.                                                                                                                                                                 |  |
| **mcp\_server\_config.log.json is missing or looks stale**                                       | The file sink is not enabled, or the server has not restarted since a configuration change.                                                                                                                  | This file captures resolved environment/system info. It's written only when the file sink is active. It's overwritten on every start and never rotates. Restart the server after any configuration change to refresh it.                                                                                       |  |

## [](#checking-logs)Checking Logs

To configure the MCP server's own logs — log level, console/file output, and file logging for support — see [Logging](logging.md).

The MCP client also keeps its own logs. Check the MCP client logs for errors or warnings:

| Client             | Log Location                                                      |  |
| ------------------ | ----------------------------------------------------------------- |  |
| **Claude Desktop** | \~/Library/Logs/Claude (macOS), %APPDATA%\\Claude\\Logs (Windows) |  |
| **Cursor**         | Bottom panel > Output > "Cursor MCP"                              |  |
| **Windsurf**       | Check Windsurf output panel                                       |  |
| **VS Code**        | Command Palette > "MCP: List Servers" > Show Output               |  |
| **JetBrains**      | Help > Show Log in Finder/Explorer > mcp > couchbase              |  |
| **Factory**        | \~/.factory/logs/ (macOS)                                         |  |

## [](#see-also)See Also

* [Tools](../learn/tools.md)
* [Environment Variables & Command Line Arguments](environment-variables.md)
* [Logging](logging.md)
* [Audit Logging](audit-logging.md)
* [Security](../security/security.md)