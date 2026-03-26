---
title: Transaction Concepts
description: A high-level overview of Distributed ACID Transactions with Couchbase.
editUrl: https://github.com/couchbase/docs-sdk-java/edit/release/3.5/modules/concept-docs/pages/transactions.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.5@java-sdk:concept-docs:transactions.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/java-sdk/3.5/concept-docs/transactions.html)

# Transaction Concepts

> A high-level overview of Distributed ACID Transactions with Couchbase. 

For a practical guide, see [Using Couchbase Transactions](../howtos/distributed-acid-transactions-from-the-sdk.md).

## [](#overview)Overview

Couchbase Distributed [ACID (atomic, consistent, isolated, and durable)](#7.1@server:learn:data/transactions.adoc#overview) Transactions allow applications to perform a series of database operations as a single unit — meaning operations are either committed together or all undone. Transactions are distributed and work across multiple documents, buckets, scopes, and collections, which can reside on multiple nodes.

## [](#transaction-mechanics)Transaction Mechanics

```java
cluster.transactions().run((ctx) -> {
    ctx.insert(collection, "doc1", doc1Content);

    var doc2 = ctx.get(collection, "doc2");
    ctx.replace(doc2, doc2Content);
});
```

A core idea of Couchbase transactions is that an application supplies the logic for the transaction inside a `lambda`, including any conditional logic required, and the transaction is then automatically committed. If a transient error occurs, such as a temporary conflict with another transaction, then the transaction will rollback what has been done so far and run the lambda again. The application does not have to do these retries and error handling itself.

Each run of the lambda is called an `attempt`, inside an overall `transaction`.

### [](#active-transaction-record-entries)Active Transaction Record Entries

The first mechanic is that each of these attempts adds an entry to a metadata document in the Couchbase cluster. These metadata documents:

* Are named Active Transaction Records, or ATRs.
* Are created and maintained automatically.
* Begin with `_txn:atr-`.
* Each contain entries for multiple attempts.
* Are viewable, and _should not be modified externally_.

Each such ATR entry stores some metadata and, crucially, whether the attempt has committed or not. In this way, the entry acts as the single point of truth for the transaction, which is essential for providing an 'atomic commit' during reads.

### [](#staged-mutations)Staged Mutations

The second mechanic is that mutating a document inside a transaction, does not directly change the body of the document. Instead, the post-transaction version of the document is staged alongside the document (technically in its [extended attributes (XATTRs)](xattr.md)). In this way, all changes are invisible to all parts of Couchbase until the commit point is reached.

These staged document changes effectively act as a lock against other transactions trying to modify the document, preventing write-write conflicts.

### [](#cleanup)Cleanup

There are safety mechanisms to ensure that leftover staged changes from a failed transaction cannot block live transactions indefinitely. These include an asynchronous cleanup process that is started with the first transaction, and scans for expired transactions created by any application, on the relevant collections.

The cleanup process is detailed in the [Cleanup](transactions-cleanup.md) page.

### [](#committing)Committing

Only once the lambda has successfully run to conclusion, will the attempt be committed. This updates the ATR entry, which is used as a signal by transactional actors to use the post-transaction version of a document from its XATTRs. Hence, updating the ATR entry is an 'atomic commit' switch for the transaction.

After this commit point is reached, the individual documents will be committed (or "unstaged"). This provides an eventually consistent commit for non-transactional actors.

### [](#rollback)Rollback

When an exception is thrown, either by the application from the lambda, or by the transactions logic itself (e.g. on a failed operation), then that attempt is rolled back.

The application's lambda may or may not be retried, depending on the error that occurred. The general rule for retrying is whether the transaction is likely to succeed on a retry. For example, if this transaction is trying to write a document that is currently involved in another transaction (a write-write conflict), this will lead to a retry as that is likely a transient state. But if the transaction is trying to get a document that does not exist, it will not retry.

If the transaction is not retried then it will throw a `TransactionFailedException`, and its `getCause` method can be used for more details on the failure.

The application can use this to signal why it triggered a rollback, as so:

```java
class BalanceInsufficient extends RuntimeException {
}

try {
    cluster.transactions().run((ctx) -> {
        var customer = ctx.get(collection, "customer-name");

        if (customer.contentAsObject().getInt("balance") < costOfItem) {
            throw new BalanceInsufficient();
        }
        // else continue transaction
    });
} catch (TransactionCommitAmbiguousException e) {
    // This exception can only be thrown at the commit point, after the
    // BalanceInsufficient logic has been passed, so there is no need to
    // check getCause here.
    throw logCommitAmbiguousError(e);
} catch (TransactionFailedException e) {
    if (e.getCause() instanceof BalanceInsufficient) {
        // Re-raise the error
        throw (RuntimeException) e.getCause();
    } else {
        throw logFailure(e);
    }
}
```

After a transaction is rolled back, it cannot be committed, no further operations are allowed on it, and the SDK will not try to automatically commit it at the end of the code block.

## [](#transaction-operations)Transaction Operations

Couchbase transactions can be initiated programmatically through the SDK, or by using the Query service directly with `BEGIN TRANSACTION`. The latter is intended for those using Query via the REST API, or using the Couchbase UI, and it is strongly recommended that application writers instead use the SDK. This provides these benefits:

* It automatically handles errors and retrying.
* It allows key-value operations and queries to be freely mixed.
* It takes care of issuing `BEGIN TRANSACTION`, `END TRANSACTION`, `COMMIT` and `ROLLBACK` automatically. These become an implementation detail, and you should not use these statements inside the lambda.

The standard key-value operations are supported by the SDK: `Insert`, `Get`, `Replace`, `Remove`.

Similarly, the majority of SQL++ (formerly N1QL) DML statements are permitted within a transaction.  
Specifically: `INSERT`, `UPSERT`, `DELETE`, `UPDATE`, `MERGE`, `SELECT`.

DDL statements such as `CREATE INDEX`, are not supported.

### [](#query-performance-advice)Query Performance Advice

This section is optional reading, and only for those looking to maximize transactions performance.

After the first query statement in a transaction, subsequent Key-Value operations in the lambda are converted into SQL++ and executed by the Query service rather than the Key-Value data service. The operation will behave identically, and this implementation detail can largely be ignored, except for these two caveats:

* These converted key-value operations are likely to be slightly slower, as the Query service is optimized for statements involving multiple documents. Those looking for the maximum possible performance are recommended to put key-value operations before the first query in the lambda, if possible.
* Those using non-blocking mechanisms to achieve concurrency should be aware that the converted key-value operations are subject to the same parallelism restrictions mentioned above, e.g. they will not be executed in parallel by the Query service.

## [](#concurrency-with-non-transactional-writes)Concurrency with Non-Transactional Writes

Couchbase transactions require a degree of co-operation from an application. Specifically, the application should ensure that non-transactional writes are never done concurrently with transactional writes, on the same document.

This requirement is to ensure that the strong key-value performance of Couchbase was not compromised. A key philosophy of Couchbase transactions is that you 'pay only for what you use'.

If two such writes **do** conflict then the behaviour is undefined: either write may 'win', overwriting the other. This still applies if the non-transactional write is using CAS.

Note this only applies to _writes_. Any non-transactional _reads_ concurrent with transactions are fine, and are at a Read Committed level.

## [](#custom-metadata-collections)Custom Metadata Collections

As described earlier, transactions automatically create and use metadata documents. By default, these are created in the default collection of the bucket of the first mutated document in the transaction. Optionally, you can instead specify a collection to store the metadata documents. Most users will not need to use this functionality, and can continue to use the default behavior. They are provided for these use-cases:

* The metadata documents contain, for documents involved in each transaction, the document's key and the name of the bucket, scope and collection it exists on. In some deployments this may be sensitive data.
* You wish to remove the default collections. Before doing this, you should ensure that all existing transactions using metadata documents in the default collections have finished.

Custom metadata collections are enabled with:

```java
var keyspace = TransactionKeyspace.create("bucketName", "scopeName", "collectionName");

var cluster = Cluster.connect("localhost", ClusterOptions.clusterOptions("username", "password")
        .environment(env -> env.transactionsConfig(TransactionsConfig.metadataCollection(keyspace))));
```

or at an individual transaction level with:

```java
cluster.transactions().run((ctx) -> {
    // Your transaction logic
}, transactionOptions().metadataCollection(collection));
```

You need to ensure that the application has RBAC data read and write privileges to any custom metadata collections, and should not delete them subsequently as that can interfere with existing transactions. You can use existing collections or create new ones.