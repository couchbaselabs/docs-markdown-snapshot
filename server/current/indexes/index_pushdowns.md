[View original HTML](/server/current/indexes/index_pushdowns.html)

> Index Pushdowns are performance optimizations where the Query engine pushes more of the work down to the Indexer. 

The GSI Indexes are a vital part of query performance and are tightly coupled with the Query engine. The Query engine implements many query processing optimizations to achieve the best possible performance for SQL++ queries.

Query Indexer not only indexes data, it also supports various operations such as point scans, range scans, array indexing, sort order, and pagination. The Query engine tries to leverage the indexer functionality as much as possible by pushing down operations to the indexer as part of the index scan. This helps performance, predominantly, in two ways:

1. Minimize the amount of data transferred from Indexer nodes to Query nodes.
2. Minimize the amount of processing done at Query nodes.

Examples on this Page

The examples in this topic use the travel-sample dataset which is shipped with Couchbase Server. For instructions on how to install the sample bucket, see [Sample Buckets](../manage/manage-settings/install-sample-buckets.md).

To use the examples on this page, you must set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql/n1ql-intro/queriesandresults.md#query-context).

## [](#index-projection)Index Projection

When processing a SELECT or DML with a WHERE clause, the Query engine picks one or more qualified indexes to be used for the query. Note that each index will have document field names explicitly specified as index-keys, and some metadata fields, such as `meta().id`, implicitly stored in the index. In earlier releases, the Indexer used to return all index-keys available in the index for the matching documents. From Couchbase Server 5.0, the Query engine requests the exact list of fields needed for the query. For a covered query, it is the fields referred in projection, predicate, GROUP BY clauses, ORDER BY clauses, HAVING clauses, ON key, and subqueries of the query. For non-covered queries, it is just `META().id`.

For example, consider the following index and query:

Example 1\. Index Projection

This example uses the `def_inventory_route_route_src_dst_day` index that comes pre-installed and can be made by the statement:

Index

```sqlpp
CREATE INDEX def_inventory_route_route_src_dst_day
ON route(sourceairport, destinationairport,
   (DISTINCT (ARRAY (v.day) FOR v IN schedule END)));
```

Query

```sqlpp
EXPLAIN SELECT sourceairport FROM route
USE INDEX (def_inventory_route_route_src_dst_day)
WHERE sourceairport = "SFO"
LIMIT 1;
```

Result

```json
{
  "plan": {
    "#operator": "Sequence",
    "~children": [
      {
        "#operator": "Sequence",
        "~children": [
          {
            "#operator": "DistinctScan",
            "limit": "1",
            "scan": {
              "#operator": "IndexScan3",
              "bucket": "travel-sample",
              "covers": [
                "cover ((`route`.`sourceairport`))",
                "cover ((`route`.`destinationairport`))",
                "cover ((distinct (array (`v`.`day`) for `v` in (`route`.`schedule`) end)))",
                "cover ((meta(`route`).`id`))"
              ],
              "filter": "(cover ((`route`.`sourceairport`)) = \"SFO\")",
              "index": "def_inventory_route_route_src_dst_day",
              "index_id": "e7eb4b4555f90179",
              "index_projection": {
                "entry_keys": [ (1)
                  0
                ],
                "primary_key": true (2)
              },
```

The query refers to fields `sourceairport` and `destinationairport`. The index is wider in scope, that is, it has `sourceairport`, `destinationairport`, and `schedule.day` fields.

So, for each matching document, the query requires only a subset of the data stored in the index. With index-projection support, the Query engine indicates the exact data requested as part of the index-scan. In this example,

| **1** | The entry\_keys in the EXPLAIN output indicate the exact index-key fields that should be returned in the index-scan result. This has only one entry (0) indicating the first index-key sourceairport. |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Also, the primary\_key indicates whether the index should return the primary key meta().id of the matching document.                                                                                  |

Note that in some cases (such as when `distinctScan` or `intersectScan` are used, as in this example), the primary key `meta().id` may be retrieved even though the query doesn’t explicitly specify it in the query. Without this optimization, index-scan would return all the index-keys defined in the index. If the `index_projection` field is missing in the EXPLAIN output, then Indexer would return all index-keys.

## [](#predicate-pushdown)Predicate Pushdown

