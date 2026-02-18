---
title: SET TRANSACTION
description: The SET TRANSACTION statement enables you to specify settings for a
  transaction.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/n1ql/pages/n1ql-language-reference/set-transaction.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/cloud/n1ql/n1ql-language-reference/set-transaction.html)

# SET TRANSACTION

> The SET TRANSACTION statement enables you to specify settings for a transaction. 

## [](#purpose)Purpose

The `SET TRANSACTION` statement enables you to specify settings for an ACID transaction. For more information, see [SQL++ Support for Couchbase Transactions](transactions.md).

You may only use this statement within a transaction.

You may also optionally specify settings when you start the transaction using the `BEGIN TRANSACTION` command.

> [!NOTE]
> Currently, the only available transaction setting is `ISOLATION LEVEL READ COMMITTED`. This setting is enabled by default. The `SET TRANSACTION` statement is therefore optional and may be omitted.

## [](#syntax)Syntax

```ebnf
set-transaction ::= 'SET' 'TRANSACTION' 'ISOLATION' 'LEVEL' 'READ' 'COMMITTED'
```

![Syntax diagram: see source code listing](../_images/n1ql-language-reference/set-transaction.png) 

## [](#example)Example

If you want to try this example, first see [Preparation](transactions.md#preparation) to set up your environment.

Example 1\. Specify transaction settings

Transaction

```sqlpp
-- Start the transaction
BEGIN TRANSACTION;

-- Specify transaction settings
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;

-- Create a booking document
UPSERT INTO bookings
VALUES("bf7ad6fa-bdb9-4099-a840-196e47179f03", {
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
USE KEYS "bf7ad6fa-bdb9-4099-a840-196e47179f03"
SET b.`user` = "0";

-- Check the content of the booking and user
SELECT b.*, u.name
FROM bookings b
USE KEYS "bf7ad6fa-bdb9-4099-a840-196e47179f03"
JOIN users u
ON KEYS b.`user`;

-- Set a second savepoint
SAVEPOINT s2;

-- Update the booking documents to change the user
UPDATE bookings AS b
USE KEYS "bf7ad6fa-bdb9-4099-a840-196e47179f03"
SET b.`user` = "1";

-- Check the content of the booking and user
SELECT b.*, u.name
FROM bookings b
USE KEYS "bf7ad6fa-bdb9-4099-a840-196e47179f03"
JOIN users u
ON KEYS b.`user`;

-- Roll back the transaction to the second savepoint
ROLLBACK TRANSACTION TO SAVEPOINT s2;

-- Check the content of the booking and user again
SELECT b.*, u.name
FROM bookings b
USE KEYS "bf7ad6fa-bdb9-4099-a840-196e47179f03"
JOIN users u
ON KEYS b.`user`;

-- Commit the transaction
COMMIT TRANSACTION;
```

Results

```json
// ...
cbq> -- Specify transaction settings
cbq> SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
{
    "requestID": "6ac24c82-76db-45f5-9f44-5a2cf15e1e34",
    "signature": "json",
    "results": [
    ],
    "status": "success",
    "metrics": {
        "elapsedTime": "231.666µs",
        "executionTime": "161.333µs",
        "resultCount": 0,
        "resultSize": 0,
        "serviceLoad": 0,
        "transactionElapsedTime": "9.523333ms",
        "transactionRemainingTime": "1m59.990474875s"
    }
}
cbq> 
cbq> -- Create a booking document
cbq> UPSERT INTO bookings
   > VALUES("bf7ad6fa-bdb9-4099-a840-196e47179f03", {
   >   "date": "07/24/2021",
   >   "flight": "WN533",
   >   "flighttime": 7713,
   >   "price": 964.13,
   >   "route": "63986"
   > });
{
    "requestID": "d34e0dba-b15c-407e-b2e5-082def71a6a9",
    "signature": null,
    "results": [
    ],
    "status": "success",
    "metrics": {
        "elapsedTime": "9.695625ms",
        "executionTime": "9.6555ms",
        "resultCount": 0,
        "resultSize": 0,
        "serviceLoad": 0,
        "mutationCount": 1,
        "transactionElapsedTime": "21.353333ms",
        "transactionRemainingTime": "1m59.97864225s"
    }
}
cbq> 
cbq> -- Set a savepoint
cbq> SAVEPOINT s1;
{
    "requestID": "1be8ab5b-c00a-4f1f-9891-55d17574d8ce",
    "signature": "json",
    "results": [
    ],
    "status": "success",
    "metrics": {
        "elapsedTime": "200.25µs",
        "executionTime": "134.209µs",
        "resultCount": 0,
        "resultSize": 0,
        "serviceLoad": 0,
        "transactionElapsedTime": "22.689167ms",
        "transactionRemainingTime": "1m59.977309042s"
    }
}
cbq> 
cbq> -- Update the booking document to include a user
cbq> UPDATE bookings AS b
   > USE KEYS "bf7ad6fa-bdb9-4099-a840-196e47179f03"
   > SET b.`user` = "0";
{
    "requestID": "e9476c21-113f-465c-ae40-d76931ba5aef",
    "signature": null,
    "results": [
    ],
    "status": "success",
    "metrics": {
        "elapsedTime": "1.35775ms",
        "executionTime": "1.217167ms",
        "resultCount": 0,
        "resultSize": 0,
        "serviceLoad": 0,
        "mutationCount": 1,
        "transactionElapsedTime": "25.2525ms",
        "transactionRemainingTime": "1m59.974745208s"
    }
}
cbq> 
cbq> -- Check the content of the booking and user
cbq> SELECT b.*, u.name
   > FROM bookings b
   > USE KEYS "bf7ad6fa-bdb9-4099-a840-196e47179f03"
   > JOIN users u
   > ON KEYS b.`user`;
{
    "requestID": "67974697-2614-4b8e-9c47-668bc183e1ea",
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
        "elapsedTime": "1.556667ms",
        "executionTime": "1.492667ms",
        "resultCount": 1,
        "resultSize": 193,
        "serviceLoad": 0,
        "transactionElapsedTime": "27.824292ms",
        "transactionRemainingTime": "1m59.972173917s"
    }
}
cbq> 
// ...
```

## [](#related-links)Related Links

* For an overview of Couchbase transactions, see [Transactions](../../../server/current/learn/data/transactions.md).
* To begin a transaction, see [BEGIN TRANSACTION](begin-transaction.md).
* To set a savepoint, see [SAVEPOINT](savepoint.md).
* To rollback a transaction, see [ROLLBACK TRANSACTION](rollback-transaction.md).
* To commit a transaction, see [COMMIT TRANSACTION](commit-transaction.md).
* Blog post: [Couchbase Transactions: Elastic, Scalable, and Distributed](https://blog.couchbase.com/transactions-n1ql-couchbase-distributed-nosql/).