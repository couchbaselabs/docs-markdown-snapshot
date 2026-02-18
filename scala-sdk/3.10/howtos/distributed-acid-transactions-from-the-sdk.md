---
title: Using Couchbase Transactions
description: A practical guide on using Couchbase Distributed ACID transactions,
  via the Scala SDK.
editUrl: https://github.com/couchbase/docs-sdk-scala/edit/release/3.10/modules/howtos/pages/distributed-acid-transactions-from-the-sdk.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/scala-sdk/3.10/howtos/distributed-acid-transactions-from-the-sdk.html)

# Using Couchbase Transactions

> A practical guide on using Couchbase Distributed ACID transactions, via the Scala SDK. 

This guide will show you examples of how to perform multi-document ACID (atomic, consistent, isolated, and durable) database transactions within your application, using the Couchbase Scala SDK.

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

Transactions are accessed via the `Cluster` object. By invoking `Cluster.transactions`, we can access the `Transactions` object and `run` a transaction.

```scala
val inventory = cluster.bucket("travel-sample").scope("inventory")

val result = cluster.transactions.run((ctx: TransactionAttemptContext) => {

  // Inserting a doc:
  ctx.insert(collection, "doc-a", JsonObject.create).get

  // Getting documents:
  val docA = ctx.get(collection, "doc-a").get

  // Replacing a doc:
  val docB = ctx.get(collection, "doc-b").get
  val content = docB.contentAs[JsonObject].get
  content.put("transactions", "are awesome")
  ctx.replace(docB, content).get

  // Removing a doc:
  val docC = ctx.get(collection, "doc-c").get
  ctx.remove(docC).get

  // Performing a SELECT N1QL query against a scope:
  val qr = ctx.query(inventory, "SELECT * FROM hotel WHERE country = $1",
    TransactionQueryOptions().parameters(Positional("United Kingdom"))).get

  val rows = qr.rowsAs[JsonObject].get

  // Performing an UPDATE N1QL query on multiple documents, in the `inventory` scope:
  ctx.query(inventory, "UPDATE route SET airlineid = $1 WHERE airline = $2",
    TransactionQueryOptions().parameters(Positional("airline_137", "AF"))).get

  Success()
})

handleTransactionResult(result).get
```

The asynchronous mode allows you to build your application in a reactive style, which can help you scale with excellent efficiency.

Transactions are accessed via the `ReactiveCluster` object. By invoking `Cluster.reactive().transactions()`, we can access the `ReactiveTransactions` object and `run` the lambda.

```scala
val inventory = cluster.bucket("travel-sample").scope("inventory").reactive
val result = cluster.reactive.transactions.run((ctx: ReactiveTransactionAttemptContext) => {

  // Inserting a doc:
  ctx.insert(collection.reactive, "doc-a", JsonObject.create)

    // Getting documents:
    .`then`(ctx.get(collection.reactive, "doc-b")

      // Replacing a doc:
      .flatMap(docB => {
        val content = docB.contentAs[JsonObject].get
        content.put("transactions", "are awesome")
        ctx.replace(docB, content)
      }))

    // Removing a doc:
    .`then`(ctx.get(collection.reactive, "doc-c")
      .flatMap(doc => ctx.remove(doc)))

    // Performing a SELECT N1QL query against a scope:
    .`then`(ctx.query(inventory, "SELECT * FROM hotel WHERE country = $1",
      TransactionQueryOptions().parameters(Positional("United Kingdom")))
      .flatMapMany(queryResult => SFlux.fromIterable(queryResult.rowsAs[JsonObject].get))
      .doOnNext(row => {
        // The application would do something with the rows here.
      })
      .collectSeq())

    // Performing an UPDATE N1QL query on multiple documents, in the `inventory` scope:
    .`then`(ctx.query(inventory, "UPDATE route SET airlineid = $1 WHERE airline = $2",
      TransactionQueryOptions().parameters(Positional("airline_137", "AF"))))

    .`then`()

}).block()
```

The transaction lambda gets passed a `TransactionAttemptContext` object — generally referred to as `ctx` in these examples. Since the lambda could be rerun multiple times, it is important that it does not contain any side effects. In particular, you should never perform regular operations on a `Collection`, such as `collection.insert()`, inside the lambda. Such operations may be performed multiple times, and will not be performed transactionally. Instead, you should perform these operations through the `ctx` object, e.g. `ctx.insert()`.

The result of a transaction is represented by a `TransactionResult` object, which can be used to expose debugging and logging information to help track what happened during a transaction.

In the event that a transaction fails, your application could run into the following errors:

