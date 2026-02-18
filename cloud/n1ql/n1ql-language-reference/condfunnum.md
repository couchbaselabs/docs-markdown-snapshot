---
title: Conditional Functions for Numbers
description: Conditional functions evaluate expressions to determine if the
  values and formulas meet the specified condition.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/n1ql/pages/n1ql-language-reference/condfunnum.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/cloud/n1ql/n1ql-language-reference/condfunnum.html)

# Conditional Functions for Numbers

> Conditional functions evaluate expressions to determine if the values and formulas meet the specified condition. 

## [](#ifinfexpr1-expr2)IFINF(`expr1`, `expr2`, …​)

This function has a synonym `IF_INF()`.

### [](#description)Description

Evaluates a list of expressions and returns the first finite number.

The function ignores `MISSING` and infinite values. If it encounters `NULL` or any non-numeric value before finding a finite number, the function returns `NULL`.

### [](#arguments)Arguments

expr1, expr2, …​

\[Required\] A list of valid expressions to evaluate. You must specify at least 2 expressions.

### [](#return-value)Return Value

The function returns 1 of the following:

* The first finite number.
* `NULL` if it encounters `NULL` or a non-number before finding a finite number.

### [](#example)Example

Example 1\. Find the first non-infinite number from a list of values

Query

```sqlpp
SELECT IFINF(5, 10, 20),
       IFINF(INF(), -INF(), 5, 10),
       IFINF(POWER(10, 400), 5, 10),
       IFINF(2.001e340, 5),
       IFINF(NULL, 5, 10),
       IFINF(MISSING, 5, NULL),
       IFINF(MISSING, NULL, 5, 10);
```

Result

```json
[
  {
    "$1": 5,
    "$2": 5,
    "$3": 5,
    "$4": 5,
    "$5": null,
    "$6": 5,
    "$7": null
  }
]
```

In this example:

* The functions `INF()` and `-INF()` return positive and negative infinity, respectively.
* The function `POWER(10, 400)` and the expression `2.001e340` return positive infinity because they exceed the maximum representable finite number.

## [](#ifnanexpr1-expr2)IFNAN(`expr1`, `expr2`, …​)

This function has a synonym `IF_NAN()`.

### [](#description-2)Description

Evaluates a list of expressions and returns the first valid number that’s not NaN (Not a Number).

The function ignores `MISSING` and NaN values. If it encounters `NULL` or any other non-number before finding a valid number, the function returns `NULL`.

### [](#arguments-2)Arguments

expr1, expr2, …​

\[Required\] A list of valid expressions to evaluate. You must specify at least 2 expressions.

### [](#return-value-2)Return Value

The function returns 1 of the following:

* The first valid number.
* `NULL` if it encounters `NULL` or a non-number before finding a number.

### [](#example-2)Example

Example 2\. Find a non-NaN number from a list of values

Query

```sqlpp
SELECT IFNAN(5, 10, 20, NAN()),
       IFNAN(SQRT(-1), 5, 10),
       IFNAN("abc", 5, NULL, 10),
       IFNAN(NULL, 5, 10),
       IFNAN(MISSING, 5, NULL),
       IFNAN(MISSING, NULL, 5, 10),
       IFNAN(NAN(), 5, 10);
```

Result

```json
[
  {
    "$1": 5,
    "$2": 5,
    "$3": null,
    "$4": null,
    "$5": 5,
    "$6": null,
    "$7": 5
  }
]
```

In this example:

* The function `NAN()` returns a NaN value.
* The function `SQRT(-1)` also returns NaN because the square root of a negative number is not a real number.

## [](#ifnanorinfexpr1-expr2)IFNANORINF(`expr1`, `expr2`, …​)

This function has a synonym `IF_NAN_OR_INF()`.

### [](#description-3)Description

Evaluates a list of expressions and returns the first number that’s neither NaN (Not a Number) nor infinite.

The function skips `MISSING`, NaN, and infinite values. If it encounters `NULL` or any other non-number before finding a valid number, the function returns `NULL`.

### [](#arguments-3)Arguments

expr1, expr2, …​

\[Required\] A list of valid expressions to evaluate. You must specify at least 2 expressions.

### [](#return-value-3)Return Value

The function returns 1 of the following:

* The first number that’s neither NaN nor infinite.
* `NULL` if it encounters `NULL` or a non-number before finding such a number.

### [](#example-3)Example

