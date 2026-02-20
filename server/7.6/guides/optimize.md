---
title: Advanced Query Features
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/guides/pages/optimize.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.6@server:guides:optimize.adoc[]
---

[View original HTML](/server/7.6/guides/optimize.html)

# Advanced Query Features

## Cost-Based Optimizer

The cost-based optimizer takes into account the cost of memory, CPU, network transport, and disk usage when choosing the optimal plan to execute a query.

* [Understand the Cost-Based Optimizer for Queries](../n1ql/n1ql-language-reference/cost-based-optimizer.md)
* [Use the Cost-Based Optimizer with Queries](cbo.md)

## SQL++ Support for Couchbase Transactions

SQL++ offers full support for Couchbase ACID transactions.

* [SQL++ Support for Couchbase Transactions](../n1ql/n1ql-language-reference/transactions.md)
* [Create Couchbase Transactions with SQL++](transactions.md)

## Flex Indexes

Flex Indexes enable a SQL++ query to use a Search index transparently with standard SQL++ syntax.

* [Use Search Indexes with a Query](../n1ql/n1ql-language-reference/flex-indexes.md)

## Time Series Data

In Couchbase Server 7.2 and later, SQL++ enables you to store and query time series data.

* [Store and Process Time Series Data](../n1ql/n1ql-language-reference/time-series.md)