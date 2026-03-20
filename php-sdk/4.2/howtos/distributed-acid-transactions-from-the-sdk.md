---
title: Using Couchbase Transactions
description: Distributed ACID Transactions in Couchbase SDKs
editUrl: https://github.com/couchbase/docs-sdk-php/edit/temp/4.2/modules/howtos/pages/distributed-acid-transactions-from-the-sdk.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:4.2@php-sdk:howtos:distributed-acid-transactions-from-the-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/php-sdk/4.2/howtos/distributed-acid-transactions-from-the-sdk.html)

# Using Couchbase Transactions

> Distributed ACID Transactions in Couchbase SDKs 

This guide will show you examples of how to perform multi-document ACID (atomic, consistent, isolated, and durable) database transactions within your application, using the Couchbase PHP SDK.

Refer to the [Transaction Concepts](../concept-docs/transactions.md) material for a high-level overview.

## [](#prerequisites)Prerequisites

* Couchbase Capella
* Couchbase Server

* Couchbase Capella account.
* You should know how to perform [key-value](kv-operations.md) or [query](n1ql-queries-with-sdk.md) operations with the SDK.
* Your application should have the relevant roles and permissions on the required buckets, scopes, and collections, to perform transactional operations. Refer to the [Organizations & Access](../../../cloud/organizations/organization-projects-overview.md) page for more details.
* If your application is using [extended attributes (XATTRs)](../concept-docs/xattr.md), you should avoid using the XATTR field `txn` — this is reserved for Couchbase use.

* Couchbase Server (6.6.1 or above).
* You should know how to perform [key-value](kv-operations.md) or [query](n1ql-queries-with-sdk.md) operations with the SDK.
* Your application should have the relevant roles and permissions on the required buckets, scopes, and collections, to perform transactional operations. Refer to the [Roles](../../../server/7.6/learn/security/roles.md) page for more details.
* If your application is using [extended attributes (XATTRs)](../concept-docs/xattr.md), you should avoid using the XATTR field `txn` — this is reserved for Couchbase use.
* NTP should be configured so nodes of the Couchbase cluster are in sync with time.

Unresolved include directive in modules/howtos/pages/distributed-acid-transactions-from-the-sdk.adoc - include::7.5@sdk:shared:partial$acid-transactions.adoc\[\]

## [](#creating-a-transaction)Creating a Transaction

Unresolved include directive in modules/howtos/pages/distributed-acid-transactions-from-the-sdk.adoc - include::7.5@sdk:shared:partial$acid-transactions.adoc\[\]

```php
try {
  $cluster->transactions()->run(
    function (TransactionAttemptContext $ctx) use ($collection) {
      // Inserting a doc:
      $ctx->insert($collection, 'doc-c', []);

      // Getting documents:
      $docA = $ctx->get($collection, 'doc-a');

      // Replacing a doc:
      $docB = $ctx->get($collection, 'doc-b');
      $content = $docB->content();
      $newContent = array_merge(
        ["transactions" => "are awesome"],
        $content
      );
      $ctx->replace($docB, $newContent);

      // Removing a doc:
      $docC = $ctx->get($collection, 'doc-c');
      $ctx->remove($docC);

      // Performing a SELECT SQL++ (N1QL) query:
      $selectQuery = 'SELECT * FROM `travel-sample`.inventory.hotel WHERE country = $1 LIMIT 5';
      $qr = $ctx->query(
        $selectQuery,
        TransactionQueryOptions::build()
          ->positionalParameters(["United Kingdom"])
      );
      foreach ($qr->rows() as $row) {
        printf("Name: %s, Country: %s\n", $row["hotel"]["name"], $row["hotel"]["country"]);
      }

      // Performing an UPDATE SQL++ (N1QL) query:
      $updateQuery = 'UPDATE `travel-sample`.inventory.route SET airlineid = $1 WHERE airline = $2 LIMIT 5';
      $ctx->query(
        $updateQuery,
        TransactionQueryOptions::build()
          ->positionalParameters(['airline_137', 'AF'])
      );
    }
  );
} catch (\Couchbase\Exception\TransactionFailedException $e) {
  echo "Transaction did not reach commit point: $e\n";
} catch (\Couchbase\Exception\TransactionCommitAmbiguousException $e) {
  echo "Transaction possibly committed: $e\n";
}
```

Unresolved include directive in modules/howtos/pages/distributed-acid-transactions-from-the-sdk.adoc - include::7.5@sdk:shared:partial$acid-transactions.adoc\[\]

