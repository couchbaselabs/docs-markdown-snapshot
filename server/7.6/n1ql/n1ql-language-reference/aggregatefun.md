---
title: Aggregate Functions
description: Aggregate functions take multiple values from documents, perform
  calculations, and return a single value as the result.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/n1ql/pages/n1ql-language-reference/aggregatefun.adoc
  xref: xref:7.6@server:n1ql:n1ql-language-reference/aggregatefun.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/n1ql/n1ql-language-reference/aggregatefun.html)

# Aggregate Functions

Aggregate functions take multiple values from documents, perform calculations, and return a single value as the result. The function names are case insensitive.

You can only use aggregate functions in `SELECT`, `LETTING`, `HAVING`, and `ORDER BY` clauses. When using an aggregate function in a query, the query operates as an aggregate query.

In Couchbase Server Enterprise Edition, you can use aggregate functions as [window functions](windowfun.md) by specifying a window definition using the [OVER Clause](#over-clause).

In Couchbase Server 7.0 and later, window functions (and aggregate functions used as window functions) may specify their own inline window definitions, or they may refer to a named window defined by the WINDOW clause elsewhere in the query. By defining a named window with the WINDOW clause, you can reuse the window definition across several functions in the query, potentially making the query easier to write and maintain.

## [](#aggregate-syntax)Syntax

This section describes the generic syntax of aggregate functions. For details of individual aggregate functions, see the sections that follow.

```ebnf
aggregate-function ::= aggregate-function-name '(' ( aggregate-quantifier? expr |
                       ( path '.' )? '*' ) ')' filter-clause? over-clause?
```

![Syntax diagram](../_images/n1ql-language-reference/aggregate-function.png) 

| aggregate-quantifier | [Aggregate Quantifier](#aggregate-quantifier) |
| -------------------- | --------------------------------------------- |
| filter-clause        | [FILTER Clause](#filter-clause)               |
| over-clause          | [OVER Clause](#over-clause)                   |

### [](#arguments)Arguments

Aggregate functions take a single [expression](index.md#N1QL%5FExpressions) as an argument, which is used to compute the aggregate function. The `COUNT` function can instead take a wildcard (\*) or a [path](index.md#nested-path-exp) with a wildcard (path.\*) as its argument.

### [](#aggregate-quantifier)Aggregate Quantifier

```ebnf
aggregate-quantifier ::= 'ALL' | 'DISTINCT'
```

![Syntax diagram](../_images/n1ql-language-reference/aggregate-quantifier.png) 

An aggregate quantifier determines whether the function aggregates all values in a group or only distinct values. You can use the quantifiers only with aggregate functions.

`ALL`

Includes all values in the computation.

`DISTINCT`

Includes only distinct values in the computation.

These quantifiers are optional and the default value is `ALL`.

### [](#filter-clause)FILTER Clause

```ebnf
filter-clause ::= 'FILTER' '(' 'WHERE' cond ')'
```

![Syntax diagram](../_images/n1ql-language-reference/filter-clause.png) 

The FILTER clause enables you to specify which values are included in the aggregate. This clause is available for aggregate functions, and aggregate functions used as window functions. (It is not permitted for dedicated window functions.)

The FILTER clause is useful when a query contains several aggregate functions, each of which requires a different condition.

cond

\[Required\] Conditional expression. Values for which the condition resolves to TRUE are included in the aggregation.

The conditional expression is subject to the same rules as the conditional expression in the query WHERE clause, and the same rules as aggregation operands. It may not contain a subquery, a window function, or an outer reference.

> [!NOTE]
> If the query block contains an aggregate function which uses the FILTER clause, the aggregation is not pushed down to the indexer. Refer to [Grouping and Aggregate Pushdown](groupby-aggregate-performance.md#filter-clause) for more details.

### [](#over-clause)OVER Clause

[ENTERPRISE EDITION](https://www.couchbase.com/products/editions)

```ebnf
over-clause ::= 'OVER' ( '(' window-definition ')' | window-ref )
```

![Syntax diagram](../_images/n1ql-language-reference/over-clause.png) 

The OVER clause introduces the window specification for the function. There are two ways of specifying the window.

* An _inline window definition_ specifies the window directly within the function call. It is delimited by parentheses `()` and has exactly the same syntax as the window definition in a WINDOW clause. For further details, refer to [Window Definition](window.md#window-definition).
* A _window reference_ is an [identifier](identifiers.md) which refers to a named window. The named window must be defined by a WINDOW clause in the same query block as the function call. For further details, refer to [WINDOW Clause](window.md).

### [](#defaults)Default Values

If there is no input row for the group, `COUNT` functions return `0`. All other aggregate functions return NULL.

## [](#array%5Fagg)ARRAY\_AGG( \[ ALL | DISTINCT \] `expression`)

### [](#description)Description

Returns an array of non-MISSING values from an expression.

You can use the `ALL` or `DISTINCT` quantifier to specify which values to include in the calculation. For more information, see [Aggregate Quantifier](#aggregate-quantifier).

The function ignores `MISSING` values, but includes `NULL` values.

### [](#arguments-2)Arguments

See [Syntax](#aggregate-syntax).

### [](#return-value)Return Value

The function returns 1 of the following:

* An array of non-MISSING values.
* `NULL` if all values are `MISSING`.

### [](#examples)Examples

List all values into an array

Query

```sqlpp
SELECT ARRAY_AGG(input) AS agg_all
FROM [1, 2, 2, 3, "abc", MISSING, NULL]
AS input;
```

Results

```json
[
  {
    "agg_all": [
      null,
      1,
      2,
      2,
      3,
      "abc"
    ]
  }
]
```

List distinct values into an array

Query

```sqlpp
SELECT ARRAY_AGG(DISTINCT input) AS agg_distinct
FROM [1, 2, 2, 3, "abc", MISSING, NULL]
AS input;
```

Results

```json
[
  {
    "agg_distinct": [
      null,
      1,
      2,
      3,
      "abc"
    ]
  }
]
```

## [](#avg)AVG( \[ ALL | DISTINCT \] `expression`)

This function has a synonym [MEAN()](#mean).

### [](#description-2)Description

Returns the arithmetic mean (average) of all numeric values in an expression.

You can use the `ALL` or `DISTINCT` quantifier to specify which values to include in the calculation. For more information, see [Aggregate Quantifier](#aggregate-quantifier).

#### [](#arguments-3)Arguments

See [Syntax](#aggregate-syntax).

### [](#return-value-2)Return Value

The function returns 1 of the following:

* A number that represents the mean.
* `NULL` if all values are non-numeric, `MISSING`, or `NULL`.

### [](#examples-2)Examples

Find the average of all numbers

Query

```sqlpp
SELECT AVG(input) AS avg_all
FROM [1, 1, 2, 2, 3, MISSING, NULL, "abc"]
AS input;
```

Results

```json
[
  {
    "avg_all": 1.8
  }
]
```

Find the average of distinct numbers

Query

```sqlpp
SELECT AVG(DISTINCT input) AS avg_distinct
FROM [1, 1, 2, 2, 3, MISSING, NULL, "abc"]
AS input;
```

Results

```sqlpp
[
  {
    "avg_distinct": 2
  }
]
```

In this example, the average is (1 + 2 + 3) / 3 = 2.

## [](#count%5Fall)COUNT(`*`)

### [](#description-3)Description

Returns the total count of all rows in an aggregated group. \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]

The `*` wildcard indicates that the function should count all rows, including those with `NULL` and `MISSING` values.

> [!TIP]
> To get the count of only non-NULL and non-MISSING values in a group, use [COUNT(expression)](#count).

### [](#arguments-4)Arguments

This function does not take any arguments.

### [](#return-value-3)Return Value

The function returns 1 of the following:

* A number that represents the count of all rows.
* `0` if the group is empty.

### [](#example)Example

Find the count of all rows

Query

```sqlpp
SELECT COUNT(*) AS count_all_rows
FROM [1, 1, 2, 2, 3, MISSING, NULL, "abc"]
AS input;
```

Results

```json
[
  {
    "count_all_rows": 8
  }
]
```

## [](#count)COUNT( \[ ALL | DISTINCT \] `expression`)

### [](#description-4)Description

Returns the count of all non-NULL and non-MISSING values in an expression. \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]

You can use the `ALL` or `DISTINCT` quantifier to specify which values to include in the calculation. For more information, see [Aggregate Quantifier](#aggregate-quantifier).

> [!TIP]
> To get the count of all rows, including those with `NULL` and `MISSING` values, use [COUNT(\*)](#count%5Fall).

### [](#return-value-4)Return Value

The function returns 1 of the following:

* A number that represents the count.
* `0` if all values are `MISSING` or `NULL`.

### [](#examples-3)Examples

Find the count of all values

Query

```sqlpp
SELECT COUNT(input) AS count_all
FROM [1, 1, 2, 2, 3, MISSING, NULL, "abc"]
AS input;
```

Results

```json
[
  {
    "count_all": 6
  }
]
```

Find the count of distinct values

Query

```sqlpp
SELECT COUNT(DISTINCT input) AS count_distinct
FROM [1, 1, 2, 2, 3, MISSING, NULL, "abc"]
AS input;
```

Results

```json
[
  {
    "count_distinct": 4
  }
]
```

## [](#countn)COUNTN( \[ ALL | DISTINCT \] `expression` )

### [](#description-5)Description

Returns the count of numeric values in an expression. \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]

You can use the `ALL` or `DISTINCT` quantifier to specify which values to include in the calculation. For more information, see [Aggregate Quantifier](#aggregate-quantifier).

### [](#arguments-5)Arguments

See [Syntax](#aggregate-syntax).

### [](#return-value-5)Return Value

The function returns 1 of the following:

* A number that represents the count.
* `0` if there are no numeric values.

### [](#examples-4)Examples

Find the count of all numeric values

Query

```sqlpp
SELECT COUNTN(input) AS count_all
FROM [ 1, 1, 2, 2, 3, "abc", MISSING, NULL]
AS input;
```

Results

```json
[
  {
    "count_all": 5
  }
]
```

Find the count of distinct numeric values

Query

```sqlpp
SELECT COUNTN(DISTINCT input) AS count_distinct
FROM [ 1, 1, 2, 2, 3, "abc", MISSING, NULL]
AS input;
```

Results

```json
[
  {
    "count_distinct": 3
  }
]
```

## [](#max)MAX( \[ ALL | DISTINCT \] `expression`)

### [](#description-6)Description

Returns the maximum value in an expression. The function ignores `MISSING` and `NULL` values.

When comparing values of different data types, the function uses SQL++ [collation rules](datatypes.md#collation) to determine precedence.

> [!NOTE]
> The `ALL` and `DISTINCT` quantifiers do not affect the result of this function. The maximum value remains the same whether or not duplicates are included.

### [](#arguments-6)Arguments

See [Syntax](#aggregate-syntax).

### [](#return-value-6)Return Value

The function returns 1 of the following:

* The maximum value in the group.
* `NULL` if all values are either `MISSING` or `NULL`.

### [](#examples-5)Examples

Find the max value from a group of numbers

Query

```sqlpp
SELECT MAX(input) AS max_value_num
FROM [1, 3, 2, 3, MISSING, NULL]
AS input;
```

Results

```json
[
  {
    "max_value_num": 3
  }
]
```

Find the max value from a group with mixed types

Query

```sqlpp
SELECT MAX(input) AS max_value_all
FROM [1, 2, 3, "airline", "2025-12-01T00:00:00Z", NULL]
AS input;
```

Results

```json
[
  {
    "max_value_all": "airline"
  }
]
```

The function returns `airline` because strings have a higher precedence than numbers and dates.

Find the max value from a group of strings

Query

```sqlpp
SELECT MAX(input) AS max_value_string
FROM ["United", "Delta", "American", "Southwest"]
AS input;
```

Results

```json
[
  {
    "max_value_string": "United"
  }
]
```

When comparing string values, the function uses alphabetical order to determine the maximum value.

## [](#mean)MEAN( \[ ALL | DISTINCT \] `expression`)

Synonym of [AVG()](#avg).

## [](#median)MEDIAN( \[ ALL | DISTINCT \] `expression`)

### [](#description-7)Description

Returns the median of all numeric values in an expression.

You can use the `ALL` or `DISTINCT` quantifier to specify which values to include in the calculation. For more information, see [Aggregate Quantifier](#aggregate-quantifier).

### [](#arguments-7)Arguments

See [Syntax](#aggregate-syntax).

### [](#return-value-7)Return Value

The function returns 1 of the following:

* A number that represents the median value.
* A number that represents the mean of the 2 median values if the number of numeric values is even.
* `NULL` if there are no numeric values in the group.

### [](#examples-6)Examples

Find the median when the number of values is odd

Query

```sqlpp
SELECT MEDIAN(input) AS median_value
FROM [1, 2, 3, 3, 4, MISSING, NULL, "abc"]
AS input;
```

Results

```json
[
  {
    "median_value": 3
 }
]
```

In this example, the median is the middle value `3`.

Find the median when the number of values is even

Query

```sqlpp
SELECT MEDIAN(input) AS median_value
FROM [1, 2, 3, 3, 4, 4, MISSING, NULL, "abc"]
AS input;
```

Results

```json
[
  {
    "median_value": 3
 }
]
```

In this example, the median is the mean of the 2 middle values (`3` and `3`), which is `3`.

Find the median of distinct values

Query

```sqlpp
SELECT MEDIAN(DISTINCT input) AS median_value
FROM [1, 2, 3, 3, 4, 4, MISSING, NULL, "abc"]
AS input;
```

Results

```json
[
  {
    "median_value": 2.5
  }
]
```

In this example, the number of distinct numeric values is even. Therefore, the median is the mean of the 2 middle values (`2` and `3`), which is `2.5`.

## [](#min)MIN( \[ ALL | DISTINCT \] `expression`)

### [](#description-8)Description

Returns the minimum value in an expression. The function ignores `MISSING` and `NULL` values.

When comparing values of different data types, the function uses SQL++ [collation rules](datatypes.md#collation) to determine precedence.

> [!NOTE]
> The `ALL` and `DISTINCT` quantifiers do not affect the result of this function. The minimum value remains the same whether or not duplicates are included.

### [](#arguments-8)Arguments

See [Syntax](#aggregate-syntax).

### [](#return-value-8)Return Value

The function returns 1 of the following:

* The minimum value in the group.
* `NULL` if all values are either `MISSING` or `NULL`.

### [](#examples-7)Examples

Find the minimum value from a group of numbers

Query

```sqlpp
SELECT MIN(input) AS min_value_num
FROM [3, 1, 2, 1, MISSING, NULL]
AS input;
```

Results

```json
[
  {
    "min_value_num": 1
  }
]
```

Find the minimum value from a group with mixed types

Query

```sqlpp
SELECT MIN(input) AS min_value_all
FROM [1, 2, 3, "airline", "2025-12-01T00:00:00Z", NULL]
AS input;
```

Results

```json
[
  {
    "min_value_all": 1
  }
]
```

The function returns `1` because numbers have a lower precedence than strings and dates.

Find the minimum value from a group of strings

Query

```sqlpp
SELECT MIN(input) AS min_value_string
FROM ["United", "Delta", "American", "Southwest"]
AS input;
```

Results

```json
[
  {
    "min_value_string": "American"
  }
]
```

When comparing string values, the function uses alphabetical order to determine the minimum value.

## [](#stddev)STDDEV( \[ ALL | DISTINCT \] `expression`)

### [](#description-9)Description

Returns the [corrected sample standard deviation](#eqn%5Fsamp%5Fstd%5Fdev) of all numeric values in an expression.

You can use the `ALL` or `DISTINCT` quantifier to specify which values to include in the calculation. For more information, see [Aggregate Quantifier](#aggregate-quantifier).

> [!NOTE]
> This function is similar to [STDDEV\_SAMP()](#stddev%5Fsamp). However, it returns `0` if there is only 1 matching value, while [STDDEV\_SAMP()](#stddev%5Fsamp) returns `NULL` in such cases.

### [](#arguments-9)Arguments

See [Syntax](#aggregate-syntax).

### [](#return-value-9)Return Value

The function returns 1 of the following:

* A number that represents the corrected sample standard deviation.
* `0` if the group contains only 1 numeric value.
* `NULL` if there are no numeric values in the group.

### [](#examples-8)Examples

Find the standard deviation of all values

Query

```sqlpp
SELECT STDDEV(input) AS std_deviation_all
FROM [1, 2, 3, 4, 4, MISSING, NULL, "abc"]
AS input;
```

Results

```json
[
  {
    "std_deviation_all": 1.3038404810405297
  }
]
```

Find the standard deviation of distinct values

Query

```sqlpp
SELECT STDDEV(DISTINCT input) AS std_deviation_distinct
FROM [1, 2, 2, 3, 4, 4, MISSING, NULL, "abc"]
AS input;
```

Results

```json
[
  {
    "std_deviation_distinct": 1.2909944487358056
  }
]
```

Find the standard deviation of a single numeric value

Query

```sqlpp
SELECT STDDEV(input) AS std_deviation_single
FROM [3, NULL, "abc"]
AS input;
```

Results

```json
[
  {
    "std_deviation_single": 0
  }
]
```

## [](#stddev%5Fpop)STDDEV\_POP( \[ ALL | DISTINCT \] `expression`)

### [](#description-10)Description

Returns the [population standard deviation](#eqn%5Fpop%5Fstd%5Fdev) of all numeric values in an expression.

You can use the `ALL` or `DISTINCT` quantifier to specify which values to include in the calculation. For more information, see [Aggregate Quantifier](#aggregate-quantifier).

### [](#arguments-10)Arguments

See [Syntax](#aggregate-syntax).

### [](#return-value-10)Return Value

The function returns 1 of the following:

* A number that represents the population standard deviation.
* `0` if the group contains only 1 numeric value.
* `NULL` if there are no numeric values in the group.

### [](#examples-9)Examples

Find the population standard deviation of all values

Query

```sqlpp
SELECT STDDEV_POP(input) AS pop_deviation_all
FROM [1, 2, 3, 4, 4, MISSING, NULL, "abc"]
AS input;
```

Results

```json
[
  {
    "pop_deviation_all": 1.16619037896906
  }
]
```

Find the population standard deviation of distinct values

Query

```sqlpp
SELECT STDDEV_POP(DISTINCT input) AS pop_deviation_distinct
FROM [1, 2, 2, 3, 4, 4, MISSING, NULL, "abc"]
AS input;
```

Results

```json
[
  {
    "pop_deviation_distinct": 1.118033988749895
  }
]
```

## [](#stddev%5Fsamp)STDDEV\_SAMP( \[ ALL | DISTINCT \] `expression`)

### [](#description-11)Description

Returns the [corrected sample standard deviation](#eqn%5Fsamp%5Fstd%5Fdev) of all numeric values in an expression.

You can use the `ALL` or `DISTINCT` quantifier to specify which values to include in the calculation. For more information, see [Aggregate Quantifier](#aggregate-quantifier).

> [!NOTE]
> This function is similar to [STDDEV()](#stddev). However, it returns `NULL` if there is only 1 matching value, while [STDDEV()](#stddev) returns `0` in such cases.

### [](#arguments-11)Arguments

See [Syntax](#aggregate-syntax).

### [](#return-value-11)Return Value

The function returns 1 of the following:

* A number that represents the sample standard deviation.
* `NULL` if there are fewer than 2 numeric values in the group.

### [](#example-2)Example

Find the sample standard deviation of all values

Query

```sqlpp
SELECT STDDEV_SAMP(input) AS std_deviation_all
FROM [1, 2, 3, 4, 4, MISSING, NULL, "abc"]
AS input;
```

Results

```json
[
  {
    "std_deviation_all": 1.3038404810405297
  }
]
```

Find the sample standard deviation of distinct values

Query

```sqlpp
SELECT STDDEV_SAMP(DISTINCT input) AS std_deviation_distinct
FROM [1, 2, 2, 3, 4, 4, MISSING, NULL, "abc"]
AS input;
```

Results

```json
[
  {
    "std_deviation_distinct": 1.2909944487358056
  }
]
```

Find the sample standard deviation of a single numeric value

Query

```sqlpp
SELECT STDDEV_SAMP(input) AS std_dev_sample
FROM [3, NULL, "abc"]
AS input;
```

Results

```json
[
  {
    "std_dev_sample": null
  }
]
```

## [](#sum)SUM( \[ ALL | DISTINCT \] `expression`)

### [](#description-12)Description

Returns the arithmetic sum of all number values in an expression.

You can use the `ALL` or `DISTINCT` quantifier to specify which values to include in the calculation. For more information, see [Aggregate Quantifier](#aggregate-quantifier).

### [](#arguments-12)Arguments

See [Syntax](#aggregate-syntax).

### [](#return-value-12)Return Value

The function returns 1 of the following:

* A number that represents the sum.
* `NULL` if there are no numeric values in the group.

### [](#examples-10)Examples

Find the sum of all numbers

Query

```sqlpp
SELECT SUM(input) AS sum_all
FROM [1, 2, 3, 4, 4, MISSING, NULL, "abc"]
AS input;
```

Results

```json
[
  {
    "sum_all": 14
  }
]
```

Find the sum of distinct numbers

Query

```sqlpp
SELECT SUM(DISTINCT input) AS sum_distinct
FROM [1, 2, 3, 4, 4, MISSING, NULL, "abc"]
AS input;
```

Results

```json
[
  {
    "sum_distinct": 10
  }
]
```

## [](#variance)VARIANCE( \[ ALL | DISTINCT \] `expression`)

### [](#description-13)Description

Returns the unbiased sample variance (the square of the [corrected sample standard deviation](#eqn%5Fsamp%5Fstd%5Fdev)) of all numeric values in an expression.

You can use the `ALL` or `DISTINCT` quantifier to specify which values to include in the calculation. For more information, see [Aggregate Quantifier](#aggregate-quantifier).

> [!NOTE]
> This function is similar to [VARIANCE\_SAMP()](#variance%5Fsamp). However, it returns `0` if there is only 1 matching value, while [VARIANCE\_SAMP()](#variance%5Fsamp) returns `NULL` in such cases.

### [](#arguments-13)Arguments

See [Syntax](#aggregate-syntax).

### [](#return-value-13)Return Value

The function returns 1 of the following:

* A number that represents the unbiased sample variance.
* `0` if the group contains only 1 numeric value.
* `NULL` if there are no numeric values in the group.

### [](#examples-11)Examples

Find the sample variance of all values

Query

```sqlpp
SELECT VARIANCE(input) AS variance_all
FROM [1, 2, 3, 4, 4, MISSING, NULL, "abc"]
AS input;
```

Results

```json
[
  {
    "variance_all": 1.7
  }
]
```

Find the sample variance of distinct values

Query

```sqlpp
SELECT VARIANCE(DISTINCT input) AS variance_distinct
FROM [1, 2, 3, 4, 4, MISSING, NULL, "abc"]
AS input;
```

Results

```json
[
  {
    "variance_distinct": 1.6666666666666667
  }
]
```

Find the sample variance of a single numeric value

Query

```sqlpp
SELECT VARIANCE(input) AS variance_single
FROM [3, NULL, "abc"]
AS input;
```

Results

```json
[
  {
    "variance_single": 0
  }
]
```

## [](#variance%5Fpop)VARIANCE\_POP( \[ ALL | DISTINCT \] `expression`)

This function has a synonym [VAR\_POP()](#var%5Fpop).

### [](#description-14)Description

Returns the population variance (the square of the [population standard deviation](#eqn%5Fpop%5Fstd%5Fdev)) of all numeric values in an expression.

You can use the `ALL` or `DISTINCT` quantifier to specify which values to include in the calculation. For more information, see [Aggregate Quantifier](#aggregate-quantifier).

### [](#arguments-14)Arguments

See [Syntax](#aggregate-syntax).

### [](#return-value-14)Return Value

The function returns 1 of the following:

* A number that represents the population variance.
* `NULL` if there are no numeric values in the group.

### [](#examples-12)Examples

Find the population variance of all values

Query

```sqlpp
SELECT VARIANCE_POP(input) AS pop_variance_all
FROM [1, 2, 3, 4, 4, MISSING, NULL, "abc"]
AS input;
```

Results

```json
[
  {
    "pop_variance_all": 1.3599999999999999
  }
]
```

Find the population variance of distinct values

Query

```sqlpp
SELECT VARIANCE_POP(DISTINCT input) AS pop_variance_distinct
FROM [1, 2, 3, 4, 4, MISSING, NULL, "abc"]
AS input;
```

Results

```json
[
  {
    "pop_variance_distinct": 1.25
  }
]
```

Find the population variance of a single numeric value

Query

```sqlpp
SELECT VARIANCE_POP(input) AS pop_variance_single
FROM [3, NULL, "abc"]
AS input;
```

Results

```json
[
  {
    "pop_variance_single": null
  }
]
```

## [](#variance%5Fsamp)VARIANCE\_SAMP( \[ ALL | DISTINCT \] `expression`)

This function has a synonym [VAR\_SAMP()](#var%5Fsamp).

### [](#description-15)Description

Returns the unbiased sample variance (the square of the [corrected sample standard deviation](#eqn%5Fsamp%5Fstd%5Fdev)) of all numeric values in an expression.

You can use the `ALL` or `DISTINCT` quantifier to specify which values to include in the calculation. For more information, see [Aggregate Quantifier](#aggregate-quantifier).

> [!NOTE]
> This function is similar to [VARIANCE()](#variance). However, it returns `NULL` if there is only 1 matching value, while [VARIANCE()](#variance) returns `0` in such cases.

### [](#arguments-15)Arguments

See [Syntax](#aggregate-syntax).

### [](#return-value-15)Return Value

The function returns 1 of the following:

* A number that represents the sample variance.
* `NULL` if there is fewer than 2 numeric values in the group.

### [](#examples-13)Examples

Find the sample standard variance of all values

Query

```sqlpp
SELECT VARIANCE_SAMP(input) AS variance_all
FROM [1, 2, 3, 4, 4, MISSING, NULL, "abc"]
AS input;
```

Results

```json
[
  {
    "variance_all": 1.7
  }
]
```

Find the sample variance of distinct values

Query

```sqlpp
SELECT VARIANCE_SAMP(DISTINCT input) AS variance_distinct
FROM [1, 2, 3, 4, 4, MISSING, NULL, "abc"]
AS input;
```

Results

```json
[
  {
    "variance_distinct": 1.6666666666666667
  }
]
```

Find the sample variance of a single numeric value

Query

```sqlpp
SELECT VARIANCE_SAMP(input) AS variance_single
FROM [3, NULL, "abc"]
AS input;
```

Results

```json
[
  {
    "variance_single": null
  }
]
```

## [](#var%5Fpop)VAR\_POP( \[ ALL | DISTINCT \] `expression`)

Synonym of [VARIANCE\_POP()](#variance%5Fpop).

## [](#var%5Fsamp)VAR\_SAMP( \[ ALL | DISTINCT \] `expression`)

Synonym of [VARIANCE\_SAMP()](#variance%5Fsamp).

## [](#formulas)Formulas

Corrected Sample Standard Deviation

Formula for calculating the corrected sample standard deviation:

\\$s = sqrt(1/(n-1) sum\_(i=1)^n (x\_i - barx)^2)\\$ 

Population Standard Deviation

Formula for calculating the population standard deviation:

\\$sigma = sqrt((sum(x\_i - mu)^2)/N)"\\$ 

## [](#related-links)Related Links

* [GROUP BY Clause](groupby.md) for GROUP BY, LETTING, and HAVING clauses.
* [WINDOW Clause](window.md) for WINDOW clauses.
* [Window Functions](windowfun.md) for window functions.

---

[1](#%5Ffootnoteref%5F1). When counting all the documents within a collection, this function usually relies on the collection statistics, which include any [transaction records](../../learn/data/transactions.md#additional-storage-use) that may be stored in that collection. However, if the query performs an index scan using the primary index on that collection, counting all documents does not include any transaction records.