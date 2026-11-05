---
title: Security
description: Layered security controls — RBAC, read-only mode, tool disabling,
  TLS, and OAuth — for using the Couchbase MCP Server safely with LLMs.
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase MCP Server
    version: "1.1"
  topic_type: concept
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/release/1.1/modules/security/pages/security.adoc
  xref: xref:1.1@mcp-server:security:security.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/1.1/security/security.html)

# Security

> Layered security controls — RBAC, read-only mode, tool disabling, TLS, and OAuth — for using the Couchbase MCP Server safely with LLMs. 

The Couchbase MCP Server provides multiple layers of security to protect your data when used with LLMs.

## [](#best-practices-quick-reference)Best Practices Quick Reference

* **Always configure RBAC**: Create a dedicated database user with least-privilege permissions.
* **Create an explicit user for the MCP server**: Use a distinct database user dedicated to the MCP server (not a shared or admin account) so all its activity is attributable to one identity for auditability.
* **Keep read-only mode enabled**: `CB_MCP_READ_ONLY_MODE=true` (default) blocks all write operations.
* **Use TLS**: Use `couchbases://` connection strings for encrypted connections.
* **Disable unnecessary tools**: Reduce the attack surface by removing tools you do not need.
* **Enable confirmation for sensitive tools**: Use `CB_MCP_CONFIRMATION_REQUIRED_TOOLS` to prompt users before executing critical operations.
* **Authenticate clients over HTTP**: When using Streamable HTTP transport, enable [OAuth](../configuration/oauth-overview.md). Only authorized clients can then reach the server.
* **Terminate TLS with a reverse proxy**: When exposing the server over Streamable HTTP, run it behind a reverse proxy that terminates TLS, so TLS encrypts tokens and data in transit.
* **Do not rely on a single layer**: Combine RBAC, OAuth, read-only mode, tool disabling, confirmation, and TLS for defense in depth.
* **Logs exclude sensitive data**: Credentials, tokens, connection strings, query parameters, and document content are not written to logs. See [Logging](../configuration/logging.md#sensitive-data-in-logs).
* **Be careful what you share with third-party LLMs**: The cluster tools need administrator privileges, and their responses can contain infrastructure information. See [Sharing Infrastructure Information with LLMs](#sharing-infrastructure-information-with-llms).
* **Enable audit logging**: Turn on `CB_MCP_AUDIT_LOG_ENABLED` to record MCP-layer authorization decisions and tool invocations for compliance review. See [Audit Logging](../configuration/audit-logging.md).
* **Treat the audit log as sensitive**: `CB_MCP_AUDIT_LOG_TOOL_ARGS` records the full arguments of every tool call, including query text, document IDs, and keyspaces, which can contain PII or other sensitive data. Allow only trusted parties to read the audit log, enforce file permissions and retention controls, and keep the log out of support bundles and other shared diagnostics. See [Capturing Tool Arguments](../configuration/audit-logging.md#capturing-tool-arguments).

## [](#read-only-mode-default)Read-Only Mode (Default)

By default, `CB_MCP_READ_ONLY_MODE=true`. This:

* **Prevents the server from loading KV write tools** \- they don't appear in tool discovery.
* **Blocks SQL++ write queries**: the server rejects INSERT, UPDATE, DELETE, MERGE, and DDL statements.

See [Read-Only Mode](../configuration/read-only-mode.md) for the full configuration reference.

## [](#rbac-best-practices)RBAC Best Practices

> [!IMPORTANT]
> Database RBAC (Role-Based Access Control) permissions are the **authoritative security control**. Always configure appropriate RBAC permissions on your Couchbase user credentials as the primary security measure.

Recommendations:

* **Create a dedicated database user** for the MCP server with only the permissions it needs.
* **Grant read-only roles** if write operations are not needed (for example, `Data Reader`, `Query Select`).
* **Scope permissions to specific buckets** rather than granting cluster-wide access.
* **Do not rely solely on `CB_MCP_READ_ONLY_MODE` or tool disabling**: these guide LLM behavior but RBAC is the enforcement layer.

See [RBAC for Couchbase Server](https://docs.couchbase.com/server/current/manage/manage-security/manage-users-and-roles.html) or [RBAC for Capella](https://docs.couchbase.com/cloud/clusters/manage-database-users.html) for configuration details.

## [](#tool-disabling)Tool Disabling

You can [disable specific tools](../configuration/disabling-tools.md) to reduce the attack surface.

> [!WARNING]
> Disabling tools alone doesn't prevent certain operations from happening.
> 
> Data modifications can still occur via `run_sql_plus_plus_query` using SQL++ DML statements - unless `CB_MCP_READ_ONLY_MODE=true` or the database user lacks RBAC permissions.

## [](#tls-mtls)TLS / mTLS

The server supports:

* **TLS connections**: Use `couchbases://` (with `s`) in your connection string for encrypted connections.
* **Custom CA certificates**: Set `CB_CA_CERT_PATH` for self-signed or untrusted server certificates.
* **mTLS (mutual TLS)**: Set `CB_CLIENT_CERT_PATH` and `CB_CLIENT_KEY_PATH` for certificate-based authentication.

For Capella connections, TLS is always on, and the server uses the bundled Capella root CA automatically.

## [](#oauth-authentication-streamable-http)OAuth Authentication (Streamable HTTP)

The preceding TLS/mTLS and RBAC controls protect the **server → cluster** connection. When you expose the server over [Streamable HTTP](../configuration/streamable-http.md), also secure the **client → server** connection. This way, only authorized clients and agents can call its tools.

OAuth lets the server act as an OAuth 2.1 Resource Server: it verifies the JWT access token on each request and enforces scope-based authorization (`couchbase-mcp:read` / `couchbase-mcp:write` by default, configurable per IdP) on tool calls. This is independent of cluster RBAC, which remains the authoritative control over what data a caller can actually read or write.

> [!IMPORTANT]
> OAuth applies only to Streamable HTTP transport. It has no effect in `stdio` mode.

The server serves plain HTTP and does not terminate TLS, so anyone on the network can read bearer tokens in transit unless you encrypt them. Run the server behind a reverse proxy that terminates TLS — see [Securing the Endpoint with TLS](../configuration/streamable-http.md#securing-the-endpoint-with-tls).

See [OAuth](../configuration/oauth-overview.md) for configuration details.

## [](#elicitation-confirmation-for-tool-calls)Elicitation / Confirmation for Tool Calls

You can require user confirmation before the server executes specific tools, by configuring `CB_MCP_CONFIRMATION_REQUIRED_TOOLS`. When enabled, the server sends an [elicitation](https://modelcontextprotocol.io/docs/concepts/elicitation) request to the client, prompting the user to approve the action before it proceeds.

> [!IMPORTANT]
> Full functionality requires client support for [elicitation](https://modelcontextprotocol.io/clients). If the client does not support it, the server executes the tools without requiring confirmation.

See [Elicitation / Confirmation for Tool Calls](../configuration/elicitation-for-tools.md) for configuration details.

## [](#sharing-infrastructure-information-with-llms)Sharing Infrastructure Information with LLMs

An MCP client sends tool results to the LLM that it uses. The Couchbase Server cluster tools need administrator privileges, and their responses can contain infrastructure information. Be careful before you share these responses with a third-party LLM.

The tools return information such as the following:

* The Cluster Setup & Health tools return node addresses, service topology, cluster membership, bucket configuration, and cluster events.
* `get_active_queries` returns the statements of requests that other users are running.
* `get_server_configuration_status` returns the connection string and username in clear text. It shows only whether secrets, such as the password, are set.

If the LLM runs in a third-party service, you share this information with that third party. Be cautious before you do. To reduce the exposure:

* Review what each tool returns before you connect the server to a third-party LLM.
* Turn off the tools you do not need with [Disabling Tools](../configuration/disabling-tools.md).
* Connect with a database user that does not have the administrator roles that these tools need.
* Use an LLM that your organization approves for this information.

See [Cluster Setup & Health](../learn/tools.md#cluster-setup-health) for the tools and the roles they need.

## [](#risks-associated-with-llms)Risks Associated with LLMs

* The use of large language models involves risks, including the potential for inaccurate or harmful outputs.
* Couchbase does not review or evaluate the quality or accuracy of LLM outputs, and such outputs may not reflect Couchbase's views.
* You're solely responsible for determining whether to use LLMs and for complying with your organization's policies.

## [](#summary)Summary

For maximum security, layer these controls:

1. **RBAC** \- Least-privilege database user permissions (primary control).
2. **Read-Only Mode** \- `CB_MCP_READ_ONLY_MODE=true` (default) blocks all write operations.
3. **Tool Disabling** \- Remove unnecessary tools from LLM discovery.
4. **Confirmation** \- Require user approval before executing sensitive tools.
5. **TLS/mTLS** \- Encrypt all network traffic.
6. **OAuth** \- Authenticate and authorize clients connecting over Streamable HTTP.