Unresolved include directive in modules/howtos/pages/distributed-acid-transactions-from-the-sdk.adoc - include::7.5@sdk:shared:partial$acid-transactions.adoc\[\]

### [](#logging)Logging

To aid troubleshooting, raise the log level on the SDK.

Please see the [PHP SDK logging documentation](collecting-information-and-logging.md) for details.

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

```php
$cluster->transactions()->run(
  function (TransactionAttemptContext $ctx) use ($collection) {
    $adoc = $ctx->insert($collection, "docId", []);
  }
);
```

### [](#get)Get

From a transaction context you may get a document:

```php
$cluster->transactions()->run(
  function (TransactionAttemptContext $ctx) use ($collection) {
    $docA = $ctx->get($collection, "doc-a");
  }
);
```

If the document does not exist, the transaction will fail with a `TransactionFailedException` (after rolling back any changes, of course).

Gets will "Read Your Own Writes", e.g. this will succeed:

```php
$cluster->transactions()->run(
  function (TransactionAttemptContext $ctx) use ($collection) {
    $docId = 'docId';
    $ctx->insert($collection, $docId, []);

    $doc = $ctx->get($collection, $docId);
  }
);
```

### [](#replace)Replace

Replacing a document requires a `$ctx→get()` call first. This is necessary so the SDK can check that the document is not involved in another transaction, and take appropriate action if so.

```php
$cluster->transactions()->run(
  function (TransactionAttemptContext $ctx) use ($collection) {
    $doc = $ctx->get($collection, "doc-b");
    $content = $doc->content();
    $newContent = array_merge(
      ["transactions" => "are awesome"],
      $content
    );

    $ctx->replace($doc, $newContent);
  }
);
```

### [](#remove)Remove

As with replaces, removing a document requires a `$ctx→get()` call first.

```php
$cluster->transactions()->run(
  function (TransactionAttemptContext $ctx) use ($collection) {
    $doc = $ctx->get($collection, "docId");
    $ctx->remove($doc);
  }
);
```

## [](#sql-queries)SQL++ Queries

