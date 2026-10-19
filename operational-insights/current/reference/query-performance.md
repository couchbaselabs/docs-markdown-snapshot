---
title: Query Performance Optimization
description: Learn techniques to make SQL++ queries in Operational Insights
  faster and more resource-efficient, from reducing the amount of data a query
  reads to creating secondary indexes, gathering optimizer samples, and tuning
  the query engine.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/reference/pages/query-performance.adoc
  xref: xref:enterprise-analytics:reference:query-performance.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/reference/query-performance.html)

# Query Performance Optimization

> Learn techniques to make SQL++ queries in Operational Insights faster and more resource-efficient, from reducing the amount of data a query reads to creating secondary indexes, gathering optimizer samples, and tuning the query engine. 

## [](#overview)Overview

Operational Insights runs queries on a massively parallel processing (MPP) query engine over a column-oriented, Log-Structured Merge (LSM) tree-based storage engine. A cost-based optimizer (CBO) chooses the plan for each query based on samples of your data. Most of the time, query performance depends on 3 things:

* How much data the query reads. Fewer fields, fewer objects, and fewer external files mean less I/O.
* Which access paths are available. Secondary indexes, array indexes, and covering indexes let the engine avoid full collection scans.
* How much the optimizer knows about your data. Optimizer samples let the CBO choose indexes, join methods, and join orders.

Work through the techniques in this topic in the following order:

