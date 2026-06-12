---
title: Data API Reference
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/data-api-reference/pages/index.adoc
pubDate: 2026-06-12T16:31:57.907Z
link: xref:cloud:data-api-reference:index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/data-api-reference/index.html)

# Data API Reference

* Introduction
  * Base URL
  * Examples
* Data API
  * Health Check
    * getGet Caller Identity
  * Basic Document Operations
    * getGet Document
    * postCreate Document
    * putUpdate Document
    * delDelete Document
    * postTouch Document
  * Binary Operations
    * postAppend to Document
    * postPrepend to Document
    * postIncrement Document
    * postDecrement Document
* Query Service
  * Query with SQL++
    * postQuery Service
    * getGET-Only Query Service
  * Query Indexes
* Search Service
  * Query with Search
    * getGet Document Count for an Index
    * postQuery a Search Index (Scoped)
  * Search Indexes
    * getGet All Search Index Definitions (Scoped)
    * getGet Index Definition (Scoped)
    * putCreate or Update an Index Definition (Scoped)
    * delDelete Index Definition (Scoped)

[API docs by Redocly](https://redocly.com/redoc/)

# Couchbase Data API (1.0.0)

Download OpenAPI specification:

[Data API Overview](https://docs.couchbase.com/cloud/data-api-guide/data-api-intro.html)

## [](#section/Introduction)Introduction

The Capella Data API provides a RESTful interface for working with data. It enables users to perform operations such as creating, reading, updating, or deleting data directly against your cluster. It also provides passthrough access to the Couchbase Services REST APIs, which enable you to query your data with SQL+⁠+, use vector search for AI applications, and more.

## [](#section/Introduction/Base-URL)Base URL

The base URL for the Data API is as follows:

`https://{clusterId}.data.cloud.couchbase.com`

where `{clusterId}` is unique to your Couchbase Capella cluster. For details, see [Get Started with the Data API](https://docs.couchbase.com/cloud/data-api-guide/data-api-start.html).

## [](#section/Introduction/Examples)Examples

In the Shell examples:

* `$BASEURL` is the base URL for the Data API.
* `$USER` is the cluster access username.
* `$PASSWORD` is the cluster access secret.

## [](#tag/Health-Check)Health Check

General utilities for the Data API.

## [](#tag/Health-Check/operation/getCallerIdentity)Get Caller Identity 

Retrieves the identity of the user making the current request.

##### header Parameters

| Authorizationrequired | string Header for authentication. |
| --------------------- | --------------------------------- |

### Responses

**200** 

Successfully fetched the current caller's identity.

**403** 

The user does not have permission to access the resource

**500** 

An internal server error occurred

get/v1/callerIdentity

https://{clusterId}.data.cloud.couchbase.com/v1/callerIdentity

### Response samples 

* 200
* 403
* 500

Content type

application/json

Copy

`{
* "user": "Administrator"
}`

## [](#tag/Basic-Document-Operations)Basic Document Operations

Create, read, update, and delete operations for single documents.

## [](#tag/Basic-Document-Operations/operation/getDocument)Get Document 

Retrieves the specified document.

##### path Parameters

| bucketNamerequired     | string The name of the bucket containing the document.     |
| ---------------------- | ---------------------------------------------------------- |
| scopeNamerequired      | string The name of the scope containing the document.      |
| collectionNamerequired | string The name of the collection containing the document. |
| documentKeyrequired    | string The ID of the document.                             |

##### query Parameters

| project | Array of strings Specific fields to project from the document. |
| ------- | -------------------------------------------------------------- |

##### header Parameters

| Authorizationrequired | string Header for authentication.                                                          |
| --------------------- | ------------------------------------------------------------------------------------------ |
| Accept-Encoding       | string Specifies the compression used for the response in HTTP content-negotiation format. |

### Responses

**200** 

Successful fetch of the document

**400** 

The request was malformed

**403** 

The user does not have permission to access the resource

**404** 

The specified resource was not found

**500** 

An internal server error occurred

**503** 

One of the underlying services was not available

**504** 

The request timed out

get/v1/buckets/{bucketName}/scopes/{scopeName}/collections/{collectionName}/documents/{documentKey}

https://{clusterId}.data.cloud.couchbase.com/v1/buckets/{bucketName}/scopes/{scopeName}/collections/{collectionName}/documents/{documentKey}

### Response samples 

* 200
* 400
* 403
* 404
* 500
* 503
* 504

Content type

application/jsontext/plainapplication/octet-stream\*application/json

Copy

 Expand all  Collapse all 

`{
* "title": "Brighton",
* "name": "Brighton Palace Pier",
* "alt": null,
* "address": "Madeira Dr, Brighton BN2 1TW",
* "directions": null,
* "phone": "01273609361",
* "tollfree": null,
* "email": "info@brightonpalacepier.co.uk",
* "url": "<https://www.brightonpier.co.uk>",
* "hours": "11am–6pm",
* "image": null,
* "price": "£2",
* "content": "The Brighton Palace Pier, commonly known as Brighton Pier or the Palace Pier, is a Grade II listed pleasure pier in Brighton, England, located in the city centre opposite the Old Steine. Established in 1899, it was the third pier to be constructed in Brighton after the Royal Suspension Chain Pier and the West Pier, but is now the only one still in operation.",
* "geo": {
  * "lat": 50.815,
  * "lon": -0.136944,
  * "accuracy": "RANGE_INTERPOLATED"  
},
* "activity": "do",
* "type": "landmark",
* "id": 10044,
* "country": "United Kingdom",
* "city": "Brighton",
* "state": null
}`

## [](#tag/Basic-Document-Operations/operation/createDocument)Create Document 

Creates a document with the given ID and contents.

##### path Parameters

| bucketNamerequired     | string The name of the bucket containing the document.     |
| ---------------------- | ---------------------------------------------------------- |
| scopeNamerequired      | string The name of the scope containing the document.      |
| collectionNamerequired | string The name of the collection containing the document. |
| documentKeyrequired    | string The ID of the document.                             |

##### header Parameters

| Authorizationrequired | string Header for authentication.                                                                                                                                                                                                                                 |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Content-Encoding      | string (DocumentEncoding) Enum: "identity" "snappy" The Content-Encoding of the body of the request.                                                                                                                                                              |
| Expires               | string The expiry time to set for the document, specified as a HTTP Date header or Go Duration string.                                                                                                                                                            |
| X-CB-Flags            | integer <uint32\> Overrides the document flags to a custom value rather than using values based on the Content-Type header.                                                                                                                                       |
| X-CB-DurabilityLevel  | string (DurabilityLevel) Enum: "None" "Majority" "MajorityAndPersistOnMaster" "PersistToMajority" The level of durability required for this write operation. For details, see [Durability](https://docs.couchbase.com/server/current/learn/data/durability.html). |

##### Request Body schema: \*

required

string <binary\> 

The contents of the document.

### Responses

**200** 

Successful creation of the document

**400** 

The request was malformed

**403** 

The user does not have permission to access the resource

**404** 

The specified resource was not found

**409** 

A conflict occurred while processing the request

**413** 

The document is too large to be stored

**500** 

An internal server error occurred

**503** 

One of the underlying services was not available

**504** 

The request timed out

post/v1/buckets/{bucketName}/scopes/{scopeName}/collections/{collectionName}/documents/{documentKey}

https://{clusterId}.data.cloud.couchbase.com/v1/buckets/{bucketName}/scopes/{scopeName}/collections/{collectionName}/documents/{documentKey}

### Response samples 

* 400
* 403
* 404
* 409
* 413
* 500
* 503
* 504

Content type

application/json

Copy

`{
* "code": "InvalidArgument",
* "message": "The request was malformed or invalid."
}`

## [](#tag/Basic-Document-Operations/operation/updateDocument)Update Document 

Updates the specified document with the given contents.

##### path Parameters

| bucketNamerequired     | string The name of the bucket containing the document.     |
| ---------------------- | ---------------------------------------------------------- |
| scopeNamerequired      | string The name of the scope containing the document.      |
| collectionNamerequired | string The name of the collection containing the document. |
| documentKeyrequired    | string The ID of the document.                             |

##### header Parameters

| Authorizationrequired | string Header for authentication.                                                                                                                                                                                                                                 |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Content-Encoding      | string (DocumentEncoding) Enum: "identity" "snappy" The Content-Encoding of the body of the request.                                                                                                                                                              |
| If-Match              | string The CAS of the document to check before updating.                                                                                                                                                                                                          |
| Expires               | string The expiry time to set for the document, specified as a HTTP Date header or Go Duration string.                                                                                                                                                            |
| X-CB-Flags            | integer <uint32\> Overrides the document flags to a custom value rather than using values based on the Content-Type header.                                                                                                                                       |
| X-CB-DurabilityLevel  | string (DurabilityLevel) Enum: "None" "Majority" "MajorityAndPersistOnMaster" "PersistToMajority" The level of durability required for this write operation. For details, see [Durability](https://docs.couchbase.com/server/current/learn/data/durability.html). |

##### Request Body schema: \*

required

string <binary\> 

The contents of the document.

### Responses

**200** 

Successful creation of the document

**400** 

The request was malformed

**403** 

The user does not have permission to access the resource

**404** 

The specified resource was not found

**409** 

A conflict occurred while processing the request

**413** 

The document is too large to be stored

**500** 

An internal server error occurred

**503** 

One of the underlying services was not available

**504** 

The request timed out

put/v1/buckets/{bucketName}/scopes/{scopeName}/collections/{collectionName}/documents/{documentKey}

https://{clusterId}.data.cloud.couchbase.com/v1/buckets/{bucketName}/scopes/{scopeName}/collections/{collectionName}/documents/{documentKey}

### Response samples 

* 400
* 403
* 404
* 409
* 413
* 500
* 503
* 504

Content type

application/json

Copy

`{
* "code": "InvalidArgument",
* "message": "The request was malformed or invalid."
}`

## [](#tag/Basic-Document-Operations/operation/deleteDocument)Delete Document 

Deletes the specified document.

##### path Parameters

| bucketNamerequired     | string The name of the bucket containing the document.     |
| ---------------------- | ---------------------------------------------------------- |
| scopeNamerequired      | string The name of the scope containing the document.      |
| collectionNamerequired | string The name of the collection containing the document. |
| documentKeyrequired    | string The ID of the document.                             |

##### header Parameters

| Authorizationrequired | string Header for authentication.                                                                                                                                                                                                                                 |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| If-Match              | string The CAS of the document to check before updating.                                                                                                                                                                                                          |
| X-CB-DurabilityLevel  | string (DurabilityLevel) Enum: "None" "Majority" "MajorityAndPersistOnMaster" "PersistToMajority" The level of durability required for this write operation. For details, see [Durability](https://docs.couchbase.com/server/current/learn/data/durability.html). |

### Responses

**200** 

Successful deletion of the document

**400** 

The request was malformed

**403** 

The user does not have permission to access the resource

**404** 

The specified resource was not found

**409** 

A conflict occurred while processing the request

**500** 

An internal server error occurred

**503** 

One of the underlying services was not available

**504** 

The request timed out

delete/v1/buckets/{bucketName}/scopes/{scopeName}/collections/{collectionName}/documents/{documentKey}

https://{clusterId}.data.cloud.couchbase.com/v1/buckets/{bucketName}/scopes/{scopeName}/collections/{collectionName}/documents/{documentKey}

### Response samples 

* 400
* 403
* 404
* 409
* 500
* 503
* 504

Content type

application/json

Copy

`{
* "code": "InvalidArgument",
* "message": "The request was malformed or invalid."
}`

## [](#tag/Basic-Document-Operations/operation/touchDocument)Touch Document 

Updates the expiry of a document. For details, see [Expiration](https://docs.couchbase.com/server/current/learn/data/expiration.html).

##### path Parameters

| bucketNamerequired     | string The name of the bucket containing the document.     |
| ---------------------- | ---------------------------------------------------------- |
| scopeNamerequired      | string The name of the scope containing the document.      |
| collectionNamerequired | string The name of the collection containing the document. |
| documentKeyrequired    | string The ID of the document.                             |

##### header Parameters

| Authorizationrequired | string Header for authentication.                                                          |
| --------------------- | ------------------------------------------------------------------------------------------ |
| Accept-Encoding       | string Specifies the compression used for the response in HTTP content-negotiation format. |

##### Request Body schema: application/json

required

| expiry        | string The new expiry to set for the document, specified as an ISO8601 string.        |
| ------------- | ------------------------------------------------------------------------------------- |
| returnContent | boolean Specifies whether the document's contents should be returned in the response. |

### Responses

**200** 

Successful updated the expiry of the document and is returning the content of the document.

**204** 

Successful updated the expiry of the document but is not returning the content of the document.

**400** 

The request was malformed

**403** 

The user does not have permission to access the resource

**404** 

The specified resource was not found

**500** 

An internal server error occurred

**503** 

One of the underlying services was not available

**504** 

The request timed out

post/v1/buckets/{bucketName}/scopes/{scopeName}/collections/{collectionName}/documents/{documentKey}/touch

https://{clusterId}.data.cloud.couchbase.com/v1/buckets/{bucketName}/scopes/{scopeName}/collections/{collectionName}/documents/{documentKey}/touch

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "expiry": "YYYY-MM-DDTHH:MM:SS.sssZ",
* "returnContent": true
}`

### Response samples 

* 200
* 400
* 403
* 404
* 500
* 503
* 504

Content type

application/jsontext/plainapplication/octet-stream\*application/json

Copy

 Expand all  Collapse all 

`{
* "title": "Brighton",
* "name": "Brighton Palace Pier",
* "alt": null,
* "address": "Madeira Dr, Brighton BN2 1TW",
* "directions": null,
* "phone": "01273609361",
* "tollfree": null,
* "email": "info@brightonpalacepier.co.uk",
* "url": "<https://www.brightonpier.co.uk>",
* "hours": "11am–6pm",
* "image": null,
* "price": "£2",
* "content": "The Brighton Palace Pier, commonly known as Brighton Pier or the Palace Pier, is a Grade II listed pleasure pier in Brighton, England, located in the city centre opposite the Old Steine. Established in 1899, it was the third pier to be constructed in Brighton after the Royal Suspension Chain Pier and the West Pier, but is now the only one still in operation.",
* "geo": {
  * "lat": 50.815,
  * "lon": -0.136944,
  * "accuracy": "RANGE_INTERPOLATED"  
},
* "activity": "do",
* "type": "landmark",
* "id": 10044,
* "country": "United Kingdom",
* "city": "Brighton",
* "state": null
}`

## [](#tag/Binary-Operations)Binary Operations

Append, prepend, increment, and decrement operations for binary documents.

## [](#tag/Binary-Operations/operation/appendToDocument)Append to Document 

Appends the specified contents to the end of the document.

##### path Parameters

| bucketNamerequired     | string The name of the bucket containing the document.     |
| ---------------------- | ---------------------------------------------------------- |
| scopeNamerequired      | string The name of the scope containing the document.      |
| collectionNamerequired | string The name of the collection containing the document. |
| documentKeyrequired    | string The ID of the document.                             |

##### header Parameters

| Authorizationrequired | string Header for authentication.                                                                                                                                                                                                                                 |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| If-Match              | string The CAS of the document to check before updating.                                                                                                                                                                                                          |
| X-CB-DurabilityLevel  | string (DurabilityLevel) Enum: "None" "Majority" "MajorityAndPersistOnMaster" "PersistToMajority" The level of durability required for this write operation. For details, see [Durability](https://docs.couchbase.com/server/current/learn/data/durability.html). |

##### Request Body schema: \*

required

any

### Responses

**200** 

Successfully appended contents to the document.

**400** 

The request was malformed

**403** 

The user does not have permission to access the resource

**404** 

The specified resource was not found

**409** 

A conflict occurred while processing the request

**500** 

An internal server error occurred

**503** 

One of the underlying services was not available

**504** 

The request timed out

post/v1/buckets/{bucketName}/scopes/{scopeName}/collections/{collectionName}/documents/{documentKey}/append

https://{clusterId}.data.cloud.couchbase.com/v1/buckets/{bucketName}/scopes/{scopeName}/collections/{collectionName}/documents/{documentKey}/append

### Response samples 

* 400
* 403
* 404
* 409
* 500
* 503
* 504

Content type

application/json

Copy

`{
* "code": "InvalidArgument",
* "message": "The request was malformed or invalid."
}`

## [](#tag/Binary-Operations/operation/prependToDocument)Prepend to Document 

Prepends the specified contents to the start of the document.

##### path Parameters

| bucketNamerequired     | string The name of the bucket containing the document.     |
| ---------------------- | ---------------------------------------------------------- |
| scopeNamerequired      | string The name of the scope containing the document.      |
| collectionNamerequired | string The name of the collection containing the document. |
| documentKeyrequired    | string The ID of the document.                             |

##### header Parameters

| Authorizationrequired | string Header for authentication.                                                                                                                                                                                                                                 |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| If-Match              | string The CAS of the document to check before updating.                                                                                                                                                                                                          |
| X-CB-DurabilityLevel  | string (DurabilityLevel) Enum: "None" "Majority" "MajorityAndPersistOnMaster" "PersistToMajority" The level of durability required for this write operation. For details, see [Durability](https://docs.couchbase.com/server/current/learn/data/durability.html). |

##### Request Body schema: \*

required

any

### Responses

**200** 

Successfully prepended contents to the document.

**400** 

The request was malformed

**403** 

The user does not have permission to access the resource

**404** 

The specified resource was not found

**409** 

A conflict occurred while processing the request

**500** 

An internal server error occurred

**503** 

One of the underlying services was not available

**504** 

The request timed out

post/v1/buckets/{bucketName}/scopes/{scopeName}/collections/{collectionName}/documents/{documentKey}/prepend

https://{clusterId}.data.cloud.couchbase.com/v1/buckets/{bucketName}/scopes/{scopeName}/collections/{collectionName}/documents/{documentKey}/prepend

### Response samples 

* 400
* 403
* 404
* 409
* 500
* 503
* 504

Content type

application/json

Copy

`{
* "code": "InvalidArgument",
* "message": "The request was malformed or invalid."
}`

## [](#tag/Binary-Operations/operation/incrementDocument)Increment Document 

Increments the value of the document. The document must contain a parsable integer as its content. For details, see [Counters](https://docs.couchbase.com/java-sdk/current/concept-docs/documents.html#counters).

If the document does not exist, sets the initial value of the document.

##### path Parameters

| bucketNamerequired     | string The name of the bucket containing the document.     |
| ---------------------- | ---------------------------------------------------------- |
| scopeNamerequired      | string The name of the scope containing the document.      |
| collectionNamerequired | string The name of the collection containing the document. |
| documentKeyrequired    | string The ID of the document.                             |

##### header Parameters

| Authorizationrequired | string Header for authentication.                                                                                                                                                                                                                                 |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Expires               | string The expiry time to set for the document, specified as a HTTP Date header or Go Duration string.                                                                                                                                                            |
| X-CB-DurabilityLevel  | string (DurabilityLevel) Enum: "None" "Majority" "MajorityAndPersistOnMaster" "PersistToMajority" The level of durability required for this write operation. For details, see [Durability](https://docs.couchbase.com/server/current/learn/data/durability.html). |

##### Request Body schema: 

application/jsonapplication/json

| initial | integer <uint64\> The value to set the document to if the document does not exist. |
| ------- | ---------------------------------------------------------------------------------- |
| delta   | integer <uint64\> The value to increment the document by if it exists.             |

### Responses

**200** 

Successfully incremented the document.

**400** 

The request was malformed

**403** 

The user does not have permission to access the resource

**404** 

The specified resource was not found

**500** 

An internal server error occurred

**503** 

One of the underlying services was not available

**504** 

The request timed out

post/v1/buckets/{bucketName}/scopes/{scopeName}/collections/{collectionName}/documents/{documentKey}/increment

https://{clusterId}.data.cloud.couchbase.com/v1/buckets/{bucketName}/scopes/{scopeName}/collections/{collectionName}/documents/{documentKey}/increment

### Request samples 

* Payload

Content type

application/jsonapplication/json

Copy

`{
* "initial": 10,
* "delta": 1
}`

### Response samples 

* 200
* 400
* 403
* 404
* 500
* 503
* 504

Content type

application/json

Copy

`10`

## [](#tag/Binary-Operations/operation/decrementDocument)Decrement Document 

Decrements the value of the document. The document must contain a parsable integer as its content. For details, see [Counters](https://docs.couchbase.com/java-sdk/current/concept-docs/documents.html#counters).

If the document does not exist, sets the initial value of the document.

##### path Parameters

| bucketNamerequired     | string The name of the bucket containing the document.     |
| ---------------------- | ---------------------------------------------------------- |
| scopeNamerequired      | string The name of the scope containing the document.      |
| collectionNamerequired | string The name of the collection containing the document. |
| documentKeyrequired    | string The ID of the document.                             |

##### header Parameters

| Authorizationrequired | string Header for authentication.                                                                                                                                                                                                                                 |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Expires               | string The expiry time to set for the document, specified as a HTTP Date header or Go Duration string.                                                                                                                                                            |
| X-CB-DurabilityLevel  | string (DurabilityLevel) Enum: "None" "Majority" "MajorityAndPersistOnMaster" "PersistToMajority" The level of durability required for this write operation. For details, see [Durability](https://docs.couchbase.com/server/current/learn/data/durability.html). |

##### Request Body schema: 

application/jsonapplication/json

| initial | integer <uint64\> The value to set the document to if the document does not exist. |
| ------- | ---------------------------------------------------------------------------------- |
| delta   | integer <uint64\> The value to decrement the document by if it exists.             |

### Responses

**200** 

Successfully incremented the document.

**400** 

The request was malformed

**403** 

The user does not have permission to access the resource

**404** 

The specified resource was not found

**500** 

An internal server error occurred

**503** 

One of the underlying services was not available

**504** 

The request timed out

post/v1/buckets/{bucketName}/scopes/{scopeName}/collections/{collectionName}/documents/{documentKey}/decrement

https://{clusterId}.data.cloud.couchbase.com/v1/buckets/{bucketName}/scopes/{scopeName}/collections/{collectionName}/documents/{documentKey}/decrement

### Request samples 

* Payload

Content type

application/jsonapplication/json

Copy

`{
* "initial": 10,
* "delta": 1
}`

### Response samples 

* 200
* 400
* 403
* 404
* 500
* 503
* 504

Content type

application/json

Copy

`11`

## [](#tag/Query)Query with SQL++

Use the following endpoints to run SQL++ queries and set request-level parameters.

## [](#tag/Query/operation/post%5Fservice)Query Service 

Enables you to execute a SQL++ statement. This method allows you to run SELECT queries and other DML statements, and specify query parameters.

##### Authorizations:

_Header_

##### Request Body schema: 

application/jsonapplication/x-www-form-urlencodedapplication/json

required

An object specifying one or more query parameters.

| args                             | Array of any Supplies the values for positional parameters in the statement. Applicable if the statement or prepared statement contains 1 or more positional parameters. The value is an array of JSON values, one for each positional parameter in the statement. For more information, see [Named Parameters and Positional Parameters](../n1ql/n1ql-manage/query-settings.html#section%5Fsrh%5Ftlm%5Fn1b).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| atrcollection                    | string Specifies the collection where the [active transaction record](/server/8.0/learn/data/transactions.html#active-transaction-record-entries) (ATR) is stored. The collection must be present. If not specified, the ATR is stored in the default collection in the default scope in the bucket containing the first mutated document within the transaction. The value must be a string in the form "bucket.scope.collection" or "namespace:bucket.scope.collection". If any part of the path contains a special character, that part of the path must be delimited in backticks \`\`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| auto\_execute                    | boolean Default: false Specifies that prepared statements should be executed automatically as soon as they're created. This saves you from having to make two separate requests in cases where you want to prepare a statement and execute it immediately. For more information, see [Auto-Execute](../n1ql/n1ql-language-reference/prepare.html#auto-execute).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| client\_context\_id              | string A piece of data supplied by the client that's echoed in the response, if present. SQL++ is agnostic about the content of this parameter; it's just echoed in the response. Maximum allowed size is 64 characters; all others will be cut. If it contains an escape character / or quote ", it will be rejected as error code 1110.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| compression                      | string Default: "NONE" Enum: "ZIP" "RLE" "LZMA" "LZO" "NONE" Compression format to use for response data on the wire. Values are case-insensitive.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| controls                         | boolean Specifies if there should be a controls section returned with the request results. When set to true, the query response document includes a controls section with runtime information provided along with the request, such as positional and named parameters or settings. If the request qualifies for caching, these values will also be cached in the completed\_requests system keyspace.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| creds                            | Array of objects In the Data API, this parameter is ignored and has no effect.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| durability\_level                | string Default: "majority" Enum: "" "none" "majority" "majorityAndPersistActive" "persistToMajority" The level of [durability](/server/8.0/learn/data/durability.html) for mutations produced by the request. If the request contains a BEGIN TRANSACTION statement, or a DML statement with the tximplicit parameter set to true, the durability level is specified for all mutations within that transaction. Durability is also supported for non-transactional DML statements. In this case, the kvtimeout parameter is used as the durability timeout. If not specified, the default durability level is "majority". Set the durability level to "none" or "" to specify no durability.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| encoded\_plan                    | string In clusters running Couchbase Server 6.5 and later, this parameter is ignored and has no effect. It's included for compatibility with previous versions of Couchbase Server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| encoding                         | string Default: "UTF-8" Desired character encoding for the query results. Only possible value is UTF-8 and is case-insensitive.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| format                           | string Default: "JSON" Enum: "JSON" "XML" "CSV" "TSV" Desired format for the query results. Values are case-insensitive.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| kvtimeout                        | string Default: "2.5s" The approximate time to wait for a KV get operation before timing out. This applies to statements within a transaction, and to non-transactional statements, whether durability\_level is set or not. If use\_replica is enabled for a query, then this parameter also specifies the approximate time to wait before fetching data from a replica vBucket when the active vBucket is inaccessible. The value for this parameter is a string. Its format includes an amount and a mandatory unit, e.g. 10ms (10 milliseconds) or 0.5s (half a second). Valid units are: ns (nanoseconds) us (microseconds) ms (milliseconds) s (seconds) m (minutes) h (hours) Specify a duration of 0 or a negative duration to disable. When disabled, no timeout is applied and the KV operation runs for however long it takes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| max\_parallelism                 | integer <int32\> Specifies the maximum parallelism for the query. The default value is the same as the number of partitions of the index selected for the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| memory\_quota                    | integer <int32\> Default: 0 Specifies the maximum amount of memory the request may use, in MB. Specify 0 (the default value) to disable. When disabled, there is no quota. This parameter enforces a ceiling on the memory used for the tracked documents required for processing a request. It does not take into account any other memory that might be used to process a request, such as the stack, the operators, or some intermediate values. Within a transaction, this setting enforces the memory quota for the transaction by tracking the delta table and the transaction log (approximately).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| metrics                          | boolean Default: true Specifies that metrics should be returned with query results.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| namespace                        | string Specifies the namespace to use. Currently, only the default namespace is available.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| natural                          | string The prompt for a natural language request. The Query Service uses the prompt to generate a SQL++ statement. If the generated statement is a SELECT statement, the generated statement is returned and executed automatically. If the generated statement is not a SELECT statement, the generated statement is returned, but not executed. In this case, you must verify the statement and execute it in a separate request. Natural language requests use the Couchbase Capella iQ service as a backend. To make a natural language request, you must have a Couchbase Capella user account. This parameter is available in clusters running Couchbase Server 8.0 and later. To use this parameter, you must also specify the natural\_cred, natural\_orgid, and natural\_context parameters. If you don't specify all four parameters, the Query Service returns an error.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| natural\_cred                    | string <password\> The Couchbase Capella user account credentials for a natural language request, in the form username:password. Be careful not to expose the credentials in log files or other output. This parameter does not support single sign-on (SSO), multi-factor authentication (MFA), or social login credentials such as Google or GitHub. Natural language requests use the Couchbase Capella iQ service as a backend. To make a natural language request, you must have a Couchbase Capella user account. This parameter is available in clusters running Couchbase Server 8.0 and later. To use this parameter, you must also specify the natural, natural\_orgid, and natural\_context parameters. If you don't specify all four parameters, the Query Service returns an error.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| natural\_orgid                   | string <uuid\> The Couchbase Capella organization ID for a natural language request. Natural language requests use the Couchbase Capella iQ service as a backend. To make a natural language request, you must have a Couchbase Capella user account. This parameter is available in clusters running Couchbase Server 8.0 and later. To use this parameter, you must also specify the natural, natural\_cred, and natural\_context parameters. If you don't specify all four parameters, the Query Service returns an error.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| natural\_context                 | string A list of paths specifying keyspaces for a natural language request. The Query Service infers the schema of each keyspace, in order to give more precise responses from the natural language request. The parameter may contain up to four paths, separated by commas. Spaces are allowed. Each path may be: A full path, in the form bucket.scope.collection or namespace:bucket.scope.collection. A path prefix, in the form namespace:bucket or bucket, to specify the default collection in the default scope. A partial path, in the form collection. In this case, you must specify the query\_context parameter to provide the bucket and scope. Natural language requests use the Couchbase Capella iQ service as a backend. To make a natural language request, you must have a Couchbase Capella user account. This parameter is available in clusters running Couchbase Server 8.0 and later. To use this parameter, you must also specify the natural, natural\_cred, and natural\_orgid parameters. If you don't specify all four parameters, the Query Service returns an error.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| natural\_output                  | string Default: "sql" Enum: "sql" "jsudf" "ftssql" Specifies the required output for a natural language request. sql — The output is a SQL++ statement. jsudf — The output is a CREATE FUNCTION statement which you can use to generate a SQL++ managed JavaScript user-defined function. ftssql — The output is a SQL++ statement which can use a Flex index, if available. Natural language requests use the Couchbase Capella iQ service as a backend. To make a natural language request, you must have a Couchbase Capella user account. This parameter is available in clusters running Couchbase Server 8.0 and later.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| numatrs                          | integer <int32\> Reserved for future use. This parameter is ignored and has no effect.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| pipeline\_batch                  | integer <int32\> Controls the number of items execution operators can batch for Fetch from the KV.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| pipeline\_cap                    | integer <int32\> Maximum number of items each execution operator can buffer between various operators.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| prepared                         | string Required if statement or natural not provided. The name of the prepared SQL++ statement to be executed. For examples, see [EXECUTE](../n1ql/n1ql-language-reference/execute.html). If both prepared and statement are present and non-empty, an error is returned.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| preserve\_expiry                 | boolean Default: false Specifies whether documents should keep their current expiration setting when modified by a DML statement. If true, documents will keep any existing expiration setting when modified by a DML statement. If the DML statement explicitly specifies the document expiration, the statement overrides this parameter, and the expiration is changed. If false, document expiration is set to 0 when modified by a DML statement, unless the DML statement explicitly specifies the document expiration. Not supported for statements in a transaction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| pretty                           | boolean Specifies the query results returned in pretty format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| profile                          | string Enum: "off" "phases" "timings" Specifies if there should be a profile section returned with the request results. The valid values are: off — No profiling information is added to the query response. phases — The query response includes a profile section with stats and details about various phases of the query plan and execution. Three phase times will be included in the system:active\_requests and system:completed\_requests monitoring keyspaces. timings — Besides the phase times, the profile section of the query response document will include a full query plan with timing and information about the number of processed documents at each phase. This information will be included in the system:active\_requests and system:completed\_requests keyspaces. If profile is not set as one of the above values, then the profile setting does not change.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| query\_context                   | string Default: "default:" Specifies the namespace, bucket, and scope used to resolve partial keyspace references within the request. The query context may be a full path, containing namespace, bucket, and scope; or a relative path, containing just the bucket and scope. Currently, only the default namespace is available. If the namespace name is omitted, the default namespace in the current session is used.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| readonly                         | boolean Default: false Controls whether a query can change a resulting recordset. If readonly is true, then the following statements are not allowed: CREATE INDEX DROP INDEX INSERT MERGE UPDATE UPSERT When using GET requests, it's best to set readonly to true.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| scan\_cap                        | integer <int32\> Maximum buffered channel size between the indexer client and the Query Service for index scans. This parameter controls when to use scan backfill. Use 0 or a negative number to disable. Smaller values reduce GC, while larger values reduce indexer backfill.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| scan\_consistency                | string Default: "not\_bounded" Enum: "not\_bounded" "at\_plus" "request\_plus" "statement\_plus" Specifies the consistency guarantee or constraint for index scanning. The valid values are: not\_bounded — No timestamp vector is used in the index scan. This is the fastest mode, because it avoids the costs of obtaining the vector and waiting for the index to catch up to the vector. at\_plus — This implements bounded consistency. When scan consistency is set to at\_plus, you must also specify the scan\_vector parameter for queries using a single keyspace, or the scan\_vectors parameter for queries using multiple keyspaces. This is used as a lower bound for the statements in the request. You can use this setting to implement read-your-own-writes (RYOW). request\_plus — This implements strong consistency per request. Before processing the request, a current vector is obtained. The vector is used as a lower bound for the statements in the request. If there are DML statements in the request, RYOW is also applied within the request. (If request\_plus is specified in a query that runs during a failover of an index node, the query waits until the rebalance operation completes and the index data has rebalanced before returning a result.) statement\_plus — This implements strong consistency per statement. Before processing each statement, a current vector is obtained and used as a lower bound for that statement. Values are case-insensitive. If the request contains a BEGIN TRANSACTION statement, or a DML statement with the tximplicit parameter set to true, then this parameter sets the transactional scan consistency. For more information, see [Transactional Scan Consistency](../n1ql/n1ql-manage/query-settings.html#transactional-scan-consistency). The default transactional scan consistency is RYOW for each statement within the transaction. If you want to disable RYOW for a statement within the transaction, set scan\_consistency for that statement to not\_bounded. |
| scan\_vector                     | Array of Full Scan Vector (any) or Sparse Scan Vector (object) (Scan Vector) Specifies the lower bound vector timestamp for a single keyspace when using at\_plus scan consistency. The scan vector may be full or sparse. A full scan vector is an array of \[value, guard\] entries, giving an entry for every vBucket in the system. A sparse scan vector is an object mapping \[value, guard\] entries to specific vBuckets. The name of each property in the object is a vBucket number (a string).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| scan\_vectors                    | object (Scan Vectors) Specifies the lower bound vector timestamps for multiple keyspaces when using at\_plus scan consistency. An object mapping scan vectors to keyspaces. The name of each property in the object is a keyspace name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| scan\_wait                       | string <duration\> Default: "" Can be supplied with scan\_consistency values of request\_plus, statement\_plus and at\_plus. Specifies the maximum time the client is willing to wait for an index to catch up to the vector timestamp in the request. Specifies how much time the client is willing to wait for the indexer to satisfy the required scan\_consistency and scan\_vector criteria. After receiving the scan request, if the indexer is unable to catch up within the scan\_wait time and start the scan, the indexer aborts with an error and the scan fails. Its format includes an amount and a mandatory unit, e.g. 10ms (10 milliseconds) or 0.5s (half a second). Valid units are: ns (nanoseconds) us (microseconds) ms (milliseconds) s (seconds) m (minutes) h (hours) Specify 0 or a negative integer to disable.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| signature                        | boolean Default: true Include a header for the results schema in the response.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| sort\_projection                 | boolean Default: false If true, causes statement projection terms to be sorted alphabetically. If false (the default), statement projection terms are returned in the order specified by the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| statement                        | string Required if prepared or natural not provided. Any valid SQL++ statement for a POST request, or a read-only SQL++ statement (SELECT, EXPLAIN) for a GET request. If both prepared and statement are present and non-empty, an error is returned. When specifying the request parameters as form data, the statement may not contain an unescaped semicolon (;). If it does, the Query Service responds with error 1040\. To avoid this, either URL-encode the semicolon as %3B, or just omit the semicolon if possible. This restriction does not apply when specifying the request parameters in JSON format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| timeout                          | string <duration\> Maximum time to spend on the request before timing out (s). The value for this parameter is a string. Its format includes an amount and an optional unit: for example, 10ms (10 milliseconds) or 0.5s (half a second). If not specified, the default unit is s (seconds). Valid units are: ns (nanoseconds) us (microseconds) ms (milliseconds) s (seconds) m (minutes) h (hours) Specify a duration of 0 or a negative duration to disable. When disabled, no timeout is applied and the request runs for however long it takes. If tximplicit or txid is set, this parameter is ignored. The request inherits the remaining time of the transaction as timeout.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| txdata                           | object Transaction data. For internal use only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| txid                             | string <UUID\> Required for statements within a transaction. Transaction ID. Specifies the transaction to which a statement belongs. For use with DML statements within a transaction, rollbacks, and commits. The transaction ID should be the same as the transaction ID generated by the BEGIN TRANSACTION statement. The transaction must be active and non-expired.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| tximplicit                       | boolean Default: false Specifies that a DML statement is a singleton transaction. When this parameter is true, the Query Service starts a transaction and executes the statement. If execution is successful, the Query Service commits the transaction; otherwise the transaction is rolled back. The statement may not be part of an ongoing transaction. If the txid request-level parameter is set, the tximplicit parameter is ignored.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| txstmtnum                        | integer <int32\> Transaction statement number. The transaction statement number must be a positive integer, and must be higher than any previous transaction statement numbers in the transaction. If the transaction statement number is lower than the transaction statement number for any previous statement, an error is generated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| txtimeout                        | string <duration\> Maximum time to spend on a transaction before timing out. Only applies to BEGIN TRANSACTION statements, or DML statements for which tximplicit is set. For other statements, it's ignored. Within a transaction, the request-level timeout parameter is ignored. The transaction timeout clock starts when the BEGIN WORK statement is successful. Once the transaction timeout is reached, no statement is allowed to continue in the transaction. The value for this parameter is a string. Its format includes an amount and a mandatory unit, e.g. 10ms (10 milliseconds) or 0.5s (half a second). Valid units are: ns (nanoseconds) us (microseconds) ms (milliseconds) s (seconds) m (minutes) h (hours) Specify a duration of 0 to disable. When disabled, the request-level timeout is set to the default. The default is "15s" for cbq files or scripts, "2m" for interactive cbq sessions or redirected input.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| use\_cbo                         | boolean Specifies whether the cost-based optimizer is enabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| use\_fts                         | boolean Default: false Specifies that the query should use a Search index. If the query contains a USING FTS hint, that takes priority over this parameter. If the query does not contain a USING FTS hint, and this parameter is set to true, all Search indexes are considered for the query. If a qualified Search index is available, it's selected for the query. If none of the available Search indexes are qualified, the available GSI indexes are considered instead. For more information, see [Flex Indexes](../n1ql/n1ql-language-reference/flex-indexes.html).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| use\_replica                     | string Default: "unset" Enum: "off" "on" "unset" Specifies whether a query can fetch data from a replica vBucket if active vBuckets are inaccessible. The possible values are: off — read from replica is disabled for this request. on — read from replica is enabled for this request, unless it has been disabled for all requests at node level. unset — read from replica is specified by the node-level setting. If the node-level setting is also unset, read from replica is disabled for this request. Do not enable read from replica when you require consistent results. Only SELECT queries that are not within a transaction can read from replica. Reading from replica is only possible if the cluster uses Couchbase Server 7.6.0 or later. You cannot currently start KV range scans on a replica vBucket. If a query uses sequential scan and a data node becomes unavailable, the query might return an error, even if read from replica is enabled for the request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| $identifier\*additional property | any Supplies the value for a named parameter in the statement. Applicable if the statement or prepared statement contains 1 or more named parameters. The name of this property consists of two parts: The $ character or the @ character. An identifier that specifies the name of the parameter. This starts with an optional underscore (\_), followed by an alpha character, followed by one or more alphanumeric characters, and ends with an optional underscore (\_). If the named parameter contains sensitive information, start and end the name of the parameter (after the initial $ or @) with an underscore (\_). This masks the parameter value in the active requests catalog, the completed requests catalog, the response controls section, the cbq shell file history, and the query logs. When masked, a string parameter value is replaced by asterisks (\*); other parameter values are replaced by null. Parameter masking is available in clusters running Couchbase Server 7.6.8 and later. The value of the named parameter can be any JSON value. For more information, see [Named Parameters and Positional Parameters](../n1ql/n1ql-manage/query-settings.html#section%5Fsrh%5Ftlm%5Fn1b).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

### Responses

**200** 

The operation was successful.

**400** 

Bad Request. The request cannot be processed for one of the following reasons: the statement contains a SQL++ syntax error; the request has a missing or unrecognized HTTP parameter; the request is badly formatted — for example, the request body contains a JSON syntax error.

**401** 

Unauthorized. The credentials provided with the request are missing or invalid.

**403** 

Forbidden. A read-only violation occurred. Either there was an attempt to create or update in a GET request or a POST request where `readonly` is set, or the client does not have the authorization to modify an object (index, keyspace or namespace) in the statement.

**404** 

Not found. The statement in the request references an invalid namespace or keyspace.

**405** 

Method not allowed. The statement in the request references an invalid namespace or keyspace.

**409** 

Conflict. The request attempted to create an object (keyspace or index) that already exists.

**410** 

Gone. The server is shutting down gracefully. Previously made requests are being completed, but no new requests are being accepted.

**413** 

Payload too large. The query is too large for the Query Service to process.

**500** 

Internal server error. An unforeseen problem occurred processing the request.

**503** 

Service unavailable. An issue (that's possibly temporary) is preventing the request being processed; the request queue is full or the data store is not accessible.

post/\_p/query/query/service

https://{clusterId}.data.cloud.couchbase.com/\_p/query/query/service

### Request samples 

* Payload
* Form Data
* JSON

Content type

application/jsonapplication/x-www-form-urlencodedapplication/json

Example

Named ParametersNumbered Positional ParametersUnnumbered Positional ParametersWildcardsBounded Consistency with a Scan VectorNamed Parameters

This request uses named parameters.

Copy

`` {
* "statement": "SELECT airline FROM `travel-sample`.inventory.route WHERE sourceairport = $aval AND distance > $dval",
* "$aval": "LAX",
* "$dval": 13000
} ``

### Response samples 

* 200
* 400
* 404
* 503

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "requestID": "615e0b26-dd61-4a1a-bda9-22333193b982",
* "signature": {
  * "name": "json"  
},
* "results": [
  * {
    * "name": "Medway Youth Hostel"  
  }  
],
* "status": "success",
* "metrics": {
  * "elapsedTime": "5.232754ms",
  * "executionTime": "5.160022ms",
  * "resultCount": 1,
  * "resultSize": 30,
  * "serviceLoad": 12  
}
}`

## [](#tag/Query/operation/get%5Fservice)GET-Only Query Service 

Enables you to execute a SQL++ statement. This method allows you to run SELECT queries and other DML statements, and specify query parameters.

This endpoint is intended for situations where use of the `POST` method is restricted.

##### Authorizations:

_Header_

##### query Parameters

| bodyrequired | object (Request Parameters) Specify the parameters in the query URL in URL-encoded format. The format for URL-encoded parameters is consistent with the syntax for variables according to RFC 6570. |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### Responses

**200** 

The operation was successful.

**400** 

Bad Request. The request cannot be processed for one of the following reasons: the statement contains a SQL++ syntax error; the request has a missing or unrecognized HTTP parameter; the request is badly formatted — for example, the request body contains a JSON syntax error.

**401** 

Unauthorized. The credentials provided with the request are missing or invalid.

**403** 

Forbidden. A read-only violation occurred. Either there was an attempt to create or update in a GET request or a POST request where `readonly` is set, or the client does not have the authorization to modify an object (index, keyspace or namespace) in the statement.

**404** 

Not found. The statement in the request references an invalid namespace or keyspace.

**405** 

Method not allowed. The statement in the request references an invalid namespace or keyspace.

**409** 

Conflict. The request attempted to create an object (keyspace or index) that already exists.

**410** 

Gone. The server is shutting down gracefully. Previously made requests are being completed, but no new requests are being accepted.

**413** 

Payload too large. The query is too large for the Query Service to process.

**500** 

Internal server error. An unforeseen problem occurred processing the request.

**503** 

Service unavailable. An issue (that's possibly temporary) is preventing the request being processed; the request queue is full or the data store is not accessible.

get/\_p/query/query/service

https://{clusterId}.data.cloud.couchbase.com/\_p/query/query/service

### Request samples 

* Shell

Copy

curl -v $BASEURL/_p/query/query/service?statement=SELECT%20name%20FROM%20%60travel-sample%60.inventory.hotel%20LIMIT%201%3B \
     -u $USER:$PASSWORD

### Response samples 

* 200
* 400
* 404
* 503

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "requestID": "615e0b26-dd61-4a1a-bda9-22333193b982",
* "signature": {
  * "name": "json"  
},
* "results": [
  * {
    * "name": "Medway Youth Hostel"  
  }  
],
* "status": "success",
* "metrics": {
  * "elapsedTime": "5.232754ms",
  * "executionTime": "5.160022ms",
  * "resultCount": 1,
  * "resultSize": 30,
  * "serviceLoad": 12  
}
}`

## [](#tag/Query-Indexes)Query Indexes

Use the [Query with SQL++](#tag/Query) endpoints to manage primary and secondary indexes. Alternatively, you can use the [Query Indexes](https://docs.couchbase.com/cloud/management-api-reference/index.html#tag/Query-Indexes) endpoints in the Management API.

## [](#tag/Search)Query with Search

Use the following endpoints to query the contents of a Search index.

## [](#tag/Search/operation/g-api-index-name-count)Get Document Count for an Index 

Returns the number of documents indexed in the specified Search index.

##### Authorizations:

_Statistics_

##### path Parameters

| INDEX\_NAMErequired | string The name of the Search index definition. You must use the fully qualified name for the index, which includes the bucket and scope. To view the full, scoped name for an index for use with this endpoint: Go to the **Search** tab in the Couchbase Server Web Console. Point to the **Index Name** for an index. |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

### Responses

**200** 

The Search Service returns a response that includes the status `ok`.

get/\_p/fts/api/index/{INDEX\_NAME}/count

https://{clusterId}.data.cloud.couchbase.com/\_p/fts/api/index/{INDEX\_NAME}/count

### Response samples 

* 200

Content type

application/json

Copy

`{
* "status": "ok",
* "count": 285
}`

## [](#tag/Search/operation/p-api-scoped-query)Query a Search Index (Scoped) 

Run a query formatted as a JSON object against the Search index definition specified in the endpoint URL. The endpoint returns a JSON object as a response. This endpoint is scoped and does not require a fully qualified `{INDEX_NAME}` value.

##### Authorizations:

_Manage_

##### path Parameters

| BUCKET\_NAMErequired | string The name of the bucket containing the Search index definition.           |
| -------------------- | ------------------------------------------------------------------------------- |
| SCOPE\_NAMErequired  | string The name of the scope containing the Search index definition.            |
| INDEX\_NAMErequired  | string^\[A-Za-z\]\[0-9A-Za-z\_\\-\]\*$ The name of the Search index definition. |

##### Request Body schema: application/json

required

A JSON object to define the settings for your Search query. For more information about how to create a Search query JSON object, see [Search Request JSON Properties](../search/search-request-params.html).

| query            | object An object that contains the properties for one of the supported query types. For more information, see [Query Object](../search/search-request-params.html#query-object).        |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| knn              | Array of objects An array that contains objects that describe a Vector Search query. For more information, see [Knn Objects](../search/search-request-params.html#knn-object).          |
| ctl              | object An object that contains properties for query consistency. For more information, see [Ctl Object](../search/search-request-params.html#ctl).                                      |
| size             | integer Set the total number of results to return for a single page of search results.                                                                                                  |
| from             | integer Set an offset value to change where pagination starts for search results.                                                                                                       |
| highlight        | object Contains properties to control search result highlighting. For more information, see [Highlight Objects](../search/search-request-params.html#highlight).                        |
| fields           | Array of strings An array of strings to specify each indexed field you want to return in search results.                                                                                |
| facets           | object Contains nested objects to define each facet you want to return with search results. For more information, see [Facet Objects](../search/search-request-params.html#facet-name). |
| explain          | boolean Whether to create an explanation for a search result's score in search results.                                                                                                 |
| sort             | Array of any Contains an array of strings or JSON objects to set how to sort search results. For more information, see [Sort Object](../search/search-request-params.html#sort).        |
| includeLocations | boolean Whether to return the position of each occurrence of a search term inside a document.                                                                                           |
| score            | string Whether to include document relevancy scoring in search results.                                                                                                                 |
| search\_after    | Array of strings Use to control pagination in search results.                                                                                                                           |
| search\_before   | Array of strings Use to control pagination in search results.                                                                                                                           |
| collections      | Array of strings An array of strings that specify the collections where you want to run the query.                                                                                      |

### Responses

**200** 

The response object has a status section that must be checked for every request. Under nearly all circumstances, the query response will be HTTP 200 even though individual index shards (partitions) may encounter a timeout or return an error.

**default** 

The Search Service returns a non-200 HTTP error code when a request fails.

post/\_p/fts/api/bucket/{BUCKET\_NAME}/scope/{SCOPE\_NAME}/index/{INDEX\_NAME}/query

https://{clusterId}.data.cloud.couchbase.com/\_p/fts/api/bucket/{BUCKET\_NAME}/scope/{SCOPE\_NAME}/index/{INDEX\_NAME}/query

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "query": { },
* "knn": [
  * { }  
],
* "ctl": { },
* "size": 0,
* "from": 0,
* "highlight": { },
* "fields": [
  * "string"  
],
* "facets": { },
* "explain": true,
* "sort": [
  * null  
],
* "includeLocations": true,
* "score": "string",
* "search_after": [
  * "string"  
],
* "search_before": [
  * "string"  
],
* "collections": [
  * "string"  
]
}`

### Response samples 

* 200
* default

Content type

application/json

Example

Success Response for a Regular QuerySuccess Response for a Hybrid QuerySuccess Response for a Regular Query

Copy

 Expand all  Collapse all 

`{
* "status": {
  * "total": 1,
  * "failed": 0,
  * "successful": 1  
},
* "request": {
  * "query": {
    * "conjuncts": [
      * {
        * "match": "location",
        * "field": "reviews.content",
        * "prefix_length": 0,
        * "fuzziness": 0,
        * "operator": "or"  
            },
      * {
        * "match_phrase": "nice view",
        * "field": "reviews.content"  
            }  
      ]  
  },
  * "size": 10,
  * "from": 0,
  * "highlight": {
    * "style": "html",
    * "fields": [
      * "reviews.content"  
      ]  
  },
  * "fields": null,
  * "facets": null,
  * "explain": true,
  * "sort": [
    * "reviews.Ratings.Cleanliness",
    * {
      * "by": "field",
      * "field": "reviews.Ratings.Cleanliness",
      * "type": "number"  
      },
    * "-_score",
    * "-_id"  
  ],
  * "includeLocations": false,
  * "score": "none",
  * "search_after": null,
  * "search_before": null  
},
* "hits": [
  * {
    * "index": "travel-sample.inventory.travel-test_53373d2948c55e82_4c1c5584",
    * "id": "hotel_7388",
    * "score": 0,
    * "explanation": {
      * "value": 0,
      * "message": "sum of:",
      * "children": [
        * {
          * "value": 0,
          * "message": "product of:",
          * "children": [
            * {
              * "value": 0,
              * "message": "sum of:",
              * "children": [
                * {
                  * "value": 0,
                  * "message": "weight(reviews.content:location^1.000000 in \u0000\u0000\u0000\u0000\u0000\u0000\u0003\n), product of:",
                  * "children": [
                    * {
                      * "value": 0.5320504947307548,
                      * "message": "queryWeight(reviews.content:location^1.000000), product of:",
                      * "children": [
                        * {
                          * "value": 1,
                          * "message": "boost"  
                                                                                                                                                            },
                        * {
                          * "value": 1.4291903588638628,
                          * "message": "idf(docFreq=596, maxDocs=917)"  
                                                                                                                                                            },
                        * {
                          * "value": 0.3722740581273647,
                          * "message": "queryNorm"  
                                                                                                                                                            }  
                                                                                                                                    ]  
                                                                                                              },
                    * {
                      * "value": 0,
                      * "message": "fieldWeight(reviews.content:location in \u0000\u0000\u0000\u0000\u0000\u0000\u0003\n), product of:",
                      * "children": [
                        * {
                          * "value": 0,
                          * "message": "tf(termFreq(reviews.content:location)=0"  
                                                                                                                                                            },
                        * {
                          * "value": 0,
                          * "message": "fieldNorm(field=reviews.content, doc=\u0000\u0000\u0000\u0000\u0000\u0000\u0003\n)"  
                                                                                                                                                            },
                        * {
                          * "value": 1.4291903588638628,
                          * "message": "idf(docFreq=596, maxDocs=917)"  
                                                                                                                                                            }  
                                                                                                                                    ]  
                                                                                                              }  
                                                                                          ]  
                                                                        }  
                                                        ]  
                                          },
            * {
              * "value": 1,
              * "message": "coord(1/1)"  
                                          }  
                              ]  
                    },
        * {
          * "value": 0,
          * "message": "sum of:",
          * "children": [
            * {
              * "value": 0,
              * "message": "weight(reviews.content:view^1.000000 in \u0000\u0000\u0000\u0000\u0000\u0000\u0003\n), product of:",
              * "children": [
                * {
                  * "value": 0.6867550119496617,
                  * "message": "queryWeight(reviews.content:view^1.000000), product of:",
                  * "children": [
                    * {
                      * "value": 1,
                      * "message": "boost"  
                                                                                                              },
                    * {
                      * "value": 1.8447565629585312,
                      * "message": "idf(docFreq=393, maxDocs=917)"  
                                                                                                              },
                    * {
                      * "value": 0.3722740581273647,
                      * "message": "queryNorm"  
                                                                                                              }  
                                                                                          ]  
                                                                        },
                * {
                  * "value": 0,
                  * "message": "fieldWeight(reviews.content:view in \u0000\u0000\u0000\u0000\u0000\u0000\u0003\n), product of:",
                  * "children": [
                    * {
                      * "value": 0,
                      * "message": "tf(termFreq(reviews.content:view)=0"  
                                                                                                              },
                    * {
                      * "value": 0,
                      * "message": "fieldNorm(field=reviews.content, doc=\u0000\u0000\u0000\u0000\u0000\u0000\u0003\n)"  
                                                                                                              },
                    * {
                      * "value": 1.8447565629585312,
                      * "message": "idf(docFreq=393, maxDocs=917)"  
                                                                                                              }  
                                                                                          ]  
                                                                        }  
                                                        ]  
                                          },
            * {
              * "value": 0,
              * "message": "weight(reviews.content:nice^1.000000 in \u0000\u0000\u0000\u0000\u0000\u0000\u0003\n), product of:",
              * "children": [
                * {
                  * "value": 0.4952674273751292,
                  * "message": "queryWeight(reviews.content:nice^1.000000), product of:",
                  * "children": [
                    * {
                      * "value": 1,
                      * "message": "boost"  
                                                                                                              },
                    * {
                      * "value": 1.3303839377539577,
                      * "message": "idf(docFreq=658, maxDocs=917)"  
                                                                                                              },
                    * {
                      * "value": 0.3722740581273647,
                      * "message": "queryNorm"  
                                                                                                              }  
                                                                                          ]  
                                                                        },
                * {
                  * "value": 0,
                  * "message": "fieldWeight(reviews.content:nice in \u0000\u0000\u0000\u0000\u0000\u0000\u0003\n), product of:",
                  * "children": [
                    * {
                      * "value": 0,
                      * "message": "tf(termFreq(reviews.content:nice)=0"  
                                                                                                              },
                    * {
                      * "value": 0,
                      * "message": "fieldNorm(field=reviews.content, doc=\u0000\u0000\u0000\u0000\u0000\u0000\u0003\n)"  
                                                                                                              },
                    * {
                      * "value": 1.3303839377539577,
                      * "message": "idf(docFreq=658, maxDocs=917)"  
                                                                                                              }  
                                                                                          ]  
                                                                        }  
                                                        ]  
                                          }  
                              ]  
                    }  
            ]  
      },
    * "locations": {
      * "reviews.content": {
        * "location": [
          * {
            * "pos": 312,
            * "start": 1641,
            * "end": 1649,
            * "array_positions": [
              * 4  
                                          ]  
                              }  
                    ],
        * "nice": [
          * {
            * "pos": 165,
            * "start": 840,
            * "end": 844,
            * "array_positions": [
              * 2  
                                          ]  
                              }  
                    ],
        * "view": [
          * {
            * "pos": 166,
            * "start": 845,
            * "end": 849,
            * "array_positions": [
              * 2  
                                          ]  
                              }  
                    ]  
            }  
      },
    * "fragments": {
      * "reviews.content": [
        * "…at&#39;s her name checked us in, very friendly and knowlegeable of the area. I would stay here again get area and right at the street car stop. nice resturants in walking distance. <mark>nice</mark> <mark>view</mark> of the city o…"  
            ]  
      },
    * "sort": [
      * "􏿿􏿿􏿿",
      * "􏿿􏿿􏿿",
      * "_score",
      * "hotel_7388"  
      ]  
  },
  * "..."  
],
* "total_hits": 27,
* "cost": 108906,
* "max_score": 0,
* "took": 14964461,
* "facets": null
}`

## [](#tag/Search-Indexes)Search Indexes

Use the following APIs to retrieve Search index definitions, create new Search indexes, or delete an existing Search index.

## [](#tag/Search-Indexes/operation/g-api-scoped-index)Get All Search Index Definitions (Scoped) 

Returns all Search index definitions inside the bucket and scope specified in the endpoint URL as a JSON object.

##### Authorizations:

_Read_

##### path Parameters

| BUCKET\_NAMErequired | string The name of the bucket containing the Search index definition. |
| -------------------- | --------------------------------------------------------------------- |
| SCOPE\_NAMErequired  | string The name of the scope containing the Search index definition.  |

### Responses

**200** 

A JSON object containing all Search index definitions.

get/\_p/fts/api/bucket/{BUCKET\_NAME}/scope/{SCOPE\_NAME}/index

https://{clusterId}.data.cloud.couchbase.com/\_p/fts/api/bucket/{BUCKET\_NAME}/scope/{SCOPE\_NAME}/index

### Response samples 

* 200

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "status": "ok",
* "indexDefs": {
  * "uuid": "23cf9530131858b8",
  * "indexDefs": {
    * "travel-sample.inventory.travel-hotel": {
      * "type": "fulltext-index",
      * "name": "travel-hotel",
      * "uuid": "a04a16f178846bc4",
      * "sourceType": "gocbcore",
      * "sourceName": "travel-sample",
      * "sourceUUID": "8f866261438f8b0d415a437552f3ae99",
      * "planParams": {
        * "maxPartitionsPerPIndex": 1024,
        * "indexPartitions": 1  
            },
      * "params": {
        * "doc_config": {
          * "docid_prefix_delim": "",
          * "docid_regexp": "",
          * "mode": "scope.collection.type_field",
          * "type_field": "type"  
                    },
        * "mapping": {
          * "analysis": { },
          * "default_analyzer": "standard",
          * "default_datetime_parser": "dateTimeOptional",
          * "default_field": "_all",
          * "default_mapping": {
            * "dynamic": true,
            * "enabled": false  
                              },
          * "default_type": "_default",
          * "docvalues_dynamic": false,
          * "index_dynamic": true,
          * "store_dynamic": false,
          * "type_field": "_type",
          * "types": {
            * "inventory.hotel": {
              * "dynamic": false,
              * "enabled": true,
              * "properties": {
                * "reviews": {
                  * "dynamic": false,
                  * "enabled": true,
                  * "properties": {
                    * "content": {
                      * "dynamic": false,
                      * "enabled": true,
                      * "fields": [
                        * {
                          * "docvalues": true,
                          * "include_in_all": true,
                          * "include_term_vectors": true,
                          * "index": true,
                          * "name": "content",
                          * "store": true,
                          * "type": "text"  
                                                                                                                                                            }  
                                                                                                                                    ]  
                                                                                                              }  
                                                                                          }  
                                                                        }  
                                                        }  
                                          }  
                              }  
                    },
        * "store": {
          * "indexType": "scorch",
          * "segmentVersion": 15  
                    }  
            },
      * "sourceParams": { }  
      },
    * "travel-sample.inventory.travel-test": {
      * "type": "fulltext-index",
      * "name": "travel-test",
      * "uuid": "766ddce5d41a3b41",
      * "sourceType": "gocbcore",
      * "sourceName": "travel-sample",
      * "sourceUUID": "8f866261438f8b0d415a437552f3ae99",
      * "planParams": {
        * "maxPartitionsPerPIndex": 1024,
        * "indexPartitions": 1  
            },
      * "params": {
        * "doc_config": {
          * "docid_prefix_delim": "",
          * "docid_regexp": "",
          * "mode": "scope.collection.type_field",
          * "type_field": "type"  
                    },
        * "mapping": {
          * "analysis": { },
          * "default_analyzer": "standard",
          * "default_datetime_parser": "dateTimeOptional",
          * "default_field": "_all",
          * "default_mapping": {
            * "dynamic": true,
            * "enabled": true  
                              },
          * "default_type": "_default",
          * "docvalues_dynamic": false,
          * "index_dynamic": true,
          * "store_dynamic": false,
          * "type_field": "_type"  
                    },
        * "store": {
          * "indexType": "scorch",
          * "segmentVersion": 15  
                    }  
            },
      * "sourceParams": { }  
      }  
  },
  * "implVersion": "5.7.0"  
}
}`

## [](#tag/Search-Indexes/operation/g-api-scoped-index-name)Get Index Definition (Scoped) 

Returns the Search index definition for the Search index specified in the endpoint URL as a JSON object. This endpoint is scoped and does not require a fully qualified `{INDEX_NAME}` value.

##### Authorizations:

_Read_

##### path Parameters

| BUCKET\_NAMErequired | string The name of the bucket containing the Search index definition.           |
| -------------------- | ------------------------------------------------------------------------------- |
| SCOPE\_NAMErequired  | string The name of the scope containing the Search index definition.            |
| INDEX\_NAMErequired  | string^\[A-Za-z\]\[0-9A-Za-z\_\\-\]\*$ The name of the Search index definition. |

### Responses

**200** 

A JSON object containing the Search index definition.

get/\_p/fts/api/bucket/{BUCKET\_NAME}/scope/{SCOPE\_NAME}/index/{INDEX\_NAME}

https://{clusterId}.data.cloud.couchbase.com/\_p/fts/api/bucket/{BUCKET\_NAME}/scope/{SCOPE\_NAME}/index/{INDEX\_NAME}

### Response samples 

* 200

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "status": "ok",
* "indexDef": {
  * "type": "fulltext-index",
  * "name": "color-test",
  * "uuid": "6ea521a918bd3837",
  * "sourceType": "gocbcore",
  * "sourceName": "vector-sample",
  * "sourceUUID": "614177a67bdfbd2823c5f9c3e62f5991",
  * "planParams": {
    * "maxPartitionsPerPIndex": 1024,
    * "indexPartitions": 1  
  },
  * "params": {
    * "doc_config": {
      * "docid_prefix_delim": "",
      * "docid_regexp": "",
      * "mode": "scope.collection.type_field",
      * "type_field": "type"  
      },
    * "mapping": {
      * "analysis": { },
      * "default_analyzer": "standard",
      * "default_datetime_parser": "dateTimeOptional",
      * "default_field": "_all",
      * "default_mapping": {
        * "dynamic": false,
        * "enabled": false  
            },
      * "default_type": "_default",
      * "docvalues_dynamic": false,
      * "index_dynamic": false,
      * "store_dynamic": false,
      * "type_field": "_type",
      * "types": {
        * "color.rgb": {
          * "dynamic": false,
          * "enabled": true,
          * "properties": {
            * "color": {
              * "dynamic": false,
              * "enabled": true,
              * "fields": [
                * {
                  * "analyzer": "en",
                  * "docvalues": true,
                  * "include_in_all": true,
                  * "include_term_vectors": true,
                  * "index": true,
                  * "name": "color",
                  * "store": true,
                  * "type": "text"  
                                                                        }  
                                                        ]  
                                          },
            * "colorvect_dot": {
              * "dynamic": false,
              * "enabled": true,
              * "fields": [
                * {
                  * "dims": 3,
                  * "index": true,
                  * "name": "colorvect_dot",
                  * "similarity": "dot_product",
                  * "type": "vector",
                  * "vector_index_optimized_for": "recall"  
                                                                        }  
                                                        ]  
                                          }  
                              }  
                    }  
            }  
      },
    * "store": {
      * "indexType": "scorch",
      * "segmentVersion": 16  
      }  
  },
  * "sourceParams": { }  
},
* "planPIndexes": [
  * {
    * "name": "vector-sample.color.color-test_6ea521a918bd3837_4c1c5584",
    * "uuid": "1543820346544e08",
    * "indexType": "fulltext-index",
    * "indexName": "vector-sample.color.color-test",
    * "indexUUID": "6ea521a918bd3837",
    * "sourceType": "gocbcore",
    * "sourceName": "vector-sample",
    * "sourceUUID": "614177a67bdfbd2823c5f9c3e62f5991",
    * "sourcePartitions": "0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359,360,361,362,363,364,365,366,367,368,369,370,371,372,373,374,375,376,377,378,379,380,381,382,383,384,385,386,387,388,389,390,391,392,393,394,395,396,397,398,399,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,426,427,428,429,430,431,432,433,434,435,436,437,438,439,440,441,442,443,444,445,446,447,448,449,450,451,452,453,454,455,456,457,458,459,460,461,462,463,464,465,466,467,468,469,470,471,472,473,474,475,476,477,478,479,480,481,482,483,484,485,486,487,488,489,490,491,492,493,494,495,496,497,498,499,500,501,502,503,504,505,506,507,508,509,510,511,512,513,514,515,516,517,518,519,520,521,522,523,524,525,526,527,528,529,530,531,532,533,534,535,536,537,538,539,540,541,542,543,544,545,546,547,548,549,550,551,552,553,554,555,556,557,558,559,560,561,562,563,564,565,566,567,568,569,570,571,572,573,574,575,576,577,578,579,580,581,582,583,584,585,586,587,588,589,590,591,592,593,594,595,596,597,598,599,600,601,602,603,604,605,606,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,623,624,625,626,627,628,629,630,631,632,633,634,635,636,637,638,639,640,641,642,643,644,645,646,647,648,649,650,651,652,653,654,655,656,657,658,659,660,661,662,663,664,665,666,667,668,669,670,671,672,673,674,675,676,677,678,679,680,681,682,683,684,685,686,687,688,689,690,691,692,693,694,695,696,697,698,699,700,701,702,703,704,705,706,707,708,709,710,711,712,713,714,715,716,717,718,719,720,721,722,723,724,725,726,727,728,729,730,731,732,733,734,735,736,737,738,739,740,741,742,743,744,745,746,747,748,749,750,751,752,753,754,755,756,757,758,759,760,761,762,763,764,765,766,767,768,769,770,771,772,773,774,775,776,777,778,779,780,781,782,783,784,785,786,787,788,789,790,791,792,793,794,795,796,797,798,799,800,801,802,803,804,805,806,807,808,809,810,811,812,813,814,815,816,817,818,819,820,821,822,823,824,825,826,827,828,829,830,831,832,833,834,835,836,837,838,839,840,841,842,843,844,845,846,847,848,849,850,851,852,853,854,855,856,857,858,859,860,861,862,863,864,865,866,867,868,869,870,871,872,873,874,875,876,877,878,879,880,881,882,883,884,885,886,887,888,889,890,891,892,893,894,895,896,897,898,899,900,901,902,903,904,905,906,907,908,909,910,911,912,913,914,915,916,917,918,919,920,921,922,923,924,925,926,927,928,929,930,931,932,933,934,935,936,937,938,939,940,941,942,943,944,945,946,947,948,949,950,951,952,953,954,955,956,957,958,959,960,961,962,963,964,965,966,967,968,969,970,971,972,973,974,975,976,977,978,979,980,981,982,983,984,985,986,987,988,989,990,991,992,993,994,995,996,997,998,999,1000,1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,1014,1015,1016,1017,1018,1019,1020,1021,1022,1023",
    * "nodes": {
      * "b7d460b7d4145482ac132dfa23727c5c": {
        * "canRead": true,
        * "canWrite": true,
        * "priority": 0  
            }  
      },
    * "indexParams": {
      * "doc_config": {
        * "docid_prefix_delim": "",
        * "docid_regexp": "",
        * "mode": "scope.collection.type_field",
        * "type_field": "type"  
            },
      * "mapping": {
        * "analysis": { },
        * "default_analyzer": "standard",
        * "default_datetime_parser": "dateTimeOptional",
        * "default_field": "_all",
        * "default_mapping": {
          * "dynamic": false,
          * "enabled": false  
                    },
        * "default_type": "_default",
        * "docvalues_dynamic": false,
        * "index_dynamic": false,
        * "store_dynamic": false,
        * "type_field": "_type",
        * "types": {
          * "color.rgb": {
            * "dynamic": false,
            * "enabled": true,
            * "properties": {
              * "color": {
                * "dynamic": false,
                * "enabled": true,
                * "fields": [
                  * {
                    * "analyzer": "en",
                    * "docvalues": true,
                    * "include_in_all": true,
                    * "include_term_vectors": true,
                    * "index": true,
                    * "name": "color",
                    * "store": true,
                    * "type": "text"  
                                                                                          }  
                                                                        ]  
                                                        },
              * "colorvect_dot": {
                * "dynamic": false,
                * "enabled": true,
                * "fields": [
                  * {
                    * "dims": 3,
                    * "index": true,
                    * "name": "colorvect_dot",
                    * "similarity": "dot_product",
                    * "type": "vector",
                    * "vector_index_optimized_for": "recall"  
                                                                                          }  
                                                                        ]  
                                                        }  
                                          }  
                              }  
                    }  
            },
      * "store": {
        * "indexType": "scorch",
        * "segmentVersion": 16  
            }  
      }  
  }  
],
* "warnings": [ ]
}`

## [](#tag/Search-Indexes/operation/p-api-scoped-index-name)Create or Update an Index Definition (Scoped) 

If the Search index in the endpoint URL does not exist, this endpoint uses a JSON object in the request body to create a new index. If the Search index already exists, this endpoint updates the Search index definition. This endpoint is scoped and does not require a fully qualified `{INDEX_NAME}` value.

##### Authorizations:

_Write_

##### path Parameters

| BUCKET\_NAMErequired | string The name of the bucket containing the Search index definition.           |
| -------------------- | ------------------------------------------------------------------------------- |
| SCOPE\_NAMErequired  | string The name of the scope containing the Search index definition.            |
| INDEX\_NAMErequired  | string^\[A-Za-z\]\[0-9A-Za-z\_\\-\]\*$ The name of the Search index definition. |

##### Request Body schema: application/json

required

The full Search index definition. For a detailed list of all parameters for the request body, see [Search Index JSON Properties](../search/search-index-params.html).

| namerequired       | string (Index Name) The name of the Search index. For more information, see [Initial Settings](../search/search-index-params.html#initial).                                       |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| typerequired       | string (Index Type) The type of the Search index. For more information, see [Initial Settings](../search/search-index-params.html#initial).                                       |
| sourceNamerequired | string (Source Name) The name of the bucket where the Search index is stored. For more information, see [Initial Settings](../search/search-index-params.html#initial).           |
| sourceUUID         | string (Source UUID) The UUID of the bucket where the Search index is stored. For more information, see [Initial Settings](../search/search-index-params.html#initial).           |
| sourceParams       | object (Source Parameters) Advanced settings for Search index behavior. For more information, see [Initial Settings](../search/search-index-params.html#initial).                 |
| sourceTyperequired | string (Source Type) The type of the bucket where the Search index is stored. For more information, see [Initial Settings](../search/search-index-params.html#initial).           |
| paramsrequired     | object (Index Parameters) The Search index's type identifier, type mappings, and analyzers. For more information, see [Params Object](../search/search-index-params.html#params). |
| planParamsrequired | object (Plan Parameters) The Search index's partitioning and replication settings. For more information, see [Plan Params Object](../search/search-index-params.html#planParams). |
| prevIndexUUID      | string The UUID of the previous index. Intended for clients that want to check that they are not overwriting the Search index definition updates of concurrent clients.           |
| uuid               | string (Index UUID) The UUID of the Search index. For more information, see [Initial Settings](../search/search-index-params.html#initial).                                       |

### Responses

**200** 

A JSON object indicating the status of the operation.

**default** 

The Search Service returns a non-200 HTTP error code when a request fails.

put/\_p/fts/api/bucket/{BUCKET\_NAME}/scope/{SCOPE\_NAME}/index/{INDEX\_NAME}

https://{clusterId}.data.cloud.couchbase.com/\_p/fts/api/bucket/{BUCKET\_NAME}/scope/{SCOPE\_NAME}/index/{INDEX\_NAME}

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "name": "string",
* "type": "string",
* "sourceName": "string",
* "sourceUUID": "string",
* "sourceParams": { },
* "sourceType": "string",
* "params": { },
* "planParams": {
  * "hierarchyRules": "string",
  * "maxPartitionsPerPIndex": 0,
  * "indexPartitions": 0,
  * "nodePlanParams": "string",
  * "numReplicas": 0,
  * "planFrozen": true  
},
* "prevIndexUUID": "string",
* "uuid": "string"
}`

### Response samples 

* 200
* default

Content type

application/json

Copy

`{
* "status": "ok",
* "name": "travel-sample.inventory.travel-test",
* "uuid": "654cb62baebf2d26"
}`

## [](#tag/Search-Indexes/operation/d-api-scoped-index-name)Delete Index Definition (Scoped) 

Delete the Search index definition from the bucket and scope specified in the endpoint URL. This endpoint is scoped and does not require a fully qualified `{INDEX_NAME}` value.

##### Authorizations:

_Write_

##### path Parameters

| BUCKET\_NAMErequired | string The name of the bucket containing the Search index definition.           |
| -------------------- | ------------------------------------------------------------------------------- |
| SCOPE\_NAMErequired  | string The name of the scope containing the Search index definition.            |
| INDEX\_NAMErequired  | string^\[A-Za-z\]\[0-9A-Za-z\_\\-\]\*$ The name of the Search index definition. |

### Responses

**200** 

A JSON object indicating the status of the operation.

**default** 

The Search Service returns a non-200 HTTP error code when a request fails.

delete/\_p/fts/api/bucket/{BUCKET\_NAME}/scope/{SCOPE\_NAME}/index/{INDEX\_NAME}

https://{clusterId}.data.cloud.couchbase.com/\_p/fts/api/bucket/{BUCKET\_NAME}/scope/{SCOPE\_NAME}/index/{INDEX\_NAME}

### Response samples 

* 200
* default

Content type

application/json

Copy

`{
* "status": "ok",
* "uuid": "687be6a2ad647c34"
}`