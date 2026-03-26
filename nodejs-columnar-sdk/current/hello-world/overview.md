---
title: Node.js Columnar SDK
editUrl: https://github.com/couchbase/docs-columnar-sdk-nodejs/edit/release/1.0/modules/hello-world/pages/overview.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:nodejs-columnar-sdk:hello-world:overview.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/nodejs-columnar-sdk/current/hello-world/overview.html)

# Node.js Columnar SDK

# Node.js Columnar SDK

The Columnar Node.js SDK allows you to connect to a [Capella Columnar](../../../analytics/intro/intro.md) cluster from Node.js. For connecting to a Couchbase Server Cluster — self-managed, or Capella Operational — see our [Node.js Server SDK](../../../nodejs-sdk/current/hello-world/overview.md).

> [!WARNING]
> Don't Mix Columnar & Operational SDKs.
> 
> Do not combine the Node.js Columnar SDK with the Node.js Operational SDK on the same app server (or development machine). This combination is not tested and not supported. There may be problems with different versions of shared dependencies if you try this. This only applies to the Node.js and Python Columnar SDKs.
> 
> Note, this does not apply to combining our Enterprise Analytics SDKs with our Operational SDKs. See the [Analytics SDK page](../../../home/analytics-sdk.md) for a reminder of which Analytics SDK to use with which Analytics service.

  
##  Using Your Columnar Cluster

How-to guides and tutorials to help you start your development journey with Columnar and the Node.js SDK.

Getting Started

* [Hello Columnar — Node.js SDK Quickstart Guide](start-using-sdk.md)
* [Connecting to Columnar](../howtos/managing-connections.md)
* [Querying with SQL++](../howtos/sqlpp-queries-with-sdk.md)

Reference

* [API Reference](https://docs.couchbase.com/sdk-api/columnar-node-client/index.html)
* [Client Settings](../ref/client-settings.md)
* [Error Messages](../ref/error-codes.md)
* [Glossary](../ref/glossary.md)

Deployment Docs

* [Columnar SDK Release Notes](../project-docs/columnar-sdk-release-notes.md)
* [Compatibility](../project-docs/compatibility.md)
* [Full Installation](../project-docs/sdk-full-installation.md)