---
title: COMMIT TRANSACTION
description: The COMMIT TRANSACTION statement enables you to commit a transaction.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/n1ql/pages/n1ql-language-reference/commit-transaction.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/cloud/n1ql/n1ql-language-reference/commit-transaction.html)

# COMMIT TRANSACTION

> The COMMIT TRANSACTION statement enables you to commit a transaction. 

## [](#purpose)Purpose

The `COMMIT TRANSACTION` statement enables you to commit an ACID transaction. For more information, see [SQL++ Support for Couchbase Transactions](transactions.md).

This statement removes all savepoints within the transaction.

> [!NOTE]
> If you’re using the cbq shell, and a transaction fails for any reason, you must use the `ROLLBACK TRANSACTION` statement to remove the transaction context and reset the transaction ID.

## [](#syntax)Syntax

```ebnf
commit-transaction ::= 'COMMIT' ( 'WORK' | 'TRAN' | 'TRANSACTION' )?
```

![Syntax diagram: see source code listing](../_images/n1ql-language-reference/commit-transaction.png) 

The `WORK`, `TRAN`, and `TRANSACTION` keywords are synonyms. These keywords are optional; you may include one of these keywords, or omit them entirely.

## [](#usage)Usage

The transaction can only be committed if the transactional [durability](../../../server/current/learn/data/durability.md) requirements can be met. The transaction durability level is set by the request-level [durability\_level](../n1ql-manage/query-settings.md#durability%5Flevel) parameter.

If transaction durability requirements cannot be met, then a 161 error code is generated when you attempt to commit the transaction, stating that the durability requirements are impossible to achieve. For example: bucket replication is specified, but there are not enough Data nodes available on which to store the specified number of replicas at the requested durability level.

To avoid this error, it’s recommended that you add the correct number of Data nodes for the required durability level, and rebalance. As a temporary measure, you can set the request-level [durability\_level](../n1ql-manage/query-settings.md#durability%5Flevel) parameter to `"none"` to turn off durability for this request, or [turn off bucket replication](../../clusters/data-service/manage-buckets.md).

## [](#examples)Examples

If you want to try these examples, first see [Preparation](transactions.md#preparation) to set up your environment.

Example 1\. Commit a transaction

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
cbq> -- Start the transaction
cbq> BEGIN TRANSACTION;
{
    "requestID": "da8567c3-d2d3-4d32-807b-c7e898f66611",
    "signature": "json",
    "results": [
    {
        "nodeUUID": "9803422b02fd9e6c9e7156b8ddb2d840",
        "txid": "fab2bd20-322e-4ed0-bc4e-035db995f349" (1)
    }
    ],
    "status": "success",
    "metrics": {
        "elapsedTime": "6.8305ms",
        "executionTime": "6.603708ms",
        "resultCount": 1,
        "resultSize": 118,
        "serviceLoad": 3,
        "transactionElapsedTime": "6.046625ms",
        "transactionRemainingTime": "1m59.993945125s"
    }
}
cbq> 
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
        "user": "0", (2)
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
cbq> -- Set a second savepoint
cbq> SAVEPOINT s2;
{
    "requestID": "c4084621-f542-41cf-9990-06bedcd19583",
    "signature": "json",
    "results": [
    ],
    "status": "success",
    "metrics": {
        "elapsedTime": "117.125µs",
        "executionTime": "81.167µs",
        "resultCount": 0,
        "resultSize": 0,
        "serviceLoad": 0,
        "transactionElapsedTime": "28.638375ms",
        "transactionRemainingTime": "1m59.971360583s"
    }
}
cbq> 
cbq> -- Update the booking documents to change the user
cbq> UPDATE bookings AS b
   > USE KEYS "bf7ad6fa-bdb9-4099-a840-196e47179f03"
   > SET b.`user` = "1";
{
    "requestID": "4277b2e3-2525-4ff9-ae04-10ba22aa9d8b",
    "signature": null,
    "results": [
    ],
    "status": "success",
    "metrics": {
        "elapsedTime": "240.458µs",
        "executionTime": "210µs",
        "resultCount": 0,
        "resultSize": 0,
        "serviceLoad": 0,
        "mutationCount": 1,
        "transactionElapsedTime": "29.538ms",
        "transactionRemainingTime": "1m59.970460542s"
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
    "requestID": "11ed6da0-da52-4b79-bb74-da1db8b3a816",
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
        "user": "1", (3)
        "name": "Rigoberto Bernier"
    }
    ],
    "status": "success",
    "metrics": {
        "elapsedTime": "451.959µs",
        "executionTime": "424.417µs",
        "resultCount": 1,
        "resultSize": 200,
        "serviceLoad": 0,
        "transactionElapsedTime": "30.652417ms",
        "transactionRemainingTime": "1m59.969346583s"
    }
}
cbq> 
cbq> -- Roll back the transaction to the second savepoint
cbq> ROLLBACK TRANSACTION TO SAVEPOINT s2;
{
    "requestID": "2ffe8d3b-85f2-4ec2-b7e1-8d774cba1065",
    "signature": "json",
    "results": [
    ],
    "status": "success",
    "metrics": {
        "elapsedTime": "230.458µs",
        "executionTime": "167.458µs",
        "resultCount": 0,
        "resultSize": 0,
        "serviceLoad": 0,
        "transactionElapsedTime": "99.111083ms",
        "transactionRemainingTime": "1m59.900884792s"
    }
}
cbq> 
cbq> -- Check the content of the booking and user again
cbq> SELECT b.*, u.name
   > FROM bookings b
   > USE KEYS "bf7ad6fa-bdb9-4099-a840-196e47179f03"
   > JOIN users u
   > ON KEYS b.`user`;
{
    "requestID": "eb45600b-e2e1-4ca4-aa56-3552ae4141eb",
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
        "user": "0", (4)
        "name": "Keon Hoppe"
    }
    ],
    "status": "success",
    "metrics": {
        "elapsedTime": "660.25µs",
        "executionTime": "621.792µs",
        "resultCount": 1,
        "resultSize": 193,
        "serviceLoad": 0,
        "transactionElapsedTime": "100.6895ms",
        "transactionRemainingTime": "1m59.899308625s"
    }
}
cbq> 
cbq> -- Commit the transaction
cbq> COMMIT TRANSACTION;
{
    "requestID": "126f4882-7fe0-46a8-b0c1-5cf0a74dade8",
    "signature": "json",
    "results": [
    ],
    "status": "success",
    "metrics": {
        "elapsedTime": "20.328375ms",
        "executionTime": "20.075042ms",
        "resultCount": 0,
        "resultSize": 0,
        "serviceLoad": 0,
        "transactionElapsedTime": "953.673167ms"
    }
}
```

| **1** | Beginning a transaction returns a transaction ID.                                                                         |
| ----- | ------------------------------------------------------------------------------------------------------------------------- |
| **2** | Before setting the second savepoint, the booking document has user "0", name "Keon Hoppe".                                |
| **3** | After setting the second savepoint and performing an update, the booking document has user "1", name "Rigoberto Bernier". |
| **4** | After rolling back to the second savepoint, the booking document again has user "0", name "Keon Hoppe".                   |

Example 2\. Check the result of [Example 1](#ex-1)

Check the result of committing the transaction.

Query

```sqlpp
SELECT b.*, u.name
FROM bookings b
USE KEYS "bf7ad6fa-bdb9-4099-a840-196e47179f03"
JOIN users u
ON KEYS b.`user`;
```

Results

```json
{
    "date": "07/24/2021",
    "flight": "WN533",
    "flighttime": 7713,
    "price": 964.13,
    "route": "63986",
    "user": "0", (1)
    "name": "Keon Hoppe"
}
```

| **1** | The booking document has been added with the attributes that were present when the transaction was committed. |
| ----- | ------------------------------------------------------------------------------------------------------------- |

## [](#related-links)Related Links

* For an overview of Couchbase transactions, see [Transactions](../../../server/current/learn/data/transactions.md).
* To begin a transaction, see [BEGIN TRANSACTION](begin-transaction.md).
* To specify transaction settings, see [SET TRANSACTION](set-transaction.md).
* To set a savepoint, see [SAVEPOINT](savepoint.md).
* To rollback a transaction, see [ROLLBACK TRANSACTION](rollback-transaction.md).
* Blog post: [Couchbase Transactions: Elastic, Scalable, and Distributed](https://blog.couchbase.com/transactions-n1ql-couchbase-distributed-nosql/).