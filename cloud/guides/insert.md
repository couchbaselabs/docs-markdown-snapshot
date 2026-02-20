---
title: Insert Data with a Query
description: How to insert documents using SQL++.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/guides/pages/insert.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:guides:insert.adoc[]
---

[View original HTML](/cloud/guides/insert.html)

# Insert Data with a Query

> How to insert documents using SQL++. 

## [](#introduction)Introduction

To insert documents in a keyspace, you can use the INSERT statement, the UPSERT statement, or the MERGE statement.

If you want to try out the examples in this section, follow the instructions given in [Create an Account and Deploy Your Free Tier Operational Cluster](../get-started/create-account.md) to create a free account, deploy a cluster, and load a sample dataset. Read the following for further information about the tools available for editing and executing queries:

* [cbq: The Command Line Shell for SQL++](../n1ql/n1ql-intro/cbq.md)
* [Query Tab](../clusters/query-service/query-workbench.md)

> [!WARNING]
> Please note that the examples in this guide will alter the data in your sample database. To restore your sample data, remove and reinstall the travel sample data. Refer to [Import Data with the Capella UI](../clusters/data-service/import-data-documents.md) for details.

## [](#inserting-a-document)Inserting a Document

To insert a document by providing the value, use the INSERT statement with the VALUES clause:

1. Use the INTO keyword to specify the keyspace into which the document is inserted.
2. Optionally, use the bracketed KEY and VALUE keywords to specify that you’re inserting a document key and body.
3. Use the VALUES clause to specify the document key and the body of the document.
4. If required, use the RETURNING clause specifies what the query returns when the document is inserted.

The following query creates a document in the `airline` keyspace.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
INSERT INTO airline (KEY,VALUE)
  VALUES ( "1025",
            {     "callsign": "MY-AIR",
                  "country": "United States",
                  "iata": "Z1",
                  "icao": "AQZ",
                  "id": "1011",
                  "name": "80-My Air",
                  "type": "airline"
            } )
RETURNING *;
```

Results

```json
{
  "requestID": "c3bd0276-5d7d-425f-98f9-b333b9ae4302",
  "signature": {
      "*": "*"
  },
  "results": [
  {
      "airline": {
          "callsign": "MY-AIR",
          "country": "United States",
          "iata": "Z1",
          "icao": "AQZ",
          "id": "1011",
          "name": "80-My Air",
          "type": "airline"
      }
  }
  ],
  "status": "success",
  "metrics": {
      "elapsedTime": "5.9133ms",
      "executionTime": "5.6264ms",
      "resultCount": 1,
      "resultSize": 254,
      "serviceLoad": 4,
      "mutationCount": 1
  }
}
```

For more information and examples, see [INSERT](../n1ql/n1ql-language-reference/insert.md).

### [](#inserting-documents-in-bulk)Inserting Documents in Bulk

To insert several documents at once, use multiple VALUES clauses. The VALUES keyword itself is optional in the second and later iterations of the clause.

The following query creates two documents in the `airline` keyspace.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
INSERT INTO airline (KEY,VALUE)
VALUES ( "airline_4444",
    { "callsign": "MY-AIR",
      "country": "United States",
      "iata": "Z1",
      "icao": "AQZ",
      "name": "80-My Air",
      "id": "4444",
      "type": "airline"} ),
VALUES ( "airline_4445",
    { "callsign": "AIR-X",
      "country": "United States",
      "iata": "X1",
      "icao": "ARX",
      "name": "10-AirX",
      "id": "4445",
      "type": "airline"} )
RETURNING *;
```

Results

```json
{
  "requestID": "2fabc03a-ea9b-49fd-a044-6ef667381311",
  "signature": {
      "*": "*"
  },
  "results": [
  {
      "airline": {
          "callsign": "MY-AIR",
          "country": "United States",
          "iata": "Z1",
          "icao": "AQZ",
          "id": "4444",
          "name": "80-My Air",
          "type": "airline"
      }
  },
  {
      "airline": {
          "callsign": "AIR-X",
          "country": "United States",
          "iata": "X1",
          "icao": "ARX",
          "id": "4445",
          "name": "10-AirX",
          "type": "airline"
      }
  }
  ],
  "status": "success",
  "metrics": {
      "elapsedTime": "5.7617ms",
      "executionTime": "5.4635ms",
      "resultCount": 2,
      "resultSize": 505,
      "serviceLoad": 4,
      "mutationCount": 2
  }
}
```

### [](#inserting-the-results-of-a-query)Inserting the Results of a Query

To insert documents using a query, use the INSERT statement with a SELECT statement.

1. Use the bracketed KEY keyword to specify the document key.
2. Use the optional VALUE keyword to specify the body of the document to insert. The body of the inserted document is usually based on the result returned by the SELECT statement.
3. Use the SELECT statement to return a resultset which is used as a basis for the inserted documents. The INSERT statement inserts a document for every result returned by the SELECT statement.
4. If required, use the RETURNING clause specifies what the query returns when the document is inserted.

