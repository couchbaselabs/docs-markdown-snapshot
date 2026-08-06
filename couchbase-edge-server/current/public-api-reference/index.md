---
title: Edge Server Public REST API
editUrl: https://github.com/couchbase/edge-server/edit/release/1.1/docs/modules/public-api-reference/pages/index.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:couchbase-edge-server:public-api-reference:index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-edge-server/current/public-api-reference/index.html)

# Edge Server Public REST API

* Introduction
* Database
  * getGet server information
  * getGet list of all database names
  * getGet database or keyspace information
* Document
  * putCreate a document
  * getGet all documents in the keyspace
  * postGet all documents in the keyspace
  * postBulk document operations
  * getGet a document
  * putUpsert a document
  * delDelete a document
  * headCheck if a document exists
  * getGet a sub-document
  * putCreate or update a sub-document
  * delDelete a sub-document
* Replication
  * getList active replications only
  * getGet status of all replications
  * postStart a replication
  * getGet status of a replication
  * delStop replication
* Changes
  * getGet changes list
  * postGet changes list
* Query
  * postRun an ad-hoc query
  * getRun a pre-defined query
  * postRun a pre-defined query

[API docs by Redocly](https://redocly.com/redoc/)

# Edge Server (1.0)

Download OpenAPI specification:

License: [Business Source License 1.1 (BSL)](https://github.com/couchbase/edge-server/blob/main/LICENSE) 

[Couchbase Edge Server / REST-Based Access](https://docs.couchbase.com/couchbase-edge-server/current/rest-based-access/rest-api-landing.html)

## [](#section/Introduction)Introduction

Edge Server is a lightweight standalone database for resource-constrained edge. It exposes a RESTful interface that enables you to get database information, perform document operations, run SQL++ queries, and manage changes feeds and replication.

## [](#tag/Database)Database

Edge Server enables you to access one or more databases. Within each database, documents are stored in keyspaces. Each keyspace maps to a collection, which is stored in a scope within the database. For details, see [Database Operations with Edge Server](https://docs.couchbase.com/couchbase-edge-server/current/rest-based-access/database-operations.html).

## [](#tag/Database/operation/get%5F-)Get server information 

Returns information about the Edge Server node.

### Responses

**200** 

Returns server information

**400** 

There was a problem with your request

get/

Public API

{protocol}://{hostname}:59840/

### Response samples 

* 200
* 400

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "couchdb": "Welcome",
* "vendor": {
  * "name": "Couchbase Edge Server",
  * "version": "1.0.0 (37; )"  
},
* "version": "CouchbaseEdgeServer/1.0.0 (37; ) CouchbaseLiteCore/0.0.0-EE (770a516a19d505b7+403e27d509bb1131)"
}`

## [](#tag/Database/operation/get%5F%5Fall%5Fdbs-)Get list of all database names 

Returns a list of all database names.

### Responses

**200** 

Returns list of database names

**400** 

There was a problem with your request

get/\_all\_dbs

Public API

{protocol}://{hostname}:59840/\_all\_dbs

### Response samples 

* 200
* 400

Content type

application/json

Copy

`[
* "scratch",
* "travel-sample"
]`

## [](#tag/Database/operation/get%5Fdb-)Get database or keyspace information 

Retrieves information about a database or keyspace.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### Responses

**200** 

Returns database or keyspace information

**404** 

Resource could not be found

get/{keyspace}

Public API

{protocol}://{hostname}:59840/{keyspace}

### Response samples 

* 200
* 404

Content type

application/json

Example

DatabaseInfoKeyspaceInfoDatabaseInfo

Copy

 Expand all  Collapse all 

`{
* "db_name": "travel-sample",
* "db_uuid": "8478be31c9674c499c07edd4e3115de7",
* "collections": {
  * "inventory.airline": {
    * "doc_count": 1,
    * "update_seq": 1  
  },
  * "inventory.airport": {
    * "doc_count": 1980,
    * "update_seq": 1980  
  },
  * "inventory.landmark": {
    * "doc_count": 0,
    * "update_seq": 0  
  }  
}
}`

## [](#tag/Document)Document

You can create, read, update, and delete documents in a keyspace using the REST API's document operations. For details, see [Document Access with Edge Server](https://docs.couchbase.com/couchbase-edge-server/current/rest-based-access/document-access.html).

## [](#tag/Document/operation/put%5Fdb-)Create a document 

Creates a document with an automatically-generated document ID.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

##### Request Body schema: application/json

| property name\*additional property | any |
| ---------------------------------- | --- |

### Responses

**200** 

New revision created successfully

**400** 

There was a problem with your request

**404** 

Resource could not be found

put/{keyspace}

Public API

{protocol}://{hostname}:59840/{keyspace}

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "type": "airport",
* "country": "United Kingdom",
* "icao": "EGOV",
* "airportname": "Anglesey Airport",
* "city": "Valley",
* "faa": "VLY",
* "tz": "Europe/London"
}`

### Response samples 

* 200
* 400
* 404

Content type

application/json

Copy

`{
* "ok": true,
* "id": "~SCH2oNtKFMBdcO-_sUhBmn",
* "rev": "1-22855783cf597c31c37ec3815d8027f3706ef6f9"
}`

## [](#tag/Document/operation/get%5Fkeyspace-%5Fall%5Fdocs-)Get all documents in the keyspace 

Returns all documents in the database, based on the specified query parameters.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

##### query Parameters

| descending    | boolean Default: false Reverses sort order (descending document ID)                                           |
| ------------- | ------------------------------------------------------------------------------------------------------------- |
| include\_docs | boolean Include the body associated with each document.                                                       |
| keys          | Array of strings An array of document ID strings to filter by.                                                |
| limit         | number This limits the number of result rows returned. Using a value of 0 has the same effect as the value 1. |
| skip          | number Offset into the result rows returned. Combined with limit can be useful for paging.                    |
| startkey      | string Return records starting with the specified key.                                                        |
| endkey        | string Stop returning records when this key is reached.                                                       |

### Responses

**200** 

Operation ran successfully

**400** 

There was a problem with your request

**404** 

Resource could not be found

get/{keyspace}/\_all\_docs

Public API

{protocol}://{hostname}:59840/{keyspace}/\_all\_docs

### Response samples 

* 200
* 400
* 404

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "rows": [
  * {
    * "key": "string",
    * "id": "string",
    * "value": {
      * "rev": "string",
      * "cv": "string"  
      },
    * "doc": {
      * "_id": "~SCH2oNtKFMBdcO-_sUhBmn",
      * "_rev": "1-22855783cf597c31c37ec3815d8027f3706ef6f9",
      * "type": "airport",
      * "country": "United States",
      * "faa": "LAX"  
      }  
  }  
],
* "total_rows": 0,
* "update_seq": 0
}`

## [](#tag/Document/operation/post%5Fkeyspace-%5Fall%5Fdocs-)Get all documents in the keyspace 

Returns all documents in the database, based on the parameters specified in the request body.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

##### Request Body schema: application/json

| descending    | boolean Default: false Reverses sort order (descending document ID) |
| ------------- | ------------------------------------------------------------------- |
| include\_docs | boolean Default: true Adds body of each doc                         |
| keys          | Array of strings Limits results to the specified document IDs       |
| limit         | number Limits number of results                                     |
| skip          | number Offset into results                                          |
| startkey      | string Document ID to start at                                      |
| endkey        | string Document ID to end at (max value, or min if descending)      |

### Responses

**200** 

Operation ran successfully

**400** 

There was a problem with your request

**404** 

Resource could not be found

post/{keyspace}/\_all\_docs

Public API

{protocol}://{hostname}:59840/{keyspace}/\_all\_docs

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "descending": false,
* "include_docs": true,
* "keys": [
  * "string"  
],
* "limit": 0,
* "skip": 0,
* "startkey": "string",
* "endkey": "string"
}`

### Response samples 

* 200
* 400
* 404

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "rows": [
  * {
    * "key": "string",
    * "id": "string",
    * "value": {
      * "rev": "string",
      * "cv": "string"  
      },
    * "doc": {
      * "_id": "~SCH2oNtKFMBdcO-_sUhBmn",
      * "_rev": "1-22855783cf597c31c37ec3815d8027f3706ef6f9",
      * "type": "airport",
      * "country": "United States",
      * "faa": "LAX"  
      }  
  }  
],
* "total_rows": 0,
* "update_seq": 0
}`

## [](#tag/Document/operation/post%5Fkeyspace-%5Fbulk%5Fdocs-)Bulk document operations 

Allows multiple documented to be created, updated or deleted in bulk.

To create a new document, add the body as an object in the `docs` array. A document ID is generated by Edge Server unless `_id` is specified.

To update an existing document, provide the document ID (`_id`) and revision ID (`_rev`) as well as the new body values.

To delete an existing document, provide the document ID (`_id`), revision ID (`_rev`), and set the deletion flag (`_deleted`) to true.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

##### Request Body schema: application/json

| new\_edits   | boolean Default: true This controls whether to assign new revision identifiers to new edits (true) or use the existing ones (false). |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| docsrequired | Array of objects                                                                                                                     |

### Responses

**201** 

All operations executed.

Each object in the returned array represents a document. Each document should be checked to make sure it was successfully added to the database.

**400** 

There was a problem with your request

**404** 

Resource could not be found

post/{keyspace}/\_bulk\_docs

Public API

{protocol}://{hostname}:59840/{keyspace}/\_bulk\_docs

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "new_edits": true,
* "docs": [
  * {
    * "_id": "FooBar",
    * "foo": "bar"  
  },
  * {
    * "_id": "AliceSettings",
    * "_rev": "5-832a6db48ed130adadede928aee54576",
    * "FailedLoginAttempts": 7  
  },
  * {
    * "_id": "BobSettings",
    * "_rev": "1-fa76ba41ee5fdfee1b91fc478ed09e59",
    * "_deleted": true  
  }  
]
}`

### Response samples 

* 201
* 400
* 404

Content type

application/json

Example

SuccessPartial successSuccess

Copy

 Expand all  Collapse all 

`[
* {
  * "id": "FooBar",
  * "rev": "1-cd809becc169215072fd567eebd8b8de"  
},
* {
  * "id": "AliceSettings",
  * "rev": "6-b3e8dcf825b71ccee112f3572ec4323c"  
},
* {
  * "id": "BobSettings",
  * "rev": "2-5145e1086bb8d1d71a531e9f6b543c58"  
}
]`

## [](#tag/Document/operation/get%5Fkeyspace-docid-)Get a document 

Retrieves a document from the database by its document ID.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docidrequired    | string Example: doc1The document ID to run the operation against.                                                                                                                                                                                                                                                                         |

##### query Parameters

| rev         | string Example: rev=2-5145e1086bb8d1d71a531e9f6b543c58The document revision to target.                                                                              |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| revs\_from  | Array of strings Trims the revision history to stop at the first revision in the provided list. If no match is found, the revisions are trimmed to the revs\_limit. |
| revs\_limit | integer Maximum number of revisions to return for each document.                                                                                                    |

### Responses

**200** 

Document found and returned successfully

**400** 

Document ID is not in an allowed format therefore is invalid.

This could be because it is over 250 characters or is prefixed with an underscore ("\_").

**404** 

Resource could not be found

**501** 

Not Implemented. It is likely this error was caused due to trying to use an Enterprise-only feature on the Community Edition.

get/{keyspace}/{docid}

Public API

{protocol}://{hostname}:59840/{keyspace}/{docid}

### Response samples 

* 200
* 400
* 404
* 501

Content type

application/json

Copy

`{
* "_id": "~SCH2oNtKFMBdcO-_sUhBmn",
* "_rev": "1-22855783cf597c31c37ec3815d8027f3706ef6f9",
* "type": "airport",
* "country": "United States",
* "faa": "LAX"
}`

## [](#tag/Document/operation/put%5Fkeyspace-docid-)Upsert a document 

Creates the specified document, if it does not already exist. If the specified document does exist, this request makes a new revision for the existing document. A revision ID must be provided if targeting an existing document.

You must specify a document ID for this endpoint. To let Edge Server generate the ID, use the `POST /{db}/` endpoint.

If the document already exists, the document content is replaced by the provided request body. Any existing fields which are not specified by the request body are removed in the new revision.

The maximum size for a document is 20MB.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docidrequired    | string Example: doc1The document ID to run the operation against.                                                                                                                                                                                                                                                                         |

##### query Parameters

| roundtrip | boolean Block until document has been received by change cache.                        |
| --------- | -------------------------------------------------------------------------------------- |
| rev       | string Example: rev=2-5145e1086bb8d1d71a531e9f6b543c58The document revision to target. |

##### header Parameters

| If-Match | string The revision ID to target. |
| -------- | --------------------------------- |

##### Request Body schema: application/json

| \_idrequired                       | string document ID                 |
| ---------------------------------- | ---------------------------------- |
| \_revrequired                      | string revision ID of the document |
| property name\*additional property | any                                |

### Responses

**201** 

Created

**400** 

There was a problem with your request

**404** 

Resource could not be found

**409** 

Resource already exists under that name

**415** 

Invalid content type

put/{keyspace}/{docid}

Public API

{protocol}://{hostname}:59840/{keyspace}/{docid}

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "_id": "~SCH2oNtKFMBdcO-_sUhBmn",
* "_rev": "1-22855783cf597c31c37ec3815d8027f3706ef6f9",
* "type": "airport",
* "country": "United States",
* "faa": "LAX"
}`

### Response samples 

* 201
* 400
* 404
* 409
* 415

Content type

application/json

Copy

`{
* "ok": true,
* "id": "~SCH2oNtKFMBdcO-_sUhBmn",
* "rev": "1-22855783cf597c31c37ec3815d8027f3706ef6f9"
}`

## [](#tag/Document/operation/delete%5Fkeyspace-docid-)Delete a document 

Deletes a document from the keyspace. A new revision is created so the database can track the deletion in synchronized copies.

A revision ID is required, either in the header or in the query parameters.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docidrequired    | string Example: doc1The document ID to run the operation against.                                                                                                                                                                                                                                                                         |

##### query Parameters

| rev | string Example: rev=2-5145e1086bb8d1d71a531e9f6b543c58The document revision to target. |
| --- | -------------------------------------------------------------------------------------- |

##### header Parameters

| If-Match | string The revision ID to target. |
| -------- | --------------------------------- |

### Responses

**200** 

New revision created successfully

**400** 

There was a problem with your request

**404** 

Resource could not be found

delete/{keyspace}/{docid}

Public API

{protocol}://{hostname}:59840/{keyspace}/{docid}

### Response samples 

* 200
* 400
* 404

Content type

application/json

Copy

`{
* "ok": true,
* "id": "~SCH2oNtKFMBdcO-_sUhBmn",
* "rev": "1-22855783cf597c31c37ec3815d8027f3706ef6f9"
}`

## [](#tag/Document/operation/head%5Fkeyspace-docid-)Check if a document exists 

Returns a status code indicating whether the document exists or not.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docidrequired    | string Example: doc1The document ID to run the operation against.                                                                                                                                                                                                                                                                         |

##### query Parameters

| rev         | string Example: rev=2-5145e1086bb8d1d71a531e9f6b543c58The document revision to target.                                                                              |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| revs\_from  | Array of strings Trims the revision history to stop at the first revision in the provided list. If no match is found, the revisions are trimmed to the revs\_limit. |
| revs\_limit | integer Maximum number of revisions to return for each document.                                                                                                    |

### Responses

**200** 

Document exists

**400** 

Document ID is not in an allowed format therefore is invalid.

This could be because it is over 250 characters or is prefixed with an underscore ("\_").

**404** 

Resource could not be found

head/{keyspace}/{docid}

Public API

{protocol}://{hostname}:59840/{keyspace}/{docid}

### Response samples 

* 400
* 404

Content type

application/json

Copy

`{
* "error": "string",
* "reason": "string"
}`

## [](#tag/Document/operation/get%5Fkeyspace-docid-key-)Get a sub-document 

Retrieves a sub-document associated with the document.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docidrequired    | string Example: doc1The document ID to run the operation against.                                                                                                                                                                                                                                                                         |
| keyrequired      | string The key of the object containing the sub-document.                                                                                                                                                                                                                                                                                 |

##### query Parameters

| rev | string Example: rev=2-5145e1086bb8d1d71a531e9f6b543c58The document revision to target. |
| --- | -------------------------------------------------------------------------------------- |

### Responses

**200** 

Found subdocument successfully. Returns the sub-document as JSON.

**404** 

Resource could not be found

get/{keyspace}/{docid}/{key}

Public API

{protocol}://{hostname}:59840/{keyspace}/{docid}/{key}

### Response samples 

* 200
* 404

Content type

application/json

Copy

`{ }`

## [](#tag/Document/operation/put%5Fkeyspace-docid-key-)Create or update a sub-document 

Adds or updates a sub-document associated with the document. If the document does not exist, it is created and the sub-document is added to it.

If the sub-document already exists, the content of the existing sub-document is replaced in the new revision.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docidrequired    | string Example: doc1The document ID to run the operation against.                                                                                                                                                                                                                                                                         |
| keyrequired      | string The key of the object containing the sub-document.                                                                                                                                                                                                                                                                                 |

##### query Parameters

| rev | string The existing document revision ID to modify. Required only when modifying an existing document. |
| --- | ------------------------------------------------------------------------------------------------------ |

##### Request Body schema: application/json

The sub-document to add or modify in the document

| property name\*additional property | any |
| ---------------------------------- | --- |

### Responses

**201** 

Sub-document added or modified successfully

**404** 

Resource could not be found

**409** 

Resource already exists under that name

put/{keyspace}/{docid}/{key}

Public API

{protocol}://{hostname}:59840/{keyspace}/{docid}/{key}

### Request samples 

* Payload

Content type

application/json

Copy

`{ }`

### Response samples 

* 201
* 404
* 409

Content type

application/json

Copy

`{
* "ok": true,
* "id": "~SCH2oNtKFMBdcO-_sUhBmn",
* "rev": "1-22855783cf597c31c37ec3815d8027f3706ef6f9"
}`

## [](#tag/Document/operation/delete%5Fkeyspace-docid-key-)Delete a sub-document 

Deletes a sub-document associated with the document.

If the sub-document exists, the sub-document is removed from the document.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docidrequired    | string Example: doc1The document ID to run the operation against.                                                                                                                                                                                                                                                                         |
| keyrequired      | string The key of the object containing the sub-document.                                                                                                                                                                                                                                                                                 |

##### query Parameters

| rev | string The existing document revision ID to modify. |
| --- | --------------------------------------------------- |

### Responses

**200** 

Sub-document removed from the document successfully

**404** 

Resource could not be found

**409** 

Resource already exists under that name

delete/{keyspace}/{docid}/{key}

Public API

{protocol}://{hostname}:59840/{keyspace}/{docid}/{key}

### Response samples 

* 200
* 404
* 409

Content type

application/json

Copy

`{
* "ok": true,
* "id": "~SCH2oNtKFMBdcO-_sUhBmn",
* "rev": "1-22855783cf597c31c37ec3815d8027f3706ef6f9"
}`

## [](#tag/Replication)Replication

The replicate endpoint enables you to synchronize Edge Server with another server, for example Sync Gateway or Couchbase Capella App Services. For details, see [Manage Replication with Edge Server](https://docs.couchbase.com/couchbase-edge-server/current/rest-based-access/replication.html).

## [](#tag/Replication/operation/get%5F%5Factive%5Ftasks-)List active replications only 

Get a list of all active tasks

### Responses

**200** 

Returns list of active replications, changes feeds, and sync tasks

**400** 

There was a problem with your request

get/\_active\_tasks

Public API

{protocol}://{hostname}:59840/\_active\_tasks

### Response samples 

* 200
* 400

Content type

application/json

Copy

 Expand all  Collapse all 

`[
* {
  * "task_id": 0,
  * "age_secs": 0,
  * "type": "changes",
  * "error": {
    * "error": "string"  
  },
  * "args": "string",
  * "ks": "string"  
}
]`

## [](#tag/Replication/operation/get%5F%5Freplicate-)Get status of all replications 

Gets the status of all replication tasks.

### Responses

**200** 

Returns list of all replication tasks

**400** 

There was a problem with your request

get/\_replicate

Public API

{protocol}://{hostname}:59840/\_replicate

### Response samples 

* 200
* 400

Content type

application/json

Copy

 Expand all  Collapse all 

`[
* {
  * "task_id": 1,
  * "age_secs": 893,
  * "type": "replication",
  * "error": {
    * "error": "Unknown hostname \\\"myofflineappservice.apps.cloud.couchbase.com\\\"",
    * "x-litecore-domain": 5,
    * "x-litecore-code": 2  
  },
  * "source": "wss://myofflineappservice.apps.cloud.couchbase.com:4984/travel-sample",
  * "target": "travel-sample",
  * "updated_on": 1741027601,
  * "status": "Offline"  
}
]`

## [](#tag/Replication/operation/post%5F%5Freplicate-)Start a replication 

Instructs Edge Server to initiate replication with another server, e.g. Sync Gateway.

##### Request Body schema: application/json

| source               | string The source database name or URL                                                                                                               |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| target               | string The destination database name or URL                                                                                                          |
| bidirectional        | boolean Default: false Set to true for bidirectional push/pull replication                                                                           |
| continuous           | boolean Default: false Set to true for continuous replication                                                                                        |
| channels             | Array of strings unique Channel filter (incompatible with 'collections')                                                                             |
| doc\_ids             | Array of strings unique Document IDs to replicate (incompatible with 'collections')                                                                  |
| headers              | object Extra HTTP headers; keys are header names, values are header values                                                                           |
| collections          | Array of strings or object Default: \["\_default"\] Collections to replicate. If omitted, defaults to \["\_default"\] (the default collection only). |
| trusted\_root\_certs | string The certificate data of an additional root certificate to be trusted                                                                          |
| pinned\_cert         | string The certificate data of the server certificate                                                                                                |
| auth                 | object Configuration for authentication to a remote server. Either for replication, or a proxy.                                                      |
| proxy                | object (ProxyConfig) Configuration of a proxy to use during replication.                                                                             |

### Responses

**200** 

Replication queued successfully

**400** 

There was a problem with your request

post/\_replicate

Public API

{protocol}://{hostname}:59840/\_replicate

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "source": "string",
* "target": "string",
* "bidirectional": false,
* "continuous": false,
* "channels": [
  * "string"  
],
* "doc_ids": [
  * "string"  
],
* "headers": {
  * "property1": "string",
  * "property2": "string"  
},
* "collections": [
  * "_default"  
],
* "trusted_root_certs": "string",
* "pinned_cert": "string",
* "auth": {
  * "user": "string",
  * "password": "string",
  * "openid_token": "string",
  * "tls_client_cert": "string",
  * "tls_client_cert_key": "string",
  * "session_cookie": "string"  
},
* "proxy": {
  * "type": "HTTP",
  * "host": "string",
  * "port": 0,
  * "auth": {
    * "user": "string",
    * "password": "string",
    * "openid_token": "string",
    * "tls_client_cert": "string",
    * "tls_client_cert_key": "string"  
  }  
}
}`

