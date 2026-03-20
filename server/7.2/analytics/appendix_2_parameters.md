---
title: "Appendix 2: Performance Tuning"
description: A description of Couchbase Analytics query performance tuning.
editUrl: https://github.com/couchbase/docs-analytics/edit/release/7.2/modules/analytics/pages/appendix_2_parameters.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:analytics:appendix_2_parameters.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/analytics/appendix_2_parameters.html)

# Appendix 2: Performance Tuning

The `SET` statement can be used to override some cluster-wide configuration parameters for a specific request:

##### [](#setstmnt)SetStmnt

![SetStmnt](_images/diagrams/SetStmnt.png) 

As parameter identifiers are qualified names (containing a '.') they have to be escaped using backticks (\`\`). Note that changing query parameters will not affect query correctness but only impact performance characteristics, such as response time and throughput.

## [](#Parallelism%5Fparameter)Parallelism Parameter

The system can execute each request using multiple cores on multiple machines (a.k.a., partitioned parallelism) in a cluster. A user can manually specify the maximum execution parallelism for a request to scale it up and down using the following parameter:

* **compiler.parallelism**: the maximum number of CPU cores can be used to process a query. There are three cases of the value _p_ for compiler.parallelism:

  * _p_ < 0 or _p_ \> the total number of cores in a cluster: the system will use all available cores in the cluster;
  * _p_ \= 0 (the default): the system will use the storage parallelism (the number of partitions of stored datasets) as the maximum parallelism for query processing;
  * all other cases: the system will use the user-specified number as the maximum number of CPU cores to use for executing the query.

Example

SET `compiler.parallelism` "16";

SELECT c.name AS cname, o.orderno AS orderno
FROM customers c JOIN orders o ON c.custid = o.custid;

## [](#Memory%5Fparameters)Memory Parameters

In the system, each blocking runtime operator such as join, group-by and order-by works within a fixed memory budget, and can gracefully spill to disks if the memory budget is smaller than the amount of data they have to hold. A user can manually configure the memory budget of those operators within a query. The supported configurable memory parameters are:

* **compiler.groupmemory**: the memory budget that each parallel group-by operator instance can use; 32MB is the default budget.
* **compiler.sortmemory**: the memory budget that each parallel sort operator instance can use; 32MB is the default budget.
* **compiler.joinmemory**: the memory budget that each parallel hash join operator instance can use; 32MB is the default budget.
* **compiler.windowmemory**: the memory budget that each parallel window aggregate operator instance can use; 32MB is the default budget.

For each memory budget value, you can use a 64-bit integer value with a 1024-based binary unit suffix (for example, B, KB, MB, GB). If there is no user-provided suffix, "B" is the default suffix. See the following examples.

Example

SET `compiler.groupmemory` "64MB";

SELECT c.custid, COUNT(*)
FROM customers c
GROUP BY c.custid;

Example

SET `compiler.sortmemory` "67108864";

SELECT VALUE o
FROM orders AS o
ORDER BY ARRAY_LENGTH(o.items) DESC;

Example

SET `compiler.joinmemory` "132000KB";

SELECT c.name AS cname, o.ordeno AS orderno
FROM customers c JOIN orders o ON c.custid = o.custid;

## [](#Parallel%5Fsort%5Fparameter)Parallel Sort Parameter

The following parameter enables you to activate or deactivate full parallel sort for order-by operations.

When full parallel sort is inactive (`false`), each existing data partition is sorted (in parallel), and then all data partitions are merged into a single node.

When full parallel sort is active (`true`), the data is first sampled, and then repartitioned so that each partition contains data that is greater than the previous partition. The data in each partition is then sorted (in parallel), but the sorted partitions are not merged into a single node.

* **compiler.sort.parallel**: A boolean specifying whether full parallel sort is active (`true`) or inactive (`false`). The default value is `false`.

Example

SET `compiler.sort.parallel` "true";

SELECT VALUE o
FROM orders AS o
ORDER BY ARRAY_LENGTH(o.items) DESC;

## [](#ArrayIndexFlag)Array Index Parameter

The following parameter enables you to choose whether the query optimizer should replace applicable data scans with array index lookups.

When this setting is `true`, the query optimizer attempts to utilize array indexes if they are available. You can set this property to `false` to make query optimizer skip array indexes.

* **compiler.arrayindex**: A boolean specifying whether array indexes will be considered as an access method for applicable queries. The default value is `true`.

Example

```sqlpp
SET `compiler.arrayindex` "false";

SELECT o.orderno
FROM orders o
WHERE SOME i IN o.items
SATISFIES i.price = 19.91;
```

## [](#CBO%5Fparameters)Cost-Based Optimizer Parameters

The following parameters enable you to specify the behavior of the cost-based optimizer.

* **compiler.queryplanshape**: A string specifying the shape of the query plan produced by the query compiler for multi-way hash join queries. Three settings are available for this parameter: `zigzag`, `leftdeep`, and `rightdeep`.

  * `zigzag` — The smaller input is the build side of the hash join, and the larger input is the probe side. This is the default value, and provides a balance between speed and memory usage.
  * `leftdeep` — After the first join, previous join results are always on the build side of the hash join, and base collections are always on the probe side. This saves memory, but is potentially slower.
  * `rightdeep` — After the first join, base collections are always on the build side of the hash join, and previous join results are always on the probe side. This is potentially quicker, but uses more memory.
* **compiler.forcejoinorder**: A boolean specifying whether joins should be performed in the order in which they are specified in the query. The default value is `false`, meaning the cost-based optimizer chooses the optimal join order.
* **compiler.cbo**: A boolean specifying whether the cost-based optimizer should be activated or not. Setting this to `false` turns off the cost-based optimizer entirely. The default value is `true`.

##### Example

The following example explicitly specifies the zigzag plan shape for a multi-join query, even though this is the default.

```sqlpp
SET `compiler.queryplanshape` "zigzag";

SELECT nation, o_year, sum(amount) AS sum_profit
FROM (SELECT n.n_name AS nation,
      DATE_PART_STR(o.o_orderdate, 'year'),
      l.l_extendedprice * (1 - l.l_discount) -
      ps.ps_supplycost * l.l_quantity as amount
      FROM part p, supplier s, lineitem l,
           partsupp ps, orders o, nation n
      WHERE s.s_suppkey = l.l_suppkey
        AND ps.ps_suppkey = l.l_suppkey
        AND s.s_suppkey = ps.ps_suppkey
        AND ps.ps_partkey = l.l_partkey
        AND p.p_partkey = l.l_partkey
        AND p.p_partkey = ps.ps_partkey
        AND o.o_orderkey = l.l_orderkey
        AND s.s_nationkey = n.n_nationkey
        AND p.p_name LIKE '%green%') AS profit
GROUP BY nation, o_year
ORDER BY nation, o_year DESC;
```

This produces a query plan which can be represented as follows. For each hash join, the left side is the build side and the right side is the probe side.

![plan-zigzag](_images/plan-zigzag-f59cbfe67a29fc8de08b6f913f05fa4b12d87fb1.svg) 

Note that the bottom three hash joins have base collections as their build side, but the top two hash joins have join results as their build side.

##### Example

The following example specifies the left deep plan shape.

```sqlpp
SET `compiler.queryplanshape` "leftdeep";
```

A left deep plan for the query above can be represented as follows. For each hash join, the left side is the build side and the right side is the probe side.

![plan-leftdeep](_images/plan-leftdeep-6821a9a27cd8e2cefb9862e191524835631dd55f.svg) 

##### Example

The following example specifies the right deep plan shape.

```sqlpp
SET `compiler.queryplanshape` "rightdeep";
```

A right deep plan for the query above can be represented as follows. For each hash join, the left side is the build side and the right side is the probe side.

![plan-rightdeep](_images/plan-rightdeep-4672f9f743b8f94bbd04e7ab0f15da0d4d45e8b9.svg) 

##### Example

The following example forces the cost-based optimizer to use the order of joins specified in the query.

```sqlpp
SET `compiler.forcejoinorder` "true";
```

##### Example

The following example turns the cost-based optimizer off.

```sqlpp
SET `compiler.cbo` "false";
```

##### Example

The following example turns the cost-based optimizer on again.

```sqlpp
SET `compiler.cbo` "true";
```

## [](#CBO%5Fhints)Cost-Based Optimizer Hints

You can supply hints to the cost-based optimizer using a hint comment. These enable you to specify the behavior of the cost-based optimizer for individual queries.

> [!TIP]
> Generally speaking, you should rely on the optimizer to generate the query plan. Optimizer hints may be useful in specific situations where the optimizer is not able to come up with the preferred plan.

### [](#productivity%5Fhint)Productivity Hint

The `productivity` hint can help the cost-based optimizer get a better join cardinality estimate for foreign key to foreign key joins.

This hint is used within the join predicate. If the join is on a composite key, then this hint needs to be provided just once on any of the join’s predicates.

The hint requires two parameters:

* **name**: A collection or alias.
* **productivity**: How many matching objects are expected from a join with the specified collection.

##### Example

In this example, the hint specifies that for each object of `n` we expect to get 600 matching objects resulting from joining `n` with `c`, that is, each `n` will produce 600 `c` matches.

```sqlpp
SELECT c.*
FROM customers c, nations n
WHERE c.nationkey /*+ productivity n 600.0 */ = n.nationkey;
```

### [](#hashjoin%5Fhint)Hash Join Hint

The `hashjoin` hint can be used in a join predicate to force a hash join.

The hint requires you to specify which side of the hash join the identified collection or alias should be on: the `build` side or the `probe` side.

The hint requires one parameter:

* **name**: A base collection or alias. The base collection or alias may be from a previous join result.

If the parameter is valid, the cost-based optimizer only considers using a hash join plan with the specified collection.

If the parameter is invalid or not specified, the cost-based optimizer ignores the hint, generates a warning, and then tries all possible join methods.

##### Example

This example specifies that the `orders` collection (`o`) should be on the build side.

```sqlpp
SELECT count(*)
FROM orders o
JOIN (SELECT c.*
      FROM customers c, nations n
      WHERE c.nationkey = n.nationkey) AS cn
ON cn.custid /*+ hashjoin build (o) */ = o.custid;
```

##### Example

This example specifies that the subquery containing the `customers` collection (`c`) should be on the build side. This is equivalent to specifying that the `orders` collection (`o`) should be on the probe side.

```sqlpp
SELECT count(*)
FROM orders o
JOIN (SELECT c.*
      FROM customers c, nations n
      WHERE c.nationkey = n.nationkey) AS cn
ON cn.custid /*+ hashjoin build (c) */ = o.custid;
```

##### Example

This example specifies that the subquery containing the `nations` collection (`n`) should be on the build side. This is equivalent to specifying that the `orders` collection (`o`) should be on the probe side.

```sqlpp
SELECT count(*)
FROM orders o
JOIN (SELECT c.*
      FROM customers c, nations n
      WHERE c.nationkey = n.nationkey) AS cn
  ON cn.custid /*+ hashjoin build (n) */ = o.custid;
```

##### Example

This example specifies that the `orders` collection (`o`) should be on the probe side.

```sqlpp
SELECT count(*)
FROM orders o
JOIN (SELECT c.*
      FROM customers c, nations n
      WHERE c.nationkey = n.nationkey) AS cn
  ON cn.custid /*+ hashjoin probe (o) */ = o.custid;
```

##### Example

This example specifies that the subquery containing the `customers` collection (`c`) should be on the probe side. This is equivalent to specifying that the `orders` collection (`o`) should be on the build side.

```sqlpp
SELECT count(*)
FROM orders o
JOIN (SELECT c.*
      FROM customers c, nations n
      WHERE c.nationkey = n.nationkey) AS cn
ON cn.custid /*+ hashjoin probe (c) */ = o.custid;
```

##### Example

This example specifies that the subquery containing the `nations` collection (`n`) should be on the probe side. This is equivalent to specifying that the `orders` collection (`o`) should be on the build side.

```sqlpp
SELECT count(*)
FROM orders o
JOIN (SELECT c.*
      FROM customers c, nations n
      WHERE c.nationkey = n.nationkey) AS cn
ON cn.custid /*+ hashjoin probe (n) */ = o.custid;
```

##### Example

This example generates a warning because `cn` is not a base collection. The hint is ignored, and all possible join orders and join methods are considered.

```sqlpp
SELECT count(*)
FROM orders o
JOIN (SELECT c.*
      FROM customers c, nations n
      WHERE c.nationkey = n.nationkey) AS cn
  ON cn.custid /*+ hashjoin build (cn) */ = o.custid;
```

### [](#hash%5Fbcast%5Fhint)Hash Broadcast Hint

By default, Analytics uses a partitioned-parallel hash join strategy to parallelize the execution of an equi-join. In this approach both sides of the join are repartitioned (if necessary) on a hash of the join key; potentially matching data items thus arrive at the same partition to be joined locally. This strategy is robust, but not always the fastest when one of the join sides is low cardinality and the other is high cardinality (since it scans and potentially moves the data from both sides). This special case can be better handled by broadcasting (replicating) the smaller side to all data partitions of the larger side and not moving the data from the other (larger) side. Analytics provides the `hash-bcast` join hint to enable this strategy. This hint forces one side of the join to be replicated while the other retains its original partitioning.

The hint may have one optional parameter:

* **name**: A base collection or alias which should be broadcast for the join. The base collection or alias may be from a previous join result.

If the parameter is valid, the cost-based optimizer only tries the broadcast plan with the specified collection.

If the parameter is not specified, the cost-based optimizer tries two broadcast plans, broadcast left and broadcast right.

If the parameter is invalid, the cost-based optimizer ignores the hint, generates a warning, and then tries all possible join methods.

##### Example

This example specifies that the query should use a broadcast plan, but does not specify which side should be on the broadcast side.

```sqlpp
SELECT count(*)
FROM orders o
JOIN (SELECT c.*
      FROM customers c, nations n
      WHERE c.nationkey = n.nationkey) AS cn
ON cn.custid /*+ hash-bcast */ = o.custid;
```

##### Example

This example specifies that the subquery containing the `customers` collection (`c`) should be on the broadcast side.

```sqlpp
SELECT count(*)
FROM orders o
JOIN (SELECT c.*
      FROM customers c, nations n
      WHERE c.nationkey = n.nationkey) AS cn
ON cn.custid /*+ hash-bcast (c) */ = o.custid;
```

##### Example

This example specifies that the subquery containing the `nations` collection (`n`) should be on the broadcast side.

```sqlpp
SELECT count(*)
FROM orders o
JOIN (SELECT c.*
      FROM customers c, nations n
      WHERE c.nationkey = n.nationkey) AS cn
ON cn.custid /*+ hash-bcast (n) */ = o.custid;
```

##### Example

This example specifies that the `orders` collection (`o`) should be on the broadcast side.

```sqlpp
SELECT count(*)
FROM orders o
JOIN (SELECT c.*
      FROM customers c, nations n
      WHERE c.nationkey = n.nationkey) AS cn
ON cn.custid /*+ hash-bcast (o) */ = o.custid;
```

##### Example

This example generates a warning because `cn` is not a base collection. The hint is ignored, and all possible join orders and join methods are considered.

```sqlpp
SELECT count(*)
FROM orders o
JOIN (SELECT c.*
      FROM customers c, nations n
      WHERE c.nationkey = n.nationkey) AS cn
ON cn.custid /*+ hash-bcast (cn) */ = o.custid;
```