* `TransactionCommitAmbiguousException`
* `TransactionFailedException`

Refer to [Error Handling](../concept-docs/transactions-error-handling.md#transaction%5Ferrors) for more details on these.

### [](#functional-error-handling)Functional Error Handling

As with everything in the Scala SDK, the transactions synchronous API presents a functional error handlling interface. The transaction itself, and each operation inside it, will return a `Try` containing either a `Success` or a `Failure` object.

To simplify the synchronous API examples, most of them will call `.get` on this `Try`, which will throw if it contains a `Failure`. Users should feel free to use this style, or pattern matching, for-comprehensions, or `.flatMap()`, as they prefer.

### [](#logging)Logging

To aid troubleshooting, each transaction maintains a list of log entries, which can be logged on failure like this:

* Synchronous API
* Asynchronous API

```scala

val result = cluster.transactions.run((ctx: TransactionAttemptContext) => {
  Success()
})

result match {
  case Failure(err: TransactionFailedException) =>
    logger.warning("Transaction did not reach commit point")
    err.logs.foreach(msg => logger.warning(msg.toString))

  case Failure(err: TransactionCommitAmbiguousException) =>
    logger.warning("Transaction possibly reached the commit point")
    err.logs.foreach(msg => logger.warning(msg.toString))

  case Success(_) =>
    logger.info("Transaction succeeded!")
}
```

```scala
cluster.reactive.transactions.run((ctx: ReactiveTransactionAttemptContext) => {
  SMono.just(())
}).doOnError {
  case err: TransactionFailedException =>
    logger.warning("Transaction did not reach commit point")
    err.logs.foreach(msg => logger.warning(msg.toString))

  case err: TransactionCommitAmbiguousException =>
    logger.warning("Transaction possibly reached the commit point")
    err.logs.foreach(msg => logger.warning(msg.toString))

  case err =>
  // This will not happen as all errors derive from TransactionFailedException
}.block()
```

A failed transaction can involve dozens, even hundreds, of lines of logging, so it may be preferable to write failed transactions into a separate file.

## [](#key-value-operations)Key-Value Operations

You can perform transactional database operations using familiar key-value CRUD methods:

* **C**reate - `ctx.insert()`
* **R**ead - `ctx.get()`
* **U**pdate - `ctx.replace()`
* **D**elete - `ctx.remove()`

> [!IMPORTANT]
> As mentioned [previously](#lambda-ops), make sure your application uses the transactional key-value operations inside the lambda — such as `ctx.insert()`, rather than `collection.insert()`.

### [](#insert)Insert

To insert a document within a transaction lambda, simply call `ctx.insert()`.

* Synchronous API
* Asynchronous API

```scala
val result = cluster.transactions.run((ctx: TransactionAttemptContext) => {
  ctx.insert(collection, "docId", JsonObject.create).get
  Success()
}).get
```

```scala
cluster.reactive.transactions.run((ctx: ReactiveTransactionAttemptContext) => {
  ctx.insert(collection.reactive, "docId", JsonObject.create).`then`()
}).block()
```

### [](#get)Get

To retrieve a document from the database you can call `ctx.get()`.

```scala
cluster.transactions.run((ctx: TransactionAttemptContext) => {
  val doc = ctx.get(collection, "a-doc").get
  Success()
}).get
```

`ctx.get()` will return a `TransactionGetResult` object, which is very similar to the `GetResult` you are used to.

If the application needs to ignore or take action on a document not existing, it can handle the failure:

```scala
cluster.transactions.run((ctx: TransactionAttemptContext) => {
  ctx.get(collection, "a-doc") match {
    case Failure(_: DocumentNotFoundException) =>
      // By not propagating this failure, the application is allowing the transaction to continue.
    case _ =>
  }
  Success()
}).get
```

Gets will "Read Your Own Writes", e.g. this will succeed:

```scala
cluster.transactions.run((ctx: TransactionAttemptContext) => {
  val docId = "docId"
  ctx.insert(collection, docId, JsonObject.create).get
  val doc = ctx.get(collection, docId).get
  Success()
}).get
```

Of course, no other transaction will be able to read that inserted document, until this transaction reaches the commit point.

### [](#replace)Replace

Replacing a document requires a `ctx.get()` call first. This is necessary so the SDK can check that the document is not involved in another transaction, and take appropriate action if so.

* Synchronous API
* Asynchronous API

```scala
cluster.transactions.run((ctx: TransactionAttemptContext) => {
  val doc = ctx.get(collection, "doc-id").get
  val content = doc.contentAs[JsonObject].get
  content.put("transactions", "are awesome")
  ctx.replace(doc, content).get
  Success()
}).get
```

```scala
cluster.reactive.transactions.run((ctx: ReactiveTransactionAttemptContext) => {
  ctx.get(collection.reactive, "doc-id")
    .flatMap(doc => {
      val content = doc.contentAs[JsonObject].get
      content.put("transactions", "are awesome")
      ctx.replace(doc, content)
    })
    .`then`()
}).block()
```

### [](#remove)Remove

As with replaces, removing a document requires a `ctx.get()` call first.

* Synchronous API
* Asynchronous API

```scala
cluster.transactions.run((ctx: TransactionAttemptContext) => {
  val doc = ctx.get(collection, "doc-id").get
  ctx.remove(doc).get
  Success()
}).get
```

```scala
cluster.reactive.transactions.run((ctx: ReactiveTransactionAttemptContext) => {
  ctx.get(collection.reactive, "anotherDoc")
    .flatMap(doc => ctx.remove(doc))
}).block()
```

> [!TIP]
> Reactor Mono<Void>
> 
> Some `ctx` methods, notably `ctx.remove()`, return `SMono[Unit]`. There is a common "gotcha" with `SMono[Unit]` in that it does not trigger a "next" reactive event - only a "completion" event. This means that some reactive operators chained afterwards, including the common `flatMap`, will not trigger. Generally, you will want to do `` ctx.remove(…​).`then ``(…​)\` rather than `ctx.remove(…​).flatMap(…​)`.

## [](#sql-queries)SQL++ Queries

If you already use [SQL++ (formerly N1QL)](https://www.couchbase.com/products/n1ql), then its use in transactions is very similar. A query returns a `TransactionQueryResult` that is very similar to the `QueryResult` you are used to, and takes most of the same options.

> [!IMPORTANT]
> As mentioned [previously](#lambda-ops), make sure your application uses the transactional query operations inside the lambda — such as `ctx.query()`, rather than `cluster.query()` or `scope.query()`.

Here is an example of selecting some rows from the `travel-sample` bucket:

```scala
val travelSample = cluster.bucket("travel-sample")
val inventory = travelSample.scope("inventory")

cluster.transactions.run((ctx: TransactionAttemptContext) => {
  val qr = ctx.query(inventory, "SELECT * FROM hotel WHERE country = $1",
    TransactionQueryOptions().parameters(Positional("United States"))).get
  val rows = qr.rowsAs[JsonObject].get
  Success()
}).get
```

An example using a `Scope` for an `UPDATE`:

```scala
val hotelChain = "http://marriot%"
val country = "United States"

cluster.transactions.run((ctx: TransactionAttemptContext) => {
  val qr = ctx.query(inventory, "UPDATE hotel SET price = $1 WHERE url LIKE $2 AND country = $3",
    TransactionQueryOptions().parameters(Positional((99.99, hotelChain, country)))).get
  assert(qr.metaData.metrics.get.mutationCount == 1)
  Success()
}).get
```

And an example combining `SELECT` and `UPDATE`.

```scala
cluster.transactions.run((ctx: TransactionAttemptContext) => {

  // Find all hotels of the chain
  val qr = ctx.query(inventory, "SELECT reviews FROM hotel WHERE url LIKE $1 AND country = $2",
    TransactionQueryOptions().parameters(Positional(hotelChain, country))).get

  // This function (not provided here) will use a trained machine learning model to provide a
  // suitable price based on recent customer reviews.
  val updatedPrice = priceFromRecentReviews(qr)

  // Set the price of all hotels in the chain
  ctx.query(inventory, "UPDATE hotel SET price = $1 WHERE url LIKE $2 AND country = $3",
    TransactionQueryOptions().parameters(Positional(updatedPrice, hotelChain, country))).get

  Success()
}).get
```

As you can see from the snippet above, it is possible to call regular Scala methods from the lambda, permitting complex logic to be performed. Just remember that since the lambda may be called multiple times, so may the method.

Like key-value operations, queries support "Read Your Own Writes". This example shows inserting a document and then selecting it again:

```scala
cluster.transactions.run((ctx: TransactionAttemptContext) => {
  ctx.query("INSERT INTO `default` VALUES ('doc', {'hello':'world'})").get (1)

  // Performing a 'Read Your Own Write'
  val st = "SELECT `default`.* FROM `default` WHERE META().id = 'doc'" (2)

  val qr = ctx.query(st).get
  assert(qr.metaData.metrics.get.resultCount == 1)

  Success()
}).get
```

| **1** | The inserted document is only staged at this point, as the transaction has not yet committed.Other transactions, and other non-transactional actors, will not be able to see this staged insert yet. |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | But the SELECT can, as we are reading a mutation staged inside the same transaction.                                                                                                                 |

### [](#query-options)Query Options

Query options can be provided via the `TransactionQueryOptions` object:

```scala
cluster.transactions.run((ctx: TransactionAttemptContext) => {
  ctx.query("INSERT INTO `default` VALUES ('doc', {'hello':'world'})",
    TransactionQueryOptions().profile(QueryProfile.Timings)).get
  Success()
}).get
```

__Table 1\. Supported Transaction Query Options__
| Name                                  | Description                                                                      |
| ------------------------------------- | -------------------------------------------------------------------------------- |
| parameters(Positional)                | Allows to set positional arguments for a parameterized query.                    |
| parameters(Named)                     | Allows you to set named arguments for a parameterized query.                     |
| scanConsistency(QueryScanConsistency) | Sets a different scan consistency for this query.                                |
| flexIndex(boolean)                    | Tells the query engine to use a flex index (utilizing the search service).       |
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

```scala
cluster.transactions.run((ctx: TransactionAttemptContext) => {
  ctx.insert(collection, "doc", JsonObject.create.put("hello", "world")).get (1)

  // Performing a 'Read Your Own Write'
  val st = "SELECT `default`.* FROM `default` WHERE META().id = 'doc'" (2)

  val qr = ctx.query(st).get
  assert(qr.metaData.metrics.get.resultCount == 1)

  Success()
}).get
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

```scala
val docIds = Seq("doc1", "doc2", "doc3", "doc4", "doc5")
val concurrency = 100 // This many operations will be in-flight at once

cluster.reactive.transactions.run((ctx: ReactiveTransactionAttemptContext) => {
  SFlux.fromIterable(docIds)
    .parallel(concurrency)
    .runOn(Schedulers.boundedElastic)
    .map(docId =>
      ctx.get(collection.reactive, docId)
        .flatMap(doc => {
          val content = doc.contentAs[JsonObject].get
          content.put("value", "updated")
          ctx.replace(doc, content)
        }))
    .sequential()
    .`then`
}).block()
```

> [!NOTE]
> Query Concurrency
> 
> Only one query statement will be performed by the Query service at a time. Non-blocking mechanisms can be used to perform multiple concurrent query statements, but this may result internally in some added network traffic due to retries, and is unlikely to provide any increased performance.

### [](#non-transactional-writes)Non-Transactional Writes

To ensure key-value performance is not compromised, and to avoid conflicting writes, applications should **never** perform non-transactional _writes_ concurrently with transactional ones, on the same document.

You can verify this when debugging your application by subscribing to the client’s event logger and checking for any `IllegalDocumentStateEvent` events. These events are raised when a non-transactional write has been detected and overridden. Note that this is on a best-effort basis and detection of every such case cannot be guaranteed.

```scala
Unresolved include directive in modules/howtos/pages/distributed-acid-transactions-from-the-sdk.adoc - include::howtos:example$TransactionsExample.scala[]
```

The event contains the key of the document involved, to aid the application with debugging.

See [Concurrency with Non-Transactional Writes](../concept-docs/transactions.md#concurrency-with-non-transactional-writes) to learn more.

## [](#configuration)Configuration

The default configuration should be appropriate for most use-cases. If needed, transactions can be globally configured at the point of creating the `Cluster`:

```scala

val env = ClusterEnvironment.builder
  .transactionsConfig(TransactionsConfig()
    .durabilityLevel(DurabilityLevel.PERSIST_TO_MAJORITY)
    .cleanupConfig(TransactionsCleanupConfig()
      .cleanupWindow(30.seconds)))
  .build.get
val cluster = Cluster.connect("hostname",
  ClusterOptions(PasswordAuthenticator.create("username", "password"), Some(env))).get

// Use the cluster
// ...

// Shutdown
cluster.disconnect()
env.shutdown()
```

The default configuration will perform all writes with the durability setting `Majority`, ensuring that each write is available in-memory on the majority of replicas before the transaction continues. There are two higher durability settings available that will additionally wait for all mutations to be written to physical storage on either the active or the majority of replicas, before continuing. This further increases safety, at a cost of additional latency.

> [!CAUTION]
> A level of `None` is present but its use is discouraged and unsupported. If durability is set to `None`, then ACID semantics are not guaranteed.

## [](#additional-resources)Additional Resources

* Learn more about [Distributed ACID Transactions](../concept-docs/transactions.md).
* Check out the SDK [API Reference](https://docs.couchbase.com/sdk-api/couchbase-scala-client/com/couchbase/client/scala/transactions/package-summary.html).