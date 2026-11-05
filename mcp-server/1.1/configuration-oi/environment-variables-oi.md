---
title: Environment Variables &amp; Command Line Arguments
description: Reference for all environment variables and CLI arguments used to
  configure the Couchbase MCP Server, including authentication examples.
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase MCP Server
    version: "1.1"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/release/1.1/modules/configuration-oi/pages/environment-variables-oi.adoc
  xref: xref:1.1@mcp-server:configuration-oi:environment-variables-oi.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/1.1/configuration-oi/environment-variables-oi.html)

# Environment Variables &amp; Command Line Arguments

> Reference for all environment variables and CLI arguments used to configure the Couchbase MCP Server, including authentication examples. 

You can configure the MCP server using environment variables or command line arguments. If you specify both, command line arguments take priority over environment variables.

## [](#configuration-reference)Configuration Reference

| Environment Variable                                          | CLI Argument                                       | Description                                                                                                                                                                                                                                                                                                                                                    | Default                                         |  |
| ------------------------------------------------------------- | -------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |  |
| CB\_OPERATIONAL\_INSIGHTS\_CONNECTION\_STRING                 | \--connection-string                               | HTTP(S) URL of the Operational Insights cluster, for example <http://localhost:8095> or <https://<host>:18095>. This is not a couchbase:// connection string. See [Configuring Connection String](../get-started-oi/quickstart-oi.md#step-2-set-your-connection-string).                                                                                       | **Required**                                    |  |
| CB\_OPERATIONAL\_INSIGHTS\_USERNAME                           | \--username                                        | Username for basic authentication. See [Configuring Authentication](#configuring-authentication).                                                                                                                                                                                                                                                              | **Required (or mTLS)**                          |  |
| CB\_OPERATIONAL\_INSIGHTS\_PASSWORD                           | \--password                                        | Password for basic authentication. See [Configuring Authentication](#configuring-authentication).                                                                                                                                                                                                                                                              | **Required (or mTLS)**                          |  |
| CB\_OPERATIONAL\_INSIGHTS\_CLIENT\_CERT\_PATH                 | \--client-cert-path                                | Path to the client certificate for mTLS. Use either a PEM certificate (paired with the client key path) or a PKCS#12 bundle (.p12 or .pfx, with the client key path left unset). Requires an https:// connection string. When set, the server ignores the username and password. See [Configuring Authentication](#configuring-authentication).                | **Required if using mTLS**                      |  |
| CB\_OPERATIONAL\_INSIGHTS\_CLIENT\_KEY\_PATH                  | \--client-key-path                                 | Path to the client certificate's private key file (PEM). Leave unset when the client certificate path is a PKCS#12 bundle that already contains the key. See [Configuring Authentication](#configuring-authentication).                                                                                                                                        | **Required for a PEM client certificate**       |  |
| CB\_OPERATIONAL\_INSIGHTS\_CLIENT\_CERT\_PASSWORD             | \--client-cert-password                            | Decryption password for the client key or PKCS#12 bundle, if it's encrypted. Omit if the file is unencrypted.                                                                                                                                                                                                                                                  | None                                            |  |
| CB\_OPERATIONAL\_INSIGHTS\_CA\_CERT\_PATH                     | \--ca-cert-path                                    | Path to the server trust store (CA certificate) file. The server uses it to verify the server certificate during authentication, for example with self-signed or untrusted certificates.                                                                                                                                                                       |                                                 |  |
| CB\_MCP\_READ\_ONLY\_MODE                                     | \--read-only-mode                                  | Prevent all data modifications. See [Read-Only Mode](read-only-mode-oi.md) for details.                                                                                                                                                                                                                                                                        | true                                            |  |
| CB\_MCP\_TRANSPORT                                            | \--transport                                       | Transport mode selection: stdio (client launches server as subprocess), http ([Streamable HTTP](streamable-http-oi.md) \- multiple clients, serves at /mcp)                                                                                                                                                                                                    | stdio                                           |  |
| CB\_MCP\_HOST                                                 | \--host                                            | Host for HTTP transport mode                                                                                                                                                                                                                                                                                                                                   | 127.0.0.1                                       |  |
| CB\_MCP\_PORT                                                 | \--port                                            | Port for HTTP transport mode. Overrides the server default of 8001.                                                                                                                                                                                                                                                                                            | None                                            |  |
| CB\_MCP\_WORKERS                                              | \--workers                                         | Number of worker processes. The Operational Insights server supports only 1 and refuses larger values.                                                                                                                                                                                                                                                         | 1                                               |  |
| CB\_MCP\_STATELESS\_HTTP                                      | \--stateless-http                                  | Run HTTP transport mode without session state, for replicas behind a load balancer without sticky sessions. See [Stateless Mode and Workers](streamable-http-oi.md#stateless-mode-and-workers).                                                                                                                                                                | false                                           |  |
| CB\_MCP\_OPERATIONAL\_INSIGHTS\_QUERY\_RESULT\_MAX\_SIZE      | \--operational-insights-query-result-max-size      | Maximum size, in bytes, of a query tool result. Unset means no limit, and the full result comes back. When set, reading stops once the limit is reached, and the response reports truncated: true. Values greater than 4194304 (4 MB) are reduced to 4 MB with a warning. See [Large Result Handling](large-results-oi.md).                                    | Unset                                           |  |
| CB\_MCP\_OPERATIONAL\_INSIGHTS\_ASYNC\_QUERY\_RESULT\_TIMEOUT | \--operational-insights-async-query-result-timeout | Timeout, in seconds, for the requests that the async query tools make to the cluster. It must be a positive integer, and the maximum is 600. The server replaces any other value with the default, and reduces a larger value to 600. It logs a warning in both cases. See [Timeout for Async Query Tools](large-results-oi.md#timeout-for-async-query-tools). | 30                                              |  |
| CB\_MCP\_DISABLED\_TOOLS                                      | \--disabled-tools                                  | Tools to disable. See [Disabling Tools](disabling-tools-oi.md)                                                                                                                                                                                                                                                                                                 | None                                            |  |
| CB\_MCP\_CONFIRMATION\_REQUIRED\_TOOLS                        | \--confirmation-required-tools                     | Tools requiring user confirmation before execution. See [Elicitation/Confirmation for Tool Calls](elicitation-for-tools-oi.md)                                                                                                                                                                                                                                 | None                                            |  |
| CB\_MCP\_OAUTH\_JWT\_JWKS\_URI                                | \--oauth-jwks-uri                                  | JWKS endpoint for verifying JWT signatures (Streamable HTTP only). See [OAuth](token-verification-oi.md).                                                                                                                                                                                                                                                      | None                                            |  |
| CB\_MCP\_OAUTH\_JWT\_ISSUER                                   | \--oauth-issuer                                    | Expected JWT iss (issuer) claim. See [OAuth](token-verification-oi.md).                                                                                                                                                                                                                                                                                        | None                                            |  |
| CB\_MCP\_OAUTH\_JWT\_AUDIENCE                                 | \--oauth-audience                                  | Expected JWT aud (audience) claim. See [OAuth](token-verification-oi.md).                                                                                                                                                                                                                                                                                      | None                                            |  |
| CB\_MCP\_OAUTH\_JWT\_ALGORITHM                                | \--oauth-algorithm                                 | JWT signing algorithm. See [OAuth](token-verification-oi.md).                                                                                                                                                                                                                                                                                                  | RS256                                           |  |
| CB\_MCP\_OAUTH\_MCP\_BASE\_URL                                | \--oauth-mcp-base-url                              | Public base URL of this server. Enables Protected Resource Metadata / DCR discovery. See [OAuth](token-verification-oi.md).                                                                                                                                                                                                                                    | None                                            |  |
| CB\_MCP\_OAUTH\_SCOPE\_READ\_LABEL                            | \--oauth-scope-read-label                          | Custom label for the read scope, for IdPs using a different naming convention. See [OAuth](oauth-overview-oi.md).                                                                                                                                                                                                                                              | couchbase-mcp:read                              |  |
| CB\_MCP\_OAUTH\_SCOPE\_WRITE\_LABEL                           | \--oauth-scope-write-label                         | Custom label for the write scope, for IdPs using a different naming convention. See [OAuth](oauth-overview-oi.md).                                                                                                                                                                                                                                             | couchbase-mcp:write                             |  |
| CB\_MCP\_LOG\_LEVEL                                           | \--log-level                                       | Minimum log level: off, debug, info, warning, error. See [Logging](logging-oi.md).                                                                                                                                                                                                                                                                             | info                                            |  |
| CB\_MCP\_LOG\_SINKS                                           | \--log-sinks                                       | Log output sinks: stderr, file (writes to all listed). See [Logging](logging-oi.md).                                                                                                                                                                                                                                                                           | stderr                                          |  |
| CB\_MCP\_LOG\_FILE                                            | \--log-file                                        | Base path for the per-level log files. Used when the file sink is enabled. See [Logging](logging-oi.md).                                                                                                                                                                                                                                                       | mcp\_server\_operational\_insights.log          |  |
| CB\_MCP\_LOG\_MAX\_BYTES                                      | \--log-max-bytes                                   | **Deprecated** — use CB\_MCP\_LOG\_ROTATION\_MAX\_SIZE\_MB instead. Still honored for backward compatibility. If both are set, the MB variable takes priority (with a startup warning). See [Logging](logging-oi.md).                                                                                                                                          | 1048576 (1 MB)                                  |  |
| CB\_MCP\_LOG\_ROTATION\_MAX\_SIZE\_MB                         | \--log-rotation-max-size-mb                        | Maximum size (MB) per log file before rotation, for all levels unless overridden per level. See [Logging](logging-oi.md#per-level-overrides).                                                                                                                                                                                                                  | 1                                               |  |
| CB\_MCP\_LOG\_RETENTION\_BACKUP\_COUNT                        | \--log-retention-backup-count                      | Number of rotated backup files kept per level, in addition to the live file, for all levels unless overridden per level. See [Logging](logging-oi.md#per-level-overrides).                                                                                                                                                                                     | 1                                               |  |
| CB\_MCP\_LOG\_ERROR\_ROTATION\_MAX\_SIZE\_MB                  | \--log-error-rotation-max-size-mb                  | Rotation size in MB for the error log file. Overrides CB\_MCP\_LOG\_ROTATION\_MAX\_SIZE\_MB for error.                                                                                                                                                                                                                                                         | Inherits CB\_MCP\_LOG\_ROTATION\_MAX\_SIZE\_MB  |  |
| CB\_MCP\_LOG\_WARNING\_ROTATION\_MAX\_SIZE\_MB                | \--log-warning-rotation-max-size-mb                | Rotation size in MB for the warning log file. Overrides CB\_MCP\_LOG\_ROTATION\_MAX\_SIZE\_MB for warning.                                                                                                                                                                                                                                                     | Inherits CB\_MCP\_LOG\_ROTATION\_MAX\_SIZE\_MB  |  |
| CB\_MCP\_LOG\_INFO\_ROTATION\_MAX\_SIZE\_MB                   | \--log-info-rotation-max-size-mb                   | Rotation size in MB for the info log file. Overrides CB\_MCP\_LOG\_ROTATION\_MAX\_SIZE\_MB for info.                                                                                                                                                                                                                                                           | Inherits CB\_MCP\_LOG\_ROTATION\_MAX\_SIZE\_MB  |  |
| CB\_MCP\_LOG\_DEBUG\_ROTATION\_MAX\_SIZE\_MB                  | \--log-debug-rotation-max-size-mb                  | Rotation size in MB for the debug log file. Overrides CB\_MCP\_LOG\_ROTATION\_MAX\_SIZE\_MB for debug.                                                                                                                                                                                                                                                         | Inherits CB\_MCP\_LOG\_ROTATION\_MAX\_SIZE\_MB  |  |
| CB\_MCP\_LOG\_ERROR\_RETENTION\_BACKUP\_COUNT                 | \--log-error-retention-backup-count                | Rotated backups kept for the error log file. Overrides the global count for error.                                                                                                                                                                                                                                                                             | Inherits CB\_MCP\_LOG\_RETENTION\_BACKUP\_COUNT |  |
| CB\_MCP\_LOG\_WARNING\_RETENTION\_BACKUP\_COUNT               | \--log-warning-retention-backup-count              | Rotated backups kept for the warning log file. Overrides the global count for warning.                                                                                                                                                                                                                                                                         | Inherits CB\_MCP\_LOG\_RETENTION\_BACKUP\_COUNT |  |
| CB\_MCP\_LOG\_INFO\_RETENTION\_BACKUP\_COUNT                  | \--log-info-retention-backup-count                 | Rotated backups kept for the info log file. Overrides the global count for info.                                                                                                                                                                                                                                                                               | Inherits CB\_MCP\_LOG\_RETENTION\_BACKUP\_COUNT |  |
| CB\_MCP\_LOG\_DEBUG\_RETENTION\_BACKUP\_COUNT                 | \--log-debug-retention-backup-count                | Rotated backups kept for the debug log file. Overrides the global count for debug.                                                                                                                                                                                                                                                                             | Inherits CB\_MCP\_LOG\_RETENTION\_BACKUP\_COUNT |  |
| CB\_MCP\_AUDIT\_LOG\_ENABLED                                  | \--audit-log-enabled                               | Turns audit logging on. See [Audit Logging](audit-logging-oi.md).                                                                                                                                                                                                                                                                                              | false                                           |  |
| CB\_MCP\_AUDIT\_LOG\_SINKS                                    | \--audit-log-sinks                                 | Comma-separated list of audit sinks. Allowed values are console and file.                                                                                                                                                                                                                                                                                      | console                                         |  |
| CB\_MCP\_AUDIT\_LOG\_FILE\_PATH                               | \--audit-log-file-path                             | Path of the audit log file. Needed when file is one of the sinks.                                                                                                                                                                                                                                                                                              | None                                            |  |
| CB\_MCP\_AUDIT\_LOG\_ROTATION\_MAX\_SIZE\_MB                  | \--audit-log-rotation-max-size-mb                  | Size (MB) that the live audit file can reach before rotation. 0 turns size-based rotation off.                                                                                                                                                                                                                                                                 | 10                                              |  |
| CB\_MCP\_AUDIT\_LOG\_ROTATION\_INTERVAL                       | \--audit-log-rotation-interval                     | Age that the live audit file can reach before rotation, as <value>d or <value>w. 0 turns time-based rotation off.                                                                                                                                                                                                                                              | 1d                                              |  |
| CB\_MCP\_AUDIT\_LOG\_RETENTION\_MAX\_BACKUPS                  | \--audit-log-retention-max-backups                 | Number of rotated backups kept for each audit file, not counting the live file.                                                                                                                                                                                                                                                                                | 10                                              |  |
| CB\_MCP\_AUDIT\_LOG\_TOOL\_ARGS                               | \--audit-log-tool-args                             | Includes tool arguments in audit records, verbatim and without redaction.                                                                                                                                                                                                                                                                                      | false                                           |  |
| CB\_MCP\_AUDIT\_LOG\_DISABLED\_EVENTS                         | \--audit-log-disabled-events                       | Numeric event IDs to turn off, as a comma-separated list or a path to a file. The server refuses to turn off write or security events.                                                                                                                                                                                                                         | None                                            |  |

> [!NOTE]
> You can also set both the rotation size and backup count per log level (`error`, `warning`, `info`, `debug`) — see [Per-Level Overrides](logging-oi.md#per-level-overrides).

## [](#checking-the-mcp-server-version)Checking the MCP Server Version

```bash
uvx couchbase-mcp-server --version
```

## [](#configuring-authentication)Configuring Authentication

For authentication, you need **either**:

* Username and Password ([basic authentication](#how-to-basic-auth))

**or**

* Client Certificate and Key paths ([mTLS authentication](#how-to-mtls-based-auth))

If you specify both, mTLS takes priority.

Optionally, you can specify a CA root certificate path to validate server certificates (useful for self-signed certificates).

---

## [](#example-configurations)Example Configurations

> [!NOTE]
> The following examples use `uvx` to run the server. You can replace these with the corresponding `docker run` commands - see [Streamable HTTP](streamable-http-oi.md) for the Docker HTTP configuration.

### [](#how-to-basic-auth)How to: Basic Auth

Provide an Operational Insights username and password. For Basic Authentication setup, see [Manage Users and Roles](https://docs.couchbase.com/server/current/manage/manage-security/manage-users-and-roles.html) (self-managed).

```json
{
  "mcpServers": {
    "couchbase-oi": {
      "command": "uvx",
      "args": ["couchbase-mcp-server", "operational-insights"],
      "env": {
        "CB_OPERATIONAL_INSIGHTS_CONNECTION_STRING": "https://your-oi-endpoint",
        "CB_OPERATIONAL_INSIGHTS_USERNAME": "username",
        "CB_OPERATIONAL_INSIGHTS_PASSWORD": "password"
      }
    }
  }
}
```

### [](#how-to-connect-with-certificates)How to: Connect with Certificates

* **Connection string**: Use `http://` for unencrypted connections or `https://` for TLS.
* **TLS certificates**: If using TLS with self-signed or untrusted certificates, set `CB_OPERATIONAL_INSIGHTS_CA_CERT_PATH` to your CA root certificate.
* **mTLS**: For certificate-based authentication, use `CB_OPERATIONAL_INSIGHTS_CLIENT_CERT_PATH` and `CB_OPERATIONAL_INSIGHTS_CLIENT_KEY_PATH` instead of username/password. For a PKCS#12 bundle (`.p12` or `.pfx`), set only `CB_OPERATIONAL_INSIGHTS_CLIENT_CERT_PATH`. If the client key or bundle is encrypted, also set `CB_OPERATIONAL_INSIGHTS_CLIENT_CERT_PASSWORD`. mTLS requires an `https://` connection string.

**Basic auth with custom CA:**

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
        "CB_OPERATIONAL_INSIGHTS_CA_CERT_PATH": "/path/to/ca-certificate.pem"
      }
    }
  }
}
```

**mTLS (no username/password):**

```json
{
  "mcpServers": {
    "couchbase-oi": {
      "command": "uvx",
      "args": ["couchbase-mcp-server", "operational-insights"],
      "env": {
        "CB_OPERATIONAL_INSIGHTS_CONNECTION_STRING": "https://your-oi-endpoint",
        "CB_OPERATIONAL_INSIGHTS_CLIENT_CERT_PATH": "/path/to/client-certificate.pem",
        "CB_OPERATIONAL_INSIGHTS_CLIENT_KEY_PATH": "/path/to/client.key",
        "CB_OPERATIONAL_INSIGHTS_CA_CERT_PATH": "/path/to/ca-certificate.pem"
      }
    }
  }
}
```

### [](#how-to-mtls-based-auth)How to: mTLS Based Auth

For environments requiring certificate-based authentication. For mTLS setup, see [Configure Client Certificate Authentication](https://docs.couchbase.com/server/current/manage/manage-security/configure-client-certificates.html).

```json
{
  "mcpServers": {
    "couchbase-oi": {
      "command": "uvx",
      "args": ["couchbase-mcp-server", "operational-insights"],
      "env": {
        "CB_OPERATIONAL_INSIGHTS_CONNECTION_STRING": "https://your-oi-endpoint",
        "CB_OPERATIONAL_INSIGHTS_CLIENT_CERT_PATH": "/path/to/client-certificate.pem",
        "CB_OPERATIONAL_INSIGHTS_CLIENT_KEY_PATH": "/path/to/client.key"
      }
    }
  }
}
```