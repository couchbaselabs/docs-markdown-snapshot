---
title: UPDATE STATISTICS
description: The UPDATE STATISTICS statement collects statistics on expressions
  over a named keyspace.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/n1ql/pages/n1ql-language-reference/updatestatistics.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:n1ql:n1ql-language-reference/updatestatistics.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/n1ql/n1ql-language-reference/updatestatistics.html)

# UPDATE STATISTICS

> The UPDATE STATISTICS statement collects statistics on expressions over a named keyspace. These statistics are used by the cost-based optimizer when choosing the optimal plan to execute a query. 

## [](#purpose)Purpose

The [cost-based optimizer](cost-based-optimizer.md) uses statistics to generate a query plan with the lowest processing cost, for [SELECT](selectintro.md), [UPDATE](update.md), [DELETE](delete.md), [MERGE](merge.md), and [INSERT INTO with SELECT](insert.md) queries.

After creating the indexes, and before running a query, you must use the `UPDATE STATISTICS` statement to gather distribution statistics for the expressions used in the query. The cost-based optimizer uses these distribution statistics, together with keyspace and index statistics, to select the optimal indexes and generate the query plan.

## [](#syntax)Syntax

```ebnf
update-statistics ::= update-statistics-expr | update-statistics-index |
                      updated-statistics-indexes | update-statistics-delete
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/update-statistics.png) 

The `UPDATE STATISTICS` statement provides several different syntaxes to enable you to manage statistics. For further details, refer to the following links.

* [Update Statistics for Index Expressions](statistics-expressions.md)
* [Update Statistics for a Single Index](statistics-index.md)
* [Update Statistics for Multiple Indexes](statistics-indexes.md)
* [Delete Statistics](statistics-delete.md)

## [](#usage)Usage

When you use an index with a query, you typically create the index on the fields which the query uses to filter. To use the cost-based optimizer with that query, you must collect statistics on the same fields that you used to create the index.

A query may have predicates on non-indexed fields, and you can collect statistics on those fields also to help the optimizer.

For a query which filters on an array or array of objects, you must collect the statistics using exactly the same expression that you used to create the index.

## [](#result)Result

If successful, the statement returns an empty array.

### [](#index-residency)Index Residency

Optimizer statistics for an index can only be gathered when the index is at least partially memory-resident. The optimizer statistics are gathered from the memory-resident portion of an index. A higher memory-resident ratio produces more accurate optimizer statistics for that index.

If an index has a memory-resident ratio of zero, then the statement returns the following warning:

```json
[
  {
    "code": 5390,
    "msg": "Index def_inventory_airport_faa is not in memory"
  }
]
```

Depending on the index storage settings, if an index has been scanned recently, it is more likely to be memory-resident; whereas if an index is not used for a long while, then it is more likely to be ejected from memory. You may be able to improve the memory-resident ratio for an index (and avoid error 5390) by running one or more queries which use that index. For further details, refer to [Storage Settings](../../learn/services-and-indexes/indexes/storage-modes.md).

## [](#optimizer-statistics)Optimizer Statistics

The `UPDATE STATISTICS` stores statistics in a system-like collection called `N1QL_CBO_STATS`. This is stored in a scope called `N1QL_SYSTEM_SCOPE` within a bucket called `N1QL_SYSTEM_BUCKET`. This bucket, scope, and collection are created automatically, if they do not already exist.

### [](#security-for-optimizer-statistics)Security for Optimizer Statistics

Access to this bucket, scope, and collection is restricted to system administrators. Regular users do not have access to the bucket, scope, or collection. Users with system administration privileges can access or drop them. If the bucket, scope, or collection is dropped, all optimizer statistics stored in the collection will be lost. A new bucket, scope, and collection will be created again the next time an `UPDATE STATISTICS` statement is run.

### [](#memory-quota-for-optimizer-statistics)Memory Quota for Optimizer Statistics

When the `N1QL_SYSTEM_BUCKET` is created, it has the minimum memory quota of 100 MB. It is recommended that system administrators monitor the memory usage of this bucket. For large clusters, when this bucket gets big, increase the memory quota for this bucket such that it does not fall under 15% memory-resident. (This is recommended for all buckets to avoid potential issues with rebalancing, etc.)

### [](#optimizer-statistics-for-multiple-query-nodes)Optimizer Statistics for Multiple Query Nodes

When a cluster has multiple Query nodes, statistics gathered from one Query node via the `UPDATE STATISTICS` statement are automatically propagated to the other Query nodes. It is not necessary to run `UPDATE STATISTICS` with the same index expression for multiple query nodes.

### [](#monitoring-optimizer-statistics)Monitoring Optimizer Statistics

You can monitor the optimizer statistics by querying the `system:dictionary` and `system:dictionary_cache` keyspaces. For further details, refer to [Monitor Queries](../../manage/monitor/monitoring-n1ql-query.md).

## [](#related-links)Related Links

* [Cost-Based Optimizer](cost-based-optimizer.md)