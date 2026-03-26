---
title: Search
description: You can use the Full Text Search service (FTS) to create queryable
  full-text indexes in Couchbase Server.
editUrl: https://github.com/couchbase/docs-sdk-python/edit/temp/4.4/modules/howtos/pages/full-text-searching-with-sdk.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:4.4@python-sdk:howtos:full-text-searching-with-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-sdk/4.4/howtos/full-text-searching-with-sdk.html)

# Search

> You can use the Full Text Search service (FTS) to create queryable full-text indexes in Couchbase Server. 

Full Text Search or FTS allows you to create, manage and query full text indexes on JSON documents stored in Couchbase buckets. It uses natural language processing for indexing and querying documents, provides relevance scoring on the results of your queries and has fast indexes for querying a wide range of possible text searches.

Some of the supported query-types include simple queries like Match and Term queries, range queries like Date Range and Numeric Range and compound queries for conjunctions, disjunctions and/or boolean queries.

The Full Text Search service also supports vector search from Couchbase Server 7.6 onwards.

## [](#getting-started)Getting Started

After familiarizing yourself with how to create and query a Search index in the UI you can query it from the SDK.

There are two APIs for querying search: `cluster.searchQuery()`, and `cluster.search()`. Both are also available at the Scope level.

The former API supports FTS queries (`SearchQuery`), while the latter additionally supports the `VectorSearch` added in 7.6\. Most of this documentation will focus on the former API, as the latter is in @Stability.Volatile status.

