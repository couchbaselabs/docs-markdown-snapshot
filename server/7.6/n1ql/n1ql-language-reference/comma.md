---
title: Comma-Separated Join
description: A comma-separated join enables you to produce new input objects by
  creating a Cartesian product of all the source objects.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/n1ql/pages/n1ql-language-reference/comma.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.6@server:n1ql:n1ql-language-reference/comma.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/n1ql/n1ql-language-reference/comma.html)

# Comma-Separated Join

> A comma-separated join enables you to produce new input objects by creating a Cartesian product of all the source objects. 

## [](#purpose)Purpose

A comma-separated join is used within the [FROM](from.md) clause. Like the [JOIN](join.md) clause, it creates an input object by combining two or more source objects. A comma-separated join can combine arbitrary fields from the source documents, and you can chain several comma-separated joins together.

The comma-separated join, by itself, does not specify a join predicate. This means that, in its basic form, the comma-separated join would produce all the possible combinations of the combined source objects — this is known as the _Cartesian product_.

In practice, it is common to use the query’s [WHERE](where.md) clause to specify a condition for the comma-separated join. Refer to the examples below for further details.

## [](#prerequisites)Prerequisites

For you to select data from keyspace or expression, you must have the `query_select` privilege on that keyspace. For more details about user roles, see [Authorization](../../learn/security/authorization-overview.md).

## [](#syntax)Syntax

```ebnf
comma-separated-join ::= ',' 'LATERAL'? ( rhs-keyspace | rhs-subquery | rhs-generic )
```

![Syntax diagram](../_images/n1ql-language-reference/comma-separated-join.png) 

