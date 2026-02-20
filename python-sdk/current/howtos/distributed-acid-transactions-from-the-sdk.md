---
title: Using Couchbase Transactions
description: A practical guide to using Couchbase distributed ACID transactions
  with the Python SDK.
editUrl: https://github.com/couchbase/docs-sdk-python/edit/temp/4.5/modules/howtos/pages/distributed-acid-transactions-from-the-sdk.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:python-sdk:howtos:distributed-acid-transactions-from-the-sdk.adoc[]
---

[View original HTML](/python-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.html)

# Using Couchbase Transactions

> A practical guide to using Couchbase distributed ACID transactions with the Python SDK. 

This guide will show you examples of how to perform multi-document ACID (atomic, consistent, isolated, and durable) database transactions within your application, using the Couchbase Python SDK.

Refer to the [Transaction Concepts](../concept-docs/transactions.md) page for a high-level overview.

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
> When using a single node cluster (for example, during development), the default number of replicas for a newly created bucket is **1**. If left at this default, all key-value writes performed with durability will fail with a `DurabilityImpossibleException`. In turn, this will cause all transactions (which perform all key-value writes durably) to fail. This setting can be changed via:
> 
> * [Capella UI](../../../cloud/clusters/data-service/manage-buckets.md#add-bucket)
> * [Couchbase Server UI](../../../server/current/manage/manage-buckets/create-bucket.md#couchbase-bucket-settings)
> * [Command Line](../../../server/current/cli/cbcli/couchbase-cli-bucket-create.md#options)
> 
> If the bucket already exists, then the server needs to be rebalanced for the setting to take effect.

Simply `pip install` the most recent version of the SDK. You may, on occasion, need to import some enumerations for particular settings, but in basic cases nothing is needed.

## [](#creating-a-transaction)Creating a Transaction

To create a transaction, an application must supply its logic inside a `lambda`, including any conditional logic required. Once the lambda has successfully run to conclusion, the transaction will be automatically committed. If at any point an error occurs, the transaction will rollback and the lambda may run again.

```python
inventory = cluster.bucket("travel-sample").scope("inventory")

def txn_example(ctx):
    # insert doc
    ctx.insert(collection, 'doc-a', {})

    # get a doc
    doc_a = ctx.get(collection, 'doc-a')

    # replace a doc
    doc_b = ctx.get(collection, 'doc-b')
    content = doc_b.content_as[dict]
    content['transactions'] = 'are awesome!'
    ctx.replace(doc_b, content)

    # remove a doc
    doc_c = ctx.get(collection, 'doc-c')
    ctx.remove(doc_c)

    query_str = 'SELECT * FROM `travel-sample`.inventory.hotel WHERE country = "United Kingdom" LIMIT 2;'
    res = ctx.query(query_str)
    rows = [r for r in res.rows()]

    query_str = 'UPDATE `travel-sample`.inventory.route SET airlineid = "airline_137" WHERE airline = "AF"'
    res = ctx.query(query_str)
    rows = [r for r in res.rows()]

try:
    cluster.transactions.run(txn_example)
except TransactionFailed as ex:
    print(f'Transaction did not reach commit point.  Error: {ex}')
except TransactionCommitAmbiguous as ex:
    print(f'Transaction possibly committed.  Error: {ex}')
```

The transaction lambda gets passed a `AttemptContext` object — generally referred to as `ctx` in these examples. Since the lambda could be rerun multiple times, it is important that it does not contain any side effects. In particular, you should never perform regular operations on a `Collection`, such as `collection.insert()`, inside the lambda. Such operations may be performed multiple times, and will not be performed transactionally. Instead, you should perform these operations through the `ctx` object, e.g. `ctx.insert()`.

The result of a transaction is represented by a `TransactionResult` object, which can be used to expose debugging and logging information to help track what happened during a transaction.

In the event that a transaction fails, your application could run into the following errors:

* `TransactionCommitAmbiguous`
* `TransactionFailed`

Refer to [Error Handling](../concept-docs/transactions-error-handling.md#transaction%5Ferrors) for more details on these.

### [](#logging)Logging

To aid troubleshooting, raise the log level on the SDK.

Please see the [Python SDK logging documentation](collecting-information-and-logging.md) for details.

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

```python
def txn_logic(ctx):
    ctx.insert(collection, key, content)

cluster.transactions.run(txn_logic)
```

### [](#get)Get

To retrieve a document from the database you can call `ctx.get()`.

```python
def txn_logic(ctx):
    doc = ctx.get(collection, key)
    doc_content = doc.content_as[dict]

cluster.transactions.run(txn_logic)
```

`ctx.get()` will return a `TransactionGetResult` object, which is very similar to the `GetResult` you are used to.

Gets will "Read Your Own Writes", e.g. this will succeed:

```python
def txn_logic(ctx):
    ctx.insert(collection, key, content)
    doc = ctx.get(collection, key)
    doc_content = doc.content_as[dict]

cluster.transactions.run(txn_logic)
```

Of course, no other transaction will be able to read that inserted document, until this transaction reaches the commit point.

### [](#replace)Replace

Replacing a document requires a `ctx.get()` call first. This is necessary so the SDK can check that the document is not involved in another transaction, and take appropriate action if so.

```python
def txn_logic(ctx):
    doc = ctx.get(collection, key)
    content = doc.content_as[dict]
    content['transactions'] = 'are awesome!'
    ctx.replace(doc, content)

cluster.transactions.run(txn_logic)
```

### [](#remove)Remove

As with replaces, removing a document requires a `ctx.get()` call first.

```python
def txn_logic(ctx):
    doc = ctx.get(collection, key)
    ctx.remove(doc)

cluster.transactions.run(txn_logic)
```

## [](#sql-queries)SQL++ Queries

If you already use [SQL++ (formerly N1QL)](https://www.couchbase.com/products/n1ql), then its use in transactions is very similar. A query returns a `TransactionQueryResult` that is very similar to the `QueryResult` you are used to, and takes most of the same options.

> [!IMPORTANT]
> As mentioned [previously](#lambda-ops), make sure your application uses the transactional query operations inside the lambda — such as `ctx.query()`, rather than `cluster.query()` or `scope.query()`.

Here is an example of selecting some rows from the `travel-sample` bucket:

```python
def txn_select(ctx):
    query_str = 'SELECT * FROM `travel-sample`.inventory.hotel WHERE country = "United Kingdom" LIMIT 2;'
    res = ctx.query(query_str)
    rows = [r for r in res.rows()]

cluster.transactions.run(txn_select)
```

And an example combining `SELECT` and an `UPDATE`.

```python
def txn_complex(ctx):
    # find all hotels of the chain
    res = ctx.query(
        'SELECT reviews FROM `travel-sample`.inventory.hotel WHERE url = "http://marriot%" AND country = "United States"')

    # This function (not provided here) will use a trained machine learning model to provide a
    # suitable price based on recent customer reviews.
    updated_price = price_from_recent_reviews(res)

    # Set the price of all hotels in the chain
    query_str = f'UPDATE `travel-sample`.inventory.hotel SET price = {updated_price} WHERE url LIKE "http://marriot%" AND country = "United States"'
    ctx.query(query_str)

cluster.transactions.run(txn_complex)
```

As you can see from the snippet above, it is possible to call regular Python methods from the lambda, permitting complex logic to be performed. Just remember that since the lambda may be called multiple times, so may the method.

Like key-value operations, queries support "Read Your Own Writes". This example shows inserting a document and then selecting it again:

```python
def txn_logic(ctx):
    ctx.query(
        "INSERT INTO `travel-sample` VALUES ('doc', {'hello':'world'})")  (1)
    query_str = "SELECT hello FROM `travel-sample` WHERE META().id = 'doc'"  (2)
    res = ctx.query(query_str)

cluster.transactions.run(txn_logic)
```

| **1** | The inserted document is only staged at this point, as the transaction has not yet committed.Other transactions, and other non-transactional actors, will not be able to see this staged insert yet. |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | But the SELECT can, as we are reading a mutation staged inside the same transaction.                                                                                                                 |

### [](#query-options)Query Options

Query options can be provided via `TransactionQueryOptions`, which provides a subset of the options in the Python SDK’s `QueryOptions`.

```python
def txn_logic(ctx):
    res = ctx.query(
        "INSERT INTO `travel-sample` VALUES ('doc-abc', {'hello':'world'})",
        TransactionQueryOptions(
            profile=QueryProfile.TIMINGS
        )
    )

cluster.transactions.run(txn_logic)
```

__Table 1\. Supported Transaction Query Options__
| Name                                         | Description                                                                      |
| -------------------------------------------- | -------------------------------------------------------------------------------- |
| positional\_parameters(Iterable\[JSONType\]) | Allows to set positional arguments for a parameterized query.                    |
| named\_parameters(Dict\[str, JSONType\])     | Allows you to set named arguments for a parameterized query.                     |
| scan\_consistency(QueryScanConsistency)      | Sets a different scan consistency for this query.                                |
| client\_context\_id(str)                     | Sets a context ID returned by the service for debugging purposes.                |
| scan\_wait(timedelta)                        | Allows to specify a maximum scan wait time.                                      |
| scan\_cap(int)                               | Specifies a maximum cap on the query scan size.                                  |
| pipeline\_batch(int)                         | Sets the batch size for the query pipeline.                                      |
| pipeline\_cap(int)                           | Sets the cap for the query pipeline.                                             |
| profile(Any)                                 | Allows you to enable additional query profiling as part of the response.         |
| read\_only(bool)                             | Tells the client and server that this query is readonly.                         |
| adhoc(bool)                                  | If set to false will prepare the query and later execute the prepared statement. |
| raw(Dict\[str, JSONType\])                   | Escape hatch to add arguments that are not covered by these options.             |

## [](#mixing-key-value-and-sql)Mixing Key-Value and SQL++

Key-Value operations and queries can be freely intermixed, and will interact with each other as you would expect. In this example we insert a document with a key-value operation, and read it with a `SELECT` query.

```python
def txn_logic(ctx):
    collection = cluster.defaultCollection()
    ctx.insert(collection, 'doc-greeting',
               {'greeting': 'hello world'})  (1)
    query_str = "SELECT greeting FROM `travel-sample` WHERE META().id = 'doc-greeting'"  (2)
    res = ctx.query(query_str)

cluster.transactions.run(txn_logic)
```

| **1** | The key-value insert operation is only staged, and so it is not visible to other transactions or non-transactional actors. |
| ----- | -------------------------------------------------------------------------------------------------------------------------- |
| **2** | But the SELECT can view it, as the insert was in the same transaction.                                                     |

> [!IMPORTANT]
> Query Mode
> 
> When a transaction executes a query statement, the transaction enters **query mode**, which means that the query is executed with the user’s query permissions. Any **key-value** operations which are executed by the transaction _after_ the query statement are _also_ executed with the user’s query permissions. These may or may not be different to the user’s data permissions; if they are different, you may get unexpected results.

## [](#concurrent-operations)Concurrent Operations

The API allows operations to be performed concurrently inside a transaction, which can assist performance. There are two rules the application needs to follow:

* The first mutation must be performed alone, in serial. This is because the first mutation also triggers the creation of metadata for the transaction.
* All concurrent operations must be allowed to complete fully, so the transaction can track which operations need to be rolled back in the event of failure. This means the application must 'swallow' the error, but record that an error occurred, and then at the end of the concurrent operations, if an error occurred, throw an error to cause the transaction to retry.

### [](#non-transactional-writes)Non-Transactional Writes

To ensure key-value performance is not compromised, and to avoid conflicting writes, applications should **never** perform non-transactional _writes_ concurrently with transactional ones, on the same document.

See [Concurrency with Non-Transactional Writes](../concept-docs/transactions.md#concurrency-with-non-transactional-writes) to learn more.

## [](#configuration)Configuration

The default configuration should be appropriate for most use-cases. Transactions can optionally be globally configured when configuring the `Cluster`. For example, if you want to change the level of durability which must be attained, this can be configured as part of the connect options:

```python
opts = ClusterOptions(authenticator=PasswordAuthenticator("Administrator", "password"),
                      transaction_config=TransactionConfig(
                          durability=ServerDurability(DurabilityLevel.PERSIST_TO_MAJORITY))
                      )

cluster = Cluster.connect('couchbase://your-ip', opts)
```

The default configuration will perform all writes with the durability setting `Majority`, ensuring that each write is available in-memory on the majority of replicas before the transaction continues. There are two higher durability settings available that will additionally wait for all mutations to be written to physical storage on either the active or the majority of replicas, before continuing. This further increases safety, at a cost of additional latency.

> [!CAUTION]
> A level of `None` is present but its use is discouraged and unsupported. If durability is set to `None`, then ACID semantics are not guaranteed.

## [](#additional-resources)Additional Resources

* Learn more about [Distributed ACID Transactions](../concept-docs/transactions.md).
* Check out the SDK [API Reference](https://docs.couchbase.com/sdk-api/couchbase-python-client/).