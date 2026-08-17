---
title: Edge Server Public REST API
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/edge-server/edit/release/1.0/docs/modules/public-api-reference/pages/index.adoc
  xref: xref:1.0@couchbase-edge-server:public-api-reference:index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-edge-server/1.0/public-api-reference/index.html)

# Edge Server Public REST API

* Database
  * getGet server information
  * getGet list of all database names
  * getGet database information
  * postCreate a document with automatically-generated docID
* Document
  * getGets all the documents in the database with the given parameters
  * postGet all the documents in the database using JSON arguments instead of query arguments
  * head/{db}/\_all\_docs
  * postBulk document operations
  * getGet a document
  * putUpsert a document
  * delDelete a document
  * headCheck if a document exists
  * getGet an attachment or sub-document from a document
  * putCreate or update an attachment or sub-document on a document
  * delDelete an attachment or sub-document on a document
* Replication
  * getList of all active tasks
  * getGet status of all replications
  * postStart a replication
  * getGet status of a replication with the given taskID
  * delStop replication with the given taskID
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

Edge Server is a REST and sync server for Couchbase Mobile databases.

## [](#tag/Database)Database

Create and manage databases

## [](#tag/Database/operation/get%5F-)Get server information 

Returns information about the Edge Server node.

### Responses

**200** 

Returned server information

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
* "ADMIN": true,
* "couchdb": "Welcome",
* "vendor": {
  * "name": "Couchbase Edge Server",
  * "version": 1  
},
* "version": "Couchbase Edge Server/1.0.0(1;a765231)"
}`

## [](#tag/Database/operation/get%5F%5Fall%5Fdbs-)Get list of all database names 

Returns list of all database names.

### Responses

**200** 

Returned list of database names

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

 Expand all  Collapse all 

`{
* "rows": [
  * "string"  
],
* "total_rows": 0
}`

## [](#tag/Database/operation/get%5Fdb-)Get database information 

Retrieve information about the database.

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

### Responses

**200** 

Successfully returned database information

**404** 

Resource could not be found

get/{db}

Public API

{protocol}://{hostname}:59840/{db}

### Response samples 

* 200
* 404

Content type

application/json

Copy

`{
* "db_name": "db",
* "update_seq": 123456,
* "committed_update_seq": 123456,
* "instance_start_time": 1644600082279583,
* "state": "Online",
* "server_uuid": "995618a6a6cc9ac79731bd13240e19b5"
}`

## [](#tag/Database/operation/put%5Fdb-)Create a document with automatically-generated docID 

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### query Parameters

| expires | integer A timestamp in UNIX seconds indicating when a doc should expire. The document will expire and be automatically purged at this time. If ttl is also specified the lower of the resulting timestamps is used. |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ttl     | integer The time-to-live (in seconds) for the document. The document will expire and be automatically purged after this time. If expires is also specified the lower of the resulting timestamps is used.           |

##### Request Body schema: application/json

| property name\*additional property | any |
| ---------------------------------- | --- |

### Responses

**201** 

Created

**400** 

There was a problem with your request

**404** 

Resource could not be found

post/{db}

Public API

{protocol}://{hostname}:59840/{db}

### Request samples 

* Payload

Content type

application/json

Copy

`{ }`

### Response samples 

* 201
* 400
* 404

Content type

application/json

Copy

`{
* "id": "string",
* "ok": true,
* "rev": "string",
* "expires": 0
}`

## [](#tag/Document)Document

Create and manage documents

## [](#tag/Document/operation/get%5Fkeyspace-%5Fall%5Fdocs-)Gets all the documents in the database with the given parameters 

Returns all documents in the database based on the specified parameters.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

##### query Parameters

| descending    | boolean Default: false Reverses sort order (descending docID)                                                 |
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
      }  
  }  
],
* "total_rows": 0,
* "update_seq": 0
}`

## [](#tag/Document/operation/post%5Fkeyspace-%5Fall%5Fdocs-)Get all the documents in the database using JSON arguments instead of query arguments 

Returns all documents in the database based on the specified parameters.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

##### Request Body schema: application/json

