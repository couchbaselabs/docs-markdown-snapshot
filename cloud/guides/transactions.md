---
title: Create Couchbase Transactions with SQL++
description: How to create Couchbase transactions using SQL++.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/guides/pages/transactions.adoc
  xref: xref:cloud:guides:transactions.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/guides/transactions.html)

# Create Couchbase Transactions with SQL++

> How to create Couchbase transactions using SQL++. 

## [](#introduction)Introduction

Couchbase transactions enable you to carry out ACID (atomic, consistent, isolated, and durable) actions on the database. This how-to guide covers SQL++ support for Couchbase transactions. Some SDKs also support Couchbase transactions. For more information, see [Related Links](#related-links).

Only DML (data modification language) statements are permitted within a transaction: [INSERT](../n1ql/n1ql-language-reference/insert.md), [UPSERT](../n1ql/n1ql-language-reference/upsert.md), [DELETE](../n1ql/n1ql-language-reference/delete.md), [UPDATE](../n1ql/n1ql-language-reference/update.md), [MERGE](../n1ql/n1ql-language-reference/merge.md), [SELECT](#n1ql:n1ql-language-reference/select.adoc), [EXECUTE FUNCTION](../n1ql/n1ql-language-reference/execfunction.md), [PREPARE](../n1ql/n1ql-language-reference/prepare.md), or [EXECUTE](../n1ql/n1ql-language-reference/execute.md).

If you want to try out the examples in this section, follow the instructions given in [Create an Account and Deploy Your Free Tier Operational Cluster](../get-started/create-account.md) to create a free account, deploy a cluster, and load a sample dataset. To create a transaction using SQL++ in Couchbase Capella, you must use the [cbq shell](../n1ql/n1ql-intro/cbq.md).

> [!WARNING]
> Please note that the examples in this guide will alter the data in your sample database. To restore your sample data, remove and reinstall the travel sample data. Refer to [Import Data with the Capella UI](../clusters/data-service/import-data-documents.md) for details.

## [](#settings)Transaction Parameters

You can specify various settings and parameters to control how transactions work. You can access transaction settings and parameters through the cbq shell.

* CBQ Shell

To specify parameters for a Couchbase transaction, use the `\SET` command.

---

The following example shows transaction parameters for the examples on this page.

```sqlpp
\SET -txtimeout "2m"; (1)
\SET -scan_consistency "not_bounded"; (2)
\SET -durability_level "none"; (3)
```

| **1** | The transaction timeout.                                      |
| ----- | ------------------------------------------------------------- |
| **2** | The transaction scan consistency.                             |
| **3** | Durability level of all the mutations within the transaction. |

Click the  View button to see this code in context.

For more information, see [Transaction Settings and Parameters](../n1ql/n1ql-language-reference/transactions.md#settings-and-parameters).

## [](#single-statement)Single Statement Transactions

You can create a Couchbase transaction containing a single DML statement.

* CBQ Shell

To execute a single statement as a transaction, set the `tximplicit` parameter to `true`.

---

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
\SET -tximplicit true;

UPDATE hotel
SET price = "from £89"
WHERE name = "Glasgow Grand Central";
```

For more information, see [Query Tools](../n1ql/n1ql-language-reference/transactions.md#query-tools).

## [](#multiple-statement)Multiple Statement Transactions

A Couchbase transaction may contain multiple DML statements. In this case, you must use SQL++ transaction statements to support the transaction:

* [BEGIN TRANSACTION](#begin) to start the transaction.
* [SET TRANSACTION](#set) to specify transaction settings.
* [SAVEPOINT](#savepoint) to set a transaction savepoint.
* [ROLLBACK TRANSACTION](#rollback) to roll back a transaction.
* [COMMIT TRANSACTION](#commit) to commit a transaction.

* CBQ Shell

To execute a transaction containing multiple statements, create the transaction one statement at a time.

Once you have started a transaction, all statements within the cbq shell session are assumed to be part of the same transaction until you rollback or commit the transaction.

> [!NOTE]
> You must be using cbq shell version 2.0 or above to use the automatic transaction ID functionality.

---

For a worked example showing a complete transaction using SQL++, see [Transaction Worked Example](../n1ql/n1ql-language-reference/transactions.md#worked-example). Individual SQL++ transaction statements are described in the sections below.

### [](#begin)Begin a Transaction

To start a transaction, use the `BEGIN TRANSACTION` statement.

The following statement begins a transaction.

```sqlpp
BEGIN TRANSACTION;
```

Click the  View button to see this code in context.

Result

```json
{
    "nodeUUID": "9803422b02fd9e6c9e7156b8ddb2d840",
    "txid": "fab2bd20-322e-4ed0-bc4e-035db995f349" (1)
}
```

| **1** | Beginning a transaction returns the transaction ID. |
| ----- | --------------------------------------------------- |

For more information, see [BEGIN TRANSACTION](../n1ql/n1ql-language-reference/begin-transaction.md).

### [](#set)Specify Transaction Settings

To specify transaction settings, use the `SET TRANSACTION` statement.

> [!NOTE]
> Currently, the only available transaction setting is `ISOLATION LEVEL READ COMMITTED`. This setting is enabled by default. The `SET TRANSACTION` statement is therefore optional and may be omitted.

The following statement specifies transaction settings.

```sqlpp
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
```

Click the  View button to see this code in context.

For more information, see [SET TRANSACTION](../n1ql/n1ql-language-reference/set-transaction.md).

### [](#savepoint)Set a Savepoint

To set a savepoint within a transaction, use the `SAVEPOINT` statement and specify a name for the savepoint.

The following statement sets a savepoint.

```sqlpp
SAVEPOINT s1;
```

Click the  View button to see this code in context.

For more information, see [SAVEPOINT](../n1ql/n1ql-language-reference/savepoint.md).

### [](#rollback)Roll Back a Transaction

To roll back a transaction, use the `ROLLBACK TRANSACTION` statement.

By default, this statement rolls back the entire transaction. If you want to roll back to a savepoint, use the `TO SAVEPOINT` keywords and specify the savepoint name.

The following statement rolls back a transaction to a specified savepoint.

```sqlpp
ROLLBACK TRANSACTION TO SAVEPOINT s2;
```

Click the  View button to see this code in context.

For more information, see [ROLLBACK TRANSACTION](../n1ql/n1ql-language-reference/rollback-transaction.md).

### [](#commit)Commit a Transaction

To commit a transaction, use the `COMMIT TRANSACTION` statement.

The following statement commits a transaction.

```sqlpp
COMMIT TRANSACTION;
```

Click the  View button to see this code in context.

For more information, see [COMMIT TRANSACTION](../n1ql/n1ql-language-reference/commit-transaction.md).

## [](#related-links)Related Links

Reference and explanation:

* [Transactions](../../server/current/learn/data/transactions.md)
* [SQL++ Support for Couchbase Transactions](../n1ql/n1ql-language-reference/transactions.md)

Online transaction simulator:

* [Query Transaction Simulator](https://transactions.couchbase.com)

Transactions with SDKs:

* C | [C++](../../cxx-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md)| [.NET](../../dotnet-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md)| [Go](../../go-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md)| [Java](../../java-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md)| [Kotlin](../../kotlin-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md)| [Node.js](../../nodejs-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md)| [PHP](../../php-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md)| [Python](../../python-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md)| Ruby | Rust | [Scala](../../scala-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md)