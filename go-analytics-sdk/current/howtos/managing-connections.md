---
title: Managing Connections
description: This section describes how to connect the Go Analytics SDK to an
  Analytics cluster.
editUrl: https://github.com/couchbase/docs-analytics-sdk-go/edit/release/1.0/modules/howtos/pages/managing-connections.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:go-analytics-sdk:howtos:managing-connections.adoc[]
---

[View original HTML](/go-analytics-sdk/current/howtos/managing-connections.html)

# Managing Connections

> This section describes how to connect the Go Analytics SDK to an Analytics cluster. It contains best practices as well as information on TLS/SSL and advanced connection options. 

Our [Getting Started pages](../hello-world/start-using-sdk.md) cover the basics of making a connection to an Enterprise Analytics cluster. This page is a wider look at the topic.

## [](#connecting-to-a-cluster)Connecting to a Cluster

A connection to an Enterprise Analytics cluster is represented by a `Cluster` object. A `Cluster` provides access to Buckets and Scopes, as well as various Couchbase services and management interfaces. The simplest way to create a `Cluster` object is to call `cbanalytics.Connect()` with a [connection string](#connection-strings), username, and password:

```golang
	cluster, err := cbanalytics.NewCluster(
		connStr,
		cbanalytics.NewBasicAuthCredential(username, password),
		// The third parameter is optional.
		// This example sets the default server query timeout to 3 minutes,
		// that is the timeout value sent to the query server.
		cbanalytics.NewClusterOptions().SetTimeoutOptions(
			cbanalytics.NewTimeoutOptions().SetQueryTimeout(3*time.Minute),
		),
	)
	handleErr(err)
```

## [](#connection-strings)Connection Strings

Typically, an Enterprise Analytics cluster will be behind a load balancer, and you will be making a connection over TLS — so the port used will be `443`. This is the defaut for the SDK, so port `443` does not need to be specified: `<https://analytics.example.com>`.

You must specify the schema — either `https://` (for TLS) or `http://` (for insecure connections — perhaps on a development machine) in the connection string. The default port for insecure connections is port `80`.

If you’re connecting to a cluster directly, without a load balancer, you can specify the port in the connection string: `<https://analytics.example.com:18095>`. For a standalone Analytics cluster, the port is usually `18095` (or `8095` for an insecure connection). Make sure to check with your administrator.

### [](#client-settings-parameters)Client Settings Parameters

Connection strings can also include client settings, which will override any that are also set in the code.

Connection string with two parameters

https://analytics.example.com?timeout.connect_timeout=30s&timeout.query_timeout=2m

The full list of recognized parameters is documented in the [client settings reference](../ref/client-settings.md).

## [](#local-development)Local Development

We strongly recommend that the client and server [are in the same LAN-like environment](../project-docs/compatibility.md#network-requirements) (e.g. AWS Region). As this may not always be possible during development, read the guidance on working with [constrained network environments](../ref/client-settings.md#commonly-used-options).