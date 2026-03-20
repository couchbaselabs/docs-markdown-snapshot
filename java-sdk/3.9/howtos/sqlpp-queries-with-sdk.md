---
title: Query
description: You can query for documents in Couchbase using the
  https://www.couchbase.com/products/n1ql[SQL++] (formerly N1QL) query language,
  a language based on SQL, but designed for structured and flexible JSON
  documents.
editUrl: https://github.com/couchbase/docs-sdk-java/edit/release/3.9/modules/howtos/pages/sqlpp-queries-with-sdk.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:3.9@java-sdk:howtos:sqlpp-queries-with-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/java-sdk/3.9/howtos/sqlpp-queries-with-sdk.html)

# Query

> You can query for documents in Couchbase using the [SQL++](https://www.couchbase.com/products/n1ql) (formerly N1QL) query language, a language based on SQL, but designed for structured and flexible JSON documents. Querying can solve typical programming tasks such as finding a user profile by email address, facebook login, or user ID. 

## [](#getting-started)Getting Started

After familiarizing yourself with the basics on how the SQL++ query language works and how to query it from the UI you can use it from the Java SDK.

Before starting, here are all of the imports used in the following examples:

```java
import com.couchbase.client.java.Bucket;
import com.couchbase.client.java.Cluster;
import com.couchbase.client.java.Scope;
import com.couchbase.client.java.json.JsonArray;
import com.couchbase.client.java.json.JsonObject;
import com.couchbase.client.java.query.QueryResult;
import com.couchbase.client.java.query.QueryScanConsistency;
import com.couchbase.client.java.query.ReactiveQueryResult;
import reactor.core.publisher.Mono;

import java.util.UUID;

import static com.couchbase.client.java.query.QueryOptions.queryOptions;
```

Here’s a complete example of doing a query and handling the results:

* Couchbase Capella Sample
* Local Couchbase Server

These examples requires the Travel Sample Bucket. The Couchbase Capella free tier version comes with this bucket, and its Query indexes, loaded and ready.

```java
public class SimpleQueryCloud {
  // Update these variables to point to your Couchbase Capella instance and credentials.
  static String connectionString = "couchbases://cb.<your-endpoint-here>.cloud.couchbase.com";
  static String username = "Administrator";
  static String password = "password";

  public static void main(String[] args) throws Exception {
    Cluster cluster = Cluster.connect(
    connectionString,
    ClusterOptions.clusterOptions(username, password).environment(env -> {
    env.applyProfile("wan-development");
    })
    );

    { 
      try {
        final QueryResult result = cluster.query("select * from `travel-sample`.inventory.airline limit 100",
        queryOptions().metrics(true));

        for (JsonObject row : result.rowsAsObject()) {
          System.out.println("Found row: " + row);
      }

      System.out.println("Reported execution time: " + result.metaData().metrics().get().executionTime());

      } catch (CouchbaseException ex) {
        ex.printStackTrace();
      }
    }
  }
}
```

To run these examples, you will need to install the Travel Sample Bucket using either the [Web interface](../../../server/current/manage/manage-settings/install-sample-buckets.md#install-sample-buckets-with-the-ui)or the [command line](../../../server/current/manage/manage-settings/install-sample-buckets.md#install-sample-buckets-with-the-cli).

```java
public class SimpleQuery {
  // Update these variables to point to your Couchbase instance and credentials.
  static String connectionString = "localhost";
  static String username = "Administrator";
  static String password = "password";

  public static void main(String[] args) throws Exception {
    Cluster cluster = Cluster.connect(connectionString, username, password);
  
    {
      try {
        final QueryResult result = cluster.query("select * from `travel-sample`.inventory.airline limit 100",
          queryOptions().metrics(true));
  
        for (JsonObject row : result.rowsAsObject()) {
          System.out.println("Found row: " + row);
        }
  
        System.out.println("Reported execution time: " + result.metaData().metrics().get().executionTime());
      } catch (CouchbaseException ex) {
        ex.printStackTrace();
      }
    }
  }
}
```

Note that building indexes is covered in some detail on the [Query concept page](../concept-docs/n1ql-query.md#index-building), which you should take a quick look at — and in the [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/manager/query/package-summary.html).

Let’s break down the above code snippet. A query is always performed at the `Cluster` level, using the `query` method. It takes the statement as a required argument and then allows to provide additional options if needed (in the example above, no options are specified).

Once a result returns you can iterate the returned rows and/or accessing the `QueryMetaData` associated with the query. If something goes wrong during the execution of the query, a derivate of the `CouchbaseException` will be thrown that also provides additional context on the operation:

```console
Exception in thread "main" com.couchbase.client.core.error.ParsingFailureException: Parsing of the input failed {"completed":true,"coreId":1,"errors":[{"code":3000,"message":"syntax error - at end of input"}],"idempotent":false,"lastDispatchedFrom":"127.0.0.1:56279","lastDispatchedTo":"127.0.0.1:8093","requestId":3,"requestType":"QueryRequest","service":{"operationId":"eee9b796-bfff-42dc-941d-1a985e019ff8","statement":"select 1=","type":"query"},"timeoutMs":75000,"timings":{"dispatchMicros":14381,"totalMicros":1365348}}
```

> [!NOTE]
> Open Buckets and Cluster-Level Queries
> 
> If you are using a cluster older than Couchbase Server 6.5, it is required that there is at least one bucket open before performing a cluster-level query. If you fail to do so, the SDK will return a `FeatureNotAvailableException` with a descriptive error message asking you to open one.

## [](#parameterized-queries)Parameterized Queries

Supplying parameters as individual arguments to the query allows the query engine to optimize the parsing and planning of the query. You can either supply these parameters by name or by position.

The first example shows how to provide them by name:

```java
QueryResult result = cluster.query(
    "select count(*) from `travel-sample`.inventory.airline where country = $country",
    queryOptions().parameters(JsonObject.create().put("country", "France")));
```

The second example by position:

```java
QueryResult result = cluster.query(
    "select count(*) from `travel-sample`.inventory.airline where country = ?",
    queryOptions().parameters(JsonArray.from("France")));
```

What style you choose is up to you, for readability in more complex queries we generally recommend using the named parameters.

Note that you cannot use parameters in all positions. If you put it in an unsupported place the server will respond with a `PlanningFailureException` or similar.

## [](#the-query-result)The Query Result

When performing a query, the response you receive is a `QueryResult`. If no exception gets raised the request succeeded and provides access to both the rows returned and also associated `QueryMetaData`.

Rows can be consumed either through a `JsonObject` directly, turned into a java collection instance (like a `Map`) or into your POJO of choice mapping directly to your domain logic.

```java
QueryResult result = cluster.query("select * from `travel-sample`.inventory.airline limit 10");
for (JsonObject row : result.rowsAsObject()) {
  System.out.println("Found row: " + row);
}
```

The `QueryMetaData` provides insight into some basic profiling/timing information as well as information like the `clientContextId`.

__Table 1\. QueryMetaData__
| Name                             | Description                                                                      |
| -------------------------------- | -------------------------------------------------------------------------------- |
| String requestId()               | Returns the request identifer of this request.                                   |
| String clientContextId()         | Returns the context ID either generated by the SDK or supplied by the user.      |
| QueryStatus status()             | An enum simply representing the state of the result.                             |
| Optional<QueryMetrics> metrics() | Returns metrics provided by the query for the request if enabled.                |
| Optional<JsonObject> signature() | If a signature is present, it will be available to consume in a generic fashion. |
| List<QueryWarning> warnings()    | Non-fatal errors are available to consume as warnings on this method.            |
| Optional<JsonObject> profile()   | If enabled returns additional profiling information of the query.                |

For example, here is how you can print the `executionTime` of a query:

```java
QueryResult result = cluster.query("select 1=1", queryOptions().metrics(true));
System.err.println("Execution time: " + result.metaData().metrics().get().executionTime());
```

## [](#query-options)Query Options

The query service provides an array of options to customize your query. The following table lists them all:

__Table 2\. Available Query Options__
| Name                                  | Description                                                                         |
| ------------------------------------- | ----------------------------------------------------------------------------------- |
| clientContextId(String)               | Sets a context ID returned by the service for debugging purposes.                   |
| parameters(JsonArray)                 | Allows to set positional arguments for a parameterized query.                       |
| parameters(JsonObject)                | Allows to set named arguments for a parameterized query.                            |
| priority(boolean)                     | Assigns a different server-side priority to the query.                              |
| raw(String, Object)                   | Escape hatch to add arguments that are not covered by these options.                |
| readonly(boolean)                     | Tells the client and server that this query is readonly.                            |
| adhoc(boolean)                        | If set to false will prepare the query and later execute the prepared statement.    |
| consistentWith(MutationState)         | Allows to be consistent with previously written mutations ("read your own writes"). |
| maxParallelism(int)                   | Tunes the maximum parallelism on the server.                                        |
| metrics(boolean)                      | Enables the server to send metrics back to the client as part of the response.      |
| pipelineBatch(int)                    | Sets the batch size for the query pipeline.                                         |
| pipelineCap(int)                      | Sets the cap for the query pipeline.                                                |
| profile(QueryProfile)                 | Allows to enable additional query profiling as part of the response.                |
| scanWait(Duration)                    | Allows to specify a maximum scan wait time.                                         |
| scanCap(int)                          | Specifies a maximum cap on the query scan size.                                     |
| scanConsistency(QueryScanConsistency) | Sets a different scan consistency for this query.                                   |
| serializer(JsonSerializer)            | Allows to use a different serializer for the decoding of the rows.                  |

## [](#scan-consistency)Scan Consistency

By default, the query engine will return whatever is currently in the index at the time of query (this mode is also called `QueryScanConsistency.NOT_BOUNDED`). If you need to include everything that has just been written, a different scan consistency must be chosen. If `QueryScanConsistency.REQUEST_PLUS` is chosen, it will likely take a bit longer to return the results but the query engine will make sure that it is as up-to-date as possible.

```java
QueryResult result = cluster.query(
    "select count(*) from `travel-sample`.inventory.airline where country = 'France'",
    queryOptions().scanConsistency(QueryScanConsistency.REQUEST_PLUS));
```

### [](#client-context-id)Client Context ID

The SDK will always send a client context ID with each query, even if none is provided by the user. By default a UUID will be generated that is mirrored back from the query engine and can be used for debugging purposes. A custom string can always be provided if you want to introduce application-specific semantics into it (so that for example in a network dump it shows up with a certain identifier). Whatever is chosen, we recommend making sure it is unique so different queries can be distinguished during debugging or monitoring.

```java
QueryResult result = cluster.query(
    "select count(*) from `travel-sample`.inventory.airline where country = 'France'",
    queryOptions().clientContextId("user-44" + UUID.randomUUID()));
```

### [](#readonly)Readonly

If the query is marked as readonly, both the server and the SDK can improve processing of the operation. On the client side, the SDK can be more liberal with retries because it can be sure that there are no state-mutating side-effects happening. The query engine will ensure that actually no data is mutated when parsing and planning the query.

```java
QueryResult result = cluster.query(
    "select count(*) from `travel-sample`.inventory.airline where country = 'France'",
    queryOptions().readonly(true));
```

### [](#custom-json-serializer)Custom JSON Serializer

Like with all JSON apis, it is possible to customize the JSON serializer. It allows to plug in your own library (like GSON) or custom configured mappings on your own Jackson serializer. This in turn makes it possible to serialize rows into POJOs or other structures that your application defines and the SDK has no idea about.

Please see the [documentation on transcoding and serialization](transcoders-nonjson.md) for more information.

## [](#reactive-and-async-apis)Reactive And Async APIs

In addition to the blocking API on `Cluster`, the SDK provides reactive and async APIs on `ReactiveCluster` or `AsyncCluster` respectively. If you are in doubt of which API to use, we recommend looking at the reactive first. It builds on top of reactor, a powerful library that allows you to compose reactive computations and deal with error handling and other related concerns (like retry) in an elegant manner. The async API on the other hand exposes a `CompletableFuture` and is more meant for lower level integration into other libraries or if you need the last drop of performance.

Also, there is another reason you want to use the reactive API: streaming large results with backpressure from the application side. Both the blocking and async APIs have no means of signalling backpressure in a good way, so if you need it the reactive API is your best option.

> [!TIP]
> Advanced Reactive Concepts Ahead
> 
> Please see the guides on reactive programming for more information on the basics, this guide is diving straight into their impact on querying.

A simple reactive query is similar to the blocking one:

```java
Mono<ReactiveQueryResult> result = cluster.reactive().query("select 1=1");

result.flatMapMany(ReactiveQueryResult::rowsAsObject).subscribe(row -> System.out.println("Found row: " + row));
```

This query will stream all rows as they become available from the server, automatically applying backpressure as necessary.

## [](#querying-at-scope-level)Querying at Scope Level

It is possible to query off the [Scope level](../concept-docs/n1ql-query.md#collections-and-scopes-and-the-query-context), _with Couchbase Server release 7.x_, using the `scope.query()` method. It takes the statement as a required argument, and then allows additional options if needed.

A complete list of `QueryOptions` can be found in the [API docs](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/AsyncScope.html#query-java.lang.String-).

```java
Bucket bucket = cluster.bucket("travel-sample");
Scope scope = bucket.scope("inventory");

QueryResult result = scope.query("select * from `airline` where country = $country LIMIT 10",
    queryOptions().parameters(JsonObject.create().put("country", "France")));

for (JsonObject row : result.rowsAsObject()) {
  System.out.println("Found row: " + row);
}
```

## [](#additional-resources)Additional Resources

> [!NOTE]
> SQL++ is not the only query option in Couchbase. Be sure to check that [your use case fits your selection of query service](../concept-docs/querying-your-data.md).

* For a deeper dive into SQL++ from the SDK, refer to our [SQL++ SDK concept doc](../concept-docs/n1ql-query.md).
* The [Server doc SQL++ intro](#7.1@server:n1ql:n1ql-language-reference/index.adoc) introduces a complete guide to the SQL++ language, including all of the latest additions.
* The [SQL++ interactive tutorial](http://query.pub.couchbase.com/tutorial/#1) is a good introduction to the basics of SQL++ use.
* For scaling up queries, be sure to [read up on Indexes](#7.1@server:learn:services-and-indexes/indexes/index-replication.adoc).
* Read more on [when to choose the Analytics service](../concept-docs/querying-your-data.md#long-running-queries-big-data).