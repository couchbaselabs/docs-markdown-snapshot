---
title: Data Operations
description: Data service offers the simplest way to retrieve or mutate data
  where the key is known. Here we cover CRUD operations, document expiration,
  and optimistic locking with CAS.
editUrl: https://github.com/couchbase/docs-sdk-scala/edit/release/3.10/modules/howtos/pages/kv-operations.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:3.10@scala-sdk:howtos:kv-operations.adoc[]
---

[View original HTML](/scala-sdk/3.10/howtos/kv-operations.html)

# Data Operations

> Data service offers the simplest way to retrieve or mutate data where the key is known. Here we cover CRUD operations, document expiration, and optimistic locking with CAS. Here we cover CRUD operations, document expiration, and optimistic locking with CAS. 

At its heart Couchbase Server is a high-performance key-value store, and the key-value interface outlined below is the fastest and best method to perform operations involving single documents.

A _document_ refers to an entry in the database (other databases may refer to the same concept as a _row_). A document has an ID (_primary key_ in other databases), which is unique to the document and by which it can be located. The document also has a value which contains the actual application data. See [the concept guide to _Documents_](../concept-docs/documents.md) for a deeper dive into documents in the Couchbase Data Platform.

Before proceeding, make sure you’re familiar with the basics of authorization and connecting to a Cluster from the [Start Using the SDK](../hello-world/start-using-sdk.md) section.

The code samples below will use these imports:

```scala
import com.couchbase.client.core.error._
import com.couchbase.client.scala._
import com.couchbase.client.scala.durability._
import com.couchbase.client.scala.implicits.Codec
import com.couchbase.client.scala.json._
import com.couchbase.client.scala.kv.{GetOptions, InsertOptions, MutationResult, ReplaceOptions}

import scala.concurrent.duration._
import scala.util.{Failure, Success, Try}
```

> [!TIP]
> The Query Service can also be used to perform many single-document operations, but we very strongly recommend using the key-value API for this instead. It can be much more efficient as the request can go directly to the correct node, there’s no query parsing overhead, and it’s over the highly optimized memcached binary protocol.

## [](#json)JSON

The Couchbase Server is a key-value store that’s agnostic to what’s stored, but it’s very common to store JSON so most of the examples below will focus on that use-case.

The Scala SDK provides you with several options for working with JSON. They are described in more detail in [this guide](json.md), and the information below is just a summary of that.

