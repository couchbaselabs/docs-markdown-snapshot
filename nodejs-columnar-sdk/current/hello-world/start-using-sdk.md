[View original HTML](/nodejs-columnar-sdk/current/hello-world/start-using-sdk.html)

> Install, connect, try. A quick start guide to get you up and running with Columnar and the Node.js Columnar SDK. 

[Capella Columnar](../../../analytics/intro/intro.md) is a real-time analytical database (RT-OLAP) for real time apps and operational intelligence. Although maintaining some syntactic similarities with [the operational SDKs](#home:sdk.adoc), the Node.js Columnar SDK is developed from the ground-up for Columnar’s analytical use cases, and supports streaming APIs to handle large datasets.

|  | Don’t Mix Columnar & Operational SDKs. Do not combine the Node.js Columnar SDK with the Node.js Operational SDK on the same app server (or development machine). This combination is not tested and not supported. There may be problems with different versions of shared dependencies if you try this. This only applies to the Node.js and Python Columnar SDKs. Note, this does not apply to combining our Enterprise Analytics SDKs with our Operational SDKs. See the [Analytics SDK page](#home::analytics-sdk.adoc) for a reminder of which Analytics SDK to use with which Analytics service. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

## [](#before-you-start)Before You Start

Sign up for a [Capella account](../../../cloud/get-started/create-account.md), and choose a [Columnar](../../../analytics/intro/intro.md) cluster.

You’ll need to add your IP address to the allowlist, during the sign-up and cluster creation process (this can also be done at any time, via the UI, should the address change, or if you need to add a new one).

### [](#prerequisites)Prerequisites

The Columnar Node.js SDK supports LTS versions of Node.js — these are 20 and 22 at the time of the 1.0.0 release (October 2024). See the [compatibility page](../project-docs/compatibility.md#platform-compatibility) for more information about platform support.

We recommend using the most recent long-term support (LTS) version of Node.js — at the time of writing (October 2024) this is version 22.

## [](#getting-the-sdk)Getting the SDK

The SDK can be installed via `npm`:

```console
npm install couchbase-columnar
```

For other installation methods, see the [installation page](../project-docs/sdk-full-installation.md).

## [](#connecting-and-executing-a-query)Connecting and Executing a Query

To use there examples, create a collection to work upon by [importing the travel-sample dataset](../../../analytics/intro/examples.md#travel-sample) into your cluster.

### [](#commonjs)CommonJS

```javascript
const columnar = require('couchbase-columnar')

async function main() {
    // Update this to your cluster
    const clusterConnStr = 'couchbases://--your-instance--'
    const username = 'username'
    const password = 'Password123!'
    // User Input ends here.

    const credential = new columnar.Credential(username, password)
    const cluster = columnar.createInstance(clusterConnStr, credential)

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
import { Certificates, Credential, createInstance } from "couchbase-columnar"

async function main() {
    // Update this to your cluster
    const clusterConnStr = 'couchbases://--your-instance--'
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