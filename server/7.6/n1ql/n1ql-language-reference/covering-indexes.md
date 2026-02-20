---
title: Covering Indexes
description: When an index includes the actual values of all the fields
  specified in the query, the index covers the query and does not require an
  additional step to fetch the actual values from the data service.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/n1ql/pages/n1ql-language-reference/covering-indexes.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.6@server:n1ql:n1ql-language-reference/covering-indexes.adoc[]
---

[View original HTML](/server/7.6/n1ql/n1ql-language-reference/covering-indexes.html)

# Covering Indexes

> When an index includes the actual values of all the fields specified in the query, the index covers the query and does not require an additional step to fetch the actual values from the data service. An index, in this case, is called a covering index and the query is called a covered query. As a result, covered queries are faster and deliver better performance. 

Examples on this Page

The examples on this page use the `travel-sample` bucket, which needs to be installed before use. See [Sample Buckets](../../manage/manage-settings/install-sample-buckets.md) for details.

To use the examples on this page, you must set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

## [](#overview)Overview

The following diagram illustrates the query execution work flow without covering indexes:

![Query execution workflow including fetch request from Data service](../_images/n1ql-query-workflow-cad39f42478d55e1bd81a8f9e1ea8f3ab1ee4c41.svg) 

Figure 1\. Query execution workflow including fetch request from Data service

The following diagram illustrates the query execution work flow with covering indexes:

![Query execution workflow with no fetch request from Data service](../_images/n1ql-query-workflow-cover-idx-323fc944ee9de4de2f3e7035e2fad372b3da7d91.svg) 

Figure 2\. Query execution workflow with no fetch request from Data service

As you can see in the second diagram, a well designed query that uses a covering index avoids the additional steps to fetch the data from the data service. This results in a considerable performance improvement.

## [](#details)Details

To see details of covering indexes at work, you can view the query execution plan using the EXPLAIN statement. When a query uses a covering index, the EXPLAIN statement shows that a covering index is used for data access, thus avoiding the overhead associated with key-value document fetches. Consider a simple index, `idx_state`, on the attribute `state` in the `hotel` keyspace:

Index

```sqlpp
CREATE INDEX idx_state on hotel (state) USING GSI;
```

If we select `state` from the `hotel` keyspace, the actual values of the field `state` that are to be returned are present in the index `idx_state`, and avoids an additional step to fetch the data. In this case, the index `idx_state` is called a covering index and the query is a covered query.

Query

```sqlpp
EXPLAIN SELECT state FROM hotel WHERE state = "CA";
```

Plan

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
            "cover ((`hotel`.`state`))",
            "cover ((meta(`hotel`).`id`))"
          ],
          "filter": "(cover ((`hotel`.`state`)) = \"CA\")",
          "index": "idx_state", (2)
// ...
          "#operator": "Parallel",
          "~child": {
            "#operator": "Sequence",
            "~children": [
              {
                "#operator": "InitialProject",
                "result_terms": [
                  {
                    "expr": "cover ((`hotel`.`state`))" (3)
                  }
                ]
              }
// ...
]}}]}}]
```

| **1** | The covers object shows details of the data covered by the index. |
| ----- | ----------------------------------------------------------------- |
| **2** | The index scan step uses the index we created …​                  |
| **3** | And the projection step uses the data covered by the index.       |

If you modify the query to select the `state` and `city` from the `hotel` keyspace using the same index `idx_state`, the index does not contain the values of the `city` field to satisfy the query, and hence a key-value fetch is performed to retrieve this data.

Query

```sqlpp
EXPLAIN SELECT state, city FROM hotel
  USE INDEX (idx_state)
  WHERE state = "CA";