### Response samples 

* 200
* 400

Content type

application/json

Copy

`{
* "ok": true,
* "task_id": 0
}`

## [](#tag/Replication/operation/get%5F%5Freplicate-taskid-)Get status of a replication 

Gets the status of the replication task with the given ID.

##### path Parameters

| taskidrequired | number Example: 1234The ID of an active replication task. |
| -------------- | --------------------------------------------------------- |

### Responses

**200** 

Returns status of the active replication

**400** 

There was a problem with your request

**404** 

Resource could not be found

get/\_replicate/{taskid}

Public API

{protocol}://{hostname}:59840/\_replicate/{taskid}

### Response samples 

* 200
* 400
* 404

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "task_id": 1,
* "age_secs": 893,
* "type": "replication",
* "error": {
  * "error": "Unknown hostname \\\"myofflineappservice.apps.cloud.couchbase.com\\\"",
  * "x-litecore-domain": 5,
  * "x-litecore-code": 2  
},
* "source": "wss://myofflineappservice.apps.cloud.couchbase.com:4984/travel-sample",
* "target": "travel-sample",
* "updated_on": 1741027601,
* "status": "Offline"
}`

## [](#tag/Replication/operation/delete%5F%5Freplicate-taskid-)Stop replication 

Stops the replication task with the given ID.

##### path Parameters

| taskidrequired | number Example: 1234The ID of an active replication task. |
| -------------- | --------------------------------------------------------- |

### Responses

**200** 

Replication stopped successfully

**400** 

There was a problem with your request

**404** 

Resource could not be found

delete/\_replicate/{taskid}

Public API

{protocol}://{hostname}:59840/\_replicate/{taskid}

### Response samples 

* 200
* 400
* 404

Content type

application/json

Copy

`{
* "ok": true
}`

## [](#tag/Changes)Changes

You can monitor changes in a keyspace using the keyspaces's changes feed. For details, see [Monitor Changes with Edge Server](https://docs.couchbase.com/couchbase-edge-server/current/rest-based-access/changes-feed.html).

## [](#tag/Changes/operation/get%5Fkeyspace-%5Fchanges-)Get changes list 

Retrieves a sorted list of changes made to documents in the database, in time order of application. Each document appears at most once, ordered by its most recent change, regardless of how many times it has been changed.

This request can be used to listen for update and modifications to the database for post processing or synchronization. A continuously connected changes feed is a reasonable approach for generating a real-time log for most applications.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

##### query Parameters

| limit         | integer Maximum number of changes to return.                                                                                                                                                                                                                                                                                                                                                                                                 |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| since         | string Starts the results from the change immediately after the given sequence ID. Sequence IDs should be considered opaque; they come from the last\_seq property of a prior response.                                                                                                                                                                                                                                                      |
| style         | string Default: "main\_only" Enum: "main\_only" "all\_docs" Controls whether to return the current winning revision (main\_only) or all the leaf revision including conflicts and deleted former conflicts (all\_docs).                                                                                                                                                                                                                      |
| active\_only  | boolean Default: "false" Set true to exclude deleted documents and notifications for documents the user no longer has access to from the changes feed.                                                                                                                                                                                                                                                                                       |
| include\_docs | boolean Include the body associated with each document.                                                                                                                                                                                                                                                                                                                                                                                      |
| revocations   | boolean If true, revocation messages are sent on the changes feed.                                                                                                                                                                                                                                                                                                                                                                           |
| filter        | string Enum: "sync\_gateway/bychannel" "\_doc\_ids" Set a filter to either filter by channels or document IDs.                                                                                                                                                                                                                                                                                                                               |
| channels      | string A comma-separated list of channel names to filter the response to only the channels specified. To use this option, the filter query option must be set to sync\_gateway/bychannels.                                                                                                                                                                                                                                                   |
| doc\_ids      | Array of strings A valid JSON array of document IDs to filter the documents in the response to only the documents specified. To use this option, the filter query option must be set to \_doc\_ids and the feed parameter must be normal. Also accepts a comma separated list of document IDs instead.                                                                                                                                       |
| heartbeat     | integer \>= 25000 Default: 0 The interval (in milliseconds) to send an empty line (CRLF) in the response. This is to help prevent gateways from deciding the socket is idle and therefore closing it. This is only applicable to feed=longpoll or feed=continuous. This overrides any timeouts to keep the feed alive indefinitely. Setting to 0 results in no heartbeat. The maximum heartbeat can be set in the replication configuration. |
| timeout       | integer \[ 0 .. 900000 \] Default: 300000 This is the maximum period (in milliseconds) to wait for a change before the response is sent, even if there are no results. This is only applicable for feed=longpoll or feed=continuous changes feeds. Setting to 0 results in no timeout.                                                                                                                                                       |
| feed          | string Default: "normal" Enum: "longpoll" "continuous" "sse" The type of changes feed to use.                                                                                                                                                                                                                                                                                                                                                |

### Responses

**200** 

Successfully returned the changes feed

**400** 

There was a problem with your request

**404** 

Resource could not be found

get/{keyspace}/\_changes

Public API

{protocol}://{hostname}:59840/{keyspace}/\_changes

### Response samples 

* 200
* 400
* 404

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "results": [
  * {
    * "seq": 0,
    * "id": "~XEltbV2jxLN04FDFsZED5_",
    * "changes": [
      * {
        * "rev": "1-22f5be403d75646a0758fab6731d7fa87c197666"  
            }  
      ]  
  },
  * {
    * "seq": 1,
    * "id": "~AxF827yGbOQprwFMNaotw2",
    * "changes": [
      * {
        * "rev": "1-22855783cf597c31c37ec3815d8027f3706ef6f9"  
            }  
      ]  
  }  
],
* "last_seq": 1
}`

