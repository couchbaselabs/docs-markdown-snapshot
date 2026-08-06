---
title: Querying Your Data
description: Querying Enterprise Analytics from the Go SDK, with SQL++.
editUrl: https://github.com/couchbase/docs-analytics-sdk-go/edit/release/1.1/modules/concept-docs/pages/querying-your-data.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:go-analytics-sdk:concept-docs:querying-your-data.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/go-analytics-sdk/current/concept-docs/querying-your-data.html)

# Querying Your Data

> Querying Enterprise Analytics from the Go SDK, with SQL++. 

SQL++ is a declarative query language for JSON data.

## [](#real-time-data-analysis)Real-Time Data Analysis

Traditionally, analyzing JSON data in NoSQL databases requires complex transformations (like flattening) to prepare it for analytics, causing delays and hindering real-time insights. Enterprise Analytics eliminates these ETL complexities by unifying operational and analytical data stores into a single platform. This enables Zero ETL, reducing costs and complexity, and improving time to insight.

## [](#long-running-queries)Long Running Queries

All versions of Enterprise Analytics support long running client-side requests. This process keeps a connection live between client and server for long running queries. For such long running queries, a better mechanism is for the client to trigger an asynchronous query without holding a connection to the server open for the duration of the query execution. This Server Asynchronous Request API is introduced in Enterprise Analytics Server 2.2\. For more information, see [Enterprise Analytics REST API](../../../enterprise-analytics/current/reference/rest-analytics.md).

After the query request is submitted, clients can monitor the status of the request and on successful execution of query, opt to stream the results of the query. This way the connection between SDK client and Analytics Server does not stay open for the long duration of query processing, and is only needed for result set streaming.

`cluster.StartQuery()` → `QueryHandle` → `QueryStatus` → `QueryResultsHandle`

This information flow can be seen in the sample code in the [SQL++ queries section](../howtos/sqlpp-queries-with-sdk.md#server-asynchronous-api).

## [](#next-steps)Next Steps

Dive right in with our [practical examples](../howtos/sqlpp-queries-with-sdk.md).