---
title: Vector Search
description: Vector Search from the SDK, to enable AI integration, semantic
  search, and the RAG framework.
editUrl: https://github.com/couchbase/docs-sdk-scala/edit/release/1.8/modules/howtos/pages/vector-searching-with-sdk.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:1.8@scala-sdk:howtos:vector-searching-with-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/scala-sdk/1.8/howtos/vector-searching-with-sdk.html)

# Vector Search

> Vector Search from the SDK, to enable AI integration, semantic search, and the RAG framework. 

This is currently implemented using [Search Indexes](full-text-searching-with-sdk.md), and can even be combined with traditional full text search queries. Vector embeddings can be an array of floats or a [base64 encoded string](../../../server/current/vector-search/run-vector-search-ui.md#base64).

## [](#prerequisites)Prerequisites

Couchbase Server 7.6.0 (7.6.2 for base64-encoded vectors) — or recent Capella instance.

#### [](#single-vector-query)Single vector query

In this first example we are performing a single vector query:

```scala
val request = SearchRequest.vectorSearch(VectorSearch(VectorQuery("vector_field", vectorQuery)))

val result: Try[SearchResult] = scope.search("vector-index", request)
```

Let’s break this down. We create a `SearchRequest`, which can contain a traditional FTS query `SearchQuery` and/or the new `VectorSearch`. Here we are just using the latter.

The `VectorSearch` allows us to perform one or more `VectorQuery` s.

The `VectorQuery` itself takes the name of the document field that contains embedded vectors ("vector\_field" here), plus actual vector query in the form of a `float[]`.

(Note that Couchbase itself is not involved in generating the vectors, and these will come from an external source such as an embeddings API.)

Finally we execute the `SearchRequest` against the FTS index "travel-sample-index", which has previously been setup to vector index the "vector\_field" field.

This happens to be a scoped index so we are using `scope.search()`. If it was a global index we would use `cluster.search()` instead - see [\[Scoped vs Global Indexes\]](#Scoped vs Global Indexes).

It returns the same `SearchResult` detailed earlier.

#### [](#multiple-vector-queries)Multiple vector queries

You can run multiple vector queries together:

```scala
val request = SearchRequest.searchQuery(SearchQuery.matchAll)
  .vectorSearch(VectorSearch(VectorQuery("vector_field", vectorQuery)))

val result = scope.search("vector-and-fts-index", request)
```

How the results are combined (ANDed or ORed) can be controlled with `vectorSearchOptions().vectorQueryCombination()`.

#### [](#combining-fts-and-vector-queries)Combining FTS and vector queries

You can combine a traditional FTS query with vector queries:

```scala
val request = SearchRequest
  .vectorSearch(VectorSearch(Seq(
    VectorQuery("vector_field", vectorQuery).numCandidates(2).boost(0.3),
    VectorQuery("vector_field", anotherVectorQuery).numCandidates(5).boost(0.7))))

val result = scope.search("vector-index", request)
```

How the results are combined (ANDed or ORed) can be controlled with `vectorSearchOptions().vectorQueryCombination()`.

## [](#further-reading)Further Reading

* [Vector Search for AI Apps docs (self-managed Couchbase Server)](../../../server/current/vector-search/vector-search.md)
* [Vector Search for AI Apps docs (Capella DBaaS)](#cloud::vector-search:vector-search.adoc)
* Vector Search in the [Scala API reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client/com/couchbase/client/scala/search/vector/index.html).