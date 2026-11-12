---
title: Environment Variables &amp; Command Line Arguments
description: Reference for all environment variables and CLI arguments used to
  configure the Couchbase MCP Server, including authentication examples.
pubDate: 2026-11-12T06:49:41.760Z
meta:
  component:
    title: Couchbase MCP Server Self-Managed
    version: "1.1"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/release/1.1/modules/configuration/pages/environment-variables.adoc
  xref: xref:mcp-server:configuration:environment-variables.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/current/configuration/environment-variables.html)

# Environment Variables &amp; Command Line Arguments

> Reference for all environment variables and CLI arguments used to configure the Couchbase MCP Server, including authentication examples. 

You can configure the MCP server using environment variables or command line arguments. If you specify both, command line arguments take priority over environment variables.

> [!NOTE]
> As of v1.1, the server can also be invoked with an explicit `operational` subcommand (`couchbase-mcp-server operational`) — see [Architecture](../reference/common-architecture.md). Running with no subcommand is unchanged and still starts the operational server.

## [](#configuration-reference)Configuration Reference

| Environment Variable                                | CLI Argument                             | Description                                                                                                                                                                                                                                                    | Default                                         |  |
| --------------------------------------------------- | ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |  |
| CB\_CONNECTION\_STRING                              | \--connection-string                     | Connection string to the Couchbase cluster. See [Configuring Connection String](../get-started/quickstart.md#step-2-set-your-connection-string).                                                                                                               | **Required**                                    |  |
| CB\_USERNAME                                        | \--username                              | Username for basic authentication. See [Configuring Authentication](#configuring-authentication).                                                                                                                                                              | **Required (or mTLS)**                          |  |
| CB\_PASSWORD                                        | \--password                              | Password for basic authentication. See [Configuring Authentication](#configuring-authentication).                                                                                                                                                              | **Required (or mTLS)**                          |  |
| CB\_CLIENT\_CERT\_PATH                              | \--client-cert-path                      | Path to client certificate for mTLS. See [Configuring Authentication](#configuring-authentication).                                                                                                                                                            | **Required if using mTLS**                      |  |
| CB\_CLIENT\_KEY\_PATH                               | \--client-key-path                       | Path to client key for mTLS. See [Configuring Authentication](#configuring-authentication).                                                                                                                                                                    | **Required if using mTLS**                      |  |
| CB\_CA\_CERT\_PATH                                  | \--ca-cert-path                          | Path to server root certificate for TLS (self-signed / untrusted certs). Not required for Capella.                                                                                                                                                             |                                                 |  |
| CB\_MCP\_READ\_ONLY\_MODE                           | \--read-only-mode                        | Prevent all data modifications (KV and Query). See [Read-Only Mode](read-only-mode.md) for details.                                                                                                                                                            | true                                            |  |
| CB\_MCP\_TRANSPORT                                  | \--transport                             | Transport mode selection: stdio (client launches server as subprocess), http ([Streamable HTTP](streamable-http.md) \- multiple clients, serves at /mcp)                                                                                                       | stdio                                           |  |
| CB\_MCP\_HOST                                       | \--host                                  | Host for HTTP transport mode                                                                                                                                                                                                                                   | 127.0.0.1                                       |  |
| CB\_MCP\_PORT                                       | \--port                                  | Port for HTTP transport mode. Overrides the server default of 8000.                                                                                                                                                                                            | None                                            |  |
| CB\_MCP\_WORKERS                                    | \--workers                               | Number of worker processes for HTTP transport mode. Values greater than 1 require the http transport and stateless mode, and you cannot combine them with \--confirmation-required-tools. See [Scaling with Workers](streamable-http.md#scaling-with-workers). | 1                                               |  |
| CB\_MCP\_STATELESS\_HTTP                            | \--stateless-http                        | Handle each HTTP request without session state. It turns on automatically when CB\_MCP\_WORKERS is greater than 1. Only the http transport honors it, and you cannot combine it with \--confirmation-required-tools.                                           | false                                           |  |
| CB\_MCP\_DISABLED\_TOOLS                            | \--disabled-tools                        | Tools to disable. See [Disabling Tools](disabling-tools.md)                                                                                                                                                                                                    | None                                            |  |
| CB\_MCP\_CONFIRMATION\_REQUIRED\_TOOLS              | \--confirmation-required-tools           | Tools requiring user confirmation before execution. See [Elicitation/Confirmation for Tool Calls](elicitation-for-tools.md)                                                                                                                                    | None                                            |  |
| CB\_MCP\_OAUTH\_JWT\_JWKS\_URI                      | \--oauth-jwks-uri                        | JWKS endpoint for verifying JWT signatures (Streamable HTTP only). See [OAuth](token-verification.md).                                                                                                                                                         | None                                            |  |
| CB\_MCP\_OAUTH\_JWT\_ISSUER                         | \--oauth-issuer                          | Expected JWT iss (issuer) claim. See [OAuth](token-verification.md).                                                                                                                                                                                           | None                                            |  |
| CB\_MCP\_OAUTH\_JWT\_AUDIENCE                       | \--oauth-audience                        | Expected JWT aud (audience) claim. See [OAuth](token-verification.md).                                                                                                                                                                                         | None                                            |  |
| CB\_MCP\_OAUTH\_JWT\_ALGORITHM                      | \--oauth-algorithm                       | JWT signing algorithm. See [OAuth](token-verification.md).                                                                                                                                                                                                     | RS256                                           |  |
| CB\_MCP\_OAUTH\_MCP\_BASE\_URL                      | \--oauth-mcp-base-url                    | Public base URL of this server. Enables Protected Resource Metadata / DCR discovery. See [OAuth](token-verification.md).                                                                                                                                       | None                                            |  |
| CB\_MCP\_OAUTH\_SCOPE\_READ\_LABEL                  | \--oauth-scope-read-label                | Custom label for the read scope, for IdPs using a different naming convention. See [OAuth](oauth-overview.md).                                                                                                                                                 | couchbase-mcp:read                              |  |
| CB\_MCP\_OAUTH\_SCOPE\_WRITE\_LABEL                 | \--oauth-scope-write-label               | Custom label for the write scope, for IdPs using a different naming convention. See [OAuth](oauth-overview.md).                                                                                                                                                | couchbase-mcp:write                             |  |
| CB\_MCP\_LOG\_LEVEL                                 | \--log-level                             | Minimum log level: off, debug, info, warning, error. See [Logging](logging.md).                                                                                                                                                                                | info                                            |  |
| CB\_MCP\_LOG\_SINKS                                 | \--log-sinks                             | Log output sinks: stderr, file (writes to all listed). See [Logging](logging.md).                                                                                                                                                                              | stderr                                          |  |
| CB\_MCP\_LOG\_FILE                                  | \--log-file                              | Base path for the per-level log files. Used when the file sink is enabled. See [Logging](logging.md).                                                                                                                                                          | mcp\_server.log                                 |  |
| CB\_MCP\_LOG\_MAX\_BYTES                            | \--log-max-bytes                         | **Deprecated** — use CB\_MCP\_LOG\_ROTATION\_MAX\_SIZE\_MB instead. Still honored for backward compatibility. If both are set, the MB variable takes priority (with a startup warning). See [Logging](logging.md).                                             | 1048576 (1 MB)                                  |  |
| CB\_MCP\_LOG\_ROTATION\_MAX\_SIZE\_MB               | \--log-rotation-max-size-mb              | Maximum size (MB) per log file before rotation, for all levels unless overridden per level. See [Logging](logging.md#per-level-overrides).                                                                                                                     | 1                                               |  |
| CB\_MCP\_LOG\_RETENTION\_BACKUP\_COUNT              | \--log-retention-backup-count            | Number of rotated backup files kept per level, in addition to the live file, for all levels unless overridden per level. See [Logging](logging.md#per-level-overrides).                                                                                        | 1                                               |  |
| CB\_MCP\_LOG\_ERROR\_ROTATION\_MAX\_SIZE\_MB        | \--log-error-rotation-max-size-mb        | Rotation size in MB for the error log file. Overrides CB\_MCP\_LOG\_ROTATION\_MAX\_SIZE\_MB for error.                                                                                                                                                         | Inherits CB\_MCP\_LOG\_ROTATION\_MAX\_SIZE\_MB  |  |
| CB\_MCP\_LOG\_WARNING\_ROTATION\_MAX\_SIZE\_MB      | \--log-warning-rotation-max-size-mb      | Rotation size in MB for the warning log file. Overrides CB\_MCP\_LOG\_ROTATION\_MAX\_SIZE\_MB for warning.                                                                                                                                                     | Inherits CB\_MCP\_LOG\_ROTATION\_MAX\_SIZE\_MB  |  |
| CB\_MCP\_LOG\_INFO\_ROTATION\_MAX\_SIZE\_MB         | \--log-info-rotation-max-size-mb         | Rotation size in MB for the info log file. Overrides CB\_MCP\_LOG\_ROTATION\_MAX\_SIZE\_MB for info.                                                                                                                                                           | Inherits CB\_MCP\_LOG\_ROTATION\_MAX\_SIZE\_MB  |  |
| CB\_MCP\_LOG\_DEBUG\_ROTATION\_MAX\_SIZE\_MB        | \--log-debug-rotation-max-size-mb        | Rotation size in MB for the debug log file. Overrides CB\_MCP\_LOG\_ROTATION\_MAX\_SIZE\_MB for debug.                                                                                                                                                         | Inherits CB\_MCP\_LOG\_ROTATION\_MAX\_SIZE\_MB  |  |
| CB\_MCP\_LOG\_ERROR\_RETENTION\_BACKUP\_COUNT       | \--log-error-retention-backup-count      | Rotated backups kept for the error log file. Overrides the global count for error.                                                                                                                                                                             | Inherits CB\_MCP\_LOG\_RETENTION\_BACKUP\_COUNT |  |
| CB\_MCP\_LOG\_WARNING\_RETENTION\_BACKUP\_COUNT     | \--log-warning-retention-backup-count    | Rotated backups kept for the warning log file. Overrides the global count for warning.                                                                                                                                                                         | Inherits CB\_MCP\_LOG\_RETENTION\_BACKUP\_COUNT |  |
| CB\_MCP\_LOG\_INFO\_RETENTION\_BACKUP\_COUNT        | \--log-info-retention-backup-count       | Rotated backups kept for the info log file. Overrides the global count for info.                                                                                                                                                                               | Inherits CB\_MCP\_LOG\_RETENTION\_BACKUP\_COUNT |  |
| CB\_MCP\_LOG\_DEBUG\_RETENTION\_BACKUP\_COUNT       | \--log-debug-retention-backup-count      | Rotated backups kept for the debug log file. Overrides the global count for debug.                                                                                                                                                                             | Inherits CB\_MCP\_LOG\_RETENTION\_BACKUP\_COUNT |  |
| CB\_MCP\_AUDIT\_LOG\_ENABLED                        | \--audit-log-enabled                     | Turns audit logging on. See [Audit Logging](audit-logging.md).                                                                                                                                                                                                 | false                                           |  |
| CB\_MCP\_AUDIT\_LOG\_SINKS                          | \--audit-log-sinks                       | Comma-separated list of audit sinks. Allowed values are console and file.                                                                                                                                                                                      | console                                         |  |
| CB\_MCP\_AUDIT\_LOG\_FILE\_PATH                     | \--audit-log-file-path                   | Path of the audit log file. Needed when file is one of the sinks.                                                                                                                                                                                              | None                                            |  |
| CB\_MCP\_AUDIT\_LOG\_ROTATION\_MAX\_SIZE\_MB        | \--audit-log-rotation-max-size-mb        | Size (MB) that the live audit file can reach before rotation. 0 turns size-based rotation off.                                                                                                                                                                 | 10                                              |  |
| CB\_MCP\_AUDIT\_LOG\_ROTATION\_INTERVAL             | \--audit-log-rotation-interval           | Age that the live audit file can reach before rotation, as <value>d or <value>w. 0 turns time-based rotation off.                                                                                                                                              | 1d                                              |  |
| CB\_MCP\_AUDIT\_LOG\_RETENTION\_MAX\_BACKUPS        | \--audit-log-retention-max-backups       | Number of rotated backups kept for each audit file, not counting the live file.                                                                                                                                                                                | 10                                              |  |
| CB\_MCP\_AUDIT\_LOG\_TOOL\_ARGS                     | \--audit-log-tool-args                   | Includes tool arguments in audit records, verbatim and without redaction.                                                                                                                                                                                      | false                                           |  |
| CB\_MCP\_AUDIT\_LOG\_DISABLED\_EVENTS               | \--audit-log-disabled-events             | Numeric event IDs to turn off, as a comma-separated list or a path to a file. The server refuses to turn off write or security events.                                                                                                                         | None                                            |  |
| CB\_MCP\_EMBEDDING\_MODEL\_PROVIDER                 | \--embedding-model-provider              | Embedding provider for the vector search tools: capella (the Capella Model Service), openai, cohere, voyage, or bedrock. The server sends the search text of every vector search to this provider. See [Embedding Providers](#embedding-providers).            | None                                            |  |
| CB\_MCP\_EMBEDDING\_MODEL                           | \--embedding-model                       | Name or ID of the embedding model.                                                                                                                                                                                                                             | None                                            |  |
| CB\_MCP\_EMBEDDING\_MODEL\_API\_KEY                 | \--embedding-model-api-key               | API key for the embedding provider. Providers other than bedrock need it. The server treats it as a secret.                                                                                                                                                    | None                                            |  |
| CB\_MCP\_EMBEDDING\_MODEL\_ENDPOINT                 | \--embedding-model-endpoint              | Base URL of the provider. Required for capella. With openai, it also allows OpenAI-compatible local servers such as Ollama or vLLM.                                                                                                                            | None                                            |  |
| CB\_MCP\_EMBEDDING\_MODEL\_AWS\_ACCESS\_KEY\_ID     | \--embedding-model-aws-access-key-id     | AWS access key ID. Bedrock only. If unset, the server uses the default AWS credential chain. The server treats it as a secret.                                                                                                                                 | None                                            |  |
| CB\_MCP\_EMBEDDING\_MODEL\_AWS\_SECRET\_ACCESS\_KEY | \--embedding-model-aws-secret-access-key | AWS secret access key. Bedrock only. If unset, the server uses the default AWS credential chain. The server treats it as a secret.                                                                                                                             | None                                            |  |
| CB\_MCP\_EMBEDDING\_MODEL\_AWS\_REGION              | \--embedding-model-aws-region            | AWS region. Bedrock only. If unset, the server uses the region that the AWS SDK resolves.                                                                                                                                                                      | None                                            |  |

> [!NOTE]
> Both the rotation size and backup count can also be set per log level (`error`, `warning`, `info`, `debug`) — see [Per-Level Overrides](logging.md#per-level-overrides).

## [](#embedding-providers)Embedding Providers

The vector search tools, `run_vector_query` and `run_vector_search`, turn the search text into an embedding with the provider that you configure. Set the provider and the model when you start the server. If you do not set a provider, the tools stay registered, and they return an error when you call them.

| Provider | Required Settings                                                                                   | Optional Settings                                                                                                                            | Notes                                                                                                                                                                                                                                                                                    |
| -------- | --------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| capella  | CB\_MCP\_EMBEDDING\_MODEL\_API\_KEY, CB\_MCP\_EMBEDDING\_MODEL, CB\_MCP\_EMBEDDING\_MODEL\_ENDPOINT | None                                                                                                                                         | The Capella Model Service, provisioned or serverless. The endpoint is the base URL of your deployment, such as <https://<id>.ai.couchbase.com>. It has no default. Find it in the Capella UI under AI Data Plane > Models. The model is the deployed model name.                         |
| openai   | CB\_MCP\_EMBEDDING\_MODEL\_API\_KEY, CB\_MCP\_EMBEDDING\_MODEL                                      | CB\_MCP\_EMBEDDING\_MODEL\_ENDPOINT                                                                                                          | An example model is text-embedding-3-small. Set the endpoint to use an OpenAI-compatible local server, such as Ollama, vLLM, or LM Studio.                                                                                                                                               |
| cohere   | CB\_MCP\_EMBEDDING\_MODEL\_API\_KEY, CB\_MCP\_EMBEDDING\_MODEL                                      | CB\_MCP\_EMBEDDING\_MODEL\_ENDPOINT                                                                                                          | An example model is embed-english-v3.0. Set the endpoint for a private Cohere deployment.                                                                                                                                                                                                |
| voyage   | CB\_MCP\_EMBEDDING\_MODEL\_API\_KEY, CB\_MCP\_EMBEDDING\_MODEL                                      | CB\_MCP\_EMBEDDING\_MODEL\_ENDPOINT                                                                                                          | An example model is voyage-3.                                                                                                                                                                                                                                                            |
| bedrock  | CB\_MCP\_EMBEDDING\_MODEL                                                                           | CB\_MCP\_EMBEDDING\_MODEL\_AWS\_ACCESS\_KEY\_ID, CB\_MCP\_EMBEDDING\_MODEL\_AWS\_SECRET\_ACCESS\_KEY, CB\_MCP\_EMBEDDING\_MODEL\_AWS\_REGION | Only the Titan embedding family works, such as amazon.titan-embed-text-v2:0. If you omit the keys, the server uses the default AWS credential chain. The region falls back to the one the AWS SDK resolves. Bedrock needs the optional extra couchbase-mcp-server\[bedrock-embeddings\]. |

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
> The following examples use `uvx` to run the server. You can replace these with the corresponding `docker run` commands - see [Streamable HTTP](streamable-http.md) for the Docker HTTP configuration.

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