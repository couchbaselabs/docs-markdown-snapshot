---
title: Configure JWT Authentication
description: Enterprise Analytics supports JSON Web Token (JWT) authentication,
  allowing clients to authenticate using bearer tokens issued by a trusted
  Identity Provider instead of a username and password.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/manage/pages/manage-security/configure-jwt.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:enterprise-analytics:manage:manage-security/configure-jwt.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/manage/manage-security/configure-jwt.html)

# Configure JWT Authentication

> Enterprise Analytics supports JSON Web Token (JWT) authentication, allowing clients to authenticate using bearer tokens issued by a trusted Identity Provider instead of a username and password. 

## [](#prerequisites)Prerequisites

To use JWT authentication with Enterprise Analytics, you need:

Identity Provider (IdP)

The trusted server that verifies a user's credentials and issues a signed JWT. Any OpenID Connect-compatible identity provider can serve as the IdP. For setup instructions, see the documentation for your IdP — for example, [Keycloak](https://www.keycloak.org/docs/latest/server%5Fadmin/) or [Okta](https://developer.okta.com/docs/guides/).

JSON Web Token (JWT)

A self-contained, signed token with three parts: a header, a payload containing user claims, and a cryptographic signature. The signature proves the token has not been tampered with.

Enterprise Analytics as Resource Server

Enterprise Analytics does not store user passwords. Instead, it receives a JWT, verifies its signature against the IdP public keys using JWKS, examines the claims to determine identity and permissions, and then enforces authorization.

Before you begin, also confirm:

* Your IdP issues JWT tokens and has a publicly accessible JWKS URI.
* You have the JWKS URI, the issuer name (the `iss` claim value), the signing algorithm, and the audience values from your IdP.
* You're running Enterprise Analytics 2.2 or later.
* You have administrator credentials for Enterprise Analytics. For more information about how to configure credentials, see [Manage Users, Groups, and Roles](manage-users-and-roles.md).

## [](#configure-jwt-authentication)Configure JWT Authentication

Use the REST API to enable JWT authentication, register your IdP, and optionally enable bearer token support for SDK clients.

### [](#step-1-enable-jwt-and-register-your-idp)Step 1: Enable JWT and Register Your IdP

Use `PUT /settings/jwt` to enable JWT authentication and register your IdP as a trusted issuer.

```bash
curl -sv -X PUT http://localhost:8091/settings/jwt \
  -H 'Content-Type: application/json' \
  -u $ADMIN_USERNAME:$ADMIN_PASSWORD \
  -d '{
    "enabled": true,
    "issuers": [{
      "name": "https://your-idp.example.com/realms/cb",
      "signingAlgorithm": "RS256",
      "subClaim": "preferred_username",
      "audClaim": "azp",
      "audienceHandling": "any",
      "audiences": ["your-client-id"],
      "publicKeySource": "jwks_uri",
      "jwksUri": "https://your-idp.example.com/realms/cb/protocol/openid-connect/certs",
      "jwksUriTlsVerifyPeer": true
    }]
  }'
```

The key parameters in the `issuers` object are:

| Parameter            | Description                                                                                                                                                  |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| name                 | The value of the iss (issuer) claim in the JWT. The value must match the issuer field in tokens from your IdP.                                               |
| signingAlgorithm     | The algorithm the IdP uses to sign tokens — for example, RS256 or RS384. Check your IdP JWKS or OpenID configuration endpoint.                               |
| subClaim             | The JWT claim that contains the username. preferred\_username is a common value. See your IdP token payload for the correct field.                           |
| audClaim             | The JWT claim that holds the audience value — typically aud or azp.                                                                                          |
| audiences            | The list of accepted audience values. Enterprise Analytics rejects tokens whose audience does not match.                                                     |
| jwksUri              | The URI where Enterprise Analytics fetches the IdP public keys to verify token signatures. Find this in your IdP /.well-known/openid-configuration endpoint. |
| jwksUriTlsVerifyPeer | Set to true to verify the TLS certificate of the JWKS URI. Recommended for production.                                                                       |

To read the configuration back and confirm it was applied:

```bash
curl -sv -X GET http://localhost:8091/settings/jwt \
  -H 'Content-Type: application/json' \
  -u $ADMIN_USERNAME:$ADMIN_PASSWORD
```

### [](#step-2-enable-bearer-token-support-for-sdk-clients-optional)Step 2: Enable Bearer Token Support for SDK Clients (Optional)

To allow Couchbase SDK clients to authenticate using JWT bearer tokens, enable `oauthBearerEnabled` on the security settings endpoint.

```bash
curl -sv -X POST http://localhost:8091/settings/security \
  -u $ADMIN_USERNAME:$ADMIN_PASSWORD \
  -d 'oauthBearerEnabled=true'
```

> [!NOTE]
> This setting is only required for SDK-based use. REST API authentication with JWT bearer tokens works without this setting.

### [](#step-3-authorize-jwt-users-in-rbac)Step 3: Authorize JWT Users in RBAC

For each JWT-authenticated user, create an entry in the external authentication domain and assign their roles.

```bash
curl -sv -X PUT http://localhost:8091/settings/rbac/users/external/$USERNAME \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -u $ADMIN_USERNAME:$ADMIN_PASSWORD \
  --data-urlencode "name=$DISPLAY_NAME" \
  --data-urlencode "roles=$ROLES"
```

Replace `$USERNAME` with the value that appears in the `subClaim` field of the JWT, and `$ROLES` with a comma-separated list of Couchbase roles — for example, `analytics_access`.

Once the user exists in RBAC, clients can authenticate REST API calls by passing the JWT as a bearer token:

```bash
curl -sv http://localhost:8091/pools/default \
  -H "Authorization: Bearer $ACCESS_TOKEN"
```

## [](#see-also)See Also

* [Manage Authentication](manage-authentication.md)
* [Manage Users, Groups, and Roles](manage-users-and-roles.md)
* [Role Based Access Control (RBAC)](rbac-overview.md)
* [Security Management Overview](security-management-overview.md)