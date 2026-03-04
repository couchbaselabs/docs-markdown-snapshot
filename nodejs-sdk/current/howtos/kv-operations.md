---
title: Data Operations
editUrl: https://github.com/couchbase/docs-sdk-nodejs/edit/temp/4.6/modules/howtos/pages/kv-operations.adoc
pubDate: 2026-03-04T03:42:46.143Z
link: xref:nodejs-sdk:howtos:kv-operations.adoc[]
---

[View original HTML](/nodejs-sdk/current/howtos/kv-operations.html)

# Data Operations

## [](#documents)Documents

A _document_ refers to an entry in the database (other databases may refer to the same concept as a _row_). A document has an ID (_primary key_ in other databases), which is unique to the document and by which it can be located. The document also has a value which contains the actual application data. See [the concept guide to _Documents_](../concept-docs/documents.md) for a deeper dive into documents in the Couchbase Data Platform. Or read on, for a hands-on introduction to working with documents from the Node.js SDK.

## [](#crud-operations)CRUD Operations

The core interface to Couchbase Server is simple KV operations on full documents. Make sure you’re familiar with the basics of authorization and connecting to a Cluster from the [Start Using the SDK section](../hello-world/start-using-sdk.md). We’re going to expand on the short _Upsert_ example we used there, adding options as we move through the various CRUD operations. Here is the _Insert_ operation at its simplest:

Insert

```javascript
const result = await collection.insert(key, document);
```

Options may be added to operations:

Insert (with options)

```javascript
const result = await collection.insert(key, document,
    { timeout: 10000 } // 10 seconds
);
```

Setting a Compare and Swap (CAS) value is a form of optimistic locking - dealt with in depth in the [CAS page](concurrent-document-mutations.md). Here we just note that the CAS is a value representing the current state of an item; each time the item is modified, its CAS changes. The CAS value is returned as part of a document’s metadata whenever a document is accessed.

_timeout_ is an optional parameter which is represented in milliseconds. Timeout sets the timeout value for the operation. We will add to these options for the _Replace_ example:

```javascript
const result = await collection.replace(key,
    document,
    { cas: cas, expiry: 60, timeout: 5000 }
);
```

