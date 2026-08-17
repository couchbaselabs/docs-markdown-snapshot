---
title: WHERE clause
description: The WHERE clause filters resultsets based specified conditions.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/n1ql/pages/n1ql-language-reference/where.adoc
  xref: xref:7.2@server:n1ql:n1ql-language-reference/where.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/n1ql/n1ql-language-reference/where.html)

# WHERE clause

> The `WHERE` clause filters resultsets based specified conditions. 

## [](#purpose)Purpose

When you want to narrow down your resultset by one or more criteria, use the `WHERE` clause to filter your resultset.

## [](#syntax)Syntax

```ebnf
where-clause ::= 'WHERE' cond
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/where-clause.png) 

## [](#arguments)Arguments

cond

\[Required\] Conditional expression that represents a filter to be applied to the resultset. Records for which the condition resolves to TRUE are propagated to the resultset.

You can construct complex conditional expressions, for example by using the [logical operators](logicalops.md) `AND`, `OR`, and `NOT`.

## [](#examples%5Fsection)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Example 1\. Use WHERE filter the resultset

To list only airports that are in France, use the `WHERE` clause for the "country" field.

```sqlpp
SELECT airportname, city, country
FROM airport
WHERE country = "France"
LIMIT 4;
```

Results

```json
[
  {
    "airportname": "Calais Dunkerque",
    "city": "Calais",
    "country": "France"
  },
  {
    "airportname": "Peronne St Quentin",
    "city": "Peronne",
    "country": "France"
  },
  {
    "airportname": "Les Loges",
    "city": "Nangis",
    "country": "France"
  },
  {
    "airportname": "Couterne",
    "city": "Bagnole-de-l'orne",
    "country": "France"
  }
]
```

Example 2\. Use WHERE and OR to filter the resultset

List only the landmarks that start with the letter "C" or "K". Note that the first position of the `SUBSTR` function is `0`.

```sqlpp
SELECT name
FROM landmark
WHERE CONTAINS(SUBSTR(name,0,1),"C")
   OR CONTAINS(SUBSTR(name,0,1),"K")
LIMIT 4;
```

Results

```json
[
  {
    "name": "City Chambers"
  },
  {
    "name": "Kingston Bridge"
  },
  {
    "name": "Clyde Arc"
  },
  {
    "name": "Clyde Auditorium"
  }
]
```

Example 3\. Use WHERE, AND and NOT to filter the resultset

List landmark restaurants, except Thai restaurants.

```sqlpp
SELECT name, activity
FROM landmark
WHERE activity = "eat"
AND NOT CONTAINS(name,"Thai")
LIMIT 4;
```

Results

```json
[
  {
    "activity": "eat",
    "name": "Hollywood Bowl"
  },
  {
    "activity": "eat",
    "name": "Spice Court"
  },
  {
    "activity": "eat",
    "name": "Beijing Inn"
  },
  {
    "activity": "eat",
    "name": "Ossie's Fish and Chips"
  }
]
```