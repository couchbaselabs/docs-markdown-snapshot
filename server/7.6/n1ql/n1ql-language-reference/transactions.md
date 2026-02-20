---
title: SQL++ Support for Couchbase Transactions
description: SQL++ offers full support for Couchbase ACID transactions based on
  optimistic concurrency.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/n1ql/pages/n1ql-language-reference/transactions.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.6@server:n1ql:n1ql-language-reference/transactions.adoc[]
---

[View original HTML](/server/7.6/n1ql/n1ql-language-reference/transactions.html)

# SQL++ Support for Couchbase Transactions

> SQL++ offers full support for Couchbase ACID transactions based on optimistic concurrency. 

A transaction is a group of operations that are either committed to the database together, or are all undone from the database if there’s a failure. Refer to [Transactions](../../learn/data/transactions.md) for an overview of Couchbase transactions.

* Only DML statements are permitted within a transaction: [INSERT](insert.md), [UPSERT](upsert.md), [DELETE](delete.md), [UPDATE](update.md), [MERGE](merge.md), [SELECT](selectintro.md), [EXECUTE FUNCTION](execfunction.md), [PREPARE](prepare.md), or [EXECUTE](execute.md).
* The `EXECUTE FUNCTION` statement is only permitted in a transaction if the user-defined function does not contain any subqueries other than `SELECT` subqueries.
* The `PREPARE` and `EXECUTE` statements are only permitted in a transaction for the DML statements listed above.

All statements within a transaction are sent to the same Query node.

## [](#statements)Statements

SQL++ provides the following statements in support of Couchbase transactions. Refer to the documentation for each statement for more information and examples.

* To begin a transaction, refer to [BEGIN TRANSACTION](begin-transaction.md).
* To specify transaction settings, refer to [SET TRANSACTION](set-transaction.md).
* To set a savepoint, refer to [SAVEPOINT](savepoint.md).
* To rollback a transaction, refer to [ROLLBACK TRANSACTION](rollback-transaction.md).
* To commit a transaction, refer to [COMMIT TRANSACTION](commit-transaction.md).

## [](#settings-and-parameters)Settings and Parameters

The Query service provides settings and parameters in support of Couchbase transactions. Refer to the documentation for each parameter for more information and examples.