Expiration sets an explicit time to live (TTL) for a document. We’ll discuss modifying `Expiration` in more details [below](#expiration-ttl). For a discussion of item (Document) _vs_ Bucket expiration, see the [Expiration Overview page](../../../server/current/learn/data/expiration.md#expiration-bucket-versus-item).

### [](#handling-errors-exceptions)Handling Errors & Exceptions

To illustrate exception handling, here is an example of a `get` method, wrapped in `try / catch` exception handling. The `get` method reads a document from a collection. If the collection does not have a document with this ID, the `get` method also throws `DocumentNotFoundError`.

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

## [](#durability)Durability

```javascript
let result = await collection.upsert(key, document,
    {
        expiry: 60,
        persist_to: 1,
        replicate_to: 0, // cannot replicate on single node
        timeout: 5000
    }
);
```

Here, we have added _Durability_ options, namely `persistTo` and `replicateTo`. In Couchbase Server releases before 6.5, Durability was set with these two options — see the [6.0 Durability documentation](#2.6@nodejs-sdk::durability.adoc) — covering how many replicas the operation must be propagated to and how many persisted copies of the modified record must exist. If a version of Couchbase Server lower than 6.5 is being used then the application can fall-back to this ['client verified' durability](../concept-docs/durability-replication-failure-considerations.md#older-server-versions).

If 6.5 or above is being used, you can take advantage of the [Durable Write](../concept-docs/durability-replication-failure-considerations.md#durable-writes) feature, in which Couchbase Server will only return success to the SDK after the requested replication level has been achieved. The three replication levels are:

* `Majority` \- The server will ensure that the change is available in memory on the majority of configured replicas.
* `MajorityAndPersistToActive` \- Majority level, plus persisted to disk on the active node.
* `PersistToMajority` \- Majority level, plus persisted to disk on the majority of configured replicas.

The options are in increasing levels of safety. Note that nothing comes for free - for a given node, waiting for writes to storage is considerably slower than waiting for it to be available in-memory. These trade offs, as well as which settings may be tuned, are discussed in the [durability page](../concept-docs/durability-replication-failure-considerations.md#durable-writes).

The following example demonstrates using the newer durability features available in Couchbase server 6.5 onwards.

```javascript
let result = await collection.upsert(key, document,
    {
        expiry: 60,  // 60 seconds,
        durabilityLevel: couchbase.DurabilityLevel.None, // Majority etc.
        timeout: 5000
    } // 5 seconds
);
```

To stress, durability is a useful feature but should not be the default for most applications, as there is a performance consideration, and the default level of safety provided by Couchbase will be reasonable for the majority of situations.

> [!TIP]
> Sub-Document Operations
> 
> All of these operations involve fetching the complete document from the Cluster. Where the number of operations or other circumstances make bandwidth a significant issue, the SDK can work on just a specific _path_ of the document with [Sub-Document Operations](subdocument-operations.md).

## [](#preferred-server-group-replica-reads)Preferred Server Group Replica Reads

> [!IMPORTANT]
> Preferred Server Group Replica Reads are only accessible with the Node.js SDK working with Couchbase Server 7.6.2 or newer (Capella or self-managed), from SDK version 4.5.0\.

[Server Groups](../../../server/current/learn/clusters-and-availability/groups.md#understanding-server-group-awareness)can be used to define subsets of nodes within a Couchbase cluster, which contain a complete set of vbuckets (active or replica). As well as high availability use cases, Servre Groups can also be used to keep much traffic within the same cloud Availability Zone.

For Capella users with high data volumes, egress charges for reads from other Availability Zones (AZ) in AWS can be a significant cost. The Node.js SDK, when making read replica requests, can make a request to a preferred Server Group — in this case the local AZ — and set to always read from a copy of the document in this local zone. This is done by putting cluster nodes in the same AZ into the same [Server Group](../../../server/current/learn/clusters-and-availability/groups.md#server-groups-and-vbuckets), too.

This may mean the application has to be tolerant of slight inconsistencies, until the local replica catches up. Alternatively, it may demand a stronger level of durability, to ensure that all copies of a document are consistent before they are accessible — provided that this is `persistToMajority` with [no more than one replica](../../../server/current/learn/data/durability.md#majority).

Couchbase does not recommend this feature where read consistency is critical, but with the appropriate durability settings consistency can be favored ahead of availability.

> [!CAUTION]
> Replicas, Nodes, and Server Groups
> 
> Implicit in the rules for durability, and the process of setting up Server Groups, is the following information — which we mention here explicitly to ensure it is all noted:
> 
> * Moving servers between Server Groups updates the `clustermap` immediately, but to move the data, an administrator **must** perform rebalance. Until the rebalance is complete, the SDK will see and be able to 'use' the new server groups, but the `vBucketMap` may still refer to data in the previous locations.
> * The cluster should have enough nodes and group to make sure that copies of the same document are not stored on the same node, and each group has nodes that cover all 1024 vbuckets (in other words, the number of the groups does not exceeds number of the copies: `active+num_replicas`). The Admin UI should emit small yellow warning if the configuration is considered unbalanced.
> * Setting **three** replicas for the bucket [disables durability for sync writes](../../../server/current/learn/data/durability.md#majority), also precluding the use of [multi-document ACID transactions](../concept-docs/transactions.md).

## [](#retrieving-full-documents)Retrieving full documents

Using the `get()` method with the document key can be done in a similar fashion to the other operations:

```javascript
const result = await collection.get(key);
document = result.value;
```

Timeout can also be set - as in the earlier `Insert` example:

Get (with options)

```javascript
const result = await collection.get(key, { timeout: 1000 });
document = result.value;
```

## [](#removing)Removing

When removing a document, you will have the same concern for durability as with any additive modification to the Bucket:

Remove (with options)

```javascript
const result = await collection.remove(key,
    {
        cas: cas,
        persist_to: 0,  // non-zero gives "not implemented"
        replicate_to: 0, // cannot replicate on single node
        timeout: 5000
    }
);
```

## [](#expiration-ttl)Expiration / TTL

By default, Couchbase documents do not expire, but transient or temporary data may be needed for user sessions, caches, or other temporary documents. Using `touch()`, or setting the `expiry` option for certain mutation operations, you can set expiration values on documents to handle transient data.

You can set an expiry value as relative seconds from now by passing in a number. A relative expiry should only be used when the expiry value is less than 50 years. For expiry values greater than 50 years, use an absolute expiry value (see below).

> [!IMPORTANT]
> Using a Unix timestamp (e.g. `Math.floor(Date.now() / 1000) + 100 // 100 seconds`) as an absolute value is not supported. As of v4.6.0 absolute values should be specified as a `Date`. Prior to v4.6.0 expiry should only be specifed as a relative number of seconds.

Using `touch()`:

```javascript
const result = await collection.touch(key, 100); // 100 seconds
```

Using `insert()`:

```javascript
const result = await collection.insert(key, document,
    { expiry: 100 } // 100 seconds
);
```

From version 4.6.0 on, expiry can be expressed as an absolute value by passing in a `Date`.

Using `touch()`:

```javascript
const expiryAsAbsoluteDate = (seconds) => {
    const now = new Date()
    return new Date(now.getTime() + seconds * 1000)
}
const expiryDate = expiryAsAbsoluteDate(60 * 24 * 60 * 60);  // 60 days
const result = await collection.touch(key, expiryDate);
```

Using `insert()`:

```javascript
const expiryAsAbsoluteDate = (seconds) => {
    const now = new Date()
    return new Date(now.getTime() + seconds * 1000)
}
const expiryDate = expiryAsAbsoluteDate(60 * 24 * 60 * 60);  // 60 days
const result = await collection.insert(key, document,
    { expiry: expiryDate }
);
```

A network timeout can be set with the options, in the same fashion as earlier examples on this page:

```javascript
const result = await collection.touch(key, 100,  // 100 seconds
    { timeout: 5000 } // 5 seconds
);
```

## [](#atomic-counters)Atomic Counters

The value of a document can be increased or decreased atomically using `binary().increment()` and `binary().decrement()`.

> [!NOTE]
> Increment & Decrement are considered part of the ‘binary’ API and as such may still be subject to change

Increment

```javascript
// increment binary value by 1
const result = await collection.binary().increment(binValKey, 1);
```

Increment (with options)

```javascript
// increment binary value by 1, if binValKey doesn’t exist, seed it at 1000
const result = await collection.binary().increment(binValKey, 1, {
    initial: 1000,
    timeout: 5000
});
```

Decrement

```javascript
// decrement binary value by 1
const result = await collection.binary().decrement(binValKey, 1);
```

Decrement (with options)

```javascript
// decrement binary value by 1, if binValKey doesn’t exist, seed it at 1000
const result = await collection.binary().decrement(binValKey, 1,
    {
        initial: 1000,
        timeout: 5000
    },
);
```

> [!TIP]
> Setting the document expiry time only works when a document is created, and it is not possible to update the expiry time of an existing counter document with the Increment method — to do this during an increment, use with the `Touch()` method.

### [](#atomicity-across-data-centers)Atomicity Across Data Centers

If you are using [Cross Data Center Replication](../../../server/current/manage/manage-xdcr/xdcr-management-overview.md) (XDCR), be sure to avoid modifying the same counter in more than one datacenter. If the same counter is modified in multiple datacenters between replications, the counter will no longer be atomic, and its value can change in unspecified ways.

A counter must be incremented or decremented by only a single datacenter. Each datacenter must have its own set of counters that it uses — a possible implementation would be including a datacenter name in the counter document ID.

## [](#kv-range-scan)KV Range Scan

A range scan gives you documents from a collection, even if you don’t know the document IDs. This feature requires Couchbase Server 7.6 or newer.

> [!TIP]
> KV range scan is suitable for use cases that require relatively low concurrency and tolerate relatively high latency. If your application does many scans at once, or requires low latency results, we recommend using SQL++ (with a primary index on the collection) instead of KV range scan.

### [](#kv-range-scan-range)Range scan

Here’s an example of a KV range scan that gets all documents in a collection:

KV Range Scan for all documents in a collection

```javascript
const { RangeScan } = require('couchbase/dist/rangeScan')

result = await collection.scan(new RangeScan()) (1)
result.forEach((r) => {
  console.log(`Found result, ID=${r.id}, content=`, r.content)
})
```

| **1** | The RangeScan class has two optional parameters: start and end. If you omit them like in this example, you’ll get all documents in the collection. These parameters are for advanced use cases; you probably won’t need to specify them. Instead, it’s more common to use the "prefix" scan type shown in the next example. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#kv-range-scan-prefix)Prefix scan

KV range scan can also give you all documents whose IDs start with the same prefix. Imagine you have a collection where documents are named like this: `<username>::<uuid>`. In other words, the document ID starts with the name of the user associated with the document, followed by a delimiter, and then a UUID. If you use this document naming scheme, you can use a prefix range scan to get all documents associated with a user. For example, to get all documents associated with user "alice", you would write:

KV Range Scan for all documents in a collection whose IDs start with `alice::`

```javascript
const { PrefixScan } = require('couchbase/dist/rangeScan')

result = await collection.scan(new PrefixScan('alice::'))
result.forEach((r) => {
  console.log(`Found result, ID=${r.id}, content=`, r.content)
})
```

### [](#kv-range-scan-sample)Sample scan

If you want to get random documents from a collection, use a sample scan.

KV Range Scan for 100 random documents

```javascript
const { SamplingScan } = require('couchbase/dist/rangeScan')

result = await collection.scan(new SamplingScan(100))
result.forEach((r) => {
  console.log(`Found result, ID=${r.id}, content=`, r.content)
})
```

### [](#kv-range-scan-only-ids)Get IDs instead of full documents

If you only want the document IDs, set the `idsOnly` field of `ScanOptions` to `true`, like this:

KV Range Scan for all document IDs in a collection

```javascript
result = await collection.scan(new RangeScan(), {idsOnly: true})
result.forEach((r) => {
  console.log(`Found result, ID=${r.id}`)
})
```

## [](#scoped-kv-operations)Scoped KV Operations

It is possible to perform scoped key value operations on named [Collections](../../../server/current/learn/data/scopes-and-collections.md) _with Couchbase Server release, 7.0_.

Here is an example showing an upsert in the `users` collection, which lives in the `travel-sample.tenant_agent_00` keyspace:

```javascript
const sampleOptions = { username: 'Administrator', password: 'password' };
const sampleCluster = new couchbase.Cluster("localhost", sampleOptions);
const sampleBucket = sampleCluster.bucket("travel-sample");
const sampleScope = sampleBucket.scope("tenant_agent_00");
sampleColl = sampleScope.collection("users");

[data-source-url=https://github.com/couchbase/docs-sdk-nodejs/blob/67bef15ecd5f68dafa3ec93b955a300ffc8e2ec7/modules/devguide/examples/nodejs/kv-operations.js#L584-L585]
let collDocument = { name: 'John Doe', preferred_email: 'johndoe111@test123.test' };
result = await sampleColl.upsert(user, collDocument);
```

## [](#additional-resources)Additional Resources

Working on just a specific path within a JSON document will reduce network bandwidth requirements - see the [Sub-Document](subdocument-operations.md) pages.

Another way of increasing network performance is to _pipeline_ operations with [Batching Operations](concurrent-async-apis.md#batching).

As well as various [Formats](../concept-docs/data-model.md) of JSON, Couchbase can work directly with [arbitary bytes, or binary format](../concept-docs/nonjson.md).

Our [Query Engine](n1ql-queries-with-sdk.md) enables retrieval using SQL++ (formerly N1QL).