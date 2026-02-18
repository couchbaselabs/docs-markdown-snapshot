---
title: Sync Gateway Public API Reference
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.2/modules/ROOT/pages/rest_api_public.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/sync-gateway/3.2/rest_api_public.html)

# Sync Gateway Public API Reference

* Introduction
* Server
  * getGet server information
  * headCheck if server online
  * getCheck if API is available
* Database Management
  * getGet database information
  * headCheck if database exists
  * putCreate DB public API stub
  * postEnsure Full Commit
* Session
  * getGet information about the current user
  * postCreate a new user session
  * delLog out
* Authentication
  * getOpenID Connect authentication initiation via Location header redirect
  * getOpenID Connect authentication initiation via WWW-Authenticate header
  * getOpenID Connect authentication callback
  * getOpenID Connect token refresh
  * postCreate a new Facebook-based session
  * postCreate a new Google-based session
* Document
  * postCreate a new document
  * getGet a document
  * putUpsert a document
  * delDelete a document
  * headCheck if a document exists
  * getGet changes list
  * postGet changes list
  * getGets all the documents in the database with the given parameters
  * postGet all the documents in the database using a built-in view
  * postBulk document operations
  * postGet multiple documents in a MIME multipart response
  * getGet local document
  * putUpsert a local document
  * delDelete a local document
  * headCheck if local document exists
  * postCompare revisions to what is in the database
* Document Attachment
  * getGet an attachment from a document
  * putCreate or update an attachment on a document
  * headCheck if attachment exists
  * delDelete an attachment on a document
* Replication
  * getHandle incoming BLIP Sync web socket request
* Unsupported
  * getGet views of a design document | Unsupported
  * putUpdate views of a design document | Unsupported
  * delDelete a design document | Unsupported
  * headCheck if view of design document exists | Unsupported
  * getQuery a view on a design document | Unsupported
  * getOpenID Connect mock provider
  * getOpenID Connect mock login page
  * postOpenID Connect mock login page
  * postOpenID Connect mock token
  * getOpenID Connect public certificates for signing keys
  * getOpenID Connect mock login page handler
  * postOpenID Connect mock login page handler

[API docs by Redocly](https://redocly.com/redoc/)

# Sync Gateway Public REST API (3.2)

Download OpenAPI specification:

License: [Business Source License 1.1 (BSL)](https://github.com/couchbase/sync%5Fgateway/blob/master/LICENSE) 

[⬆️ Public REST API Overview](rest-api.html)

## [](#section/Introduction)Introduction

Sync Gateway manages access and synchronization between Couchbase Lite and Couchbase Server. The Sync Gateway Public REST API is used for client replication.

## [](#tag/Server)Server

Manage server activities

## [](#tag/Server/operation/get%5F-)Get server information 

Returns information about the Sync Gateway node.

### Responses

**200** 

Returned server information

get/

Public API

{protocol}://{hostname}:4984/

### Response samples 

* 200

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "ADMIN": true,
* "couchdb": "Welcome",
* "vendor": {
  * "name": "Couchbase Sync Gateway",
  * "version": 3.1  
},
* "version": "Couchbase Sync Gateway/3.1.0(1;a765231) EE",
* "persistent_config": true
}`

## [](#tag/Server/operation/head%5F-)Check if server online 

Check if the server is online by checking the status code of response.

### Responses

**200** 

Server is online

head/

Public API

{protocol}://{hostname}:4984/

## [](#tag/Server/operation/get%5F%5Fping)Check if API is available 

Returns OK status if API is available.

### Responses

**200** 

Returned status

get/\_ping

Public API

{protocol}://{hostname}:4984/\_ping

### Response samples 

* 200

Content type

text/plain

Copy

OK

## [](#tag/Database-Management)Database Management

Create and manage Sync Gateway databases

## [](#tag/Database-Management/operation/get%5Fdb-)Get database information 

Retrieve information about the database.

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

### Responses

**200** 

Successfully returned database information

**404** 

Resource could not be found

get/{db}/

Public API

{protocol}://{hostname}:4984/{db}/

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
* "compact_running": true,
* "purge_seq": 0,
* "disk_format_version": 0,
* "state": "Online",
* "server_uuid": "995618a6a6cc9ac79731bd13240e19b5"
}`

## [](#tag/Database-Management/operation/head%5Fdb-)Check if database exists 

Check if a database exists by using the response status code.

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

### Responses

**200** 

Database exists

**404** 

Resource could not be found

head/{db}/

Public API

{protocol}://{hostname}:4984/{db}/

### Response samples 

* 404

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`

## [](#tag/Database-Management/operation/put%5Ftargetdb-)Create DB public API stub 

A stub that always returns an error on the Public API, for createTarget/CouchDB compatibility.

##### path Parameters

| targetdbrequired | string The database name to target. |
| ---------------- | ----------------------------------- |

### Responses

**403** 

Database does not exist and cannot be created over the public API

**412** 

Database exists

put/{targetdb}/

Public API

{protocol}://{hostname}:4984/{targetdb}/

## [](#tag/Database-Management/operation/post%5Fdb-%5Fensure%5Ffull%5Fcommit)Ensure Full Commit  Deprecated 

This endpoint is non-functional but is present for CouchDB compatibility. This was deprecated in CouchDB 3.0.

Required Sync Gateway RBAC roles:

* Sync Gateway Application
* Sync Gateway Application Read Only

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

### Responses

**201** 

OK

post/{db}/\_ensure\_full\_commit

Public API

{protocol}://{hostname}:4984/{db}/\_ensure\_full\_commit

### Response samples 

* 201

Content type

application/json

Copy

`{
* "instance_start_time": 1644600082279583,
* "ok": true
}`

## [](#tag/Session)Session

Manage user sessions

## [](#tag/Session/operation/get%5Fdb-%5Fsession)Get information about the current user 

This will get the information about the current user.

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

### Responses

**200** 

Properties associated with a user session

**404** 

Resource could not be found

get/{db}/\_session

Public API

{protocol}://{hostname}:4984/{db}/\_session

### Response samples 

* 200
* 404

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "authentication_handlers": [
  * "string"  
],
* "ok": true,
* "userCtx": {
  * "channels": { },
  * "name": "string"  
}
}`

## [](#tag/Session/operation/post%5Fdb-%5Fsession)Create a new user session 

Generates a login session for the user based on the credentials provided in the request body or if that fails (due to invalid credentials or none provided at all), generates the new session for the currently authenticated user instead. On a successful session creation, a session cookie is stored to keep the user authenticated for future API calls.

If CORS is enabled, the origin must match an allowed login origin otherwise an error will be returned.

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### Request Body schema: application/json

The body can depend on if using the Public or Admin APIs.

| name     | string User name to generate the session for.            |
| -------- | -------------------------------------------------------- |
| password | string Password of the user to generate the session for. |

### Responses

**200** 

Session created successfully. Returned body is dependant on if using Public or Admin APIs

**400** 

Origin is not in the approved list of allowed origins

**404** 

Resource could not be found

post/{db}/\_session

Public API

{protocol}://{hostname}:4984/{db}/\_session

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "name": "string",
* "password": "string"
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
* "authentication_handlers": [
  * "default"  
],
* "ok": true,
* "userCtx": {
  * "channels": {
    * "!": 1,
    * "channelA": 2  
  },
  * "name": "string"  
}
}`

## [](#tag/Session/operation/delete%5Fdb-%5Fsession)Log out 

Invalidates the session for the currently authenticated user and removes their session cookie.

If CORS is enabled, the origin must match an allowed login origin otherwise an error will be returned.

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

### Responses

**200** 

Successfully removed session (logged out)

**400** 

Bad Request

**404** 

Resource could not be found

delete/{db}/\_session

Public API

{protocol}://{hostname}:4984/{db}/\_session

### Response samples 

* 404

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`

