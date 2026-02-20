---
title: Early Filters, Order, and Pagination
description: When covering indexes and index pushdowns are not available, the
  Query Service may use early filtering, early ordering, and early pagination to
  improve the query response time.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/learn/pages/services-and-indexes/indexes/early-filters-and-pagination.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:learn:services-and-indexes/indexes/early-filters-and-pagination.adoc[]
---

[View original HTML](/server/7.2/learn/services-and-indexes/indexes/early-filters-and-pagination.html)

# Early Filters, Order, and Pagination

> When covering indexes and index pushdowns are not available, the Query Service may use early filtering, early ordering, and early pagination to improve the query response time. 

Examples on this Page

The examples in this topic use the travel-sample dataset which is shipped with Couchbase Server. For instructions on how to install the sample bucket, see [Sample Buckets](../../../manage/manage-settings/install-sample-buckets.md).

To use the examples on this page, you must set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../../../n1ql/n1ql-intro/queriesandresults.md#query-context).

## [](#overview)Overview

If a query has a [covering index](../../../n1ql/n1ql-language-reference/covering-indexes.md), and the query is on a single keyspace, then the index contains all the data needed to perform the query. The Query service does not need to fetch data from the Data service. Any filters, order, or pagination (offset and limit) are performed by the Index service.

![Covering index](../../_images/covered-query-de029e9f9f78a6a058b39e65712213c37d1ce53e.svg) 

Figure 1\. Covering index

If a query is _not_ covered by an index, then the query needs to fetch data from the Data service after performing the index scan, in order to return the requested results. By default, any filters, order, or pagination are performed by the Query service after the fetch.

![Default filters, order, and pagination](../../_images/uncovered-query-b91efe10bbbf0bd863f1e0fcdbb4238f3944a93b.svg) 

Figure 2\. Default filters, order, and pagination

Fetching data from the Data service can be expensive. Any feature that can reduce the amount of data to be fetched will improve the query response time. It would obviously be inefficient to fetch an entire dataset, and then discard a large portion of it by applying filters and pagination. Couchbase Server therefore attempts to apply filters, order, and pagination _before_ fetching data, wherever possible.

Index [pushdowns](index%5Fpushdowns.md) provide one way to reduce the amount of data to be fetched. Some filters, ordering, and pagination may be pushed down to the Index service, along with grouping and aggregates. The Index service applies these operations to the result of the index scan. The Query service then only needs to fetch the remaining data.

![Filter, order, and pagination pushdown](../../_images/index-pushdown-aa849e293a44528889237caa1d03e48d8928a6d7.svg) 

Figure 3\. Filter, order, and pagination pushdown

However, there are some operations that cannot be pushed down to the Index service: for example, a filter that uses a function or a LIKE operator on top of an index term. These operations must be performed by the Query service. If the Query Service has to perform a fetch from the Data service, and then apply any operations that could not be pushed down to the Index service, this still leads to some inefficient queries.

In Couchbase Server, _early filtering_, _early ordering_, and _early pagination_ provide another line of defense, in cases where covering indexes and index pushdowns are not available. With this feature, the Query service may apply filtering, ordering, and pagination directly to the results returned by the Index service, before performing the fetch.

![Early filters, order, and pagination](../../_images/early-filter-pagination-1814fda3e5907f6a0318b8ef829a8f6d808c8d90.svg) 

Figure 4\. Early filters, order, and pagination

