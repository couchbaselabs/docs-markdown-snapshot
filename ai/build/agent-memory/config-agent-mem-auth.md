---
title: Configure Agent Memory Authentication
description: Secure Agent Memory with OIDC/OAuth2 authentication by connecting
  it to your external identity provider (IdP).
editUrl: https://github.com/couchbaselabs/docs-ai/edit/main/modules/build/pages/agent-memory/config-agent-mem-auth.adoc
pubDate: 2026-07-20T13:54:32.914Z
link: xref:ai:build:agent-memory/config-agent-mem-auth.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ai/build/agent-memory/config-agent-mem-auth.html)

# Configure Agent Memory Authentication

> Secure Agent Memory with OIDC/OAuth2 authentication by connecting it to your external identity provider (IdP). 

Agent Memory acts as a stateless resource server that validates JWT access tokens issued by an IdP. Agent Memory never issues tokens or stores secrets such as client credentials or refresh tokens. Agent Memory validates each request independently using a cached JSON Web Key Set (JWKS) fetched from your IdP.

You can connect Agent Memory to any OIDC-compliant identity provider, including:

* [Keycloak](https://www.keycloak.org/docs/latest/securing%5Fapps/)
* [Auth0](https://auth0.com/docs/authenticate/protocols/openid-connect-protocol)
* [Okta](https://developer.okta.com/docs/concepts/oauth-openid/)
* [Microsoft Entra ID (Azure AD)](https://learn.microsoft.com/en-us/entra/identity-platform/)
* [AWS Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-oidc.html)
* [Google Identity Platform](https://developers.google.com/identity/openid-connect/openid-connect)
* [PingIdentity / PingFederate](https://docs.pingidentity.com/)
* [Dex](https://dexidp.io/docs/)
* [Ory Hydra](https://www.ory.sh/docs/hydra/)
* [OneLogin](https://onelogin.service-now.com/support/oidc)

## [](#prerequisites)Prerequisites

* You have an identity provider that supports OIDC and is reachable over HTTPS.
* Your IdP meets the following technical requirements:  
OIDC Discovery endpoint  
Your IdP must expose a discovery document at `/.well-known/openid-configuration`.  
JWKS endpoint  
The discovery document must contain a `jwks_uri` field pointing to the JSON Web Key Set endpoint.  
RS256 signing algorithm  
Access tokens must be signed with RS256 (RSA + SHA-256).  
Key ID (`kid`) claim  
The JWT header must include a `kid` claim for key lookup against the JWKS endpoint.  
Standard claims  
Access tokens must include the following claims: `iss`, `aud`, `exp`.

## [](#procedure)Procedure

To configure authentication for Agent Memory:

1. Configure a client in your IdP.  
> [!IMPORTANT]  
> The steps to configure a client in your IdP vary by provider. For more information, see your IdP's documentation.  
When configuring your client, make sure to complete the following:

  1. Create a new client or application. Use a `confidential` client type with the `client credentials` grant (service account), so that your application can obtain tokens without user interaction.
  2. Set the signing algorithm to `RS256`.
  3. Note the following values for the next step:  
  Issuer URL  
  The base URL of your IdP realm or tenant, for example `https://your-idp.example.com/realms/myrealm`.  
  Audience  
  The `aud` value that appears in access tokens, typically the client ID or a custom API identifier.  
  Client ID and Client secret  
  Your application uses these to obtain access tokens from the IdP.
2. Add the following environment variables to the `.env` file in your Agent Memory project directory:  
```bash  
OIDC_AUTH_ENABLED=true  
OIDC_ISSUER=$OIDC_ISSUER_URL  
OIDC_AUDIENCE=$OIDC_AUDIENCE  
```  
Replace each `$` placeholder with the values from your IdP client configuration. For a description of all available variables, see [Environment Variables](#env-vars).
3. Recreate the Agent Memory container to apply the new environment variables:  
> [!CAUTION]  
> This command briefly interrupts the Agent Memory service. In-flight requests fail until the new container is ready.  
```console  
docker compose up -d --force-recreate agentmemory-server  
```  
On startup, Agent Memory fetches and caches the JWKS from your IdP. The JWKS cache has no expiry time and persists until Agent Memory encounters a token signed with an unrecognized `kid`, at which point it re-fetches the JWKS once. If your IdP rotates key material while reusing the same `kid`, Agent Memory cannot detect the change automatically and continues to use the old key until you restart the container. The logs include the following message:  
```none  
OIDC authentication initialized issuer=\https://your-idp.example.com/realms/myrealm  
```
4. Verify that authentication is working by sending a request with a Bearer token.

  1. Obtain an access token from your IdP using the client credentials flow:  
  ```console  
  TOKEN=$(curl -s -X POST "$IDP_TOKEN_ENDPOINT" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials" \
  -d "client_id=$CLIENT_ID" \
  -d "client_secret=$CLIENT_SECRET" \
  | jq -r '.access_token')  
  ```
  2. Send an authenticated request to Agent Memory:  
  ```console  
  curl -X POST "https://$AGENTMEM_HOST/users" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "test-user-1", "name": "Test User"}'  
  ```  
  A `401 Unauthorized` response with `{"detail": "Authentication required"}` means the token was not sent or is invalid.

## [](#env-vars)Environment Variables

| Variable            | Required | Default | Description                                                                          |
| ------------------- | -------- | ------- | ------------------------------------------------------------------------------------ |
| OIDC\_AUTH\_ENABLED | No       | false   | Enable or disable authentication. Set to true to require tokens on all requests.     |
| OIDC\_ISSUER        | Yes1     | —       | OIDC provider issuer URL, for example <https://your-idp.example.com/realms/myrealm>. |
| OIDC\_AUDIENCE      | Yes1     | —       | Expected aud claim value in access tokens.                                           |

1 Required when `OIDC_AUTH_ENABLED=true`.

> [!CAUTION]
> Production Considerations
> 
> Agent Memory normalizes `host.docker.internal` to `localhost` when comparing the issuer URL in a token against `OIDC_ISSUER`. This means tokens issued with either hostname validate against the other. In production, always set `OIDC_ISSUER` to the real public issuer URL. Never use `localhost` or `host.docker.internal`.

## [](#troubleshooting)Troubleshooting

If you encounter an error when setting up authentication for your Agent Memory instance, use the following information to help troubleshoot:

| Error                           | Cause                                                                                                                                                                                                                                                | Solution                                                                                                                                                                                                                                                                                                                                           |           |                                                                 |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | --------------------------------------------------------------- |
| "OIDC provider not initialized" | Auth is enabled but OIDC discovery failed at startup. Agent Memory retries discovery 3 times with exponential backoff, then exits the container. A transient network issue at container start can trigger this, not only a misconfigured issuer URL. | Verify that OIDC\_ISSUER is reachable over HTTPS and exposes /.well-known/openid-configuration. Check that the network path from the container to your IdP is available when the container starts. If you use an orchestrator such as Docker Compose or Kubernetes, configure a restart policy so the container restarts automatically on failure. |           |                                                                 |
| "Token has expired"             | The token's exp claim is in the past.                                                                                                                                                                                                                | Obtain a fresh access token from your IdP.                                                                                                                                                                                                                                                                                                         |           |                                                                 |
| "Invalid token claims"          | iss or aud in the token does not match OIDC\_ISSUER or OIDC\_AUDIENCE.                                                                                                                                                                               | Decode your token with echo $TOKEN \| cut -d'.' -f2                                                                                                                                                                                                                                                                                                | base64 -d | jq . and compare the claims against your environment variables. |
| "Unknown signing key"           | A token arrived with a kid (key ID) not present in the cached JWKS.                                                                                                                                                                                  | Agent Memory re-fetches the JWKS once on encountering an unknown kid. If the issue persists, the IdP may have rotated key material while reusing the same kid — a rotation pattern Agent Memory cannot detect automatically. Restart Agent Memory to force a fresh JWKS fetch.                                                                     |           |                                                                 |
| "ID tokens are not accepted"    | An ID token was used instead of an access token.                                                                                                                                                                                                     | Use the access\_token field from the /token response, not id\_token.                                                                                                                                                                                                                                                                               |           |                                                                 |

## [](#next-steps)Next Steps

* [Deploy Agent Memory for Production](deploy-agent-mem-prod.md)
* [Agent Memory Environment Variable Reference](config-agent-mem-env.md)
* [Develop with the Agent Memory SDK](develop-agent-mem.md)