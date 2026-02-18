---
title: Modifying Data with SQL++
description: How to modify documents using SQL++.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/guides/pages/update.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/guides/update.html)

# Modifying Data with SQL++

> How to modify documents using SQL++.  
> This guide is for Couchbase Server.

## [](#introduction)Introduction

To modify documents in a keyspace, you can use the UPDATE statement or the MERGE statement.

If you want to try out the examples in this section, follow the instructions given in [Do a Quick Install](../getting-started/do-a-quick-install.md) to install Couchbase Server, configure a cluster, and load a sample dataset. Read the following for further information about the tools available for editing and executing queries:

* [cbq: The Command Line Shell for SQL++](../tools/cbq-shell.md)
* [Query Workbench](../tools/query-workbench.md)

> [!WARNING]
> Please note that the examples in this guide will alter the data in your sample database. To restore your sample data, remove and reinstall the travel sample data. Refer to [Sample Buckets](../manage/manage-settings/install-sample-buckets.md) for details.

## [](#modifying-documents-by-key)Modifying Documents by Key

To modify one or more documents by key, use the UPDATE statement with the USE KEYS hint:

1. Use the FROM keyword to specify the keyspace which contains the documents to be modified.
2. Use the USE KEYS hint to specify a document keys or array of document keys.
3. Use the SET and UNSET clauses to set and unset attributes as required.
4. If required, use the RETURNING clause to specify what should be returned when the documents are deleted.

You can combine this approach with the WHERE clause if necessary.

The following query adds an attribute to a document with the key `"landmark_10090"` and returns the added attribute.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
UPDATE landmark
USE KEYS "landmark_10090"
SET nickname = "Squiggly Bridge"
RETURNING landmark.nickname;
```

Results

```json
[
  {
    "nickname": "Squiggly Bridge"
  }
]
```

The following query removes an attribute from a document with the key `"landmark_10090"` and returns the `name` attribute.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
UPDATE landmark
USE KEYS "landmark_10090"
UNSET nickname
RETURNING landmark.name;
```

Results

```json
[
  {
    "name": "Tradeston Pedestrian Bridge"
  }
]
```

## [](#modifying-documents-by-filter)Modifying Documents by Filter

To modify documents by filter, use the UPDATE statement with the WHERE clause:

1. Use the FROM keyword to specify the keyspace which contains the documents to be modified.
2. Use the SET and UNSET clauses to set and unset attributes as required.
3. Use the WHERE clause to specify the condition that needs to be met for documents to be modified.
4. If required, use the LIMIT clause to specify the greatest number of documents that may be modified.
5. If required, use the RETURNING clause to specify what should be returned when the documents are modified.

You can combine this approach with the USE KEYS hint if necessary.

The following query standardizes the capitalization of the `city` field for all airports in San Francisco.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
UPDATE airport
SET city = "San Francisco"
WHERE lower(city) = "san francisco"
RETURNING *;
```

Results

```json
[
  {
    "airport": {
      "airportname": "San Francisco Intl",
      "city": "San Francisco",
      "country": "United States",
      "faa": "SFO",
      "geo": {
        "alt": 13,
        "lat": 37.618972,
        "lon": -122.374889
      },
      "icao": "KSFO",
      "id": 3469,
      "type": "airport",
      "tz": "America/Los_Angeles"
    }
  }
]
```

## [](#modifying-documents-by-subquery)Modifying Documents by Subquery

To modify documents based on the results returned by a SELECT query, use a subquery in the filter.

The following query adds an attribute to the airport whose FAA code is `NCE`, containing a list of every hotel in Nice.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
UPDATE airport AS a
SET hotels =
  (SELECT  h.name, h.id
  FROM  hotel AS h
  WHERE h.city = "Nice")
WHERE a.faa ="NCE"
RETURNING a;
```

Results

```json
[
  {
    "a": {
      "airportname": "Cote D\\'Azur",
      "city": "Nice",
      "country": "France",
      "faa": "NCE",
      "geo": {
        "alt": 12,
        "lat": 43.658411,
        "lon": 7.215872
      },
      "hotels": [
        {
          "id": 20419,
          "name": "Best Western Hotel Riviera Nice"
        },
        {
          "id": 20420,
          "name": "Hotel Anis"
        },
        {
          "id": 20421,
          "name": "NH Nice"
        },
        {
          "id": 20422,
          "name": "Hotel Suisse"
        },
        {
          "id": 20423,
          "name": "Gounod"
        },
        {
          "id": 20424,
          "name": "Grimaldi Hotel Nice"
        },
        {
          "id": 20425,
          "name": "Negresco"
        }
      ],
      "icao": "LFMN",
      "id": 1354,
      "type": "airport",
      "tz": "Europe/Paris"
    }
  }
]
```

## [](#modifying-nested-arrays-and-objects)Modifying Nested Arrays and Objects

To modify nested objects in an array, use the FOR clause within the SET or UNSET clause.

1. Use the FOR keyword to specify a dummy variable that refers to each object in the array.
2. Use the IN keyword to specify the path to the array.
3. If required, use the WHEN clause to filter the objects in the array.

