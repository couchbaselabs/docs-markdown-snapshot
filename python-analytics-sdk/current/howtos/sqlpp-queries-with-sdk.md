---
title: Querying with SQL++
description: You can query for documents in Couchbase using the SQL++ query
  language, a language based on SQL, but designed for structured and flexible
  JSON documents.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-analytics-sdk-python/edit/release/1.1/modules/howtos/pages/sqlpp-queries-with-sdk.adoc
  xref: xref:python-analytics-sdk:howtos:sqlpp-queries-with-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-analytics-sdk/current/howtos/sqlpp-queries-with-sdk.html)

# Querying with SQL++

> You can query for documents in Couchbase using the SQL++ query language, a language based on SQL, but designed for structured and flexible JSON documents. 

On this page we dive straight into using the Query Service API from the Python Analytics SDK. For a deeper look at the concepts, to help you better understand the Query Service, and the SQL++ language, see the links in the [Further Information](#further-information) section at the end of this page.

## [](#before-you-start)Before You Start

This page assumes that you have [installed the Python Analytics SDK](../hello-world/start-using-sdk.md), added your IP address to the allowlist, and [created an Enterprise Analytics cluster](#analytics:manage:manage-nodes/create-cluster.adoc#cluster).

Create a collection to work upon by [importing the travel-sample dataset](#analytics:intro:connecting-to-data-sources.adoc#import-the-travel-sample-collections) into your cluster.

## [](#querying-your-dataset)Querying Your Dataset

> [!TIP]
> API Enhancements & Async
> 
> The 1.1 Python Analytics SDK adds support for JWT and client certificate authentication, as well as a new poll-based Server Asynchronous Request API that uses request handles to fetch results. Introduced in self-managed Enterprise Analytics Server 2.2, this API eliminates the need for long-running server connections.
> 
> The examples in this first section of the page are for the standard API, working with all 2.x releases of Enterprise Analytics (with Server Asynchronous Request API examples following in the [Server Async section](#server-asynchronous-api)). Note, you will still be able to use this API with 2.2+ releases of Enterprise Analytics, in addition to the new API.

Most queries return more than one result, and you want to iterate over the results:

### [](#scope-level-queries)Scope Level Queries

* Sync API
* Async API

```python
scope = cluster.database('travel-sample').scope('inventory')

query = """
        SELECT airline, COUNT(*) AS route_count, AVG(route.distance) AS avg_route_distance
        FROM route
        GROUP BY airline
        ORDER BY route_count DESC
        """

res = scope.execute_query(query)

print('Rows:')
for row in res.rows():
    print(row)

print(f'\nMetadata: {res.metadata()}')
```

```python
scope = cluster.database('travel-sample').scope('inventory')

query = """
        SELECT airline, COUNT(*) AS route_count, AVG(route.distance) AS avg_route_distance
        FROM route
        GROUP BY airline
        ORDER BY route_count DESC
        """

res = await scope.execute_query(query)

print('Rows:')
async for row in res.rows():
    print(row)

print(f'\nMetadata: {res.metadata()}')
```

### [](#cluster-level-queries)Cluster Level Queries

* Sync API
* Async API

```python
query = """
        SELECT airline, COUNT(*) AS route_count, AVG(route.distance) AS avg_route_distance
        FROM `travel-sample`.inventory.route
        GROUP BY airline
        ORDER BY route_count DESC
        """

res = cluster.execute_query(query)
```

```python
query = """
        SELECT airline, COUNT(*) AS route_count, AVG(route.distance) AS avg_route_distance
        FROM `travel-sample`.inventory.route
        GROUP BY airline
        ORDER BY route_count DESC
        """

res = await cluster.execute_query(query)
```

### [](#positional-and-named-parameters)Positional and Named Parameters

Supplying parameters as individual arguments to the query allows the query engine to optimize the parsing and planning of the query. You can either supply these parameters by name or by position.

#### [](#positional-parameters)Positional Parameters

Execute a query with positional arguments:

* Sync API
* Async API

```python
from couchbase_analytics.options import QueryOptions

query = """
        SELECT airline, COUNT(*) AS route_count, AVG(route.distance) AS avg_route_distance
        FROM route
        WHERE sourceairport=$1 AND distance>=$2
        GROUP BY airline
        ORDER BY route_count DESC
        """

res = scope.execute_query(query, QueryOptions(positional_parameters=['SFO', 1000]))
```

```python
from acouchbase_analytics.options import QueryOptions

query = """
        SELECT airline, COUNT(*) AS route_count, AVG(route.distance) AS avg_route_distance
        FROM route
        WHERE sourceairport=$1 AND distance>=$2
        GROUP BY airline
        ORDER BY route_count DESC
        """

res = await scope.execute_query(query, QueryOptions(positional_parameters=['SFO', 1000]))
```

#### [](#named-parameters)Named Parameters

Execute a query with named arguments:

* Sync API
* Async API

```python
query = """
        SELECT airline, COUNT(*) AS route_count, AVG(route.distance) AS avg_route_distance
        FROM route
        WHERE sourceairport=$source_airport AND distance>=$min_distance
        GROUP BY airline
        ORDER BY route_count DESC
        """

res = scope.execute_query(query, QueryOptions(named_parameters={'source_airport': 'SFO', 'min_distance': 1000}))
```

```python
query = """
        SELECT airline, COUNT(*) AS route_count, AVG(route.distance) AS avg_route_distance
        FROM route
        WHERE sourceairport=$source_airport AND distance>=$min_distance
        GROUP BY airline
        ORDER BY route_count DESC
        """

res = await scope.execute_query(query, QueryOptions(named_parameters={'source_airport': 'SFO', 'min_distance': 1000}))
```

## [](#query-options)Query Options

The query service provides an array of options to customize your query. The following table lists them all:

__Table 1\. Available Query Options__
| Name                                                              | Description                                                                                                                          |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| client\_context\_id: Optional\[str\]                              | An optional identifier for the query.                                                                                                |
| deserializer: Optional\[Deserializer\]                            | Sets the deserializer applied to results. If not specified, defaults to the cluster's default deserializer, DefaultJsonDeserializer. |
| named\_parameters: Optional\[Dict\[str, JSONType\]\]              | Values to use for named placeholders in query.                                                                                       |
| positional\_parameters: Optional\[Iterable\[JSONType\]\]          | Values to use for positional placeholders in query.                                                                                  |
| query\_context: Optional\[str\]                                   | Specifies the context within which this query should be executed.                                                                    |
| raw: Optional\[Dict\[str, Any\]\]                                 | Specifies any additional parameters which should be passed to the Analytics engine when executing the query.                         |
| readonly: Optional\[bool\]                                        | Specifies that this query should be executed in read-only mode, disabling the ability for the query to make any changes to the data. |
| scan\_consistency: Optional\[Union\[QueryScanConsistency, str\]\] | Specifies the consistency requirements when executing the query.                                                                     |
| timeout: Optional\[timedelta\]                                    | Set to configure allowed time for operation to complete. Defaults to None (75s).                                                     |

## [](#using-the-query-result)Using the Query Result

Results from the Couchbase Analytics SDK can easily be used with several common Data Analytics Python libraries, including [Pandas](https://pandas.pydata.org/) and [PyArrow](https://arrow.apache.org/docs/python/index.html).

Importing the result to a `pandas` `DataFrame`.

```python
import pandas as pd

res = scope.execute_query(query)
df = pd.DataFrame.from_records(res.rows(), index='airline')

print(df.head())
#          route_count  avg_route_distance
# airline
# AA              2354         2314.884359
# UA              2180         2350.365407
# DL              1981         2350.494112
# US              1960         2101.417609
# WN              1146         1397.736500
```

Importing the query result to a `PyArrow` table.

```python
import pyarrow as pa

res = scope.execute_query(query)
table = pa.Table.from_pylist(res.get_all_rows())

print(table.to_string())
# pyarrow.Table
# route_count: int64
# avg_route_distance: double
# airline: string
```

## [](#server-asynchronous-api)Server Asynchronous Request API (with Python Blocking API)

Enterprise Analytics Server 2.2 adds aServer Asynchronous Request API. The SDK will send a request, poll for results, and then fetch once the result is available.

Server Asynchronous API Example

```python
import logging
import time

from couchbase_analytics import LOG_DATE_FORMAT, LOG_FORMAT
from couchbase_analytics.cluster import Cluster
from couchbase_analytics.credential import Credential
from couchbase_analytics.query_handle import BlockingQueryHandle, BlockingQueryResultHandle

# setup logger via basicConfig
logging.basicConfig(format=LOG_FORMAT, datefmt=LOG_DATE_FORMAT, level=logging.DEBUG)

def wait_for_query_results(handle: BlockingQueryHandle,
                           delay: float = 2.5,
                           timeout: int = 120) -> BlockingQueryResultHandle:
    current_time = time.monotonic()
    deadline = current_time + timeout  # seconds
    status = None
    while True:
        try:
            status = handle.fetch_status()
            if status.results_ready():
                return status.result_handle()
        except Exception as e:
            # Depending on the use case, you might want to break here or continue retrying.
            print(f'Error fetching query results: {e}')

        current_time = time.monotonic()
        delay_time = current_time + delay
        if deadline < delay_time:
            raise TimeoutError(f'Query results not ready within {timeout} seconds.')
        else:
            if status is not None:
                print(f'Query status: {status}')
            print(f'Query results not ready yet, sleeping for {delay} seconds...')

        time.sleep(delay)


def main() -> None:
    # Update this to your cluster
    # IMPORTANT:  The appropriate port needs to be specified. The SDK's default ports are 80 (http) and 443 (https).
    #             If attempting to connect to Capella, the correct ports are most likely to be 8095 (http) and 18095 (https).    # noqa: E501
    #             Capella example: https://cb.2xg3vwszqgqcrsix.cloud.couchbase.com:18095
    endpoint = 'http://localhost'
    username = 'Administrator'
    pw = 'password'
    # User Input ends here.

    cred = Credential.from_username_and_password(username, pw)
    cluster = Cluster.create_instance(endpoint, cred)
    statement = 'SELECT VALUE SLEEP("x", 100) FROM RANGE(1, 100) AS id;'
    handle = cluster.start_query(statement)

    result_handle = wait_for_query_results(handle, delay=2.5, timeout=60)
    res = result_handle.fetch_results()

    for row in res:
        print(f'Found row: {row}')
    print(f'metadata={res.metadata()}')
    result_handle.discard_results()


if __name__ == '__main__':
    main()
```

## [](#further-information)Further Information

The [SQL++ for Analytics Reference](../../../analytics/sqlpp/1%5Fintro.md)offers a complete guide to the SQL++ language for both of our analytics services, including all of the latest additions.