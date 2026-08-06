---
title: Performance Tuning
description: This topic describes options for Enterprise Analytics query performance tuning.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/sqlpp/pages/appendix_2_parameters.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:enterprise-analytics:sqlpp:appendix_2_parameters.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/sqlpp/appendix_2_parameters.html)

# Performance Tuning

> This topic describes options for Enterprise Analytics query performance tuning. 

You can use a `SET` statement to override some default system parameters for a specific request.

##### SetStmnt

![SetStmnt](_images/SetStmnt.png) 

Parameter identifiers are often compound names that contain `.` characters. As a result, you must delimit these identifiers using backticks (``` `` ```) in your queries. See the examples that follow.

Changing configuration parameters does not affect the correctness of the query results. Changes can impact query performance characteristics such as response time and throughput.

## [](#Parallel%5Fsort%5Fparameter)Parallel Sort Parameter

The following parameter enables you to activate or deactivate full parallel sort for order-by operations.

When full parallel sort is inactive (`false`), each existing data partition is sorted (in parallel), and then all data partitions are finally merged on a single node.

When full parallel sort is active (`true`), the data is first sampled, and then repartitioned so that each partition contains data that is greater than the previous partition. The data in each partition is then sorted (in parallel) to produce the final result, and there is no need to perform a final merge of the sorted partitions on a single node.

**compiler.sort.parallel**: A Boolean specifying whether full parallel sort is active (`true`) or inactive (`false`). The default value is `false`.

Example

```SQL++
SET `compiler.sort.parallel` "true";

SELECT VALUE o
FROM orders AS o
ORDER BY ARRAY_LENGTH(o.o_items) DESC;
```

## [](#ArrayIndexFlag)Array Index Parameter

The following parameter enables you to specify whether the query optimizer should use any applicable array indexes to speed up scanning of data collections.

When this setting is `true`, the query optimizer attempts to use array indexes if they're available. You can set this parameter to `false` to make the query optimizer skip array indexes.

**compiler.arrayindex**: A Boolean specifying whether array indexes will be considered as an access method for applicable queries. The default value is `true`.

Example

```SQL++
SET `compiler.arrayindex` "false";

SELECT o.o_orderkey
FROM orders o
WHERE SOME i IN o.o_items
SATISFIES i.price = 19.91;
```

## [](#CBO%5Fparameters)Cost-Based Optimizer Parameters

The following parameters enable you to specify the behavior of the cost-based optimizer.

* **compiler.queryplanshape**: A string specifying the shape of the query plan produced by the query optimizer for multi-way hash join queries.  
Three settings are available for this parameter: `zigzag`, `leftdeep`, and `rightdeep`.

  * `zigzag` — The smaller input is chosen as the build side of the hash join, and the larger input is chosen as the probe side. This is the default value, and provides a balance between speed and memory usage.
  * `leftdeep` — After the first join, previous join results are always chosen as the build side of the hash join, and base collections are always chosen as the probe side. This saves memory, but can be potentially slower.
  * `rightdeep` — After the first join, base collections are always chosen as the build side of the hash join, and previous join results are always chosen as the probe side. This can be potentially faster, but uses more memory.
* **compiler.forcejoinorder**: A Boolean specifying whether joins should be performed in the order in which they are specified in the from clause of the query. The default value is `false`, meaning the cost-based optimizer chooses the optimal join order.
* **compiler.cbo**: A Boolean specifying whether the cost-based optimizer should be activated or not. Setting this to `false` turns off the cost-based optimizer entirely. The default value is `true`.

##### Example

The following example explicitly specifies the `zigzag` plan shape for a multi-join query, even though this is the default.