| descending    | boolean Default: false Reverses sort order (descending docID) |
| ------------- | ------------------------------------------------------------- |
| include\_docs | boolean Default: true Adds body of each doc                   |
| keys          | Array of strings List of docIDs to limit results to           |
| limit         | number Limits number of results                               |
| skip          | number Offset into results                                    |
| startkey      | string docID to start at                                      |
| endkey        | string docID to end at (max value, or min if descending)      |

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
      }  
  }  
],
* "total_rows": 0,
* "update_seq": 0
}`

## [](#tag/Document/operation/head%5Fkeyspace-%5Fall%5Fdocs-)/{db}/\_all\_docs 

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

##### query Parameters

| include\_docs | boolean Include the body associated with each document.                                                       |
| ------------- | ------------------------------------------------------------------------------------------------------------- |
| keys          | Array of strings An array of document ID strings to filter by.                                                |
| startkey      | string Return records starting with the specified key.                                                        |
| endkey        | string Stop returning records when this key is reached.                                                       |
| limit         | number This limits the number of result rows returned. Using a value of 0 has the same effect as the value 1. |

### Responses

**200** 

OK

**400** 

There was a problem with your request

**404** 

Resource could not be found

head/{keyspace}/\_all\_docs

Public API

{protocol}://{hostname}:59840/{keyspace}/\_all\_docs

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

## [](#tag/Document/operation/post%5Fkeyspace-%5Fbulk%5Fdocs-)Bulk document operations 

This will allow multiple documented to be created, updated or deleted in bulk.

To create a new document, simply add the body in an object under `docs`. A doc ID will be generated by Edge Server unless `_id` is specified.

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

Executed all operations.

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

Retrieve a document from the database by its doc ID.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docidrequired    | string Example: doc1The document ID to run the operation against.                                                                                                                                                                                                                                                                         |

##### query Parameters

| rev         | string Example: rev=2-5145e1086bb8d1d71a531e9f6b543c58The document revision to target.                                                                                 |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| revs\_from  | Array of strings Trim the revision history to stop at the first revision in the provided list. If no match is found, the revisions will be trimmed to the revs\_limit. |
| revs\_limit | integer Maximum amount of revisions to return for each document.                                                                                                       |

### Responses

**200** 

Document found and returned successfully

**400** 

Document ID is not in an allowed format therefore is invalid.

This could be because it is over 250 characters or is prefixed with an underscore ("\_").

**404** 

Resource could not be found

**501** 

Not Implemented. It is likely this error was caused due to trying to use an enterprise-only feature on the community edition.

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

 Expand all  Collapse all 

`{
* "FailedLoginAttempts": 5,
* "Friends": [
  * "Bob"  
],
* "_id": "AliceSettings",
* "_rev": "1-64d4a1f179db5c1848fe52967b47c166",
* "_cv": "1@src"
}`

## [](#tag/Document/operation/put%5Fkeyspace-docid-)Upsert a document 

This will upsert a document meaning if it does not exist, then it will be created. Otherwise a new revision will be made for the existing document. A revision ID must be provided if targetting an existing document.

A document ID must be specified for this endpoint. To let Edge Server generate the ID, use the `POST /{db}/` endpoint.

If a document does exist, then replace the document content with the request body. This means unspecified fields will be removed in the new revision.

The maximum size for a document is 20MB.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docidrequired    | string Example: doc1The document ID to run the operation against.                                                                                                                                                                                                                                                                         |

##### query Parameters

| roundtrip | boolean Block until document has been received by change cache                                                                                                                                                      |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| rev       | string Example: rev=2-5145e1086bb8d1d71a531e9f6b543c58The document revision to target.                                                                                                                              |
| expires   | integer A timestamp in UNIX seconds indicating when a doc should expire. The document will expire and be automatically purged at this time. If ttl is also specified the lower of the resulting timestamps is used. |
| ttl       | integer The time-to-live (in seconds) for the document. The document will expire and be automatically purged after this time. If expires is also specified the lower of the resulting timestamps is used.           |

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
* "_id": "string",
* "_rev": "string"
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
* "id": "string",
* "ok": true,
* "rev": "string",
* "expires": 0
}`

## [](#tag/Document/operation/delete%5Fkeyspace-docid-)Delete a document 

Delete a document from the database. A new revision is created so the database can track the deletion in synchronized copies.

A revision ID either in the header or on the query parameters is required.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docidrequired    | string Example: doc1The document ID to run the operation against.                                                                                                                                                                                                                                                                         |

##### query Parameters

