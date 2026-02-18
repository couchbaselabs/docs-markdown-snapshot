---
title: Using Couchbase Transactions
description: A practical guide on using Couchbase Distributed ACID transactions,
  via the Java SDK.
editUrl: https://github.com/couchbase/docs-sdk-java/edit/release/3.10/modules/howtos/pages/distributed-acid-transactions-from-the-sdk.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/java-sdk/3.10/howtos/distributed-acid-transactions-from-the-sdk.html)

# Using Couchbase Transactions

> A practical guide on using Couchbase Distributed ACID transactions, via the Java SDK. 

> [!IMPORTANT]
> The Couchbase transactions feature was previously distributed as a separate library, before being integrated into the SDK from version `3.3.0`. Users of the transactions library are recommended to follow the [Transactions Migration Guide](../project-docs/distributed-acid-transactions-migration-guide.md).

This guide will show you examples of how to perform multi-document ACID (atomic, consistent, isolated, and durable) database transactions within your application, using the Couchbase Java SDK.

Refer to the [Transaction Concepts](../concept-docs/transactions.md) page for a high-level overview.

## [](#prerequisites)Prerequisites

* Couchbase Capella
* Couchbase Server

* Couchbase Capella account.
* You should know how to perform [key-value](kv-operations.md) or [query](sqlpp-queries-with-sdk.md) operations with the SDK.
* Your application should have the relevant roles and permissions on the required buckets, scopes, and collections, to perform transactional operations. Refer to the [Organizations & Access](../../../cloud/organizations/organization-projects-overview.md) page for more details.
* If your application is using [extended attributes (XATTRs)](../concept-docs/xattr.md), you should avoid using the XATTR field `txn` — this is reserved for Couchbase use.

* Couchbase Server (6.6.1 or above).
* You should know how to perform [key-value](kv-operations.md) or [query](sqlpp-queries-with-sdk.md) operations with the SDK.
* Your application should have the relevant roles and permissions on the required buckets, scopes, and collections, to perform transactional operations. Refer to the [Roles](../../../server/current/learn/security/roles.md) page for more details.
* If your application is using [extended attributes (XATTRs)](../concept-docs/xattr.md), you should avoid using the XATTR field `txn` — this is reserved for Couchbase use.
* NTP should be configured so nodes of the Couchbase cluster are in sync with time.

