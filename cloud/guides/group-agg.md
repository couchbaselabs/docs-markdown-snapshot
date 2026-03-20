---
title: Calculate Aggregates and Group Results
description: How to calculate aggregates and group the results.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/guides/pages/group-agg.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:cloud:guides:group-agg.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/guides/group-agg.html)

# Calculate Aggregates and Group Results

> How to calculate aggregates and group the results. 

## [](#introduction)Introduction

You can use aggregate functions to perform calculations over multiple values. Grouping enables you to display the results in groups.

If you want to try out the examples in this section, follow the instructions given in [Create an Account and Deploy Your Free Tier Operational Cluster](../get-started/create-account.md) to create a free account, deploy a cluster, and load a sample dataset. Read the following for further information about the tools available for editing and executing queries:

* [cbq: The Command Line Shell for SQL++](../n1ql/n1ql-intro/cbq.md)
* [Query Tab](../clusters/query-service/query-workbench.md)

## [](#aggregate-functions)Aggregate Functions

To take multiple values from documents, perform calculations, and return a single value as the result, use an aggregate function, such as [AVG()](../n1ql/n1ql-language-reference/aggregatefun.md#avg), [COUNT()](../n1ql/n1ql-language-reference/aggregatefun.md#count), [MIN()](../n1ql/n1ql-language-reference/aggregatefun.md#min), [MAX()](../n1ql/n1ql-language-reference/aggregatefun.md#max), or [SUM()](../n1ql/n1ql-language-reference/aggregatefun.md#sum).

For example, the following query finds the average altitude of airports in the airport keyspace.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
SELECT AVG(geo.alt) AS AverageAltitude FROM airport;
```

Results

```json
[
  {
    "AverageAltitude": 870.1651422764228
  }
]
```

For more information and examples, see [Aggregate Functions](../n1ql/n1ql-language-reference/aggregatefun.md).

### [](#aggregating-distinct-values)Aggregating Distinct Values

To aggregate all values, omit the aggregate quantifier, or optionally include the `ALL` keyword before the function arguments.

For example, the following query finds the average number of stops per route.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
SELECT AVG(ALL stops) AS AvgAllStops FROM route;
```

Results

```json
[
  {
    "AvgAllStops": 0.0002
  }
]
```

Results in 0.0002 since nearly all routes have 0 stops.

To aggregate distinct values only, include the `DISTINCT` keyword before the function arguments.

For example, the following query finds the average of the distinct numbers of stops.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
SELECT AVG(DISTINCT stops) AS AvgDistinctStops FROM route;
```

Results

```json
[
  {
    "AvgDistinctStops": 0.5
  }
]
```

Results in 0.5 since the routes contain only 1 or 0 stops.

For more information, see [Aggregate Quantifier](../n1ql/n1ql-language-reference/aggregatefun.md#aggregate-quantifier).

### [](#filtering-the-aggregates)Filtering the Aggregates

To filter the values used by an aggregate function, use the FILTER clause after the function.

For example, the following query finds the minimum value of a string field, only including strings that start with `"A"` or greater.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
SELECT MIN(name) FILTER (WHERE SUBSTR(name,0)>="A") AS MinName
FROM hotel;
```

Results

```json
[
  {
    "MinName": "AIRE NATURELLE LE GROZEAU Aire naturelle"
  }
]
```

For more information, see [FILTER Clause](../n1ql/n1ql-language-reference/aggregatefun.md#filter-clause).

## [](#grouping-the-results)Grouping the Results

By default, an aggregate function returns a single result for all the documents that the query selects. It’s often more useful to group the documents (by a different field) and return the aggregate result for each group.

To group the results of an aggregate query, use the GROUP BY clause.

For example, the following query groups unique landmarks by city.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

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

For more information and examples, see [GROUP BY Clause](../n1ql/n1ql-language-reference/groupby.md).

### [](#filtering-the-groups)Filtering the Groups

To filter the groups by an aggregate function, use the HAVING clause within the GROUP BY clause.

For example, the following query groups unique landmarks by city, and specifies cities that have more than 180 landmarks.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

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

For more information and examples, see [HAVING Clause](../n1ql/n1ql-language-reference/groupby.md#having-clause).

### [](#defining-an-expression-within-the-group-by-clause)Defining an Expression within the GROUP BY Clause

To define an expression for use within the GROUP BY clause, use the LETTING clause before the HAVING clause.

For example, the following clause uses an expression to define the minimum number of landmarks for each city.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

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

For more information and examples, see [LETTING Clause](../n1ql/n1ql-language-reference/groupby.md#letting-clause).

## [](#related-links)Related Links

Reference and explanation:

* [Aggregate Functions](../n1ql/n1ql-language-reference/aggregatefun.md)
* [GROUP BY Clause](../n1ql/n1ql-language-reference/groupby.md)

Tutorials:

* [SQL++ Query Language Tutorial](https://query-tutorial.couchbase.com/tutorial/#1)

Querying with SDKs:

* [C](../../c-sdk/current/howtos/n1ql-queries-with-sdk.md)| [C++](../../cxx-sdk/current/howtos/sqlpp-queries-with-sdk.md)| [.NET](../../dotnet-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Go](../../go-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Java](../../java-sdk/current/howtos/sqlpp-queries-with-sdk.md)| [Kotlin](../../kotlin-sdk/current/howtos/n1ql-queries.md)| [Node.js](../../nodejs-sdk/current/howtos/n1ql-queries-with-sdk.md)| [PHP](../../php-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Python](../../python-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Ruby](../../ruby-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Rust](../../rust-sdk/current/howtos/sqlpp-queries-with-sdk.md)| [Scala](../../scala-sdk/current/howtos/sqlpp-queries-with-sdk.md)