## [](#tag/Changes/operation/post%5Fkeyspace-%5Fchanges-)Get changes list 

Retrieves a sorted list of changes made to documents in the database, in time order of application. Each document appears at most once, ordered by its most recent change, regardless of how many times it has been changed.

This request can be used to listen for update and modifications to the database for post processing or synchronization. A continuously connected changes feed is a reasonable approach for generating a real-time log for most applications.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

##### Request Body schema: application/json

| limit         | string Maximum number of changes to return.                                                                                                                                                                                                                                                                                                                                                                            |
| ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| style         | string Controls whether to return the current winning revision (main\_only) or all the leaf revision including conflicts and deleted former conflicts (all\_docs).                                                                                                                                                                                                                                                     |
| active\_only  | string Set true to exclude deleted documents and notifications for documents the user no longer has access to from the changes feed.                                                                                                                                                                                                                                                                                   |
| include\_docs | boolean Include the body associated with each document.                                                                                                                                                                                                                                                                                                                                                                |
| revocations   | string If true, revocation messages are sent on the changes feed.                                                                                                                                                                                                                                                                                                                                                      |
| filter        | string Set a filter to either filter by channels or document IDs.                                                                                                                                                                                                                                                                                                                                                      |
| channels      | string A comma-separated list of channel names to filter the response to only the channels specified. To use this option, the filter query option must be set to sync\_gateway/bychannels.                                                                                                                                                                                                                             |
| doc\_ids      | string A valid JSON array of document IDs to filter the documents in the response to only the documents specified. To use this option, the filter query option must be set to \_doc\_ids and the feed parameter must be normal.                                                                                                                                                                                        |
| heartbeat     | string The interval (in milliseconds) to send an empty line (CRLF) in the response. This is to help prevent gateways from deciding the socket is idle and therefore closing it. This is only applicable to feed=longpoll or feed=continuous. This overrides any timeouts to keep the feed alive indefinitely. Setting to 0 results in no heartbeat. The maximum heartbeat can be set in the replication configuration. |
| timeout       | string This is the maximum period (in milliseconds) to wait for a change before the response is sent, even if there are no results. This is only applicable for feed=longpoll or feed=continuous changes feeds. Setting to 0 results in no timeout.                                                                                                                                                                    |
| feed          | string The type of changes feed to use.                                                                                                                                                                                                                                                                                                                                                                                |

