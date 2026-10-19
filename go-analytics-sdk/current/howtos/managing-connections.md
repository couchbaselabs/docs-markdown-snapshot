---
title: Managing Connections
description: This section describes how to connect the Go Analytics SDK to an
  Operational Insights cluster.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Go Analytics SDK
    version: "1.1"
antora:
  editUrl: https://github.com/couchbase/docs-analytics-sdk-go/edit/release/1.1/modules/howtos/pages/managing-connections.adoc
  xref: xref:go-analytics-sdk:howtos:managing-connections.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/go-analytics-sdk/current/howtos/managing-connections.html)

# Managing Connections

> This section describes how to connect the Go Analytics SDK to an Operational Insights cluster. It contains best practices as well as information on TLS/SSL and advanced connection options. 

Our [Getting Started pages](../hello-world/start-using-sdk.md) cover the basics of making a connection to an Operational Insights cluster. This page is a wider look at the topic.

## [](#connecting-to-a-cluster)Connecting to a Cluster

A connection to an Operational Insights cluster is represented by a `Cluster` object. A `Cluster` provides access to Buckets and Scopes, as well as various Couchbase services and management interfaces. The simplest way to create a `Cluster` object is to call `cbanalytics.Connect()` with a [connection string](#connection-strings), username, and password:

```golang
cred := cbanalytics.NewBasicAuthCredential(username, password)
cluster, err := cbanalytics.NewCluster(endpoint, cred)
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

JWT is supported with Operational Insights Server `2.2+`.

```go
cred := cbanalytics.NewJwtCredential(yourJWTtoken)
cluster, err := cbanalytics.NewCluster(endpoint, cred)
```

Typically, JWTs have a short validity period. Renew JWTs with `SetCredential(newCredential)`.

### [](#certificate-authentication)Certificate Authentication

Certificate authentication is supported with Operational Insights Server `2.2+`. A conceptual and architectural overview of Operational Insights's support of X.509 certificates is provided in the [Server certificates docs](../../../server/current/learn/security/certificates.md). Practical information on handling certificates can be found in the [Operational Insights certificates docs](../../../operational-insights/2.2/manage/manage-security/manage-certificates.md).

The Analytics SDK authenticates the client during the TLS handshake. The SDK reads the certificate and private key from a `PKCS#12` file:

```go
cert, err := tls.LoadX509KeyPair("path/to/cert.pem", "path/to/key.pem")
if err != nil {
	handleErr(err)
}
cred := cbanalytics.NewCertificateCredential(&cert)
cluster, err := cbanalytics.NewCluster(endpoint, cred)
```

## [](#certificate-authority)Certificate Authority

To make a TLS connection to an Operational Insights cluster with a root certificate issued by a trusted CA (Certificate Authority), you do not need to add this to your configuration — the platform's defaults are automatically trusted.

The cluster's root certificate just needs to be issued by a CA whose certificate is in your system trust store. This includes well known CAs (including GoDaddy and Verisign), plus any other CA certificates that you wish to add.

## [](#local-development)Local Development

We strongly recommend that the client and server [are in the same LAN-like environment](../project-docs/compatibility.md#network-requirements) (e.g. AWS Region).