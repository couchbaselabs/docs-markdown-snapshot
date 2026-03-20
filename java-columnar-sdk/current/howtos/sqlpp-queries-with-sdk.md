---
title: Querying with SQL++
description: You can query for documents in Couchbase using the SQL++ query
  language, a language based on SQL, but designed for structured and flexible
  JSON documents.
editUrl: https://github.com/couchbase/docs-columnar-sdk-java/edit/release/1.0/modules/howtos/pages/sqlpp-queries-with-sdk.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:java-columnar-sdk:howtos:sqlpp-queries-with-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/java-columnar-sdk/current/howtos/sqlpp-queries-with-sdk.html)

# Querying with SQL++

> You can query for documents in Couchbase using the SQL++ query language, a language based on SQL, but designed for structured and flexible JSON documents. 

On this page we dive straight into using the Query Service API from the Java Columnar SDK. For a deeper look at the concepts, to help you better understand the Query Service, and the SQL++ language, see the links in the [Further Information](#further-information) section at the end of this page.

Here we show queries against the Travel Sample collection, at cluster and scope level, and give links to information on adding other collections to your data.

## [](#before-you-start)Before You Start

This page assumes that you have [installed the Java Columnar SDK](../hello-world/start-using-sdk.md), added your IP address to the allowlist, and [created a Columnar cluster](../../../analytics/admin/prepare-project.md#cluster).

Create a collection to work upon by [importing the travel-sample dataset](../../../analytics/intro/examples.md#travel-sample) into your cluster.

## [](#querying-your-dataset)Querying Your Dataset

Execute a query and buffer all result rows in client memory:

Scope Level

```java
QueryResult result = scope.executeQuery("select 1");
result.rows().forEach(row -> System.out.println("Got row: " + row));
```

Cluster Level

```java
QueryResult result = cluster.executeQuery("select 1");
result.rows().forEach(row -> System.out.println("Got row: " + row));
```

### [](#streaming-queries)Streaming Queries

If you can buffer all of the results in memory, then `executeQuery()` is the simplest method to use, but frequently the data size will be too large for this — or you need to plan for that possibility. Use `executeStreamingQuery()` to execute a query statement and pass the resultant rows to the given `rowAction` callback, one by one, as they arrive from the server.

The callback action is guaranteed to execute in the same thread (or virtual thread) that called this method. If the callback throws an exception, the query is cancelled and the exception is re-thrown by this method. See the [API reference](https://docs.couchbase.com/sdk-api/couchbase-columnar-java-client/com.couchbase.columnar.client.java/com/couchbase/columnar/client/java/Cluster.html#executeStreamingQuery%28java.lang.String,java.util.function.Consumer,java.util.function.Consumer%29) for more details.

### [](#positional-and-named-parameters)Positional and Named Parameters

Supplying parameters as individual arguments to the query allows the query engine to optimize the parsing and planning of the query. You can either supply these parameters by name or by position.

Execute a streaming query with positional arguments:

Positional Parameters

```java
cluster.executeStreamingQuery(
  "select ?=1",
  row -> System.out.println("Got row: " + row),
  options -> options
    .parameters(List.of(1))
);
```

Execute a streaming query with named arguments:

Named Parameters

```java
cluster.executeStreamingQuery(
  "select $foo=1",
  row -> System.out.println("Got row: " + row),
  options -> options
    .parameters(Map.of("foo", 1))
);
```

## [](#further-information)Further Information

The [SQL++ for Analytics Reference](../../../server/current/analytics/1%5Fintro.md)offers a complete guide to the SQL++ language for both of our analytics services, including all of the latest additions.