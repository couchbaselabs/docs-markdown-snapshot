---
title: Create Couchbase Transactions with SQL++
description: How to create Couchbase transactions using SQL++.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/guides/pages/transactions.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/current/guides/transactions.html)

# Create Couchbase Transactions with SQL++

> How to create Couchbase transactions using SQL++. 

## [](#introduction)Introduction

Couchbase transactions enable you to carry out ACID (atomic, consistent, isolated, and durable) actions on the database. This how-to guide covers SQL++ support for Couchbase transactions. Some SDKs also support Couchbase transactions. For more information, see [Related Links](#related-links).

Only DML (data modification language) statements are permitted within a transaction: [INSERT](../n1ql/n1ql-language-reference/insert.md), [UPSERT](../n1ql/n1ql-language-reference/upsert.md), [DELETE](../n1ql/n1ql-language-reference/delete.md), [UPDATE](../n1ql/n1ql-language-reference/update.md), [MERGE](../n1ql/n1ql-language-reference/merge.md), [SELECT](#n1ql:n1ql-language-reference/select.adoc), [EXECUTE FUNCTION](../n1ql/n1ql-language-reference/execfunction.md), [PREPARE](../n1ql/n1ql-language-reference/prepare.md), or [EXECUTE](../n1ql/n1ql-language-reference/execute.md).

If you want to try out the examples in this section, follow the instructions given in [Do a Quick Install](../getting-started/do-a-quick-install.md) to install Couchbase Server, configure a cluster, and load a sample dataset. Read the following for further information about the tools available for editing and executing queries:

* [cbq: The Command Line Shell for SQL++](../n1ql/n1ql-intro/cbq.md)
* [Query Workbench](../tools/query-workbench.md)

> [!WARNING]
> Please note that the examples in this guide will alter the data in your sample database. To restore your sample data, remove and reinstall the travel sample data. Refer to [Sample Buckets](../manage/manage-settings/install-sample-buckets.md) for details.

## [](#settings)Transaction Parameters

You can specify various settings and parameters to control how transactions work. You can access transaction settings and parameters through any of the usual Query tools, such as the Query Workbench or the cbq shell.

* Query Workbench
* CBQ Shell

To specify parameters for a Couchbase transaction, use the Query Run-Time Preferences window.

1. To display the Run-Time Preferences window, click the cog icon .
2. To specify the transaction scan consistency, open the **Scan Consistency** drop-down list and select an option.
3. To specify the transaction timeout, in the **Transaction Timeout** box, enter a value in seconds.
4. To specify any other transaction parameters, click the **+** button in the **Named Parameters** section. For the new named parameter, enter a name in the **name** box and a value in the **value** box.
5. To save the preferences and return to the Query Workbench, click **Save Preferences**.

---

The following example shows transaction parameters for the examples on this page.

![The Run-Time Preferences dialog, with Scan Consistency set to "not_bounded", Transaction Timeout set to "120", and named parameter "durability_level" set to "none"](_images/transactions-preferences.png) 

| **1** | The transaction scan consistency is set to not\_bounded.                           |
| ----- | ---------------------------------------------------------------------------------- |
| **2** | The durability level of all the mutations within the transaction is set to "none". |
| **3** | The transaction timeout is set to 120.                                             |

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

* Query Workbench
* CBQ Shell

To execute a single statement as a transaction, enter the statement in the query editor and click **Run as TX**.

---

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
UPDATE hotel
SET price = "from £89"
WHERE name = "Glasgow Grand Central";
```

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

* Query Workbench
* CBQ Shell

To execute a transaction containing multiple statements:

1. Compose the sequence of statements in the query editor. Each statement must be terminated with a semicolon.
2. After each statement, press Shift+Enter to start a new line without executing the query.
3. When you have entered the entire transaction, click **Execute** to execute the transaction.

---

For a worked example showing a complete transaction using SQL++, see [Transaction Worked Example](../n1ql/n1ql-language-reference/transactions.md#worked-example). Individual SQL++ transaction statements are described in the sections below.

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
  "nodeUUID": "b30cc79a9d942784c8a6b8968fe086ec",
  "txid": "d81d9b4a-b758-4f98-b007-87ba262d3a51" (1)
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

* [Transactions](../learn/data/transactions.md)
* [SQL++ Support for Couchbase Transactions](../n1ql/n1ql-language-reference/transactions.md)

Online transaction simulator:

* [Query Transaction Simulator](https://transactions.couchbase.com)

Transactions with SDKs:

* C | [C++](../../../cxx-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md)| [.NET](../../../dotnet-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md)| [Go](../../../go-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md)| [Java](../../../java-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md)| [Kotlin](../../../kotlin-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md)| [Node.js](../../../nodejs-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md)| [PHP](../../../php-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md)| [Python](../../../python-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md)| Ruby | Rust | [Scala](../../../scala-sdk/current/howtos/distributed-acid-transactions-from-the-sdk.md)