---
title: Aggregate Functions
description: Aggregate functions take multiple values from documents, perform
  calculations, and return a single value as the result.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/n1ql/pages/n1ql-language-reference/aggregatefun.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:n1ql:n1ql-language-reference/aggregatefun.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/n1ql/n1ql-language-reference/aggregatefun.html)

# Aggregate Functions

Aggregate functions take multiple values from documents, perform calculations, and return a single value as the result. The function names are case insensitive.

You can only use aggregate functions in `SELECT`, `LETTING`, `HAVING`, and `ORDER BY` clauses. When using an aggregate function in a query, the query operates as an aggregate query.

In Couchbase Server Enterprise Edition, aggregate functions can also be used as [window functions](windowfun.md) when they are used with a window specification, which is introduced by the `OVER` keyword.

In Couchbase Server 7.0 and later, window functions (and aggregate functions used as window functions) may specify their own inline window definitions, or they may refer to a named window defined by the WINDOW clause elsewhere in the query. By defining a named window with the WINDOW clause, you can reuse the window definition across several functions in the query, potentially making the query easier to write and maintain.

## [](#syntax)Syntax

This section describes the generic syntax of aggregate functions. Refer to sections below for details of individual aggregate functions.

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

The **aggregate quantifier** determines whether the function aggregates all values in the group, or distinct values only.

`ALL`

All objects are included in the computation.

`DISTINCT`

Only distinct objects are included in the computation.

This quantifier can only be used with aggregate functions.

This quantifier is optional. If omitted, the default value is `ALL`.

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

### [](#return-value)Return Value

With the `ALL` quantifier, or no quantifier, returns an array of the non-MISSING values in the group, including NULL values.

With the `DISTINCT` quantifier, returns an array of the distinct non-MISSING values in the group, including NULL values.

### [](#examples)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

List all values of the `Cleanliness` reviews given:

Query

```sqlpp
SELECT ARRAY_AGG(reviews[0].ratings.Cleanliness) AS Reviews
FROM hotel;
```

Results

```json
[
  {
    "Reviews": [
      -1,
      -1,
      -1,
      -1,
      -1,
      // ...
    ]
  }
]
```

List all unique values of the `Cleanliness` reviews given:

Query

```sqlpp
SELECT ARRAY_AGG(DISTINCT reviews[0].ratings.Cleanliness) AS Reviews
FROM hotel;
```

Results

```json
[
  {
    "UniqueReviews": [
      -1,
      1,
      2,
      3,
      4,
      5
    ]
  }
]
```

## [](#avg)AVG( \[ ALL | DISTINCT \] `expression`)

This function has an alias [MEAN()](#mean).

### [](#return-value-2)Return Value

With the `ALL` quantifier, or no quantifier, returns the arithmetic mean (average) of all the number values in the group.

With the `DISTINCT` quantifier, returns the arithmetic mean (average) of all the distinct number values in the group.

Returns NULL if there are no number values in the group.

### [](#examples-2)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Find the average altitude of airports in the `airport` keyspace:

Query

```sqlpp
SELECT AVG(geo.alt) AS AverageAltitude FROM airport;
```

Results

```json
[
  {
    "AverageAltitude": 870.1651422764228
  }
]
```

Find the average number of stops per route vs. the average of distinct numbers of stops:

Query

```sqlpp
SELECT AVG(ALL stops) AS AvgAllStops FROM route;
```

Results in 0.0002 since nearly all routes have 0 stops.

```sqlpp
SELECT AVG(DISTINCT stops) AS AvgDistinctStops FROM route;
```

Results in 0.5 since all routes have only 1 or 0 stops.

## [](#count%5Fall)COUNT(\*)

### [](#return-value-3)Return Value

Returns count of all the input rows for the group, regardless of value. \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]

### [](#example)Example

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Find the number of documents in the `landmark` keyspace:

Query

```sqlpp
SELECT COUNT(*) AS CountAll FROM landmark;
```

Results

```json
[
  {
    "CountAll": 4495
  }
]
```