### Responses

**200** 

Successfully returned the changes feed

**400** 

There was a problem with your request

**404** 

Resource could not be found

post/{keyspace}/\_changes

Public API

{protocol}://{hostname}:59840/{keyspace}/\_changes

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "limit": "string",
* "style": "string",
* "active_only": "string",
* "include_docs": true,
* "revocations": "string",
* "filter": "string",
* "channels": "string",
* "doc_ids": "string",
* "heartbeat": "string",
* "timeout": "string",
* "feed": "string"
}`

### Response samples 

* 200
* 400
* 404

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "results": [
  * {
    * "seq": 0,
    * "id": "~XEltbV2jxLN04FDFsZED5_",
    * "changes": [
      * {
        * "rev": "1-22f5be403d75646a0758fab6731d7fa87c197666"  
            }  
      ]  
  },
  * {
    * "seq": 1,
    * "id": "~AxF827yGbOQprwFMNaotw2",
    * "changes": [
      * {
        * "rev": "1-22855783cf597c31c37ec3815d8027f3706ef6f9"  
            }  
      ]  
  }  
],
* "last_seq": 1
}`

## [](#tag/Query)Query

You can run SQL++ queries in a keyspace using the keyspace's query endpoint. For details, see [Run Queries with Edge Server](https://docs.couchbase.com/couchbase-edge-server/current/rest-based-access/queries-api.html).

