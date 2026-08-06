---
title: Using Couchbase Transactions
description: A practical guide on using Couchbase Distributed ACID transactions,
  via the Node.js API.
editUrl: https://github.com/couchbase/docs-sdk-nodejs/edit/temp/4.7/modules/howtos/pages/distributed-acid-transactions-from-the-sdk.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:nodejs-sdk:howtos:distributed-acid-transactions-from-the-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/nodejs-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.html)

# Using Couchbase Transactions

> A practical guide on using Couchbase Distributed ACID transactions, via the Node.js API. 

This guide will show you examples of how to perform multi-document ACID (atomic, consistent, isolated, and durable) database transactions within your application, using the Couchbase Node.js SDK.

Refer to the [Transaction Concepts](../concept-docs/transactions.md) concept page for a high-level overview.

## [](#prerequisites)Prerequisites

* Couchbase Capella
* Couchbase Server

* Couchbase Capella account.
* You should know how to perform [key-value](kv-operations.md) or [query](n1ql-queries-with-sdk.md) operations with the SDK.
* Your application should have the relevant roles and permissions on the required buckets, scopes, and collections, to perform transactional operations. Refer to the [Organizations & Access](../../../cloud/organizations/organization-projects-overview.md) page for more details.
* If your application is using [extended attributes (XATTRs)](../concept-docs/xattr.md), you should avoid using the XATTR field `txn` — this is reserved for Couchbase use.

* Couchbase Server (6.6.1 or above).
* You should know how to perform [key-value](kv-operations.md) or [query](n1ql-queries-with-sdk.md) operations with the SDK.
* Your application should have the relevant roles and permissions on the required buckets, scopes, and collections, to perform transactional operations. Refer to the [Roles](../../../server/current/learn/security/roles.md) page for more details.
* If your application is using [extended attributes (XATTRs)](../concept-docs/xattr.md), you should avoid using the XATTR field `txn` — this is reserved for Couchbase use.
* NTP should be configured so nodes of the Couchbase cluster are in sync with time.

