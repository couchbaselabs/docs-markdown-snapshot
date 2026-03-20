---
title: Query
description: You can query for documents in Couchbase using the SQL++ query language.
editUrl: https://github.com/couchbase/docs-sdk-kotlin/edit/temp/1.4/modules/howtos/pages/n1ql-queries.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:1.4@kotlin-sdk:howtos:n1ql-queries.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/kotlin-sdk/1.4/howtos/n1ql-queries.html)

# Query

> You can query for documents in Couchbase using the SQL++ query language. SQL++ (formerly N1QL) is based on SQL, but designed for structured and flexible JSON documents. 

## [](#prerequisites)Before You Start

You should know [how to write a SQL++ query](http://query.pub.couchbase.com/tutorial/#1).

You should know [how to connect to a Couchbase cluster](connecting.md).

You should know about [documents and collections](organizing-documents.md).

The examples on this page use the `travel-sample` [sample bucket](../../../server/7.6/manage/manage-settings/install-sample-buckets.md).

## [](#search-default-collection)Searching the Default Collection

This example uses a SQL++ query to get 10 documents from the default collection in the `travel-sample` bucket.

```kotlin
val queryResult: QueryResult = cluster
    .query("SELECT * FROM `travel-sample` LIMIT 10")
    .execute() (1)

queryResult.rows.forEach { row: QueryRow ->
    println("Found row: " + row.contentAs<Map<String, Any?>>())
}
```

| **1** | The query method returns a Flow<QueryFlowItem>. Nothing happens until you collect the flow. Calling execute is an easy way to collect the flow. |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------- |

> [!CAUTION]
> Buckets and Queries Before Couchbase 6.5
> 
> If you use a version of Couchbase before 6.5, you must open a bucket before doing a query. It does not need to be the bucket you are searching. If you forget to open a bucket, the SDK throws `FeatureNotAvailableException`.

## [](#search-non-default-collection)Searching a Non-Default Collection

The `travel-sample` bucket has a scope called `inventory`. This scope has copies of the documents from the default collection, organized into collections.

This example gets 10 documents from the `airline` collection in the `inventory` scope. There are two versions of the example. Both versions do the same thing, but one uses `Cluster.query`, and the other uses `Scope.query`. Look at both to see the difference.

* Cluster.query
* Scope.query

If you use `Cluster.query` to search a non-default collection, the `FROM` clause must have the bucket name, scope name, and collection name.

```kotlin
val queryResult: QueryResult = cluster
    .query("""
        SELECT * 
        FROM `travel-sample`.inventory.airline 
        LIMIT 10
        """)
    .execute()

queryResult.rows.forEach { row: QueryRow ->
    println("Found row: " + row.contentAs<Map<String, Any?>>())
}
```

If you use `Scope.query` to search a non-default collection, the `FROM` clause does not need the bucket name or scope name. Instead, this information comes from the `Scope` object.

```kotlin
val scope: Scope = cluster
    .bucket("travel-sample")
    .scope("inventory")

val queryResult: QueryResult = scope
    .query("SELECT * FROM airline LIMIT 10")
    .execute()

queryResult.rows.forEach { row: QueryRow ->
    println("Found row: " + row.contentAs<Map<String, Any?>>())
}
```

## [](#parameters)Query Parameters

A "query parameter" is like a variable in a SQL++ statement. Query parameters protect you from SQL injection. They also help the server parse and plan the query.

You can give parameters names, or refer to them by position.

> [!NOTE]
> Some parts of a SQL++ statement cannot be parameters. If you use a parameter where it is not allowed, the SDK throws an exception.

### [](#named-parameters)Named parameters

Using named parameters often make it easier to read complex queries.

A query with named parameters

```kotlin
val queryResult: QueryResult = cluster
    .query(
        statement = """
            SELECT *
            FROM `travel-sample`.inventory.airline
            WHERE country = @country (1)
        """,
        parameters = QueryParameters.named(
            "country" to "France"
        )
    )
    .execute()
```

| **1** | As a courtesy to Kotlin users, Couchbase Server 7.2.0 and later let you use either @ or $ when referencing named parameters in SQL++ statements. If you use an older version of Couchbase Server, use $ instead of @. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

> [!WARNING]
> When using `$` to reference a named parameter, always escape the `$`. Otherwise, Kotlin does string interpolation, which does not prevent SQL injection.

### [](#positional-parameters)Positional parameters

If you use positional parameters, the order of the parameters must match the order of the question mark (`?`) placeholders in the statement.

A query with positional parameters

```kotlin
val queryResult: QueryResult = cluster
    .query(
        statement = """
            SELECT *
            FROM `travel-sample`.inventory.airline
            WHERE country = ?
        """,
        parameters = QueryParameters.positional(
            listOf("France")
        )
    )
    .execute()
```

## [](#metadata)Metadata

The server returns more than just rows. It also returns information about how the query was executed, how long it took, and any bad things that happened. This information is called "query metadata." A `QueryMetadata` object holds this information.

It is expensive to return some kinds of metadata, like metrics and profiling information. If you want that information, you must ask for it when doing the query.

This example asks for all metadata, and prints it:

```kotlin
val queryResult: QueryResult = cluster
    .query(
        statement = "SELECT * FROM `travel-sample`.inventory.airline",
        metrics = true,
        profile = QueryProfile.TIMINGS,
    )
    .execute()

val metadata: QueryMetadata = queryResult.metadata

println("Client context ID: ${metadata.clientContextId}")
println("Request ID: ${metadata.requestId}")
println("Signature: ${metadata.signature}")
println("Status: ${metadata.status}")
println("Warnings: ${metadata.warnings}")

metadata.metrics?.let { metrics: QueryMetrics ->
    println("Reported execution time: ${metrics.executionTime}")
    println("Other metrics: $metrics")
}

metadata.profile?.let { profile: Map<String, Any?> ->
    println("Profile: $profile")
}
```

## [](#streaming)Streaming

The previous examples store all result rows in memory. If there are many rows, this can use a lot of memory.

To use less memory, pass a lambda to `execute` and work on each row one at a time, like this:

```kotlin
val metadata: QueryMetadata = cluster
    .query("SELECT * FROM `travel-sample`.inventory.airline")
    .execute { row: QueryRow ->
        println("Found row: " + row.contentAs<Map<String, Any?>>())
    }
```

> [!NOTE]
> The streaming version of `execute` returns `QueryMetadata` instead of `QueryResult`.

## [](#prepared-statements)Prepared Statements

Each time you execute a query, the server makes a plan for finding the results. You can ask the server to remember the plan. This turns your query into a "prepared statement."

To run a query as a prepared statement, pass `adhoc = false` to the `query` method, like this:

```kotlin
val queryResult: QueryResult = cluster
    .query(
        statement = "SELECT * FROM `travel-sample` LIMIT 10",
        adhoc = false,
    )
    .execute()
```

A prepared statement is not always faster than an adhoc query. Sometimes the server can make a better plan for an adhoc query than for a prepared statement. It’s good to measure the performance of your query, so you know if it’s good to use a prepared statement.

## [](#read-only)Read-Only Queries

If a query does not change data, it’s good to tell the SDK the query is "read-only."

The server ensures a read-only query does not change data. If a read-only query fails, the SDK retries it because it knows it’s safe to retry.

To run a read-only query, pass `readonly = true` to the `query` method, like this:

```kotlin
val queryResult: QueryResult = cluster
    .query(
        statement = "SELECT * FROM `travel-sample` LIMIT 10",
        readonly = true,
    )
    .execute()
```

## [](#scan-consistency)Scan Consistency

When you change a document in Couchbase, it takes time for the Query service to index the document. A query index "runs behind" the KV service. When you execute a query, you get to choose if you want to wait for the index to "catch up" to the latest KV changes.

### [](#scan-consistency-unbounded)Unbounded

By default, the Query service does not wait. It only searches documents that were already indexed when the query started. This is called "unbounded" scan consistency.

This is the default value for the `query` method’s `consistency` parameter.

### [](#scan-consistency-request-plus)Request Plus

When you choose "request plus" scan consistency, changes that happened before you called `execute` are always reflected in the query results. "Request plus" is more expensive than "unbounded", because the server must wait for the query index to catch up. (The "plus" in "request plus" means changes that happened after you called `execute` might be reflected in the results, too.)

### [](#scan-consistency-consistent-with)Consistent With

If you made some changes, you can tell the server to wait for the changes to be indexed. In other words, the query results are "consistent with" the changes you made. To use this kind of scan consistency, you must keep track of the mutation tokens from the changes you want to wait for.

```kotlin
val collection = cluster
    .bucket("travel-sample")
    .scope("inventory")
    .collection("airline")

val mutationResult: MutationResult =
    collection.upsert("my-fake-airline", mapOf("id" to 9000))

val mutationState = MutationState()
mutationState.add(mutationResult)

val queryResult: QueryResult = cluster
    .query(
        statement = "SELECT * FROM `travel-sample`.inventory.airline LIMIT 10",
        consistency = QueryScanConsistency
            .consistentWith(mutationState)
    )
    .execute()
```

## [](#client-context-id)Client Context ID

Each query has a "client context ID" that helps with debugging. If you know a query’s ID, you can search for the ID in the Couchbase Server logs or a network trace.

The ID can be any string. It’s good for the ID to be different every time you execute a query. If you do not set the ID, the SDK uses a different random UUID every time.

In this example, the client context ID includes the name of an application user, so it’s easy to search for all queries related to the user.

Setting the client context ID

```kotlin
val queryResult: QueryResult = cluster
    .query(
        statement = "SELECT * FROM `travel-sample` LIMIT 10",
        clientContextId = "user-44-" + UUID.randomUUID(),
    )
    .execute()
```