| Setting / Parameter                                                                                                                                                                                                                                                                                                                                                                                                           | Description                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| [txid](../n1ql-manage/query-settings.md#txid) request-level parameter                                                                                                                                                                                                                                                                                                                                                         | Specifies the transaction to which a statement belongs.                                       |
| [tximplicit](../n1ql-manage/query-settings.md#tximplicit) request-level parameter                                                                                                                                                                                                                                                                                                                                             | Specifies that a statement is a single transaction.                                           |
| [txstmtnum](../n1ql-manage/query-settings.md#txstmtnum) request-level parameter                                                                                                                                                                                                                                                                                                                                               | Specifies the transaction statement number.                                                   |
| [kvtimeout](../n1ql-manage/query-settings.md#kvtimeout) request-level parameter                                                                                                                                                                                                                                                                                                                                               | Specifies the maximum time to spend on a KV operation within a transaction before timing out. |
| [durability\_level](../n1ql-manage/query-settings.md#durability%5Flevel) request-level parameter                                                                                                                                                                                                                                                                                                                              | Specifies the transactional durability level.                                                 |
| [txtimeout](../n1ql-manage/query-settings.md#txtimeout%5Freq) request-level parameter [txtimeout](../n1ql-manage/query-settings.md#txtimeout-srv) node-level setting [queryTxTimeout](../n1ql-manage/query-settings.md#queryTxTimeout) cluster-level setting                                                                                                                                                                  | Specify the maximum time to spend on a transaction before timing out.                         |
| [atrcollection](../n1ql-manage/query-settings.md#atrcollection%5Freq) request-level parameter [atrcollection](../n1ql-manage/query-settings.md#atrcollection-srv) node-level setting                                                                                                                                                                                                                                          | Specify where the active transaction record is stored.                                        |
| [cleanupclientattempts](../n1ql-manage/query-settings.md#cleanupclientattempts) node-level setting [queryCleanupClientAttempts](../n1ql-manage/query-settings.md#queryCleanupClientAttempts) cluster-level setting [cleanuplostattempts](../n1ql-manage/query-settings.md#cleanuplostattempts) node-level setting [queryCleanupLostAttempts](../n1ql-manage/query-settings.md#queryCleanupLostAttempts) cluster-level setting | Specify how expired transactions are cleaned up.                                              |
| [cleanupwindow](../n1ql-manage/query-settings.md#cleanupwindow) node-level setting [queryCleanupWindow](../n1ql-manage/query-settings.md#queryCleanupWindow) cluster-level setting                                                                                                                                                                                                                                            | Specify how frequently active transaction records are checked for cleanup.                    |
| [numatrs](../n1ql-manage/query-settings.md#numatrs-srv) node-level setting [queryNumAtrs](../n1ql-manage/query-settings.md#queryNumAtrs) cluster-level setting                                                                                                                                                                                                                                                                | Specify the total number of active transaction records.                                       |

In addition, the [scan-consistency](../n1ql-manage/query-settings.md#scan%5Fconsistency) request-level parameter is used to specify the transactional scan consistency. Refer to [Transactional Scan Consistency](../n1ql-manage/query-settings.md#transactional-scan-consistency) for details.

## [](#query-tools)Query Tools

To create a Couchbase transaction using SQL++, you can use any of the tools that you use to run a SQL++ query: the [Query Workbench](../../tools/query-workbench.md), the [cbq shell](../n1ql-intro/cbq.md), or the [Query REST API](../../n1ql-rest-query/index.md). There are slight differences in the way these tools operate when creating Couchbase transactions. These are explained in the sections below.

Note that some Couchbase SDKs provide APIs to support Couchbase transactions. For further details, refer to [Transactions](../../learn/data/transactions.md).

### [](#couchbase-transactions-with-the-query-workbench)Couchbase Transactions with the Query Workbench

* To execute a transaction containing multiple statements, compose the sequence of statements in the Query Editor. Each statement must be terminated with a semicolon. After each statement, you must press Shift+Enter to start a new line _without_ executing the query. You can then click **Execute** to execute the transaction.
* To execute a single statement as a transaction, simply enter the statement in the Query Editor and click **Run as TX**.
* In either case, you do not need to specify the `txid` parameter or the `tximplicit` parameter. If you need to specify any other parameters for the Couchbase transaction, you can use the query run-time preferences window.

### [](#couchbase-transactions-with-the-cbq-shell)Couchbase Transactions with the cbq shell

* To execute a transaction containing multiple statements, you can create the transaction one statement at a time. Once you have started a transaction, all statements within the cbq shell session are assumed to be part of the same transaction until you rollback or commit the transaction. In this case, you don’t need to set the `txid` parameter. \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]
* Alternatively, you can use the `tximplicit` parameter to run a single statement as a transaction. In this case, you do not need to specify the `txid` parameter either.
* You can specify parameters for the Couchbase transaction using the `\SET` command.

### [](#couchbase-transactions-with-the-query-rest-api)Couchbase Transactions with the Query REST API

* To execute a transaction containing multiple statements, you can create the transaction one statement at a time. Once you have started the transaction, you must set the `txid` parameter to specify the transaction to which each subsequent statement belongs.
* Alternatively, you can use the `tximplicit` parameter to run a single statement as a transaction. In this case, you do not need to specify the `txid` parameter.
* You can specify parameters for the Couchbase transaction as body parameters or query parameters alongside the query statement.

## [](#monitoring)Monitoring

You can monitor active Couchbase transactions using the `system:transactions` catalog. For more information, refer to [system:transactions](../n1ql-intro/sysinfo.md#sys-transactions).

## [](#permissions)Permissions

When developing a transaction with an SDK, the transaction may contain a mixture of key-value operations and query statements.

To execute a key-value operation within a transaction, users must have the relevant _Administrative_ or _Data_ RBAC roles, and permissions on the relevant buckets, scopes and collections.

Similarly, to run a query statement within a transaction, users must have the relevant _Administrative_ or _Query & Index_ RBAC roles, and permissions on the relevant buckets, scopes and collections.

Refer to [Roles](../../learn/security/roles.md) for details.

> [!NOTE]
> Query Mode
> 
> When a transaction executes a query statement, the transaction enters query mode, which means that the query is executed with the user’s query permissions. Any key-value operations which are executed by the transaction _after_ the query statement are _also_ executed with the user’s query permissions. These may or may not be different to the user’s data permissions; if they are different, you may get unexpected results.

## [](#worked-example)Worked Example

This worked example guides you through a complete Couchbase transaction session using SQL++.

### [](#preparation)Preparation

The worked example assumes that the supplied `travel-sample` bucket is installed. Refer to [Sample Buckets](../../manage/manage-settings/install-sample-buckets.md) for installation details.

Context

For this worked example, set the query context to the `tenant_agent_00` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

* Query Workbench
* CBQ Shell

![The query context drop-down menu, with the tenant_agent_00 scope selected](../../guides/_images/transactions-context.png) 

```sqlpp
\SET -query_context travel-sample.tenant_agent_00;
```

Parameters

If necessary, set the transaction parameters for this worked example. In particular, you will turn off durability for the purposes of this example, in order to make sure that there are no problems meeting the transaction durability requirements.

* Query Workbench
* CBQ Shell

1. Click the cog icon  to display the Run-Time Preferences window.
2. Open the **Scan Consistency** drop-down list and select **not\_bounded**.
3. In the **Transaction Timeout** box, enter `120`.
4. In the **Named Parameters** section, click the **+** button to add a named parameter.
5. When the new named parameter appears, enter `durability_level` in the **name** box and `"none"` (with double quotes) in the **value** box.
6. Choose **Save Preferences** to save the preferences and return to the Query Workbench.

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

Example 1\. Transaction using the Query Workbench or cbq shell

Copy the entire sequence below and paste it into either the [Query Workbench](../../tools/query-workbench.md) or the [cbq shell](../n1ql-intro/cbq.md). Note that you must be using cbq shell version 2.0 or above.

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

The results of running the transaction in the Query Workbench are shown below. If you are using the cbq shell, the results are formatted differently, but contain the same information.

Results

```json
[
  {
    "_sequence_num": 1,
    "_sequence_query": "-- Start the transaction\nBEGIN TRANSACTION;",
    "_sequence_query_status": "success",
    "_sequence_result": [
      {
        "nodeUUID": "b30cc79a9d942784c8a6b8968fe086ec",
        "txid": "d81d9b4a-b758-4f98-b007-87ba262d3a51" (1)
      }
    ]
  },
// ...
```

Beginning a transaction returns a unique transaction ID `txid`.

```json
// ...
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
  {
    "_sequence_num": 4,
    "_sequence_query": "\n\n-- Set a savepoint\nSAVEPOINT s1;",
    "_sequence_query_status": "success",
    "_sequence_result": {
      "results": []
    }
  },
  {
    "_sequence_num": 5,
    "_sequence_query": "\n\n-- Update the booking document to include a user\nUPDATE bookings AS b\nUSE KEYS \"bf7ad6fa-bdb9-4099-a840-196e47179f03\"\nSET b.`user` = \"0\";",
    "_sequence_query_status": "success",
    "_sequence_result": {
      "results": []
    }
  },
  {
    "_sequence_num": 6,
    "_sequence_query": "\n\n-- Check the content of the booking and user\nSELECT b.*, u.name\nFROM bookings b\nUSE KEYS \"bf7ad6fa-bdb9-4099-a840-196e47179f03\"\nJOIN users u\nON KEYS b.`user`;",
    "_sequence_query_status": "success",
    "_sequence_result": [
      {
        "date": "07/24/2021",
        "flight": "WN533",
        "flighttime": 7713,
        "price": 964.13,
        "route": "63986",
        "user": "0", (1)
        "name": "Keon Hoppe"
      }
    ]
  },
// ...
```

Before setting the second savepoint, the booking document has user `"0"`, name `"Keon Hoppe"`.

```json
// ...
  {
    "_sequence_num": 7,
    "_sequence_query": "\n\n-- Set a second savepoint\nSAVEPOINT s2;",
    "_sequence_query_status": "success",
    "_sequence_result": {
      "results": []
    }
  },
  {
    "_sequence_num": 8,
    "_sequence_query": "\n\n-- Update the booking documents to change the user\nUPDATE bookings AS b\nUSE KEYS \"bf7ad6fa-bdb9-4099-a840-196e47179f03\"\nSET b.`user` = \"1\";",
    "_sequence_query_status": "success",
    "_sequence_result": {
      "results": []
    }
  },
  {
    "_sequence_num": 9,
    "_sequence_query": "\n\n-- Check the content of the booking and user\nSELECT b.*, u.name\nFROM bookings b\nUSE KEYS \"bf7ad6fa-bdb9-4099-a840-196e47179f03\"\nJOIN users u\nON KEYS b.`user`;",
    "_sequence_query_status": "success",
    "_sequence_result": [
      {
        "date": "07/24/2021",
        "flight": "WN533",
        "flighttime": 7713,
        "price": 964.13,
        "route": "63986",
        "user": "1", (1)
        "name": "Rigoberto Bernier"
      }
    ]
  },
// ...
```

After setting the second savepoint and performing an update, the booking document has user `"1"`, name `"Rigoberto Bernier"`.

```json
// ...
  {
    "_sequence_num": 10,
    "_sequence_query": "\n\n-- Roll back the transaction to the second savepoint\nROLLBACK TRANSACTION TO SAVEPOINT s2;",
    "_sequence_query_status": "success",
    "_sequence_result": {
      "results": []
    }
  },
  {
    "_sequence_num": 11,
    "_sequence_query": "\n\n-- Check the content of the booking and user again\nSELECT b.*, u.name\nFROM bookings b\nUSE KEYS \"bf7ad6fa-bdb9-4099-a840-196e47179f03\"\nJOIN users u\nON KEYS b.`user`;",
    "_sequence_query_status": "success",
    "_sequence_result": [
      {
        "date": "07/24/2021",
        "flight": "WN533",
        "flighttime": 7713,
        "price": 964.13,
        "route": "63986",
        "user": "0", (1)
        "name": "Keon Hoppe"
      }
    ]
  },
  {
    "_sequence_num": 12,
    "_sequence_query": "\n\n-- Commit the transaction\nCOMMIT TRANSACTION;",
    "_sequence_query_status": "success",
    "_sequence_result": {
      "results": []
    }
  }
]
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

Example 3\. Transaction using the Query REST API

For reference, this example shows the equivalent of [Example 1](#ex-1) using the Query REST API.

Begin transaction and set parameters

```sh
curl http://localhost:8093/query/service \
-u Administrator:password \
-H 'Content-Type: application/json' \
-d '{
  "statement": "BEGIN TRANSACTION",
  "query_context": "`travel-sample`.tenant_agent_00",
  "txtimeout": "2m",
  "scan_consistency": "request_plus",
  "durability_level": "none"
}' | jq '.results[0].txid'
```

This statement uses [jq](https://jqlang.org) to get the transaction ID from the query results. After beginning the transaction, each subsequent statement in the transaction must specify the transaction ID that was generated when the transaction began.

Specify transaction settings

```sh
curl http://localhost:8093/query/service \
-u Administrator:password \
-H 'Content-Type: application/json' \
-d '{
  "statement": "SET TRANSACTION ISOLATION LEVEL READ COMMITTED;",
  "query_context": "`travel-sample`.tenant_agent_00",
  "txid": '${TXID}'
}'
```

In this and the following statements, replace `'${TXID}'` with the transaction ID, wrapped in double quotes `""`.

Create a booking document

```sh
curl http://localhost:8093/query/service \
-u Administrator:password \
-H 'Content-Type: application/json' \
-d '{
  "statement": "UPSERT INTO bookings VALUES(\"bf7ad6fa-bdb9-4099-a840-196e47179f03\", {\"date\": \"07/24/2021\", \"flight\": \"WN533\", \"flighttime\": 7713, \"price\": 964.13, \"route\": \"63986\"});",
  "query_context": "`travel-sample`.tenant_agent_00",
  "txid": '${TXID}'
}'
```

Set a savepoint

```sh
curl http://localhost:8093/query/service \
-u Administrator:password \
-H 'Content-Type: application/json' \
-d '{
  "statement": "SAVEPOINT s1;",
  "query_context": "`travel-sample`.tenant_agent_00",
  "txid": '${TXID}'
}'
```

Update the booking document to include a user

```sh
curl http://localhost:8093/query/service \
-u Administrator:password \
-H 'Content-Type: application/json' \
-d '{
  "statement": "UPDATE bookings AS b USE KEYS \"bf7ad6fa-bdb9-4099-a840-196e47179f03\" SET b.`user` = \"0\";",
  "query_context": "`travel-sample`.tenant_agent_00",
  "txid": '${TXID}'
}'
```

Check the content of the booking and user

```sh
curl http://localhost:8093/query/service \
-u Administrator:password \
-H 'Content-Type: application/json' \
-d '{
  "statement": "SELECT b.*, u.name FROM bookings b USE KEYS \"bf7ad6fa-bdb9-4099-a840-196e47179f03\" JOIN users u ON KEYS b.`user`;",
  "query_context": "`travel-sample`.tenant_agent_00",
  "txid": '${TXID}'
}'
```

Set a second savepoint

```sh
curl http://localhost:8093/query/service \
-u Administrator:password \
-H 'Content-Type: application/json' \
-d '{
  "statement": "SAVEPOINT s2;",
  "query_context": "`travel-sample`.tenant_agent_00",
  "txid": '${TXID}'
}'
```

Update the booking documents to change the user

```sh
curl http://localhost:8093/query/service \
-u Administrator:password \
-H 'Content-Type: application/json' \
-d '{
  "statement": "UPDATE bookings AS b USE KEYS \"bf7ad6fa-bdb9-4099-a840-196e47179f03\" SET b.`user` = \"1\";",
  "query_context": "`travel-sample`.tenant_agent_00",
  "txid": '${TXID}'
}'
```

Check the content of the booking and user

```sh
curl http://localhost:8093/query/service \
-u Administrator:password \
-H 'Content-Type: application/json' \
-d '{
  "statement": "SELECT b.*, u.name FROM bookings b USE KEYS \"bf7ad6fa-bdb9-4099-a840-196e47179f03\" JOIN users u ON KEYS b.`user`;",
  "query_context": "`travel-sample`.tenant_agent_00",
  "txid": '${TXID}'
}'
```

Roll back the transaction to the second savepoint

```sh
curl http://localhost:8093/query/service \
-u Administrator:password \
-H 'Content-Type: application/json' \
-d '{
  "statement": "ROLLBACK TRANSACTION TO SAVEPOINT s2;",
  "query_context": "`travel-sample`.tenant_agent_00",
  "txid": '${TXID}'
}'
```

Check the content of the booking and user again

```sh
curl http://localhost:8093/query/service \
-u Administrator:password \
-H 'Content-Type: application/json' \
-d '{
  "statement": "SELECT b.*, u.name FROM bookings b USE KEYS \"bf7ad6fa-bdb9-4099-a840-196e47179f03\" JOIN users u ON KEYS b.`user`;",
  "query_context": "`travel-sample`.tenant_agent_00",
  "txid": '${TXID}'
}'
```

Commit the transaction

```sh
curl http://localhost:8093/query/service \
-u Administrator:password \
-H 'Content-Type: application/json' \
-d '{
  "statement": "COMMIT TRANSACTION",
  "query_context": "`travel-sample`.tenant_agent_00",
  "txid": '${TXID}'
}'
```

## [](#related-links)Related Links

* Blog post: [Couchbase Transactions: Elastic, Scalable, and Distributed](https://blog.couchbase.com/transactions-n1ql-couchbase-distributed-nosql/).

---

[1](#%5Ffootnoteref%5F1). You must be using cbq shell version 2.0 or above to use the automatic transaction ID functionality.