| rhs-keyspace | [Right-Hand Side Keyspace](#rhs-keyspace)          |
| ------------ | -------------------------------------------------- |
| rhs-subquery | [Right-Hand Side Subquery](#rhs-subquery)          |
| rhs-generic  | [Right-Hand Side Generic Expression](#rhs-generic) |

### [](#from-term)Left-Hand Side

The comma-separated join cannot be the first term within the `FROM` clause; it must be preceded by another FROM term. The term immediately preceding the comma-separated join represents the _left-hand side_ of the comma-separated join.

You can chain the comma-separated join with any of the other permitted FROM terms, including another comma-separated join. For more information, see the page on the [FROM](from.md) clause.

There are restrictions on what types of FROM terms may be chained and in what order — see the descriptions on this page for more details.

The types of FROM term that may be used as the left-hand side of the comma-separated join are summarized in the following table.

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

| Type                                                              | Example                                                                                                                                                                                                                                                       |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [keyspace identifier](from.md#sec%5Ffrom-keyspace)                | hotel                                                                                                                                                                                                                                                         |
| [generic expression](from.md#generic-expr)                        | 20+10 AS Total                                                                                                                                                                                                                                                |
| [subquery](from.md#select-expr)                                   | SELECT ARRAY\_AGG(t1.city) AS cities,   SUM(t1.city\_cnt) AS apnum FROM (   SELECT city, city\_cnt, country,     ARRAY\_AGG(airportname) AS apnames   FROM airport   GROUP BY city, country   LETTING city\_cnt = COUNT(city) ) AS t1 WHERE t1.city\_cnt > 5; |
| previous [join](join.md), [nest](nest.md), or [unnest](unnest.md) | SELECT \* FROM route AS rte JOIN airport AS apt   ON rte.destinationairport = apt.faa NEST landmark AS lmk   ON apt.city = lmk.city LIMIT 5;                                                                                                                  |
| previous comma-separated join                                     | SELECT a.airportname, h.name AS hotel, l.name AS landmark FROM airport AS a,      hotel AS h,      landmark AS l WHERE a.city = h.city   AND h.city = l.city LIMIT 5;                                                                                         |

The comma-separated join is a type of inner join. For each joined object produced, both the left-hand side and right-hand side source objects must be non-MISSING and non-NULL.

The _right-hand side_ of a comma-separated join may be a keyspace reference, a subquery, or a generic expression term.

### [](#comma-join-lateral)LATERAL Join

_(Introduced in Couchbase Server 7.6)_

When an expression on the right-hand side of a comma-separated join references a keyspace that is already specified in the same FROM clause, the expression is said to be correlated. In relational databases, a join which contains correlated expressions is referred to as a lateral join. In SQL++, lateral correlations are detected automatically, and there is no need to specify that a join is lateral.

In Couchbase Server 7.6 and later, you can use the LATERAL keyword as a visual reminder that a join contains correlated expressions. The LATERAL keyword is not required — the keyword is included solely for compatibility with queries from relational databases.

If you use the LATERAL keyword in a join that has no lateral correlation, the keyword is ignored.

You can use the optional LATERAL keyword in front of the right-hand side keyspace of a comma-separated join.

> [!NOTE]
> Using the LATERAL keyword in a comma-separated join implies that the right-hand side of the join must appear after the left-hand side of the join. This may prevent the cost-based optimizer from reordering joins in the query to give the optimal join order. For details, see [Join Enumeration](cost-based-optimizer.md#join-enumeration).

### [](#rhs-keyspace)Right-Hand Side Keyspace

```ebnf
rhs-keyspace ::= keyspace-ref ( 'AS'? alias )? ansi-join-hints?
```

![Syntax diagram](../_images/n1ql-language-reference/rhs-keyspace.png) 

| keyspace-ref    | [Keyspace Reference](#rhs-keyspace-ref) |
| --------------- | --------------------------------------- |
| alias           | [AS Alias](#rhs-keyspace-alias)         |
| ansi-join-hints | [USE Clause](#rhs-keyspace-hints)       |

#### [](#rhs-keyspace-ref)Keyspace Reference

Keyspace reference for the right-hand side of the comma-separated join. For details, see [Keyspace Reference](from.md#from-keyspace-ref).

#### [](#rhs-keyspace-alias)AS Alias

Assigns another name to the keyspace reference. For details, see [AS Clause](from.md#section%5Fax5%5F2nx%5F1db).

Assigning an alias to the keyspace reference is optional. If you assign an alias to the keyspace reference, the `AS` keyword may be omitted.

#### [](#rhs-keyspace-hints)USE Clause

Enables you to specify that the join should use particular keys, a particular index, or a particular join method. For details, see [ANSI JOIN Hints](join.md#ansi-join-hints).

> [!TIP]
> You can also supply a join hint within a specially-formatted [hint comment](optimizer-hints.md). Note that you cannot specify a join hint for the same keyspace using both the `USE` clause and a hint comment. If you do this, the `USE` clause and the hint comment are both marked as erroneous and ignored by the optimizer.

### [](#rhs-subquery)Right-Hand Side Subquery

```ebnf
rhs-subquery ::= subquery-expr 'AS'? alias
```

![Syntax diagram](../_images/n1ql-language-reference/rhs-subquery.png) 

| subquery-expr | [Subquery Expression](#ansi-subquery-expr) |
| ------------- | ------------------------------------------ |
| alias         | [AS Alias](#ansi-subquery-alias)           |

#### [](#ansi-subquery-expr)Subquery Expression

Use parentheses to specify a subquery for the right-hand side of the comma-separated join. For details, see [Subquery Expression](from.md#select-expr-clause).

> [!NOTE]
> A subquery on the right-hand side of the comma-separated join cannot be **correlated**, i.e. it cannot refer to a keyspace in the outer query block. This will lead to an error.

#### [](#ansi-subquery-alias)AS Alias

Assigns another name to the subquery. For details, see [AS Clause](from.md#section%5Fax5%5F2nx%5F1db).

You must assign an alias to a subquery on the right-hand side of the join. However, when you assign an alias to the subquery, the `AS` keyword may be omitted.

### [](#rhs-generic)Right-Hand Side Generic Expression

```ebnf
rhs-generic ::= expr ( 'AS'? alias )?
```

![Syntax diagram](../_images/n1ql-language-reference/rhs-generic.png) 

| expr  | [Expression Term](#ansi-generic-expr) |
| ----- | ------------------------------------- |
| alias | [AS Alias](#ansi-generic-alias)       |

#### [](#ansi-generic-expr)Expression Term

A SQL++ [expression](index.md#N1QL%5FExpressions) generating JSON documents or objects for the right-hand side of the comma-separated join.

> [!NOTE]
> An expression on the right-hand side of the comma-separated join may be **correlated**, i.e. it may refer to a keyspace on the left-hand side of the join. In this case, only a [nested-loop join](#ansi-join-hints) may be used.

#### [](#ansi-generic-alias)AS Alias

Assigns another name to the generic expression. For details, see [AS Clause](from.md#section%5Fax5%5F2nx%5F1db).

You must assign an alias to the generic expression if it is not an identifier; otherwise, assigning an alias is optional. However, when you assign an alias to the generic expression, the `AS` keyword may be omitted.

## [](#limitations)Limitations

* You can chain comma-separated joins with ANSI `JOIN` clauses, ANSI `NEST` clauses, and `UNNEST` clauses. However, you cannot chain comma-separated joins with lookup `JOIN` and `NEST` clauses, or index `JOIN` and `NEST` clauses.
* The right-hand side of a comma-separated join can only be a keyspace identifier, a subquery, or a generic expression. This means that comma-separated joins must come _after_ any `JOIN`, `NEST`, or `UNNEST` clauses.

## [](#examples)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Example 1\. Cartesian product

The following query lists every possible combination of the two input objects.

Comma-separated join

```sqlpp
SELECT * FROM [{"abc": 1}, {"abc": 2}, {"abc": 3}] AS a,
              [{"xyz": 1}, {"xyz": 2}] AS b;
```

Compare the query above with the following query using an ANSI join.

ANSI join

```sqlpp
SELECT * FROM [{"abc": 1}, {"abc": 2}, {"abc": 3}] AS a
         JOIN [{"xyz": 1}, {"xyz": 2}] AS b ON true;
```

The results of the two queries are the same.

Results

```json
[
  {
    "a": {
      "abc": 1
    },
    "b": {
      "xyz": 1
    }
  },
  {
    "a": {
      "abc": 1
    },
    "b": {
      "xyz": 2
    }
  },
  {
    "a": {
      "abc": 2
    },
    "b": {
      "xyz": 1
    }
  },
  {
    "a": {
      "abc": 2
    },
    "b": {
      "xyz": 2
    }
  },
  {
    "a": {
      "abc": 3
    },
    "b": {
      "xyz": 1
    }
  },
  {
    "a": {
      "abc": 3
    },
    "b": {
      "xyz": 2
    }
  }
]
```

Example 2\. Comma-separated join condition

The following query uses the WHERE clause to define the condition for a comma-separated join.

Comma-separated join

```sqlpp
SELECT a.airportname AS airport, r.id AS route
FROM route AS r,
     airport AS a
WHERE a.faa = r.sourceairport
LIMIT 4;
```

Compare the query above with the following query using an ANSI join.

ANSI join

```sqlpp
SELECT a.airportname AS airport, r.id AS route
FROM route AS r
JOIN airport AS a
  ON a.faa = r.sourceairport
LIMIT 4;
```

The results of the two queries are the same.

Results

```json
[
  {
    "airport": "Lehigh Valley Intl",
    "route": 20010
  },
  {
    "airport": "Lehigh Valley Intl",
    "route": 20011
  },
  {
    "airport": "Lehigh Valley Intl",
    "route": 28856
  },
  {
    "airport": "Lehigh Valley Intl",
    "route": 28857
  }
]
```

Example 3\. Comma-separated join with filters

The following query uses the WHERE clause to define a condition for a comma-separated join and to filter the query.

Comma-separated join

```sqlpp
SELECT a.airportname AS airport, r.id AS route
FROM route AS r,
     airport AS a
WHERE a.faa = r.sourceairport
  AND r.sourceairport = "SFO"
LIMIT 4;
```

Compare the query above with the following query using an ANSI join.

ANSI join

```sqlpp
SELECT a.airportname AS airport, r.id AS route
FROM route AS r
JOIN airport AS a
  ON a.faa = r.sourceairport
WHERE r.sourceairport = "SFO"
LIMIT 4;
```

The results of the two queries are the same.

Results

```json
[
  {
    "airport": "San Francisco Intl",
    "route": 10624
  },
  {
    "airport": "San Francisco Intl",
    "route": 10625
  },
  {
    "airport": "San Francisco Intl",
    "route": 11212
  },
  {
    "airport": "San Francisco Intl",
    "route": 11213
  }
]
```

Example 4\. Comma-separated join with hints

The following query uses the USE clause to specify hints for a comma-separated join.

Comma-separated join

```sqlpp
EXPLAIN SELECT a.airportname AS airport, r.id AS route
FROM route AS r,
     airport AS a
     USE INDEX(def_inventory_airport_faa) NL
WHERE a.faa = r.sourceairport
  AND r.sourceairport = "SFO"
LIMIT 4;
```

Compare the query above with the following query using an ANSI join.

ANSI join

```sqlpp
EXPLAIN SELECT a.airportname AS airport, r.id AS route
FROM route AS r
JOIN airport AS a
 USE INDEX(def_inventory_airport_faa) NL
  ON a.faa = r.sourceairport
WHERE r.sourceairport = "SFO"
LIMIT 4;
```

The results of the two queries are the same.

Results

```json
[
  {
    "optimizer_hints": {
      "hints_followed": [
        "USE_NL(a)",
        "INDEX(a def_inventory_airport_faa)"
      ]
    },
    // ...
  }
]
```

Example 5\. Chaining ANSI joins with comma-separated joins

The following query chains an ANSI join with a comma-separated join.

Query

```sqlpp
SELECT l.name AS airline, a.airportname AS airport, r.id AS route
FROM airline AS l
JOIN route AS r
  ON META(l).id = r.airlineid,
     airport AS a
WHERE a.faa = r.sourceairport
  AND r.sourceairport = "SFO"
LIMIT 4;
```

Results

```json
[
  {
    "airline": "AirTran Airways",
    "airport": "San Francisco Intl",
    "route": 25480
  },
  {
    "airline": "AirTran Airways",
    "airport": "San Francisco Intl",
    "route": 25481
  },
  {
    "airline": "AirTran Airways",
    "airport": "San Francisco Intl",
    "route": 25482
  },
  {
    "airline": "AirTran Airways",
    "airport": "San Francisco Intl",
    "route": 25483
  }
]
```

Example 6\. Lateral correlation

The following query has a lateral correlation between the subquery and the `airport` keyspace.

Comma-separated join

```sqlpp
SELECT airport.airportname, t2.name
FROM airport,
(SELECT name FROM hotel WHERE hotel.city = airport.city) AS t2
LIMIT 5;
```

Compare the query above with the following query using the LATERAL keyword.

Comma-separated join with LATERAL keyword

```sqlpp
SELECT airport.airportname, t2.name
FROM airport,
LATERAL (SELECT name FROM hotel WHERE hotel.city = airport.city) AS t2
LIMIT 5;
```

The results of the two queries are the same.

Results

```json
[
  {
    "airportname": "Mandelieu",
    "name": "Hotel Cybelle"
  },
  {
    "airportname": "Cote D\\'Azur",
    "name": "Best Western Hotel Riviera Nice"
  },
  {
    "airportname": "Cote D\\'Azur",
    "name": "Hotel Anis"
  },
  {
    "airportname": "Cote D\\'Azur",
    "name": "NH Nice"
  },
  {
    "airportname": "Cote D\\'Azur",
    "name": "Hotel Suisse"
  }
]
```