---
title: Use Business Intelligence Tools
description: You can apply features available for visualizing and analyzing data
  in the Tableau from Salesforce, Microsoft Power BI, or Apache Superset
  interactive data visualization platforms to the query results you obtain in
  Capella Analytics.
editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/query/pages/bi.adoc
pubDate: 2026-03-13T03:41:17.220Z
link: xref:analytics:query:bi.adoc[]
---

[View original HTML](/analytics/query/bi.html)

# Use Business Intelligence Tools

> You can apply features available for visualizing and analyzing data in the Tableau from Salesforce, Microsoft Power BI, or Apache Superset interactive data visualization platforms to the query results you obtain in Capella Analytics. 

## [](#prerequisites)Prerequisites

To make data from Capella Analytics services accessible to a third-party business intelligence tool, you:

* Download and configure the [Couchbase Tableau Connector](#tableau-connector), the [Couchbase Power BI Connector](#power-bi-connector), or the [Couchbase Superset Connector](#superset-connector).
* Create tabular analytics views of your Capella Analytics collections or query results for consumption by these tools. See [Save Results as a Tabular View](views-tavs.md#TAV) or [Tabular Views](../sqlpp/5a%5Fviews.md).

## [](#tableau-connector)Use the Couchbase Tableau Connector

The Couchbase Tableau Connector provides the integration between tabular views of your Capella Analytics collections or query results and the Salesforce Tableau interactive data visualization platform.

> [!NOTE]
> Capella Analytics services are only compatible with the Couchbase Tableau Connector for Desktop and Server version 1.1.3 and later.  
> You can download the latest version of the Couchbase Tableau Connector from the [Release notes](../../tableau-connector/current/release-notes.md) page.

For information about setting up the connector, see the [Introduction](../../tableau-connector/current/index.md) documentation.

> [!NOTE]
> When using this documentation with Capella Analytics, note the following:
> 
> * References to "Couchbase Server" apply to Capella Analytics services as well.
> * You do not need to complete the instructions for enabling the Analytics Service.
> * To prepare a tabular view in Capella Analytics, see [Save Results as a Tabular View](views-tavs.md#TAV) or [Tabular Views](../sqlpp/5a%5Fviews.md).

## [](#power-bi-connector)Use the Couchbase Power BI Connector

The Couchbase Power BI Connector provides the integration between tabular views of your Capella Analytics collections or query results and Microsoft’s Power BI interactive data visualization platform.

For information about setting up the connector, see the [power-bi-connector:ROOT:index.adoc](#power-bi-connector:ROOT:index.adoc) documentation.

## [](#superset-connector)Use the Couchbase Superset Connector

The Couchbase Apache Superset Connector lets you visualize data from Tabular Analytics Views (TAV) in Apache Superset. It works by connecting Capella Analytics to Apache Superset using SQLAlchemy, allowing you to create interactive visualizations from your tabular data.

For information about setting up the connector, see the [Introduction](../../superset-connector/current/index.md) documentation.

## [](#see-also)See Also

* [Introduction](../../tableau-connector/current/index.md)
* [power-bi-connector:ROOT:index.adoc](#power-bi-connector:ROOT:index.adoc)
* [Save Results as a Tabular View](views-tavs.md#TAV)
* [Views and Tabular Views](../sqlpp/5a%5Fviews.md)