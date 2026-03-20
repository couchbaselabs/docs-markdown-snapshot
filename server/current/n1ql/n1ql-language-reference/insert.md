---
title: INSERT
description: Use the INSERT statement to insert one or more new documents into
  an existing keyspace.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/n1ql/pages/n1ql-language-reference/insert.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:server:n1ql:n1ql-language-reference/insert.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/n1ql/n1ql-language-reference/insert.html)

# INSERT

> Use the INSERT statement to insert one or more new documents into an existing keyspace. Each INSERT statement requires a unique document key and well-formed JSON as values. In Couchbase, documents in a single keyspace must have a unique key. 

The INSERT statement can compute and return any expression based on the actual inserted documents.

> [!TIP]
> Use the [UPSERT](upsert.md) statement if you want to overwrite a document with the same key, in case it already exists.

> [!WARNING]
> Please note that the examples below will alter the data in your sample buckets. To restore your sample data, remove and reinstall the `travel-sample` bucket. Refer to [Sample Buckets](../../manage/manage-settings/install-sample-buckets.md) for details.

## [](#insert-prerequisites)Prerequisites

The INSERT statement must include the following:

* Name of the keyspace to insert the document.
* Unique document key.
* A well-formed JSON document specified as key-value pairs, or the projection of a SELECT statement which generates a well-formed single JSON to insert. See and for details.
* Optionally, you can specify the values or an expression to be returned after the INSERT statement completes successfully.

### [](#security-requirements)Security Requirements

You should have read-write permission to the keyspace, to be able to insert documents into a keyspace. Any user who has the keyspace credentials or any Couchbase administrator should be able to insert documents into a keyspace. This includes the keyspace administrator for the specified keyspace, the cluster administrator, and the full administrator roles. See [Roles](../../learn/security/roles.md) for details about access privileges for various administrators.

> [!WARNING]
> You cannot insert documents into a SASL bucket if you have a read-only role for the SASL bucket.

### [](#rbac-privileges)RBAC Privileges

To execute the INSERT statement, you must have the _Query Insert_ privilege on the target keyspace.

If the statement has any SELECT or RETURNING data-read clauses, then the _Query Select_ privilege is also required on the keyspaces referred in the respective clauses. For more details about roles and privileges, see [Authorization](../../learn/security/authorization-overview.md).

RBAC Examples 

For this example, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

To execute the following statement, you must have the _Query Insert_ privilege on `hotel`.

```sqlpp
INSERT INTO hotel (KEY, VALUE)
VALUES ("key1", { "type" : "hotel", "name" : "new hotel" });
```

To execute the following statement, you must have the _Query Insert_ and _Query Select_ privileges on `hotel`.

```sqlpp
INSERT INTO hotel (KEY, VALUE)
VALUES ("key1", { "type" : "hotel", "name" : "new hotel" }) RETURNING *;
```

To execute the following statement, you must have the _Query Insert_ privilege on `hotel` and _Query Select_ privilege on `` `beer-sample` ``.

```sqlpp
INSERT INTO landmark (KEY foo, VALUE bar)
SELECT META(doc).id AS foo, doc AS bar
FROM `beer-sample` AS doc WHERE type = "brewery";
```

To execute the following statement, you must have the _Query Insert_ and _Query Select_ privileges on `hotel`.

```sqlpp
INSERT INTO hotel (KEY foo, VALUE bar)
SELECT "copy_" || meta(doc).id AS foo, doc AS bar
FROM hotel AS doc;
```

## [](#insert-syntax)Syntax

```ebnf
insert ::= 'INSERT' 'INTO' target-keyspace ( insert-values | insert-select )
            returning-clause?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/insert.png) 

| target-keyspace  | [Insert Target](#insert-target)       |
| ---------------- | ------------------------------------- |
| insert-values    | [Insert Values](#insert-values)       |
| insert-select    | [Insert Select](#insert-select)       |
| returning-clause | [RETURNING Clause](#returning-clause) |

### [](#insert-target)Insert Target

```ebnf
target-keyspace ::= keyspace-ref ( 'AS'? alias )?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/target-keyspace.png) 