## [](#tag/Authentication)Authentication

Manage OpenID Connect Authentication

## [](#tag/Authentication/operation/get%5Fdb-%5Foidc)OpenID Connect authentication initiation via Location header redirect 

Called by clients to initiate the OpenID Connect Authorization Code Flow. Redirects to the OpenID Connect provider if successful. 

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### query Parameters

| provider | string The OpenID Connect provider to use for authentication. The list of providers are defined in the Sync Gateway config. If left empty, the default provider will be used.                                               |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| offline  | string If true, the OpenID Connect provider is requested to confirm with the user the permissions requested and refresh the OIDC token. To do this, access\_type=offline and prompt=consent is set on the redirection link. |

### Responses

**302** 

Successfully connected with the OpenID Connect provider so now redirecting to the requested OIDC provider for authentication.

**400** 

The provider provided is not defined in the Sync Gateway config. If no provided was specified then there is no default provider set. 

**404** 

Resource could not be found

**500** 

Unable to connect and validate with the OpenID Connect provider requested

get/{db}/\_oidc

Public API

{protocol}://{hostname}:4984/{db}/\_oidc

### Response samples 

* 404

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`

## [](#tag/Authentication/operation/get%5Fdb-%5Foidc%5Fchallenge)OpenID Connect authentication initiation via WWW-Authenticate header 

Called by clients to initiate the OpenID Connect Authorization Code Flow. This will establish a connection with the provider, then put the redirect URL in the `WWW-Authenticate` header.

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### query Parameters

| provider | string The OpenID Connect provider to use for authentication. The list of providers are defined in the Sync Gateway config. If left empty, the default provider will be used.                                               |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| offline  | string If true, the OpenID Connect provider is requested to confirm with the user the permissions requested and refresh the OIDC token. To do this, access\_type=offline and prompt=consent is set on the redirection link. |

### Responses

**400** 

The provider provided is not defined in the Sync Gateway config. If no provided was specified then there is no default provider set. 

**401** 

Successfully connected with the OpenID Connect provider so now the client can login.

**404** 

Resource could not be found

**500** 

Unable to connect and validate with the OpenID Connect provider requested

get/{db}/\_oidc\_challenge

Public API

{protocol}://{hostname}:4984/{db}/\_oidc\_challenge

### Response samples 

* 404

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`

## [](#tag/Authentication/operation/get%5Fdb-%5Foidc%5Fcallback)OpenID Connect authentication callback 

The callback URL that the client is redirected to after authenticating with the OpenID Connect provider.

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### query Parameters

| error        | string The OpenID Connect error, if any occurred.                                                                                                                                                                               |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| coderequired | string The OpenID Connect authentication code.                                                                                                                                                                                  |
| provider     | string The OpenID Connect provider to use for authentication. The list of providers are defined in the Sync Gateway config. If left empty, the default provider will be used.                                                   |
| state        | string The OpenID Connect state to verify against the state cookie. This is used to prevent cross-site request forgery (CSRF). This is not required if disable\_callback\_state=true for the provider config (NOT recommended). |

### Responses

**200** 

Successfully authenticated with OpenID Connect.

**400** 

A problem occurred when reading the callback request body

**401** 

An error was received from the OpenID Connect provider. This means the error query parameter was filled.

**404** 

Resource could not be found

**500** 

A problem occurred in regards to the token

get/{db}/\_oidc\_callback

Public API

{protocol}://{hostname}:4984/{db}/\_oidc\_callback

### Response samples 

* 200
* 404
* 500

Content type

application/json

Copy

`{
* "id_token": "string",
* "refresh_token": "string",
* "session_id": "string",
* "name": "string",
* "access_token": "string",
* "token_type": "string",
* "expires_in": 0
}`

## [](#tag/Authentication/operation/get%5Fdb-%5Foidc%5Frefresh)OpenID Connect token refresh 

Refresh the OpenID Connect token based on the provided refresh token.

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### query Parameters

| refresh\_tokenrequired | string The OpenID Connect refresh token.                                                                                                                                      |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| provider               | string The OpenID Connect provider to use for authentication. The list of providers are defined in the Sync Gateway config. If left empty, the default provider will be used. |

### Responses

**200** 

Successfully authenticated with OpenID Connect.

**400** 

The provider provided is not defined in the Sync Gateway config. If no provided was specified then there is no default provider set. 

**404** 

Resource could not be found

**500** 

Unable to connect and validate with the OpenID Connect provider requested

get/{db}/\_oidc\_refresh

Public API

{protocol}://{hostname}:4984/{db}/\_oidc\_refresh

### Response samples 

* 200
* 404

Content type

application/json

Copy

`{
* "id_token": "string",
* "refresh_token": "string",
* "session_id": "string",
* "name": "string",
* "access_token": "string",
* "token_type": "string",
* "expires_in": 0
}`

## [](#tag/Authentication/operation/post%5Fdb-%5Ffacebook)Create a new Facebook-based session  Deprecated 

Creates a new session based on a Facebook user. On a successful session creation, a session cookie is stored to keep the user authenticated for future API calls.

If CORS is enabled, the origin must match an allowed login origin otherwise an error will be returned.

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### Request Body schema: application/json

| access\_tokenrequired | string Facebook access token to base the new session on. |
| --------------------- | -------------------------------------------------------- |

### Responses

**200** 

Session created successfully

**400** 

Origin is not in the approved list of allowed origins

**401** 

Received error from Facebook verifier

**404** 

Resource could not be found

**502** 

Received invalid response from the Facebook verifier

**504** 

Unable to send request to Facebook API

post/{db}/\_facebook

Public API

