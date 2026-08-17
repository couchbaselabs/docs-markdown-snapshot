---
title: Window Functions
description: Window functions are used to compute cumulative, moving, and
  reporting aggregations.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/n1ql/pages/n1ql-language-reference/windowfun.adoc
  xref: xref:7.6@server:n1ql:n1ql-language-reference/windowfun.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/n1ql/n1ql-language-reference/windowfun.html)

# Window Functions

> Window functions are used to compute cumulative, moving, and reporting aggregations. 

Window functions are used to compute an aggregate or cumulative value, based on a group of objects. The objects are not grouped into a single output object — each object remains separate in the query output.

All window functions must have a window definition. This divides the query result set into one or more partitions, and determines the order of objects in those partitions. Within each partition, a movable window frame is defined for every input object. The window frame determines the objects to be used by the window function.

SQL++ has a dedicated set of window functions. Each window function call includes an OVER clause, which introduces the window specification. Some window functions take additional window options, which are specified by further clauses before the OVER clause.

In Couchbase Server Enterprise Edition, [aggregate functions](aggregatefun.md) can also be used as window functions when they are used with an OVER clause.

In Couchbase Server 7.0 and later, window functions (and aggregate functions used as window functions) may specify their own inline window definitions, or they may refer to a named window defined by the WINDOW clause elsewhere in the query. By defining a named window with the WINDOW clause, you can reuse the window definition across several functions in the query, potentially making the query easier to write and maintain.

## [](#syntax)Syntax

This section shows the generic syntax of window functions, including window options and the OVER clause. See the sections below for details of the syntax of individual window functions.

### [](#window-function)Window Function

```ebnf
window-function ::= window-function-name '(' window-function-arguments ')'
                    window-function-options? over-clause
```

![Syntax diagram](../_images/n1ql-language-reference/window-function.png) 

