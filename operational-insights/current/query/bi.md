---
title: Use Business Intelligence Tools
description: You can apply features available for visualizing and analyzing data
  in Tableau from Salesforce, Microsoft Power BI, or Apache Superset interactive
  data visualization platforms to the query results you obtain in Operational
  Insights.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: concept
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/query/pages/bi.adoc
  xref: xref:enterprise-analytics:query:bi.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/query/bi.html)

# Use Business Intelligence Tools

> You can apply features available for visualizing and analyzing data in Tableau from Salesforce, Microsoft Power BI, or Apache Superset interactive data visualization platforms to the query results you obtain in Operational Insights. 

## [](#prerequisites)Prerequisites

To make data from Operational Insights services accessible to a third-party business intelligence tool, you:

* Download and configure the connector for your BI tool of choice. See [Supported Business Intelligence Tools](#supported-bi-tools).
* Create tabular analytics views on your Operational Insights collections, and query those tabular views for consumption by BI tools. See [Tabular Views](../sqlpp/5a%5Fviews.md).

## [](#supported-bi-tools)Supported Business Intelligence Tools

Operational Insights integrates with the following business intelligence tools:

* [Power BI](power-bi.md) — Connect Operational Insights to Microsoft Power BI using the Couchbase Power BI Connector.
* [Tableau](tableau.md) — Connect Operational Insights to Salesforce Tableau using the Couchbase Tableau Connector.
* [Apache Superset](superset.md) — Connect Operational Insights to Apache Superset using the Couchbase Superset Connector.

## [](#see-also)See Also

* [Views and Tabular Views](../sqlpp/5a%5Fviews.md)