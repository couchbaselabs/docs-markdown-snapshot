---
title: Full Text Search (FTS) Using the C SDK with Couchbase Server
description: You can use the Full-Text Search service (FTS) to create queryable
  full-text indexes in Couchbase Server.
editUrl: https://github.com/couchbase/docs-sdk-c/edit/release/3.3/modules/howtos/pages/full-text-searching-with-sdk.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:c-sdk:howtos:full-text-searching-with-sdk.adoc[]
---

[View original HTML](/c-sdk/current/howtos/full-text-searching-with-sdk.html)

# Full Text Search (FTS) Using the C SDK with Couchbase Server

> You can use the Full-Text Search service (FTS) to create queryable full-text indexes in Couchbase Server. 

Full-Text Search or FTS allows you to create, manage, and query full text indexes on JSON documents stored in Couchbase buckets. It uses natural language processing for querying documents, provides relevance scoring on the results of your queries, and has fast indexes for querying a wide range of possible text searches. Some of the supported query types include simple queries like Match and Term queries; range queries like Date Range and Numeric Range; and compound queries for conjunctions, disjunctions, and/or boolean queries. The C SDK exposes an API for performing FTS queries which abstracts some of the complexity of using the underlying REST API.

> [!NOTE]
> When using a Couchbase version < 6.5 you must create a valid Bucket connection using `cluster.Bucket(name)` before you can use Search.

## [](#getting-started)Getting Started

After familiarizing yourself with how to create and query a search index in the UI you can query it from the SDK. Search queries are executed at Cluster level (not bucket or collection). As of Couchbase Server 6.5+ they do also not require a bucket to be opened first. In older versions of Couchbase Server, even though executed at Cluster level, a bucket must be opened before performing queries.

## [](#example)Example

For a full Search example, see the [API documentation](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.3.18/example%5F2fts%5F2fts%5F8c-example.html).