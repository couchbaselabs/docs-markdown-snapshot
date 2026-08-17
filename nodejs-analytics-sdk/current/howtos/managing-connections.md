---
title: Managing Connections
description: This section describes how to connect the Node.js Analytics SDK to
  an Enterprise Analytics cluster.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-analytics-sdk-nodejs/edit/release/1.1/modules/howtos/pages/managing-connections.adoc
  xref: xref:nodejs-analytics-sdk:howtos:managing-connections.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/nodejs-analytics-sdk/current/howtos/managing-connections.html)

# Managing Connections

> This section describes how to connect the Node.js Analytics SDK to an Enterprise Analytics cluster. It contains best practices as well as information on TLS/SSL and advanced connection options. 

Our [Getting Started pages](../hello-world/start-using-sdk.md) cover the basics of making a connection to an Enterprise Analytics cluster. This page is a wider look at the topic.

## [](#connecting-to-a-cluster)Connecting to a Cluster

A connection to an Analytics cluster is represented by an `analytics` object. Connect to Enterprise Analytics by calling `analytics.createInstance` with the connection string, credentials, and any required optional parameters.

```javascript
const analytics = require('couchbase-analytics')

async function main() {
    // Update this to your cluster
    const clusterConnStr = 'https://<your_hostname>:<PORT>'
    const username = 'username'
    const password = 'Password123!'
    // User Input ends here.

    const credential = new analytics.Credential(username, password)
    const cluster = analytics.createInstance(clusterConnStr, credential)
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

```javascript
async function main() {
    const _EXAMPLE_JWT = 'eyJhbGbiOiJSUzI1NiIsInR5cCI6IkpXVCJ9.payload.signature'
    const endpoint = 'https://--your-instance--'
    const credential = new JwtCredential(_EXAMPLE_JWT)
    const cluster = createInstance(endpoint, credential)
```

# [](#certificate-authority)Certificate Authority

To make a TLS connection to an Enterprise Analytics cluster with a root certificate issued by a trusted CA (Certificate Authority), you do not need to add this to your configuration — the platform's defaults are automatically trusted.

The cluster's root certificate just needs to be issued by a CA whose certificate is in your system trust store. This includes well known CAs (including GoDaddy and Verisign), plus any other CA certificates that you wish to add.

### [](#certificate-authentication)Certificate Authentication

From the 1.1 Analytics SDK (with Enterprise Analytics Server 2.2+) certificate authentication is supported. A conceptual and architectural overview of Enterprise Analytics's support of X.509 certificates is provided in the [Server certificates docs](../../../server/current/learn/security/certificates.md). Practical information on handling certificates can be found in the [Enterprise Analytics certificates docs](../../../enterprise-analytics/current/manage/manage-security/manage-certificates.md).

The Analytics SDK authenticates the client during the TLS handshake. The SDK reads the certificate and private key from a `PKCS#12` file:

```javascript
  const clusterConnStr = 'https://--your-instance--'
  const cert = fs.ReadFileSync('/path/to/client/certificate.pem')
  const key = fs.ReadFileSync('/path/to/client/key.pem')
  const credential = new CertificateCredential({
    cert: cert,
    key: key
  })

  const cluster = createInstance(clusterConnStr, credential)
```

## [](#local-development)Local Development

We strongly recommend that the client and server [are in the same LAN-like environment](../project-docs/compatibility.md#network-requirements) (e.g. AWS Region).