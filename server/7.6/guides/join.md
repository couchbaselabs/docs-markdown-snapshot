---
title: Query Across Relationships
description: How to join data sources for a SQL++ selection query.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/guides/pages/join.adoc
  xref: xref:7.6@server:guides:join.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/guides/join.html)

# Query Across Relationships

> How to join data sources for a SQL++ selection query. 

## [](#introduction)Introduction

You can use a join to read objects from one data source, combine them with corresponding objects from another data source, and return the joined objects. The first data source is said to be on the left-hand side of the join and the second is said to be on the right-hand side of the join.

If you want to try out the examples in this section, follow the instructions given in [Do a Quick Install](../getting-started/do-a-quick-install.md) to install Couchbase Server, configure a cluster, and load a sample dataset. Read the following for further information about the tools available for editing and executing queries:

* [cbq: The Command Line Shell for SQL++](../n1ql/n1ql-intro/cbq.md)
* [Query Workbench](../tools/query-workbench.md)

## [](#creating-a-join)Creating a Join

SQL++ offers several types of join syntax. This guide focuses on ANSI join, which is the recommended join syntax. It enables you to join one data source to another using arbitrary fields.

To create a join:

1. Use the FROM clause to specify the data source on the left-hand side of the join. This may be a keyspace identifier, a subquery, or a generic expression.
2. Use the JOIN clause to specify the data source on the right-hand side of the join. For ANSI joins, this may be a keyspace identifier, a subquery, or a generic expression.
3. Use the ON keyword to specify the join predicate. This is a condition that must be met to join an object on the right-hand side to an object on the left-hand side.

