---
title: ROLLBACK TRANSACTION
description: The ROLLBACK TRANSACTION statement enables you to rollback a transaction.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/n1ql/pages/n1ql-language-reference/rollback-transaction.adoc
  xref: xref:cloud:n1ql:n1ql-language-reference/rollback-transaction.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/n1ql/n1ql-language-reference/rollback-transaction.html)

# ROLLBACK TRANSACTION

> The ROLLBACK TRANSACTION statement enables you to rollback a transaction. 

## [](#purpose)Purpose

The `ROLLBACK TRANSACTION` statement enables you to rollback an ACID transaction. You can rollback the entire transaction, or rollback to a previous savepoint. For more information, see [SQL++ Support for Couchbase Transactions](transactions.md).

This statement may only be used within a transaction.

When you rollback the entire transaction, this statement removes all savepoints within the transaction.

> [!NOTE]
> If you're using the cbq shell, and a transaction fails for any reason, you must use the `ROLLBACK TRANSACTION` statement to remove the transaction context and reset the transaction ID.

## [](#syntax)Syntax

```ebnf
rollback-transaction ::= 'ROLLBACK' ( 'WORK' | 'TRAN' | 'TRANSACTION' )?
                       ( 'TO' 'SAVEPOINT' savepointname )?
```

![Syntax diagram: see source code listing](../_images/n1ql-language-reference/rollback-transaction.png) 

The `WORK`, `TRAN`, and `TRANSACTION` keywords are synonyms. These keywords are optional; you may include one of these keywords, or omit them entirely.

### [](#rollback-to-a-savepoint)Rollback to a Savepoint

The `TO SAVEPOINT` clause enables you to rollback to a specified savepoint. This clause is optional. If omitted, the entire transaction is rolled back.

savepointname

An identifier specifying a name for the savepoint.

## [](#examples)Examples

