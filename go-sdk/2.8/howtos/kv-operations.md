---
title: Data Operations
description: Key Value (KV) or data service offers the simplest way to retrieve
  or mutate data where the key is known.
editUrl: https://github.com/couchbase/docs-sdk-go/edit/temp/2.8/modules/howtos/pages/kv-operations.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.8@go-sdk:howtos:kv-operations.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/go-sdk/2.8/howtos/kv-operations.html)

# Data Operations

> Key Value (KV) or data service offers the simplest way to retrieve or mutate data where the key is known. Here we cover CRUD operations, document expiration, and optimistic locking with CAS. 

The complete code sample used on this page can be downloaded from [here](https://github.com/couchbase/docs-sdk-go/blob/release/2.6/modules/devguide/examples/go/kv-crud.go) — from which you can see in context how to authenticate and connect to a Couchbase Cluster, then perform these Collection operations.

## [](#documents)Documents

A _document_ refers to an entry in the database (other databases may refer to the same concept as a _row_). A document has an ID (_primary key_ in other databases), which is unique to the document and by which it can be located. The document also has a value which contains the actual application data. See [the concept guide to _Documents_](../concept-docs/documents.md) for a deeper dive into documents in the Couchbase Data Platform. Or read on, for a hands-on introduction to working with documents from the Go SDK.

## [](#crud-operations)CRUD Operations

The core interface to Couchbase Server is simple KV operations on full documents. Make sure you're familiar with the basics of authorization and connecting to a Cluster from the [Start Using the SDK section](../hello-world/start-using-sdk.md). We're going to expand on the short _Upsert_ example we used there, adding options as we move through the various CRUD operations. Here is the _Insert_ operation at its simplest:

```go
	// Insert Document
	type myDoc struct {
		Foo string `json:"foo"`
		Bar string `json:"bar"`
	}
	document := myDoc{Foo: "bar", Bar: "foo"}
	result, err := collection.Insert("document-key", &document, nil)
	if err != nil {
		panic(err)
	}
```

Options like timeout may also be added to operations. _Timeout_ in the Go SDK has a type value of `time.Duration`. Timeout sets the timeout value for the underlying network connection.

```go
	// Insert Document with options
	resultwithOptions, err := collection.Insert("document-key-options", &document, &gocb.InsertOptions{
		Timeout: 3 * time.Second,
	})
	if err != nil {
		panic(err)
	}
```

### [](#cas)CAS

Setting a Compare and Swap (CAS) value is a form of optimistic locking - dealt with in depth in the [CAS page](concurrent-document-mutations.md). Here we just note that the CAS is a value representing the current state of an item; each time the item is modified, its CAS changes. The CAS value is returned as part of a document's metadata whenever a document is accessed. Without explicitly setting it, a newly-created document would have a CAS value of _0_.

```go
	// Replace Document with Cas
	replaceResultWithCas, err := collection.Replace("document-key", &document, &gocb.ReplaceOptions{
		Cas: 12345,
	})
	if err != nil {
		// We expect this to error
		fmt.Println(err)
	}
```

Typically we would want to use CAS for something more meaningful like performing a Get, modifying the result and updating the document. By using the CAS value we know that if anyone else modified this document and updated it before our update then ours will error.

```go
	// Get and Replace Document with Cas
	updateGetResult, err := collection.Get("document-key", nil)
	if err != nil {
		panic(err)
	}

	var doc myDoc
	err = updateGetResult.Content(&doc)
	if err != nil {
		panic(err)
	}

	doc.Bar = "moo"

	updateResult, err := collection.Replace("document-key", doc, &gocb.ReplaceOptions{
		Cas: updateGetResult.Cas(),
	})
```

Expiry sets an explicit time to live (TTL) for a document in seconds. For a discussion of item (Document) _vs_ Bucket expiration, see the [Expiration Overview page](#7.1@server:learn:buckets-memory-and-storage/expiration.adoc#expiration-bucket-versus-item).

```go
	// Upsert with Expiry
	expiryResult, err := collection.Upsert(key, &document, &gocb.UpsertOptions{
		Timeout: 100 * time.Millisecond,
		Expiry:  60 * time.Second,
	})
```

## [](#durability)Durability

Writes in Couchbase are written to a single node, and from there the Couchbase Server will take care of sending that mutation to any configured replicas. The optional durability parameter, which all mutating operations accept, allows the application to wait until this replication (or persistence) is successful before proceeding.

In Couchbase Server releases before 6.5, Durability was set with two options — see the [6.0 Durability documentation](#1.6@go-sdk::durability.adoc) — covering how many replicas the operation must be propagated to and how many persisted copies of the modified record must exist. Couchbase Data Platform 6.5 refines these two options, with [Durable Writes](#7.1@server:learn:data/durability.adoc) — although they remain essentially the same in use. The Go SDK exposes both of these forms of Durability.

First we will cover the newer durability features available in Couchbase server 6.5 onwards. The SDK exposes three durability levels:

// DurabilityLevelMajority specifies that a mutation must be replicated (held in memory) to a majority of nodes.
DurabilityLevelMajority = DurabilityLevel(1)

// DurabilityLevelMajorityAndPersistToActive specifies that a mutation must be replicated (held in memory) to a
// majority of nodes and also persisted (written to disk) on the active node.
DurabilityLevelMajorityAndPersistToActive = DurabilityLevel(2)

// DurabilityLevelPersistToMajority specifies that a mutation must be persisted (written to disk) to a majority
// of nodes.
DurabilityLevelPersistToMajority = DurabilityLevel(3)

The options are in increasing levels of safety. Note that nothing comes for free - for a given node, waiting for writes to storage is considerably slower than waiting for it to be available in-memory. These trade offs, as well as which settings may be tuned, are discussed in the [durability page](../concept-docs/durability-replication-failure-considerations.md#durable-writes).

Below we can see how to set this on an operation:

```go
	// Upsert with Durability level Majority
	durableResult, err := collection.Upsert("document-key", &document, &gocb.UpsertOptions{
		DurabilityLevel: gocb.DurabilityLevelMajority,
	})
```

If a version of Couchbase Server lower than 6.5 is being used then the application can fall-back to ['client verified' durability](../concept-docs/durability-replication-failure-considerations.md#older-server-versions). The older type of durability, also known as _observe based durability_, works by monitoring the server to ensure that the change has been replicated or persisted to the required number of nodes within the timeout specified on the operation. Here we can see how that is set:

```go
	key = "replicateToAndPersistTo"
	val = "Durabilty ReplicateTo and PersistTo Test Value"
	_, err = collection.Upsert(key, &val, &gocb.UpsertOptions{
		PersistTo:   1,
		ReplicateTo: 1,
	})
	if err != nil {
		panic(err)
	}
```

To stress, durability is a useful feature but should not be the default for most applications, as there is a performance consideration, and the default level of safety provided by Couchbase will be reasonable for the majority of situations.

> [!TIP]
> Sub-Document Operations
> 
> All of these operations involve fetching the complete document from the Cluster. Where the number of operations or other circumstances make bandwidth a significant issue, the SDK can work on just a specific _path_ of the document with [Sub-Document Operations](subdocument-operations.md).

## [](#retrieving-full-documents)Retrieving full documents

Using the `Get()` method with the document key can be done in a similar fashion to the other operations:

```go
	// Get
	getResult, err := collection.Get("document-key", nil)
	if err != nil {
		panic(err)
	}

	var getDoc myDoc
	err = getResult.Content(&getDoc)
	if err != nil {
		panic(err)
	}
	fmt.Println(getDoc)
```

Timeout can also be set, as in the earlier `Insert` example:

```go
	// Get with timeout
	getTimeoutResult, err := collection.Get("document-key", &gocb.GetOptions{
		Timeout: 10 * time.Millisecond,
	})
	if err != nil {
		panic(err)
	}

	var getTimeoutDoc myDoc
	err = getTimeoutResult.Content(&getTimeoutDoc)
	if err != nil {
		panic(err)
	}
	fmt.Println(getTimeoutDoc)
```

## [](#removing)Removing

When removing a document, you will have the same concern for durability as with any additive modification to the Bucket:

```go
	// Remove with Durability
	removeResult, err := collection.Remove("document-key", &gocb.RemoveOptions{
		Timeout:         100 * time.Millisecond,
		DurabilityLevel: gocb.DurabilityLevelMajority,
	})
	if err != nil {
		panic(err)
	}
```

## [](#expiration-ttl)Expiration / TTL

We already touched on how to set `Expiry` on an operation but we didn't discuss how to handle extending that expiry time. By default, Couchbase documents do not expire, but transient or temporary data may be needed for user sessions, caches, or other temporary documents. You can use expiration values on documents to handle transient data. To prevent a document that already has expiry from expiring you can use `Touch` operations which will extend the expiry by the time specified.

```go
	// Touch
	touchResult, err := collection.Touch(key, 60*time.Second, &gocb.TouchOptions{
		Timeout: 100 * time.Millisecond,
	})
	if err != nil {
		panic(err)
	}
```

If you want to get the document at the same time as extending expiry then you can use `GetAndTouch`.

```go
	// GetAndTouch
	getAndTouchResult, err := collection.GetAndTouch(key, 60, &gocb.GetAndTouchOptions{
		Timeout: 100 * time.Millisecond,
	})
	if err != nil {
		panic(err)
	}

	var getAndTouchDoc myDoc
	err = getAndTouchResult.Content(&getAndTouchDoc)
	if err != nil {
		panic(err)
	}

	fmt.Println(getAndTouchDoc)
```

## [](#atomic-counters)Atomic Counters

The value of a document can be increased or decreased atomically using `Binary().Increment()` and `Binary().Decrement()`.

> [!NOTE]
> Increment & Decrement are considered part of the 'binary' API and as such may still be subject to change.

Increment

```go
	binaryC := collection.Binary()
	key := "goDevguideExampleCounter"
	curKeyValue, err := binaryC.Increment(key, &gocb.IncrementOptions{
		Initial: 10,
		Delta:   2,
	})
	if err != nil {
		panic(err)
	}
```

Decrement

```go
	// Issue same operation, increment value by 2, to 12
	curKeyValue, err = binaryC.Decrement(key, &gocb.DecrementOptions{
		Initial: 10,
		Delta:   4,
	})
	if err != nil {
		panic(err)
	}
```

> [!TIP]
> Setting the document expiry time only works when a document is created, and it is not possible to update the expiry time of an existing counter document with the Increment method — to do this during an increment, use with the `Touch()` method.

### [](#atomicity-across-data-centers)Atomicity Across Data Centers

If you are using [Cross Data Center Replication](#7.1@server:manage:manage-xdcr/xdcr-management-overview.adoc) (XDCR), be sure to avoid modifying the same counter in more than one datacenter. If the same counter is modified in multiple datacenters between replications, the counter will no longer be atomic, and its value can change in unspecified ways.

A counter must be incremented or decremented by only a single datacenter. Each datacenter must have its own set of counters that it uses — a possible implementation would be including a datacenter name in the counter document ID.

## [](#kv-range-scan)KV Range Scan

A range scan gives you documents from a collection, even if you don't know the document IDs. This feature requires Couchbase Server 7.6 or newer.

> [!TIP]
> KV range scan is suitable for use cases that require relatively low concurrency and tolerate relatively high latency. If your application does many scans at once, or requires low latency results, we recommend using SQL++ (with a primary index on the collection) instead of KV range scan.

### [](#kv-range-scan-range)Range scan

Here's an example of a KV range scan that gets all documents in a collection:

KV Range Scan for all documents in a collection

```go
results, err := collection.Scan(gocb.RangeScan{}, nil) (1)
if err != nil {
	panic(err)
}
for {
	item := results.Next()
	if item == nil {
		break
	}
	var content interface{}
	err = item.Content(&content)
	if err != nil {
		panic(err)
	}
	fmt.Printf("ID = %s, \tContent = %s\n", item.ID(), content)
}
// Always check for errors after iterating
err = results.Err()
if err != nil {
	panic(err)
}
```

| **1** | The RangeScan struct has two optional fields: From and To. If you omit them like in this example, you'll get all documents in the collection. These parameters are for advanced use cases; you probably won't need to specify them. Instead, it's more common to use the "prefix" scan type shown in the next example. |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#kv-range-scan-prefix)Prefix scan

KV range scan can also give you all documents whose IDs start with the same prefix. Imagine you have a collection where documents are named like this: `<username>::<uuid>`. In other words, the document ID starts with the name of the user associated with the document, followed by a delimiter, and then a UUID. If you use this document naming scheme, you can use a prefix range scan to get all documents associated with a user. For example, to get all documents associated with user "alice", you would write:

KV Range Scan for all documents in a collection whose IDs start with `alice::`

```go
results, err := collection.Scan(gocb.NewRangeScanForPrefix("alice::"), nil) (1)
if err != nil {
	panic(err)
}
for {
	item := results.Next()
	if item == nil {
		break
	}
	var content interface{}
	err = item.Content(&content)
	if err != nil {
		panic(err)
	}
	fmt.Printf("ID = %s, \tContent = %s\n", item.ID(), content)
}
// Always check for errors after iterating
err = results.Err()
if err != nil {
	panic(err)
}
```

| **1** | Note the use of the NewRangeScanForPrefix helper function which gives a RangeScan scan type configured to return all documents with the given prefix. |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#kv-range-scan-sample)Sample scan

If you want to get random documents from a collection, use a sample scan.

KV Range Scan for 100 random documents

```go
results, err := collection.Scan(gocb.SamplingScan{Limit: 100}, nil)
if err != nil {
	panic(err)
}
for {
	item := results.Next()
	if item == nil {
		break
	}
	var content interface{}
	err = item.Content(&content)
	if err != nil {
		panic(err)
	}
	fmt.Printf("ID = %s, \tContent = %s\n", item.ID(), content)
}
// Always check for errors after iterating
err = results.Err()
if err != nil {
	panic(err)
}
```

### [](#kv-range-scan-only-ids)Get IDs instead of full documents

If you only want the document IDs, set the `IDsOnly` field of `ScanOptions` to `true`, like this:

KV Range Scan for all document IDs in a collection

```go
results, err := collection.Scan(gocb.RangeScan{}, &gocb.ScanOptions{IDsOnly: true})
if err != nil {
	panic(err)
}
for {
	item := results.Next()
	if item == nil {
		break
	}
	fmt.Printf("ID = %s\n", item.ID())
}
// Always check for errors after iterating
err = results.Err()
if err != nil {
	panic(err)
}
```

## [](#scoped-kv-operations)Scoped KV Operations

It is possible to perform scoped key-value operations on named [Collections](#7.1@server:learn:data/scopes-and-collections.adoc) _with Couchbase Server release 7.0_ onwards. See the [API docs](https://pkg.go.dev/github.com/couchbase/gocb/v2#Collection) for more information.

Here is an example showing an upsert in the `users` collection, which lives in the `travel-sample.tenant_agent_00` keyspace:

```go
agentScope := bucket.Scope("tenant_agent_00")
usersCollection := agentScope.Collection("users")

type userDoc struct {
	Name           string `json:"name"`
	PreferredEmail string `json:"preferred_email"`
}
document := userDoc{Name: "John Doe", PreferredEmail: "johndoe111@test123.test"}

result, err := usersCollection.Upsert("user-key", &document, &gocb.UpsertOptions{})
if err != nil {
	panic(err)
}
```

## [](#additional-resources)Additional Resources

Working on just a specific path within a JSON document will reduce network bandwidth requirements - see the [Sub-Document](subdocument-operations.md) pages.

Another way of increasing network performance is to _pipeline_ operations with [Bulk Operations API](concurrent-async-apis.md#bulk-operations-api).

As well as various [Formats](../concept-docs/data-model.md) of JSON, Couchbase can work directly with [arbitary bytes, or binary format](../concept-docs/nonjson.md).

Our [Query Engine](n1ql-queries-with-sdk.md) enables retrieval of information using the SQL-like syntax of [SQL++ (formerly N1QL)](https://www.couchbase.com/products/n1ql).