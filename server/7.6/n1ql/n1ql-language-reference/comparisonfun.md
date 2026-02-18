---
title: Comparison Functions
description: Comparison functions determine the greatest or least value from a
  set of values.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/n1ql/pages/n1ql-language-reference/comparisonfun.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.6/n1ql/n1ql-language-reference/comparisonfun.html)

# Comparison Functions

> Comparison functions determine the greatest or least value from a set of values. 

## [](#comparison-func-greatest)GREATEST(`expr1` , `expr2`, …​)

### [](#description)Description

Returns the greatest value from a list of expressions.

The function compares values based on the sort order of their data types. For example, it compares strings alphabetically and dates chronologically. When comparing values of different data types, the function uses [collation rules](datatypes.md#collation) to determine precedence.

The function requires at least 2 expressions and ignores `NULL` and `MISSING` when evaluating values.

### [](#arguments)Arguments

expr1, expr2, …​

The expressions to compare. You must specify at least 2 expressions.

### [](#return-value)Return Value

The function returns:

* The largest value among the provided expressions.
* `NULL` if all expressions are `NULL` or `MISSING`.

### [](#examples)Examples

Example 1\. Find the greatest value from a list of numbers

Query

```sqlpp
SELECT GREATEST(19.50, 15, 21.50, 18) AS greatest_number;
```

Result

```json
[
  {
    "greatest_number": 21.5
  }
]
```

Example 2\. Find the greatest value from a list of strings

Query

```sqlpp
SELECT GREATEST("United", "Delta", "American", "Southwest")
AS last_airline_name;
```

Result

```json
[
  {
    "last_airline_name": "United"
  }
]
```

When comparing string values, the function uses alphabetical order to determine the greatest value.

Example 3\. Find the greatest value from a list with mixed types

Query

```sqlpp
SELECT GREATEST(42, "airline", "2025-12-01T00:00:00Z", NULL)
AS greatest_value;
```

Result

```json
[
  {
    "greatest_value": "airline"
  }
]
```

The function returns `"airline"` because strings have a higher precedence than numbers and dates.

## [](#comparison-func-least)LEAST(`expr1` , `expr2`, …​)

### [](#description-2)Description

Returns the smallest value from a list of expressions.

The function compares values based on the sort order of their data types. For example, it compares strings alphabetically and dates chronologically. When comparing values of different data types, the function uses [collation rules](datatypes.md#collation) to determine precedence.

The function requires at least 2 expressions and ignores `NULL` and `MISSING` when evaluating values.

### [](#arguments-2)Arguments

expr1, expr2, …​

The expressions to compare. You must specify at least 2 expressions.

### [](#return-value-2)Return Value

The function returns:

* The smallest value among the provided expressions.
* `NULL` if all expressions are `NULL` or `MISSING`.

### [](#examples-2)Examples

Example 4\. Find the least value from a list of numbers

Query

```sqlpp
SELECT LEAST(19.50, 15, 21.50, 18) AS lowest_number;
```

Result

```json
[
  {
    "lowest_number": 15
  }
]
```

Example 5\. Find the least value from a list of strings

Query

```sqlpp
SELECT LEAST("United", "Delta", "American", "Southwest")
AS first_airline_name;
```

Result

```json
[
  {
    "first_airline_name": "American"
  }
]
```

When comparing string values, the function uses alphabetical order to determine the least value.

Example 6\. Find the least value from a list with mixed types

Query

```sqlpp
SELECT LEAST(42, "airline", "2025-12-01T00:00:00Z", NULL)
AS least_value;
```

Result

```json
[
  {
    "least_value": 42
  }
]
```

The function returns `42` because numbers have a lower precedence than strings and dates.