We will perform an FTS query here - see the [Vector Search](#vector-search) section for examples of that.

```python
from couchbase.cluster import Cluster
from couchbase.options import ClusterOptions, SearchOptions
from couchbase.auth import PasswordAuthenticator
from couchbase.exceptions import CouchbaseException
import couchbase.search as search

auth = PasswordAuthenticator('Administrator', 'password')
cluster = Cluster.connect('couchbase://your-ip', ClusterOptions(auth))
bucket = cluster.bucket('travel-sample')
scope = bucket.scope('inventory')
collection = scope.collection('hotel')

try:
    result = cluster.search_query('travel-sample-index',
                                  search.QueryStringQuery('Paris'))

    for row in result.rows():
        print(f'Found row: {row}')

    print(f'Reported total rows: {result.metadata().metrics().total_rows()}')

except CouchbaseException as ex:
    import traceback
    traceback.print_exc()
```

> [!NOTE]
> When using a Couchbase version < 6.5 you must create a valid Bucket connection using `cluster.bucket(name)` before you can use Search.

Let's break it down. The `search_query` API takes the name of the index and the type of query as required arguments and then allows to provide additional options if needed (in the example above, no options are specified).

Once a result returns you can iterate over the returned rows, and/or access the `search.metadata` associated with the query.

## [](#search-queries)Search Queries

The second mandatory argument in the example above used `QueryStringQuery("query")` to specify the query to run against the search index. The query string is the simplest form, but there are many more available. The table below lists all of them with a short description of each. You can combine them with `conjuncts` and `disjuncts` respectively. `Location` objects are specified as a `Tuple[SupportsFloat,SupportsFloat]` of longitude and latitude respectively.

__Table 1\. Available Search Queries__
| Name                                                              | Description                                                                                                                        |
| ----------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| QueryStringQuery(query: str)                                      | Accept query strings, which express query-requirements in a special syntax.                                                        |
| MatchQuery(match: str)                                            | A match query analyzes input text, and uses the results to query an index.                                                         |
| MatchPhraseQuery(match\_phrase: str)                              | The input text is analyzed, and a phrase query is built with the terms resulting from the analysis.                                |
| PrefixQuery(prefix: str)                                          | A prefix query finds documents containing terms that start with the specified prefix.                                              |
| RegexQuery(regexp: str)                                           | A regexp query finds documents containing terms that match the specified regular expression.                                       |
| TermRangeQuery()                                                  | A term range query finds documents containing a term in the specified field within the specified range.                            |
| NumericRangeQuery()                                               | A numeric range query finds documents containing a numeric value in the specified field within the specified range.                |
| DateRangeQuery()                                                  | A date range query finds documents containing a date value, in the specified field within the specified range.                     |
| DisjunctionQuery(\*queries: SearchQuery)                          | A disjunction query contains multiple child queries. Its result documents must satisfy a configurable min number of child queries. |
| ConjunctionQuery(\*queries: SearchQuery)                          | A conjunction query contains multiple child queries. Its result documents must satisfy all of the child queries.                   |
| WildcardQuery(wildcard: str)                                      | A wildcard query uses a wildcard expression, to search within individual terms for matches.                                        |
| DocIdQuery(\*ids: str)                                            | A doc ID query returns the indexed document or documents among the specified set.                                                  |
| BooleanFieldQuery(value: bool)                                    | A boolean field query searches fields that contain boolean true or false values.                                                   |
| TermQuery(term: str)                                              | Performs an exact match in the index for the provided term.                                                                        |
| PhraseQuery(\*terms: str)                                         | A phrase query searches for terms occurring in the specified position and offsets.                                                 |
| MatchAllQuery()                                                   | Matches all documents in an index, irrespective of terms.                                                                          |
| MatchNoneQuery()                                                  | Matches no documents in the index.                                                                                                 |
| GeoBoundingBoxQuery(top\_left: Location, bottom\_right: Location) | Searches inside the given bounding box coordinates.                                                                                |
| GeoDistanceQuery(distance: str, location: Location )              | Searches inside the distance from the given location coordinate.                                                                   |

## [](#the-search-result)The Search Result

Once the Search query is executed successfully, the server starts sending back the resultant hits.

```python
result = cluster.search_query('travel-sample-index',
                              search.PrefixQuery('swim'),
                              SearchOptions(fields=['description']))

for row in result.rows():
    print(f'Score: {row.score}')
    print(f'Document Id: {row.id}')

    # print fields included in query:
    print(row.fields)
```

The `SearchRow` contains the following methods:

__Table 2\. SearchRow__
| index → str                                 | The name of the FTS index that gave this result.                |
| ------------------------------------------- | --------------------------------------------------------------- |
| id → str                                    | The id of the matching document.                                |
| score →float                                | The score of this hit.                                          |
| explanation → str                           | If enabled provides an explanation in JSON form.                |
| locations → SearchRowLocations              | The individual locations of the hits.                           |
| fragments → Optional\[Mapping\[str, str\]\] | The fragments for each field that was requested as highlighted. |
| fields → Dict\[str, Any\]                   | Access to the returned fields.                                  |

Note that the `SearchMetaData` also contains potential `errors`, because the SDK will keep streaming results if the initial response came back successfully. This makes sure that even with partial data usually Search results are useable, so if you absolutely need to check if all partitions are present in the result double check the error (and not only catch an exception on the query itself).

## [](#scoped-vs-global-indexes)Scoped vs Global Indexes

The FTS APIs exist at both the `Cluster` and `Scope` levels.

This is because FTS supports, as of Couchbase Server 7.6, a new form of "scoped index" in addition to the traditional "global index".

It's important to use the `Cluster.searchQuery()` / `Cluster.search()` for global indexes, and `Scope.search()` for scoped indexes.

## [](#vector-search)Vector Search

As of Couchbase Server 7.6, the FTS service supports vector search in additional to traditional full text search queries.

### [](#examples)Examples

#### [](#single-vector-query)Single vector query

In this first example we are performing a single vector query:

```python
# NOTE: new imports needed for vector search
from couchbase.vector_search import VectorQuery, VectorSearch

vector_search = VectorSearch.from_vector_query(VectorQuery('vector_field',
                                                           query_vector))
request = search.SearchRequest.create(vector_search)
result = scope.search('vector-index', request)
```

Let's break this down. We create a `SearchRequest`, which can contain a traditional FTS query `SearchQuery` and/or the new `VectorSearch`. Here we are just using the latter.

The `VectorSearch` allows us to perform one or more `VectorQuery` s.

The `VectorQuery` itself takes the name of the document field that contains embedded vectors ("vector\_field" here), plus actual vector query in the form of a `float[]`.

(Note that Couchbase itself is not involved in generating the vectors, and these will come from an external source such as an embeddings API.)

Finally we execute the `SearchRequest` against the FTS index "vector-index", which has previously been setup to vector index the "vector\_field" field.

This happens to be a scoped index so we are using `scope.search()`. If it was a global index we would use `cluster.search()` instead - see [Scoped vs Global Indexes](#scoped-vs-global-indexes).

It returns the same `SearchResult` detailed earlier.

#### [](#multiple-vector-queries)Multiple vector queries

You can run multiple vector queries together:

```python
request = search.SearchRequest.create(VectorSearch([
    VectorQuery.create('vector_field',
                       query_vector,
                       num_candidates=2,
                       boost=0.3),
    VectorQuery.create('vector_field',
                       another_query_vector,
                       num_candidates=5,
                       boost=0.7)
]))
result = scope.search('vector-index', request)
```

How the results are combined (ANDed or ORed) can be controlled with `vector_query_combination` in `VectorSearchOptions`.

#### [](#combining-fts-and-vector-queries)Combining FTS and vector queries

You can combine a traditional FTS query with vector queries:

```python
request = (search.SearchRequest.create(search.MatchAllQuery())
           .with_vector_search(VectorSearch.from_vector_query(VectorQuery('vector_field',
                                                                          query_vector))))
result = scope.search('vector-and-fts-index', request)
```

How the results are combined (ANDed or ORed) can be controlled with `vector_query_combination` in `VectorSearchOptions`.

#### [](#fts-queries)FTS queries

And note that traditional FTS queries, without vector search, are also supported with the new `cluster.search()` / `scope.search()` APIs:

```python
request = search.SearchRequest.create(search.MatchAllQuery())
result = scope.search('travel-sample-index', request)
```

The `SearchQuery` is created in the same way as detailed earlier.

## [](#search-options)Search Options

The `cluster.search_query` function provides an array of named parameters to customize your query via `**kwargs` or `SearchOptions`. The following table lists them all:

__Table 3\. Available Search Options__
| Name                                     | Description                                                          |
| ---------------------------------------- | -------------------------------------------------------------------- |
| limit: int                               | Allows to limit the number of hits returned.                         |
| skip: int                                | Allows to skip the first N hits of the results returned.             |
| explain: bool                            | Adds additional explain debug information to the result.             |
| scan\_consistency: SearchScanConsistency | Specifies a different consistency level for the result hits.         |
| consistent\_with: MutationState          | Allows to be consistent with previously performed mutations.         |
| highlight\_style: HighlightStyle         | Specifies highlighting rules for matched fields.                     |
| highlight\_fields: List\[str\]           | Specifies fields to highlight.                                       |
| sort: List\[str\]                        | Allows to provide custom sorting rules.                              |
| facets: Map\[str, SearchFacet\]          | Allows to fetch facets in addition to the regular hits.              |
| fields: List\[str\]                      | Specifies fields to be included.                                     |
| raw: JSON                                | Escape hatch to add arguments that are not covered by these options. |
| collections: List\[str\]                 | Limits the search query to a specific list of collection names.      |

### [](#limit-and-skip)Limit and Skip

It is possible to limit the returned results to a maximum amount using the `limit` option. If you want to skip the first N records it can be done with the `skip` option.

```python
result = cluster.search_query('travel-sample-index',
                              search.TermQuery('swanky'),
                              SearchOptions(limit=4, skip=3))
```

### [](#scanconsistency-and-consistentwith)ScanConsistency and ConsistentWith

By default, all Search queries will return the data from whatever is in the index at the time of query. These semantics can be tuned if needed so that the hits returned include the most recently performed mutations, at the cost of slightly higher latency since the index needs to be updated first.

There are two ways to control consistency: either by supplying a custom `SearchScanConsistency` or using `consistentWith`. At the moment the cluster only supports `consistentWith`, which is why you only see `SearchScanConsistency.NOT_BOUNDED` in the enum which is the default setting. The way to make sure that recently written documents show up in the rfc works as follows (commonly referred to "read your own writes" — RYOW):

Scan consistency example:

```python
result = cluster.search_query('travel-sample-index',
                              search.TermQuery('swanky'),
                              SearchOptions(scan_consistency=SearchScanConsistency.NOT_BOUNDED))
```

ConsistentWith consistency example:

```python
res = collection.upsert(f'hotel_example-123456', {'description': 'swanky'})
ms = MutationState(res)
result = cluster.search_query('travel-sample-index',
                              search.QueryStringQuery('swanky'),
                              SearchOptions(consistent_with=ms))
```

### [](#highlight)Highlight

It is possible to enable highlighting for matched fields. You can either rely on the default highlighting style or provide a specific one. The following snippet uses HTML formatting for two fields:

```python
result = cluster.search_query('travel-sample-index',
                              search.TermQuery('downtown'),
                              SearchOptions(highlight_style=HighlightStyle.Html,
                                            highlight_fields=['description', 'name']))
```

### [](#sort)Sort

By default the Search Engine will sort the results in descending order by score. This behavior can be modified by providing a different sorting order which can also be nested.

```python
result = cluster.search_query('travel-sample-index',
                              search.TermQuery('downtown'),
                              SearchOptions(sort=['_score', 'description']))
```

### [](#facets)Facets

Facets are aggregate information collected on a result set and are useful when it comes to categorization of result data. The SDK allows you to provide many different facet configurations to the Search Engine, the following example shows how to create a facet based on a term. Other possible facets include numeric and date ranges.

```python
facet_name = 'activity'
facet = TermFacet('activity')
query = TermQuery('home')
q_res = cluster.search_query('travel-sample-index',
                            query,
                            SearchOptions(limit=10, facets={facet_name: facet}))

for row in q_res.rows():
    print(f'Found row: {row}')

print(f'facets: {q_res.facets()}')
```

### [](#fields)Fields

You can tell the Search Engine to include the full content of a certain number of indexed fields in the response.

```python
result = cluster.search_query('travel-sample-index',
                              search.TermQuery('swanky'),
                              SearchOptions(fields=['name', 'description']))
```

### [](#collections)Collections

It is now possible to limit the search query to a specific list of collection names.

Note that this feature is only supported with Couchbase Server 7.0 or later.

```python
result = cluster.search_query('travel-sample-index',
                              search.QueryStringQuery('San Francisco'),
                              SearchOptions(collections=['landmark', 'airport']))
```

## [](#async-apis)Async APIs

In addition to the blocking API on `Cluster`, the SDK provides asyncio and Twisted APIs on `ACluster` or `TxCluster` respectively. If you are in doubt of which API to use, we recommend looking at the asyncio API first.

Simple queries with both asyncio and Twisted APIs look similar to the blocking one:

ACouchbase

```python
from acouchbase.cluster import Cluster, get_event_loop
from couchbase.options import ClusterOptions
from couchbase.auth import PasswordAuthenticator
from couchbase.exceptions import CouchbaseException
import couchbase.search as search


async def get_couchbase():
    cluster = Cluster(
        "couchbase://your-ip",
        ClusterOptions(PasswordAuthenticator("Administrator", "password")))
    bucket = cluster.bucket("travel-sample")
    await bucket.on_connect()
    collection = bucket.default_collection()

    return cluster, bucket, collection

# NOTE: the travel-sample-index search index might need to be created
async def simple_query(cluster):
    try:
        result = cluster.search_query(
            "travel-sample-index", search.QueryStringQuery("swanky"))

        async for row in result:
            print("Found row: {}".format(row))
        
    except CouchbaseException as ex:
        print(ex)


loop = get_event_loop()
cluster, bucket, collection = loop.run_until_complete(get_couchbase())
loop.run_until_complete(simple_query(cluster))
```

TxCouchbase

```python
# **IMPORTANT** need to do this import prior to importing the reactor (new to the Python 4.x SDK)
import txcouchbase
from twisted.internet import reactor

from txcouchbase.cluster import TxCluster
from couchbase.options import ClusterOptions
from couchbase.auth import PasswordAuthenticator
import couchbase.search as search


def handle_query_results(result):
    for r in result.rows():
        print("query row: {}".format(r))
    print("loop finished")
    reactor.stop()


def on_streaming_error(error):
    print("Streaming operation had an error.\nError: {}".format(error))
    reactor.stop()

# NOTE: the travel-sample-index search index might need to be created
def on_connect_ok(result, cluster):
    # create a bucket object
    bucket = cluster.bucket("travel-sample")
    # create a collection object
    cb = bucket.default_collection()

    d = cluster.search_query("travel-sample-index", search.QueryStringQuery("swanky"))
    d.addCallback(handle_query_results).addErrback(on_streaming_error)


def on_connect_err(error):
    print(f"Unable to connect.\n{error}")


cluster = TxCluster("couchbase://your-ip",
                    ClusterOptions(PasswordAuthenticator("Administrator", "password")))

# wait for connect
cluster.on_connect().addCallback(on_connect_ok, cluster).addErrback(on_connect_err)

reactor.run()
```