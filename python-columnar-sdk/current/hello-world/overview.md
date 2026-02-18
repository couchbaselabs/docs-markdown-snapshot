---
title: Python Columnar SDK
editUrl: https://github.com/couchbase/docs-columnar-sdk-python/edit/release/1.0/modules/hello-world/pages/overview.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/python-columnar-sdk/current/hello-world/overview.html)

# Python Columnar SDK

# Python Columnar SDK

The Columnar Python SDK allows you to connect to a Capella Columnar cluster from python. For connecting to a Couchbase Server Cluster — self-managed, or Capella Operational — see our [Python Server SDK](../../../python-sdk/current/hello-world/overview.md).

> [!WARNING]
> Don’t Mix Columnar & Operational SDKs.
> 
> Do not combine the Python Columnar SDK with the Python Operational SDK on the same app server (or development machine). This combination is not tested and not supported. There may be problems with different versions of shared dependencies if you try this. This only applies to the Node.js and Python Columnar SDKs.
> 
> Note, this does not apply to combining our Enterprise Analytics SDKs with our Operational SDKs. See the [Analytics SDK page](#home::analytics-sdk.adoc) for a reminder of which Analytics SDK to use with which Analytics service.

  
##  Using Your Columnar Cluster

How-to guides and tutorials to help you start your development journey with Columnar and the Python SDK.

Getting Started

* [Hello Columnar — Python SDK Quickstart Guide](start-using-sdk.md)
* [Connecting to Columnar](../howtos/managing-connections.md)
* [Querying with SQL++](../howtos/sqlpp-queries-with-sdk.md)

Reference

* [API Reference](https://docs.couchbase.com/sdk-api/columnar-python-client/index.html)
* [Client Settings](../ref/client-settings.md)
* [Error Messages](../ref/error-codes.md)
* [Glossary](../ref/glossary.md)

Deployment Docs

* [Columnar SDK Release Notes](../project-docs/columnar-sdk-release-notes.md)
* [Compatibility](../project-docs/compatibility.md)
* [Full Installation](../project-docs/sdk-full-installation.md)