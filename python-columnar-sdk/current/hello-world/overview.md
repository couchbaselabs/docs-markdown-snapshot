---
title: Python Columnar SDK
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Python Columnar SDK
    version: "1.0"
antora:
  editUrl: https://github.com/couchbase/docs-columnar-sdk-python/edit/release/1.0/modules/hello-world/pages/overview.adoc
  xref: xref:python-columnar-sdk:hello-world:overview.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-columnar-sdk/current/hello-world/overview.html)

# Python Columnar SDK

# Python Columnar SDK

The Columnar Python SDK allows you to connect to an Operational Insights (Capella) cluster from python. For connecting to a Couchbase Server Cluster — self-managed, or Capella Operational — see our [Python Server SDK](../../../python-sdk/current/hello-world/overview.md).

> [!WARNING]
> Don't Mix Columnar & Operational SDKs.
> 
> Do not combine the Python Columnar SDK with the Python Operational SDK on the same app server (or development machine). This combination is not tested and not supported. There may be problems with different versions of shared dependencies if you try this. This only applies to the Node.js and Python Columnar SDKs.
> 
> Note, this does not apply to combining our Operational Insights SDKs with our Operational SDKs. See the [Operational Insights SDK page](../../../home/operational-insights-sdk.md) for a reminder of which Insights SDK to use with which Insights or Analytics service.

  
##  Using Your Operational Insights (Capella) Cluster

How-to guides and tutorials to help you start your development journey with Operational Insights (Capella) and the Python SDK.

Getting Started

* [Hello Operational Insights (Capella) — Python SDK Quickstart Guide](start-using-sdk.md)
* [Connecting to Operational Insights (Capella)](../howtos/managing-connections.md)
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