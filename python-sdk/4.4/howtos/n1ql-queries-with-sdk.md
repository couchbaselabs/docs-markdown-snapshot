---
title: Query
description: You can query for documents in Couchbase using the SQL++ query
  language, a language based on SQL, but designed for structured and flexible
  JSON documents.
editUrl: https://github.com/couchbase/docs-sdk-python/edit/temp/4.4/modules/howtos/pages/n1ql-queries-with-sdk.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/python-sdk/4.4/howtos/n1ql-queries-with-sdk.html)

# Query

> You can query for documents in Couchbase using the SQL++ query language, a language based on SQL, but designed for structured and flexible JSON documents. Querying can solve typical programming tasks such as finding a user profile by email address, facebook login, or user ID. 

Our query service uses SQL++ (formerly N1QL), which will be fairly familiar to anyone who’s used any dialect of SQL. [Further resources](#additional-resources) for learning about SQL++ are listed at the bottom of the page. Before you get started you may wish to checkout the [SQL++ intro page](../../../server/7.6/n1ql/n1ql-language-reference/index.md), or just dive in with a query against our "travel-sample" data set. In this case, note that before you can query a bucket, you must define at least one index. You can define a _primary_ index on a bucket. When a primary index is defined you can issue non-covered queries on the bucket as well.

Use [cbq](#7.6@server::tools/cbq-shell.html), our interactive Query shell. Open it, and enter the following:

```n1ql
CREATE PRIMARY INDEX ON `travel-sample`
```

or replace _travel-sample_ with a different Bucket name to build an index on a different dataset.

> [!NOTE]
> The default installation places cbq in `/opt/couchbase/bin/` on Linux, `/Applications/Couchbase Server.app/Contents/Resources/couchbase-core/bin/cbq` on OS X, and `C:\Program Files\Couchbase\Server\bin\cbq.exe` on Microsoft Windows.

Note that building indexes is covered in more detail on the [Query concept page](../concept-docs/n1ql-query.md#index-building) — and in the [API Reference](https://docs.couchbase.com/sdk-api/couchbase-python-client/couchbase%5Fapi/couchbase%5Fmanagement.html#module-couchbase.management.queries).

## [](#getting-started)Getting Started

After familiarizing yourself with the basics on how the SQL++ query language works and how to query it from the UI you can use it from the Python SDK. Here’s a complete example of doing a query and handling the results:

```python
from couchbase.cluster import Cluster
from couchbase.options import ClusterOptions, QueryOptions
from couchbase.auth import PasswordAuthenticator
from couchbase.exceptions import CouchbaseException

cluster = Cluster.connect(
    "couchbase://your-ip",
    ClusterOptions(PasswordAuthenticator("Administrator", "password")))
bucket = cluster.bucket("travel-sample")
collection = bucket.default_collection()

try:
    result = cluster.query(
        "SELECT * FROM `travel-sample`.inventory.airport LIMIT 10", QueryOptions(metrics=True))

    for row in result.rows():
        print(f"Found row: {row}")

    print(f"Report execution time: {result.metadata().metrics().execution_time()}")

except CouchbaseException as ex:
    import traceback
    traceback.print_exc()
```

> [!NOTE]
> When using a Couchbase version < 6.5 you must create a valid Bucket connection using `cluster.bucket(name)` before you can execute queries.

Let’s break it down. A query is always performed at the `Cluster` level, using the `query` method. It takes the statement as a required argument and then allows to provide additional options if needed.

Once a result returns you can iterate the returned rows and/or access the `QueryMetaData` associated with the query.

## [](#queries-placeholders)Queries & Placeholders

Placeholders allow you to specify variable constraints for an otherwise constant query. There are two variants of placeholders: postional and named parameters. Positional parameters use an ordinal placeholder for substitution and named parameters use variables. A named or positional parameter is a placeholder for a value in the WHERE, LIMIT or OFFSET clause of a query. Note that both parameters and options are optional.

Positional parameter example:

```python
result = cluster.query(
    "SELECT ts.* FROM `travel-sample`.inventory.airport WHERE city=$1",
    "San Jose")
```

```python
result = cluster.query(
    "SELECT ts.* FROM `travel-sample`.inventory.airport WHERE city=$1",
    QueryOptions(positional_parameters=["San Jose"]))
```

Named parameter example:

```python
result = cluster.query(
    "SELECT ts.* FROM `travel-sample`.inventory.airport WHERE city=$city",
    city='San Jose')
```

```python
result = cluster.query(
    "SELECT ts.* FROM `travel-sample`.inventory.airport WHERE city=$city",
    QueryOptions(named_parameters={"city": "San Jose"}))
```

The complete code for this page’s example can be found at [n1ql\_ops.py](https://github.com/couchbase/docs-sdk-python/blob/release/3.2/modules/howtos/examples/n1ql%5Fops.py). What style you choose is up to you, for readability in more complex queries we generally recommend using the named parameters. Note that you cannot use parameters in all positions. If you put it in an unsupported place the server will respond with a `ParsingFailedException` or similar.

## [](#the-query-result)The Query Result

When performing a query, the response you receive is a `QueryResult`. If no error is returned then the request succeeded and the result provides access to both the rows returned and also associated `QueryMetaData`.

```python
result = cluster.query(
    "SELECT * FROM `travel-sample`.inventory.airline LIMIT 10")

# iterate over rows
for row in result:
    # each row is an instance of the query call
    try:
        name = row["airline"]["name"]
        callsign = row["airline"]["callsign"]
        print(f"Airline name: {name}, callsign: {callsign}")
    except KeyError:
        print("Row does not contain 'name' key")
```

> [!NOTE]
> The SDK executes queries lazily, meaning the query is only run against the cluster when you try to use the `QueryResult` object. You therefore cannot iterate over the `QueryResult` multiple times, and attempting to do so raises an `AlreadyQueriedException`.

The `QueryMetaData` provides insight into some basic profiling/timing information as well as information like the `ClientContextID`.

__Table 1\. QueryMetaData__
| Name                                 | Description                                                                      |
| ------------------------------------ | -------------------------------------------------------------------------------- |
| request\_id() → str                  | Returns the request identifer of this request.                                   |
| client\_context\_id() → str          | Returns the context ID either generated by the SDK or supplied by the user.      |
| status() → QueryStatus               | An enum simply representing the state of the result.                             |
| metrics() → Optional\[QueryMetrics\] | Returns metrics provided by the query for the request if enabled.                |
| signature() → Optional\[JSON\]       | If a signature is present, it will be available to consume in a generic fashion. |
| warnings() → List\[QueryWarning\]    | Non-fatal errors are available to consume as warnings on this method.            |
| profile() → Optional\[JSON\]         | If enabled returns additional profiling information of the query.                |

For example, here is how you can print the `executionTime` of a query:

```python

result = cluster.query("SELECT 1=1", QueryOptions(metrics=True))
for row in result:
    print(f"Result: {row}")
print(f"Execution time: {result.metadata().metrics().execution_time()}")
```

## [](#query-options)Query Options

The query service provides an array of options to customize your query. The following table lists them all:

__Table 2\. Available Query Options__
| Name                                      | Description                                                                         |
| ----------------------------------------- | ----------------------------------------------------------------------------------- |
| client\_context\_id (str)                 | Sets a context ID returned by the service for debugging purposes.                   |
| positional\_parameters (Iterable\[JSON\]) | Allows to set positional arguments for a parameterized query.                       |
| named\_parameters (dict\[str,JSON\])      | Allows to set named arguments for a parameterized query.                            |
| priority(boolean)                         | Assigns a different server-side priority to the query.                              |
| raw (dict\[str,JSON\])                    | Escape hatch to add arguments that are not covered by these options.                |
| read\_only (bool)                         | Tells the client and server that this query is readonly.                            |
| adhoc (bool)                              | If set to false will prepare the query and later execute the prepared statement.    |
| consistent\_with (MutationState)          | Allows to be consistent with previously written mutations ("read your own writes"). |
| max\_parallelism (int)                    | Tunes the maximum parallelism on the server.                                        |
| metrics (bool)                            | Enables the server to send metrics back to the client as part of the response.      |
| pipeline\_batch (int)                     | Sets the batch size for the query pipeline.                                         |
| pipeline\_cap (int)                       | Sets the cap for the query pipeline.                                                |
| profile (QueryProfile)                    | Allows to enable additional query profiling as part of the response.                |
| scan\_wait (timedelta)                    | Allows to specify a maximum scan wait time.                                         |
| scan\_cap (int)                           | Specifies a maximum cap on the query scan size.                                     |
| scan\_consistency (QueryScanConsistency)  | Sets a different scan consistency for this query.                                   |
| query\_context                            | Allows to set target bucket and/or scope.                                           |

## [](#scan-consistency)Scan Consistency

By default, the query engine will return whatever is currently in the index at the time of query (this mode is also called `QueryScanConsistency.NOT_BOUNDED`). If you need to include everything that has just been written, a different scan consistency must be chosen. If `QueryScanConsistency.REQUEST_PLUS` is chosen, it will likely take a bit longer to return the results but the query engine will make sure that it is as up-to-date as possible.

```python
result = cluster.query(
    "SELECT * FROM `travel-sample`.inventory.airline LIMIT 10",
    QueryOptions(scan_consistency=QueryScanConsistency.REQUEST_PLUS))
```

You can also use `consistent_with=MutationState` for a more narrowed-down scan consistency. Construct the `MutationState` from individual \`MutationToken\`s that are returned from KV \`MutationResult\`s to make sure at least those mutations are visible. Depending on the index update rate this might provide a speedier response.

```python
new_hotel = {
    "callsign": None,
    "country": "United States",
    "iata": "TX",
    "icao": "TX99",
    "id": 123456789,
    "name": "Howdy Airlines",
    "type": "airline"
}

res = collection.upsert(
    "airline_{}".format(new_hotel["id"]), new_hotel)

ms = MutationState(res)

result = cluster.query(
    "SELECT ts.* FROM `travel-sample`.inventory.airline LIMIT 10",
    QueryOptions(consistent_with=ms))
```

### [](#client-context-id)Client Context ID

The SDK will always send a client context ID with each query, even if none is provided by the user. By default a UUID will be generated that is mirrored back from the query engine and can be used for debugging purposes. A custom string can always be provided if you want to introduce application-specific semantics into it (so that for example in a network dump it shows up with a certain identifier). Whatever is chosen, we recommend making sure it is unique so different queries can be distinguished during debugging or monitoring.

```python
result = cluster.query(
    "SELECT ts.* FROM `travel-sample`.inventory.hotel LIMIT 10",
    QueryOptions(client_context_id="user-44{}".format(uuid.uuid4())))
```

### [](#readonly)ReadOnly

If the query is marked as readonly, both the server and the SDK can improve processing of the operation. On the client side, the SDK can be more liberal with retries because it can be sure that there are no state-mutating side-effects happening. The query engine will ensure that actually no data is mutated when parsing and planning the query.

```python
result = cluster.query(
    "SELECT ts.* FROM `travel-sample`.inventory.hotel LIMIT 10",
    QueryOptions(read_only=True))
```

## [](#streaming-large-result-sets)Streaming Large Result Sets

By default, the Python SDK will stream the result set from the server, where the client will start a persistent connection with the server and only read the header until the Rows are enumerated; then, each row or JSON object will be de-serialized one at a time.

This decreases pressure on Garbage Collection and helps to prevent OutOfMemory errors.

## [](#async-apis)Async APIs

In addition to the blocking API on `Cluster`, the SDK provides asyncio and Twisted APIs on `ACluster` or `TxCluster` respectively. If you are in doubt of which API to use, we recommend looking at the asyncio API first.

Simple queries with both asyncio and Twisted APIs look similar to the blocking one:

ACouchbase

```python
from acouchbase.cluster import Cluster, get_event_loop
from couchbase.options import ClusterOptions, QueryOptions
from couchbase.auth import PasswordAuthenticator
from couchbase.exceptions import ParsingFailedException


async def get_couchbase():
    cluster = Cluster(
        "couchbase://your-ip",
        ClusterOptions(PasswordAuthenticator("Administrator", "password")))
    bucket = cluster.bucket("travel-sample")
    await bucket.on_connect()
    collection = bucket.default_collection()

    return cluster, bucket, collection


async def simple_query(cluster):
    try:
        result = cluster.query(
            "SELECT ts.* FROM `travel-sample` ts WHERE ts.`type`=$type LIMIT 10",
            QueryOptions(named_parameters={"type": "hotel"}))
        async for row in result:
            print("Found row: {}".format(row))
    except ParsingFailedException as ex:
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
from couchbase.options import ClusterOptions, QueryOptions
from couchbase.auth import PasswordAuthenticator


def handle_query_results(result):
    for r in result.rows():
        print("query row: {}".format(r))
    reactor.stop()


def on_streaming_error(error):
    print("Streaming operation had an error.\nError: {}".format(error))
    reactor.stop()


def on_connect_ok(result, cluster):
    # create a bucket object
    bucket = cluster.bucket("travel-sample")
    # create a collection object
    cb = bucket.default_collection()

    d = cluster.query("SELECT ts.* FROM `travel-sample` ts WHERE ts.`type`=$type LIMIT 10",
                    QueryOptions(named_parameters={"type": "hotel"}))
    d.addCallback(handle_query_results).addErrback(on_streaming_error)


def on_connect_err(error):
    print("Unable to connect.\n{}".format(error))

cluster = TxCluster("couchbase://your-ip",
                    ClusterOptions(PasswordAuthenticator("Administrator", "password")))

# wait for connect
cluster.on_connect().addCallback(on_connect_ok, cluster).addErrback(on_connect_err)


reactor.run()
```

## [](#querying-at-scope-level)Querying at Scope Level

It is possible to query off the [Scope level](../concept-docs/n1ql-query.md#collections-and-scopes-and-the-query-context), _with Couchbase Server release 7.0_, using the `scope.query()` method. It takes the statement as a required argument, and then allows additional options if needed.

```python
agent_scope = bucket.scope("inventory")

result = agent_scope.query(
        "SELECT a.* FROM `airline` a WHERE a.country=$country LIMIT 10",
        country='France')
```

## [](#additional-resources)Additional Resources

> [!NOTE]
> SQL++ is not the only query option in Couchbase. Be sure to check that [your use case fits your selection of query service](../concept-docs/data-services.md).

* For a deeper dive into SQL++ from the SDK, refer to our [SQL++ SDK concept doc](../concept-docs/n1ql-query.md).
* The [Server doc SQL++ intro](../../../server/7.6/n1ql/n1ql-language-reference/index.md) introduces a complete guide to the SQL++ language, including all of the latest additions.
* The [SQL++ interactive tutorial](http://query.pub.couchbase.com/tutorial/#1) is a good introduction to the basics of SQL++ use.
* For scaling up queries, be sure to [read up on Indexes](../../../server/7.6/n1ql/n1ql-language-reference/index.md).
* The Query Service is for operational queries; for analytical workloads, read more on [when to choose Analytics Service](../concept-docs/data-services.md#Long-Running-Queries-&-Big-Data).