The following query adds an attribute to each object in the `schedule` array in document `"landmark_10090"`.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
UPDATE route t
USE KEYS "route_10003"
SET s.codeshare = NULL FOR s IN schedule END
RETURNING t;
```

Results

```json
[
  {
    "t": {
      "airline": "AF",
      "airlineid": "airline_137",
      "destinationairport": "ATL",
      "distance": 654.9546621929924,
      "equipment": "757 739",
      "id": 10003,
      "schedule": [
        {
          "codeshare": null,
          "day": 0,
          "flight": "AF986",
          "utc": "22:26:00"
        },
        {
          "codeshare": null,
          "day": 0,
          "flight": "AF962",
          "utc": "04:25:00"
        },
// ...
      ],
      "sourceairport": "TPA",
      "stops": 0,
      "type": "route"
    }
  }
]
```

### [](#using-object-functions-and-array-functions)Using Object Functions and Array Functions

To modify an object attribute, use an object function. Similarly, to modify an array attribute, use an array function.

The following query adds an attribute to the `ratings` object within each review in document `"landmark_10025"`.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
UPDATE hotel AS h USE KEYS "hotel_10025"
SET i.ratings = OBJECT_ADD(i.ratings, "new", "new_value" ) FOR i IN reviews END
RETURNING h.reviews[*].ratings;
```

Results

```json
[
  {
    "ratings": [
      {
        "Cleanliness": 5,
        "Location": 4,
        "Overall": 4,
        "Rooms": 3,
        "Service": 5,
        "Value": 4,
        "new": "new_value"
      },
      {
        "Business service (e.g., internet access)": 4,
        "Check in / front desk": 4,
        "Cleanliness": 4,
        "Location": 4,
        "Overall": 4,
        "Rooms": 3,
        "Service": 3,
        "Value": 5,
        "new": "new_value"
      }
    ]
  }
]
```

For more information and examples, see [Object Functions](../n1ql/n1ql-language-reference/objectfun.md) and [Array Functions](../n1ql/n1ql-language-reference/arrayfun.md).

### [](#using-the-array-operator)Using the ARRAY Operator

Alternatively, to access deeply nested attributes, use the ARRAY operator.

The following query removes an attribute from the `ratings` object within each review in document `"landmark_10025"`.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
UPDATE hotel AS h USE KEYS "hotel_10025"
UNSET i.new FOR i IN
  (ARRAY j.ratings FOR j IN reviews END)
END
RETURNING h.reviews[*].ratings;
```

Results

```json
[
  {
    "ratings": [
      {
        "Cleanliness": 5,
        "Location": 4,
        "Overall": 4,
        "Rooms": 3,
        "Service": 5,
        "Value": 4
      },
      {
        "Business service (e.g., internet access)": 4,
        "Check in / front desk": 4,
        "Cleanliness": 4,
        "Location": 4,
        "Overall": 4,
        "Rooms": 3,
        "Service": 3,
        "Value": 5
      }
    ]
  }
]
```

For more information and examples, see [ARRAY](../n1ql/n1ql-language-reference/collectionops.md#array).

## [](#merging-and-updating-documents)Merging and Updating Documents

You can also update documents by merging: in other words, by joining one data source to another, and updating any documents that match.

To update documents using a merge, use the MERGE statement with the UPDATE action:

1. Use the INTO keyword to specify the target. This is the data source in which documents will be updated.
2. Use the USING keyword to specify the source. This is the data source to check against the target.
3. Use the ON keyword to specify the merge predicate. This is a condition that must be met to match an object in the source with an object in the target.
4. Use WHEN MATCHED THEN UPDATE to specify that when a document in the source matches a document in the target, the document in the target should be updated.

  1. Use the SET and UNSET clauses to set and unset attributes as required.
  2. If necessary, use the WHERE clause to specify any further conditions that must be met for documents to be updated.
5. If required, use the LIMIT clause to specify the greatest number of documents that may be updated.
6. If required, use the RETURNING clause to specify what should be returned when the documents are updated.

The following query compares a source set of hotel data with the target `hotel` keyspace. If the hotel already exists in the `hotel` keyspace, the record is updated, and the query returns the target document key and the attributes which were changed.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
MERGE INTO hotel t
USING [
  {"id":"21728", "vacancy": true},
  {"id":"21730", "vacancy": true}
] source
ON meta(t).id = "hotel_" || source.id
WHEN MATCHED THEN
  UPDATE SET t.old_vacancy = t.vacancy,
             t.vacancy = source.vacancy
RETURNING meta(t).id, t.old_vacancy, t.vacancy;
```

Results

```json
[
  {
    "id": "hotel_21728",
    "old_vacancy": false,
    "vacancy": true
  },
  {
    "id": "hotel_21730",
    "old_vacancy": true,
    "vacancy": true
  }
]
```

For more information and examples, see [MERGE](../n1ql/n1ql-language-reference/merge.md).

## [](#related-links)Related Links

Reference and explanation:

* [UPDATE](../n1ql/n1ql-language-reference/update.md)
* [MERGE](../n1ql/n1ql-language-reference/merge.md)

Querying with SDKs:

* [C](../../../c-sdk/current/howtos/n1ql-queries-with-sdk.md)| [C++](../../../cxx-sdk/current/howtos/sqlpp-queries-with-sdk.md)| [.NET](../../../dotnet-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Go](../../../go-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Java](../../../java-sdk/current/howtos/sqlpp-queries-with-sdk.md)| [Kotlin](../../../kotlin-sdk/current/howtos/n1ql-queries.md)| [Node.js](../../../nodejs-sdk/current/howtos/n1ql-queries-with-sdk.md)| [PHP](../../../php-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Python](../../../python-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Ruby](../../../ruby-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Scala](../../../scala-sdk/current/howtos/sqlpp-queries-with-sdk.md)