{protocol}://{hostname}:4984/{db}/\_facebook

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "access_token": "string"
}`

### Response samples 

* 400
* 401
* 404
* 502
* 504

Content type

application/json

Copy

`{
* "error": "string",
* "reason": "string"
}`

## [](#tag/Authentication/operation/post%5Fdb-%5Fgoogle)Create a new Google-based session  Deprecated 

Creates a new session based on a Google user. On a successful session creation, a session cookie is stored to keep the user authenticated for future API calls.

If CORS is enabled, the origin must match an allowed login origin otherwise an error will be returned.

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### Request Body schema: application/json

| id\_tokenrequired | string Google ID token to base the new session on. |
| ----------------- | -------------------------------------------------- |

### Responses

**200** 

Session created successfully

**400** 

Origin is not in the approved list of allowed origins

**401** 

Received error from Google token verifier or invalid application ID in the config

**404** 

Resource could not be found

**502** 

Received invalid response from the Google token verifier

**504** 

Unable to send request to the Google token verifier

post/{db}/\_google

Public API

{protocol}://{hostname}:4984/{db}/\_google

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "id_token": "string"
}`

### Response samples 

* 400
* 401
* 404
* 502

Content type

application/json

Copy

`{
* "error": "string",
* "reason": "string"
}`

## [](#tag/Document)Document

Create and manage documents

## [](#tag/Document/operation/post%5Fkeyspace-)Create a new document 

Create a new document in the keyspace.

This will generate a random document ID unless specified in the body.

A document can have a maximum size of 20MB.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

##### query Parameters

| roundtrip | boolean Block until document has been received by change cache |
| --------- | -------------------------------------------------------------- |

##### Request Body schema: application/json

| \_id                               | string The ID of the document.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \_rev                              | string The revision of the document.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| \_exp                              | string Expiry time after which the document will be purged. The expiration time is set and managed on the Couchbase Server document. The value can be specified in two ways; in ISO-8601 format, for example the 6th of July 2022 at 17:00 in the BST timezone would be 2016-07-06T17:00:00+01:00; it can also be specified as a numeric Couchbase Server expiry value. Couchbase Server expiry values are specified as Unix time, and if the desired TTL is below 30 days then it can also represent an interval in seconds from the current time (for example, a value of 5 will remove the document 5 seconds after it is written to Couchbase Server). The document expiration time is returned in the response of GET /{db}/{doc}  when show\_exp=true is included in the query. As with the existing explicit purge mechanism, this applies only to the local database; it has nothing to do with replication. This expiration time is not propagated when the document is replicated. The purge of the document does not cause it to be deleted on any other database. |
| \_deleted                          | boolean Whether the document is a tombstone or not. If true, it is a tombstone.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| \_revisions                        | object                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| \_attachments                      | object                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| property name\*additional property | any                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

### Responses

**200** 

New document revision created successfully.

**400** 

There was a problem with your request

**404** 

Resource could not be found

**409** 

Resource already exists under that name

**415** 

Invalid content type

post/{keyspace}/

Public API

{protocol}://{hostname}:4984/{keyspace}/

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "_id": "string",
* "_rev": "string",
* "_exp": "string",
* "_deleted": true,
* "_revisions": {
  * "start": 0,
  * "ids": [
    * "string"  
  ]  
},
* "_attachments": {
  * "attachmentname1": {
    * "content_type": "string",
    * "data": "string"  
  },
  * "attachmentname2": {
    * "content_type": "string",
    * "data": "string"  
  }  
}
}`

### Response samples 

* 200
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
* "rev": "string"
}`

## [](#tag/Document/operation/get%5Fkeyspace-docid)Get a document 

Retrieve a document from the database by its doc ID.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docidrequired    | string Example: doc1The document ID to run the operation against.                                                                                                                                                                                                                                                                         |

##### query Parameters

| rev         | string Example: rev=2-5145e1086bb8d1d71a531e9f6b543c58The document revision to target.                                                                                                                                                                                                                                                                                                                                                   |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| open\_revs  | Array of strings Option to fetch specified revisions of the document. The value can be all to fetch all leaf revisions or an array of revision numbers (i.e. open\_revs=\["rev1", "rev2"\]). Only leaf revision bodies that haven't been pruned are guaranteed to be returned. If this option is specified the response will be in multipart format. Use the Accept: application/json request header to get the result as a JSON object. |
| show\_exp   | boolean Whether to show the expiry property (\_exp) in the response.                                                                                                                                                                                                                                                                                                                                                                     |
| revs\_from  | Array of strings Trim the revision history to stop at the first revision in the provided list. If no match is found, the revisions will be trimmed to the revs\_limit.                                                                                                                                                                                                                                                                   |
| atts\_since | Array of strings Include attachments only since specified revisions. Excludes the attachments for the specified revisions. Only gets used if attachments=true.                                                                                                                                                                                                                                                                           |
| revs\_limit | integer Maximum amount of revisions to return for each document.                                                                                                                                                                                                                                                                                                                                                                         |
| attachments | boolean Include attachment bodies in response.                                                                                                                                                                                                                                                                                                                                                                                           |
| replicator2 | boolean Returns the document with the required properties for replication. This is an enterprise-edition only feature.                                                                                                                                                                                                                                                                                                                   |

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

{protocol}://{hostname}:4984/{keyspace}/{docid}

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
* "_rev": "1-64d4a1f179db5c1848fe52967b47c166"
}`

## [](#tag/Document/operation/put%5Fkeyspace-docid)Upsert a document 

This will upsert a document meaning if it does not exist, then it will be created. Otherwise a new revision will be made for the existing document. A revision ID must be provided if targetting an existing document.

A document ID must be specified for this endpoint. To let Sync Gateway generate the ID, use the `POST /{db}/` endpoint.

If a document does exist, then replace the document content with the request body. This means unspecified fields will be removed in the new revision.

The maximum size for a document is 20MB.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docidrequired    | string Example: doc1The document ID to run the operation against.                                                                                                                                                                                                                                                                         |

##### query Parameters

| roundtrip   | boolean Block until document has been received by change cache                                                                                                                                                                                                                                                                                              |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| replicator2 | boolean Returns the document with the required properties for replication. This is an enterprise-edition only feature.                                                                                                                                                                                                                                      |
| new\_edits  | boolean Default: "true" Setting this to false indicates that the request body is an already-existing revision that should be directly inserted into the database, instead of a modification to apply to the current document. This mode is used for replication. This option must be used in conjunction with the \_revisions property in the request body. |
| rev         | string Example: rev=2-5145e1086bb8d1d71a531e9f6b543c58The document revision to target.                                                                                                                                                                                                                                                                      |

##### header Parameters

| If-Match | string The revision ID to target. |
| -------- | --------------------------------- |

##### Request Body schema: application/json

| \_id                               | string The ID of the document.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \_rev                              | string The revision of the document.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| \_exp                              | string Expiry time after which the document will be purged. The expiration time is set and managed on the Couchbase Server document. The value can be specified in two ways; in ISO-8601 format, for example the 6th of July 2022 at 17:00 in the BST timezone would be 2016-07-06T17:00:00+01:00; it can also be specified as a numeric Couchbase Server expiry value. Couchbase Server expiry values are specified as Unix time, and if the desired TTL is below 30 days then it can also represent an interval in seconds from the current time (for example, a value of 5 will remove the document 5 seconds after it is written to Couchbase Server). The document expiration time is returned in the response of GET /{db}/{doc}  when show\_exp=true is included in the query. As with the existing explicit purge mechanism, this applies only to the local database; it has nothing to do with replication. This expiration time is not propagated when the document is replicated. The purge of the document does not cause it to be deleted on any other database. |
| \_deleted                          | boolean Whether the document is a tombstone or not. If true, it is a tombstone.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| \_revisions                        | object                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| \_attachments                      | object                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| property name\*additional property | any                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

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

{protocol}://{hostname}:4984/{keyspace}/{docid}

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "_id": "string",
* "_rev": "string",
* "_exp": "string",
* "_deleted": true,
* "_revisions": {
  * "start": 0,
  * "ids": [
    * "string"  
  ]  
},
* "_attachments": {
  * "attachmentname1": {
    * "content_type": "string",
    * "data": "string"  
  },
  * "attachmentname2": {
    * "content_type": "string",
    * "data": "string"  
  }  
}
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
* "rev": "string"
}`

