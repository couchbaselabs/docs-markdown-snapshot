---
title: SET TRANSACTION
description: The SET TRANSACTION statement enables you to specify settings for a
  transaction.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/n1ql/pages/n1ql-language-reference/set-transaction.adoc
  xref: xref:7.2@server:n1ql:n1ql-language-reference/set-transaction.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/n1ql/n1ql-language-reference/set-transaction.html)

# SET TRANSACTION

> The SET TRANSACTION statement enables you to specify settings for a transaction. 

## [](#purpose)Purpose

The `SET TRANSACTION` statement enables you to specify settings for an ACID transaction. Refer to [SQL++ Support for Couchbase Transactions](transactions.md) for further information.

This statement may only be used within a transaction.

If you are using the Query REST API, you must set the [txid](../../settings/query-settings.md#txid) query parameter to specify the transaction ID.

If you are using the Query Workbench, you don't need to specify the transaction ID, as long as the statement is part of a multi-statement request. When you start a transaction within a multi-statement request, all statements within the request are assumed to be part of the same transaction until you rollback or commit the transaction.

Similarly, if you are using the cbq shell, you don't need to specify the transaction ID. Once you have started a transaction, all statements within the cbq shell session are assumed to be part of the same transaction until you rollback or commit the transaction. \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]

You may also optionally specify settings when you start the transaction using the `BEGIN TRANSACTION` command.

> [!NOTE]
> Currently, the only available transaction setting is "isolation level read committed". This setting is enabled by default. The `SET TRANSACTION` statement is therefore optional and may be omitted.

## [](#syntax)Syntax

```ebnf
set-transaction ::= 'SET' 'TRANSACTION' 'ISOLATION' 'LEVEL' 'READ' 'COMMITTED'
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/set-transaction.png) 

## [](#example)Example

If you want to try this example, first refer to [Preparation](transactions.md#preparation) to set up your environment.

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
[
  {
    "_sequence_num": 1,
    "_sequence_query": "-- Start the transaction\nBEGIN TRANSACTION;",
    "_sequence_query_status": "success",
    "_sequence_result": [
      {
        "txid": "d81d9b4a-b758-4f98-b007-87ba262d3a51" (1)
      }
    ]
  },
  {
    "_sequence_num": 2,
    "_sequence_query": "\n\n-- Specify transaction settings\nSET TRANSACTION ISOLATION LEVEL READ COMMITTED;",
    "_sequence_query_status": "success",
    "_sequence_result": {
      "results": []
    }
  },
  {
    "_sequence_num": 3,
    "_sequence_query": "\n\n-- Create a booking document\nUPSERT INTO bookings\nVALUES(\"bf7ad6fa-bdb9-4099-a840-196e47179f03\", {\n  \"date\": \"07/24/2021\",\n  \"flight\": \"WN533\",\n  \"flighttime\": 7713,\n  \"price\": 964.13,\n  \"route\": \"63986\"\n});",
    "_sequence_query_status": "success",
    "_sequence_result": {
      "results": []
    }
  },
// ...
```

| **1** | Beginning a transaction returns a transaction ID. |
| ----- | ------------------------------------------------- |

## [](#related-links)Related Links

* For an overview of Couchbase transactions, refer to [Transactions](../../learn/data/transactions.md).
* To begin a transaction, refer to [BEGIN TRANSACTION](begin-transaction.md).
* To set a savepoint, refer to [SAVEPOINT](savepoint.md).
* To rollback a transaction, refer to [ROLLBACK TRANSACTION](rollback-transaction.md).
* To commit a transaction, refer to [COMMIT TRANSACTION](commit-transaction.md).
* Blog post: [Couchbase Transactions: Elastic, Scalable, and Distributed](https://blog.couchbase.com/transactions-n1ql-couchbase-distributed-nosql/).

---

[1](#%5Ffootnoteref%5F1). You must be using cbq shell version 2.0 or above to use the automatic transaction ID functionality.