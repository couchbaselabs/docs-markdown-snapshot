---
title: Analytics
description: Parallel data management for complex queries over many records,
  using a familiar SQL++ syntax.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-python/edit/temp/4.4/modules/howtos/pages/analytics-using-sdk.adoc
  xref: xref:4.4@python-sdk:howtos:analytics-using-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-sdk/4.4/howtos/analytics-using-sdk.html)

# Analytics

> Parallel data management for complex queries over many records, using a familiar SQL++ syntax. 

This page covers using our operational Python SDK to connect to the Analytics Service of a Capella Operational or self-managed Couchbase Server cluster. As well as this row-based analytics service, a speedy, column-based analytics database is available for real-time analytics.

> [!TIP]
> Analytics SDKs
> 
> SDKs for [Enterprise Analytics](../../../enterprise-analytics/current/intro/intro.md) — Couchbase's analytical database for real time apps and operational intelligence (RT-OLAP) — are available for the Go, Java, Node.js, and Python platforms. See the [Enterprise Analytics SDK pages](../../../home/analytics-sdk.md) for more information.
> 
> Currently, different SDKs are needed to connect to [Capella Analytics](../../../analytics/intro/intro.md) — as this service does not have Enterprise Analytics' load balancer, and uses a different connection protocol. Capella Analytics SDKs (also known as Columnar SDKs) are available for the Go, Java, Node.js, and Python platforms. See the [Capella Analytics SDK pages](../../../home/columnar-sdk.md) for more information.

For complex and long-running queries, involving large ad hoc join, set, aggregation, and grouping operations, Couchbase Data Platform offers the [Couchbase Analytics Service (CBAS)](../../../server/7.6/analytics/introduction.md). This is the analytic counterpart to our [operational data focussed Query Service](n1ql-queries-with-sdk.md).

The analytics service is available in [Capella operational](../../../cloud/clusters/analytics-service/analytics-service.md)or the Enterprise Edition of self-managed Couchbase Server.

## [](#getting-started)Getting Started

After familiarizing yourself with our [introductory primer](../../../server/7.6/analytics/primer-beer.md), in particular creating a dataset and linking it to a bucket, try Couchbase Analytics using the Python SDK. Intentionally, the API for analytics is nearly identical to that of the query service.

Here's a complete example of doing a analytics and handling the results:

```py
from couchbase.cluster import Cluster, ClusterOptions, AnalyticsOptions
from couchbase.auth import PasswordAuthenticator
from couchbase.exceptions import CouchbaseException
from couchbase.analytics import AnalyticsScanConsistency

cluster = Cluster.connect(
    "couchbase://your-ip",
    ClusterOptions(PasswordAuthenticator("Administrator", "password")))
bucket = cluster.bucket("travel-sample")
collection = bucket.default_collection()

try:
    result = cluster.analytics_query("SELECT 'hello' AS greeting")

    for row in result.rows():
        print("Found row: {}".format(row))

    print("Reported execution time: {}".format(
        result.metadata().metrics().execution_time()))

except CouchbaseException as ex:
    import traceback
    traceback.print_exc()
```

> [!NOTE]
> When using a Couchbase version < 6.5 you must create a valid Bucket connection using `cluster.bucket(name)` before you can use Analytics.

Let's break it down. An analytics query is always performed at the `Cluster` level, using the `analytics_query` method. It takes the statement as a required argument and then allows to provide additional options if needed.

Once a result returns you can iterate the returned rows and/or access the `AnalyticsMetaData` associated with the query.

## [](#parameterized-queries)Parameterized Queries

Supplying parameters as individual arguments to the query allows the analytics engine to optimize the parsing and planning of the query. You can either supply these parameters by name or by position.

The first example shows how to provide them by name:

Positional parameter example:

```python
result = cluster.analytics_query(
    "SELECT count(*) FROM airports a WHERE a.country = ?",
    "France")
```

```python
result = cluster.analytics_query(
    "SELECT count(*) FROM airports a WHERE a.country = ?",
    AnalyticsOptions(positional_parameters=["France"]))
```

Named parameter example:

```python
result = cluster.analytics_query(
    "SELECT count(*) FROM airports a WHERE a.country = $country",
    country="France")
```

