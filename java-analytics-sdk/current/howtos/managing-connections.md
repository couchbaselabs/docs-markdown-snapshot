---
title: Managing Connections
description: This section describes how to connect the Java Analytics SDK to an
  Analytics cluster.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-analytics-sdk-java/edit/release/1.1/modules/howtos/pages/managing-connections.adoc
  xref: xref:java-analytics-sdk:howtos:managing-connections.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/java-analytics-sdk/current/howtos/managing-connections.html)

# Managing Connections

> This section describes how to connect the Java Analytics SDK to an Analytics cluster. It contains best practices as well as information on TLS/SSL and advanced connection options. 

Our [Getting Started pages](../hello-world/start-using-sdk.md) cover the basics of making a connection to an Enterprise Analytics cluster. This page is a wider look at the topic.

## [](#connecting-to-a-cluster)Connecting to a Cluster

The examples below use these imports:

```java
import com.couchbase.analytics.client.java.Cluster;
import com.couchbase.analytics.client.java.Credential;
import com.couchbase.analytics.client.java.QueryResult;
```

A connection to an Enterprise Analytics cluster is represented by a `Cluster` object. A `Cluster` provides access to databases, scopes, and collections, as well as various Analytics services and management interfaces. The simplest way to create a `Cluster` object is to call `Cluster.newInstance()` with a [connection string](#connection-strings), username, and password:

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

```java
var credential = Credential.ofJwt("...");
var cluster = Cluster.newInstance(connectionString, credential);
```

Typically, JWTs have a short validity period. Renew JWTs with `cluster.credential(freshJwtCredential)`

### [](#certificate-authentication)Certificate Authentication

From the 1.1 Analytics SDK (with Enterprise Analytics Server 2.2+) certificate authentication is supported. A conceptual and architectural overview of Enterprise Analytics's support of X.509 certificates is provided in the [Server certificates docs](../../../server/current/learn/security/certificates.md). Practical information on handling certificates can be found in the [Enterprise Analytics certificates docs](../../../enterprise-analytics/current/manage/manage-security/manage-certificates.md).

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