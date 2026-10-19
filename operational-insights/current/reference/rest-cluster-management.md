---
title: Cluster Management APIs
description: "The Cluster Management APIs manage the Operational Insights
  cluster: its nodes, rebalance and failover, server groups, security, and
  service settings."
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/reference/pages/rest-cluster-management.adoc
  xref: xref:enterprise-analytics:reference:rest-cluster-management.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/reference/rest-cluster-management.html)

# Cluster Management APIs

> The Cluster Management APIs manage the Operational Insights cluster: its nodes, rebalance and failover, server groups, security, and service settings. 

The Cluster Management APIs are served by the cluster manager on every node. By default, they listen on port 8091, or 18091 for secure access.

For the APIs that run requests and manage the service, such as querying, links, and configuration parameters, see [Service APIs](rest-analytics.md).

> [!NOTE]
> Some `GET` endpoints in these APIs return fields that do not apply to Operational Insights. These fields are not documented, and can be ignored.

## [](#apis-in-this-section)APIs in this Section

* [Nodes and Clusters API](rest-cluster-intro.md)
* [Server Group API](rest-rza.md)
* [Security API](rest-security.md)
* [Service Settings API](#service-settings-api)

For a complete list of the methods and URIs, see [REST API Overview](rest-intro.md).

## [](#service-settings-api)Service Settings API

The Service Settings API configures cluster-wide settings for the service, such as the object storage that holds its data.

| HTTP Method | URI                           | Documented at                                                                            |
| ----------- | ----------------------------- | ---------------------------------------------------------------------------------------- |
| GET         | /settings/operationalInsights | [View Service Settings](../analytics-rest-settings/index.md#operation/get%5Fsettings)    |
| POST        | /settings/operationalInsights | [Modify Service Settings](../analytics-rest-settings/index.md#operation/post%5Fsettings) |