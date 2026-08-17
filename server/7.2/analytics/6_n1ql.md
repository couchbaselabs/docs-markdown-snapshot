---
title: SQL++ for Analytics vs. SQL++ for Query
description: A comparison between SQL++ for Analytics and SQL++ for Query.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-analytics/edit/release/7.2/modules/analytics/pages/6_n1ql.adoc
  xref: xref:7.2@server:analytics:6_n1ql.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/analytics/6_n1ql.html)

# SQL++ for Analytics vs. SQL++ for Query

SQL++ for Analytics offers the following key advancements beyond SQL++ for Query:

* WITH: SQL++ for Analytics supports the ANSI SQL WITH clause to allow the definition of inlined views or variables of primitive types to simplify complex query construction.
* JOIN: SQL++ for Analytics supports the ANSI join syntax and allows joins on any condition expressions over Analytics collections, arrays, or subqueries.
* GROUP BY: In SQL++ for Analytics, in addition to a set of aggregate functions as in standard SQL, the groups created by the `GROUP BY` clause are directly usable in nested queries and/or to obtain nested results.
* Subquery: Any valid SQL++ for Analytics query can be used as a subquery.

For SQL++ for Query users, the following matrix is a quick compatibility cheat sheet for SQL++ for Analytics.

| Feature                      | SQL++ for Query                                                                                            | SQL++ for Analytics Equivalent                                                                                                                |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| USE KEYS                     | SELECT fname, email FROM tutorial USE KEYS \["dave", "ian"\];                                              | SELECT fname, email FROM tutorial WHERE meta().id IN \["dave", "ian"\];                                                                       |
| ON KEYS                      | SELECT \* FROM user uJOIN orders o ON KEYS ARRAY s.order\_id FOR s IN u.order\_history END;                | SELECT \* FROM user u, u.order\_history sJOIN orders o ON s.order\_id = meta(o).id;                                                           |
| ON KEY                       | SELECT \* FROM user uJOIN orders o ON KEY o.user\_id FOR u;                                                | SELECT \* FROM user uJOIN orders o ON meta(u).id = o.user\_id;                                                                                |
| NEST                         | SELECT \* FROM user uNEST orders ordersON KEYS ARRAY s.order\_id FOR s IN u.order\_history END;            | SELECT u, orders FROM users uLET orders=(SELECT VALUE o FROM u.order\_history s, orders o WHERE meta(o).id = s.order\_id)WHERE EXISTS orders; |
| LEFT OUTER NEST              | SELECT \* FROM user uLEFT OUTER NEST orders ordersON KEYS ARRAY s.order\_id FOR s IN u.order\_history END; | SELECT u, (SELECT VALUE o FROM u.order\_history s, orders o WHERE meta(o).id = s.order\_id) ordersFROM users u;                               |
| ARRAY                        | ARRAY i FOR i IN \[1, 2\] END                                                                              | (SELECT VALUE i FROM \[1, 2\] AS i)                                                                                                           |
| ARRAY FIRST                  | ARRAY FIRST arr                                                                                            | arr\[0\]                                                                                                                                      |
| LIMIT l OFFSET o             | Allows OFFSET without LIMIT                                                                                | Doesn't support OFFSET without LIMIT                                                                                                          |
| UNION, INTERSECT, and EXCEPT | All three are supported (with ALL and DISTINCT variants)                                                   | Only UNION ALL is supported (and necessary for query expressibility)                                                                          |
| <, <=, =, etc. operators     | Can compare either complex values or scalar values                                                         | Only scalar values may be compared                                                                                                            |
| ORDER BY                     | Can order by complex values or scalar values                                                               | Can only order by scalar values                                                                                                               |
| SELECT DISTINCT              | Supported                                                                                                  | SELECT DISTINCT VALUE is supported when the returned values are scalars                                                                       |
| CREATE INDEX                 | Supported                                                                                                  | Supported but different (e.g., typed)                                                                                                         |
| INSERT/UPSERT/DELETE         | Supported                                                                                                  | Unsupported (by design)                                                                                                                       |

SQL++ for Analytics generalizes SQL++ for Query's syntax constructs such as `USE KEYS`, `ON KEYS`, `ON KEY`, `NEST`, `LEFT OUTER NEST` and `ARRAY` and thus eliminates cases where must-be-indexed or must-use-keys restrictions are required for certain SQL++ for Query queries or expressions to be acceptable. In addition, the general composability of SQL++ for Analytics queries eliminates the need for some of SQL++ for Query's special syntax; for example, SQL++ for Analytics does not require or support the IN/WITHIN subclauses of SQL++ for Query's existential (SOME, ANY, or EVERY) expressions.

Note that INSERT/UPSERT/DELETE are not supported at all in the Couchbase Analytics Service. Data is mutated in Couchbase Server, using the Couchbase Server SDK or SQL++ for Query mutation, and the mutations will then be automatically synchronized into the Couchbase Analytics Service.