## [](#tag/Document/operation/delete%5Fkeyspace-docid)Delete a document 

Delete a document from the database. A new revision is created so the database can track the deletion in synchronized copies.

A revision ID either in the header or on the query parameters is required.

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

{protocol}://{hostname}:4984/{keyspace}/{docid}

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
* "rev": "string"
}`

## [](#tag/Document/operation/head%5Fkeyspace-docid)Check if a document exists 

Return a status code based on if the document exists or not.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docidrequired    | string Example: doc1The document ID to run the operation against.                                                                                                                                                                                                                                                                         |

##### query Parameters

| rev         | string Example: rev=2-5145e1086bb8d1d71a531e9f6b543c58The document revision to target.                                                                                                                                                                                                                                                                                                                                                   |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| open\_revs  | Array of strings Option to fetch specified revisions of the document. The value can be all to fetch all leaf revisions or an array of revision numbers (i.e. open\_revs=\["rev1", "rev2"\]). Only leaf revision bodies that haven't been pruned are guaranteed to be returned. If this option is specified the response will be in multipart format. Use the Accept: application/json request header to get the result as a JSON object. |
| show\_exp   | boolean Whether to show the expiry property (\_exp) in the response.                                                                                                                                                                                                                                                                                                                                                                     |
| revs\_from  | Array of strings Trim the revision history to stop at the first revision in the provided list. If no match is found, the revisions will be trimmed to the revs\_limit.                                                                                                                                                                                                                                                                   |
| atts\_since | Array of strings Include attachments only since specified revisions. Excludes the attachments for the specified revisions. Only gets used if attachments=true.                                                                                                                                                                                                                                                                           |
| revs\_limit | integer Maximum amount of revisions to return for each document.                                                                                                                                                                                                                                                                                                                                                                         |
| attachments | boolean Include attachment bodies in response.                                                                                                                                                                                                                                                                                                                                                                                           |
| replicator2 | boolean Returns the document with the required properties for replication. This is an enterprise-edition only feature.                                                                                                                                                                                                                                                                                                                   |

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

{protocol}://{hostname}:4984/{keyspace}/{docid}

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

## [](#tag/Document/operation/get%5Fkeyspace-%5Fchanges)Get changes list 

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
| feed          | string Default: "normal" Enum: "normal" "longpoll" "continuous" "websocket" The type of changes feed to use.                                                                                                                                                                                                                                                                                                                                            |

### Responses

**200** 

Successfully returned the changes feed

**400** 

There was a problem with your request

**404** 

Resource could not be found

get/{keyspace}/\_changes

Public API

{protocol}://{hostname}:4984/{keyspace}/\_changes

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

## [](#tag/Document/operation/post%5Fkeyspace-%5Fchanges)Get changes list 

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

{protocol}://{hostname}:4984/{keyspace}/\_changes

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

## [](#tag/Document/operation/get%5Fkeyspace-%5Fall%5Fdocs)Gets all the documents in the database with the given parameters 

Returns all documents in the database based on the specified parameters.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

##### query Parameters

| include\_docs | boolean Include the body associated with each document.                                                       |
| ------------- | ------------------------------------------------------------------------------------------------------------- |
| channels      | boolean Include the channels each document is part of that the calling user also has access too.              |
| access        | boolean Include what user/roles that each document grants access too.                                         |
| revs          | boolean Include all the revisions for each document under the \_revisions property.                           |
| update\_seq   | boolean Include the document sequence number update\_seq property for each document.                          |
| keys          | Array of strings An array of document ID strings to filter by.                                                |
| startkey      | string Return records starting with the specified key.                                                        |
| endkey        | string Stop returning records when this key is reached.                                                       |
| limit         | number This limits the number of result rows returned. Using a value of 0 has the same effect as the value 1. |

### Responses

**200** 

Operation ran successfully

**400** 

There was a problem with your request

**404** 

Resource could not be found

get/{keyspace}/\_all\_docs

Public API

{protocol}://{hostname}:4984/{keyspace}/\_all\_docs

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
      * "rev": "string"  
      }  
  }  
],
* "total_rows": 0,
* "update_seq": 0
}`

## [](#tag/Document/operation/post%5Fkeyspace-%5Fall%5Fdocs)Get all the documents in the database using a built-in view 

Returns all documents in the database based on the specified parameters.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

##### query Parameters

| include\_docs | boolean Include the body associated with each document.                                                       |
| ------------- | ------------------------------------------------------------------------------------------------------------- |
| channels      | boolean Include the channels each document is part of that the calling user also has access too.              |
| access        | boolean Include what user/roles that each document grants access too.                                         |
| revs          | boolean Include all the revisions for each document under the \_revisions property.                           |
| update\_seq   | boolean Include the document sequence number update\_seq property for each document.                          |
| startkey      | string Return records starting with the specified key.                                                        |
| endkey        | string Stop returning records when this key is reached.                                                       |
| limit         | number This limits the number of result rows returned. Using a value of 0 has the same effect as the value 1. |

##### Request Body schema: application/json

| keysrequired | Array of strings List of the documents to retrieve. |
| ------------ | --------------------------------------------------- |

### Responses

**200** 

Operation ran successfully

**400** 

There was a problem with your request

**404** 

Resource could not be found

post/{keyspace}/\_all\_docs

Public API