```python
result = cluster.analytics_query(
    "SELECT count(*) FROM airports a WHERE a.country = $country",
    AnalyticsOptions(named_parameters={"country": "France"}))
```

The complete code for this page's example can be found at [analytics\_ops.py](https://github.com/couchbase/docs-sdk-python/blob/release/3.2/modules/howtos/examples/analytics%5Fops.py). What style you choose is up to you, for readability in more complex queries we generally recommend using the named parameters. Note that you cannot use parameters in all positions. If you put it in an unsupported place the server will respond with a `CompilationFailedException` or similar.

## [](#the-analytics-result)The Analytics Result

When performing an analytics query, the response you receive is an `AnalyticsResult`. If no exception gets raised the request succeeded and provides access to both the rows returned and also associated `AnalyticsMetaData`.

```python
result = cluster.analytics_query(
    "SELECT a.* FROM airports a LIMIT 10")

# iterate over rows
for row in result:
    # each row is an instance of the query call
    print("Found row: {}".format(row))
```

The `AnalyticsMetaData` provides insight into some basic profiling/timing information as well as information like the `clientContextId`.

__Table 1\. AnalyticsMetaData__
| Name                                      | Description                                                                      |
| ----------------------------------------- | -------------------------------------------------------------------------------- |
| request\_id() → str                       | Returns the request identifer of this request.                                   |
| client\_context\_id() → str               | Returns the context ID either generated by the SDK or supplied by the user.      |
| status() → AnalyticsStatus                | An enum simply representing the state of the result.                             |
| metrics() → Optional\[AnalyticsMetrics\]  | Returns metrics provided by analytics for the request.                           |
| signature() → Optional\[JSON\]            | If a signature is present, it will be available to consume in a generic fashion. |
| warnings() → Iterable\[AnalyticsWarning\] | Non-fatal errors are available to consume as warnings on this method.            |

For example, here is how you can print the `executionTime` of a query:

```python
result = cluster.analytics_query("SELECT 1=1")

print("Execution time: {}".format(
    result.metadata().metrics().execution_time()))
```

## [](#analytics-options)Analytics Options

The analytics service provides an array of options to customize your query. The following table lists them all:

__Table 2\. Available Analytics Options__
| Name                                        | Description                                                          |
| ------------------------------------------- | -------------------------------------------------------------------- |
| client\_context\_id: str                    | Sets a context ID returned by the service for debugging purposes.    |
| positional\_parameters: Iterable\[str\]     | Allows to set positional arguments for a parameterized query.        |
| named\_parameters: Dict\[str,str\]          | Allows to set named arguments for a parameterized query.             |
| priority: bool                              | Assigns a different server-side priority to the query.               |
| raw: Dict\[str, Any\]                       | Escape hatch to add arguments that are not covered by these options. |
| read\_only: bool                            | Tells the client and server that this query is readonly.             |
| scan\_consistency: AnalyticsScanConsistency | Sets a different scan consistency for this query.                    |

### [](#scan-consistency)Scan Consistency

By default, the analytics engine will return whatever is currently in the index at the time of query (this mode is also called `AnalyticsScanConsistency.NOT_BOUNDED`). If you need to include everything that has just been written, a different scan consistency must be chosen. If `AnalyticsScanConsistency.REQUEST_PLUS` is chosen, it will likely take a bit longer to return the results but the analytics engine will make sure that it is as up-to-date as possible.

```py
result = cluster.analytics_query(
    "SELECT count(*) FROM airports a WHERE a.country = 'France'",
    AnalyticsOptions(scan_consistency=AnalyticsScanConsistency.REQUEST_PLUS))
```

### [](#client-context-id)Client Context Id

The SDK will always send a client context ID with each query, even if none is provided by the user. By default a UUID will be generated that is mirrored back from the analytics engine and can be used for debugging purposes. A custom string can always be provided if you want to introduce application-specific semantics into it (so that for example in a network dump it shows up with a certain identifier). Whatever is chosen, we recommend making sure it is unique so different queries can be distinguished during debugging or monitoring.

```python
result = cluster.analytics_query(
    "SELECT count(*) FROM airports a WHERE a.country = 'France'",
    AnalyticsOptions(client_context_id="user-44{}".format(uuid.uuid4())))
```