> [!CAUTION]
> Single Node Cluster
> 
> When using a single node cluster (for example, during development), the default number of replicas for a newly created bucket is **1**. If left at this default, all key-value writes performed with durability will fail with a `DurabilityImpossibleError`. In turn, this will cause all transactions (which perform all key-value writes durably) to fail. This setting can be changed via:
> 
> * [Capella UI](../../../cloud/clusters/data-service/manage-buckets.md#add-bucket)
> * [Couchbase Server UI](../../../server/current/manage/manage-buckets/create-bucket.md#couchbase-bucket-settings)
> * [Command Line](../../../server/current/cli/cbcli/couchbase-cli-bucket-create.md#options)
> 
> If the bucket already exists, then the server needs to be rebalanced for the setting to take effect.

Simply `npm install` the most recent version of the SDK. You may, on occasion, need to import some enumerations for particular settings, but in basic cases nothing is needed.

## [](#creating-a-transaction)Creating a Transaction

To create a transaction, an application must supply its logic inside an `arrow function`, including any conditional logic required. Once the arrow function has successfully run to conclusion, the transaction will be automatically committed. If at any point an error occurs, the transaction will rollback and the arrow function may run again.

```typescript
Unresolved include directive in modules/howtos/pages/distributed-acid-transactions-from-the-sdk.adoc - include::example$transactions-example.ts[]
```

The transaction arrow function gets passed a `TransactionAttemptContext` object — generally referred to as `ctx` in these examples. Since the arrow function could be rerun multiple times, it is important that it does not contain any side effects. In particular, you should never perform regular operations on a `Collection`, such as `collection.insert()`, inside the arrow function. Such operations may be performed multiple times, and will not be performed transactionally. Instead, you should perform these operations through the `ctx` object, e.g. `ctx.insert()`.

The result of a transaction is represented by a `TransactionResult` object, which can be used to expose debugging and logging information to help track what happened during a transaction.

In the event that a transaction fails, your application could run into the following errors:

* `TransactionCommitAmbiguousError`
* `TransactionFailedError`

Refer to [Error Handling](../concept-docs/transactions-error-handling.md#transaction%5Ferrors) for more details on these.

### [](#logging)Logging

To aid troubleshooting, raise the log level on the SDK.

Please see the [Node.js SDK logging documentation](collecting-information-and-logging.md) for details.

## [](#key-value-operations)Key-Value Operations

You can perform transactional database operations using familiar key-value CRUD methods:

* **C**reate - `insert()`
* **R**ead - `get()`
* **U**pdate - `replace()`
* **D**elete - `remove()`

> [!IMPORTANT]
> As mentioned [previously](#lambda-ops), make sure your application uses the transactional key-value operations inside the arrow function — such as `ctx.insert()`, rather than `collection.insert()`.

### [](#insert)Insert

To insert a document within a transaction arrow function, simply call `ctx.insert()`.

```typescript
Unresolved include directive in modules/howtos/pages/distributed-acid-transactions-from-the-sdk.adoc - include::example$transactions-example.ts[]
```

### [](#get)Get

To retrieve a document from the database you can call `ctx.get()`.

```typescript
Unresolved include directive in modules/howtos/pages/distributed-acid-transactions-from-the-sdk.adoc - include::example$transactions-example.ts[]
```

As you can see, `ctx.get()` will return a `TransactionGetResult` object, which is very similar to the `GetResult` you are used to.

Gets will "Read Your Own Writes", e.g. this will succeed:

```typescript
Unresolved include directive in modules/howtos/pages/distributed-acid-transactions-from-the-sdk.adoc - include::example$transactions-example.ts[]
```

Of course, no other transaction will be able to read that inserted document, until this transaction reaches the commit point.

### [](#replace)Replace

Replacing a document requires a `ctx.get()` call first. This is necessary so the SDK can check that the document is not involved in another transaction, and take appropriate action if so.

```typescript
Unresolved include directive in modules/howtos/pages/distributed-acid-transactions-from-the-sdk.adoc - include::example$transactions-example.ts[]
```

### [](#remove)Remove

As with replaces, removing a document requires a `ctx.get()` call first.

```typescript
Unresolved include directive in modules/howtos/pages/distributed-acid-transactions-from-the-sdk.adoc - include::example$transactions-example.ts[]
```

## [](#sql-queries)SQL++ Queries

If you already use [SQL++ (formerly N1QL)](https://www.couchbase.com/products/n1ql), then its use in transactions is very similar. A query returns a `TransactionQueryResult` that is very similar to the `QueryResult` you are used to, and takes most of the same options.

> [!IMPORTANT]
> As mentioned [previously](#lambda-ops), make sure your application uses the transactional query operations inside the arrow function — such as `ctx.query()`, rather than `cluster.query()` or `scope.query()`.

Here is an example of selecting some rows from the `travel-sample` bucket:

```typescript
Unresolved include directive in modules/howtos/pages/distributed-acid-transactions-from-the-sdk.adoc - include::example$transactions-example.ts[]
```

An example using a `Scope` for an `UPDATE`:

```typescript
Unresolved include directive in modules/howtos/pages/distributed-acid-transactions-from-the-sdk.adoc - include::example$transactions-example.ts[]
```

And an example combining `SELECT` and an `UPDATE`.

```typescript
Unresolved include directive in modules/howtos/pages/distributed-acid-transactions-from-the-sdk.adoc - include::example$transactions-example.ts[]
```

As you can see from the snippet above, it is possible to call regular Node.js methods from the arrow function, permitting complex logic to be performed. Just remember that since the arrow function may be called multiple times, so may the method.

Like key-value operations, queries support "Read Your Own Writes". This example shows inserting a document and then selecting it again:

```typescript
Unresolved include directive in modules/howtos/pages/distributed-acid-transactions-from-the-sdk.adoc - include::example$transactions-example.ts[]
```

| **1** | The inserted document is only staged at this point. as the transaction has not yet committed.Other transactions, and other non-transactional actors, will not be able to see this staged insert yet. |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | But the SELECT can, as we are reading a mutation staged inside the same transaction.                                                                                                                 |

### [](#query-options)Query Options

Query options can be provided via `TransactionQueryOptions`, which provides a subset of the options in the Node.js SDK's `QueryOptions`.

```typescript
Unresolved include directive in modules/howtos/pages/distributed-acid-transactions-from-the-sdk.adoc - include::example$transactions-example.ts[]
```

__Table 1\. Supported Transaction Query Options__
| Name                                  | Description                                                                      |
| ------------------------------------- | -------------------------------------------------------------------------------- |
| parameters(any\[\])                   | Allows to set positional arguments for a parameterized query.                    |
| parameters({ \[key: string\]: any })  | Allows you to set named arguments for a parameterized query.                     |
| scanConsistency(QueryScanConsistency) | Sets a different scan consistency for this query.                                |
| clientContextId(string)               | Sets a context ID returned by the service for debugging purposes.                |
| scanWait(number)                      | Allows to specify a maximum scan wait time.                                      |
| scanCap(number)                       | Specifies a maximum cap on the query scan size.                                  |
| pipelineBatch(number)                 | Sets the batch size for the query pipeline.                                      |
| pipelineCap(number)                   | Sets the cap for the query pipeline.                                             |
| profile(QueryProfileMode)             | Allows you to enable additional query profiling as part of the response.         |
| readOnly(boolean)                     | Tells the client and server that this query is readonly.                         |
| adhoc(boolean)                        | If set to false will prepare the query and later execute the prepared statement. |
| raw({ \[key: string\]: any })         | Escape hatch to add arguments that are not covered by these options.             |

## [](#mixing-key-value-and-sql)Mixing Key-Value and SQL++

Key-Value and SQL++ query operations can be freely intermixed, and will interact with each other as you would expect. In this example we insert a document with a key-value operation, and read it with a `SELECT` query.

```typescript
Unresolved include directive in modules/howtos/pages/distributed-acid-transactions-from-the-sdk.adoc - include::example$transactions-example.ts[]
```

| **1** | The key-value insert operation is only staged, and so it is not visible to other transactions or non-transactional actors. |
| ----- | -------------------------------------------------------------------------------------------------------------------------- |
| **2** | But the SELECT can view it, as the insert was in the same transaction.                                                     |

> [!IMPORTANT]
> Query Mode
> 
> When a transaction executes a query statement, the transaction enters **query mode**, which means that the query is executed with the user's query permissions. Any **key-value** operations which are executed by the transaction _after_ the query statement are _also_ executed with the user's query permissions. These may or may not be different to the user's data permissions; if they are different, you may get unexpected results.

## [](#concurrent-operations)Concurrent Operations

The API allows operations to be performed concurrently inside a transaction, which can assist performance. There are two rules the application needs to follow:

* The first mutation must be performed alone, in serial. This is because the first mutation also triggers the creation of metadata for the transaction.
* All concurrent operations must be allowed to complete fully, so the transaction can track which operations need to be rolled back in the event of failure. This means the application must 'swallow' the error, but record that an error occurred, and then at the end of the concurrent operations, if an error occurred, throw an error to cause the transaction to retry.

> [!NOTE]
> Query Concurrency
> 
> Only one query statement will be performed by the Query service at a time. Non-blocking mechanisms can be used to perform multiple concurrent query statements, but this may result internally in some added network traffic due to retries, and is unlikely to provide any increased performance.

### [](#non-transactional-writes)Non-Transactional Writes

To ensure key-value performance is not compromised, and to avoid conflicting writes, applications should **never** perform non-transactional _writes_ concurrently with transactional ones, on the same document.

See [Concurrency with Non-Transactional Writes](../concept-docs/transactions.md#concurrency-with-non-transactional-writes) to learn more.

## [](#configuration)Configuration

The default configuration should be appropriate for most use-cases. Transactions can optionally be globally configured when configuring the `Cluster`. For example, if you want to change the level of durability which must be attained, this can be configured as part of the connect options:

```typescript
Unresolved include directive in modules/howtos/pages/distributed-acid-transactions-from-the-sdk.adoc - include::example$transactions-example.ts[]
```

The default configuration will perform all writes with the durability setting `Majority`, ensuring that each write is available in-memory on the majority of replicas before the transaction continues. There are two higher durability settings available that will additionally wait for all mutations to be written to physical storage on either the active or the majority of replicas, before continuing. This further increases safety, at a cost of additional latency.

> [!CAUTION]
> A level of `None` is present but its use is discouraged and unsupported. If durability is set to `None`, then ACID semantics are not guaranteed.

## [](#additional-resources)Additional Resources

* Learn more about [Distributed ACID Transactions](../concept-docs/transactions.md).
* Check out the SDK [API Reference](https://docs.couchbase.com/sdk-api/couchbase-node-client/index.html).