{protocol}://{hostname}:4984/{keyspace}/\_all\_docs

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "keys": [
  * "string"  
]
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
      * "rev": "string"  
      }  
  }  
],
* "total_rows": 0,
* "update_seq": 0
}`

## [](#tag/Document/operation/post%5Fkeyspace-%5Fbulk%5Fdocs)Bulk document operations 

This will allow multiple documented to be created, updated or deleted in bulk.

To create a new document, simply add the body in an object under `docs`. A doc ID will be generated by Sync Gateway unless `_id` is specified.

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

{protocol}://{hostname}:4984/{keyspace}/\_bulk\_docs

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

## [](#tag/Document/operation/post%5Fkeyspace-%5Fbulk%5Fget)Get multiple documents in a MIME multipart response 

This request returns any number of documents, as individual bodies in a MIME multipart response.

Each enclosed body contains one requested document. The bodies appear in the same order as in the request, but can also be identified by their `X-Doc-ID` and `X-Rev-ID` headers (if the `attachments` query is `true`).

A body for a document with no attachments will have content type `application/json` and contain the document itself.

A body for a document that has attachments will be written as a nested `multipart/related` body.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

##### query Parameters

| attachments | boolean Default: "false" This is for whether to include attachments in each of the documents returned or not.                                                                                                                                      |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| revs        | boolean Include all the revisions for each document under the \_revisions property.                                                                                                                                                                |
| revs\_limit | integer The number of revisions to include in the response from the document history. This parameter only makes a different if the revs query parameter is set to true. The full revision history will be returned if revs is set but this is not. |

##### header Parameters

| X-Accept-Part-Encoding | string If this header includes gzip then the part HTTP compression encoding will be done.                                                                                                                                                                                                       |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Accept-Encoding        | string If this header includes gzip then the the HTTP response will be compressed. This takes priority over X-Accept-Part-Encoding. Only part compression will be done if X-Accept-Part-Encoding=gzip and the User-Agent is below 1.2 due to clients not being able to handle full compression. |

##### Request Body schema: application/json

| docsrequired | Array of objects |
| ------------ | ---------------- |

### Responses

**200** 

Returned the requested docs as `multipart/mixed` response type

**400** 

Bad Request

**404** 

Resource could not be found

post/{keyspace}/\_bulk\_get

Public API

{protocol}://{hostname}:4984/{keyspace}/\_bulk\_get

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "docs": [
  * {
    * "id": "FooBar"  
  },
  * {
    * "id": "attachment"  
  },
  * {
    * "id": "AliceSettings"  
  }  
]
}`

### Response samples 

* 404

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`

## [](#tag/Document/operation/get%5Fkeyspace-%5Flocal-docid)Get local document 

This request retrieves a local document.

Local document IDs begin with `_local/`. Local documents are not replicated or indexed, don't support attachments, and don't save revision histories. In practice they are almost only used by Couchbase Lite's replicator, as a place to store replication checkpoint data.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docidrequired    | string The name of the local document ID excluding the \_local/ prefix.                                                                                                                                                                                                                                                                   |

### Responses

**200** 

Successfully found local document

**400** 

There was a problem with your request

**404** 

Resource could not be found

get/{keyspace}/\_local/{docid}

Public API

{protocol}://{hostname}:4984/{keyspace}/\_local/{docid}

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

## [](#tag/Document/operation/put%5Fkeyspace-%5Flocal-docid)Upsert a local document 

This request creates or updates a local document. Updating a local document requires that the revision ID be put in the body under `_rev`.

Local document IDs are given a `_local/` prefix. Local documents are not replicated or indexed, don't support attachments, and don't save revision histories. In practice they are almost only used by the client's replicator, as a place to store replication checkpoint data.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docidrequired    | string The name of the local document ID excluding the \_local/ prefix.                                                                                                                                                                                                                                                                   |

##### Request Body schema: application/json

The body of the document

| \_rev | string Revision to replace. Required if updating existing local document. |
| ----- | ------------------------------------------------------------------------- |

### Responses

**201** 

Document successfully written. The document ID will be prefixed with `_local/`.

**400** 

There was a problem with your request

**404** 

Resource could not be found

**409** 

A revision ID conflict would result from updating this document revision.

put/{keyspace}/\_local/{docid}

Public API

{protocol}://{hostname}:4984/{keyspace}/\_local/{docid}

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "_rev": "string"
}`

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
* "rev": "string"
}`

## [](#tag/Document/operation/delete%5Fkeyspace-%5Flocal-docid)Delete a local document 

This request deletes a local document.

Local document IDs begin with `_local/`. Local documents are not replicated or indexed, don't support attachments, and don't save revision histories. In practice they are almost only used by Couchbase Lite's replicator, as a place to store replication checkpoint data.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docidrequired    | string The name of the local document ID excluding the \_local/ prefix.                                                                                                                                                                                                                                                                   |

##### query Parameters

| revrequired | string The revision ID of the revision to delete. |
| ----------- | ------------------------------------------------- |

### Responses

**200** 

Successfully removed the local document.

**400** 

There was a problem with your request

**404** 

Resource could not be found

**409** 

A revision ID conflict would result from deleting this document revision.

delete/{keyspace}/\_local/{docid}

Public API

{protocol}://{hostname}:4984/{keyspace}/\_local/{docid}

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

## [](#tag/Document/operation/head%5Fkeyspace-%5Flocal-docid)Check if local document exists 

This request checks if a local document exists.

Local document IDs begin with `_local/`. Local documents are not replicated or indexed, don't support attachments, and don't save revision histories. In practice they are almost only used by Couchbase Lite's replicator, as a place to store replication checkpoint data.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docidrequired    | string The name of the local document ID excluding the \_local/ prefix.                                                                                                                                                                                                                                                                   |

### Responses

**200** 

Document exists

**400** 

There was a problem with your request

**404** 

Resource could not be found

head/{keyspace}/\_local/{docid}

Public API

{protocol}://{hostname}:4984/{keyspace}/\_local/{docid}

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

## [](#tag/Document/operation/post%5Fkeyspace-%5Frevs%5Fdiff)Compare revisions to what is in the database 

Takes a set of document IDs, each with a set of revision IDs. For each document, an array of unknown revisions are returned with an array of known revisions that may be recent ancestors.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

##### Request Body schema: application/json

| docid | Array of strings The document ID with an array of revisions to use for the comparison. |
| ----- | -------------------------------------------------------------------------------------- |

### Responses

**200** 

Comparisons successful

**404** 

Resource could not be found

post/{keyspace}/\_revs\_diff

Public API

{protocol}://{hostname}:4984/{keyspace}/\_revs\_diff

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "docid": [
  * "string"  
]
}`

### Response samples 