| rev     | string Example: rev=2-5145e1086bb8d1d71a531e9f6b543c58The document revision to target.                                                                                                                              |
| ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| expires | integer A timestamp in UNIX seconds indicating when a doc should expire. The document will expire and be automatically purged at this time. If ttl is also specified the lower of the resulting timestamps is used. |
| ttl     | integer The time-to-live (in seconds) for the document. The document will expire and be automatically purged after this time. If expires is also specified the lower of the resulting timestamps is used.           |

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
* "id": "string",
* "ok": true,
* "rev": "string",
* "expires": 0
}`

## [](#tag/Document/operation/head%5Fkeyspace-docid-)Check if a document exists 

Return a status code based on if the document exists or not.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docidrequired    | string Example: doc1The document ID to run the operation against.                                                                                                                                                                                                                                                                         |

##### query Parameters

| rev         | string Example: rev=2-5145e1086bb8d1d71a531e9f6b543c58The document revision to target.                                                                                 |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| revs\_from  | Array of strings Trim the revision history to stop at the first revision in the provided list. If no match is found, the revisions will be trimmed to the revs\_limit. |
| revs\_limit | integer Maximum amount of revisions to return for each document.                                                                                                       |

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

## [](#tag/Document/operation/get%5Fkeyspace-docid-key-)Get an attachment or sub-document from a document 

This request retrieves a file attachment or sub-document associated with the document.

The raw data of the associated attachment is returned (just as if you were accessing a static file). The `Content-Type` response header is the same content type set when the document attachment was added to the database. The `Content-Disposition` response header will be set if the content type is considered unsafe to display in a browser (unless overridden by by database config option `serve_insecure_attachment_types`) which will force the attachment to be downloaded.

If the `meta` query parameter is set then the response will be in JSON with the additional metadata tags.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docidrequired    | string Example: doc1The document ID to run the operation against.                                                                                                                                                                                                                                                                         |
| keyrequired      | string If key identifies a document property that's a blob, the response will be the contents of the blob. Otherwise, the property value is returned as JSON. For compatibility with CouchDB, if key doesn't exist but \_attachments/key does, the response will be a redirect to the latter path.                                        |

##### query Parameters

| rev | string Example: rev=2-5145e1086bb8d1d71a531e9f6b543c58The document revision to target. |
| --- | -------------------------------------------------------------------------------------- |

### Responses

**200** 

Found attachment or subdocument successfully. Type will be application/json for sub-document, text/plain for blob.

**404** 

Resource could not be found

get/{keyspace}/{docid}/{key}

Public API

{protocol}://{hostname}:59840/{keyspace}/{docid}/{key}

### Response samples 

* 200
* 404

Content type

application/jsontext/plainapplication/json

Copy

`{ }`

## [](#tag/Document/operation/put%5Fkeyspace-docid-key-)Create or update an attachment or sub-document on a document 

This request adds or updates an attachment associated with the document. If the document does not exist, it will be created and the attachment will be added to it.

If the attachment already exists, the data of the existing attachment will be replaced in the new revision.

The maximum content size of an attachment is 20MB. The `Content-Type` header of the request specifies the content type of the attachment.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docidrequired    | string Example: doc1The document ID to run the operation against.                                                                                                                                                                                                                                                                         |
| keyrequired      | string If key identifies a document property that's a blob, the response will be the contents of the blob. Otherwise, the property value is returned as JSON. For compatibility with CouchDB, if key doesn't exist but \_attachments/key does, the response will be a redirect to the latter path.                                        |

##### query Parameters

| rev | string The existing document revision ID to modify. Required only when modifying an existing document. |
| --- | ------------------------------------------------------------------------------------------------------ |

##### header Parameters

| Content-Type | string Default: application/octet-stream The content type of the attachment. |
| ------------ | ---------------------------------------------------------------------------- |

##### Request Body schema: 

Attachment content typeapplication/jsonAttachment content type

The attachment data

string

The content to store in the body

### Responses

**201** 

Attachment or sub-document added to new or existing document successfully

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

Attachment content typeapplication/jsonAttachment content type

No sample

### Response samples 

* 201
* 404
* 409

Content type

application/json

Copy

`{
* "id": "string",
* "ok": true,
* "rev": "string",
* "expires": 0
}`

## [](#tag/Document/operation/delete%5Fkeyspace-docid-key-)Delete an attachment or sub-document on a document 

This request deletes an attachment associated with the document.

If the attachment exists, the attachment will be removed from the document.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docidrequired    | string Example: doc1The document ID to run the operation against.                                                                                                                                                                                                                                                                         |
| keyrequired      | string If key identifies a document property that's a blob, the response will be the contents of the blob. Otherwise, the property value is returned as JSON. For compatibility with CouchDB, if key doesn't exist but \_attachments/key does, the response will be a redirect to the latter path.                                        |

##### query Parameters

| rev | string The existing document revision ID to modify. |
| --- | --------------------------------------------------- |

### Responses

**200** 

Attachment or sub-document removed from the document successfully

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
* "id": "string",
* "ok": true,
* "rev": "string",
* "expires": 0
}`

## [](#tag/Replication)Replication

Create and manage replications

## [](#tag/Replication/operation/get%5F%5Factive%5Ftasks-)List of all active tasks 

