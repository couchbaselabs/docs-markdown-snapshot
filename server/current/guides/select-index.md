---
title: Select Indexes
description: How to select an index for a query.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/guides/pages/select-index.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:guides:select-index.adoc[]
---

[View original HTML](/server/current/guides/select-index.html)

# Select Indexes

> How to select an index for a query. 

## [](#introduction)Introduction

Couchbase Server attempts to select an appropriate secondary index for a query, based on the filters in the WHERE clause. If it cannot select a secondary query, the Query Service falls back on the primary index for the keyspace, if one exists.

If you want to try out the examples in this section, follow the instructions given in [Do a Quick Install](../getting-started/do-a-quick-install.md) to install Couchbase Server, configure a cluster, and load a sample dataset. Read the following for further information about the tools available for editing and executing queries:

* [cbq: The Command Line Shell for SQL++](../n1ql/n1ql-intro/cbq.md)
* [Query Workbench](../tools/query-workbench.md)

## [](#specifying-predicates-to-select-an-index)Specifying Predicates to Select an Index

To specify an index using query predicates, specify the leading query predicates in the WHERE clause in the same order as the index keys in the index.

> [!TIP]
> Use `IS NOT MISSING` as the predicate for any fields which are required by the index, but which are not actually used for filtering data in the query.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Queries

The following query creates a secondary index on the `image_direct_url` field in the `landmark` keyspace.

```sqlpp
CREATE INDEX `idx_image_direct_url`
ON landmark(`image_direct_url`);
```

The following query uses a minimal filter on the `image_direct_url` field to select the `idx_image_direct_url` index.

```sqlpp
SELECT image_direct_url FROM landmark
WHERE image_direct_url IS NOT MISSING;
```

For more information and examples, see [Index Selection](../n1ql/n1ql-language-reference/selectintro.md#index-selection).

## [](#specifying-an-index-hint)Specifying an Index Hint

You can use an index hint to specify that a query should use a particular index. The index must be applicable to the query.

To specify an index by name:

1. Use an index hint within a hint comment, immediately after the SELECT keyword.
2. In the index hint, specify the keyspace to which the hint applies, and the index to use.

This example uses an index hint to select the index `def_inventory_route_route_src_dst_day`, which is installed with the travel sample data.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
SELECT /*+ INDEX (route def_inventory_route_route_src_dst_day) */ id (1)
FROM route (2)
WHERE sourceairport = "SFO"
LIMIT 1;
```

For more information and examples, see [INDEX](../n1ql/n1ql-language-reference/keyspace-hints.md#index).

## [](#related-links)Related Links

Reference and explanation:

* [Primary and Secondary Index Reference](../indexes/indexing-overview.md)
* [SELECT](../n1ql/n1ql-language-reference/selectintro.md)
* [Hints](../n1ql/n1ql-language-reference/optimizer-hints.md)

Administrator guides:

* [Manage Indexes](../manage/manage-indexes/manage-indexes.md)
* [Monitor Indexes](../manage/monitor/monitoring-indexes.md)

Tutorials:

* [SQL++ Query Language Tutorial](https://query-tutorial.couchbase.com/tutorial/#1)

Indexes with SDKs:

* [C](../../../c-sdk/current/concept-docs/n1ql-query.md#indexes)| [C++](../../../cxx-sdk/current/concept-docs/n1ql-query.md#indexes)| [.NET](../../../dotnet-sdk/current/concept-docs/n1ql-query.md#indexes)| [Go](../../../go-sdk/current/concept-docs/n1ql-query.md#indexes)| [Java](../../../java-sdk/current/concept-docs/n1ql-query.md#indexes)| Kotlin | [Node.js](../../../nodejs-sdk/current/concept-docs/n1ql-query.md#indexes)| [PHP](../../../php-sdk/current/concept-docs/n1ql-query.md#indexes)| [Python](../../../python-sdk/current/concept-docs/n1ql-query.md#indexes)| [Ruby](../../../ruby-sdk/current/concept-docs/n1ql-query.md#indexes)| [Rust](../../../rust-sdk/current/concept-docs/n1ql-query.md#indexes)| [Scala](../../../scala-sdk/current/concept-docs/n1ql-query.md#indexes)