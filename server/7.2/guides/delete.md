[View original HTML](/server/7.2/guides/delete.html)

> How to delete documents using SQL++.  
> This guide is for Couchbase Server.

## [](#introduction)Introduction

To delete documents from a keyspace, you can use the DELETE statement or the MERGE statement.

If you want to try out the examples in this section, follow the instructions given in [Do a Quick Install](../getting-started/do-a-quick-install.md) to install Couchbase Server, configure a cluster, and load a sample dataset. Read the following for further information about the tools available for editing and executing queries:

* [cbq: The Command Line Shell for SQL++](../tools/cbq-shell.md)
* [Query Workbench](../tools/query-workbench.md)

|  | Please note that the examples in this guide will alter the data in your sample database. To restore your sample data, remove and reinstall the travel sample data. Refer to [Sample Buckets](../manage/manage-settings/install-sample-buckets.md) for details. |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#deleting-documents-by-key)Deleting Documents by Key

To delete one or more documents by key, use the DELETE statement with the USE KEYS hint:

1. Use the FROM keyword to specify the keyspace which contains the documents to be deleted.
2. Use the USE KEYS hint to specify a document keys or array of document keys.
3. If required, use the RETURNING clause to specify what should be returned when the documents are deleted.

You can combine this approach with the WHERE clause if necessary.

The following query deletes a document with the key `"airline_4444"` and returns the deleted document.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
DELETE FROM airline k
USE KEYS "airline_4444"
RETURNING k
```

Results

```json
[
  {
    "k": {
      "callsign": "MY-AIR",
      "country": "United States",
      "iata": "Z1",
      "icao": "AQZ",
      "name": "80-My Air",
      "id": "4444",
      "type": "airline"
    }
  }
]
```

For more information and examples, see [DELETE](../n1ql/n1ql-language-reference/delete.md).

## [](#deleting-documents-by-filter)Deleting Documents by Filter

To delete documents by filter, use the DELETE statement with the WHERE clause:

1. Use the FROM keyword to specify the keyspace which contains the documents to be deleted.
2. Use the WHERE clause to specify the condition that needs to be met for documents to be deleted.
3. If required, use the LIMIT clause to specify the greatest number of documents that may be deleted.
4. If required, use the RETURNING clause to specify what should be returned when the documents are deleted.

You can combine this approach with the USE KEYS hint if necessary.

The following query deletes any airline whose callsign is `"AIR-X"`, returning the content of the airline’s `id` field.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
DELETE FROM airline f
WHERE f.callsign = "AIR-X"
RETURNING f.id
```

Results

```json
[
  {
    "id": "4445"
  }
]
```

## [](#deleting-documents-by-subquery)Deleting Documents by Subquery

To delete documents based on the results returned by a SELECT query, use a subquery in the filter.

The following query finds the last city in alphanumeric order in the `airport` keyspace, and deletes any airports in that city.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
DELETE FROM airport
WHERE city IN (SELECT RAW MAX(t.city) FROM airport AS t)
RETURNING airportname;
```

Results

```json
[
  {
    "airportname": "√éle d'Yeu Airport"
  }
]
```

## [](#merging-and-deleting-documents)Merging and Deleting Documents

You can also delete documents by merging: in other words, by joining one keyspace to another, and deleting any documents that match.

To delete documents using a merge, use the MERGE statement with the DELETE action:

1. Use the INTO keyword to specify the target. This is the data source containing the documents to delete.
2. Use the USING keyword to specify the source. This is the data source to check against the target.
3. Use the ON keyword to specify the merge predicate. This is a condition that must be met to match an object in the source with an object in the target.
4. Use WHEN MATCHED THEN DELETE to specify that when a document in the source matches a document in the target, the document in the target should be deleted.
5. If necessary, use the WHERE clause to specify any further conditions that must be met for documents to be deleted.
6. If required, use the LIMIT clause to specify the greatest number of documents that may be deleted.
7. If required, use the RETURNING clause to specify what should be returned when the documents are deleted.

The following query finds all BA routes whose source airport is in France. If any flights are using equipment 319, they’re updated to use 797\. If any flights are using equipment 757, they’re deleted.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
MERGE INTO route
USING airport
ON route.sourceairport = airport.faa
WHEN MATCHED THEN UPDATE
  SET route.old_equipment = route.equipment,
      route.equipment = "797",
      route.updated = true
  WHERE airport.country = "France"
    AND route.airline = "BA"
    AND CONTAINS(route.equipment, "319")
WHEN MATCHED THEN DELETE
  WHERE airport.country = "France"
    AND route.airline = "BA"
    AND CONTAINS(route.equipment, "757")
RETURNING route.old_equipment, route.equipment, airport.faa;
```

Results

```json
[
  {
    "equipment": "763 757",
    "sourceairport": "CDG"
  },
  {
    "equipment": "797",
    "old_equipment": "734 319",
    "sourceairport": "BOD"
  },
  {
    "equipment": "797",
    "old_equipment": "319 320 321",
    "sourceairport": "CDG"
  },
  {
    "equipment": "797",
    "old_equipment": "319",
    "sourceairport": "LYS"
  },
  {
    "equipment": "797",
    "old_equipment": "319 320",
    "sourceairport": "MRS"
  },
  {
    "equipment": "797",
    "old_equipment": "319 320 734",
    "sourceairport": "NCE"
  },
  {
    "equipment": "797",
    "old_equipment": "319 320 321",
    "sourceairport": "NCE"
  },
  {
    "equipment": "797",
    "old_equipment": "319 320",
    "sourceairport": "ORY"
  },
  {
    "equipment": "797",
    "old_equipment": "320 319 321",
    "sourceairport": "TLS"
  }
]
```

For more information and examples, see [MERGE](../n1ql/n1ql-language-reference/merge.md).

## [](#related-links)Related Links

Reference and explanation:

* [DELETE](../n1ql/n1ql-language-reference/delete.md)
* [MERGE](../n1ql/n1ql-language-reference/merge.md)

Querying with SDKs:

* [C](../../../c-sdk/current/howtos/n1ql-queries-with-sdk.md)| [C++](../../../cxx-sdk/current/howtos/sqlpp-queries-with-sdk.md)| [.NET](../../../dotnet-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Go](../../../go-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Java](../../../java-sdk/current/howtos/sqlpp-queries-with-sdk.md)| [Kotlin](../../../kotlin-sdk/current/howtos/n1ql-queries.md)| [Node.js](../../../nodejs-sdk/current/howtos/n1ql-queries-with-sdk.md)| [PHP](../../../php-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Python](../../../python-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Ruby](../../../ruby-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Scala](../../../scala-sdk/current/howtos/sqlpp-queries-with-sdk.md)