```

Plan

```json
[
  {
    "plan": {
      "#operator": "Sequence",
      "~children": [
        {
          "#operator": "IndexScan3", (1)
          "bucket": "travel-sample",
          "index": "idx_state", (2)
// ...
          "#operator": "Parallel",
          "~child": {
            "#operator": "Sequence",
            "~children": [
              {
                "#operator": "Filter",
                "condition": "((`hotel`.`state`) = \"CA\")"
              },
              {
                "#operator": "InitialProject",
                "result_terms": [
                  {
                    "expr": "(`hotel`.`state`)" (3)
                  },
                  {
                    "expr": "(`hotel`.`city`)"
                  }
                ]
              }
// ...
]}}]}}]
```

| **1** | There is no covers object, showing that the data is not covered by the index. |
| ----- | ----------------------------------------------------------------------------- |
| **2** | The index scan step uses the index we created …​                              |
| **3** | But the projection step does not use the data covered by the index.           |

To use a covering index for the modified query, you must define an index with the `state` and `city` attributes before executing the query.

Index

```sqlpp
CREATE INDEX idx_state_city on hotel (state, city)
USING GSI;
```

> [!IMPORTANT]
> `MISSING` items are not indexed by indexers. To take advantage of covering indexes and for the index to qualify, a query needs to exclude documents where the index key expression evaluates to `MISSING`. For example, the index `index1` defined below covers the following query.
> 
> CREATE INDEX _index1_ ON _keyspace_(_attribute1_) WHERE _attribute2_ = "_value_";
> 
> SELECT _attribute1_ FROM _keyspace_ WHERE _attribute2_ = "_value_" AND _attribute1_ IS NOT MISSING;

Covering indexes are applicable to secondary index scans and can be used with global secondary indexes (GSI). Queries with expressions and aggregates benefit from covering indexes.

> [!NOTE]
> You cannot use multiple GSI indexes to cover a query. You must create a composite index with all the required fields for the query engine to cover by GSI and not require reading the documents from the data nodes.

[Prepared statements](prepare.md) also benefit from using covering indexes.

## [](#examples)Scenarios

The following queries can benefit from covering indexes. Try these statements using `cbq` or the Query Workbench to see the query execution plan.

Example 1\. Expressions and Aggregates

For the first few examples, you must create the following covering index.

Index

```sqlpp
CREATE INDEX idx_city_country on hotel (city, country);
```

Aggregate Query

```sqlpp
EXPLAIN SELECT MAX(country) FROM hotel
WHERE city = "Paris";
```

Plan

```json
// ...
  "covers": [
    "cover ((`hotel`.`city`))",
    "cover ((`hotel`.`country`))",
    "cover ((meta(`hotel`).`id`))",
    "cover (max(cover ((`hotel`.`country`))))"
  ],
  "index": "idx_city_country",
// ...
```

Expression Query

```sqlpp
EXPLAIN SELECT country || city FROM hotel
WHERE city = "Paris";
```

Plan

```json
// ...
  "covers": [
    "cover ((`hotel`.`city`))",
    "cover ((`hotel`.`country`))",
    "cover ((meta(`hotel`).`id`))"
  ],
  "filter": "(cover ((`hotel`.`city`)) = \"Paris\")",
  "index": "idx_city_country",
// ...
```

Example 2\. UNION/INTERSECT/EXCEPT

This example uses the index `idx_city_country` defined previously.

Query

```sqlpp
SELECT country FROM hotel WHERE city = "Paris"
    UNION ALL
SELECT country FROM hotel WHERE city = "San Francisco";
```

Plan

```json
// ...
  "covers": [
      "cover ((`hotel`.`city`))",
      "cover ((`hotel`.`country`))",
      "cover ((meta(`hotel`).`id`))"
  ],
  "filter": "(cover ((`hotel`.`city`)) = \"Paris\")",
  "index": "idx_city_country",
// ...
  "covers": [
      "cover ((`hotel`.`city`))",
      "cover ((`hotel`.`country`))",
      "cover ((meta(`hotel`).`id`))"
  ],
  "filter": "(cover ((`hotel`.`city`)) = \"San Francisco\")",
  "index": "idx_city_country",
// ...
```

Example 3\. Sub-queries

This example uses the index `idx_city_country` defined previously.

Query

```sqlpp
SELECT * FROM (
  SELECT country FROM hotel WHERE city = "Paris"
    UNION ALL
  SELECT country FROM hotel WHERE city = "San Francisco"
) AS newtab;
```

Plan

```json
// ...
  "covers": [
      "cover ((`hotel`.`city`))",
      "cover ((`hotel`.`country`))",
      "cover ((meta(`hotel`).`id`))"
  ],
  "filter": "(cover ((`hotel`.`city`)) = \"Paris\")",
  "index": "idx_city_country",
// ...
  "covers": [
      "cover ((`hotel`.`city`))",
      "cover ((`hotel`.`country`))",
      "cover ((meta(`hotel`).`id`))"
  ],
  "filter": "(cover ((`hotel`.`city`)) = \"San Francisco\")",
  "index": "idx_city_country",
// ...
```

Example 4\. SELECT in INSERT statements

This example uses the index `idx_city_country` defined previously.

Query

```sqlpp
INSERT INTO hotel (KEY UUID(), VALUE city)
  SELECT country, city FROM hotel WHERE city = "Paris";
