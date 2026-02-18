---
title: Run a Search With a Search Index
description: Run a Search query to search and return the contents of a Search index.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/search/pages/run-searches.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.6/search/run-searches.html)

# Run a Search With a Search Index

> Run a Search query to search and return the contents of a Search index. 

If you use the default search result [sorting](search-request-params.md#sort) of `_score`, a document’s [score](#scoring) determines where it appears in your search results.

> [!NOTE]
> You must [create a Search index](create-search-indexes.md) before you can run a search with the Search Service.

You can run a search against a Search index with:

* The [Couchbase Server Web Console](#ui).
* The [Search Service REST API with curl and HTTP](#api).
* A [SQL++ query](#sql).
* The Couchbase SDKs:  
[.NET](../../../dotnet-sdk/current/howtos/full-text-searching-with-sdk.md)| [Go](../../../go-sdk/current/howtos/full-text-searching-with-sdk.md)| [Java](../../../java-sdk/current/howtos/full-text-searching-with-sdk.md)| [Kotlin](../../../kotlin-sdk/current/howtos/full-text-search.md)| [Node.js](../../../nodejs-sdk/current/howtos/full-text-searching-with-sdk.md)| [PHP](../../../php-sdk/current/howtos/full-text-searching-with-sdk.md)| [Python](../../../python-sdk/current/howtos/full-text-searching-with-sdk.md)| [Ruby](../../../ruby-sdk/current/howtos/full-text-searching-with-sdk.md)| [Scala](../../../scala-sdk/current/howtos/full-text-searching-with-sdk.md)

To run a Search query against multiple Search indexes at once, [Create a Search Index Alias with the Web Console](create-search-index-alias.md).

## [](#scoring)Scoring for Search Queries

To determine a document’s score in search results, the Search Service uses the [tf-idf](https://en.wikipedia.org/wiki/Tf%E2%80%93idf) algorithm. `tf-idf` increases the score of a document based on term frequency, or the number of times a term appears in a document divided by the total number of terms in the document. It penalizes document frequency, or how often a term appears across all documents.

The `tf-idf` score is calculated at a partition level in a Search index.

The Search Service uses `tf-idf` to calculate the hit score for a document, multiplied by any [boost](search-request-params.md#boost) parameters applied to each query inside the [query object](search-request-params.md#query-object):

hit_score = (query_1_boost * query_1_hit_score) + (query_2_boost * query_2_hit_score)

If one of your Search queries is a [Vector Search query](../vector-search/vector-search.md), the calculation changes to:

hit_score = (query_1_boost * query_1_hit_score) + (knn_boost * knn_distance)

When running a hybrid search with the [Server Web Console](#ui) or [REST API](#api), the Search Service displays results as a disjunct (`OR`) between your regular Search and Vector Search queries.

> [!TIP]
> When running a hybrid Search query, you should add a `boost` value to your regular Search query to level the `tf-idf` score with the knn distance. Otherwise, you might see unexpected search results. This is because of the differences in the scoring algorithms between the 2 query types.

## [](#ui)Run a Search with the Server Web Console

You can use the Server Web Console to test your Search index before you integrate search into your application.

You can enter a basic search query in the Server Web Console, or use a [query object](search-request-params.md#query) and other JSON properties for a more complex search. If your cluster is running Couchbase Server version 7.6.2 and later, the Server Web Console lets you generate a command-line curl example or edit the JSON for your query using a built-in code editor.

For more information about how to run a search with the Server Web Console, see [Run A Simple Search with the Web Console](simple-search-ui.md).

For more information about how to configure a Search index and search for geospatial data, see [Run a Geospatial Search Query with the Web Console](geo-search-ui.md).

## [](#api)Run a Search with the REST API

You can also use the REST API, curl, and HTTP to run a search.

Use a [Search request JSON payload](search-request-params.md) to control how the Search Service returns results.

For more information about how to run a search with the REST API, see [Run a Simple Search with the REST API and curl/HTTP](simple-search-rest-api.md).

For more information about how to configure a Search index and search for geospatial data, see [Run a Geospatial Search Query with the REST API and curl/HTTP](geo-search-rest-api.md).

## [](#sql)Run a Search with a SQL++ Query

Use the [Query tab](../tools/query-workbench.md) to search using natural-language search and SQL++ features in the same query.

When using SQL++ with a hybrid [Vector Search](../vector-search/vector-search.md) query, you have more flexibility in how you choose to display your search results. When running a hybrid search with the [Server Web Console](#ui) or [REST API](#api), the Search Service displays results as a disjunct (`OR`) between your 2 search queries. For example:

{
    "query":
    {
        "match_phrase": "my regular query"
    }
}

OR

{
    "knn": [
        "k": 5,
        "field": "vector_field",
        "vector": [0, 0, 128]
    ]
}

SQL++ allows you to choose whether to return search results as a conjunct (`AND`) or a disjunct (`OR`) between for hybrid search queries.

As a conjunct, the Search Service:

* Returns matches that score highly for both the regular Search query and the Vector Search query.
* Excludes matches that only match the Vector Search query.

For example:

```sqlpp
SELECT meta().id FROM <key_space>
WHERE text = "content"
AND SEARCH(<key_space>, {"query": {"match": "content", "field": "text"}, "knn": {"vector": <vector_embedding>", "field": "vector_field", "k": 5}});
```

As a disjunct, the Search Service:

* Returns matches for the regular Search query, followed by matches for the Vector Search query.

As a result, you could see matches for the Vector Search query that do not contain matches for the regular Search query.

For example:

```sqlpp
SELECT meta().id FROM <key_space>
WHERE SEARCH (<key_space>, {"query": {"match": "content", "field": "text"}, "knn": {"vector": <vector_embedding>", "field": "vector_field", "k": 5}});
```

For more information about how to use the Search Service from a SQL++ query, see [Search Functions](../n1ql/n1ql-language-reference/searchfun.md).

## [](#see-also)See Also

* [Create a Search Index](create-search-indexes.md)
* [Customize a Search Index with the Web Console](customize-index.md)
* [Create Search Index Aliases](index-aliases.md)
* [Collect Additional Information with Search Facets](search-facets.md)