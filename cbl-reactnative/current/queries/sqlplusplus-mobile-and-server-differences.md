---
title: SQL&#43;&#43; for Mobile and Server Differences
pubDate: 2026-10-03T04:27:21.374Z
meta:
  component:
    title: Couchbase Lite React Native
    version: "1.1"
antora:
  editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-react-native/edit/release/1.1/modules/queries/pages/sqlplusplus-mobile-and-server-differences.adoc
  xref: xref:cbl-reactnative:queries:sqlplusplus-mobile-and-server-differences.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cbl-reactnative/current/queries/sqlplusplus-mobile-and-server-differences.html)

# SQL&#43;&#43; for Mobile and Server Differences

> [!IMPORTANT]
> N1QL is Couchbase's implementation of the developing SQL++ standard. As such the terms N1QL and SQL++ are used interchangeably in all Couchbase documentation unless explicitly stated otherwise.

There are several minor but notable behavior differences between SQL++ for Mobile queries and SQL++ for Server, as shown in [Table 1](#table-1-sql-query-comparison).

In some instances, if required, you can force SQL++ for Mobile to work in the same way as SQL++ for Server. These instances are noted in the content below.

#### Table 1\. SQL++ Query Comparison

| Feature                   | SQL++ for Server                                                                                                                                                                   | SQL++ for Mobile                                                                                                                                                                                          |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| USE KEYS                  | SELECT fname, email FROM tutorial USE KEYS ('dave', 'ian');                                                                                                                        | SELECT fname, email FROM tutorial WHERE META().id IN ('dave', 'ian');                                                                                                                                     |
| ON KEYS                   | SELECT \* FROM user u JOIN orders o ON KEYS ARRAY s.order\_id FOR s IN u.order\_history END;                                                                                       | SELECT \* FROM user u, u.order\_history s JOIN orders o ON s.order\_id = Meta(o).id;                                                                                                                      |
| USE KEY                   | SELECT \* FROM user u JOIN orders o ON KEY o.user\_id FOR u;                                                                                                                       | SELECT \* FROM user u JOIN orders o ON META(u).id = o.user\_id;                                                                                                                                           |
| NEST                      | SELECT \* FROM user u NEST orders orders ON KEYS ARRAY s.order\_id FOR s IN u.order\_history END;                                                                                  | NEST/UNNEST not supported                                                                                                                                                                                 |
| LEFT OUTER NEST           | SELECT \* FROM user u LEFT OUTER NEST orders orders ON KEYS ARRAY s.order\_id FOR s IN u.order\_history END;                                                                       | NEST/UNNEST not supported                                                                                                                                                                                 |
| ARRAY                     | ARRAY i FOR i IN \[1, 2\] END                                                                                                                                                      | (SELECT VALUE i FROM \[1, 2\] AS i)                                                                                                                                                                       |
| ARRAY FIRST               | ARRAY FIRST arr                                                                                                                                                                    | arr\[0\]                                                                                                                                                                                                  |
| LIMIT l OFFSET o          | Allows OFFSET without LIMIT                                                                                                                                                        | Allows OFFSET without LIMIT                                                                                                                                                                               |
| UNION, INTERSECT, EXCEPT  | All three are supported (with ALL and DISTINCT variants).                                                                                                                          | Not supported                                                                                                                                                                                             |
| OUTER JOIN                | Both LEFT and RIGHT OUTER JOIN are supported.                                                                                                                                      | Only LEFT OUTER JOIN supported (and necessary for query expressability).                                                                                                                                  |
| <, <=, \=, etc. operators | Can compare either complex values or scalar values.                                                                                                                                | Only scalar values may be compared.                                                                                                                                                                       |
| ORDER BY                  | Result sequencing is based on specific rules described in [SQL++ for Server ORDER BY clause](https://docs.couchbase.com/server/current/n1ql/n1ql-language-reference/orderby.html). | Result sequencing is based on the SQLite ordering described in [SQLite select overview](https://sqlite.org/lang%5Fselect.html). The ordering of Dictionary and Array objects is based on binary ordering. |
| SELECT DISTINGCT          | Supported                                                                                                                                                                          | SELECT DISTINCT VALUE is supported when the returned values are scalars.                                                                                                                                  |
| CREATE INDEX              | Supported                                                                                                                                                                          | Not Supported                                                                                                                                                                                             |
| INSERT, UPSERT, DELETE    | Supported                                                                                                                                                                          | Not Supported                                                                                                                                                                                             |

## [](#boolean-logic-rules)Boolean Logic Rules

### [](#sql-for-server)SQL++ for Server

Couchbase Server operates in the same way as Couchbase Lite, except:

* `MISSING`, `NULL` and `FALSE` are `FALSE`
* Numbers `0` is `FALSE`
* Empty strings, arrays, and objects are `FALSE`
* All other values are `TRUE`

You can choose to use Couchbase Server's SQL++ rules by using the `TOBOOLEAN(expr)` function to convert a value to its boolean value.

### [](#sql-for-mobile)SQL++ for Mobile

SQL++ for Mobile's boolean logic rules are based on SQLite's, so:

* `TRUE` is `TRUE`, and `FALSE` is `FALSE`
* Numbers `0` or `0.0` are `FALSE`
* Arrays and dictionaries are `FALSE`
* String and Blob are `TRUE` if the values are casted as a non-zero or `FALSE`if the values are casted as `0` or `0.0` \- see: [SQLITE's CAST and Boolean expressions](https://sqlite.org/lang%5Fexpr.html) for more details.
* `NULL` is `FALSE`
* `MISSING` is `MISSING`

### [](#logical-operations)Logical Operations

In SQL++ for Mobile logical operations will return one of three possible values; `TRUE`, `FALSE`, or `MISSING`.

Logical operations with the `MISSING` value could result in `TRUE` or `FALSE` if the result can be determined regardless of the missing value, otherwise the result will be `MISSING`.

In SQL++ for Mobile - unlike SQL++ for Server - `NULL` is implicitly converted to `FALSE` before evaluating logical operations. [Table 2](#table-2-logical-operations-comparison) summarizes the result of logical operations with different operand values and also shows where the Couchbase Server behavior differs.

#### [](#table-2-logical-operations-comparison)Table 2\. Logical Operations Comparison

| Operanda | Operandb | SQL ++ for Mobilea AND b | SQL ++ for Mobilea OR b | SQL ++ for Servera AND b | SQL ++ for Servera OR b |
| -------- | -------- | ------------------------ | ----------------------- | ------------------------ | ----------------------- |
| TRUE     | TRUE     | TRUE                     | TRUE                    | \-                       | \-                      |
|          | FALSE    | FALSE                    | TRUE                    | \-                       | \-                      |
|          | NULL     | FALSE                    | TRUE                    | NULL                     | \-                      |
|          | MISSING  | MISSING                  | TRUE                    | \-                       | \-                      |
| FALSE    | TRUE     | FALSE                    | TRUE                    | \-                       | \-                      |
|          | FALSE    | FALSE                    | FALSE                   | \-                       | \-                      |
|          | NULL     | FALSE                    | FALSE                   | \-                       | NULL                    |
|          | MISSING  | FALSE                    | MISSING                 | \-                       | \-                      |
| NULL     | TRUE     | FALSE                    | TRUE                    | NULL                     | \-                      |
|          | FALSE    | FALSE                    | FALSE                   | \-                       | NULL                    |
|          | NULL     | FALSE                    | FALSE                   | NULL                     | NULL                    |
|          | MISSING  | FALSE                    | MISSING                 | MISSING                  | NULL                    |
| MISSING  | TRUE     | MISSING                  | TRUE                    | \-                       | \-                      |
|          | FALSE    | FALSE                    | MISSING                 | \-                       | \-                      |
|          | NULL     | FALSE                    | MISSING                 | MISSING                  | NULL                    |
|          | MISSING  | MISSING                  | MISSING                 | \-                       | \-                      |

## [](#crud-operations)CRUD Operations

* SQL++ for Mobile only supports Read or Query operations.
* SQL++ for Server fully supports CRUD operation.

## [](#functions)Functions

### [](#division-operator)Division Operator

| SQL ++ for Server                                                                                                                                                         | SQL++ for Mobile                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SQL++ for Server always performs float division regardless of the types of the operands. You can force this behavior in SQL++ for Mobile by using the DIV(x, y) function. | The operand types determine the division operation performed. If both are integers, integer division is used. If one is a floating number, then float division is used. |

### [](#round-function)Round Function

| SQL ++ for Server                                                                                                                                                                                | SQL++ for Mobile                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SQL++ for Server ROUND() uses the Rounding to Nearest Even convention (for example, ROUND(1.85) returns 1.8). You can force this behavior in Couchbase Lite by using the ROUND\_EVEN() function. | The ROUND() function returns a value to the given number of integer digits to the right of the decimal point (left if digits is negative). Digits are 0 if not given. Midpoint values are handled using the Rounding Away From Zero convention, which rounds them to the next number away from zero (for example, ROUND(1.85) returns 1.9). |