## [](#count)COUNT( \[ ALL | DISTINCT \] `expression`)

### [](#return-value-4)Return Value

With the `ALL` quantifier, or no quantifier, returns count of all the non-NULL and non-MISSING values in the group. \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]

With the `DISTINCT` quantifier, returns count of all the distinct non-NULL and non-MISSING values in the group.

### [](#examples-3)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Find the number of documents with an airline route stop in the `route` keyspace regardless of its value:

Query

```sqlpp
SELECT COUNT(stops) AS CountOfStops FROM route;
```

Results

```json
[
  {
    "CountOfStops": 24024
  }
]
```

Find the number of unique values of airline route stops in the `route` keyspace:

Query

```sqlpp
SELECT COUNT(DISTINCT stops) AS CountOfDistinctStops
FROM route;
```

Results

```json
[
  {
    "CountOfSDistinctStops": 2 (1)
  }
]
```

| **1** | Results in 2 because there are only 0 or 1 stops. |
| ----- | ------------------------------------------------- |

## [](#countn)COUNTN( \[ ALL | DISTINCT \] `expression` )

### [](#return-value-5)Return Value

With the `ALL` quantifier, or no quantifier, returns a count of all the numeric values in the group. \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]

With the `DISTINCT` quantifier, returns a count of all the distinct numeric values in the group.

### [](#examples-4)Examples

The count of numeric values in a mixed group.

```sqlpp
SELECT COUNTN(list.val) AS CountOfNumbers
FROM [
  {"val":1},
  {"val":1},
  {"val":2},
  {"val":"abc"}
] AS list;
```

Results

```json
[
  {
    "CountOfNumbers": 3
  }
]
```

The count of unique numeric values in a mixed group.

```sqlpp
SELECT COUNTN(DISTINCT list.val) AS CountOfNumbers
FROM [
  {"val":1},
  {"val":1},
  {"val":2},
  {"val":"abc"}
] AS list;
```

Results

```json
[
  {
    "CountOfNumbers": 2
  }
]
```

## [](#max)MAX( \[ ALL | DISTINCT \] `expression`)

### [](#return-value-6)Return Value

Returns the maximum non-NULL, non-MISSING value in the group in SQL++ collation order.

This function returns the same result with the `ALL` quantifier, the `DISTINCT` quantifier, or no quantifier.

### [](#examples-5)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Max of an integer field

Find the northernmost latitude of any hotel in the `hotel` keyspace:

Query

```sqlpp
SELECT MAX(geo.lat) AS MaxLatitude FROM hotel;
```

Results

```json
[
  {
    "MaxLatitude": 60.15356
  }
]
```

Max of a string field

Find the hotel whose name is last alphabetically in the `hotel` keyspace:

Query

```sqlpp
SELECT MAX(name) AS MaxName FROM hotel;
```

Results

```json
[
  {
    "MaxName": "pentahotel Birmingham"
  }
]
```

That result might have been surprising since lowercase letters come after uppercase letters and are therefore "higher" than uppercase letters. To avoid this uppercase/lowercase confusion, you should first make all values uppercase or lowercase, as in the following example.

Max of a string field, regardless of case

Find the hotel whose name is last alphabetically in the `hotel` keyspace:

Query

```sqlpp
SELECT MAX(UPPER(name)) AS MaxName FROM hotel;
```

Results

```json
[
  {
    "MaxName": "YOSEMITE LODGE AT THE FALLS"
  }
]
```

## [](#mean)MEAN( \[ ALL | DISTINCT \] `expression`)