Get a list of all active tasks

### Responses

**200** 

Returned list of active tasks

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

`{
* "rows": [
  * {
    * "age_secs": 0,
    * "ip": "string",
    * "type": "changes",
    * "task_id": 0,
    * "user": "string",
    * "args": "string",
    * "ks": "string"  
  }  
]
}`

## [](#tag/Replication/operation/get%5F%5Freplicate-)Get status of all replications 

Get status of all replications

### Responses

**200** 

List of all active replications

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

`{
* "rows": [
  * {
    * "id": 0  
  }  
],
* "total_rows": 0
}`

## [](#tag/Replication/operation/post%5F%5Freplicate-)Start a replication 

Instruct Edge Server to initiate replication/sync with another server, i.e. Sync Gateway. Not the same as `/db/_blipsync`, which is for clients initiating replication with the Edge Server.

##### Request Body schema: application/json

| source        | string The source database name or URL                                                                       |
| ------------- | ------------------------------------------------------------------------------------------------------------ |
| target        | string The destination database name or URL                                                                  |
| bidirectional | boolean Default: false Set to true for bidirectional push/pull replication                                   |
| continuous    | boolean Default: false Set to true for continuous replication                                                |
| collections   | Array of strings                                                                                             |
| auth          | object (AuthConfig) Configuration for authentication to a remote server. Either for replication, or a proxy. |
| proxy         | object (ProxyConfig) Configuration of a proxy to use during replication.                                     |

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
* "collections": [
  * "string"  
],
* "auth": {
  * "user": "string",
  * "password": "string",
  * "session_cookie": "string",
  * "openid_token": "string",
  * "tls_client_cert": "string",
  * "tls_client_cert_key": "string"  
},
* "proxy": {
  * "type": "HTTP",
  * "host": "string",
  * "port": 0,
  * "auth": {
    * "user": "string",
    * "password": "string",
    * "session_cookie": "string",
    * "openid_token": "string",
    * "tls_client_cert": "string",
    * "tls_client_cert_key": "string"  
  }  
}
}`

### Response samples 

* 400

Content type

application/json

Copy

`{
* "error": "string",
* "reason": "string"
}`

## [](#tag/Replication/operation/get%5F%5Freplicate-taskid-)Get status of a replication with the given taskID 

Get status of a replication with the given taskID

##### path Parameters

| taskidrequired | number Example: 1234The ID of an active task. |
| -------------- | --------------------------------------------- |

### Responses

**200** 

Status of the active replication

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

`{
* "id": 0
}`

## [](#tag/Replication/operation/delete%5F%5Freplicate-taskid-)Stop replication with the given taskID 

Instruct Edge Server to stop the replication with the given taskID

##### path Parameters

| taskidrequired | number Example: 1234The ID of an active task. |
| -------------- | --------------------------------------------- |

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

* 400
* 404

Content type

application/json

Copy

`{
* "error": "string",
* "reason": "string"
}`

## [](#tag/Replication/operation/get%5Fkeyspace-%5Fchanges-)Get changes list 

This request retrieves a sorted list of changes made to documents in the database, in time order of application. Each document appears at most once, ordered by its most recent change, regardless of how many times it has been changed.

This request can be used to listen for update and modifications to the database for post processing or synchronization. A continuously connected changes feed is a reasonable approach for generating a real-time log for most applications.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

##### query Parameters

| limit         | integer Maximum number of changes to return.                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| since         | string Starts the results from the change immediately after the given sequence ID. Sequence IDs should be considered opaque; they come from the last\_seq property of a prior response.                                                                                                                                                                                                                                                                 |
| style         | string Default: "main\_only" Enum: "main\_only" "all\_docs" Controls whether to return the current winning revision (main\_only) or all the leaf revision including conflicts and deleted former conflicts (all\_docs).                                                                                                                                                                                                                                 |
| active\_only  | boolean Default: "false" Set true to exclude deleted documents and notifications for documents the user no longer has access to from the changes feed.                                                                                                                                                                                                                                                                                                  |
| include\_docs | boolean Include the body associated with each document.                                                                                                                                                                                                                                                                                                                                                                                                 |
| revocations   | boolean If true, revocation messages will be sent on the changes feed.                                                                                                                                                                                                                                                                                                                                                                                  |
| filter        | string Enum: "sync\_gateway/bychannel" "\_doc\_ids" Set a filter to either filter by channels or document IDs.                                                                                                                                                                                                                                                                                                                                          |
| channels      | string A comma-separated list of channel names to filter the response to only the channels specified. To use this option, the filter query option must be set to sync\_gateway/bychannels.                                                                                                                                                                                                                                                              |
| doc\_ids      | Array of strings A valid JSON array of document IDs to filter the documents in the response to only the documents specified. To use this option, the filter query option must be set to \_doc\_ids and the feed parameter must be normal. Also accepts a comma separated list of document IDs instead.                                                                                                                                                  |
| heartbeat     | integer \>= 25000 Default: 0 The interval (in milliseconds) to send an empty line (CRLF) in the response. This is to help prevent gateways from deciding the socket is idle and therefore closing it. This is only applicable to feed=longpoll or feed=continuous. This will override any timeouts to keep the feed alive indefinitely. Setting to 0 results in no heartbeat. The maximum heartbeat can be set in the server replication configuration. |
| timeout       | integer \[ 0 .. 900000 \] Default: 300000 This is the maximum period (in milliseconds) to wait for a change before the response is sent, even if there are no results. This is only applicable for feed=longpoll or feed=continuous changes feeds. Setting to 0 results in no timeout.                                                                                                                                                                  |
| feed          | string Default: "normal" Enum: "longpoll" "continuous" "sse" The type of changes feed to use.                                                                                                                                                                                                                                                                                                                                                           |

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
    * "id": "string",
    * "changes": [
      * {
        * "rev": "string"  
            }  
      ]  
  }  
],
* "last_seq": "string"
}`

