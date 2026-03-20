---
title: Conditional Functions for Numbers
description: Conditional functions evaluate expressions to determine if the
  values and formulas meet the specified condition.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/n1ql/pages/n1ql-language-reference/condfunnum.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:n1ql:n1ql-language-reference/condfunnum.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/n1ql/n1ql-language-reference/condfunnum.html)

# Conditional Functions for Numbers

Conditional functions evaluate expressions to determine if the values and formulas meet the specified condition.

## [](#ifinfexpression1-expression2)IFINF(expression1, expression2, ...)

### [](#description)Description

Returns first non-MISSING, non-Inf number. Returns MISSING or NULL if a non-number input is encountered first.

## [](#ifnanexpression1-expression2)IFNAN(expression1, expression2, ...)

### [](#description-2)Description

Returns first non-MISSING, non-NaN number. Returns MISSING or NULL if a non-number input is encountered first.

## [](#ifnanorinfexpression1-expression2)IFNANORINF(expression1, expression2, ...)

### [](#description-3)Description

Returns first non-MISSING, non-Inf, or non-NaN number. Returns MISSING or NULL if a non-number input is encountered first.

## [](#nanifexpression1-expression2)NANIF(expression1, expression2)

### [](#description-4)Description

Returns NaN if expression1 = expression2, otherwise returns expression1\. Returns MISSING or NULL if either input is MISSING or NULL.

## [](#neginfifexpression1-expression2)NEGINFIF(expression1, expression2)

### [](#description-5)Description

Returns NegInf if expression1 = expression2, otherwise returns expression1\. Returns MISSING or NULL if either input is MISSING or NULL.

## [](#posinfifexpression1-expression2)POSINFIF(expression1, expression2)

### [](#description-6)Description

Returns PosInf if expression1 = expression2, otherwise returns expression1\. Returns MISSING or NULL if either input is MISSING or NULL.

### [](#examples)Examples

Example 1\. Return null if infinite value is encountered.

Query

```sqlpp
select IFINF(0 / 0, 25, 23) as INF
```

Result

[
  {
    "INF": null
  }
]

Example 2\. Return first non-infinite value encountered.

Query

select IFINF(35, 0 / 0, 25, 23) as NONINF

Result

[
  {
    "NONINF": 35
  }
]