* 200
* 404

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "docid": {
  * "missing": [
    * "string"  
  ],
  * "possible_ancestors": [
    * "string"  
  ]  
}
}`

## [](#tag/Document-Attachment)Document Attachment

Create and manage document attachments

## [](#tag/Document-Attachment/operation/get%5Fkeyspace-docid-attach)Get an attachment from a document 

This request retrieves a file attachment associated with the document.

The raw data of the associated attachment is returned (just as if you were accessing a static file). The `Content-Type` response header is the same content type set when the document attachment was added to the database. The `Content-Disposition` response header will be set if the content type is considered unsafe to display in a browser (unless overridden by by database config option `serve_insecure_attachment_types`) which will force the attachment to be downloaded.

If the `meta` query parameter is set then the response will be in JSON with the additional metadata tags.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docidrequired    | string Example: doc1The document ID to run the operation against.                                                                                                                                                                                                                                                                         |
| attachrequired   | string The attachment name. This value must be URL encoded. For example, if the attachment name is blob\_/avatar, the path component passed to the URL should be blob\_%2Favatar (tested with [URLEncoder](https://www.urlencoder.org/)).                                                                                                 |

##### query Parameters

| rev               | string Example: rev=2-5145e1086bb8d1d71a531e9f6b543c58The document revision to target.    |
| ----------------- | ----------------------------------------------------------------------------------------- |
| content\_encoding | boolean Default: "true" Set to false to disable the Content-Encoding response header.     |
| meta              | boolean Default: "false" Return only the metadata of the attachment in the response body. |

##### header Parameters

| Range | string Example: bytes=123-456RFC-2616 bytes range header. |
| ----- | --------------------------------------------------------- |

### Responses

**200** 

Found attachment successfully.

**206** 

Partial attachment content returned

**404** 

Resource could not be found

**416** 

Requested range exceeds content length

get/{keyspace}/{docid}/{attach}

Public API

{protocol}://{hostname}:4984/{keyspace}/{docid}/{attach}

### Response samples 

* 404

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`

## [](#tag/Document-Attachment/operation/put%5Fkeyspace-docid-attach)Create or update an attachment on a document 

This request adds or updates an attachment associated with the document. If the document does not exist, it will be created and the attachment will be added to it.

If the attachment already exists, the data of the existing attachment will be replaced in the new revision.

