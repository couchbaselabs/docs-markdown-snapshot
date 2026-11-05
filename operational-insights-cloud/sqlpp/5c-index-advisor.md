---
title: Index Advisor
description: This topic describes how to use the Index Advisor to get index
  recommendations for your queries.
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Operational Insights Capella
    version: ""
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/sqlpp/pages/5c-index-advisor.adoc
  xref: xref:analytics:sqlpp:5c-index-advisor.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights-cloud/sqlpp/5c-index-advisor.html)

# Index Advisor

> This topic describes how to use the Index Advisor to get index recommendations for your queries. 

Well-designed secondary indexes can significantly improve the performance of analytical queries. The Index Advisor helps you identify optimal secondary indexes based on the query pattern and the underlying data distribution. Index recommendations are cost-based decisions, and they rely on statistics derived from data samples. Before using the Index Advisor, you must collect samples on all collections referenced in the query.

For more information about indexes, see [Indexes](7%5Fusing%5Findex.md). To collect samples, see [Collecting Samples](5b%5Fcbo.md#Collecting%5Fsamples).

> [!NOTE]
> * Index Advisor works only with `SELECT` statements.
> * Queries that reference external collections are not supported.
> * Samples must exist for all collections involved in the query.
> * Index Advisor does not recommend covering indexes.

## [](#using-the-workbench)Using the Workbench

Operational Insights provides an **Index Advice** tab in the [Workbench](../query/workbench.md), alongside the **History** and **iQ** tabs, for interactive index recommendations.

### [](#main-query-advice)Main Query Advice

The Main Query Advice section displays index recommendations for the query in the active query editor. Run the query, or click **Update Advice**, to refresh the recommendations. Refreshing recommendations typically takes a few seconds, because the Index Advisor works from collection samples rather than the full dataset.

The panel shows one of the following states:

* **Existing indexes are sufficient** — the current index definition already satisfies the query, and no new index is suggested.
* **Advice available** — the panel displays the message "The index(es) below can speed up this query," along with the current index and the suggested indexes. Click **Build Suggested** to create the suggested index. After the index finishes building, the panel updates to show that existing indexes are sufficient.

While an index is building, **Build Suggested** is grayed out and the panel shows `Building Index`. The new index also appears in the [index list](#index-list) with a status of `Building`. The Index Advice panel remains responsive during this process, and it updates if you run a new query or toggle **Recent Queries**.

### [](#rbac)RBAC

Retrieving index advice requires read access. Building a suggested index requires read and write access.

### [](#errors)Errors

The Index Advice panel reports the following conditions:

* **Missing collection samples**: If a collection referenced in the query does not have samples, the panel shows an error along with the `ANALYZE COLLECTION` statement needed to create them. If more than one collection is missing samples, the panel lists the statements in sequence. After you run the statements, the panel automatically shows index advice.  
Index recommendations are cost-based decisions that rely on statistics derived from data samples. You must collect samples on all collections referenced in the query before using the Index Advisor. For more information, see [Collecting Samples](5b%5Fcbo.md#Collecting%5Fsamples).
* **Cost-based optimizer disabled**: If the Cost-Based Optimizer (CBO) is off, the panel does not return index recommendations and shows a message that the CBO is off. For more information, see [Turning the Cost-Based Optimizer On or Off](5b%5Fcbo.md#Activation).

### [](#index-list)Index List

The lower half of the **Index Advice** tab displays a namespace-filtered list of indexes. Selecting a database and scope in the query editor's query context shows a collection filter for the index list.

Each index appears as a collapsible row:

* The row header shows the index name, its keyspace path, and a status badge (`Active` or `Building`).
* Expanding a row shows the index type (`Standard` or `Array`) and the indexed fields.

## [](#syntax)Syntax

To get index recommendations, prefix your query with `ADVISE`.

## [](#examples)Examples

**Example 1: single collection query** 

The Index Advisor can recommend indexes for queries involving a single collection.

```SQL++
ADVISE
SELECT order_id, total_amount
FROM orders
WHERE customer_id = 101
AND order_date = '2026-02-02';
```

**Output:**

```json
[
  {
    "#operator": "Advise",
    "advice": {
      "#operator": "IndexAdvice",
      "adviseinfo": {
        "current_indexes": [],
        "recommended_indexes": {
          "indexes": [
            {
              "index_statement": "CREATE INDEX idx_adv_customer_id_order_date ON `Default`.`Default`.`orders`(customer_id, order_date) EXCLUDE UNKNOWN KEY;"
            }
          ]
        }
      }
    }
  }
]
```

**Example 2: join queries** 

Index Advisor also supports queries involving joins.

```SQL++
ADVISE
SELECT o.order_id, c.customer_name
FROM orders o
JOIN customers c
  ON o.customer_id = c.customer_id
WHERE o.order_date >= '2025-01-01'
AND c.name like 'Michael%';
```

**Output:**

```json
[
  {
    "#operator": "Advise",
    "advice": {
      "#operator": "IndexAdvice",
      "adviseinfo": {
        "current_indexes": [
            {
              "index_statement": "CREATE INDEX idx_cname ON `Default`.`Default`.`customers`(name) EXCLUDE UNKNOWN KEY;"
            }
          ],
        "recommended_indexes": {
          "indexes": [
            {
              "index_statement": "CREATE INDEX idx_adv_customer_id ON `Default`.`Default`.`orders`(customer_id) EXCLUDE UNKNOWN KEY;"
            }
          ]
        }
      }
    }
  }
]
```

Before you run ADVISE on a join query, make sure you have collected samples for every collection in the query and that the query does not reference any external collections.

The Index Advisor might recommend indexes on join keys, filter columns, or both.

**Example 3: array index support** 

Index Advisor can recommend indexes for queries that involve array fields.

```SQL++
ADVISE
SELECT *
FROM products p
WHERE "electronics" IN p.tags;
```

**Output:**

```json
[
  {
    "#operator": "Advise",
    "advice": {
      "#operator": "IndexAdvice",
      "adviseinfo": {
        "current_indexes": [],
        "recommended_indexes": {
          "indexes": [
            {
              "index_statement": "CREATE INDEX idx_adv_array_categories ON `Default`.`Default`.`products`(UNNEST `tags` : string) EXCLUDE UNKNOWN KEY;"
            }
          ]
        }
      }
    }
  }
]
```

If the query filters on array elements, the Index Advisor may suggest an appropriate array index to support efficient evaluation.

## [](#see-also)See Also

* [Using Indexes](7%5Fusing%5Findex.md)
* [Cost-Based Optimizer](5b%5Fcbo.md)