* [Measure the query](#measure-the-query)
* [Reduce the data the query reads](#reduce-the-data)
* [Optimize queries on external collections](#optimize-external)
* [Create secondary indexes](#create-indexes)
* [Enable cost-based optimization](#enable-cbo)
* [Tune join execution](#tune-joins)
* [Tune sorting and OR predicates](#tune-sorting)
* [Precompute repeated work](#precompute)
* [Configure service resources](#configure-resources)

> [!NOTE]
> Changing the configuration parameters and hints in this topic does not change query correctness — they affect only performance characteristics such as response time, memory use, and throughput. Scan consistency, covered separately in [Configure Service Resources](#configure-resources), is the exception: it can change which data a query sees.

## [](#measure-the-query)Measure the Query

Before you change anything, find out where the query spends its time. Operational Insights provides query metrics, a query plan, per-operator timings, and a view of running queries to help you do this.

### [](#review-query-metrics)Review Query Metrics

When you run a query in the Workbench, metrics for that query appear between the query editor and the results pane:

| Metric           | What it tells you                                                                                                                    |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| elapsed          | The overall query time.                                                                                                              |
| execution        | The query execution time.                                                                                                            |
| waiting in queue | Time spent waiting before execution started. A high value points to a concurrency or capacity issue rather than to the query itself. |
| docs scanned     | The number of JSON documents scanned.                                                                                                |
| docs returned    | The number of JSON documents returned.                                                                                               |
| size             | The size of the results, in bytes.                                                                                                   |

A large gap between `docs scanned` and `docs returned` usually means that the query is scanning a whole collection to find a small number of matches. In that case, consider a more selective filter, a secondary index, or a narrower location path for an external collection.

### [](#inspect-the-query-plan)Inspect the Query Plan

The Workbench returns the query plan with every query. Select the Plan tab for a graphical plan, or the Plan Text tab for the plan in JSON format. In the plan, check:

* Whether the query uses a secondary index or scans the whole collection.
* Which join methods the plan uses (hash join, hash broadcast join, or index nested-loop join), and which side is the build side.
* The operator-estimates section (`cardinality`, `op-cost`, `total-cost`) that the cost-based optimizer adds to each operator. If this section is missing, the collections in the query have no optimizer samples. See [Enable Cost-Based Optimization](#enable-cbo).

### [](#collect-per-operator-timings)Collect Per-Operator Timings

To see how long each operator takes, open the Workbench Run-Time Preferences (the Settings icon), select Collect query timings, and run the query again. The timings appear in the query plan.

If you submit queries through the Analytics Service REST API, you can request the `optimized-logical-plan`, `logical-plan`, `job`, and `profile` in the query response.

### [](#monitor-running-queries)Monitor Running Queries

In the Workbench, click monitor to see active, completed, and open queries, including their duration and the node where each ran. You can cancel long-running queries from the Active page.

## [](#reduce-the-data)Reduce the Data the Query Reads

The following techniques reduce how much data Operational Insights has to read for a query.

### [](#project-only-the-fields-you-need)Project Only the Fields You Need

Operational Insights stores collections in a columnar format, so a query reads only the columns for the fields it references. Queries that return entire objects with `SELECT *` have to read every column. Name only the fields you need. `SELECT EXCLUDE` trims fields from the output after the full record is read, so it does not reduce I/O the way naming fields does.

Example

```sql
-- Reads every column of every object
SELECT * FROM sampleAnalytics.Commerce.customers;

-- Reads only three columns
SELECT c.custid, c.name, c.rating
FROM sampleAnalytics.Commerce.customers AS c;
```

### [](#keep-the-column-storage-format)Keep the Column Storage Format

Remote collections use the column storage format by default. You can set the format explicitly with the `storage-format` parameter when you create the collection. Keep the default column format for analytical workloads.

Example

```sql
CREATE COLLECTION sampleAnalytics.Commerce.orders
WITH { "storage-format": { "format": "column" } }
ON commerce.inventory.orders AT myLink;
```

### [](#filter-and-reshape-data-at-ingestion)Filter and Reshape Data at Ingestion

Data that never lands in Operational Insights is data that no query has to read. When you create a remote collection, you can do either of the following. You cannot use both on the same collection.

* Add a `WHERE` clause so that Operational Insights ingests only matching documents.
* Attach a `TRANSFORM FUNCTION` with `APPLY FUNCTION` to filter records, remove unneeded fields, or reshape each incoming document before it's stored.

Example

```sql
-- Ingest only French airports
CREATE COLLECTION `travel-sample`.inventory.airports_fr
ON `travel-sample`.inventory.airport AT myLink
WHERE country = "France";

-- Keep only the fields that analysts query
CREATE TRANSFORM FUNCTION project_fields(input) {
  SELECT VALUE doc FROM (
    SELECT d.custid, d.name, d.rating FROM [input] d
  ) AS doc
};

CREATE COLLECTION sampleAnalytics.Commerce.customers_slim
ON commerce.inventory.customers AT myLink
APPLY FUNCTION project_fields;
```

### [](#write-filters-that-the-engine-can-use)Write Filters That the Engine Can Use

* Filter early and selectively. Put the most selective predicates in the `WHERE` clause rather than filtering results in an outer query or in your application.
* Compare a field directly with a literal. Predicates of the form `field operator literal`, where the operator is `=`, `<`, `⇐`, `>`, `>=`, or `BETWEEN`, can use secondary indexes.
* Match the stored data type. `WHERE age < 30` and `WHERE age < "30"` match different objects. Use literals of the same type as the stored values, and use the same type in your index definitions.
* Use `LIMIT` when you need only a subset of the results.

Operational Insights keeps minimum and maximum values for stored columns and uses these column filters to skip data that cannot match a range or equality predicate. Operational Insights enables column filters by default. The `compilerColumnFilter` service configuration parameter controls them.

### [](#avoid-unbounded-field-names)Avoid Unbounded Field Names

In the columnar format, each distinct field name becomes a column. Do not use unique values, such as IDs or timestamps, as field names: for example, `{"u_1839": {…​}, "u_1840": {…​}}`. Documents shaped like this can create thousands of columns, which increases memory use, slows ingestion and merge operations, and can cause out-of-memory errors. Store such values as field values inside an array instead, or reshape the data with a `TRANSFORM FUNCTION` at ingestion.

For more information, see [About Operational Insights Enterprise](../intro/intro.md), [SELECT Statements](../sqlpp/3%5Fquery.md), [CREATE a Remote Collection](../sqlpp/5%5Fddl%5Fremote.md), [User-Defined Functions](../sqlpp/9%5Fudf.md), and [Operational Insights Release Notes](../release-notes/release-notes.md).

## [](#optimize-external)Optimize Queries on External Collections

You cannot create indexes or gather optimizer samples on external collections. Instead, you make external queries efficient by reducing the number of files and fields that Operational Insights reads from object storage. Reading fewer files also reduces requests to your storage provider and the associated costs.

### [](#make-the-location-path-as-specific-as-possible)Make the Location Path as Specific as Possible

The `PATH` (or `USING`) clause of `CREATE EXTERNAL COLLECTION` acts as a filter on the bucket. Operational Insights never reads files outside that path, so point it at the smallest set of prefixes that holds the data you need.

A `WHERE` clause on a collection with only static prefixes does not reduce the number of files read: the engine reads every file under the path first, then applies the filter afterwards.

### [](#use-dynamic-prefixes-to-filter-files-at-query-time)Use Dynamic Prefixes to Filter Files at Query Time

Dynamic prefixes are typed tokens in the path, in the format `{TOKEN_NAME:DATA_TYPE}`, where the data type is `int`, `double`, or `string`. When a query supplies values for these tokens in its `WHERE` clause, Operational Insights reads only the matching prefixes. The `WHERE` clause can use `=`, `!=`, `<`, `>`, `BETWEEN`, and `IN` on the tokens.

Example

```sql
CREATE EXTERNAL COLLECTION reviewsCollection
ON `myBucket`
USING "reviews/{year:int}/{month:string}"
AT myLink
WITH { "format": "json", "embed-filter-values": "true" };

-- Reads all 24 files
SELECT * FROM reviewsCollection;

-- Reads 12 files, under reviews/2022/
SELECT * FROM reviewsCollection WHERE year = 2022;

-- Reads 1 file, under reviews/2022/dec/
SELECT * FROM reviewsCollection WHERE year = 2022 AND month = "dec";
```

With dynamic prefixes, a single collection can replace many static-path collections while still reading only the files each query needs.

### [](#include-or-exclude-files)Include or Exclude Files

Use the `include` or `exclude` parameter in the `WITH` clause to query only files that match a name pattern, such as `"include": "*.parquet"`. You can specify one or the other, not both.

### [](#prefer-column-oriented-table-formats)Prefer Column-Oriented Table Formats

External collections can read JSON, CSV, TSV, Parquet, and Avro files, as well as Delta Lake and Apache Iceberg tables. For large analytical datasets, prefer columnar formats such as Parquet, Delta Lake, and Iceberg:

* Field pushdown. Operational Insights pushes field accesses down to the external scan operator, so it reads only the referenced fields. Operational Insights enables this by default through the `compilerExternalFieldPushdown` service configuration parameter.
* Iceberg pruning. For Iceberg tables, Operational Insights applies `WHERE` predicates to perform partition pruning and manifest-level exclusion before it reads any data files, and projects only the required columns.
* Parquet file splits. The `compilerParquetFilesplits` service configuration parameter lets Operational Insights split large Parquet files into parallel scan units. It's disabled by default.

For more information, see [External Storage Data Organization](../sources/dynamic-prefixes.md), [CREATE an External Collection](../sqlpp/5%5Fddl%5Fexternal.md), [Apache Iceberg](../sqlpp/5%5Fddl%5Ficeberg.md), and [Set Up an External Data Source](../sources/manage-external.md).

## [](#create-indexes)Create Secondary Indexes

A secondary index is a materialized lookup structure on a remote or standalone collection. Operational Insights maintains indexes automatically as it ingests data, and rebalances them when the cluster scales. You cannot index external collections.

### [](#when-the-optimizer-uses-an-index)When the Optimizer Uses an Index

The optimizer considers a secondary index when both of these conditions are true:

* The query has a conjunctive equality or range predicate (`=`, `>`, `>=`, `<`, `⇐`, `BETWEEN`) on one or more fields, or a join predicate.
* The fields in the predicate form a prefix of the index key.

Example

```sql
CREATE INDEX idx_s_d ON foo(c_s: STRING, c_d: DOUBLE);

-- Uses idx_s_d: c_s is a prefix of (c_s, c_d)
SELECT f.c_x FROM foo f WHERE f.c_s = "world";

-- Cannot use idx_s_d: c_d alone is not a prefix
SELECT f.c_x FROM foo f WHERE f.c_d = 3.5;
```

### [](#order-composite-index-fields-by-filter-usage)Order Composite Index Fields by Filter Usage

Put the fields your queries filter on first in a composite index. If one index is on `(age, name)` and another is on `(name)`, a query that filters on `name` uses the `(name)` index, because its leading field matches the predicate.

### [](#use-covering-indexes)Use Covering Indexes

A covering index contains every field that a query needs, both for filtering and for its results. The optimizer can usually answer the query from the index alone, without fetching the underlying objects, though it can still fall back to a primary-index lookup for some entries. The `compiler.index.covering` parameter enables covering (index-only) plans by default.

Example

```sql
CREATE INDEX idx_name ON user(name: STRING);

-- Answered entirely from idx_name
SELECT u.name FROM user u WHERE u.name = "name1";
```

### [](#combine-indexes-with-index-intersection)Combine Indexes with Index Intersection

When a query filters on several separately indexed fields, the optimizer can use all of those indexes and intersect the matching primary keys. For example, with one index on `c1` and another on `c2`, the predicate `c1 = 100 AND c2 = 200` can use both.

### [](#use-array-indexes-for-nested-arrays)Use Array Indexes for Nested Arrays

Array indexes index the values in an array, or fields of objects nested in arrays, at any depth. You must specify `EXCLUDE UNKNOWN KEY` when you create an array index.

Example

```sql
CREATE INDEX pCategoriesIdx
ON products (UNNEST categories: STRING)
EXCLUDE UNKNOWN KEY;

-- Membership and existential queries use the index
SELECT p FROM products p WHERE "Food" IN p.categories;
SELECT p FROM products p WHERE SOME c IN p.categories SATISFIES c = "Food";
```

To make sure the optimizer can use an array index:

* For universal (`EVERY`) queries, add a non-empty condition such as `LEN(o.items) > 0`. Empty arrays are not stored in array indexes.
* For explicit `UNNEST` queries on a multi-field array index, include a predicate on every indexed field, even if it's a placeholder such as `i.price > 0`.
* Do not rely on array indexes to cover queries. They only accelerate predicates on arrays.

### [](#index-join-keys)Index Join Keys

If one side of a join is small and the larger (inner) side has an index on the join field, an index nested-loop join can be the most efficient plan. The cost-based optimizer chooses this plan when it's the cheapest. You can also request it with the `indexnl` hint. See [Tune Join Execution](#tune-joins).

### [](#index-collections-behind-views-and-tabular-views)Index Collections Behind Views and Tabular Views

Views are not materialized, so you create indexes on the underlying collection. For a tabular view, add a `CAST` clause so that it casts the indexed values the same way the view casts them.

Example

```sql
CREATE INDEX idx2 ON staff(hiredate: DATE) CAST (DEFAULT NULL DATE "MM/DD/YYYY");
```

### [](#get-recommendations-from-the-index-advisor)Get Recommendations from the Index Advisor

The Index Advisor recommends secondary indexes, including array indexes and join-key indexes, based on your query and the data distribution. Prefix a `SELECT` statement with `ADVISE`, or click Index Advisor in the Workbench.

Example

```sql
ADVISE
SELECT order_id, total_amount
FROM orders
WHERE customer_id = 101 AND order_date = "2026-02-02";
```

> [!NOTE]
> Before you use the Index Advisor, run `ANALYZE COLLECTION` on every collection in the query. The Index Advisor works only with `SELECT` statements, does not support external collections, and does not currently recommend covering indexes.

### [](#skip-an-index-when-it-does-not-help)Skip an Index When It Does Not Help

If a predicate matches a large part of the collection, a full scan can be faster than an index lookup. The optimizer usually makes this decision for you. To override it for a single predicate, use the `skip-index` hint:

Example

```sql
SELECT f.c_x FROM foo f WHERE f.c_s /*+ skip-index */ = "world";
```

To stop the optimizer from considering array indexes for a query, set `compiler.arrayindex` to `false`.

For more information, see [Indexes](../sqlpp/7%5Fusing%5Findex.md), [CREATE INDEX Statements](../sqlpp/5%5Fddl%5Findex.md), [Index Advisor](../sqlpp/5c-index-advisor.md), and [Views and Tabular Views](../sqlpp/5a%5Fviews.md).

## [](#enable-cbo)Enable Cost-Based Optimization

Operational Insights runs queries through a cost-based optimizer (CBO). The CBO chooses which indexes to use, which join method to use, and in what order to join collections, based on samples of your data. Without a sample for a collection, the optimizer has no information about its data, so Operational Insights falls back to rule-based optimization for any query that touches it.

You can tell whether a query used the CBO by checking its query plan. When the CBO plans a query, each operator in the plan includes an operator-estimates section. If that section is missing, the collections in the query have no samples yet.

### [](#gather-samples)Gather Samples

Run `ANALYZE COLLECTION` on each remote and standalone collection that you query:

Example

```sql
ANALYZE COLLECTION sampleAnalytics.Commerce.customers;

-- Larger, repeatable sample: sample-seed requires sample-method "full-scan"
ANALYZE COLLECTION sampleAnalytics.Commerce.customers
WITH { "sample": "medium", "sample-method": "full-scan", "sample-seed": 42 };
```

| Sample size   | Objects sampled                                                |
| ------------- | -------------------------------------------------------------- |
| low (default) | 1063                                                           |
| medium        | 4 × 1063                                                       |
| high          | 4 × 4 × 1063                                                   |
| integer       | Any value from 1063 to 68032, to set the sample size directly. |

Use a larger sample when data is skewed or estimates in the query plan are far from actual row counts.

### [](#keep-samples-current)Keep Samples Current

* Run `ANALYZE COLLECTION` again when a collection's data changes significantly. Base the frequency on the collection's rate of change and on how often you query it.
* Run `ANALYZE COLLECTION` after you populate a collection with `CREATE COLLECTION AS`, `COPY INTO`, or bulk `INSERT` and `UPSERT` statements.
* You can gather samples only from collections, not from views or external collections.

### [](#verify-that-the-cbo-ran)Verify That the CBO Ran

The cost-based optimizer is on by default (`compiler.cbo`). Hash joins also show a build-side field in the plan when the CBO runs. To remove a sample, use `ANALYZE COLLECTION … DROP STATISTICS`.

For more information, see [Cost-Based Optimizer](../sqlpp/5b%5Fcbo.md) and [Performance Tuning](../sqlpp/appendix%5F2%5Fparameters.md).

## [](#tune-joins)Tune Join Execution

With samples in place, the cost-based optimizer usually chooses the best join method and order. Use the parameters and hints in this section only when you have confirmed from the query plan that the optimizer's choice is not optimal.

### [](#choose-a-plan-shape-for-multi-way-joins)Choose a Plan Shape for Multi-Way Joins

Set `compiler.queryplanshape` to control how the optimizer builds multi-way hash joins:

| Value            | Behavior                                                        | Trade-off                        |
| ---------------- | --------------------------------------------------------------- | -------------------------------- |
| zigzag (default) | The smaller input is the build side.                            | Balances speed and memory.       |
| leftdeep         | After the first join, previous join results are the build side. | Uses less memory. Can be slower. |
| rightdeep        | After the first join, base collections are the build side.      | Can be faster. Uses more memory. |

Example

```sql
SET `compiler.queryplanshape` "leftdeep";
SELECT ...
```

To join collections in the order they appear in the `FROM` clause, set `compiler.forcejoinorder` to `true`.

### [](#use-join-hints)Use Join Hints

| Hint                  | Use when                                                                                                                                                        | Example                                                                                           |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| productivity          | The optimizer misestimates join cardinality, especially for joins between 2 foreign keys.                                                                       | c.c\_nationkey /\*+ productivity s 600.0 \*/ = s.s\_nationkey                                     |
| hashjoin build\|probe | You want a hash join with a specific collection on the build or probe side.                                                                                     | cn.c\_custkey /\*+ hashjoin build (o) \*/ = o.o\_custkey                                          |
| hash-bcast            | One side of the join is small and the other is large. Operational Insights replicates the small side to all partitions and does not repartition the large side. | c.c\_nationkey /\*+ hash-bcast (n) \*/ = n.n\_nationkey (in a subquery where n is the small side) |
| indexnl               | The outer side is small and the inner side has an index on the join field.                                                                                      | c.c\_nationkey /\*+ indexnl \*/ = n.n\_nationkey                                                  |

A hint's parameter must name a base collection or alias. If it does not, the optimizer ignores the hint, returns a warning, and considers all join methods.

For more information, see [Performance Tuning](../sqlpp/appendix%5F2%5Fparameters.md).

## [](#tune-sorting)Tune Sorting and OR Predicates

This section covers 2 techniques: speeding up large `ORDER BY` results with full parallel sort, and tuning how the engine evaluates large `OR` predicates.

### [](#use-full-parallel-sort-for-large-order-by-results)Use Full Parallel Sort for Large ORDER BY Results

By default, Operational Insights uses full parallel sort: it samples and range-partitions the data first, so it does not need a final single-node merge. Set `compiler.sort.parallel` to `false` only to compare against the older, single-node-merge behavior.

Example

```sql
SET `compiler.sort.parallel` "true";
SELECT VALUE o
FROM orders AS o
ORDER BY ARRAY_LENGTH(o.o_items) DESC;
```

### [](#tune-evaluation-of-large-or-predicates)Tune Evaluation of Large OR Predicates

The following service configuration parameters control how the engine evaluates disjunctions (`OR` predicates):

* `compilerDisjunctionAsJoin`: rewrites disjunctions as joins in query plans.
* `compilerDisjunctionHashThreshold`: the number of disjunctions above which the engine uses a hash-based approach. The default is `40` on a cluster provisioned from 3.0 onwards. Clusters upgraded from before 2.1.1 keep `-1` (disabled), to preserve their existing plans.

For more information, see [Performance Tuning](../sqlpp/appendix%5F2%5Fparameters.md) and [Operational Insights Configuration REST API](../analytics-rest-config/index.md).

## [](#precompute)Precompute Repeated Work

If many queries repeat the same expensive joins, unnesting, or aggregations, compute the result once and query the result instead.

### [](#views-are-not-materialized)Views Are Not Materialized

A view stores only its definition. Every query on a view merges the view definition into the query and recomputes it. Views and tabular views make queries easier to write and let BI tools connect, but they do not store precomputed results. To speed up queries on views, index the underlying collections.

### [](#materialize-results-in-a-standalone-collection)Materialize Results in a Standalone Collection

Use `CREATE COLLECTION AS` to create a standalone collection and populate it with the results of a query in one statement. Then run `ANALYZE COLLECTION` and add indexes on the new collection.

Example

```sql
CREATE COLLECTION sampleAnalytics.Commerce.order_revenue
PRIMARY KEY (orderno: BIGINT)
AS
SELECT o.orderno, o.order_date, o.custid, SUM(i.qty * i.price) AS revenue
FROM sampleAnalytics.Commerce.orders AS o UNNEST o.items AS i
GROUP BY o.orderno, o.order_date, o.custid;

ANALYZE COLLECTION sampleAnalytics.Commerce.order_revenue;
CREATE INDEX idx_rev_date ON sampleAnalytics.Commerce.order_revenue(order_date: STRING);
```

### [](#refresh-materialized-results)Refresh Materialized Results

To keep a materialized collection current, run `UPSERT INTO … SELECT` on a schedule that matches how stale the results can be. Remove outdated objects with `DELETE`, or `TRUNCATE` the collection and reload it. Refresh the optimizer sample afterwards.

### [](#export-results-for-downstream-use)Export Results for Downstream Use

* Use `COPY TO` to write query results to object storage in Parquet, JSON, or CSV format. You can then query Parquet output efficiently as an external collection.
* Use `COPY TO KV` to write results back to a Couchbase operational bucket, so that applications can read precomputed results through key-value access.

For more information, see [Views and Tabular Views](../sqlpp/5a%5Fviews.md), [CREATE COLLECTION AS Statements](../sqlpp/5%5Fdml%5Fcreate%5Fas.md), [UPSERT INTO Statements](../sqlpp/5%5Fdml%5Fupsert.md), [Parquet](../sqlpp/5%5Fdml%5Fcopy%5Fto%5Fparquet.md), and [Write Back to Couchbase](../query/copy-to-kv.md).

## [](#configure-resources)Configure Service Resources

If a well-written, well-indexed query is still slow, or queries wait in the queue, check how the service is provisioned. Unless noted otherwise, the following are service-level configuration parameters that you set through the Configuration REST API. Changes apply to all queries.

### [](#operator-memory-budgets)Operator Memory Budgets

Sort, join, group-by, and window operators spill to disk when they exceed their memory budget. The budget applies to each operator instance in each partition. If the query timings show heavy spilling, increase the relevant budget:

| Parameter                  | Operator      | Default |
| -------------------------- | ------------- | ------- |
| compilerSortmemory         | Sort          | 32 MiB  |
| compilerJoinmemory         | Join          | 32 MiB  |
| compilerGroupmemory        | Group by      | 32 MiB  |
| compilerWindowmemory       | Window        | 32 MiB  |
| compilerExternalscanmemory | External scan | 8 KiB   |

Higher budgets increase the memory each query needs, which can reduce how many queries run at the same time.

### [](#parallelism-and-concurrency)Parallelism and Concurrency

* `compilerParallelism`: the degree of parallelism for query execution. The default, `0`, uses the storage parallelism.
* `coresMultiplier`: multiplied by the number of cores to determine the maximum number of queries that run concurrently. The default is 3.
* `compilerBatchLookup`: batches point lookups when queries use secondary indexes. Enabled by default.

### [](#memory-and-caching)Memory and Caching

* Allocate enough memory to the Operational Insights service with the service memory quota (`cbasMemoryQuota`). See [General Settings](../manage/manage-settings/general-settings.md).
* `storageBuffercacheSize`: the memory allocated to the disk buffer cache. The default is 1/4 of the JVM maximum heap.
* `cloudStorageCachePolicy`: controls how Operational Insights caches data from object storage on local disk. `selective` (default) caches data on first access and evicts cold data under disk pressure, `eager` caches all data at startup, and `lazy` caches data on first access with no eviction.
* `cloudStorageAllocationPercentage`: under the `selective` policy, the share of disk used for cached data. The rest is query workspace for operators that spill to disk. The default is `0.8` (80% of disk space).

### [](#scan-consistency)Scan Consistency

The `not_bounded` scan consistency is the fastest mode because it does not wait to obtain a timestamp vector. Use `request_plus` only when a query must see all data ingested before it started. You can set scan consistency in the Workbench Run-Time Preferences or with the `scan_consistency` parameter of the Analytics Service REST API.

### [](#scale-out-and-follow-platform-guidelines)Scale Out and Follow Platform Guidelines

* Operational Insights separates compute from storage. To add query capacity, add nodes and rebalance. Operational Insights redistributes data and indexes automatically.
* Follow the deployment guidelines: disable Transparent Huge Pages (THP), set kernel swappiness to 0 or 1, and use the XFS file system.
* Use the TSC clock source on Linux. Other clock sources, such as XEN, can use up to 25% of available CPU time.

For more information, see [Operational Insights Configuration REST API](../analytics-rest-config/index.md), [Add a Node and Rebalance](../manage/manage-nodes/add-node-and-rebalance.md), [Deployment Guidelines](../install/deploy-guidelines.md), and [System Resource Requirements](../install/sys-resource-req.md).

## [](#optimization-checklist)Optimization Checklist

Use the following checklist to match a symptom you're seeing to the technique that addresses it.

| Symptom                                        | Check                                                                     | Technique                                                                              |
| ---------------------------------------------- | ------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| docs scanned is much higher than docs returned | Does the plan show a full collection scan?                                | Add a secondary index or array index. Use the Index Advisor.                           |
| Index exists but is not used                   | Is the predicate on a prefix of the index key, with a matching data type? | Reorder composite index fields. Fix literal types. Add LEN(arr) > 0 for EVERY queries. |
| Plan has no operator-estimates                 | Do all collections in the query have samples?                             | Run ANALYZE COLLECTION.                                                                |
| Poor join order or join method                 | Are the CBO estimates close to actual counts?                             | Refresh or enlarge samples. Use productivity, hash-bcast, or indexnl hints.            |
| Slow queries on external data                  | Does the path or WHERE clause limit which files the engine reads?         | Use a narrower path, dynamic prefixes, include or exclude, and columnar formats.       |
| The same heavy aggregation runs repeatedly     | Does it query a view?                                                     | Materialize the results with CREATE COLLECTION AS and refresh on a schedule.           |
| Large sorts are slow                           | Is the final merge on one node the bottleneck?                            | compiler.sort.parallel is true by default. Confirm it has not been set to false.       |
| Operators spill to disk                        | Do per-operator timings show sort, join, or group-by as the slowest step? | Increase operator memory budgets.                                                      |
| High waiting-in-queue time                     | Is the cluster at its concurrency limit?                                  | Tune coresMultiplier. Add nodes and rebalance.                                         |

## [](#see-also)See Also

* [Indexes](../sqlpp/7%5Fusing%5Findex.md)
* [Index Advisor](../sqlpp/5c-index-advisor.md)
* [Cost-Based Optimizer](../sqlpp/5b%5Fcbo.md)
* [Performance Tuning](../sqlpp/appendix%5F2%5Fparameters.md)
* [External Storage Data Organization](../sources/dynamic-prefixes.md)
* [View Query Metrics or Plan](../query/metrics-plan.md)
* [Operational Insights Configuration REST API](../analytics-rest-config/index.md)