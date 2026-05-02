---
title: Analyze Large Datasets
description: The Analytics Service provides a parallel data-management
  capability, allowing the running of complex analytical queries.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/analytics-service/analytics-service.adoc
pubDate: 2026-05-02T05:28:41.565Z
link: xref:cloud:clusters:analytics-service/analytics-service.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/clusters/analytics-service/analytics-service.html)

# Analyze Large Datasets

> The Analytics Service provides a parallel data-management capability, allowing the running of complex analytical queries. 

## [](#about-the-analytics-service)About the Analytics Service

The Analytics Service is a parallel data management capability that's designed to efficiently run complex queries over many records. It supports large join, set, aggregation, and grouping operations, any of which may result in long running queries, high CPU usage, high memory consumption, or excessive network latency due to data fetching and cross node coordination.

The Analytics Service enables you to create up to 8 datasets, which contain shadow copies of the data that you want to analyze. When the Analytics datasets are linked to the operational data, changes in the operational data are reflected in your Analytics data in real time. The Analytics Service also enables you to create external links to analyze data from external sources.

The Analytics Service supports the SQL++ for Analytics query language, a next-generation declarative query language for JSON data. SQL++ for Analytics has much in common with SQL, but it also includes a small number of extensions that address the different data models that the languages were designed to query. For more information, see [SQL++ for Analytics vs. SQL++ for Query](../../../server/current/analytics/6%5Fn1ql.md) and the [SQL++ for Analytics Language Reference](../../../server/current/analytics/1%5Fintro.md).

## [](#using-the-analytics-service)Using the Analytics Service

Like the other Couchbase services, the Analytics Service can be deployed during [cluster creation](../create-database.md), or by [adding it to an existing cluster](../scale-database.md). The Analytics Service depends on the [Data Service](../data-service/data-service.md). This service must also be deployed on the cluster in order to use the Analytics Service. For more information about how these services interact with each other, see the [Couchbase Server documentation](../../../server/current/learn/services-and-indexes/services/analytics-service.md).

If a cluster has the Analytics Service deployed, SQL++ for Analytics queries can be issued using the Couchbase SDK and the interactive [Analytics Workbench](analytics-workbench.md).

> [!TIP]
> Use the Cost-Based Optimizer for Analytics to select the most efficient query operations. For more information, see [Cost-Based Optimizer for Analytics](../../../server/current/analytics/5b%5Fcbo.md).