```

Plan

```json
// ...
  "covers": [
      "cover ((`hotel`.`city`))",
      "cover ((`hotel`.`country`))",
      "cover ((meta(`hotel`).`id`))"
  ],
  "filter": "(cover ((`hotel`.`city`)) = \"Paris\")",
  "index": "idx_city_country",
// ...
```

Example 5\. Arrays in WHERE clauses

First, create a new index, `idx_array`.

```sqlpp
CREATE INDEX idx_array ON hotel(public_likes, name);
```

Then, run the following query:

```sqlpp
SELECT name FROM hotel
  USE INDEX (idx_array)
  WHERE ARRAY_CONTAINS(public_likes, "Jazmyn Harris");
```

Plan

```json
// ...
  "covers": [
      "cover ((`hotel`.`public_likes`))",
      "cover ((`hotel`.`name`))",
      "cover ((meta(`hotel`).`id`))"
  ],
  "filter": "array_contains(cover ((`hotel`.`public_likes`)), \"Jazmyn Harris\")",
  "index": "idx_array",
// ...
```

Example 6\. Collection Operators: FIRST, ARRAY, ANY, EVERY, and ANY AND EVERY

For this example, first insert the following documents into the default collection in the default scope in the `travel-sample` bucket:

```sqlpp
INSERT INTO `travel-sample` VALUES ("account-customerXYZ-123456789",
{ "accountNumber": 123456789,
  "docId": "account-customerXYZ-123456789",
  "code": "001",
  "transDate":"2016-07-02" } );

INSERT INTO `travel-sample` VALUES ("codes-version-9",
{ "version": 9,
  "docId": "codes-version-9",
  "codes": [
    { "code": "001",
      "type": "P",
      "title": "SYSTEM W MCC",
      "weight": 26.2466
    },
    { "code": "166",
      "type": "P",
      "title": "SYSTEM W/O MCC",
      "weight": 14.6448 }
  ]
});
```

Create an index, `idx_account_customer_xyz_transDate`:

```sqlpp
CREATE INDEX idx_account_customer_xyz_transDate
    ON `travel-sample` (SUBSTR(transDate,0,10),code)
    WHERE code != "" AND meta().id LIKE "account-customerXYZ%";
```

Then, run the following query:

```sqlpp
SELECT SUBSTR(account.transDate,0,10) AS transDate, AVG(codes.weight) AS avgWeight
FROM `travel-sample` AS account
JOIN `travel-sample` AS codesDoc ON KEYS "codes-version-9"
LET codes = FIRST c FOR c IN codesDoc.codes WHEN c.code = account.code END
WHERE account.code != "" AND meta(account).id LIKE "account-customerXYZ-%"
AND SUBSTR(account.transDate,0,10) >= "2016-07-01"
AND SUBSTR(account.transDate,0,10) < "2016-07-03"
GROUP BY SUBSTR(account.transDate,0,10);
```

Results

```json
[
  {
    "avgWeight": 26.2466,
    "transDate": "2016-07-02"
  }
]
```

The query plan for the above query shows that the index covers the query.

Plan

```json
// ...
  "covers": [
      "cover (substr0((`account`.`transDate`), 0, 10))",
      "cover ((`account`.`code`))",
      "cover ((meta(`account`).`id`))"
  ],
  "filter": "(cover ((not ((`account`.`code`) = \"\"))) and (cover ((meta(`account`).`id`)) like \"account-customerXYZ-%\") and (\"2016-07-01\" <= cover (substr0((`account`.`transDate`), 0, 10))) and (cover (substr0((`account`.`transDate`), 0, 10)) < \"2016-07-03\"))",
  "filter_covers": {
      "cover ((\"account-customerXYZ\" <= (meta(`account`).`id`)))": true,
      "cover (((meta(`account`).`id`) < \"account-customerXY[\"))": true,
      "cover (((meta(`account`).`id`) like \"account-customerXYZ%\"))": true,
      "cover ((not ((`account`.`code`) = \"\")))": true
  },
  "index": "idx_account_customer_xyz_transDate",
// ...
```

## [](#related-links)Related Links

* [Query Execution: Details](../../learn/services-and-indexes/indexes/index-scans.md#query-execution-details)
* [Index Pushdown Optimizations](../../learn/services-and-indexes/indexes/index%5Fpushdowns.md)
* [Grouping and Aggregate Pushdown](groupby-aggregate-performance.md)
* [Early Filters, Ordering and Pagination](../../learn/services-and-indexes/indexes/early-filters-and-pagination.md)