The Query engine and GSI indexes support many optimizations for efficiently processing predicate push-downs. In general, this performance optimization is leveraged when the Query engine decides to use an Index-scan for processing a query, and whole or partial predicates can be pushed to the indexer to filter documents of interest to the query.

For example, in the above query [Example 1](#example-simple) with a simple WHERE clause, the predicate (`sourceairport = "SFO"`) is pushed to the index `def_inventory_route_route_src_dst_day` with the following single `span` and `range`. These attributes exactly define different characteristics of the index scan:

Example 2\. Predicate Pushdown

The `span` and `range` from the EXPLAIN output of [Example 1](#example-simple).

Result

```json
              "spans": [
                {
                  "exact": true,
                  "range": [
                    {
                      "high": "\"SFO\"",
                      "inclusion": 3,
                      "low": "\"SFO\""
                    }
                  ]
                }
              ],
```

* Each span defines details about one index-key summarizing corresponding predicate conditions into a range-scan lookup for the index. In this example, the predicate condition (`sourceairport = "SFO"`) translates to one span with one range that specifies both `low` and `high` values of "SFO" (to imply equals condition).
* Refer to section [Index Scans](index-scans.md) for more information.

## [](#composite-predicate-pushdown)Composite Predicate Pushdown

Compound or composite predicates are those with multiple conditions on different fields of the document. When the predicate is conjunctive with multiple `AND` conditions, then a single span with multiple ranges is specified in the index-scan request. When the predicate is disjunctive, then multiple spans are specified. See [Index Scans](index-scans.md) for more details and examples on how predicate pushdown works for various types of index-scans, as well as the conjunctive predicate `AND` and the disjunctive predicate `OR`.

### [](#index-key-order-and-structure)Index Key Order and Structure

Composite indexes have more than one index key, and the order of the index keys is important for any lookup or scan of the index, because the indexes structure all the indexed entries in linearized default collation sorted order of all the index-keys. For example, consider the following hypothetical index:

```sqlpp
CREATE INDEX `idx_age_name` ON users(age, name);
```

![Order of keys in a composite index](_images/IndexKeyOrder.png) 

Various age and name values are stored in the index in a tree-like structure, represented in simplified form in the diagram above, with all the index key values linearly sorted as ordered pairs. For instance,

* The diagram above shows index-entries with all names in sorted order with an age of 20 followed by the entries for age 21 and related names.
* The arrowed paths logically depict how an index lookup or scan would find entries in the index.
* A point lookup query for `age=20 AND name="joe"` may follow arrows labelled **p1**.
* Similarly, a range scan for `(age BETWEEN 20 and 21) AND (name="joe")` may find entries of interest between the paths labelled **p1** and **p2** (highlighted in green).

|  | This range may include some unwanted entries (such as "mark", "abby", "anne") which will be filtered subsequently. Queries with predicates such as (age = 20) AND (name BETWEEN "joe" and "mark") will need all the entries found using range scans. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

In general, when the predicate has a range condition on prefixing index-keys (such as `age`) may produce unwanted results from the range-scan index-lookups. In Couchbase Server, the Query service and Indexer are enhanced with complete and accurate predicate pushdown to filter such unnecessary results in the Indexer itself. This improves query performance as it saves the additional overhead in transferring the unwanted data/results to query nodes and subsequently filtering the results. This is explained with an example in the following section: [Composite Predicate with Range Scan on Prefix Index-Keys](#range-scan-prefix).

### [](#range-scan-prefix)Composite Predicate with Range Scan on Prefix Index-Keys

The Query engine supports efficient predicate pushdown to indexes in the cases when the WHERE clause has a range predicate on any of the prefixing index-keys.

Consider the following query, which finds all destination airports within 2000 miles of LAX.

Example 3\. Composite Predicate with Range Scan

Index

```sqlpp
CREATE INDEX idx_route_src_dst_dist
ON route(distance, sourceairport, destinationairport);
```

Query

```sqlpp
EXPLAIN SELECT destinationairport
FROM route
USE INDEX (idx_route_src_dst_dist)
WHERE distance < 2000 AND sourceairport = "LAX"; (1)
```

| **1** | In this query, the predicate has the range condition on the first index-key distance and an equality predicate on the 2nd index-key sourceairport. |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------- |

Results

```json
{
  "plan": {
    "#operator": "Sequence",
    "~children": [
      {
        "#operator": "IndexScan3",
        "bucket": "travel-sample",
        "covers": [
          "cover ((`route`.`distance`))",
          "cover ((`route`.`sourceairport`))",
          "cover ((`route`.`destinationairport`))",
          "cover ((meta(`route`).`id`))"
        ],
        "filter": "((cover ((`route`.`distance`)) < 2000) and (cover ((`route`.`sourceairport`)) = \"LAX\"))",
        "index": "idx_route_src_dst_dist",
        "index_id": "6a502445eefe20b5",
        "index_projection": {
          "entry_keys": [
            0,
            1,
            2
          ]
        },
        "keyspace": "route",
        "namespace": "default",
        "scope": "inventory",
        "spans": [ (1)
          {
            "exact": true,
            "range": [ (2)
              {
                "high": "2000", (3)
                "inclusion": 0,
                "low": "null"
              },
              {
                "high": "\"LAX\"", (4)
                "inclusion": 3,
                "low": "\"LAX\""
              }
            ]
          }
        ],
```

| **1** | The spans attribute of the EXPLAIN query plan output shows that the predicate is accurately represented and pushed-down to the indexer.          |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **2** | The range\[\] attribute is an array of the predicate bounds for individual index-keys involved in the compound predicate.                        |
| **3** | The first element of range\[\] corresponds to the index-key distance with (low, high) values (null, 2000) respectively.                          |
| **4** | The second element of range\[\] corresponds to the index-key sourceairport with (low, high) values ("LAX", "LAX") representing equals condition. |

The Indexer processes the lookup request and exactly returns only the documents matching the predicate conditions. For example, when you [enable monitoring](../n1ql/n1ql-manage/monitoring-n1ql-query.md) with the configuration parameter `profile = "timings"` for this query, you can see that the indexer returns 165 documents, which is the same as the final result set of the query.

```json
    "~children": [
      {
        "#operator": "IndexScan3",
        "#stats": {
          "#heartbeatYields": 54,
          "#itemsOut": 165,
          "#phaseSwitches": 663,
          "execTime": "462.968µs",
          "kernTime": "638.333µs",
          "servTime": "38.110289ms"
        },
// ...
      {
        "#operator": "Stream",
        "#stats": {
          "#itemsIn": 165,
          "#itemsOut": 165,
          "#phaseSwitches": 166,
          "execTime": "354.652µs"
        }
      }
```

### [](#composite-predicate-with-skip-key-range-scan)Composite Predicate with Skip-Key Range Scan

In [Example 3](#example-comp-explain) above, the query has a composite predicate on continuous leading index-keys, namely the index-keys `distance` and `sourceairport`, which occur together at the start of the index definition. In Couchbase Server 6.5 and later, it is possible to push down a composite predicate on non-continuous leading index-keys. There must be a predicate on the first key in the index definition, and then on any of the subsequent index-keys.

Consider the following query, which is a variant of the query in [Example 3](#example-comp-explain) above, and uses the same index.

Example 4\. Composite Predicate with Skip-Key Range Scan

Query

```sqlpp
EXPLAIN SELECT sourceairport
FROM route
USE INDEX (idx_route_src_dst_dist)
WHERE distance < 2000 AND destinationairport = "LAX"; (1)
```

| **1** | This query has a range predicate on the first index-key distance and an equality predicate on the 3rd index-key destinationairport. There is no predicate on the 2nd index-key sourceairport. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Results

```json
[
  {
    "plan": {
      "#operator": "Sequence",
      "~children": [
        {
          "#operator": "IndexScan3",
          "bucket": "travel-sample",
          "covers": [
            "cover ((`route`.`distance`))",
            "cover ((`route`.`sourceairport`))",
            "cover ((`route`.`destinationairport`))",
            "cover ((meta(`route`).`id`))"
          ],
          "filter": "((cover ((`route`.`distance`)) < 2000) and (cover ((`route`.`destinationairport`)) = \"LAX\"))",
          "index": "idx_route_src_dst_dist",
          "index_id": "6a502445eefe20b5",
          "index_projection": {
            "entry_keys": [
              0,
              1,
              2
            ]
          },
          "keyspace": "route",
          "namespace": "default",
          "scope": "inventory",
          "spans": [ (1)
            {
              "exact": true,
              "range": [
                {
                  "high": "2000", (2)
                  "inclusion": 0,
                  "low": "null"
                },
                {
                  "inclusion": 0 (3)
                },
                {
                  "high": "\"LAX\"", (4)
                  "inclusion": 3,
                  "low": "\"LAX\""
                }
              ]
            }
          ],
```

| **1** | The EXPLAIN query plan output shows that the predicate is pushed-down to the indexer.                                                                |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | The first element of range\[\] corresponds to the index-key distance with (low, high) values (null, 2000) respectively.                              |
| **3** | The second element of range\[\] corresponds to the index-key sourceairport with no low or high bounds, i.e. a whole range scan.                      |
| **4** | The third element of range\[\] corresponds to the index-key destinationairport with (low, high) values ("LAX", "LAX") representing equals condition. |

By skipping the index-key that does not have a predicate, and including all the non-continuous index-keys that do have predicates, the query uses the index more effectively and reduces the number of documents that need to be fetched. This increases query preparation time a little, but vastly speeds up the execution of the query.

## [](#pagination-pushdown)Pagination Pushdown

Pagination in SQL++ queries is achieved by using the LIMIT and OFFSET clauses, and both of the operators can be pushed to indexer whenever possible. These operators may not always be pushed to Indexer, depending on the following factors:

* Whether or not the whole predicate in the WHERE clause can be completely and accurately pushed to a single index.
* When using IntersectScan, the Query engine uses multiple indexes to process the query. As such, LIMIT/OFFSET will need to be processed in the Query engine at a later stage of query processing, and hence cannot be pushed to the Indexer.
* Whether or not the SELECT query has other clauses that may impact pagination, such as ORDER BY or JOIN. For example,

  * When ORDER BY key in the query is different from that of the index order, then the query layer will need to process the sort; and hence, in those cases, the pagination cannot be pushed to the indexer as shown in [Example 7](#example-page-3) below.
  * For JOIN queries, index scans can be used only for the left side keyspace. Subsequent JOIN phrases may filter some documents, after which only LIMIT/OFFSET can be applied. Hence, the pagination operators cannot be pushed when a query has JOIN clauses.

Example 5\. Pagination with Secondary Index

When using a secondary index, both LIMIT and OFFSET operators are pushed to the index. This example uses the `def_inventory_landmark_city` index that comes pre-installed and can be made by the statement:

Index

```sqlpp
CREATE INDEX def_inventory_landmark_city ON landmark(city);
```

Query

```sqlpp
EXPLAIN SELECT * FROM landmark
WHERE city = "San Francisco"
OFFSET  4000  LIMIT 10000;
```

Result

```json
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
            "index": "def_inventory_landmark_city",
            "index_id": "39eb8e83720948f",
            "index_projection": {
              "primary_key": true
            },
            "keyspace": "landmark",
            "limit": "10000", (1)
            "namespace": "default",
            "offset": "4000", (2)
            "scope": "inventory",
            "spans": [
              {
                "exact": true,
                "range": [
                  {
                    "high": "\"San Francisco\"",
                    "inclusion": 3,
                    "low": "\"San Francisco\""
                  }
                ]
              }
            ],
```

| **1** | The IndexScan3 operator handles limit.  |
| ----- | --------------------------------------- |
| **2** | The IndexScan3 operator handles offset. |

Example 6\. Pagination with Primary Index

When using a primary index, both LIMIT and OFFSET operators are pushed to the Indexer. This example uses the `def_inventory_landmark_primary` index that comes pre-installed and can be made by the statement:

Index

```sqlpp
CREATE PRIMARY INDEX `def_inventory_landmark_primary`
  ON landmark;
```

Query

```sqlpp
EXPLAIN SELECT * FROM landmark
OFFSET  4000  LIMIT 10000;
```

Result

```json
{
  "plan": {
    "#operator": "Sequence",
    "~children": [
      {
        "#operator": "Sequence",
        "~children": [
          {
            "#operator": "PrimaryScan3",
            "bucket": "travel-sample",
            "index": "def_inventory_landmark_primary",
            "index_projection": {
              "primary_key": true
            },
            "keyspace": "landmark",
            "limit": "10000", (1)
            "namespace": "default",
            "offset": "4000", (2)
            "scope": "inventory",
            "using": "gsi"
          },
```

| **1** | The PrimaryScan3 operator handles limit.  |
| ----- | ----------------------------------------- |
| **2** | The PrimaryScan3 operator handles offset. |

Example 7\. Pagination with Different Index Order

LIMIT and OFFSET operators are not pushed to the Indexer when the index order is different from that specified in the ORDER BY. This example uses the `def_inventory_landmark_city` index that comes pre-installed and can be made by the statement:

Index

```sqlpp
CREATE INDEX def_inventory_landmark_city ON landmark(city);
```

Query

```sqlpp
EXPLAIN SELECT * FROM landmark
USE INDEX(def_inventory_landmark_city)
WHERE city = "San Francisco"
ORDER BY name
OFFSET  4000  LIMIT 10000;
```

Result

```json
{
  "plan": {
    "#operator": "Sequence",
    "~children": [
      {
        "#operator": "Sequence",
        "~children": [
          {
            "#operator": "IndexScan3", (1)
            "bucket": "travel-sample",
            "index": "def_inventory_landmark_city",
            "index_id": "39eb8e83720948f",
            "index_projection": {
              "primary_key": true
            },
            "keyspace": "landmark",
            "namespace": "default",
            "scope": "inventory",
// ...
      {
        "#operator": "Order",
        "limit": "10000",
        "offset": "4000",
        "sort_terms": [
          {
            "expr": "(`landmark`.`name`)"
          }
        ]
      },
      {
        "#operator": "Offset", (2)
        "expr": "4000"
      },
      {
        "#operator": "Limit", (3)
        "expr": "10000"
      }
```

| **1** | The IndexScan3 operator does not handle offset or limit. |
| ----- | -------------------------------------------------------- |
| **2** | The Offset operator is handled by the Query engine.      |
| **3** | The Limit operator is handled by the Query engine.       |

## [](#using-index-order)Using Index Order

The Query engine may avoid ORDER BY processing in cases where the ordering of entries in the index can be leveraged for the query. The Query engine carefully evaluates each query to decide whether ORDER BY keys are aligned with the index key order. For example, ORDER BY may not be pushed down when the ORDER BY fields are not aligned with the index-key order defining the index.

Example 8\. Ascending Sort by String Field

Find all cities that start with "San", and sort the results by the city name in ascending order. This example uses the `def_inventory_landmark_city` index that comes pre-installed and can be made by the statement:

Index

```sqlpp
CREATE INDEX def_inventory_landmark_city ON landmark(city);
```

Query

```sqlpp
EXPLAIN SELECT city FROM landmark
WHERE city LIKE "San%"
ORDER BY city;
```

Result

```json
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
              "cover ((meta(`landmark`).`id`))"
            ],
            "filter": "(cover ((`landmark`.`city`)) like \"San%\")",
            "index": "def_inventory_landmark_city",
// ...
                {
                  "#operator": "InitialProject",
                  "result_terms": [
                    {
                      "expr": "cover ((`landmark`.`city`))"
                    }
                  ]
                } (1)
// ...
```

| **1** | In this example, you can see that the query plan does not have an ORDER operator before the final projection. That means order pushdown is being leveraged, and the query is relying on the index order. |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Example 9\. Ascending Sort by Primary Key

Find all cities that start with "San", and sort the results by the document primary key in ascending order. This example uses the `def_inventory_landmark_city` index that comes pre-installed and can be made by the statement:

Index

```sqlpp
CREATE INDEX def_inventory_landmark_city ON landmark(city);
```

Query

```sqlpp
EXPLAIN SELECT city FROM landmark
WHERE city LIKE "San%"
ORDER BY meta().id;
```

Result

```json
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
              "cover ((meta(`landmark`).`id`))"
            ],
            "filter": "(cover ((`landmark`.`city`)) like \"San%\")",
            "index": "def_inventory_landmark_city",
// ...
                {
                  "#operator": "InitialProject",
                  "result_terms": [
                    {
                      "expr": "cover ((`landmark`.`city`))"
                    }
                  ]
                }
              ]
            }
          }
        ]
      },
      {
        "#operator": "Order", (1)
        "sort_terms": [
          {
            "expr": "cover ((meta(`landmark`).`id`))"
          }
        ]
      }
```

| **1** | In this example, you can see an additional ORDER operator before the final projection, because the ORDER BY field meta().id is different from the index order key city. |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### Limitation

Currently the Query engine supports order pushdown only when the ORDER BY keys are aligned with the Index order. But reverse-scan of the index is not supported.

For example, in [Example 8](#example-idx-1) above, you can see that the query plan does not have an ORDER operator before the final projection, because the index order is the same as the ascending order specified in the query. Similarly, in the following example [Example 10](#example-idx-3), the ORDER BY clause has DESC, and that matches with the index order defined by the index `idx_landmark_city_desc`.

However, the ASC order in [Example 8](#example-idx-1) will not be able to leverage the index order in the index `idx_landmark_city_desc`, nor will the DESC order in [Example 10](#example-idx-3) be able to leverage the index order in the index `def_inventory_landmark_city`.

Example 10\. Descending Sort by String Field

Descending variation of [Example 8](#example-idx-1).

Index

```sqlpp
CREATE INDEX idx_landmark_city_desc ON landmark(city DESC);
```

Query

```sqlpp
EXPLAIN SELECT city FROM landmark
WHERE city LIKE "San%"
ORDER BY city DESC;
```

Result

```json
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
              "cover ((meta(`landmark`).`id`))"
            ],
            "filter": "(cover ((`landmark`.`city`)) like \"San%\")",
            "index": "idx_landmark_city_desc",
            "index_id": "efc36547ec1c0f00",
            "index_order": [
              {
                "desc": true,
                "keypos": 0
              }
// ...
                {
                  "#operator": "InitialProject",
                  "result_terms": [
                    {
                      "expr": "cover ((`landmark`.`city`))"
                    }
                  ]
                }
```

## [](#operator-pushdowns)Operator Pushdowns

The Query engine tries to avoid unnecessary processing operators such as MIN(), MAX(), and COUNT(), which can be processed by the Indexer much more efficiently. In such cases, the Query engine pushes down necessary hints or options to the Indexer to process the following operators.

### [](#max-pushdown)MAX() Pushdown

This function returns the highest value of the input field based on the default collation rules. (For details, see [Data Types](../n1ql/n1ql-language-reference/datatypes.md) and [Comparison Operators](../n1ql/n1ql-language-reference/comparisonops.md).)

You do not need to create the index with the matching index keys sorted in descending order to push MAX() to the Indexer.

Example 11\. MAX of a String Field

Find the alphabetically highest city name in the `landmark` collection. This example uses the `def_inventory_landmark_city` index that comes pre-installed and can be made by the statement:

Index

```sqlpp
CREATE INDEX def_inventory_landmark_city ON landmark(city);
```

Query

```sqlpp
EXPLAIN SELECT MAX(city)
FROM landmark
USE INDEX (def_inventory_landmark_city)
WHERE city IS NOT NULL;
```

Result

```json
{
  "plan": {
    "#operator": "Sequence",
    "~children": [
      {
        "#operator": "IndexScan3",
        "bucket": "travel-sample",
        "covers": [
          "cover ((`landmark`.`city`))",
          "cover ((meta(`landmark`).`id`))",
          "cover (max(cover ((`landmark`.`city`))))"
        ],
        "index": "def_inventory_landmark_city",
        "index_group_aggs": {
          "aggregates": [
            {
              "aggregate": "MAX",
              "depends": [
                0
              ],
              "expr": "cover ((`landmark`.`city`))",
              "id": 2,
              "keypos": 0
            }
```

### [](#min-pushdown)MIN() Pushdown

This function returns the lowest value of the input field based on the default collation rules. (For details, see [Data Types](../n1ql/n1ql-language-reference/datatypes.md) and [Comparison Operators](../n1ql/n1ql-language-reference/comparisonops.md).)

You do not need to create the index with the matching index keys sorted in ascending order to push MIN() to the Indexer.

Example 12\. MIN of a String Field

Find the alphabetically lowest city name in the `landmark` collection. This example uses the `def_inventory_landmark_city` index that comes pre-installed and can be made by the statement:

Index

```sqlpp
CREATE INDEX def_inventory_landmark_city ON landmark(city);
```

Query

```sqlpp
EXPLAIN SELECT MIN(city)
FROM landmark
USE INDEX (def_inventory_landmark_city)
WHERE city IS NOT NULL;
```

Result

```json
{
  "plan": {
    "#operator": "Sequence",
    "~children": [
      {
        "#operator": "IndexScan3",
        "bucket": "travel-sample",
        "covers": [
          "cover ((`landmark`.`city`))",
          "cover ((meta(`landmark`).`id`))",
          "cover (min(cover ((`landmark`.`city`))))"
        ],
        "index": "def_inventory_landmark_city",
        "index_group_aggs": {
          "aggregates": [
            {
              "aggregate": "MIN",
              "depends": [
                0
              ],
              "expr": "cover ((`landmark`.`city`))",
              "id": 2,
              "keypos": 0
            }
```

### [](#count-pushdown)COUNT() Pushdown

This function returns the total number of non-Null values of an input field from the matching documents of an index scan.

Example 13\. Count of a String Field

Find the number of cities entered in the `landmark` collection. This example uses the `def_inventory_landmark_city` index that comes pre-installed and can be made by the statement:

Index

```sqlpp
CREATE INDEX def_inventory_landmark_city ON landmark(city);
```

Query

```sqlpp
SELECT COUNT(city) AS NumberOfCities
FROM landmark
USE INDEX (def_inventory_landmark_city)
WHERE city IS NOT NULL;
```

Result

```json
[
  {
    "NumberOfCities": 4479
  }
]
```

Example 14\. Count Details

The details behind [Example 13](#example-count-out).

Query

```sqlpp
EXPLAIN SELECT COUNT(city) AS NumberOfCities
FROM landmark
USE INDEX (def_inventory_landmark_city)
WHERE city IS NOT NULL;
```

Result

```json
{
  "plan": {
    "#operator": "Sequence",
    "~children": [
      {
        "#operator": "IndexScan3", (1)
        "bucket": "travel-sample",
        "covers": [
          "cover ((`landmark`.`city`))",
          "cover ((meta(`landmark`).`id`))",
          "cover (count(cover ((`landmark`.`city`))))"
        ],
        "index": "def_inventory_landmark_city",
        "index_group_aggs": {
          "aggregates": [
            {
              "aggregate": "COUNT",
              "depends": [
                0
              ],
              "expr": "cover ((`landmark`.`city`))",
              "id": 2,
              "keypos": 0
            }
```

| **1** | The index operator IndexCountScan3 counts values so the Query Service does not need to do additional processing. |
| ----- | ---------------------------------------------------------------------------------------------------------------- |

### [](#countdistinct-pushdown)COUNT(DISTINCT) Pushdown

This function returns the total number of unique non-Null values of an input field from the matching documents of an index scan.

Example 15\. Count Distinct of a String Field

Find the number of unique city names in the `landmark` collection. This example uses the `def_inventory_landmark_city` index that comes pre-installed and can be made by the statement:

Index

```sqlpp
CREATE INDEX def_inventory_landmark_city ON landmark(city);
```

Query

```sqlpp
SELECT COUNT (DISTINCT city) AS NumberOfDistinctCities
FROM landmark
USE index (def_inventory_landmark_city)
WHERE city IS NOT NULL;
```

Result

```json
[
  {
    "NumberOfDistinctCities": 625
  }
]
```

Example 16\. Count Distinct Details

The details behind [Example 15](#example-distinct-out).

Query

```sqlpp
EXPLAIN SELECT COUNT (DISTINCT city) AS NumberOfDistinctCities
FROM landmark
USE index (def_inventory_landmark_city)
WHERE city IS NOT NULL;
```

Result

```json
{
  "plan": {
    "#operator": "Sequence",
    "~children": [
      {
        "#operator": "IndexScan3", (1)
        "bucket": "travel-sample",
        "covers": [
          "cover ((`landmark`.`city`))",
          "cover ((meta(`landmark`).`id`))",
          "cover (count(DISTINCT cover ((`landmark`.`city`))))"
        ],
        "index": "def_inventory_landmark_city",
        "index_group_aggs": {
          "aggregates": [
            {
              "aggregate": "COUNT",
              "depends": [
                0
              ],
              "distinct": true,
              "expr": "cover ((`landmark`.`city`))",
              "id": 2,
              "keypos": 0
            }
```

| **1** | The index operator IndexCountScan3 counts distinct values so the Query Service does not need to do additional processing. |
| ----- | ------------------------------------------------------------------------------------------------------------------------- |

## [](#related-links)Related Links

* [Query Execution: Details](index-scans.md#query-execution-details)
* [Covering Indexes](covering-indexes.md)
* [Grouping and Aggregate Pushdowns](groupby-aggregate-performance.md)
* [Early Filters, Order, and Pagination](early-filters-and-pagination.md)