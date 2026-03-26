---
title: Hello World
description: Install, connect, try. A quick start guide to get you up and
  running with Couchbase and the Node.js SDK.
editUrl: https://github.com/couchbase/docs-sdk-nodejs/edit/temp/4.4/modules/hello-world/pages/start-using-sdk.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:4.4@nodejs-sdk:hello-world:start-using-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/nodejs-sdk/4.4/hello-world/start-using-sdk.html)

# Hello World

> Install, connect, try. A quick start guide to get you up and running with Couchbase and the Node.js SDK. 

Couchbase has a simple interface for creating and modifying records in a document, based upon the **collection** into which the documents are organized. You can read more about data modeling [below](#data-modeling), but first let's look at those data operations, and installing the Node.js SDK.

Upsert with a Unique ID

```javascript
const docId = crypto.randomUUID()
await collection.upsert(docId, json)
```

`upsert` inserts (creates) the document if it does not exist, or replaces it if it does. We'll explore creating and retrieving data records in more detail [below](#create-read-update-delete), after walking through a quick installation.

## [](#before-you-start)Before You Start

Couchbase Capella, our Database-as-a-Service, lets you get on with what matters, while we take care of the administration for you. Alternately, if you need to control every aspect of deployment — or just want to run the Server in a VM on your laptop — there are several self-managed options available:

* Couchbase Capella
* Self-Managed Couchbase Server

If you haven't already got a cluster set up, the easiest route is to [sign up to Couchbase Capella and deploy a free tier cluster](https://cloud.couchbase.com/sign-up), then come back to this page. Make a note of the [endpoint](../../../cloud/get-started/connect.md) to connect to, and remember the credentials for the user that you set up.

Install Couchbase Server locally, or in your private Cloud:

* [Deployment overview](../../../server/7.6/install/get-started.md)
* [Docker Install](../../../server/7.6/install/getting-started-docker.md)
* [Couchbase Autonomous Operator](../../../operator/current/overview.md)

  * [Kubernetes](../../../operator/current/install-kubernetes.md)
  * [Openshift](../../../operator/current/install-openshift.md)
* [Cloud Marketplace](#7.6server:cloud:couchbase-cloud-deployment.adoc):

  * [AWS Marketplace](../../../server/7.6/cloud/couchbase-aws-marketplace.md)
  * [Azure Marketplace](../../../server/7.6/cloud/couchbase-azure-marketplace.md)
  * [GCP Marketplace](../../../server/7.6/cloud/couchbase-gcp-cloud-launcher.md)

For the example code below to run, you'll need the username and password of the Administrator user that you create, and the IP address of at least one of the nodes of the cluster.

### [](#prerequisites)Prerequisites

* The Node.js SDK is tested against LTS versions of Node.js — see the [compatibility docs](../project-docs/compatibility.md).

The code examples also assume:

* Couchbase Capella
* Self-Managed Couchbase Server

* You have signed up to [Couchbase Capella](https://cloud.couchbase.com/sign-up).
* You have created your own bucket, or loaded the Travel Sample dataset. Note, the Travel Sample dataset is installed automatically when deploying a Capella free tier cluster.
* A user is created with permissions to access the cluster (at least Application Access permissions). See the [Capella connection page](../../../cloud/get-started/run-first-queries.md#credentials) for more details.

> [!IMPORTANT]
> Couchbase Capella uses [Roles](../../../cloud/organizations/organization-projects-overview.md) to control user access to cluster resources. For the purposes of this guide, you can use the **Organization Owner** role automatically assigned to your account during installation of the Capella cluster. In production, Couchbase strongly recommends setting up users with more granular access roles as a best practice for data security.

* [Couchbase Server](#7.6@server:getting-started/do-a-quick-install.adoc) is installed and accessible locally.
* You have created your own bucket, or loaded the Travel Sample dataset using the [Web interface](../../../server/7.6/manage/manage-settings/install-sample-buckets.md#install-sample-buckets-with-the-ui).
* A user is created with permissions to access your cluster (at least Application Access permissions). See [Manage Users, Groups and Roles](../../../server/7.6/manage/manage-security/manage-users-and-roles.md) for more details.

> [!IMPORTANT]
> Couchbase Server uses [Role-Based Access Control (RBAC)](../../../server/7.6/learn/security/roles.md) to control access to cluster resources. In this guide we suggest using the **Full Admin** role created during setup of your local Couchbase Server cluster. In production, Couchbase strongly recommends setting up users with more granular access roles as a best practice for data security.

## [](#installation)Installation

More details of the installation process are in the [full installation guide](../project-docs/sdk-full-installation.md).

```console
$ npm install couchbase --save
```

This will download the latest Couchbase Node.js SDK, and add a dependency to your `package.json`.

### [](#typescript-support)TypeScript Support

If you intend to use `TypeScript` instead of `JavaScript`, then also do the following:

```console
$ npm install -g typescript ts-node
```

### [](#grab-the-code)Grab the Code

If you're all set up and in a real hurry, just grab this code sample and add in your Capella details.

Complete Hello World code sample \[**Click to open or collapse the listing**\] 

* JavaScript
* TypeScript

```javascript
/*
 * Copyright (c) 2024 Couchbase, Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import couchbase from 'couchbase'

async function main() {
    // tag::connect[]
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
    // end::connect[]

    // tag::bucket[]
    const bucket = cluster.bucket(bucketName)
    // end::bucket[]

    // tag::collection[]
    const collection = bucket.scope('inventory').collection('airport')
    // end::collection[]

    // tag::json[]
    const json = {
        "status": "awesome"
    }
    // end::json[]

    // tag::upsert[]
    const docId = crypto.randomUUID()
    await collection.upsert(docId, json)
    // end::upsert[]

    // tag::get[]
    try {
        let getResult = await collection.get(docId)
        console.log('Couchbase is ' + getResult.content.status)
    } catch (e) {
        if (e instanceof couchbase.DocumentNotFoundError) {
            console.log("Document does not exist")
        } else {
            console.log(`Error: ${e}`)
        }
    }
    // end::get[]

    const newJson = {
        "status": "fast"
    }

    // tag::replace[]
    const replaceOpts = {
        expiry: 10,
        durabilityLevel: DurabilityLevel.Majority
    }
    await collection.replace(docId, newJson, replaceOpts)
    // end::replace[]

    // tag::remove[]
    await collection.remove(docId)
    // end::remove[]
}

main()
    .catch((err) => {
        console.log('ERR:', err);
        process.exit(1);
    })
    .then(() => process.exit());
```

```typescript
/*
 * Copyright (c) 2024 Couchbase, Inc.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *    http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

import {
    Bucket,
    Cluster,
    Collection,
    connect,
    ConnectOptions,
    DocumentNotFoundError,
    DurabilityLevel,
    GetResult,
    ReplaceOptions,
} from 'couchbase'

async function main() {
    // tag::connect[]
    const clusterConnStr =
        'couchbases://cb.<your-endpoint>.cloud.couchbase.com'
    const username = 'username'
    const password = 'Password!123'
    const bucketName = 'travel-sample'

    const connectOptions: ConnectOptions = {
        username: username,
        password: password,
        // Sets a pre-configured profile called "wanDevelopment" to help avoid latency issues
        // when accessing Capella from a different Wide Area Network
        // or Availability Zone (e.g. your laptop).
        configProfile: 'wanDevelopment'
    }

    const cluster: Cluster = await connect(clusterConnStr, connectOptions)
    // end::connect[]

    // tag::bucket[]
    const bucket: Bucket = cluster.bucket(bucketName)
    //end::bucket[]

    // tag::collection[]
    const collection: Collection = bucket.scope('inventory').collection('airport')
    // end::collection[]

    // tag::json[]
    const json = {
        "status": "awesome"
    }
    // end::json[]

    // tag::upsert[]
    const docId = crypto.randomUUID()
    await collection.upsert(docId, json)
    // end::upsert[]

    // tag::get[]
    try {
        let getResult: GetResult = await collection.get(docId)
        console.log('Couchbase is ' + getResult.content.status)
    } catch (e) {
        if (e instanceof DocumentNotFoundError) {
            console.log("Document does not exist")
        } else {
            console.log(`Error: ${e}`)
        }
    }
    // end::get[]
    const newJson = {
        "status": "fast"
    }

    // tag::replace[]
    const replaceOpts: ReplaceOptions = {
        expiry: 10,
        durabilityLevel: DurabilityLevel.Majority
    }
    await collection.replace(docId, newJson, replaceOpts)
    // end::replace[]

    // tag::remove[]
    await collection.remove(docId)
    // end::remove[]
}

// Run the main function
main()
    .catch((err) => {
        console.log('ERR:', err)
        process.exit(1)
    })
    .then(() => process.exit())
```

Otherwise, read on as we introduce the CRUD API and connection to Capella or self-managed Couchbase Server.

> [!TIP]
> There's a **View** link to the complete sample code on GitHub above each of the snippets on these SDK pages, and a **Copy** icon to grab just the snippet shown.

> [!NOTE]
> The code samples on this page use ESModules, but the Node.js SDK is fully compatible with CommonJS as well. Simply adjust the import syntax as needed.

## [](#connect-to-your-database)Connect to your Database

Connect to your Couchbase Capella operational cluster (or your local Couchbase Cluster, if you are trying out self-managed Couchbase).

* Couchbase Capella (JavaScript)
* Couchbase Capella (Typescript)
* Self-Managed Couchbase Server (Javascript)
* Self-Managed Couchbase Server (Typescript)

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

Note, the client certificate for connecting to a Capella cluster is included in the SDK installation.

```typescript
const clusterConnStr =
    'couchbases://cb.<your-endpoint>.cloud.couchbase.com'
const username = 'username'
const password = 'Password!123'
const bucketName = 'travel-sample'

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

Note, the client certificate for connecting to a Capella cluster is included in the SDK installation.

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

```javascript
// For a secure cluster connection, use `couchbases://<your-cluster-ip>` instead.
const clusterConnStr = 'couchbase://localhost'
const username = 'username'
const password = 'Password!123'
const bucketName = 'travel-sample'

const connectOptions: ConnectOptions = {
    username: username,
    password: password,
}

const cluster: Cluster = await connect(clusterConnStr, connectOptions)
```

The `ClientOptions` are covered more fully on the [Client Settings](../ref/client-settings.md) page.

For a deeper look at connection options, read [Managing Connections](../howtos/managing-connections.md).

> [!TIP]
> The connection code for getting started uses the Administrator password that you were given during set up. In any production app you should create a role restricted to the permissions needed for your app

### [](#opening-a-bucket)Opening a Bucket

Following successful authentication, open the bucket with:

* Javascript
* Typescript

```javascript
const bucket = cluster.bucket(bucketName)
```

```typescript
const bucket: Bucket = cluster.bucket(bucketName)
```

**Collections** allow documents to be grouped by purpose or theme, according to a specified **scope** — see data modeling, [below](#data-modeling). Here we will use the `airport` collection within the `inventory` scope from `travel-sample` bucket as an example.

* Javascript
* Typescript

```javascript
const collection = bucket.scope('inventory').collection('airport')
```

```typescript
const collection: Collection = bucket.scope('inventory').collection('airport')
```

## [](#create-read-update-delete)Create, Read, Update, Delete

Couchbase documents are organized into buckets, scopes, and collections. [CRUD operations](https://en.wikipedia.org/wiki/CRUD) — Create, Read, Update, Delete — can be performed upon documents in a collection.

### [](#json)JSON

We'll create a regular javascript object to start with:

* Javascript
* Typescript

```javascript
const json = {
    "status": "awesome"
}
```

```typescript
const json = {
    "status": "awesome"
}
```

### [](#insert-create-and-upsert)Insert (Create) and Upsert

`insert` and `upsert` will both create a new document. The difference between the two is that if a document with that key already exists, the `insert` operation will fail, while the `upsert` operation will succeed, replacing the content.

We need to provide a unique ID as the key, and we'll use a UUID here:

Creating a new document

* Javascript
* Typescript

```javascript
const docId = crypto.randomUUID()
await collection.upsert(docId, json)
```

```typescript
const docId = crypto.randomUUID()
await collection.upsert(docId, json)
```

### [](#get-read)Get (Read)

The `get` method reads a document from a collection. If the collection does not have a document with this ID, the `get` method also throws `DocumentNotFoundError`.

* Javascript
* Typescript

```javascript
try {
    let getResult = await collection.get(docId)
    console.log('Couchbase is ' + getResult.content.status)
} catch (e) {
    if (e instanceof couchbase.DocumentNotFoundError) {
        console.log("Document does not exist")
    } else {
        console.log(`Error: ${e}`)
    }
}
```

```typescript
try {
    let getResult: GetResult = await collection.get(docId)
    console.log('Couchbase is ' + getResult.content.status)
} catch (e) {
    if (e instanceof DocumentNotFoundError) {
        console.log("Document does not exist")
    } else {
        console.log(`Error: ${e}`)
    }
}
```

### [](#replace-update)Replace (Update)

The replace method updates the value of an existing document

* Javascript
* Typescript

```javascript
const replaceOpts = {
    expiry: 10,
    durabilityLevel: DurabilityLevel.Majority
}
await collection.replace(docId, newJson, replaceOpts)
```

```typescript
const replaceOpts: ReplaceOptions = {
    expiry: 10,
    durabilityLevel: DurabilityLevel.Majority
}
await collection.replace(docId, newJson, replaceOpts)
```

> [!CAUTION]
> When you replace a document, it's usually good practice to use [optimistic locking](../howtos/concurrent-document-mutations.md). Otherwise, changes might get lost if two people change the same document at the same time.

### [](#remove-delete)Remove (Delete)

The remove method deletes a document from a collection:

* Javascript
* Typescript

```javascript
await collection.remove(docId)
```

```typescript
await collection.remove(docId)
```

## [](#data-modeling)Data Modeling

Documents are organized into collections — collections of documents that belong together. You get to decide what it means to "belong." Developers usually put documents of the same type in the same collection.

For example, imagine you have two types of documents: customers and invoices. You could put the customer documents in a collection called `customers`, and the invoice documents in a collection called `invoices`.

Each document belongs to exactly one collection. A document's ID is unique _within_ the collection.

Different scopes can hold collections with different names. There is no relationship between collections in different scopes. Each collection belongs to just one scope and a collection's name is unique within the scope.

More details can be found on the [Data Model page](../concept-docs/data-model.md).

## [](#what-next)What Next?

### [](#help-and-troubleshooting)Help and Troubleshooting

* [Troubleshooting common network problems](../howtos/troubleshooting-cloud-connections.md).
* [Help forum](https://www.couchbase.com/forums/c/node-js-sdk/12).
* [Discord channel](https://discord.com/channels/915294689681362954/1217642561645318194).
* Read the [error handling page](../howtos/error-handling.md).
* [Get help from Couchbase iQ](../../../cloud/get-started/capella-iq/get-started-with-iq.md#generate-sdk-code-preview).