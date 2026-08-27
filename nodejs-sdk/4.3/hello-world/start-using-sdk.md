---
title: Start Using the Node.js SDK
description: The Couchbase Node.js SDK enables you to interact with a Couchbase
  Server or Capella cluster from the Node.js runtime, using TypeScript or
  JavaScript.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-nodejs/edit/temp/4.3/modules/hello-world/pages/start-using-sdk.adoc
  xref: xref:4.3@nodejs-sdk:hello-world:start-using-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/nodejs-sdk/4.3/hello-world/start-using-sdk.html)

# Start Using the Node.js SDK

> The Couchbase Node.js SDK enables you to interact with a Couchbase Server or Capella cluster from the Node.js runtime, using TypeScript or JavaScript. 

The Couchbase SDK API 3 (implemented by Node.js SDK 3._x_ and 4._x_) is a complete rewrite of the API, reducing the number of overloads to present a simplified surface area, and adding support for Couchbase Server features like [Collections and Scopes](../concept-docs/collections.md) (available from Couchbase Server 7.0).

Node.js SDK 4._x_ implements the same SDK API 3 bindings, but the internals are completely rewritten — using the Couchbase++ library rather than libcouchbase — to allow upcoming new features such as transactions, and fix some long-standing bugs. Please note any [caveats](../project-docs/migrating-sdk-code-to-3.n.md#sdk4-specifics) in the migration guide.

In this guide, you will learn:

* How to [connect to Couchbase Capella or Couchbase Server](#connect).
* How to [add and retrieve Documents](#add-and-retrieve-documents).
* How to [lookup documents](#sql-lookup) with the [SQL++ (formerly N1QL)](https://www.couchbase.com/products/n1ql) query language.

## [](#hello-couchbase)Hello Couchbase

We will go through the code sample step by step, but for those in a hurry to see it, here it is:

* Couchbase Capella (JavaScript)
* Couchbase Capella (TypeScript)
* Local Couchbase Server

To connect to [Couchbase Capella](../../../home/cloud.md), be sure to get the correct endpoint as well as user, password and bucket name.

```javascript
var couchbase = require('couchbase')

async function main() {
  const clusterConnStr = 'couchbases://cb.<your-endpoint>.cloud.couchbase.com'
  const username = 'username'
  const password = 'Password!123'
  const bucketName = 'travel-sample'

  const cluster = await couchbase.connect(clusterConnStr, {
    username: username,
    password: password,
    // Sets a pre-configured profile called "wanDevelopment" to help avoid latency issues
    // when accessing Capella from a different Wide Area Network
    // or Availability Zone (e.g. your laptop).
    configProfile: 'wanDevelopment',
  })

  const bucket = cluster.bucket(bucketName)

  // Get a reference to the default collection, required only for older Couchbase server versions
  const defaultCollection = bucket.defaultCollection()

  const collection = bucket.scope('tenant_agent_00').collection('users')

  const user = {
    type: 'user',
    name: 'Michael',
    email: 'michael123@test.com',
    interests: ['Swimming', 'Rowing'],
  }

  // Create and store a document
  await collection.upsert('michael123', user)

  // Load the Document and print it
  // Prints Content and Metadata of the stored Document
  let getResult = await collection.get('michael123')
  console.log('Get Result: ', getResult)

  // Perform a SQL++ (N1QL) Query
  const queryResult = await bucket
    .scope('inventory')
    .query('SELECT name FROM `airline` WHERE country=$1 LIMIT 10', {
      parameters: ['United States'],
    })
  console.log('Query Results:')
  queryResult.rows.forEach((row) => {
    console.log(row)
  })
}

// Run the main function
main()
  .catch((err) => {
    console.log('ERR:', err)
    process.exit(1)
  })
  .then(process.exit)
```

To connect to [Couchbase Capella](../../../home/cloud.md), be sure to get the correct endpoint as well as user, password and bucket name.

```typescript
'use strict'

import {
  Bucket,
  Cluster,
  Collection,
  connect,
  ConnectOptions,
  GetResult,
  QueryResult,
} from 'couchbase'

async function main() {
  const clusterConnStr: string =
    'couchbases://cb.<your-endpoint>.cloud.couchbase.com'
  const username: string = 'username'
  const password: string = 'Password!123'
  const bucketName: string = 'travel-sample'

  const connectOptions: ConnectOptions = {
    username: username,
    password: password,
    // Sets a pre-configured profile called "wanDevelopment" to help avoid latency issues
    // when accessing Capella from a different Wide Area Network
    // or Availability Zone (e.g. your laptop).
    configProfile: 'wanDevelopment'
  }

  const cluster: Cluster = await connect(clusterConnStr, connectOptions)

  const bucket: Bucket = cluster.bucket(bucketName)

  const collection: Collection = bucket
    .scope('tenant_agent_00')
    .collection('users')

  // Get a reference to the default collection, required only for older Couchbase server versions
  const collection_default: Collection = bucket.defaultCollection()

  interface User {
    type: string
    name: string
    email: string
    interests: string[]
  }

  const user: User = {
    type: 'user',
    name: 'Michael',
    email: 'michael123@test.com',
    interests: ['Swimming', 'Rowing'],
  }

  await collection.upsert('michael123', user)

  // Load the Document and print it
  // Prints Content and Metadata of the stored document
  const getResult: GetResult = await collection.get('michael123')
  console.log('Get Result:', getResult)

  // Perform a N1QL Query
  const queryResult: QueryResult = await bucket
    .scope('inventory')
    .query('SELECT name FROM `airline` WHERE country=$1 LIMIT 10', {
      parameters: ['United States'],
    })
  console.log('Query Results:')
  queryResult.rows.forEach((row) => {
    console.log(row)
  })
}

// Run the main function
main()
  .catch((err) => {
    console.log('ERR:', err)
    process.exit(1)
  })
  .then(() => process.exit(0))
```

As well as the Node.js SDK, and a running instance of Couchbase Server, you will need to load up the Travel Sample Bucket using either the [Web interface](#7.1@server:manage:manage-settings/install-sample-buckets.adoc#install-sample-buckets-with-the-ui)or the [command line](#7.1@server:manage:manage-settings/install-sample-buckets.adoc#install-sample-buckets-with-the-cli).

```nodejs
const couchbase = require('couchbase')

async function main() {
  // For a secure cluster connection, use `couchbases://<your-cluster-ip>` instead.
  const clusterConnStr = 'couchbase://localhost'
  const username = 'Administrator'
  const password = 'password'
  const bucketName = 'travel-sample'

  const cluster = await couchbase.connect(clusterConnStr, {
    username: username,
    password: password,
  })

  const bucket = cluster.bucket(bucketName)

  // Get a reference to the default collection, required only for older Couchbase server versions
  const defaultCollection = bucket.defaultCollection()

  const collection = bucket.scope('tenant_agent_00').collection('users')

  const user = {
    type: 'user',
    name: 'Michael',
    email: 'michael123@test.com',
    interests: ['Swimming', 'Rowing'],
  }

  // Create and store a document
  await collection.upsert('michael123', user)

  // Load the Document and print it
  // Prints Content and Metadata of the stored Document
  let getResult = await collection.get('michael123')
  console.log('Get Result: ', getResult)

  // Perform a N1QL Query
  const queryResult = await bucket
    .scope('inventory')
    .query('SELECT name FROM `airline` WHERE country=$1 LIMIT 10', {
      parameters: ['United States'],
    })
  console.log('Query Results:')
  queryResult.rows.forEach((row) => {
    console.log(row)
  })
}

// Run the main function
main()
  .catch((err) => {
    console.log('ERR:', err)
    process.exit(1)
  })
  .then(process.exit)
```

The Couchbase Capella free tier version comes with the Travel Sample Bucket, and its Query indexes, loaded and ready.

## [](#quick-installation)Quick Installation

```console
$ npm install couchbase --save
```

This will download the latest Couchbase Node.js SDK, and add a dependency to your `package.json`.

Information on new features, fixes, known issues, as well as information on how to install older release versions is in the [release notes](../project-docs/sdk-release-notes.md), and a fuller installation guide can be found [here](../project-docs/sdk-full-installation.md).

### [](#typescript-support)TypeScript Support

If you intend to use `TypeScript` instead of `JavaScript`, then also do the following:

```console
$ npm install -g typescript ts-node
```

## [](#prerequisites)Prerequisites

The following code samples assume:

* Couchbase Capella
* Local Couchbase Server

* You have signed up to [Couchbase Capella](https://cloud.couchbase.com/sign-up).
* You have created your own bucket, or loaded the Travel Sample dataset. Note, the Travel Sample dataset is installed automatically when deploying a Capella free tier cluster..
* A user is created with permissions to access the cluster (at least Application Access permissions). See the [Capella connection page](../../../cloud/get-started/run-first-queries.md#credentials) for more details.

> [!IMPORTANT]
> Couchbase Capella uses [Roles](../../../cloud/organizations/organization-projects-overview.md) to control user access to database resources. For the purposes of this guide, you can use the **Organization Owner** role automatically assigned to your account during installation of the Capella cluster. In a production scenario, we strongly recommend setting up users with more granular access roles as a best practice.

* [Couchbase Server](#7.6@server:getting-started/do-a-quick-install.adoc) is installed and accessible locally.
* You have created your own bucket, or loaded the Travel Sample dataset using the [Web interface](../../../server/7.6/manage/manage-settings/install-sample-buckets.md#install-sample-buckets-with-the-ui).
* A user is created with permissions to access your cluster (at least Application Access permissions). See [Manage Users, Groups and Roles](../../../server/7.6/manage/manage-security/manage-users-and-roles.md) for more details.

> [!IMPORTANT]
> Couchbase Server uses [Role Based Access Control (RBAC)](../../../server/7.6/learn/security/roles.md) to control access to resources. In this guide we suggest using the **Full Admin** role created during setup of your local Couchbase Server cluster. For production client code, you will want to use more appropriate, restrictive settings.

## [](#step-by-step)Step by Step

Create an empty file named `index.js`, or alternatively `index.ts` for TypeScript, and walk through step by step.

Here are all the imports that you will need to run the sample code.

* JavaScript
* TypeScript

```javascript
var couchbase = require('couchbase')
```

```typescript
import {
  Bucket,
  Cluster,
  Collection,
  connect,
  ConnectOptions,
  GetResult,
  QueryResult,
} from 'couchbase'
```

Now, create an empty `main()` function.

```javascript
async function main() {
  // add code here...
}
```

We will update this function as we go along the steps in this guide.

### [](#connect)Connect

Connect to your cluster by calling the `connect()` function and pass it your connection details. The basic connection details that you'll need are given below — for more background information, see [Managing Connections](../howtos/managing-connections.md).

* Couchbase Capella (JavaScript)
* Couchbase Capella (TypeScript)
* Local Couchbase Server

From version 4.1, the Node.js SDK includes Capella's standard certificates by default, so you don't need any additional configuration. You do need to enable TLS, which can be done by simply using `couchbases://` in the connection string as in this example.

```javascript
const clusterConnStr = 'couchbases://cb.<your-endpoint>.cloud.couchbase.com'
const username = 'username'
const password = 'Password!123'
const bucketName = 'travel-sample'

const cluster = await couchbase.connect(clusterConnStr, {
  username: username,
  password: password,
  // Sets a pre-configured profile called "wanDevelopment" to help avoid latency issues
  // when accessing Capella from a different Wide Area Network
  // or Availability Zone (e.g. your laptop).
  configProfile: 'wanDevelopment',
})
```

When accessing Capella from a different Wide Area Network or Availability Zone, you may experience latency issues with the default connection settings. SDK 4.2 introduces a `wanDevelopment` Configuration Profile, which provides pre-configured timeout settings suitable for working in high latency environments. Basic usage is shown in the example above, but if you want to learn more see [Constrained Network Environments](../ref/client-settings.md#constrained-network-environments).

> [!CAUTION]
> The Configuration Profiles feature is currently a [Volatile API](../../current/project-docs/compatibility.md#interface-stability) and may be subject to change.

From version 4.1, the Node.js SDK includes Capella's standard certificates by default, so you don't need any additional configuration. You do need to enable TLS, which can be done by simply using `couchbases://` in the connection string as in this example.

```typescript
  const clusterConnStr: string =
    'couchbases://cb.<your-endpoint>.cloud.couchbase.com'
  const username: string = 'username'
  const password: string = 'Password!123'
  const bucketName: string = 'travel-sample'

  const connectOptions: ConnectOptions = {
    username: username,
    password: password,
    // Sets a pre-configured profile called "wanDevelopment" to help avoid latency issues
    // when accessing Capella from a different Wide Area Network
    // or Availability Zone (e.g. your laptop).
    configProfile: 'wanDevelopment'
  }

  const cluster: Cluster = await connect(clusterConnStr, connectOptions)
```

When accessing Capella from a different Wide Area Network or Availability Zone, you may experience latency issues with the default connection settings. SDK 4.2 introduces a `wanDevelopment` Configuration Profile, which provides pre-configured timeout settings suitable for working in high latency environments. Basic usage is shown in the example above, but if you want to learn more see [Constrained Network Environments](../ref/client-settings.md#constrained-network-environments).

> [!CAUTION]
> The Configuration Profiles feature is currently a [Volatile API](../../current/project-docs/compatibility.md#interface-stability) and may be subject to change.

```javascript
// For a secure cluster connection, use `couchbases://<your-cluster-ip>` instead.
const clusterConnStr = 'couchbase://localhost'
const username = 'Administrator'
const password = 'password'
const bucketName = 'travel-sample'

const cluster = await couchbase.connect(clusterConnStr, {
  username: username,
  password: password,
})
```

For developing locally on the same machine as Couchbase Server, your URI can be `couchbase://localhost` as shown here. For production deployments, you will want to use a secure server, with `couchbases://`.

Following successful authentication, add this code snippet to access your `Bucket`:

* JavaScript
* TypeScript

```javascript
const bucket = cluster.bucket(bucketName)
```

```typescript
const bucket: Bucket = cluster.bucket(bucketName)
```

### [](#add-and-retrieve-documents)Add and Retrieve Documents

The Node.js SDK supports full integration with the [Collections](../concept-docs/collections.md) feature introduced in Couchbase Server 7.0\. _Collections_ allow documents to be grouped by purpose or theme, according to a specified _Scope_.

Here we refer to the `users` collection within the `tenant_agent_00` scope from the Travel Sample bucket as an example, but you may replace this with your own data.

* JavaScript
* TypeScript

```javascript
const collection = bucket.scope('tenant_agent_00').collection('users')
```

```typescript
const collection: Collection = bucket
  .scope('tenant_agent_00')
  .collection('users')
```

The code shows how you would use a named collection and scope. A named or default collection will provide the same functionality as bucket-level operations did in previous versions of Couchbase Server.

> [!NOTE]
> The `defaultCollection` must be used when connecting to a 6.6 cluster or earlier.

* JavaScript
* TypeScript

```javascript
// Get a reference to the default collection, required only for older Couchbase server versions
const defaultCollection = bucket.defaultCollection()
```

```typescript
// Get a reference to the default collection, required only for older Couchbase server versions
const collection_default: Collection = bucket.defaultCollection()
```

[Document operations](../howtos/kv-operations.md), such as storing and retrieving documents, can be done using `Collection.upsert()` and `Collection.get()`.

Add the following code to create a new document and retrieve it:

* JavaScript
* TypeScript

```javascript
const user = {
  type: 'user',
  name: 'Michael',
  email: 'michael123@test.com',
  interests: ['Swimming', 'Rowing'],
}

// Create and store a document
await collection.upsert('michael123', user)

// Load the Document and print it
// Prints Content and Metadata of the stored Document
let getResult = await collection.get('michael123')
console.log('Get Result: ', getResult)
```

```typescript
interface User {
  type: string
  name: string
  email: string
  interests: string[]
}

const user: User = {
  type: 'user',
  name: 'Michael',
  email: 'michael123@test.com',
  interests: ['Swimming', 'Rowing'],
}

await collection.upsert('michael123', user)

// Load the Document and print it
// Prints Content and Metadata of the stored document
const getResult: GetResult = await collection.get('michael123')
console.log('Get Result:', getResult)
```

### [](#sql-lookup)SQL++ Lookup

Couchbase SQL++ queries can be performed at the `Cluster` or `Scope` level by invoking `Cluster.query()` or `Scope.query()`.

Cluster level queries require you to specify the fully qualified keyspace each time (e.g. `travel-sample.inventory.airline`). However, with a Scope level query you only need to specify the Collection name — which in this case is `airline`:

* JavaScript
* TypeScript

```javascript
// Perform a SQL++ (N1QL) Query
const queryResult = await bucket
  .scope('inventory')
  .query('SELECT name FROM `airline` WHERE country=$1 LIMIT 10', {
    parameters: ['United States'],
  })
console.log('Query Results:')
queryResult.rows.forEach((row) => {
  console.log(row)
})
```

```typescript
// Perform a N1QL Query
const queryResult: QueryResult = await bucket
  .scope('inventory')
  .query('SELECT name FROM `airline` WHERE country=$1 LIMIT 10', {
    parameters: ['United States'],
  })
console.log('Query Results:')
queryResult.rows.forEach((row) => {
  console.log(row)
})
```

### [](#execute)Execute!

To ensure that we can run the main function, we add this last line of code:

* JavaScript
* TypeScript

```javascript
// Run the main function
main()
  .catch((err) => {
    console.log('ERR:', err)
    process.exit(1)
  })
  .then(process.exit)
```

```typescript
// Run the main function
main()
  .catch((err) => {
    console.log('ERR:', err)
    process.exit(1)
  })
  .then(() => process.exit(0))
```

Now we can run our code:

* JavaScript
* TypeScript

```console
$ node index.js
```

```console
$ ts-node index.ts
```

The results you should expect are as follows:

```console
Get Result: GetResult {
  content: {
    type: 'user',
    name: 'Michael',
    email: 'michael123@test.com',
    interests: [ 'Swimming', 'Rowing' ]
  },
  cas: Cas<1665739583483674624>,
  expiryTime: undefined
}
Query Results:
{ name: '40-Mile Air' }
{ name: 'Texas Wings' }
{ name: 'Atifly' }
{ name: 'Locair' }
{ name: 'SeaPort Airlines' }
{ name: 'Alaska Central Express' }
{ name: 'AirTran Airways' }
{ name: 'U.S. Air' }
{ name: 'PanAm World Airways' }
{ name: 'Bemidji Airlines' }
```

## [](#next-steps)Next Steps

Now you're up and running, try one of the following:

* Our [Travel Sample Application](sample-application.md) demonstrates all the basics you need to know;
* Explore [Key Value Operations](../howtos/kv-operations.md) against a document database;
* Or [Query](../howtos/n1ql-queries-with-sdk.md) with our SQL++ language;
* Or read up on [which service fits your use case](../concept-docs/data-services.md).

### [](#additional-resources)Additional Resources

The API reference is generated for each release and the latest can be found [here](https://docs.couchbase.com/sdk-api/couchbase-node-client/index.html).

Links to each release are to be found in the [individual release notes](../project-docs/sdk-release-notes.md).

The [Migrating from SDK API 2 to 3](../project-docs/migrating-sdk-code-to-3.n.md) page highlights the main differences to be aware of when migrating your code.

Couchbase welcomes community contributions to the Node.js SDK. The Node.js SDK source code is available on [GitHub](https://github.com/couchbase/couchnode).

### [](#troubleshooting)Troubleshooting

* Couchbase Server is designed to work in the same WAN or availability zone as the client application. If you're running the SDK on your laptop against a Capella cluster, see further information on:

  * Notes on [Constrained Network Environments](../ref/client-settings.md#constrained-network-environments).
  * [Network Requirements](../project-docs/compatibility.md#network-requirements).
  * If you have a consumer-grade router which has problems with DNS-SRV records review our [Troubleshooting Guide](../howtos/troubleshooting-cloud-connections.md#troubleshooting-host-not-found).
* Our [community forum](https://forums.couchbase.com/c/node-js-sdk/12) is a great source of help.