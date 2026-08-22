---
title: Environment Variables &amp; Command Line Arguments
description: Reference for all environment variables and CLI arguments used to
  configure the Couchbase MCP Server, including authentication examples.
pubDate: 2026-08-22T04:32:17.641Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/release/1.0/modules/configuration/pages/environment-variables.adoc
  xref: xref:mcp-server:configuration:environment-variables.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/configuration/environment-variables.html)

# Environment Variables &amp; Command Line Arguments

> Reference for all environment variables and CLI arguments used to configure the Couchbase MCP Server, including authentication examples. 

The MCP server can be configured using environment variables or command line arguments. If both are specified, command line arguments take priority over environment variables.

## [](#configuration-reference)Configuration Reference

| Environment Variable                            | CLI Argument                          | Description                                                                                                                                                                                                        | Default                                         |  |
| ----------------------------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------- |  |
| CB\_CONNECTION\_STRING                          | \--connection-string                  | Connection string to the Couchbase cluster. See [Configuring Connection String](../get-started/quickstart.md#step-2-set-your-connection-string).                                                                   | **Required**                                    |  |
| CB\_USERNAME                                    | \--username                           | Username for basic authentication. See [Configuring Authentication](#configuring-authentication).                                                                                                                  | **Required (or mTLS)**                          |  |
| CB\_PASSWORD                                    | \--password                           | Password for basic authentication. See [Configuring Authentication](#configuring-authentication).                                                                                                                  | **Required (or mTLS)**                          |  |
| CB\_CLIENT\_CERT\_PATH                          | \--client-cert-path                   | Path to client certificate for mTLS. See [Configuring Authentication](#configuring-authentication).                                                                                                                | **Required if using mTLS**                      |  |
| CB\_CLIENT\_KEY\_PATH                           | \--client-key-path                    | Path to client key for mTLS. See [Configuring Authentication](#configuring-authentication).                                                                                                                        | **Required if using mTLS**                      |  |
| CB\_CA\_CERT\_PATH                              | \--ca-cert-path                       | Path to server root certificate for TLS (self-signed / untrusted certs). Not required for Capella.                                                                                                                 |                                                 |  |
| CB\_MCP\_READ\_ONLY\_MODE                       | \--read-only-mode                     | Prevent all data modifications (KV and Query). See [Read-Only Mode](read-only-mode.md) for details.                                                                                                                | true                                            |  |
| CB\_MCP\_TRANSPORT                              | \--transport                          | Transport mode selection: stdio (client launches server as subprocess), http ([Streamable HTTP](streamable-http.md) \- multiple clients, serves at /mcp)                                                           | stdio                                           |  |
| CB\_MCP\_HOST                                   | \--host                               | Host for HTTP transport mode                                                                                                                                                                                       | 127.0.0.1                                       |  |
| CB\_MCP\_PORT                                   | \--port                               | Port for HTTP transport mode                                                                                                                                                                                       | 8000                                            |  |
| CB\_MCP\_DISABLED\_TOOLS                        | \--disabled-tools                     | Tools to disable. See [Disabling Tools](disabling-tools.md)                                                                                                                                                        | None                                            |  |
| CB\_MCP\_CONFIRMATION\_REQUIRED\_TOOLS          | \--confirmation-required-tools        | Tools requiring user confirmation before execution. See [Elicitation/Confirmation for Tool Calls](elicitation-for-tools.md)                                                                                        | None                                            |  |
| CB\_MCP\_OAUTH\_JWT\_JWKS\_URI                  | \--oauth-jwks-uri                     | JWKS endpoint for verifying JWT signatures (Streamable HTTP only). See [OAuth](token-verification.md).                                                                                                             | None                                            |  |
| CB\_MCP\_OAUTH\_JWT\_ISSUER                     | \--oauth-issuer                       | Expected JWT iss (issuer) claim. See [OAuth](token-verification.md).                                                                                                                                               | None                                            |  |
| CB\_MCP\_OAUTH\_JWT\_AUDIENCE                   | \--oauth-audience                     | Expected JWT aud (audience) claim. See [OAuth](token-verification.md).                                                                                                                                             | None                                            |  |
| CB\_MCP\_OAUTH\_JWT\_ALGORITHM                  | \--oauth-algorithm                    | JWT signing algorithm. See [OAuth](token-verification.md).                                                                                                                                                         | RS256                                           |  |
| CB\_MCP\_OAUTH\_MCP\_BASE\_URL                  | \--oauth-mcp-base-url                 | Public base URL of this server; enables Protected Resource Metadata / DCR discovery. See [OAuth](token-verification.md).                                                                                           | None                                            |  |
| CB\_MCP\_OAUTH\_SCOPE\_READ\_LABEL              | \--oauth-scope-read-label             | Custom label for the read scope, for IdPs using a different naming convention. See [OAuth](oauth-overview.md).                                                                                                     | couchbase-mcp:read                              |  |
| CB\_MCP\_OAUTH\_SCOPE\_WRITE\_LABEL             | \--oauth-scope-write-label            | Custom label for the write scope, for IdPs using a different naming convention. See [OAuth](oauth-overview.md).                                                                                                    | couchbase-mcp:write                             |  |
| CB\_MCP\_LOG\_LEVEL                             | \--log-level                          | Minimum log level: off, debug, info, warning, error. See [Logging](logging.md).                                                                                                                                    | info                                            |  |
| CB\_MCP\_LOG\_SINKS                             | \--log-sinks                          | Log output sinks: stderr, file (writes to all listed). See [Logging](logging.md).                                                                                                                                  | stderr                                          |  |
| CB\_MCP\_LOG\_FILE                              | \--log-file                           | Base path for the per-level log files; used when the file sink is enabled. See [Logging](logging.md).                                                                                                              | mcp\_server.log                                 |  |
| CB\_MCP\_LOG\_MAX\_BYTES                        | \--log-max-bytes                      | **Deprecated** — use CB\_MCP\_LOG\_ROTATION\_MAX\_SIZE\_MB instead. Still honored for backward compatibility; if both are set, the MB variable takes priority (with a startup warning). See [Logging](logging.md). | 1048576 (1 MB)                                  |  |
| CB\_MCP\_LOG\_ROTATION\_MAX\_SIZE\_MB           | \--log-rotation-max-size-mb           | Maximum size (MB) per log file before rotation, for all levels unless overridden per level. See [Logging](logging.md#per-level-overrides).                                                                         | 1                                               |  |
| CB\_MCP\_LOG\_RETENTION\_BACKUP\_COUNT          | \--log-retention-backup-count         | Number of rotated backup files kept per level, in addition to the live file, for all levels unless overridden per level. See [Logging](logging.md#per-level-overrides).                                            | 1                                               |  |
| CB\_MCP\_LOG\_ERROR\_ROTATION\_MAX\_SIZE\_MB    | \--log-error-rotation-max-size-mb     | Rotation size in MB for the error log file; overrides CB\_MCP\_LOG\_ROTATION\_MAX\_SIZE\_MB for error.                                                                                                             | Inherits CB\_MCP\_LOG\_ROTATION\_MAX\_SIZE\_MB  |  |
| CB\_MCP\_LOG\_WARNING\_ROTATION\_MAX\_SIZE\_MB  | \--log-warning-rotation-max-size-mb   | Rotation size in MB for the warning log file; overrides CB\_MCP\_LOG\_ROTATION\_MAX\_SIZE\_MB for warning.                                                                                                         | Inherits CB\_MCP\_LOG\_ROTATION\_MAX\_SIZE\_MB  |  |
| CB\_MCP\_LOG\_INFO\_ROTATION\_MAX\_SIZE\_MB     | \--log-info-rotation-max-size-mb      | Rotation size in MB for the info log file; overrides CB\_MCP\_LOG\_ROTATION\_MAX\_SIZE\_MB for info.                                                                                                               | Inherits CB\_MCP\_LOG\_ROTATION\_MAX\_SIZE\_MB  |  |
| CB\_MCP\_LOG\_DEBUG\_ROTATION\_MAX\_SIZE\_MB    | \--log-debug-rotation-max-size-mb     | Rotation size in MB for the debug log file; overrides CB\_MCP\_LOG\_ROTATION\_MAX\_SIZE\_MB for debug.                                                                                                             | Inherits CB\_MCP\_LOG\_ROTATION\_MAX\_SIZE\_MB  |  |
| CB\_MCP\_LOG\_ERROR\_RETENTION\_BACKUP\_COUNT   | \--log-error-retention-backup-count   | Rotated backups kept for the error log file; overrides the global count for error.                                                                                                                                 | Inherits CB\_MCP\_LOG\_RETENTION\_BACKUP\_COUNT |  |
| CB\_MCP\_LOG\_WARNING\_RETENTION\_BACKUP\_COUNT | \--log-warning-retention-backup-count | Rotated backups kept for the warning log file; overrides the global count for warning.                                                                                                                             | Inherits CB\_MCP\_LOG\_RETENTION\_BACKUP\_COUNT |  |
| CB\_MCP\_LOG\_INFO\_RETENTION\_BACKUP\_COUNT    | \--log-info-retention-backup-count    | Rotated backups kept for the info log file; overrides the global count for info.                                                                                                                                   | Inherits CB\_MCP\_LOG\_RETENTION\_BACKUP\_COUNT |  |
| CB\_MCP\_LOG\_DEBUG\_RETENTION\_BACKUP\_COUNT   | \--log-debug-retention-backup-count   | Rotated backups kept for the debug log file; overrides the global count for debug.                                                                                                                                 | Inherits CB\_MCP\_LOG\_RETENTION\_BACKUP\_COUNT |  |

> [!NOTE]
> Both the rotation size and backup count can also be set per log level (`error`, `warning`, `info`, `debug`) — see [Per-Level Overrides](logging.md#per-level-overrides).

## [](#checking-the-mcp-server-version)Checking the MCP Server Version

```bash
uvx couchbase-mcp-server --version
```

## [](#configuring-authentication)Configuring Authentication

For authentication, you need **either**:

* Username and Password ([basic authentication](#how-to-basic-auth))

**or**

* Client Certificate and Key paths ([mTLS authentication](#how-to-mtls-based-auth))

If both are specified, mTLS takes priority.

Optionally, you can specify a CA root certificate path to validate server certificates (useful for self-signed certificates).

---

## [](#example-configurations)Example Configurations

> [!NOTE]
> All examples below use `uvx` to run the server. These can be replaced with the corresponding `docker run` commands - see [Streamable HTTP](streamable-http.md) for the Docker HTTP configuration.

### [](#how-to-basic-auth)How to: Basic Auth

Provide a Couchbase database username and password. For Basic Authentication setup, see [Manage Database Credentials](https://docs.couchbase.com/cloud/clusters/manage-database-users.html) (Capella) or [Manage Users and Roles](https://docs.couchbase.com/server/current/manage/manage-security/manage-users-and-roles.html) (self-managed).

```json
{
  "mcpServers": {
    "couchbase": {
      "command": "uvx",
      "args": ["couchbase-mcp-server"],
      "env": {
        "CB_CONNECTION_STRING": "couchbases://your-connection-string",
        "CB_USERNAME": "username",
        "CB_PASSWORD": "password"
      }
    }
  }
}
```

### [](#how-to-connect-to-capella)How to: Connect to Capella

* **Connection string**: Use `couchbases://` (with `s`) — TLS is always enabled. Find your connection string in the [Capella UI](https://docs.couchbase.com/cloud/get-started/connect.html) under **Cluster** \> **Connect**.
* **TLS certificates**: The bundled Capella root CA is used automatically. You do not need to set `CB_CA_CERT_PATH`.
* **IP allowlisting**: Ensure the machine running the MCP server has its IP [allowed](https://docs.couchbase.com/cloud/clusters/allow-ip-address.html) in the Capella cluster settings. Required only when the server reaches Capella over the public Internet — not if it's on a VPC or a private network connected to Capella.

```json
{
  "mcpServers": {
    "couchbase": {
      "command": "uvx",
      "args": ["couchbase-mcp-server"],
      "env": {
        "CB_CONNECTION_STRING": "couchbases://cb.your-capella-endpoint.cloud.couchbase.com",
        "CB_USERNAME": "username",
        "CB_PASSWORD": "password"
      }
    }
  }
}
```

### [](#how-to-connect-to-self-managed-server-with-certificates)How to: Connect to Self-Managed Server with Certificates

* **Connection string**: Use `couchbase://` for unencrypted connections or `couchbases://` for TLS.
* **TLS certificates**: If using TLS with self-signed or untrusted certificates, set `CB_CA_CERT_PATH` to your CA root certificate.
* **mTLS**: For certificate-based authentication, use `CB_CLIENT_CERT_PATH` and `CB_CLIENT_KEY_PATH` instead of username/password.

**Basic auth with custom CA:**

```json
{
  "mcpServers": {
    "couchbase": {
      "command": "uvx",
      "args": ["couchbase-mcp-server"],
      "env": {
        "CB_CONNECTION_STRING": "couchbases://your-server-hostname",
        "CB_USERNAME": "username",
        "CB_PASSWORD": "password",
        "CB_CA_CERT_PATH": "/path/to/ca-certificate.pem"
      }
    }
  }
}
```

**mTLS (no username/password):**

```json
{
  "mcpServers": {
    "couchbase": {
      "command": "uvx",
      "args": ["couchbase-mcp-server"],
      "env": {
        "CB_CONNECTION_STRING": "couchbases://your-server-hostname",
        "CB_CLIENT_CERT_PATH": "/path/to/client-certificate.pem",
        "CB_CLIENT_KEY_PATH": "/path/to/client.key",
        "CB_CA_CERT_PATH": "/path/to/ca-certificate.pem"
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
    "couchbase": {
      "command": "uvx",
      "args": ["couchbase-mcp-server"],
      "env": {
        "CB_CONNECTION_STRING": "couchbases://your-connection-string",
        "CB_CLIENT_CERT_PATH": "/path/to/client-certificate.pem",
        "CB_CLIENT_KEY_PATH": "/path/to/client.key"
      }
    }
  }
}
```