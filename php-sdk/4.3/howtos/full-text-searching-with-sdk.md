---
title: Search
description: You can use the Full Text Search service (FTS) to create queryable
  full-text indexes in Couchbase Server.
editUrl: https://github.com/couchbase/docs-sdk-php/edit/temp/4.3/modules/howtos/pages/full-text-searching-with-sdk.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:4.3@php-sdk:howtos:full-text-searching-with-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/php-sdk/4.3/howtos/full-text-searching-with-sdk.html)

# Search

> You can use the Full Text Search service (FTS) to create queryable full-text indexes in Couchbase Server. 

Full Text Search or FTS allows you to create, manage, and query full text indexes on JSON documents stored in Couchbase buckets. It uses natural language processing for querying documents, provides relevance scoring on the results of your queries, and has fast indexes for querying a wide range of possible text searches.

Some of the supported query types include simple queries like Match and Term queries; range queries like Date Range and Numeric Range; and compound queries for conjunctions, disjunctions, and/or boolean queries.

The PHP SDK exposes an API for performing FTS queries which abstracts some of the complexity of using the underlying REST API.

There are two APIs for querying search: `cluster.searchQuery()`, and `cluster.search()`. Both are also available at the Scope level.

The former API supports FTS queries (`SearchQuery`), while the latter additionally supports the `VectorSearch` added in 7.6\. Most of this documentation will focus on the former API, as the latter is in @Stability.Volatile status.

