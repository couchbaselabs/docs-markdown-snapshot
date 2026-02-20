---
title: Optimizing Performance
description: These guides explain some of the features that you can use to
  optimize the performance of SQL++ queries.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/guides/pages/optimize.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:guides:optimize.adoc[]
---

[View original HTML](/server/7.2/guides/optimize.html)

# Optimizing Performance

These guides explain some of the features that you can use to optimize the performance of SQL++ queries.  
This page is for Couchbase Server.

## Prepared Statements

If you need to execute certain SQL++ statements repeatedly, you can use placeholder parameters and prepared statements to optimize query reuse.

* [Prepared Statements](prep-statements.md)

## Index Advisor

In Couchbase Server Enterprise Edition, the Index Advisor can analyze your queries and provide recommended indexes to optimize response times.

* [Index Advisor](index-advisor.md)

## Cost-Based Optimizer

In Couchbase Server Enterprise Edition, the Cost-Based Optimizer enables the Query Service to create the most efficient plan to execute a query.

* [Cost-Based Optimizer](cbo.md)

## Related Links

Refer to the following guide for information on creating and using primary indexes and global secondary indexes.

* [Indexes](indexes.md)