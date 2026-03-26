---
title: Data Operations
description: The Key Value (KV) service, sometimes called the "data service", is
  often the best way to get or change a document when you know its ID.
editUrl: https://github.com/couchbase/docs-sdk-kotlin/edit/temp/3.9/modules/howtos/pages/kv-operations.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.9@kotlin-sdk:howtos:kv-operations.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/kotlin-sdk/3.9/howtos/kv-operations.html)

# Data Operations

> The Key Value (KV) service, sometimes called the "data service", is often the best way to get or change a document when you know its ID. Here we cover CRUD operations and locking strategies. 

## [](#prerequisites)Before You Start

You should know [how to connect to a Couchbase cluster](connecting.md).

You should know about [documents and collections, and how to get a Couchbase Collection object](organizing-documents.md).

You should know [how to call a Kotlin suspending function](https://kotlinlang.org/docs/coroutines-basics.html).

## [](#basic-kv-ops)CRUD Operations

The KV service has [CRUD](https://en.wikipedia.org/wiki/CRUD) operations for working with whole documents. This table shows the Couchbase KV method for each CRUD operation.

| CRUD operation   | Couchbase KV method            |
| ---------------- | ------------------------------ |
| Create           | [Collection.insert](#insert)   |
| Read             | [Collection.get](#get)         |
| Update           | [Collection.replace](#replace) |
| Delete           | [Collection.remove](#remove)   |
| Create or Update | [Collection.upsert](#upsert)   |

### [](#insert)Insert (Create)

The `insert` method creates a new document in a collection.

This method has two required parameters:

* **`id: String`** \- The new document's ID.
* **`content: Any?`** \- The new document's value.

If the collection already has a document with the same ID, the `insert` method throws `DocumentExistsException`.

For example, let's pretend we're writing a program that helps a storyteller remember details about characters in a story.

To start, let's insert a document that represents a character in a story. The document ID is the character's name. The document content is some information about the character.

Creating a new document

```kotlin
try {
    collection.insert(
        id = "alice",
        content = mapOf("favoriteColor" to "blue"), (1)
    )
} catch (t: DocumentExistsException) {
    println("Insert failed because the document already exists.")
}
```

| **1** | The content doesn't have to be a Map. To learn more, please read [Working with JSON](json.md). |
| ----- | ---------------------------------------------------------------------------------------------- |

### [](#get)Get (Read)

The `get` method reads a document from a collection.

It has one required parameter:

* **`id: String`** \- The ID of the document to get.

If the collection does not have a document with this ID, the `get` method throws `DocumentNotFoundException`.

Reading a document

```kotlin
try {
    val result: GetResult = collection.get(id = "alice")
    val content = result.contentAs<Map<String, Any?>>()
    println("The character's favorite color is ${content["favoriteColor"]}")
} catch (t: DocumentNotFoundException) {
    println("Get failed because the document does not exist.")
}
```

### [](#replace)Replace (Update)

The `replace` method updates the value of an existing document.

This method has two required parameters:

* **`id: String`** \- The ID of the document to replace.
* **`content: Any?`** \- The document's new value.

If the collection does not have a document with this ID, the `replace` method throws `DocumentNotFoundException`.

Updating an existing document

```kotlin
try {
    collection.replace(
        id = "alice",
        content = mapOf("favoriteColor" to "red"),
    )
} catch (t: DocumentNotFoundException) {
    println("Replace failed because there was no document to replace.")
}
```

> [!CAUTION]
> When you replace a document, it's usually good to use [optimistic locking](#optimistic-locking). Otherwise, changes might get lost if two people change the same document at the same time.

### [](#remove)Remove (Delete)

The `remove` method deletes a document from a collection.

This method has one required parameter:

* **`id: String`** \- The ID of the document to remove.

If the collection does not have a document with this ID, the `remove` method throws `DocumentNotFoundException`.

Deleting a document

```kotlin
try {
    collection.remove(id = "alice")
} catch (t: DocumentNotFoundException) {
    println("Remove failed because there was no document to remove.")
}
```

### [](#upsert)Upsert (Create or Update)

The word "upsert" is a [portmanteau word](https://simple.wikipedia.org/wiki/Portmanteau%5Fword) that means "**up**date or in**sert**."

If the document already exists, the `upsert` method updates (replaces) it. If the document does not exist, the `upsert` method inserts it.

This method has two required parameters:

* **`id: String`** \- The ID of the document to create or update.
* **`content: Any?`** \- The document's new value.

Creating or updating a document

```kotlin
collection.upsert(
    id = "alice",
    content = mapOf("favoriteColor" to "blue"),
)
```

You can run this example many times. It should succeed each time, because the `upsert` method does not care if the document already exists.

## [](#bulk)Bulk Operations

The Couchbase Kotlin SDK does not have bulk operations. However, coroutines make it easy to do many things at the same time.

Here is an example `bulkGet` function you can add to your project. This function can get many documents at the same time.

Extension function `Collection.bulkGet`

```kotlin
/**
 * Gets many documents at the same time.
 *
 * @param ids The IDs of the documents to get.
 * @param maxConcurrency Limits how many operations happen
 * at the same time.
 * @return A map where the key is a document ID, and the value
 * is a [kotlin.Result] indicating success or failure.
 */
suspend fun com.couchbase.client.kotlin.Collection.bulkGet(
    ids: Iterable<String>,
    maxConcurrency: Int = 128,
): Map<String, Result<GetResult>> {
    val result = ConcurrentHashMap<String, Result<GetResult>>()
    val semaphore = kotlinx.coroutines.sync.Semaphore(maxConcurrency)

    coroutineScope { (1)
        ids.forEach { id ->
            launch { (2)
                semaphore.withPermit { (3)
                    result[id] = runCatching { get(id) }
                }
            }
        }
    }
    return result
}
```

| **1** | Starting a new coroutine scope ensures the bulkGet method does not return until all coroutines launched inside the scope finish.                                                                                                                                |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Start a new coroutine for each get operation, so all the gets happen at the same time.                                                                                                                                                                          |
| **3** | The semaphore prevents sending too many requests at once. You can change the function to take the semaphore as a parameter, and pass the same semaphore whenever calling the method. If you do that, the concurrency limit will be shared by all bulk requests. |

After adding the `Collection.bulkGet` extension function to your project, call it like this:

Calling the `Collection.bulkGet` extension function

```kotlin
val ids = listOf("airline_10", "airline_10123", "airline_10226")

collection.bulkGet(ids).forEach { (id, result) ->
    println("$id = $result")
}
```

> [!TIP]
> You can copy the `bulkGet` extension function and change it to do other operations, like upsert.

## [](#locking)Locking

> [!NOTE]
> What is an "atomic" operation?
> 
> An atomic operation succeeds completely or fails completely. When Couchbase Server works on an atomic operation, you never see the result of incomplete work. A failed atomic operation never changes a document.
> 
> If two or more atomic operations use the same document, Couchbase Server works on only one of the operations at a time.

A KV operation is atomic. However, a _sequence_ of KV operations is _not_ atomic.

You can use a locking strategy to make a sequence of KV operations on the same document succeed or fail together. This makes the sequence of operations behave like a single atomic operation.

The locking strategy can be optimistic or pessimistic.

### [](#optimistic-locking)Optimistic Locking

When you use optimistic locking, you assume nobody else will change a document while you work with it. If somebody else _does_ change the document, start again. Keep trying until you succeed or decide to give up.

How do you tell if the document changed? Every Couchbase document has a Compare-And-Swap (CAS) value. The CAS value is a number that changes every time the document changes.

Most KV operations that change documents have a `cas` parameter. If you set this parameter, the operation fails with `CasMismatchException` if the document's current CAS value does not match the `cas` parameter value.

Optimistic locking can make `get` and `replace` behave like an atomic unit:

1. Read a document using the `get` method. Remember the document's CAS value.
2. Use the old document content to make new content. For example, add or remove a field, or change a field value.
3. Replace the document content using the `replace` method. Pass the new content and the CAS value from step 1\. If `replace` throws `CasMismatchException`, start again at step 1.

If you pass a CAS value to `replace`, the operation succeeds only if nobody changed the document after you got the CAS value.

This example shows how to safely change a document, without losing changes made by somebody else at the same time:

```kotlin
while (true) { (1)
    val result: GetResult = collection.get(id = "alice")

    val oldContent = result.contentAs<Map<String, Any?>>()
    val newContent = oldContent + ("favoriteFood" to "hamburger")

    try {
        collection.replace(
            id = "alice",
            content = newContent,
            cas = result.cas
        )
        return

    } catch (t: CasMismatchException) {
        // Someone else changed the document after we read it!
        // Start again.
    }
}
```

| **1** | This example keeps trying until the coroutine is cancelled. Another choice would be to set a time limit, or limit the number of tries. |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------- |

> [!TIP]
> You don't need to write all of that code every time you want to use optimistic locking. Instead, you can define your own extension function like this:
> 
> ```kotlin
> suspend inline fun <reified T> Collection.mutate(
>     id: String,
>     expiry: Expiry = Expiry.none(),
>     preserveExpiry: Boolean = false,
>     transcoder: Transcoder? = null,
>     durability: Durability = Durability.none(),
>     common: CommonOptions = CommonOptions.Default,
>     transform: (GetResult) -> T,
> ): MutationResult {
>     while (true) {
>         val old = get(
>             id = id,
>             withExpiry = preserveExpiry,
>             common = common,
>         )
> 
>         val newContent = transform(old)
>         val newExpiry = if (preserveExpiry) old.expiry else expiry
> 
>         try {
>             return replace(
>                 id = id,
>                 content = newContent,
>                 common = common,
>                 transcoder = transcoder,
>                 durability = durability,
>                 expiry = newExpiry,
>                 cas = old.cas
>             )
>         } catch (_: CasMismatchException) {
>             // Someone else modified the document. Start again.
>         }
>     }
> }
> ```
> 
> Now the optimistic locking example from before looks like this:
> 
> ```kotlin
> collection.mutate("alice") { old: GetResult ->
>     val oldContent = old.contentAs<Map<String, Any?>>()
>     return@mutate oldContent + ("favoriteFood" to "hamburger")
> }
> ```

### [](#pessimistic-locking)Pessimistic Locking

Pessimistic locking stops anyone except you from changing a document.

When a document is locked, only people who know the CAS value from `getAndLock` can modify the document.

The lock is released when you change the document using the correct CAS, or when you call the `unlock` method.

Changing a document safely, using pessimistic locking

```kotlin
val result: GetResult = collection.getAndLock(
    id = "alice",
    lockTime = 15.seconds, (1)
)

val oldContent = result.contentAs<Map<String, Any?>>()
val newContent = oldContent + ("favoriteFood" to "hamburger")

collection.replace( (2)
    id = "alice",
    content = newContent,
    cas = result.cas,
)
```

| **1** | The lock is automatically released (unlocked) after this duration. The lock time can be as short as 1 second, or as long as 30 seconds. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | replace automatically releases the lock. Alternatively, you can release the lock by calling unlock.                                     |

Pessimistic locking is expensive. It's usually better to use optimistic locking.

## [](#selecting-fields)Selecting Fields

The `project()` feature allows you to select a couple of fields — specify a path or paths within the JSON document, and this list is fetched rather than the whole document.

```kotlin
	project​(Iterable<String> paths)
	project​(String path, String... morePaths)
```

This feature is implemented by internally using our subdocument API, which you can access directly — for more sophisticated selection of portions of a document — [subdocument-operations.adoc](#subdocument-operations.adoc).

## [](#preferred-server-group-replica-reads)Preferred Server Group Replica Reads

> [!IMPORTANT]
> Preferred Server Group Replica Reads are only accessible with the Kotlin SDK working with Couchbase Server 7.6.2 or newer (Capella or self-managed), from SDK version 1.4.8\.

[Server Groups](../../../server/current/learn/clusters-and-availability/groups.md#understanding-server-group-awareness)can be used to define subsets of nodes within a Couchbase cluster, which contain a complete set of vbuckets (active or replica). As well as high availability use cases, Servre Groups can also be used to keep much traffic within the same cloud Availability Zone.

For Capella users with high data volumes, egress charges for reads from other Availability Zones (AZ) in AWS can be a significant cost. The Kotlin SDK, when making read replica requests, can make a request to a preferred Server Group — in this case the local AZ — and set to always read from a copy of the document in this local zone. This is done by putting cluster nodes in the same AZ into the same [Server Group](../../../server/current/learn/clusters-and-availability/groups.md#server-groups-and-vbuckets), too.

This may mean the application has to be tolerant of slight inconsistencies, until the local replica catches up. Alternatively, it may demand a stronger level of durability, to ensure that all copies of a document are consistent before they are accessible — provided that this is `persistToMajority` with [no more than one replica](../../../server/current/learn/data/durability.md#majority).

Couchbase does not recommend this feature where read consistency is critical, but with the appropriate durability settings consistency can be favored ahead of availability.

> [!CAUTION]
> Replicas, Nodes, and Server Groups
> 
> Implicit in the rules for durability, and the process of setting up Server Groups, is the following information — which we mention here explicitly to ensure it is all noted:
> 
> * Moving servers between Server Groups updates the `clustermap` immediately, but to move the data, an administrator **must** perform rebalance. Until the rebalance is complete, the SDK will see and be able to 'use' the new server groups, but the `vBucketMap` may still refer to data in the previous locations.
> * The cluster should have enough nodes and group to make sure that copies of the same document are not stored on the same node, and each group has nodes that cover all 1024 vbuckets (in other words, the number of the groups does not exceeds number of the copies: `active+num_replicas`). The Admin UI should emit small yellow warning if the configuration is considered unbalanced.
> * Setting **three** replicas for the bucket [disables durability for sync writes](../../../server/current/learn/data/durability.md#majority), also precluding the use of [multi-document ACID transactions](#concept-docs:transactions.adoc).

## [](#kv-range-scan)KV Range Scan

A range scan gives you documents from a collection, even if you don't know the document IDs. This feature requires Couchbase Server 7.6 or newer.

> [!TIP]
> KV range scan is suitable for use cases that require relatively low concurrency and tolerate relatively high latency. If your application does many scans at once, or requires low latency results, we recommend using SQL++ (with a primary index on the collection) instead of KV range scan.

### [](#kv-range-scan-range)Range scan

Here's an example of a KV range scan that gets all documents in a collection:

KV Range Scan for all documents in a collection

```kotlin
val results: Flow<GetResult> = collection.scanDocuments(
    type = ScanType.range() (1)
)
results.collect { println(it) }
```

| **1** | The ScanType.range() method has two optional parameters: from and to. If you omit them like in this example, you'll get all documents in the collection. These parameters are for advanced use cases; you probably won't need to specify them. Instead, it's more common to use the "prefix" scan type shown in the next example. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#kv-range-scan-prefix)Prefix scan

KV range scan can also give you all documents whose IDs start with the same prefix.

Imagine you have a collection where documents are named like this: `<username>::<uuid>`. In other words, the document ID starts with the name of the user associated with the document, followed by a delimiter, and then a UUID. If you use this document naming scheme, you can use a prefix range scan to get all documents associated with a user.

For example, to get all documents associated with user "alice", you would write:

KV Range Scan for all documents in a collection whose IDs start with `alice::`

```kotlin
val results: Flow<GetResult> = collection.scanDocuments(
    type = ScanType.prefix("alice::") (1)
)
results.collect { println(it) }
```

| **1** | Note the scan type is **prefix**. |
| ----- | --------------------------------- |

### [](#kv-range-scan-sample)Sample scan

If you want to get random documents from a collection, use a sample scan.

KV Range Scan for 100 random documents

```kotlin
val results: Flow<GetResult> = collection.scanDocuments(
    type = ScanType.sample(limit = 100)
)
results.collect { println(it) }
```

### [](#kv-range-scan-only-ids)Get IDs instead of full document

If you only want the document IDs, call `scanIds()` instead of `scanDocuments()`, like this:

KV Range Scan for all document IDs in a collection

```kotlin
val ids: Flow<String> = collection.scanIds( (1)
    type = ScanType.range()
)
ids.collect { println(it) }
```

| **1** | Note the call to scanIds() instead of scanDocuments(). |
| ----- | ------------------------------------------------------ |

The `scanIds()` methods also works with the other scan types described above.

## [](#summary)Summary

The Couchbase Key Value (KV) service is the fastest way to work with single documents when you know the document ID.

The `insert`, `get`, `replace`, `remove`, and `upsert` methods of the `Collection` object do the standard [CRUD operations](#basic-kv-ops) on full documents.

When changing a document, use a [locking strategy](#locking) if the new content depends on the old content. [Optimistic locking](#optimistic-locking) usually performs better than [pessimistic locking](#pessimistic-locking).

You can do a KV range scan to get documents even if you don't know their IDs. However, it's faster to use SQL++ for this.