## [](#tag/Query/operation/post%5Fkeyspace-%5Fquery-)Run an ad-hoc query 

Runs an ad-hoc query. Only possible when the database's `enable_adhoc_queries` property is true.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

##### Request Body schema: application/json

| queryrequired | string SQL++ Query string |
| ------------- | ------------------------- |
| parameters    | object Query parameters   |

### Responses

**200** 

Array of objects returned from query

**400** 

There was a problem with your request

**404** 

Resource could not be found

post/{keyspace}/\_query

Public API

{protocol}://{hostname}:59840/{keyspace}/\_query

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "query": "string",
* "parameters": { }
}`

### Response samples 

* 200
* 400
* 404

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "_": {
  * "id": 7630,
  * "type": "airport",
  * "country": "United States",
  * "faa": "MPI",
  * "tz": "America/Los_Angeles"  
}
}`

## [](#tag/Query/operation/get%5Fkeyspace-%5Fquery-name-)Run a pre-defined query 

Runs a pre-defined query as named by the database configuration's `query` object. If the query has parameters, they should be passed as query parameters, like `?key=value`.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| namerequired     | string Name of the query as defined in the database configuration.                                                                                                                                                                                                                                                                        |

### Responses

**200** 

Array of objects returned from query

**400** 

There was a problem with your request

