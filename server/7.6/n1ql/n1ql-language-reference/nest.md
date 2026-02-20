---
title: NEST Clause
description: The NEST clause creates an input object by producing a single
  result of nesting keyspaces.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/n1ql/pages/n1ql-language-reference/nest.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.6@server:n1ql:n1ql-language-reference/nest.adoc[]
---

[View original HTML](/server/7.6/n1ql/n1ql-language-reference/nest.html)

# NEST Clause

> The `NEST` clause creates an input object by producing a single result of nesting keyspaces. 

## [](#purpose)Purpose

The `NEST` clause is used within the [FROM](from.md) clause. It enables you to create an input object by producing a single result of nesting keyspaces via [ANSI NEST](#section%5Ftc1%5Fnnx%5F1db), [Lookup NEST](#nest), or [Index NEST](#section%5Frgr%5Frnx%5F1db).

## [](#prerequisites)Prerequisites

For you to select data from keyspace or expression, you must have the `query_select` privilege on that keyspace. For more details about user roles, see [Authorization](../../learn/security/authorization-overview.md).

## [](#syntax)Syntax

```ebnf
nest-clause ::= ansi-nest-clause | lookup-nest-clause | index-nest-clause
```

![Syntax diagram](../_images/n1ql-language-reference/nest-clause.png) 

| ansi-nest-clause   | [ANSI NEST Clause](#section%5Ftc1%5Fnnx%5F1db)  |
| ------------------ | ----------------------------------------------- |
| lookup-nest-clause | [Lookup NEST Clause](#nest)                     |
| index-nest-clause  | [Index NEST Clause](#section%5Frgr%5Frnx%5F1db) |

### [](#from-term)Left-Hand Side

The `NEST` clause cannot be the first term within the `FROM` clause; it must be preceded by another FROM term. The term immediately preceding the `NEST` clause represents the _left-hand side_ of the `NEST` clause.

You can chain the `NEST` clause with any of the other permitted FROM terms, including another `NEST` clause. For more information, see the page on the [FROM](from.md) clause.

There are restrictions on what types of FROM terms may be chained and in what order — see the descriptions on this page for more details.

The types of FROM term that may be used as the left-hand side of the `NEST` clause are summarized in the following table.

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

| Type                                                        | Example                                                                                                                                                                                                                                                       |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [keyspace identifier](from.md#sec%5Ffrom-keyspace)          | hotel                                                                                                                                                                                                                                                         |
| [generic expression](from.md#generic-expr)                  | 20+10 AS Total                                                                                                                                                                                                                                                |
| [subquery](from.md#select-expr)                             | SELECT ARRAY\_AGG(t1.city) AS cities,   SUM(t1.city\_cnt) AS apnum FROM (   SELECT city, city\_cnt, country,     ARRAY\_AGG(airportname) AS apnames   FROM airport   GROUP BY city, country   LETTING city\_cnt = COUNT(city) ) AS t1 WHERE t1.city\_cnt > 5; |
| previous [join](join.md), [nest](#), or [unnest](unnest.md) | SELECT \* FROM route AS rte JOIN airport AS apt   ON rte.destinationairport = apt.faa NEST landmark AS lmk   ON apt.city = lmk.city LIMIT 5;                                                                                                                  |

## [](#section%5Ftc1%5Fnnx%5F1db)ANSI NEST Clause

> [!NOTE]
> [ANSI JOIN](join.md#section%5Fek1%5Fjnx%5F1db) and [ANSI NEST](#section%5Ftc1%5Fnnx%5F1db) clauses have much more flexible functionality than their earlier INDEX and LOOKUP equivalents. Since these are standard compliant and more flexible, we recommend you to use ANSI JOIN and ANSI NEST exclusively, where possible.

ANSI NEST supports more nest types than Lookup NEST or Index NEXT. ANSI NEST can nest arbitrary fields of the documents, and can be chained together.

The key difference between ANSI NEST and other supported NEST types is the replacement of the `ON KEYS` or `ON KEY … FOR` clauses with a simple `ON` clause. The `ON KEYS` or `ON KEY … FOR` clauses dictate that those nests can only be done on a document key (primary key for a document). The `ON` clause can contain any expression, and thus it opens up many more nest possibilities.

### [](#syntax-2)Syntax

```ebnf
ansi-nest-clause ::= ansi-nest-type? 'NEST' 'LATERAL'? ansi-nest-rhs ansi-nest-predicate
```

![Syntax diagram](../_images/n1ql-language-reference/ansi-nest-clause.png) 

| ansi-nest-type      | [Nest Type](#ansi-nest-type)           |
| ------------------- | -------------------------------------- |
| ansi-nest-lateral   | [LATERAL Nest](#ansi-nest-lateral)     |
| ansi-nest-rhs       | [Nest Right-Hand Side](#ansi-nest-rhs) |
| ansi-nest-predicate | [Nest Predicate](#ansi-nest-predicate) |

#### [](#ansi-nest-type)Nest Type

```ebnf
ansi-nest-type ::= 'INNER' | ( 'LEFT' 'OUTER'? )
```

![Syntax diagram](../_images/n1ql-language-reference/ansi-nest-type.png) 

This clause represents the type of ANSI nest.

`INNER`

For each nested object produced, both the left-hand and right-hand source objects must be non-MISSING and non-NULL.

`LEFT [OUTER]`

\[Query Service interprets `LEFT` as `LEFT OUTER`\]

For each nested object produced, only the left-hand source objects must be non-MISSING and non-NULL.

This clause is optional. If omitted, the default is `INNER`.

#### [](#ansi-nest-lateral)LATERAL Nest

_(Introduced in Couchbase Server 7.6)_

When an expression on the right-hand side of an ANSI nest references a keyspace that is already specified in the same FROM clause, the expression is said to be correlated. In relational databases, a join which contains correlated expressions is referred to as a lateral join. In SQL++, lateral correlations are detected automatically, and there is no need to specify that a nest or join is lateral.

In Couchbase Server 7.6 and later, you can use the LATERAL keyword as a visual reminder that a nest contains correlated expressions. The LATERAL keyword is not required — the keyword is included solely for compatibility with queries from relational databases.

If you use the LATERAL keyword in a nest that has no lateral correlation, the keyword is ignored.

INNER NEST and LEFT OUTER NEST support the optional LATERAL keyword in front of the right-hand side keyspace.

#### [](#ansi-nest-rhs)Nest Right-Hand Side

```ebnf
ansi-nest-rhs ::= keyspace-ref ( 'AS'? alias )?
```

![Syntax diagram](../_images/n1ql-language-reference/ansi-nest-rhs.png) 

| keyspace-ref | [Keyspace Reference](#ansi-keyspace-ref) |
| ------------ | ---------------------------------------- |
| alias        | [AS Alias](#ansi-as-alias)               |

##### [](#ansi-keyspace-ref)Keyspace Reference

Keyspace reference or expression representing the right-hand side of the NEST clause. For details, see [Keyspace Reference](from.md#from-keyspace-ref).

##### [](#ansi-as-alias)AS Alias

Assigns another name to the right-hand side of the NEST clause. For details, see [AS Clause](from.md#section%5Fax5%5F2nx%5F1db).

Assigning an alias to the keyspace reference is optional. If you assign an alias to the keyspace reference, the `AS` keyword may be omitted.

#### [](#ansi-nest-predicate)Nest Predicate

```ebnf
ansi-nest-predicate ::= 'ON' expr
```

![Syntax diagram](../_images/n1ql-language-reference/ansi-nest-predicate.png) 

`expr`

Boolean expression representing the nest condition between the left-hand side [FROM term](#from-term) and the right-hand side [Keyspace Reference](#ansi-keyspace-ref). This expression may contain fields, constant expressions, or any complex SQL++ expression.

### [](#limitations)Limitations

* Full OUTER nest and cross nest types are currently not supported.
* No mixing of ANSI nest syntax with lookup or index nest syntax in the same FROM clause.
* The right-hand-side of any nest must be a keyspace. Expressions, subqueries, or other join combinations cannot be on the right-hand-side of a nest.
* A nest can only be executed when appropriate index exists on the inner side of the ANSI nest.
* Adaptive indexes are not considered when selecting indexes on inner side of the nest.
* You may chain ANSI nests with comma-separated joins; however, the comma-separated joins must come after any JOIN, NEST, or UNNEST clauses.

### [](#examples)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Example 1\. Inner ANSI NEST

List only airports in Toulouse which have routes starting from them, and nest details of the routes.

Query

```sqlpp
SELECT *
FROM airport a
  INNER NEST route r
  ON a.faa = r.sourceairport
WHERE a.city = "Toulouse"
ORDER BY a.airportname;
```

Results

```JSON
[
  {
    "a": {
      "airportname": "Blagnac",
      "city": "Toulouse",
      "country": "France",
      "faa": "TLS",
      "geo": {
        "alt": 499,
        "lat": 43.629075,
        "lon": 1.363819
      },
      "icao": "LFBO",
      "id": 1273,
      "type": "airport",
      "tz": "Europe/Paris"
    },
    "r": [
      {
        "airline": "AH",
        "airlineid": "airline_794",
        "destinationairport": "ALG",
        "distance": 787.299015326995,
        "equipment": "736",
        "id": 10265,
// ...
      },
      {
        "airline": "AH",
        "airlineid": "airline_794",
        "destinationairport": "ORN",
        "distance": 906.1483088609814,
        "equipment": "736",
        "id": 10266,
// ...
    ]
  }
]
```

Example 2\. Inner LATERAL NEST

This example is the same as [Example 1](#ANSI-NEST-Example-1), but it includes the optional LATERAL keyword.

Query

```sqlpp
SELECT *
FROM airport a
  NEST LATERAL (
    SELECT r1.* FROM route r1
    WHERE a.faa = r1.sourceairport
  ) AS r
  ON true
WHERE a.city = "Toulouse"
ORDER BY a.airportname;
```

Results

```JSON
[
  {
    "a": {
      "id": 1273,
      "type": "airport",
      "airportname": "Blagnac",
      "city": "Toulouse",
      "country": "France",
      "faa": "TLS",
      "icao": "LFBO",
      "tz": "Europe/Paris",
      "geo": {
        "lat": 43.629075,
        "lon": 1.363819,
        "alt": 499
      }
    },
    "r": [
      {
        "airline": "AH",
        "airlineid": "airline_794",
        "destinationairport": "ALG",
        "distance": 787.299015326995,
        "equipment": "736",
        "id": 10265,
  // ...
```

Example 3\. Left Outer ANSI NEST

List all airports in Toulouse, and nest details of any routes that start from each airport.

Query

```sqlpp
SELECT *
FROM airport a
  LEFT NEST route r
  ON a.faa = r.sourceairport
WHERE a.city = "Toulouse"
ORDER BY a.airportname;
```

Results

```JSON
[
  {
    "a": {
      "airportname": "Blagnac",
      "city": "Toulouse",
      "country": "France",
      "faa": "TLS",
      "geo": {
        "alt": 499,
        "lat": 43.629075,
        "lon": 1.363819
      },
      "icao": "LFBO",
      "id": 1273,
      "type": "airport",
      "tz": "Europe/Paris"
    },
    "r": [
      {
        "airline": "AH",
        "airlineid": "airline_794",
        "destinationairport": "ALG",
        "distance": 787.299015326995,
        "equipment": "736",
        "id": 10265,
// ...
      }
    ]
  },
  {
    "a": {
      "airportname": "Francazal",
      "city": "Toulouse",
      "country": "France",
      "faa": null,
      "geo": {
        "alt": 535,
        "lat": 43.545555,
        "lon": 1.3675
      },
      "icao": "LFBF",
      "id": 1266,
      "type": "airport",
      "tz": "Europe/Paris"
    },
    "r": [] (1)
  },
  {
    "a": {
      "airportname": "Lasbordes",
      "city": "Toulouse",
      "country": "France",
      "faa": null,
      "geo": {
        "alt": 459,
        "lat": 43.586113,
        "lon": 1.499167
      },
      "icao": "LFCL",
      "id": 1286,
      "type": "airport",
      "tz": "Europe/Paris"
    },
    "r": []
  }
]
```

| **1** | The LEFT OUTER NEST lists all the left-side results, even if there are no matching right-side documents, as indicated by the results in which the fields from the route keyspace are null or missing. |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#nest)Lookup NEST Clause

Nesting is conceptually the inverse of unnesting. Nesting performs a join across two keyspaces. But instead of producing a cross-product of the left and right inputs, a single result is produced for each left input, while the corresponding right inputs are collected into an array and nested as a single array-valued field in the result object.

### [](#syntax-3)Syntax

```ebnf
lookup-nest-clause ::= lookup-nest-type? 'NEST' lookup-nest-rhs lookup-nest-predicate
```

![Syntax diagram](../_images/n1ql-language-reference/lookup-nest-clause.png) 

| lookup-nest-type      | [Nest Type](#lookup-nest-type)           |
| --------------------- | ---------------------------------------- |
| lookup-nest-rhs       | [Nest Right-Hand Side](#lookup-nest-rhs) |
| lookup-nest-predicate | [Nest Predicate](#lookup-nest-predicate) |

#### [](#lookup-nest-type)Nest Type

```ebnf
lookup-nest-type ::= 'INNER' | ( 'LEFT' 'OUTER'? )
```

![Syntax diagram](../_images/n1ql-language-reference/lookup-nest-type.png) 

This clause represents the type of lookup nest.

`INNER`

For each result object produced, both the left-hand and right-hand source objects must be non-`MISSING` and non-`NULL`.

`LEFT [OUTER]`

\[Query Service interprets `LEFT` as `LEFT OUTER`\]

A left-outer unnest is performed, and at least one result object is produced for each left source object.

For each joined object produced, only the left-hand source objects must be non-`MISSING` and non-`NULL`.

This clause is optional. If omitted, the default is `INNER`.

#### [](#lookup-nest-rhs)Nest Right-Hand Side

```ebnf
lookup-nest-rhs ::= keyspace-ref ( 'AS'? alias )?
```

![Syntax diagram](../_images/n1ql-language-reference/lookup-nest-rhs.png) 

| keyspace-ref | [Keyspace Reference](#lookup-keyspace-ref) |
| ------------ | ------------------------------------------ |
| alias        | [AS Alias](#lookup-as-alias)               |

##### [](#lookup-keyspace-ref)Keyspace Reference

Keyspace reference for the right-hand side of the lookup nest. For details, see [Keyspace Reference](from.md#from-keyspace-ref).

##### [](#lookup-as-alias)AS Alias

Assigns another name to the right-hand side of the lookup nest. For details, see [AS Clause](from.md#section%5Fax5%5F2nx%5F1db).

Assigning an alias to the keyspace reference is optional. If you assign an alias to the keyspace reference, the `AS` keyword may be omitted.

#### [](#lookup-nest-predicate)Nest Predicate

```ebnf
lookup-nest-predicate ::= 'ON' 'KEYS' expr
```

![Syntax diagram](../_images/n1ql-language-reference/lookup-nest-predicate.png) 

The `ON KEYS` expression produces a document key or array of document keys for the right-hand side of the lookup nest.

expr

\[Required\] String or expression representing the primary keys of the documents for the right-hand side keyspace.

### [](#return-values)Return Values

If the right-hand source object is NULL, MISSING, empty, or a non-array value, then the result object’s right-side value is MISSING (omitted).

Nests can be chained with other NEST, JOIN, and UNNEST clauses. By default, an INNER NEST is performed. This means that for each result object produced, both the left and right source objects must be non-missing and non-null. The right-hand side result of NEST is always an array or MISSING. If there is no matching right source object, then the right source object is as follows:

| If the ON KEYS expression evaluates to | Then the right-side value is |
| -------------------------------------- | ---------------------------- |
| MISSING                                | MISSING                      |
| NULL                                   | MISSING                      |
| an array                               | an empty array               |
| a non-array value                      | an empty array               |

### [](#limitations-2)Limitations

Lookup nests can be chained with other lookup joins or nests and index joins or nests, but they cannot be mixed with ANSI joins, ANSI nests, or comma-separated joins.

### [](#examples-2)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Example 4\. Join two keyspaces producing an output for each left input

Show one set of routes for one airline in the `airline` keyspace.

Query

```sqlpp
SELECT *
FROM route
  INNER NEST airline
  ON KEYS route.airlineid
LIMIT 1;
```

Results

```JSON
[
  {
    "airline": [
      {
        "callsign": "AIRFRANS",
        "country": "France",
        "iata": "AF",
        "icao": "AFR",
        "id": 137,
        "name": "Air France",
        "type": "airline"
      }
    ],
    "route": {
      "airline": "AF",
      "airlineid": "airline_137",
      "destinationairport": "MRS",
      "distance": 2881.617376098415,
      "equipment": "320",
      "id": 10000,
      "schedule": [
// ...
      ],
      "sourceairport": "TLV",
      "stops": 0,
      "type": "route"
    }
  }
]
```

## [](#section%5Frgr%5Frnx%5F1db)Index NEST Clause

Index NESTs allow you to flip the direction of a Lookup NEST clause. Index NESTs can be used efficiently when Lookup NESTs cannot efficiently nest left-hand side documents with right-to-left nests, and your situation cannot be flipped because your predicate needs to be on the left-hand side, such as [Example 4](#Lookup-NEST-Example-1) above where airline documents have no reference to route documents.

> [!NOTE]
> For index nests, the syntax uses `ON KEY` (singular) instead of `ON KEYS` (plural). This is because an Index NEST’s `ON KEY` expression must produce a scalar value; whereas a Lookup NEST’s `ON KEYS` expression can produce either a scalar or an array value.

### [](#syntax-4)Syntax

```ebnf
index-nest-clause ::= index-nest-type? 'NEST' index-nest-rhs index-nest-predicate
```

![Syntax diagram](../_images/n1ql-language-reference/index-nest-clause.png) 

| index-nest-type      | [Nest Type](#index-nest-type)           |
| -------------------- | --------------------------------------- |
| index-nest-rhs       | [Nest Right-Hand Side](#index-nest-rhs) |
| index-nest-predicate | [Nest Predicate](#index-nest-predicate) |

#### [](#index-nest-type)Nest Type

```ebnf
index-nest-type ::= 'INNER' | ( 'LEFT' 'OUTER'? )
```

![Syntax diagram](../_images/n1ql-language-reference/index-nest-type.png) 

This clause represents the type of index nest.

`INNER`

For each nested object produced, both the left-hand and right-hand source objects must be non-MISSING and non-NULL.

`LEFT [OUTER]`

\[Query Service interprets `LEFT` as `LEFT OUTER`\]

For each nested object produced, only the left-hand source objects must be non-MISSING and non-NULL.

This clause is optional. If omitted, the default is `INNER`.

#### [](#index-nest-rhs)Nest Right-Hand Side

```ebnf
index-nest-rhs ::= keyspace-ref ( 'AS'? alias )?
```

![Syntax diagram](../_images/n1ql-language-reference/index-nest-rhs.png) 

| keyspace-ref | [Keyspace Reference](#index-keyspace-ref) |
| ------------ | ----------------------------------------- |
| alias        | [AS Alias](#index-as-alias)               |

##### [](#index-keyspace-ref)Keyspace Reference

Keyspace reference or expression representing the right-hand side of the NEST clause. For details, see [Keyspace Reference](from.md#from-keyspace-ref).

##### [](#index-as-alias)AS Alias

Assigns another name to the right-hand side of the NEST clause. For details, see [AS Clause](from.md#section%5Fax5%5F2nx%5F1db).

Assigning an alias to the keyspace reference is optional. If you assign an alias to the keyspace reference, the `AS` keyword may be omitted.

#### [](#index-nest-predicate)Nest Predicate

```ebnf
index-nest-predicate ::= 'ON' 'KEY' expr 'FOR' alias
```

![Syntax diagram](../_images/n1ql-language-reference/index-nest-predicate.png) 

`expr`

Expression in the form `_rhs-expression_._lhs-expression-key_`:

`_rhs-expression_`

Keyspace reference for the right-hand side of the index nest.

`_lhs-expression-key_`

String or expression representing the attribute in `_rhs-expression_` and referencing the document key for `alias`.

`alias`

Keyspace reference for the left-hand side of the index nest.

### [](#limitations-3)Limitations

Index nests can be chained with other index joins or nests and lookup joins or nests, but they cannot be mixed with ANSI joins, ANSI nests, or comma-separated joins.

### [](#examples-3)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Example 5\. Use INDEX nest to flip the direction of [Example 4](#Lookup-NEST-Example-1) above

This example nests the airline routes for each airline after creating the following index. (Note that the index will not match if it contains a WHERE clause.)

Index

```sqlpp
CREATE INDEX route_airlineid ON route(airlineid);
```

Query

```sqlpp
SELECT *
FROM airline aline
  INNER NEST route rte
  ON KEY rte.airlineid FOR aline
LIMIT 1;
```

Results

```JSON
[
  {
    "aline": {
      "callsign": "MILE-AIR",
      "country": "United States",
      "iata": "Q5",
      "icao": "MLA",
      "id": 10,
      "name": "40-Mile Air",
      "type": "airline"
    },
    "rte": [
      {
        "airline": "Q5",
        "airlineid": "airline_10",
        "destinationairport": "FAI",
        "distance": 118.20183585107631,
        "equipment": "CNA",
        "id": 46587,
        "schedule": [
// ...
        ],
        "sourceairport": "HKB",
        "stops": 0,
        "type": "route"
      },
      {
        "airline": "Q5",
        "airlineid": "airline_10",
        "destinationairport": "HKB",
        "distance": 118.20183585107631,
        "equipment": "CNA",
        "id": 46586,
        "schedule": [
// ...
        ],
        "sourceairport": "FAI",
        "stops": 0,
        "type": "route"
      }
    ]
  }
]
```

If you generalize the same query, it looks like the following:

CREATE INDEX _on-key-for-index-name_ _rhs-expression_ (_lhs-expression-key_);

SELECT _projection-list_
FROM _lhs-expression_
  NEST _rhs-expression_
  ON KEY _rhs-expression_._lhs-expression-key_ FOR _lhs-expression_
[ WHERE _predicates_ ] ;

There are three important changes in the index scan syntax example above:

* `CREATE INDEX` on the `ON KEY` expression `rte.airlineid` to access `route` documents using `airlineid` (which are produced on the left-hand side).
* The `ON KEY rte.airlineid FOR aline` enables SQL++ to use the index `route_airlineid`.
* Create any optional index, such as `route_airline`, that can be used on `airline` (left-hand side).

## [](#as)Appendix: Summary of NEST Types

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

### [](#ansi)ANSI

| **Left-Hand Side (lhs)**  | Any field or expression that produces a value that will be matched on the right-hand side. |
| ------------------------- | ------------------------------------------------------------------------------------------ |
| **Right-Hand Side (rhs)** | Anything that can have a proper index on the join expression.                              |
| **Syntax**                | _lhs-expr_ NEST _rhs-keyspace_ ON _any nest condition_                                     |
| **Example**               | SELECT \* FROM route r NEST airline a ON r.airlineid = META(a).id LIMIT 4;                 |

### [](#lookup)Lookup

| **Left-Hand Side (lhs)**  | Must produce a Document Key for the right-hand side.               |
| ------------------------- | ------------------------------------------------------------------ |
| **Right-Hand Side (rhs)** | Must have a Document Key.                                          |
| **Syntax**                | _lhs-expr_ NEST _rhs-keyspace_ ON KEYS _lhs-expr.foreign\_key_     |
| **Example**               | SELECT \* FROM route r NEST airline a ON KEYS r.airlineid LIMIT 4; |

### [](#index)Index

| **Left-Hand Side (lhs)**  | Must produce a key for the right-hand side index.                                                        |
| ------------------------- | -------------------------------------------------------------------------------------------------------- |
| **Right-Hand Side (rhs)** | Must have a proper index on the field or expression that maps to the Document Key of the left-hand side. |
| **Syntax**                | _lhs-keyspace_ NEST _rhs-keyspace_ ON KEY _rhs-kspace.idx\_key_ FOR _lhs-keyspace_                       |
| **Example**               | SELECT \* FROM airline a NEST route r ON KEY r.airlineid FOR a LIMIT 4;                                  |