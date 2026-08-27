---
title: Data Operations
description: Data service offers the simplest way to retrieve or mutate data
  where the key is known. Here we cover CRUD operations, document expiration,
  and optimistic locking with CAS.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-dotnet/edit/temp/3.6/modules/howtos/pages/kv-operations.adoc
  xref: xref:3.6@dotnet-sdk:howtos:kv-operations.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/dotnet-sdk/3.6/howtos/kv-operations.html)

# Data Operations

> Data service offers the simplest way to retrieve or mutate data where the key is known. Here we cover CRUD operations, document expiration, and optimistic locking with CAS. 

## [](#documents)Documents

A _document_ refers to an entry in the database (other databases may refer to the same concept as a _row_). A document has an ID (_primary key_ in other databases), which is unique to the document and by which it can be located. The document also has a value which contains the actual application data. See [the concept guide to _Documents_](../concept-docs/documents.md) for a deeper dive into documents in the Couchbase Data Platform. Or read on, for a hands-on introduction to working with documents from the .NET SDK.

## [](#crud-operations)CRUD Operations

The core interface to Couchbase Server is simple KV operations on full documents. Make sure you're familiar with the basics of authorization and connecting to a Cluster from the [Start Using the SDK section](../hello-world/start-using-sdk.md). We're going to expand on the short _Upsert_ example we used there, adding options as we move through the various CRUD operations. Here is the _Insert_ operation at its simplest:

Insert

```csharp
var document = new {foo = "bar", bar = "foo"};
try {
    var result = await collection.InsertAsync("document-key", document);
}
catch (DocumentExistsException) {
    Console.WriteLine("Document already exists");
}
```

Options may be added to operations:

Insert (with options)

```csharp
try {
    var document = new {foo = "bar", bar = "foo"};

    var result = await collection.InsertAsync("document-key", document,
        options =>
        {
            options.Expiry(TimeSpan.FromDays(1));
            options.Timeout(TimeSpan.FromSeconds(5));
        }
    );
}
catch (DocumentExistsException) {
    // handle exception
}
```

Setting a Compare and Swap (CAS) value is a form of optimistic locking - dealt with in depth in the [CAS page](concurrent-document-mutations.md). Here we just note that the CAS is a value representing the current state of an item; each time the item is modified, its CAS changes. The CAS value is returned as part of a document's metadata whenever a document is accessed. Without explicitly setting it, a newly-created document would have a CAS value of _0_.

_Timeout_ is an optional parameter which in the .NET SDK has a type value of `TimeSpan`. Timeout sets the timeout value for the underlying network connection. We will add to these options for the _Replace_ example:

```csharp
var previousResult = await collection.GetAsync("document-key");
var cas = previousResult.Cas;

var document = new {foo = "bar", bar = "foo"};

var result = await collection.ReplaceAsync("document-key", document,
    options =>
    {
        options.Cas(cas);
        options.Expiry(TimeSpan.FromMinutes(1));
        options.Timeout(TimeSpan.FromSeconds(5));
    }
);
```

Expiration sets an explicit time to live (TTL) for a document. We'll discuss modifying `Expiration` in more details [below](#expiration-ttl). For a discussion of item (Document) _vs_ Bucket expiration, see the [Expiration Overview page](#7.1@server:learn:buckets-memory-and-storage/expiration.adoc#expiration-ttl).

```csharp
var document = new { foo = "bar", bar = "foo" };
var result = await collection.UpsertAsync("document-key", document,
    options =>
    {
        options.Expiry(TimeSpan.FromMinutes(1));
        options.Durability(PersistTo.One, ReplicateTo.One);
        options.Timeout(TimeSpan.FromSeconds(5));
    }
);
```

Here, we have add _Durability_ options, namely `PersistTo` and `ReplicateTo`.

## [](#durability)Durability