If you already use [SQL++ (formerly N1QL)](https://www.couchbase.com/products/n1ql), then its use in transactions is very similar. It returns the same `QueryResult` you are used to, and takes most of the same options.

> [!IMPORTANT]
> As mentioned [previously](#lambda-ops), make sure your application uses the transactional query operations inside the lambda — such as `ctx.query()`, rather than `cluster.query()` or `scope.query()`.

Here is an example of selecting some rows from the `travel-sample` bucket:

```php
$cluster->transactions()->run(
  function (TransactionAttemptContext $ctx) {
    $st = "SELECT * FROM `travel-sample`.inventory.hotel WHERE country = $1";
    $qr = $ctx->query(
      $st,
      TransactionQueryOptions::build()
        ->positionalParameters(["United Kingdom"])
    );

    foreach ($qr->rows() as $row) {
      // do something
    }
  }
);
```

And an example combining `SELECT` and an `UPDATE`.

```php
$cluster->transactions()->run(
  function (TransactionAttemptContext $ctx) use ($hotelChain, $country) {
    // Find all hotels of the chain
    $qr = $ctx->query(
      'SELECT reviews FROM `travel-sample`.inventory.hotel WHERE url LIKE $1 AND country = $2',
      TransactionQueryOptions::build()
        ->positionalParameters([$hotelChain, $country])
    );

    // This function (not provided here) will use a trained machine learning model to provide a
    // suitable price based on recent customer reviews.
    function priceFromRecentReviews(Couchbase\QueryResult $qr)
    {
      // this would call a trained ML model to get the best price
      return 99.98;
    }
    $updatedPrice = priceFromRecentReviews($qr);

    // Set the price of all hotels in the chain
    $ctx->query(
      'UPDATE `travel-sample`.inventory.hotel SET price = $1 WHERE url LIKE $2 AND country = $3',
      TransactionQueryOptions::build()
        ->positionalParameters([$updatedPrice, $hotelChain, $country])
    );
  }
);
```

As you can see from the snippet above, it is possible to call regular PHP functions from the lambda, permitting complex logic to be performed. Just remember that since the lambda may be called multiple times, so may the method.

Like key-value operations, queries support "Read Your Own Writes". This example shows inserting a document and then selecting it again:

```php
$cluster->transactions()->run(
  function (TransactionAttemptContext $ctx) {
    // Query INSERT
    $ctx->query(
      "INSERT INTO `travel-sample`.inventory.airline VALUES ('doc-c', {'hello':'world'})" (1)
    );

    // Query SELECT
    $ctx->query(
      "SELECT hello FROM `travel-sample`.inventory.airline WHERE META().id = 'doc-c'" (2)
    );
  }
);
```

| **1** | The inserted document is only staged at this point, as the transaction has not yet committed.Other transactions, and other non-transactional actors, will not be able to see this staged insert yet. |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | But the SELECT can, as we are reading a mutation staged inside the same transaction.                                                                                                                 |

### [](#query-options)Query Options

Query options can be provided via `TransactionQueryOptions`, which provides a subset of the options in the PHP SDK’s `QueryOptions`.

```php
$cluster->transactions()->run(
  function (TransactionAttemptContext $ctx) {
    $txQo = TransactionQueryOptions::build()
      ->readonly(false)
      ->positionalParameters(["key", "value"]);

    $ctx->query(
      "UPSERT INTO `travel-sample`.inventory.airline VALUES ('docId', {\$1:\$2})",
      $txQo
    );
  }
);
```

__Table 1\. Supported Transaction Query Options__
| Name                                            | Description                                                                      |
| ----------------------------------------------- | -------------------------------------------------------------------------------- |
| positionalParameters(array<string\|int, mixed>) | Allows to set positional arguments for a parameterized query.                    |
| namedParameters(array<string\|int, mixed>)      | Allows you to set named arguments for a parameterized query.                     |
| scanConsistency(string)                         | Sets a different scan consistency for this query.                                |
| clientContextId(string)                         | Sets a context ID returned by the service for debugging purposes.                |
| scanWaitMilliseconds(int)                       | Allows to specify a maximum scan wait time.                                      |
| scanCap(int)                                    | Specifies a maximum cap on the query scan size.                                  |
| pipelineBatch(int)                              | Sets the batch size for the query pipeline.                                      |
| pipelineCap(int)                                | Sets the cap for the query pipeline.                                             |
| profile(int)                                    | Allows you to enable additional query profiling as part of the response.         |
| readonly(bool)                                  | Tells the client and server that this query is readonly.                         |
| adHoc(bool)                                     | If set to false will prepare the query and later execute the prepared statement. |
| raw(string)                                     | Escape hatch to add arguments that are not covered by these options.             |

## [](#mixing-key-value-and-sql)Mixing Key-Value and SQL++

Key-Value operations and queries can be freely intermixed, and will interact with each other as you would expect.

In this example we insert a document with a key-value operation, and read it with a `SELECT` query.

```php
$cluster->transactions()->run(
  function (TransactionAttemptContext $ctx) use ($collection) {
    // Key-Value insert
    $ctx->insert($collection, "doc-greeting", ["greeting" => "Hello World"]); (1)

    // Query SELECT 
    $selectQuery = "SELECT greeting FROM `travel-sample`.inventory.airline WHERE META().id = 'doc-greeting'";
    $ctx->query($selectQuery); (2)
  }
);
```

| **1** | The key-value insert operation is only staged, and so it is not visible to other transactions or non-transactional actors. |
| ----- | -------------------------------------------------------------------------------------------------------------------------- |
| **2** | But the SELECT can view it, as the insert was in the same transaction.                                                     |

## [](#configuration)Configuration

Transactions can optionally be globally configured when configuring the `Cluster`. For example, if you want to change the level of durability which must be attained, this can be configured as part of the connect options:

```php
$CB_USER = getenv('CB_USER') ?: 'Administrator';
$CB_PASS = getenv('CB_PASS') ?: 'password';
$CB_HOST = getenv('CB_HOST') ?: 'couchbase://localhost';

$options = new ClusterOptions();
$options->credentials($CB_USER, $CB_PASS);

$transactions_configuration = new TransactionsConfiguration();
$transactions_configuration->durabilityLevel(Couchbase\DurabilityLevel::PERSIST_TO_MAJORITY);
$options->transactionsConfiguration($transactions_configuration);

$cluster = new Cluster($CB_HOST, $options);
```

Unresolved include directive in modules/howtos/pages/distributed-acid-transactions-from-the-sdk.adoc - include::7.5@sdk:shared:partial$acid-transactions.adoc\[\]

## [](#additional-resources)Additional Resources

* Learn more about [Distributed ACID Transactions](../concept-docs/transactions.md).
* Check out the SDK [API Reference](https://docs.couchbase.com/sdk-api/couchbase-php-client/namespaces/couchbase.html).