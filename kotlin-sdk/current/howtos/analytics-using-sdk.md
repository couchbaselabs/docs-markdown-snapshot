[View original HTML](/kotlin-sdk/current/howtos/analytics-using-sdk.html)

> Parallel data management for complex queries over many records, using a familiar SQL++ syntax. 

This page covers using our operational Kotlin SDK to connect to the Analytics Service of a Capella Operational or self-managed Couchbase Server cluster. As well as this row-based analytics service, a speedy, column-based analytics database is available for real-time analytics.

|  | Analytics SDKs SDKs for [Enterprise Analytics](../../../enterprise-analytics/current/intro/intro.md) — Couchbase’s analytical database for real time apps and operational intelligence (RT-OLAP) — are available for the .NET, Go, Java, Node.js, and Python platforms. See the [Enterprise Analytics SDK pages](#home::analytics-sdk.adoc) for more information. Currently, different SDKs are needed to connect to [Capella Analytics](../../../analytics/intro/intro.md) — as this service does not have Enterprise Analytics' load balancer, and uses a different connection protocol. Capella Analytics SDKs (also known as Columnar SDKs) are available for the Go, Java, Node.js, and Python platforms. See the [Capella Analytics SDK pages](#home::columnar-sdk.adoc) for more information. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

For complex and long-running queries, involving large ad hoc join, set, aggregation, and grouping operations, Couchbase Data Platform offers the [Couchbase Analytics Service (CBAS)](../../../server/current/analytics/introduction.md). This is the analytic counterpart to our [operational data focussed Query Service](#sqlpp-queries-with-sdk.adoc).

The analytics service is available in [Capella operational](../../../cloud/clusters/analytics-service/analytics-service.md)or the Enterprise Edition of self-managed Couchbase Server.

|  | The Scala 3 version of the SDK does not carry forward support for analytics. Please see [Migrating to Scala 3](#project-docs:migrating-to-scala-3.adoc) for guidance on these and other changes. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

## [](#getting-started)Getting Started

After familiarizing yourself with our [introductory primer](../../../server/current/analytics/primer-beer.md), in particular creating a dataset and linking it to a bucket to shadow the operational data, try Couchbase Analytics using the Scala SDK. Intentionally, the API for analytics is very similar to that of the query service.

Before starting, here’s all imports used in the following examples:

```scala
Unresolved include directive in modules/howtos/pages/analytics-using-sdk.adoc - include::devguide:example$scala/Analytics.scala[]
```

Here’s a complete example of doing an analytics query and handling the results:

```scala
Unresolved include directive in modules/howtos/pages/analytics-using-sdk.adoc - include::devguide:example$scala/Analytics.scala[]
```

Let’s break this down. First, we get the results in the form of a `Try[AnalyticsResult]`. The Scala SDK returns `Try` rather than throwing exceptions, to allow you to handle errors in a functional way. A `Try` can either be a `Success(AnalyticsResult)` if the query was successfully executed, or `Failure(Throwable)` if something went wrong.

An `AnalyticsResult` contains various things of interest, such as metrics, but the main thing we’re interested in are the rows (results). They’re fetched with the `allRowsAs` call. Note that the `flatMap` means the `allRowsAs` call will only be attempted if the initial query was successful. Otherwise `rows` will contain the `Failure(Throwable)` from the query result.

Here we’re fetching rows converted into `JsonObject`, but as with SQL++ (formerly N1QL) there’s many more options available. Rows can be returned as JSON representations from multiple third party Scala libraries, such as Circe, directly as case classes, and more. Please see [JSON Libraries](json.md) for full details.

Finally, we pattern match on the `rows` to find whether the operations were successful. We check explicitly for `AnalyticsError` which indicates an error from the analytics service. There can be other errors returned, please see [Error Handling](#howtos:error-handling.adoc) for details.

We can write that example more concisely, like this:

```scala
Unresolved include directive in modules/howtos/pages/analytics-using-sdk.adoc - include::devguide:example$scala/Analytics.scala[]
```

## [](#queries)Queries

A query can either be `simple` or be `parameterized`. If parameters are used, they can either be `positional` or `named`. Here is one example of each:

```scala
Unresolved include directive in modules/howtos/pages/analytics-using-sdk.adoc - include::devguide:example$scala/Analytics.scala[]
```

```scala
Unresolved include directive in modules/howtos/pages/analytics-using-sdk.adoc - include::devguide:example$scala/Analytics.scala[]
```

## [](#additional-parameters)Additional Parameters

The handful of additional parameters are illustrated here:

```scala
Unresolved include directive in modules/howtos/pages/analytics-using-sdk.adoc - include::devguide:example$scala/Analytics.scala[]
```

### [](#metadata)Metadata

`AnalyticsResult` contains a `meta.metrics` field that contains useful metadata, such as `elapsedTime`, and `resultCount`:

```scala
Unresolved include directive in modules/howtos/pages/analytics-using-sdk.adoc - include::devguide:example$scala/Analytics.scala[]
```

## [](#streaming-large-result-sets)Streaming Large Result Sets

The Scala SDK provides three SDKs (documented further on [Choosing an API](#howtos:concurrent-async-apis.adoc)):

* The blocking API you’ve seen so far, that returns an `AnalyticsResult` containing all rows.
* An async API that returns a `Future[AnalyticsResult]`, which also contains all rows. This can be accessed like this:

```scala
Unresolved include directive in modules/howtos/pages/analytics-using-sdk.adoc - include::devguide:example$scala/Analytics.scala[]
```

* A reactive API, that can be used to stream rows.

The former two APIs buffer all rows in-memory until they can be returned to you. With smaller queries this is likely to be fine, but for large data sets this could lead to Java `OutOfMemoryError` exceptions.

The recommended solution is to use the reactive API. Reactive programming is a sophisticated paradigm that is rapidly gaining popularity for its ability to handle, amongst other things, streaming large amounts of data over fallible networks, while allowing error handling and backpressure.

The Scala SDK exposes primitives from the [Project Reactor](https://projectreactor.io/) library, most notably `Mono` and `Flux`. We strongly recommend [learning](https://projectreactor.io/learn) a little of this library first, and the following examples will assume basic familiarity with Reactor.

|  | You’ll see both reactor.core.scala.publisher and reactor.core.publisher imports available for Reactor. Use the former, it is the Scala-optimized variant that the Scala SDK will return. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Here’s how to perform a query and stream the results using the reactive API:

```scala
Unresolved include directive in modules/howtos/pages/analytics-using-sdk.adoc - include::devguide:example$scala/Analytics.scala[]
```