---
title: SQL for Mobile -- Differences from SQL for Server
description: Differences between Couchbase Server SQL++ and Couchbase Lite N1QL
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.2/modules/c/pages/query-n1ql-mobile-server-diffs.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.2@couchbase-lite:c:query-n1ql-mobile-server-diffs.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.2/c/query-n1ql-mobile-server-diffs.html)

# SQL for Mobile -- Differences from SQL for Server

> Description — _Differences between Couchbase Server SQL++ and Couchbase Lite N1QL_  
> Related Content — [Predictive Queries](#c:querybuilder.adoc#lbl-predquery) | [Live Queries](query-live.md) | [Indexing](indexing.md)

> [!IMPORTANT]
> N1QL is Couchbase's implementation of the developing **SQL++** standard. As such the terms _N1QL_ and _SQL++_ are used interchangeably in Couchbase documentation unless explicitly stated otherwise.

There are several minor but notable behavior differences between _SQL++ for Mobile_ queries and _SQL++ for Server_, as shown in [Table 1](#tbl-diffs).

In some instances, if required, you can force SQL++ for Mobile to work in the same way as SQL++ for Server. This table compares Couchbase Server and Mobile instances:

__Table 1\. SQL++ Query Comparison__
|                              | SQL++ Comparison                                                                                                                                           |                                                                                                                                                                                                              |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Feature                      | SQL++ for Couchbase Server                                                                                                                                 | SQL++ for Mobile                                                                                                                                                                                             |
| Scopes and Collections       | SELECT \*FROM \`travel-sample\`.inventory.airport                                                                                                          | SELECT \*FROM inventory.airport                                                                                                                                                                              |
| Scopes and Collections       | SELECT \*FROM \`travel-sample\`.inventory.airport                                                                                                          | SELECT \*FROM inventory.airport                                                                                                                                                                              |
| USE KEYS                     | SELECT fname, email FROM tutorial USE KEYS \["dave", "ian"\];                                                                                              | SELECT fname, email FROM tutorial WHERE meta().id IN ("dave", "ian");                                                                                                                                        |
| ON KEYS                      | SELECT \*FROM \`user\` uJOIN orders o ON KEYS ARRAY s.order\_idFOR s IN u.order\_history END;                                                              | SELECT \* FROM user u, u.order\_history sJOIN orders o ON s.order\_id = meta(o).id;                                                                                                                          |
| ON KEY                       | SELECT \*FROM \`user\` u JOIN orders o ON KEY o.user\_id FOR u;                                                                                            | SELECT \* FROM user uJOIN orders o ON meta(u).id = o.user\_id;                                                                                                                                               |
| NEST                         | SELECT \*FROM \`user\` u NEST orders orders ON KEYS ARRAY s.order\_id FOR s IN u.order\_history END;                                                       | NEST/UNNEST not supported                                                                                                                                                                                    |
| LEFT OUTER NEST              | SELECT \* FROM user uLEFT OUTER NEST orders ordersON KEYS ARRAY s.order\_id FOR s IN u.order\_history END;                                                 | NEST/UNNEST not supported                                                                                                                                                                                    |
| ARRAY                        | ARRAY i FOR i IN \[1, 2\] END                                                                                                                              | (SELECT VALUE i FROM \[1, 2\] AS i)                                                                                                                                                                          |
| ARRAY FIRST                  | ARRAY FIRST arr                                                                                                                                            | arr\[0\]                                                                                                                                                                                                     |
| LIMIT l OFFSET o             | Allows OFFSET without LIMIT                                                                                                                                | Allows OFFSET without LIMIT                                                                                                                                                                                  |
| UNION, INTERSECT, and EXCEPT | All three are supported (with ALL and DISTINCT variants)                                                                                                   | Not supported                                                                                                                                                                                                |
| OUTER JOIN                   | Both LEFT and RIGHT OUTER JOIN supported                                                                                                                   | Only LEFT OUTER JOIN supported (and necessary for query expressability)                                                                                                                                      |
| <, <=, =, etc. operators     | Can compare either complex values or scalar values                                                                                                         | Only scalar values may be compared                                                                                                                                                                           |
| ORDER BY                     | Result sequencing is based on specific rules described in [SQL++ (server) OrderBy clause](../../../server/current/n1ql/n1ql-language-reference/orderby.md) | Result sequencing is based on the SQLite ordering described in [SQLite select overview](https://sqlite.org/lang%5Fselect.html) The ordering of _Dictionary_ and _Array_ objects is based on binary ordering. |
| SELECT DISTINCT              | Supported                                                                                                                                                  | SELECT DISTINCT VALUE is supported when the returned values are scalars                                                                                                                                      |
| CREATE INDEX                 | Supported                                                                                                                                                  | Not Supported                                                                                                                                                                                                |
| INSERT/UPSERT/DELETE         | Supported                                                                                                                                                  | Not Supported                                                                                                                                                                                                |

## [](#boolean-logic-rules)Boolean Logic Rules

| SQL++ for Couchbase Server                                                                                                                                                                                                                                                                                                             | SQL++ for Mobile                                                                                                                                                                                                                                                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Couchbase Server operates in the same way as Couchbase Lite, except: MISSING, NULL and FALSE are FALSE Numbers 0 is FALSE Empty strings, arrays, and objects are FALSE All other values are TRUE You can choose to use _Couchbase Server's SQL++ rules_ by using the TOBOOLEAN(expr) function to convert a value to its boolean value. | SQL++ for Mobile's boolean logic rules are based on SQLite's, so: TRUE is TRUE, and FALSE is FALSE Numbers 0 or 0.0 are FALSE Arrays and dictionaries are FALSE String and Blob are TRUE if the values are casted as a non-zero or FALSE if the values are casted as 0 or 0.0 — see: [SQLITE's CAST and Boolean expressions](https://sqlite.org/lang%5Fexpr.html)^ for more details) NULL is FALSE MISSING is MISSING |

### [](#logical-operations)Logical Operations

In SQL++ for Mobile logical operations will return one of three possible values; `TRUE`, `FALSE`, or `MISSING`.

Logical operations with the `MISSING` value could result in `TRUE` or `FALSE` if the result can be determined regardless of the missing value, otherwise the result will be `MISSING`.

In SQL++ for Mobile — unlike SQL++ for Server — `NULL` is implicitly converted to `FALSE` before evaluating logical operations. [Table 2](#tbl-logops) summarizes the result of logical operations with different operand values and also shows where the Couchbase Server behavior differs.

__Table 2\. Logical Operations Comparison__
| Operanda | SQL++ for Mobile | SQL++ for Server |      |             |          |    |
| -------- | ---------------- | ---------------- | ---- | ----------- | -------- | -- |
| b        | a AND b          | a OR b           | b    | a AND b     | a OR b   |    |
| TRUE     | TRUE             | TRUE             | TRUE | \-          | \-       | \- |
| FALSE    | FALSE            | TRUE             | \-   | \-          | \-       |    |
| NULL     | FALSE            | TRUE             | \-   | **NULL**    | \-       |    |
| MISSING  | MISSING          | TRUE             | \-   | \-          | \-       |    |
| FALSE    | TRUE             | FALSE            | TRUE | \-          | \-       | \- |
| FALSE    | FALSE            | FALSE            | \-   | \-          | \-       |    |
| NULL     | FALSE            | FALSE            | \-   | \-          | **NULL** |    |
| MISSING  | FALSE            | MISSING          | \-   | \-          | \-       |    |
| NULL     | TRUE             | FALSE            | TRUE | \-          | **NULL** | \- |
| FALSE    | FALSE            | FALSE            | \-   | \-          | **NULL** |    |
| NULL     | FALSE            | FALSE            | \-   | **NULL**    | **NULL** |    |
| MISSING  | FALSE            | MISSING          | \-   | **MISSING** | **NULL** |    |
| MISSING  | TRUE             | MISSING          | TRUE | \-          | \-       | \- |
| FALSE    | FALSE            | MISSING          | \-   | \-          | \-       |    |
| NULL     | FALSE            | MISSING          | \-   | **MISSING** | **NULL** |    |
| MISSING  | MISSING          | MISSING          | \-   | \-          | \-       |    |

## [](#crud-operations)CRUD Operations

SQL++ for Mobile only supports Read or Query operations.

SQL++ for Server fully supports CRUD operation.

## [](#functions)Functions

### [](#division-operator)Division Operator

| SQL++ for Server                                                                                                                                                          | SQL++ for Mobile                                                                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SQL++ for Server always performs float division regardless of the types of the operands. You can force this behavior in SQL++ for Mobile by using the DIV(x, y) function. | The operand types determine the division operation performed.If both are integers, integer division is used.If one is a floating number, then float division is used. |

### [](#round-function)Round Function

| SQL++ for Server                                                                                                                                                                                   | SQL++ for Mobile                                                                                                                                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SQL++ for Server ROUND() uses the _Rounding to Nearest Even_ convention (for example, ROUND(1.85) returns 1.8). You can force this behavior in Couchbase Lite by using the ROUND\_EVEN() function. | The ROUND() function returns a value to the given number of integer digits to the right of the decimal point (left if digits is negative). Digits are 0 if not given. Midpoint values are handled using the _Rounding Away From Zero_ convention, which rounds them to the next number away from zero (for example, ROUND(1.85) returns 1.9). |

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Prerequisites](#c:gs-prereqs.adoc)
* [Install](gs-install.md)
* [Build and Run](gs-build.md)

.

###### [](#-2)

Learn more . . .

* [Databases](database.md)
* [Documents](document.md)
* [Blobs](blob.md)
* [Remote Sync Gateway](replication.md)
* [Handling Data Conflicts](conflict.md)

.

###### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.