> [!NOTE]
> The document key that you specify must be unique for every document that you insert. For example, you can use the [UUID()](../n1ql/n1ql-language-reference/metafun.md#uuid) function to generate a unique key for each document.

The following query creates a copy in the `airport` keyspace of any document whose `airportname` is Heathrow.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
INSERT INTO airport (KEY UUID(), VALUE _airport)
    SELECT _airport FROM airport _airport
    WHERE airportname = "Heathrow"
RETURNING *;
```

Results

```json
[
  {
    "airport": {
      "airportname": "Heathrow",
      "city": "London",
      "country": "United Kingdom",
      "faa": "LHR",
      "geo": {
        "alt": 83,
        "lat": 51.4775,
        "lon": -0.461389
      },
      "icao": "EGLL",
      "id": 507,
      "type": "airport",
      "tz": "Europe/London"
    }
  }
]
```

## [](#replacing-existing-documents)Replacing Existing Documents

The INSERT statement fails if a document with the same document key already exists in the keyspace.

To insert documents into a keyspace and replace any existing documents with the same key, use the UPSERT statement. This has the same syntax as the INSERT statement.

The following query creates two documents in the `landmark` keyspace. If documents with the same keys already exist, the existing documents are replaced.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
UPSERT INTO landmark (KEY, VALUE)
VALUES ("upsert-1", { "name": "The Minster Inn", "type": "landmark-pub"}),
("upsert-2", {"name": "The Black Swan", "type": "landmark-pub"})
RETURNING VALUE name;
```

Results

```json
[
  "The Minster Inn",
  "The Black Swan"
]
```

For more information and examples, see [UPSERT](../n1ql/n1ql-language-reference/upsert.md).

## [](#merging-and-inserting-documents)Merging and Inserting Documents

You can also insert documents by merging: in other words, by joining one data source to another, and inserting documents that do not match.

To insert documents using a merge, use the MERGE statement with the INSERT action:

1. Use the INTO keyword to specify the target data source. This is the data source into which documents will be inserted.
2. Use the USING keyword to specify the source. This is the data source to check against the target.
3. Use the ON keyword to specify the merge predicate. This is a condition that must be met to match an object in the source with an object in the target.
4. Use WHEN NOT MATCHED THEN INSERT to specify that when a document in the source does not match a document in the target, the document should be inserted in the target.

  1. If necessary, use the bracketed KEY keyword to specify the document key.
  2. If necessary, use the bracketed VALUE keyword to specify the body of the document to insert.
  3. If necessary, use the WHERE clause to specify any further conditions that must be met for documents to be inserted.
5. If required, use the LIMIT clause to specify the greatest number of documents that may be inserted.
6. If required, use the RETURNING clause to specify what should be returned when the documents are inserted.

The following query compares a source set of airport data with the target `airport` keyspace. If the airport already exists in the `airport` keyspace, the record is updated. If the airport does not exist in the `airport` keyspace, a new record is inserted.

Context

Set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Setting the Query Context](select.md#query-context).

Query

```sqlpp
MERGE INTO airport AS target
USING [
  {"iata":"DSA", "name": "Doncaster Sheffield Airport"},
  {"iata":"VLY", "name": "Anglesey Airport / Maes Awyr Môn"}
] AS source
ON target.faa = source.iata
WHEN MATCHED THEN
  UPDATE SET target.old_name = target.airportname,
             target.airportname = source.name,
             target.updated = true
WHEN NOT MATCHED THEN
  INSERT (KEY UUID(),
          VALUE {"faa": source.iata,
                 "airportname": source.name,
                 "type": "airport",
                 "inserted": true} )
RETURNING *;
```

Results

```json
[
  {
    "target": {
      "airportname": "Anglesey Airport / Maes Awyr Môn",
      "faa": "VLY",
      "inserted": true,
      "type": "airport"
    }
  },
  {
    "source": {
      "iata": "DSA",
      "name": "Doncaster Sheffield Airport"
    },
    "target": {
      "airportname": "Doncaster Sheffield Airport",
      "city": "Doncaster, Sheffield",
      "country": "United Kingdom",
      "faa": "DSA",
      "geo": {
        "alt": 55,
        "lat": 53.474722,
        "lon": -1.004444
      },
      "icao": "EGCN",
      "id": 5562,
      "old_name": "Robin Hood Doncaster Sheffield Airport",
      "type": "airport",
      "tz": "Europe/London",
      "updated": true
    }
  }
]
```

For more information and examples, see [MERGE](../n1ql/n1ql-language-reference/merge.md).

## [](#related-links)Related Links

Reference and explanation:

* [INSERT](../n1ql/n1ql-language-reference/insert.md)
* [UPSERT](../n1ql/n1ql-language-reference/upsert.md)
* [MERGE](../n1ql/n1ql-language-reference/merge.md)

Querying with SDKs:

* [C](../../c-sdk/current/howtos/n1ql-queries-with-sdk.md)| [C++](../../cxx-sdk/current/howtos/sqlpp-queries-with-sdk.md)| [.NET](../../dotnet-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Go](../../go-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Java](../../java-sdk/current/howtos/sqlpp-queries-with-sdk.md)| [Kotlin](../../kotlin-sdk/current/howtos/n1ql-queries.md)| [Node.js](../../nodejs-sdk/current/howtos/n1ql-queries-with-sdk.md)| [PHP](../../php-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Python](../../python-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Ruby](../../ruby-sdk/current/howtos/n1ql-queries-with-sdk.md)| [Rust](../../rust-sdk/current/howtos/sqlpp-queries-with-sdk.md)| [Scala](../../scala-sdk/current/howtos/sqlpp-queries-with-sdk.md)