Note that in practice, an uncovered query may use a mixture of the methods illustrated by [Figure 2](#fig-uncovered), [Figure 3](#fig-pushdown), and [Figure 4](#fig-early). In addition, early filtering may be performed independently of early ordering and pagination, and vice versa.

## [](#early-filtering)Early Filtering

Early filtering may be applied independently of early ordering and pagination. For an illustration of early filtering, consider the following index.

Index I

```sqlpp
CREATE INDEX idx_eat_city_name
ON landmark(city DESC, name)
WHERE activity = "eat";
```

This index contains all the data needed to perform [Example 1](#early-filter-1); it therefore acts as a covering index to this query.

Example 1\. Covered query

Query

```sqlpp
EXPLAIN SELECT city, name FROM landmark
WHERE city = "Paris" AND activity = "eat";
```

The query plan shows that the query is covered. In addition, the predicate `city = "Paris"` is applied as a span by the Index service.

```json
[
  {
    "plan": {
      "#operator": "Sequence",
      "~children": [
        {
          "#operator": "IndexScan3",
          "bucket": "travel-sample",
          "covers": [ (1)
            "cover ((`landmark`.`city`))",
            "cover ((`landmark`.`name`))",
            "cover ((meta(`landmark`).`id`))"
          ],
          "filter_covers": {
            "cover ((`landmark`.`activity`))": "eat"
          },
          "index": "idx_eat_city_name",
// ...
          "spans": [
            {
              "exact": true,
              "range": [ (2)
                {
                  "high": "\"Paris\"",
                  "inclusion": 3,
                  "index_key": "`city`",
                  "low": "\"Paris\""
                }
              ]
// ...
```

| **1** | The covers section shows that the query is covered.                                    |
| ----- | -------------------------------------------------------------------------------------- |
| **2** | The range section shows that this predicate is applied as a span by the Index service. |

[Example 2](#early-filter-2) adds an extra field to the projection. Now the query is no longer covered, and the Query service needs to fetch documents based on keys returned from the index.

Example 2\. Predicate pushdown

Query

```sqlpp
EXPLAIN SELECT city, name, address FROM landmark
WHERE city = "Paris" AND activity = "eat";
```

This query does not run too slowly, since the predicate `city = "Paris"` is pushed down to the Index service. The index only returns document keys for documents matching the predicate.

```json
[
  {
    "plan": {
      "#operator": "Sequence",
      "~children": [
        {
          "#operator": "IndexScan3",
          "bucket": "travel-sample",
          "index": "idx_eat_city_name",
          "index_id": "e5dbf76060ed1d19",
          "index_projection": {
            "primary_key": true
          },
          "keyspace": "landmark",
          "namespace": "default",
          "scope": "inventory",
          "spans": [
            {
              "exact": true,
              "range": [ (1)
                {
                  "high": "\"Paris\"",
                  "inclusion": 3,
                  "index_key": "`city`",
                  "low": "\"Paris\""
                }
              ]
            }
          ],
          "using": "gsi"
        },
        {
          "#operator": "Fetch", (2)
          "bucket": "travel-sample",
          "keyspace": "landmark",
          "namespace": "default",
          "scope": "inventory"
        },
// ...
```

| **1** | The range section shows that this predicate is pushed down to the Index service. |
| ----- | -------------------------------------------------------------------------------- |
| **2** | After the pushdown, the Query service fetches documents from the Data service.   |

Now let’s consider the case when the filter is not on the index key exactly, but applies a function on top of the index key.

Example 3\. Early filtering

Query

```sqlpp
EXPLAIN SELECT city, name, address FROM landmark
WHERE LOWER(city) = "paris" AND activity = "eat";
```

In this case, the filter cannot be pushed down to the Index service. This is where early filtering comes into play. The Query service can apply the specified filter to the results of the index scan, before fetching the matching documents from the Data service.

```json
[
  {
    "plan": {
      "#operator": "Sequence",
      "~children": [
        {
          "#operator": "IndexScan3",
          "bucket": "travel-sample",
          "filter": "(lower(_index_key ((`landmark`.`city`))) = \"paris\")", (1)
          "index": "idx_eat_city_name",
          "index_conditions": { (2)
            "_index_condition ((`landmark`.`activity`))": "eat"
          },
          "index_id": "e5dbf76060ed1d19",
          "index_keys": [ (3)
            "_index_key ((`landmark`.`city`))",
            "_index_key ((meta(`landmark`).`id`))"
          ],
          "index_projection": {
            "entry_keys": [ (4)
              0
            ],
            "primary_key": true
          },
// ...
```

| **1** | The early index filters, including all the filters that can be evaluated on the index keys. Inside the filter, \_index\_key ((\`landmark\`.\`city\`)) is analogous to cover ((\`landmark\`.\`city\`)) for a covering index scan. |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | The index\_conditions section is analogous to the filter\_covers section in the plan for a covered query.                                                                                                                        |
| **3** | The index\_keys section is analogous to the covers section in the plan for a covered query.                                                                                                                                      |
| **4** | The index\_projection section contains the \_index\_key needed for evaluating the early index filters — in this case position 0 for "city".                                                                                      |

If necessary, the Query service may use a mixture of index pushdowns and early filtering, as shown in the following example.

Example 4\. Predicate pushdown and early filter

Query

```sqlpp
EXPLAIN SELECT city, name, address FROM landmark
WHERE city = "Paris" AND name LIKE "%Paris%" AND activity = "eat";
```

The Index service evaluates the filters used to generate the index spans first, before returning to the Query service. As a result, the early filters only contain the predicates that were not pushed down to the Index service.

```json
[
  {
    "plan": {
      "#operator": "Sequence",
      "~children": [
        {
          "#operator": "IndexScan3",
          "bucket": "travel-sample",
          "filter": "(_index_key ((`landmark`.`name`)) like \"%Paris%\")", (1)
          "index": "idx_eat_city_name",
          "index_conditions": {
            "_index_condition ((`landmark`.`activity`))": "eat"
          },
          "index_id": "e5dbf76060ed1d19",
          "index_keys": [
            "_index_key ((`landmark`.`name`))",
            "_index_key ((meta(`landmark`).`id`))"
          ],
// ...
          "spans": [ (2)
            {
              "range": [
                {
                  "high": "\"Paris\"",
                  "inclusion": 3,
                  "index_key": "`city`",
                  "low": "\"Paris\""
                },
                {
                  "high": "[]",
                  "inclusion": 1,
                  "index_key": "`name`",
                  "low": "\"\""
                }
              ]
// ...
```

| **1** | The filter name LIKE "%Paris%" does not generate an exact index span, and needs to be evaluated as an early index filter. |
| ----- | ------------------------------------------------------------------------------------------------------------------------- |
| **2** | The filter city = "Paris" generates an exact span, and thus can be pushed down to the Index service.                      |

## [](#early-order-and-pagination)Early Order and Pagination

Early order and pagination may be applied independently of early filtering. As an illustration, consider the following index.

Index II

```sqlpp
CREATE INDEX idx_landmark_city_name
ON landmark(city DESC, name);
```

This index acts as a covering index to [Example 5](#early-paginate-1).

Example 5\. Covered query

Query

```sqlpp
EXPLAIN SELECT city, name FROM landmark
WHERE city IS NOT MISSING
ORDER BY city DESC, name OFFSET 100 LIMIT 5;
```

The `covers` section of the query plan shows that the query is covered. In addition, the ordering, offset, and limit are performed by the Index service.

```json
[
  {
    "plan": {
      "#operator": "Sequence",
      "~children": [
        {
          "#operator": "Sequence",
          "~children": [
            {
              "#operator": "IndexScan3",
              "bucket": "travel-sample",
              "covers": [
                "cover ((`landmark`.`city`))",
                "cover ((`landmark`.`name`))",
                "cover ((meta(`landmark`).`id`))"
              ],
              "index": "idx_landmark_city_name",
              "index_id": "c2a48a468ef63f23",
              "index_order": [ (1)
                {
                  "desc": true,
                  "keypos": 0
                },
                {
                  "keypos": 1
                }
              ],
              "index_projection": {
                "entry_keys": [
                  0,
                  1
                ]
              },
              "keyspace": "landmark",
              "limit": "5", (2)
              "namespace": "default",
              "offset": "100", (3)
              "scope": "inventory",
// ...
```

| **1** | Index order performed by index operator |
| ----- | --------------------------------------- |
| **2** | Limit performed by index operator       |
| **3** | Offset performed by index operator      |

[Example 6](#early-paginate-2) adds an extra field to the projection. Now the query is no longer covered.

Example 6\. Order and pagination pushdown

Query

```sqlpp
EXPLAIN SELECT city, name, address FROM landmark
WHERE city IS NOT MISSING
ORDER BY city DESC, name OFFSET 100 LIMIT 5;
```

However the query runs pretty quickly, since the ordering, offset, and limit can still be pushed down to the Index service.

```json
[
  {
    "plan": {
      "#operator": "Sequence",
      "~children": [
        {
          "#operator": "Sequence",
          "~children": [
            {
              "#operator": "IndexScan3",
              "bucket": "travel-sample",
              "index": "idx_landmark_city_name",
              "index_id": "c2a48a468ef63f23",
              "index_order": [ (1)
                {
                  "desc": true,
                  "keypos": 0
                },
                {
                  "keypos": 1
                }
              ],
              "index_projection": {
                "primary_key": true
              },
              "keyspace": "landmark",
              "limit": "5", (2)
              "namespace": "default",
              "offset": "100", (3)
              "scope": "inventory",
// ...
```

| **1** | Index order pushdown |
| ----- | -------------------- |
| **2** | Limit pushdown       |
| **3** | Offset pushdown      |

However, if we change the order of the ordering terms so that they no longer match the index key order, ordering cannot be pushed down to the Index service.

Example 7\. Early order and pagination

Query

```sqlpp
EXPLAIN SELECT city, name, address FROM landmark
WHERE city IS NOT MISSING
ORDER BY name, city DESC OFFSET 100 LIMIT 5;
```

So in this case, early ordering, limit, and offset are done by the Query service before fetch.

```json
[
  {
    "plan": {
      "#operator": "Sequence",
      "~children": [
        {
          "#operator": "Sequence",
          "~children": [
            {
              "#operator": "IndexScan3",
              "bucket": "travel-sample",
              "index": "idx_landmark_city_name",
              "index_id": "c2a48a468ef63f23",
              "index_keys": [
                "_index_key ((`landmark`.`city`))",
                "_index_key ((`landmark`.`name`))",
                "_index_key ((meta(`landmark`).`id`))"
              ],
              "keyspace": "landmark",
              "namespace": "default",
              "scope": "inventory",
              "spans": [
                {
                  "exact": true,
                  "range": [
                    {
                      "inclusion": 1,
                      "index_key": "`city`",
                      "low": "null"
                    }
                  ]
                }
              ],
              "using": "gsi"
            },
            {
              "#operator": "Order", (1)
              "flags": 1,
              "limit": "5", (2)
              "offset": "100", (3)
              "sort_terms": [
                {
                  "expr": "_index_key ((`landmark`.`name`))"
                },
                {
                  "desc": "\"desc\"",
                  "expr": "_index_key ((`landmark`.`city`))"
                }
              ]
            },
// ...
```

| **1** | Early ordering |
| ----- | -------------- |
| **2** | Early limit    |
| **3** | Early offset   |

Similarly, if we change the direction of the sort from descending to ascending, the ordering cannot be pushed down to the Index service, since it does not support reverse index scan.

Example 8\. Early reverse order and pagination

Query

```sqlpp
EXPLAIN SELECT city, name, address FROM landmark
WHERE city IS NOT MISSING
ORDER BY city ASC, name OFFSET 100 LIMIT 5;
```

In this case also, early ordering, limit, and offset are done by the Query service before fetch.

```json
// ...
            {
              "#operator": "Order",
              "flags": 1,
              "limit": "5",
              "offset": "100",
              "sort_terms": [ (1)
                {
                  "desc": "\"asc\"",
                  "expr": "_index_key ((`landmark`.`city`))"
                },
                {
                  "expr": "_index_key ((`landmark`.`name`))"
                }
              ]
            },
// ...
```

| **1** | The sort\_terms section uses \_index\_key expressions to sort the results using the index keys. |
| ----- | ----------------------------------------------------------------------------------------------- |

### [](#limitations)Limitations

The optimizer only selects early ordering and pagination when the following conditions are met. Many of these conditions are similar to the conditions for index order pushdowns.

* The query must be simple, referencing a single keyspace with no joins.
* There can be no `GROUP BY` or aggregates in the query.
* Index pushdown for `ORDER`, `LIMIT` and `OFFSET` must not be possible.
* The `ORDER BY` clause and `LIMIT` clause must be present. The `OFFSET` clause is optional.
* All expression references in the `ORDER BY` clause must be present in the index — similar to the covering requirement for index pushdown. However there is no requirement for exact index spans.
* Projection alias can be used in the `ORDER BY` clause, if all the references in the aliased expression are available from the index.
* Only simple `IndexScan` is supported for early ordering. More complex index scans such as `IntersectScan`, `OrderedIntersectScan`, `UnionScan` and `DistinctScan` are not supported.
* When early ordering is in effect, parallelism is turned off.

## [](#summary)Summary

The following table summarizes the different methods of performing filtering, order, or pagination, from most efficient to least.

|                                          | Covering index | Index pushdown [\[note\]](#note) | Early filters, order, or pagination [\[note\]](#note) | Default filters, order, or pagination [\[note\]](#note) |
| ---------------------------------------- | -------------- | -------------------------------- | ----------------------------------------------------- | ------------------------------------------------------- |
| Fetch required?                          | No             | Yes                              | Yes                                                   | Yes                                                     |
| Filters, order, and paginationperformed: | After scan     | After scan,before fetch          | After scan,before fetch                               | After fetch                                             |
| …​ by:                                   | Index service  | Index service                    | Query service                                         | Query service                                           |

> [!NOTE]
> An uncovered query may use a mixture of these methods.

## [](#related-links)Related Links

* [Query Execution: Details](index-scans.md#query-execution-details)
* [Covering Indexes](../../../n1ql/n1ql-language-reference/covering-indexes.md)
* [Index Pushdown Optimizations](index%5Fpushdowns.md)
* [Grouping and Aggregate Pushdown](../../../n1ql/n1ql-language-reference/groupby-aggregate-performance.md)
* [WHERE Clause](../../../n1ql/n1ql-language-reference/where.md) — to apply a filter
* [ORDER BY Clause](../../../n1ql/n1ql-language-reference/orderby.md) — to apply a sort
* [OFFSET Clause](../../../n1ql/n1ql-language-reference/offset.md) and [LIMIT Clause](../../../n1ql/n1ql-language-reference/limit.md) — to apply pagination