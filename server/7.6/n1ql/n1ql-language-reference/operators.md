---
title: Operators Overview
description: Operators perform a specific operation on the input values or expressions.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/n1ql/pages/n1ql-language-reference/operators.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.6/n1ql/n1ql-language-reference/operators.html)

# Operators Overview

> Operators perform a specific operation on the input values or expressions. 

SQL++ provides a full set of operators that you can use within its statements. Here are the categories of SQL++ operators:

* [Arithmetic Operators](arithmetic.md) to perform basic mathematical operations (such as addition, subtraction, multiplication, and divisions) on numbers.
* [Collection Operators](collectionops.md) to evaluate expressions on collections or objects.
* [Comparison Operators](comparisonops.md) to compare two expressions.
* [Conditional Operators](conditionalops.md) to evaluate conditional logic in an expression.
* [Construction Operators](constructionops.md) to construct arrays and objects.
* [Logical Operators](logicalops.md) to combine operators using Boolean logic.
* [Nested Operators and Expressions](nestedops.md) to access nested elements and embedded arrays.
* [Sequence Operators](sequenceops.md) to access values in a sequence.
* [String Operators](stringops.md) to concatenate two expressions.

## [](#operator-precedence)Operator Precedence

SQL++ supports the use of parentheses to group operators and expressions. Expressions enclosed in parentheses are evaluated first.

The following table shows operator precedence level. An operator at a higher level is evaluated before an operator at a lower level.

| Evaluation Order | Operator                                                                                       |
| ---------------- | ---------------------------------------------------------------------------------------------- |
| 1                | CASE                                                                                           |
| 2                | . (period)                                                                                     |
| 3                | \[ \] (left and right bracket)                                                                 |
| 4                | \- (unary)                                                                                     |
| 5                | \* (multiply), / (divide), % (modulo)                                                          |
| 6                | +, \- (binary)                                                                                 |
| 7                | IS                                                                                             |
| 8                | IN                                                                                             |
| 9                | BETWEEN                                                                                        |
| 10               | LIKE                                                                                           |
| 11               | < (less than, <= (less than or equal to, \> (greater than), and \=> (equal to or greater than) |
| 12               | \= (equal to) , \== (equal to), <> (less than or greater than), != (not equal to)              |
| 13               | NOT                                                                                            |
| 15               | AND                                                                                            |
| 16               | OR                                                                                             |