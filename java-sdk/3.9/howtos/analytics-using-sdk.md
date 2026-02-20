---
title: Analytics
description: Parallel data management for complex queries over many records,
  using a familiar SQL-like syntax.
editUrl: https://github.com/couchbase/docs-sdk-java/edit/release/3.9/modules/howtos/pages/analytics-using-sdk.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:3.9@java-sdk:howtos:analytics-using-sdk.adoc[]
---

[View original HTML](/java-sdk/3.9/howtos/analytics-using-sdk.html)

# Analytics

> Parallel data management for complex queries over many records, using a familiar SQL-like syntax. 

This page covers using our operational Java SDK to connect to the Analytics Service of a Capella Operational or self-managed Couchbase Server cluster. As well as this row-based analytics service, a speedy, column-based analytics database is available for real-time analytics.

> [!TIP]
> Analytics SDKs
> 
> SDKs for [Enterprise Analytics](../../../enterprise-analytics/current/intro/intro.md) — Couchbase’s analytical database for real time apps and operational intelligence (RT-OLAP) — are available for the .NET, Go, Java, Node.js, and Python platforms. See the [Enterprise Analytics SDK pages](#home::analytics-sdk.adoc) for more information.
> 
> Currently, different SDKs are needed to connect to [Capella Analytics](../../../analytics/intro/intro.md) — as this service does not have Enterprise Analytics' load balancer, and uses a different connection protocol. Capella Analytics SDKs (also known as Columnar SDKs) are available for the Go, Java, Node.js, and Python platforms. See the [Capella Analytics SDK pages](#home::columnar-sdk.adoc) for more information.

For complex and long-running queries, involving large ad hoc join, set, aggregation, and grouping operations, Couchbase Data Platform offers the [Couchbase Analytics Service (CBAS)](../../../server/current/analytics/introduction.md). This is the analytic counterpart to our [operational data focussed Query Service](sqlpp-queries-with-sdk.md).

The analytics service is available in [Capella operational](../../../cloud/clusters/analytics-service/analytics-service.md)or the Enterprise Edition of self-managed Couchbase Server.

## [](#getting-started)Getting Started

After familiarizing yourself with our [introductory primer](#7.1@server:analytics:primer-beer.adoc), in particular creating a dataset and linking it to a bucket, try Couchbase Analytics using the Java SDK. Intentionally, the API for analytics is nearly identical to that of the query service.

Before starting, here’s all imports used in the following examples:

```java
import com.couchbase.client.core.error.CouchbaseException;
import com.couchbase.client.java.Bucket;
import com.couchbase.client.java.Cluster;
import com.couchbase.client.java.Scope;
import com.couchbase.client.java.analytics.AnalyticsResult;
import com.couchbase.client.java.analytics.AnalyticsScanConsistency;
import com.couchbase.client.java.analytics.ReactiveAnalyticsResult;
import com.couchbase.client.java.json.JsonArray;
import com.couchbase.client.java.json.JsonObject;
import reactor.core.publisher.Mono;

import java.util.UUID;

import static com.couchbase.client.java.analytics.AnalyticsOptions.analyticsOptions;
```

Here’s a complete example of doing an analytics query and handling the results:

```java
try {
  final AnalyticsResult result = cluster
    .analyticsQuery("select \"hello\" as greeting");

  for (JsonObject row : result.rowsAsObject()) {
    System.out.println("Found row: " + row);
  }

  System.out.println("Reported execution time: "
    + result.metaData().metrics().executionTime());

  System.out.println();

} catch (CouchbaseException ex) {
  ex.printStackTrace();
}
```

Let’s break it down. An analytics query is always performed at the `Cluster` level, using the `analyticsQuery` method. It takes the statement as a required argument and then allows to provide additional options if needed (in the example above, no options are specified).

Once a result returns you can iterate the returned rows and/or accessing the `AnalyticsMetaData` associated with the query. If something goes wrong during the execution of the query, a derivate of the `CouchbaseException` will be thrown that also provides additional context on the operation:

```console
Exception in thread "main" com.couchbase.client.core.error.ParsingFailureException: Parsing of the input failed {"completed":true,"coreId":1,"errors":[{"code":24000,"message":"Syntax error: In line 1 >>select 1=;<< Encountered \"=\" at column 9. "}], ... }
```

> [!NOTE]
> Open Buckets and Cluster-Level Queries
> 
> If you are using a cluster older than Couchbase Server 6.5, it is required that there is at least one bucket open before performing a cluster-level query. If you fail to do so, the SDK will return a `FeatureNotAvailableException` with a descriptive error message asking you to open one.

## [](#parameterized-queries)Parameterized Queries

Supplying parameters as individual arguments to the query allows the analytics engine to optimize the parsing and planning of the query. You can either supply these parameters by name or by position.

The first example shows how to provide them by name:

```java
AnalyticsResult result = cluster.analyticsQuery(
  "select count(*) from airport where country = $country",
  analyticsOptions().parameters(JsonObject.create().put("country", "France")));
```

The second example by position:

```java
AnalyticsResult result = cluster.analyticsQuery(
  "select count(*) from airport where country = ?",
  analyticsOptions().parameters(JsonArray.from("France"))
);
```

What style you choose is up to you, for readability in more complex queries we generally recommend using the named parameters.

Note that you cannot use parameters in all positions. If you put it in an unsupported place the server will respond with a `ParsingFailureException`.

## [](#the-analytics-result)The Analytics Result

When performing an analytics query, the response you receive is an `AnalyticsResult`. If no exception gets raised the request succeeded and provides access to both the rows returned and also associated `AnalyticsMetaData`.

Rows can be consumed either through a `JsonObject` directly, turned into a java collection instance (like a `Map`) or into your POJO of choice mapping directly to your domain logic.

```java
AnalyticsResult result = cluster.analyticsQuery(
  "select * from airport limit 3"
);
for (JsonObject row : result.rowsAsObject()) {
  System.out.println("Found row: " + row);
}
```

The `AnalyticsMetaData` provides insight into some basic profiling/timing information as well as information like the `clientContextId`.

__Table 1\. AnalyticsMetaData__
| Name                              | Description                                                                      |
| --------------------------------- | -------------------------------------------------------------------------------- |
| String requestId()                | Returns the request identifer of this request.                                   |
| String clientContextId()          | Returns the context ID either generated by the SDK or supplied by the user.      |
| AnalyticsStatus status()          | An enum simply representing the state of the result.                             |
| AnalyticsMetrics metrics()        | Returns metrics provided by analytics for the request.                           |
| Optional<JsonObject> signature()  | If a signature is present, it will be available to consume in a generic fashion. |
| List<AnalyticsWarning> warnings() | Non-fatal errors are available to consume as warnings on this method.            |

For example, here is how you can print the `executionTime` of a query:

```java
AnalyticsResult result = cluster.analyticsQuery("select 1=1");
System.err.println(
  "Execution time: " + result.metaData().metrics().executionTime()
);
```

## [](#analytics-options)Analytics Options

The analytics service provides an array of options to customize your query. The following table lists them all:

__Table 2\. Available Analytics Options__
| Name                                      | Description                                                          |
| ----------------------------------------- | -------------------------------------------------------------------- |
| clientContextId(String)                   | Sets a context ID returned by the service for debugging purposes.    |
| parameters(JsonArray)                     | Allows to set positional arguments for a parameterized query.        |
| parameters(JsonObject)                    | Allows to set named arguments for a parameterized query.             |
| priority(boolean)                         | Assigns a different server-side priority to the query.               |
| raw(String, Object)                       | Escape hatch to add arguments that are not covered by these options. |
| readonly(boolean)                         | Tells the client and server that this query is readonly.             |
| scanConsistency(AnalyticsScanConsistency) | Sets a different scan consistency for this query.                    |
| serializer(JsonSerializer)                | Allows to use a different serializer for the decoding of the rows.   |

### [](#scan-consistency)Scan Consistency

By default, the analytics engine will return whatever is currently in the index at the time of query (this mode is also called `AnalyticsScanConsistency.NOT_BOUNDED`). If you need to include everything that has just been written, a different scan consistency must be chosen. If `AnalyticsScanConsistency.REQUEST_PLUS` is chosen, it will likely take a bit longer to return the results but the analytics engine will make sure that it is as up-to-date as possible.

```java
AnalyticsResult result = cluster.analyticsQuery(
  "select count(*) from airport where country = 'France'",
  analyticsOptions().scanConsistency(AnalyticsScanConsistency.REQUEST_PLUS)
);
```

### [](#client-context-id)Client Context Id

The SDK will always send a client context ID with each query, even if none is provided by the user. By default a UUID will be generated that is mirrored back from the analytics engine and can be used for debugging purposes. A custom string can always be provided if you want to introduce application-specific semantics into it (so that for example in a network dump it shows up with a certain identifier). Whatever is chosen, we recommend making sure it is unique so different queries can be distinguished during debugging or monitoring.

```java
AnalyticsResult result = cluster.analyticsQuery(
  "select count(*) from airport where country = 'France'",
  analyticsOptions().clientContextId("user-44" + UUID.randomUUID())
);
```

### [](#priority)Priority

By default, every analytics query has the same priority on the server. By setting this boolean flag to true, you are indicating that you need expedited dispatch in the analytice engine for this request.

```java
AnalyticsResult result = cluster.analyticsQuery(
  "select count(*) from airport where country = 'France'",
  analyticsOptions().priority(true)
);
```

### [](#readonly)Readonly

If the query is marked as readonly, both the server and the SDK can improve processing of the operation. On the client side, the SDK can be more liberal with retries because it can be sure that there are no state-mutating side-effects happening. The query engine will ensure that actually no data is mutated when parsing and planning the query.

```java
AnalyticsResult result = cluster.analyticsQuery(
  "select count(*) from airport where country = 'France'",
  analyticsOptions().readonly(true)
);
```

### [](#custom-json-serializer)Custom JSON Serializer

Like with all JSON apis, it is possible to customize the JSON serializer. It allows to plug in your own library (like GSON) or custom configured mappings on your own Jackson serializer. This in turn makes it possible to serialize rows into POJOs or other structures that your application defines and the SDK has no idea about.

Please see the documentation transcoding and serialization for more information.

## [](#reactive-and-async-apis)Reactive And Async APIs

In addition to the blocking API on `Cluster`, the SDK provides reactive and async APIs on `ReactiveCluster` or `AsyncCluster` respectively. If you are in doubt of which API to use, we recommend looking at the reactive first. It builds on top of reactor, a powerful library that allows you to compose reactive computations and deal with error handling and other related concerns (like retry) in an elegant manner. The async API on the other hand exposes a `CompletableFuture` and is more meant for lower level integration into other libraries or if you need the last drop of performance.

Also, there is another reason you want to use the reactive API: streaming large results with backpressure from the application side. Both the blocking and async APIs have no means of signalling backpressure in a good way, so if you need it the reactive API is your best option.

> [!TIP]
> Advanced Reactive Concepts Ahead
> 
> Please see the guides on reactive programming for more information on the basics, this guide is diving straight into their impact on querying analytics.

A simple reactive query is similar to the blocking one:

```java
Mono<ReactiveAnalyticsResult> result = cluster
  .reactive()
  .analyticsQuery("select 1=1");

result
  .flatMapMany(ReactiveAnalyticsResult::rowsAsObject)
  .subscribe(row -> System.out.println("Found row: " + row));
```

This query will stream all rows as they become available from the server, automatically applying backpressure as necessary.

## [](#scoped-queries-on-named-collections)Scoped Queries on Named Collections

In addition to creating a dataset with a WHERE clause to filter the results to documents with certain characteristics, the SDK allows you to create a dataset against a named collection, for example:

```sqlpp
ALTER COLLECTION `travel-sample`.inventory.airport ENABLE ANALYTICS;

-- NB: this is more or less equivalent to:
CREATE DATAVERSE `travel-sample`.inventory;
CREATE DATASET `travel-sample`.inventory.airport ON `travel-sample`.inventory.airport;
```

We can then query the Dataset as normal, using the fully qualified keyspace:

```java
AnalyticsResult result = cluster.analyticsQuery(
  "SELECT airportname, country FROM `travel-sample`.inventory.airport WHERE country='France' LIMIT 3");
```

Note that using the `CREATE DATASET` syntax we could choose any Dataset name in any Dataverse, including the default. However the SDK supports this standard convention, allowing us to query from the Scope object:

```java
Bucket bucket = cluster.bucket("travel-sample");
Scope scope = bucket.scope("inventory");
AnalyticsResult result = scope.analyticsQuery(
  "SELECT airportname, country FROM `airport` WHERE country='France' LIMIT 4");
```