In Couchbase Server releases before 6.5, Durability was set with these two options — see the [6.0 Durability documentation](#https://docs.couchbase.com/dotnet-sdk/2.7/durability.html) — covering how many replicas the operation must be propagated to and how many persisted copies of the modified record must exist. If 6.5 or above is being used, you can take advantage of the [Durable Write](../concept-docs/durability-replication-failure-considerations.md#durable-writes) feature, in which Couchbase Server will only return success to the SDK after the requested replication level has been achieved. The three replication levels are:

* `Majority` \- The server will ensure that the change is available in memory on the majority of configured replicas.
* `MajorityAndPersistToActive` \- Majority level, plus persisted to disk on the active node.
* `PersistToMajority` \- Majority level, plus persisted to disk on the majority of configured replicas.

The options are in increasing levels of safety. Note that nothing comes for free - for a given node, waiting for writes to storage is considerably slower than waiting for it to be available in-memory. These trade offs, as well as which settings may be tuned, are discussed in the [durability page](../concept-docs/durability-replication-failure-considerations.md#durable-writes).

The following example demonstrates using the newer durability features available in Couchbase server 6.5 onwards.

```csharp
var document = new { foo = "bar", bar = "foo" };
var result = await collection.UpsertAsync("document-key", document,
    options =>
    {
        options.Expiry(TimeSpan.FromMinutes(1));
        options.Durability(DurabilityLevel.Majority);
        options.Timeout(TimeSpan.FromSeconds(5));
    }
);
```

If a version of Couchbase Server earlier than 6.5 is being used then the application can fall-back to ['client verified' durability](../concept-docs/durability-replication-failure-considerations.md#older-server-versions). Here the SDK will do a simple poll of the replicas and only return once the requested durability level is achieved.

To stress, durability is a useful feature but should not be the default for most applications, as there is a performance consideration, and the default level of safety provided by Couchbase will be reasonable for the majority of situations.

> [!TIP]
> Sub-Document Operations
> 
> All of these operations involve fetching the complete document from the Cluster. Where the number of operations or other circumstances make bandwidth a significant issue, the SDK can work on just a specific _path_ of the document with [Sub-Docunent Operations](subdocument-operations.md).

## [](#retrieving-full-documents)Retrieving full documents

Using the `GetAsync()` method with the document key can be done in a similar fashion to the other operations:

```csharp
var previousResult = await collection.UpsertAsync("string-key", "string value");

using var result = await collection.GetAsync("string-key");
var content = result.ContentAs<String>();
```

Timeout can also be set - as in the earlier `Insert` example:

Get (with options)

```csharp
var result = await collection.GetAsync("string-key",
    options =>
    {
        options.Timeout(TimeSpan.FromSeconds(5));
    }
);
var content = result.ContentAs<string>();
```

## [](#removing)Removing

When removing a document, you will have the same concern for durability as with any additive modification to the Bucket:

Remove (with options)

```csharp
var previousResult = await collection.GetAsync("document-key");

await collection.RemoveAsync("document-key",
    options =>
    {
        options.Cas(previousResult.Cas);
        options.Timeout(TimeSpan.FromSeconds(5));
    }
);
```

## [](#expiration-ttl)Expiration / TTL

By default, Couchbase documents do not expire, but transient or temporary data may be needed for user sessions, caches, or other temporary documents. Using `Touch()`, you can set expiration values on documents to handle transient data:

```csharp
await collection.TouchAsync("document-key", TimeSpan.FromSeconds(10));
```

A network timeout can be set with the optional `TouchOptions()`, in the same fashion as earlier examples on this page:

```csharp
await collection.TouchAsync("document-key", TimeSpan.FromSeconds(30),
    options =>
    {
        options.Timeout(TimeSpan.FromSeconds(5));
    }
);
```

> [!NOTE]
> If the absolute value of the expiry is less than 30 days (such as `60 * 60 * 24 * 30`), it is considered an _offset_. If the value is greater, it is considered an _absolute time stamp_. For more on expiration see the [expiration section](../concept-docs/documents.md#setting-document-expiration) of our documents discussion doc.

> [!IMPORTANT]
> If you are using the overloads that take `IDocument`, note that the `IDocument.Expiry` property assumes ms (milli-seconds), and is converted to seconds before being sent to the server. All other overloads take a `TimeSpan` or an `uint`, and assume an expiry in seconds A time of zero will set the document to never expire (a negative number will set expiry to immediate — creating a [tombstone](#7.1@server:learn:buckets-memory-and-storage/storage.adoc#tombstones)). Values above 0ms but below 1000ms are rounded up to one second before being sent to the server — _if you are using .NET SDK 3.0.4 or later_.

## [](#atomic-counters)Atomic Counters

The value of a document can be increased or decreased atomically using `Binary.Increment()` and `Binary.Decrement()`.

> [!NOTE]
> Increment & Decrement are considered part of the 'binary' API and as such may still be subject to change

Increment

```csharp
// increment binary value by 1, if document doesn’t exist, seed it at 1
await collection.Binary.IncrementAsync("binary-key");
```

Increment (with options)

```csharp
await collection.Binary.IncrementAsync("binary-key",
options =>
    {
        options.Delta(1);
        options.Initial(1000);
        options.Timeout(TimeSpan.FromSeconds(5));
    }
);
```

Decrement

```csharp
// decrement binary value by 1, if document doesn’t exist, seed it at 1
await collection.Binary.DecrementAsync("binary-key");
```

Decrement (with options)

```csharp
await collection.Binary.DecrementAsync("binary-key",
    options =>
    {
        options.Delta(1);
        options.Initial(1000);
        options.Timeout(TimeSpan.FromSeconds(5));
    }
);
```

> [!TIP]
> Setting the document expiry time only works when a document is created, and it is not possible to update the expiry time of an existing counter document with the Increment method — to do this during an increment, use with the `Touch()` method.

### [](#atomicity-across-data-centers)Atomicity Across Data Centers

If you are using [Cross Data Center Replication](#7.1@server:manage:manage-xdcr/xdcr-management-overview.adoc) (XDCR), be sure to avoid modifying the same counter in more than one datacenter. If the same counter is modified in multiple datacenters between replications, the counter will no longer be atomic, and its value can change in unspecified ways.

A counter must be incremented or decremented by only a single datacenter. Each datacenter must have its own set of counters that it uses — a possible implementation would be including a datacenter name in the counter document ID.

## [](#scoped-kv-operations)Scoped KV Operations

It is possible to perform scoped key value operations on named [Collections](#7.1@server:learn:data/scopes-and-collections.adoc) with _Couchbase Server release 7.0_ onwards.

Here is an example showing an upsert in the `users` collection, which lives in the `travel-sample.tenant_agent_00` keyspace:

```csharp
var agentScope = await bucket.ScopeAsync("tenant_agent_00");
var usersCollection = await agentScope.CollectionAsync("users");

var content = new { name = "John Doe", preferred_email = "johndoe111@test123.test" };

var result = await usersCollection.UpsertAsync("user-key", content);
```

## [](#kv-range-scan)KV Range Scan

A range scan gives you documents from a collection, even if you don't know the document IDs. This feature requires Couchbase Server 7.6 or newer.

> [!TIP]
> KV range scan is suitable for use cases that require relatively low concurrency and tolerate relatively high latency. If your application does many scans at once, or requires low latency results, we recommend using SQL++ (with a primary index on the collection) instead of KV range scan.

### [](#kv-range-scan-range)Range scan

Here's an example of a KV range scan that gets all documents in a collection:

KV Range Scan for all documents in a collection

```csharp
IAsyncEnumerable<IScanResult> results = collection.ScanAsync(new RangeScan());

await foreach (var scanResult in results)
{
    Log.Information(scanResult.Id);
    Log.Information(scanResult.ContentAs<Hotel>().ToString());
}

// alternate declaration
var scan2 = new RangeScan(from: ScanTerm.Inclusive("id001"), to: ScanTerm.Inclusive("id999"));
```

| **1** | The RangeScan() constructor has two optional nullable parameters: from and to. If you pass null like in this example, you'll get all documents in the collection. These parameters are for advanced use cases; you probably won't need to specify them. Instead, it's more common to use the "prefix" scan type shown in the next example. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

### [](#kv-range-scan-prefix)Prefix scan

KV range scan can also give you all documents whose IDs start with the same prefix.

Imagine you have a collection where documents are named like this: `<username>::<uuid>`. In other words, the document ID starts with the name of the user associated with the document, followed by a delimiter, and then a UUID. If you use this document naming scheme, you can use a prefix range scan to get all documents associated with a user.

For example, to get all documents associated with user "alice", you would write:

KV Range Scan for all documents in a collection whose IDs start with "alice::"

```csharp
IAsyncEnumerable<IScanResult> results = collection.ScanAsync(
    new PrefixScan("alice::")
);

await foreach (var scanResult in results)
{
    Log.Information(scanResult.Id);
}
```

| **1** | Note the scan type is **prefixScan**. |
| ----- | ------------------------------------- |

### [](#kv-range-scan-sample)Sample scan

If you want to get random documents from a collection, use a sample scan.

KV Range Scan for 100 random documents

```csharp
IAsyncEnumerable<IScanResult> results = collection.ScanAsync(
    new SamplingScan(limit: 100)
);

await foreach (var scanResult in results)
{
    Log.Information(scanResult.Id);
}
```

| **1** | In this example, no more than 100 documents are returned. |
| ----- | --------------------------------------------------------- |

### [](#kv-range-scan-only-ids)Get IDs instead of full document

If you only want the document IDs, set the `idsOnly` option to true, like this:

KV Range Scan for all document IDs in a collection

```csharp
IAsyncEnumerable<IScanResult> results = collection.ScanAsync(
    new RangeScan(),
    new ScanOptions().IdsOnly(true));

await foreach (var scanResult in results)
{
    Log.Information(scanResult.Id);
}
```

| **1** | The returned ScanResult objects throw NoSuchElementException if you try to access any property other than Id. |
| ----- | ------------------------------------------------------------------------------------------------------------- |

Setting `IdsOnly` to true also works with the other scan types described above.

## [](#additional-resources)Additional Resources

Working on just a specific path within a JSON document will reduce network bandwidth requirements - see the [Sub-Document](subdocument-operations.md) pages.

Another way of increasing network performance is to _pipeline_ operations with [Batching Operations](concurrent-async-apis.md#batching).

As well as various [Formats](../concept-docs/data-model.md) of JSON, Couchbase can work directly with [arbitary bytes, or binary format](../concept-docs/nonjson.md).

Our [Query Engine](n1ql-queries-with-sdk.md) enables retrieval of information using the SQL-like syntax of SQL++ (formerly N1QL).