**404** 

Resource could not be found

get/{keyspace}/\_query/{name}

Public API

{protocol}://{hostname}:59840/{keyspace}/\_query/{name}

### Response samples 

* 200
* 400
* 404

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "_": {
  * "id": 7630,
  * "type": "airport",
  * "country": "United States",
  * "faa": "MPI",
  * "tz": "America/Los_Angeles"  
}
}`

## [](#tag/Query/operation/post%5Fkeyspace-%5Fquery-name-)Run a pre-defined query 

Runs a pre-defined query as named by the database configuration's `query` object. If the query has parameters, they should be passed as JSON object in the request body.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| namerequired     | string Name of the query as defined in the database configuration.                                                                                                                                                                                                                                                                        |

##### Request Body schema: application/json

| property name\*additional property | any |
| ---------------------------------- | --- |

### Responses

**200** 

Array of objects returned from query

**400** 

There was a problem with your request

**404** 

Resource could not be found

post/{keyspace}/\_query/{name}

Public API

{protocol}://{hostname}:59840/{keyspace}/\_query/{name}

### Request samples 

* Payload

Content type

application/json

Copy

`{ }`

### Response samples 

* 200
* 400
* 404

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "_": {
  * "id": 7630,
  * "type": "airport",
  * "country": "United States",
  * "faa": "MPI",
  * "tz": "America/Los_Angeles"  
}
}`