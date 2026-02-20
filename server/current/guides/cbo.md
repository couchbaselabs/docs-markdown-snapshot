---
title: Use the Cost-Based Optimizer with Queries
description: How to use the Cost-Based Optimizer and manage optimizer statistics.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/guides/pages/cbo.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:guides:cbo.adoc[]
---

[View original HTML](/server/current/guides/cbo.html)

# Use the Cost-Based Optimizer with Queries

> How to use the Cost-Based Optimizer and manage optimizer statistics. 

## [](#introduction)Introduction

In Couchbase Server Enterprise Edition, the Cost-Based Optimizer enables the Query Service to create the most efficient plan to execute a query. The Cost-Based Optimizer analyzes keyspace statistics, index statistics, and distribution statistics to select the optimal indexes and create the query execution plan.

The Cost-Based Optimizer can generate a query plan for [SELECT](../n1ql/n1ql-language-reference/selectintro.md), [UPDATE](../n1ql/n1ql-language-reference/update.md), [DELETE](../n1ql/n1ql-language-reference/delete.md), [MERGE](../n1ql/n1ql-language-reference/merge.md), and [INSERT INTO with SELECT](../n1ql/n1ql-language-reference/insert.md) queries.

> [!NOTE]
> If the Cost-Based Optimizer is unavailable or inactive, or if statistics are not available, the Query Service falls back on the legacy rules-based optimizer to generate the query execution plan.

If you want to try out the examples in this section, follow the instructions given in [Do a Quick Install](../getting-started/do-a-quick-install.md) to install Couchbase Server, configure a cluster, and load a sample dataset. Read the following for further information about the tools available for editing and executing queries:

* [cbq: The Command Line Shell for SQL++](../n1ql/n1ql-intro/cbq.md)
* [Query Workbench](../tools/query-workbench.md)

## [](#activating-the-cost-based-optimizer)Activating the Cost-Based Optimizer

The Cost-Based Optimizer is active by default. This section shows how to activate or deactivate the Cost-Based Optimizer for a request. You can also activate or deactivate the Cost-Based Optimizer for a query node, or for all the query nodes in the cluster.

* Query Workbench
* CBQ Shell

To activate or deactivate the Cost-Based Optimizer for a request, use the Query Run-Time Preferences window.

1. Click the cog icon  to display the Run-Time Preferences window.
2. Check or uncheck the **Use Cost-Based Optimizer** box as required.
3. Choose **Save Preferences** to save the preferences and return to the Query Workbench.

---

The following setting deactivates the Cost-Based Optimizer for subsequent requests on this Query node.

![The Run-Time Preferences dialog, with Use Cost-Based Optimizer unchecked](_images/cbo-inactive.png) 

The following setting activates the Cost-Based Optimizer for subsequent requests on this Query node.

![The Run-Time Preferences dialog, with Use Cost-Based Optimizer checked](_images/cbo-active.png) 

To activate or deactivate the Cost-Based Optimizer for a request, use `\SET` command with the `use_cbo` parameter.

> [!NOTE]
> The parameter name must be prefixed by a hyphen. The parameter is set to `true` by default.

---

For example, the following code deactivates the Cost-Based Optimizer for subsequent requests on this Query node.

```sqlpp
\SET -use_cbo false;
```

The following code activates the Cost-Based Optimizer for subsequent requests on this Query node.

```sqlpp
\SET -use_cbo true;
```

For more information and examples, see [Configure Queries](../n1ql/n1ql-manage/query-settings.md).

## [](#updating-statistics)Updating Statistics

Before you can use the Cost-Based Optimizer with a query, you must first gather the statistics that it needs. The Query Service automatically gathers statistics whenever an index is created or built, and you can update statistics at any time.