```SQL++
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

This produces a query plan which can be represented as follows. Notice that for each hash join, the left side is the build side and the right side is the probe side.

![Representation of multi-join query plan](_images/plan-zigzag.svg) 

Notice that the bottom three hash joins have base collections as their build side, but the top two hash joins have join results as their build side.

##### Example

The following example specifies the left deep plan shape.

```SQL++
SET `compiler.queryplanshape` "leftdeep";
```

A left deep plan for the query above can be represented as follows. Notice that for each hash join, the left side is the build side and the right side is the probe side.

![Representation of multi-join query plan](_images/plan-leftdeep.svg) 

##### Example

The following example specifies the right deep plan shape.

```SQL++
SET `compiler.queryplanshape` "rightdeep";
```

A right deep plan for the query above can be represented as follows. Notice that for each hash join, the left side is the build side and the right side is the probe side.

![Representation of multi-join query plan](_images/plan-rightdeep.svg) 

##### Example

The following example forces the cost-based optimizer to use the order of joins specified in the from clause of the query.

```SQL++
SET `compiler.forcejoinorder` "true";
```

##### Example

The following example turns the cost-based optimizer off.

```SQL++
SET `compiler.cbo` "false";
```

##### Example

The following example turns the cost-based optimizer on again.

```SQL++
SET `compiler.cbo` "true";
```

## [](#CBO%5Fhints)Cost-Based Optimizer Hints

You can supply hints to the cost-based optimizer using a hint comment. These enable you to specify the behavior of the cost-based optimizer for individual queries.

> [!TIP]
> Generally speaking, you should rely on the optimizer to generate the optimal query plan. Optimizer hints may be useful to nudge the query optimizer in specific—hopefully rare—situations where it's not able to come up with the optimal plan.

### [](#productivity%5Fhint)Productivity Hint

The `productivity` hint can help the cost-based optimizer get a better join cardinality estimate, especially for foreign key to foreign key joins.

This hint is used within the join predicate. If the join is on a composite key, then this hint needs to be provided just once on any of the join predicates.

The hint requires two parameters:

* **name**: A base collection or alias.
* **productivity**: How many matching objects are expected from a join with the specified collection or alias.

##### Example

In this example, the hint specifies that for each object of `s` we expect to get 600 matching objects resulting from joining `s` with `c`, that is, each `s` will produce 600 `c` matches.

```SQL++
SELECT c.*
FROM customers c, supplier s
WHERE c.c_nationkey /*+ productivity s 600.0 */ = s.s_nationkey;
```

### [](#hashjoin%5Fhint)Hash Join Hint

The `hashjoin` hint can be used in a join predicate to force a hash join.

The hint also specifies which side of the hash join the identified collection or alias should be on: the `build` side or the `probe` side.

The hint requires one parameter:

**name**: A base collection or alias. The base collection or alias may be from a previous join result.

If the parameter is valid, the cost-based optimizer only considers using a hash join plan with the specified collection.

If the parameter is invalid or not specified, the cost-based optimizer ignores the hint, generates a warning, and then tries all possible join methods.

##### Example

This example specifies that the `orders` collection (`o`) should be on the build side of the hash join between `o` and `cn`.

```SQL++
SELECT count(*)
FROM orders o
JOIN (SELECT *
      FROM customers c, nations n
      WHERE c.c_nationkey = n.n_nationkey) AS cn
ON cn.c_custkey /*+ hashjoin build (o) */ = o.c_custkey;
```

##### Example

This example specifies that the subquery result containing the `customers` collection (`c`) should be on the build side of the hash join between `o` and `cn`. This is equivalent to specifying that the `orders` collection (`o`) should be on the probe side.

```SQL++
SELECT count(*)
FROM orders o
JOIN (SELECT *
      FROM customers c, nations n
      WHERE c.c_nationkey = n.n_nationkey) AS cn
ON cn.c_custkey /*+ hashjoin build (c) */ = o.o_custkey;
```

##### Example

This example specifies that the subquery result containing the `nations` collection (`n`) should be on the build side of the hash join between `o` and `cn`. This is equivalent to specifying that the `orders` collection (`o`) should be on the probe side.

```SQL++
SELECT count(*)
FROM orders o
JOIN (SELECT *
      FROM customers c, nations n
      WHERE c.c_nationkey = n.n_nationkey) AS cn
  ON cn.c_custkey /*+ hashjoin build (n) */ = o.o_custkey;
```

##### Example

This example specifies that the `orders` collection (`o`) should be on the probe side of the hash join between `o` and `cn`.

```SQL++
SELECT count(*)
FROM orders o
JOIN (SELECT *
      FROM customers c, nations n
      WHERE c.c_nationkey = n.n_nationkey) AS cn
  ON cn.c_custkey /*+ hashjoin probe (o) */ = o.o_custkey;
```

##### Example

This example specifies that the subquery result containing the `customers` collection (`c`) should be on the probe side of the hash join between `o` and `cn`. This is equivalent to specifying that the `orders` collection (`o`) should be on the build side.

```SQL++
SELECT count(*)
FROM orders o
JOIN (SELECT *
      FROM customers c, nations n
      WHERE c.c_nationkey = n.n_nationkey) AS cn
