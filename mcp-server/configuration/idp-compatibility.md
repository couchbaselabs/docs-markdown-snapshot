---
title: IDP Compatibility
description: Compare OAuth support across popular identity providers for use
  with the Couchbase MCP Server.
pubDate: 2026-08-22T04:32:17.641Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-mcp-server/edit/release/1.0/modules/configuration/pages/idp-compatibility.adoc
  xref: xref:mcp-server:configuration:idp-compatibility.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/mcp-server/configuration/idp-compatibility.html)

# IDP Compatibility

> Compare OAuth support across popular identity providers for use with the Couchbase MCP Server. 

The Couchbase MCP Server acts as an OAuth 2.1 resource server, so it works with identity providers (IdPs) that can issue **JWT access tokens** carrying the server's scopes. Whether a given IdP fits depends mainly on how it handles scope strings.

## [](#scope-compatibility)Scope Compatibility — The General Rule

The server's default scopes are `couchbase-mcp:read` and `couchbase-mcp:write`. You can remap these with `CB_MCP_OAUTH_SCOPE_READ_LABEL` / `CB_MCP_OAUTH_SCOPE_WRITE_LABEL` to match the naming convention used by a given identity provider. For more information, see [Environment Variables](environment-variables.md).

* **Works out of the box**: IdPs that let you define a scope string verbatim, or whose fixed scope format can be matched using the custom scope labels. The token can carry the configured read scope, the write scope, or both.
* **Needs a different IdP**: IdPs whose scope catalog cannot be matched even with custom labels.
* **Not suitable**: providers that issue opaque (non-JWT) tokens.

They cannot act as JWT resource-server authorization servers for custom scopes.

## [](#per-provider-support)Per-Provider Support

OAuth support across popular identity providers is not consistent — the level of support varies from one IdP to the next, both in which methods they offer (M2M, non-DCR, DCR) and in details like the scope format they emit. No single behavior applies across providers, so use the table below as a reference guide when operating with an IdP and a particular method.

> [!NOTE]
> This table describes support for OAuth client registration and machine-to-machine flows — it does not cover scope-string compatibility. A provider marked **No** can still work with the server if it issues JWTs with the required scopes directly, or via the custom scope labels described in [Scope Compatibility — The General Rule](#scope-compatibility).

| Authorization server                                                                           | Machine-to-Machine (client credentials) | Non-DCR (manual / pre-registered clients, user flow) | DCR (Dynamic Client Registration) |  |
| ---------------------------------------------------------------------------------------------- | --------------------------------------- | ---------------------------------------------------- | --------------------------------- |  |
| [Auth0](https://auth0.com)                                                                     | Yes                                     | Yes                                                  | Yes                               |  |
| [Descope](https://www.descope.com)                                                             | Yes                                     | Yes                                                  | Yes                               |  |
| [Stytch](https://stytch.com)                                                                   | Yes                                     | Yes                                                  | Yes                               |  |
| [Keycloak](https://www.keycloak.org)                                                           | Yes                                     | Yes                                                  | Yes                               |  |
| [Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity)                         | No                                      | Yes                                                  | No                                |  |
| [Okta](https://www.okta.com)                                                                   | Yes                                     | Yes                                                  | No                                |  |
| [AWS Cognito](https://aws.amazon.com/cognito/)                                                 | No                                      | Yes                                                  | No                                |  |
| [WorkOS](https://workos.com) / [AuthKit](https://www.authkit.com)                              | No                                      | No                                                   | Yes                               |  |
| [Google Identity](https://cloud.google.com/identity-platform)                                  | No                                      | No                                                   | No                                |  |
| [GitHub](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/scopes-for-oauth-apps) | No                                      | No                                                   | No                                |  |
| [Discord](https://docs.discord.com/developers/topics/oauth2)                                   | No                                      | No                                                   | No                                |  |

## [](#see-also)See Also

* [Choosing a Setup](choosing-a-setup.md)
* [Token Verification & PRM](token-verification.md)