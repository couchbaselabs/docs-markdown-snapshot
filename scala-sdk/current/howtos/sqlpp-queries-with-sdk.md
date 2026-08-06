---
title: Querying with SQL++
description: You can query for documents in Couchbase using the SQL++ query
  language, a language based on SQL, but designed for structured and flexible
  JSON documents.
editUrl: https://github.com/couchbase/docs-sdk-scala/edit/release/3.12/modules/howtos/pages/sqlpp-queries-with-sdk.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:scala-sdk:howtos:sqlpp-queries-with-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/scala-sdk/current/howtos/sqlpp-queries-with-sdk.html)

# Querying with SQL++

> You can query for documents in Couchbase using the SQL++ query language, a language based on SQL, but designed for structured and flexible JSON documents. 

On this page we dive straight into using the Query Service API from the Scala SDK. For a deeper look at the concepts, to help you better understand the Query Service, the SQL++ language, and the Index Service, see the links in the [Further Information](#further-information) section at the end of this page.

> You can query for documents in Couchbase using the SQL++ query language (formerly N1QL), a language based on SQL, but designed for structured and flexible JSON documents. 

Our query service uses SQL++, which will be fairly familiar to anyone who's used any dialect of SQL. [Additional Resources](#additional-resources) for learning about SQL++ are listed at the bottom of the page. Before you get started you may wish to checkout the [SQL++ intro page](#6.5@server:n1ql:n1ql-language-reference/index.adoc).

> [!TIP]
> SQL++ Compared to Key-Value
> 
> SQL++ is excellent for performing queries against multiple documents, but if you only need to access or mutate a single document and you know its unique ID, it will be much more efficient to use the Key-Value API. We strongly recommend using both APIs to create a flexible, performant application.

## [](#getting-started)Getting Started

Let's get started by pulling in all the imports needed in the examples below:

```scala
import com.couchbase.client.scala._
import com.couchbase.client.scala.implicits.Codec
import com.couchbase.client.scala.json._
import com.couchbase.client.scala.kv.MutationState
import com.couchbase.client.scala.query._
import reactor.core.scala.publisher._

import scala.concurrent.Future
import scala.util.{Failure, Success, Try}
```

Then we connect to a Couchbase cluster, as usual (of course, change the address and credentials to match your own cluster's):

```scala
    val cluster = Cluster.connect("localhost", "Administrator", "password").get
    val bucket = cluster.bucket("travel-sample")
    val collection = bucket.defaultCollection
```

The examples below will use the travel-sample example bucket. This can be installed through the Couchbase Admin UI in Settings → Sample Buckets.

In order to be able to use query on a bucket, it must have at least a primary index created. The easiest way to create this is through the Couchbase Admin UI. Simply visit the Query tab then write this in the Query Editor and hit Execute:

```n1ql
CREATE PRIMARY INDEX ON `travel-sample`
```

Note that building indexes is covered in more detail on the [Query concept page](../concept-docs/n1ql-query.md#index-building) — and in the [API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client/com/couchbase/client/scala/manager/query/index.html).

## [](#a-simple-query)A Simple Query

Here's the basics of how to run a simple query to fetch 10 random rows from travel-sample and print the results:

```scala
val statement = """select * from `travel-sample` limit 10;"""
val result: Try[QueryResult] = cluster.query(statement)
```

(Note that we won't be covering the SQL++ language itself in any detail here, but if you're familiar with SQL you'll see it's very similar.)

The Scala SDK returns `Try` rather than throwing exceptions, to allow you to handle errors in a functional way. A `Try` can either be a `Success(QueryResult)` if the SQL++ statement was successfully executed, or `Failure(Throwable)` if something went wrong. It can be pattern matched on like this:

```scala
result match {
  case Success(result: QueryResult) =>
    result.rowsAs[JsonObject] match {
      case Success(rows) =>
        println(s"Got ${rows} rows")
      case Failure(err) => println(s"Error: $err")
    }
  case Failure(err) => println(s"Error: $err")
}
```

The returned `QueryResult` contains an `rowsAs[T]` method, allowing the results to be converted into something useful. The above example demonstrates returning the results as `JsonObject`, the JSON library built-in to the Scala SDK.

Other things rowsAs can convert to are:

* `io.circe.Json` from the popular Scala JSON library [Circe](https://circe.github.io/circe/)
* Similar support is included for other excellent JSON libraries: [uPickle/uJson](https://github.com/lihaoyi/upickle), [Play Json](https://github.com/playframework/play-json), [Jawn](https://github.com/typelevel/jawn), and [Json4s](https://github.com/json4s/json4s).
* Scala case classes. A tiny amount of boilerplate is needed to support this: see [Key-Value Operations](kv-operations.md) for details.
* `String`
* `Array[Byte]`

Please see [this guide](json.md) for more information on the supported ways of working with JSON.

Of course, it wouldn't be Scala if we couldn't elegantly combine the operations above more concisely:

```scala
cluster
  .query("""select * from `travel-sample` limit 10;""")
  .flatMap(_.rowsAs[JsonObject]) match {
  case Success(rows: Seq[JsonObject]) =>
    rows.foreach(row => println(row))
  case Failure(err) =>
    println(s"Error: $err")
}
```

> [!NOTE]
> Most of the examples here use the simplest of the three APIs provided by the Scala SDK, which blocks until the operation is performed. There's also an asynchronous API that is based around Scala `Future`, and a streaming reactive API, for which we'll see an example later.

## [](#placeholder-and-named-arguments)Placeholder and Named Arguments

Placeholders allow you to specify variable constraints for a query.

There are two variants of placeholders: positional and named parameters. Both are used as placeholders for values in the WHERE, LIMIT or OFFSET clause of a query.

Positional parameters use an ordinal placeholder for substitution and can be used like this:

```scala
      val stmt =
        """select count(*)
        from `travel-sample`.inventory.airport
        where country=$1;"""
      val result = cluster.query(
        stmt,
        QueryOptions()
          .adhoc(false)
          .parameters(QueryParameters.Positional("United States"))
      )
```

Whereas named parameters can be used like this:

```scala
      val stmt =
        """select `travel-sample`.* from `travel-sample` where type=$type and country=$country limit 10;"""
      val result = cluster.query(
        stmt,
        QueryOptions().parameters(
          QueryParameters.Named(Map("type" -> "airline", "country" -> "United States"))
        )
      )
```

## [](#scan-consistency)Scan Consistency

Queries take an optional `scanConsistency` parameter that enables a tradeoff between latency and (eventual) consistency.

* A SQL++ query using the default `NotBounded` scan consistency will not wait for any indexes to finish updating before running the query and returning results, meaning that results are returned quickly, but the query will not return any documents that are yet to be indexed.
* With scan consistency set to `RequestPlus`, all outstanding document changes and index updates are processed before the query is run. Select this when consistency is always more important than performance.
* For a middle ground, `AtPlus` is a "read your own write" (RYOW) option, which means it just waits for the documents that you specify to be indexed.

Here's how to specify the `RequestPlus` scan consistency level:

```scala
      val result = cluster.query(
        "select `travel-sample`.* from `travel-sample` limit 10;",
        QueryOptions().scanConsistency(QueryScanConsistency.RequestPlus())
      )
```

And the `AtPlus` level is represented with `QueryScanConsistency.ConsistentWith`:

```scala
val result = collection.upsert("id", content)
  .flatMap(upsertResult => {
    val ms = MutationState.from(upsertResult)

    cluster.query(
      "select `travel-sample`.* from `travel-sample` limit 10;",
        QueryOptions().scanConsistency(QueryScanConsistency.ConsistentWith(ms))
    )
  })

result match {
  case Success(_) =>
  case Failure(err) => println(s"Operation failed with error $err")
}
```

## [](#returning-results-as-case-classes)Returning Results as Case Classes

The Scala SDK supports returning SQL++ results directly as Scala case classes.

A small amount of boilerplate is required to tell the SDK how to convert your case class to/from JSON. There are more details available [here](json.md#case-classes), but the short version is to add a `Codec` in the case class's companion object like this:

```scala
case class Address(line1: String)
case class User(name: String, age: Int, addresses: Seq[Address])
object User {
  implicit val codec: Codec[User] = Codec.codec[User]
}
```

Now you're free to pull out the results directly as your case class:

```scala

val statement =
  """select `users`.* from `users` limit 10;"""

val users = cluster
  .query(statement)
  .flatMap(_.rowsAs[User]) match {
  case Success(rows: Seq[User]) =>
    rows.foreach(row => println(row))
  case Failure(err) =>
    println(s"Error: $err")
}
```

## [](#streaming-large-result-sets)Streaming Large Result Sets

As mentioned earlier, the Scala SDK provides three SDKs (documented further on [Choosing an API](concurrent-async-apis.md)):

* The blocking API you've seen so far, that returns a `QueryResult` containing all rows.
* An async API that returns a `Future[QueryResult]`, which also contains all rows. This can be accessed like this:

```scala
// When we work with Scala Futures an ExecutionContext must be provided.
// For this example we'll just use the global default
      import scala.concurrent.ExecutionContext.Implicits.global

      val stmt = """select `travel-sample`.* from `travel-sample` limit 10;"""
      val future: Future[QueryResult] = cluster.async.query(stmt)

      future onComplete {
        case Success(result) =>
          result.rowsAs[JsonObject] match {
            case Success(rows) => rows.foreach(println(_))
            case Failure(err)  => println(s"Error: $err")
          }
        case Failure(err) => println(s"Error: $err")
      }
```

* A reactive API, that can be used to stream rows.

The former two APIs buffer all rows in-memory until they can be returned to you. With smaller queries this is likely to be fine, but for large data sets this could lead to Java `OutOfMemoryError` exceptions.

The recommended solution is to use the reactive API. Reactive programming is a sophisticated paradigm that is rapidly gaining popularity for its ability to handle, amongst other things, streaming large amounts of data over fallible networks, while allowing error handling and backpressure.

The Scala SDK exposes primitives from the [Project Reactor](https://projectreactor.io/) library, most notably `Mono` and `Flux`. We strongly recommend [learning](https://projectreactor.io/learn) a little of this library first, and the following examples will assume basic familiarity with Reactor.

> [!NOTE]
> You'll see both `reactor.core.scala.publisher` and `reactor.core.publisher` imports available for Reactor. Use the former, it is the Scala-optimized variant that the Scala SDK will return.

Here's how to perform a query and stream the results using the reactive API:

```scala
val stmt = """select `travel-sample`.* from `travel-sample`;"""
val mono: SMono[ReactiveQueryResult] = cluster.reactive.query(stmt)

val rows: SFlux[JsonObject] = mono
// ReactiveQueryResult contains a rows: Flux[QueryRow]
  .flatMapMany(result => result.rowsAs[JsonObject])

// Just for example, block on the rows.  This is not best practice and apps
// should generally not block.
val allRows: Seq[JsonObject] = rows
  .doOnNext(row => println(row))
  .doOnError(err => println(s"Error: $err"))
  .collectSeq()
  .block()
```

> [!NOTE]
> The Scala 3 version of the SDK does not carry forward support for the reactive API, since it depends on an external library that is end-of-life. Please see [Migrating to Scala 3](../project-docs/migrating-to-scala-3.md) for guidance on these and other changes.

## [](#querying-at-scope-level)Querying at Scope Level

It is possible to query off the [Scope level](../../../server/current/learn/data/scopes-and-collections.md) with _Couchbase Server version 7.0_ onwards, using the `scope.query()` method. It takes the statement as a required argument, and then allows additional options if needed.

The code snippet below shows how to run a simple query to fetch 10 random rows from travel-sample and print the results, the assumption is that the `airline` collection exists within a scope `us`.

```scala
scope
  .query("""select * from `airline` limit 10;""")
  .flatMap(_.rowsAs[JsonObject]) match {
  case Success(rows: Seq[JsonObject]) =>
    rows.foreach(row => println(row))
  case Failure(err) =>
    println(s"Error: $err")
}
```

A complete list of `QueryOptions` can be found in the [API docs](https://docs.couchbase.com/sdk-api/couchbase-scala-client/com/couchbase/client/scala/query/QueryOptions.html).

## [](#additional-resources)Additional Resources

> [!NOTE]
> SQL++ is not the only query option in Couchbase. Be sure to check that [your use case fits your selection of query service](../concept-docs/querying-your-data.md).

The [SQL++ interactive tutorial](http://query.pub.couchbase.com/tutorial/#1) is a good introduction to the basics of SQL++ use.