The maximum content size of an attachment is 20MB. The `Content-Type` header of the request specifies the content type of the attachment.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docidrequired    | string Example: doc1The document ID to run the operation against.                                                                                                                                                                                                                                                                         |
| attachrequired   | string The attachment name. This value must be URL encoded. For example, if the attachment name is blob\_/avatar, the path component passed to the URL should be blob\_%2Favatar (tested with [URLEncoder](https://www.urlencoder.org/)).                                                                                                 |

##### query Parameters

| rev | string The existing document revision ID to modify. Required only when modifying an existing document. |
| --- | ------------------------------------------------------------------------------------------------------ |

##### header Parameters

| Content-Type | string Default: application/octet-stream The content type of the attachment. |
| ------------ | ---------------------------------------------------------------------------- |
| If-Match     | string An alternative way of specifying the document revision ID.            |

##### Request Body schema: Attachment content type

The attachment data

string

The content to store in the body

### Responses

**201** 

Attachment added to new or existing document successfully

**404** 

Resource could not be found

**409** 

Resource already exists under that name

put/{keyspace}/{docid}/{attach}

Public API

{protocol}://{hostname}:4984/{keyspace}/{docid}/{attach}

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
* "rev": "string"
}`

## [](#tag/Document-Attachment/operation/head%5Fkeyspace-docid-attach)Check if attachment exists 

This request check if the attachment exists on the specified document.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docidrequired    | string Example: doc1The document ID to run the operation against.                                                                                                                                                                                                                                                                         |
| attachrequired   | string The attachment name. This value must be URL encoded. For example, if the attachment name is blob\_/avatar, the path component passed to the URL should be blob\_%2Favatar (tested with [URLEncoder](https://www.urlencoder.org/)).                                                                                                 |

##### query Parameters

| rev | string Example: rev=2-5145e1086bb8d1d71a531e9f6b543c58The document revision to target. |
| --- | -------------------------------------------------------------------------------------- |

### Responses

**200** 

The document exists and the attachment exists on the document.

**404** 

Resource could not be found

head/{keyspace}/{docid}/{attach}

Public API

{protocol}://{hostname}:4984/{keyspace}/{docid}/{attach}

### Response samples 

* 404

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`

## [](#tag/Document-Attachment/operation/delete%5Fkeyspace-docid-attach)Delete an attachment on a document 

This request deletes an attachment associated with the document.

If the attachment exists, the attachment will be removed from the document.

##### path Parameters

| keyspacerequired | string Examples: db1 \- Default scope and collectiondb1.collection1 \- Named collection within the default scopedb1.scope1.collection1 \- Fully-qualified scope and collectionThe keyspace to run the operation against. A keyspace is a dot-separated string, comprised of a database name, and optionally a named scope and collection. |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| docidrequired    | string Example: doc1The document ID to run the operation against.                                                                                                                                                                                                                                                                         |
| attachrequired   | string The attachment name. This value must be URL encoded. For example, if the attachment name is blob\_/avatar, the path component passed to the URL should be blob\_%2Favatar (tested with [URLEncoder](https://www.urlencoder.org/)).                                                                                                 |

##### query Parameters

| rev | string The existing document revision ID to modify. |
| --- | --------------------------------------------------- |

##### header Parameters

| If-Match | string An alternative way of specifying the document revision ID. |
| -------- | ----------------------------------------------------------------- |

### Responses

**200** 

Attachment removed from the document successfully

**404** 

Resource could not be found

**409** 

Resource already exists under that name

delete/{keyspace}/{docid}/{attach}

Public API

{protocol}://{hostname}:4984/{keyspace}/{docid}/{attach}

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
* "rev": "string"
}`

## [](#tag/Replication)Replication

Create and manage inter-Sync Gateway replications

## [](#tag/Replication/operation/get%5Fdb-%5Fblipsync)Handle incoming BLIP Sync web socket request 

This handles incoming BLIP Sync requests from either Couchbase Lite or another Sync Gateway node. The connection has to be upgradable to a websocket connection or else the request will fail.

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### query Parameters

| client | string Default: "cbl2" Enum: "cbl2" "sgr2" This is the client type that is making the BLIP Sync request. Used to control client-type specific replication behaviour. |
| ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### Responses

**101** 

Upgraded to a web socket connection

**404** 

Resource could not be found

**426** 

Cannot upgrade connection to a web socket connection

get/{db}/\_blipsync

Public API

{protocol}://{hostname}:4984/{db}/\_blipsync

### Response samples 

* 404
* 426

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`

## [](#tag/Unsupported)Unsupported

Endpoints that are not supported by Sync Gateway

## [](#tag/Unsupported/operation/get%5Fdb-%5Fdesign-ddoc)Get views of a design document | Unsupported 

**This is unsupported**

Query a design document.

##### path Parameters

| dbrequired   | string Example: db1The name of the database to run the operation against. |
| ------------ | ------------------------------------------------------------------------- |
| ddocrequired | string The design document name.                                          |

### Responses

**200** 

Successfully returned design document.

**403** 

Forbidden access possibly due to not using the Admin API or the design document is a built-in Sync Gateway one.

**404** 

Resource could not be found

get/{db}/\_design/{ddoc}

Public API

{protocol}://{hostname}:4984/{db}/\_design/{ddoc}

### Response samples 

* 200
* 404

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "language": "string",
* "views": {
  * "viewname1": {
    * "map": "string",
    * "reduce": "string"  
  },
  * "viewname2": {
    * "map": "string",
    * "reduce": "string"  
  }  
},
* "options": {
  * "local_seq": "string",
  * "include_design": "string",
  * "raw": "string",
  * "index_xattr_on_deleted_docs": "string"  
}
}`

## [](#tag/Unsupported/operation/put%5Fdb-%5Fdesign-ddoc)Update views of a design document | Unsupported 

**This is unsupported**

Update the views of a design document.

##### path Parameters

| dbrequired   | string Example: db1The name of the database to run the operation against. |
| ------------ | ------------------------------------------------------------------------- |
| ddocrequired | string The design document name.                                          |

##### Request Body schema: application/json

| language | string |
| -------- | ------ |
| views    | object |
| options  | object |

### Responses

**200** 

Design document changes successfully

**403** 

Forbidden access possibly due to not using the Admin API or the design document is a built-in Sync Gateway one.

**404** 

Resource could not be found

put/{db}/\_design/{ddoc}

Public API

{protocol}://{hostname}:4984/{db}/\_design/{ddoc}

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "language": "string",
* "views": {
  * "viewname1": {
    * "map": "string",
    * "reduce": "string"  
  },
  * "viewname2": {
    * "map": "string",
    * "reduce": "string"  
  }  
},
* "options": {
  * "local_seq": "string",
  * "include_design": "string",
  * "raw": "string",
  * "index_xattr_on_deleted_docs": "string"  
}
}`

### Response samples 

* 404

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`

## [](#tag/Unsupported/operation/delete%5Fdb-%5Fdesign-ddoc)Delete a design document | Unsupported 

**This is unsupported**

Delete a design document.

##### path Parameters

| dbrequired   | string Example: db1The name of the database to run the operation against. |
| ------------ | ------------------------------------------------------------------------- |
| ddocrequired | string The design document name.                                          |

### Responses

**200** 

Design document deleted successfully

**403** 

Forbidden access possibly due to not using the Admin API or the design document is a built-in Sync Gateway one.

**404** 

Resource could not be found

delete/{db}/\_design/{ddoc}

Public API

{protocol}://{hostname}:4984/{db}/\_design/{ddoc}

### Response samples 

* 404

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`

## [](#tag/Unsupported/operation/head%5Fdb-%5Fdesign-ddoc)Check if view of design document exists | Unsupported 

**This is unsupported**

Check if a design document can be queried.

##### path Parameters

| dbrequired   | string Example: db1The name of the database to run the operation against. |
| ------------ | ------------------------------------------------------------------------- |
| ddocrequired | string The design document name.                                          |

### Responses

**200** 

Design document exists

**403** 

Forbidden access possibly due to not using the Admin API or the design document is a built-in Sync Gateway one.

**404** 

Resource could not be found

head/{db}/\_design/{ddoc}

Public API

{protocol}://{hostname}:4984/{db}/\_design/{ddoc}

### Response samples 

* 404

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`

## [](#tag/Unsupported/operation/get%5Fdb-%5Fdesign-ddoc-%5Fview-view)Query a view on a design document | Unsupported 

**This is unsupported**

Query a view on a design document.

##### path Parameters

| dbrequired   | string Example: db1The name of the database to run the operation against. |
| ------------ | ------------------------------------------------------------------------- |
| ddocrequired | string The design document name.                                          |
| viewrequired | string The view to target.                                                |

##### query Parameters

| inclusive\_end  | boolean Indicates whether the specified end key should be included in the result.                                                                                    |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| descending      | boolean Return documents in descending order.                                                                                                                        |
| include\_docs   | boolean Only works when using Couchbase Server 3.0 and earlier. Indicates whether to include the full content of the documents in the response.                      |
| reduce          | boolean Whether to execute a reduce function on the response or not.                                                                                                 |
| group           | boolean Group the results using the reduce function to a group or single row.                                                                                        |
| skip            | integer Skip the specified number of documents before starting to return results.                                                                                    |
| limit           | integer Return only the specified number of documents                                                                                                                |
| group\_level    | integer Specify the group level to be used.                                                                                                                          |
| startkey\_docid | string Return documents starting with the specified document identifier.                                                                                             |
| endkey\_docid   | string Stop returning records when the specified document identifier is reached.                                                                                     |
| stale           | string Enum: "ok" "update\_after" Allow the results from a stale view to be used, without triggering a rebuild of all views within the encompassing design document. |
| startkey        | string Return records starting with the specified key.                                                                                                               |
| endkey          | string Stop returning records when this key is reached.                                                                                                              |
| key             | string Return only the document that matches the specified key.                                                                                                      |
| keys            | Array of strings An array of document ID strings to filter by.                                                                                                       |

### Responses

**200** 

Returned view successfully

**403** 

Forbidden

**404** 

Resource could not be found

get/{db}/\_design/{ddoc}/\_view/{view}

Public API

{protocol}://{hostname}:4984/{db}/\_design/{ddoc}/\_view/{view}

### Response samples 

* 200
* 404

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "total_rows": 0,
* "rows": [
  * {
    * "id": "string",
    * "key": { },
    * "value": { },
    * "doc": { }  
  }  
],
* "errors": [
  * {
    * "From": "string",
    * "Reason": "string"  
  }  
]
}`

## [](#tag/Unsupported/operation/get%5Fdb-%5Foidc%5Ftesting-.well-known-openid-configuration)OpenID Connect mock provider 

Mock an OpenID Connect provider response for testing purposes. This returns a response that is the same structure as what Sync Gateway expects from an OIDC provider after initiating OIDC authentication.

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

### Responses

**200** 

Successfully generated OpenID Connect provider mock response. 

**403** 

The OpenID Connect unsupported config option `oidc_test_provider` is not enabled. To use this endpoint, this option must be enabled.

**404** 

Resource could not be found

get/{db}/\_oidc\_testing/.well-known/openid-configuration

Public API

{protocol}://{hostname}:4984/{db}/\_oidc\_testing/.well-known/openid-configuration

### Response samples 

* 200
* 404

Content type

application/json

Copy

`{
* "issuer": "string",
* "authorization_endpoint": "string",
* "token_endpoint": "string",
* "jwks_uri": "string",
* "userinfo_endpoint": "string",
* "id_token_signing_alg_values_supported": "string",
* "response_types_supported": "string",
* "subject_types_supported": "string",
* "scopes_supported": "string",
* "claims_supported": "string",
* "token_endpoint_auth_methods_supported": "string"
}`

## [](#tag/Unsupported/operation/get%5Fdb-%5Foidc%5Ftesting-authorize)OpenID Connect mock login page 

Show a mock OpenID Connect login page for the client to log in to.

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### query Parameters

| scoperequired | string The OpenID Connect authentication scope. |
| ------------- | ----------------------------------------------- |

### Responses

**200** 

OK

**400** 

A validation error occurred with the scope.

**403** 

The OpenID Connect unsupported config option `oidc_test_provider` is not enabled. To use this endpoint, this option must be enabled.

**404** 

Resource could not be found

**500** 

An error occurred.

get/{db}/\_oidc\_testing/authorize

Public API

{protocol}://{hostname}:4984/{db}/\_oidc\_testing/authorize

### Response samples 

* 400
* 404
* 500

Content type

application/json

Copy

`{
* "error": "string",
* "reason": "string"
}`

## [](#tag/Unsupported/operation/post%5Fdb-%5Foidc%5Ftesting-authorize)OpenID Connect mock login page 

Show a mock OpenID Connect login page for the client to log in to.

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### query Parameters

| scoperequired | string The OpenID Connect authentication scope. |
| ------------- | ----------------------------------------------- |

### Responses

**200** 

OK

**400** 

A validation error occurred with the scope.

**403** 

The OpenID Connect unsupported config option `oidc_test_provider` is not enabled. To use this endpoint, this option must be enabled.

**404** 

Resource could not be found

**500** 

An error occurred.

post/{db}/\_oidc\_testing/authorize

Public API

{protocol}://{hostname}:4984/{db}/\_oidc\_testing/authorize

### Response samples 

* 400
* 404
* 500

Content type

application/json

Copy

`{
* "error": "string",
* "reason": "string"
}`

## [](#tag/Unsupported/operation/post%5Fdb-%5Foidc%5Ftesting-token)OpenID Connect mock token 

Return a mock OpenID Connect token for the OIDC authentication flow.

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### Request Body schema: application/json

| grant\_typerequired | string The grant type of the token to request. Can either be an authorization\_code or refresh\_token. |
| ------------------- | ------------------------------------------------------------------------------------------------------ |
| code                | string **grant\_type=authorization\_code only**: The OpenID Connect authentication token.              |
| refresh\_token      | string **grant\_type=refresh\_token only**: The OpenID Connect refresh token.                          |

### Responses

**200** 

Properties expected back from an OpenID Connect provider after successful authentication

**400** 

Invalid token provided

**403** 

The OpenID Connect unsupported config option `oidc_test_provider` is not enabled. To use this endpoint, this option must be enabled.

**404** 

Resource could not be found

post/{db}/\_oidc\_testing/token

Public API

{protocol}://{hostname}:4984/{db}/\_oidc\_testing/token

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "grant_type": "string",
* "code": "string",
* "refresh_token": "string"
}`

### Response samples 

* 200
* 404

Content type

application/json

Copy

`{
* "access_token": "string",
* "token_type": "string",
* "refresh_token": "string",
* "expires_in": "string",
* "id_token": "string"
}`

## [](#tag/Unsupported/operation/get%5Fdb-%5Foidc%5Ftesting-certs)OpenID Connect public certificates for signing keys 

Return a mock OpenID Connect public key to be used as signing keys.

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

### Responses

**200** 

Returned public key successfully

**403** 

The OpenID Connect unsupported config option `oidc_test_provider` is not enabled. To use this endpoint, this option must be enabled.

**404** 

Resource could not be found

**500** 

An error occurred while getting the private RSA key

get/{db}/\_oidc\_testing/certs

Public API

{protocol}://{hostname}:4984/{db}/\_oidc\_testing/certs

### Response samples 

* 200
* 404
* 500

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "keys": [
  * {
    * "Key": { },
    * "KeyID": "string",
    * "Use": "string",
    * "Certificates": [
      * { }  
      ],
    * "Algorithm": "string"  
  }  
]
}`

