---
title: Troubleshooting
description: Common issues and fixes for the Couchbase MCP Server, covering
  connections, transport, OAuth, and logging.
pubDate: 2026-08-22T04:32:17.641Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/release/1.0/modules/reference/pages/troubleshooting.adoc
  xref: xref:mcp-server:reference:troubleshooting.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/reference/troubleshooting.html)

# Troubleshooting

> Common issues and fixes for the Couchbase MCP Server, covering connections, transport, OAuth, and logging. 

Common issues that you might run into while using the Couchbase MCP Server and their solutions.

## [](#uvuvx-issues)uv/uvx Issues

If you see errors related to `uv` or `uvx`, check the following:

* **`uvx` not found**: Ensure `uv` is on your system PATH. Install uv following the [official instructions](https://docs.astral.sh/uv/getting-started/installation/). If installed via a package manager, verify it's on your PATH.
* Run `which uv` (macOS/Linux) or `where uv` (Windows) to find the path. You may need to provide the absolute path to `uv`/`uvx` in the `command` field of your MCP client configuration.
* **After updating source code**, run `uv sync` to update [dependencies](https://docs.astral.sh/uv/concepts/projects/sync/#syncing-the-environment). This is only required when running from source after pulling new changes.

## [](#connection-issues)Connection Issues

If you see errors related to connecting to the Couchbase cluster, check the following:

* **Check credentials**: Ensure your connection string, username, password, or certificate paths are correct.
* **Cluster accessibility**: Ensure the cluster is accessible from the machine running the MCP server. If using Couchbase Capella, ensure the machine's IP is [allowed](https://docs.couchbase.com/cloud/clusters/allow-ip-address.html) in the cluster settings — required only when connecting over the public Internet, not on a VPC or a private network to Capella.
* **Bucket permissions**: Check that the database user has proper permissions to access at least one bucket.
* **Connection string format**: Use `couchbases://` for Capella and TLS-enabled clusters, `couchbase://` for unencrypted local connections.
* Use `couchbase://` for unencrypted connections
* **Certificates for TLS**: If you're connecting with TLS enabled on non-Capella clusters, ensure that the certificate is configured correctly via `CB_CA_CERT_PATH`.

## [](#transport-mode-issues)Transport Mode Issues

If the MCP client is unable to communicate with the server, check the following based on your configured transport mode:

* **stdio**: Ensure the MCP client is configured to launch the server as a subprocess. Check the client's server configuration for the correct command and arguments to start the server.
* **HTTP**: Check that the configured port is not in use. Verify that the URL ends with `/mcp`. Also check if the [client configuration](../configuration/streamable-http.md) is set correctly.
* **Port conflicts**: If the default port 8000 is in use, set a different port with `CB_MCP_PORT` or `--port`.
* **Host binding**: By default, the server binds to `127.0.0.1` (localhost only). To allow external connections, set `CB_MCP_HOST=0.0.0.0` or `--host`.

## [](#read-only-mode-issues)Read-Only Mode Issues

If you're trying to perform write operations but they're not working as expected, check the following:

* Check whether `CB_MCP_READ_ONLY_MODE=true` (the default).
* When `CB_MCP_READ_ONLY_MODE=true`, KV write tools are not loaded and SQL++ write queries are blocked. Set `CB_MCP_READ_ONLY_MODE=false` to allow write operations.
* See [Read-Only Mode](../configuration/read-only-mode.md) for the full behavior reference.

## [](#tool-disabling-issues)Tool Disabling Issues

If a tool you expect to be disabled is still executing, check the following:

* Verify tool names are spelled exactly as listed in the [Tools](../learn/tools.md) reference.
* If using a file path for `CB_MCP_DISABLED_TOOLS`, ensure the file exists and is readable by the server process. If using Docker, ensure the file is included in the container and the path is correct.
* Remember that disabling tools alone does not prevent operations - RBAC is the authoritative security control. See [Security](../security/security.md).

## [](#elicitationtools-requiring-confirmation)Elicitation/Tools Requiring Confirmation

If the tool you expect to require confirmation is executing without it, check the following:

* Ensure that the MCP client supports [Elicitation](https://modelcontextprotocol.io/docs/concepts/elicitation). If the client does not support it, the tools will be executed without requiring confirmation.
* Verify tool names are spelled exactly as listed in the [Tools](../learn/tools.md) reference.
* If using a file path for `CB_MCP_CONFIRMATION_REQUIRED_TOOLS`, ensure the file exists and is readable by the server process. If using Docker, ensure the file is included in the container and the path is correct.

## [](#environment-variable-issues)Environment Variable Issues

If you're setting environment variables but they do not seem to be taking effect, check the following:

* **Variables not taking effect**: Ensure variables are set in the `env` block of your MCP client configuration, not as system environment variables (unless your client supports that).
* **CLI vs environment variable conflicts**: Command line arguments take priority over environment variables. If a setting is not behaving as expected, check if it's being overridden by a CLI argument.
* See [Environment Variables](../configuration/environment-variables.md) for the full reference.

## [](#oauth-issues)OAuth Issues

OAuth applies only to the **Streamable HTTP** transport — it's ignored on `stdio`. For the full configuration reference, see [OAuth](../configuration/oauth-overview.md).

### [](#quick-first-pass-diagnosis)Quick first-pass diagnosis

Before digging in, confirm these five things — a surprising number of OAuth issues are resolved here:

| # | Check                                                      | Expected                                                                                                                      |  |
| - | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |  |
| 1 | What transport is the server on?                           | Streamable HTTP (\--transport=http); OAuth is ignored on stdio                                                                |  |
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

Returned by the auth middleware before any tool runs; the log shows `Auth error returned: invalid_token (status=401)`. Decode the token and compare it against your server config.

| Symptom                                       | Meaning                          | Fix                                                                                                                                                                            |  |
| --------------------------------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |  |
| **audience mismatch (got 'X', expected 'Y')** | Token's aud ≠ \--oauth-audience. | Decode a sample token, copy the aud value verbatim, and set \--oauth-audience to match exactly (no trailing-slash differences). Some IdPs emit a different aud per grant type. |  |
| **issuer mismatch (got 'X', expected 'Y')**   | Token's iss ≠ \--oauth-issuer.   | Decode a token, copy iss verbatim, and match it. A trailing-slash difference is the most common cause.                                                                         |  |
| **token expired**                             | The exp claim is in the past.    | Mint a fresh token. If you suspect clock skew, run NTP on the server host — the server applies no leeway by default.                                                           |  |

### [](#403-forbidden-scope-enforcement)403 Forbidden — scope enforcement

Returned after JWT validation succeeds; the message names the required and missing scopes.

| Symptom                                                                     | Meaning                                                                                       | Fix                                                                                                                                     |  |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |  |
| **Tool 'X' requires scope(s) \['couchbase-mcp:read'\]; token is missing …** | The token does not carry the required scope.                                                  | Decode the token and check both the scope (space-separated string) and scp (array) claims. Mint a token that includes the needed scope. |  |
| **SQL++ tool rejected for a write-only token**                              | By design, couchbase-mcp:write permits KV mutations only; SQL++ is classified as a read tool. | If the agent must run SQL++, mint a token carrying **both** couchbase-mcp:read and couchbase-mcp:write.                                 |  |
| **SQL++ INSERT/UPDATE rejected even with both scopes**                      | Read-only mode is on, or the token lacks couchbase-mcp:write.                                 | Set CB\_MCP\_READ\_ONLY\_MODE=false (or \--read-only-mode=false) and confirm the token has both scopes.                                 |  |

### [](#couchbase-layer-errors-after-oauth-succeeds)Couchbase-layer errors (after OAuth succeeds)

These appear after the JWT validated and the scope check passed — they come from the Couchbase SDK or RBAC, not the OAuth layer.

| Symptom                                                             | Meaning                                                                         | Fix                                                                                                                                                                                                  |  |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |  |
| **AuthenticationException(<ec=6, …>) from the SDK**                 | CB\_USERNAME / CB\_PASSWORD do not authenticate against CB\_CONNECTION\_STRING. | Verify the cluster credentials directly — curl -u "$CB\_USERNAME:$CB\_PASSWORD" "<host>:8091/pools" should return 200. Check the connection scheme (couchbase:// vs couchbases://) and reachability. |  |
| **InvalidArgumentException(<message=The username must be a str.>)** | The server started without cluster credentials.                                 | Set CB\_CONNECTION\_STRING, CB\_USERNAME, and CB\_PASSWORD.                                                                                                                                          |  |
| **Reads succeed but writes fail**                                   | The Couchbase user lacks RBAC write permission on the target keyspace.          | RBAC is the ultimate authority — even a valid couchbase-mcp:write token cannot exceed the server's cluster credentials. Grant read/write (or equivalent) on the target bucket/scope.                 |  |

## [](#logging-issues)Logging Issues

The MCP server's own logging is configured at startup through environment variables or CLI flags — see [Logging](../configuration/logging.md) for the full configuration reference. Every start emits one `INFO` **boot summary** line reporting the _resolved_ configuration: the level in effect, which sinks are live, and the exact file paths being written. For example:

```none
2026-06-29T18:08:49+0530 - couchbase - INFO - Logging configured: level=INFO, sinks=stderr,file, log_files={'INFO': 'mcp_server.info.log', 'WARNING': 'mcp_server.warning.log', 'ERROR': 'mcp_server.error.log'}, max_bytes=1048576
```

When logging behaves unexpectedly, **read this line first** — then work through the table below.

| Symptom                                                                                          | Likely cause                                                                                                                                                                                                 | Fix                                                                                                                                                                                                                                                                                                                              |  |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |  |
| **No log files anywhere**                                                                        | The file sink is not enabled — the default is stderr only.                                                                                                                                                   | Set CB\_MCP\_LOG\_SINKS=stderr,file (or \--log-sinks file). Confirm via the boot summary line.                                                                                                                                                                                                                                   |  |
| **Files exist but one stays empty**                                                              | Each level's file is filtered to _exactly_ its level, so an idle server may legitimately have an empty warning/error file.                                                                                   | This is expected. The info file should grow during normal use; if it does not, recheck the level and sinks in the boot line.                                                                                                                                                                                                     |  |
| **A per-level file I expected is missing** (for example, no debug file, or no info/warning file) | That level is below the configured threshold — a file is created only for levels at or above CB\_MCP\_LOG\_LEVEL.                                                                                            | Lower the level to include it: \--log-level=debug produces all four files; at warning, only the warning \+ error files exist.                                                                                                                                                                                                    |  |
| **Server logged "File logging is disabled…" warning**                                            | The file sink was not requested, so support files are not being persisted.                                                                                                                                   | Expected when running stderr\-only. Add file to \--log-sinks if you need persisted logs.                                                                                                                                                                                                                                         |  |
| **I set a log level and nothing changed**                                                        | An invalid level value silently fell back to info.                                                                                                                                                           | Check the boot output for Ignored invalid log level …. Valid values are off/debug/info/warning/error.                                                                                                                                                                                                                            |  |
| **A sink I configured is being ignored**                                                         | An unrecognized \--log-sinks token was dropped.                                                                                                                                                              | Look for Ignored invalid log sink value(s) … at startup. Valid tokens are stderr and file only.                                                                                                                                                                                                                                  |  |
| **I set a rotation size to 0 and got a warning**                                                 | 0 is not a valid rotation size — this applies to CB\_MCP\_LOG\_ROTATION\_MAX\_SIZE\_MB, any per-level override, and the deprecated CB\_MCP\_LOG\_MAX\_BYTES. Both variables route through the same resolver. | The server logs a warning and falls back to the 1 MB default; rotation cannot be disabled this way. To control disk usage, adjust CB\_MCP\_LOG\_RETENTION\_BACKUP\_COUNT and CB\_MCP\_LOG\_ROTATION\_MAX\_SIZE\_MB (globally or per level) instead — see [Per-Level Overrides](../configuration/logging.md#per-level-overrides). |  |
| **Startup warning: CB\_MCP\_LOG\_MAX\_BYTES is deprecated**                                      | You're using the deprecated byte-based size variable.                                                                                                                                                        | Switch to CB\_MCP\_LOG\_ROTATION\_MAX\_SIZE\_MB (megabytes, not bytes). If both are set, the new variable wins and the old one is ignored.                                                                                                                                                                                       |  |
| **ERROR lines I want to suppress keep appearing**                                                | ERROR cannot be raised away — only off silences it.                                                                                                                                                          | Set CB\_MCP\_LOG\_LEVEL=off to silence everything (understanding you lose error visibility too).                                                                                                                                                                                                                                 |  |
| **An ERROR line has no stack trace**                                                             | Stack traces are emitted at DEBUG, by design — ERROR stays a clean one-liner.                                                                                                                                | Re-run at \--log-level=debug to capture the traceback for the same failure.                                                                                                                                                                                                                                                      |  |
| **No logs at all from the server**                                                               | Either \--log-level=off, or you're looking in the wrong place (the client captures stderr).                                                                                                                  | Confirm the boot line appears; for stdio clients, see [Checking Logs](#checking-logs) below for client log locations.                                                                                                                                                                                                            |  |
| **mcp\_server\_config.log.json is missing or looks stale**                                       | The file sink is not enabled, or the server has not restarted since a configuration change.                                                                                                                  | This file captures resolved environment/system info. It's written only when the file sink is active. It's overwritten on every start and never rotates. Restart the server after any configuration change to refresh it.                                                                                                         |  |

## [](#checking-logs)Checking Logs

To configure the MCP server's own logs — log level, console/file output, and file logging for support — see [Logging](../configuration/logging.md).

The MCP client also keeps its own logs. Check the MCP client logs for errors or warnings:

| Client             | Log Location                                                      |  |
| ------------------ | ----------------------------------------------------------------- |  |
| **Claude Desktop** | \~/Library/Logs/Claude (macOS), %APPDATA%\\Claude\\Logs (Windows) |  |
| **Cursor**         | Bottom panel > Output > "Cursor MCP"                              |  |
| **Windsurf**       | Check Windsurf output panel                                       |  |
| **VS Code**        | Command Palette > "MCP: List Servers" > Show Output               |  |
| **JetBrains**      | Help > Show Log in Finder/Explorer > mcp > couchbase              |  |
| **Factory**        | \~/.factory/logs/ (macOS)                                         |  |