Example 3\. Find a number that’s neither NaN nor infinite from a list of values

Query

```sqlpp
SELECT IFNANORINF(5, 10, NAN(), INF()),
       IFNANORINF(SQRT(-1), -INF(), 5, 10),
       IFNANORINF(2.001e340, 5, 10),
       IFNANORINF("abc", 5, NULL, 10),
       IFNANORINF(NULL, 5, 10),
       IFNANORINF(MISSING, 5, NULL);
```

Result

```json
[
  {
    "$1": 5,
    "$2": 5,
    "$3": 5,
    "$4": null,
    "$5": null,
    "$6": 5
  }
]
```

In this example:

* The function `NAN()` returns a NaN value.
* The functions `INF()` and `-INF()` return positive and negative infinity, respectively.
* The function `SQRT(-1)` returns NaN because the square root of a negative number is not a real number.
* The expression `2.001e340` returns positive infinity because it exceeds the maximum representable finite number.

## [](#nanifexpr1-expr2)NANIF(`expr1`, `expr2`)

This function has a synonym `NAN_IF()`.

### [](#description-4)Description

Compares 2 expressions and returns `NaN` (Not a Number) if they’re equal; otherwise, it returns the value of the first expression.

### [](#arguments-4)Arguments

expr1

\[Required\] A valid expression.

expr2

\[Required\] A valid expression to compare with `expr1`.

### [](#return-value-4)Return Value

The function returns 1 of the following:

* `"NaN"` if `expr1` is equal to `expr2`.
* `expr1` if the expressions are not equal.
* `NULL` if either expression is `MISSING` or `NULL`.

### [](#example-4)Example

Example 4\. Compare 2 values and return NaN if they’re equal

Query

```sqlpp
SELECT NANIF(10, 10) AS nan_equal,
       NANIF(10, 5) AS nan_not_equal,
       NANIF(NULL, 5) AS nan_null;
```

Result

```json
[
  {
    "nan_equal": "NaN",
    "nan_not_equal": 10,
    "nan_null": null
  }
]
```

## [](#neginfifexpr1-expr2)NEGINFIF(`expr1`, `expr2`)

This function has a synonym `NEGINF_IF()`.

### [](#description-5)Description

Compares 2 expressions and returns negative infinity if they’re equal; otherwise, it returns the value of the first expression.

### [](#arguments-5)Arguments

expr1

\[Required\] A valid expression.

expr2

\[Required\] A valid expression to compare with `expr1`.

### [](#return-value-5)Return Value

The function returns 1 of the following:

* `"-Infinity"` if `expr1` is equal to `expr2`.
* `expr1` if the expressions are not equal.
* `NULL` if either expression is `MISSING` or `NULL`.

### [](#example-5)Example

Example 5\. Compare 2 values and return negative infinity if they’re equal

Query

```sqlpp
SELECT NEGINFIF(10, 10) AS neg_inf_equal,
       NEGINFIF(10, 5) AS neg_inf_not_equal,
       NEGINFIF(NULL, 5) AS neg_inf_null;
```

Result

```json
[
  {
    "neg_inf_equal": "-Infinity",
    "neg_inf_not_equal": 10,
    "neg_inf_null": null
  }
]
```

## [](#posinfifexpr1-expr2)POSINFIF(`expr1`, `expr2`)

This function has a synonym `POSINF_IF()`.

### [](#description-6)Description

Compares 2 expressions and returns positive infinity if they’re equal; otherwise, it returns the value of the first expression.

### [](#arguments-6)Arguments

expr1

\[Required\] A valid expression.

expr2

\[Required\] A valid expression to compare with `expr1`.

### [](#return-value-6)Return Value

The function returns 1 of the following:

* `"+Infinity"` if `expr1` is equal to `expr2`.
* `expr1` if the expressions are not equal.
* `NULL` if either expression is `MISSING` or `NULL`.

### [](#example-6)Example

Example 6\. Compare 2 values and return positive infinity if they’re equal

Query

```sqlpp
SELECT POSINFIF(10, 10) AS pos_inf_equal,
       POSINFIF(10, 5) AS pos_inf_not_equal,
       POSINFIF(NULL, 5) AS pos_inf_null;
```

Result

```json
[
  {
    "pos_inf_equal": "+Infinity",
    "pos_inf_not_equal": 10,
    "pos_inf_null": null
  }
]
```