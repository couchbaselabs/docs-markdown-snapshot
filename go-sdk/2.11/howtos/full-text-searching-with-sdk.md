---
title: Search
description: You can use the Full Text Search service (FTS) to create queryable
  full-text indexes in Couchbase Server.
editUrl: https://github.com/couchbase/docs-sdk-go/edit/temp/2.11/modules/howtos/pages/full-text-searching-with-sdk.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.11@go-sdk:howtos:full-text-searching-with-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/go-sdk/2.11/howtos/full-text-searching-with-sdk.html)

# Search

> You can use the Full Text Search service (FTS) to create queryable full-text indexes in Couchbase Server. 

Full Text Search or FTS allows you to create, manage, and query full text indexes on JSON documents stored in Couchbase buckets. It uses natural language processing for querying documents, provides relevance scoring on the results of your queries, and has fast indexes for querying a wide range of possible text searches. Some of the supported query types include simple queries like Match and Term queries; range queries like Date Range and Numeric Range; and compound queries for conjunctions, disjunctions, and/or boolean queries. The Go SDK exposes an API for performing FTS queries which abstracts some of the complexity of using the underlying REST API.

## [](#getting-started)Getting Started

After familiarizing yourself with how to create and query a search index in the UI you can query it from the SDK. From Couchbase Server 7.6, Search queries are executed at the Scope level, or the Cluster level — for earlier versions of Couchbase, it’s just the Cluster level. Search queries, facets, and sorting have a slightly different import from other components of `gocb`, you can import them using `import "github.com/couchbase/gocb/v2/search"`.

There are two APIs for querying search: `cluster.SearchQuery()`, and `cluster.Search()`. Both are also available at the Scope level.

The former API supports FTS queries (`SearchQuery`), while the latter additionally supports the `VectorSearch` added in 7.6\. Most of this documentation will focus on the former API, as the latter is in @Stability.Volatile status.

