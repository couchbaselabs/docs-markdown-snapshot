---
title: Transaction Concepts
description: A high-level overview of Distributed ACID Transactions with Couchbase.
editUrl: https://github.com/couchbase/docs-sdk-php/edit/temp/4.2/modules/concept-docs/pages/transactions.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:4.2@php-sdk:concept-docs:transactions.adoc[]
---

[View original HTML](/php-sdk/4.2/concept-docs/transactions.html)

# Transaction Concepts

> A high-level overview of Distributed ACID Transactions with Couchbase. 

For a practical guide, see [Distributed ACID Transactions from the PHP SDK](../howtos/distributed-acid-transactions-from-the-sdk.md).

## [](#overview)Overview

Unresolved include directive in modules/concept-docs/pages/transactions.adoc - include::7.5@sdk:shared:partial$acid-transactions.adoc\[\]

## [](#transaction-mechanics)Transaction Mechanics

```php
$cluster->transactions()->run(
  function (TransactionAttemptContext $ctx) use ($collection) {
    $ctx->insert($collection, 'doc1', ['hello' => 'world']);

    $doc = $ctx->get($collection, 'doc1');
    $ctx->replace($doc, ['foo' => 'bar']);
  }
);
```

Unresolved include directive in modules/concept-docs/pages/transactions.adoc - include::7.5@sdk:shared:partial$acid-transactions.adoc\[\]

## [](#rollback)Rollback

If an exception is thrown by the application from the lambda, then that attempt is rolled back. The transaction logic may or may not be retried, depending on the exception.

If the transaction is not retried then it will throw an exception, and its `context()` method can be used to inspect the details of the failure.

The application can use this to signal why it triggered a rollback, as so:

```php
$costOfItem = 10;

try {
  $cluster->transactions()->run(
    function (TransactionAttemptContext $ctx) use ($collection, $costOfItem) {
      $customer = $ctx->get($collection, "customer-name");

      if ($customer->content()["balance"] < $costOfItem) {
        throw new \InsufficientBalanceException("Transaction failed, customer does not have enough funds.");
      }
      // else continue transaction
    }
  );
} catch (\Couchbase\Exception\TransactionFailedException $e) {
  echo "Transaction did not reach commit point: $e\n";
} catch (\Couchbase\Exception\TransactionCommitAmbiguousException $e) {
  echo "Transaction possibly committed: $e\n";
}
```

After a transaction is rolled back, it cannot be committed, no further operations are allowed on it, and the system will not try to automatically commit it at the end of the code block.

## [](#transaction-operations)Transaction Operations

Unresolved include directive in modules/concept-docs/pages/transactions.adoc - include::7.5@sdk:shared:partial$acid-transactions.adoc\[\]

## [](#concurrency-with-non-transactional-writes)Concurrency with Non-Transactional Writes

Unresolved include directive in modules/concept-docs/pages/transactions.adoc - include::7.5@sdk:shared:partial$acid-transactions.adoc\[\]