---
title: Async &amp; Reactive APIs
description: "The Couchbase Scala SDK allows the use, and mixing, of three
  distinct APIs: blocking, asynchronous, and reactive."
editUrl: https://github.com/couchbase/docs-sdk-scala/edit/release/3.11/modules/howtos/pages/concurrent-async-apis.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:3.11@scala-sdk:howtos:concurrent-async-apis.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/scala-sdk/3.11/howtos/concurrent-async-apis.html)

# Async &amp; Reactive APIs

> The Couchbase Scala SDK allows the use, and mixing, of three distinct APIs: blocking, asynchronous, and reactive. 

The Scala SDK provides three APIs, which can be freely mixed:

* A simple blocking one, that returns `Try`.
* An asynchronous one, that returns `Future`.
* A reactive one, that returns reactive primitives from the [Project Reactor](https://projectreactor.io/) library, e.g. `Mono` and `Flux`.

> [!NOTE]
> The Scala 3 version of the SDK does not carry forward support for the reactive API, since it depends on an external library that is end-of-life. Please see [Migrating to Scala 3](../project-docs/migrating-to-scala-3.md) for guidance on these and other changes.

## [](#using-the-blocking-api)Using the Blocking API

This is the simplest API, in which all operations are synchronous and blocking. A simple upsert example looks like this:

```scala
val json = JsonObject("foo" -> "bar", "baz" -> "qux")

val result = collection.upsert("document-key", json)
```

Methods in the blocking API that can error will return a Scala `Try` object, which can either be a `Success` containing the result, or a `Failure` containing a _Throwable_ exception that derives from `CouchbaseException`.

This can be pattern matched on, like this:

```scala
val json = JsonObject("foo" -> "bar", "baz" -> "qux")

collection.upsert("document-key", json) match {
  case Success(_) => println("Successfully upserted")
  case Failure(exception) => println("Error: " + exception)
}
```

Simple pattern matching like this works fine for simple examples, but starts to look complicated when doing multiple operations:

```scala
// Create some initial JSON
val json = JsonObject("status" -> "awesome!")

// Upsert it
collection.upsert("document-key", json) match {
  case Success(result) =>
  case Failure(err) => println("Error: " + err)
}

// Get it back
collection.get("document-key") match {
  case Success(result) =>

    // Convert the content to a JsonObjectSafe
    result.contentAs[JsonObjectSafe] match {
      case Success(json) =>

        // Pull out the JSON's status field, if it exists
        json.str("status") match {
          case Success(status) => println(s"Couchbase is $status")
          case _ => println("Field 'status' did not exist")
        }
      case Failure(err) => println("Error decoding result: " + err)
    }
  case Failure(err) => println("Error getting document: " + err)
}
```

Developers may prefer to use `flatMap`, which lets all the `Try` be checked in one place. Here, the call to `collection.get` will only be attempted if the call to `collection.upsert` was successful — that is, returned `Success`.

```scala
val json = JsonObject("status" -> "awesome!")

val result: Try[String] = collection.upsert("document-key", json)
  .flatMap(_ => collection.get("document-key"))
  .flatMap(_.contentAs[JsonObjectSafe])
  .flatMap(_.str("status"))

result match {
  case Success(status) => println(s"Couchbase is $status")
  case Failure(err) =>    println("Error: " + err)
}
```

## [](#using-the-asynchronous-api)Using the Asynchronous API

The asynchronous API returns Scala `Future`, representing the execution of an asynchronous task and the promise of a future result.

Here's what a simple upsert looks like, handling `Success` or `Failure`(note we are not actually blocking on the result here — if you need that then you can use the methods in Scala's `Await`, or simply use the blocking Couchbase API):

```scala
val json = JsonObject("foo" -> "bar", "baz" -> "qux")

val result: Future[MutationResult] = collection.async.upsert("document-key", json)

result onComplete {
  case Success(_)         => println("Successfully upserted")
  case Failure(exception) => println("Error: " + exception)
}
```

But, the compiler will fail to compile this, reporting that an implicit `ExecutionContext` cannot be found for onComplete.

As you may know, to do anything with a `Future` — including `onComplete`, `map` and `flatMap` — an `ExecutionContext` is required. Here's how to create one that creates an unlimited thread-pool with named threads:

```scala
val threadPool = Executors.newCachedThreadPool(new ThreadFactory {
  override def newThread(runnable: Runnable): Thread = {
    val thread = new Thread(runnable)
    // Make it a daemon thread so it doesn't block app exit
    thread.setDaemon(true)
    thread.setName("my-thread-prefix-" + thread.getId)
    thread
  }
})
implicit val ec = ExecutionContext.fromExecutor(threadPool)
```

Now there's an implicit ExecutionContext available, the upsert example will compile.

Let's see a more complex example combining operations together. `Future` compose well, with `flatMap` being the most common tool:

