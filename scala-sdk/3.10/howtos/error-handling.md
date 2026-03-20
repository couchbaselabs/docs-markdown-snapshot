---
title: Handling Errors
description: Errors are inevitable. Scala offers several flexible approaches to
  handling them.
editUrl: https://github.com/couchbase/docs-sdk-scala/edit/release/3.10/modules/howtos/pages/error-handling.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:3.10@scala-sdk:howtos:error-handling.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/scala-sdk/3.10/howtos/error-handling.html)

# Handling Errors

> Errors are inevitable. Scala offers several flexible approaches to handling them. 

The developer’s job is to be prepared for whatever is likely to come up — and to try and be prepared for anything that conceivably could come up. Couchbase gives you a lot of flexibility, but it is recommended that you equip yourself with an understanding of the possibilities.

As covered [here](concurrent-async-apis.md), the Scala SDK ships with three different APIs, allowing you to structure your application the way you want. That guide also covers how errors are actually returned (e.g. via `Try`, `Future`, or `Mono`) and handled, so this document will focus instead on specific errors, along with a broader look at error handling strategies.

## [](#key-value-errors)Key-Value Errors

The KV Service exposes several common errors that can be encountered - both during development, and to be handled by the production app. Here we will cover some of the most common errors.

If a particular key cannot be found it is raised as an `DocumentNotFoundException`:

```scala
val json = JsonObject("foo" -> "bar", "baz" -> "qux")

collection.replace("does-not-exist", json) match {
  case Success(_) => println("Successful")
  case Failure(err: DocumentNotFoundException) => println("Key not found")
  case Failure(exception) => println("Error: " + exception)
}
```

```scala
collection.get("document-key") match {
  case Success(result) =>
  case Failure(err: DocumentNotFoundException) => println("Key not found")
  case Failure(err) => println("Error getting document: " + err)
}
```

On the other hand if the key already exists and should not (e.g. on an insert) then it is raised as a `DocumentExistsException`:

```scala
val json = JsonObject("foo" -> "bar", "baz" -> "qux")

collection.insert("does-already-exist", json) match {
  case Success(_) => println("Successful")
  case Failure(err: DocumentExistsException) => println("Key already exists")
  case Failure(exception) => println("Error: " + exception)
}
```

### [](#concurrency)Concurrency

Couchbase provides optimistic concurrency using CAS ([Compare and Swap](concurrent-document-mutations.md)). Each document gets a CAS value on the server, which is changed on each mutation. When you get a document you automatically receive its CAS value. When replacing the document, if you provide that CAS the server can check that the document has not been concurrently modified by another agent in-between. If it has, it returns `CasMismatchException`, and the most appropriate response is to simply retry it:

```scala
def doOperation(guard: Int = 3): Try[MutationResult] = {
  collection.get("doc")
    .flatMap(doc => collection.replace(doc.id, newJson, ReplaceOptions().cas(doc.cas))) match {

    case Success(value) => Success(value)

    case Failure(err: CasMismatchException) =>
      // Simply recursively retry until guard is hit
      if (guard != 0) doOperation(guard - 1)
      else Failure(err)

    case Failure(exception) => Failure(exception)
  }
}
```

### [](#ambiguity)Ambiguity

There are situations with any distributed system in which it is simply impossible to know for sure if the operation completed successfully or not. Take this as an example: your application requests that a new document be created on Couchbase Server. This completes, but, just before the server can notify the client that it was successful, a network switch dies and the application’s connection to the server is lost. The client will timeout waiting for a response and will raise a `TimeoutException`, but it’s ambiguous to the app whether the operation succeeded or not.

Another ambiguous error is `DurabilityAmbiguousException`, which can returned when performing a durable operation. This similarly indicates that the operation may or may not have succeeded — though when using durability you are guaranteed that the operation will either have been applied to all replicas, or none.

Given the inevitability of ambiguity, how is the application supposed to handle this?

It really needs to be considered case-by-case, but the general strategy is to become certain if the operation succeeded or not, and to retry it if required.

For instance, for inserts, they can simply be retried to see if they fail on `DocumentExistsException`, in which case the operation was successful:

```scala
def doInsert(docId: String, json: JsonObject, guard: Int = InitialGuard): Try[String] = {
  val result = collection.insert(docId, json, InsertOptions().durability(Durability.Majority))

  result match {

    case Success(value) => Success("ok!")

    case Failure(err: DocumentExistsException) =>
      // The logic here is that if we failed to insert on the first attempt then
      // it's a true error, otherwise we retried due to an ambiguous error, and
      // it's ok to continue as the operation was actually successful
      if (guard == InitialGuard) Failure(err)
      else Success("ok!")

    // For ambiguous errors on inserts, simply retry them
    case Failure(err: DurabilityAmbiguousException) =>
      if (guard != 0) doInsert(docId, json, guard - 1)
      else Failure(err)

    case Failure(err: TimeoutException) =>
      if (guard != 0) doInsert(docId, json, guard - 1)
      else Failure(err)

    case Failure(err) => Failure(err)
  }
}
```