> [!TIP]
> To use a [document key](../learn/data/data.md#keys) in the join predicate, use the [META()](../n1ql/n1ql-language-reference/metafun.md#meta) function to return the `id` field from the document metadata.

For example, the following query selects a route and the associated airline.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
SELECT *
FROM route r (1)
JOIN airline a (2)
ON r.airlineid = META(a).id (3)
LIMIT 1;
```

| **1** | The route keyspace is the left-hand side of the join.                                               |
| ----- | --------------------------------------------------------------------------------------------------- |
| **2** | The airline keyspace is the right-hand side of the join.                                            |
| **3** | The airlineid field on the left-hand side must be equal to the document key on the right-hand side. |

For more information and examples, see [ANSI JOIN Clause](../n1ql/n1ql-language-reference/join.md#section%5Fek1%5Fjnx%5F1db).

## [](#join-types)Join Types

ANSI joins support three types of join: inner joins, left outer joins, and right outer joins.

### [](#inner-joins)Inner Joins

The default join is an inner join. An inner join returns joined objects only where a source object from the left-hand side of the join matches a source object from the right-hand side of the join.

![Inner join: the result contains only matching objects from the left-hand side and right-hand side](_images/inner-join.png) 

To create an inner join, omit the join type, or optionally include the `INNER` keyword before the JOIN clause.

For example, the following query lists all the source airports and airlines that fly into San Francisco.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
SELECT route.airlineid, airline.name, route.sourceairport, route.destinationairport
FROM route
INNER JOIN airline
ON route.airlineid = META(airline).id
WHERE route.destinationairport = "SFO"
ORDER BY route.sourceairport;
```

Results

```json
[
  {
    "airlineid": "airline_5209",
    "destinationairport": "SFO",
    "name": "United Airlines",
    "sourceairport": "ABQ"
  },
  {
    "airlineid": "airline_5209",
    "destinationairport": "SFO",
    "name": "United Airlines",
    "sourceairport": "ACV"
  },
  {
    "airlineid": "airline_5209",
    "destinationairport": "SFO",
    "name": "United Airlines",
    "sourceairport": "AKL"
  },
// ...
```

### [](#left-outer-joins)Left Outer Joins

A left outer join returns joined objects using all the source objects from the left-hand side of the join, but only including source objects from the right-hand side of the join if they match.

![Left outer join: the result contains all objects from the left-hand side, and only matching objects from the right-hand side](_images/left-join.png) 

To create a left outer join, include the `LEFT` or `LEFT OUTER` keywords before the JOIN clause.

For example, the following query lists all airports in the United States, and for each airport gives the first listed landmark in the same city, if any.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
SELECT DISTINCT  MIN(aport.airportname) AS Airport__Name,
                 MIN(aport.tz) AS Airport__Time,
                 MIN(lmark.name) AS Landmark_Name
FROM airport aport (1)
LEFT JOIN landmark lmark (2)
  ON aport.city = lmark.city
  AND lmark.country = "United States"
GROUP BY aport.airportname
ORDER BY aport.airportname
LIMIT 4;
```

| **1** | The airport keyspace is on the left-hand side of the join.   |
| ----- | ------------------------------------------------------------ |
| **2** | The landmark keyspace is on the right-hand side of the join. |

Results

```json
[
  {
    "Airport__Name": "Abbeville",
    "Airport__Time": "Europe/Paris",
    "Landmark_Name": null (1)
  },
  {
    "Airport__Name": "Aberdeen Regional Airport",
    "Airport__Time": "America/Chicago",
    "Landmark_Name": null
  },
  {
    "Airport__Name": "Abilene Rgnl",
    "Airport__Time": "America/Chicago",
    "Landmark_Name": null
  },
  {
    "Airport__Name": "Abraham Lincoln Capital",
    "Airport__Time": "America/Chicago",
    "Landmark_Name": null
  }
]
```

| **1** | If there is no corresponding data object on the right-hand side of the join, fields from the right-hand side are missing or null. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------- |

### [](#right-outer-joins)Right Outer Joins

A right outer join returns joined objects using all the source objects from the right-hand side of the join, but only including source objects from the left-hand side of the join if they match.

![Right outer join: the result contains only matching objects from the left-hand side, and all objects from the right-hand side](_images/right-join.png) 

To create a right outer join, include the `RIGHT` or `RIGHT OUTER` keywords before the JOIN clause.

For example, the following query lists all landmarks in the United States, and for each landmark gives the first listed airport in the same city, if any.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
SELECT DISTINCT MIN(aport.airportname) AS Airport__Name,
                MIN(aport.tz) AS Airport__Time,
                MIN(lmark.name) AS Landmark_Name,
FROM airport aport (1)
RIGHT JOIN landmark lmark (2)
  ON aport.city = lmark.city
  AND aport.country = "United States"
GROUP BY lmark.name
ORDER BY lmark.name
LIMIT 4;
```

| **1** | The airport keyspace is on the left-hand side of the join.   |
| ----- | ------------------------------------------------------------ |
| **2** | The landmark keyspace is on the right-hand side of the join. |

Results

```json
[
  {
    "Airport__Name": "San Francisco Intl",
    "Airport__Time": "America/Los_Angeles",
    "Landmark_Name": "&quot;Hippie Temptation&quot; house"
  },
  {
    "Airport__Name": null, (1)
    "Airport__Time": null,
    "Landmark_Name": "'The Argyll Arms Hotel"
  },
  {
    "Airport__Name": null,
    "Airport__Time": null,
    "Landmark_Name": "'Visit the Hut of the Shadows and other End of the Road sculptures"
  },
  {
    "Airport__Name": "London-Corbin Airport-MaGee Field",
    "Airport__Time": "America/New_York",
    "Landmark_Name": "02 Shepherd's Bush Empire"
  }
]
```

| **1** | If there is no corresponding data object on the left-hand side of the join, fields from the left-hand side are missing or null. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------- |

## [](#chaining-joins)Chaining Joins

To chain joins, nests, and unnests, use the right-hand side of one JOIN, NEST, or UNNEST clause as the left-hand side of the next.

For example, the following query joins routes to airports by destination airport, and then nests landmarks in the same city as each airport.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
SELECT *
FROM route AS rte (1)
JOIN airport AS apt (2)
  ON rte.destinationairport = apt.faa
NEST landmark AS lmk (3)
  ON apt.city = lmk.city
LIMIT 5;
```

| **1** | The route keyspace is on the left-hand side of the join.                                       |
| ----- | ---------------------------------------------------------------------------------------------- |
| **2** | The airport keyspace is on the right-hand side of the join and the left-hand side of the nest. |
| **3** | The landmark keyspace is on the right-hand side of the nest.                                   |

For more information and examples, see [Left-Hand Side](../n1ql/n1ql-language-reference/join.md#section%5Fnkd%5F3nx%5F1db) for the JOIN clause.

## [](#related-links)Related Links

Reference and explanation:

* [JOIN Clause](../n1ql/n1ql-language-reference/join.md)

Tutorials:

* [SQL++ Query Language Tutorial](https://query-tutorial.couchbase.com/tutorial/#1)

Querying with SDKs:

* [C](../../../c-sdk/current/howtos/n1ql-queries-with-sdk.md)| [C++](../../../cxx-sdk/current/howtos/sqlpp-queries-with-sdk.md)| [.NET](../../../dotnet-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Go](../../../go-sdk/current/howtos/sqlpp-queries-with-sdk.md)| [Java](../../../java-sdk/current/howtos/sqlpp-queries-with-sdk.md)| [Kotlin](../../../kotlin-sdk/current/howtos/n1ql-queries.md)| [Node.js](../../../nodejs-sdk/current/howtos/n1ql-queries-with-sdk.md)| [PHP](../../../php-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Python](../../../python-sdk/current/howtos/sqlpp-queries-with-sdk.md)| [Ruby](../../../ruby-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Rust](../../../rust-sdk/current/howtos/sqlpp-queries-with-sdk.md)| [Scala](../../../scala-sdk/current/howtos/sqlpp-queries-with-sdk.md)