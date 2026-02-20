---
title: Async APIs
description: The Couchbase Python SDK offers both asyncio and Twisted APIs for
  async operation.
editUrl: https://github.com/couchbase/docs-sdk-python/edit/temp/4.3/modules/howtos/pages/concurrent-async-apis.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:4.3@python-sdk:howtos:concurrent-async-apis.adoc[]
---

[View original HTML](/python-sdk/4.3/howtos/concurrent-async-apis.html)

# Async APIs

> The Couchbase Python SDK offers both asyncio and Twisted APIs for async operation. 

## [](#asyncio)Asyncio

To use the Python SDK with [asyncio](https://docs.python.org/3/library/asyncio.html), use the _acouchbase_ module. As opposed to the synchronous SDK methods which wait for completion and return `Result` objects, the _acouchbase_ methods return a `Future`. You may `await` the success or failure of the `Future`. If a `Future` is awaited, the method awaiting the task must have the `async` keyword in its signature. `Result` objects are obtained after `await` ing the `Future` as seen in the examples below.

Create an _acouchbase_ Cluster

```python

# needed for cluster creation
from acouchbase.cluster import Cluster
from couchbase.options import ClusterOptions
from couchbase.auth import PasswordAuthenticator


async def get_couchbase():
    cluster = Cluster(
        "couchbase://your-ip",
        ClusterOptions(PasswordAuthenticator("Administrator", "password")))
    bucket = cluster.bucket("travel-sample")
    await bucket.on_connect()

    return cluster, bucket
```

### [](#asyncio-document-kv-operations)Asyncio Document (KV) Operations

Key-value and sub-document operations return `Future` objects which can then be used for `await` clauses. The `Future`’s result will always be the relevant `Result` object for the operation performed.

KV - Operations

```python
async def kv_operations(collection):
    key = "hotel_10025"
    res = await collection.get(key)
    hotel = res.content_as[dict]
    print("Hotel: {}".format(hotel))

    hotel["alias"] = "Hostel"
    res = await collection.upsert(key, hotel)
    print("CAS: {}".format(res.cas))

    # handle exception
    try:
        res = await collection.get("not-a-key")
    except DocumentNotFoundException as ex:
        print("Document not found exception caught!")
```

Sub-document Operations

```python
async def sub_doc_operations(collection):
    key = "hotel_10025"
    res = await collection.lookup_in(key,
                                     [SD.get("reviews[0].ratings")])

    print("Review ratings: {}".format(res.content_as[dict](0)))

    res = await collection.mutate_in(key,
                                     [SD.replace("reviews[0].ratings.Rooms", 3.5)])
    print("CAS: {}".format(res.cas))
```

### [](#asyncio-sql-operations)Asyncio SQL++ Operations

The API for issuing SQL++ (formerly N1QL) queries is almost identical to the synchronous API. The notable difference is the use of `async for` rather than `for` when iterating over the results.

SQL++ Query

```python
async def n1ql_query(cluster):
    try:
        result = cluster.query(
            "SELECT h.* FROM `travel-sample`.inventory.hotel h WHERE h.country=$country LIMIT 10",
            QueryOptions(named_parameters={"country": "United Kingdom"}))

        async for row in result:
            print("Found row: {}".format(row))
    except ParsingFailedException as ex:
        print(ex)
    except CouchbaseException as ex:
        print(ex)
```

### [](#asyncio-search-operations)Asyncio Search Operations

The API for issuing full text search queries is almost identical to the synchronous API. The notable difference is the use of `async for` rather than `for` when iterating over the results.

Search Query

```python
async def search_query(cluster):
    try:
        result = cluster.search_query(
            "travel-sample-index", search.QueryStringQuery("swanky"))

        async for row in result:
            print(f"Found row: {row}")
        print(f"Reported total rows: {result.metadata().metrics().total_rows()}")

    except CouchbaseException as ex:
        print(ex)
```

### [](#asyncio-analytics-operations)Asyncio Analytics Operations

The API for issuing analytics queries is almost identical to the synchronous API. The notable difference is the use of `async for` rather than `for` when iterating over the results.

Analytics Query

```python
async def analytics_query(cluster):
    try:
        result = cluster.analytics_query(
            "SELECT a.* FROM `travel-sample`.inventory.airports a WHERE a.country = $country LIMIT 10",
            AnalyticsOptions(named_parameters={"country": "France"}))
        async for row in result:
            print("Found row: {}".format(row))
    except CouchbaseException as ex:
        print(ex)
```

## [](#twisted)Twisted

To use the Python SDK with the ["Twisted"](https://twistedmatrix.com/trac/) framework, use the _txcouchbase_ module. As opposed to the synchronous SDK methods which wait for completion and return `Result` objects, the _txcouchbase_ methods return a Twisted `Deferred`. You may configure `Deferred` with callback and errback handlers. `Result` objects are propagated to the callback as seen in the examples below.

> [!IMPORTANT]
> The txcouchbase package _must_ be imported prior to importing the Twisted reactor.

_txcouchbase_ imports

```python
# **IMPORTANT** need to do this import prior to importing the reactor (new to the Python 4.x SDK)
import txcouchbase
from twisted.internet import reactor

# needed for FTS support
import couchbase.search as search

# needed for sub-document operations
import couchbase.subdocument as SD

# used for analytics operations
from couchbase.analytics import AnalyticsOptions

# used to support SQL++ (N1QL) query
from couchbase.options import QueryOptions

# needed for cluster creation
from couchbase.auth import PasswordAuthenticator
from txcouchbase.cluster import TxCluster

# used for handling result objects
from couchbase.result import GetResult, LookupInResult
```

Create a _txcouchbase_ Cluster

```python
def on_connect_ok(result, cluster):
    # create a bucket object
    bucket = cluster.bucket('travel-sample')
    # get a reference to the default collection, required for older Couchbase server versions
    cb_coll_default = bucket.default_collection()
    # get a reference a named collection
    cb_coll = bucket.scope("inventory").collection("hotel")
    do_stuff(cluster, bucket, cb_coll, cb_coll_default)


def on_connect_err(error):
    print("Unable to connect.\n{}".format(error))


# create a cluster object
cluster = TxCluster('couchbase://your-ip',
                    authenticator=PasswordAuthenticator(
                        'Administrator',
                        'password'))

# wait for connect
cluster.on_connect().addCallback(on_connect_ok, cluster).addErrback(on_connect_err)
```

### [](#twisted-document-kv-operations)Twisted Document (KV) Operations

Key-value and sub-document operations return `Deferred` objects which can then be configured with callback and errback handlers. The `Deferred`’s result will always be the relevant `Result` object for the operation performed.

KV - Operations

```python
def on_kv_ok(result):
    if isinstance(result, GetResult):
        print("Document: {}".format(result.content_as[dict]))
    else:
        print("CAS: {}".format(result.cas))


def on_kv_error(error):
    print("Operation had an error.\nError: {}".format(error))


def kv_operations(collection):
    key = "hotel_10025"
    collection.get(key).addCallback(on_kv_ok).addErrback(on_kv_error)

    new_hotel = {
        "title": "Couchbase",
        "name": "The Couchbase Hotel",
        "address": "Pennington Street",
        "directions": None,
        "phone": "+44 1457 855449",
    }

    collection.upsert("hotel_98765", new_hotel).addCallback(
        on_kv_ok).addErrback(on_kv_error)

    collection.get("not-a-key").addCallback(on_kv_ok).addErrback(on_kv_error)
```

Sub-document Operations

```python
def on_sd_ok(result, idx=0):
    if isinstance(result, LookupInResult):
        print("Sub-document: {}".format(result.content_as[dict](idx)))
    else:
        print("CAS: {}".format(result.cas))


def on_sd_error(error):
    print("Operation had an error.\nError: {}".format(error))


def sub_doc_operations(collection):
    key = "hotel_10025"

    collection.lookup_in(key, [SD.get("reviews[0].ratings")]).addCallback(
        on_sd_ok).addErrback(on_sd_error)

    collection.mutate_in(key, [SD.replace("reviews[0].ratings.Rooms", 3.5)]).addCallback(
        on_sd_ok).addErrback(on_sd_error)
```

### [](#twisted-sql-operations)Twisted SQL++ Operations

The API for issuing SQL++ queries is almost identical to the synchronous API. The notable difference is the use of a callback in order to handle iterating over results.

SQL++ Query

```python
def handle_n1ql_results(result):
    for r in result.rows():
        print("Query row: {}".format(r))


def n1ql_query(cluster):
    d = cluster.query(
        "SELECT h.* FROM `travel-sample`.inventory.hotel h WHERE h.country=$country LIMIT 2",
        QueryOptions(named_parameters={"country": "United Kingdom"}))
    d.addCallback(handle_n1ql_results).addErrback(on_streaming_error)
```

### [](#twisted-search-operations)Twisted Search Operations

The API for issuing full text search queries is almost identical to the synchronous API. The notable difference is the use of a callback in order to handle iterating over results.

Search Query

```python
def handle_search_results(result):
    for r in result.rows():
        print("Search row: {}".format(r))


def search_query(cluster):
    d = cluster.search_query(
        "travel-sample-index", search.QueryStringQuery("swanky"))
    d.addCallback(handle_search_results).addErrback(on_streaming_error)
```

### [](#twisted-analytics-operations)Twisted Analytics Operations

The API for issuing analytics queries is almost identical to the synchronous API. The notable difference is the use of a callback in order to handle iterating over results.

Analytics Query

```python
def handle_analytics_results(result):
    for r in result.rows():
        print("Analytics row: {}".format(r))

def analytics_query(cluster):
    d = cluster.analytics_query(
        "SELECT id, country FROM `travel-sample`.inventory.airports a WHERE a.country = $country LIMIT 10",
        AnalyticsOptions(named_parameters={"country": "France"}))
    d.addCallback(handle_analytics_results).addErrback(on_streaming_error)
```