ON cn.c_custkey /*+ hashjoin probe (c) */ = o.o_custkey;
```

##### Example

This example specifies that the subquery result containing the `nations` collection (`n`) should be on the probe side. This is equivalent to specifying that the `orders` collection (`o`) should be on the build side.

```SQL++
SELECT count(*)
FROM orders o
JOIN (SELECT *
      FROM customers c, nations n
      WHERE c.c_nationkey = n.n_nationkey) AS cn
  ON cn.c_custkey /*+ hashjoin build (cn) */ = o.o_custkey;
```

##### Example

This example generates a warning because `cn` is not a base collection. The hint is ignored, and all possible join orders and join methods are considered.

```SQL++
SELECT count(*)
FROM orders o
JOIN (SELECT *
      FROM customers c, nations n
      WHERE c.c_nationkey = n.n_nationkey) AS cn
  ON cn.c_custkey /*+ hashjoin build (cn) */ = o.o_custkey;
```

### [](#hash%5Fbcast%5Fhint)Hash Broadcast Join Hint

For regular hash joins, Enterprise Analytics uses a partitioned-parallel hash join strategy to parallelize the execution of an equi-join. In this approach, both sides of the join are repartitioned (if necessary) on a hash of the join key; potentially matching data items thus arrive at the same partition to be joined locally.

This strategy is robust, but not always the fastest when one of the join sides is of low cardinality and the other is of high cardinality (since it scans and potentially moves the data from both sides). This special case can be better handled by broadcasting (replicating) the smaller side to all data partitions of the larger side and not moving the data from the other (larger) side. Enterprise Analytics provides the `hash-bcast` join hint to enable this strategy. This hint forces one side of the join to be replicated while the other retains its original partitioning and is not repartitioned.

The hint can have one optional parameter:

**name**: A base collection or alias which should be broadcast for the join. The base collection or alias may be from a previous join result.

If the parameter is valid, the cost-based optimizer only tries the broadcast plan with the specified collection.

If the parameter is not specified, the cost-based optimizer tries two broadcast plans, broadcast left and broadcast right.

If the parameter is invalid, the cost-based optimizer ignores the hint, generates a warning, and then tries all possible join methods.

##### Example

This example specifies that the query should use a broadcast plan, but does not specify which side should be on the broadcast side.

```SQL++
SELECT count(*)
FROM orders o
JOIN (SELECT *
      FROM customers c, nations n
      WHERE c.c_nationkey = n.n_nationkey) AS cn
ON cn.c_custkey /*+ hash-bcast */ = o.o_custkey;
```

##### Example

This example specifies that the subquery result containing the `customers` collection (`c`) should be on the broadcast side.

```SQL++
SELECT count(*)
FROM orders o
JOIN (SELECT c.*
      FROM customers c, nations n
      WHERE c.nationkey = n.nationkey) AS cn
ON cn.custid /*+ hash-bcast (c) */ = o.custid;
```

##### Example

This example specifies that the subquery containing the `nations` collection (`n`) should be on the broadcast side.

```SQL++
SELECT count(*)
FROM orders o
JOIN (SELECT *
      FROM customers c, nations n
      WHERE c.c_nationkey = n.n_nationkey) AS cn
ON cn.c_custkey /*+ hash-bcast (n) */ = o.o_custkey;
```

##### Example

This example specifies that the `orders` collection (`o`) should be on the broadcast side.

```SQL++
SELECT count(*)
FROM orders o
JOIN (SELECT *
      FROM customers c, nations n
      WHERE c.c_nationkey = n.n_nationkey) AS cn
ON cn.c_custkey /*+ hash-bcast (o) */ = o.o_custkey;
```

##### Example

This example generates a warning because `cn` is not a base collection. The hint is ignored, and all possible join orders and join methods are considered.

```SQL++
SELECT count(*)
FROM orders o
JOIN (SELECT *
      FROM customers c, nations n
      WHERE c.c_nationkey = n.n_nationkey) AS cn
ON cn.c_custkey /*+ hash-bcast (cn) */ = o.o_custkey;
```

### [](#index-nested-loops-join-hint)Index Nested Loops Join Hint

In certain cases, when one of the join sides (outer) is of low cardinality and the other side (inner) is of high cardinality and there is an index on the joining column of the high cardinality (inner) side, an index nested loops join may be the most efficient join strategy.

Enterprise Analytics provides the `indexnl` join hint to enable this strategy.

Suppose that there is an index on `customers` as follows:

```SQL++
  CREATE index idx_cust ON customers(c_nationkey);
```

Then an index nested loops join will be used for the following query.

```SQL++
SELECT *
FROM nations n, customers c
WHERE c.c_nationkey /*+ indexnl */ = n.n_nationkey
```