## [](#tag/Unsupported/operation/get%5Fdb-%5Foidc%5Ftesting-authenticate)OpenID Connect mock login page handler 

Used to handle the login page displayed for the `GET /{db}/_oidc_testing/authorize` endpoint.

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### query Parameters

| redirect\_uri                  | string The Sync Gateway OpenID Connect callback URL. |
| ------------------------------ | ---------------------------------------------------- |
| scoperequired                  | string The OpenID Connect authentication scope.      |
| usernamerequired               | string                                               |
| tokenttlrequired               | integer                                              |
| identity-token-formatsrequired | string                                               |
| authenticatedrequired          | string                                               |

### Responses

**302** 

Redirecting to Sync Gateway OpenID Connect callback URL

**403** 

The OpenID Connect unsupported config option `oidc_test_provider` is not enabled. To use this endpoint, this option must be enabled.

**404** 

Resource could not be found

get/{db}/\_oidc\_testing/authenticate

Public API

{protocol}://{hostname}:4984/{db}/\_oidc\_testing/authenticate

### Response samples 

* 404

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`

## [](#tag/Unsupported/operation/post%5Fdb-%5Foidc%5Ftesting-authenticate)OpenID Connect mock login page handler 

Used to handle the login page displayed for the `GET /{db}/_oidc_testing/authorize` endpoint.

##### path Parameters

| dbrequired | string Example: db1The name of the database to run the operation against. |
| ---------- | ------------------------------------------------------------------------- |

##### query Parameters

| redirect\_uri | string The Sync Gateway OpenID Connect callback URL. |
| ------------- | ---------------------------------------------------- |
| scoperequired | string The OpenID Connect authentication scope.      |

##### Request Body schema: application/json

Properties passed from the OpenID Connect mock login page to the handler

| usernamerequired               | string |
| ------------------------------ | ------ |
| tokenttlrequired               | string |
| identity-token-formatsrequired | string |
| authenticatedrequired          | string |

### Responses

**302** 

Redirecting to Sync Gateway OpenID Connect callback URL

**403** 

The OpenID Connect unsupported config option `oidc_test_provider` is not enabled. To use this endpoint, this option must be enabled.

**404** 

Resource could not be found

post/{db}/\_oidc\_testing/authenticate

Public API

{protocol}://{hostname}:4984/{db}/\_oidc\_testing/authenticate

### Request samples 

* Payload

Content type

application/json

Copy

`{
* "username": "string",
* "tokenttl": "string",
* "identity-token-formats": "string",
* "authenticated": "string"
}`

### Response samples 

* 404

Content type

application/json

Copy

`{
* "error": "not_found",
* "reason": "no such database \"invalid-db\""
}`