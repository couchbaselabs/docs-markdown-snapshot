---
title: Managing Connections
description: This section describes how to connect the .NET Analytics SDK to an
  Analytics cluster.
editUrl: https://github.com/couchbase/docs-analytics-sdk-dotnet/edit/release/1.1/modules/howtos/pages/managing-connections.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:dotnet-analytics-sdk:howtos:managing-connections.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/dotnet-analytics-sdk/current/howtos/managing-connections.html)

# Managing Connections

> This section describes how to connect the .NET Analytics SDK to an Analytics cluster. It contains best practices as well as information on TLS/SSL and advanced connection options, and a sub-page on troubleshooting remote connections during devlopment. 

Our [Getting Started pages](../hello-world/start-using-sdk.md) cover the basics of making a connection to an Enterprise Analytics cluster. This page is a wider look at the topic.

## [](#connecting-to-a-cluster)Connecting to a Cluster

The examples below use these imports:

```csharp
using Couchbase.AnalyticsClient;
using Couchbase.AnalyticsClient.HTTP;
using Couchbase.AnalyticsClient.Options;
```

A connection to an Enterprise Analytics cluster is represented by a `Cluster` object. A `Cluster` provides access to databases, scopes, and collections, as well as various Analytics services and management interfaces. The simplest way to create a `Cluster` object is to call `Cluster.Create()` with a [connection string](#connection-strings), username, and password:

```csharp
var credential = Credential.Create("username", "password");
public static Cluster Create(string connectionString, ICredential credential);
```

## [](#connection-strings)Connection Strings

Typically, an Enterprise Analytics cluster will be behind a load balancer, and you will be making a connection over TLS — so the port used will be `443`. This is the defaut for the SDK, so port `443` does not need to be specified:

https://analytics.example.com

You must specify the schema — either `https://` (for TLS) or `http://` (for insecure connections — perhaps on a development machine) in the connection string. The default port for insecure connections is port `80`.

If you're connecting to a cluster directly, without a load balancer, you can specify the port in the connection string:

https://analytics.example.com:18095

For a standalone Analytics cluster, the port is usually `18095` (or `8095` for an insecure connection). Make sure to check with your administrator.

### [](#client-settings-parameters)Client Settings Parameters

Connection strings can also include client settings, which will override any that are also set in the code.

Connection string with two parameters

https://analytics.example.com?timeout.connect_timeout=30s&timeout.query_timeout=2m

The full list of recognized parameters is documented in the [client settings reference](../ref/client-settings.md).

## [](#authentication-by-credential)Authentication by Credential

Similarly to the `Authenticator` abstraction in Couchbase Operational SDKs, Analytics SDKs use a `Credential` abstraction covering regular password authentication (Basic Access Authentication), JSON Web Tokens (JWT), and Client Certificates through mTLS.

Basic Access Authentication is shown in the example [above](#connecting-to-a-cluster).

### [](#json-web-tokens-jwt)JSON Web Tokens (JWT)

From the 1.1 SDK (with Enterprise Analytics Server 2.2+) JWT is supported.

```csharp
var credential = JwtCredential.Create(token);
public static Cluster Create(string connectionString, ICredential credential);
```

### [](#certificate-authentication)Certificate Authentication

From the 1.1 Analytics SDK (with Enterprise Analytics Server 2.2+) certificate authentication is supported. A conceptual and architectural overview of Enterprise Analytics's support of X.509 certificates is provided in the [Server certificates docs](../../../server/current/learn/security/certificates.md). Practical information on handling certificates can be found in the [Enterprise Analytics certificates docs](../../../enterprise-analytics/current/manage/manage-security/manage-certificates.md).

The Analytics SDK authenticates the client during the TLS handshake. The SDK reads the certificate and private key from a `PKCS#12` file:

```csharp
var credential = CertificateCredential.FromPem(certPath, keyPath);
public static Cluster Create(string connectionString, ICredential credential);
```

Typically, JWTs have a short validity period. Renew JWTs with `Cluster.UpdateCredential(ICredential newCredential)`.

## [](#certificate-authority)Certificate Authority

To make a TLS connection to an Enterprise Analytics cluster with a root certificate issued by a trusted CA (Certificate Authority), you do not need to add this to your configuration — the platform's defaults are automatically trusted.

The cluster's root certificate just needs to be issued by a CA whose certificate is in your system trust store. This includes well known CAs (including GoDaddy and Verisign), plus any other CA certificates that you wish to add.

## [](#local-development)Local Development

We strongly recommend that the client and server [are in the same LAN-like environment](../project-docs/compatibility.md#network-requirements) (for example, the same AWS Region).