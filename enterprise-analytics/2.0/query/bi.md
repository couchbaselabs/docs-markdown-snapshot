---
title: Use Business Intelligence Tools
description: You can apply features available for visualizing and analyzing data
  in the Tableau from Salesforce, Microsoft Power BI, or Apache Superset
  interactive data visualization platforms to the query results you obtain in
  Enterprise Analytics.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/query/pages/bi.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.0@enterprise-analytics:query:bi.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.0/query/bi.html)

# Use Business Intelligence Tools

> You can apply features available for visualizing and analyzing data in the Tableau from Salesforce, Microsoft Power BI, or Apache Superset interactive data visualization platforms to the query results you obtain in Enterprise Analytics. 

## [](#prerequisites)Prerequisites

To make data from Enterprise Analytics services accessible to a third-party business intelligence tool, you:

* Download and configure the [Couchbase Tableau Connector](#tableau-connector), the [Couchbase Power BI Connector](#power-bi-connector), or the [Couchbase Superset Connector](#superset-connector).
* Create tabular analytics views on your Enterprise Analytics collections, and query those tabular views for consumption by BI tools. See [Tabular Views](../sqlpp/5a%5Fviews.md).

## [](#tableau-connector)Use the Couchbase Tableau Connector

The Couchbase Tableau Connector provides the integration between tabular views of your Enterprise Analytics collections or query results of those tabular views in the Salesforce Tableau interactive data visualization platform

> [!NOTE]
> Enterprise Analytics services are only compatible with the Couchbase Tableau Connector for Desktop and Server version 1.1.3 and later.  
> You can download the latest version of the Couchbase Tableau Connector from the [Release notes](../../../tableau-connector/current/release-notes.md) page.

For information about setting up the connector, see the [tableau-connector:index.adoc](#tableau-connector:index.adoc) documentation.

## [](#power-bi-connector)Use the Couchbase Power BI Connector

The Couchbase Tableau Connector provides the integration between tabular views of your Enterprise Analytics collections or query results of those tabular views in the Salesforce Tableau interactive data visualization platform

For information about setting up the connector, see the [Introduction](../../../power-bi-connector/current/index.md) documentation.

## [](#superset-connector)Use the Couchbase Superset Connector

The Couchbase Apache Superset Connector lets you visualize data from Tabular Analytics Views (TAV) in Apache Superset. It works by connecting Enterprise Analytics to Apache Superset using SQLAlchemy, allowing you to create interactive visualizations from your tabular data.

For information about setting up the connector, see the [Introduction](../../../superset-connector/current/index.md) documentation.

## [](#see-also)See Also

* [Tableau Introduction](../../../tableau-connector/current/index.md)
* [Power BI Introduction](../../../power-bi-connector/current/index.md)
* [Views and Tabular Views](../sqlpp/5a%5Fviews.md)