You can also configure a scheduled task to automatically check and update statistics using [Auto Update Statistics (AUS)](../n1ql/n1ql-language-reference/auto-update-statistics.md). During the scheduled window, AUS evaluates the existing statistics and updates them if they are outdated. For more information on how to enable this feature and set the schedule, see [Enable and Schedule AUS](../n1ql/n1ql-language-reference/auto-update-statistics.md#enable-and-schedule-aus).

When you use an index with a query, you typically create the index on the fields which the query uses to filter. To use the cost-based optimizer with that query, you must collect statistics on the same fields that you used to create the index.

A query may have predicates on non-indexed fields, and you can collect statistics on those fields also to help the optimizer.

For a query which filters on an array or array of objects, you must collect the statistics using exactly the same expression that you used to create the index.

### [](#updating-statistics-for-expressions)Updating Statistics for Expressions

To gather statistics for specified expressions, use the `UPDATE STATISTICS` command.

The following example creates two indexes, gathers statistics for the index key expressions and for predicate required by the query, and then runs the query.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Create indexes

```sqlpp
CREATE INDEX idx_country_city ON hotel(country, city);
CREATE INDEX idx_city_country ON hotel(city, country);
```

Update statistics

```sqlpp
UPDATE STATISTICS FOR hotel(city, country, free_breakfast);
```

Query

```sqlpp
SELECT COUNT(*) FROM hotel
WHERE country = 'United States' AND free_breakfast = true;
```

For more information and examples, see [Update Statistics for Index Expressions](../n1ql/n1ql-language-reference/statistics-expressions.md).

### [](#updating-statistics-for-an-index)Updating Statistics for an Index

To gather statistics for all the index key expressions used by an index, use the `UPDATE STATISTICS` command with the `INDEX` clause.

For example, the following query gathers statistics for all the index expressions used by the specified index.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
UPDATE STATISTICS FOR
INDEX airport.def_inventory_airport_city;
```

For more information and examples, see [Update Statistics for a Single Index](../n1ql/n1ql-language-reference/statistics-index.md).

### [](#updating-statistics-for-multiple-indexes)Updating Statistics for Multiple Indexes

To gather statistics for all the index key expressions used by multiple indexes, use the `UPDATE STATISTICS` command with the `INDEX` clause and a list of index names.

For example, the following query gathers statistics for the index expressions used by the specified indexes.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
UPDATE STATISTICS FOR airport
INDEX (def_inventory_airport_faa, def_inventory_airport_city);
```

---

The following query gathers statistics for the index expressions used by all indexes in the specified keyspace.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
UPDATE STATISTICS FOR airport INDEX ALL;
```

For more information and examples, see [Update Statistics for Multiple Indexes](../n1ql/n1ql-language-reference/statistics-indexes.md).

### [](#deleting-statistics)Deleting Statistics

To delete statistics, use the `UPDATE STATISTICS` command with the `DELETE` clause.

> [!NOTE]
> Deleting statistics for a set of index expressions effectively turns off the Cost-Based Optimizer for queries which use predicates on those expressions.

For example, the following query deletes statistics for the specified index expressions.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
UPDATE STATISTICS FOR hotel
DELETE (city, country, free_breakfast);
```

---

The following query deletes statistics for the index expressions used by all indexes in the specified keyspace.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
UPDATE STATISTICS FOR airport DELETE ALL;
```

For more information and examples, see [Delete Statistics](../n1ql/n1ql-language-reference/statistics-delete.md).

## [](#related-links)Related Links

Explanation:

* [Cost-Based Optimizer](../n1ql/n1ql-language-reference/cost-based-optimizer.md)

Reference:

* [UPDATE STATISTICS](../n1ql/n1ql-language-reference/updatestatistics.md)
* [Auto Update Statistics](../n1ql/n1ql-language-reference/auto-update-statistics.md)

Administrator guides:

* [General Settings](../manage/manage-settings/general-settings.md)
* [Monitor Statistics](../n1ql/n1ql-intro/sysinfo.md#sys-dictionary)

Querying with SDKs:

* [C](../../../c-sdk/current/howtos/n1ql-queries-with-sdk.md)| [C++](../../../cxx-sdk/current/howtos/sqlpp-queries-with-sdk.md)| [.NET](../../../dotnet-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Go](../../../go-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Java](../../../java-sdk/current/howtos/sqlpp-queries-with-sdk.md)| [Kotlin](../../../kotlin-sdk/current/howtos/n1ql-queries.md)| [Node.js](../../../nodejs-sdk/current/howtos/n1ql-queries-with-sdk.md)| [PHP](../../../php-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Python](../../../python-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Ruby](../../../ruby-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Rust](../../../rust-sdk/current/howtos/sqlpp-queries-with-sdk.md)| [Scala](../../../scala-sdk/current/howtos/sqlpp-queries-with-sdk.md)