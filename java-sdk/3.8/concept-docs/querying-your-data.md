---
title: Querying Your Data
description: Choosing the right service to query your data.
editUrl: https://github.com/couchbase/docs-sdk-java/edit/release/3.8/modules/concept-docs/pages/querying-your-data.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.8@java-sdk:concept-docs:querying-your-data.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/java-sdk/3.8/concept-docs/querying-your-data.html)

# Querying Your Data

> Choosing the right service to query your data. SQL++ is a declarative query language for JSON data. Couchbase also offers fuzzy search, including Vector Search. 

The data service stores your documents, but is the best route to retrieving them?

SQL++ is a SQL-family language, and an easy way for anyone familiar with Relational Databases (RDBMS) to work with documents stored in Couchbase — if you're sure that's the service that you want, jump to our [Query Howto doc](../howtos/sqlpp-queries-with-sdk.md).

Couchbase also has a powerful Search Service, supporting similarity and hybrid search, combining text, vector, range, and geospatial search. [Search functions](../../../server/7.6/n1ql/n1ql-language-reference/searchfun.md) enable you to use Search queries directly within a SQL++ query.

> [!TIP]
> SQL++ or CRUD API?
> 
> Maybe you'd prefer to retrieve whole documents and work on them as objects in Java, or do this after running just a few queries, reducing the number of Query and Index Service nodes you need on your Capella (or self-managed) cluster. Whether you go through the Data Service, or Query, you'll find that both follow the typical DML (Data Manipulation Language) patterns that you encounter in the relational database world. See the [Data Service section](data-durability-acid-transactions.md) for information on CRUD with the Data Service, with its fast binary protocol.

## [](#your-use-case)Your Use Case

How you combine the Data Service and SQL++ should depend on your use case, but you should also examine the other options of longer running (or real time) analytical queries, fuzzy searches (such as full-text search and Geo search), and vector search.

### [](#analytics-queries)Analytics Queries

Couchbase offers a choice of:

* [Capella Columnar](../../../analytics/intro/intro.md) for real-time analytics, with data stored elsewhere in your data lake.
* [Couchbase Analytics Service (CBAS)](../howtos/analytics-using-sdk.md) for traditional data analytics against your operational cluster.

Both use versions of the SQL++ query language.

This page covers using our operational Java SDK to connect to the Analytics Service of a Capella Operational or self-managed Couchbase Server cluster. As well as this row-based analytics service, a speedy, column-based analytics database is available for real-time analytics.

> [!TIP]
> Analytics SDKs
> 
> SDKs for [Enterprise Analytics](../../../enterprise-analytics/current/intro/intro.md) — Couchbase's analytical database for real time apps and operational intelligence (RT-OLAP) — are available for the Go, Java, Node.js, and Python platforms. See the [Enterprise Analytics SDK pages](../../../home/analytics-sdk.md) for more information.
> 
> Currently, different SDKs are needed to connect to [Capella Analytics](../../../analytics/intro/intro.md) — as this service does not have Enterprise Analytics' load balancer, and uses a different connection protocol. Capella Analytics SDKs (also known as Columnar SDKs) are available for the Go, Java, Node.js, and Python platforms. See the [Capella Analytics SDK pages](../../../home/columnar-sdk.md) for more information.

### [](#search)Search

Fuzzy search with text or a variety of other data:

* [Vectors](#vector-search)
* Structured or unstructured text
* Dates
* Numbers
* CIDR notation
* Geospatial data

Searches use indexes created against data at the Scope or the budket level.

### [](#vector-search)Vector Search

Couchbase Server 7.6 introduces Vector Search to enable AI integration, semantic search, and the RAG framework. A developer-friendly vector indexing engine exposes a vector database and search functionality. With Couchbase Vector Search, you can enable fast and highly accurate semantic search, ground LLM responses in relevant data to reduce hallucinations, and enhance or enable use cases like personalized searches in e-commerce and media & entertainment, product recommendations, fraud detection, and reverse image search. You can also enable full access to an AI ecosystem with a Langchain integration, the most popular open-source framework for LLM-driven applications.

Read more in our [Vector Search documentation](../../../server/7.6/vector-search/vector-search.md), or dive in and try [Vector Search with the Java SDK](../howtos/vector-searching-with-sdk.md).

## [](#data-service)Data Service

When you already know the Key (ID) of the document, then [Data Operations](../howtos/kv-operations.md) (using the KV — or _Key - Value_ Service) are by far the simplest way to retrieve or mutate it. The binary protocol used is far quicker than streaming JSON with the Query Service.

If you know the path to the piece of information that you need within a JSON document, then [Sub-Document operations](../howtos/subdocument-operations.md) will not only retrieve the information more quickly, but will reduce the amount of data that needs to be sent over the network.

### [](#range-scan)Range Scan

From version 7.6 of self-managed Couchbase Server — and the current Capella — [KV Range Scan](../howtos/kv-operations.md#kv-range-scan) offers the opportunity to group operations by ranges of alphanumerically adjacent keys. One common use case would be sequentially captured data given date/time-prefixed keys.

Use this API for low concurrency batch queries where latency is not a critical as the system may have to scan a lot of documents to find the matching documents. For low latency range queries, it is recommended that you use SQL++ with the necessary indexes.

### [](#query-without-index)Query without Index

From Couchbase Server 7.6 onwards, CRUD operations (such as `CREATE`, `INSERT`, and `SELECT`) and `JOIN` can be performed against the Query Service without an index (primary or secondary). This uses a [sequential scan](#server:learn:services-and-indexes:indexes/query-without-index.adoc#sequential-scans), relying on a KV range scan to deliver the keys.

Sequential scans are best suited to small collections where key order is unimportant, or where the overhead of maintaining an index can't be justified. For larger collections and greater performance, define the appropriate indexes to speed up your queries. For ordered document key operations, a primary index provides the same functionality, and will outperform a sequential scan.

Read on to learn more about the Query and Index services.

## [](#query-index)Query & Index

If you are familiar with SQL, Couhbase's SQL++ dialect will hold few surprises. Combining semi-flexible schema with SQL works well in a lot of use cases, but do remember that our Data Service is even faster if you do already know the keys.

### [](#index)Index

There are three things important in database systems: performance, performance, performance.

Creating the right index, with the right keys, right order, and right expression is critical to query performance in any database system. That's true for Couchbase as well. See the [Query](n1ql-query.md) page for an in depth look at indexes — but essentially a Primary Index on the document keys will give you better search performance than trying to [query without index](#query-without-index), but well-chosen secondary indexes will make all the difference to query performance.

### [](#query)Query

Our [Querying with SQL++ guide](../howtos/sqlpp-queries-with-sdk.md) will get you started. See also the [Further Reading](#furthre-reading) section at the end of this page.

## [](#ai-help)AI Help

[Capella iQ](../../../cloud/get-started/capella-iq/get-started-with-iq.md) is an AI copilot which offers help with generating SQL++ queries. It can also help to [generate SDK code](../../../cloud/get-started/capella-iq/get-started-with-iq.md#generate-sdk-code-preview) as an aid to getting started on your application.

## [](#further-reading)Further Reading

* [Index Advisor](../../../cloud/guides/index-advisor.md) for recommendations to generate the best index(es) for your queries.