| window-function-arguments | [Window Function Arguments](#window-function-arguments) |
| ------------------------- | ------------------------------------------------------- |
| window-function-options   | [Window Function Options](#window-function-options)     |
| over-clause               | [OVER Clause](#over-clause)                             |

### [](#window-function-arguments)Window Function Arguments

```ebnf
window-function-arguments ::= ( expr ( ',' expr ( ',' expr )? )? )?
```

![Syntax diagram](../_images/n1ql-language-reference/window-function-arguments.png) 

Refer to individual functions below for details of the arguments.

### [](#window-function-options)Window Function Options

```ebnf
window-function-options ::= nthval-from? nulls-treatment?
```

![Syntax diagram](../_images/n1ql-language-reference/window-function-options.png) 

| nthval-from     | [From Modifier](#nthval-from)      |
| --------------- | ---------------------------------- |
| nulls-treatment | [Nulls Modifier](#nulls-treatment) |

Window function options can only be used with some window functions, as described below.

#### [](#nthval-from)From Modifier

```ebnf
nthval-from ::= 'FROM' ( 'FIRST' | 'LAST' )
```

![Syntax diagram](../_images/n1ql-language-reference/nthval-from.png) 

The **from modifier** determines whether the computation begins at the first or last object in the window.

This clause can only be used with the [NTH\_VALUE()](#fn-window-nth-value) function.

This clause is optional. If omitted, the default setting is `FROM FIRST`.

#### [](#nulls-treatment)Nulls Modifier

```ebnf
nulls-treatment ::= ( 'RESPECT' | 'IGNORE' ) 'NULLS'
```

![Syntax diagram](../_images/n1ql-language-reference/nulls-treatment.png) 

The **nulls modifier** determines whether NULL values are included in the computation, or ignored. MISSING values are treated the same way as NULL values.

This clause can only be used with the [FIRST\_VALUE()](#fn-window-first-value), [LAST\_VALUE()](#fn-window-last-value), [NTH\_VALUE()](#fn-window-nth-value), [LAG()](#fn-window-lag), and [LEAD()](#fn-window-lead) functions.

This clause is optional. If omitted, the default setting is `RESPECT NULLS`.

### [](#over-clause)OVER Clause

```ebnf
over-clause ::= 'OVER' ( '(' window-definition ')' | window-ref )
```

![Syntax diagram](../_images/n1ql-language-reference/over-clause.png) 

The OVER clause introduces the window specification for the function. There are two ways of specifying the window.

* An _inline window definition_ specifies the window directly within the function call. It is delimited by parentheses `()` and has exactly the same syntax as the window definition in a WINDOW clause. For further details, refer to [Window Definition](window.md#window-definition).
* A _window reference_ is an [identifier](identifiers.md) which refers to a named window. The named window must be defined by a WINDOW clause in the same query block as the function call. For further details, refer to [WINDOW Clause](window.md).

With some window functions, the window specification may include a [window partition clause](window.md#window-partition-clause), a [window order clause](window.md#window-order-clause), and a [window frame clause](window.md#window-frame-clause). With other window functions, the window specification may only include a subset of these clauses. Refer to individual functions below for details of the clauses permitted within the window specification.

Note that any restrictions on the clauses permitted in the window specification apply equally, whether the function has an inline window definition, or a reference to a named window.

## [](#usage)Usage

Window functions can only appear in the [SELECT](selectclause.md) projection clause or query [ORDER BY](orderby.md) clause.

> [!TIP]
> Any expression within a window function may be a subquery. However, this will lead to repeated evaluation when the query is processed. If required, use a [LET clause](let.md), a [WITH clause](with.md), or an intervening [subquery](subqueries.md) to avoid repeated evaluation.

> [!NOTE]
> An expression within the window function may not contain another, nested window function. If necessary, you can specify one window function in a [subquery](subqueries.md), and another window function in the parent query.

Window functions are processed after [JOIN](join.md) clauses, the [LET](let.md) clause, the [WHERE](where.md) clause, and the [GROUP BY](groupby.md), [LETTING](groupby.md), and [HAVING](groupby.md) clauses. Window functions therefore operate on the query result set.

## [](#fn-window-cume-dist)CUME\_DIST()

### [](#description)Description

Returns the percentile rank of the current object as part of the cumulative distribution — that is, the number of objects ranked lower than or equal to the current object, including the current object, divided by the total number of objects in the window partition.

### [](#syntax-2)Syntax

```ebnf
cume-dist-function ::= 'CUME_DIST' '()' 'OVER' ( '(' window-definition ')' | window-ref )
```

![Syntax diagram](../_images/n1ql-language-reference/cume-dist-function.png) 

### [](#arguments)Arguments

None.

### [](#window-specification)Window Specification

The window specification may include an optional [window partition clause](window.md#window-partition-clause), and must include a [window order clause](window.md#window-order-clause).

### [](#return-value)Return Value

A number greater than 0 and less than or equal to 1\. The higher the value, the higher the ranking.

### [](#example)Example

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

For each destination airport, find the cumulative distribution of all routes in order of distance:

Query

```sqlpp
SELECT d.id, d.destinationairport, CUME_DIST() OVER (
  PARTITION BY d.destinationairport
  ORDER BY d.distance NULLS LAST
) AS `rank`
FROM route AS d
LIMIT 7;
```

Results

```json
[
  {
      "destinationairport": "AAE",
      "id": 10201,
      "rank": 0.25
  },
  {
      "destinationairport": "AAE",
      "id": 10190,
      "rank": 0.5
  },
  {
      "destinationairport": "AAE",
      "id": 10240,
      "rank": 0.75
  },
  {
      "destinationairport": "AAE",
      "id": 10136,
      "rank": 1
  },
  {
      "destinationairport": "AAL",
      "id": 14392,
      "rank": 0.3333333333333333
  },
  {
      "destinationairport": "AAL",
      "id": 14867,
      "rank": 0.6666666666666666
  },
  {
      "destinationairport": "AAL",
      "id": 22505,
      "rank": 1
  },
]
```

## [](#fn-window-dense-rank)DENSE\_RANK()

### [](#description-2)Description

Returns the dense rank of the current object — that is, the number of distinct objects preceding this object in the current window partition, plus one.

The objects are ordered by the [window order clause](window.md#window-order-clause). If any objects are tied, they will have the same rank.

For this function, when any objects have the same rank, the rank of the next object will be consecutive, so there will not be a gap in the sequence of returned values. For example, if there are three objects ranked 2, the next dense rank is 3.

### [](#syntax-3)Syntax

```ebnf
dense-rank-function ::= 'DENSE_RANK' '()' 'OVER' ( '(' window-definition ')' | window-ref )
```

![Syntax diagram](../_images/n1ql-language-reference/dense-rank-function.png) 

### [](#arguments-2)Arguments

None.

### [](#window-specification-2)Window Specification

The window specification may include an optional [window partition clause](window.md#window-partition-clause), and must include a [window order clause](window.md#window-order-clause).

### [](#return-values)Return Values

An integer, greater than or equal to 1.

### [](#example-2)Example

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

For each country, find the dense rank of all airports in order of altitude:

Query

```sqlpp
SELECT a.airportname, a.geo.alt, DENSE_RANK() OVER (
  PARTITION BY a.country
  ORDER BY a.geo.alt NULLS LAST
) AS `rank`
FROM airport AS a
LIMIT 10;
```

Results

```json
[
  {
    "airportname": "Croisette Heliport",
    "alt": 0,
    "rank": 1
  },
  {
    "airportname": "Andernos-Les-Bains",
    "alt": 0,
    "rank": 1
  },
  {
    "airportname": "La Defense Heliport",
    "alt": 0,
    "rank": 1
  },
  {
    "airportname": "Marigot Bus Stop",
    "alt": 0,
    "rank": 1
  },
  {
    "airportname": "Lille",
    "alt": 1,
    "rank": 2
  },
  {
    "airportname": "Le Palyvestre",
    "alt": 7,
    "rank": 3
  },
  {
    "airportname": "Frejus Saint Raphael",
    "alt": 7,
    "rank": 3
  },
  {
    "airportname": "Calais Dunkerque",
    "alt": 12,
    "rank": 4
  },
  {
    "airportname": "Cote D\\'Azur",
    "alt": 12,
    "rank": 4
  },
  {
    "airportname": "Propriano",
    "alt": 13,
    "rank": 5
  }
]
```

## [](#fn-window-first-value)FIRST\_VALUE(`expr`)

### [](#description-3)Description

Returns the requested value from the first object in the current window frame, where the window frame is determined by the [window definition](window.md#window-definition).

### [](#syntax-4)Syntax

```ebnf
first-value-function ::= 'FIRST_VALUE' '(' expr ')' nulls-treatment?
                         'OVER' ( '(' window-definition ')' | window-ref )
```

![Syntax diagram](../_images/n1ql-language-reference/first-value-function.png) 

### [](#fn-window-first-value-args)Arguments

expr

\[Required\] The value that you want to return from the first object in the window frame. \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]

#### [](#fn-window-first-value-nulls)Nulls Modifier

The [nulls modifier](#nulls-treatment) determines how NULL or MISSING values are treated when finding the first object in the window frame:

`IGNORE NULLS`

If the values for any objects evaluate to NULL or MISSING, those objects are not included when finding the first object. In this case, the function returns the first non-NULL, non-MISSING value.

`RESPECT NULLS`

If the values for any objects evaluate to NULL or MISSING, those objects are included when finding the first object.

If the [nulls modifier](#nulls-treatment) is omitted, the default is `RESPECT NULLS`.

### [](#window-specification-3)Window Specification

The window specification may include an optional [window partition clause](window.md#window-partition-clause), an optional [window order clause](window.md#window-order-clause), and an optional [window frame clause](window.md#window-frame-clause).

### [](#return-values-2)Return Values

The specified value from the first object.

If all values are NULL or MISSING it returns NULL.

> [!NOTE]
> In the following cases, this function may return unpredictable results.
> 
> * If the [window order clause](window.md#window-order-clause) is omitted.
> * If the window frame is defined by `ROWS`, and there are tied objects in the window frame.
> 
> To make the function return deterministic results, add a [window order clause](window.md#window-order-clause), or add further ordering terms to the [window order clause](window.md#window-order-clause) so that no objects are tied.
> 
> If the window frame is defined by `RANGE` or `GROUPS`, and there are tied objects in the window frame, the function returns the lowest value of the input expression.

### [](#example-3)Example

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

For each airport, show each route starting at that airport, including the distance of the route and the distance of the shortest route from that airport:

Query

```sqlpp
SELECT r.sourceairport, r.destinationairport, r.distance,
FIRST_VALUE(r.distance) OVER (
  PARTITION BY r.sourceairport
  ORDER BY r.distance
) AS `shortest_distance`
FROM route AS r
LIMIT 7;
```

Results

```json
[
  {
      "destinationairport": "MRS",
      "distance": 767.6526005881392,
      "shortest_distance": 767.6526005881392,
      "sourceairport": "AAE"
  },
  {
      "destinationairport": "LYS",
      "distance": 1015.6529968903878,
      "shortest_distance": 767.6526005881392,
      "sourceairport": "AAE"
  },
  {
      "destinationairport": "ORY",
      "distance": 1395.3690007167947,
      "shortest_distance": 767.6526005881392,
      "sourceairport": "AAE"
  },
  {
      "destinationairport": "CDG",
      "distance": 1420.6731433915318,
      "shortest_distance": 767.6526005881392,
      "sourceairport": "AAE"
  },
  {
      "destinationairport": "AAR",
      "distance": 99.89861063028253,
      "shortest_distance": 99.89861063028253,
      "sourceairport": "AAL"
  },
  {
      "destinationairport": "OSL",
      "distance": 352.33081791745275,
      "shortest_distance": 99.89861063028253,
      "sourceairport": "AAL"
  },
  {
      "destinationairport": "LGW",
      "distance": 928.284226131001,
      "shortest_distance": 99.89861063028253,
      "sourceairport": "AAL"
  }
]
```

Refer also to [WINDOW Clause example 3](window.md#ex-3) for a query showing this function used with the WINDOW clause.

## [](#fn-window-lag)LAG(`expr` \[, `offset` \[, `default` \] \] )

### [](#description-4)Description

Returns the value of an object at a given offset prior to the current object position.

### [](#syntax-5)Syntax

```ebnf
lag-function ::= 'LAG' '(' expr ( ',' offset ( ',' default )? )? ')' nulls-treatment?
                 'OVER' ( '(' window-definition ')' | window-ref )
```

![Syntax diagram](../_images/n1ql-language-reference/lag-function.png) 

### [](#fn-window-lag-args)Arguments

expr

\[Required\] The value that you want to return from the offset object. \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]

offset

\[Optional\] A positive integer greater than 0\. If omitted, the default is 1.

default

\[Optional\] The value to return when the offset goes out of window scope. If omitted, the default is NULL.

#### [](#fn-window-lag-nulls)Nulls Modifier

The [nulls modifier](#nulls-treatment) determines how NULL or MISSING values are treated when counting the offset:

`IGNORE NULLS`

If the values for any objects evaluate to NULL or MISSING, those objects are not included when counting the offset.

`RESPECT NULLS`

If the values for any objects evaluate to NULL or MISSING, those objects are included when counting the offset.

If the [nulls modifier](#nulls-treatment) is omitted, the default is `RESPECT NULLS`.

### [](#window-specification-4)Window Specification

The window specification may include an optional [window partition clause](window.md#window-partition-clause), and must include a [window order clause](window.md#window-order-clause).

### [](#return-values-3)Return Values

The specified value from the offset object.

If the offset object is out of scope, it returns the default value, or NULL if no default is specified.

### [](#example-4)Example

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

For each airline, show each route operated by that airline, including the length of the route and the length of the next-shortest route:

Query

```sqlpp
SELECT r.airline, r.id, r.distance,
LAG(r.distance, 1, "No previous distance") OVER (
  PARTITION BY r.airline
  ORDER BY r.distance NULLS LAST
) AS `previous-distance`
FROM route AS r
LIMIT 7;
```

Results

```json
[
  {
      "airline": "2L",
      "distance": 770.9691328580009,
      "id": 125,
      "previous-distance": "No previous distance"
  },
  {
      "airline": "2L",
      "distance": 770.969132858001,
      "id": 117,
      "previous-distance": 770.9691328580009
  },
  {
      "airline": "2L",
      "distance": 922.7579695456559,
      "id": 118,
      "previous-distance": 770.969132858001
  },
  {
      "airline": "2L",
      "distance": 922.7579695456559,
      "id": 126,
      "previous-distance": 922.7579695456559
  },
  {
      "airline": "3F",
      "distance": 23.957943869396804,
      "id": 274,
      "previous-distance": "No previous distance"
  },
  {
      "airline": "3F",
      "distance": 23.957943869396804,
      "id": 276,
      "previous-distance": 23.957943869396804
  },
  {
      "airline": "3F",
      "distance": 26.397914084363418,
      "id": 282,
      "previous-distance": 23.957943869396804
  }
]
```

Refer also to [WINDOW Clause example 1](window.md#ex-1) for a query showing this function used with the WINDOW clause.

## [](#fn-window-last-value)LAST\_VALUE(`expr`)

### [](#description-5)Description

Returns the requested value from the last object in the current window frame, where the window frame is specified by the [window definition](window.md#window-definition).

### [](#syntax-6)Syntax

```ebnf
last-value-function ::= 'LAST_VALUE' '(' expr ')' nulls-treatment?
                        'OVER' ( '(' window-definition ')' | window-ref )
```

![Syntax diagram](../_images/n1ql-language-reference/last-value-function.png) 

### [](#fn-window-last-value-args)Arguments

expr

\[Required\] The value that you want to return from the last object in the window frame. \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]

#### [](#fn-window-last-value-nulls)Nulls Modifier

The [nulls modifier](#nulls-treatment) determines how NULL or MISSING values are treated when finding the last object in the window frame:

`IGNORE NULLS`

If the values for any objects evaluate to NULL or MISSING, those objects are not included when finding the last object. In this case, the function returns the last non-NULL, non-MISSING value.

`RESPECT NULLS`

If the values for any objects evaluate to NULL or MISSING, those objects are included when finding the last object.

If the [nulls modifier](#nulls-treatment) is omitted, the default is `RESPECT NULLS`.

### [](#window-specification-5)Window Specification

The window specification may include an optional [window partition clause](window.md#window-partition-clause), an optional [window order clause](window.md#window-order-clause), and an optional [window frame clause](window.md#window-frame-clause).

### [](#return-values-4)Return Values

The specified value from the last object.

If all values are NULL or MISSING it returns NULL.

> [!NOTE]
> In the following cases, this function may return unpredictable results.
> 
> * If the [window order clause](window.md#window-order-clause) is omitted.
> * If the [window frame clause](window.md#window-frame-clause) is omitted.
> * If the window frame is defined by `ROWS`, and there are tied objects in the window frame.
> 
> To make the function return deterministic results, add a [window order clause](window.md#window-order-clause), or add further ordering terms to the [window order clause](window.md#window-order-clause) so that no objects are tied.
> 
> If the window frame is defined by `RANGE` or `GROUPS`, and there are tied objects in the window frame, the function returns the highest value of the input expression.

### [](#example-5)Example

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

For each airport, show each route starting at that airport, including the distance of the route and the distance of the longest route from that airport:

Query

```sqlpp
SELECT r.sourceairport, r.destinationairport, r.distance,
LAST_VALUE(r.distance) OVER (
  PARTITION BY r.sourceairport
  ORDER BY r.distance
  ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING (1)
) AS `longest_distance`
FROM route AS r
LIMIT 7;
```

| **1** | This clause specifies that the window frame should extend to the end of the window partition. Without this clause, the end point of the window frame would always be the current object. This would mean that the longest distance would always be the same as the current distance. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

Results

```json
[
  {
      "destinationairport": "MRS",
      "distance": 767.6526005881392,
      "longest_distance": 1420.6731433915318,
      "sourceairport": "AAE"
  },
  {
      "destinationairport": "LYS",
      "distance": 1015.6529968903878,
      "longest_distance": 1420.6731433915318,
      "sourceairport": "AAE"
  },
  {
      "destinationairport": "ORY",
      "distance": 1395.3690007167947,
      "longest_distance": 1420.6731433915318,
      "sourceairport": "AAE"
  },
  {
      "destinationairport": "CDG",
      "distance": 1420.6731433915318,
      "longest_distance": 1420.6731433915318,
      "sourceairport": "AAE"
  },
  {
      "destinationairport": "AAR",
      "distance": 99.89861063028253,
      "longest_distance": 928.284226131001,
      "sourceairport": "AAL"
  },
  {
      "destinationairport": "OSL",
      "distance": 352.33081791745275,
      "longest_distance": 928.284226131001,
      "sourceairport": "AAL"
  },
  {
      "destinationairport": "LGW",
      "distance": 928.284226131001,
      "longest_distance": 928.284226131001,
      "sourceairport": "AAL"
  }
]
```

Refer also to [WINDOW Clause example 3](window.md#ex-3) for a query showing this function used with the WINDOW clause.

## [](#fn-window-lead)LEAD(`expr` \[, `offset` \[, `default` \] \] )

### [](#description-6)Description

Returns the value of an object at a given offset ahead of the current object position.

### [](#syntax-7)Syntax

```ebnf
lead-function ::= 'LEAD' '(' expr ( ',' offset ( ',' default )? )? ')' nulls-treatment?
                  'OVER' ( '(' window-definition ')' | window-ref )
```

![Syntax diagram](../_images/n1ql-language-reference/lead-function.png) 

### [](#fn-window-lead-args)Arguments

expr

\[Required\] The value that you want to return from the offset object. \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]

offset

\[Optional\] A positive integer greater than 0\. If omitted, the default is 1.

default

\[Optional\] The value to return when the offset goes out of window scope. If omitted, the default is NULL.

#### [](#fn-window-lead-nulls)Nulls Modifier

The [nulls modifier](#nulls-treatment) determines how NULL or MISSING values are treated when counting the offset:

`IGNORE NULLS`

If the values for any objects evaluate to NULL or MISSING, those objects are not included when counting the offset.

`RESPECT NULLS`

If the values for any objects evaluate to NULL or MISSING, those objects are included when counting the offset.

If the [nulls modifier](#nulls-treatment) is omitted, the default is `RESPECT NULLS`.

### [](#window-specification-6)Window Specification

The window specification may include an optional [window partition clause](window.md#window-partition-clause), and must include a [window order clause](window.md#window-order-clause).

### [](#return-values-5)Return Values

The specified value from the offset object.

If the offset object is out of scope, it returns the default value, or NULL if no default is specified.

### [](#example-6)Example

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

For each airline, show each route operated by that airline, including the length of the route and the length of the next-longest route:

Query

```sqlpp
SELECT r.airline, r.id, r.distance,
LEAD(r.distance, 1, "No next distance") OVER (
  PARTITION BY r.airline
  ORDER BY r.distance NULLS LAST
) AS `next-distance`
FROM route AS r
LIMIT 7;
```

Results

```json
  [
  {
      "airline": "2L",
      "distance": 770.9691328580009,
      "id": 125,
      "next-distance": 770.969132858001
  },
  {
      "airline": "2L",
      "distance": 770.969132858001,
      "id": 117,
      "next-distance": 922.7579695456559
  },
  {
      "airline": "2L",
      "distance": 922.7579695456559,
      "id": 118,
      "next-distance": 922.7579695456559
  },
  {
      "airline": "2L",
      "distance": 922.7579695456559,
      "id": 126,
      "next-distance": "No next distance"
  },
  {
      "airline": "3F",
      "distance": 23.957943869396804,
      "id": 274,
      "next-distance": 23.957943869396804
  },
  {
      "airline": "3F",
      "distance": 23.957943869396804,
      "id": 276,
      "next-distance": 26.397914084363418
  },
  {
      "airline": "3F",
      "distance": 26.397914084363418,
      "id": 282,
      "next-distance": 26.397914084363418
  }
]
```

Refer also to [WINDOW Clause example 1](window.md#ex-1) for a query showing this function used with the WINDOW clause.

## [](#fn-window-nth-value)NTH\_VALUE(`expr`, `offset`)

### [](#description-7)Description

Returns the requested value from an object in the current window frame, where the window frame is specified by the [window definition](window.md#window-definition).

### [](#syntax-8)Syntax

```ebnf
nth-value-function ::= 'NTH_VALUE' '(' expr ',' offset ')' nthval-from? nulls-treatment?
                       'OVER' ( '(' window-definition ')' | window-ref )
```

![Syntax diagram](../_images/n1ql-language-reference/nth-value-function.png) 

### [](#fn-window-nth-value-args)Arguments

expr

\[Required\] The value that you want to return from the offset object in the window frame. \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]

offset

\[Required\] The number of the offset object within the window frame, counting from 1.

#### [](#fn-window-nth-value-from)From Modifier

The [from modifier](#nthval-from) determines where the function starts counting the offset.

`FROM FIRST`

Offset counting starts at the first object in the window frame. In this case, an offset of 1 is the first object in the window frame, 2 is the second object, and so on.

`FROM LAST`

Offset counting starts at the last object in the window frame. In this case, an offset of 1 is the last object in the window frame, 2 is the second-to-last object, and so on.

#### [](#fn-window-nth-value-nulls)Nulls Modifier

The [nulls modifier](#nulls-treatment) determines how NULL or MISSING values are treated when counting the offset:

`IGNORE NULLS`

If the values for any objects evaluate to NULL or MISSING, those objects are not included when counting the offset.

`RESPECT NULLS`

If the values for any objects evaluate to NULL or MISSING, those objects are included when counting the offset.

If the [nulls modifier](#nulls-treatment) is omitted, the default is `RESPECT NULLS`.

### [](#window-specification-7)Window Specification

The window specification may include an optional [window partition clause](window.md#window-partition-clause), an optional [window order clause](window.md#window-order-clause), and an optional [window frame clause](window.md#window-frame-clause).

### [](#return-values-6)Return Values

The specified value from the offset object.

> [!NOTE]
> In the following cases, this function may return unpredictable results.
> 
> * If the [window order clause](window.md#window-order-clause) is omitted.
> * If the [window frame clause](window.md#window-frame-clause) is omitted.
> * If the window frame is defined by `ROWS`, and there are tied objects in the window frame.
> 
> To make the function return deterministic results, add a [window order clause](window.md#window-order-clause), or add further ordering terms to the [window order clause](window.md#window-order-clause) so that no objects are tied.
> 
> If the window frame is defined by `RANGE` or `GROUPS`, and there are tied objects in the window frame, the function returns the lowest value of the input expression when counting `FROM FIRST`, or the highest value of the input expression when counting `FROM LAST`.

### [](#examples)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

For each airport, show each route starting at that airport, including the distance of the route and the distance of the second shortest route from that airport:

Query

```sqlpp
SELECT r.sourceairport, r.destinationairport, r.distance,
NTH_VALUE(r.distance, 2) FROM FIRST OVER (
  PARTITION BY r.sourceairport
  ORDER BY r.distance
  ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING (1)
) AS `shortest_distance_but_1`
FROM route AS r
LIMIT 7;
```

| **1** | This clause specifies that the window frame should extend to the end of the window partition. Without this clause, the end point of the window frame would always be the current object. This would mean that for the route with the shortest distance, the function would be unable to find the route with the second shortest distance. |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Results

```json
[
  {
      "destinationairport": "MRS",
      "distance": 767.6526005881392,
      "shortest_distance_but_1": 1015.6529968903878,
      "sourceairport": "AAE"
  },
  {
      "destinationairport": "LYS", (1)
      "distance": 1015.6529968903878,
      "shortest_distance_but_1": 1015.6529968903878,
      "sourceairport": "AAE"
  },
  {
      "destinationairport": "ORY",
      "distance": 1395.3690007167947,
      "shortest_distance_but_1": 1015.6529968903878,
      "sourceairport": "AAE"
  },
  {
      "destinationairport": "CDG",
      "distance": 1420.6731433915318,
      "shortest_distance_but_1": 1015.6529968903878,
      "sourceairport": "AAE"
  },
  {
      "destinationairport": "AAR",
      "distance": 99.89861063028253,
      "shortest_distance_but_1": 352.33081791745275,
      "sourceairport": "AAL"
  },
  {
      "destinationairport": "OSL", (2)
      "distance": 352.33081791745275,
      "shortest_distance_but_1": 352.33081791745275,
      "sourceairport": "AAL"
  },
  {
      "destinationairport": "LGW",
      "distance": 928.284226131001,
      "shortest_distance_but_1": 352.33081791745275,
      "sourceairport": "AAL"
  }
]
```

| **1** | This is the route with the second shortest distance from AAE. |
| ----- | ------------------------------------------------------------- |
| **2** | This is the route with the second shortest distance from AAL. |

For each airport, show each route starting at that airport, including the distance of the route and the distance of the second longest route from that airport:

Query

```sqlpp
SELECT r.sourceairport, r.destinationairport, r.distance,
NTH_VALUE(r.distance, 2) FROM LAST OVER (
  PARTITION BY r.sourceairport
  ORDER BY r.distance
  ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING (1)
) AS `longest_distance_but_1`
FROM route AS r
LIMIT 7;
```

| **1** | This clause specifies that the window frame should extend to the end of the window partition. Without this clause, the end point of the window frame would always be the current object. This would mean the function would be unable to find the route with the second longest distance for routes with shorter distances. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Results

```json
[
  {
      "destinationairport": "MRS",
      "distance": 767.6526005881392,
      "longest_distance_but_1": 1395.3690007167947,
      "sourceairport": "AAE"
  },
  {
      "destinationairport": "LYS",
      "distance": 1015.6529968903878,
      "longest_distance_but_1": 1395.3690007167947,
      "sourceairport": "AAE"
  },
  {
      "destinationairport": "ORY",
      "distance": 1395.3690007167947,
      "longest_distance_but_1": 1395.3690007167947, (1)
      "sourceairport": "AAE"
  },
  {
      "destinationairport": "CDG",
      "distance": 1420.6731433915318,
      "longest_distance_but_1": 1395.3690007167947,
      "sourceairport": "AAE"
  },
  {
      "destinationairport": "AAR",
      "distance": 99.89861063028253,
      "longest_distance_but_1": 352.33081791745275,
      "sourceairport": "AAL"
  },
  {
      "destinationairport": "OSL",
      "distance": 352.33081791745275,
      "longest_distance_but_1": 352.33081791745275, (2)
      "sourceairport": "AAL"
  },
  {
      "destinationairport": "LGW",
      "distance": 928.284226131001,
      "longest_distance_but_1": 352.33081791745275,
      "sourceairport": "AAL"
  }
]
```

| **1** | This is the route with the second longest distance from AAE. |
| ----- | ------------------------------------------------------------ |
| **2** | This is the route with the second longest distance from AAL. |

## [](#fn-window-ntile)NTILE(`num_tiles`)

### [](#description-8)Description

Divides the window partition into the specified number of tiles, and allocates each object in the window partition to a tile, so that as far as possible each tile has an equal number of objects. When the set of objects is not equally divisible by the number of tiles, the function puts more objects into the lower-numbered tiles. For each object, the function returns the number of the tile into which that object was placed.

### [](#syntax-9)Syntax

```ebnf
ntile-function ::= 'NTILE' '(' num_tiles ')'
                   'OVER' ( '(' window-definition ')' | window-ref )
```

![Syntax diagram](../_images/n1ql-language-reference/ntile-function.png) 

### [](#fn-window-ntile-args)Arguments

num\_tiles

\[Required\] The number of tiles into which you want to divide the window partition. This argument can be an expression and must evaluate to a number. If the number is not an integer, it will be truncated. If the expression depends on an object, it evaluates from the first object in the window partition.

### [](#window-specification-8)Window Specification

The window specification may include an optional [window partition clause](window.md#window-partition-clause), and must include a [window order clause](window.md#window-order-clause).

### [](#return-values-7)Return Values

An value greater than or equal to 1 and less than or equal to the number of tiles.

### [](#example-7)Example

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

For each airline, allocate each route to one of three tiles by distance:

Query

```sqlpp
SELECT r.airline, r.distance, NTILE(3) OVER (
  PARTITION BY r.airline
  ORDER BY r.distance
) AS `ntile`
FROM route AS r
LIMIT 16;
```

Results

```json
[
  {
    "airline": "2L",
    "distance": 770.9691328580009,
    "ntile": 1
  },
  {
    "airline": "2L",
    "distance": 770.969132858001,
    "ntile": 1
  },
  {
    "airline": "2L",
    "distance": 922.7579695456559,
    "ntile": 2
  },
  {
    "airline": "2L",
    "distance": 922.7579695456559,
    "ntile": 3
  },
  {
    "airline": "3F",
    "distance": 23.957943869396804,
    "ntile": 1
  },
  {
    "airline": "3F",
    "distance": 23.957943869396804,
    "ntile": 1
  },
  {
    "airline": "3F",
    "distance": 26.397914084363418,
    "ntile": 1
  },
  {
    "airline": "3F",
    "distance": 26.397914084363418,
    "ntile": 1
  },
  {
    "airline": "3F",
    "distance": 31.613003135476145,
    "ntile": 2
  },
  {
    "airline": "3F",
    "distance": 31.613003135476145,
    "ntile": 2
  },
  {
    "airline": "3F",
    "distance": 60.49012512494272,
    "ntile": 2
  },
  {
    "airline": "3F",
    "distance": 60.490125124942736,
    "ntile": 2
  },
  {
    "airline": "3F",
    "distance": 63.640308584677314,
    "ntile": 3
  },
  {
    "airline": "3F",
    "distance": 63.640308584677314,
    "ntile": 3
  },
  {
    "airline": "3F",
    "distance": 91.53839302649642,
    "ntile": 3
  },
  {
    "airline": "3F",
    "distance": 91.53839302649642,
    "ntile": 3
  }
]
```

## [](#fn-window-percent-rank)PERCENT\_RANK()

### [](#description-9)Description

Returns the percentile rank of the current object — that is, the rank of the object minus one, divided by the total number of objects in the window partition minus one.

### [](#syntax-10)Syntax

```ebnf
percent-rank-function ::= 'PERCENT_RANK' '()'
                          'OVER' ( '(' window-definition ')' | window-ref )
```

![Syntax diagram](../_images/n1ql-language-reference/percent-rank-function.png) 

### [](#arguments-3)Arguments

None.

### [](#window-specification-9)Window Specification

The window specification may include an optional [window partition clause](window.md#window-partition-clause), and must include a [window order clause](window.md#window-order-clause).

### [](#return-values-8)Return Values

A number between 0 and 1\. The higher the value, the higher the ranking.

### [](#example-8)Example

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

For each destination airport, find the percentile rank of all routes in order of distance:

Query

```sqlpp
SELECT d.id, d.destinationairport, PERCENT_RANK() OVER (
  PARTITION BY d.destinationairport
  ORDER BY d.distance NULLS LAST
) AS `rank`
FROM route AS d
LIMIT 7;
```

Results

```json
[
  {
      "destinationairport": "AAE",
      "id": 10201,
      "rank": 0
  },
  {
      "destinationairport": "AAE",
      "id": 10190,
      "rank": 0.3333333333333333
  },
  {
      "destinationairport": "AAE",
      "id": 10240,
      "rank": 0.6666666666666666
  },
  {
      "destinationairport": "AAE",
      "id": 10136,
      "rank": 1
  },
  {
      "destinationairport": "AAL",
      "id": 14392,
      "rank": 0
  },
  {
      "destinationairport": "AAL",
      "id": 14867,
      "rank": 0.5
  },
  {
      "destinationairport": "AAL",
      "id": 22505,
      "rank": 1
  }
]
```

## [](#fn-window-rank)RANK()

### [](#description-10)Description

Returns the rank of the current object — that is, the number of distinct objects preceding this object in the current window partition, plus one.

The objects are ordered by the [window order clause](window.md#window-order-clause). If any objects are tied, they will have the same rank.

When any objects have the same rank, the rank of the next object will include all preceding objects, so there may be a gap in the sequence of returned values. For example, if there are three objects ranked 2, the next rank is 5.

### [](#syntax-11)Syntax

```ebnf
rank-function ::= 'RANK' '()' 'OVER' ( '(' window-definition ')' | window-ref )
```

![Syntax diagram](../_images/n1ql-language-reference/rank-function.png) 

### [](#arguments-4)Arguments

None.

### [](#window-specification-10)Window Specification

The window specification may include an optional [window partition clause](window.md#window-partition-clause), and must include a [window order clause](window.md#window-order-clause).

### [](#return-values-9)Return Values

An integer, greater than or equal to 1.

### [](#example-9)Example

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

For each country, find the rank of all airports in order of altitude:

Query

```sqlpp
SELECT a.airportname, a.geo.alt, RANK() OVER (
  PARTITION BY a.country
  ORDER BY a.geo.alt NULLS LAST
) AS `rank`
FROM airport AS a
LIMIT 10;
```

Results

```json
[
  {
    "airportname": "Croisette Heliport",
    "alt": 0,
    "rank": 1
  },
  {
    "airportname": "Andernos-Les-Bains",
    "alt": 0,
    "rank": 1
  },
  {
    "airportname": "La Defense Heliport",
    "alt": 0,
    "rank": 1
  },
  {
    "airportname": "Marigot Bus Stop",
    "alt": 0,
    "rank": 1
  },
  {
    "airportname": "Lille",
    "alt": 1,
    "rank": 5
  },
  {
    "airportname": "Le Palyvestre",
    "alt": 7,
    "rank": 6
  },
  {
    "airportname": "Frejus Saint Raphael",
    "alt": 7,
    "rank": 6
  },
  {
    "airportname": "Calais Dunkerque",
    "alt": 12,
    "rank": 8
  },
  {
    "airportname": "Cote D\\'Azur",
    "alt": 12,
    "rank": 8
  },
  {
    "airportname": "Propriano",
    "alt": 13,
    "rank": 10
  }
]
```

## [](#fn-window-ratio-to-report)RATIO\_TO\_REPORT(`expr`)

### [](#description-11)Description

Returns the fractional ratio of the specified value for each object to the sum of values for all objects in the window frame. If the [window frame clause](window.md#window-frame-clause) is not specified, the fractional ratio is calculated for the whole window partition.

### [](#syntax-12)Syntax

```ebnf
ratio-to-report-function ::= 'RATIO_TO_REPORT' '(' expr ')'
                             'OVER' ( '(' window-definition ')' | window-ref )
```

![Syntax diagram](../_images/n1ql-language-reference/ratio-to-report-function.png) 

### [](#fn-window-ratio-to-report-args)Arguments

expr

\[Required\] The value for which you want to calculate the fractional ratio. \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]

### [](#window-specification-11)Window Specification

The window specification may include an optional [window partition clause](window.md#window-partition-clause), an optional [window order clause](window.md#window-order-clause), and an optional [window frame clause](window.md#window-frame-clause).

### [](#return-values-10)Return Values

A number between 0 and 1, representing the fractional ratio of the value for the current object to the sum of values for all objects in the current window frame. The sum of values for all objects in the current window frame is 1.

If the input expression does not evaluate to a number, or the sum of values for all objects is zero, it returns NULL.

### [](#example-10)Example

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

For each destination airport, calculate the distance of each route as a fraction of the total distance of all routes:

Query

```sqlpp
SELECT d.id, d.destinationairport, RATIO_TO_REPORT(d.distance) OVER (
  PARTITION BY d.destinationairport
) AS `distance-ratio`
FROM route AS d
LIMIT 7;
```

Results

```json
[
  {
      "destinationairport": "AAE",
      "distance-ratio": 0.3088857862487639,
      "id": 10136
  },
  {
      "destinationairport": "AAE",
      "distance-ratio": 0.22082544177013463,
      "id": 10190
  },
  {
      "destinationairport": "AAE",
      "distance-ratio": 0.3033841055547952,
      "id": 10240
  },
  {
      "destinationairport": "AAE",
      "distance-ratio": 0.16690466642630636,
      "id": 10201
  },
  {
      "destinationairport": "AAL",
      "distance-ratio": 0.25521719160354467,
      "id": 14867
  },
  {
      "destinationairport": "AAL",
      "distance-ratio": 0.6724194454614251,
      "id": 22505
  },
  {
      "destinationairport": "AAL",
      "distance-ratio": 0.07236336293503035,
      "id": 14392
  }
]
```

Refer also to [WINDOW Clause example 2](window.md#ex-2) for a query showing this function used with the WINDOW clause.

## [](#fn-window-row-number)ROW\_NUMBER()

### [](#description-12)Description

Returns a unique row number for every object in every window partition. In each window partition, the row numbering starts at 1.

The [window order clause](window.md#window-order-clause) determines the sort order of the objects. If the [window order clause](window.md#window-order-clause) is omitted, the return values may be unpredictable.

### [](#syntax-13)Syntax

```ebnf
row-number-function ::= 'ROW_NUMBER' '()' 'OVER' ( '(' window-definition ')' | window-ref )
```

![Syntax diagram](../_images/n1ql-language-reference/row-number-function.png) 

### [](#arguments-5)Arguments

None.

### [](#window-specification-12)Window Specification

The window specification may include an optional [window partition clause](window.md#window-partition-clause), and an optional [window order clause](window.md#window-order-clause).

### [](#return-values-11)Return Values

An integer, greater than or equal to 1.

### [](#example-11)Example

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

For each destination airport, number all routes in order of distance:

Query

```sqlpp
SELECT d.id, d.destinationairport, ROW_NUMBER() OVER (
  PARTITION BY d.destinationairport
  ORDER BY d.distance NULLS LAST
) AS `row`
FROM route AS d
LIMIT 7;
```

Results

```json
[
  {
    "destinationairport": "AAE",
    "id": 10201,
    "row": 1
  },
  {
    "destinationairport": "AAE",
    "id": 10190,
    "row": 2
  },
  {
    "destinationairport": "AAE",
    "id": 10240,
    "row": 3
  },
  {
    "destinationairport": "AAE",
    "id": 10136,
    "row": 4
  },
  {
    "destinationairport": "AAL",
    "id": 14392,
    "row": 1
  },
  {
    "destinationairport": "AAL",
    "id": 14867,
    "row": 2
  },
  {
    "destinationairport": "AAL",
    "id": 22505,
    "row": 3
  }
]
```

Refer also to [WINDOW Clause example 2](window.md#ex-2) for a query showing this function used with the WINDOW clause.

## [](#related-links)Related Links

* [Aggregate Functions](aggregatefun.md)
* [WINDOW Clause](window.md)

---

[1](#%5Ffootnoteref%5F1). If the query contains the [GROUP BY](groupby.md) clause or [aggregate functions](aggregatefun.md), this expression must only depend on GROUP BY expressions or aggregate functions.