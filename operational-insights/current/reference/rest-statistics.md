---
title: Statistics
description: The REST API allows cluster statistics to be retrieved; either
  individually, or in bulk.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/reference/pages/rest-statistics.adoc
  xref: xref:enterprise-analytics:reference:rest-statistics.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/reference/rest-statistics.html)

# Statistics

> The REST API allows cluster statistics to be retrieved; either individually, or in bulk. 

## [](#apis-in-this-section)APIs in this Section

Metrics are provided for the Data Service and the Analytics Service, and also for the Cluster Manager. All metrics can be queried by means of the REST API.

For a complete list of available metrics that can be queried, see the [Metrics Reference](../metrics-reference/metrics-reference.md).

The APIs described in this section are listed below.

| HTTP Method | URI                                                               | Documented at                                              |
| ----------- | ----------------------------------------------------------------- | ---------------------------------------------------------- |
| GET         | /pools/default/stats/range/<metric\_name>/\[function-expression\] | [Getting a Single Statistic](rest-statistics-single.md)    |
| POST        | /pools/default/stats/range                                        | [Getting Multiple Statistics](rest-statistics-multiple.md) |
| GET         | /prometheus\_sd\_config                                           | [Prometheus Discovery API](rest-discovery-api.md)          |