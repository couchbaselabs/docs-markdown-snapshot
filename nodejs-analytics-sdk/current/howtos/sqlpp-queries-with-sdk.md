---
title: Querying with SQL++
description: You can query for documents in Couchbase using the SQL++ query
  language -- a language based on SQL, but designed for structured and flexible
  JSON documents.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-analytics-sdk-nodejs/edit/release/1.1/modules/howtos/pages/sqlpp-queries-with-sdk.adoc
  xref: xref:nodejs-analytics-sdk:howtos:sqlpp-queries-with-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/nodejs-analytics-sdk/current/howtos/sqlpp-queries-with-sdk.html)

# Querying with SQL++

> You can query for documents in Couchbase using the SQL++ query language — a language based on SQL, but designed for structured and flexible JSON documents. 

On this page we dive straight into using the Query Service API from the Node.js Analytics SDK. For a deeper look at the concepts, to help you better understand the Query Service, and the SQL++ language, see the links in the [Further Information](#further-information) section at the end of this page.

## [](#before-you-start)Before You Start

This page assumes that you have [installed the Node.js Analytics SDK](../hello-world/start-using-sdk.md), added your IP address to the allowlist, and [created an Enterprise Analytics cluster](#analytics:manage:manage-nodes/create-cluster.adoc#cluster).

Create a collection to work upon by [importing the travel-sample dataset](#analytics:intro:connecting-to-data-sources.adoc#import-the-travel-sample-collections) into your cluster.

## [](#querying-your-dataset)Querying Your Dataset

> [!TIP]
> API Enhancements & Async
> 
> The 1.1 Node.js Analytics SDK adds support for JWT and client certificate authentication, as well as a new poll-based Server Asynchronous Request API that uses request handles to fetch results. Introduced in self-managed Enterprise Analytics Server 2.2, this API eliminates the need for long-running server connections.
> 
> The examples in this first section of the page are for the standard API, working with all 2.x releases of Enterprise Analytics (with Server Asynchronous Request API examples following in the [Server Async section](#server-asynchronous-api)). Note, you will still be able to use this API with 2.2+ releases of Enterprise Analytics, in addition to the new API.

Most queries return more than one result, and you want to iterate over the results:

Scope Level

```javascript
const scope = cluster.database('travel-sample').scope('inventory')

let qs =
    `
    SELECT airline, COUNT(*) AS route_count, AVG(route.distance) AS avg_route_distance
    FROM route
    GROUP BY airline
    ORDER BY route_count DESC
    `

let res = await scope.executeQuery(qs)

for await (let row of res.rows()) {
    console.log(row)
}

console.log('Metadata: ', res.metadata())
```

Cluster Level

```javascript
let qs =
    `
    SELECT r.airline, COUNT(*) AS route_count, AVG(r.distance) AS avg_route_distance
    FROM \`travel-sample\`.\`inventory\`.\`route\` AS r
    GROUP BY r.airline
    ORDER BY route_count DESC
    `

let res = await cluster.executeQuery(qs)
```

### [](#positional-and-named-parameters)Positional and Named Parameters

Supplying parameters as individual arguments to the query allows the query engine to optimize the parsing and planning of the query. You can either supply these parameters by name or by position.

Execute an async query with positional arguments:

Positional Parameters

```javascript
const scope = cluster.database('travel-sample').scope('inventory')

let qs =
    `
    SELECT airline, COUNT(*) AS route_count, AVG(route.distance) AS avg_route_distance
    FROM route
    WHERE sourceairport = $1 AND distance >= $2
    GROUP BY airline
    ORDER BY route_count DESC
    `

let res = await scope.executeQuery(qs, {
    positionalParameters: ['SFO', 1000],
})
```

Execute an async query with named arguments:

Named Parameters

```javascript
const scope = cluster.database('travel-sample').scope('inventory')

let qs =
    `
    SELECT airline, COUNT(*) AS route_count, AVG(route.distance) AS avg_route_distance
    FROM route
    WHERE sourceairport = $sourceAirport AND distance >= $distance
    GROUP BY airline
    ORDER BY route_count DESC
    `

let res = await scope.executeQuery(qs, {
    namedParameters: {sourceAirport: 'SFO', distance: 1000}
})
```

## [](#server-asynchronous-api)Server Asynchronous Request API

Enterprise Analytics Server 2.2 adds aServer Asynchronous Request API. The SDK will send a request, poll for results, and then fetch once the result is available.

### [](#commonjs)CommonJS

Server Asynchronous API Example

```javascript
const analytics = require('couchbase-analytics')

async function waitForQueryResults(handle, delayMs = 2500, timeoutMs = 120000) {
  const deadline = Date.now() + timeoutMs
  let status = null
  while (true) {
    try {
      status = await handle.fetchStatus()
      if (status.resultsReady()) {
        return status.resultsHandle()
      }
    } catch (e) {
      console.log(`Error fetching query status: ${e}`)
    }

    const now = Date.now()
    if (deadline < now + delayMs) {
      throw new Error(
        `Query results not ready within ${timeoutMs / 1000} seconds.`
      )
    }

    if (status !== null) {
      console.log(`Query status: ${status}`)
    }
    console.log(
      `Query results not ready yet, sleeping for ${delayMs / 1000} seconds...`
    )
    await new Promise((resolve) => setTimeout(resolve, delayMs))
  }
}

async function main() {
  // Update this to your cluster
  // IMPORTANT:  The appropriate port needs to be specified. The SDK's default ports are 80 (http) and 443 (https).
  //             If attempting to connect to Capella, the correct ports are most likely to be 8095 (http) and 18095 (https).
  //             Capella example: https://cb.2xg3vwszqgqcrsix.cloud.couchbase.com:18095
  const clusterConnStr = 'https://--your-instance--'
  const username = 'Administrator'
  const password = 'password'
  // User Input ends here.

  const credential = new analytics.Credential(username, password)
  const cluster = analytics.createInstance(clusterConnStr, credential)
  const statement = 'SELECT VALUE SLEEP("x", 100) FROM RANGE(1, 100) AS id;'
  const handle = await cluster.startQuery(statement)

  const resultHandle = await waitForQueryResults(handle, 2500, 60000)
  const res = await resultHandle.fetchResults()

  for await (let row of res.rows()) {
    console.log('Found row: ', row)
  }
  console.log('Metadata: ', res.metadata())
  await resultHandle.discardResults()
}

main()
  .then(() => {
    console.log('Finished.  Exiting app...')
  })
  .catch((err) => {
    console.log('ERR: ', err)
    console.log('Exiting app...')
    process.exit(1)
  })
```

### [](#es-modules)ES Modules

```typescript
/*
 *  Copyright 2016-2026. Couchbase, Inc.
 *  All Rights Reserved.
 *
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 */

import {
    Credential,
    createInstance,
    QueryHandle,
    QueryResultHandle,
    QueryStatus,
  } from 'couchbase-analytics'

  async function waitForQueryResults(
    handle: QueryHandle,
    delayMs: number = 2500,
    timeoutMs: number = 120000
  ): Promise<QueryResultHandle> {
    const deadline = Date.now() + timeoutMs
    let status: QueryStatus | null = null
    while (true) {
      try {
        status = await handle.fetchStatus()
        if (status.resultsReady()) {
          return status.resultsHandle()
        }
      } catch (e) {
        console.log(`Error fetching query status: ${e}`)
      }

      const now = Date.now()
      if (deadline < now + delayMs) {
        throw new Error(
          `Query results not ready within ${timeoutMs / 1000} seconds.`
        )
      }

      if (status !== null) {
        console.log(`Query status: ${status}`)
      }
      console.log(
        `Query results not ready yet, sleeping for ${delayMs / 1000} seconds...`
      )
      await new Promise((resolve) => setTimeout(resolve, delayMs))
    }
  }

  async function main(): Promise<void> {
    // Update this to your cluster
    // IMPORTANT:  The appropriate port needs to be specified. The SDK's default ports are 80 (http) and 443 (https).
    //             If attempting to connect to Capella, the correct ports are most likely to be 8095 (http) and 18095 (https).
    //             Capella example: https://cb.2xg3vwszqgqcrsix.cloud.couchbase.com:18095
    const clusterConnStr = 'https://--your-instance--'
    const username = 'Administrator'
    const password = 'password'
    // User Input ends here.

    const credential = new Credential(username, password)
    const cluster = createInstance(clusterConnStr, credential)
    const statement = 'SELECT VALUE SLEEP("x", 100) FROM RANGE(1, 100) AS id;'
    const handle = await cluster.startQuery(statement)

    const resultHandle = await waitForQueryResults(handle, 2500, 60000)
    const res = await resultHandle.fetchResults()

    for await (const row of res.rows()) {
      console.log('Found row: ', row)
    }
    console.log('Metadata: ', res.metadata())
    await resultHandle.discardResults()
  }

  main()
    .then(() => {
      console.log('Finished.  Exiting app...')
    })
    .catch((err) => {
      console.log('ERR: ', err)
      console.log('Exiting app...')
      process.exit(1)
    })
```

## [](#query-options)Query Options

The Query Service provides an array of options to customize your query. The following table lists them all:

__Table 1\. Available Query Options__
| Name                                            | Description                                                                                                                                                 |
| ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| abortSignal?: AbortSignal                       | Sets an abort signal for the query allowing the operation to be cancelled.                                                                                  |
| clientContextId?: string                        | The returned client context id for this query.                                                                                                              |
| deserializer?: Deserializer                     | Sets the deserializer used by QueryResult.rows to convert query result rows into objects. If not specified, defaults to the cluster's default deserializer. |
| namedParameters?: {     \[key: string\]: any; } | Named values to be used for the placeholders within the query.                                                                                              |
| positionalParameters?: any\[\]                  | Positional values to be used for the placeholders within the query.                                                                                         |
| raw?: {     \[key: string\]: any; }             | Specifies any additional parameters which should be passed to the query engine when executing the query.                                                    |
| readOnly?: boolean                              | Indicates whether this query should be executed in read-only mode.                                                                                          |
| scanConsistency?: QueryScanConsistency          | Specifies the consistency requirements when executing the query.                                                                                            |
| timeout?: number                                | The timeout for this operation, represented in milliseconds.                                                                                                |

## [](#further-information)Further Information

The [SQL++ for Analytics Reference](../../../analytics/sqlpp/1%5Fintro.md)\] offers a complete guide to the SQL++ language for both of our analytics services, including all of the latest additions.