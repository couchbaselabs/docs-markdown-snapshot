---
title: Transaction Concepts
description: A high-level overview of Distributed ACID Transactions with Couchbase.
editUrl: https://github.com/couchbase/docs-sdk-go/edit/temp/2.9/modules/concept-docs/pages/transactions.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:2.9@go-sdk:concept-docs:transactions.adoc[]
---

[View original HTML](/go-sdk/2.9/concept-docs/transactions.html)

# Transaction Concepts

> A high-level overview of Distributed ACID Transactions with Couchbase. 

For a practical guide, see [Distributed ACID Transactions from the Go SDK](../howtos/distributed-acid-transactions-from-the-sdk.md).

## [](#overview)Overview

Couchbase Distributed [ACID (atomic, consistent, isolated, and durable)](../../../server/current/learn/data/transactions.md#overview) Transactions allow applications to perform a series of database operations as a single unit — meaning operations are either committed together or all undone. Transactions are distributed and work across multiple documents, buckets, scopes, and collections, which can reside on multiple nodes.

## [](#transaction-mechanics)Transaction Mechanics

The starting point is the `Transactions` object, which is effectively a singleton belonging to a `Cluster` object. Internally `Transactions` is created on `gocb.Connect(…​)` and its lifetime is bound to the parent `Cluster` object.

```go
// Initialize the Couchbase cluster
opts := gocb.ClusterOptions{
	Authenticator: gocb.PasswordAuthenticator{
		Username: "Administrator",
		Password: "password",
	},
}

cluster, err := gocb.Connect("localhost", opts)
if err != nil {
	panic(err)
}

bucket := cluster.Bucket("travel-sample")

scope := bucket.Scope("inventory")
collection := scope.Collection("airport")

transactions := cluster.Transactions()
```

> [!NOTE]
> Multiple calls to `cluster.Transactions()` will yield the same `Transactions` object. This is because the `Transactions` object performs automated [background processes](transactions-cleanup.md) that should not be duplicated.

```go
result, err := cluster.Transactions().Run(func(ctx *gocb.TransactionAttemptContext) error {
	if _, err := ctx.Insert(collection, "doc1", map[string]interface{}{}); err != nil {
		return err
	}

	// Replace
	doc, err := ctx.Get(collection, "doc1")
	if err != nil {
		return err
	}

	var content map[string]interface{}
	err = doc.Content(&content)
	if err != nil {
		return err
	}
	content["transactions"] = "are awesome"
	_, err = ctx.Replace(doc, content)
	if err != nil {
		return err
	}

	return nil
}, nil)
if err != nil {
	log.Printf("%+v", err)
}
```

A core idea of Couchbase transactions is that an application supplies the logic for the transaction inside a `function literal`, including any conditional logic required, and the transaction is then automatically committed. If a transient error occurs, such as a temporary conflict with another transaction, then the transaction will rollback what has been done so far and run the function literal again. The application does not have to do these retries and error handling itself.

Each run of the function literal is called an `attempt`, inside an overall `transaction`.

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

Only once the function literal has successfully run to conclusion, will the attempt be committed. This updates the ATR entry, which is used as a signal by transactional actors to use the post-transaction version of a document from its XATTRs. Hence, updating the ATR entry is an 'atomic commit' switch for the transaction.

After this commit point is reached, the individual documents will be committed (or "unstaged"). This provides an eventually consistent commit for non-transactional actors.

### [](#rollback)Rollback

When an error is thrown, either by the application from the function literal, or by the transactions logic itself (e.g. on a failed operation), then that attempt is rolled back.

The application’s function literal may or may not be retried, depending on the error that occurred. The general rule for retrying is whether the transaction is likely to succeed on a retry. For example, if this transaction is trying to write a document that is currently involved in another transaction (a write-write conflict), this will lead to a retry as that is likely a transient state. But if the transaction is trying to get a document that does not exist, it will not retry.

If the transaction is not retried then it will return a `TransactionFailedError` error, and its `Unwrap` function can be used for more details on the failure.

The application can use this to signal why it triggered a rollback, as so:

```go
var ErrBalanceInsufficient = errors.New("insufficient funds")

_, err := cluster.Transactions().Run(func(ctx *gocb.TransactionAttemptContext) error {
	doc, err := ctx.Get(collection, "customer-name")
	if err != nil {
		return err
	}

	var cust customer
	err = doc.Content(&cust)
	if err != nil {
		return err
	}

	if cust.Balance < costOfItem {
		return ErrBalanceInsufficient
	}
	// else continue transaction

	return nil
}, nil)
var ambigErr gocb.TransactionCommitAmbiguousError
if errors.As(err, &ambigErr) {
	// This error can only be thrown at the commit point, after the
	// BalanceInsufficient logic has been passed, so there is no need to
	// check getCause here.
	fmt.Println("Transaction possibly committed")
	fmt.Printf("%+v", ambigErr)
	return
}

var transactionFailedErr gocb.TransactionFailedError
if errors.As(err, &transactionFailedErr) {
	if errors.Is(transactionFailedErr, ErrBalanceInsufficient) {
		// Re-raise the error
		panic(transactionFailedErr)
	} else {
		fmt.Println("Transaction did not reach commit point")
		fmt.Printf("%+v", transactionFailedErr)
	}
	return
}
```

After a transaction is rolled back, it cannot be committed, no further operations are allowed on it, and the SDK will not try to automatically commit it at the end of the code block.

## [](#transaction-operations)Transaction Operations

Couchbase transactions can be initiated programmatically through the SDK, or by using the Query service directly with `BEGIN TRANSACTION`. The latter is intended for those using Query via the REST API, or using the Couchbase UI, and it is strongly recommended that application writers instead use the SDK. This provides these benefits:

* It automatically handles errors and retrying.
* It allows key-value operations and queries to be freely mixed.
* It takes care of issuing `BEGIN TRANSACTION`, `END TRANSACTION`, `COMMIT` and `ROLLBACK` automatically. These become an implementation detail, and you should not use these statements inside the function literal.

The standard key-value operations are supported by the SDK: `Insert`, `Get`, `Replace`, `Remove`.

Similarly, the majority of SQL++ (formerly N1QL) DML statements are permitted within a transaction.  
Specifically: `INSERT`, `UPSERT`, `DELETE`, `UPDATE`, `MERGE`, `SELECT`.

DDL statements such as `CREATE INDEX`, are not supported.

### [](#query-performance-advice)Query Performance Advice

This section is optional reading, and only for those looking to maximize transactions performance.

After the first query statement in a transaction, subsequent Key-Value operations in the function literal are converted into SQL++ and executed by the Query service rather than the Key-Value data service. The operation will behave identically, and this implementation detail can largely be ignored, except for these two caveats:

* These converted key-value operations are likely to be slightly slower, as the Query service is optimized for statements involving multiple documents. Those looking for the maximum possible performance are recommended to put key-value operations before the first query in the function literal, if possible.
* Those using non-blocking mechanisms to achieve concurrency should be aware that the converted key-value operations are subject to the same parallelism restrictions mentioned above, e.g. they will not be executed in parallel by the Query service.

## [](#concurrency-with-non-transactional-writes)Concurrency with Non-Transactional Writes

Couchbase transactions require a degree of co-operation from an application. Specifically, the application should ensure that non-transactional writes are never done concurrently with transactional writes, on the same document.

This requirement is to ensure that the strong key-value performance of Couchbase was not compromised. A key philosophy of Couchbase transactions is that you 'pay only for what you use'.

If two such writes **do** conflict then the behaviour is undefined: either write may 'win', overwriting the other. This still applies if the non-transactional write is using CAS.

Note this only applies to _writes_. Any non-transactional _reads_ concurrent with transactions are fine, and are at a Read Committed level.

## [](#custom-metadata-collections)Custom Metadata Collections

As described earlier, transactions automatically create and use metadata documents. By default, these are created in the default collection of the bucket of the first mutated document in the transaction. Optionally, you can instead specify a collection to store the metadata documents. Most users will not need to use this functionality, and can continue to use the default behavior. They are provided for these use-cases:

* The metadata documents contain, for documents involved in each transaction, the document’s key and the name of the bucket, scope and collection it exists on. In some deployments this may be sensitive data.
* You wish to remove the default collections. Before doing this, you should ensure that all existing transactions using metadata documents in the default collections have finished.

Custom metadata collections are enabled with:

```go
cluster, err := gocb.Connect("localhost", gocb.ClusterOptions{
	TransactionsConfig: gocb.TransactionsConfig{
		MetadataCollection: &gocb.TransactionKeyspace{
			BucketName:     "travel-sample",
			ScopeName:      "transactions",
			CollectionName: "metadata",
		},
	},
})
```

When specified:

* Any transactions created from this `Transactions` object, will create and use metadata in that collection.
* The asynchronous cleanup started by this `Transactions` object will be looking for expired transactions only in this collection, unless additional `CleanupCollections` are provided or a transaction explicitly overrides the metadata collection.

Custom metadata collections can also be provided at the transaction level itself.

```go
metaCollection := cluster.Bucket("travel-sample").Scope("transactions").Collection("other-metadata")
result, err := cluster.Transactions().Run(func(ctx *gocb.TransactionAttemptContext) error {
	// ... transactional code here ...
	return nil
}, &gocb.TransactionOptions{
	MetadataCollection: metaCollection,
})
```

This will override any metadata collection that has been provided at the `Transactions` level.

You need to ensure that the application has RBAC data read and write privileges to any custom metadata collections, and should not delete them subsequently as that can interfere with existing transactions. You can use existing collections or create new ones.