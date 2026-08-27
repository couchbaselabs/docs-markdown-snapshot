---
title: Node.js Analytics SDK Quickstart Guide
description: Install, connect, try. A quick start guide to get you up and
  running with Enterprise Analytics and the Node.js Analytics SDK.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-analytics-sdk-nodejs/edit/release/1.1/modules/hello-world/pages/start-using-sdk.adoc
  xref: xref:nodejs-analytics-sdk:hello-world:start-using-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/nodejs-analytics-sdk/current/hello-world/start-using-sdk.html)

# Node.js Analytics SDK Quickstart Guide

> Install, connect, try. A quick start guide to get you up and running with Enterprise Analytics and the Node.js Analytics SDK. 

[Enterprise Analytics](../../../analytics/intro/intro.md) is a real-time analytical database (RT-OLAP) for real time apps and operational intelligence. Although maintaining some syntactic similarities with [the operational SDKs](../../../home/sdk.md), the Node.js Analytics SDK is developed from the ground-up for column-based analytical use cases, and supports streaming APIs to handle large datasets.

## [](#before-you-start)Before You Start

Install and configure an [Enterprise Analytics Cluster](../../../enterprise-analytics/current/intro/intro.md).

### [](#prerequisites)Prerequisites

The Analytics Node.js SDK supports LTS versions of Node.js — these are 24 and 22 at the time of the 1.0.0 release (August 2025). See the [compatibility page](../project-docs/compatibility.md#platform-compatibility) for more information about platform support.

## [](#getting-the-sdk)Getting the SDK

The SDK can be installed via `npm`:

```console
npm install couchbase-analytics
```

For other installation methods, see the [installation page](../project-docs/sdk-full-installation.md).

## [](#connecting-and-executing-a-query)Connecting and Executing a Query

Node.js Analytics SDK 1.1 adds support for JWT and client certificate authentication, as well as a new Server Asynchronous Request API that uses request handles to fetch results. Introduced in the self-managed Enterprise Analytics Server 2.2, this API eliminates the need for long-running server connections.

The examples in this first section of the page are for the standard API — async on the client side — working with Enterprise Analytics 2.0 and later (with Server Asynchronous Request API examples following in the [Server Async section](#server-asynchronous-api)). You can still use this API with Enterprise Analytics 2.2 and later, in addition to the new API.

### [](#server-synchronous-request-api)Server Synchronous Request API

#### [](#commonjs)CommonJS

```javascript
const analytics = require('couchbase-analytics')

async function main() {
    // Update this to your cluster
    const clusterConnStr = 'https://<your_hostname>:<PORT>'
    const username = 'username'
    const password = 'Password123!'
    // User Input ends here.

    const credential = new analytics.Credential(username, password)
    const cluster = analytics.createInstance(clusterConnStr, credential)

    // Execute a streaming query with positional arguments.
    let qs = 'SELECT * FROM `travel-sample`.inventory.airline LIMIT 10;'
    let res = await cluster.executeQuery(qs)
    for await (let row of res.rows()) {
        console.log('Found row: ', row)
    }
    console.log('Metadata: ', res.metadata())

    // Execute a streaming query with positional arguments.
    qs =
        'SELECT * FROM `travel-sample`.inventory.airline WHERE country=$1 LIMIT $2;'
    res = await cluster.executeQuery(qs, { parameters: ['United States', 10] })
    for await (let row of res.rows()) {
        console.log('Found row: ', row)
    }
    console.log('Metadata: ', res.metadata())

    // Execute a streaming query with named parameters.
    qs =
        'SELECT * FROM `travel-sample`.inventory.airline WHERE country=$country LIMIT $limit;'
    res = await cluster.executeQuery(qs, {
        parameters: { country: 'United States', limit: 10 },
    })
    for await (let row of res.rows()) {
        console.log('Found row: ', row)
    }
    console.log('Metadata: ', res.metadata())
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

#### [](#es-modules)ES Modules

```javascript
import { Credential, createInstance } from "couchbase-analytics"

async function main() {
    // Update this to your cluster
    const clusterConnStr = 'https://<your_hostname>:<PORT>'
    const username = 'username'
    const password = 'Password123!'
    // User Input ends here.

    const credential = new Credential(username, password)
    const cluster = createInstance(clusterConnStr, credential)

    // Execute a streaming query with positional arguments.
    let qs = "SELECT * FROM `travel-sample`.inventory.airline LIMIT 10;"
    let res = await cluster.executeQuery(qs)
    for await (let row of res.rows()) {
        console.log("Found row: ", row)
    }
    console.log("Metadata: ", res.metadata())

    // Execute a streaming query with positional arguments.
    qs =
        "SELECT * FROM `travel-sample`.inventory.airline WHERE country=$1 LIMIT $2;"
    res = await cluster.executeQuery(qs, { parameters: ["United States", 10] })
    for await (let row of res.rows()) {
        console.log("Found row: ", row)
    }
    console.log("Metadata: ", res.metadata())

    // Execute a streaming query with named parameters.
    qs =
        "SELECT * FROM `travel-sample`.inventory.airline WHERE country=$country LIMIT $limit;"
    res = await cluster.executeQuery(qs, {
        parameters: { country: "United States", limit: 10 },
    })
    for await (let row of res.rows()) {
        console.log("Found row: ", row)
    }
    console.log("Metadata: ", res.metadata())
}

main()
    .then(() => {
        console.log("Finished.  Exiting app...")
    })
    .catch((err) => {
        console.log("ERR: ", err)
        console.log("Exiting app...")
        process.exit(1)
    })
```

### [](#server-asynchronous-api)Server Asynchronous Request API

Enterprise Analytics 2.2 introduces a Server Asynchronous Request API. The SDK sends a request, polls for results, and then fetches once the result is available.

#### [](#commonjs-2)CommonJS

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

#### [](#es-modules-2)ES Modules

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

### [](#connection-string)Connection String

The `clusterConnStr` in the above example should takes the form of "https://<your\_hostname>:" + PORT. The default port is 443, for TLS connections. You do not need to give a port number if you are using port 443 — `hostname = "https://<your_hostname>"` is effectively the same as \`hostname = "https://<your\_hostname>:" + "443"

If you are using a different port — for example, connecting to a cluster without a load balancer, directly to the Analytics port, `18095` — or not using TLS, then see the [Connecting to Enterprise Analytics](../howtos/managing-connections.md) page.

## [](#migration-from-row-based-analytics)Migration from Row-Based Analytics

If you are migrating a project from CBAS — our Analytics service on Capella Operational and Couchbase Server, using our operational SDKs — then information on migration can be found in the [Enterprise Analytics docs](../../../enterprise-analytics/current/migration/overview.md).

In particular, refer to the [SDK section](../../../enterprise-analytics/current/migration/migration-process.md#sdk-migration) of the Enterprise Analytics migration pages.