We will perform an FTS query here - see the [Vector Search](#vector-search) section for examples of that.

## [](#examples)Examples

For the purposes of the below examples we will use the Travel Sample sample bucket with the below Full Text Search index (dynamic mapping for type `hotel`).

```json
{
  "type": "fulltext-index",
  "name": "travel-sample-index",
  "uuid": "ea630dfe35e1f415",
  "sourceType": "couchbase",
  "sourceName": "travel-sample",
  "sourceUUID": "8ee9d874356f4c92a63a244f5e34210a",
  "planParams": {
    "maxPartitionsPerPIndex": 171,
    "indexPartitions": 6
  },
  "params": {
    "doc_config": {
      "docid_prefix_delim": "",
      "docid_regexp": "",
      "mode": "type_field",
      "type_field": "type"
    },
    "mapping": {
      "analysis": {},
      "default_analyzer": "standard",
      "default_datetime_parser": "dateTimeOptional",
      "default_field": "_all",
      "default_mapping": {
        "dynamic": true,
        "enabled": true
      },
      "default_type": "_default",
      "docvalues_dynamic": true,
      "index_dynamic": true,
      "store_dynamic": false,
      "type_field": "_type"
    },
    "store": {
      "indexType": "scorch"
    }
  },
  "sourceParams": {}
}
```

Search queries are executed at Cluster level (not bucket or collection). As of Couchbase Server 6.5+ they do also not require a bucket to be opened first. In older versions of Couchbase Server, even though executed at Cluster level, a bucket must be opened before performing queries.

Here is a simple MatchQuery that looks for the text “swanky” using a defined index:

```php
$matchQuery = new MatchSearchQuery("swanky");
$matchQuery->field("reviews.content");
$opts = new SearchOptions();
$opts->limit(10);
$res = $cluster->searchQuery("travel-sample-index", $matchQuery, $opts);
printf("Match query: \"swanky\":\n");
foreach ($res->rows() as $row) {
    printf("id: %s, score: %f\n", $row['id'], $row['score']);
}
```

All simple query types are created in the same manner, although some have additional properties, which can be seen in common query type descriptions. Couchbase FTS’s [range of query types](#7.1@server:fts:fts-query-types.adoc) enable powerful searching using multiple options, to ensure results are just within the range wanted. Here is a numeric range query that looks for hotels with `"Cleanliness"` ratings higher than `5`:

```php
$numericRangeQuery = new NumericRangeSearchQuery();
$numericRangeQuery->field("reviews.ratings.Cleanliness")->min(5);
$opts = new SearchOptions();
$opts->limit(10);
$res = $cluster->searchQuery("travel-sample-index", $numericRangeQuery, $opts);
printf("Cleanliness 5+:\n");
foreach ($res->rows() as $row) {
    printf("id: %s, score: %f\n", $row['id'], $row['score']);
}
```

Queries can also be combined together. A conjunction query contains multiple child queries; its result documents must satisfy all of the child queries:

```php
$conjunction = new ConjunctionSearchQuery([$matchQuery, $numericRangeQuery]);
$opts = new SearchOptions();
$opts->limit(10);
$res = $cluster->searchQuery("travel-sample-index", $conjunction, $opts);
printf("Swanky and with cleanliness 5+:\n");
foreach ($res->rows() as $row) {
    printf("id: %s, score: %f\n", $row['id'], $row['score']);
}
```

## [](#working-with-results)Working with Results

The result of a search query has three components: rows, facets, and metdata. Rows are the documents that match the query. Facets allow the aggregation of information collected on a particular result set. Metdata holds additional information not directly related to your query, such as success total hits and how long the query took to execute in the cluster.

### [](#iterating-rows)Iterating Rows

Here we are iterating over the rows that were returned in the results (for context, see the same in the two samples below this one):

```php
foreach ($res->rows() as $row) {
    printf("id: %s, score: %f\n", $row['id'], $row['score']);
}
```

### [](#facets)Facets

Facets can only be accessed once `Close` has been called on rows.

```php
$query = (new TermSearchQuery("beer"))->field("type");
$options = new SearchOptions();
$options->facets([
    "foo" => new TermSearchFacet("name", 3),
    "bar" => (new DateRangeSearchFacet("updated", 1))
                ->addRange("old", NULL,  mktime(0, 0, 0, 1, 1, 2014)), // "2014-01-01T00:00:00" also acceptable
    "baz" => (new NumericRangeSearchFacet("abv", 2))
                ->addRange("strong", 4.9, NULL)
                ->addRange("light", NULL, 4.89)
]);
$res = $cluster->searchQuery("beer-search", $query, $options);

$facet = $res->facets()["foo"];
printf("Term facet \"foo\" on field \"%s\". Total: %d, missing: %d: other: %d\n",
    $facet["field"], $facet["total"], $facet["missing"], $facet["other"]);
foreach ($facet["terms"] as $term) {
    printf(" * %-5s ... %d\n", $term["term"], $term["count"]);
}

$facet = $res->facets()["bar"];
printf("Date range facet \"bar\" on field \"%s\". Total: %d, missing: %d: other: %d\n",
    $facet["field"], $facet["total"], $facet["missing"], $facet["other"]);
foreach ($facet["date_ranges"] as $range) {
    printf(" * %-20s ... %d\n", $range["end"], $range["count"]);
}

$facet = $res->facets()["baz"];
printf("Numeric range facet \"baz\" on field \"%s\". Total: %d, missing: %d: other: %d\n",
    $facet["field"], $facet["total"], $facet["missing"], $facet["other"]);
foreach ($facet["numeric_ranges"] as $range) {
    if (isset($range["max"])) {
        printf(" * max %-4s ... %d\n", $range["max"], $range["count"]);
    } else {
        printf(" * min %-4s ... %d\n", $range["min"], $range["count"]);
    }
}
```

## [](#scoped-vs-global-indexes)Scoped vs Global Indexes

The FTS APIs exist at both the `Cluster` and `Scope` levels.

This is because FTS supports, as of Couchbase Server 7.6, a new form of "scoped index" in addition to the traditional "global index".

It’s important to use the `Cluster.searchQuery()` / `Cluster.search()` for global indexes, and `Scope.search()` for scoped indexes.

## [](#vector-search)Vector Search

As of Couchbase Server 7.6, the FTS service supports vector search in additional to traditional full text search queries.

### [](#examples-2)Examples

#### [](#single-vector-query)Single vector query

In this first example we are performing a single vector query:

```php
$request = SearchRequest::build(VectorSearch::build([
    VectorQuery::build("vector_field", $vectorQuery)
]));

$result = $scope->search("vector-index", $request);
```

Let’s break this down. We create a `SearchRequest`, which can contain a traditional FTS query `SearchQuery` and/or the new `VectorSearch`. Here we are just using the latter.

The `VectorSearch` allows us to perform one or more `VectorQuery` s.

The `VectorQuery` itself takes the name of the document field that contains embedded vectors ("vector\_field" here), plus actual vector query in the form of a `float[]`.

(Note that Couchbase itself is not involved in generating the vectors, and these will come from an external source such as an embeddings API.)

Finally we execute the `SearchRequest` against the FTS index "vector-index", which has previously been setup to vector index the "vector\_field" field.

This happens to be a scoped index so we are using `scope.search()`. If it was a global index we would use `cluster.search()` instead - see [Scoped vs Global Indexes](#scoped-vs-global-indexes).

It returns the same `SearchResult` detailed earlier.

#### [](#multiple-vector-queries)Multiple vector queries

You can run multiple vector queries together:

```php
$request = SearchRequest::build(VectorSearch::build([
    VectorQuery::build("vector_field", $vectorQuery)->numCandidates(2)->boost(0.3),
    VectorQuery::build("vector_field", $anotherVectorQuery)->numCandidates(5)->boost(0.7)
]));

$result = $scope->search("vector-index", $request);
```

How the results are combined (ANDed or ORed) can be controlled with `VectorSearchOptions→vectorQueryCombination()`.

#### [](#combining-fts-and-vector-queries)Combining FTS and vector queries

You can combine a traditional FTS query with vector queries:

```php
$request = SearchRequest::build(MatchAllSearchQuery::build());
$request->vectorSearch(VectorSearch::build([
    VectorQuery::build("vector_field", $vectorQuery)
]));

$result = $scope->search("vector-and-fts-index", $request);
```

#### [](#fts-queries)FTS queries

And note that traditional FTS queries, without vector search, are also supported with the new `cluster.search()` / `scope.search()` APIs:

```php
$request = SearchRequest::build(MatchAllSearchQuery::build());

$result = $scope->search("travel-sample-index", $request);
```

The `SearchQuery` is created in the same way as detailed earlier.

## [](#consistency)Consistency

Like the Couchbase Query Service, FTS allows `RequestPlus` queries — _Read-Your-Own\_Writes (RYOW)_ consistency, ensuring results contain information from updated indexes:

```php
// Create new hotel document and demonstrate query with consistency requirement
$scope = $cluster->bucket('travel-sample')->scope('inventory');
$collection = $scope->collection('hotel');
$hotel = [
    "name" => "super hotel",
    "reviews" => [
        [
            "content" => "Super swanky hotel!",
            "ratings" => [
                "Cleanliness" => 6
            ]
        ]
    ]
];
$res = $collection->upsert("a-new-hotel", $hotel);
$mutationState = new MutationState();
$mutationState->add($res);
$opts = new SearchOptions();
$opts->limit(10);
$opts->consistentWith("travel-sample-index", $mutationState);
$res = $cluster->searchQuery("travel-sample-index", $matchQuery, $opts);
printf("Match query: \"swanky\":\n");
foreach ($res->rows() as $row) {
    printf("id: %s, score: %f\n", $row['id'], $row['score']);
}
```

## [](#further-reading)Further Reading

* More details on Search Queries can be found [in the Server docs](#7.1@server:fts:fts-query-types.adoc).
* More information can be found in the API docs for [searchQuery](https://docs.couchbase.com/sdk-api/couchbase-php-client/classes/Couchbase-Cluster.html#method%5FsearchQuery) and [SearchResult](https://docs.couchbase.com/sdk-api/couchbase-php-client/classes/Couchbase-SearchResult.html).