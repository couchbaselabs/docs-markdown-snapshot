[View original HTML](/scala-sdk/3.9/howtos/analytics-using-sdk.html)

> Parallel data management for complex queries over many records, using a familiar SQL++ syntax. 

This page covers using our operational Scala SDK to connect to the Analytics Service of a Capella Operational or self-managed Couchbase Server cluster. As well as this row-based analytics service, a speedy, column-based analytics database is available for real-time analytics.

|  | Analytics SDKs SDKs for [Enterprise Analytics](../../../enterprise-analytics/current/intro/intro.md) — Couchbase’s analytical database for real time apps and operational intelligence (RT-OLAP) — are available for the .NET, Go, Java, Node.js, and Python platforms. See the [Enterprise Analytics SDK pages](#home::analytics-sdk.adoc) for more information. Currently, different SDKs are needed to connect to [Capella Analytics](../../../analytics/intro/intro.md) — as this service does not have Enterprise Analytics' load balancer, and uses a different connection protocol. Capella Analytics SDKs (also known as Columnar SDKs) are available for the Go, Java, Node.js, and Python platforms. See the [Capella Analytics SDK pages](#home::columnar-sdk.adoc) for more information. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

For complex and long-running queries, involving large ad hoc join, set, aggregation, and grouping operations, Couchbase Data Platform offers the [Couchbase Analytics Service (CBAS)](../../../server/current/analytics/introduction.md). This is the analytic counterpart to our [operational data focussed Query Service](sqlpp-queries-with-sdk.md).

The analytics service is available in [Capella operational](../../../cloud/clusters/analytics-service/analytics-service.md)or the Enterprise Edition of self-managed Couchbase Server.

|  | The Scala 3 version of the SDK does not carry forward support for analytics. Please see [Migrating to Scala 3](../project-docs/migrating-to-scala-3.md) for guidance on these and other changes. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

## [](#getting-started)Getting Started

After familiarizing yourself with our [introductory primer](../../../server/current/analytics/primer-beer.md), in particular creating a dataset and linking it to a bucket to shadow the operational data, try Couchbase Analytics using the Scala SDK. Intentionally, the API for analytics is very similar to that of the query service.

Before starting, here’s all imports used in the following examples:

```scala
import com.couchbase.client.scala._
import com.couchbase.client.scala.analytics.{AnalyticsOptions, AnalyticsParameters, AnalyticsResult, ReactiveAnalyticsResult}
import com.couchbase.client.scala.json._
import reactor.core.scala.publisher.{SFlux, SMono}

import scala.concurrent.Future
import scala.concurrent.duration._
import scala.util.{Failure, Success, Try}
```

Here’s a complete example of doing an analytics query and handling the results:

```scala
val query = """select "hello" as greeting;"""
val result: Try[AnalyticsResult] = cluster.analyticsQuery(query)
val rows: Try[Seq[JsonObject]] = result.flatMap(_.rowsAs[JsonObject])

rows match {
  case Success(r: Seq[JsonObject]) => println(s"Row: ${r.head}")
  case Failure(err) => println(s"Failure ${err}")
}
```

Let’s break this down. First, we get the results in the form of a `Try[AnalyticsResult]`. The Scala SDK returns `Try` rather than throwing exceptions, to allow you to handle errors in a functional way. A `Try` can either be a `Success(AnalyticsResult)` if the query was successfully executed, or `Failure(Throwable)` if something went wrong.

An `AnalyticsResult` contains various things of interest, such as metrics, but the main thing we’re interested in are the rows (results). They’re fetched with the `allRowsAs` call. Note that the `flatMap` means the `allRowsAs` call will only be attempted if the initial query was successful. Otherwise `rows` will contain the `Failure(Throwable)` from the query result.

Here we’re fetching rows converted into `JsonObject`, but as with SQL++ (formerly N1QL) there’s many more options available. Rows can be returned as JSON representations from multiple third party Scala libraries, such as Circe, directly as case classes, and more. Please see [JSON Libraries](json.md) for full details.

Finally, we pattern match on the `rows` to find whether the operations were successful. We check explicitly for `AnalyticsError` which indicates an error from the analytics service. There can be other errors returned, please see [Error Handling](error-handling.md) for details.

We can write that example more concisely, like this:

```scala
cluster.analyticsQuery("""select "hello" as greeting;""")
  .flatMap(_.rowsAs[JsonObject]) match {
  case Success(r)   => println(s"Row: ${r.head}")
  case Failure(err) => println(s"Failure ${err}")
}
```

## [](#queries)Queries

A query can either be `simple` or be `parameterized`. If parameters are used, they can either be `positional` or `named`. Here is one example of each:

```scala
cluster.analyticsQuery(
  """select airportname, country from airports where country = ?;""",
  AnalyticsOptions().parameters(AnalyticsParameters.Positional("France")))
  .flatMap(_.rowsAs[JsonObject]) match {
  case Success(r)   => r.foreach(row => println(s"Row: ${row}"))
  case Failure(err) => println(s"Failure ${err}")
}
```

```scala
cluster.analyticsQuery(
  """select airportname, country from airports where country = $country;""",
  AnalyticsOptions().parameters(AnalyticsParameters.Named(Map("country" -> "France"))))
  .flatMap(_.rowsAs[JsonObject]) match {
  case Success(r)   => r.foreach(row => println(s"Row: ${row}"))
  case Failure(err) => println(s"Failure ${err}")
}
```

## [](#additional-parameters)Additional Parameters

The handful of additional parameters are illustrated here:

```scala
  cluster.analyticsQuery(
    """select airportname, country from airports where country = "France";""",
    AnalyticsOptions()
      // Ask the analytics service to give this request higher priority
      .priority(true)

      // The client context id is returned in the results, so can be used by the
      // application to correlate requests and responses
      .clientContextId("my-id")

      // Override how long the analytics query is allowed to take before timing out
      .timeout(90.seconds)
  ) match {
    case Success(r: AnalyticsResult) =>
      assert(r.metaData.clientContextId.contains("my-id"))
    case Failure(err) => println(s"Failure ${err}")
  }
}
```

### [](#metadata)Metadata

`AnalyticsResult` contains a `meta.metrics` field that contains useful metadata, such as `elapsedTime`, and `resultCount`:

```scala
val stmt =
  """select airportname, country from airports where country = "France";"""
cluster.analyticsQuery(stmt) match {
  case Success(result) =>
    val metrics = result.metaData.metrics
    println(s"Elapsed: ${metrics.elapsedTime}")
    println(s"Results: ${metrics.resultCount}")
    println(s"Errors:  ${metrics.errorCount}")
  case Failure(err) => println(s"Failure ${err}")
}
```

## [](#streaming-large-result-sets)Streaming Large Result Sets

The Scala SDK provides three SDKs (documented further on [Choosing an API](concurrent-async-apis.md)):

* The blocking API you’ve seen so far, that returns an `AnalyticsResult` containing all rows.
* An async API that returns a `Future[AnalyticsResult]`, which also contains all rows. This can be accessed like this:

```scala
// When we work with Scala Futures an ExecutionContext must be provided.
// For this example we'll just use the global default
import scala.concurrent.ExecutionContext.Implicits.global

val stmt = """select airportname, country from airports where country = "France";"""
val future: Future[AnalyticsResult] = cluster.async.analyticsQuery(stmt)

future onComplete {
  case Success(result) =>
    result.rowsAs[JsonObject] match {
      case Success(rows) => rows.foreach(println(_))
      case Failure(err) => println(s"Error: $err")
    }
  case Failure(err) => println(s"Error: $err")
}
```

* A reactive API, that can be used to stream rows.

The former two APIs buffer all rows in-memory until they can be returned to you. With smaller queries this is likely to be fine, but for large data sets this could lead to Java `OutOfMemoryError` exceptions.

The recommended solution is to use the reactive API. Reactive programming is a sophisticated paradigm that is rapidly gaining popularity for its ability to handle, amongst other things, streaming large amounts of data over fallible networks, while allowing error handling and backpressure.

The Scala SDK exposes primitives from the [Project Reactor](https://projectreactor.io/) library, most notably `Mono` and `Flux`. We strongly recommend [learning](https://projectreactor.io/learn) a little of this library first, and the following examples will assume basic familiarity with Reactor.

|  | You’ll see both reactor.core.scala.publisher and reactor.core.publisher imports available for Reactor. Use the former, it is the Scala-optimized variant that the Scala SDK will return. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Here’s how to perform a query and stream the results using the reactive API:

```scala
val stmt =
  """select airportname, country from airports where country = "France";"""
val mono: SMono[ReactiveAnalyticsResult] = cluster.reactive.analyticsQuery(stmt)

val rows: SFlux[JsonObject] = mono
  // ReactiveQueryResult contains a rows: Flux[AnalyticsRow]
  .flatMapMany(result => result.rowsAs[JsonObject])

// Just for example, block on the rows.  This is not best practice and apps
// should generally not block.
val allRows: Seq[JsonObject] = rows
  .doOnNext(row => println(row))
  .doOnError(err => println(s"Error: $err"))
  .collectSeq()
  .block()
```