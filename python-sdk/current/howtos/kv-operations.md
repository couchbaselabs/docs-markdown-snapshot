---
title: Data Operations
description: Key Value (KV) or data service offers the simplest way to retrieve
  or mutate data where the key is known.
editUrl: https://github.com/couchbase/docs-sdk-python/edit/temp/4.5/modules/howtos/pages/kv-operations.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:python-sdk:howtos:kv-operations.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/python-sdk/current/howtos/kv-operations.html)

# Data Operations

> Key Value (KV) or data service offers the simplest way to retrieve or mutate data where the key is known. Here we cover CRUD operations, document expiration, and optimistic locking with CAS. 

The complete code sample used on this page can be downloaded from [the GitHub repo for the Python docs](https://github.com/couchbase/docs-sdk-python/blob/release/4.5/modules/howtos/examples/kv%5Foperations.py), from which you can see in context how to authenticate and connect to a Couchbase Cluster, then perform these Collection operations.

## [](#documents)Documents

A _document_ refers to an entry in the database (other databases may refer to the same concept as a _row_). A document has an ID (_primary key_ in other databases), which is unique to the document and by which it can be located. The document also has a value which contains the actual application data. See [the concept guide to _Documents_](../concept-docs/documents.md) for a deeper dive into documents in the Couchbase Data Platform. Or read on, for a hands-on introduction to working with documents from the Python SDK.

## [](#crud-operations)CRUD Operations

The core interface to Couchbase Server is simple KV operations on full documents. Make sure you’re familiar with the basics of authorization and connecting to a Cluster from the [Start Using the SDK section](../hello-world/start-using-sdk.md). We’re going to expand on the short _Upsert_ example we used there, adding options as we move through the various CRUD operations. Here is the _Insert_ operation at its simplest:

Insert

```python
# Insert document
document = {"foo": "bar", "bar": "foo"}
result = collection.insert("document-key", document)
cas = result.cas
```

Options may be added to operations. It is best practice to use the \*Options() class that matches name of the operation (e.g. GetOptions(), InsertOptions(), etc.). However, keyword arguments can be used as an override to a corresponding value within the options.

Options like _timeout_ and _expiry_ are timedelta objects.

Insert (with options)

```python
# Insert document with options
document = {"foo": "bar", "bar": "foo"}
opts = InsertOptions(timeout=timedelta(seconds=5))
result = collection.insert("document-key-opts",
                           document,
                           opts,
                           expiry=timedelta(seconds=30))
```

Expiration sets an explicit time to live (TTL) for a document. We’ll discuss modifying `Expiration` in more details [below](#expiration-ttl). For a discussion of item (Document) _vs_ Bucket expiration, see the [Expiration Overview page](#6.6@server:learn:buckets-memory-and-storage/expiration.adoc#expiration-bucket-versus-item).

### [](#cas)CAS

Setting a Compare and Swap (CAS) value is a form of optimistic locking — dealt with in depth in the [CAS page](concurrent-document-mutations.md). Here we just note that the CAS is a value representing the current state of an item; each time the item is modified, its CAS changes. The CAS value is returned as part of a document’s metadata whenever a document is accessed. Without explicitly setting it, a newly-created document would have a CAS value of _0_.

```python
# Replace document with CAS
document = {"foo": "bar", "bar": "foo"}
result = collection.replace(
    "document-key",
    document,
    cas=cas,
    timeout=timedelta(
        minutes=1))
```

Typically we would want to use CAS for something more meaningful like performing a Get, modifying the result and updating the document. By using the CAS value we know that if anyone else modified this document and updated it before our update then ours will error.

```python
# Replace document with CAS
result = collection.get("document-key")
doc = result.content_as[dict]
doc["bar"] = "baz"
opts = ReplaceOptions(cas=result.cas)
result = collection.replace("document-key", doc, opts)
```

## [](#durability)Durability

Writes in Couchbase are written to a single node, and from there the Couchbase Server will take care of sending that mutation to any configured replicas. The optional durability parameter, which all mutating operations accept, allows the application to wait until this replication (or persistence) is successful before proceeding.

In Couchbase Server releases before 6.5, Durability was set with two options — see the [6.0 Durability documentation](#2.5@python-sdk::durability.adoc) — covering how many replicas the operation must be propagated to and how many persisted copies of the modified record must exist. Couchbase Data Platform 6.5 refines these two options, with [Durable Writes](../../../server/current/learn/data/durability.md) — although they remain essentially the same in use. The Python SDK exposes both of these forms of Durability.

First we will cover the newer durability features available in Couchbase server 6.5 onwards. The SDK exposes three durability levels:

* `Majority` \- The server will ensure that the change is available in memory on the majority of configured replicas.
* `MajorityAndPersistToActive` \- Majority level, plus persisted to disk on the active node.
* `PersistToMajority` \- Majority level, plus persisted to disk on the majority of configured replicas.

The options are in increasing levels of safety. Note that nothing comes for free - for a given node, waiting for writes to storage is considerably slower than waiting for it to be available in-memory. These trade offs, as well as which settings may be tuned, are discussed in the [durability page](../concept-docs/durability-replication-failure-considerations.md#durable-writes).

The following example demonstrates using the newer durability features available in Couchbase server 6.5 onwards.

```python
    # Upsert with Durability (Couchbase Server >= 6.5) level Majority
    document = dict(foo="bar", bar="foo")
    opts = UpsertOptions(durability=ServerDurability(Durability.MAJORITY))
    result = collection.upsert("document-key", document, opts)
```

If a version of Couchbase Server lower than 6.5 is being used then the application can fall-back to ['client verified' durability](../concept-docs/durability-replication-failure-considerations.md#older-server-versions). The older type of durability, also known as _observe based durability_, works by monitoring the server to ensure that the change has been replicated or persisted to the required number of nodes within the timeout specified on the operation. Here we can see how that is set:

```python
    # Upsert with observe based durability (Couchbase Server < 6.5)
    document = {"foo": "bar", "bar": "foo"}
    opts = UpsertOptions(
        durability=ClientDurability(
            ReplicateTo.ONE,
            PersistTo.ONE))
    result = collection.upsert("document-key", document, opts)
```

To stress, durability is a useful feature but should not be the default for most applications, as there is a performance consideration, and the default level of safety provided by Couchbase will be reasonable for the majority of situations.

> [!TIP]
> Sub-Document Operations
> 
> All of these operations involve fetching the complete document from the Cluster. Where the number of operations or other circumstances make bandwidth a significant issue, the SDK can work on just a specific _path_ of the document with [Sub-Document Operations](subdocument-operations.md).

## [](#preferred-server-group-replica-reads)Preferred Server Group Replica Reads

> [!IMPORTANT]
> Preferred Server Group Replica Reads are only accessible with the Python SDK working with Couchbase Server 7.6.2 or newer (Capella or self-managed), from SDK version 4.4.0\.

[Server Groups](../../../server/current/learn/clusters-and-availability/groups.md#understanding-server-group-awareness)can be used to define subsets of nodes within a Couchbase cluster, which contain a complete set of vbuckets (active or replica). As well as high availability use cases, Servre Groups can also be used to keep much traffic within the same cloud Availability Zone.

For Capella users with high data volumes, egress charges for reads from other Availability Zones (AZ) in AWS can be a significant cost. The Python SDK, when making read replica requests, can make a request to a preferred Server Group — in this case the local AZ — and set to always read from a copy of the document in this local zone. This is done by putting cluster nodes in the same AZ into the same [Server Group](../../../server/current/learn/clusters-and-availability/groups.md#server-groups-and-vbuckets), too.

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

```python
result = collection.get("document-key")
print(result.content_as[dict])
```

_Timeout_ can also be set, as in the earlier `Insert` operation example:

```python
opts = GetOptions(timeout=timedelta(seconds=5))
result = collection.get("document-key", opts)
print(result.content_as[dict])
```

## [](#removing)Removing

When removing a document, you will have the same concern for durability as with any additive modification to the Bucket:

Remove (with options)

```python
# remove document with options
result = collection.remove(
    "document-key",
    RemoveOptions(
        cas=12345,
        durability=ServerDurability(
            Durability.MAJORITY)))
```

## [](#expiration-ttl)Expiration / TTL

We already touched on how to set `Expiry` on an operation but we didn’t discuss how to handle extending that expiry time. By default, Couchbase documents do not expire, but transient or temporary data may be needed for user sessions, caches, or other temporary documents. You can use expiration values on documents to handle transient data. To prevent a document that already has expiry from expiring you can use `Touch` operations which will extend the expiry by the time specified.

```python
result = collection.touch("document-key", timedelta(seconds=10))
```

When getting a document, the expiry is not provided automatically by Couchbase Server but it can be requested:

```python
result = collection.get("document-key", GetOptions(with_expiry=True))
print("Expiry of result: {}".format(result.expiryTime))
```

Some applications may find `get_and_touch` useful, which fetches a document while updating its expiry field. It can be used like this:

```python
result = collection.get_and_touch("document-key", timedelta(seconds=10))
```

## [](#atomic-counters)Atomic Counters

The value of a document can be increased or decreased atomically using `.increment()` and `.decrement()`.

> [!NOTE]
> Increment & Decrement are considered part of the ‘binary’ API, and as such may still be subject to change.

Increment

```python
# Increment binary value by 1
collection.binary().increment(
    "counter-key",
    IncrementOptions(
        delta=DeltaValue(1)))
```

Increment (with seed)

```python
# Increment binary value by 5, if key doesn't exist, seed it at 1000
collection.binary().increment(
    "counter-key",
    IncrementOptions(
        delta=DeltaValue(5),
        initial=SignedInt64(1000)))
```

Decrement

```python
# Decrement binary value by 1
collection.binary().decrement(
    "counter-key",
    DecrementOptions(
        delta=DeltaValue(1)))
```

Decrement (with seed)

```python
# Decrement binary value by 2, if key doesn't exist, seed it at 1000
collection.binary().decrement(
    "counter-key",
    DecrementOptions(
        delta=DeltaValue(2),
        initial=SignedInt64(1000)))
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

```python
from couchbase.kv_range_scan import RangeScan
result = collection.scan(RangeScan()) (1)
for r in result:
    print(f'Found result, ID={r.id}, content={r.content_as[dict]}')
```

| **1** | The RangeScan class has two optional parameters: start and end. If you omit them like in this example, you’ll get all documents in the collection. These parameters are for advanced use cases; you probably won’t need to specify them. Instead, it’s more common to use the "prefix" scan type shown in the next example. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#kv-range-scan-prefix)Prefix scan

KV range scan can also give you all documents whose IDs start with the same prefix. Imagine you have a collection where documents are named like this: `<username>::<uuid>`. In other words, the document ID starts with the name of the user associated with the document, followed by a delimiter, and then a UUID. If you use this document naming scheme, you can use a prefix range scan to get all documents associated with a user. For example, to get all documents associated with user "alice", you would write:

KV Range Scan for all documents in a collection whose IDs start with `alice::`

```python
from couchbase.kv_range_scan import PrefixScan
result = collection.scan(PrefixScan('alice::'))
for r in result:
    print(f'Found result, ID={r.id}, content={r.content_as[dict]}')

from couchbase.kv_range_scan import SamplingScan
result = collection.scan(SamplingScan(100))
for r in result:
    print(f'Found result, ID={r.id}, content={r.content_as[dict]}')
```

### [](#kv-range-scan-sample)Sample scan

If you want to get random documents from a collection, use a sample scan.

KV Range Scan for 100 random documents

```python
from couchbase.kv_range_scan import SamplingScan
result = collection.scan(SamplingScan(100))
for r in result:
    print(f'Found result, ID={r.id}, content={r.content_as[dict]}')
```

### [](#kv-range-scan-only-ids)Get IDs instead of full documents

If you only want the document IDs, set the `ids_only` field of `ScanOptions` to `true`, like this:

KV Range Scan for all document IDs in a collection

```python
from couchbase.options import ScanOptions
# ids_only via ScanOptions
result = collection.scan(RangeScan(), ScanOptions(ids_only=True))
# NOTE: An InvalidArgumentException is raised if content_as is 
# accessed when ids_only=True is used
for r in result:
    print(f'Found result, ID={r.id}')

# ids_only via kwargs
result = collection.scan(RangeScan(), ids_only=True)
for r in result:
    print(f'Found result, ID={r.id}')
```

## [](#scoped-kv-operations)Scoped KV Operations

It is possible to perform scoped key-value operations on named [Collections](../../../server/current/learn/data/scopes-and-collections.md) _with Couchbase Server release 7.0_. See the [API docs](https://docs.couchbase.com/sdk-api/couchbase-python-client/api/couchbase.html#collection-object) for more information.

Here is an example showing an upsert in the `users` collection, which lives in the `travel-sample.tenant_agent_00` keyspace:

```python
agent_scope = bucket.scope("tenant_agent_00");
users_collection = agent_scope.collection("users");

content = {"name": "John Doe", "preferred_email": "johndoe111@test123.test" }

result = users_collection.upsert("user-key", content);
```

## [](#additional-resources)Additional Resources

A [complete Caching example](https://github.com/couchbase/docs-sdk-python/blob/release/3.1/modules/howtos/examples/caching%5Fflask.py) for the Python 3.x SDK, using Flask, is [worked through here](caching-example.md).

Working on just a specific path within a JSON document will reduce network bandwidth requirements - see the [Sub-Document](subdocument-operations.md) pages.

For another way of increasing performance, reference our [asynchronous programmaing options](concurrent-async-apis.md).

Our [Query Engine](n1ql-queries-with-sdk.md) enables retrieval of information using the SQL-like syntax of SQL++ (formerly N1QL).