The insert target is the keyspace into which the documents are inserted. Ensure that the keyspace exists before trying to insert a document.

| keyspace-ref | [Keyspace Reference](#insert-target-ref) |
| ------------ | ---------------------------------------- |
| alias        | [AS Alias](#insert-target-alias)         |

#### [](#insert-target-ref)Keyspace Reference

```ebnf
keyspace-ref ::= keyspace-path | keyspace-partial
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/keyspace-ref.png) 

```ebnf
keyspace-path ::= ( namespace ':' )? bucket ( '.' scope '.' collection )?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/keyspace-path.png) 

```ebnf
keyspace-partial ::= collection
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/keyspace-partial.png) 

Keyspace reference for the insert target. For more details, refer to [Keyspace Reference](from.md#from-keyspace-ref).

#### [](#insert-target-alias)AS Alias

Assigns another name to the keyspace reference. For details, refer to [AS Clause](from.md#section%5Fax5%5F2nx%5F1db).

Assigning an alias to the keyspace reference is optional. If you assign an alias to the keyspace reference, the `AS` keyword may be omitted.

### [](#insert-values)Insert Values

```ebnf
insert-values ::= ( '(' 'PRIMARY'? 'KEY' ',' 'VALUE' ( ',' 'OPTIONS' )? ')' )? values-clause
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/insert-values.png) 

Specifies one or more documents to be inserted using the [VALUES clause](#values-clause). Each document requires a unique key and the values must be specified as well-formed JSON.

The bracketed KEY and VALUE keywords are purely a visual mnemonic to indicate that you are setting the key and value for the inserted document. There is no syntactic requirement to include these keywords when using the Insert Values syntax. Also note that there is no syntactic difference between PRIMARY KEY and KEY.

Similarly, the OPTIONS keyword is purely a visual mnemonic to indicate that you are setting metadata for the inserted document. There is no syntactic requirement to include the OPTIONS keyword when setting metadata for the inserted document.

#### [](#values-clause)VALUES Clause

```ebnf
values-clause ::= 'VALUES'  '(' key ',' value ( ',' options )? ')'
            ( ',' 'VALUES'? '(' key ',' value ( ',' options )? ')' )*
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/values-clause.png) 

| key     | A string, or an expression resolving to a string, representing the ID of the document to be inserted. The KEY cannot be MISSING or NULL, and must be unique within the Couchbase keyspace. It can be a string or an expression that produces a string.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| value   | A JSON object or value, or an expression resolving to a JSON object or value, representing the body of the document to be inserted. (See <http://json.org/example.html> for examples of well-formed JSON.) You can insert NULL, empty, or MISSING values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| options | \[Optional\] An object representing the metadata to be set for the inserted document. Only the listed attributes have any effect; the statement ignores the others. expiration An integer, or an expression resolving to an integer, representing the [document expiration](../../../../java-sdk/current/howtos/kv-operations.md#document-expiration). If the expiration time is less than 30 days, specify the value in seconds. For example, 60\*60\*24\*14 sets the document to expire in 14 days. If the expiration time is 30 days or more, specify the value as a Unix timestamp. If no expiration is specified, the value defaults to 0. In this case, the document expiration matches the [bucket or collection expiration](../../learn/data/expiration.md). Setting an incorrect expiration may cause documents to expire earlier than intended, resulting in data loss. xattrs An object containing top-level extended attribute (XATTR) names and their corresponding JSON values. The object includes only the attributes you want to add or update and does not affect other existing attributes. For each atttribute, you must provide its complete value. You cannot specify or update individual nested fields, as each attribute is updated as a whole. Starting with Couchbase Server 8.0, you can include up to 15 XATTRs per query. |

For examples illustrating the VALUES clause, see [Examples](#insert-examples).

### [](#insert-select)Insert Select

```ebnf
insert-select ::= '(' 'PRIMARY'? 'KEY' key ( ',' 'VALUE' value )?
                   ( ',' 'OPTIONS' options )? ')' select
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/insert-select.png) 

Use the projection of a SELECT statement which generates well-formed JSON to insert.

