---
title: Transaction Concepts
description: A high-level overview of Distributed ACID Transactions with Couchbase.
editUrl: https://github.com/couchbase/docs-sdk-nodejs/edit/temp/4.7/modules/concept-docs/pages/transactions.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:nodejs-sdk:concept-docs:transactions.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/nodejs-sdk/current/concept-docs/transactions.html)

# Transaction Concepts

> A high-level overview of Distributed ACID Transactions with Couchbase. 

For a practical guide, see [Distributed ACID Transactions from the Node.js SDK](../howtos/distributed-acid-transactions-from-the-sdk.md).

## [](#overview)Overview

Couchbase Distributed [ACID (atomic, consistent, isolated, and durable)](../../../server/current/learn/data/transactions.md#overview) Transactions allow applications to perform a series of database operations as a single unit — meaning operations are either committed together or all undone. Transactions are distributed and work across multiple documents, buckets, scopes, and collections, which can reside on multiple nodes.

## [](#transaction-mechanics)Transaction Mechanics

```typescript
await cluster.transactions().run(async (ctx) => {
  ctx.insert(collection, 'doc1', { hello: 'world' })

  const doc2 = await ctx.get(collection, "doc2")
  await ctx.replace(doc2, { foo: "bar" })
})
```

A core idea of Couchbase transactions is that an application supplies the logic for the transaction inside an `arrow function`, including any conditional logic required, and the transaction is then automatically committed. If a transient error occurs, such as a temporary conflict with another transaction, then the transaction will rollback what has been done so far and run the arrow function again. The application does not have to do these retries and error handling itself.

Each run of the arrow function is called an `attempt`, inside an overall `transaction`.

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

Only once the arrow function has successfully run to conclusion, will the attempt be committed. This updates the ATR entry, which is used as a signal by transactional actors to use the post-transaction version of a document from its XATTRs. Hence, updating the ATR entry is an 'atomic commit' switch for the transaction.

After this commit point is reached, the individual documents will be committed (or "unstaged"). This provides an eventually consistent commit for non-transactional actors.

## [](#rollback)Rollback

If an exception is thrown, either by the application from the lambda, or by the transaction internally, then that attempt is rolled back. The transaction logic may or may not be retried, depending on the exception.

If the transaction is not retried then it will throw an exception, and its `error` will contain details on the failure. In Typescript, you may branch your error handling based on `instanceof` with one of `TransactionFailedError`, `TransactionExpiredError` or `TransactionCommitAmbiguousError`.

The application can use this to signal why it triggered a rollback, as so:

```typescript
try {
  cluster.transactions().run(async (ctx) => {
    const customer = await ctx.get(collection, 'customer-name')

    if (customer.content.balance < costOfItem) {
      throw new InsufficientBalanceError()
    }
    // else continue transaction
  })
} catch (error) {
  if (error instanceof TransactionCommitAmbiguousError) {
    // This exception can only be thrown at the commit point, after the
    // BalanceInsufficient logic has been passed, so there is no need to
    // check the cause property here.
  } else if (error instanceof InsufficientBalanceError) {
    console.error('user had insufficient balance')
  }
}
```

After a transaction is rolled back, it cannot be committed, no further operations are allowed on it, and the system will not try to automatically commit it at the end of the code block.

## [](#transaction-operations)Transaction Operations

Couchbase transactions can be initiated programmatically through the SDK, or by using the Query service directly with `BEGIN TRANSACTION`. The latter is intended for those using Query via the REST API, or using the Couchbase UI, and it is strongly recommended that application writers instead use the SDK. This provides these benefits:

* It automatically handles errors and retrying.
* It allows key-value operations and queries to be freely mixed.
* It takes care of issuing `BEGIN TRANSACTION`, `END TRANSACTION`, `COMMIT` and `ROLLBACK` automatically. These become an implementation detail, and you should not use these statements inside the arrow function.

The standard key-value operations are supported by the SDK: `Insert`, `Get`, `Replace`, `Remove`.

Similarly, the majority of SQL++ (formerly N1QL) DML statements are permitted within a transaction.  
Specifically: `INSERT`, `UPSERT`, `DELETE`, `UPDATE`, `MERGE`, `SELECT`.

DDL statements such as `CREATE INDEX`, are not supported.

### [](#query-performance-advice)Query Performance Advice

This section is optional reading, and only for those looking to maximize transactions performance.

After the first query statement in a transaction, subsequent Key-Value operations in the arrow function are converted into SQL++ and executed by the Query service rather than the Key-Value data service. The operation will behave identically, and this implementation detail can largely be ignored, except for these two caveats:

* These converted key-value operations are likely to be slightly slower, as the Query service is optimized for statements involving multiple documents. Those looking for the maximum possible performance are recommended to put key-value operations before the first query in the arrow function, if possible.
* Those using non-blocking mechanisms to achieve concurrency should be aware that the converted key-value operations are subject to the same parallelism restrictions mentioned above, e.g. they will not be executed in parallel by the Query service.

## [](#concurrency-with-non-transactional-writes)Concurrency with Non-Transactional Writes

Couchbase transactions require a degree of co-operation from an application. Specifically, the application should ensure that non-transactional writes are never done concurrently with transactional writes, on the same document.

This requirement is to ensure that the strong key-value performance of Couchbase was not compromised. A key philosophy of Couchbase transactions is that you 'pay only for what you use'.

If two such writes **do** conflict then the behaviour is undefined: either write may 'win', overwriting the other. This still applies if the non-transactional write is using CAS.

Note this only applies to _writes_. Any non-transactional _reads_ concurrent with transactions are fine, and are at a Read Committed level.