---
title: Vector Search
description: Vector Search from the SDK, to enable AI integration, semantic
  search, and use of RAG frameworks.
editUrl: https://github.com/couchbase/docs-sdk-go/edit/temp/2.11/modules/howtos/pages/vector-searching-with-sdk.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:go-sdk:howtos:vector-searching-with-sdk.adoc[]
---

[View original HTML](/go-sdk/current/howtos/vector-searching-with-sdk.html)

# Vector Search

> Vector Search from the SDK, to enable AI integration, semantic search, and use of RAG frameworks. 

Vector Search has been available in Couchbase Capella Operational and self-managed Server since version 7.6, using the Couchbase Search Service. Version 8.0 introduces vector query using Global Secondary Indexes (GSI), the Query Service index — using either a fast Hyperscale index, or a composite index to combine scalar queries with semantic search.

For fast and scalable vector queries, use one of the above two GSI choices — detailed in the next section. If you don’t require the speed and scale of vector query with GSI, or need to combine vector, geo-spatial search, range search, and traditional fuzzy text searches, then consider [Vector Search With the Search Service](#vector-search-with-the-search-service).

## [](#vector-search-with-the-query-service-and-gsi)Vector Search With the Query Service and GSI

From the SDK, a vector query using GSI is the same as any other query. However, you will need to build one or more indexes.

### [](#prerequisites)Prerequisites

* Couchbase Server 8.0.0 or newer — or a recent Capella instance.
* Your chosen [vector index](../../../server/current/vector-index/use-vector-indexes.md) — hyperscale or composite.

You will need to refer to the [Use Vector Indexes for AI Applications](../../../server/current/vector-index/vectors-and-indexes-overview.md) pages for a full discussion of using Vector Indexes with Vector Queries. In particular, you will need to [create a Vector Index](../../../server/current/vector-index/hyperscale-filter.md#creating-a-hyperscale-vector-index-with-included-scalar-values).

### [](#examples)Examples

The [Use Vector Indexes for AI Applications](../../../server/current/vector-index/vectors-and-indexes-overview.md) pages contain examples using both hyperscale and compound indexes.

Here is the [Hyperscale Index](../../../server/current/vector-index/hyperscale-vector-index.md#query-example) example, wrapped inside the Go SDK Query API.

Hyperscale Index Example

```go
		query := "SELECT d.id, d.question, d.wanted_similar_color_from_search, " +
			"ARRAY_CONCAT( " +
			"d.couchbase_search_query.knn[0].vector[0:4], " +
			"['...'] " +
			") AS vector " +
			"FROM `vector-sample`.`color`.`rgb-questions` AS d " +
			"WHERE d.id = '#87CEEB';"

		rows, err := cluster.Query(query, &gocb.QueryOptions{Metrics: true})

		// check query was successful
		if err != nil {
			panic(err)
		}

		// iterate over rows
		for rows.Next() {
			var r interface{}
			err := rows.Row(&r)
			if err != nil {
				panic(err)
			}
			fmt.Println(r)
		}

		// always check for errors after iterating
		err = rows.Err()
		if err != nil {
			panic(err)
		}
```

Parameterizing the query, as with [regular queries](#sqlpp-queries-with-sdk.adoc#parameterized-queries), will allow the reuse of the [Query Plan](../../../server/current/n1ql/n1ql-intro/queriesandresults.md#prepare-stmts). This can be more efficient, unless you are doing a lot of optimization to your query.

Parameterized Vector Query

```go
		query := "SELECT d.id, d.question, d.wanted_similar_color_from_search, " +
			"ARRAY_CONCAT( " +
			"d.couchbase_search_query.knn[0].vector[0:4], " +
			"['...'] " +
			") AS vector " +
			"FROM `vector-sample`.`color`.`rgb-questions` AS d " +
			"WHERE d.id = $id;"

		rows, err := cluster.Query(query, &gocb.QueryOptions{
			NamedParameters: map[string]interface{}{
				"id": "#87CEEB",
			},
		})

		// check query was successful
		if err != nil {
			panic(err)
		}

		// iterate over rows
		for rows.Next() {
			var r interface{}
			err := rows.Row(&r)
			if err != nil {
				panic(err)
			}
			fmt.Println(r)
		}

		// always check for errors after iterating
		err = rows.Err()
		if err != nil {
			panic(err)
		}
```

## [](#vector-search-with-the-search-service)Vector Search With the Search Service

Vector search is also implemented using [Search Indexes](full-text-searching-with-sdk.md), and can be combined with traditional full text search queries. Vector embeddings can be an array of floats or a [base64 encoded string](../../../server/current/vector-search/run-vector-search-ui.md#base64).

### [](#prerequisites-2)Prerequisites

Couchbase Server 7.6.0 (7.6.2 for base64-encoded vectors) — or a Capella Operational cluster.

### [](#examples-2)Examples

#### [](#single-vector-query)Single vector query

In this first example we are performing a single vector query:

```go
		request := gocb.SearchRequest{
			VectorSearch: vector.NewSearch(
				[]*vector.Query{
					vector.NewQuery("vector_field", vectorQuery),
				}, nil,
			),
		}
		vectorResult, err := scope.Search("vector-index", request, nil)
		if err != nil {
			panic(err)
		}
```

Let’s break this down. We create a `SearchRequest`, which can contain a traditional FTS query `SearchQuery` and/or the new `VectorSearch`. Here we are just using the latter.

The `VectorSearch` allows us to perform one or more `VectorQuery` s.

The `VectorQuery` itself takes the name of the document field that contains embedded vectors ("vector\_field" here), plus actual vector query in the form of a `[]float32`.

(Note that Couchbase itself is not involved in generating the vectors, and these will come from an external source such as an embeddings API.)

Finally we execute the `SearchRequest` against the FTS index "travel-sample-index", which has previously been setup to vector index the "vector\_field" field.

This happens to be a scoped index so we are using `scope.Search()`. If it was a global index we would use `cluster.Search()` instead - see [\[Scoped vs Global Indexes\]](#Scoped vs Global Indexes).

It returns the same `SearchResult` detailed earlier.

#### [](#pre-filters)Pre-Filters

From Couchbase Server 7.6.4 — and in Capella Operational clusters — [pre-filtering with similarity search](../../../server/current/vector-search/pre-filtering-vector-search.md#about-pre-filtering) is available. This is a non-vector query that the server executes first to get an intermediate result. Then it executes the vector query on the intermediate result to get the final result.

```go
func (q *Query) Prefilter(query search.Query) *Query
```

If no prefilter is specified, the server executes the vector query on all indexed documents.

Simple Match

```go
vector.NewQuery("vector_field", vectorQuery).
	Prefilter(search.NewMatchQuery("primary").
		Field("color_wheel_pos")).
	NumCandidates(10)
```

Note that `NumCandidates` sets how many similar vectors are returned. If it is not set, then the Cluster’s default of `3` will be used — this corresponds with `k` on the Server side, for K-Nearest Neighbors.

The prefilter can be any Search Query — from a simple match, as above, to a string query:

String Query

```go
vector.NewQuery("vector_field", vectorQuery).
	Prefilter(search.NewQueryStringQuery("+description:sea -color_hex:fff5ee"))
```

See the [API reference](https://pkg.go.dev/github.com/couchbase/gocb/v2@v2.11.0/vector#Query.Prefilter).

#### [](#multiple-vector-queries)Multiple vector queries

You can run multiple vector queries together:

```go
		request := gocb.SearchRequest{
			VectorSearch: vector.NewSearch(
				[]*vector.Query{
					vector.NewQuery("vector_field", vectorQuery).NumCandidates(2).Boost(0.3),
					vector.NewQuery("vector_field", anotherVectorQuery).NumCandidates(5).Boost(0.7),
				},
				&vector.SearchOptions{
					VectorQueryCombination: vector.VectorQueryCombinationAnd,
				},
			),
		}
		vectorResult, err := scope.Search("vector-index", request, nil)
		if err != nil {
			panic(err)
		}
```

How the results are combined (ANDed or ORed) can be controlled with `vector.SearchOptions.VectorQueryCombination`.

#### [](#combining-fts-and-vector-queries)Combining FTS and vector queries

You can combine a traditional FTS query with vector queries:

```go
		request := gocb.SearchRequest{
			VectorSearch: vector.NewSearch(
				[]*vector.Query{
					vector.NewQuery("vector_field", vectorQuery).NumCandidates(2).Boost(0.3),
					vector.NewQuery("vector_field", anotherVectorQuery).NumCandidates(5).Boost(0.7),
				}, nil,
			),
			SearchQuery: search.NewMatchAllQuery(),
		}
		vectorResult, err := scope.Search("vector-and-fts-index", request, nil)
		if err != nil {
			panic(err)
		}
```

How the results are combined (ANDed or ORed) can be controlled with `vector.SearchOptions.VectorQueryCombination`.

Scoring for these hybrid search queries combines the boost multipliers to get to the final score.

hit_score = (query_1_boost * query_1_hit_score) + (query_2_boost * query_2_hit_score)

### [](#query-methods)Query Methods

As part of the Search service, you can use the same [Search query methods](full-text-searching-with-sdk.md#search-queries) as regular Searches. See a fuller list, with Vector properties, in the [Capella docs](../../../cloud/search/search-request-params.md).

## [](#further-reading)Further Reading

### [](#vector-query)Vector Query

* [Vector Query for AI Apps docs (self-managed Couchbase Server)](../../../server/current/vector-index/vectors-and-indexes-overview.md).
* [Vector Query for AI Apps docs (Capella DBaaS)](#cloud::vector-index/vectors-and-indexes-overview.adoc)

### [](#vector-search)Vector Search

* [Vector Search for AI Apps docs (self-managed Couchbase Server)](../../../server/current/vector-search/vector-search.md)
* [Vector Search for AI Apps docs (Capella DBaaS)](#cloud::vector-search:vector-search.adoc)
* Vector Search in the [Go API reference](https://pkg.go.dev/github.com/couchbase/gocb/v2#SearchRequest.VectorSearch).