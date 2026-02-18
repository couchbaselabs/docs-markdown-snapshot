---
title: Boolean Logic
description: Some clauses, such as <code>WHERE</code>, <code>WHEN</code>, and
  <code>HAVING</code>, require values to be interpreted as Boolean values.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/n1ql/pages/n1ql-language-reference/booleanlogic.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/n1ql/n1ql-language-reference/booleanlogic.html)

# Boolean Logic

> Some clauses, such as `WHERE`, `WHEN`, and `HAVING`, require values to be interpreted as Boolean values. 

The following rules apply when evaluating these types of clauses:

* MISSING, NULL, and FALSE are FALSE
* numbers +0, -0, and NaN are FALSE
* empty strings, arrays, and objects are FALSE
* all other values are TRUE

## [](#four-valued-logic)Four-valued logic

In SQL++, Boolean propositions can evaluate to NULL or MISSING (as well as to TRUE and FALSE).

The following table describes how these values relate to the logical operators:

| a       | b       | a AND b | a OR b | NOT a   |
| ------- | ------- | ------- | ------ | ------- |
| TRUE    | TRUE    | TRUE    | TRUE   | FALSE   |
| FALSE   | FALSE   | TRUE    |        |         |
| NULL    | NULL    | TRUE    |        |         |
| MISSING | MISSING | TRUE    |        |         |
| FALSE   | TRUE    | FALSE   | TRUE   | TRUE    |
| FALSE   | FALSE   | FALSE   |        |         |
| NULL    | FALSE   | NULL    |        |         |
| MISSING | FALSE   | MISSING |        |         |
| NULL    | TRUE    | NULL    | TRUE   | NULL    |
| FALSE   | FALSE   | NULL    |        |         |
| NULL    | NULL    | NULL    |        |         |
| MISSING | MISSING | NULL    |        |         |
| MISSING | TRUE    | MISSING | TRUE   | MISSING |
| FALSE   | FALSE   | MISSING |        |         |
| NULL    | MISSING | NULL    |        |         |
| MISSING | MISSING | MISSING |        |         |

## [](#comparing-null-and-missing-values)Comparing NULL and MISSING values

| Operator       | Non-NULL Value | NULL  | MISSING |
| -------------- | -------------- | ----- | ------- |
| IS NULL        | FALSE          | TRUE  | MISSING |
| IS NOT NULL    | TRUE           | FALSE | MISSING |
| IS MISSING     | FALSE          | FALSE | TRUE    |
| IS NOT MISSING | TRUE           | TRUE  | FALSE   |
| IS VALUED      | TRUE           | FALSE | FALSE   |
| IS NOT VALUED  | FALSE          | TRUE  | TRUE    |