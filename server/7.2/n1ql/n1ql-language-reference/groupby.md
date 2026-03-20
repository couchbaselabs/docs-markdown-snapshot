---
title: GROUP BY Clause
description: The GROUP BY clause arranges aggregate values into groups, based on
  one or more fields.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/n1ql/pages/n1ql-language-reference/groupby.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:n1ql:n1ql-language-reference/groupby.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/n1ql/n1ql-language-reference/groupby.html)

# GROUP BY Clause

> The GROUP BY clause arranges aggregate values into groups, based on one or more fields. 

## [](#purpose)Purpose

Use the GROUP BY clause to arrange aggregate values into groups of one or more fields. This `GROUP BY` clause follows the `WHERE` clause and precedes the optional `LETTING`, `HAVING`, and `ORDER BY` clauses.

## [](#syntax)Syntax

```ebnf
group-by-clause ::= 'GROUP' 'BY' group-term ( ',' group-term )*
                    letting-clause? having-clause? | letting-clause
```

![Syntax diagram](../_images/n1ql-language-reference/group-by-clause.png) 

| group-term     | [Group Term](#group-term)         |
| -------------- | --------------------------------- |
| letting-clause | [LETTING Clause](#letting-clause) |
| having-clause  | [HAVING Clause](#having-clause)   |

### [](#group-term)Group Term

```ebnf
group-term ::= expr ( ('AS')? alias )?
```

![Syntax diagram](../_images/n1ql-language-reference/group-term.png) 

At least one group term is required.

expr

String or expression representing an [aggregate function](aggregatefun.md) or field to group together.

alias

Assigns another name to the group term. For details, see [AS Clause](from.md#section%5Fax5%5F2nx%5F1db).

Assigning an alias to the group term is optional. If you assign an alias, the `AS` keyword may be omitted.

### [](#letting-clause)LETTING Clause

```ebnf
letting-clause ::= 'LETTING' alias '=' expr ( ',' alias '=' expr )*
```

![Syntax diagram](../_images/n1ql-language-reference/letting-clause.png) 

\[Optional\] Stores the result of a sub-expression in order to use it in subsequent clauses.

alias

String or expression representing the name of the clause to be referred to.

expr

String or expression representing the value of the `LETTING` `alias` variable.

### [](#having-clause)HAVING Clause

```ebnf
having-clause ::= 'HAVING' cond
```

![Syntax diagram](../_images/n1ql-language-reference/having-clause.png) 

\[Optional\] To return items where [aggregate](aggregatefun.md) values meet the specified conditions.

cond

String or expression representing the clause of aggregate values.

## [](#limitations)Limitations

`GROUP BY` works only on a group key or [aggregate function](aggregatefun.md).

A query needs a predicate on a leading index key to ensure that the optimizer can select a secondary index for the query. Without a matching predicate, the query will use the primary index. The simplest predicate is `WHERE _leading-index-key_ IS NOT MISSING`. This is usually only necessary in queries which do not otherwise have a WHERE clause; for example, some GROUP BY and aggregate queries. For more details, refer to [Index Selection](selectintro.md#index-selection).

## [](#examples)Examples

Example 1\. Group the unique landmarks by city and list the top 4 cities with the most landmarks in descending order

```sqlpp
SELECT city City, COUNT(DISTINCT name) LandmarkCount
FROM landmark
GROUP BY city
ORDER BY LandmarkCount DESC
LIMIT 4;
```

Results

```json
[
  {
    "City": "San Francisco",
    "LandmarkCount": 797
  },
  {
    "City": "London",
    "LandmarkCount": 443
  },
  {
    "City": "Los Angeles",
    "LandmarkCount": 284
  },
  {
    "City": "San Diego",
    "LandmarkCount": 197
  }
]
```

Example 2\. Use LETTING to find cities that have a minimum number of things to see

```sqlpp
SELECT city City, COUNT(DISTINCT name) LandmarkCount
FROM landmark
GROUP BY city
LETTING MinimumThingsToSee = 400
HAVING COUNT(DISTINCT name) > MinimumThingsToSee;
```

Results

```json
[
  {
    "City": "London",
    "LandmarkCount": 443
  },
  {
    "City": "San Francisco",
    "LandmarkCount": 797
  }
]
```

Example 3\. Use HAVING to specify cities that have more than 180 landmarks

```sqlpp
SELECT city City, COUNT(DISTINCT name) LandmarkCount
FROM landmark
GROUP BY city
HAVING COUNT(DISTINCT name) > 180;
```

Results

```json
[
  {
    "City": "London",
    "LandmarkCount": 443
  },
  {
    "City": "Los Angeles",
    "LandmarkCount": 284
  },
  {
    "City": "San Francisco",
    "LandmarkCount": 797
  },
  {
    "City": "San Diego",
    "LandmarkCount": 197
  }
]
```

> [!NOTE]
> The above `HAVING` clause must use the [aggregate function](aggregatefun.md) `COUNT` instead of its alias `LandmarkCount`.

Example 4\. Use HAVING to specify landmarks that begin with an "S" or higher

```sqlpp
SELECT city City, COUNT(DISTINCT name) LandmarkCount
FROM landmark
GROUP BY city
HAVING city > "S"
ORDER BY city;
```

Results

```json
[
  {
    "City": "Sacramento",
    "LandmarkCount": 2
  },
  {
    "City": "Saint Albans",
    "LandmarkCount": 5
  },
  {
    "City": "Saint Andrews",
    "LandmarkCount": 13
  },
  {
    "City": "Saint Annes Head",
    "LandmarkCount": 1
  },
// ...
```

(execution: 1s docs: 138)

Example 5\. Using WHERE yields the same results as HAVING, however, WHERE is faster

```sqlpp
SELECT city City, COUNT(DISTINCT name) LandmarkCount
FROM landmark
WHERE city > "S"
GROUP BY city
ORDER BY city;
```

Results

```json
[
  {
    "City": "Sacramento",
    "LandmarkCount": 2
  },
  {
    "City": "Saint Albans",
    "LandmarkCount": 5
  },
  {
    "City": "Saint Andrews",
    "LandmarkCount": 13
  },
  {
    "City": "Saint Annes Head",
    "LandmarkCount": 1
  },
// ...
```

(execution: 480.2ms docs: 138)

> [!NOTE]
> The `WHERE` clause is faster because `WHERE` gets processed _before_ any `GROUP BY` and doesn’t have access to aggregated values. `HAVING` gets processed _after_ `GROUP BY` and is used to constrain the resultset to only those with aggregated values.

Example 6\. Using an alias for a group term

```sqlpp
SELECT Hemisphere, COUNT(DISTINCT name) AS LandmarkCount
FROM landmark AS l
GROUP BY CASE
  WHEN l.geo.lon <0 THEN "West"
  ELSE "East"
END AS Hemisphere;
```

Results

```json
[
  {
    "Hemisphere": "East",
    "LandmarkCount": 459
  },
  {
    "Hemisphere": "West",
    "LandmarkCount": 3885
  }
]
```

> [!NOTE]
> The `CASE` expression categorizes each landmark into the Western hemisphere if its longitude is negative, or the Eastern hemisphere otherwise. The alias in the `GROUP BY` clause enables you to refer to the `CASE` expression in the `SELECT` clause.

## [](#related-links)Related Links

* For further examples, refer to [Group By and Aggregate Performance](groupby-aggregate-performance.md).