## [](#tag/Replication/operation/post%5Fkeyspace-%5Fchanges-)Get changes list 

This request retrieves a sorted list of changes made to documents in the database, in time order of application. Each document appears at most once, ordered by its most recent change, regardless of how many times it has been changed.

This request can be used to listen for update and modifications to the database for post processing or synchronization. A continuously connected changes feed is a reasonable approach for generating a real-time log for most applications.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

##### Request Body schema: application/json

| limit         | string Maximum number of changes to return.                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| style         | string Controls whether to return the current winning revision (main\_only) or all the leaf revision including conflicts and deleted former conflicts (all\_docs).                                                                                                                                                                                                                                                                |
| active\_only  | string Set true to exclude deleted documents and notifications for documents the user no longer has access to from the changes feed.                                                                                                                                                                                                                                                                                              |
| include\_docs | boolean Include the body associated with each document.                                                                                                                                                                                                                                                                                                                                                                           |
| revocations   | string If true, revocation messages will be sent on the changes feed.                                                                                                                                                                                                                                                                                                                                                             |
| filter        | string Set a filter to either filter by channels or document IDs.                                                                                                                                                                                                                                                                                                                                                                 |
| channels      | string A comma-separated list of channel names to filter the response to only the channels specified. To use this option, the filter query option must be set to sync\_gateway/bychannels.                                                                                                                                                                                                                                        |
| doc\_ids      | string A valid JSON array of document IDs to filter the documents in the response to only the documents specified. To use this option, the filter query option must be set to \_doc\_ids and the feed parameter must be normal.                                                                                                                                                                                                   |
| heartbeat     | string The interval (in milliseconds) to send an empty line (CRLF) in the response. This is to help prevent gateways from deciding the socket is idle and therefore closing it. This is only applicable to feed=longpoll or feed=continuous. This will override any timeouts to keep the feed alive indefinitely. Setting to 0 results in no heartbeat. The maximum heartbeat can be set in the server replication configuration. |
| timeout       | string This is the maximum period (in milliseconds) to wait for a change before the response is sent, even if there are no results. This is only applicable for feed=longpoll or feed=continuous changes feeds. Setting to 0 results in no timeout.                                                                                                                                                                               |
| feed          | string The type of changes feed to use.                                                                                                                                                                                                                                                                                                                                                                                           |

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
    * "id": "string",
    * "changes": [
      * {
        * "rev": "string"  
            }  
      ]  
  }  
],
* "last_seq": "string"
}`

## [](#tag/Query)Query

Run queries

## [](#tag/Query/operation/post%5Fkeyspace-%5Fquery-)Run an ad-hoc query 

\-| Run an ad-hoc query. Only possible when the database's `enable_adhoc_queries` property is true.

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

`[
* { }
]`

## [](#tag/Query/operation/get%5Fkeyspace-%5Fquery-name-)Run a pre-defined query 

Run a pre-defined query as named by the database configuration's `query` object. If the query has parameters, they should be passed as query parameters like `?key=value`.

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

`[
* { }
]`

## [](#tag/Query/operation/post%5Fkeyspace-%5Fquery-name-)Run a pre-defined query 

Run a pre-defined query as named by the database configuration's `query` object. If the query has parameters, they should be passed as JSON object in the request body.

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

`[
* { }
]`