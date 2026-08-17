---
title: Managing Connections
description: This section describes how to connect the Node.js Columnar SDK to a
  Columnar cluster.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-columnar-sdk-nodejs/edit/release/1.0/modules/howtos/pages/managing-connections.adoc
  xref: xref:nodejs-columnar-sdk:howtos:managing-connections.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/nodejs-columnar-sdk/current/howtos/managing-connections.html)

# Managing Connections

> This section describes how to connect the Node.js Columnar SDK to a Columnar cluster. It contains best practices as well as information on TLS/SSL and advanced connection options. 

Our [Getting Started pages](../hello-world/start-using-sdk.md) cover the basics of making a connection to a Capella Columnar cluster. This page is a wider look at the topic.

> [!WARNING]
> Don't Mix Columnar & Operational SDKs.
> 
> Do not combine the Node.js Columnar SDK with the Node.js Operational SDK on the same app server (or development machine). This combination is not tested and not supported. There may be problems with different versions of shared dependencies if you try this. This only applies to the Node.js and Python Columnar SDKs.
> 
> Note, this does not apply to combining our Enterprise Analytics SDKs with our Operational SDKs. See the [Analytics SDK page](../../../home/analytics-sdk.md) for a reminder of which Analytics SDK to use with which Analytics service.

## [](#connecting-to-a-cluster)Connecting to a Cluster

A connection to a Columnar cluster is represented by a `columnar` object. Connect to Columnar by calling `columnar.createInstance` with the connection string, credentials, and any required optional parameters.

```javascript
const columnar = require('couchbase-columnar')

async function main() {
  // Update this to your cluster
  const clusterConnStr = 'couchbases://--your-instance--'
  const username = 'username'
  const password = 'Password123!'
  // User Input ends here.

  const credential = new columnar.Credential(username, password)
  const cluster = columnar.createInstance(clusterConnStr, credential)
```

> [!NOTE]
> Capella's root certificate is **not** signed by a well known Certificate Authority. However, the certificate is bundled with the SDK, and is automatically trusted unless you specify a different certificate to trust.

### [](#connection-strings)Connection Strings

A Couchbase connection string is a comma-delimited list of IP addresses and/or hostnames, optionally followed by a list of parameters.

The parameter list is just like the query component of a URI; name-value pairs have an equals sign (`=`) separating the name and value, with an ampersand (`&`) between each pair. Just as in a URI, the first parameter is prefixed by a question mark (`?`).

For Columnar, as for all Capella products, connection must be made with Transport Layer Security (TLS) — for full encryption of client-side traffic — for which the `couchbases://` schema is used as the root of the connection string (note the trailing **s**).

Simple connection string with one seed node

couchbases://cb.<your-endpoint>.cloud.couchbase.com

Connection string with two parameters

couchbases://cb.<your-endpoint>.cloud.couchbase.com?timeout.connect_timeout=75s&timeout.query_timeout=100s

The full list of recognized parameters is documented in the [client settings reference](../ref/client-settings.md).

## [](#local-development)Local Development

We strongly recommend that the client and server [are in the same LAN-like environment](../project-docs/compatibility.md#network-requirements) (e.g. AWS Region). As this may not always be possible during development, read the guidance on working with [constrained network environments](../ref/client-settings.md#commonly-used-options). More details on connecting your client code to Couchbase Capella can be found [in the Capella Operational docs](../../../cloud/get-started/connect.md#connecting-your-sdk-to-capella).

### [](#troubleshooting-connections-to-cloud)Troubleshooting Connections to Cloud

Some DNS caching providers (notably, home routers) can't handle an SRV record that's large — if you have DNS-SRV issues with such a set-up, reduce your DNS-SRV to only include three records. \[_For development only, not production._\].