We will perform an FTS query here - see the [Vector Search](#vector-search) section for examples of that. Here is a simple MatchQuery that looks for the text “swanky” using a defined index:

```go
	cluster, err := gocb.Connect("localhost", opts)
	if err != nil {
		panic(err)
	}

	// For Server versions 6.5 or later you do not need to open a bucket here
	bucket := cluster.Bucket("travel-sample")

	// We wait until the bucket is definitely connected and setup.
	// For Server versions 6.5 or later if we hadn't opened a bucket then we could use cluster.WaitUntilReady here.
	err = bucket.WaitUntilReady(5*time.Second, nil)
	if err != nil {
		panic(err)
	}

	matchResult, err := cluster.SearchQuery(
		"travel-sample-index",
		search.NewMatchQuery("swanky"),
		&gocb.SearchOptions{
			Limit:  10,
			Fields: []string{"description"},
		},
	)
	if err != nil {
		panic(err)
	}
```

We have also included the `Fields` option which will get the content of the specified (indexed) field as a part of the response.

All simple query types are created in the same manner, although some have additional properties, which can be seen in common query type descriptions. Couchbase FTS’s [range of query types](#8.0@server:fts:fts-query-types.adoc) enable powerful searching using multiple options, to ensure results are just within the range wanted. Here is a date range query that looks for dates between 1st January 2019 and 1st February, the second parameter is whether the date should be considered inclusive:

```go
	dateRangeResult, err := cluster.SearchQuery(
		"travel-sample-index",
		search.NewDateRangeQuery().Start("2019-01-01", true).End("2019-02-01", false),
		&gocb.SearchOptions{
			Limit: 10,
		},
	)
	if err != nil {
		panic(err)
	}
```

Queries can also be combined together. A conjunction query contains multiple child queries; its result documents must satisfy all of the child queries:

```go
	conjunctionResult, err := cluster.SearchQuery(
		"travel-sample-index",
		search.NewConjunctionQuery(
			search.NewMatchQuery("swanky"),
			search.NewDateRangeQuery().Start("2019-01-01", true).End("2019-02-01", false),
		),
		&gocb.SearchOptions{
			Limit: 10,
		},
	)
	if err != nil {
		panic(err)
	}
```

## [](#working-with-results)Working with Results

The result of a search query has three components: rows, facets, and metdata. Rows are the documents that match the query. Facets allow the aggregation of information collected on a particular result set. Metdata holds additional information not directly related to your query, such as success total hits and how long the query took to execute in the cluster.

Iterating Rows

Here we are iterating over the rows that were returned in the results. Note that `Fields` is a special case, where it’s a function. `Fields` will include any fields that were requested as part of the SearchQuery (`Fields` option within the options block).

```go
	for matchResult.Next() {
		row := matchResult.Row()
		docID := row.ID
		score := row.Score

		var fields interface{}
		err := row.Fields(&fields)
		if err != nil {
			panic(err)
		}

		fmt.Printf("Document ID: %s, search score: %f, fields included in result: %v\n", docID, score, fields)
	}

	// always check for errors after iterating
	err = matchResult.Err()
	if err != nil {
		panic(err)
	}
```

Take care to ensure you call `Err` after accessing rows and check for any errors returned.

Iterating facets

Facets can only be accessed once all the rows have been iterated.

```go
	facetsResult, err := cluster.SearchQuery(
		"travel-sample-index",
		search.NewMatchAllQuery(),
		&gocb.SearchOptions{
			Limit: 10,
			Facets: map[string]search.Facet{
				"type": search.NewTermFacet("type", 5),
			},
		},
	)
	if err != nil {
		panic(err)
	}

	for facetsResult.Next() {
	}

	facets, err := facetsResult.Facets()
	if err != nil {
		panic(err)
	}
	for _, facet := range facets {
		field := facet.Field
		total := facet.Total

		fmt.Printf("Facet field: %s, total: %d\n", field, total)
	}
```

## [](#scoped-vs-global-indexes)Scoped vs Global Indexes

The FTS APIs exist at both the `Cluster` and `Scope` levels.

This is because FTS supports, as of Couchbase Server 7.6, a new form of "scoped index" in addition to the traditional "global index".

It’s important to use the `Cluster.searchQuery()` / `Cluster.search()` for global indexes, and `Scope.search()` for scoped indexes.

## [](#vector-search)Vector Search

As of Couchbase Server 7.6, the FTS service supports vector search in additional to traditional full text search queries.

Vector search queries have a slightly different import from other components of `gocb`, you can import them using `import "github.com/couchbase/gocb/v2/vector"`.

### [](#examples)Examples

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

This happens to be a scoped index so we are using `scope.Search()`. If it was a global index we would use `cluster.Search()` instead - see [Scoped vs Global Indexes](#scoped-vs-global-indexes).

It returns the same `SearchResult` detailed earlier.

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

#### [](#fts-queries)FTS queries

And note that traditional FTS queries, without vector search, are also supported with the new `cluster.Search()` / `scope.Search()` APIs:

```go
		request := gocb.SearchRequest{
			SearchQuery: search.NewMatchQuery("swanky"),
		}

		result, err := scope.Search("travel-sample-index", request, nil)
		if err != nil {
			panic(err)
		}
```

The `SearchQuery` is created in the same way as detailed earlier.

## [](#consistency)Consistency

Like the Couchbase Query Service, FTS allows `RequestPlus` queries — _Read-Your-Own\_Writes (RYOW)_ consistency, ensuring results contain information from updated indexes:

```go
	collection := bucket.Scope("inventory").Collection("hotel")

	hotel := struct {
		Description string `json:"description"`
	}{Description: "super swanky"}
	myWriteResult, err := collection.Upsert("a-new-hotel", hotel, nil)
	if err != nil {
		panic(err)
	}
	time.Sleep(5 * time.Second)

	consistentWithResult, err := cluster.SearchQuery(
		"travel-sample-index",
		search.NewMatchQuery("swanky"),
		&gocb.SearchOptions{
			Limit:          10,
			ConsistentWith: gocb.NewMutationState(*myWriteResult.MutationToken()),
		},
	)
	if err != nil {
		panic(err)
	}
```