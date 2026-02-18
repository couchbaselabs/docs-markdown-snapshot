---
title: BEGIN TRANSACTION
description: The BEGIN TRANSACTION statement enables you to begin a transaction.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/n1ql/pages/n1ql-language-reference/begin-transaction.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/cloud/n1ql/n1ql-language-reference/begin-transaction.html)

# BEGIN TRANSACTION

> The BEGIN TRANSACTION statement enables you to begin a transaction. 

## [](#purpose)Purpose

The `BEGIN TRANSACTION` statement enables you to begin a sequence of statements as an ACID transaction. For more information, see [SQL++ Support for Couchbase Transactions](transactions.md).

* Only DML statements are permitted within a transaction: [INSERT](insert.md), [UPSERT](upsert.md), [DELETE](delete.md), [UPDATE](update.md), [MERGE](merge.md), [SELECT](selectintro.md), [EXECUTE FUNCTION](execfunction.md), [PREPARE](prepare.md), or [EXECUTE](execute.md).
* The `EXECUTE FUNCTION` statement is only permitted in a transaction if the user-defined function does not contain any subqueries other than `SELECT` subqueries.
* The `PREPARE` and `EXECUTE` statements are only permitted in a transaction for the DML statements listed above.

All statements within a transaction are sent to the same Query node. If your cluster uses private endpoints, the load balancer ensures that the same query node carries out all the steps in the transaction.

> [!NOTE]
> You can also specify a single DML statement as an ACID transaction by setting the [tximplicit](../n1ql-manage/query-settings.md#tximplicit) query parameter.

## [](#syntax)Syntax

```ebnf
begin-transaction ::= ( 'BEGIN' | 'START' ) ( 'WORK' | 'TRAN' | 'TRANSACTION' )
                      ( 'ISOLATION' 'LEVEL' 'READ' 'COMMITTED' )?
```

![Syntax diagram: see source code listing](../_images/n1ql-language-reference/begin-transaction.png) 

The `BEGIN` and `START` keywords are synonyms. The statement must begin with one of these keywords.

The `WORK`, `TRAN`, and `TRANSACTION` keywords are synonyms. The statement must contain one of these keywords.

### [](#transaction-settings)Transaction Settings

Currently, the only available transaction setting is `ISOLATION LEVEL READ COMMITTED`. This setting is enabled by default. The `ISOLATION LEVEL READ COMMITTED` keywords are therefore optional and may be omitted.

## [](#return-value)Return Value

The statement returns an object containing the following properties.

| Name                    | Description                                            | Schema |
| ----------------------- | ------------------------------------------------------ | ------ |
| **nodeUUID** _required_ | The UUID of the Query node performing the transaction. | String |
| **txid** _required_     | The transaction ID.                                    | String |

If you’re using the cbq shell, you do not need to specify the transaction ID for any statements that form a part of the same transaction. Once you have started a transaction, all statements within the cbq shell session are assumed to be part of the same transaction until you rollback or commit the transaction. \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]

## [](#example)Example

If you want to try this example, first see [Preparation](transactions.md#preparation) to set up your environment.

Example 1\. Begin a transaction

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
// ...
```

| **1** | Beginning a transaction returns a transaction ID. |
| ----- | ------------------------------------------------- |

## [](#related-links)Related Links

* For an overview of Couchbase transactions, see [Transactions](../../../server/current/learn/data/transactions.md).
* To specify transaction settings, see [SET TRANSACTION](set-transaction.md).
* To set a savepoint, see [SAVEPOINT](savepoint.md).
* To rollback a transaction, see [ROLLBACK TRANSACTION](rollback-transaction.md).
* To commit a transaction, see [COMMIT TRANSACTION](commit-transaction.md).
* Blog post: [Couchbase Transactions: Elastic, Scalable, and Distributed](https://blog.couchbase.com/transactions-n1ql-couchbase-distributed-nosql/).

---

[1](#%5Ffootnoteref%5F1). You must be using cbq shell version 2.0 or above to use the automatic transaction ID functionality.