| key     | A string, or an expression resolving to a string, representing the ID of the document to be inserted. If the project of a SELECT statement generates multiple JSON documents, then your INSERT statement must handle the generation of unique keys for each of the documents.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| value   | \[Optional\] An object, or an expression resolving to an object, representing the body of the document to be inserted. This may be an alias assigned by the SELECT statement. If the VALUE is omitted, the entire JSON document generated by the SELECT statement is inserted.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| options | \[Optional\] An object representing the metadata to be set for the inserted document. Only the listed attributes have any effect; the statement ignores the others. expiration An integer, or an expression resolving to an integer, representing the [document expiration](../../../../java-sdk/current/howtos/kv-operations.md#document-expiration) in seconds. If the document expiration is not specified, it defaults to 0, meaning the document expiration is the same as the [bucket or collection expiration](../../learn/data/expiration.md). xattrs An object containing top-level extended attribute (XATTR) names and their corresponding JSON values. The object includes only the attributes you want to add or update and does not affect other existing attributes. For each atttribute, you must provide its complete value. You cannot specify or update individual nested fields, as each attribute is updated as a whole. Starting with Couchbase Server 8.0, you can include up to 15 XATTRs per query. |
| select  | [SELECT Statement](#select-statement)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

#### [](#select-statement)SELECT Statement

SELECT statements let you retrieve data from specified keyspaces. For details, see [SELECT Syntax](select-syntax.md).

For examples illustrating the SELECT statement, see [Examples](#insert-examples).

### [](#returning-clause)RETURNING Clause

```ebnf
returning-clause ::= 'RETURNING' (result-expr (',' result-expr)* |
                    ('RAW' | 'ELEMENT' | 'VALUE') expr)
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/returning-clause.png) 

Specifies the fields that must be returned as part of the results object.

| result-expr | [Result Expression](#result-expr) |
| ----------- | --------------------------------- |

#### [](#result-expr)Result Expression

```ebnf
result-expr ::= ( path '.' )? '*' | expr ( 'AS'? alias )?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/result-expr.png) 

Specifies an expression on the inserted documents, that will be returned as output. Use `*` to return all the fields in all the documents that were inserted.

For examples illustrating the RETURNING clause, see [Examples](#insert-examples).

## [](#result)Result

The INSERT statement returns the requestID, the signature, results including the keyspace and JSON document inserted, status of the query, and metrics.

* `requestID`: Request ID of the statement generated by the server.
* `signature`: Signature of the fields specified in the returning clause.
* `results`: If the query specified the returning clause, then results contains one or more fields as specified in the returning clause. If not, returns an empty results array.
* `errors`: Returns the error codes and messages if the statement fails with errors. Returned only when the statement fails with errors. Errors can also include timeouts.
* `status`: Status of the statement - "`successful`" or "`errors`".
* `metrics`: Provides metrics for the statement such as `elapsedTime`, `executionTime`, `resultCount`, `resultSize`, and `mutationCount`. For more information, see [Metrics](#insert-metrics).

### [](#insert-metrics)Metrics

The INSERT statement returns the following metrics along with the results and status:

* `elapsedTime`: Total elapsed time for the statement.
* `executionTime`: Time taken by Couchbase Server to execute the statement. This value is independent of network latency, platform code execution time, and so on.
* `resultCount`: Total number of results returned by the statement. In case of `INSERT` without a `RETURNING` clause, the value is `0`.
* `resultSize`: Total number of results that satisfy the query.
* `mutationCount`: Specifies the number of documents that were inserted by the `INSERT` statement.

### [](#insert-monitoring)Monitoring

You can use the query monitoring API to gather diagnostic information. For example, if you are performing a bulk insert using a `SELECT` statement, you can use the query monitoring API to get the number of documents being inserted. Check `system:active_requests` catalog for more information on monitoring active queries. For more information, see [Query Monitoring](../../tools/query-monitoring.md).

You can also take a look at the keyspace metrics from the Web Console. To do so, go to the Data Buckets tab and click the bucket that you want to monitor. In the General Bucket Analytics screen, scroll to the Query section to gather information such as requests/sec, selects/sec and so on.

## [](#insert-restrictions)Restrictions

When inserting documents into a specified keyspace, keep in mind the following restrictions which would help avoid errors during execution.

* The keyspace must exist. The INSERT statement returns an error if the keyspace does not exist.
* Do not insert a document with a duplicate key. If you are inserting multiple documents, the statement aborts at the first error encountered.
* Timeouts can affect the completion of an INSERT statement, especially when performing bulk inserts. Ensure that the timeout is set to a reasonable value that allows the bulk insert operation to complete.  
To set the indexer timeout, use the Index Settings REST API to set the `indexer.settings.scan_timeout` property. For an example, see [Set the Indexer Scan Timeout](../../index-rest-settings/index.md#ex-scan-timeout).
* When inserting multiple documents, no cleanup or rollback is done for the already inserted documents if the INSERT operations hits an error. This means, when you are inserting 10 documents, if the INSERT operation fails when inserting the 6th document, the operator quits and exits. It does not rollback the first five documents that were inserted. Nor does it ignore the failure and continue to insert the remaining documents.

## [](#insert-performance)Performance and Best Practices

When a single INSERT statement is executed, SQL++ prepares the statement, scans the values and then inserts the document. When inserting a large number of documents, you can improve the performance of the INSERT statement by using one of the following techniques:

* Batching the documents to perform bulk inserts, which decreases the latency and increases the throughput. The INSERT statement sends documents to the data node in batches, with a default batch size of 16\. You can configure this value using the [pipeline\_batch](../n1ql-manage/query-settings.md#pipeline%5Fbatch%5Freq) request-level parameter, or the [pipeline-batch](../n1ql-manage/query-settings.md#pipeline-batch-srv) service-level setting. Note that the maximum batch size is (232 \-1) and specifying a value higher than the maximum batch size may increase the memory consumption. The following example command sets the pipeline-batch size to 32 instead of the default 16:  
```sh  
curl -v -X POST http://localhost:8093/admin/settings -u Administrator:password \
-d '{ "debug":true, "pipeline-batch": 32 }'  
```
* Use the [max\_parallelism](../n1ql-manage/query-settings.md#max%5Fparallelism%5Freq) request-level parameter, or the [max-parallelism](../n1ql-manage/query-settings.md#max-parallelism-srv) service-level setting when inserting multiple documents.
* When performing bulk inserts, use prepared statements or multiple values.
* When new documents are inserted, the indexes are updated. When a large number of documents are inserted, this may affect the performance of the cluster.

## [](#insert-examples)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Example 1\. Overview

The following statement inserts a single JSON document into the `airline` keyspace with key "k001". The returning clause specifies the function `META().id` to return the key of the inserted document (metadata), and the wildcard (\*) to return the inserted document.

Query

```sqlpp
INSERT INTO airline ( KEY, VALUE )
  VALUES
  (
    "k001",
    { "id": "01", "type": "airline"}
  )
RETURNING META().id as docid, *;
```

Results

```json
{
  "requestID": "df5846b1-1044-4b1f-ae8a-979be25282d1",
  "signature": {
      "*": "*",
      "docid": "json"
  },
  "results": [
  {
      "airline": {
          "id": "01",
          "type": "airline"
      },
      "docid": "k001"
  }
  ],
  "status": "success",
  "metrics": {
      "elapsedTime": "6.916ms",
      "executionTime": "6.6224ms",
      "resultCount": 1,
      "resultSize": 117,
      "serviceLoad": 4,
      "mutationCount": 1
  }
}
```

The simplest use case of an INSERT statement is to insert a single document into the keyspace.

Example 2\. Insert a single document

Insert a new document with `key` "1025" into the `airline` keyspace.

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

You can batch insert multiple documents using multiple VALUES clauses. The VALUES keyword itself is optional in the second and later iterations of the clause.

Example 3\. Perform bulk inserts

Insert two documents with `key` "airline\_4444" and "airline\_4445" into the `airline` keyspace:

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

Example 4\. Specify a key using an expression

You can specify a key using an expression, as shown here.

Query

```sqlpp
INSERT INTO airline ( KEY, VALUE )
                    VALUES ( "airline" || TOSTRING(1234),
                    { "callsign": "" } )
                    RETURNING META().id;
```

Example 5\. Generate a unique key

If you don’t require the document key to be in a specific format, you can use the function [UUID()](metafun.md#uuid) to generate a unique key, as shown here.

Query

```sqlpp
INSERT INTO airline ( KEY, VALUE )
            VALUES ( UUID(),
                    { "callsign": "" } )
RETURNING META().id;
```

Since the document key is auto-generated, you can find the value of the key by specifying META().id in the returning clause.

Example 6\. Insert an empty value

Query

```sqlpp
INSERT INTO airline (KEY, VALUE)
    VALUES ( "airline::432",
              { "callsign": "",
                "country" : "USA",
                "type" : "airline"} )
RETURNING *;
```

Results

```json
[
  {
    "airline": {
      "callsign": "",
      "country": "USA",
      "type": "airline"
    }
  }
]
```

Example 7\. Insert a NULL value

Query

```sqlpp
INSERT INTO airline (KEY, VALUE)
    VALUES ( "airline::1432",
            { "callsign": NULL,
              "country" : "USA",
              "type" : "airline"} )
RETURNING *;
```

Results

```json
[
  {
    "airline": {
      "callsign": null,
      "country": "USA",
      "type": "airline"
    }
  }
]
```

Example 8\. Insert a MISSING value

Query

```sqlpp
INSERT INTO airline (KEY, VALUE)
    VALUES ( "airline::142",
            { "callsign": MISSING,
              "country" : "USA",
              "type" : "airline"} )
RETURNING *;
```

Results

```json
[
  {
    "airline": {
      "country": "USA",
      "type": "airline"
    }
  }
]
```

Example 9\. Insert a NULL JSON document

Query

```sqlpp
INSERT INTO hotel (KEY, VALUE)
    VALUES ( "1021",
              { } )
              RETURNING *;
```

Example 10\. Insert a document with expiration

Insert a document into the `airline` keyspace using an expiration of 5 days.

Query

```sqlpp
INSERT INTO airline (KEY, VALUE, OPTIONS)
    VALUES ( "airline::ttl",
             { "callsign": "Temporary",
               "country" : "USA",
               "type" : "airline" },
             { "expiration": 5*24*60*60 } );
```

Example 11\. Return the document ID and country

Query

```sqlpp
INSERT INTO airline (KEY, VALUE)
    VALUES ( "airline_24444",
            { "callsign": "USA-AIR",
              "country" : "USA",
              "type" : "airline"})
RETURNING META().id as docid, country;
```

Results

```json
[
  {
    "country": "USA",
    "docid": "airline_24444"
  }
]
```

Example 12\. Return the document ID and an expression

Use the `UUID()` function to generate the key and show the usage of the `RETURNING` clause to retrieve the generated document key and the last element of the `callsign` array with an expression.

Query

```sqlpp
INSERT INTO airline (KEY, VALUE)
    VALUES ( UUID(),
            { "callsign": [ "USA-AIR", "America-AIR" ],
              "country" : "USA",
              "type" : "airline"} )
RETURNING META().id as docid, callsign[ARRAY_LENGTH(callsign)-1];
```

Results

```json
[
  {
    "$1": "America-AIR",
    "docid": "6af57793-65d2-4cc3-beea-5d713c7f3c29"
  }
]
```

Instead of providing actual values, you can specify the data to be inserted using the SELECT statement which selects the data from an existing keyspace.

Example 13\. Insert values using SELECT

Query the `airport` keyspace for documents with `airportname` "Heathrow", and then insert the projection (1 document) into the `airport` keyspace using a unique key generated using `UUID()`.

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

Example 14\. Insert with SELECT and set expiration

Query the `airport` keyspace for documents with `airportname` "Heathrow", and then insert the projection into the `airport` keyspace using a unique key and an expiration of 2 hours.

Query

```sqlpp
INSERT INTO airport
   (KEY UUID(), VALUE doc, OPTIONS {"expiration": 2*60*60})
    SELECT a AS doc FROM airport a
      WHERE airportname = "Heathrow";
```

Example 15\. Insert with SELECT and preserve expiration

If you want to copy the expiration of an existing document to the inserted document, you can use a [META().expiration](metafun.md#meta) expression in the SELECT statement, as shown here.

Query

```sqlpp
INSERT INTO airport
   (KEY UUID(), VALUE doc, OPTIONS {"expiration": ttl})
    SELECT META(a).expiration AS ttl, a AS doc FROM airport a
      WHERE airportname = "Heathrow";
```

Example 16\. Insert values with a combination key, generated using the projection and expressions

Generate a document key as a combination of the projection and some function, such as `<countryname>::<system-clock>`. The SELECT statement retrieves the country name "k1" and concatenates it with a delimiter "::" and the system clock function using the string `concat` operator "`||`".

Query

```sqlpp
INSERT INTO airport (KEY k1||"::"||clock_str(), value t)
    SELECT DISTINCT t.country AS k1,t
      FROM airport t
      LIMIT 5
RETURNING META().id as docid, *;
```

The result shows the META().id generated as a result of this concatenation (highlighted below).

Results

```json
[
  {
    "airport": {
      "airportname": "Calais Dunkerque",
      "city": "Calais",
      "country": "France",
      "faa": "CQF",
      "geo": {
        "alt": 12,
        "lat": 50.962097,
        "lon": 1.954764
      },
      "icao": "LFAC",
      "id": 1254,
      "type": "airport",
      "tz": "Europe/Paris"
    },
    "docid": "France::2021-02-09T13:53:28.445Z"
  }
]
```

Example 17\. Use insert to copy keyspace data to another keyspace

Use the INSERT statement to create a copy of `keyspace_1` under the new name `keyspace_2`.

Query

```sqlpp
INSERT INTO keyspace_2(key _k, value _v)
    SELECT META().id _k, _v
      FROM keyspace_1 _v;
```

Sub-queries can be used with INSERT in the insert-select form of the statement. The `SELECT` part can be any sophisticated query in itself.

Example 18\. Insert values using subqueries

Insert a new `type` in documents from all hotels in the cities that have landmarks.

Query

```sqlpp
INSERT INTO hotel (KEY UUID()) (3)
    SELECT x.name, x.city, "landmark_hotels" AS type (2)
      FROM hotel x
      WHERE x.city WITHIN
        ( SELECT DISTINCT t.city (1)
            FROM landmark t)
      LIMIT 4
RETURNING *;
```

| **1** | The inner most SELECT finds all cities that have landmarks.                                                                                                                                                                            |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | The outer SELECT finds the hotels that are in the cities selected by the inner query in Step 1\. It also adds a new type attribute with the value "landmark\_hotels" to the projected result. For brevity, we SELECT only 4 documents. |
| **3** | Finally, the INSERT statement inserts the result of Step 2 with UUID() generated keys.                                                                                                                                                 |

Results

```json
[
  {
    "hotel": {
      "city": "Aberdeenshire",
      "name": "Castle Hotel",
      "type": "landmark_hotels"
    }
  },
  {
    "hotel": {
      "city": "Aberdeenshire",
      "name": "Two Bears Cottage",
      "type": "landmark_hotels"
    }
  },
  {
    "hotel": {
      "city": "Agoura Hills",
      "name": "Malibu Creek Campground",
      "type": "landmark_hotels"
    }
  },
  {
    "hotel": {
      "city": "Altrincham",
      "name": "Cresta Court Hotel",
      "type": "landmark_hotels"
    }
  }
]
```

Example 19\. Insert values using functions

Set the parameter `$faa_code` using the cbq prompt, or the [Run-Time Preferences](../../tools/query-workbench.md#query-preferences) in the Query Workbench.

Parameters

```sqlpp
\SET -$faa_code "blr" ;
```

Query

```sqlpp
INSERT INTO airport (KEY, VALUE)
      VALUES ("airport_" || UUID(), (1)(2)
             { "type" : "airport",
               "tz" : "India Standard Time",
               "country" : "India",
               "faa" : UPPER($faa_code)} ) (3)
RETURNING *;
```

The query uses multiple functions during the INSERT:

| **1** | UUID() function to generate unique key for the document being inserted. |
| ----- | ----------------------------------------------------------------------- |
| **2** | The string concatenation operator \|| to join "airport\_" and the UUID. |
| **3** | UPPER string function to insert only uppercase values of the FAA code.  |

Results

```json
{
    "requestID": "4fea5296-c9f4-4fd3-be78-95e5a04531eb",
    "signature": {
        "*": "*"
    },
    "results": [
    {
        "airport": {
            "country": "India",
            "faa": "BLR",
            "type": "airport",
            "tz": "India Standard Time"
        }
    }
    ],
    "status": "success",
    "metrics": {
        "elapsedTime": "7.7853ms",
        "executionTime": "7.6472ms",
        "resultCount": 1,
        "resultSize": 167,
        "serviceLoad": 4,
        "mutationCount": 1
    }
}
```

Example 20\. Insert values using prepared statements

Prepare an `INSERT` statement and execute it by passing parameters. The `INSERT` statement has some of the attribute values preset while it takes the document `key` and airport `faa_code` as parameters.

First, prepare the `INSERT` statement.

Query

```sqlpp
PREPARE ins_india FROM
      INSERT INTO airport (KEY, VALUE)
        VALUES ( $key,
                { "type" : "airport",
                  "tz" : "India Standard Time",
                  "country" : "India",
                  "faa" : $faa_code} )
RETURNING *;
```

Now execute the prepared statement using the cbq shell or the Query Workbench, passing the parameters `key` and `faa_code`.

Query

```sqlpp
EXECUTE ins_india
USING {"key": "airport_10001", "faa_code": "DEL"};
```

Results

```json
[
  {
    "airport": {
      "country": "India",
      "faa": "DEL",
      "type": "airport",
      "tz": "India Standard Time"
    }
  }
]
```

Alternatively, execute the prepared statement using the REST API, passing `$key` and `$faa_code` as REST parameters.

Request

```sh
curl -v http://localhost:8093/query/service -u Administrator:password \
-d 'prepared="ins_india"&$key="airport_10002"&$faa_code="BLR"'
```

Results

```json
{
   "requestID":"55ff7e8a-7410-470f-ab83-c464f9d0092d",
   "signature":{
      "*":"*"
   },
   "results":[
      {
         "airport":{
            "country":"India",
            "faa":"BLR",
            "type":"airport",
            "tz":"India Standard Time"
         }
      }
   ],
   "status":"success",
   "metrics":{
      "elapsedTime":"22.6797ms",
      "executionTime":"17.0216ms",
      "resultCount":1,
      "resultSize":87,
      "serviceLoad":4,
      "mutationCount":1
   }
}
```

Example 21\. Insert a document with an extended attribute (XATTR)

Insert a document into the `airline` keyspace with an extended attribute, `metadata`.

Query

```sqlpp
INSERT INTO airline (KEY, VALUE, OPTIONS)
    VALUES ("airline:1402",
            { "callsign": "MY-AIR",
              "country": "United States",
              "type": "airline" },
            { "xattrs": { "metadata": { "created_by": "admin", "created_at": "2025-08-05" } } });
```

## [](#insert-explain-plan)Explain Plan

To understand how the INSERT statement is executed by SQL++, let us take a look at two examples. For detailed explanation about the EXPLAIN plan, see the [EXPLAIN](explain.md) statement.

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Example 22\. Simple INSERT statement using KEY VALUE pairs to insert two documents

Query

```sqlpp
EXPLAIN INSERT INTO airline (KEY,VALUE)
VALUES ( "1025",
          { "callsign": "SKY-AIR",
            "country": "United States",
            "id": "1025",
            "type": "airline"
          } ),
VALUES ( "1026",
          { "callsign": "F1-AIR",
            "country": "United States",
            "id": "1014"
          } )
RETURNING *;
```

Results

```json
{
    "requestID": "5d1797cb-a7df-409d-b924-130ba0cc597a",
    "signature": "json",
    "results": [
    {
        "plan": {
            "#operator": "Sequence",
            "~children": [
                {
                    "#operator": "ValueScan",
                    "cardinality": 2,
                    "cost": 0.032,
                    "values": "[[\"1025\", {\"callsign\": \"SKY-AIR\", \"country\": \"United States\", \"id\": \"1025\", \"type\": \"airline\"}], [\"1026\", {\"callsign\": \"F1-AIR\", \"country\": \"United States\", \"id\": \"1014\"}]]"
                },
                {
                    "#operator": "Parallel",
                    "maxParallelism": 1,
                    "~child": {
                        "#operator": "Sequence",
                        "~children": [
                            {
                                "#operator": "SendInsert",
                                "alias": "airline",
                                "bucket": "travel-sample",
                                "keyspace": "airline",
                                "namespace": "default",
                                "scope": "inventory"
                            },
                            {
                                "#operator": "InitialProject",
                                "result_terms": [
                                    {
                                        "expr": "self",
                                        "star": true
                                    }
                                ]
                            }
                        ]
                    }
                }
            ]
        },
        "text": "INSERT INTO airline (KEY,VALUE) VALUES ( \"1025\", { \"callsign\": \"SKY-AIR\", \"country\": \"United States\", \"id\": \"1025\", \"type\": \"airline\" } ), VALUES ( \"1026\", { \"callsign\": \"F1-AIR\", \"country\": \"United States\", \"id\": \"1014\" } ) RETURNING *;"
    }
    ],
    "status": "success",
    "metrics": {
        "elapsedTime": "6.5577ms",
        "executionTime": "6.2773ms",
        "resultCount": 1,
        "resultSize": 1898,
        "serviceLoad": 4
    }
}
```

The query engine first scans the input values shown by the operator `ValueScan` to obtain the input values, and then it inserts the documents into the specified keyspace (shown by the operator `SendInsert`).

Example 23\. INSERT statement using the projection of a select statement to generate values

Query

```sqlpp
EXPLAIN INSERT INTO airport (key UUID(), value airport)
    SELECT airport FROM airport
      WHERE airportname = "Heathrow";
```

Results

```json
[
  {
    "plan": {
      "#operator": "Sequence",
      "~children": [
        {
          "#operator": "Sequence",
          "~children": [
            {
              "#operator": "IndexScan3", (1)
              "bucket": "travel-sample",
              "index": "def_inventory_airport_airportname",
              "index_id": "14b05d2b21bd6eee",
// ...
            },
            {
              "#operator": "Fetch", (2)
              "bucket": "travel-sample",
              "keyspace": "airport",
              "namespace": "default",
              "scope": "inventory"
            },
            {
              "#operator": "Parallel",
              "~child": {
                "#operator": "Sequence",
                "~children": [
                  {
                    "#operator": "Filter", (3)
                    "condition": "((`airport`.`airportname`) = \"Heathrow\")"
                  },
// ...
                ]
              }
            }
          ]
        },
        {
          "#operator": "Parallel",
          "~child": {
            "#operator": "Sequence",
            "~children": [
              {
                "#operator": "SendInsert", (4)
                "alias": "airport",
                "bucket": "travel-sample",
                "key": "uuid()",
                "keyspace": "airport",
                "namespace": "default",
                "scope": "inventory",
                "value": "`airport`"
              },
// ...
            ]
          }
        }
      ]
    },
    "text": "INSERT INTO airport (key UUID(), value airport)\n    SELECT airport FROM airport\n      WHERE airportname = \"Heathrow\";"
  }
]
```

The Query Engine first executes the `SELECT` statement and then uses the projection to insert into the `airport` keyspace, performing the operations in the order listed:

| **1** | An IndexScan to search for documents using the def\_inventory\_airport\_airportname index. |
| ----- | ------------------------------------------------------------------------------------------ |
| **2** | A Fetch for the document in the airport keyspace.                                          |
| **3** | A Filter for documents with airportname="Heathrow".                                        |
| **4** | An Insert of the value along with the auto-generated key into the airport keyspace.        |