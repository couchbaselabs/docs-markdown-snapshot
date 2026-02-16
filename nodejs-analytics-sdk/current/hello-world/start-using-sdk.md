[View original HTML](/nodejs-analytics-sdk/current/hello-world/start-using-sdk.html)

> Install, connect, try. A quick start guide to get you up and running with Enterprise Analytics and the Node.js Analytics SDK. 

[Enterprise Analytics](../../../analytics/intro/intro.md) is a real-time analytical database (RT-OLAP) for real time apps and operational intelligence. Although maintaining some syntactic similarities with [the operational SDKs](#home::sdk.adoc), the Node.js Analytics SDK is developed from the ground-up for column-based analytical use cases, and supports streaming APIs to handle large datasets.

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

To use these examples, create a collection to work upon by [importing the travel-sample dataset](../../../enterprise-analytics/current/intro/connecting-to-data-sources.md#import-the-travel-sample-collections) into your cluster.

### [](#commonjs)CommonJS

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

### [](#es-modules)ES Modules

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

### [](#connection-string)Connection String

The `clusterConnStr` in the above example should takes the form of "https://<your\_hostname>:" + PORT. The default port is 443, for TLS connections. You do not need to give a port number if you are using port 443 — `hostname = "https://<your_hostname>"` is effectively the same as \`hostname = "https://<your\_hostname>:" + "443"

If you are using a different port — for example, connecting to a cluster without a load balancer, directly to the Analytics port, `18095` — or not using TLS, then see the [Connecting to Enterprise Analytics](../howtos/managing-connections.md) page.

## [](#migration-from-row-based-analytics)Migration from Row-Based Analytics

If you are migrating a project from CBAS — our Analytics service on Capella Operational and Couchbase Server, using our operational SDKs — then information on migration can be found in the [Enterprise Analytics docs](../../../enterprise-analytics/current/migration/overview.md).

In particular, refer to the [SDK section](../../../enterprise-analytics/current/migration/migration-process.md#sdk-migration) of the Enterprise Analytics migration pages.