The SDK directly supports several popular JSON libraries: [uPickle/uJson](https://github.com/lihaoyi/upickle), [Circe](https://circe.github.io/circe/), [Play Json](https://github.com/playframework/play-json), [Jawn](https://github.com/typelevel/jawn), and [Json4s](https://github.com/json4s/json4s).

In addition you can supply and receive JSON as a `String` or `Array[Byte]`, opening the door to any JSON library; [Jsoniter](https://jsoniter.com/) and [Jackson](https://github.com/FasterXML/jackson) have been tested, but any should work.

You can also directly encode and decode Scala case classes to and from the SDK.

To make things easy and to help get you started, the Scala SDK also bundles a home-grown small JSON library, which you are free to use instead of or alongside any of the other supported JSON libraries. The philosophy behind this library is to provide a very easy-to-use API and the fastest JSON implementation possible.

> [!NOTE]
> The Scala 3 version of the SDK removes direct support for external JSON libraries and direct handling of case classes, though it remains easy to integrate both. Please see [Migrating to Scala 3](../project-docs/migrating-to-scala-3.md) for guidance on these and other changes.

### [](#using-jsonobject-and-jsonarray)Using JsonObject and JsonArray

Using the built-in JSON library here’s how to create some simple JSON:

```scala
val json = JsonObject(
  "name" -> "Eric Wimp",
  "age" -> 9,
  "addresses" -> JsonArray(JsonObject("address" -> "29 Acacia Road"))
)

val str = json.toString()
// """{"name":"Eric Wimp","age":9,"addresses":[{"address","29 Acacia Road"}]}"""
```

`JsonObject` and `JsonArray` are both mutable, so they can also be created this way:

```scala
val obj = JsonObject.create.put("name", "Eric Wimp")
obj.put("age", 9)
val arr = JsonArray.create
arr.add(JsonObject("address" -> "29 Acacia Road"))
obj.put("addresses", arr)
```

It’s easy to retrieve data:

```scala
json.str("name") // "Eric Wimp"
json.arr("addresses").obj(0).str("address") // "29 Acacia Road"
```

Or, using a feature of Scala called `Dynamic`, you can use an alternative syntax like this:

```scala
json.dyn.name.str // "Eric Wimp"
json.dyn.addresses(0).address.str // "29 Acacia Road"
```

The majority of the Scala SDK will not throw exceptions. Methods on `JsonObject` are one of the few cases where they are thrown.

If you’d rather not deal with exceptions, `JsonObject` comes with a counterpart `JsonObjectSafe` that provides an alternative interface, in which all methods return Scala `Try` results rather than throwing:

```scala
val safe: JsonObjectSafe = json.safe

val r: Try[String] = safe.str("name")

r match {
  case Success(name) => println(s"Their name is $name")
  case Failure(err)  => println(s"Could not find field 'name': $err")
}
```

(Don’t worry if `Try` is unfamiliar, you’ll see plenty of examples of how to use it and combine it with other `Try` in the examples below.)

A `JsonArraySafe` counterpart for `JsonArray` also exists. Note that `JsonObjectSafe`, though presenting a more functional interface, is still mutable.

> [!NOTE]
> Using JsonObject and JsonArray is 100% optional. If you would rather use a purely functional JSON library, with immutable data, lenses, cursors and other functional goodies, then the Scala SDK includes full support for the excellent [Circe](https://circe.github.io/circe/), among other great JSON libraries.

## [](#upsert)Upsert

Here is a simple upsert operation, which will insert the document if it does not exist, or replace it if it does.

```scala
val json = JsonObject("foo" -> "bar", "baz" -> "qux")

collection.upsert("document-key", json) match {
  case Success(result)    => println("Document upsert successful")
  case Failure(exception) => println("Error: " + exception)
}
```

> [!NOTE]
> All the examples here use the Scala SDK’s simplest API, which blocks until the operation is performed. There’s also an asynchronous API that is based around Scala `Future`, and a reactive API. See [Choosing an API](concurrent-async-apis.md#choosing-an-api) for more details.

## [](#handling-single-errors)Handling Single Errors

A note on error handling: the Scala SDK will not throw exceptions.

Instead, methods that can error will return a Scala `Try` object, which can either be a `Success` containing the result, or a `Failure` containing a _Throwable_ exception.

Pattern matching can be used to handle a `Try`, as above.

Don’t worry about cluttering up your code with explicit error handling for every operation: Scala provides useful methods to chain multiple `Try` together, and we’ll go into these later.

> [!NOTE]
> We will use `println` to simply print any errors in these samples, but the application will of course want to perform better error handling.

## [](#insert)Insert

Insert works very similarly to upsert, but will fail if the document already exists:

```scala
val json = JsonObject("foo" -> "bar", "baz" -> "qux")

collection.insert("document-key2", json) match {
  case Success(result) => println("Document inserted successfully")
  case Failure(err: DocumentExistsException) =>
    println("The document already exists")
  case Failure(err) => println("Error: " + err)
}
```

Note that a `Try` lets us check for a particular sort of error. The case clauses are tried in order from the top: if it is not a `Success`, and not a `Failure` containing a `DocumentExistsException`, it will drop to the default `Failure(err)` case.

## [](#retrieving-documents)Retrieving Documents

We’ve tried upserting and inserting documents into Couchbase Server, let’s get them back:

```scala
collection.get("document-key") match {
  case Success(result) => println("Document fetched successfully")
  case Failure(err)    => println("Error getting document: " + err)
}
```

Of course if we’re getting a document we probably want to do something with the content:

```scala
// Create some initial JSON
val json = JsonObject("status" -> "awesome!")

// Insert it
collection.insert("document-key3", json) match {
  case Success(result) => println("Document inserted successfully")
  case Failure(err)    => println("Error: " + err)
}

// Get it back
collection.get("document-key3") match {
  case Success(result) =>
    // Convert the content to a JsonObjectSafe
    result.contentAs[JsonObjectSafe] match {
      case Success(json) =>
        // Pull out the JSON's status field, if it exists
        json.str("status") match {
          case Success(status) => println(s"Couchbase is $status")
          case _               => println("Field 'status' did not exist")
        }
      case Failure(err) => println("Error decoding result: " + err)
    }
  case Failure(err) => println("Error getting document: " + err)
}
```

Woah, this looks messy! Don’t worry, this is the ugliest possible way of handling multiple `Try` results and we’ll see ways of tidying this up very soon.

For now, let’s break down what’s going on here.

First, we create some JSON and insert it.

Then, we get the document.

If it’s successful, we convert the document’s content into a `JsonObjectSafe`.

We can use `contentAs` to return the document’s content in all sorts of ways: as a String, as an Array\[Byte\], as a `org.json4s.JValue` from the [json4s library](https://github.com/json4s/json4s)…​ it’s very flexible (see [the JSON docs](json.md) for details). Here, we’ve asked for it to be returned as a `JsonObjectSafe` \- a 'safe' interface to the `JsonObject` that doesn’t throw exceptions.

Finally, if the conversion to a `JsonObjectSafe` was successful, we try to get the "status" field (which returns a `Try` with `JsonObjectSafe`), and print it if we were successful.

## [](#handling-multiple-errors)Handling Multiple Errors

Nesting multiple `Try` in that way quickly gets very hard to parse. Luckily, Scala provides functional tools to easily combine `Try` and handle them in one place.

First there’s `flatMap`, which can be used to rewrite the previous example like this:

```scala
val r: Try[String] = collection
  .get("document-key3")
  .flatMap(_.contentAs[JsonObjectSafe])
  .flatMap(_.str("status"))

r match {
  case Success(status) => println(s"Couchbase is $status")
  case Failure(err)    => println("Error: " + err)
}
```

Here, if the `get` is successful then the `contentAs` is tried, and if that is successful then the `str` call is tried. The end result is a single `Try[String]` that will be `Success` if all three operations succeeded, or otherwise `Failure`.

Some may prefer a for-comprehension, which is simply syntactic sugar around the `flatMap` example:

```scala
val r: Try[String] = for {
  result <- collection.get("document-key3")
  json <- result.contentAs[JsonObjectSafe]
  status <- json.str("status")
} yield status

r match {
  case Success(status) => println(s"Couchbase is $status")
  case Failure(err)    => println("Error: " + err)
}
```

## [](#replace)Replace

A very common operation is to `get` a document, modify its contents, and `replace` it. Let’s use a for-comprehension:

```scala
val initial = JsonObject("status" -> "great")

val r: Try[MutationResult] = for {
  // Insert a document.  Don't care about the exact details of the result, just
  // whether it was successful, so store result in _
  _ <- collection.insert("document-key4", initial)

  // Get the document back
  doc <- collection.get("document-key4")

  // Extract the content as a JsonObjectSafe
  json <- doc.contentAs[JsonObjectSafe]

  // Modify the content (JsonObjectSafe is mutable)
  _ <- json.put("status", "awesome!")

  // Replace the document with the updated content, and the document's CAS value
  // (which we'll cover in a moment)
  result <- collection.replace("document-key4", json, cas = doc.cas)
} yield result

r match {
  case Success(result) => println("Document replaced successfully")
  case Failure(err: CasMismatchException) =>
    println(
      "Could not write as another agent has concurrently modified the document"
    )
  case Failure(err) => println("Error: " + err)
}
```

There’s a couple of things to cover with the `replace` line.

First, most of the methods in the Scala SDK take optional parameters that have sensible defaults. One of them, `cas`, is provided here. We’ll see more throughout this document.

### [](#optimistic-locking)What is CAS?

CAS, or Compare and Swap, is a form of optimistic locking. Every document in Couchbase has a CAS value, and it’s changed on every mutation. When you `get` a document you also get the document’s CAS, and then when it’s time to write the document, you send the same CAS back. If another agent has modified that document, the Couchbase Server can detect you’ve provided a now-outdated CAS, and return an error instead of mutating the document. This provides cheap, safe concurrency. See [this detailed description of CAS](concurrent-document-mutations.md) for further details.

In general, you’ll want to provide a CAS value whenever you `replace` a document, to prevent overwriting another agent’s mutations.

### [](#retrying-on-cas-failures)Retrying on CAS Failures

But if we get a CAS mismatch, we usually just want to retry the operation. Let’s see a more advanced `replace` example that shows one way to handle this:

```scala
val initial = JsonObject("status" -> "great")

// Insert some initial data
collection.insert("document-key5", initial) match {
  case Success(result) =>
    // This is the get-and-replace we want to do, as a lambda
    val op = () =>
      for {
        doc <- collection.get("document-key5")
        json <- doc.contentAs[JsonObjectSafe]
        _ <- json.put("status", "awesome!")
        result <- collection.replace("document-key5", json, cas = doc.cas)
      } yield result

    // Send our lambda to retryOnCASMismatch to take care of retrying it
    // For space reasons, error-handling of r is left out
    val r: Try[MutationResult] = retryOnCASMismatch(op)

  case Failure(err) => println("Error: " + err)
}

// Try the provided operation, retrying on CasMismatchException
def retryOnCASMismatch(
  op: () => Try[MutationResult]
): Try[MutationResult] = {
  // Perform the operation
  val result = op()

  result match {
    // Retry on any CasMismatchException errors
    case Failure(err: CasMismatchException) =>
      retryOnCASMismatch(op)

    // If Success or any other Failure, return it
    case _ => result
  }
}
```

## [](#removing)Removing

Removing a document is straightforward:

```scala
collection.remove("document-key") match {
  case Success(result) => println("Document removed successfully")
  case Failure(err: DocumentNotFoundException) =>
    println("The document does not exist")
  case Failure(err) => println("Error: " + err)
}
```

## [](#sub-document-operations)Sub-Document Operations

All of the operations seen so far involve fetching the complete document.

As an optimization the application may consider using the [Sub-Document API](subdocument-operations.md) to access or mutate specific parts of a document.

## [](#case-classes)Case Classes

So far we’ve used JSON directly with `JsonObject` and `JsonObjectSafe`, but it can be very useful to deal with Scala case classes instead.

See [this guide](json.md#case-classes) for details.

## [](#durability)Durability

Writes in Couchbase are written initially to a single active node, and from there the Couchbase Server will take care of sending that mutation to any configured replicas.

The optional `durability` parameter, which all mutating operations accept, allows the application to wait until this replication is successful before proceeding.

It can be used like this:

```scala
collection.remove("document-key2", durability = Durability.Majority) match {
  case Success(result) => println("Document removed successfully")
  // The mutation is available in-memory on at least a majority of replicas
  case Failure(err: DocumentNotFoundException) =>
    println("The document does not exist")
  case Failure(err) => println("Error: " + err)
}
```

The default is `Durability.Disabled`, in which the SDK will return as soon as Couchbase Server has the mutation available in-memory on the active node. This is the default for a reason: it’s the fastest mode, and the majority of the time is all the application needs.

However, we recognize that there are times when the application needs that extra certainty that especially vital mutations have been successfully replicated, and the other durability options provide the means to achieve this.

The options differ depend on what Couchbase Server version is in use. If 6.5 or above is being used, you can take advantage of the [Durable Write](../concept-docs/durability-replication-failure-considerations.md#durable-writes) feature, in which Couchbase Server will only return success to the SDK after the requested replication level has been achieved. The three replication levels are:

`Majority` \- The server will ensure that the change is available in memory on the majority of configured replicas.

`MajorityAndPersistToActive` \- Majority level, plus persisted to disk on the active node.

`PersistToMajority` \- Majority level, plus persisted to disk on the majority of configured replicas.

The options are in increasing levels of failure-resistance. Note that nothing comes for free - for a given node, waiting for writes to storage is considerably slower than waiting for it to be available in-memory. These trade offs, as well as which settings may be tuned, are discussed in the [durability page](../concept-docs/durability-replication-failure-considerations.md#durable-writes).

If a version of Couchbase Server lower than 6.5 is being used then the application can fall-back to ['client verified' durability](../concept-docs/durability-replication-failure-considerations.md#older-server-versions). Here the SDK will do a simple poll of the replicas and only return once the requested durability level is achieved. This can be achieved like this:

```scala
collection.remove(
  "document-key3",
  durability = Durability.ClientVerified(ReplicateTo.Two, PersistTo.None)
) match {
  case Success(result) => println("Document successfully removed")
  // The mutation is available in-memory on at least two replicas
  case Failure(err: DocumentNotFoundException) =>
    println("The document does not exist")
  case Failure(err) => println("Error: " + err)
}
```

To stress, durability is a useful feature but should not be the default for most applications, as there is a performance consideration, and the default level of safety provided by Couchbase will be reasonable for the majority of situations.

## [](#expirationttl)Expiration/TTL

Couchbase Server includes an option to have particular documents automatically expire after a set time. This can be useful for some use-cases, such as user sessions, caches, or other temporary documents.

You can set an expiration value when creating a document:

```scala
val json = JsonObject("foo" -> "bar", "baz" -> "qux")

collection.insert("document-key", json, InsertOptions().expiry(2.hours)) match {
  case Success(result) => println("Document with expiry inserted successfully")
  case Failure(err)    => println("Error: " + err)
}
```

When getting a document, the expiry is not provided automatically by Couchbase Server but it can be requested:

```scala
collection.get("document-key", GetOptions().withExpiry(true)) match {
  case Success(result) =>
    result.expiry match {
      case Some(expiry) => println(s"Got expiry: $expiry")
      case _            => println("Err: no expiration field")
    }

  case Failure(err) => println("Error getting document: " + err)
}
```

Note that when updating the document, special care must be taken to avoid resetting the expiry to zero. Here’s how:

```scala
val r: Try[MutationResult] = for {
  doc <- collection.get("document-key", GetOptions().withExpiry(true))
  expiry <- Try(doc.expiry.get)
  // ^^ doc.expiration is an Option, but we can't mix Try and
  // Option inside the same for-comprehension, so convert here
  json <- doc.contentAs[JsonObjectSafe]
  _ <- json.put("foo", "bar")
  result <- collection.replace("document-key", json, ReplaceOptions().expiry(expiry))
} yield result

r match {
  case Success(status) => println("Document with expiry replaced successfully")
  case Failure(err)    => println("Error: " + err)
}
```

Some applications may find `getAndTouch` useful, which fetches a document while updating its expiry field. It can be used like this:

```scala
collection.getAndTouch("document-key", expiry = 4.hours) match {
  case Success(result) => println("Document fetched and updated with expiry")
  case Failure(err)    => println("Error: " + err)
}
```

## [](#atomic-counter-operations)Atomic Counter Operations

To support counter use-cases, a Couchbase document can be treated as an integer counter and adjusted or created atomically like this:

```scala
// Increase a counter by 1, seeding it at an initial value of 1 if it does not exist
collection.binary.increment("document-key6", delta = 1, initial = Some(1)) match {
  case Success(result) =>
    println(s"Counter now: ${result.content}")
  case Failure(err) => println("Error: " + err)
}

// Decrease a counter by 1, seeding it at an initial value of 10 if it does not exist
collection.binary.decrement("document-key6", delta = 1, initial = Some(10)) match {
  case Success(result) =>
    println(s"Counter now: ${result.content}")
  case Failure(err) => println("Error: " + err)
}
```

Note that a counter cannot be below 0.

> [!NOTE]
> Increment & Decrement are considered part of the 'binary' API and as such may still be subject to change

> [!TIP]
> Setting the document expiry time only works when a document is created, and it is not possible to update the expiry time of an existing counter document with the Increment method — to do this during an increment, use with the `Touch()` method.

### [](#atomicity-across-data-centers)Atomicity Across Data Centers

If you are using [Cross Data Center Replication](../../../server/current/manage/manage-xdcr/xdcr-management-overview.md) (XDCR), be sure to avoid modifying the same counter in more than one datacenter. If the same counter is modified in multiple datacenters between replications, the counter will no longer be atomic, and its value can change in unspecified ways.

A counter must be incremented or decremented by only a single datacenter. Each datacenter must have its own set of counters that it uses — a possible implementation would be including a datacenter name in the counter document ID.

## [](#kv-range-scan)KV Range Scan

A range scan gives you documents from a collection, even if you don’t know the document IDs.

This feature requires Couchbase Server 7.6 or newer.

> [!TIP]
> KV range scan is suitable for use cases that require relatively low concurrency and tolerate relatively high latency. If your application does many scans at once, or requires low latency results, we recommend using SQL++ instead of KV range scan.

### [](#kv-range-scan-range)Range scan

Here’s an example of a KV range scan that gets all documents in a collection:

KV Range Scan for all documents in a collection

```scala
val results: Try[Iterator[ScanResult]] = collection.scan(ScanType.RangeScan(from = None, to = None))

results match {
  case Success(value) =>
    value.foreach(scanResult => println(scanResult))
  case Failure(exception) =>
    println(s"Scan operation failed with ${exception}")
}
```

### [](#kv-range-scan-prefix)Prefix scan

KV range scan can also give you all documents whose IDs start with the same prefix.

Imagine you have a collection where documents are named like this: `<username>::<uuid>`. In other words, the document ID starts with the name of the user associated with the document, followed by a delimiter, and then a UUID. If you use this document naming scheme, you can use a prefix range scan to get all documents associated with a user. For example, to get all documents associated with user "alice", you would write:

KV Range Scan for all documents in a collection whose IDs start with `alice::`

```scala
val results = collection.scan(ScanType.PrefixScan(prefix = "alice::"))
```

### [](#kv-range-scan-sample)Sample scan

If you want to get random documents from a collection, use a sample scan.

KV Range Scan for 100 random documents

```scala
val results = collection.scan(ScanType.SamplingScan(limit = 100))
```

### [](#kv-range-scan-only-ids)Get IDs instead of full document

To save network bandwidth it’s possible to retrieve only the document IDs from any scan.

KV Range Scan for all document IDs in a collection

```scala
val results: Try[Iterator[ScanResult]] = collection.scan(ScanType.RangeScan(from = None, to = None),
  ScanOptions().idsOnly(true))

results match {
  case Success(value) =>
    // Note only the id is present on each result - all other fields will be Option.None
    value.foreach(scanResult => println(scanResult.id))
  case Failure(exception) =>
    println(s"Scan operation failed with ${exception}")
}
```

| **1** | Note the call to scanIds() instead of scanDocuments(). The scanIds() methods also works with the other scan types described above. |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------- |

## [](#additional-resources)Additional Resources

Working on just a specific path within a JSON document will reduce network bandwidth requirements — see the [Sub-Document](subdocument-operations.md) pages.

As well as various [Formats](../concept-docs/data-model.md) of JSON, Couchbase can work directly with [arbitrary bytes, or binary format](../concept-docs/nonjson.md).

Our [Query Engine](sqlpp-queries-with-sdk.md) enables retrieval of information using the SQL-like syntax of SQL++ (formerly N1QL).