### [](#priority)Priority

By default, every analytics query has the same priority on the server. By setting this boolean flag to true, you are indicating that you need expedited dispatch in the analytice engine for this request.

```python
result = cluster.analytics_query(
    "SELECT count(*) FROM airports a WHERE a.country = 'France'",
    AnalyticsOptions(priority=True))
```

### [](#readonly)Readonly

If the query is marked as readonly, both the server and the SDK can improve processing of the operation. On the client side, the SDK can be more liberal with retries because it can be sure that there are no state-mutating side-effects happening. The query engine will ensure that actually no data is mutated when parsing and planning the query.

```python
result = cluster.analytics_query(
    "SELECT count(*) FROM airports a WHERE a.country = 'France'",
    AnalyticsOptions(read_only=True))
```

## [](#async-apis)Async APIs

In addition to the blocking API on `Cluster`, the SDK provides asyncio and Twisted APIs on `ACluster` or `TxCluster` respectively. If you are in doubt of which API to use, we recommend looking at the asyncio API first.

Simple queries with both asyncio and Twisted APIs look similar to the blocking one:

ACouchbase

```python
from acouchbase.cluster import Cluster, get_event_loop
from couchbase.options import AnalyticsOptions, ClusterOptions
from couchbase.auth import PasswordAuthenticator
from couchbase.exceptions import CouchbaseException


async def get_couchbase():
    cluster = Cluster(
        "couchbase://your-ip",
        ClusterOptions(PasswordAuthenticator("Administrator", "password")))
    bucket = cluster.bucket("travel-sample")
    await bucket.on_connect()
    collection = bucket.default_collection()

    return cluster, bucket, collection

# NOTE: the analytics dataset might need to be created
async def simple_query(cluster):
    try:
        result = cluster.analytics_query(
            "SELECT id, country FROM airports a WHERE a.country = $country LIMIT 10",
            AnalyticsOptions(named_parameters={"country": "France"}))
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
from couchbase.options import AnalyticsOptions, ClusterOptions
from couchbase.auth import PasswordAuthenticator


def handle_query_results(result):
    for r in result.rows():
        print("query row: {}".format(r))
    reactor.stop()


def on_streaming_error(error):
    print("Streaming operation had an error.\nError: {}".format(error))
    reactor.stop()

# NOTE: the analytics dataset might need to be created
def on_connect_ok(result, cluster):
    # create a bucket object
    bucket = cluster.bucket("travel-sample")
    # create a collection object
    cb = bucket.default_collection()

    d = cluster.analytics_query(
        "SELECT id, country FROM airports a WHERE a.country = $country LIMIT 10",
        AnalyticsOptions(named_parameters={"country": "France"}))
    d.addCallback(handle_query_results).addErrback(on_streaming_error)


def on_connect_err(error):
    print("Unable to connect.\n{}".format(error))

cluster = TxCluster("couchbase://your-ip",
                    ClusterOptions(PasswordAuthenticator("Administrator", "password")))

# wait for connect
cluster.on_connect().addCallback(on_connect_ok, cluster).addErrback(on_connect_err)

reactor.run()
```

## [](#scoped-queries-on-named-collections)Scoped Queries on Named Collections

In addition to creating a dataset with a WHERE clause to filter the results to documents with certain characteristics, SDK 3.2 now allows you to create a dataset against a named collection, for example:

```n1ql
ALTER COLLECTION `travel-sample`.inventory.airport ENABLE ANALYTICS;

-- NB: this is more or less equivalent to:
CREATE DATAVERSE `travel-sample`.inventory;
CREATE DATASET `travel-sample`.inventory.airport ON `travel-sample`.inventory.airport;
```

We can then query the Dataset as normal, using the fully qualified keyspace:

```python
result = cluster.analytics_query(
    "SELECT airportname, country FROM `travel-sample`.inventory.airport a WHERE a.country = 'France' LIMIT 3")
```

Note that using the `CREATE DATASET` syntax we could choose any Dataset name in any Dataverse, including the default. However the SDK supports this standard convention, allowing us to query from the Scope object:

```python
scope = bucket.scope("inventory")
result = scope.analytics_query(
    "SELECT airportname, country FROM airport a WHERE a.country = 'France' LIMIT 3")
```