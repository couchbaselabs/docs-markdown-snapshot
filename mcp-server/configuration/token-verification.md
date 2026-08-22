---
title: Token Verification &amp; PRM
description: Configure JWT token verification and optional Protected Resource
  Metadata (PRM) for OAuth on the Couchbase MCP Server.
pubDate: 2026-08-22T04:32:17.641Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/release/1.0/modules/configuration/pages/token-verification.adoc
  xref: xref:mcp-server:configuration:token-verification.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/configuration/token-verification.html)

# Token Verification &amp; PRM

> Configure JWT token verification and optional Protected Resource Metadata (PRM) for OAuth on the Couchbase MCP Server. 

This page covers the server-side OAuth configuration: **Token Verification** (always required to enable OAuth) and **Protected Resource Metadata (PRM)**, which builds on it to enable discovery and Dynamic Client Registration.

> [!IMPORTANT]
> These settings apply only in **Streamable HTTP** transport mode (`--transport=http`). OAuth is initialized only when the token-verification settings below are configured.

## [](#token-verification)Token Verification

The server validates incoming JWT bearer tokens issued by your identity provider (IdP) or authorization server. The server does not issue tokens or manage user identities — it only verifies them. (In Machine-to-Machine setups, the client obtains its own scoped JWT directly from the IdP; no PRM is needed.)

For each request, the server:

1. Reads the token from the `Authorization: Bearer <token>` header.
2. Fetches the IdP's public keys from the configured JWKS endpoint (cached and auto-rotated).
3. Verifies the JWT signature, and checks the `iss`, `aud`, and `exp` / `nbf` / `iat` claims.
4. Checks that the token's scope claim contains the scope required for the requested tool.

If token validation fails, the server responds with **401 Unauthorized**. If the token is valid but lacks the required scope, it responds with **403 Forbidden**.

### [](#configuration)Configuration

| Environment Variable                | Description                                                                                                  | Default             |  |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------- |  |
| CB\_MCP\_OAUTH\_JWT\_JWKS\_URI      | JWKS endpoint used to fetch the public keys for verifying token signatures.                                  | —                   |  |
| CB\_MCP\_OAUTH\_JWT\_ISSUER         | Expected iss (issuer) claim. Tokens from any other issuer are rejected.                                      | —                   |  |
| CB\_MCP\_OAUTH\_JWT\_AUDIENCE       | Expected aud (audience) claim, identifying this MCP server.                                                  | —                   |  |
| CB\_MCP\_OAUTH\_JWT\_ALGORITHM      | Signing algorithm used to verify tokens. Supported: RS256/RS384/RS512, ES256/ES384/ES512, PS256/PS384/PS512. | RS256               |  |
| CB\_MCP\_OAUTH\_SCOPE\_READ\_LABEL  | Custom label for the read scope, for IdPs using a different naming convention.                               | couchbase-mcp:read  |  |
| CB\_MCP\_OAUTH\_SCOPE\_WRITE\_LABEL | Custom label for the write scope, for IdPs using a different naming convention.                              | couchbase-mcp:write |  |

> [!NOTE]
> `CB_MCP_OAUTH_JWT_JWKS_URI`, `CB_MCP_OAUTH_JWT_ISSUER`, and `CB_MCP_OAUTH_JWT_AUDIENCE` are all-or-nothing: set **all three** to enable OAuth, or **none** to run without it. Providing only some of them is a configuration error and the server refuses to start (`Incomplete OAuth configuration`). `CB_MCP_OAUTH_JWT_ALGORITHM` is optional and defaults to `RS256`.

### [](#example)Example

**Start the server (CLI):**

In Streamable HTTP mode the server is run as a standalone process. Start it with the transport and OAuth options:

```bash
uvx couchbase-mcp-server \
  --connection-string='couchbases://your-connection-string' \
  --username='your-username' \
  --password='your-password' \
  --transport=http \
  --oauth-jwks-uri='https://auth.yourcompany.com/.well-known/jwks.json' \
  --oauth-issuer='https://auth.yourcompany.com' \
  --oauth-audience='couchbase-mcp-server'
```

**MCP client configuration (JSON):**

The client connects exactly as it would to any [Streamable HTTP](streamable-http.md) server — by URL. The client is responsible for obtaining and presenting the OAuth access token when calling the server.

```json
{
  "mcpServers": {
    "couchbase-http": {
      "url": "http://localhost:8000/mcp"
    }
  }
}
```

## [](#protected-resource-metadata-prm)Protected Resource Metadata (PRM)

By default the server only **verifies** tokens; clients must be told out of band how to obtain one. If your authorization server supports **Dynamic Client Registration (DCR)**, the server can instead publish a Protected Resource Metadata document at `/.well-known/oauth-protected-resource/mcp` (the server's `/mcp` resource path is appended, per RFC 9728), allowing compatible clients to automatically discover the authorization server and register themselves — no manual client configuration required.

Set `CB_MCP_OAUTH_MCP_BASE_URL` to enable this, in addition to the token-verification settings above. The authorization-server details advertised in the metadata are derived from `CB_MCP_OAUTH_JWT_ISSUER`.

> [!NOTE]
> PRM is **effectively required for IDE clients even in the non-DCR setup** — an IDE client has no other way to discover the authorization server, token endpoint, and scopes. It's only truly optional for a custom client where you hard-code that metadata yourself. See [Choosing a Setup](choosing-a-setup.md).

### [](#configuration-2)Configuration

| Environment Variable           | Description                                                                                                                                            | Default             |  |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------- |  |
| CB\_MCP\_OAUTH\_MCP\_BASE\_URL | Public base URL of this MCP server. When set, the server publishes the /.well-known/oauth-protected-resource/mcp endpoint to enable discovery and DCR. | None (PRM disabled) |  |

### [](#example-2)Example

**Start the server (CLI):**

Add `--oauth-mcp-base-url` to the token-verification options to publish the Protected Resource Metadata endpoint:

```bash
uvx couchbase-mcp-server \
  --connection-string='couchbases://your-connection-string' \
  --username='your-username' \
  --password='your-password' \
  --transport=http \
  --oauth-jwks-uri='https://auth.yourcompany.com/.well-known/jwks.json' \
  --oauth-issuer='https://auth.yourcompany.com' \
  --oauth-audience='couchbase-mcp-server' \
  --oauth-mcp-base-url='https://mcp.yourcompany.com'
```

**MCP client configuration (JSON):**

The client connects by URL, the same as any [Streamable HTTP](streamable-http.md) server. With PRM enabled, DCR-capable clients discover the authorization server and register automatically.

```json
{
  "mcpServers": {
    "couchbase-http": {
      "url": "https://mcp.yourcompany.com/mcp"
    }
  }
}
```

## [](#see-also)See Also

* [Choosing a Setup](choosing-a-setup.md)
* [IDP Compatibility](idp-compatibility.md)
* [Streamable HTTP Transport Mode](streamable-http.md)
* [Environment Variables & Command Line Arguments](environment-variables.md)