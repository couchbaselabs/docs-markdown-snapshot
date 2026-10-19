---
title: Managing Connections
description: This section describes how to connect the Python Operational
  Insights SDK to an Operational Insights cluster.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Python Operational Insights SDK
    version: "1.0"
antora:
  editUrl: https://github.com/couchbase/docs-operational-insights-sdk-python/edit/release/1.0/modules/howtos/pages/managing-connections.adoc
  xref: xref:python-operational-insights-sdk:howtos:managing-connections.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-operational-insights-sdk/current/howtos/managing-connections.html)

# Managing Connections

> This section describes how to connect the Python Operational Insights SDK to an Operational Insights cluster. It contains best practices as well as information on TLS/SSL and advanced connection options. 

Our [Getting Started pages](../hello-world/start-using-sdk.md) cover the basics of making a connection to an Operational Insights cluster. This page is a wider look at the topic.

## [](#connecting-to-a-cluster)Connecting to a Cluster

The examples below use these imports:

```python
from couchbase_operational_insights.cluster import Cluster
from couchbase_operational_insights.credential import Credential
from couchbase_operational_insights.options import (ClusterOptions,
                                        SecurityOptions)
```

A connection to an Enterprise Analytics cluster is represented by a `Cluster` object. The simplest way to create a `Cluster` object is to call `Cluster.createnstance()` with a [connection string](#connection-strings), user credentials, and any optional settings:

```python
def main() -> None:
    # Update this to your cluster
    connstr = 'https://--your-instance--'
    username = 'username'
    pw = 'Password!123'
    # User Input ends here.

    cred = Credential.from_username_and_password(username, pw)
    cluster = Cluster.create_instance(connstr, cred, opts)
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

```python
def main() -> None:
    _EXAMPLE_JWT = 'eyJhbGbiOiJSUzI1NiIsInR5cCI6IkpXVCJ9.payload.signature'
    endpoint = 'https://--your-instance--'
    cred = Credential.from_jwt(_EXAMPLE_JWT)
    cluster = Cluster.create_instance(endpoint, cred)
```

### [](#certificate-authentication)Certificate Authentication

Certificate authentication is supported with Operational Insights Server 2.2+. A conceptual and architectural overview of Operational Insights's support of X.509 certificates is provided in the [Server certificates docs](../../../server/current/learn/security/certificates.md). Practical information on handling certificates can be found in the [Operational Insights certificates docs](#3.0@operational-insights:manage:manage-security/manage-certificates.adoc).

The Insights SDK authenticates the client during the TLS handshake. The SDK reads the certificate and private key from a `PKCS#12` file:

```python
clientdir = "etc/x509-cert/SSLCA/clientdir"
endpoint = 'https://--your-instance--'
cred = Credential.from_certificate(os.path.join(clientdir, "client.pem"),
                                   os.path.join(clientdir, "client.key"))
cluster = Cluster.create_instance(endpoint, cred)
```

## [](#local-development)Local Development

We strongly recommend that the client and server [are in the same LAN-like environment](../project-docs/compatibility.md#network-requirements) (e.g. AWS Region). As this may not always be possible during development, read the guidance on working with [constrained network environments](../ref/client-settings.md#commonly-used-options).