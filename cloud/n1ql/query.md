---
title: Query Data with SQL++
description: The Query Service supports the querying of data by means of the
  SQL++ query language.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/n1ql/pages/query.adoc
  xref: xref:cloud:n1ql:query.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/n1ql/query.html)

# Query Data with SQL++

> The Query Service supports the querying of data by means of the SQL++ query language. 

As its primary function, the Query Service enables you to issue queries to extract data from Couchbase Capella. You can also issue queries for data definition (defining indexes) and data manipulation (adding or deleting data). The Query Service needs both the Index Service and the Data Service to be running on Couchbase Capella.

You can run queries from the Query tab in the Couchbase Capella UI, the cbq shell, the Data API, or the Couchbase SDKs.

## When to Use Queries

Use the Query Service for query analysis and execution to help you build applications.

Use the Analytics Service for online analytical processing (OLAP) — large datasets with complex analytical or ad hoc queries.

Use the Search Service for Full-Text Search with natural language processing across multiple data types and languages — custom text analysis, Geospatial search, and more.

## SQL++ for Query

To create queries, you must use a query language that's structured so that the Query Service understands what it needs to retrieve. Couchbase Capella uses a query language called SQL++. The Couchbase implementation of SQL++ was formerly known as [N1QL](https://www.couchbase.com/products/n1ql) (pronounced "nickel").

SQL++ is an expressive, powerful, and complete SQL dialect for querying, updating, and manipulating JSON data. Based on SQL, it's immediately familiar to developers who can quickly start developing rich applications.

## How-To Guides

* [Understand Queries](n1ql-intro/index.md)
* [Select Data with Queries](../guides/query.md)
* [Use Primary and Secondary Indexes](../guides/indexes.md)
* [Manipulate Data with Queries](../guides/manipulate.md)
* [User-Defined Functions for Queries](../guides/javascript-udfs.md)
* [Advanced Query Features](../guides/optimize.md)

## Query Administration

* [Administer Queries and Indexes](n1ql-manage/index.md)

## Query References

* [SQL++ for Query Reference](n1ql-language-reference/index.md)
* [Primary and Secondary Index Reference](../indexes/indexing-overview.md)
* [JavaScript Functions for Query Reference](../javascript-udfs/javascript-functions-with-couchbase.md)

## Related Links

* [Query Service architecture](../../server/current/learn/services-and-indexes/services/query-service.md)
* [Data](../../server/current/learn/data/data.md)