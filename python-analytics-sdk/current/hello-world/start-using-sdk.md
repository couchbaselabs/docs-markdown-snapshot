---
title: Python Analytics SDK Quickstart Guide
description: Install, connect, try. A quick start guide to get you up and
  running with Enterprise Analytics and the Python Analytics SDK.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-analytics-sdk-python/edit/release/1.1/modules/hello-world/pages/start-using-sdk.adoc
  xref: xref:python-analytics-sdk:hello-world:start-using-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-analytics-sdk/current/hello-world/start-using-sdk.html)

# Python Analytics SDK Quickstart Guide

> Install, connect, try. A quick start guide to get you up and running with Enterprise Analytics and the Python Analytics SDK. 

[Enterprise Analytics](../../../analytics/intro/intro.md) is a real-time analytical database (RT-OLAP) for real time apps and operational intelligence. Although maintaining some syntactic similarities with [the operational SDKs](../../../home/sdk.md), the Python Analytics SDK is developed from the ground-up for column-based analytical use cases, and supports streaming APIs to handle large datasets.

## [](#before-you-start)Before You Start

Install and configure an [Enterprise Analytics Cluster](../../../enterprise-analytics/current/intro/intro.md).

### [](#prerequisites)Prerequisites

Currently Python 3.10 - Python 3.14 is supported. See the [compatibility page](../project-docs/compatibility.md#platform-compatibility) for more information about platform support.

## [](#getting-the-sdk)Getting the SDK

The SDK can be installed via `pip`:

```console
$ python3 -m pip install couchbase-analytics
```

For other installation methods, see the [installation page](../project-docs/sdk-full-installation.md).

## [](#connecting-and-executing-a-query)Connecting and Executing a Query

Python Analytics SDK 1.1 adds support for JWT and client certificate authentication, as well as a new Server Asynchronous Request API that uses request handles to fetch results. Introduced in the self-managed Enterprise Analytics Server 2.2, this API eliminates the need for long-running server connections.

The examples in this first section of the page are for the standard API — with blocking and async client-side APIs — working with Enterprise Analytics 2.0 and later (with Server Asynchronous Request API examples following in the [Server Async section](#server-asynchronous-api)). You can still use this API with Enterprise Analytics 2.2 and later, in addition to the new API.

### [](#server-synchronous-request-api)Server Synchronous Request API

#### [](#client-synchronous-api)Client Synchronous API

Blocking API Example

```python
from couchbase_analytics.cluster import Cluster
from couchbase_analytics.credential import Credential
from couchbase_analytics.options import QueryOptions


def main() -> None:
    # Update this to your cluster
    endpoint = 'https://--your-instance--'
    username = 'username'
    pw = 'Password!123'
    # User Input ends here.

    cred = Credential.from_username_and_password(username, pw)
    cluster = Cluster.create_instance(endpoint, cred)

    # Execute a query and buffer all result rows in client memory.
    statement = 'SELECT * FROM `travel-sample`.inventory.airline LIMIT 10;'
    res = cluster.execute_query(statement)
    all_rows = res.get_all_rows()
    for row in all_rows:
        print(f'Found row: {row}')
    print(f'metadata={res.metadata()}')

    # Execute a query and process rows as they arrive from server.
    statement = 'SELECT * FROM `travel-sample`.inventory.airline WHERE country="United States" LIMIT 10;'
    res = cluster.execute_query(statement)
    for row in res.rows():
        print(f'Found row: {row}')
    print(f'metadata={res.metadata()}')

    # Execute a streaming query with positional arguments.
    statement = 'SELECT * FROM `travel-sample`.inventory.airline WHERE country=$1 LIMIT $2;'
    res = cluster.execute_query(statement, QueryOptions(positional_parameters=['United States', 10]))
    for row in res:
        print(f'Found row: {row}')
    print(f'metadata={res.metadata()}')

    # Execute a streaming query with named arguments.
    statement = 'SELECT * FROM `travel-sample`.inventory.airline WHERE country=$country LIMIT $limit;'
    res = cluster.execute_query(statement, QueryOptions(named_parameters={'country': 'United States',
                                                                          'limit': 10}))
    for row in res.rows():
        print(f'Found row: {row}')
    print(f'metadata={res.metadata()}')


if __name__ == '__main__':
    main()
```

#### [](#python-asynchronous-api-with-asyncio)Python Asynchronous API with asyncio

asyncio Example

```python
import asyncio

from acouchbase_analytics.cluster import AsyncCluster
from acouchbase_analytics.credential import Credential
from acouchbase_analytics.options import QueryOptions


async def main() -> None:
    # Update this to your cluster
    endpoint = 'https://--your-instance--'
    username = 'username'
    pw = 'Password!123'
    # User Input ends here.

    cred = Credential.from_username_and_password(username, pw)
    cluster = AsyncCluster.create_instance(endpoint, cred)

    # Execute a query and buffer all result rows in client memory.
    statement = 'SELECT * FROM `travel-sample`.inventory.airline LIMIT 10;'
    res = await cluster.execute_query(statement)
    all_rows = await res.get_all_rows()
    # NOTE: all_rows is a list, _do not_ use `async for`
    for row in all_rows:
        print(f'Found row: {row}')
    print(f'metadata={res.metadata()}')

    # Execute a query and process rows as they arrive from server.
    statement = 'SELECT * FROM `travel-sample`.inventory.airline WHERE country="United States" LIMIT 10;'
    res = await cluster.execute_query(statement)
    async for row in res.rows():
        print(f'Found row: {row}')
    print(f'metadata={res.metadata()}')

    # Execute a streaming query with positional arguments.
    statement = 'SELECT * FROM `travel-sample`.inventory.airline WHERE country=$1 LIMIT $2;'
    res = await cluster.execute_query(statement, QueryOptions(positional_parameters=['United States', 10]))
    async for row in res:
        print(f'Found row: {row}')
    print(f'metadata={res.metadata()}')

    # Execute a streaming query with named arguments.
    statement = 'SELECT * FROM `travel-sample`.inventory.airline WHERE country=$country LIMIT $limit;'
    res = await cluster.execute_query(statement, QueryOptions(named_parameters={'country': 'United States',
                                                                                'limit': 10}))
    async for row in res.rows():
        print(f'Found row: {row}')
    print(f'metadata={res.metadata()}')

if __name__ == '__main__':
    asyncio.run(main())
```

### [](#server-asynchronous-api)Server Asynchronous Request API (with Python Blocking API)

Enterprise Analytics 2.2 introduces a Server Asynchronous Request API. The SDK sends a request, polls for results, and then fetches once the result is available. The SDK supports each stage of this information flow:

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

### [](#connection-string)Connection String

The `connStr` in the above example should takes the form of "https://<your\_hostname>:" + PORT. The default port is 443, for TLS connections. You do not need to give a port number if you are using port 443 — `hostname = "https://<your_hostname>"` is effectively the same as \`hostname = "https://<your\_hostname>:" + "443"

If you are using a different port — for example, connecting to a cluster without a load balancer, directly to the Analytics port, `18095` — or not using TLS, then see the [Connecting to Enterprise Analytics](../howtos/managing-connections.md) page.

## [](#migration-from-row-based-analytics)Migration from Row-Based Analytics

If you are migrating a project from CBAS — our Analytics service on Capella Operational and Couchbase Server, using our operational SDKs — then information on migration can be found in the [Enterprise Analytics docs](../../../enterprise-analytics/current/migration/overview.md).

In particular, refer to the [SDK section](../../../enterprise-analytics/current/migration/migration-process.md#sdk-migration) of the Enterprise Analytics migration pages.