If you want to try these examples, first see [Preparation](transactions.md#preparation) to set up your environment.

Example 1\. Rollback a transaction

Transaction

```sqlpp
-- Start the transaction
BEGIN TRANSACTION;

-- Specify transaction settings
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

-- Create a booking document
UPSERT INTO bookings
VALUES("42641d7a-cde3-4a4d-bfd5-fec321510f70", {
  "date": "07/24/2021",
  "flight": "WN533",
  "flighttime": 7713,
  "price": 964.13,
  "route": "63986"
});

-- Set a savepoint
SAVEPOINT s1;

-- Update the booking document to include a user
UPDATE bookings AS b
USE KEYS "42641d7a-cde3-4a4d-bfd5-fec321510f70"
SET b.`user` = "0";

-- Check the content of the booking and user
SELECT b.*, u.name
FROM bookings b
USE KEYS "42641d7a-cde3-4a4d-bfd5-fec321510f70"
JOIN users u
ON KEYS b.`user`;

-- Set a second savepoint
SAVEPOINT s2;

-- Update the booking documents to change the user
UPDATE bookings AS b
USE KEYS "42641d7a-cde3-4a4d-bfd5-fec321510f70"
SET b.`user` = "1";

-- Check the content of the booking and user
SELECT b.*, u.name
FROM bookings b
USE KEYS "42641d7a-cde3-4a4d-bfd5-fec321510f70"
JOIN users u
ON KEYS b.`user`;

-- Roll back the transaction to the second savepoint
ROLLBACK TRANSACTION TO SAVEPOINT s2;

-- Check the content of the booking and user again
SELECT b.*, u.name
FROM bookings b
USE KEYS "42641d7a-cde3-4a4d-bfd5-fec321510f70"
JOIN users u
ON KEYS b.`user`;

-- Roll back the entire transaction
ROLLBACK TRANSACTION;
```

Results

```json
cbq> -- Start the transaction
cbq> BEGIN TRANSACTION;
{
    "requestID": "f805c9b5-d772-467a-b04f-fbaf3a3d25ad",
    "signature": "json",
    "results": [
    {
        "nodeUUID": "9803422b02fd9e6c9e7156b8ddb2d840",
        "txid": "c202bfd7-5a48-46e5-bd78-8d36a7bafde9"
    }
    ],
    "status": "success",
    "metrics": {
        "elapsedTime": "10.074958ms",
        "executionTime": "9.617791ms",
        "resultCount": 1,
        "resultSize": 118,
        "serviceLoad": 3,
        "transactionElapsedTime": "8.30125ms",
        "transactionRemainingTime": "1m59.991689125s"
    }
}
cbq>
cbq> -- Specify transaction settings
cbq> SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
{
    "requestID": "e1bae101-640f-4274-8f01-66f8d6af9256",
    "signature": "json",
    "results": [
    ],
    "status": "success",
    "metrics": {
        "elapsedTime": "327µs",
        "executionTime": "212.125µs",
        "resultCount": 0,
        "resultSize": 0,
        "serviceLoad": 0,
        "transactionElapsedTime": "11.105959ms",
        "transactionRemainingTime": "1m59.988890208s"
    }
}
cbq>
cbq> -- Create a booking document
cbq> UPSERT INTO bookings
   > VALUES("42641d7a-cde3-4a4d-bfd5-fec321510f70", {
   >   "date": "07/24/2021",
   >   "flight": "WN533",
   >   "flighttime": 7713,
   >   "price": 964.13,
   >   "route": "63986"
   > });
{
    "requestID": "5ddabc64-866f-483c-8d76-db66ca27a759",
    "signature": null,
    "results": [
    ],
    "status": "success",
    "metrics": {
        "elapsedTime": "1.076084ms",
        "executionTime": "1.015ms",
        "resultCount": 0,
        "resultSize": 0,
        "serviceLoad": 0,
        "mutationCount": 1,
        "transactionElapsedTime": "13.296584ms",
        "transactionRemainingTime": "1m59.986700083s"
    }
}
cbq>
cbq> -- Set a savepoint
cbq> SAVEPOINT s1;
{
    "requestID": "3eb22544-5aa4-40b8-b948-ee7c517ad6c4",
    "signature": "json",
    "results": [
    ],
    "status": "success",
    "metrics": {
        "elapsedTime": "314.375µs",
        "executionTime": "205µs",
        "resultCount": 0,
        "resultSize": 0,
        "serviceLoad": 0,
        "transactionElapsedTime": "14.777709ms",
        "transactionRemainingTime": "1m59.98522s"
    }
}
cbq>
cbq> -- Update the booking document to include a user
cbq> UPDATE bookings AS b
   > USE KEYS "42641d7a-cde3-4a4d-bfd5-fec321510f70"
   > SET b.`user` = "0";
{
    "requestID": "4b0fe1b6-104f-495b-a0bb-6fab253c6db7",
    "signature": null,
    "results": [
    ],
    "status": "success",
    "metrics": {
        "elapsedTime": "606.583µs",
        "executionTime": "562.666µs",
        "resultCount": 0,
        "resultSize": 0,
        "serviceLoad": 0,
        "mutationCount": 1,
        "transactionElapsedTime": "16.228375ms",
        "transactionRemainingTime": "1m59.983768625s"
    }
}
cbq>
cbq> -- Check the content of the booking and user
cbq> SELECT b.*, u.name
   > FROM bookings b
   > USE KEYS "42641d7a-cde3-4a4d-bfd5-fec321510f70"
   > JOIN users u
   > ON KEYS b.`user`;
{
    "requestID": "a30e07c4-bcb4-4b89-8f3e-b6cdeb1c5e90",
    "signature": {
        "*": "*",
        "name": "json"
    },
    "results": [
    {
        "date": "07/24/2021",
        "flight": "WN533",
        "flighttime": 7713,
        "price": 964.13,
        "route": "63986",
        "user": "0", (1)
        "name": "Keon Hoppe"
    }
    ],
    "status": "success",
    "metrics": {
        "elapsedTime": "2.025708ms",
        "executionTime": "1.957291ms",
        "resultCount": 1,
        "resultSize": 193,
        "serviceLoad": 0,
        "transactionElapsedTime": "19.637375ms",
        "transactionRemainingTime": "1m59.980359458s"
    }
}
cbq>
cbq> -- Set a second savepoint
cbq> SAVEPOINT s2;
{
    "requestID": "a47c1035-ab53-45b6-9cc0-f62a161b5fe8",
    "signature": "json",
    "results": [
    ],
    "status": "success",
    "metrics": {
        "elapsedTime": "139.792µs",
        "executionTime": "104.667µs",
        "resultCount": 0,
        "resultSize": 0,
        "serviceLoad": 0,
        "transactionElapsedTime": "21.032834ms",
        "transactionRemainingTime": "1m59.978965083s"
    }
}
cbq>
cbq> -- Update the booking documents to change the user
cbq> UPDATE bookings AS b
   > USE KEYS "42641d7a-cde3-4a4d-bfd5-fec321510f70"
   > SET b.`user` = "1";
{
    "requestID": "e79410d6-d5e3-433b-a848-59c3e11f09de",
    "signature": null,
    "results": [
    ],
    "status": "success",
    "metrics": {
        "elapsedTime": "314.625µs",
        "executionTime": "275.625µs",
        "resultCount": 0,
        "resultSize": 0,
        "serviceLoad": 0,
        "mutationCount": 1,
        "transactionElapsedTime": "22.070584ms",
        "transactionRemainingTime": "1m59.977926666s"
    }
}
cbq>
cbq> -- Check the content of the booking and user
cbq> SELECT b.*, u.name
   > FROM bookings b
   > USE KEYS "42641d7a-cde3-4a4d-bfd5-fec321510f70"
   > JOIN users u
   > ON KEYS b.`user`;
{
    "requestID": "1fd5601b-e819-43be-a68e-60858ed12ec3",
    "signature": {
        "*": "*",
        "name": "json"
    },
    "results": [
    {
        "date": "07/24/2021",
        "flight": "WN533",
        "flighttime": 7713,
        "price": 964.13,
        "route": "63986",
        "user": "1", (2)
        "name": "Rigoberto Bernier"
    }
    ],
    "status": "success",
    "metrics": {
        "elapsedTime": "1.770875ms",
        "executionTime": "1.744375ms",
        "resultCount": 1,
        "resultSize": 200,
        "serviceLoad": 0,
        "transactionElapsedTime": "24.681959ms",
        "transactionRemainingTime": "1m59.975315916s"
    }
}
cbq>
cbq> -- Roll back the transaction to the second savepoint
cbq> ROLLBACK TRANSACTION TO SAVEPOINT s2;
{
    "requestID": "ac2e9b13-33f3-4241-9a00-1f908457f4b0",
    "signature": "json",
    "results": [
    ],
    "status": "success",
    "metrics": {
        "elapsedTime": "257µs",
        "executionTime": "177.167µs",
        "resultCount": 0,
        "resultSize": 0,
        "serviceLoad": 0,
        "transactionElapsedTime": "88.869667ms",
        "transactionRemainingTime": "1m59.911126791s"
    }
}
cbq>
cbq> -- Check the content of the booking and user again
cbq> SELECT b.*, u.name
   > FROM bookings b
   > USE KEYS "42641d7a-cde3-4a4d-bfd5-fec321510f70"
   > JOIN users u
   > ON KEYS b.`user`;
{
    "requestID": "4b78450e-3bf7-449b-b7c0-d682511b47c7",
    "signature": {
        "*": "*",
        "name": "json"
    },
    "results": [
    {
        "date": "07/24/2021",
        "flight": "WN533",
        "flighttime": 7713,
        "price": 964.13,
        "route": "63986",
        "user": "0", (3)
        "name": "Keon Hoppe"
    }
    ],
    "status": "success",
    "metrics": {
        "elapsedTime": "757.375µs",
        "executionTime": "728.25µs",
        "resultCount": 1,
        "resultSize": 193,
        "serviceLoad": 0,
        "transactionElapsedTime": "90.762584ms",
        "transactionRemainingTime": "1m59.909234916s"
    }
}
cbq>
cbq> -- Roll back the entire transaction
cbq> ROLLBACK TRANSACTION;
{
    "requestID": "b62038bf-467f-435f-abb4-bbca92a7d446",
    "signature": "json",
    "results": [
    ],
    "status": "success",
    "metrics": {
        "elapsedTime": "539.958µs",
        "executionTime": "434µs",
        "resultCount": 0,
        "resultSize": 0,
        "serviceLoad": 0,
        "transactionElapsedTime": "1.002745501s"
    }
  }
  }
]
}
]
```

| **1** | Before setting the second savepoint, the booking document has user "0", name "Keon Hoppe".                                |
| ----- | ------------------------------------------------------------------------------------------------------------------------- |
| **2** | After setting the second savepoint and performing an update, the booking document has user "1", name "Rigoberto Bernier". |
| **3** | After rolling back to the second savepoint, the booking document again has user "0", name "Keon Hoppe".                   |

Example 2\. Check the result of [Example 1](#ex-1)

Check the result of rolling back the transaction.

Query

```sqlpp
SELECT b.*, u.name
FROM bookings b
USE KEYS "42641d7a-cde3-4a4d-bfd5-fec321510f70"
JOIN users u
ON KEYS b.`user`;
```

Results

```json
{
  "results": []
}
```

Notice the booking document no longer exists.

## [](#related-links)Related Links

* For an overview of Couchbase transactions, see [Transactions](../../../server/current/learn/data/transactions.md).
* To begin a transaction, see [BEGIN TRANSACTION](begin-transaction.md).
* To specify transaction settings, see [SET TRANSACTION](set-transaction.md).
* To set a savepoint, see [SAVEPOINT](savepoint.md).
* To commit a transaction, see [COMMIT TRANSACTION](commit-transaction.md).
* Blog post: [Couchbase Transactions: Elastic, Scalable, and Distributed](https://blog.couchbase.com/transactions-n1ql-couchbase-distributed-nosql/).