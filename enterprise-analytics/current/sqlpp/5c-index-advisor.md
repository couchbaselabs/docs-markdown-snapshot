---
title: Index Advisor
description: This topic describes how to use the Index Advisor to get index
  recommendations for your queries.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/sqlpp/pages/5c-index-advisor.adoc
  xref: xref:enterprise-analytics:sqlpp:5c-index-advisor.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/sqlpp/5c-index-advisor.html)

# Index Advisor

> This topic describes how to use the Index Advisor to get index recommendations for your queries. 

Well-designed Secondary indexes can significantly improve the performance of analytical queries. The Index Advisor helps you identify optimal secondary indexes based on the query pattern and the underlying data distribution. Index recommendations are cost based decisions, and they rely on statistics derived from data samples. Therefore, before using the Index Advisor, you must collect samples on all collections referenced in the query.

For more information about Indexes documentation, see [Indexes](7%5Fusing%5Findex.md). To collect samples, see [Collecting Samples](5b%5Fcbo.md#Collecting%5Fsamples).

> [!NOTE]
> * Index Advisor works only with SELECT statements.
> * Queries that reference external collections are not supported.
> * Samples must exist for all collections involved in the query.
> * Index Advisor does not currently recommend covering indexes.

## [](#using-the-workbench)Using the Workbench

To retrieve index recommendations in Enterprise Analytics, navigate to the **Workbench** and click **Index Advisor**. The **Advise** window opens and displays the recommended index statements.

## [](#syntax)Syntax

To get index recommendations, prefix your query with `ADVISE`.

### [](#example)Example

```SQL++
ADVISE SELECT * FROM orders WHERE customer_id = 101;
```

## [](#examples)Examples

**Example 1: Single collection query** 

The Index Advisor can recommend indexes for queries involving a single collection.

```SQL++
ADVISE
SELECT order_id, total_amount
FROM orders
WHERE customer_id = 101
AND order_date = '2026-02-02';
```

**Output:**

```SQL++
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

**Example 2: Join Queries** 

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

```SQL++
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

For join queries, ensure the following:

* Samples are collected for all the collections involved in the query.
* The query does not reference external collections.
* The advisor may recommend indexes on join keys, filter columns, or both.

**Example 3: Array Index Support** 

Index Advisor can recommend indexes for queries that involve array fields.

```SQL++
ADVISE
SELECT *
FROM products p
WHERE "electronics" IN p.tags;
```

**Output:**

```SQL++
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

If the query filters on array elements, the advisor may suggest an appropriate array index to support efficient evaluation.

## [](#see-also)See Also

* [Using Indexes](7%5Fusing%5Findex.md)
* [Cost-Based Optimizer](5b%5Fcbo.md)