---
title: SQL++ Support for Couchbase Transactions
description: SQL++ offers full support for Couchbase ACID transactions based on
  optimistic concurrency.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/n1ql/pages/n1ql-language-reference/transactions.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:n1ql:n1ql-language-reference/transactions.adoc[]
---

[View original HTML](/cloud/n1ql/n1ql-language-reference/transactions.html)

# SQL++ Support for Couchbase Transactions

> SQL++ offers full support for Couchbase ACID transactions based on optimistic concurrency. 

A transaction is a group of operations that are either committed to the database together, or are all undone from the database if there’s a failure. For an overview of Couchbase transactions, see [Transactions](../../../server/current/learn/data/transactions.md).

* Only DML statements are permitted within a transaction: [INSERT](insert.md), [UPSERT](upsert.md), [DELETE](delete.md), [UPDATE](update.md), [MERGE](merge.md), [SELECT](selectintro.md), [EXECUTE FUNCTION](execfunction.md), [PREPARE](prepare.md), or [EXECUTE](execute.md).
* The `EXECUTE FUNCTION` statement is only permitted in a transaction if the user-defined function does not contain any subqueries other than `SELECT` subqueries.
* The `PREPARE` and `EXECUTE` statements are only permitted in a transaction for the DML statements listed above.

All statements within a transaction are sent to the same Query node. If your cluster uses private endpoints, the load balancer ensures that the same query node carries out all the steps in the transaction.

## [](#statements)Statements

SQL++ provides the following statements in support of Couchbase transactions. See the documentation for each statement for more information and examples.

* To begin a transaction, see [BEGIN TRANSACTION](begin-transaction.md).
* To specify transaction settings, see [SET TRANSACTION](set-transaction.md).
* To set a savepoint, see [SAVEPOINT](savepoint.md).
* To rollback a transaction, see [ROLLBACK TRANSACTION](rollback-transaction.md).
* To commit a transaction, see [COMMIT TRANSACTION](commit-transaction.md).

## [](#settings-and-parameters)Settings and Parameters

The Query Service provides settings and parameters in support of Couchbase transactions. For more information and examples, see the documentation for each parameter.

| Setting / Parameter                                                                              | Description                                                                                   |
| ------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------- |
| [txid](../n1ql-manage/query-settings.md#txid) request-level parameter                            | Specifies the transaction to which a statement belongs.                                       |
| [tximplicit](../n1ql-manage/query-settings.md#tximplicit) request-level parameter                | Specifies that a statement is a single transaction.                                           |
| [txstmtnum](../n1ql-manage/query-settings.md#txstmtnum) request-level parameter                  | Specifies the transaction statement number.                                                   |
| [kvtimeout](../n1ql-manage/query-settings.md#kvtimeout) request-level parameter                  | Specifies the maximum time to spend on a KV operation within a transaction before timing out. |
| [durability\_level](../n1ql-manage/query-settings.md#durability%5Flevel) request-level parameter | Specifies the transactional durability level.                                                 |
| [txtimeout](../n1ql-manage/query-settings.md#txtimeout%5Freq) request-level parameter            | Specify the maximum time to spend on a transaction before timing out.                         |
| [atrcollection](../n1ql-manage/query-settings.md#atrcollection%5Freq) request-level parameter    | Specify where the active transaction record is stored.                                        |

In addition, use the [scan-consistency](../n1ql-manage/query-settings.md#scan%5Fconsistency) request-level parameter to specify the transactional scan consistency. For more information, see [Transactional Scan Consistency](../n1ql-manage/query-settings.md#transactional-scan-consistency).

## [](#query-tools)Query Tools

To create a Couchbase transaction using SQL++, you can use:

* The [cbq shell](../n1ql-intro/cbq.md)

Some Couchbase SDKs provide APIs to support Couchbase transactions. For more information, see [Transactions](../../../server/current/learn/data/transactions.md) in the Server documentation.

> [!NOTE]
> Couchbase Transactions are not supported via the Couchbase Capella Query tab or the Data API (Query Service passthrough). The Query Service requires that the whole transaction must be executed by a single node, and there is currently no way for the Query tab or the Data API to enforce this.

### [](#couchbase-transactions-with-the-cbq-shell)Couchbase Transactions with the cbq shell

* To execute a transaction containing multiple statements, you can create the transaction one statement at a time. Once you have started a transaction, all statements within the cbq shell session are assumed to be part of the same transaction until you rollback or commit the transaction. In this case, you do not need to set the `txid` parameter. \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]
* Alternatively, you can use the `tximplicit` parameter to run a single statement as a transaction. In this case, you do not need to specify the `txid` parameter either.
* You can specify parameters for the Couchbase transaction using the `\SET` command.

## [](#monitoring)Monitoring

You can monitor active Couchbase transactions using the `system:transactions` catalog. For more information, see [system:transactions](../n1ql-intro/sysinfo.md#sys-transactions).

## [](#permissions)Permissions

When developing a transaction with an SDK, the transaction may contain a mixture of key-value operations and query statements.

To execute key-value operations or query statements within a transaction, users must have the relevant cluster access privileges, with permissions on the relevant buckets, scopes and collections.

See [Manage Cluster Access Credentials](../../clusters/manage-database-users.md) for details.

## [](#worked-example)Worked Example

This worked example guides you through a complete Couchbase transaction session using SQL++.

### [](#preparation)Preparation

The worked example assumes that the supplied `travel-sample` bucket is installed. For more information, see [Import Sample Data](../../clusters/data-service/import-data-documents.md#import-sample-data).

Context

For this worked example, set the query context to the `tenant_agent_00` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

* CBQ Shell

```sqlpp
\SET -query_context travel-sample.tenant_agent_00;
```

Parameters

If necessary, set the transaction parameters for this worked example. In particular, turn off durability for the purposes of this example, to make sure that there are no problems meeting the transaction durability requirements.

* CBQ Shell

Enter the following parameters.

```sqlpp
\SET -txtimeout "2m"; (1)
\SET -scan_consistency "not_bounded"; (2)
\SET -durability_level "none"; (3)
```

| **1** | The transaction timeout.                                                                                                                                           |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **2** | The transaction scan consistency. No scan consistency is set for individual statements within the transaction; they inherit from the transaction scan consistency. |
| **3** | Durability level of all the mutations within the transaction.                                                                                                      |

### [](#transaction)Transaction

Example 1\. Transaction with multiple statements

Copy the entire sequence below and paste it into the [cbq shell](../n1ql-intro/cbq.md). You must be using cbq shell version 2.0 or above.

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

The results of running the transaction are shown below.

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

Beginning a transaction returns a unique transaction ID `txid`.

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

Before setting the second savepoint, the booking document has user `"0"`, name `"Keon Hoppe"`.

```json
// ...
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
        "user": "1", (1)
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
// ...
```

After setting the second savepoint and performing an update, the booking document has user `"1"`, name `"Rigoberto Bernier"`.

```json
// ...
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
        "user": "0", (1)
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

After rolling back to the second savepoint, the booking document again has user `"0"`, name `"Keon Hoppe"`.

Example 2\. Check the results of [Example 1](#ex-1)

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

The booking document has been added with the attributes that were present when the transaction was committed.

## [](#related-links)Related Links

* Blog post: [Couchbase Transactions: Elastic, Scalable, and Distributed](https://blog.couchbase.com/transactions-n1ql-couchbase-distributed-nosql/).

---

[1](#%5Ffootnoteref%5F1). You must be using cbq shell version 2.0 or above to use the automatic transaction ID functionality.