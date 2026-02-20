---
title: "Query: Fundamentals"
description: The Query Service supports the querying of data by means of the
  SQL++ query language.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/n1ql/pages/query.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:n1ql:query.adoc[]
---

[View original HTML](/server/7.2/n1ql/query.html)

# Query: Fundamentals

> The Query Service supports the querying of data by means of the SQL++ query language. 

As its primary function, the Query service enables you to issue queries to extract data from Couchbase server. You can also issue queries for data definition (defining indexes) and data manipulation (adding or deleting data). The Query Service depends on both the Index Service and the Data Service.

To issue queries, you can use a Couchbase SDK, the REST API, or the tools provided by the Query service: the cbq shell or the Query workbench.

## When to Use Queries

Use the Query service for operational queries — for example, the front-end queries behind every page display or navigation.

Use the Analytics service when you don’t know every aspect of the query in advance — for example, if the data access patterns change frequently, or you want to avoid creating an index for each data access pattern, or you want to run ad hoc queries for data exploration or visualization.

Use the Full Text Search service when you want to take advantage of natural-language querying.

## SQL++ for Query

Couchbase Server can be queried using SQL++, the Couchbase Server query language. The Couchbase implementation of SQL++ was formerly known as [N1QL](https://www.couchbase.com/products/n1ql) (pronounced "nickel"), which derives its name from the non-first normal form of the data model.

SQL++ is an expressive, powerful, and complete SQL dialect for querying, transforming, and manipulating JSON data. Based on SQL, it’s immediately familiar to developers who can quickly start developing rich applications.

## What’s Next

* [Running Queries](n1ql-intro/index.md)
* [Tutorials](tutorial.md)
* [Query Tools](../tools/tools-ref.md)
* [Settings and Parameters](../settings/query-settings.md)
* [Using Indexes](../learn/services-and-indexes/indexes/global-secondary-indexes.md)
* [Advanced Features](advanced.md)
* [SQL++ Language Reference](n1ql-language-reference/index.md)
* [JavaScript Functions with Couchbase](../javascript-udfs/javascript-functions-with-couchbase.md)

## Related Links

* [Query Service architecture](../learn/services-and-indexes/services/query-service.md)
* [Data](../learn/data/data.md)