Alias for [AVG()](#avg).

## [](#median)MEDIAN( \[ ALL | DISTINCT \] `expression`)

### [](#return-value-7)Return Value

With the `ALL` quantifier, or no quantifier, returns the median of all the number values in the group. If there is an even number of number values, returns the mean of the median two values.

With the `DISTINCT` quantifier, returns the median of all the distinct number values in the group. If there is an even number of distinct number values, returns the mean of the median two values.

Returns NULL if there are no number values in the group.

### [](#examples-6)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Find the median altitude of airports in the `airport` keyspace:

Query

```sqlpp
SELECT MEDIAN(geo.alt) AS MedianAltitude
FROM airport;
```

Results

```json
[
  {
    "MedianAltitude": 361.5
  }
]
```

Find the median of distinct altitudes of airports in the `airport` keyspace:

Query

```sqlpp
SELECT MEDIAN(DISTINCT geo.alt) AS MedianAltitude FROM airport;
```

Results

```json
[
  {
    "MedianDistinctAltitude": 758
  }
]
```

## [](#min)MIN( \[ ALL | DISTINCT \] `expression`)

### [](#return-value-8)Return Value

Returns the minimum non-NULL, non-MISSING value in the group in SQL++ collation order.

This function returns the same result with the `ALL` quantifier, the `DISTINCT` quantifier, or no quantifier.

### [](#examples-7)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Min of an integer field

Find the southernmost latitude of any hotel in the `hotel` keyspace:

Query

```sqlpp
SELECT MIN(geo.lat) AS MinLatitude FROM hotel;
```

Results

```json
[
  {
    "MinLatitude": 32.68092
  }
]
```

Min of a string field

Find the hotel whose name is first alphabetically in the `hotel` keyspace:

Query

```sqlpp
SELECT MIN(name) AS MinName FROM hotel;
```

Results

```json
[
  {
    "MinName": "'La Mirande Hotel"
  }
]
```

That result might have been surprising since some symbols come before letters and are therefore "lower" than letters. To avoid this symbol confusion, you can specify letters only, as in the following example.

Min of a string field, regardless of preceding non-letters

Find the first hotel alphabetically in the `hotel` keyspace:

Query

```sqlpp
SELECT MIN(name) FILTER (WHERE SUBSTR(name,0)>="A") AS MinName
FROM hotel;
```

Results

```json
[
  {
    "MinName": "AIRE NATURELLE LE GROZEAU Aire naturelle"
  }
]
```

## [](#stddev)STDDEV( \[ ALL | DISTINCT \] `expression`)

### [](#return-value-9)Return Value

With the `ALL` quantifier, or no quantifier, returns the [corrected sample standard deviation](#eqn%5Fsamp%5Fstd%5Fdev) of all the number values in the group.

With the `DISTINCT` quantifier, returns the [corrected sample standard deviation](#eqn%5Fsamp%5Fstd%5Fdev) of all the distinct number values in the group.

Returns NULL if there are no number values in the group.

### [](#examples-8)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Find the sample standard deviation of all values:

Query

```sqlpp
SELECT STDDEV(reviews[0].ratings.Cleanliness) AS StdDev
FROM hotel
WHERE city="London";
```

Results

```json
[
  {
    "StdDev": 2.0554275433769753
  }
]
```

Find the sample standard deviation of a single value:

Query

```sqlpp
SELECT STDDEV(reviews[0].ratings.Cleanliness) AS StdDevSingle
FROM hotel
WHERE name="Sachas Hotel";
```

Results

```json
[
  {
    "StdDevSingle": 0 (1)
  }
]
```

| **1** | There is only one matching result in the input, so the function returns 0. |
| ----- | -------------------------------------------------------------------------- |

Find the sample standard deviation of distinct values:

Query

```sqlpp
SELECT STDDEV(DISTINCT reviews[0].ratings.Cleanliness) AS StdDev
FROM hotel
WHERE city="London";
```

Results

```json
[
  {
    "StdDevDistinct": 2.1602468994692865
  }
]
```

## [](#stddev%5Fpop)STDDEV\_POP( \[ ALL | DISTINCT \] `expression`)

### [](#return-value-10)Return Value

With the `ALL` quantifier, or no quantifier, returns the [population standard deviation](#eqn%5Fpop%5Fstd%5Fdev) of all the number values in the group.

With the `DISTINCT` quantifier, returns the [population standard deviation](#eqn%5Fpop%5Fstd%5Fdev) of all the distinct number values in the group.

Returns NULL if there are no number values in the group.

### [](#examples-9)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Find the population standard deviation of all values:

Query

```sqlpp
SELECT STDDEV_POP(reviews[0].ratings.Cleanliness) AS PopStdDev
FROM hotel
WHERE city="London";
```

Results

```json
[
  {
    "PopStdDev": 2.0390493736539432
  }
]
```

Find the population standard deviation of distinct values:

Query

```sqlpp
SELECT STDDEV_POP(DISTINCT reviews[0].ratings.Cleanliness) AS PopStdDev
FROM hotel
WHERE city="London";
```

Results

```json
[
  {
      "PopStdDevDistinct": 1.9720265943665387
  }
]
```

## [](#stddev%5Fsamp)STDDEV\_SAMP( \[ ALL | DISTINCT \] `expression`)

A near-synonym for [STDDEV()](#stddev). The only difference is that `STDDEV_SAMP()` returns NULL if there is only one matching element.

### [](#example-2)Example

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Find the sample standard deviation of a single value:

Query

```sqlpp
SELECT STDDEV_SAMP(reviews[0].ratings.Cleanliness) AS StdDevSingle
FROM hotel
WHERE name="Sachas Hotel";
```

Results

```json
[
  {
    "StdDevSamp": null (1)
  }
]
```

| **1** | There is only one matching result in the input, so the function returns NULL. |
| ----- | ----------------------------------------------------------------------------- |

## [](#sum)SUM( \[ ALL | DISTINCT \] `expression`)

### [](#return-value-11)Return Value

With the `ALL` quantifier, or no quantifier, returns the sum of all the number values in the group.

With the `DISTINCT` quantifier, returns the arithmetic sum of all the distinct number values in the group.

Returns NULL if there are no number values in the group.

### [](#examples-10)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Find the sum total of all airline route stops in the `route` keyspace:

Query

```sqlpp
SELECT SUM(stops) AS SumOfStops FROM route;
```

> [!NOTE]
> In the `route` keyspace, nearly all flights are non-stop (0 stops) and only six flights have 1 stop, so we expect 6 flights of 1 stop each, a total of 6\.

Results

```json
[
  {
    "SumOfStops": 6 (1)
  }
]
```

| **1** | There are 6 routes with 1 stop each. |
| ----- | ------------------------------------ |

Find the sum total of all unique numbers of airline route stops in the `route` keyspace:

Query

```sqlpp
SELECT SUM(DISTINCT stops) AS SumOfStops FROM route;
```

Results

```json
[
  {
    "SumOfDistinctStops": 1 (1)
  }
]
```

| **1** | There are only 0 and 1 stops per route; and 0 + 1 = 1. |
| ----- | ------------------------------------------------------ |

## [](#variance)VARIANCE( \[ ALL | DISTINCT \] `expression`)

### [](#return-value-12)Return Value

With the `ALL` quantifier, or no quantifier, returns the unbiased sample variance (the square of the [corrected sample standard deviation](#eqn%5Fsamp%5Fstd%5Fdev)) of all the number values in the group.

With the `DISTINCT` quantifier, returns the unbiased sample variance (the square of the [corrected sample standard deviation](#eqn%5Fsamp%5Fstd%5Fdev)) of all the distinct number values in the group.

Returns NULL if there are no number values in the group.

This function has a near-synonym [VARIANCE\_SAMP()](#variance%5Fsamp). The only difference is that `VARIANCE()` returns NULL if there is only one matching element.

### [](#examples-11)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Find the sample variance of all values:

Query

```sqlpp
SELECT VARIANCE(reviews[0].ratings.Cleanliness) AS Variance
FROM hotel
WHERE city="London";
```

Results

```json
[
  {
    "Variance": 4.224782386072708
  }
]
```

Find the sample variance of a single value:

Query

```sqlpp
SELECT VARIANCE(reviews[0].ratings.Cleanliness) AS VarianceSingle
FROM hotel
WHERE name="Sachas Hotel";
```

Results

```json
[
  {
    "VarianceSingle": 0 (1)
  }
]
```

| **1** | There is only one matching result in the input, so the function returns 0. |
| ----- | -------------------------------------------------------------------------- |

Find the sampling variance of distinct values:

Query

```sqlpp
SELECT VARIANCE(DISTINCT reviews[0].ratings.Cleanliness) AS Variance
FROM hotel
WHERE city="London";
```

Results

```json
[
  {
    "VarianceDistinct": 4.666666666666667
  }
]
```

## [](#variance%5Fpop)VARIANCE\_POP( \[ ALL | DISTINCT \] `expression`)

This function has an alias [VAR\_POP()](#var%5Fpop).

### [](#return-value-13)Return Value

With the `ALL` quantifier, or no quantifier, returns the population variance (the square of the [population standard deviation](#eqn%5Fpop%5Fstd%5Fdev)) of all the number values in the group.

With the `DISTINCT` quantifier, returns the population variance (the square of the [population standard deviation](#eqn%5Fpop%5Fstd%5Fdev)) of all the distinct number values in the group.

Returns NULL if there are no number values in the group.

### [](#examples-12)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Find the population variance of all values:

Query

```sqlpp
SELECT VARIANCE_POP(reviews[0].ratings.Cleanliness) AS PopVariance
FROM hotel
WHERE city="London";
```

Results

```json
[
  {
    "PopVariance": 4.157722348198537
  }
]
```

Find the population variance of distinct values:

Query

```sqlpp
SELECT VARIANCE_POP(DISTINCT reviews[0].ratings.Cleanliness) AS PopVarianceDistinct
FROM hotel
WHERE city="London";
```

Results

```json
[
  {
      "PopVarianceDistinct": 3.8888888888888893
  }
]
```

## [](#variance%5Fsamp)VARIANCE\_SAMP( \[ ALL | DISTINCT \] `expression`)

A near-synonym for [VARIANCE()](#variance). The only difference is that `VARIANCE_SAMP()` returns NULL if there is only one matching element.

This function has an alias [VAR\_SAMP()](#var%5Fsamp).

### [](#example-3)Example

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Find the sample standard deviation of a single value:

Query

```sqlpp
SELECT VARIANCE_SAMP(reviews[0].ratings.Cleanliness) AS VarianceSamp
FROM hotel
WHERE name="Sachas Hotel";
```

Results

```json
[
  {
    "VarianceSamp": null (1)
  }
]
```

| **1** | There is only one matching result in the input, so the function returns NULL. |
| ----- | ----------------------------------------------------------------------------- |

## [](#var%5Fpop)VAR\_POP( \[ ALL | DISTINCT \] `expression`)

Alias for [VARIANCE\_POP()](#variance%5Fpop).

## [](#var%5Fsamp)VAR\_SAMP( \[ ALL | DISTINCT \] `expression`)

Alias for [VARIANCE\_SAMP()](#variance%5Fsamp).

## [](#formulas)Formulas

Corrected Sample Standard Deviation

The corrected sample standard deviation is calculated according to the following formula.

\\$s = sqrt(1/(n-1) sum\_(i=1)^n (x\_i - barx)^2)\\$ 

Population Standard Deviation

The population standard deviation is calculated according to the following formula.

\\$sigma = sqrt((sum(x\_i - mu)^2)/N)"\\$ 

## [](#related-links)Related Links

* [GROUP BY Clause](groupby.md) for GROUP BY, LETTING, and HAVING clauses.
* [WINDOW Clause](window.md) for WINDOW clauses.
* [Window Functions](windowfun.md) for window functions.

---

[1](#%5Ffootnoteref%5F1). When counting all the documents within a collection, this function usually relies on the collection statistics, which include any [transaction records](../../learn/data/transactions.md#additional-storage-use) that may be stored in that collection. However, if the query performs an index scan using the primary index on that collection, counting all documents does not include any transaction records.