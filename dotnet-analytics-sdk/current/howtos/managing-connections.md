---
title: Managing Connections
description: This section describes how to connect the .NET Analytics SDK to an
  Analytics cluster.
editUrl: https://github.com/couchbase/docs-analytics-sdk-dotnet/edit/release/1.0/modules/howtos/pages/managing-connections.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:dotnet-analytics-sdk:howtos:managing-connections.adoc[]
---

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

var cluster = Cluster.Create(
    connectionString: "https://analytics.my-couchbase.example.com:18095",
    credential: credential);
```

> [!NOTE]
> Capella’s root certificate is **not** signed by a well known Certificate Authority. However, the certificate is bundled with the SDK, and is automatically trusted unless you specify a different certificate to trust.

## [](#connection-strings)Connection Strings

Typically, an Enterprise Analytics cluster will be behind a load balancer, and you will be making a connection over TLS — so the port used will be `443`. This is the defaut for the SDK, so port `443` does not need to be specified: `<https://analytics.example.com>`.

You must specify the schema — either `https://` (for TLS) or `http://` (for insecure connections — perhaps on a development machine) in the connection string. The default port for insecure connections is port `80`.

If you’re connecting to a cluster directly, without a load balancer, you can specify the port in the connection string: `<https://analytics.example.com:18095>`. For a standalone Analytics cluster, the port is usually `18095` (or `8095` for an insecure connection). Make sure to check with your administrator.

### [](#client-settings-parameters)Client Settings Parameters

Connection strings can also include client settings, which will override any that are also set in the code.

Connection string with two parameters

https://analytics.example.com?timeout.connect_timeout=30s&timeout.query_timeout=2m

The full list of recognized parameters is documented in the [client settings reference](../ref/client-settings.md).

Connection string with two parameters

http://localhost:8095?timeout.connect_timeout=30s&timeout.query_timeout=2m

The full list of recognized parameters is documented in the [client settings reference](../ref/client-settings.md).

## [](#local-development)Local Development

We strongly recommend that the client and server [are in the same LAN-like environment](../project-docs/compatibility.md#network-requirements) (for example, the same AWS Region).