---
title: Authentication
description: Couchbase Edge Server supports multiple authentication mechanisms
  to control client access to the REST API and sync connections.
editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-edge-server/edit/release/1.0/modules/configuration/pages/authentication.adoc
pubDate: 2026-04-15T05:26:28.652Z
link: xref:couchbase-edge-server:configuration:authentication.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-edge-server/current/configuration/authentication.html)

# Authentication

> Couchbase Edge Server supports multiple authentication mechanisms to control client access to the REST API and sync connections. 

## [](#overview)Overview

By default, all HTTP requests to Couchbase Edge Server require authentication. Couchbase Edge Server supports two independent authentication mechanisms:

* **Basic authentication** — Set username and password credentials in users files.
* **Mutual TLS (mTLS)** — client certificate authentication.

Both mechanisms can be active simultaneously. A client may authenticate using either.

> [!NOTE]
> Authentication governs access to the REST API and client sync connections. Replication connections to a remote server use separate credentials configured in the `replications` block of the configuration file. See [Manage Replication with Edge Server](../rest-based-access/replication.md) for details.

## [](#anonymous-access)Anonymous Access

Setting `enable_anonymous_users: true` in the configuration file allows unauthenticated requests from any client.

> [!CAUTION]
> If you followed the [Get Started](../get-started/install.md) guide, your configuration uses `enable_anonymous_users: true`. This is suitable for development and testing only. Disable anonymous access and configure an authentication mechanism before deploying to production.

```json5
{
  enable_anonymous_users: true
}
```

## [](#basic-auth)Basic Authentication

Basic authentication uses username and password credentials. You store credentials in a JSON users file and set the path using the top-level `users` property in the configuration file.

```json5
{
  users: "/etc/edge-server/users.json"
}
```

### [](#users-file)Users File

The users file is a JSON object where each key is a username and each value describes that user's credentials and roles. Store passwords as [bcrypt](https://en.wikipedia.org/wiki/Bcrypt) hashes, not plaintext.

```json
{
  "alice": {
    "password": "$2y$05$...",
    "roles": ["admin"]
  },
  "bob": {
    "password": "$2y$05$...",
    "roles": ["replicate"]
  }
}
```

The server reads the users file at startup. You must restart the server for changes to take effect.

For instructions on creating users files and adding users, see [Usernames and Passwords](../rest-based-access/rest-api-start.md#usernames-and-passwords).

> [!WARNING]
> Never use basic authentication without TLS. Without TLS, attackers can capture passwords as cleartext using packet sniffers.

### [](#user-roles)User Roles

Roles grant additional privileges to a user account. A user without a role can authenticate and view the REST API but cannot manage replications.

| Role      | Privileges                                                                        |
| --------- | --------------------------------------------------------------------------------- |
| replicate | Allows access to /\_replicate to start, stop, and monitor replications.           |
| admin     | Grants full administrative access, including all privileges granted by replicate. |

## [](#mtls)Mutual TLS

Mutual TLS (mTLS) requires clients to present a certificate during the TLS handshake. Couchbase Edge Server verifies that a configured Certificate Authority (CA) signs the certificate.

When you set `client_cert_path` in the `https` block of the configuration file, all clients must connect using TLS client certificates. The server only accepts certificates signed by the configured CA.

> [!NOTE]
> The server records the Common Name (`CN`) field of the client certificate in server logs for identification purposes only. The server does not match it against entries in the `users` file, and you do not need to create a corresponding entry in the users file for mTLS clients.

For instructions on configuring mTLS, see [Client Certificate Authentication](../rest-based-access/rest-api-start.md#client-cert-authentication-mtls).

### [](#using-basic-auth-and-mtls-together)Using Basic Auth and mTLS Together

Basic auth and mTLS are independent mechanisms and can be active simultaneously. When you configure both, a client may authenticate using either a valid client certificate or username and password credentials.

## [](#server-tls)Server TLS

Server TLS encrypts the connection between client and server but does not authenticate the client. It's separate from mTLS; enable it alongside whichever client authentication mechanism you use.

```json5
{
  https: {
    tls_cert_path: "./cert.pem",
    tls_key_path: "private.key"
  }
}
```

For instructions on enabling server TLS and creating a certificate, see [Server Authentication with TLS](../rest-based-access/rest-api-start.md#server-auth-with-tls).

## [](#see-also)See Also

* [Edge Server Configuration](edge-server-configuration.md)
* [Get Started with the Edge Server REST API](../rest-based-access/rest-api-start.md)
* [Manage Replication with Edge Server](../rest-based-access/replication.md)