---
title: Security
description: Layered security controls — RBAC, read-only mode, tool disabling,
  TLS, and OAuth — for using the Couchbase MCP Server safely with LLMs.
pubDate: 2026-08-22T04:32:17.641Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/release/1.0/modules/security/pages/security.adoc
  xref: xref:mcp-server:security:security.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/security/security.html)

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
* **Authenticate clients over HTTP**: When using Streamable HTTP transport, enable [OAuth](../configuration/oauth-overview.md) so only authorized clients can reach the server.
* **Terminate TLS with a reverse proxy**: When exposing the server over Streamable HTTP, run it behind a reverse proxy that terminates TLS so tokens and data are encrypted in transit.
* **Do not rely on a single layer**: Combine RBAC, OAuth, read-only mode, tool disabling, confirmation, and TLS for defense in depth.
* **Logs exclude sensitive data**: Credentials, tokens, connection strings, query parameters, and document content are not written to logs. See [Logging](../configuration/logging.md#sensitive-data-in-logs).

## [](#read-only-mode-default)Read-Only Mode (Default)

By default, `CB_MCP_READ_ONLY_MODE=true`. This:

* **Prevents KV write tools** from being loaded - they will not appear in tool discovery.
* **Blocks SQL++ write queries**: INSERT, UPDATE, DELETE, MERGE, and DDL statements are rejected.

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
> Disabling tools alone does not guarantee operations cannot be performed.
> 
> Data modifications can still occur via `run_sql_plus_plus_query` using SQL++ DML statements - unless `CB_MCP_READ_ONLY_MODE=true` or the database user lacks RBAC permissions.

## [](#tls-mtls)TLS / mTLS

The server supports:

* **TLS connections**: Use `couchbases://` (with `s`) in your connection string for encrypted connections.
* **Custom CA certificates**: Set `CB_CA_CERT_PATH` for self-signed or untrusted server certificates.
* **mTLS (mutual TLS)**: Set `CB_CLIENT_CERT_PATH` and `CB_CLIENT_KEY_PATH` for certificate-based authentication.

For Capella connections, TLS is always enabled and the bundled Capella root CA is used automatically.

## [](#oauth-authentication-streamable-http)OAuth Authentication (Streamable HTTP)

The TLS/mTLS and RBAC controls above protect the **server → cluster** connection. When the server is exposed over [Streamable HTTP](../configuration/streamable-http.md), you should also secure the **client → server** connection so that only authorized clients and agents can call its tools.

OAuth lets the server act as an OAuth 2.1 Resource Server: it verifies the JWT access token on each request and enforces scope-based authorization (`couchbase-mcp:read` / `couchbase-mcp:write` by default, configurable per IdP) on tool calls. This is independent of cluster RBAC, which remains the authoritative control over what data can actually be read or written.

> [!IMPORTANT]
> OAuth applies only to Streamable HTTP transport. It has no effect in `stdio` mode.

The server serves plain HTTP and does not terminate TLS, so bearer tokens are exposed in transit unless encrypted. Run the server behind a reverse proxy that terminates TLS — see [Securing the Endpoint with TLS](../configuration/streamable-http.md#securing-the-endpoint-with-tls).

See [OAuth](../configuration/oauth-overview.md) for configuration details.

## [](#elicitation-confirmation-for-tool-calls)Elicitation / Confirmation for Tool Calls

You can require user confirmation before specific tools are executed by configuring `CB_MCP_CONFIRMATION_REQUIRED_TOOLS`. When enabled, the server sends an [elicitation](https://modelcontextprotocol.io/docs/concepts/elicitation) request to the client, prompting the user to approve the action before it proceeds.

> [!IMPORTANT]
> Full functionality requires client support for [elicitation](https://modelcontextprotocol.io/clients). If the client does not support it, the tools will be executed without requiring confirmation.

See [Elicitation / Confirmation for Tool Calls](../configuration/elicitation-for-tools.md) for configuration details.

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