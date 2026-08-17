---
title: Transaction Concepts
description: A high-level overview of Distributed ACID Transactions with Couchbase.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-dotnet/edit/temp/3.7/modules/concept-docs/pages/transactions.adoc
  xref: xref:3.7@dotnet-sdk:concept-docs:transactions.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/dotnet-sdk/3.7/concept-docs/transactions.html)

# Transaction Concepts

> A high-level overview of Distributed ACID Transactions with Couchbase. 

For a practical guide, see [Distributed ACID Transactions from the .NET SDK](../howtos/distributed-acid-transactions-from-the-sdk.md).

## [](#overview)Overview

Couchbase Distributed [ACID (atomic, consistent, isolated, and durable)](../../../server/current/learn/data/transactions.md#overview) Transactions allow applications to perform a series of database operations as a single unit — meaning operations are either committed together or all undone. Transactions are distributed and work across multiple documents, buckets, scopes, and collections, which can reside on multiple nodes.

## [](#transaction-mechanics)Transaction Mechanics

```csharp
var doc1Content = new {content = "some doc1 content" };
var doc2Content = new {content = "some doc2 content" };

await _transactions.RunAsync(async (ctx) =>
{
    await ctx.InsertAsync(_collection, "doc-1", doc1Content).ConfigureAwait(false);

    var doc2 = await ctx.GetAsync(_collection, "doc-2").ConfigureAwait(false);
    await ctx.ReplaceAsync(doc2, doc2Content).ConfigureAwait(false);
}).ConfigureAwait(false);
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

There are safety mechanisms to ensure that leftover staged changes from a failed transaction cannot block live transactions indefinitely. These include an asynchronous cleanup process that is started with the creation of the `Transactions` object, and scans for expired transactions created by any application, on all buckets.

The cleanup process is detailed in the [Cleanup](transactions-cleanup.md) page.

### [](#committing)Committing

Only once the lambda has successfully run to conclusion, will the attempt be committed. This updates the ATR entry, which is used as a signal by transactional actors to use the post-transaction version of a document from its XATTRs. Hence, updating the ATR entry is an 'atomic commit' switch for the transaction.

After this commit point is reached, the individual documents will be committed (or "unstaged"). This provides an eventually consistent commit for non-transactional actors.

> [!TIP]
> Committing is automatic: if there is no explicit call to `ctx.CommitAsync()` at the end of the transaction logic callback, and no exception is thrown, it will be committed.

### [](#rollback)Rollback

When an exception is thrown, either by the application from the lambda, or by the transactions logic itself (e.g. on a failed operation), then that attempt is rolled back.

The application's lambda may or may not be retried, depending on the error that occurred. The general rule for retrying is whether the transaction is likely to succeed on a retry. For example, if this transaction is trying to write a document that is currently involved in another transaction (a write-write conflict), this will lead to a retry as that is likely a transient state. But if the transaction is trying to get a document that does not exist, it will not retry.

If the transaction is not retried then it will throw a `TransactionFailedException`.

```csharp
public class BalanceInsufficientException : Exception { }
const int CostOfItem = 10;
private async Task RollbackCause()
{
    try
    {
        await _transactions.RunAsync(async ctx =>
        {
            var customer = await ctx.GetAsync(_collection, "customer-name").ConfigureAwait(false);

            if (customer.ContentAs<dynamic>()?.balance < CostOfItem) throw new BalanceInsufficientException();
            // else continue transaction
        }).ConfigureAwait(false);
    }
    catch (TransactionCommitAmbiguousException e)
    {
        // This exception can only be thrown at the commit point, after the
        // BalanceInsufficient logic has been passed.
        Console.Error.WriteLine("Transaction possibly committed");
        Console.Error.WriteLine(e);
    }
    catch (TransactionFailedException e)
    {
        Console.Error.WriteLine("Transaction did not reach commit point");
    }

}
```

## [](#transaction-operations)Transaction Operations

Couchbase transactions can be initiated programmatically through a library, or by using the Query service directly with `BEGIN TRANSACTION`. The latter is intended for those using Query via the REST API, or using the Couchbase UI, and it is strongly recommended that application writers instead use the transactions library. This provides these benefits:

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

## [](#custom-metadata-collections)Custom Metadata Collections

As described earlier, transactions automatically create and use metadata documents. By default, these are created in the default collection of the bucket of the first mutated document in the transaction. Optionally, you can instead specify a collection to store the metadata documents. Most users will not need to use this functionality, and can continue to use the default behavior. They are provided for these use-cases:

* The metadata documents contain, for documents involved in each transaction, the document's key and the name of the bucket, scope and collection it exists on. In some deployments this may be sensitive data.
* You wish to remove the default collections. Before doing this, you should ensure that all existing transactions using metadata documents in the default collections have finished.

Custom metadata collections are enabled with:

```csharp
// Replace with your own metadata collection.

// define a Keyspace to use for transaction metadata
var metadataCollection = new Keyspace("bucket", "scope", "collection");

// now configure the cluster to use it in transactions.
var transactionsConfig = TransactionsConfigBuilder.Create()
    .MetadataCollection(metadataCollection)
    .Build();
var options = new ClusterOptions()
{
    UserName = "Administrator",
    Password = "Administrator",
    TransactionsConfig = transactionsConfig,
};
var cluster = await Cluster.ConnectAsync("couchbase://your-ip", options).ConfigureAwait(false);

// now all transactions using the Transactions in this cluster will use the
// specified keyspace for the metadata.
var transactionsWithCustomMetadataCollection = cluster.Transactions;
```

When specified:

* Any transactions created from this `Transactions` object, will create and use metadata in that collection.
* The asynchronous cleanup started by this `Transactions` object will be looking for expired transactions only in this collection.

You need to ensure that this application has RBAC data read and write privileges to it, and should not delete the collection subsequently as it can interfere with existing transactions. You can use an existing collection or create a new one.