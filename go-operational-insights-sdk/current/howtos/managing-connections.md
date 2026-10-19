---
title: Managing Connections
description: This section describes how to connect the Go Operational Insights
  SDK to an Operational Insights cluster.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Go Operational Insights SDK
    version: "1.0"
antora:
  editUrl: https://github.com/couchbase/docs-operational-insights-sdk-go/edit/release/1.0/modules/howtos/pages/managing-connections.adoc
  xref: xref:go-operational-insights-sdk:howtos:managing-connections.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/go-operational-insights-sdk/current/howtos/managing-connections.html)

# Managing Connections

> This section describes how to connect the Go Operational Insights SDK to an Operational Insights cluster. It contains best practices as well as information on TLS/SSL and advanced connection options. 

Our [Getting Started pages](../hello-world/start-using-sdk.md) cover the basics of making a connection to an Operational Insights cluster. This page is a wider look at the topic.

## [](#connecting-to-a-cluster)Connecting to a Cluster

A connection to an Operational Insights cluster is represented by a `Cluster` object. A `Cluster` provides access to Buckets and Scopes, as well as various Couchbase services and management interfaces. The simplest way to create a `Cluster` object is to call `cbinsights.Connect()` with a [connection string](#connection-strings), username, and password:

```golang
	cluster, err := cbinsights.NewCluster(
		connStr,
		cbinsights.NewBasicAuthCredential(username, password),
		// The third parameter is optional.
		// This example sets the default server query timeout to 3 minutes,
		// that is the timeout value sent to the query server.
		cbinsights.NewClusterOptions().SetTimeoutOptions(
			cbinsights.NewTimeoutOptions().SetQueryTimeout(3*time.Minute),
		),
	)
	handleErr(err)
```

## [](#connection-strings)Connection Strings

Typically, an Operational Insights Enterprise cluster will be behind a load balancer, and you will be making a connection over TLS — so the port used will be `443`. This is the defaut for the SDK, so port `443` does not need to be specified: `<https://insights.example.com>`.

You must specify the schema — either `https://` (for TLS) or `http://` (for insecure connections — perhaps on a development machine) in the connection string. The default port for insecure connections is port `80`.

If you're connecting to a cluster directly, without a load balancer, you can specify the port in the connection string: `<https://insights.example.com:18095>`. For a standalone Operational Insights cluster, the port is usually `18095` (or `8095` for an insecure connection). Make sure to check with your administrator.

### [](#client-settings-parameters)Client Settings Parameters

Connection strings can also include client settings, which will override any that are also set in the code.

Connection string with two parameters

https://insights.example.com?timeout.connect_timeout=30s&timeout.query_timeout=2m

The full list of recognized parameters is documented in the [client settings reference](../ref/client-settings.md).

## [](#authentication-by-credential)Authentication by Credential

Similarly to the `Authenticator` abstraction in Couchbase Operational SDKs, Operational Insights SDKs use a `Credential` abstraction covering regular password authentication (Basic Access Authentication), JSON Web Tokens (JWT), and Client Certificates through mTLS.

Basic Access Authentication is shown in the example [above](#connecting-to-a-cluster).

### [](#json-web-tokens-jwt)JSON Web Tokens (JWT)

JWT is supported from OI Server 2.2+.

```go
var credential = JwtCredential.Create(token);
public static Cluster Create(string connectionString, ICredential credential);
```

Typically, JWTs have a short validity period. Renew JWTs with `SetCredential(newCredential)`.

### [](#certificate-authentication)Certificate Authentication

Certificate authentication is supported with Operational Insights Server 2.2+. A conceptual and architectural overview of Operational Insights's support of X.509 certificates is provided in the [Server certificates docs](../../../server/current/learn/security/certificates.md). Practical information on handling certificates can be found in the [Operational Insights certificates docs](../../../operational-insights/current/manage/manage-security/manage-certificates.md).

The Insights SDK authenticates the client during the TLS handshake. The SDK reads the certificate and private key from a `PKCS#12` file:

```go
	opts := gocb.ClusterOptions{
		Authenticator: gocb.CertificateAuthenticator{
			ClientCertificate: &cert,
		},
	}
	cluster, err := gocb.Connect("couchbases://--your-ip--", opts)
	if err != nil {
		panic(err)
	}
```

## [](#certificate-authority)Certificate Authority

To make a TLS connection to an Operational Insights cluster with a root certificate issued by a trusted CA (Certificate Authority), you do not need to add this to your configuration — the platform's defaults are automatically trusted.

The cluster's root certificate just needs to be issued by a CA whose certificate is in your system trust store. This includes well known CAs (including GoDaddy and Verisign), plus any other CA certificates that you wish to add.

## [](#local-development)Local Development

We strongly recommend that the client and server [are in the same LAN-like environment](../project-docs/compatibility.md#network-requirements) (e.g. AWS Region).