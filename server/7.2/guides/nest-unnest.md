---
title: Nesting and Unnesting Documents
description: How to nest and unnest arrays of embedded objects.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/guides/pages/nest-unnest.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:guides:nest-unnest.adoc[]
---

[View original HTML](/server/7.2/guides/nest-unnest.html)

# Nesting and Unnesting Documents

> How to nest and unnest arrays of embedded objects.  
> This guide is for Couchbase Server.

## [](#introduction)Introduction

Couchbase Server is a document database. Data is stored as JSON documents in keyspaces, rather than as rows in tables. This means that documents can contain arrays of embedded Sub-Documents. SQL++ provides syntax which enables you to nest (create) or unnest (flatten) arrays of embedded documents in a query.

If you want to try out the examples in this section, follow the instructions given in [Do a Quick Install](../getting-started/do-a-quick-install.md) to install Couchbase Server, configure a cluster, and load a sample dataset. Read the following for further information about the tools available for editing and executing queries:

* [cbq: The Command Line Shell for SQL++](../tools/cbq-shell.md)
* [Query Workbench](../tools/query-workbench.md)

## [](#nesting-data)Nesting Data

Nesting is like creating a join from a document to documents from another data source. However, in the resultset, the nested documents are embedded in an array within the parent document.

SQL++ offers several types of nest syntax. This guide focuses on ANSI nest, which is the recommended nest syntax. It enables you to nest objects from one data source within objects from another, using arbitrary fields.

To create a nest:

1. Use the FROM clause to specify the data source on the left-hand side of the nest. This may be a keyspace identifier, a subquery, or a subquery.
2. Use the NEST clause to specify the data source on the right-hand side of the nest. This must be a keyspace reference.
3. Use the ON keyword to specify the nest predicate. This is a condition that must be met in order to nest an object on the right-hand side within an object on the left-hand side.

> [!TIP]
> To use a [document key](../learn/data/data.md#keys) in the nest predicate, use the [META()](../n1ql/n1ql-language-reference/metafun.md#meta) function to return the `id` field from the document metadata.

For example, the following query selects a route and the associated airline.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
SELECT *
FROM route r (1)
NEST airline a (2)
ON r.airlineid = META(a).id (3)
LIMIT 1;
```

| **1** | The route keyspace is the left-hand side of the nest.                                               |
| ----- | --------------------------------------------------------------------------------------------------- |
| **2** | The airline keyspace is the right-hand side of the nest.                                            |
| **3** | The airlineid field on the left-hand side must be equal to the document key on the right-hand side. |

> [!NOTE]
> Before running a query containing a nest, make sure all the required indexes exist. To check which indexes may be required, use the [Index Advisor](../n1ql/n1ql-language-reference/advise.md).

For more information and examples, see [ANSI NEST Clause](../n1ql/n1ql-language-reference/nest.md#section%5Ftc1%5Fnnx%5F1db).

## [](#nest-types)Nest Types

ANSI nests support two types of nest: inner nests and left outer nests. (SQL++ cannot support right outer nests, because objects from the right-hand side cannot be nested within an object that does not exist.)

### [](#inner-nests)Inner Nests

The default nest type is an inner nest. An inner nest returns nested objects only where a source object from the left-hand side of the nest matches a source object from the right-hand side of the nest.

![Inner nest: the result contains only matching objects from the left-hand side and right-hand side](_images/inner-nest.png) 

To create an inner nest, omit the nest type, or optionally include the `INNER` keyword before the NEST clause.

For example, the following query lists only airports in Toulouse which have routes starting from them, and nests details of the routes.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

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

```json
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

### [](#left-outer-nests)Left Outer Nests

A left outer nest returns nested objects using all the source objects from the left-hand side of the nest, but only including source objects from the right-hand side of the nest if they match.

![Left outer nest: the result contains all objects from the left-hand side, and only matching objects from the right-hand side](_images/left-nest.png) 

To create a left outer nest, include the `LEFT` or `LEFT OUTER` keywords before the NEST clause.

For example, the following query lists all airports in Toulouse, and nests details of any routes that start from each airport.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

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

```json
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

| **1** | If there is no corresponding data object on the right-hand side of the nest, fields from the right-hand side are missing or null. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------- |

## [](#unnesting-data)Unnesting Data

Unnesting data is the opposite of nesting. Unnesting is like creating a join from a parent document to Sub-Documents in an array within that document. In the resultset, the Sub-Documents are flattened and joined to the parent document.

![Unnest: the result contains Sub-Documents flattened and joined to their parent documents](_images/unnest.png) 

To unnest Sub-Documents from an array:

1. Use the FROM clause to specify the parent data source on the left-hand side of the unnest.
2. Use the UNNEST clause to specify the nested data on the right-hand side of the unnest.

For example, the following query unnests the schedule data from within the route document to get details of flights on Monday (day `1`).

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
SELECT route.sourceairport, route.destinationairport, sched.flight, sched.utc
FROM route
UNNEST schedule sched
WHERE  sched.day = 1
LIMIT 3;
```

Results

```json
[
  {
    "destinationairport": "MRS",
    "flight": "AF356",
    "sourceairport": "TLV",
    "utc": "12:40:00"
  },
  {
    "destinationairport": "MRS",
    "flight": "AF480",
    "sourceairport": "TLV",
    "utc": "08:58:00"
  },
  {
    "destinationairport": "MRS",
    "flight": "AF250",
    "sourceairport": "TLV",
    "utc": "12:59:00"
  }
]
```

For more information and examples, see [UNNEST Clause](../n1ql/n1ql-language-reference/unnest.md).

## [](#chaining-nests-and-unnests)Chaining Nests and Unnests

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

For more information, see [Left-Hand Side](../n1ql/n1ql-language-reference/nest.md#from-term) for NEST clauses, or [Left-Hand Side](../n1ql/n1ql-language-reference/unnest.md#from-term) for UNNEST clauses.

## [](#related-links)Related Links

Reference and explanation:

* [NEST Clause](../n1ql/n1ql-language-reference/nest.md)
* [UNNEST Clause](../n1ql/n1ql-language-reference/unnest.md)

Tutorials:

* [SQL++ Query Language Tutorial](https://query-tutorial.couchbase.com/tutorial/#1)

Querying with SDKs:

* [C](../../../c-sdk/current/howtos/n1ql-queries-with-sdk.md)| [C++](../../../cxx-sdk/current/howtos/sqlpp-queries-with-sdk.md)| [.NET](../../../dotnet-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Go](../../../go-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Java](../../../java-sdk/current/howtos/sqlpp-queries-with-sdk.md)| [Kotlin](../../../kotlin-sdk/current/howtos/n1ql-queries.md)| [Node.js](../../../nodejs-sdk/current/howtos/n1ql-queries-with-sdk.md)| [PHP](../../../php-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Python](../../../python-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Ruby](../../../ruby-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Scala](../../../scala-sdk/current/howtos/sqlpp-queries-with-sdk.md)