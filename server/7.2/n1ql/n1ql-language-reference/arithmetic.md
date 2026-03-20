---
title: Arithmetic Operators
description: Arithmetic operations perform the basic mathematical operations of
  addition, subtraction, multiplication, division, and modulo within an
  expression or any numerical value retrieved as part of query clauses.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/n1ql/pages/n1ql-language-reference/arithmetic.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:n1ql:n1ql-language-reference/arithmetic.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/n1ql/n1ql-language-reference/arithmetic.html)

# Arithmetic Operators

Arithmetic operations perform the basic mathematical operations of addition, subtraction, multiplication, division, and modulo within an expression or any numerical value retrieved as part of query clauses. Additionally, SQL++ provides a negation operation which changes the sign of a value.

> [!NOTE]
> These arithmetic operators only operate on numbers. In SQL++, arithmetic operators have their usual meaning. However, in any of these expressions:
> 
> * If any operand is MISSING, the value of the expression is MISSING.
> * If any operand is NULL and no operand is MISSING, the value of the expression is NULL.
> * If any operand is not a number, the operator evaluates to NULL.

## [](#syntax)Syntax

There are six different arithmetic syntaxes:

```ebnf
arithmetic-term ::= expr '+' expr |
                    expr '-' expr |
                    expr '*' expr |
                    expr '/' expr |
                    expr '%' expr |
                    '-' expr
```

![Syntax diagram](../_images/n1ql-language-reference/arithmetic-term.png) 

| Operator | Description                                                                                                                                              |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| +        | Add values.                                                                                                                                              |
| \-       | Subtract right value from left value.                                                                                                                    |
| \*       | Multiply values.                                                                                                                                         |
| /        | Divide left value by right value.                                                                                                                        |
| %        | Modulo. Divide left value by right value and return the remainder. NOTE: Modulo is an integer operator and will use only the integer part of each value. |
| \-value  | Negate value.                                                                                                                                            |

## [](#arguments)Arguments

expr1, expr2

Number or an expression that results in a number value.

## [](#return-value)Return Value

A number, representing the value of the arithmetic operation.

## [](#examples)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Example 1\. Select the longest flight and return its two airports and the distance in feet

Query

```sqlpp
SELECT sourceairport, destinationairport, ROUND(distance) AS DistanceInMiles,
       ROUND(distance)*5280 AS DistanceInFeet
FROM route
ORDER BY distance DESC
LIMIT 1;
```

Returns

```json
[
  {
    "DistanceInFeet": 72906240,
    "DistanceInMiles": 13808,
    "destinationairport": "DFW",
    "sourceairport": "SYD"
  }
]
```

Example 2\. Select the modulo of 5 and 3 and compare to the modulo of 5.4 and 3.4

Modulo with integers

```sqlpp
SELECT 5 % 3;
```

Returns

```json
[
  {
    "$1": 2
  }
]
```

Modulo with fractions

```sqlpp
SELECT 5.4 % 3.4;
```

Returns

```json
[
  {
    "$1": 2
  }
]
```

## [](#related-links)Related Links

Refer to [Comparison Operators](comparisonops.md) for numeric comparisons.