> [!CAUTION]
> Single Node Cluster
> 
> When using a single node cluster (for example, during development), the default number of replicas for a newly created bucket is **1**. If left at this default, all key-value writes performed with durability will fail with a `DurabilityImpossibleException`. In turn, this will cause all transactions (which perform all key-value writes durably) to fail. This setting can be changed via:
> 
> * [Capella UI](../../../cloud/clusters/data-service/manage-buckets.md#add-bucket)
> * [Couchbase Server UI](../../../server/current/manage/manage-buckets/create-bucket.md#couchbase-bucket-settings)
> * [Command Line](../../../server/current/cli/cbcli/couchbase-cli-bucket-create.md#options)
> 
> If the bucket already exists, then the server needs to be rebalanced for the setting to take effect.

## [](#creating-a-transaction)Creating a Transaction

To create a transaction, an application must supply its logic inside a `lambda`, including any conditional logic required. Once the lambda has successfully run to conclusion, the transaction will be automatically committed. If at any point an error occurs, the transaction will rollback and the lambda may run again.

You can create transactions either _synchronously_ or _asynchronously_ (using the [Project Reactor](https://projectreactor.io/) reactive library).

* Synchronous API
* Asynchronous API

The synchronous mode is the easiest to write and understand.

Transactions are accessed via the `Cluster` object. By invoking `Cluster.transactions()`, we can access the `Transactions` object and `run` the lambda.

```java
Scope inventory = cluster.bucket("travel-sample").scope("inventory");

try {
    TransactionResult result = cluster.transactions().run((ctx) -> {
        // Inserting a doc:
        ctx.insert(collection, "doc-a", JsonObject.create());

        // Getting documents:
        TransactionGetResult docA = ctx.get(collection, "doc-a");

        // Replacing a doc:
        TransactionGetResult docB = ctx.get(collection, "doc-b");
        JsonObject content = docB.contentAs(JsonObject.class);
        content.put("transactions", "are awesome");
        ctx.replace(docB, content);

        // Removing a doc:
        TransactionGetResult docC = ctx.get(collection, "doc-c");
        ctx.remove(docC);

        // Performing a SELECT N1QL query against a scope:
        TransactionQueryResult qr = ctx.query(inventory, "SELECT * FROM hotel WHERE country = $1",
                TransactionQueryOptions.queryOptions()
                        .parameters(JsonArray.from("United Kingdom")));
        var rows = qr.rowsAs(JsonObject.class);

        // Performing an UPDATE N1QL query on multiple documents, in the `inventory` scope:
        ctx.query(inventory, "UPDATE route SET airlineid = $1 WHERE airline = $2",
                TransactionQueryOptions.queryOptions()
                        .parameters(JsonArray.from("airline_137", "AF")));
    });
} catch (TransactionCommitAmbiguousException e) {
    throw logCommitAmbiguousError(e);
} catch (TransactionFailedException e) {
    throw logFailure(e);
}
```

The asynchronous mode allows you to build your application in a reactive style, which can help you scale with excellent efficiency.

Transactions are accessed via the `ReactiveCluster` object. By invoking `Cluster.reactive().transactions()`, we can access the `ReactiveTransactions` object and `run` the lambda.

```java
ReactiveScope inventory = cluster.bucket("travel-sample").scope("inventory").reactive();

Mono<TransactionResult> result = cluster.reactive().transactions().run((ctx) -> {
    // Inserting a doc:
    return ctx.insert(collection.reactive(), "doc-a", JsonObject.create())

            // Getting and replacing a doc:
            .then(ctx.get(collection.reactive(), "doc-b")).flatMap(docB -> {
                var content = docB.contentAs(JsonObject.class);
                content.put("transactions", "are awesome");
                return ctx.replace(docB, content);
            })

            // Getting and removing a doc:
            .then(ctx.get(collection.reactive(), "doc-c"))
                .flatMap(doc -> ctx.remove(doc))

            // Performing a SELECT N1QL query, in the `inventory` scope:
            .then(ctx.query(inventory, "SELECT * FROM hotel WHERE country = $1",
                    TransactionQueryOptions.queryOptions()
                            .parameters(JsonArray.from("United Kingdom"))))

            .flatMap(queryResult -> {
                var rows = queryResult.rowsAs(JsonObject.class);
                // The application would do something with the rows here.
                return Mono.empty();
            })

            // Performing an UPDATE N1QL query on multiple documents, in the `inventory` scope:
            .then(ctx.query(inventory, "UPDATE route SET airlineid = $1 WHERE airline = $2",
                    TransactionQueryOptions.queryOptions()
                            .parameters(JsonArray.from("airline_137", "AF"))));
}).doOnError(err -> {
    if (err instanceof TransactionCommitAmbiguousException) {
        throw logCommitAmbiguousError((TransactionCommitAmbiguousException) err);
    } else if (err instanceof TransactionFailedException) {
        throw logFailure((TransactionFailedException) err);
    }
});

// Normally you will chain this result further and ultimately subscribe.
// For simplicity, here we just block on the result.
result.block();
```

The transaction lambda gets passed a `TransactionAttemptContext` object — generally referred to as `ctx` in these examples. Since the lambda could be rerun multiple times, it is important that it does not contain any side effects. In particular, you should never perform regular operations on a `Collection`, such as `collection.insert()`, inside the lambda. Such operations may be performed multiple times, and will not be performed transactionally. Instead, you should perform these operations through the `ctx` object, e.g. `ctx.insert()`.

The result of a transaction is represented by a `TransactionResult` object, which can be used to expose debugging and logging information to help track what happened during a transaction.

In the event that a transaction fails, your application could run into the following errors:

* `TransactionCommitAmbiguousException`
* `TransactionFailedException`

Refer to [Error Handling](../concept-docs/transactions-error-handling.md#transaction%5Ferrors) for more details on these.

### [](#logging)Logging

To aid troubleshooting, each transaction maintains a list of log entries, which can be logged on failure like this:

* Synchronous API
* Asynchronous API

```java
} catch (TransactionCommitAmbiguousException e) {
    throw logCommitAmbiguousError(e);
} catch (TransactionFailedException e) {
    throw logFailure(e);
}
```

```java
}).doOnError(err -> {
    if (err instanceof TransactionCommitAmbiguousException) {
        throw logCommitAmbiguousError((TransactionCommitAmbiguousException) err);
    } else if (err instanceof TransactionFailedException) {
        throw logFailure((TransactionFailedException) err);
    }
});
```

It is a good practice for the application to log any failed transactions into its own logging system, here represented with a logger object:

```java
public static RuntimeException logCommitAmbiguousError(TransactionCommitAmbiguousException err) {
    // This example will intentionally not compile: the application needs to use
    // its own logging system to replace `logger`.
    logger.warning("Transaction possibly reached the commit point");

    for (TransactionLogEvent msg : err.logs()) {
        logger.warning(msg.toString());
    }

    return err;
}

public static RuntimeException logFailure(TransactionFailedException err) {
    logger.warning("Transaction did not reach commit point");

    for (TransactionLogEvent msg : err.logs()) {
        logger.warning(msg.toString());
    }

    return err;
}
```

Of course, you should replace `logger.warning` with the logging system of choice for your application.

A failed transaction can involve dozens, even hundreds, of lines of logging, so it may be preferable to write failed transactions into a separate file.

You could also log a successful transaction like so:

```java
TransactionResult result = cluster.transactions().run((ctx) -> {
    // Your transaction logic
});

result.logs().forEach(message -> logger.info(message.toString()));
```

## [](#key-value-operations)Key-Value Operations

You can perform transactional database operations using familiar key-value CRUD methods:

* **C**reate - `insert()`
* **R**ead - `get()`
* **U**pdate - `replace()`
* **D**elete - `remove()`

> [!IMPORTANT]
> As mentioned [previously](#lambda-ops), make sure your application uses the transactional key-value operations inside the lambda — such as `ctx.insert()`, rather than `collection.insert()`.

### [](#insert)Insert

To insert a document within a transaction lambda, simply call `ctx.insert()`.

* Synchronous API
* Asynchronous API

```java
cluster.transactions().run((ctx) -> {
    String docId = "docId";

    ctx.insert(collection, docId, JsonObject.create());
});
```

```java
cluster.reactive().transactions().run((ctx) -> {
    return ctx.insert(collection.reactive(), "docId", JsonObject.create());
}).block();
```

### [](#get)Get

To retrieve a document from the database you can call `ctx.get()`.

```java
cluster.transactions().run((ctx) -> {
    TransactionGetResult doc = ctx.get(collection, "a-doc");
});
```

As you can see, `ctx.get()` will return a `TransactionGetResult` object, which is very similar to the `GetResult` you are used to.

If the application needs to ignore or take action on a document not existing, it can catch the exception:

```java
cluster.transactions().run((ctx) -> {
    try {
        TransactionGetResult doc = ctx.get(collection, "a-doc");
    }
    catch (DocumentNotFoundException err) {
        // The application can continue the transaction here if needed, or take alternative action
    }
});
```

Gets will "Read Your Own Writes", e.g. this will succeed:

```java
cluster.transactions().run((ctx) -> {
    String docId = "docId";

    ctx.insert(collection, docId, JsonObject.create());

    TransactionGetResult doc = ctx.get(collection, docId);
});
```

Of course, no other transaction will be able to read that inserted document, until this transaction reaches the commit point.

### [](#replace)Replace

Replacing a document requires a `ctx.get()` call first. This is necessary so the SDK can check that the document is not involved in another transaction, and take appropriate action if so.

* Synchronous API
* Asynchronous API

```java
cluster.transactions().run((ctx) -> {
    TransactionGetResult doc = ctx.get(collection, "doc-id");
    JsonObject content = doc.contentAs(JsonObject.class);
    content.put("transactions", "are awesome");
    ctx.replace(doc, content);
});
```

```java
cluster.reactive().transactions().run((ctx) -> {
    return ctx.get(collection.reactive(), "doc-id").flatMap(doc -> {
        JsonObject content = doc.contentAs(JsonObject.class);
        content.put("transactions", "are awesome");
        return ctx.replace(doc, content);
    });
});
```

### [](#remove)Remove

As with replaces, removing a document requires a `ctx.get()` call first.

* Synchronous API
* Asynchronous API

```java
cluster.transactions().run((ctx) -> {
    TransactionGetResult doc = ctx.get(collection, "doc-id");
    ctx.remove(doc);
});
```

```java
cluster.reactive().transactions().run((ctx) -> {
    return ctx.get(collection.reactive(), "anotherDoc")
            .flatMap(doc -> ctx.remove(doc));
});
```

> [!TIP]
> Reactor Mono<Void>
> 
> Some `ctx` methods, notably `ctx.remove()`, return `Mono<Void>`. There is a common "gotcha" with `Mono<Void>` in that it does not trigger a "next" reactive event - only a "completion" event. This means that some reactive operators chained afterwards, including the common `flatMap`, will not trigger. Generally, you will need to do `ctx.remove(…​).then(…​)` rather than `ctx.remove(…​).flatMap(…​)`.

## [](#sql-queries)SQL++ Queries

If you already use [SQL++ (formerly N1QL)](https://www.couchbase.com/products/n1ql), then its use in transactions is very similar. A query returns a `TransactionQueryResult` that is very similar to the `QueryResult` you are used to, and takes most of the same options.

> [!IMPORTANT]
> As mentioned [previously](#lambda-ops), make sure your application uses the transactional query operations inside the lambda — such as `ctx.query()`, rather than `cluster.query()` or `scope.query()`.

Here is an example of selecting some rows from the `travel-sample` bucket:

```java
Bucket travelSample = cluster.bucket("travel-sample");
Scope inventory = travelSample.scope("inventory");

cluster.transactions().run((ctx) -> {
    var qr = ctx.query(inventory, "SELECT * FROM hotel WHERE country = $1",
            TransactionQueryOptions.queryOptions()
                    .parameters(JsonArray.from("United States")));
    var rows = qr.rowsAs(JsonObject.class);
});
```

An example using a `Scope` for an `UPDATE`:

```java
String hotelChain = "http://marriot%";
String country = "United States";

cluster.transactions().run((ctx) -> {
    var qr = ctx.query(inventory, "UPDATE hotel SET price = $1 WHERE url LIKE $2 AND country = $3",
            TransactionQueryOptions.queryOptions()
                    .parameters(JsonArray.from(99.99, hotelChain, country)));
    assert(qr.metaData().metrics().get().mutationCount() == 1);
});
```

And an example combining `SELECT` and `UPDATE`.

```java
cluster.transactions().run((ctx) -> {
    // Find all hotels of the chain
    var qr = ctx.query(inventory, "SELECT reviews FROM hotel WHERE url LIKE $1 AND country = $2",
            TransactionQueryOptions.queryOptions()
                    .parameters(JsonArray.from(hotelChain, country)));

    // This function (not provided here) will use a trained machine learning model to provide a
    // suitable price based on recent customer reviews.
    double updatedPrice = priceFromRecentReviews(qr);

    // Set the price of all hotels in the chain
    ctx.query(inventory, "UPDATE hotel SET price = $1 WHERE url LIKE $2 AND country = $3",
            TransactionQueryOptions.queryOptions()
                    .parameters(JsonArray.from(updatedPrice, hotelChain, country)));
});
```

As you can see from the snippet above, it is possible to call regular Java methods from the lambda, permitting complex logic to be performed. Just remember that since the lambda may be called multiple times, so may the method.

Like key-value operations, queries support "Read Your Own Writes". This example shows inserting a document and then selecting it again:

```java
cluster.transactions().run((ctx) -> {
    ctx.query("INSERT INTO `default` VALUES ('doc', {'hello':'world'})");  (1)

    // Performing a 'Read Your Own Write'
    var st = "SELECT `default`.* FROM `default` WHERE META().id = 'doc'"; (2)
    var qr = ctx.query(st);
    assert(qr.metaData().metrics().get().resultCount() == 1);
});
```

| **1** | The inserted document is only staged at this point, as the transaction has not yet committed.Other transactions, and other non-transactional actors, will not be able to see this staged insert yet. |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | But the SELECT can, as we are reading a mutation staged inside the same transaction.                                                                                                                 |

### [](#query-options)Query Options

Query options can be provided via the `TransactionQueryOptions` object:

```java
cluster.transactions().run((ctx) -> {
    ctx.query("INSERT INTO `default` VALUES ('doc', {'hello':'world'})",
            TransactionQueryOptions.queryOptions().profile(QueryProfile.TIMINGS));
});
```

__Table 1\. Supported Transaction Query Options__
| Name                                  | Description                                                                      |
| ------------------------------------- | -------------------------------------------------------------------------------- |
| parameters(JsonArray)                 | Allows to set positional arguments for a parameterized query.                    |
| parameters(JsonObject)                | Allows you to set named arguments for a parameterized query.                     |
| scanConsistency(QueryScanConsistency) | Sets a different scan consistency for this query.                                |
| flexIndex(boolean)                    | Tells the query engine to use a flex index (utilizing the search service).       |
| serializer(JsonSerializer)            | Allows to use a different serializer for the decoding of the rows.               |
| clientContextId(String)               | Sets a context ID returned by the service for debugging purposes.                |
| scanWait(Duration)                    | Allows to specify a maximum scan wait time.                                      |
| scanCap(int)                          | Specifies a maximum cap on the query scan size.                                  |
| pipelineBatch(int)                    | Sets the batch size for the query pipeline.                                      |
| pipelineCap(int)                      | Sets the cap for the query pipeline.                                             |
| profile(QueryProfile)                 | Allows you to enable additional query profiling as part of the response.         |
| readonly(boolean)                     | Tells the client and server that this query is readonly.                         |
| adhoc(boolean)                        | If set to false will prepare the query and later execute the prepared statement. |
| raw(String, Object)                   | Escape hatch to add arguments that are not covered by these options.             |

## [](#mixing-key-value-and-sql)Mixing Key-Value and SQL++

Key-Value and SQL++ query operations can be freely intermixed, and will interact with each other as you would expect. In this example we insert a document with a key-value operation, and read it with a `SELECT` query.

```java
cluster.transactions().run((ctx) -> {
    ctx.insert(collection, "doc", JsonObject.create().put("hello", "world")); (1)

    // Performing a 'Read Your Own Write'
    var st = "SELECT `default`.* FROM `default` WHERE META().id = 'doc'"; (2)
    var qr = ctx.query(st);
    assert(qr.metaData().metrics().get().resultCount() == 1);
});
```

| **1** | The key-value insert operation is only staged, and so it is not visible to other transactions or non-transactional actors. |
| ----- | -------------------------------------------------------------------------------------------------------------------------- |
| **2** | But the SELECT can view it, as the insert was in the same transaction.                                                     |

> [!IMPORTANT]
> Query Mode
> 
> When a transaction executes a query statement, the transaction enters **query mode**, which means that the query is executed with the user’s query permissions. Any **key-value** operations which are executed by the transaction _after_ the query statement are _also_ executed with the user’s query permissions. These may or may not be different to the user’s data permissions; if they are different, you may get unexpected results.

## [](#concurrent-operations)Concurrent Operations

The reactive API allows operations to be performed concurrently inside a transaction, which can assist performance.

An example of performing parallel operations using the reactive API:

```java
List<String> docIds = Arrays.asList("doc1", "doc2", "doc3", "doc4", "doc5");
int concurrency = 100; // This many operations will be in-flight at once

var result = cluster.reactive().transactions().run((ctx) -> {
    return Flux.fromIterable(docIds)
            .parallel(concurrency)
            .runOn(Schedulers.boundedElastic())
            .concatMap(docId -> ctx.get(collection.reactive(), docId)
                    .flatMap(doc -> {
                        var content = doc.contentAsObject();
                        content.put("value", "updated");
                        return ctx.replace(doc, content);
                    }))
            .sequential()
            .then();
}).block();
```

> [!NOTE]
> Query Concurrency
> 
> Only one query statement will be performed by the Query service at a time. Non-blocking mechanisms can be used to perform multiple concurrent query statements, but this may result internally in some added network traffic due to retries, and is unlikely to provide any increased performance.

### [](#non-transactional-writes)Non-Transactional Writes

To ensure key-value performance is not compromised, and to avoid conflicting writes, applications should **never** perform non-transactional _writes_ concurrently with transactional ones, on the same document.

You can verify this when debugging your application by subscribing to the client’s event logger and checking for any `IllegalDocumentStateEvent` events. These events are raised when a non-transactional write has been detected and overridden.

```java
cluster.environment().eventBus().subscribe(event -> {
    if (event instanceof IllegalDocumentStateEvent) {
        // log this event for review
    }
});
```

The event contains the key of the document involved, to aid the application with debugging.

See [Concurrency with Non-Transactional Writes](../concept-docs/transactions.md#concurrency-with-non-transactional-writes) to learn more.

## [](#configuration)Configuration

The default configuration should be appropriate for most use-cases. If needed, transactions can be globally configured at the point of creating the `Cluster`. As usual with `Cluster` configuration, you can either explicitly create and manage the `ClusterEnvironment` yourself:

```java
ClusterEnvironment env = ClusterEnvironment.builder()
        .transactionsConfig(TransactionsConfig.durabilityLevel(DurabilityLevel.PERSIST_TO_MAJORITY)
                .cleanupConfig(TransactionsCleanupConfig.cleanupWindow(Duration.ofSeconds(30)))
                .queryConfig(TransactionsQueryConfig.scanConsistency(QueryScanConsistency.NOT_BOUNDED)))
        .build();

Cluster cluster = Cluster.connect("localhost", ClusterOptions.clusterOptions("username", "password")
        .environment(env));

// Use the cluster
// ...

// Shutdown
cluster.disconnect();
env.shutdown();
```

or alternatively use this lambda syntax, which leads to the `ClusterEnvironment` being owned and managed by the `Cluster`:

```java
Cluster cluster = Cluster.connect("localhost", ClusterOptions.clusterOptions("username", "password")
        .environment(env -> env.transactionsConfig(TransactionsConfig
                .durabilityLevel(DurabilityLevel.PERSIST_TO_MAJORITY)
                .cleanupConfig(TransactionsCleanupConfig
                        .cleanupWindow(Duration.ofSeconds(30)))
                .queryConfig(TransactionsQueryConfig
                        .scanConsistency(QueryScanConsistency.NOT_BOUNDED)))));
// Use the cluster
// ...

// Shutdown
cluster.disconnect();
```

The default configuration will perform all writes with the durability setting `Majority`, ensuring that each write is available in-memory on the majority of replicas before the transaction continues. There are two higher durability settings available that will additionally wait for all mutations to be written to physical storage on either the active or the majority of replicas, before continuing. This further increases safety, at a cost of additional latency.

> [!CAUTION]
> A level of `None` is present but its use is discouraged and unsupported. If durability is set to `None`, then ACID semantics are not guaranteed.

## [](#additional-resources)Additional Resources

* Learn more about [Distributed ACID Transactions](../../../server/current/learn/data/transactions.md).
* Learn more about [Distributed ACID Transactions with the Java SDK](../concept-docs/transactions.md).
* Check out the SDK [API Reference](https://docs.couchbase.com/sdk-api/couchbase-java-client/com/couchbase/client/java/transactions/package-summary.html).