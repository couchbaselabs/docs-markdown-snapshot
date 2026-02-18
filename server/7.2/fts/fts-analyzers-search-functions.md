---
title: Analyzers - Search Functions
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/fts/pages/fts-analyzers-search-functions.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/fts/fts-analyzers-search-functions.html)

# Analyzers - Search Functions

[Search functions](../n1ql/n1ql-language-reference/searchfun.md) allow users to execute full text search requests within a SQL++ query.

In the context of SQL++ queries, a full text search index can be described as one of the following :

* [Covering index](../n1ql/n1ql-language-reference/covering-indexes.md)
* Non-covering index

This characterization depends on the extent to which it could answer all aspects of the SELECT predicate and the WHERE clauses of a SQL++ query. A SQL++ query against a non-covering index will go through a "Verification phase". In this phase documents are fetched from the query service based on the results of the search index, and the documents are validated as per the clauses defined in the query.

For example, an index with only the field `field1` configured is considered a non-covering index for a query `field1=abc` and `field2=xyz`.

## [](#use-case)Use case

Consider a use case where a user has defined a special analyzer for a field in their full text search index. The following can be expected:

1. If the query does not use the same analyzer as specified in the full text search index, the query will not be allowed to run.
2. By default, the analyzer used for indexing the field (as per the index definition) will be picked up if no analyzer is specified in the analytic query.
3. If the index is a non-covering index for an analytic query and the user has not specified an explicit analyzer to be used, the verification phase might drop documents that should have been returned as results due to lack of query context.

The user can explicitly specify the search query context in the following three ways:

1. Explicitly specify the analyzer to use in the query (to match with that specified in the index).  
Example 1  
SEARCH(keyspace, {"match": "xyz", "field": "abc", "analyzer": "en"})
2. Specify index name within the options argument of the SEARCH function, so this index’s mapping is picked up during the verification process  
Example 2  
SEARCH(keyspace, {"match": "xyz", "field": "abc"}, {"index": "fts-index-1"})
3. Specify the index mapping itself as a JSON object within the options argument of the SEARCH function, which is used directly for the verification process  
Example 3  
SEARCH(keyspace, {"match": "xyz", "field": "abc"}, {"index": {...<an index mapping>....})

> [!NOTE]
> If users fail to provide this query context for non-covering queries, they may see incorrect results, including dropped documents, especially while using non-standard and custom analyzers.