That example is much closer to what an application will want to be doing. Let’s flesh it out further.

### [](#real-world-error-handling)Real-World Error Handling

The application can write wrappers so that it can easily do operations without having to duplicate the error handling each time. Something like this:

```scala
def doInsert(docId: String,
             json: JsonObject,
             guard: Int = InitialGuard,
             delay: Duration = Duration(10, TimeUnit.MILLISECONDS)): Try[String] = {
  val result = collection.insert(docId, json, InsertOptions().durability(Durability.Majority))

  result match {

    case Success(value) => Success("ok!")

    case Failure(err: DocumentExistsException) =>
      // The logic here is that if we failed to insert on the first attempt then
      // it's a true error, otherwise we retried due to an ambiguous error, and
      // it's ok to continue as the operation was actually successful
      if (guard == InitialGuard) Failure(err)
      else Success("ok!")

    // Ambiguous errors.  The operation may or may not have succeeded.  For inserts,
    // the insert can be retried, and a DocumentExistsException indicates it was
    // successful.
    case Failure(_: DurabilityAmbiguousException)
         | Failure(_: TimeoutException)

         // Temporary/transient errors that are likely to be resolved
         // on a retry
         | Failure(_: TemporaryFailureException)
         | Failure(_: DurableWriteInProgressException)
         | Failure(_: DurableWriteReCommitInProgressException)

         // These transient errors won't be returned on an insert, but can be used
         // when writing similar wrappers for other mutation operations
         | Failure(_: CasMismatchException) =>

      if (guard != 0) {
        // Retry the operation after a sleep (which increases on each failure),
        // to avoid potentially further overloading an already failing server.
        Thread.sleep(delay.toMillis)
        doInsert(docId, json, guard - 1, delay * 2)
      }
      // Replace this CouchbaseException with your own
      else Failure(new CouchbaseException("Failed to insert " + docId))

    // Other errors, propagate up
    case Failure(err) => Failure(err)
  }
}
```

This will make a 'best effort' to do the insert (though its retry strategy is rather naïve, and applications may want to implement a more sophisticated approach involving exponential backoff and circuit breaking.)

If that best effort fails, and the `doInsert` call still returns a `Failure`, then it’s highly context-dependent how to handle that. Examples would include displaying a "please try again later" error to a user, if there is one, and logging it for manual human review. The application must make a suitable call for each case.

The application can write similar wrappers for the other operations — replace, upsert, _et al_. Note that the logic is a little different in each case: for inserts, we confirm if the operation has already been successful on an ambiguous result by checking for `DocumentExistsException`But this wouldn’t make sense for an upsert.

### [](#idempotent-and-non-idempotent-operations)Idempotent and Non-Idempotent Operations

> [!TIP]
> Idempotent operations are those that can be applied multiple times and only have one effect. Repeatedly setting an email field is idempotent — increasing a counter by one is not.

Some operations we can view as idempotent as they will fail with no effect after the first success — such as inserts.

Idempotent operations are much easier to handle, as on ambiguous error results (`DurabilityAmbiguousException` and `TimeoutException`) the operation can simply be retried.

Most key-value operations are idempotent. For those that aren’t, such as a Sub-Document `arrayAppend` call, or a counter increment, the application should, on an ambiguous result, first read the document to see if that change was applied.

## [](#query-and-analytics-errors)Query and Analytics Errors

A SQL++ (formerly N1QL) query either returns results or `QueryError`, like so:

```scala
val stmt =
  """select * from `travel-sample` limit 10;"""
cluster.query(stmt)
  .map(_.rowsAs[JsonObject]) match {
  case Success(rows) =>
  case Failure(err) => println(s"Error: ${err}")
}
```

Analytics works in an identical fashion, raising an `AnalyticsError`.

## [](#cloud-native-gateway)Cloud Native Gateway

If you connect to the Kubernetes or OpenShift over our [CloudNative Gateway](managing-connections.md#cloud-native-gateway), using the new `couchbase2://` endpoints, there are a few changes in the error messages returned.

Some error codes are more generic — in cases where the client would not be expected to need to take specific action — but should cause no problem, unless you have written code looking at individual strings within the error messages.

## [](#additional-resources)Additional Resources

Errors & Exception handling is an expansive topic. Here, we have covered examples of the kinds of exception scenarios that you are most likely to face. More fundamentally, you also need to weigh up [concepts of durability](../concept-docs/durability-replication-failure-considerations.md).

Diagnostic methods are available to check on the [health of the cluster](health-check.md), and the [health of the network](#tracing-from-the-sdk.adoc).

Logging methods are dependent upon the platform and SDK used. We offer [recommendations and practical examples](collecting-information-and-logging.md).

We have a [listing of error messages](../ref/error-codes.md), with some pointers to what to do when you encounter them.