```scala
val json = JsonObject("foo" -> "bar", "baz" -> "qux")

val result: Future[String]   = collection.async.upsert("document-key", json)
  .flatMap(_                => collection.async.get("document-key"))
  .map((v: GetResult)       => v.contentAs[JsonObject])
  .map((v: Try[JsonObject]) => v.get)
  .map((v: JsonObject)      => v.str("status"))

result onComplete {
  case Success(status) => println(s"Status ${status}")
  case Failure(err: DocumentNotFoundException) => println("Doc not found")
  case Failure(err: NoSuchElementException) => println("JSON not in expected format")
  case Failure(exception) => println("Error: " + exception)
}
```

Interestingly, you'll see a couple of calls to `Try.get()` here. These throw exceptions if the Try is `Failure`, and exceptions are usually something we try to avoid in Scala. But here there's no problem as the `Future` will capture the exception, and raise in so it can be handled in a `Failure`, as in the example.

## [](#using-the-reactive-api)Using the Reactive API

Reactive Programming is an advanced paradigm designed to handle the challenges of building modern, network-aware and fault-tolerant programs.

The reactive API uses primitives from [Project Reactor](https://projectreactor.io/), namely `Mono` (returning at most one result) and `Flux` (returning many). These are compliant with the [reactive streams specification](https://www.reactive-streams.org/), and so can easily be converted into other reactive implementations such as RxJava.

Here's how to do a simple reactive upsert operation, logging any errors:

```scala
val json = JsonObject("foo" -> "bar", "baz" -> "qux")

collection.reactive.upsert("document-key", json)
    .doOnError(err  => println(s"Error during upsert: ${err}"))
    .doOnNext(_     => println("Success"))
    .subscribe()
```

`upsert` returns `Mono[MutationResult]`. The `subscribe` starts the operation - without a subscribe, nothing will happen. The operation happens in the background.

Normally with reactive programming you will chain multiple operations together, and it's often possible to continue handling the chain in a reactive manner too. For instance, many web frameworks allow an endpoint to stream back a reactive result.

In the rare cases where you need to block on a reactive primitive (say, in a unit test) you can do it like this:

```scala
val json = JsonObject("foo" -> "bar", "baz" -> "qux")

val result: MutationResult = collection.reactive.upsert("document-key", json)
  .doOnError(err => println(s"Error during upsert: ${err}"))
  .doOnNext(mutationResult => println("Success"))
  .block()
```

The `block` call here also does a `subscribe` under the hood.

Let's look at a more complex example, combining multiple operations. As with `Future`, reactive primitives can be composed, with `flatMap` being the most common tool.

```scala
val json = JsonObject("foo" -> "bar", "baz" -> "qux")

// This example is written in a verbose style for clarity
collection.reactive.upsert("document-key", json)
  .flatMap(_                  => collection.reactive.get("document-key"))
  .map((v: GetResult)         => v.contentAs[JsonObject])
  .map((v: Try[JsonObject])   => v.get)
  .map((v: JsonObject)        => v.str("status"))

  .doOnError {
    case err: DocumentNotFoundException => println("Doc not found")
    case err: NoSuchElementException => println("JSON not in expected format")
    case err => println(s"Error: ${err}")
  }

  .subscribe()
```

Similar to the `Future` example, you'll note some calls to .get, on `Option` and `Try` that will throw exceptions if they do not contain `Some` or `Success` respectively. This is fine — the reactive code will capture it, and raise it in the standard reactive way — e.g. through `doOnError` and similar operators.

While it's beyond the scope of this guide to teach reactive programming, it's important to touch on a handful of golden rules:

1. Never do blocking calls inside operators (operators are `doOnNext`, `flatMap`, etc.). Those operators are executing on a limited number of threads, and blocking calls will limit concurrency. Instead, convert the blocking call into a `Mono` or `Flux`, and `flatMap` to it.
2. Never subscribe to a reactive primitive inside an operator. Instead, `flatMap` to it.
3. Always subscribe. A `Mono` or `Flux` will not start until it's subscribed to.

### [](#bulk-operations)Bulk Operations

For bulk operations, and applying the golden rules above, call `flatMap` inside `SFlux`, as in the `upsert` example following:

```scala
val json = JsonObject("foo" -> "bar", "baz" -> "qux")
val parallelism = 32

val result: Seq[Either[Throwable, MutationResult]] = SFlux.fromIterable(Seq("doc1", "doc2", "doc3"))
      .flatMap(docId => collection.reactive.upsert(docId, json)
              .map(result => Right(result))
              .onErrorResume(err => SMono.just(Left(err))),
          parallelism)
      .collectSeq()
      .block()
```

## [](#choosing-an-api)Choosing an API

So which API should you choose?

It's really down to you and the needs of your application. If you're already writing code in a synchronous way already then it may make sense to continue that way. If you're writing a web application that supports reactive streams, it may make sense to use the reactive API. And you can use different APIs at different times.

The most important thing to consider is when streaming back large queries from Query, Full Text Search, and Analytics. Here, the reactive API will provide full backpressure: that is, if your application is processing rows slower than the service is returning them, then automatically fewer rows will be requested from the service to give the application time to catch up. The upshot of this is that few rows are ever buffered in-memory, and the application shouldn't get out-of-memory exceptions.

By contrast, the blocking and asynchronous APIs will buffer all rows in-memory before returning them to the application. This will generally be fine, but if you're doing any large queries then you may want to consider the reactive API.