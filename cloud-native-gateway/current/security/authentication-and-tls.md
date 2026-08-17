---
title: Authentication and TLS
description: How Cloud Native Gateway authenticates client requests using
  credentials, TLS client certificates, and On-Behalf-Of semantics, and how TLS
  secures all communication.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-cloud-native-gateway/edit/release/1.2/modules/security/pages/authentication-and-tls.adoc
  xref: xref:cloud-native-gateway:security:authentication-and-tls.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud-native-gateway/current/security/authentication-and-tls.html)

# Authentication and TLS

> How Cloud Native Gateway authenticates client requests using credentials, TLS client certificates, and On-Behalf-Of semantics, and how TLS secures all communication. 

## [](#authentication-methods)Authentication Methods

Cloud Native Gateway authenticates every request and does not permit anonymous access. It validates credentials per-request to align with Protostellar's stateless nature.

### [](#username-and-password-authentication)Username and Password Authentication

This method is the most common authentication approach in which clients send credentials with every request.

For gRPC (Protostellar) requests, clients include credentials in the gRPC metadata as an Authorization header that uses the HTTP Basic scheme:Authorization: Basic <base64(username:password)>.

For Data API (HTTPS) requests, clients include credentials in the standard HTTP Authorization header by using the Basic or Bearer schemes.

Cloud Native Gateway validates credentials against the Couchbase cluster's internal authentication system. Any users configured in Couchbase Server, including local and LDAP‑backed users, can authenticate through Cloud Native Gateway. The following example shows a Data API request that uses HTTP Basic authentication:

```console
$ curl -u myuser:mypassword https://cng.example.com:18099/v1/callerIdentity
```

### [](#tls-client-certificate-authentication)TLS Client Certificate Authentication

Cloud Native Gateway supports mutual TLS (mTLS), where the client presents a TLS certificate during the TLS handshake. When you enable mTLS:

1. You configure Cloud Native Gateway with a trusted client CA certificate by using the `--client-ca` flag or an equivalent operator setting.
2. Cloud Native Gateway configures TLS with `VerifyClientCertIfGiven` to validate client certificates against the configured CA. Clients that do not present a certificate can still authenticate by using a username and password.
3. When a client presents a valid certificate, Cloud Native Gateway extracts the identity from the certificate. It then validates that identity by using Couchbase Server certificate authentication.

Client certificate authentication is essential for:

* Service-to-service communication where managing passwords is undesirable.
* Environments that require certificate-based identity such as mTLS service meshes.

> [!NOTE]
> You can use client certificate authentication and username/password authentication simultaneously on the same Cloud Native Gateway instance. Cloud Native Gateway performs `Authorization` header authentication even when a client presents a certificate.

## [](#tls-architecture)TLS Architecture

All communication to and from Cloud Native Gateway is TLS-encrypted.

### [](#client-to-cloud-native-gateway-tls)Client-to-Cloud Native Gateway TLS

* Both the Protostellar (gRPC) and Data API (HTTPS) interfaces require TLS.
* Cloud Native Gateway serves with a configurable TLS certificate (see [Cluster Level Configuration](../configuration-management/cluster-level-configuration.md)).
* Go's `crypto/tls` defaults determine the minimum TLS version and cipher suites, which follow current best practices and turn off known-weak algorithms.
* Cloud Native Gateway rotates its certificate dynamically — you can update the certificate without restarting the process.

### [](#cloud-native-gateway-to-cluster-tls)Cloud Native Gateway-to-Cluster TLS

* When connecting to a TLS-enabled Couchbase cluster (`couchbases://`), Cloud Native Gateway validates the cluster's certificate against the configured cluster CA.
* KV connections use TLS with the Memcached binary protocol.
* HTTP connections such as Query, Search, Analytics, Management use standard HTTPS.
* For production deployments, Couchbase recommends TLS between Cloud Native Gateway and the cluster.

### [](#end-to-end-encryption)End-to-End Encryption

In a properly configured deployment, traffic is encrypted at every hop:

```none
Client --[TLS/gRPC]--> CNG --[TLS/memcached]--> KV Node
Client --[TLS/gRPC]--> CNG --[TLS/HTTPS]------> Query Node
Client --[TLS/HTTPS]-> CNG --[TLS/HTTPS]------> Search Node
```

## [](#single-user-authentication-mode)Single-User Authentication Mode

Cloud Native Gateway can operate in single-user mode (`--single-user-auth`) for development and testing. All requests authenticate using a single configured username and password without validating with Couchbase Server.

This mode is **not recommended for production** because:

* Cloud Native Gateway does not enforce per-user RBAC, as all requests share the same identity.
* Cloud Native Gateway does not integrate with Couchbase Server user management.

Single-user mode is useful for local development, automated testing, and environments where Couchbase Server auth passthrough is not available.