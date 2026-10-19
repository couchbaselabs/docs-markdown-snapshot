---
title: Managing Connections
description: This section describes how to connect the Java Operational Insights
  SDK to an Operational Insights cluster.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Java Operational Insights SDK
    version: "1.0"
antora:
  editUrl: https://github.com/couchbase/docs-operational-insights-sdk-java/edit/release/1.0/modules/howtos/pages/managing-connections.adoc
  xref: xref:java-operational-insights-sdk:howtos:managing-connections.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/java-operational-insights-sdk/current/howtos/managing-connections.html)

# Managing Connections

> This section describes how to connect the Java Operational Insights SDK to an Operational Insights cluster. It contains best practices as well as information on TLS/SSL and advanced connection options. 

Our [Getting Started pages](../hello-world/start-using-sdk.md) cover the basics of making a connection to an Operational Insights cluster. This page is a wider look at the topic.

## [](#connecting-to-a-cluster)Connecting to a Cluster

The examples below use these imports:

```java
import com.couchbase.insights.client.java.Cluster;
import com.couchbase.insights.client.java.Credential;
import com.couchbase.insights.client.java.QueryResult;
```

A connection to an Operational Insights cluster is represented by a `Cluster` object. A `Cluster` provides access to databases, scopes, and collections, as well as various Insights services and management interfaces. The simplest way to create a `Cluster` object is to call `Cluster.newInstance()` with a [connection string](#connection-strings), username, and password:

```java
public class Example {
  public static void main(String[] args) {
    var connectionString = "https://192.168.5.5:18095";
    var username = "...";
    var password = "...";

    try (Cluster cluster = Cluster.newInstance(
      connectionString,
      Credential.of(username, password)
    )) {
        // Interact with the cluster here
    }
  }
}
```

> [!WARNING]
> The above example uses a `try-with-resources` block to ensure the `Cluster` instance gets closed at the end. It's important to either use a `try-with-resources` block, or make sure to call `cluster.close()` when you're done with the cluster.

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

Similarly to the `Authenticator` abstraction in Couchbase Operational SDKs, Analytics SDKs use a `Credential` abstraction covering regular password authentication (Basic Access Authentication), JSON Web Tokens (JWT), and Client Certificates through mTLS.

Basic Access Authentication is shown in the example [above](#connecting-to-a-cluster).

### [](#json-web-tokens-jwt)JSON Web Tokens (JWT)

JWT is supported with Operational Insights Server 2.2+.

```java
var credential = Credential.ofJwt("...");
var cluster = Cluster.newInstance(connectionString, credential);
```

Typically, JWTs have a short validity period. Renew JWTs with `cluster.credential(freshJwtCredential)`

### [](#certificate-authentication)Certificate Authentication

Certificate authentication is supported with Operational Insights Server 2.2+. A conceptual and architectural overview of Enterprise Analytics's support of X.509 certificates is provided in the [Server certificates docs](../../../server/current/learn/security/certificates.md). Practical information on handling certificates can be found in the [Enterprise Analytics certificates docs](../../../operational-insights/current/manage/manage-security/manage-certificates.md).

The Analytics SDK authenticates the client during the TLS handshake. The SDK reads the certificate and private key from a `PKCS#12` file:

```java
var credential = Credential.fromKeyStore(
    Paths.get("path/to/client-cert-and-key.p12"),
    password
);
var cluster = Cluster.newInstance(connectionString, credential);
```

## [](#certificate-authority)Certificate Authority

By default, the Analytics SDK trusts the same well-known Certificate Authorities (CAs) as the JVM, plus the Couchbase Capella CA. This works for most deployments.

If you need to trust a different CA, or want to trust only a specific CA, you can override the default trust settings by telling the Analytics SDK which CA certificates to trust.

```java
var cluster = Cluster.newInstance(
  connectionString,
  credential,
  options -> options
    .security(sec -> sec.trustOnlyPemFile(Paths.get("path/to/ca.pem")))
);
```

## [](#local-development)Local Development

We strongly recommend that the client and server [are in the same LAN-like environment](../project-docs/compatibility.md#network-requirements) (e.g. AWS Region).