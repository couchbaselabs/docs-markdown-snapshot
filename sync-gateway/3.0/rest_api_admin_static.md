---
title: Admin REST API (Static Page)
description: Description of the Sync Gateway Admin REST API, alternative
  representation as a static page
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.0/modules/ROOT/pages/rest_api_admin_static.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.0@sync-gateway::rest_api_admin_static.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.0/rest_api_admin_static.html)

# Admin REST API (Static Page)

> Description of the Sync Gateway Admin REST API, alternative representation as a static page  

Related _REST API_ topics: [Public REST API (Static Page)](rest%5Fapi%5Fpublic%5Fstatic.md) | [Metrics REST API (Static Page)](rest%5Fapi%5Fmetrics%5Fstatic.md)

## [](#%5Fpaths)Resources

This resources section groups together the available API operations under functional categories.

* [Access Control](#%5Faccess%5Fcontrol%5Fresource)
* [Authentication](#%5Fauthentication%5Fresource)
* [Bootstrap Configuration](#%5Fbootstrap%5Fconfiguration%5Fresource)
* [Database Configuration](#%5Fdatabase%5Fconfiguration%5Fresource)
* [Database Management](#%5Fdatabase%5Fmanagement%5Fresource)
* [Database Security](#%5Fdatabase%5Fsecurity%5Fresource)
* [Design Documents](#%5Fdesign%5Fdocuments%5Fresource)
* [Document](#%5Fdocument%5Fresource)
* [Logging](#%5Flogging%5Fresource)
* [Replication](#%5Freplication%5Fresource)
* [Server](#%5Fserver%5Fresource)
* [Session](#%5Fsession%5Fresource)

### [](#%5Faccess%5Fcontrol%5Fresource)Access Control

Convenience API for Sync function upsert

#### [](#%5Fget%5Fsync%5Ffunction)Get Sync Function

GET /{db}/_config/sync

##### [](#description)Description

Get the content of the current Sync Function

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Architect

##### [](#parameters)Parameters

| Type     | Name              | Description   | Schema |
| -------- | ----------------- | ------------- | ------ |
| **Path** | **db** _required_ | Database name | string |

##### [](#responses)Responses

| HTTP Code | Description                                       | Schema                          |
| --------- | ------------------------------------------------- | ------------------------------- |
| **200**   | OK                                                | [Sync\_model](#%5Fsync%5Fmodel) |
| **401**   | 401 - Unauthorized - Error validating credentials | No Content                      |

##### [](#consumes)Consumes

* `application/javascript`

##### [](#example-http-response)Example HTTP response

###### [](#response-200)Response 200

```json
"\"function(doc, oldDoc) {\\n  channel(doc.channels);\\n}\\n\\n\""
```

#### [](#%5Fupdate%5Fsync%5Ffunction)Update Sync Function

PUT /{db}/_config/sync

##### [](#description-2)Description

Use this convenience endpoint to add or update the `Sync` function for an existing Sync Gateway database

See the 'Model' below for more info

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Architect

##### [](#parameters-2)Parameters

| Type     | Name                         | Description                              | Schema                          |
| -------- | ---------------------------- | ---------------------------------------- | ------------------------------- |
| **Path** | **db** _required_            | Database name                            | string                          |
| **Body** | **sync function** _required_ | The Javascipt code for the sync function | [Sync\_model](#%5Fsync%5Fmodel) |

##### [](#responses-2)Responses

| HTTP Code | Description                                       | Schema                          |
| --------- | ------------------------------------------------- | ------------------------------- |
| **200**   | OK                                                | [Sync\_model](#%5Fsync%5Fmodel) |
| **401**   | 401 - Unauthorized - Error validating credentials | No Content                      |

##### [](#consumes-2)Consumes

* `application/javascript`

##### [](#security)Security

##### [](#example-http-request)Example HTTP request

###### [](#request-body)Request body

```json
"\"function(doc, oldDoc) {\\n  channel(doc.channels);\\n}\\n\\n\""
```

##### [](#example-http-response-2)Example HTTP response

###### [](#response-200-2)Response 200

```json
"\"function(doc, oldDoc) {\\n  channel(doc.channels);\\n}\\n\\n\""
```

#### [](#%5Fdelete%5Fsync%5Ffunction)Delete Sync Function

DELETE /{db}/_config/sync

##### [](#description-3)Description

Use this convenience endpoint to remove an existing `Sync` function

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Architect

##### [](#parameters-3)Parameters

| Type     | Name                         | Description                              | Schema                          |
| -------- | ---------------------------- | ---------------------------------------- | ------------------------------- |
| **Path** | **db** _required_            | Database name                            | string                          |
| **Body** | **sync function** _required_ | The Javascipt code for the sync function | [Sync\_model](#%5Fsync%5Fmodel) |

##### [](#responses-3)Responses

| HTTP Code | Description                                       | Schema                          |
| --------- | ------------------------------------------------- | ------------------------------- |
| **200**   | OK                                                | [Sync\_model](#%5Fsync%5Fmodel) |
| **401**   | 401 - Unauthorized - Error validating credentials | No Content                      |

##### [](#consumes-3)Consumes

* `application/javascript`

##### [](#example-http-request-2)Example HTTP request

###### [](#request-body-2)Request body

```json
"\"function(doc, oldDoc) {\\n  channel(doc.channels);\\n}\\n\\n\""
```

##### [](#example-http-response-3)Example HTTP response

###### [](#response-200-3)Response 200

```json
"\"function(doc, oldDoc) {\\n  channel(doc.channels);\\n}\\n\\n\""
```

### [](#%5Fauthentication%5Fresource)Authentication

Manage OpenID Connect providers

#### [](#%5Fdb%5Foidc%5Fget)OpenID Connect Authentication.

GET /{db}/_oidc

##### [](#description-4)Description

Called by clients to initiate the OIDC Authorization Code flow.

##### [](#parameters-4)Parameters

| Type      | Name                    | Description                                                                                                                                                                                                               | Schema  |
| --------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **Path**  | **db** _required_       | Database name                                                                                                                                                                                                             | string  |
| **Query** | **offline** _optional_  | When true, requests a refresh token from the OP. Sets access\_type=offline and prompt=consent on the redirect to the OP. Secure clients should set offline=true and persist the returned refresh token to secure storage. | boolean |
| **Query** | **provider** _optional_ | OpenId Connect provider to be used for authentication, from the list of providers defined in the Sync Gateway Config. If not specified, will attempt to authenticate using the default provider.                          | string  |

##### [](#responses-4)Responses

| HTTP Code | Description                                                                                                                                                                                                                                                                               | Schema     |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **302**   | Redirect to the requested OpenID Connect provider for authentication. Redirect link is returned in the Location header.                                                                                                                                                                   | No Content |
| **400**   | Bad request. Reason is returned as "OpenID Connect not configured for database default". If a provider was specified in the request, that provider was not defined in the Sync Gateway config. If no provider was specified, OpenID Connect is not configured in the Sync Gateway config. | No Content |
| **500**   | Server Error. Sync Gateway is unable to connect and validate the OpenID Connect provider requested.                                                                                                                                                                                       | No Content |

#### [](#%5Fdb%5Foidc%5Fcallback%5Fget)OpenID Connect Authentication callback.

GET /{db}/_oidc_callback

##### [](#description-5)Description

Sync Gateway callback URL that clients are redirected to by the OpenID Connect provider.

##### [](#parameters-5)Parameters

| Type      | Name                    | Description                                                                                                                                                                                      | Schema |
| --------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------ |
| **Path**  | **db** _required_       | Database name                                                                                                                                                                                    | string |
| **Query** | **code** _required_     | OpenID Connect Authorization code.                                                                                                                                                               | string |
| **Query** | **provider** _optional_ | OpenId Connect provider to be used for authentication, from the list of providers defined in the Sync Gateway Config. If not specified, will attempt to authenticate using the default provider. | string |

##### [](#responses-5)Responses

| HTTP Code | Description                                                  | Schema                                                          |
| --------- | ------------------------------------------------------------ | --------------------------------------------------------------- |
| **200**   | Successful OpenID Connect authentication.                    | [Response 200](#%5Fdb%5Foidc%5Fcallback%5Fget%5Fresponse%5F200) |
| **400**   | Bad request.                                                 | No Content                                                      |
| **401**   | Authentication failed. Reason returned in the response body. | No Content                                                      |

**Response 200**

| Name                          | Description                  | Schema |
| ----------------------------- | ---------------------------- | ------ |
| **access\_token** _optional_  | OpenID Connect access token  | string |
| **expires\_in** _optional_    | TTL for id\_token            | number |
| **id\_token** _optional_      | OpenID Connect ID token      | string |
| **name** _optional_           | Sync Gateway username        | string |
| **refresh\_token** _optional_ | OpenID Connect refresh token | string |
| **session\_id** _optional_    | Sync Gateway session token   | string |
| **token\_type** _optional_    | OpenID Connect token type    | string |

#### [](#%5Fdb%5Foidc%5Fchallenge%5Fget)OpenID Connect Authentication.

GET /{db}/_oidc_challenge

##### [](#description-6)Description

Called by clients to initiate the OIDC Authorization Code flow.

##### [](#parameters-6)Parameters

| Type      | Name                    | Description                                                                                                                                                                                                               | Schema  |
| --------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **Path**  | **db** _required_       | Database name                                                                                                                                                                                                             | string  |
| **Query** | **offline** _optional_  | When true, requests a refresh token from the OP. Sets access\_type=offline and prompt=consent on the redirect to the OP. Secure clients should set offline=true and persist the returned refresh token to secure storage. | boolean |
| **Query** | **provider** _optional_ | OpenId Connect provider to be used for authentication, from the list of providers defined in the Sync Gateway Config. If not specified, will attempt to authenticate using the default provider.                          | string  |

##### [](#responses-6)Responses

| HTTP Code | Description                                                                                                                                                                                                                                                                               | Schema     |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **302**   | Redirect to the requested OpenID Connect provider for authentication. Redirect link is returned in the Location header.                                                                                                                                                                   | No Content |
| **400**   | Bad request. Reason is returned as "OpenID Connect not configured for database default". If a provider was specified in the request, that provider was not defined in the Sync Gateway config. If no provider was specified, OpenID Connect is not configured in the Sync Gateway config. | No Content |
| **500**   | Server Error. Sync Gateway is unable to connect and validate the OpenID Connect provider requested.                                                                                                                                                                                       | No Content |

#### [](#%5Fdb%5Foidc%5Frefresh%5Fget)OpenID Connect refresh.

GET /{db}/_oidc_refresh

##### [](#description-7)Description

Used to obtain a new OpenID Connect ID token based on the provided refresh token.

##### [](#parameters-7)Parameters

| Type      | Name                          | Description                                                                                                                                                                                      | Schema |
| --------- | ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------ |
| **Path**  | **db** _required_             | Database name                                                                                                                                                                                    | string |
| **Query** | **provider** _optional_       | OpenId Connect provider to be used for authentication, from the list of providers defined in the Sync Gateway Config. If not specified, will attempt to authenticate using the default provider. | string |
| **Query** | **refresh\_token** _required_ | OpenID Connect refresh token.                                                                                                                                                                    | string |

##### [](#responses-7)Responses

| HTTP Code | Description                                     | Schema                                                         |
| --------- | ----------------------------------------------- | -------------------------------------------------------------- |
| **200**   | Successful OpenID Connect authentication.       | [Response 200](#%5Fdb%5Foidc%5Frefresh%5Fget%5Fresponse%5F200) |
| **400**   | Bad request.                                    | No Content                                                     |
| **401**   | Authentication failed. Unable to refresh token. | No Content                                                     |

**Response 200**

| Name                         | Description                 | Schema |
| ---------------------------- | --------------------------- | ------ |
| **access\_token** _optional_ | OpenID Connect access token | string |
| **expires\_in** _optional_   | TTL for id\_token           | number |
| **id\_token** _optional_     | OpenID Connect ID token     | string |
| **name** _optional_          | Sync Gateway username       | string |
| **session\_id** _optional_   | Sync Gateway session token  | string |
| **token\_type** _optional_   | OpenID Connect token type   | string |

### [](#%5Fbootstrap%5Fconfiguration%5Fresource)Bootstrap Configuration

Returns bootstrap settings and updates logging options

#### [](#%5Fget%5Fserver%5Fconfiguration)Get Server Configuration

GET /_config

##### [](#description-8)Description

Returns the Sync Gateway configuration of the running instance. This is a good method to check if a particular key was set correctly on the config file.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Dev Ops

##### [](#responses-8)Responses

| HTTP Code | Description                                         | Schema                                    |
| --------- | --------------------------------------------------- | ----------------------------------------- |
| **200**   | Sync Gateway configuration of the running instance. | [Bootstrap\_model](#%5Fbootstrap%5Fmodel) |

#### [](#%5Fput%5Flogging%5Foptions)Update Logging Options

PUT /_config

##### [](#description-9)Description

Update bootstrap logging options without needing a restart

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Dev Ops

##### [](#parameters-8)Parameters

| Type     | Name                                     | Schema                                |
| -------- | ---------------------------------------- | ------------------------------------- |
| **Body** | **bootstrap logging setting** _required_ | [Logging\_model](#%5Flogging%5Fmodel) |

##### [](#responses-9)Responses

| HTTP Code | Description                                 | Schema                                |
| --------- | ------------------------------------------- | ------------------------------------- |
| **200**   | Returned updated Bootstrap logging settings | [Logging\_model](#%5Flogging%5Fmodel) |

### [](#%5Fdatabase%5Fconfiguration%5Fresource)Database Configuration

Configure sync gateway databases

#### [](#%5Fdb%5Fconfig%5Fget)Get Database Configuration

GET /{db}/_config

##### [](#description-10)Description

Returns the Sync Gateway configuration of the database specified in the URL. This is a good method to check if a particular key was set correctly on the config file.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Architect

##### [](#parameters-9)Parameters

| Type     | Name              | Description   | Schema |
| -------- | ----------------- | ------------- | ------ |
| **Path** | **db** _required_ | Database name | string |

##### [](#responses-10)Responses

| HTTP Code | Description                                         | Schema     |
| --------- | --------------------------------------------------- | ---------- |
| **200**   | Sync Gateway configuration of the running instance. | No Content |

#### [](#%5Fupdate%5Fdatabase%5Fconfig)Update Database Configuration

PUT /{db}/_config

##### [](#description-11)Description

Use this endpoint to update the configuration of an existing Sync Gateway database.

Provide the database name in the URL path. Provide the required database configuration settings as a JSON object in the request body.

By default the updated database is brought online immediately, **unless** you include `"offline": true` in the configuration.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Architect
* Sync Gateway Application

##### [](#parameters-10)Parameters

| Type     | Name                                          | Description                                                                 | Schema                                  |
| -------- | --------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------- |
| **Path** | **db** _required_                             | Database name                                                               | string                                  |
| **Body** | **database configuration details** _optional_ | Provision the database configuration details as JSON object in request body | [Database\_model](#%5Fdatabase%5Fmodel) |

##### [](#responses-11)Responses

| HTTP Code | Description                                       | Schema     |
| --------- | ------------------------------------------------- | ---------- |
| **200**   | 200 - OK - Operation successful                   | No Content |
| **401**   | 401 - Unauthorized - Error validating credentials | No Content |

##### [](#security-2)Security

#### [](#%5Fget%5Fimport%5Ffilter)Get Import\_Filter Function

GET /{db}/_config/import_filter

##### [](#description-12)Description

Use this convenience endpoint to get the content of the current `import_filter`

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Architect

##### [](#parameters-11)Parameters

| Type     | Name              | Description   | Schema |
| -------- | ----------------- | ------------- | ------ |
| **Path** | **db** _required_ | Database name | string |

##### [](#responses-12)Responses

| HTTP Code | Description                                       | Schema                                               |
| --------- | ------------------------------------------------- | ---------------------------------------------------- |
| **200**   | OK                                                | [Import\_filter\_model](#%5Fimport%5Ffilter%5Fmodel) |
| **401**   | 401 - Unauthorized - Error validating credentials | No Content                                           |

##### [](#consumes-4)Consumes

* `application/javascript`

##### [](#example-http-response-4)Example HTTP response

###### [](#response-200-4)Response 200

```json
"\"function(doc) {\\n  if (doc.type != 'mobile') {\\n    return false\\n  }\\n  return true\\n}\\n\\n\""
```

#### [](#%5Fupdate%5Fimport%5Ffilter)Update Import\_Filter Function

PUT /{db}/_config/import_filter

##### [](#description-13)Description

Use this convenience endpoint to add or update the `import_filter` Javascript function for an existing Sync Gateway database.

See the 'Model' below for more info

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Architect

##### [](#parameters-12)Parameters

| Type     | Name                          | Description                                       | Schema                                               |
| -------- | ----------------------------- | ------------------------------------------------- | ---------------------------------------------------- |
| **Path** | **db** _required_             | Database name                                     | string                                               |
| **Body** | **import\_filter** _required_ | The Javascipt code for the import filter function | [Import\_filter\_model](#%5Fimport%5Ffilter%5Fmodel) |

##### [](#responses-13)Responses

| HTTP Code | Description                                       | Schema                                               |
| --------- | ------------------------------------------------- | ---------------------------------------------------- |
| **200**   | OK                                                | [Import\_filter\_model](#%5Fimport%5Ffilter%5Fmodel) |
| **401**   | 401 - Unauthorized - Error validating credentials | No Content                                           |

##### [](#consumes-5)Consumes

* `application/javascript`

##### [](#security-3)Security

##### [](#example-http-request-3)Example HTTP request

###### [](#request-body-3)Request body

```json
"\"function(doc) {\\n  if (doc.type != 'mobile') {\\n    return false\\n  }\\n  return true\\n}\\n\\n\""
```

##### [](#example-http-response-5)Example HTTP response

###### [](#response-200-5)Response 200

```json
"\"function(doc) {\\n  if (doc.type != 'mobile') {\\n    return false\\n  }\\n  return true\\n}\\n\\n\""
```

#### [](#%5Fdelete%5Fimport%5Ffilter)Delete Import\_Filter Function

DELETE /{db}/_config/import_filter

##### [](#description-14)Description

Use this convenience endpoint to remove an existing\`import\_filter\`.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Architect

##### [](#parameters-13)Parameters

| Type     | Name              | Description   | Schema |
| -------- | ----------------- | ------------- | ------ |
| **Path** | **db** _required_ | Database name | string |

##### [](#responses-14)Responses

| HTTP Code | Description                                       | Schema                                               |
| --------- | ------------------------------------------------- | ---------------------------------------------------- |
| **200**   | OK                                                | [Import\_filter\_model](#%5Fimport%5Ffilter%5Fmodel) |
| **401**   | 401 - Unauthorized - Error validating credentials | No Content                                           |

##### [](#consumes-6)Consumes

* `application/javascript`

##### [](#example-http-response-6)Example HTTP response

###### [](#response-200-6)Response 200

```json
"\"function(doc) {\\n  if (doc.type != 'mobile') {\\n    return false\\n  }\\n  return true\\n}\\n\\n\""
```

#### [](#%5Fget%5Fsync%5Ffunction)Get Sync Function

GET /{db}/_config/sync

##### [](#description-15)Description

Get the content of the current Sync Function

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Architect

##### [](#parameters-14)Parameters

| Type     | Name              | Description   | Schema |
| -------- | ----------------- | ------------- | ------ |
| **Path** | **db** _required_ | Database name | string |

##### [](#responses-15)Responses

| HTTP Code | Description                                       | Schema                          |
| --------- | ------------------------------------------------- | ------------------------------- |
| **200**   | OK                                                | [Sync\_model](#%5Fsync%5Fmodel) |
| **401**   | 401 - Unauthorized - Error validating credentials | No Content                      |

##### [](#consumes-7)Consumes

* `application/javascript`

##### [](#example-http-response-7)Example HTTP response

###### [](#response-200-7)Response 200

```json
"\"function(doc, oldDoc) {\\n  channel(doc.channels);\\n}\\n\\n\""
```

#### [](#%5Fupdate%5Fsync%5Ffunction)Update Sync Function

PUT /{db}/_config/sync

##### [](#description-16)Description

Use this convenience endpoint to add or update the `Sync` function for an existing Sync Gateway database

See the 'Model' below for more info

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Architect

##### [](#parameters-15)Parameters

| Type     | Name                         | Description                              | Schema                          |
| -------- | ---------------------------- | ---------------------------------------- | ------------------------------- |
| **Path** | **db** _required_            | Database name                            | string                          |
| **Body** | **sync function** _required_ | The Javascipt code for the sync function | [Sync\_model](#%5Fsync%5Fmodel) |

##### [](#responses-16)Responses

| HTTP Code | Description                                       | Schema                          |
| --------- | ------------------------------------------------- | ------------------------------- |
| **200**   | OK                                                | [Sync\_model](#%5Fsync%5Fmodel) |
| **401**   | 401 - Unauthorized - Error validating credentials | No Content                      |

##### [](#consumes-8)Consumes

* `application/javascript`

##### [](#security-4)Security

##### [](#example-http-request-4)Example HTTP request

###### [](#request-body-4)Request body

```json
"\"function(doc, oldDoc) {\\n  channel(doc.channels);\\n}\\n\\n\""
```

##### [](#example-http-response-8)Example HTTP response

###### [](#response-200-8)Response 200

```json
"\"function(doc, oldDoc) {\\n  channel(doc.channels);\\n}\\n\\n\""
```

#### [](#%5Fdelete%5Fsync%5Ffunction)Delete Sync Function

DELETE /{db}/_config/sync

##### [](#description-17)Description

Use this convenience endpoint to remove an existing `Sync` function

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Architect

##### [](#parameters-16)Parameters

| Type     | Name                         | Description                              | Schema                          |
| -------- | ---------------------------- | ---------------------------------------- | ------------------------------- |
| **Path** | **db** _required_            | Database name                            | string                          |
| **Body** | **sync function** _required_ | The Javascipt code for the sync function | [Sync\_model](#%5Fsync%5Fmodel) |

##### [](#responses-17)Responses

| HTTP Code | Description                                       | Schema                          |
| --------- | ------------------------------------------------- | ------------------------------- |
| **200**   | OK                                                | [Sync\_model](#%5Fsync%5Fmodel) |
| **401**   | 401 - Unauthorized - Error validating credentials | No Content                      |

##### [](#consumes-9)Consumes

* `application/javascript`

##### [](#example-http-request-5)Example HTTP request

###### [](#request-body-5)Request body

```json
"\"function(doc, oldDoc) {\\n  channel(doc.channels);\\n}\\n\\n\""
```

##### [](#example-http-response-9)Example HTTP response

###### [](#response-200-9)Response 200

```json
"\"function(doc, oldDoc) {\\n  channel(doc.channels);\\n}\\n\\n\""
```

### [](#%5Fdatabase%5Fmanagement%5Fresource)Database Management

Create and manage sync gateway databases

#### [](#%5Fget%5Fdatabase%5Finformation)Get Database Data

GET /{db}/

##### [](#description-18)Description

This request retrieves information about the database.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Dev Ops

##### [](#parameters-17)Parameters

| Type     | Name              | Description   | Schema |
| -------- | ----------------- | ------------- | ------ |
| **Path** | **db** _required_ | Database name | string |

##### [](#responses-18)Responses

| HTTP Code | Description                                                                       | Schema                                                            |
| --------- | --------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| **200**   | Request completed successfully. The information is returned in the response body. | [Response 200](#%5Fget%5Fdatabase%5Finformation%5Fresponse%5F200) |
| **401**   | Unauthorized. Login required.                                                     | No Content                                                        |
| **404**   | Not Found. Requested database not found.                                          | No Content                                                        |

**Response 200**

| Name                                 | Description                                                                                                                                                                                                            | Schema  |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **db\_name** _optional_              | Name of the database                                                                                                                                                                                                   | string  |
| **db\_uuid** _optional_              | Database identifier                                                                                                                                                                                                    | integer |
| **disk\_format\_version** _optional_ | Database schema version                                                                                                                                                                                                | integer |
| **disk\_size** _optional_            | Total amount of data stored on the disk (in bytes)                                                                                                                                                                     | integer |
| **instance\_start\_time** _optional_ | Date and time the database was opened (in microseconds since 1 January 1970)                                                                                                                                           | string  |
| **state** _optional_                 | The state of the specified database. Possible values are 'Online' and 'Offline'. A database can be taken offline and brought back online using the /{db}/\_offline and /{db}/\_online endpoints on the Admin REST API. | string  |
| **update\_seq** _optional_           | Number of updates to the database                                                                                                                                                                                      | string  |

#### [](#%5Fcreate%5Fdatabase)Create Database

PUT /{db}/

##### [](#description-19)Description

Use this method to create a new Sync Gateway database.

The database name is taken from the URL path. Pass the required database configuration settings as a JSON object in the request body.

{
    "name": "todo_db"
    "bucket": "todo_app"
}

By default the created database is brought online immediately, **unless** you include `"offline": true` in the configuration.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Architect

##### [](#parameters-18)Parameters

| Type     | Name                                          | Description                                                                 | Schema                                  |
| -------- | --------------------------------------------- | --------------------------------------------------------------------------- | --------------------------------------- |
| **Path** | **db** _required_                             | Database name                                                               | string                                  |
| **Body** | **database configuration details** _optional_ | Provision the database configuration details as JSON object in request body | [Database\_model](#%5Fdatabase%5Fmodel) |

##### [](#responses-19)Responses

| HTTP Code | Description                                       | Schema     |
| --------- | ------------------------------------------------- | ---------- |
| **201**   | 201 - OK - Create Operation successful            | No Content |
| **401**   | 401 - Unauthorized - Error validating credentials | No Content |

##### [](#security-5)Security

#### [](#%5Fdb%5Fdelete)Delete Database

DELETE /{db}/

##### [](#description-20)Description

Delete database

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Architect

##### [](#parameters-19)Parameters

| Type     | Name              | Description   | Schema |
| -------- | ----------------- | ------------- | ------ |
| **Path** | **db** _required_ | Database name | string |

##### [](#responses-20)Responses

| HTTP Code | Description                      | Schema                   |
| --------- | -------------------------------- | ------------------------ |
| **200**   | Operation completed successfully | [doc-resp](#%5Fdoc-resp) |

#### [](#%5Fdb%5Fall%5Fdocs%5Fpost)All docs

POST /{db}/_all_docs

##### [](#description-21)Description

This request retrieves specified documents from the database.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Application
* Sync Gateway Application Read Only

##### [](#parameters-20)Parameters

| Type      | Name                         | Description                                                                                                                                                                                                                                                       | Schema                 | Default |
| --------- | ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------- | ------- |
| **Path**  | **db** _required_            | Database name                                                                                                                                                                                                                                                     | string                 |         |
| **Query** | **access** _optional_        | Indicates whether to include in the response a list of what access this document grants (i.e. which users it allows to access which channels.) This option may only be used from the admin port.                                                                  | boolean                | "false" |
| **Query** | **channels** _optional_      | Indicates whether to include in the response a channels property containing an array of channels this document is assigned to. Channels not accessible by the user making the request will not be listed.                                                         | boolean                | "false" |
| **Query** | **include\_docs** _optional_ | Default is false. Indicates whether to include the associated document with each result. If there are conflicts, only the winning revision is returned.                                                                                                           | boolean                | "false" |
| **Query** | **revs** _optional_          | Default is false. Indicates whether to include a \_revisions property for each document in the response, which contains a revision history of the document. The length of the returned revision tree can be specified with the revs\_limit querystring parameter. | boolean                | "false" |
| **Query** | **update\_seq** _optional_   | Default is false. Indicates whether to include the update\_seq (document sequence ID) property in the response.                                                                                                                                                   | boolean                | "false" |
| **Body**  | **body** _optional_          | Request body                                                                                                                                                                                                                                                      | [AllDocs](#%5Falldocs) |         |

##### [](#responses-21)Responses

| HTTP Code | Description   | Schema                         |
| --------- | ------------- | ------------------------------ |
| **200**   | Query results | [QueryResult](#%5Fqueryresult) |

#### [](#%5Fdb%5Fall%5Fdocs%5Fget)All docs

GET /{db}/_all_docs

##### [](#description-22)Description

This request returns a built-in view of all the documents in the database.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Application
* Sync Gateway Application Read Only

##### [](#parameters-21)Parameters

| Type      | Name                         | Description                                                                                                                                                                                                                                                                                             | Schema           | Default |
| --------- | ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------- |
| **Path**  | **db** _required_            | Database name                                                                                                                                                                                                                                                                                           | string           |         |
| **Query** | **access** _optional_        | Indicates whether to include in the response a list of what access this document grants (i.e. which users it allows to access which channels.) This option may only be used from the admin port.                                                                                                        | boolean          | "false" |
| **Query** | **channels** _optional_      | Indicates whether to include in the response a channels property containing an array of channels this document is assigned to. Channels not accessible by the user making the request will not be listed.                                                                                               | boolean          | "false" |
| **Query** | **endkey** _optional_        | If this parameter is provided, stop returning records when the specified key is reached.                                                                                                                                                                                                                | string           |         |
| **Query** | **include\_docs** _optional_ | Default is false. Indicates whether to include the associated document with each result. If there are conflicts, only the winning revision is returned.                                                                                                                                                 | boolean          | "false" |
| **Query** | **keys** _optional_          | Specify a list of document IDs. Note that this is an array field, so to retrieve docs with Ids of "keyid1" and "keyid4", for example, use a request in this format – curl -X GET \\ '[%22keyid1%22,%22keyid4%22](http://localhost:4985/test%5Fdb/%5Fall%5Fdocs?keys=)' \\ -H 'Accept: application/json' | < string > array |         |
| **Query** | **limit** _optional_         | Limits the number of result rows to the specified value. Using a value of 0 has the same effect as the value 1.                                                                                                                                                                                         | integer          |         |
| **Query** | **revs** _optional_          | Default is false. Indicates whether to include a \_revisions property for each document in the response, which contains a revision history of the document. The length of the returned revision tree can be specified with the revs\_limit querystring parameter.                                       | boolean          | "false" |
| **Query** | **startkey** _optional_      | Returns records starting with the specified key.                                                                                                                                                                                                                                                        | string           |         |
| **Query** | **update\_seq** _optional_   | Default is false. Indicates whether to include the update\_seq (document sequence ID) property in the response.                                                                                                                                                                                         | boolean          | "false" |

##### [](#responses-22)Responses

| HTTP Code | Description   | Schema                         |
| --------- | ------------- | ------------------------------ |
| **200**   | Query results | [QueryResult](#%5Fqueryresult) |

#### [](#%5Fdb%5Fbulk%5Fdocs%5Fpost)Add, Update or Delete Bulk Documents

POST /{db}/_bulk_docs

##### [](#description-23)Description

This request enables you to add, update, or delete multiple documents to a database in a single request. To add new documents, you can either specify the ID (`_id`) or let the software create an ID. To update existing documents, you must provide the document ID, revision identifier (`_rev`), and new document values. To delete existing documents you must provide the document ID, revision identifier, and the deletion flag (`_deleted`).

The JSON returned by the `_bulk_docs` operation consists of an array of JSON structures, one for each document in the original submission. The returned JSON structure should be examined to ensure that all of the documents submitted in the original request were successfully added to the database.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Application

##### [](#parameters-22)Parameters

| Type     | Name                        | Description      | Schema                                                     |
| -------- | --------------------------- | ---------------- | ---------------------------------------------------------- |
| **Path** | **db** _required_           | Database name    | string                                                     |
| **Body** | **BulkDocsBody** _optional_ | The request body | [BulkDocsBody](#%5Fdb%5Fbulk%5Fdocs%5Fpost%5Fbulkdocsbody) |

**BulkDocsBody**

| Name                      | Description                                                                                                                                                               | Schema                                             |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| **docs** _optional_       | List containing new or updated documents. Each object in the array can contain the following properties \_id, \_rev, \_deleted, and values for new and updated documents. | < [Document\_model](#%5Fdocument%5Fmodel) \> array |
| **new\_edits** _optional_ | Indicates whether to assign new revision identifiers to new edits. **Default** : true                                                                                     | boolean                                            |

##### [](#responses-23)Responses

| HTTP Code | Description                                                                                                                                       | Schema                                 |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| **201**   | Documents have been created or updated. The response object is an array with the status for each document submitted in the original request.      | [BulkDocsSuccess](#%5Fbulkdocssuccess) |
| **409**   | The operation failed with a forbidden error. Probably because the document already exists in the database but a revision number wasn't specified. | [Forbidden](#%5Fforbidden)             |

#### [](#%5Fdb%5Fbulk%5Fget%5Fpost)Get Bulk Documents

POST /{db}/_bulk_get

##### [](#description-24)Description

This request returns any number of documents, as individual bodies in a MIME multipart response.

Each enclosed body contains one requested document. The bodies appear in the same order as in the request, but can also be identified by their X-Doc-ID and X-Rev-ID headers. - A body for a document with no attachments will have content type application/json and contain the document itself. - A body for a document that has attachments will be written as a nested multipart/related body. Its first part will be the document's JSON, and the subsequent parts will be the attachments (each identified by a Content-Disposition header giving its attachment name.)

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Application
* Sync Gateway Application Read Only

##### [](#parameters-23)Parameters

| Type      | Name                       | Description                                                                                                                                                                                                                                                                                                | Schema                                                             | Default |
| --------- | -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ------- |
| **Path**  | **db** _required_          | Database name                                                                                                                                                                                                                                                                                              | string                                                             |         |
| **Query** | **attachments** _optional_ | Include attachment bodies in response. Default is false.                                                                                                                                                                                                                                                   | boolean                                                            | "false" |
| **Query** | **revs** _optional_        | Default is false. Indicates whether to include a \_revisions property for each document in the response, which contains a revision history of the document. The length of the returned revision tree can be specified with the revs\_limit querystring parameter.                                          | boolean                                                            | "false" |
| **Query** | **revs\_limit** _optional_ | The number of revisions to include in the response from the document history. This property is only honoured if revs=true is also sent in the request. If revs=true is specified and revs\_limit isn't, the full revision history is returned. For more information see: [Revisions](revisions.html) page. | integer                                                            |         |
| **Body**  | **BulkGetBody** _optional_ | List of documents being requested. Each array element is an object that must contain an id property giving the document ID. It may contain a rev property if a specific revision is desired. It may contain an atts\_since property (as in a single-document GET) to limit which attachments are sent.     | < [BulkGetBody](#%5Fdb%5Fbulk%5Fget%5Fpost%5Fbulkgetbody) \> array |         |

**BulkGetBody**

| Name                      | Description  | Schema |
| ------------------------- | ------------ | ------ |
| **att\_since** _optional_ | att\_since   | string |
| **id** _optional_         | Document ID. | string |
| **rev** _optional_        | rev          | string |

##### [](#responses-24)Responses

| HTTP Code | Description                                                                                                                                                                                | Schema                                                      |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------- |
| **200**   | Request completed successfully                                                                                                                                                             | No Content                                                  |
| **301**   | Request failed with a forbidden error. This usually happens because the user requesting that document doesn't have access to it. Access to documents is granted to users through channels. | [Response 301](#%5Fdb%5Fbulk%5Fget%5Fpost%5Fresponse%5F301) |

**Response 301**

| Name                     | Description                            | Schema  |
| ------------------------ | -------------------------------------- | ------- |
| **\_id** _optional_      | The document ID that was requested     | string  |
| **\_removed** _optional_ | **Default** : true                     | boolean |
| **\_rev** _optional_     | The revision number that was requested | string  |

##### [](#produces)Produces

* `multipart/mixed`

##### [](#example-http-response-10)Example HTTP response

###### [](#response-200-10)Response 200

```json
{
  "multipart/mixed (document found)" : "--1cba224ff2aa106566e3ab65de9c861c24558ba368f8cd7f6fcde53b88f4\nContent-Type: application/json\n\n{\"_id\":\"doc123\",\"_rev\":\"1-c543d6514c609f65180f94af247aaffe\",\"hello\":\"world!\"}\n--1cba224ff2aa106566e3ab65de9c861c24558ba368f8cd7f6fcde53b88f4\n",
  "multipart/mixed (document not found)" : "--1cba224ff2aa106566e3ab65de9c861c24558ba368f8cd7f6fcde53b88f4\nContent-Type: application/json; error=\"true\"\n\n{\"error\":\"not_found\",\"id\":\"doc1234\",\"reason\":\"missing\",\"status\":404}\n--1cba224ff2aa106566e3ab65de9c861c24558ba368f8cd7f6fcde53b88f4\n"
}
```

#### [](#%5Fdb%5Fchanges%5Fpost)Changes

POST /{db}/_changes

##### [](#description-25)Description

Same as the GET /\_changes request except the parameters are in the JSON body.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Application
* Sync Gateway Application Read Only

##### [](#parameters-24)Parameters

| Type     | Name                       | Description      | Schema                                               |
| -------- | -------------------------- | ---------------- | ---------------------------------------------------- |
| **Path** | **db** _required_          | Database name    | string                                               |
| **Body** | **ChangesBody** _optional_ | The request body | [ChangesBody](#%5Fdb%5Fchanges%5Fpost%5Fchangesbody) |

**ChangesBody**

| Name                         | Description                                                                                                                                                                                                                                                                                                                      | Schema           |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| **active\_only** _optional_  | Default is false. When true, the changes response doesn't include either deleted documents, or notification for documents that the user no longer has access to. **Default** : false                                                                                                                                             | boolean          |
| **channels** _optional_      | A comma-separated list of channel names. The response will be filtered to only documents in these channels. (This parameter must be used with the sync\_gateway/bychannel filter parameter; see below.)                                                                                                                          | string           |
| **doc\_ids** _optional_      | A list of document IDs as a valid JSON array. The response will be filtered to only documents with these IDs. (This parameter must be used with the \_doc\_ids filter parameter; see below.)                                                                                                                                     | < string > array |
| **feed** _optional_          | Default is 'normal'. Specifies type of change feed. Valid values are normal, continuous, longpoll, websocket. **Default** : "normal"                                                                                                                                                                                             | string           |
| **filter** _optional_        | Indicates that the returned documents should be filtered. The valid values are sync\_gateway/bychannel and \_doc\_ids.                                                                                                                                                                                                           | string           |
| **heartbeat** _optional_     | Default is 0\. Interval in milliseconds at which an empty line (CRLF) is written to the response. This helps prevent gateways from deciding the socket is idle and closing it. Only applicable to longpoll or continuous feeds. Overrides any timeout to keep the feed alive indefinitely. Setting to 0 results in no heartbeat. | integer          |
| **include\_docs** _optional_ | Default is false. Indicates whether to include the associated document with each result. If there are conflicts, only the winning revision is returned. **Default** : false                                                                                                                                                      | boolean          |
| **limit** _optional_         | Limits the number of result rows to the specified value. Using a value of 0 has the same effect as the value 1.                                                                                                                                                                                                                  | integer          |
| **since** _optional_         | Starts the results from the change immediately after the given sequence ID. Sequence IDs should be considered opaque; they come from the last\_seq property of a prior response.                                                                                                                                                 | object           |
| **style** _optional_         | Default is 'main\_only'. Number of revisions to return in the changes array. The only possible value is all\_docs and it returns all leaf revisions including conflicts and deleted former conflicts. **Default** : "main\_only"                                                                                                 | string           |
| **timeout** _optional_       | Default is 300000\. Maximum period in milliseconds to wait for a change before the response is sent, even if there are no results. Only applicable for longpoll or continuous feeds. Setting to 0 results in no timeout.                                                                                                         | integer          |

##### [](#responses-25)Responses

| HTTP Code | Description                    | Schema                 |
| --------- | ------------------------------ | ---------------------- |
| **200**   | Request completed successfully | [Changes](#%5Fchanges) |

#### [](#%5Fdb%5Fchanges%5Fget)Get List of Changes (query parameters)

GET /{db}/_changes

##### [](#description-26)Description

This request retrieves a sorted list of changes made to documents in the database, in time order of application.

Each document appears at most once, ordered by its most recent change, regardless of how many times it's been changed. This request can be used to listen for update and modifications to the database for post processing or synchronization. A continuously connected changes feed is a reasonable approach for generating a real-time log for most applications.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Application
* Sync Gateway Application Read Only

##### [](#parameters-25)Parameters

| Type      | Name                         | Description                                                                                                                                                                                                                                                                                                                      | Schema           | Default      |
| --------- | ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------------ |
| **Path**  | **db** _required_            | Database name                                                                                                                                                                                                                                                                                                                    | string           |              |
| **Query** | **active\_only** _optional_  | Default is false. When true, the changes response doesn't include either deleted documents, or notification for documents that the user no longer has access to.                                                                                                                                                                 | boolean          | "false"      |
| **Query** | **channels** _optional_      | A comma-separated list of channel names. The response will be filtered to only documents in these channels. (This parameter must be used with the **sync\_gateway/bychannel** filter parameter; see below.)                                                                                                                      | string           |              |
| **Query** | **doc\_ids** _optional_      | A list of document IDs as a valid JSON array. The response will be filtered to only documents with these IDs. This parameter must be used with the filter=\_doc\_ids and feed=normal parameters.                                                                                                                                 | < string > array |              |
| **Query** | **feed** _optional_          | Default is 'normal'. Specifies type of change feed. Valid values are normal, continuous, longpoll, websocket.                                                                                                                                                                                                                    | string           | "normal"     |
| **Query** | **filter** _optional_        | Indicates that the reported documents should be filtered. The valid values are sync\_gateway/bychannel and \_doc\_ids.                                                                                                                                                                                                           | string           |              |
| **Query** | **heartbeat** _optional_     | Default is 0\. Interval in milliseconds at which an empty line (CRLF) is written to the response. This helps prevent gateways from deciding the socket is idle and closing it. Only applicable to longpoll or continuous feeds. Overrides any timeout to keep the feed alive indefinitely. Setting to 0 results in no heartbeat. | integer          | 0            |
| **Query** | **include\_docs** _optional_ | Default is false. Indicates whether to include the associated document with each result. If there are conflicts, only the winning revision is returned.                                                                                                                                                                          | boolean          | "false"      |
| **Query** | **limit** _optional_         | Limits the number of result rows to the specified value. Using a value of 0 has the same effect as the value 1.                                                                                                                                                                                                                  | integer          |              |
| **Query** | **since** _optional_         | Starts the results from the change immediately after the given sequence ID. Sequence IDs should be considered opaque; they come from the last\_seq property of a prior response.                                                                                                                                                 | integer          |              |
| **Query** | **style** _optional_         | Default is 'main\_only'. Number of revisions to return in the changes array. main\_only returns the current winning revision, all\_docs returns all leaf revisions including conflicts and deleted former conflicts.                                                                                                             | string           | "main\_only" |
| **Query** | **timeout** _optional_       | Default is 300000\. Maximum period in milliseconds to wait for a change before the response is sent, even if there are no results. Only applicable for longpoll or continuous feeds. Setting to 0 results in no timeout.                                                                                                         | integer          | 300000       |

##### [](#responses-26)Responses

| HTTP Code | Description                    | Schema                 |
| --------- | ------------------------------ | ---------------------- |
| **200**   | Request completed successfully | [Changes](#%5Fchanges) |

#### [](#%5Fdb%5Fcompact%5Fpost)Compact Database

POST /{db}/_compact

##### [](#description-27)Description

Use the `/{db}/_compact` endpoint to start a compaction process. The process purges the JSON bodies of non-leaf revisions.

Using this endpoint following a failed compaction will trigger a restart of the compact\_id at the appropriate phase (where possible).

This process is also run periodically by the system.

Note - Leaf revisions are not purged during compaction.

Compaction does not remove JSON bodies of leaf nodes (conflicting branches). So it is also important to resolve conflicts in your application in order to re-claim disk space.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Architect

##### [](#parameters-26)Parameters

| Type      | Name                    | Description                                                                                                                                                                                                                                                                                                       | Schema | Default     |
| --------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | ----------- |
| **Path**  | **db** _required_       | Database name                                                                                                                                                                                                                                                                                                     | string |             |
| **Query** | **action** _optional_   | Use the action parameter to _start_ or _stop_ a \_compact process. The value must be one of : - start \- immediately starts (or restarts) a compaction and returns its status \* stop \- immediately stops the active compaction and returns the status This parameter works in conjunction with compaction type. | string | "start"     |
| **Query** | **dry\_run** _optional_ | Use dry\_run only for attachment compaction. If this is set to true the process will run but will not execute the final purge of attachments. It can be used to check how many attachments will be purged.                                                                                                        | string | "false"     |
| **Query** | **reset** _optional_    | Use reset only for attachment compaction. If this is set to true the start action will not attempt to resume a failed process but will force a fresh compact to start.                                                                                                                                            | string | "false"     |
| **Query** | **type** _optional_     | Use the type option to specify the type of compaction required. The type must be one of : - attachment for legacy pre-3.0 attachment compaction \* tombstone for database compaction, which purges the JSON bodies of non-leaf revisions. This parameter works in conjunction with compaction action.             | string | "tombstone" |

##### [](#responses-27)Responses

| HTTP Code | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Schema                                      |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| **200**   | OK - This successful response indicates \_compact process was started. The response body comprises a JSON object showing the \_compact status.                                                                                                                                                                                                                                                                                                                                                                                                                                  | [Compact\_Response](#%5Fcompact%5Fresponse) |
| **400**   | Bad Request This can mean that a required parameter has not been provided, the value supplied is invalid, or the combination of provided parameters is invalid. Compaction API returns a 400 Bad Request error in the following cases: - A GET /{db}/\_compact request is submitted with an invalid value for type parameter (anything other than tombstone or attachment). - A POST /{db}/\_compact request is submitted with an invalid value for type parameter (type must be either tombstone or attachment) and or action parameter (action must be either start or stop). | No Content                                  |
| **503**   | Service Unavailable A 503 Service Unavailable error indicates that the system is not ready to handle the submitted compaction start request due another compaction is running. You may encounter this error when you submit a compaction request in the middle of another.                                                                                                                                                                                                                                                                                                      | No Content                                  |

#### [](#%5Fdb%5Fcompact%5Fget)Get Compact Status

GET /{db}/_compact

##### [](#description-28)Description

Use this request to return the current status of a compaction.

Set the `type` parameter to one of: - tombstone - A GET request to /{db}/\_compact?type=tombstone returns the number of tombstones removed. - attachment - A GET request to /{db}/\_compact?type=attachment returns the number of attachments that are removed from the bucket.

For example: `{ "status": "running", "start_time": "2021-12-02T18:26:17.086152Z", "last_error": "", "marked_attachments": 0, "purged_attachments": 0, "compact_id": "68302d2d-2c56-434e-94e0-33c0d0437828", "phase": "cleanup" }`

##### [](#parameters-27)Parameters

| Type      | Name                | Description                                                                                                                                                                                                                                                                                           | Schema | Default     |
| --------- | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | ----------- |
| **Path**  | **db** _required_   | Database name                                                                                                                                                                                                                                                                                         | string |             |
| **Query** | **type** _optional_ | Use the type option to specify the type of compaction required. The type must be one of : - attachment for legacy pre-3.0 attachment compaction \* tombstone for database compaction, which purges the JSON bodies of non-leaf revisions. This parameter works in conjunction with compaction action. | string | "tombstone" |

##### [](#responses-28)Responses

| HTTP Code | Description                                                                                                                                                | Schema                                      |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| **200**   | OK - A successful response will return a JSON object containing the \_compact status. The current phase of running compact processes is returned in phase. | [Compact\_Response](#%5Fcompact%5Fresponse) |

#### [](#%5Ftake%5Fdatabase%5Foffline)Take Database Offline

POST /{db}/_offline

##### [](#description-29)Description

This request takes the specified database offline.

An offline database is not accessible through Sync Gateway's Public REST API. However, some commands can be given to Sync Gateway through the Admin REST API.

Taking a database offline will:

* Cleanly closes all active `_changes` feeds for this database.
* Rejects all access to the database through the Public REST API (503 Service Unavailable).
* Rejects most Admin API requests (503 Service Unavailable). A specific, short list of Admin REST API requests remain available (`GET /{db}`, `PUT /{db}/_config`, `POST /{db}/_resync`).
* Stops webhook event handlers.
* Does not take the backing Couchbase Server bucket offline. The bucket remains available and Sync Gateway keeps its connection to the bucket.

When a database is offline, you can load properties for the database, without stopping and re-starting the Sync Gateway instance. The new properties are applied when the database is brought online.

Taking a database offline that is in the progress of coming online will take the database offline after it comes online.

For more information about taking a database offline and bringing it back online, see [this guide](database-offline.html).

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Architect

##### [](#parameters-28)Parameters

| Type     | Name              | Description   | Schema |
| -------- | ----------------- | ------------- | ------ |
| **Path** | **db** _required_ | Database name | string |

##### [](#responses-29)Responses

| HTTP Code | Description             | Schema     |
| --------- | ----------------------- | ---------- |
| **200**   | Database brought online | No Content |

#### [](#%5Fdb%5Fonline%5Fpost)Bring Database Online.

POST /{db}/_online

##### [](#description-30)Description

When a database is online, Sync Gateway serves both Public and Admin REST API requests for the database. This request brings the specified database online, either immediately or after a specified delay.

Bringing a database online:

* Closes the databases connection to the backing Couchbase Server bucket.
* Reloads the database configuration, and connects to the backing Couchbase Server bucket.
* Re-establishes access to the database from the Public REST API.
* Accepts all Admin API requests.

You can bring an offline database online after a specific delay. Uses for this include:

* Making a database available for Couchbase Mobile clients at a specific time.
* Making databases on several Sync Gateway instances available at the same time.

For more information about taking a database offline and bringing it back online, see [this guide](database-offline.html).

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Architect

##### [](#parameters-29)Parameters

| Type     | Name                | Description                               | Schema                                |
| -------- | ------------------- | ----------------------------------------- | ------------------------------------- |
| **Path** | **db** _required_   | Database name                             | string                                |
| **Body** | **body** _optional_ | Optional request body to specify a delay. | [body](#%5Fdb%5Fonline%5Fpost%5Fbody) |

**body**

| Name                 | Description                                           | Schema  |
| -------------------- | ----------------------------------------------------- | ------- |
| **delay** _optional_ | Delay in seconds before bringing the database online. | integer |

##### [](#responses-30)Responses

| HTTP Code | Description                                           | Schema     |
| --------- | ----------------------------------------------------- | ---------- |
| **200**   | OK - online request accepted.                         | No Content |
| **503**   | Service Unavailable - Database resync is in progress. | No Content |

#### [](#%5Fdb%5Fresync%5Fpost)Start or Stop Resync

POST /{db}/_resync

##### [](#description-31)Description

Use the \_resync operation whenever you have modified the database's sync function such that the channel or access mappings for any existing document would change as a result.

The request will start or stop the \_resync process depending upon the `action` parameter provided. If no `action` parameter is given then `start` is assumed.

**`action=start`**

The start action causes all documents to be reprocessed by the database's sync function. This is an **asynchronous** operation.

When the sync function is invoked by `_resync`, the requireUser() and requireRole() calls will always return 'true'.

A \_resync operation on a database that is not in the offline state will be rejected (503 Service Unavailable).

**`action=stop`**

The currently running resync operation is stopped.

**`regenerate_sequences=true`** **Use this only when requested to do so by the Couchbase support team**

This request will start a resync while regenerating sequences.

The resync action is carried out **only** on the node that the POST is made to. It is not cross-node aware.

In a multi-node cluster, the resync must be only run on one node. Users should bring other nodes offline before initiating this action. Starting it on more than one node will result in multiple resyncs running, with undefined system behavior.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Architect

##### [](#parameters-30)Parameters

| Type      | Name                                 | Description                                                                                                                                                                                                        | Schema | Default |
| --------- | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------ | ------- |
| **Path**  | **db** _required_                    | Database name                                                                                                                                                                                                      | string |         |
| **Query** | **action** _optional_                | The action query can be "start" or "stop". If neither is provided,"start" is used as the default. \* Start will 'begin' the asynchrounous resync operation. \* Stop will stop the resync operation and will return | string | "start" |
| **Query** | **regenerate\_sequences** _optional_ | **Use this only when requested to do so by the Couchbase support team** Set **regenerate\_sequences=true** along with action=start in order to begin a resync while regenerating sequences.                        | string | "none"  |

##### [](#responses-31)Responses

| HTTP Code | Description                                                                                                                                                                                      | Schema                                 |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------- |
| **200**   | OK                                                                                                                                                                                               | [Resync-response](#%5Fresync-response) |
| **400**   | 400 - Database \_resync not running                                                                                                                                                              | No Content                             |
| **503**   | 503 error code. The meaning varies depending on the action parameter: \* action=start - Database must be offline before calling \_resync. \* action=stop - Database \_resync already in progress | No Content                             |

#### [](#%5Fdb%5Fresync%5Fget)Show resync status

GET /{db}/_resync

##### [](#description-32)Description

This request returns the status of the asynchronous `_resync` operation, including:

* status
* docs processed
* docs changed
* last error (if any)

**Sync Gateway Roles Required:**

* Sync Gateway Architect

##### [](#parameters-31)Parameters

| Type     | Name              | Description   | Schema |
| -------- | ----------------- | ------------- | ------ |
| **Path** | **db** _required_ | Database name | string |

##### [](#responses-32)Responses

| HTTP Code | Description | Schema                                 |
| --------- | ----------- | -------------------------------------- |
| **200**   | OK          | [Resync-response](#%5Fresync-response) |

#### [](#%5Fdb%5Frevs%5Fdiff%5Fpost)Get Revisions DIff List

POST /{db}/_revs_diff

##### [](#description-33)Description

Given a set of document/revision IDs, returns the subset of those that do not correspond to revisions stored in the database.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Application

##### [](#parameters-32)Parameters

| Type     | Name                | Description   | Schema                                                |
| -------- | ------------------- | ------------- | ----------------------------------------------------- |
| **Path** | **db** _required_   | Database name | string                                                |
| **Body** | **body** _optional_ | Request body  | < [body](#%5Fdb%5Frevs%5Fdiff%5Fpost%5Fbody) \> array |

**body**

| Name                 | Description | Schema |
| -------------------- | ----------- | ------ |
| **key** _optional_   | document id | string |
| **value** _optional_ | revision id | string |

##### [](#responses-33)Responses

| HTTP Code | Description                                                                                                                 | Schema                                                                  |
| --------- | --------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| **200**   | The request was successful. Returns a list of revision IDs for that document (the ones that are not stored in the database) | < [Response 200](#%5Fdb%5Frevs%5Fdiff%5Fpost%5Fresponse%5F200) \> array |

**Response 200**

| Name                 | Description | Schema |
| -------------------- | ----------- | ------ |
| **key** _optional_   | document id | string |
| **value** _optional_ | revision id | string |

### [](#%5Fdatabase%5Fsecurity%5Fresource)Database Security

Create and manage database users and roles

#### [](#%5Fdb%5Frole%5Fpost)Create New Role

POST /{db}/_role

##### [](#description-34)Description

This request creates a new role

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Architect
* Sync Gateway Application

##### [](#parameters-33)Parameters

| Type     | Name                | Description                                                              | Schema                          |
| -------- | ------------------- | ------------------------------------------------------------------------ | ------------------------------- |
| **Path** | **db** _required_   | Database name                                                            | string                          |
| **Body** | **role** _optional_ | The message body is a JSON document that contains the following objects. | [Role\_model](#%5Frole%5Fmodel) |

##### [](#responses-34)Responses

| HTTP Code | Description                                                           | Schema     |
| --------- | --------------------------------------------------------------------- | ---------- |
| **201**   | 201 - OK - Create Operation successful                                | No Content |
| **401**   | 401 - Unauthorized - Error validating credentials                     | No Content |
| **409**   | 409 - Conflict - For example, an object with this name already exists | No Content |

#### [](#%5Fdb%5Frole%5Fget)Get All Roles

GET /{db}/_role

##### [](#description-35)Description

This request returns all the roles in the specified database.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Architect
* Sync Gateway Application
* Sync Gateway Application Read Only

##### [](#parameters-34)Parameters

| Type     | Name              | Description   | Schema |
| -------- | ----------------- | ------------- | ------ |
| **Path** | **db** _required_ | Database name | string |

##### [](#responses-35)Responses

| HTTP Code | Description                                                                                                                                                                                                             | Schema           |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| **200**   | 200 OK - Returns the list of roles as an array of strings The message body contains the list of roles in a JSON array. Each element of the array is a string representing the name of a role in the specified database. | < string > array |
| **401**   | 401 - Unauthorized - Error validating credentials                                                                                                                                                                       | No Content       |

#### [](#%5Fdb%5Frole%5Fname%5Fget)Get Specific Role

GET /{db}/_role/{name}

##### [](#description-36)Description

Request a specific role by name.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Architect
* Sync Gateway Application
* Sync Gateway Application Read Only

Without `Application` or `Application Read Only` users will be unable to see dynamic user or role data.

##### [](#parameters-35)Parameters

| Type     | Name                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Schema |
| -------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------ |
| **Path** | **db** _required_   | Database name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | string |
| **Path** | **name** _required_ | Role name, may contain any combination of the characters \[a-z A-Z 0-9 - + . @ %\], when creating a role any other characters must be percent encoded, see: <https://en.wikipedia.org/wiki/Percent-encoding>. When passing a role name in a URL path it must be escaped again using percent encoding for example if a role is created with the name "0\|59", the '|' character must first be percent-encoded resulting in "0%7C59". When using the same role name in a URL path it must be percent-encoded a second time resulting in "0%257C59" | string |

##### [](#responses-36)Responses

| HTTP Code | Description                                        | Schema                                                      |
| --------- | -------------------------------------------------- | ----------------------------------------------------------- |
| **200**   | The response contains information about this role. | [Response 200](#%5Fdb%5Frole%5Fname%5Fget%5Fresponse%5F200) |
| **401**   | 401 - Unauthorized - Error validating credentials  | No Content                                                  |

**Response 200**

| Name                           | Description                                                                                                                                                    | Schema           |
| ------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| **admin\_channels** _optional_ | The admin channels that this role has granted access to. Admin channels are the ones which are granted access to in the config file or via the Admin REST API. | < string > array |
| **all\_channels** _optional_   | All the channels that this role has access to.                                                                                                                 | < string > array |
| **name** _optional_            |                                                                                                                                                                | string           |

#### [](#%5Fupsert%5Frole)Update Specific Role

PUT /{db}/_role/{name}

##### [](#description-37)Description

Use this convenience endpoint to upsert a Sync Gateway role.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Architect
* Sync Gateway Application

##### [](#parameters-36)Parameters

| Type     | Name                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Schema                          |
| -------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------- |
| **Path** | **db** _required_   | Database name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | string                          |
| **Path** | **name** _required_ | Role name, may contain any combination of the characters \[a-z A-Z 0-9 - + . @ %\], when creating a role any other characters must be percent encoded, see: <https://en.wikipedia.org/wiki/Percent-encoding>. When passing a role name in a URL path it must be escaped again using percent encoding for example if a role is created with the name "0\|59", the '|' character must first be percent-encoded resulting in "0%7C59". When using the same role name in a URL path it must be percent-encoded a second time resulting in "0%257C59" | string                          |
| **Body** | **role** _optional_ | The message body is a JSON document that contains the following objects.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [Role\_model](#%5Frole%5Fmodel) |

##### [](#responses-37)Responses

| HTTP Code | Description                                       | Schema     |
| --------- | ------------------------------------------------- | ---------- |
| **200**   | 200 - OK - Operation successful                   | No Content |
| **201**   | 201 - OK - Create Operation successful            | No Content |
| **401**   | 401 - Unauthorized - Error validating credentials | No Content |

##### [](#security-6)Security

#### [](#%5Fdb%5Frole%5Fname%5Fdelete)Delete Specific Role

DELETE /{db}/_role/{name}

##### [](#description-38)Description

This request deletes the role with the specified name.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Architect
* Sync Gateway Application

##### [](#parameters-37)Parameters

| Type     | Name                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Schema |
| -------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------ |
| **Path** | **db** _required_   | Database name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | string |
| **Path** | **name** _required_ | Role name, may contain any combination of the characters \[a-z A-Z 0-9 - + . @ %\], when creating a role any other characters must be percent encoded, see: <https://en.wikipedia.org/wiki/Percent-encoding>. When passing a role name in a URL path it must be escaped again using percent encoding for example if a role is created with the name "0\|59", the '|' character must first be percent-encoded resulting in "0%7C59". When using the same role name in a URL path it must be percent-encoded a second time resulting in "0%257C59" | string |

##### [](#responses-38)Responses

| HTTP Code | Description                                | Schema     |
| --------- | ------------------------------------------ | ---------- |
| **200**   | 200 OK - The role was successfully deleted | No Content |

#### [](#%5Fdb%5Fuser%5Fpost)Create New User

POST /{db}/_user/

##### [](#description-39)Description

This request creates a new user

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Architect
* Sync Gateway Application\`

##### [](#parameters-38)Parameters

| Type     | Name                                   | Description                                                      | Schema                          |
| -------- | -------------------------------------- | ---------------------------------------------------------------- | ------------------------------- |
| **Path** | **db** _required_                      | Database name                                                    | string                          |
| **Body** | **user configuration data** _optional_ | Provision the user configuration data in JSON format in the body | [User\_model](#%5Fuser%5Fmodel) |

##### [](#responses-39)Responses

| HTTP Code | Description                                                           | Schema     |
| --------- | --------------------------------------------------------------------- | ---------- |
| **201**   | 201 - OK - Create Operation successful                                | No Content |
| **401**   | 401 - Unauthorized - Error validating credentials                     | No Content |
| **409**   | 409 - Conflict - For example, an object with this name already exists | No Content |

#### [](#%5Fdb%5Fuser%5Fget)Get All Users

GET /{db}/_user/

##### [](#description-40)Description

This request returns a list of all users

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Architect
* Sync Gateway Application
* Sync Gateway Application Read Only

##### [](#parameters-39)Parameters

| Type     | Name              | Description   | Schema |
| -------- | ----------------- | ------------- | ------ |
| **Path** | **db** _required_ | Database name | string |

##### [](#responses-40)Responses

| HTTP Code | Description                                                                                                                                                   | Schema           |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| **200**   | The message body contains the list of users in a JSON array. Each element of the array is a string representing the name of a user in the specified database. | < string > array |
| **404**   | 404 - Not Found - Object missing or misreferenced                                                                                                             | No Content       |

#### [](#%5Fdb%5Fuser%5Fname%5Fget)Get User Data

GET /{db}/_user/{name}

##### [](#description-41)Description

This request returns information about the specified user.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Architect
* Sync Gateway Application
* Sync Gateway Application Read Only

Without `Application` or `Application Read Only` users will be unable to see dynamic user or role data.

##### [](#parameters-40)Parameters

| Type     | Name                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Schema |
| -------- | ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **Path** | **db** _required_   | Database name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | string |
| **Path** | **name** _required_ | User's name, may contain contain any combination of the characters \[a-z A-Z 0-9 - + . @ %\], when creating a user any other characters must be percent encoded, see: <https://en.wikipedia.org/wiki/Percent-encoding>. When passing a user name in a URL path it must be escaped again using percent encoding for example if a user is created with the name "0\|59", the '|' character must first be percent-encoded resulting in "0%7C59". When using the same user name in a URL path it must be percent-encoded a second time resulting in "0%257C59" | string |

##### [](#responses-41)Responses

| HTTP Code | Description                                           | Schema                             |
| --------- | ----------------------------------------------------- | ---------------------------------- |
| **200**   | 200 OK - Returns information about the specified user | [User-response](#%5Fuser-response) |
| **401**   | 401 - Unauthorized - Error validating credentials     | No Content                         |

#### [](#%5Fupsert%5Fuser)Update User Data

PUT /{db}/_user/{name}

##### [](#description-42)Description

Use this method to create or update a user

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Architect
* Sync Gateway Application

##### [](#parameters-41)Parameters

| Type     | Name                                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Schema                          |
| -------- | -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| **Path** | **db** _required_                      | Database name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | string                          |
| **Path** | **name** _required_                    | User's name, may contain contain any combination of the characters \[a-z A-Z 0-9 - + . @ %\], when creating a user any other characters must be percent encoded, see: <https://en.wikipedia.org/wiki/Percent-encoding>. When passing a user name in a URL path it must be escaped again using percent encoding for example if a user is created with the name "0\|59", the '|' character must first be percent-encoded resulting in "0%7C59". When using the same user name in a URL path it must be percent-encoded a second time resulting in "0%257C59" | string                          |
| **Body** | **user configuration data** _optional_ | Provision the user configuration data in JSON format in the body                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | [User\_model](#%5Fuser%5Fmodel) |

##### [](#responses-42)Responses

| HTTP Code | Description                                       | Schema     |
| --------- | ------------------------------------------------- | ---------- |
| **200**   | 200 - OK - Operation successful                   | No Content |
| **201**   | 201 - OK - Create Operation successful            | No Content |
| **401**   | 401 - Unauthorized - Error validating credentials | No Content |

##### [](#security-7)Security

#### [](#%5Fdb%5Fuser%5Fname%5Fdelete)Delete Specific User

DELETE /{db}/_user/{name}

##### [](#description-43)Description

This request deletes the user with the specified name

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Architect
* Sync Gateway Application

##### [](#parameters-42)Parameters

| Type     | Name                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Schema |
| -------- | ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **Path** | **db** _required_   | Database name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | string |
| **Path** | **name** _required_ | User's name, may contain contain any combination of the characters \[a-z A-Z 0-9 - + . @ %\], when creating a user any other characters must be percent encoded, see: <https://en.wikipedia.org/wiki/Percent-encoding>. When passing a user name in a URL path it must be escaped again using percent encoding for example if a user is created with the name "0\|59", the '|' character must first be percent-encoded resulting in "0%7C59". When using the same user name in a URL path it must be percent-encoded a second time resulting in "0%257C59" | string |

##### [](#responses-43)Responses

| HTTP Code | Description                                       | Schema     |
| --------- | ------------------------------------------------- | ---------- |
| **200**   | 200 - OK - Operation successful                   | No Content |
| **401**   | 401 - Unauthorized - Error validating credentials | No Content |

### [](#%5Fdesign%5Fdocuments%5Fresource)Design Documents

Work with sync gateway design docs

#### [](#%5Fdb%5Fdesign%5Fddoc%5Fget)Get Views of a design document

GET /{db}/_design/{ddoc}

##### [](#description-44)Description

Query a design document.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Application
* Sync Gateway Application Read Only

##### [](#parameters-43)Parameters

| Type     | Name                | Description          | Schema |
| -------- | ------------------- | -------------------- | ------ |
| **Path** | **db** _required_   | Database name        | string |
| **Path** | **ddoc** _required_ | Design document name | string |

##### [](#responses-44)Responses

| HTTP Code | Description               | Schema                                                        |
| --------- | ------------------------- | ------------------------------------------------------------- |
| **200**   | Views for design document | [Response 200](#%5Fdb%5Fdesign%5Fddoc%5Fget%5Fresponse%5F200) |

**Response 200**

| Name                          | Schema           |
| ----------------------------- | ---------------- |
| **my\_view\_name** _optional_ | [View](#%5Fview) |

#### [](#%5Fdb%5Fdesign%5Fddoc%5Fput)Update views of a design document

PUT /{db}/_design/{ddoc}

##### [](#description-45)Description

Update views of a design document

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Application

##### [](#parameters-44)Parameters

| Type     | Name                | Description          | Schema           |
| -------- | ------------------- | -------------------- | ---------------- |
| **Path** | **db** _required_   | Database name        | string           |
| **Path** | **ddoc** _required_ | Design document name | string           |
| **Body** | **body** _optional_ | The request body     | [View](#%5Fview) |

##### [](#responses-45)Responses

| HTTP Code | Description | Schema     |
| --------- | ----------- | ---------- |
| **200**   | OK          | No Content |

#### [](#%5Fdb%5Fdesign%5Fddoc%5Fdelete)Delete design document

DELETE /{db}/_design/{ddoc}

##### [](#description-46)Description

Delete a design document.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Application

##### [](#parameters-45)Parameters

| Type     | Name                | Description          | Schema |
| -------- | ------------------- | -------------------- | ------ |
| **Path** | **db** _required_   | Database name        | string |
| **Path** | **ddoc** _required_ | Design document name | string |

##### [](#responses-46)Responses

| HTTP Code   | Description      | Schema               |
| ----------- | ---------------- | -------------------- |
| **200**     | The status       | [Design](#%5Fdesign) |
| **default** | Unexpected error | [Error](#%5Ferror)   |

#### [](#%5Fdb%5Fdesign%5Fddoc%5Fview%5Fview%5Fget)Query a view

GET /{db}/_design/{ddoc}/_view/{view}

##### [](#description-47)Description

Query a view on a design document.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Application
* Sync Gateway Application Read Only

##### [](#parameters-46)Parameters

| Type      | Name                             | Description                                                                                                                                                               | Schema  |
| --------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **Path**  | **db** _required_                | Database name                                                                                                                                                             | string  |
| **Path**  | **ddoc** _required_              | Design document name                                                                                                                                                      | string  |
| **Path**  | **view** _required_              | View name                                                                                                                                                                 | string  |
| **Query** | **conflicts** _optional_         | Include conflict information in the response. This parameter is ignored if the include\_docs parameter is false.                                                          | boolean |
| **Query** | **descending** _optional_        | Return documents in descending order.                                                                                                                                     | boolean |
| **Query** | **end\_key** _optional_          | Alias for the endkey parameter.                                                                                                                                           | string  |
| **Query** | **end\_key\_doc\_id** _optional_ | Alias for the endkey\_docid parameter.                                                                                                                                    | string  |
| **Query** | **endkey** _optional_            | If this parameter is provided, stop returning records when the specified key is reached.                                                                                  | string  |
| **Query** | **endkey\_docid** _optional_     | If this parameter is provided, stop returning records when the specified document identifier is reached.                                                                  | string  |
| **Query** | **group** _optional_             | Group the results using the reduce function to a group or single row.                                                                                                     | boolean |
| **Query** | **group\_level** _optional_      | Specify the group level to be used.                                                                                                                                       | integer |
| **Query** | **include\_docs** _optional_     | Only works when using Couchbase Server 3.0 and earlier. Indicates whether to include the full content of the documents in the response.                                   | boolean |
| **Query** | **inclusive\_end** _optional_    | Indicates whether the specified end key should be included in the result.                                                                                                 | boolean |
| **Query** | **key** _optional_               | If this parameter is provided, return only document that match the specified key.                                                                                         | string  |
| **Query** | **limit** _optional_             | If this parameter is provided, return only the specified number of documents.                                                                                             | integer |
| **Query** | **skip** _optional_              | If this parameter is provided, skip the specified number of documents before starting to return results.                                                                  | integer |
| **Query** | **stale** _optional_             | Allow the results from a stale view to be used, without triggering a rebuild of all views within the encompassing design document. Valid values are ok and update\_after. | string  |
| **Query** | **start\_key** _optional_        | Alias for startkey param.                                                                                                                                                 | string  |
| **Query** | **startkey** _optional_          | If this parameter is provided, return documents starting with the specified key.                                                                                          | string  |
| **Query** | **startkey\_docid** _optional_   | If this parameter is provided, return documents starting with the specified document identifier.                                                                          | string  |
| **Query** | **update\_seq** _optional_       | Indicates whether to include the update\_seq property in the response.                                                                                                    | boolean |

##### [](#responses-47)Responses

| HTTP Code | Description   | Schema                         |
| --------- | ------------- | ------------------------------ |
| **200**   | Query results | [QueryResult](#%5Fqueryresult) |

### [](#%5Fdocument%5Fresource)Document

Manage documents and attachments

#### [](#%5Fcreate%5Fdatabase%5Fdocument)Create Document

POST /{db}/

##### [](#description-48)Description

This request creates a new document in the specified database.

You can either specify the document ID by including the \_id in the request message body (the value must be a string), or let the software generate an ID.

The maximum size allowed for a document is 20MB.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Application

##### [](#parameters-47)Parameters

| Type     | Name                | Description       | Schema |
| -------- | ------------------- | ----------------- | ------ |
| **Path** | **db** _required_   | Database name     | string |
| **Body** | **body** _optional_ | The document body | object |

##### [](#responses-48)Responses

| HTTP Code | Description                      | Schema                   |
| --------- | -------------------------------- | ------------------------ |
| **201**   | Operation completed successfully | [doc-resp](#%5Fdoc-resp) |

#### [](#%5Fdb%5Flocal%5Flocal%5Fdoc%5Fget)Get Specific Local Document

GET /{db}/_local/{local_doc}

##### [](#description-49)Description

This request retrieves a local document.

Local document IDs begin with \_local/. Local documents are not replicated or indexed, don't support attachments, and don't save revision histories. In practice they are almost only used by Couchbase Lite's replicator, as a place to store replication checkpoint data.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Application
* Sync Gateway Application Read Only

##### [](#parameters-48)Parameters

| Type     | Name                      | Description                             | Schema |
| -------- | ------------------------- | --------------------------------------- | ------ |
| **Path** | **db** _required_         | Database name                           | string |
| **Path** | **local\_doc** _required_ | Local document IDs begin with \_local/. | string |

##### [](#responses-49)Responses

| HTTP Code | Description | Schema     |
| --------- | ----------- | ---------- |
| **200**   | OK          | No Content |

#### [](#%5Fdb%5Flocal%5Flocal%5Fdoc%5Fput)Update Specific Local Document

PUT /{db}/_local/{local_doc}

##### [](#description-50)Description

This request creates or updates a local document. Local document IDs begin with \_local/. Local documents are not replicated or indexed, don't support attachments, and don't save revision histories. In practice they are almost only used by the client's replicator, as a place to store replication checkpoint data.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Application

##### [](#parameters-49)Parameters

| Type     | Name                      | Description                             | Schema |
| -------- | ------------------------- | --------------------------------------- | ------ |
| **Path** | **db** _required_         | Database name                           | string |
| **Path** | **local\_doc** _required_ | Local document IDs begin with \_local/. | string |

##### [](#responses-50)Responses

| HTTP Code | Description                      | Schema                   |
| --------- | -------------------------------- | ------------------------ |
| **201**   | Operation completed successfully | [doc-resp](#%5Fdoc-resp) |

#### [](#%5Fdb%5Flocal%5Flocal%5Fdoc%5Fdelete)Delete Specific Local Document

DELETE /{db}/_local/{local_doc}

##### [](#description-51)Description

This request deletes a local document. Local document IDs begin with \_local/. Local documents are not replicated or indexed, don't support attachments, and don't save revision histories. In practice they are almost only used by Couchbase Lite's replicator, as a place to store replication checkpoint data.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Application

##### [](#parameters-50)Parameters

| Type      | Name                      | Description                                                                                                     | Schema |
| --------- | ------------------------- | --------------------------------------------------------------------------------------------------------------- | ------ |
| **Path**  | **db** _required_         | Database name                                                                                                   | string |
| **Path**  | **local\_doc** _required_ | Local document IDs begin with \_local/.                                                                         | string |
| **Query** | **batch** _optional_      | Stores the document in batch mode. To use, set the value to ok.                                                 | string |
| **Query** | **rev** _optional_        | Revision identifier of the parent revision the new one should replace. (Not used when creating a new document.) | string |

##### [](#responses-51)Responses

| HTTP Code | Description                      | Schema                   |
| --------- | -------------------------------- | ------------------------ |
| **200**   | Operation completed successfully | [doc-resp](#%5Fdoc-resp) |

#### [](#%5Fdb%5Fpurge%5Fpost)Purge document

POST /{db}/_purge

##### [](#description-52)Description

The purge command provides a way to remove a document from the bucket itself. The operation removes all the revisions (active and tombstones) for the specified document(s). A common usage of this endpoint is to remove tombstone documents that are no longer needed, thus recovering storage space and reducing data replicated to clients. Other clients are not notified when a revision has been purged; so in order to purge a revision from the system it must be done from all databases (on Couchbase Lite and Sync Gateway).

When **convergence** is enabled (introduced in Sync Gateway 1.5), this endpoint removes the document and its associated extended attributes.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Application

##### [](#parameters-51)Parameters

| Type     | Name                | Description                                                              | Schema                     |
| -------- | ------------------- | ------------------------------------------------------------------------ | -------------------------- |
| **Path** | **db** _required_   | Database name                                                            | string                     |
| **Body** | **body** _optional_ | The message body is a JSON document that contains the following objects. | [PurgeBody](#%5Fpurgebody) |

##### [](#responses-52)Responses

| HTTP Code | Description                             | Schema           |
| --------- | --------------------------------------- | ---------------- |
| **200**   | OK - The purge operation was successful | < string > array |

#### [](#%5Fdb%5Fraw%5Fdoc%5Fget)Document with metadata

GET /{db}/_raw/{doc}

##### [](#description-53)Description

Returns the document with the metadata.

Note: The direct use of this endpoint is unsupported. The sync metadata is maintained internally by Sync Gateway and its structure can change. It should not be used to drive business logic of applications since the response to the `/{db}/_raw/{id}` endpoint can change at any time.\\

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Application
* Sync Gateway Application Read Only

##### [](#parameters-52)Parameters

| Type     | Name               | Description   | Schema |
| -------- | ------------------ | ------------- | ------ |
| **Path** | **db** _required_  | Database name | string |
| **Path** | **doc** _required_ | Document ID   | string |

##### [](#responses-53)Responses

| HTTP Code | Description | Schema                         |
| --------- | ----------- | ------------------------------ |
| **200**   | OK          | [DocMetadata](#%5Fdocmetadata) |

#### [](#%5Fdb%5Frevtree%5Fdoc%5Fget)Revision Tree structure in Graphviz Dot format | not officially supported

GET /{db}/_revtree/{doc}

##### [](#description-54)Description

Returns the dot syntax of the revision tree which can be rendered into a PNG image with the [CLI dot tool](http://www.graphviz.org/).

* Install the dot tool via `brew install graphviz`.
* Save the response text to a file (for example, **revtree.dot**).
* Render a PNG by calling `dot -Tpng revtree.dot > revtree.png`.

**Note:** This endpoint is useful for debugging purposes only. It is not officially supported.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Application
* Sync Gateway Application Read Only

##### [](#parameters-53)Parameters

| Type     | Name               | Description   | Schema |
| -------- | ------------------ | ------------- | ------ |
| **Path** | **db** _required_  | Database name | string |
| **Path** | **doc** _required_ | Document ID   | string |

##### [](#responses-54)Responses

| HTTP Code | Description                                    | Schema     |
| --------- | ---------------------------------------------- | ---------- |
| **200**   | Success and returns the revtree as plain text. | No Content |

##### [](#produces-2)Produces

* `text/plain`

#### [](#%5Fdb%5Fdoc%5Fget)Get Specific Document

GET /{db}/{doc}

##### [](#description-55)Description

This request retrieves a document from a database. _Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_\- Sync Gateway Application - Sync Gateway Application Read Only

##### [](#parameters-54)Parameters

| Type      | Name                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                              | Schema           | Default |
| --------- | -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------- |
| **Path**  | **db** _required_          | Database name                                                                                                                                                                                                                                                                                                                                                                                                                            | string           |         |
| **Path**  | **doc** _required_         | Document ID                                                                                                                                                                                                                                                                                                                                                                                                                              | string           |         |
| **Query** | **attachments** _optional_ | Include attachment bodies in response. Default is false.                                                                                                                                                                                                                                                                                                                                                                                 | boolean          | "false" |
| **Query** | **atts\_since** _optional_ | Include attachments only since specified revisions. Does not include attachments for specified revisions.                                                                                                                                                                                                                                                                                                                                | < string > array |         |
| **Query** | **open\_revs** _optional_  | Option to fetch specified revisions of the document. The value can be all to fetch all leaf revisions or an array of revision numbers (i.e. open\_revs=\["rev1", "rev2"\]). Only [leaf revision](glossary.html) bodies that haven't been pruned are guaranteed to be returned. If this option is specified the response will be in multipart format. Use the Accept: application/json request header to get the result as a JSON object. | string           |         |
| **Query** | **rev** _optional_         | Revision identifier of the revision to get. By default, Sync Gateway returns the current revision. This parameter is generally only needed for conflict resolution. For example where the app might need to retrieve a conflicting leaf revision that isn't the current revision.                                                                                                                                                        | string           |         |
| **Query** | **revs** _optional_        | Default is false. Indicates whether to include a \_revisions property for each document in the response, which contains a revision history of the document. The length of the returned revision tree can be specified with the revs\_limit querystring parameter.                                                                                                                                                                        | boolean          | "false" |
| **Query** | **show\_exp** _optional_   | Whether to show the \_exp property in the response.                                                                                                                                                                                                                                                                                                                                                                                      | boolean          | "false" |

##### [](#responses-55)Responses

| HTTP Code | Description                                                         | Schema |
| --------- | ------------------------------------------------------------------- | ------ |
| **200**   | The message body contains the following objects in a JSON document. | object |

#### [](#%5Fdb%5Fdoc%5Fput)Create or update document

PUT /{db}/{doc}

##### [](#description-56)Description

This request creates a new document or creates a new revision of an existing document. It enables you to specify the identifier for a new document rather than letting the software create an identifier. If you want to create a new document and let the software create an identifier, use the POST /db request. If the document specified by doc does not exist, a new document is created and assigned the identifier specified in doc. If the document already exists, the document is updated with the JSON document in the message body and given a new revision. The maximum size allowed for a document is 20MB.

Since Sync Gateway 1.3, an expiry property (`_exp`) can also be specified to purge the document after a given time. If **convergence** is enabled (introduced in Sync Gateway 1.5), the behavior of the expiry feature changes in the following way: when the expiry value is reached, instead of getting purged, the **active** revision of the document is tombstoned. If there is another non-tombstoned revision for this document (i.e a conflict) it will become the active revision. The tombstoned revision will be purged when the server's metadata purge interval is reached.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Application

##### [](#parameters-55)Parameters

| Type      | Name                      | Description                                                                                                                                                                                                                                                                                                                                             | Schema                                  | Default |
| --------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- | ------- |
| **Path**  | **db** _required_         | Database name                                                                                                                                                                                                                                                                                                                                           | string                                  |         |
| **Path**  | **doc** _required_        | Document ID                                                                                                                                                                                                                                                                                                                                             | string                                  |         |
| **Query** | **new\_edits** _optional_ | Default is true. Setting this to false indicates that the request body is an already-existing revision that should be directly inserted into the database, instead of a modification to apply to the current document. (This mode is used by the replicato.) This option must be used in conjunction with the \_revisions property in the request body. | boolean                                 | "true"  |
| **Query** | **rev** _required_        | Revision identifier of the revision to update. It must be the last revision in the history.                                                                                                                                                                                                                                                             | string                                  |         |
| **Body**  | **Document** _optional_   | Request body                                                                                                                                                                                                                                                                                                                                            | [Document\_model](#%5Fdocument%5Fmodel) |         |

##### [](#responses-56)Responses

| HTTP Code | Description                      | Schema                   |
| --------- | -------------------------------- | ------------------------ |
| **200**   | Operation completed successfully | [doc-resp](#%5Fdoc-resp) |

#### [](#%5Fdb%5Fdoc%5Fdelete)Delete document

DELETE /{db}/{doc}

##### [](#description-57)Description

This request deletes a document from the database. When a document is deleted, the revision number is updated so the database can track the deletion in synchronized copies.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Application

##### [](#parameters-56)Parameters

| Type      | Name               | Description                                                                                                     | Schema |
| --------- | ------------------ | --------------------------------------------------------------------------------------------------------------- | ------ |
| **Path**  | **db** _required_  | Database name                                                                                                   | string |
| **Path**  | **doc** _required_ | Document ID                                                                                                     | string |
| **Query** | **rev** _required_ | Revision identifier of the revision to delete. It must be the identifier of the latest revision in the history. | string |

##### [](#responses-57)Responses

| HTTP Code | Description | Schema     |
| --------- | ----------- | ---------- |
| **200**   | OK          | No Content |

#### [](#%5Fdb%5Fdoc%5Fattachment%5Fget)Get attachment

GET /{db}/{doc}/{attachment}

##### [](#description-58)Description

Use this request to get the file attachment associated with a document. It returns the raw data of the associated attachment, just as if you were accessing a static file.

The Content-Type response header is the same content type set when the document attachment was added to the database.

To remove an attachment from a document, simply update the `_attachments` dictionary of the document in the PUT "/{db}/{id}" request.

Use the `meta` parameter to request that only the document ID of the attachment blob be returned

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Application
* Sync Gateway Application Read Only

##### [](#parameters-57)Parameters

| Type      | Name                      | Description                                                                                                                                                                                                                    | Schema  | Default |
| --------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- | ------- |
| **Path**  | **attachment** _required_ | Attachment name. This value must be URL encoded. For example, if the attachment name is blob\_/avatar, the path component passed to the URL should be blob\_%2Favatar (tested with [URLEncoder](https://www.urlencoder.org/)). | string  |         |
| **Path**  | **db** _required_         | Database name                                                                                                                                                                                                                  | string  |         |
| **Path**  | **doc** _required_        | Document ID                                                                                                                                                                                                                    | string  |         |
| **Query** | **meta** _optional_       | If true only the document ID of the attachment blob is returned in the response body                                                                                                                                           | boolean | "false" |
| **Query** | **rev** _optional_        | Revision identifier of the parent revision the new one should replace. (Not used when creating a new document.)                                                                                                                | string  |         |

##### [](#responses-58)Responses

| HTTP Code | Description                                                                                   | Schema          |
| --------- | --------------------------------------------------------------------------------------------- | --------------- |
| **200**   | The message body contains the attachment, in the format specified in the Content-Type header. | string (binary) |
| **304**   | Not Modified, the attachment wasn't modified if ETag equals the If-None-Match header          | No Content      |
| **400**   | Bad Request - A non boolean value was supplied for the meta parameter.                        | No Content      |
| **404**   | Not Found, the specified database, document or attachment was not found.                      | No Content      |

##### [](#example-http-response-11)Example HTTP response

###### [](#response-200-11)Response 200

```json
"GET /{db}/{doc}/{attachment}?meta=true\n{\n  \"content_type\": \"text/plain\",\n  \"length\": 2,\n  \"key\": \"_sync:att2:uU0nuZNNPgilLlLX2n2r+sSE7+N6U4DukIj3rOLvzek=:sha1-Kq5sNclPz7QV2+lfQIuc6R7oRu0=\"\n}\n\n"
```

#### [](#%5Fdb%5Fdoc%5Fattachment%5Fput)Add or update a document attachment

PUT /{db}/{doc}/{attachment}

##### [](#description-59)Description

Use this request to add or update the supplied request content as an attachment to the specified document.

* The maximum content size of an attachment is 20MB.
* The attachment name must be a URL-encoded string (the file name).
* You must also supply either the rev query parameter or the If-Match HTTP header for validation, and the Content-Type headers (to set the attachment content type).

When uploading an attachment using an existing attachment name, the corresponding stored content of the database will be updated. Because you must supply the revision information to add an attachment to the document, this serves as validation to update the existing attachment.

Uploading an attachment updates the corresponding document revision. Revisions are tracked for the parent document, not individual attachments.

To remove an attachment from a document, simply update the `_attachments` dictionary of the document in the PUT "{db}/{id}" request.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Application

##### [](#parameters-58)Parameters

| Type       | Name                        | Description                                                                                                                                                                                                                    | Schema          |
| ---------- | --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------- |
| **Header** | **Content-Type** _optional_ | Attachment Content-Type                                                                                                                                                                                                        | string          |
| **Path**   | **attachment** _required_   | Attachment name. This value must be URL encoded. For example, if the attachment name is blob\_/avatar, the path component passed to the URL should be blob\_%2Favatar (tested with [URLEncoder](https://www.urlencoder.org/)). | string          |
| **Path**   | **db** _required_           | Database name                                                                                                                                                                                                                  | string          |
| **Path**   | **doc** _required_          | Document ID                                                                                                                                                                                                                    | string          |
| **Query**  | **rev** _optional_          | Revision identifier of the parent revision the new one should replace. (Not used when creating a new document.)                                                                                                                | string          |
| **Body**   | **body** _optional_         | The request body                                                                                                                                                                                                               | string (binary) |

##### [](#responses-59)Responses

| HTTP Code | Description                                                              | Schema     |
| --------- | ------------------------------------------------------------------------ | ---------- |
| **200**   | Operation completed successfully                                         | No Content |
| **409**   | Conflict, the document revision wasn't specified or it's not the latest. | No Content |

### [](#%5Flogging%5Fresource)Logging

Update bootstrap logging settings

#### [](#%5Fput%5Flogging%5Foptions)Update Logging Options

PUT /_config

##### [](#description-60)Description

Update bootstrap logging options without needing a restart

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Dev Ops

##### [](#parameters-59)Parameters

| Type     | Name                                     | Schema                                |
| -------- | ---------------------------------------- | ------------------------------------- |
| **Body** | **bootstrap logging setting** _required_ | [Logging\_model](#%5Flogging%5Fmodel) |

##### [](#responses-60)Responses

| HTTP Code | Description                                 | Schema                                |
| --------- | ------------------------------------------- | ------------------------------------- |
| **200**   | Returned updated Bootstrap logging settings | [Logging\_model](#%5Flogging%5Fmodel) |

### [](#%5Freplication%5Fresource)Replication

Manage inter-Sync Gateway replication

#### [](#%5Fdb%5Freplication%5Fpost)Create a new replication definition

POST /{db}/_replication

##### [](#description-61)Description

The _replication endpoint is used to manage both \_ad hoc_ and _persistent_ replication operations. 

Using a POST request you can insert a new set of replication details.

**To Cancel a Replication**You can cancel continuous replications by adding the cancel field to the JSON request object and setting the value to true. Note that the structure of the request must be identical to the original for the cancellation request to be honoured. For example, if you requested continuous replication, the cancellation request must also contain the continuous field.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Replicator

##### [](#parameters-60)Parameters

| Type     | Name                           | Description                                                                                                                                                                                                                                                                                                 | Schema                                        |
| -------- | ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **Path** | **db** _required_              | Database name                                                                                                                                                                                                                                                                                               | string                                        |
| **Body** | **ReplicationBody** _optional_ | This replication request message body is a JSON document that comprises all the properties required to upsert a replication. If the replicationID matches an existing replication\_id then the values of any properties provided in the body are used to update the existing replication's property values. | [Replication\_model](#%5Freplication%5Fmodel) |

##### [](#responses-61)Responses

| HTTP Code | Description                       | Schema                                         |
| --------- | --------------------------------- | ---------------------------------------------- |
| **200**   | Replication successfully updated  | [ReplicationResponse](#%5Freplicationresponse) |
| **201**   | Replication successfully inserted | [ReplicationResponse](#%5Freplicationresponse) |

#### [](#%5Fdb%5Freplication%5Fget)Get all replication definitions

GET /{db}/_replication

##### [](#description-62)Description

Returns an array object containing all replication definitions

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Replicator

##### [](#parameters-61)Parameters

| Type     | Name              | Description   | Schema |
| -------- | ----------------- | ------------- | ------ |
| **Path** | **db** _required_ | Database name | string |

##### [](#responses-62)Responses

| HTTP Code | Description                                                                           | Schema                                                 |
| --------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------ |
| **200**   | Successful response - returns an array of replication definitions in the body as JSON | [ReplicationResponseBody](#%5Freplicationresponsebody) |

#### [](#%5Fdb%5Freplication%5Freplicationid%5Fget)Get a replication definition

GET /{db}/_replication/{replicationID}

##### [](#description-63)Description

Returns requested (**replicationID**) replication definition

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Replicator

##### [](#parameters-62)Parameters

| Type     | Name                         | Description                                                      | Schema |
| -------- | ---------------------------- | ---------------------------------------------------------------- | ------ |
| **Path** | **db** _required_            | Database name                                                    | string |
| **Path** | **replicationID** _required_ | The {replicationID} parameter identifies the target replication. | string |

##### [](#responses-63)Responses

| HTTP Code | Description                                                                        | Schema                                                 |
| --------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------ |
| **200**   | Successful response - returns requested replication definition in the body as JSON | [ReplicationResponseBody](#%5Freplicationresponsebody) |

#### [](#%5Fupsert%5Freplication)Upsert a replication definition

PUT /{db}/_replication/{replicationID}

##### [](#description-64)Description

The _replication endpoint is used to manage both \_ad hoc_ and _persistent_ replication operations. 

Using a PUT request you can update (or insert, if it doesn't exist) a set of replication details.

**To cancel a replication**You can cancel continuous replications by adding the cancel field to the JSON request object and setting the value to true.

Note that the structure of the request must be identical to the original for the cancellation request to be honoured.

For example, if you requested continuous replication, the cancellation request must also contain the continuous field.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Replicator

##### [](#parameters-63)Parameters

| Type     | Name                           | Description                                                                                                                                                                                                                                                                                                 | Schema                                        |
| -------- | ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **Path** | **db** _required_              | Database name                                                                                                                                                                                                                                                                                               | string                                        |
| **Path** | **replicationID** _required_   | If supplied, the <i>replicationID</i> parameter must be a valid replication id. If it is not supplied for a <i>new</i> replication\*, then a random UUID is generated.                                                                                                                                      | string                                        |
| **Body** | **ReplicationBody** _optional_ | This replication request message body is a JSON document that comprises all the properties required to upsert a replication. If the replicationID matches an existing replication\_id then the values of any properties provided in the body are used to update the existing replication's property values. | [Replication\_model](#%5Freplication%5Fmodel) |

##### [](#responses-64)Responses

| HTTP Code | Description                       | Schema                                         |
| --------- | --------------------------------- | ---------------------------------------------- |
| **200**   | Replication successfully updated  | [ReplicationResponse](#%5Freplicationresponse) |
| **201**   | Replication successfully inserted | [ReplicationResponse](#%5Freplicationresponse) |

##### [](#security-8)Security

#### [](#%5Fdb%5Freplication%5Freplicationid%5Fdelete)Cancel and delete replication

DELETE /{db}/_replication/{replicationID}

##### [](#description-65)Description

Deletes a specific (**replicationID**) replication - Removes persisted replication definition - Removes all checkpoints associated with the replication - Deletes all replication status information associated with the replication

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Replicator

##### [](#parameters-64)Parameters

| Type     | Name                         | Description                                                      | Schema |
| -------- | ---------------------------- | ---------------------------------------------------------------- | ------ |
| **Path** | **db** _required_            | Database name                                                    | string |
| **Path** | **replicationID** _required_ | The {replicationID} parameter identifies the target replication. | string |

##### [](#responses-65)Responses

| HTTP Code | Description                      | Schema     |
| --------- | -------------------------------- | ---------- |
| **200**   | Replication successfully deleted | No Content |

#### [](#%5Fdb%5Freplicationstatus%5Fget)Returns replication status data for replications matching the criteria

GET /{db}/_replicationStatus

##### [](#description-66)Description

**About**

Returns replication status data for all replications matching the criteria specified in the {querystring} parameter.

**Options**

The `{queryString}` parameter supports the following filter parameters - see _Parameter_ section for more details

* `activeOnly`
* `localOnly`
* `includeConfig`
* `includeError`

**Behavior**

The selection is made from all replications across _all_ nodes.

By default the response includes status data for replications in any state (starting, running, stopped or error) from across all nodes.

<h5>Example</h5>

```none
 http://localhost:4985/{db}/_replicationStatus?activeOnly=false&localOnly=false&includeError=true
```

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Replicator

##### [](#parameters-65)Parameters

| Type      | Name                         | Description                                                                                                                                                                             | Schema  | Default |
| --------- | ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------- |
| **Path**  | **db** _required_            | Database name                                                                                                                                                                           | string  |         |
| **Query** | **activeOnly** _optional_    | When _true_, only active replications (state=starting, running, stopping) are returned                                                                                                  | boolean | "false" |
| **Query** | **includeConfig** _optional_ | When _true_ the replication definition is included in the response.                                                                                                                     | boolean | "false" |
| **Query** | **includeError** _optional_  | When false, omits replications stopped due to error (state=error) By default the response includes replications in error state.                                                         | boolean | "true"  |
| **Query** | **localOnly** _optional_     | When _true_ returns only replications run (or running) the local node since startup. By default the response includes replications run or running across all nodes since node start-up. | boolean | "false" |

##### [](#responses-66)Responses

| HTTP Code | Description                                       | Schema                                                             |
| --------- | ------------------------------------------------- | ------------------------------------------------------------------ |
| **200**   | Returns information about the active replications | [ReplicationStatusResponseBody](#%5Freplicationstatusresponsebody) |

#### [](#%5Fdb%5Freplicationstatus%5Freplicationid%5Fget)Returns information on specified replication

GET /{db}/_replicationStatus/{replicationID}

##### [](#description-67)Description

Returns the status of the requested (**replicationID**) replication

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Replicator

##### [](#parameters-66)Parameters

| Type     | Name                         | Description                                                      | Schema |
| -------- | ---------------------------- | ---------------------------------------------------------------- | ------ |
| **Path** | **db** _required_            | Database name                                                    | string |
| **Path** | **replicationID** _required_ | The {replicationID} parameter identifies the target replication. | string |

##### [](#responses-67)Responses

| HTTP Code | Description                              | Schema                                                             |
| --------- | ---------------------------------------- | ------------------------------------------------------------------ |
| **200**   | Information about specified replication. | [ReplicationStatusResponseBody](#%5Freplicationstatusresponsebody) |

#### [](#%5Fdb%5Freplicationstatus%5Freplicationid%5Fput)Modify replication status

PUT /{db}/_replicationStatus/{replicationID}

##### [](#description-68)Description

Use this endpoint to change the status of the specified (**replicationID**) replication using the value of the `action` parameter.

The `action` parameter specifies the status to be set - valid values are

* `start` \- starts a stopped replication
* `stop` \- stops an active replication
* `reset` \- resets a stopped replication (resets checkpoint to zero). For bidirectional replication, both push and pull checkpoints are reset to zero.

For example

\` <http://localhost:4985/fred/%5FreplicationStatus/{replicationID}?action=start>\`

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Replicator

##### [](#parameters-67)Parameters

| Type      | Name                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                  | Schema | Default |
| --------- | ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ | ------- |
| **Path**  | **db** _required_            | Database name                                                                                                                                                                                                                                                                                                                                                                                                                                | string |         |
| **Path**  | **replicationID** _required_ | The {replicationID} parameter identifies the target replication.                                                                                                                                                                                                                                                                                                                                                                             | string |         |
| **Query** | **action** _required_        | The value of the {action} parameter specifies the value you want the selected replication's status set to. Valid values are: \* **start** : Use this action to start a stopped replication \* **stop** : Use this action to stop a started replication \* **reset** : Use this action to reset a stopped replication. This will set the checkpoint to zero. For bidirectional replication, both push and pull checkpoints are reset to zero. | string | "none"  |

##### [](#responses-68)Responses

| HTTP Code | Description                             | Schema                                                             |
| --------- | --------------------------------------- | ------------------------------------------------------------------ |
| **200**   | The required status is successfully set | [ReplicationStatusResponseBody](#%5Freplicationstatusresponsebody) |

### [](#%5Fserver%5Fresource)Server

Manage server activities

#### [](#%5Fget%5Fserver%5Fmetadata)Get Server Metadata

GET /

##### [](#description-69)Description

Returns meta-information about the server.

##### [](#responses-69)Responses

| HTTP Code | Description                        | Schema               |
| --------- | ---------------------------------- | -------------------- |
| **200**   | Meta-information about the server. | [Server](#%5Fserver) |

#### [](#%5Factive%5Ftasks%5Fget)Get List of Active Tasks (v1 replications only)

GET /_active_tasks

> [!CAUTION]
> operation.deprecated

##### [](#description-70)Description

_Deprecated @ 2.8_

Replaced by Inter-Sync Gateway Replication (v2)'s _\[\_replicationStatus\](#/server/get\_\_replicationStatus)_ endpoint. This **\_active\_tasks** endpoint is retained **only** for backward compatibility.

Use this end point to return the status of active Inter-Sync Gateway Replication (v1) replications. Only replications configured on the local node are returned.

The response is as defined in \[\_replicationStatus\](#/replications/get_db_\_replicationStatus) except that it also includes:

* **end\_last\_seq**, which returns the maximum of (last\_seq\_pull, last\_seq\_push)
* **start\_last\_seq**, which is not populated (as was the case prior to Sync Gateway 2.8)

The Inter-Sync Gateway Replication (v2) equivalent is `_replicationStatus?localOnly=true&activeOnly=true` \- see \[\_replicationStatus\](#/replications/get_db_\_replicationStatus).

##### [](#responses-70)Responses

| HTTP Code | Description                            | Schema                                        |
| --------- | -------------------------------------- | --------------------------------------------- |
| **200**   | Information about active replications. | [ActiveTasks\_model](#%5Factivetasks%5Fmodel) |

#### [](#%5Fall%5Fdbs%5Fget)Get List of All Databases

GET /_all_dbs

##### [](#description-71)Description

List all databases

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Dev Ops

##### [](#responses-71)Responses

| HTTP Code | Description                      | Schema                                      |
| --------- | -------------------------------- | ------------------------------------------- |
| **200**   | Identify all available databases | < [AllDatabases](#%5Falldatabases) \> array |

#### [](#%5Fget%5Fserver%5Fconfiguration)Get Server Configuration

GET /_config

##### [](#description-72)Description

Returns the Sync Gateway configuration of the running instance. This is a good method to check if a particular key was set correctly on the config file.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Dev Ops

##### [](#responses-72)Responses

| HTTP Code | Description                                         | Schema                                    |
| --------- | --------------------------------------------------- | ----------------------------------------- |
| **200**   | Sync Gateway configuration of the running instance. | [Bootstrap\_model](#%5Fbootstrap%5Fmodel) |

#### [](#%5Fput%5Flogging%5Foptions)Update Logging Options

PUT /_config

##### [](#description-73)Description

Update bootstrap logging options without needing a restart

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Dev Ops

##### [](#parameters-68)Parameters

| Type     | Name                                     | Schema                                |
| -------- | ---------------------------------------- | ------------------------------------- |
| **Body** | **bootstrap logging setting** _required_ | [Logging\_model](#%5Flogging%5Fmodel) |

##### [](#responses-73)Responses

| HTTP Code | Description                                 | Schema                                |
| --------- | ------------------------------------------- | ------------------------------------- |
| **200**   | Returned updated Bootstrap logging settings | [Logging\_model](#%5Flogging%5Fmodel) |

#### [](#%5Fget%5Fsync%5Fgateway%5Fstatistics)Get Sync Gateway Statistics

GET /_expvar

##### [](#description-74)Description

The \`Expvar\`method returns a number of runtime variables that you can view for debugging or performance monitoring purposes.

This method can also be accessed using Sync Gateway's [Metrics REST API](rest-api-metrics.html)

**See** : [Sync Gateway Statistics Schema](stats-monitoring.html) for more details on the metrics collected and reported by Sync Gateway.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Dev Ops
* External stats reader

##### [](#responses-74)Responses

| HTTP Code | Description            | Schema                 |
| --------- | ---------------------- | ---------------------- |
| **200**   | OK - indicates success | [ExpVars](#%5Fexpvars) |

#### [](#%5Flogging%5Ftags%5Fpost)Set Logging Tags

POST /_logging

##### [](#description-75)Description

Enabling logging for a tag provides additional diagnostic information for that logging area.

The POST request only updates the tags specified in the request body.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Dev Ops

##### [](#parameters-69)Parameters

| Type      | Name                     | Description                                                                                                                                                                                                                   | Schema                                              |
| --------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| **Query** | **level** _optional_     | **Deprecated** \- please use logLevel instead This setting determines the verbosity of the logging - level=1 - The default, regular, logging - level=2 - Enables warnings and panics logging - level=3 - Will log panics only | integer                                             |
| **Query** | **logLevel** _optional_  | This setting determines the verbosity of the logging. Available values are - none\- error\- warn\- info\- debug\- trace Note that the setting is additive. For example, setting info will also enable both error and warn.    | string                                              |
| **Body**  | **log\_keys** _optional_ | Use the body to provide a list of the log keys you want to set. For example - {"Changes++":true, "Cache":true, "HTTP":true, "DCP":true, "WS": true, "WSFrame": true, "Replicate": true}                                       | [log\_keys](#%5Flogging%5Ftags%5Fpost%5Flog%5Fkeys) |

**log\_keys**

Name

Description

Schema

**Access**  
_optional_

Anytime an access() call is made in the sync function.

boolean

**Admin**  
_optional_

Admin processes in Sync Gateway.

boolean

**All**  
_optional_

Use the wildcard character  to set all log keys For example `{"":true}` 

boolean

**Auth**  
_optional_

Authentication.

boolean

**Bucket**  
_optional_

Sync Gateway interactions with the bucket (trace level only).

boolean

**CRUD**  
_optional_

Updates made by Sync Gateway to documents.

boolean

**Cache**  
_optional_

Interactions with Sync Gateway's in-memory channel cache.

boolean

**Changes**  
_optional_

Processing of /{db}/\_changes requests.

boolean

**DCP**  
_optional_

DCP-feed processing.

boolean

**Events**  
_optional_

Event processing (webhooks).

boolean

**HTTP**  
_optional_

All requests made to the Sync Gateway REST APIs.

boolean

**HTTP+**  
_optional_

Additional information about HTTP requests (response times, status codes).

boolean

**Import**  
_optional_

Introduced in Sync Gateway 1.5 to help troubleshoot the import process of a document (this is the Sync Gateway process to make a document that was added through N1QL or the Server SDKs mobile-aware). This log key can be useful to troubleshoot why a given document was not successfully imported.

boolean

**Javascript**  
_optional_

All logging from Javascript. This includes - sync function, import filters, webhook filter function, and the custom ISGR conflict resolvers

boolean

**Migrate**  
_optional_

Logs messages thhat show when old inline document metdata is upgraded to xattrs

boolean

**Query**  
_optional_

Query is used for Sync Gateway code related to N1QL queries

boolean

**Replicate**  
_optional_

Log messages related to replications between Sync Gateways (using sg-replicate). This tag cannot be used for replications initiated by Couchbase Lite.

boolean

**SGCluster**  
_optional_

Log messages related to the sharded import and HA sg-replicate

boolean

**Sync**  
_optional_

Activity which relates to synchronization between Couchbase Lite and Sync Gateway

boolean

**SyncMsg**  
_optional_

Can be used for additional Sync logging output

boolean

**WS**  
_optional_

Websocket replication log messages

boolean

**WSFrame**  
_optional_

Can be used for additional WS logging output

boolean

**gocb**  
_optional_

All logging emitted by the GoCB SDK

boolean

**none**  
_optional_

Use "none" or "" as the key to disable all log keys. For example `{"none":true}`

boolean

##### [](#responses-75)Responses

| HTTP Code | Description                  | Schema     |
| --------- | ---------------------------- | ---------- |
| **201**   | The operation was successful | No Content |

#### [](#%5Fget%5Flogging%5Ftags)Get Logging Tags

GET /_logging

##### [](#description-76)Description

Get logging tags of running instance.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Dev Ops

##### [](#responses-76)Responses

| HTTP Code | Description                                                                                                                        | Schema                 |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------- |
| **200**   | The response is a set of key-value pairs. The key is a log tag and the value is a boolean to indicate whether this tag is enabled. | [LogTags](#%5Flogtags) |

#### [](#%5Flogging%5Ftags%5Fput)Set Logging Tags

PUT /_logging

##### [](#description-77)Description

Enabling logging for a tag provides additional diagnostic information for that logging area.

The PUT request replaces all existing logging tags with the ones specified in the request body.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Dev Ops

##### [](#parameters-70)Parameters

| Type      | Name                     | Description                                                                                                                                                                                                                   | Schema                                             |
| --------- | ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| **Query** | **level** _optional_     | **Deprecated** \- please use logLevel instead This setting determines the verbosity of the logging - level=1 - The default, regular, logging - level=2 - Enables warnings and panics logging - level=3 - Will log panics only | integer                                            |
| **Query** | **logLevel** _optional_  | This setting determines the verbosity of the logging. Available values are - none\- error\- warn\- info\- debug\- trace Note that the setting is additive. For example, setting info will also enable both error and warn.    | string                                             |
| **Body**  | **log\_keys** _optional_ | Use the body to provide a list of the log keys you want to set. For example - {"Changes++":true, "Cache":true, "HTTP":true, "DCP":true, "WS": true, "WSFrame": true, "Replicate": true}                                       | [log\_keys](#%5Flogging%5Ftags%5Fput%5Flog%5Fkeys) |

**log\_keys**

Name

Description

Schema

**Access**  
_optional_

Anytime an access() call is made in the sync function.

boolean

**Admin**  
_optional_

Admin processes in Sync Gateway.

boolean

**All**  
_optional_

Use the wildcard character  to set all log keys For example `{"":true}` 

boolean

**Auth**  
_optional_

Authentication.

boolean

**Bucket**  
_optional_

Sync Gateway interactions with the bucket (trace level only).

boolean

**CRUD**  
_optional_

Updates made by Sync Gateway to documents.

boolean

**Cache**  
_optional_

Interactions with Sync Gateway's in-memory channel cache.

boolean

**Changes**  
_optional_

Processing of /{db}/\_changes requests.

boolean

**DCP**  
_optional_

DCP-feed processing.

boolean

**Events**  
_optional_

Event processing (webhooks).

boolean

**HTTP**  
_optional_

All requests made to the Sync Gateway REST APIs.

boolean

**HTTP+**  
_optional_

Additional information about HTTP requests (response times, status codes).

boolean

**Import**  
_optional_

Introduced in Sync Gateway 1.5 to help troubleshoot the import process of a document (this is the Sync Gateway process to make a document that was added through N1QL or the Server SDKs mobile-aware). This log key can be useful to troubleshoot why a given document was not successfully imported.

boolean

**Javascript**  
_optional_

All logging from Javascript. This includes - sync function, import filters, webhook filter function, and the custom ISGR conflict resolvers

boolean

**Migrate**  
_optional_

Logs messages thhat show when old inline document metdata is upgraded to xattrs

boolean

**Query**  
_optional_

Query is used for Sync Gateway code related to N1QL queries

boolean

**Replicate**  
_optional_

Log messages related to replications between Sync Gateways (using sg-replicate). This tag cannot be used for replications initiated by Couchbase Lite.

boolean

**SGCluster**  
_optional_

Log messages related to the sharded import and HA sg-replicate

boolean

**Sync**  
_optional_

Activity which relates to synchronization between Couchbase Lite and Sync Gateway

boolean

**SyncMsg**  
_optional_

Can be used for additional Sync logging output

boolean

**WS**  
_optional_

Websocket replication log messages

boolean

**WSFrame**  
_optional_

Can be used for additional WS logging output

boolean

**gocb**  
_optional_

All logging emitted by the GoCB SDK

boolean

**none**  
_optional_

Use "none" or "" as the key to disable all log keys. For example `{"none":true}`

boolean

##### [](#responses-77)Responses

| HTTP Code | Description                  | Schema     |
| --------- | ---------------------------- | ---------- |
| **201**   | The operation was successful | No Content |

#### [](#%5Fpost%5Fupgrade%5Fpost)Delete Obsolete Design Documents

POST /_post_upgrade

##### [](#description-78)Description

Starting in Sync Gateway 2.0, design documents used internally by Sync Gateway will include a version number in their name.

This version is incremented at each change, but the previous version of the design documents are retained, as they may be required by other nodes.

Use this `_post_upgrade` endpoint to remove any obsolete design documents when you are sure they are no longer needed.

_TIP:_ Use the `preview=true` query string option to check which design documents will be removed.

Typical use cases for this end point include:

* After upgrading Sync Gateway - see ([upgrade guide](upgrade.html#upgrade)).
* After moving from _non-import-docs_ to _import-docs_ methods. That is, from `import-docs=False` to `import-docs=True`

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Dev Ops

##### [](#parameters-71)Parameters

| Type      | Name                   | Description                                                                            | Schema  | Default |
| --------- | ---------------------- | -------------------------------------------------------------------------------------- | ------- | ------- |
| **Query** | **preview** _optional_ | Lists the design documents to be removed if the request is sent without this paramter. | boolean | "false" |

##### [](#responses-78)Responses

| HTTP Code | Description                 | Schema     |
| --------- | --------------------------- | ---------- |
| **200**   | The request was successful. | No Content |

#### [](#%5Freplicate%5Fpost)Start or Cancels Replication

POST /_replicate

> [!CAUTION]
> operation.deprecated

##### [](#description-79)Description

This API endpoint is now deprecated. It is replaced by the Inter-Sync Gateway Replication (v2) replication endpoint

_About_

This endpoint is used to start or cancel a database replication operation.

* Starting a replication with the \_replicate endpoint will implicitly set `adhoc=true` for the replication
* Setting `cancel=true` will set the replication state to **STOPPING**

_Canceling replications_

You can cancel continuous replications by adding the cancel field to the JSON request object and setting the value to true.

Note that the structure of the request must be identical to the original for the cancellation request to be honoured. For example, if you requested continuous replication, the cancellation request must also contain the continuous field.

_Constraints_

* Use this endpoint only for Inter-Sync Gateway Replication (v1) replications.

##### [](#parameters-72)Parameters

| Type     | Name                           | Description                                                                                       | Schema                                                    |
| -------- | ------------------------------ | ------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| **Body** | **ReplicationBody** _optional_ | SGR1 replication The request message body is a JSON document that contains the following objects. | [ReplicationBody](#%5Freplicate%5Fpost%5Freplicationbody) |

**ReplicationBody**

| Name                                | Description                                                                                                                                                                                                                                                                                    | Schema  |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **cancel** _optional_               | Indicates that a running replication task should be cancelled, the running task is identified by passing its replication\_id or by passing the original source and target values.                                                                                                              | boolean |
| **changes\_feed\_limit** _optional_ | The maximum number of change entries to pull in each loop of a continuous changes feed.                                                                                                                                                                                                        | integer |
| **continuous** _optional_           | Specifies whether the replication should be in continuous mode.                                                                                                                                                                                                                                | boolean |
| **filter** _optional_               | Indicates that the documents should be filtered using the specified filter function name. A common value used when replicating from Sync Gateway is sync\_gateway/bychannel to limit the pull replication to a set of channels.                                                                | string  |
| **query\_params** _optional_        | A set of key/value pairs to use in the querystring of the replication. For example, the channels field can be used to pull from a set of channels (in this particular case, the filter key must be set for the channels field to work as expected).                                            | object  |
| **replication\_id** _optional_      | If the cancel parameter is true then this is the id of the active replication task to be cancelled, otherwise this is the replication\_id to be used for the new replication. If no replication\_id is given for a new replication it will be assigned a random UUID.                          | string  |
| **source** _optional_               | Identifies the database to copy revisions from. Can be a string containing a local database name or a remote database URL, or an object whose url property contains the database name or URL. Also an object can contain headers property that contains custom header values such as a cookie. | string  |
| **target** _optional_               | Identifies the database to copy revisions to. Same format and interpretation as source.                                                                                                                                                                                                        | string  |

##### [](#responses-79)Responses

| HTTP Code | Description | Schema                                         |
| --------- | ----------- | ---------------------------------------------- |
| **200**   | 200 OK      | [ReplicationResponse](#%5Freplicationresponse) |

#### [](#%5Fsgcollect%5Finfo%5Fpost)Start Sgcollect\_info

POST /_sgcollect_info

##### [](#description-80)Description

Starting in Sync Gateway 2.1, sgcollect\_info can be triggered using this endpoint.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Dev Ops

##### [](#parameters-73)Parameters

| Type     | Name                           | Description                                                    | Schema                                                            |
| -------- | ------------------------------ | -------------------------------------------------------------- | ----------------------------------------------------------------- |
| **Body** | **sgcollect\_info** _optional_ | Options that can be specified to use in an sgcollect\_info run | [sgcollect\_info](#%5Fsgcollect%5Finfo%5Fpost%5Fsgcollect%5Finfo) |

**sgcollect\_info**

| Name                         | Description                                                                                                                  | Schema  |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------- |
| **customer** _optional_      | Customer name to use when uploading logs. required - if upload is set                                                        | string  |
| **output\_dir** _optional_   | Where to store the collected zip. **Default** : "configured \`LogFilePath location (for example /home/sync\_gateway/logs)"\` | string  |
| **redact\_level** _optional_ | Can be set to none or partial for redaction of collected logs. **Default** : "none"                                          | string  |
| **redact\_salt** _optional_  | If set, use this salt when redacting logs.                                                                                   | string  |
| **ticket** _optional_        | Zendesk ticket number to use when uploading logs.                                                                            | string  |
| **upload** _optional_        | Whether to upload the collected logs. **Default** : false                                                                    | boolean |
| **upload\_host** _optional_  | s3 URL for upload. **Default** : "https://uploads.couchbase.com"                                                             | string  |

##### [](#responses-80)Responses

| HTTP Code | Description                 | Schema     |
| --------- | --------------------------- | ---------- |
| **200**   | The request was successful. | No Content |

#### [](#%5Fsgcollect%5Finfo%5Fget)Get Sgcollect\_info Status

GET /_sgcollect_info

##### [](#description-81)Description

Will return information about whether sgcollect\_info is currently running or not.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Dev Ops

##### [](#responses-81)Responses

| HTTP Code | Description                  | Schema                                       |
| --------- | ---------------------------- | -------------------------------------------- |
| **200**   | The operation was successful | [SGCollectInfoStats](#%5Fsgcollectinfostats) |

#### [](#%5Fsgcollect%5Finfo%5Fdelete)Stop Sgcollect\_info

DELETE /_sgcollect_info

##### [](#description-82)Description

sgcollect\_info can be cancelled using ths endpoint.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Dev Ops

##### [](#parameters-74)Parameters

| Type     | Name                           | Description                                                    | Schema                                                              |
| -------- | ------------------------------ | -------------------------------------------------------------- | ------------------------------------------------------------------- |
| **Body** | **sgcollect\_info** _optional_ | Options that can be specified to use in an sgcollect\_info run | [sgcollect\_info](#%5Fsgcollect%5Finfo%5Fdelete%5Fsgcollect%5Finfo) |

**sgcollect\_info**

| Name                         | Description                                                                                                                  | Schema  |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ------- |
| **customer** _optional_      | Customer name to use when uploading logs. required - if upload is set                                                        | string  |
| **output\_dir** _optional_   | Where to store the collected zip. **Default** : "configured \`LogFilePath location (for example /home/sync\_gateway/logs)"\` | string  |
| **redact\_level** _optional_ | Can be set to none or partial for redaction of collected logs. **Default** : "none"                                          | string  |
| **redact\_salt** _optional_  | If set, use this salt when redacting logs.                                                                                   | string  |
| **ticket** _optional_        | Zendesk ticket number to use when uploading logs.                                                                            | string  |
| **upload** _optional_        | Whether to upload the collected logs. **Default** : false                                                                    | boolean |
| **upload\_host** _optional_  | s3 URL for upload. **Default** : "https://uploads.couchbase.com"                                                             | string  |

##### [](#responses-82)Responses

| HTTP Code | Description                 | Schema     |
| --------- | --------------------------- | ---------- |
| **200**   | The request was successful. | No Content |

### [](#%5Fsession%5Fresource)Session

Manage user sessions

#### [](#%5Fdb%5Fsession%5Fpost)Create New Session

POST /{db}/_session

##### [](#description-83)Description

If the credentials provided in the request body are valid, the session is created with an idle session timeout of 24 hours. An idle session timeout in the context of Sync Gateway is defined as the following: - If 10% or more of the current expiration time has elapsed when a subsequent request with that session id is processed, the session's expiry time is automatically updated to 24 hours from that time.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Architect
* Sync Gateway Application

##### [](#parameters-75)Parameters

| Type     | Name                       | Description                                                              | Schema                                               |
| -------- | -------------------------- | ------------------------------------------------------------------------ | ---------------------------------------------------- |
| **Path** | **db** _required_          | Database name                                                            | string                                               |
| **Body** | **SessionBody** _optional_ | The message body is a JSON document that contains the following objects. | [SessionBody](#%5Fdb%5Fsession%5Fpost%5Fsessionbody) |

**SessionBody**

| Name                | Description                                                                                                                                 | Schema  |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **name** _optional_ | Username of the user the session will be associated to.                                                                                     | string  |
| **ttl** _optional_  | Default is 24 hours (86400 seconds). The TTL (time-to-live) of the session, in seconds. The value must be greater than 0. **Example** : 180 | integer |

##### [](#responses-83)Responses

| HTTP Code | Description                   | Schema                                                   |
| --------- | ----------------------------- | -------------------------------------------------------- |
| **200**   | Session successfully created. | [Response 200](#%5Fdb%5Fsession%5Fpost%5Fresponse%5F200) |

**Response 200**

| Name                        | Description                      | Schema |
| --------------------------- | -------------------------------- | ------ |
| **cookie\_name** _optional_ | Cookie used for session handling | string |
| **expires** _optional_      | Expiration time for session.     | string |
| **session\_id** _optional_  | Session ID.                      | string |

#### [](#%5Fdb%5Fsession%5Fsessionid%5Fget)Get Session Data

GET /{db}/_session/{sessionid}

##### [](#description-84)Description

This request retrieves information about a session.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Architect
* Sync Gateway Application
* Sync Gateway Application Read Only

##### [](#parameters-76)Parameters

| Type     | Name                     | Description   | Schema |
| -------- | ------------------------ | ------------- | ------ |
| **Path** | **db** _required_        | Database name | string |
| **Path** | **sessionid** _required_ | Session id    | string |

##### [](#responses-84)Responses

| HTTP Code | Description                              | Schema                                                              |
| --------- | ---------------------------------------- | ------------------------------------------------------------------- |
| **200**   | 200 OK - Request completed successfully. | [Response 200](#%5Fdb%5Fsession%5Fsessionid%5Fget%5Fresponse%5F200) |

**Response 200**

| Name                                    | Description                                                                                                                                                 | Schema           |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| **authentication\_handlers** _optional_ |                                                                                                                                                             | < object > array |
| **ok** _optional_                       | Success flag                                                                                                                                                | boolean          |
| **userCtx** _optional_                  | Contains an object with properties channels (the list of channels for the user associated with the session) and name (the user associated with the session) | object           |

#### [](#%5Fdb%5Fsession%5Fsessionid%5Fdelete)Delete Specific Session

DELETE /{db}/_session/{sessionid}

##### [](#description-85)Description

This request deletes a single session.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Architect
* Sync Gateway Application

##### [](#parameters-77)Parameters

| Type     | Name                     | Description   | Schema |
| -------- | ------------------------ | ------------- | ------ |
| **Path** | **db** _required_        | Database name | string |
| **Path** | **sessionid** _required_ | Session id    | string |

##### [](#responses-85)Responses

| HTTP Code | Description                                                                                                                                                                                          | Schema     |
| --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **200**   | 200 OK - Request completed successfully. If the session is successfully deleted, the response has an empty message body. If the session is not deleted, the message body contains error information. | No Content |

#### [](#%5Fdb%5Fuser%5Fname%5Fsession%5Fdelete)Delete All User Sessions

DELETE /{db}/_user/{name}/_session

##### [](#description-86)Description

This request delete the session for the specified user.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Architect
* Sync Gateway Application

##### [](#parameters-78)Parameters

| Type     | Name                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Schema |
| -------- | ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **Path** | **db** _required_   | Database name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | string |
| **Path** | **name** _required_ | User's name, may contain contain any combination of the characters \[a-z A-Z 0-9 - + . @ %\], when creating a user any other characters must be percent encoded, see: <https://en.wikipedia.org/wiki/Percent-encoding>. When passing a user name in a URL path it must be escaped again using percent encoding for example if a user is created with the name "0\|59", the '|' character must first be percent-encoded resulting in "0%7C59". When using the same user name in a URL path it must be percent-encoded a second time resulting in "0%257C59" | string |

##### [](#responses-86)Responses

| HTTP Code | Description           | Schema     |
| --------- | --------------------- | ---------- |
| **200**   | User session deleted. | No Content |

#### [](#%5Fdb%5Fuser%5Fname%5Fsession%5Fsessionid%5Fdelete)Delete Specific User Session

DELETE /{db}/_user/{name}/_session/{sessionid}

##### [](#description-87)Description

This request delete the specified session for the specified user.

_Sync Gateway Roles Required (CBS 7.0.2 Developer Preview):_

* Sync Gateway Architect
* Sync Gateway Application

##### [](#parameters-79)Parameters

| Type     | Name                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Schema |
| -------- | ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **Path** | **db** _required_        | Database name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | string |
| **Path** | **name** _required_      | User's name, may contain contain any combination of the characters \[a-z A-Z 0-9 - + . @ %\], when creating a user any other characters must be percent encoded, see: <https://en.wikipedia.org/wiki/Percent-encoding>. When passing a user name in a URL path it must be escaped again using percent encoding for example if a user is created with the name "0\|59", the '|' character must first be percent-encoded resulting in "0%7C59". When using the same user name in a URL path it must be percent-encoded a second time resulting in "0%257C59" | string |
| **Path** | **sessionid** _required_ | Session id                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | string |

##### [](#responses-87)Responses

| HTTP Code | Description           | Schema     |
| --------- | --------------------- | ---------- |
| **200**   | User session deleted. | No Content |

## [](#%5Fdefinitions)Definitions

### [](#%5Fbootstrap%5Fmodel)Bootstrap\_model

Sync Gateway's start-up configuration properties

| Name                                  | Description                                                   | Schema                                                       |
| ------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------------------ |
| **api** _optional_                    | Define API related configuration properties                   | [API configuration](#%5Fapi%5Fconfiguration)                 |
| **auth** _optional_                   | Define Auth related configuration properties                  | [Auth configuration](#%5Fauth%5Fconfiguration)               |
| **bootstrap** _optional_              | Define fundamental bootstrap related configuration properties | [Bootstrap configuration](#%5Fbootstrap%5Fconfiguration)     |
| **logging** _optional_                | Define logging configuration                                  | [Logging\_model](#%5Flogging%5Fmodel)                        |
| **max\_file\_descriptors** _optional_ | Maximum number of open file descriptors.                      | integer                                                      |
| **replicator** _optional_             | Define Replicator related configuration properties            | [Replicator configuration](#%5Freplicator%5Fconfiguration)   |
| **unsupported** _optional_            | Collection of unsupported properties                          | [Unsupported configuration](#%5Funsupported%5Fconfiguration) |

**API configuration**

| Name                                              | Description                                                                                                                                                                                                                                                                                                                                                                                            | Schema                                 |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------- |
| **admin\_interface** _optional_                   | Port or TCP network address (IP address and the port) that the Admin REST API listens on. The loopback address prefix before the port (127.0.0.1) means the interface will not be reachable from other hosts. To make it reachable, change it to ":4985". Change requires restart of Admin API **Default** : "127.0.0.1:4985"                                                                          | string                                 |
| **admin\_interface\_authentication** _optional_   | Use the admin\_interface\_authentication property to disable authentication for the metrics API. This option should be used with discretion and only in test environments. By default the Admin API requires Couchbase Server RBAC authentication. The user must provide credentials to an existing user with an appropriate Sync Gateway role. **Default** : true                                     | boolean                                |
| **compress\_responses** _optional_                | Whether to compress HTTP responses. Set to false to disable compression of HTTP responses. **Default** : true                                                                                                                                                                                                                                                                                          | boolean                                |
| **cors** _optional_                               | Configuration object for allowing cross-origin resource sharing (CORS). This is useful to interact directly with Sync Gateway from HTML 5 applications via XHR. Change requires HTTP server restart                                                                                                                                                                                                    | [cors](#%5Fbootstrap%5Fmodel%5Fcors)   |
| **hide\_product\_version** _optional_             | Determines whether product versions are removed from Server headers and REST API responses. This setting does not apply to the Admin REST API. This customization of the Sync Gateway response avoids revealing the version of the Sync Gateway to HTTP requests to the root path. **Default** : false                                                                                                 | boolean                                |
| **https** _optional_                              | Group in which to specify any API HTTPS configuration properties                                                                                                                                                                                                                                                                                                                                       | [https](#%5Fbootstrap%5Fmodel%5Fhttps) |
| **idle\_timeout** _optional_                      | Maximum duration (in seconds) to wait for the next request when keep-alives are enabled Change requires HTTP server restart                                                                                                                                                                                                                                                                            | integer                                |
| **max\_connections** _optional_                   | Maximum number of incoming HTTP connections to accept. Change requires HTTP server restart                                                                                                                                                                                                                                                                                                             | integer                                |
| **metrics\_interface** _optional_                 | This defines the Port or TCP network address (IP address and the port) that the Metrics REST API will listen on. Using the loopback address prefix before the port (127.0.0.1) means the interface will not be reachable from other hosts. For example "metricsInterface": "127.0.0.1:4986" **Default** : "127.0.0.1:4986"                                                                             | string                                 |
| **metrics\_interface\_authentication** _optional_ | Use the metrics\_interface\_authentication property to disable authentication for the metrics API. This option should be used with discretion and only in test environments. By default the Metrics API requires Couchbase Server RBAC authentication. The user must provide credentials to an existing user with an appropriate Sync Gateway role. **Default** : true                                 | boolean                                |
| **pretty** _optional_                             | (**Deprecated**) Whether to pretty-print JSON responses. **Default** : false                                                                                                                                                                                                                                                                                                                           | boolean                                |
| **profile\_interface** _optional_                 | TCP network address (IP address and the port) that the Go profile API listens on. You can obtain Go profiling information from the interface. You can omit the IP address.                                                                                                                                                                                                                             | string                                 |
| **public\_interface** _optional_                  | Public REST API port Change requires restart of Public API **Default** : ":4984"                                                                                                                                                                                                                                                                                                                       | string                                 |
| **read\_header\_timeout** _optional_              | Maximum duration (in seconds) allowed to read request headers Change requires HTTP server restart                                                                                                                                                                                                                                                                                                      | integer                                |
| **server\_read\_timeout** _optional_              | Maximum duration in seconds before timing out the read of an HTTP(S) request. This property only effects the HTTP connections on the Sync Gateway public and admin ports. Sync Gateway is written in the Go programming language, therefore the value set in the configuration file is passed to Go's server instance <https://golang.org/pkg/net/http/#Server>. Change requires HTTP server restart   | integer                                |
| **server\_write\_timeout** _optional_             | Maximum duration in seconds before timing out the write of an HTTP(S) response. This property only effects the HTTP connections on the Sync Gateway public and admin ports. Sync Gateway is written in the Go programming language, therefore the value set in the configuration file is passed to Go's server instance <https://golang.org/pkg/net/http/#Server>. Change requires HTTP server restart | integer                                |

**cors**

Name

Description

Schema

**headers**  
_optional_

List of HTTP headers that can be used by domains specified in the `origin` and `login_origin` properties.

A common value is `["Content-Type"]` as clients use the `Content-Type: application/json` header when sending data as JSON in the body of POST/PUT requests.

Change requires HTTP server restart

< string > array

**login\_origin**  
_optional_

List of allowed login origins.

Change requires HTTP server restart

< string > array

**max\_age**  
_optional_

Value for the Access-Control-Max-Age header. This is the period of time, in seconds, that the response to a CORS preflight request is cached before sending another preflight request.

Change requires HTTP server restart

integer

**origin**  
_optional_

List of allowed origins; use a wildcard character () to allow access from everywhere. 

\*Note that the wildcard (\*) cannot be used if you plan to authenticate users as well (by using the `withCredentials` flag on the client side). Instead specify the explicit domain(s) in the `origin` and `login_origin` properties of the configuration file.

Change requires HTTP server restart

< string > array

**https**

| Name                                 | Description                                                                                                                                                                                                                                                                                                                     | Schema |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **tls\_cert\_path** _optional_       | Absolute or relative path on the filesystem to the TLS certificate file, if TLS is used to secure Sync Gateway connections To use plaintext, omit both this property and the tls\_key\_path property. A relative path is from the directory that contains the Sync Gateway executable file. Change requires HTTP server restart | string |
| **tls\_key\_path** _optional_        | Absolute or relative path on the filesystem to the TLS private key files. To use plaintext, omit both this property and the tls\_cert\_path property. A relative path is from the directory that contains the Sync Gateway executable file. Change requires HTTP server restart                                                 | string |
| **tls\_minimum\_version** _optional_ | Enforce a minimum TLS version to be used in replications with Couchbase Lite. Possible values are: \* "tlsv1" \* "tlsv1.1" \* "tlsv1.2" \* "tlsv1.3" Change requires HTTP server restart **Default** : "tlsv1.2"                                                                                                                | string |

**Auth configuration**

| Name                        | Description                            | Schema  |
| --------------------------- | -------------------------------------- | ------- |
| **bcrypt\_cost** _optional_ | Cost to use for bcrypt password hashes | integer |

**Bootstrap configuration**

| Name                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Schema  |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **ca\_cert\_path** _optional_              | Absolute or relative path on the filesystem to the root CA certificate to verify the certificate chain and hostname of the Couchbase Server cluster. Works in conjunction with server\_tls\_skip\_verify to control whether system root pool is used or not. Set this empty and server\_tls\_skip\_verify true to avoid using system root pool                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | string  |
| **config\_update\_frequency** _optional_   | Sets the interval between checks for new or updated configurations made by other nodes in Couchbase Server It is provided as string, which uses Go's duration format (e.g: 1s = 1 second, 5m = 5 minutes , 1h32m15s = 1 hour, 32 mins, 15 seconds) see: <https://pkg.go.dev/time#ParseDuration> **Default** : "10s"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | string  |
| **group\_id** _optional_                   | The ID of the configuration group to which this node belongs. **Default** : "default"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | string  |
| **kv\_tls\_port** _optional_               | Optional value for the Memcached TLS port, if not using the default (11207)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | integer |
| **max\_concurrent\_query\_ops** _optional_ | Sets the maximum number of concurrent query operations allowed                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | integer |
| **password** _optional_                    | The password to be used when authenticating to the server. **Default** : "none"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | string  |
| **server** _optional_                      | Sets the endpoint for the Couchbase Server holding (database) configuration details. The value of the _server_ property specifies the Hostname(s) to the Couchbase Server node(s) in the cluster. Sync Gateway supports the ability to specify multiple hosts in the configuration. Sync Gateway supports both the couchbase:// and http:// schemes for specifying connection endpoints. Sync Gateway also supports _SSL_ in the connection to Couchbase Server; use the couchbases:// scheme for this. As with the Couchbase Server SDKs, the https:// scheme is **not** supported. Examples of valid server values for _IPv4_ include: - couchbase://host1\- couchbases://host1\- couchbase://host1,host2\- couchbase://host1:11210,host2,\- couchbases://host1:11207,host2\- <http://host1:8091>\- <http://host1,host2:8091>\- <http://foo:bar@host1:8091> Examples of valid server values for _IPv6_ include: - http://\[2001:db8::8811\]:8091 _// single node IPv6 - http scheme with default server port_\- couchbases://\[2001:db8::8811\] _// single node SSL IPv6 - default port (omitted)_\- couchbase://\[2001:db8::8811\],\[2001:db8::8822\]:888 _// node1 default port, node2 port 888_ As with the SDK, when using the couchbase:// or couchbases:// schemes, the port is not required, but if specified should be the external/internal bucket ports (defaults are 11210 or 11207 respectively). Attempting to use the admin ports (8091/18091) will result in a startup error. **Alternate Addresses** On startup, Sync Gateway will try each hostname that is provided until it is able to connect successfully. By default, if a remote cluster has an external address set, then when SG connects it will apply a heuristic to determine whether to choose between external or default (internal) addresses. The choice is based on the host names supplied in the connection string. - SG uses external networking only when none of the supplied host names match any of Couchbase Server's internal node addresses, and an external address is defined. - In all other cases Sync Gateway uses the default (internal) networking. However, it is possible to override this behavior by adding a network parameter to the connection string. The network parameter can be – - auto - this is the default value if no parameter is provided. In this case the heuristic described above is applied to determine the address used; so effectively there is no override. - external - to always force use of the external address - default - to always force use of the internal address For example: "server": "couchbases://my-cbs-server?network=default" Will force the connection to ignore any alternative external addresses configured on the Couchbase Server node. **Lost Connections** If the connection to Couchbase Server is lost during normal operations, Sync Gateway will automatically re-connect to another node in the cluster. During that re-connection period, the Sync Gateway will appear offline - see [Taking Databases Offline](database-offline.html) \- and documents will not be replicated to mobile clients. **Default** : "none" | string  |
| **server\_tls\_skip\_verify** _optional_   | Defaults to false, which requires a valid CA Cert Path. Works in conjunction with ca\_cert\_path to control whether system root pool is used or not. Set this true and ca\_cert\_path empty to allow, for example, self-signed or un-trusted certificates. This will be the default of-of-the-box setting.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | boolean |
| **use\_tls\_server** _optional_            | Default to true, which forces the connection to Couchbase Server to use TLS. Use use\_tls\_server to enforce use of a secure scheme (for example, couchbases://) to connect to Couchbase Server. Set this false to use a non-secure scheme (for example with couchbase://). If the scheme used does not match that indicated by the use\_tls\_server value (for example, couchbases:// with use\_tls\_server \= false) then Sync Gateway will error and refuse to start. **Default** : true                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | boolean |
| **username** _optional_                    | The username to be used when authenticating to the server. **Default** : "none"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | string  |
| **x509\_cert\_path** _optional_            | Use x509\_cert\_path to define the absolute or relative path on the filesystem to the x509 certificate. Relative paths are relative to the directory containing the Sync Gateway executable.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | string  |
| **x509\_key\_path** _optional_             | Absolute or relative path on the filesystem to the X509 key. Relative paths are relative to the directory containing the Sync Gateway executable.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | string  |

**Replicator configuration**

| Name                             | Description                                                                                                                                                                                                                 | Schema  |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **blip\_compression** _optional_ | This sets the 'deflate' compression level to use when compressing messages sent via the WebSocket protocol, where: \* 0 means no compression, \* 1 means fastest (least) compression \* 9 means slowest (most) compression. | integer |
| **max\_heartbeat** _optional_    | This specifies the Maximum Heartbeat value for the \_changes feed requests; the time in second between heartbeats. - The default value of maxHeartbeat is 0 (zero) - The minimum value of maxHeartbeat is 25 (25,000 ms)    | integer |

**Unsupported configuration**

| Name                             | Description                                                                                                                                                                                             | Schema  |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **http2.enabled** _optional_     | **Default** : false                                                                                                                                                                                     | boolean |
| **stats\_log\_freq** _optional_  | It is provided as string, which uses Go's duration format (e.g: 1s = 1 second, 5m = 5 minutes , 1h32m15s = 1 hour, 32 mins, 15 seconds) see: <https://pkg.go.dev/time#ParseDuration> **Default** : "1m" | string  |
| **use\_stdlib\_json** _optional_ | **Default** : false                                                                                                                                                                                     | boolean |

### [](#%5Flogging%5Fmodel)Logging\_model

Holding object for all logging-related settings.

Note that in addition to setting these logging values in the bootstrap configuration file, you can also use the ADMIN Rest API to set or change the values without requiring a full reload. See: [Rest Admin API](rest-api-admin.html)

A full logging initialization is required.

See the [Logging](logging.html) page for a fuller explanation on logging settings.

| Name                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Schema                                   |
| ------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| **console** _optional_          | Settings for the console output logging.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | [console](#%5Flogging%5Fmodel%5Fconsole) |
| **debug** _optional_            | The debug logging-level provides lower level development analysis \* Minimum max\_age is 1 day \_ Log File Name is sg\_debug.log                                                                                                                                                                                                                                                                                                                                                                                           | [debug](#%5Flogging%5Fmodel%5Fdebug)     |
| **error** _optional_            | Activate the error logging level - see [Logging](logging.html) page for more on log levels.                                                                                                                                                                                                                                                                                                                                                                                                                                | [error](#%5Flogging%5Fmodel%5Ferror)     |
| **info** _optional_             | The information logging-level provides important diagnostics for support and customers                                                                                                                                                                                                                                                                                                                                                                                                                                     | [info](#%5Flogging%5Fmodel%5Finfo)       |
| **log\_file\_path** _optional_  | Absolute or relative path on the filesystem to the log file. A relative path is from the directory that contains the Sync Gateway executable file. Changes require full logging re-initialization                                                                                                                                                                                                                                                                                                                          | string                                   |
| **redaction\_level** _optional_ | Optionally, log files can be redacted. This means that user-data, considered to be private, is removed. Such data includes: \* Key/value pairs in JSON documents \* Usernames \* Query-fields that reference key/value pairs and/or usernames \* Names and email addresses retrieved during product registration \* Extended attributes This redaction of user-data is referred to as partial redaction. To enable it, set this property to "redaction\_level" : "partial" in the configuration file: **Default** : "none" | string                                   |
| **stats** _optional_            | The stats logging level                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | [stats](#%5Flogging%5Fmodel%5Fstats)     |
| **trace** _optional_            | The trace logging-level.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | [trace](#%5Flogging%5Fmodel%5Ftrace)     |
| **warn** _optional_             | The warning logging-level is triggered when Sync Gateway detects something is wrong but it can still service requests \* Minimum max\_age is 90 days \* Log File Name is sg\_warn.log                                                                                                                                                                                                                                                                                                                                      | [warn](#%5Flogging%5Fmodel%5Fwarn)       |

**console**

| Name                                   | Description                                                                                                                                                                                             | Schema                                     |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| **collation\_buffer\_size** _optional_ | Size of the collation buffer                                                                                                                                                                            | integer                                    |
| **color\_enabled** _optional_          | Use ANSI color codes in the console output (Linux/MacOS only). **Default** : false                                                                                                                      | boolean                                    |
| **enabled** _optional_                 | Indicates whether console logging is enabled                                                                                                                                                            | boolean                                    |
| **file\_output** _optional_            | Changes require full logging re-initialization                                                                                                                                                          | string                                     |
| **log\_keys** _optional_               | List of log keys to enable for diagnostic logging. Available log key values are described in the [Log Keys](logging.html#lbl-log-keys) page                                                             | < string > array                           |
| **log\_level** _optional_              | The level of logging. Log levels are cumulative (that is, log entries at WARN will also be included in the INFO and DEBUG logs). See: [Log Levels](logging.html#lbl-log-keys) page **Default** : "info" | string                                     |
| **rotation** _optional_                | The log file may be rotated by defining a "rotation" sub document. See details in [log rotation](logging.html#lbl-logrotate).                                                                           | [rotation](#%5Flogging%5Fmodel%5Frotation) |

**rotation**

| Name                                      | Description                                                                                                                                                                                 | Schema  |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **localtime** _optional_                  | If true, it uses the computer's local time to format the backup timestamp. False uses UTC. **Default** : false                                                                              | boolean |
| **max\_age** _optional_                   | The maximum number of days to retain old log files. This can't be set below the minimum allowed value for the given level.                                                                  | integer |
| **max\_size** _optional_                  | The maximum size in MB of the log file before it gets rotated.                                                                                                                              | integer |
| **rotated\_logs\_size\_limit** _optional_ | Controls how much disk space the rotated (and compressed) log files for this level can take up. The value is expressed in megabytes. The minimum value is 10 and there is no maximum value. | integer |

**debug**

| Name                                   | Description                                                                                                                                                                                                                                                  | Schema                                     |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------ |
| **collation\_buffer\_size** _optional_ | Size of the collation buffer                                                                                                                                                                                                                                 | integer                                    |
| **enabled** _optional_                 | Sets this logging-level on or off. Note, you are advised to keep this log level enabled when troubleshooting issues. Enabling this log level is a requirement to receive [Enterprise Support](https://www.couchbase.com/support-policy). **Default** : false | boolean                                    |
| **rotation** _optional_                | The log file may be rotated by defining a "rotation" sub document. See details in [log rotation](logging.html#lbl-logrotate).                                                                                                                                | [rotation](#%5Flogging%5Fmodel%5Frotation) |

**rotation**

| Name                                      | Description                                                                                                                                                                                 | Schema  |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **localtime** _optional_                  | If true, it uses the computer's local time to format the backup timestamp. False uses UTC. **Default** : false                                                                              | boolean |
| **max\_age** _optional_                   | The maximum number of days to retain old log files. This can't be set below the minimum allowed value for the given level.                                                                  | integer |
| **max\_size** _optional_                  | The maximum size in MB of the log file before it gets rotated.                                                                                                                              | integer |
| **rotated\_logs\_size\_limit** _optional_ | Controls how much disk space the rotated (and compressed) log files for this level can take up. The value is expressed in megabytes. The minimum value is 10 and there is no maximum value. | integer |

**error**

| Name                                   | Description                                                                                                                                                                                                                                                                                                                                               | Schema                                     |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| **collation\_buffer\_size** _optional_ | Size of the collation buffer                                                                                                                                                                                                                                                                                                                              | integer                                    |
| **enabled** _optional_                 | Enable this _error_ log level. \* The _error_, _warn_ and _info_ log levels are enabled by default. \* The _debug_ log level is disabled by default. **Note:** You are advised to keep this log level enabled to troubleshoot issues. Enabling this log level is a requirement to receive [Enterprise Support](https://www.couchbase.com/support-policy). | boolean                                    |
| **rotation** _optional_                | The log file may be rotated by defining a "rotation" sub document. See details in [log rotation](logging.html#lbl-logrotate).                                                                                                                                                                                                                             | [rotation](#%5Flogging%5Fmodel%5Frotation) |

**rotation**

| Name                                      | Description                                                                                                                                                                                 | Schema  |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **localtime** _optional_                  | If true, it uses the computer's local time to format the backup timestamp. False uses UTC. **Default** : false                                                                              | boolean |
| **max\_age** _optional_                   | The maximum number of days to retain old log files. This can't be set below the minimum allowed value for the given level.                                                                  | integer |
| **max\_size** _optional_                  | The maximum size in MB of the log file before it gets rotated.                                                                                                                              | integer |
| **rotated\_logs\_size\_limit** _optional_ | Controls how much disk space the rotated (and compressed) log files for this level can take up. The value is expressed in megabytes. The minimum value is 10 and there is no maximum value. | integer |

**info**

| Name                                   | Description                                                       | Schema                                     |
| -------------------------------------- | ----------------------------------------------------------------- | ------------------------------------------ |
| **collation\_buffer\_size** _optional_ | Size of the collation buffer                                      | integer                                    |
| **enabled** _optional_                 | Whether to enable this log level. **Default** : true              | boolean                                    |
| **rotation** _optional_                | The log file may be rotated by defining a "rotation" sub document | [rotation](#%5Flogging%5Fmodel%5Frotation) |

**rotation**

| Name                                      | Description                                                                                                                                                                                 | Schema  |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **localtime** _optional_                  | If true, it uses the computer's local time to format the backup timestamp. False uses UTC. **Default** : false                                                                              | boolean |
| **max\_age** _optional_                   | The maximum number of days to retain old log files. This can't be set below the minimum allowed value for the given level.                                                                  | integer |
| **max\_size** _optional_                  | The maximum size in MB of the log file before it gets rotated.                                                                                                                              | integer |
| **rotated\_logs\_size\_limit** _optional_ | Controls how much disk space the rotated (and compressed) log files for this level can take up. The value is expressed in megabytes. The minimum value is 10 and there is no maximum value. | integer |

**stats**

| Name                                   | Description                                                                                                                   | Schema                                     |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| **collation\_buffer\_size** _optional_ | Size of the collation buffer                                                                                                  | integer                                    |
| **enabled** _optional_                 | Whether to enable this log level. **Default** : false                                                                         | boolean                                    |
| **rotation** _optional_                | The log file may be rotated by defining a "rotation" sub document. See details in [log rotation](logging.html#lbl-logrotate). | [rotation](#%5Flogging%5Fmodel%5Frotation) |

**rotation**

| Name                                      | Description                                                                                                                                                                                 | Schema  |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **localtime** _optional_                  | If true, it uses the computer's local time to format the backup timestamp. False uses UTC. **Default** : false                                                                              | boolean |
| **max\_age** _optional_                   | The maximum number of days to retain old log files. This can't be set below the minimum allowed value for the given level.                                                                  | integer |
| **max\_size** _optional_                  | The maximum size in MB of the log file before it gets rotated.                                                                                                                              | integer |
| **rotated\_logs\_size\_limit** _optional_ | Controls how much disk space the rotated (and compressed) log files for this level can take up. The value is expressed in megabytes. The minimum value is 10 and there is no maximum value. | integer |

**trace**

| Name                                   | Description                                                                                                                   | Schema                                     |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| **collation\_buffer\_size** _optional_ | Size of the collation buffer                                                                                                  | integer                                    |
| **enabled** _optional_                 | Whether to enable this log level. **Default** : false                                                                         | boolean                                    |
| **rotation** _optional_                | The log file may be rotated by defining a "rotation" sub document. See details in [log rotation](logging.html#lbl-logrotate). | [rotation](#%5Flogging%5Fmodel%5Frotation) |

**rotation**

| Name                                      | Description                                                                                                                                                                                 | Schema  |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **localtime** _optional_                  | If true, it uses the computer's local time to format the backup timestamp. False uses UTC. **Default** : false                                                                              | boolean |
| **max\_age** _optional_                   | The maximum number of days to retain old log files. This can't be set below the minimum allowed value for the given level.                                                                  | integer |
| **max\_size** _optional_                  | The maximum size in MB of the log file before it gets rotated.                                                                                                                              | integer |
| **rotated\_logs\_size\_limit** _optional_ | Controls how much disk space the rotated (and compressed) log files for this level can take up. The value is expressed in megabytes. The minimum value is 10 and there is no maximum value. | integer |

**warn**

| Name                                   | Description                                                                                                                                                                                                                                                                                                                                                      | Schema                                     |
| -------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| **collation\_buffer\_size** _optional_ | Size of the collation buffer                                                                                                                                                                                                                                                                                                                                     | integer                                    |
| **enabled** _optional_                 | Whether to enable this log level. The _error_, _warn_ and _info_ log levels are enabled by default. The _debug_ log level is disabled by default. Note, however, that you are advised to keep this log level enabled to troubleshoot issues. Enabling this log level is a requirement to receive [Enterprise Support](https://www.couchbase.com/support-policy). | boolean                                    |
| **rotation** _optional_                | The log file may be rotated by defining a "rotation" sub document. See details in [log rotation](logging.html#lbl-logrotate).                                                                                                                                                                                                                                    | [rotation](#%5Flogging%5Fmodel%5Frotation) |

**rotation**

| Name                                      | Description                                                                                                                                                                                 | Schema  |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **localtime** _optional_                  | If true, it uses the computer's local time to format the backup timestamp. False uses UTC. **Default** : false                                                                              | boolean |
| **max\_age** _optional_                   | The maximum number of days to retain old log files. This can't be set below the minimum allowed value for the given level.                                                                  | integer |
| **max\_size** _optional_                  | The maximum size in MB of the log file before it gets rotated.                                                                                                                              | integer |
| **rotated\_logs\_size\_limit** _optional_ | Controls how much disk space the rotated (and compressed) log files for this level can take up. The value is expressed in megabytes. The minimum value is 10 and there is no maximum value. | integer |

### [](#%5Fdatabase%5Fmodel)Database\_model

This `database` object defines the JSON configuration of a sync gateway database.

Provision the configuration using the request message body of a `put /{db}/` and-or `put /{db}/_config`that comprises all the properties required to upsert a replication.

| Name                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Schema                                                               |
| ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| **allow\_conflicts** _optional_                   | Use allow\_conflict to define whether Sync Gateway will handle conflicts. The default of true indicates that conflicts are handled. Set the value to false to cause Sync Gateway to reject any attempt to write conflicting revisions (returning a 409 HTTP status code). It will be up to the client to resolve the conflict. Restarting Sync Gateway with this property enabled will not automatically result in disk space savings (compaction on a document won't occur until a document is updated). _Constraints:_\- Push replications to pre-2.8 targets do not support the "allow\_conflicts": false setting; the target must use "allow\_conflicts": true. Change initiates a database restart. **Default** : true                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | boolean                                                              |
| **allow\_empty\_password** _optional_             | Use allow\_empty\_password to define whether to Sync Gateway users can be created with empty passwords. **Default** : false                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | boolean                                                              |
| **bucket** _optional_                             | Defines the Couchbase Server bucket to be used for this Sync Gateway database bucket If not specified, then the database name is used as the bucket name. **Default** : "the database name"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | string                                                               |
| **bucket\_op\_timeout\_ms** _optional_            | Use bucket\_op\_timeout\_ms to define how long Sync Gateway will wait for a bucket operation to complete before timing out and trying again. You may increase this value where there is a heavy load on Couchbase Server and operations are likely to take more than 2.5 seconds to complete. The default value is 2500 milliseconds. Changes initiate a database restart.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | integer                                                              |
| **cache** _optional_                              | The cache group of properties define the configuration for this database's channel and revision caches                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | [Cache](#%5Fcache)                                                   |
| **client\_partition\_window\_secs** _optional_    | Use the client\_partition\_window\_secs property to define how long clients can remain offline for without losing replication metadata. Default 2 592 000 seconds (30 days) **Default** : "2592000"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | string                                                               |
| **compact\_interval\_days** _optional_            | Use \`\` property to define the interval between scheduled compaction runs (in days). Set a zero (0) value to suppress running compactions. Change initiates a database restart.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | number                                                               |
| **delta\_sync** _optional_                        | _NOTE:_ Delta Sync is an Enterprise Edition feature on Sync Gateway and Couchbase Lite. Use the delta\_sync object to specify the delta sync configuration properties. In this context, delta-sync, is the ability to replicate only those parts of a Couchbase mobile document that have changed. This results in significant savings in bandwidth consumption as well as throughput improvements; both useful benefits when network bandwidth is typically constrained. Delta Sync does not apply to attachment contents. Delta Sync is disabled by default on the Sync Gateway. You can enable it through the enabled property. If delta sync is enabled on Sync Gateway, then Couchbase Lite clients will switch to using delta sync automatically. Similarly, if delta sync is disabled on Sync Gateway, clients will switch to normal mode. Changes initiate a database reload                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | [Delta Sync](#%5Fdelta%5Fsync)                                       |
| **enable\_shared\_bucket\_access** _optional_     | Use the enable\_shared\_bucket\_access property to define whether to use extended attributes to store sync metadata. This is required to enable mobile-to-server data sync (_mobile convergence_). You can learn more about this functionality in [Syncing with Couchbase Server](sync-with-couchbase-server.html) This property works in conjunction with the import\_docs property, which determines whether a node participates in import processing. Leave enable\_shared\_bucket\_access true on all nodes participating in such a configuration. On start-up, Sync Gateway will generate the mobile-specific metadata for all the pre-existing documents in the Couchbase Server bucket. From then on, documents can be inserted on the Server directly (with N1QL or SDKs) or through the Sync Gateway REST API. Change initiates a database restart **Default** : true                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | boolean                                                              |
| **event\_handlers** _optional_                    | Webhooks in Sync Gateway are designed to minimize performance impacts on Sync Gateway's regular processing. Sync Gateway manages the number of processes that are spawned for webhook event handling, so that slow response times from the HTTP POST operations don't consume available CPU resources on Sync Gateway nodes. When a webhook event handler is defined, after Sync Gateway has updated a document, Sync Gateway adds a document\_changed event to an asynchronous event-processing queue (the event queue). New processes are then spawned to apply the filter function to the documents and to perform the HTTP POST operations. When an event is not added to the event queue, but is instead discarded, a warning message is written to the the Sync Gateway log. You can configure Sync Gateway to log information about event handling, by including either the log key Event or Events+ in the Log property in your Sync Gateway configuration file. Events+ is more verbose. See also: [Webhook](webhooks.html)..                                                                                                                                                                                                                                                                                                                                                               | [Event Handler](#%5Fevent%5Fhandler)                                 |
| **guest** _optional_                              | Defines whether a GUEST user is available and able to interacted, unauthenticated, with the Public REST API                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | [guest](#%5Fdatabase%5Fmodel%5Fguest)                                |
| **import\_backup\_old\_rev** _optional_           | Use the import\_backup\_old\_rev property to define whether import should attempt to create a temporary backup of the previous revision body, when available                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | string                                                               |
| **import\_docs** _optional_                       | Use the import\_docs property to define whether the Sync Gateway node should automatically import Couchbase Server documents; This property works in conjunction with the enable\_shared\_bucket\_access property, which enables Xattrs. Since Sync Gateway 2.7, all Sync Gateway nodes can be configured as import nodes. This results in performance benefits as the import process is shared across all Sync Gateway nodes. Prior to version 2.7, import\_docs can only be set to true on a single node. Changes initiate a database restart **Default** : false                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | boolean                                                              |
| **import\_filter** _optional_                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | [Import\_filter\_model](#%5Fimport%5Ffilter%5Fmodel)                 |
| **import\_partitions** _optional_                 | Use the import\_partitions property to define how many import partitions should be used for import sharding. Partitions are distributed among all Sync Gateway nodes participating in import processing (import\_docs:true), and each process a subset of the server's vbuckets. Each partition is processed by a separate goroutine, so import\_partitions can be used to tune concurrency based on the number of Sync Gateway nodes, and the number of cores per node.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | integer                                                              |
| **isgr\_enabled** _optional_                      | Use the isgr\_enabled property to define whether this Sync Gateway node can be assigned inter-Sync Gateway replications for this database. If set to false, the Sync Gateway node will not participate in inter-Sync Gateway replications. **Default** : true                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | boolean                                                              |
| **isgr\_websocket\_heartbeat\_secs** _optional_   | If set, this duration (in seconds) is used as a custom heartbeat interval for websocket ping frames in inter-Sync Gateway replications.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | integer                                                              |
| **local\_doc\_expiry\_secs** _optional_           | Use the local\_doc\_expiry\_secs property to define an expiry value for local documents managed on Sync Gateway. Local documents are used by the Couchbase Lite replicator to track up to which sequence number a given client has synchronized and where it should resume the next time it connects to Sync Gateway. Clients failing to replicate within the expiry window are forced to restart their replication from the beginning (sequence zero). This property is intended to minimize accumulation of obsolete replication checkpoint documents in the Couchbase Server bucket. The default is 7776000 seconds (90 days).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | integer                                                              |
| **name** _optional_                               | Use name to define the Sync Gateway database name. Change initiates database restart                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | string                                                               |
| **num\_index\_replicas** _optional_               | use num\_index\_replicas property to define the number of index replicas used when creating the core Sync Gateway indexes. Only applicable if databases.$db.use\_views is set to false (default value). Change initiates a database restart.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | integer                                                              |
| **offline** _optional_                            | Use offline to determine whether Sync Gateway should start the database in offline mode. The default of false means the database will be online. **Default** : false                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | boolean                                                              |
| **oidc** _optional_                               | Use the oidc object properties to defined any OpenID Connect providers and associated credentials.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | [OIDC Group](#%5Foidc%5Fgroup)                                       |
| **old\_rev\_expiry\_seconds** _optional_          | Use the old\_rev\_expiry\_seconds property to define the number of seconds before old revisions are removed from Couchbase Server buckets.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | integer                                                              |
| **query\_pagination\_limit** _optional_           | Use the query\_pagination\_limit property to define the Query limit to be used during pagination of large queries. Change initiates a database restart.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | integer                                                              |
| **revs\_limit** _optional_                        | This property defines the maximum depth to which a document's revision tree can grow. It value governs the point at which to prune a document's revision tree. For more information see: [Revisions](revisions.html) page.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | integer                                                              |
| **send\_www\_authenticate\_header** _optional_    | Whether to send WWW-Authenticate header in 401 responses. **Default** : true                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | boolean                                                              |
| **serve\_insecure\_attachment\_types** _optional_ | The sending of a content-disposition header for attachments with headers such as "text/html" forces a download, rather than browser rendering. Use this option to suppress sending the content-disposition, allowing the browser to render the attachment. **Default** : false                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | boolean                                                              |
| **session\_cookie\_http\_only** _optional_        | This flag disallows cookies from being used by Javascript; by default javascript CAN use them **Default** : false                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | boolean                                                              |
| **session\_cookie\_name** _optional_              | Starting in Sync Gateway 2.0, it is possible to customize the session cookie name that is used for this database. This property is mostly used by web applications interacting with multiple Sync Gateway databases. Browsers typically have two methods of determining which cookie to use for a given request: the URL path, or the cookie name. Use this property, to set different cookie names for each database specified in the configuration file. Let's consider the following configuration file: \[source,json\] ---- { "databases": { "db1": { "session\_cookie\_name": "CustomName1", "bucket": "bucket-1" }, "db2": { "session\_cookie\_name": "CustomName2", "bucket": "bucket-2" } } } } \---- With this configuration, the Set-Cookie response header of the POST :4984/{db}/\_session endpoint (Public REST API) would then have the form "CustomName1=3cad4b95524179bf144fe0d92b8f09877bb86bf5;path=/db1/". When using POST :4985/{db}/\_session (Admin REST API) to create a session, the cookie value is returned in the response body instead of the Set-Cookie header. In this case, it could also be set by the client, for web applications it would be the following in JavaScript: \[source,javascript\] ---- cookie1String = "CustomName1=3cad4b95524179bf144fe0d92b8f09877bb86bf5;path=/db1/"; document.cookie = cookie1String; ---- **Default** : "SyncGatewaySession" | string                                                               |
| **session\_cookie\_secure** _optional_            | Override secure cookie flag (that is, disable secure cookies). If SSLCert is set, then secure cookies are also used by default. However, this flag can be set false to override this behavior and allow insecure cookies to be used alongside SSL. If SSLCert is not set then this flag defaults to false. **Default** : true                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | boolean                                                              |
| **slow\_query\_warning\_threshold** _optional_    | The maximum wait time, in milliseconds,for N1QL or View queries made by Sync Gateway Log warnings if the run time of a N1QL or View query, made by Sync Gateway, exceeds this value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | integer                                                              |
| **sync** _optional_                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | [Sync\_model](#%5Fsync%5Fmodel)                                      |
| **unsupported** _optional_                        | This group comprises an unrelated collection of unsupported properties that may, potentially, be useful in controlled testing scenarios. NOTE: Due to the unsupported nature of these options, there is no guarantee on their continued availability.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | [Unsupported Properties Model](#%5Funsupported%5Fproperties%5Fmodel) |
| **use\_views** _optional_                         | If set to true, Sync Gateway will use views instead of GSI for system functions like authentication and replication. **Default** : false                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | boolean                                                              |
| **user\_xattr\_key** _optional_                   | The user\_xattr\_key identifies the user xattr used to hold the channel access grants for documents in this database. If it is not specified or its value is spaces or null then this feature is disabled (default). If you change the value of this key, no existing grant assignments will be changed until a document mutation is triggered. This can be done in a number of ways: - a mutation to the document which we'll see via DCP - an on-demand import either through write or get - by using the resync function. _Dependencies:_The user\_xattr\_key feature requires that – \* enable\_shared\_bucket\_access be = true \* xattrs be supported on the connected Couchbase Server Change initiates a database restart **Default** : "none"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | string                                                               |
| **view\_query\_timeout\_secs** _optional_         | Use the view\_query\_timeout\_secs property to define the view query timeout in seconds. This is the time Sync Gateway should wait for a view query response from Couchbase Server before it times out. The timeout applies to both view and N1QL queries issued by Sync Gateway.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | integer                                                              |

**Cache**

| Name                          | Description                                                                                                             | Schema                                 |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| **channel\_cache** _optional_ | Use the channel\_cache group's properties to configure the database's channel cache Changes initiate a database restart | [Channel Cache](#%5Fchannel%5Fcache)   |
| **rev\_cache** _optional_     | Use the rev\_cache properties to configure the revision cache                                                           | [Revision Cache](#%5Frevision%5Fcache) |

**Channel Cache**

| Name                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Schema  |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **compact\_high\_watermark\_pct** _optional_ | Use compact\_high\_watermark\_pct to define the trigger value for starting channel cache eviction. Specify the value as a percentage (of max\_number) When the cache size, determined by max\_number, reaches the high watermark, the eviction process iterates through the cache, removing inactive channels.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | integer |
| **compact\_low\_watermark\_pct** _optional_  | Use compact\_low\_watermark\_pct to define the trigger value for stopping channel cache eviction. Specify the value as a percentage (of max\_number) When the cache size, determined by max\_number returns to a value lower than compact\_low\_watermark\_pct, the cache eviction process is stopped.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | integer |
| **enable\_star\_channel** _optional_         | Use enable\_star\_channel to define whether Sync GAteway should use the all documents (\*) channel - sometimes referred to as the 'star' channel. **Default** : true                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | boolean |
| **expiry\_seconds** _optional_               | Use expiry\_seconds to define how long (in seconds) Sync Gateway should keep cached entries beyond the minimum retained.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | integer |
| **max\_length** _optional_                   | Maximum number of entries maintained in cache per channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | integer |
| **max\_num\_pending** _optional_             | Use max\_num\_pending to define the maximum number of pending sequences before skipping the sequence.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | integer |
| **max\_number** _optional_                   | Use max\_number to define the maximum number of channel caches allowed at any one point. This property is used alongside the associated eviction watermarks compact\_low\_watermark\_pct and compact\_high\_watermark\_pct to control the cache size. The default value for this property is 50000\. Assuming the default channel min\_length and max\_length values, this would result in a memory usage under 1GB. Tuning this property is an [Enterprise Edition](https://www.couchbase.com/products/editions) feature - in the Community Edition any change to the default value is ignored. _Enterprise Edition Only_: The max\_number value can be tuned to optimize for cache hits (requests that are handled using the cache), as opposed to cache misses (requests that require a round-trip to Couchbase Server to fetch data). The cache hit/miss ratio can be obtained with the following: cache hit/miss ratio \= cache.chan\_cache\_hits / cache.chan\_cache\_misses Increasing the max\_number value can increase the cache hit/miss ratio, resulting in better cache utilization. If the cache size grows to reach the high watermark (compact\_high\_watermark\_pct), channels with no connected replications will be evicted before channels which are associated with an active pull replication (i.e a blip-based pull replication in Couchbase Lite 2.x, or an active /{db}/\_changes request in Couchbase Lite 1.x). The minimum allowed value is 100. It isn't possible to remove the limit altogether, users who wish to remove the limit would need to set max\_number to an arbitrarily high value. | integer |
| **max\_wait\_pending** _optional_            | Maximum wait time in milliseconds for a pending sequence before skipping sequences.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | integer |
| **max\_wait\_skipped** _optional_            | Maximum wait time in milliseconds for a skipped sequence before abandoning the sequence.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | integer |
| **min\_length** _optional_                   | Minimum number of entries maintained in cache per channel.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | integer |
| **query\_limit** _optional_                  | Limit used for channel queries                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | integer |

**Revision Cache**

| Name                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Schema  |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **shard\_count** _optional_ | Tuning this property is an [Enterprise Edition](https://www.couchbase.com/products/editions) feature. The Community Edition is configured with the default value, and will ignore any value in the configuration file. Number of shards the rev cache should be split into. More shards allows for lower cache contention when accessing distinct revisions, at the cost of some memory overhead per-shard. This generally should not greatly exceed the number of CPU threads available to Sync Gateway. It is generally not recommended to set this property, unless advised by Couchbase [Enterprise Support](https://www.couchbase.com/support-policy).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | integer |
| **size** _optional_         | Size of the revision cache, specified as the total number of document revisions to cache in memory for all recently accessed documents. When the revision cache is full, Sync Gateway removes less recent document revisions to make room for new document revisions. Adjust this property to tune memory consumption by Sync Gateway, for example on servers with less memory and in cases when Sync Gateway creates many new documents and/or updates many documents relative to the number of read operations. _Disabling the revision cache_ Disabling the revision cache is an [Enterprise Edition](https://www.couchbase.com/products/editions) feature. To disable the revision entirely, set this property to 0\. Setting this property to 0 on the Community Edition is ignored. Disabling the revision cache would be useful when there are very large documents or if you expect a very low cache hit rate. Otherwise it could negatively impact the latency of replications. It is generally not recommended to disable the revision cache, unless advised by Couchbase [Enterprise Support](https://www.couchbase.com/support-policy). | integer |

**Delta Sync**

| Name                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Schema  |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **enabled** _optional_                | Use the delta\_sync.enabled property to turn delta sync mode on or off for the given database. The following configuration example enables delta sync. \[source,json\] ---- { "databases": { "db": { "delta\_sync": { "enabled": true, "rev\_max\_age\_seconds": 86400 } } } } ---- Footnotes \* Use of Delta Sync incurs additional bucket storage requirements which can be tuned with the [rev\_max\_age\_seconds](#databases-this%5Fdb-delta%5Fsync-rev%5Fmax%5Fage%5Fseconds) property. \* Delta Sync is automatically enabled for peer-to-peer sync between Couchbase Lite clients. \* Delta sync is disabled for Couchbase Lite database replicas. \* Push replications do not use Delta Sync when pushing to a pre-2.8 target. **Default** : false                                                                                                                                                                                                                                        | boolean |
| **rev\_max\_age\_seconds** _optional_ | Use delta\_sync.rev\_max\_age\_seconds to adjust the time box within which deltas can be generated. On a write operation, the revision body is backed up in the bucket and retained for rev\_max\_age\_seconds to calculate future revision deltas. As a result, new deltas can only be generated for read requests that come in within the rev\_max\_age\_seconds time window. The storage of backed up revision bodies for delta sync incurs additional bucket storage requirements. The additional storage can be calculated with the following formula: (doc\_size \* updates\_per\_day \* 86400) / rev\_max\_age\_seconds. For example, with rev\_max\_age\_seconds's default value, an average document size of 4 KB and 100 writes/day, enabling delta sync would take up an additional 400 KB of storage on Couchbase Server ((4 \* 100 \* 86400)/86400\`). Setting this value to 0 will generate deltas opportunistically on pull replications, with no additional storage requirements. | integer |

**Event Handler**

| Name                              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Schema                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| **db\_state\_changed** _optional_ | Use the db\_state\_changed property group to define the actions to perform when a db\_state change is detected.                                                                                                                                                                                                                                                                                                                                                                                 | [db\_state\_changed model](#%5Fdb%5Fstate%5Fchanged%5Fmodel) |
| **document\_changed** _optional_  | The configuration for the action to perform when a document change is detected.                                                                                                                                                                                                                                                                                                                                                                                                                 | [Document Changed](#%5Fdocument%5Fchanged)                   |
| **max\_processes** _optional_     | Maximum number of events that can be processed concurrently, that is, no more than max\_processes concurrent processes will be spawned for event handling. The default value should work well in the majority of cases. You should not need to adjust it to tune performance. However, if you wish to ensure that most webhook posts are sent, you can set it to sufficiently high value.                                                                                                       | integer                                                      |
| **wait\_for\_process** _optional_ | Maximum wait time in milliseconds before canceling event processing for an event that is detected when the event queue is full. If you set the value to 0 (zero), then incoming events are discarded immediately if the event queue is full. If you wish to avoid any blocking of standard Sync Gateway processing this may be a desirable value to use. The default value should work well in the majority of cases. You should not need to adjust it to tune performance. **Default** : "100" | string                                                       |

**db\_state\_changed model**

| Name                   | Description                                                                                                    | Schema  |
| ---------------------- | -------------------------------------------------------------------------------------------------------------- | ------- |
| **filter** _optional_  | Use db\_state\_changed.filter\`\` to define a JavaScript function that determines which state changes to post. | string  |
| **handler** _optional_ | Specify the type of event handler. This must be webhook currently).                                            | string  |
| **options** _optional_ | Options can be specified per-handler, and are specific to each handler type.                                   | string  |
| **timeout** _optional_ | Defines the period in seconds to wait for a response to the operation. Default: 60                             | integer |
| **url** _optional_     | Defines the URL to post to (for a webhook event handler).                                                      | string  |

**Document Changed**

| Name                   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Schema  |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **filter** _optional_  | Use document\_changed.filter to define a JavaScript function that determines which documents to post. The filter function accepts the document body as input and returns a boolean value. \* If the filter function returns true, then Sync Gateway posts the document. \* If the filter function returns false, then Sync Gateway does not post the document. \* If no filter function is defined, then Sync Gateway posts all changed documents. Filtering only determines which documents to post. It does not extract specific content from documents and post only that. | string  |
| **handler** _optional_ | Specify the type of event handler. This must be webhook currently).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | string  |
| **options** _optional_ | Options can be specified per-handler, and are specific to each handler type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | string  |
| **timeout** _optional_ | Defines the period in seconds to wait for a response to the POST operation. Using a timeout ensures that slow-running POST operations don't cause the webhook event queue to back up. Slow-running POST operations are discarded (if they time out), so that new events can be processed. When the timeout is reached, Sync Gateway stops listening for a response. A value of 0 (zero) means no timeout. You should not need to adjust it to tune performance as he default value should work well in the majority of cases.                                                 | integer |
| **url** _optional_     | Defines the URL to post documents to (for a webhook event handler).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | string  |

**guest**

| Name                    | Description                                                                                                                                                                                                    | Schema  |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **disabled** _optional_ | Set disabled \= false to allow GUEST For example: curl -X PUT username:password@localhost:4985/db/\_config -H "Content-Type: application/json" --data-binary '{"guest": {"disabled":false}} **Default** : true | boolean |

**OIDC Group**

| Name                             | Description                                                                                                                                                                                                                                                                                                                                                    | Schema                                 |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- |
| **default\_provider** _optional_ | Use this default\_provider property to identify the provider to use for OIDC requests that do not specify a provider. If only one provider is specified in the providers map, then that is used as the default provider. If multiple providers are defined and default\_provider is not specified, requests to /db/\_oidc must specify the provider parameter. | string                                 |
| **providers** _optional_         | Include an entry for each OIDC provider                                                                                                                                                                                                                                                                                                                        | [OIDC Providers](#%5Foidc%5Fproviders) |

**OIDC Providers**

| Name                          | Schema                               |
| ----------------------------- | ------------------------------------ |
| **this\_provider** _optional_ | [OIDC Provider](#%5Foidc%5Fprovider) |

**OIDC Provider**

Name

Description

Schema

**allow\_unsigned\_provider\_tokens**  
_optional_

Unsigned provider tokens are not accepted.

Set `"allow_unsigned_provider_tokens": true` to opt-in to accepting unsigned tokens from providers.  
**Default** : `false`

boolean

**callback\_url**  
_optional_

The callback URL to be invoked after the end-user obtains a client token. When not provided, Sync Gateway will generate it based on the incoming request.

_Optional_

string

**client\_id**  
_optional_

The client ID defined in the provider for Sync Gateway.

string

**disable\_callback\_state**  
_optional_

DisableCallbackState determines whether or not to maintain state between the `/_oidc` and `/_oidc_callback` endpoints.

Disabling this action is NOT recommended as it will increase vulnerability to Cross-Site Request Forgery (CSRF, XSRF).

Set `"disable_callback_state": true` to switch-off callback state.  
**Default** : `false`

boolean

**disable\_cfg\_validation**  
_optional_

Couchbase Sync Gateway, by default, applies strict validation of the OpenID Connect configuration based on the OIDC specification.

Set `"disable_cfg_validation": true` when you do not want strict validation of the OIDC configuration.  
**Default** : `false`

boolean

**disable\_session**  
_optional_

By default, Sync Gateway will create a new session for the user upon successful OIDC authentication, and set that session in the usual way on the oidc\_callback and \_oidc\_refresh responses. 

If disable\_session is set to true, the session is not created (clients must use the ID token for subsequent authentications).

\_Optional

string

**discovery\_url**  
_optional_

Optional. Discovery URL used to obtain the OpenID Connect provider configuration. If not specified, the default discovery endpoint of \[issuer\]/.well-known/openid-configuration will be used.

string

**include\_access**  
_optional_

Optional. When true, the oidccallback response will include the access\_token, expires\_at and token\_type properties returned by the OP.

string

**issuer**  
_optional_

The OpenID Connect Provider issuer.

string

**register**  
_optional_

Whether Sync Gateway should automatically create users for successfully authenticated users that don't have an already existing user in Sync Gateway.

Optional.

string

**scope**  
_optional_

By default, Sync Gateway uses the scope "openid email" when calling the OP's authorize endpoint.

If the scope property is defined in the config (as an array of string values), it will override this scope.

\*Optional. \*

string

**user\_prefix**  
_optional_

Optional. Specifies the prefix for Sync Gateway usernames for the provider. When not specified, defaults to issuer.

string

**username\_claim**  
_optional_

You can use `username_claim` to specify a claim other than subject to use as the Sync Gateway username.

The specified claim must be a string, as numeric claims may be un-marshalled inconsistently between Sync Gateway and the underlying OIDC library.

When authenticating incoming OIDC tokens, Sync Gateway currently treats the username as \[subject\]. By default user\_prefix is the issuer, but can be customized in the Sync Gateway provider config. Subject is always the sub claim in the token. 

Behavior:

\* If username\_claim is set but user\_prefix is not set, use that claim as the Sync Gateway username.

\* If username\_claim is set and user\_prefix is also set, use \[user\_prefix\]\[username\_claim\] as the Sync Gateway username.

\* If username\_claim is not set and user\_prefix is set, use \[subject\] as the Sync Gateway username (existing behavior). 

\* If neither username\_claim nor user\_prefix are set, use \[issuer\]\[subject\] as the Sync Gateway username (existing behavior).  
**Default** : `"optional"`

string

**validation\_key**  
_optional_

Client secret associated with the client. Required for auth code flow.

string

**Unsupported Properties Model**

| Name                                             | Description                                                                                                                                                                                            | Schema                                                                |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------- |
| **api\_endpoints** _optional_                    |                                                                                                                                                                                                        | [api\_endpoints](#%5Fdatabase%5Fmodel%5Fapi%5Fendpoints)              |
| **disable\_clean\_skipped\_query** _optional_    | Clean skipped sequence processing bypasses final check                                                                                                                                                 | boolean                                                               |
| **oidc\_test\_provider** _optional_              | Config settings for OIDC test provider                                                                                                                                                                 | [oidc\_test\_provider](#%5Fdatabase%5Fmodel%5Foidc%5Ftest%5Fprovider) |
| **oidc\_tls\_skip\_verify** _optional_           | Unsupported option for use in development and testing environment ONLY oidc\_tls\_skip\_verify can be used to enable the use of self-signed certs for OpenID Connection testing. **Default** : false   | boolean                                                               |
| **remote\_config\_tls\_skip\_verify** _optional_ | Unsupported option for use in development and testing environment ONLY Use only to enable self signed certificates for testing external JavaScript load. **Default** : false                           | boolean                                                               |
| **sgr\_tls\_skip\_verify** _optional_            | Unsupported option for use in development and testing environment ONLY sgr\_tls\_skip\_verify can be used to skip validation of TLS certs used for Inter-Sync Gateway Replication. **Default** : false | boolean                                                               |
| **user\_views** _optional_                       | Configuration settings for user views                                                                                                                                                                  | [user\_views](#%5Fdatabase%5Fmodel%5Fuser%5Fviews)                    |
| **warning\_thresholds** _optional_               |                                                                                                                                                                                                        | [Warning Threshold](#%5Fwarning%5Fthreshold)                          |

**api\_endpoints**

| Name                                            | Description                                                                                                                                                                               | Schema  |
| ----------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **enable\_couchbase\_bucket\_flush** _optional_ | Determines whether Couchbase buckets can be flushed using the Admin REST API. Use _only_ for testing purposes if it is necessary to flush data in between tests to start with a clean DB. | boolean |

**oidc\_test\_provider**

| Name                   | Description                                                                                                                                                       | Schema  |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **enabled** _optional_ | Unsupported option for use in development and testing environment ONLY Determines whether the oidc\_test\_provider endpoints should be exposed on the public API. | boolean |

**user\_views**

| Name                                | Description                                                                                                                                             | Schema  |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **user\_views\_enabled** _optional_ | Unsupported option for use in development and testing environment ONLY Use to determine whether pass-through view query is supported through public API | boolean |

**Warning Threshold**

| Name                                               | Description                                                                                      | Schema  |
| -------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ------- |
| **access\_and\_role\_grants\_per\_doc** _optional_ | Number of access and role grants per document to be used as a threshold for grant count warnings | boolean |
| **channel\_name\_size** _optional_                 | Number of channel name characters to be used as a threshold for channel name warnings            | boolean |
| **channels\_per\_doc** _optional_                  | Number of channels per document to be used as a threshold for channel count warnings             | boolean |
| **channels\_per\_user** _optional_                 | Number of channels per user to be used as a threshold for channel count warnings                 | boolean |
| **xattr\_size\_bytes** _optional_                  | Number of bytes to be used as a threshold for XATTR size limit warnings                          | boolean |

### [](#%5Fimport%5Ffilter%5Fmodel)Import\_filter\_model

The `import_filter` controls whether a document written to the Couchbase Server bucket should be made available to Couchbase Mobile clients (that is, whether it ought to be imported).

You should provision the filter as a Javascript function in the request body of a call to the Admin Rest API endpoint `put {db}/_config/import_filter`.

Set the header's content type to `content-Type: application/javascript`.

The function takes the document body as parameter and is expected to return a boolean to indicate whether the document should be imported.

If you do not provide a filter function then no filter will be applied and ALL documents will be imported.

_Type_ : string

### [](#%5Frole%5Fmodel)Role\_model

Use the `role` property to define a Sync Gateway role

| Name                           | Description                                                                                                                                          | Schema           |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| **admin\_channels** _optional_ | Array of channel names the role allows access to                                                                                                     | < string > array |
| **all\_channels** _optional_   | Lists all the channels the role has access to including any assigned by the sync function. This is a derived property and changes to it are ignored. | < string > array |
| **name** _required_            | Name of the role                                                                                                                                     | string           |

### [](#%5Frole%5Fand%5Fuser%5Fmodel)Role\_and\_User\_model

| Name                | Schema                          |
| ------------------- | ------------------------------- |
| **Role** _optional_ | [Role\_model](#%5Frole%5Fmodel) |
| **User** _optional_ | [User\_model](#%5Fuser%5Fmodel) |

### [](#%5Fsync%5Fmodel)Sync\_model

The `sync` property is a Javascript function that determines which users can access which documents.

This JavaScript function is provisioned using the Admin Rest API Endpoint `put /{db}/_config/sync`

Add the function as plain javascript in the request body, with the `content-Type: application/javascript` header.

_Type_ : string

### [](#%5Fuser%5Fmodel)User\_model

Definition of a Sync Gateway user

Change initiates database restart

| Name                           | Description                                                                                                                                                                                                                                                                                            | Schema           |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------- |
| **admin\_channels** _optional_ | The channels that the user is able to access.                                                                                                                                                                                                                                                          | < string > array |
| **admin\_roles** _optional_    | An array of the roles this user is associated with.                                                                                                                                                                                                                                                    | < string > array |
| **all\_channels** _optional_   | Shows the channels the user can access, as granted by the sync function. This is a read-only property. Changes to it are ignored.                                                                                                                                                                      | < string > array |
| **disabled** _optional_        | This property is usually not included. If the value is true, access for the account is disabled and the user will not be able to login.                                                                                                                                                                | boolean          |
| **email** _optional_           | Email address of the user.                                                                                                                                                                                                                                                                             | string           |
| **name** _required_            | The user name (the same name used in the URL path). The valid characters for a user name are alphanumeric ASCII characters and the underscore character. The name property is required in a POST request. You don't need to include it in a PUT request because the user name is specified in the URL. | string           |
| **password** _optional_        | Password of the user. Mandatory, unless allow\_empty\_password=true.                                                                                                                                                                                                                                   | string           |
| **roles** _optional_           | Shows the roles this user is associated with by the Sync function. This is a read-only property. Changes to it are ignored.                                                                                                                                                                            | < string > array |

### [](#%5Fuser-response)User-response

| Name                           | Description                                                                                                                             | Schema           |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| **admin\_channels** _optional_ | The channels that the user is able to access.                                                                                           | < string > array |
| **all\_channels** _optional_   | Shows the channels the user can access, as granted by the sync function.                                                                | < string > array |
| **disabled** _optional_        | This property is usually not included. If the value is true, access for the account is disabled and the user will not be able to login. | boolean          |
| **email** _optional_           | Email address of the user.                                                                                                              | string           |
| **name** _optional_            | The user name (the same name used in the URL path).                                                                                     | string           |

### [](#%5Falldatabases)AllDatabases

List of available databases in cluster

_Type_ : < string > array

### [](#%5Factivetasks%5Fmodel)ActiveTasks\_model

| Name                                | Description                                                                                                                                                                                                                                                                                                       | Schema  |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **continuous** _optional_           | Whether the replication is continuously monitoring for changes on the source database to send them to the target.                                                                                                                                                                                                 | boolean |
| **direction** _optional_            | Inter-Sync Gateway Replication (v1) is uni-directional; valid values are **push** or **pull**.                                                                                                                                                                                                                    | string  |
| **doc\_write\_failures** _optional_ | The number of docs that have failed to be written (pushed) to the target database. These docs will not be retried.                                                                                                                                                                                                | integer |
| **docs\_read** _optional_           | The number of docs that have been read (fetched) from the source database.                                                                                                                                                                                                                                        | integer |
| **docs\_written** _optional_        | The number of docs that have been written (pushed) to the target database.                                                                                                                                                                                                                                        | integer |
| **end\_last\_seq** _optional_       | _Deprecated_ The most recent last\_seq value received from the source database during replication. Use the **last\_seq\_push** and **last\_seq\_pull** values instead.                                                                                                                                            | integer |
| **is\_persistent** _optional_       | flag to distinguish between the persistent and adhoc replications                                                                                                                                                                                                                                                 | boolean |
| **last\_seq\_pull** _optional_      | The last seq number pulled from the source to target. The last\_seq\_pull result can be used by apps to determine if a specific document has been synced to target or not. Do this by querying the **\_raw** endpoint and comparing the sequence number of document with the last\_seq value that was replicated. | integer |
| **last\_seq\_push** _optional_      | The last seq number pushed from the source to target. The last\_seq\_push result can be used by apps to determine if a specific document has been synced to target or not. Do this by querying the **\_raw** endpoint and comparing the sequence number of document with the last\_seq value that was replicated. | integer |
| **replication\_id** _optional_      | The replication Id.                                                                                                                                                                                                                                                                                               | string  |
| **source** _optional_               | The URL of the source database (i.e "<http://example.com:4985/source">;).                                                                                                                                                                                                                                         | string  |
| **status** _optional_               | Stopped / running These will be **adhoc** replications (running) or persistent replications (stopped or running).                                                                                                                                                                                                 | string  |
| **target** _optional_               | The URL of the target database (i.e "<http://example.com:4985/target">;).                                                                                                                                                                                                                                         | string  |

### [](#%5Fdocmetadata)DocMetadata

| Name                  | Schema                           |
| --------------------- | -------------------------------- |
| **\_sync** _optional_ | [\_sync](#%5Fdocmetadata%5Fsync) |

**\_sync**

| Name                             | Description                             | Schema                               |
| -------------------------------- | --------------------------------------- | ------------------------------------ |
| **history** _optional_           |                                         | [history](#%5Fdocmetadata%5Fhistory) |
| **parents** _optional_           |                                         | < integer > array                    |
| **recent\_sequences** _optional_ |                                         | < integer > array                    |
| **rev** _optional_               | Revision number of the current revision | string                               |
| **sequence** _optional_          | Sequence number of this document        | integer                              |

**history**

| Name                       | Description                      | Schema            |
| -------------------------- | -------------------------------- | ----------------- |
| **channels** _optional_    |                                  | < string > array  |
| **parents** _optional_     |                                  | < integer > array |
| **revs** _optional_        |                                  | < string > array  |
| **time\_saved** _optional_ | Timestamp of the last operation? | string            |

### [](#%5Ferror)Error

| Name                   | Schema          |
| ---------------------- | --------------- |
| **code** _optional_    | integer (int32) |
| **fields** _optional_  | string          |
| **message** _optional_ | string          |

### [](#%5Fsgcollectinfostats)SGCollectInfoStats

| Name                  | Description                           | Schema |
| --------------------- | ------------------------------------- | ------ |
| **status** _optional_ | The current status of sgcollect\_info | string |

### [](#%5Fexpvars)ExpVars

| Name                                    | Description                                                                     | Schema                                                              |
| --------------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| **cb** _optional_                       | Variables reported by the Couchbase SDK (go\_couchbase package)                 | object                                                              |
| **cmdline** _optional_                  | Built-in variables from the Go runtime, lists the command-line arguments        | object                                                              |
| **mc** _optional_                       | Variables reported by the low-level memcached API (gomemcached package)         | object                                                              |
| **memstats** _optional_                 | Dumps a large amount of information about the memory heap and garbage collector | object                                                              |
| **syncGateway\_changeCache** _optional_ |                                                                                 | [syncGateway\_changeCache](#%5Fexpvars%5Fsyncgateway%5Fchangecache) |
| **syncGateway\_db** _optional_          |                                                                                 | [syncGateway\_db](#%5Fexpvars%5Fsyncgateway%5Fdb)                   |
| **syncgateway** _optional_              | Monitoring stats                                                                | [syncgateway](#%5Fexpvars%5Fsyncgateway)                            |

**syncGateway\_changeCache**

| Name                            | Description                                                          | Schema |
| ------------------------------- | -------------------------------------------------------------------- | ------ |
| **lag-queue-0000ms** _optional_ | Histogram of delay from Tap feed till doc is posted to changes feed  | object |
| **lag-tap-0000ms** _optional_   | Histogram of delay from doc save till it shows up in Tap feed        | object |
| **lag-total-0000ms** _optional_ | Histogram of total delay from doc save till posted to changes feed   | object |
| **maxPending** _optional_       | Max number of sequences waiting on a missing earlier sequence number | object |
| **outOfOrder** _optional_       | Number of out-of-order sequences posted                              | object |
| **view\_queries** _optional_    | Number of queries to channels view                                   | object |

**syncGateway\_db**

| Name                                       | Description                                                                                           | Schema |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------- | ------ |
| **channelChangesFeeds** _optional_         | Number of calls to db.changesFeed, i.e. generating a changes feed for a single channel.               | object |
| **channelLogAdds** _optional_              | Number of entries added to channel logs                                                               | object |
| **channelLogAppends** _optional_           | Number of times entries were written to channel logs using an APPEND operation                        | object |
| **channelLogCacheHits** _optional_         | Number of requests for channel-logs that were fulfilled from the in-memory cache                      | object |
| **channelLogRewriteCollisions** _optional_ | Number of collisions while attempting to rewrite channel logs using SET                               | object |
| **channelLogRewrites** _optional_          | Number of times entries were written to channel logs using a SET operation (rewriting the entire log) | object |
| **document\_gets** _optional_              | Number of times a document was read from the database                                                 | object |
| **revisionCache\_adds** _optional_         | Number of revisions added to the revision cache                                                       | object |
| **revisionCache\_hits** _optional_         | Number of times a revision-cache lookup succeeded                                                     | object |
| **revisionCache\_misses** _optional_       | Number of times a revision-cache lookup failed                                                        | object |
| **revs\_added** _optional_                 | Number of revisions added to the database (including deletions)                                       | object |
| **sequence\_gets** _optional_              | Number of times the database's lastSequence was read                                                  | object |
| **sequence\_reserves** _optional_          | Number of times the database's lastSequence was incremented                                           | object |

**syncgateway**

| Name                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Schema                                                         |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **global** _optional_           | Global Sync Gateway stats                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [global](#%5Fexpvars%5Fglobal)                                 |
| **per\_db** _optional_          | This array contains stats for all databases declared in the config file - see the [Sync Gateway Statistics Schema](stats-monitoring.html) for more details on the metrics collected and reported by Sync Gateway. The statistics for each {$db\_name} database are grouped into: \* cache related statistics \* cbl\_replication\_push \* cbl\_replication\_pull \* database\_related\_statistics \* delta\_sync \* gsi\_views \* security\_related\_statistics \* shared\_bucket\_import \* per\_replication statistics for each replication\_id | < [per\_db](#%5Fexpvars%5Fper%5Fdb) \> array                   |
| **per\_replication** _optional_ | An array of stats for each replication declared in the config file **Deprecated @ 2.8**: used only by inter-sync-gateway replications version 1.                                                                                                                                                                                                                                                                                                                                                                                                  | < [per\_replication](#%5Fexpvars%5Fper%5Freplication) \> array |

**global**

| Name                                 | Description                | Schema                                                                 |
| ------------------------------------ | -------------------------- | ---------------------------------------------------------------------- |
| **resource\_utilization** _optional_ | Resource utilization stats | [resource\_utilization](#%5Fexpvars%5Fglobal%5Fresource%5Futilization) |

**resource\_utilization**

| Name                                              | Schema  |
| ------------------------------------------------- | ------- |
| **admin\_net\_bytes\_recv** _optional_            | integer |
| **admin\_net\_bytes\_sent** _optional_            | integer |
| **error\_count** _optional_                       | integer |
| **go\_memstats\_heapalloc** _optional_            | integer |
| **go\_memstats\_heapidle** _optional_             | integer |
| **go\_memstats\_heapinuse** _optional_            | integer |
| **go\_memstats\_heapreleased** _optional_         | integer |
| **go\_memstats\_pausetotalns** _optional_         | integer |
| **go\_memstats\_stackinuse** _optional_           | integer |
| **go\_memstats\_stacksys** _optional_             | integer |
| **go\_memstats\_sys** _optional_                  | integer |
| **goroutines\_high\_watermark** _optional_        | integer |
| **num\_goroutines** _optional_                    | integer |
| **process\_cpu\_percent\_utilization** _optional_ | integer |
| **process\_memory\_resident** _optional_          | integer |
| **pub\_net\_bytes\_recv** _optional_              | integer |
| **pub\_net\_bytes\_sent** _optional_              | integer |
| **system\_memory\_total** _optional_              | integer |
| **warn\_count** _optional_                        | integer |

**per\_db**

| Name                            | Schema           |
| ------------------------------- | ---------------- |
| **cache** _optional_            | object           |
| **database** _optional_         | object           |
| **per\_replication** _optional_ | < object > array |
| **security** _optional_         | object           |

**per\_replication**

| Name                            | Schema                                                                 |
| ------------------------------- | ---------------------------------------------------------------------- |
| **$replication\_id** _optional_ | [$replication\_id](#%5Fexpvars%5Fper%5Freplication%5Freplication%5Fid) |

**$replication\_id**

| Name                                                    | Description                                                                                                                                                                                                                                                                                                         | Schema  |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **sgr\_active** _optional_                              | Whether the replication is active at this time. **Deprecated @ 2.8**: used only by inter-sync-gateway replications version 1.                                                                                                                                                                                       | boolean |
| **sgr\_docs\_checked\_sent** _optional_                 | The total number of documents checked for changes since replication started. This represents the number of potential change notifications pushed by Sync Gateway. **Constraints**This is not necessarily the number of documents pushed, as a given target might already have the change. Used by versions 1 and 2. | integer |
| **sgr\_num\_attachment\_bytes\_transferred** _optional_ | The total number of attachment bytes transferred since replication started. **Deprecated @ 2.8**: used only by inter-sync-gateway replications version 1.                                                                                                                                                           | integer |
| **sgr\_num\_attachments\_transferred** _optional_       | The total number of attachments transferred since replication started. **Deprecated @ 2.8**: used only by inter-sync-gateway replications version 1.                                                                                                                                                                | integer |
| **sgr\_num\_docs\_failed\_to\_push** _optional_         | The total number of documents that failed to be pushed since replication started. Used by versions 1 and 2.                                                                                                                                                                                                         | integer |
| **sgr\_num\_docs\_pushed** _optional_                   | The total number of documents that were pushed since replication started. Used by versions 1 and 2.                                                                                                                                                                                                                 | integer |

### [](#%5Fforbidden)Forbidden

| Name                  | Description              | Schema  |
| --------------------- | ------------------------ | ------- |
| **error** _optional_  | **Default** : "conflict" | string  |
| **id** _optional_     |                          | string  |
| **reason** _optional_ |                          | string  |
| **status** _optional_ |                          | integer |

### [](#%5Flogtags)LogTags

| Name                   | Description                                                                                                                                                                                                                                                   | Schema  |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **Access** _optional_  | access() calls made by the sync function                                                                                                                                                                                                                      | boolean |
| **Attach** _optional_  | Attachment processing                                                                                                                                                                                                                                         | boolean |
| **Auth** _optional_    | Authentication                                                                                                                                                                                                                                                | boolean |
| **Bucket** _optional_  | Sync Gateway interactions with the bucket (verbose logging).                                                                                                                                                                                                  | boolean |
| **CRUD** _optional_    | Updates made by Sync Gateway to documents (CRUD+ for verbose logging)                                                                                                                                                                                         | boolean |
| **Cache** _optional_   | Interactions with Sync Gateway's in-memory channel cache (Cache+ for verbose logging)                                                                                                                                                                         | boolean |
| **Changes** _optional_ | Processing of \_changes requests (Changes+ for verbose logging)                                                                                                                                                                                               | boolean |
| **DCP** _optional_     | DCP-feed processing (verbose logging)                                                                                                                                                                                                                         | boolean |
| **Events** _optional_  | Event processing (webhooks) (Events+ for verbose logging)                                                                                                                                                                                                     | boolean |
| **Feed** _optional_    | Server-feed processing (Feed+ for verbose logging)                                                                                                                                                                                                            | boolean |
| **HTTP** _optional_    | All requests made to the Sync Gateway REST APIs (Sync and Admin). Note that the log keyword HTTP is always enabled, which means that HTTP requests and error responses are always logged (in a non-verbose manner). HTTP+ provides more verbose HTTP logging. | boolean |

### [](#%5Fpurgebody)PurgeBody

Document ID

| Name                      | Description                                                                                 | Schema              |
| ------------------------- | ------------------------------------------------------------------------------------------- | ------------------- |
| **a\_doc\_id** _optional_ | Only possible value is \["\*"\]. It permanently removes all revisions for that document ID. | < enum (\*) > array |

### [](#%5Fbulkdocssuccess)BulkDocsSuccess

| Name               | Description                | Schema |
| ------------------ | -------------------------- | ------ |
| **id** _optional_  | Design document identifier | string |
| **rev** _optional_ | Revision identifier        | string |

### [](#%5Fchangesfeedrow)ChangesFeedRow

| Name                   | Description                                                             | Schema                                             |
| ---------------------- | ----------------------------------------------------------------------- | -------------------------------------------------- |
| **changes** _optional_ | List of the document's leafs. Each leaf object contains one field, rev. | < [changes](#%5Fchangesfeedrow%5Fchanges) \> array |
| **id** _optional_      | Document identifier                                                     | string                                             |
| **seq** _optional_     | Update sequence number                                                  | integer                                            |

**changes**

| Name               | Description                                       | Schema |
| ------------------ | ------------------------------------------------- | ------ |
| **rev** _optional_ | Identifier of the document revision that changed. | string |

### [](#%5Fqueryrow)QueryRow

| Name                 | Description                                                                             | Schema |
| -------------------- | --------------------------------------------------------------------------------------- | ------ |
| **doc** _optional_   | The document body. This is only returned if include\_docs=true is specified in the URL. | object |
| **id** _optional_    | The ID of the document.                                                                 | string |
| **key** _optional_   | The key in the output row.                                                              | object |
| **value** _optional_ | The value in the output row.                                                            | object |

### [](#%5Fdesign)Design

| Name                  | Description                            | Schema          |
| --------------------- | -------------------------------------- | --------------- |
| **count** _optional_  | Total number of items available.       | integer (int32) |
| **limit** _optional_  | Number of items to retrieve (100 max). | integer (int32) |
| **offset** _optional_ | Position in pagination.                | integer (int32) |

### [](#%5Falldocs)AllDocs

| Name                | Description                                      | Schema           |
| ------------------- | ------------------------------------------------ | ---------------- |
| **keys** _optional_ | List of identifiers of the documents to retrieve | < string > array |

### [](#%5Fchanges)Changes

| Name                     | Description                                                                                   | Schema                                          |
| ------------------------ | --------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| **last\_seq** _optional_ | Last change sequence number                                                                   | object                                          |
| **results** _optional_   | List of changes to the database. See the following table for a list of fields in this object. | < [ChangesFeedRow](#%5Fchangesfeedrow) \> array |

### [](#%5Fcompact%5Fresponse)Compact\_Response

JSON Respponse to a \_compact request

| Name                               | Description                                                                                                                                                                                                                                                         | Schema  |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **compact\_id** _optional_         | Unique identifier                                                                                                                                                                                                                                                   | string  |
| **end\_time** _optional_           | Time the \_compact process ended for example "2015-09-23T17:27:17.55+01:00"                                                                                                                                                                                         | string  |
| **last\_error** _optional_         | Text of the last error message.                                                                                                                                                                                                                                     | string  |
| **marked\_attachments** _optional_ | The number of attachments marked during the mark\` phase.                                                                                                                                                                                                           | integer |
| **phase** _optional_               | This item indicates the current phase of running compact processes. It can be useful in monitoring progress. For failed processes, this indicates the phase at which a compact\_id restart will commence (where relevant). Phases include: - mark - sweep - cleanup | string  |
| **purged\_attachments** _optional_ | The number of attachments purged by the sweep phase of the \_compact process.                                                                                                                                                                                       | integer |
| **start\_time** _optional_         | Time the \_compact process started for example "2015-09-23T17:27:17.55+01:00"                                                                                                                                                                                       | string  |
| **status** _optional_              | State of the \_compact process (Running, Stopped, Completed)                                                                                                                                                                                                        | string  |

### [](#%5Fdocument%5Fmodel)Document\_model

| Name                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Schema                                                         |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **\_attachments** _optional_ | Array of attachments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | < [\_attachments](#%5Fdocument%5Fmodel%5Fattachments) \> array |
| **\_exp** _optional_         | Expiry time after which the document will be purged. The expiration time is set and managed on the Couchbase Server document (TTL is not supported for databases in walrus mode). The value can be specified in two ways; in ISO-8601 format, for example the 6th of July 2016 at 17:00 in the BST timezone would be 2016-07-06T17:00:00+01:00; it can also be specified as a numeric Couchbase Server expiry value. Couchbase Server expiries are specified as Unix time, and if the desired TTL is below 30 days then it can also represent an interval in seconds from the current time (for example, a value of 5 will remove the document 5 seconds after it is written to Couchbase Server). The document expiration time is returned in the response of GET /{db}/{doc} when show\_exp=true is included in the querystring. As with the existing explicit purge mechanism, this applies only to the local database; it has nothing to do with replication. This expiration time is not propagated when the document is replicated. The purge of the document does not cause it to be deleted on any other database. | string                                                         |
| **\_id** _optional_          | The document ID.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | string                                                         |
| **\_rev** _optional_         | Revision identifier of the parent revision the new one should replace. (Not used when creating a new document.)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | string                                                         |
| **\_revisions** _optional_   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | [\_revisions](#%5Fdocument%5Fmodel%5Frevisions)                |

**\_attachments**

| Name                            | Schema                                                       |
| ------------------------------- | ------------------------------------------------------------ |
| **attachment\_name** _optional_ | [attachment\_name](#%5Fdocument%5Fmodel%5Fattachment%5Fname) |

**attachment\_name**

| Name                         | Description                                                                                               | Schema  |
| ---------------------------- | --------------------------------------------------------------------------------------------------------- | ------- |
| **content\_type** _optional_ | The content type of the attachment.                                                                       | string  |
| **digest** _optional_        | Reference to stored attachment content                                                                    | string  |
| **length** _optional_        |                                                                                                           | integer |
| **revpos** _optional_        |                                                                                                           | integer |
| **stub** _optional_          | **Default** : true                                                                                        | boolean |
| **ver** _optional_           | Indicate that the attachment reference is made through the new reference scheme (not exposed). Value = 2. | integer |

**\_revisions**

| Name                 | Description                                                   | Schema           |
| -------------------- | ------------------------------------------------------------- | ---------------- |
| **ids** _optional_   | Array of valid revision IDs, in reverse order (latest first). | < string > array |
| **start** _optional_ | Prefix number for the latest revision.                        | integer          |

### [](#%5Fdoc-resp)doc-resp

| Name               | Description                                    | Schema  |
| ------------------ | ---------------------------------------------- | ------- |
| **id** _optional_  | Document identifier                            | string  |
| **ok** _optional_  | Indicates whether the operation was successful | boolean |
| **rev** _optional_ | Revision identifier                            | string  |

### [](#%5Fqueryresult)QueryResult

| Name                       | Description                                                                          | Schema                              |
| -------------------------- | ------------------------------------------------------------------------------------ | ----------------------------------- |
| **offset** _optional_      | Starting index of the returned rows.                                                 | string                              |
| **rows** _optional_        |                                                                                      | < [QueryRow](#%5Fqueryrow) \> array |
| **total\_rows** _optional_ | Number of documents in the database. This number is not the number of rows returned. | integer                             |

### [](#%5Freplicationresponse)ReplicationResponse

| Name                       | Description                                                | Schema  |
| -------------------------- | ---------------------------------------------------------- | ------- |
| **ok** _optional_          | Indicates whether the replication operation was successful | boolean |
| **session\_id** _optional_ | Session identifier                                         | string  |

### [](#%5Freplication%5Fmodel)Replication\_model

Data schema for the replication model

Name

Description

Schema

**adhoc**  
_optional_

" **About**

Use the Admin REST API's `adhoc` parameter to specify that a replication is ad hoc rather than persistent.

**Behavior**

Ad hoc replications behave the same as normal replications, but they are automatically removed when their status changes to stopped. This will usually be on completion, but may also be as a result of user action.

**Constraints**

This parameter is **NOT** available to configured replications; only those initialized using the Admin REST API."  
**Default** : `false`

boolean

**batch\_size**  
_optional_

**About**

Use the optional `batch_size` property to specify the number of changes to be included in a single batch during replication.

integer

**cancel**  
_optional_

**About**

Use this parameter on,y when you want to want to cancel an existing active replication.

**Constraints**

\* This parameter is **NOT** available in configured replications; only those initialized using the Admin REST API.

\* **NOTE** that the body of the request must be the same as the replication's replication definition for the cancellation request to be honoured. For example, if you requested continuous replication, the cancellation request must also contain the continuous field.  
**Default** : `false`

boolean

**conflict\_resolution\_type**  
_optional_

**About**

The **`conflict_resolution_type`** property defines the conflict resolution policy that Sync Gateway applies when resolving conflicting revisions.

The default behavior is that automatic conflict resolution policy is applied.

**Valid options**\- `default`\- `localWins`\- `remoteWins`\- `custom`

**Behavior**

\* _default_ \- Selecting `default` applies the following conflict resolution policy \* Deletes always win (the delete with longest revision history wins if both revisions are deletes) \* The revision with the longest revision history wins (so, the one with most changes and consequently the highest revision Id). \* _localWins_ \- Selecting `localWins` will result in local revisions always being the winner in any conflict.

\* _remoteWins_ \- Selecting `remoteWins` will result in remote revisions always being the winner in any conflict. \* _custom_ \- Selecting `custom` specifies that you want to handle conflict resolution with your own application logic. You **must** provide this logic as a Javascript function by specifying it in using the custom-conflict-resolver parameter.

**Example**

\---- "conflict\_resolution\_type":"remoteWins" ----

**Constraints**

\* Replications created prior to version 2.8 will default to `default`.  
**Default** : `"default"`

string

**continuous**  
_optional_

**About**

The `continuous` property specifies whether this replication will run in continuous mode.

**Behavior**

\* `continuous=true`– In continuous mode, changes are immediately synced in accordance with the replication definition. \* `continuous=false`– Detected changes are synced in accordance with the replication definition. The replication ceases once all revisions are processed.

**Constraints**

\* Optional for stops and removes  
**Default** : `false`

boolean

**custom\_conflict\_resolver**  
_optional_

**About**

The optional `custom_conflict_resolver` property specifies the Javascript function that will be used to resolve conflicts, if the custom conflict resolution type is specified in the `conflict_resolution_type`.

**Options**

The property is _mandatory_ when `conflict_resolution_type=custom` and will be ignored in all other cases.

**Using**

Provide the required logic in a Javascript function, as a string within backticks (see also the description for the `sync` function\`.

The function takes one parameter `struct` representing the conflict and comprising - the document id - the local document - the remote document

The function returns a document `struct` representing the winning revision.

**Example**

\---- "custom\_conflict\_resolver":\` function(conflict) { console.log("full remoteDoc doc: "+JSON.stringify(conflict.RemoteDocument)); return conflict.RemoteDocument; }\` ----

**Constraints**

Using complex `custom_conflict_resolver` functions can noticeably degrade performance. Use a built-in resolver whenever possible.  
**Default** : `"none"`

string

**direction**  
_optional_

**About**

The mandatory `direction` property specifies whether the replication is _push_, _pull_ or _pushAndPull_ relative to this node.

The property value is referenced by the [remote](rest-api-admin.html#database-this%5Fdb-replications-remote) property.

**Behavior**

\* `pull` \- changes are pulled from the `remote` database \* `push` \- changes are pushed to the `remote` database \* `pushAndPull` \- changes are both pushed-to and pulled-from the `remote` database

**Constraints**

Replications created prior to version 2.8 derive their _direction_ from the source/target url of the replication.

string

**enable\_delta\_sync**  
_optional_

**About**

The optional `enable_delta_sync` parameter turns on delta sync for a replication. It works in conjunction with the database level setting `delta_sync.enabled`.

**Options**

\* `"enable_delta_sync": true`, the replication can use delta sync (depending on `delta_sync.enabled` setting) \* `"enable_delta_sync": false`, the replication cannot use delta sync

**Behavior**

The optional `enable_delta_sync` parameter works in conjunction with the database level `delta_sync.enabled` setting, to determine whether this replication uses delta sync.

\* **If** `"delta_sync.enabled": true` for both databases involved in the replication, then this parameter enables or disables its use for this specific replication. \* In all other cases it has no effect and the replication runs without delta-sync.

**Constraints**

\* Applies **ONLY** to Enterprise Edition deployments. \* Depends upon the setting of the database level parameter `delta_sync.enabled`\* Replications created prior to version 2.8 must run with `"enable_delta_sync": false`\* Push replications will not use Delta Sync when pushing to a pre-2.8 target  
**Default** : `false`

boolean

**filter**  
_optional_

**About**

Use the optional filter\`property to defines the function to be used to filter documents. 

**Options**

A common value used when replicating from Sync Gateway is \`sync\_gateway/bychannel. This option limits the pull replication to a specific set of channels. You can specify the required channels using `query_params`.

**Behavior**

Works in conjunction with `query_params` to control the documents processed by the replication.

**Example**

\---- "filter":"sync\_gateway/bychannel" ----

**Constraints**

OPTIONAL for stops and removes (even if defined during creation)

string

**initial\_state**  
_optional_

**About**

The optional `initial_state` property is used to specify that the replication must be launched in 'Stopped' mode

**Behavior**

All replications are configured to start on Sync Gateway launch. So, if omitted, the state defaults to 'Running'.

Constraints\* 

Replications created prior to version 2.8 will all default to a state of 'Running'.  
Default\*\* : `"Running"`

string

**max\_backoff\_time**  
_optional_

The \*max\_backoff\_time\*property specifies the time-period (in minutes) during which Sync Gateway will attempt to reconnect lost or unreachable _remote_ targets.

On disconnection, Sync Gateway will do an exponential backoff up to the specified value, after which it will attempt to reconnect indefinitely every _max\_backoff\_time_ minutes.

If a zero value is specified, then Sync Gateway will do an exponential backoff up to an interval of five minutes before stopping the replication.

NOTE - this value defaults to five minutes for replications created prior to version 2.8.

integer

**password**  
_optional_

**About**

Use `password` to provide the login password value for the accredited user running this replication.

**Behavior**

These details are used to authenticate credentials and approve access to data.

Once provided and recorded, the password data is redacted and will not be displayed in either the configuration file or Admin REST API. A string of ****\* will be displayed in its place.** 
**Default**\* : `"mandatory"` 

string

**purge\_on\_removal**  
_optional_

**About**

The optional `purge_on_removal` property specifies, per replication, whether the removal of a `channel` triggers a purge.

**Options**\- `true` or `false`\- Default = false - Document removals are ignored by receiving end

**Behavior**

If `purge_on_removal=false`, then the removal of channels is ignored (not purged) by the receiving end.

**Constraints**

\* Applies only to PULL replications, including the PULL portion of a PUSHANDPULL replication.

\* Replications created prior to version 2.8 _must_ be run with `purge_on_removal=false`.  
**Default** : `false`

boolean

**query\_params**  
_optional_

**About**

The `query_params` property defines a set of key/value pairs used in the query string of the replication.

**Behavior**

This property works in conjunction with `filters` and `channels` to provide routing.

**Using**

You can use `` query_params’ _channels_ function to _pull_ from a specific set of `channels ``. To do so, you would also need to set the `filter` to `sync_gateway/bychannels`.

**Example**

\[source,json\] ---- "filter":"sync\_gateway/bychannel", "query\_params": { "channels":\["channel.user1"\] }, ----

**Constraints**

OPTIONAL for stops and removes (even if defined during creation)

< string > array

**remote**  
_optional_

**About**

The **remote** property represents the endpoint of a database for the remote Sync Gateway. That is, it identifies the remote Sync Gateway database that is the subject of this replication's push, pull or pushAndPull action.

Typically the endpoint will include URI, Port and Database name elements.

You can also include user credentials in the URL, in the form `<username>:<password>`. The credentials relate to an existing Sync Gateway user on the remote server.

**Example**\`"remote": "<http://user:password@example.com:4985/db1-remote">; \`

**Format**

\* a string containing a valid URL for a (remote) Sync Gateway database. \* an object whose url property contains the Sync Gateway database URL.

**Behavior**

Dependent upon setting of **direction**.

If **direction** is : - _pull_, 'remote' defines the remote cluster _from_ which data is pulled - _push_, 'remote' defines the remote cluster _to_ which data is pushed - _pushAndPull_, 'remote' defines the _push_ configuration.

**Example**

\[source,json\] ---- "remote": "http://www.example.com:4984/sample-database", ----

string

**replication\_id**  
_optional_

**About**

The _replication\_id_ property specifies either:

\* For NEW replications, the ID to be assigned to the the replication. If no _replication\_id_ is specified, Sync Gateway will assign a random UUID to new replications.

\* For existing replications, this is the ID of the required replication.

\* If **cancel=true**, this is the id of the active replication task to be cancelled.

**Constraints**

If this is specified in the body of a POST or PUT request then it must be the same value as specified in the request URL.

string

**username**  
_optional_

**About**

Use `username` to provide the name of the accredited user running this replication.

**Behavior**

These details are used to authenticate credentials and approve access to data

Once provided and recorded, the username data is redacted and will not be displayed in either the configuration file or Admin REST API. A string of ****\* will be displayed in its place.** 
**Default**\* : `"Mandatory"` 

string

### [](#%5Freplicationstatusresponsebody)ReplicationStatusResponseBody

| Name                                | Description                                                                                                                                                                                                                                                                                                                                         | Schema  |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **config** _optional_               | This optional response content is returned only when using the {querystring} option with includeConfig=true. For example, \---- GET <http://localhost:4985/db-local/%5FreplicationStatus?includeError=true&includeConfig=true>\---- It comprises the replication definition as would be returned using a GET request to the \_replication endpoint. | object  |
| **delta\_recv** _optional_          | The number of delta-sync changes sent                                                                                                                                                                                                                                                                                                               | integer |
| **delta\_requested** _optional_     | The number of delta-sync changes requested. This should always be non-zero when delta\_sync.enabled is true.                                                                                                                                                                                                                                        | integer |
| **delta\_sent** _optional_          | This is the number of deltas sent. Whether or not deltas are sent and-or received is based on whether the remote: \* has deltas enabled, and-or \* can generate a delta for the requested revision.                                                                                                                                                 | integer |
| **doc\_write\_conflict** _optional_ | The number of docs that were in conflict.                                                                                                                                                                                                                                                                                                           | integer |
| **doc\_write\_failures** _optional_ | The number of docs that have failed to be written (pushed) to the target database. These docs will not be retried.                                                                                                                                                                                                                                  | integer |
| **docs\_purged** _optional_         | The number of docs that have been purged.                                                                                                                                                                                                                                                                                                           | integer |
| **docs\_read** _optional_           | The number of docs that have been read (fetched) from the source database.                                                                                                                                                                                                                                                                          | integer |
| **docs\_written** _optional_        | The number of docs that have been written (pushed) to the target database.                                                                                                                                                                                                                                                                          | integer |
| **error\_message** _optional_       | A message describing the reason for the latest error. It is reset each Sync Gateway restart.                                                                                                                                                                                                                                                        | string  |
| **last\_seq\_pull** _optional_      | Last sequence number processed in pull replication. The last\_seq\_pull result can be used by apps to determine if a specific document has been synced to target or not. To do this, query the **\_raw** endpoint and compare the sequence number of the document with the last\_seq value (push or pull as approperiate) replicated.               | string  |
| **last\_seq\_push** _optional_      | Last sequence value processed in push replication. The last\_seq\_push result can be used by apps to determine if a specific document has been synced to target or not. To do this, query the **\_raw** endpoint and compare the sequence number of the document with the last\_seq value (push or pull as approperiate) replicated.                | string  |
| **rejected\_by\_local** _optional_  | Count of documents that were received by the local but did not get replicated because they were rejected by the sync function on the local                                                                                                                                                                                                          | integer |
| **rejected\_by\_remote** _optional_ | Count of documents that were sent to the remote but did not get replicated because they were rejected by the sync function on the remote                                                                                                                                                                                                            | integer |
| **replication\_id** _optional_      | The replication Id.                                                                                                                                                                                                                                                                                                                                 | string  |
| **status** _optional_               | The status of the replication. Valid values are: - Starting - Started - Stopping - Stopped - Error                                                                                                                                                                                                                                                  | string  |

### [](#%5Fresync-response)Resync-response

| Name                          | Description                                                                                                                                                                                                        | Schema  |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------- |
| **docs\_changed** _optional_  | Shows the number of documents that have been changed as a result of the sync function. Docs are only changed if when run through the new sync function the resulting doc is different to the currently stored doc. | integer |
| **docs\_procesed** _optional_ | Shows the number of documents that have been run through the sync function.                                                                                                                                        | integer |
| **last\_error** _optional_    | Will ONLY be present when status = "stopped on error" In the event of an error in the \_resync process this field will contain error details. Otherwise it is not visible.                                         | string  |
| **start\_time** _optional_    | The \_resync process start time in ISO 8601 format (for example: 2012-04-23T18:25:43.511Z)                                                                                                                         | string  |
| **status** _optional_         | Indicates the status of the resync operation. Possible values: \* running, \* stopped, \* stopping, \* stopped on error                                                                                            | string  |

### [](#%5Fserver)Server

| Name                          | Description                                                                     | Schema |
| ----------------------------- | ------------------------------------------------------------------------------- | ------ |
| **couchdb** _optional_        | Contains the string 'Welcome' (this is required for compatibility with CouchDB) | string |
| **vendor/name** _optional_    | The server type ('Couchbase Sync Gateway)                                       | string |
| **vendor/version** _optional_ | The server version                                                              | string |
| **version** _optional_        | Sync Gateway version number                                                     | string |

### [](#%5Freplicationresponsebody)ReplicationResponseBody

This is the replication definition set returned in response to a `GET` request.

| Name                     | Description                                                                   | Schema                                                |
| ------------------------ | ----------------------------------------------------------------------------- | ----------------------------------------------------- |
| **this\_rep** _optional_ | This is the replication definition set returned in response to a GET request. | [this\_rep](#%5Freplicationresponsebody%5Fthis%5Frep) |

**this\_rep**

Name

Description

Schema

**adhoc**  
_optional_

Indicates whether this replication is ad hoc (`"adhoc": true`) or Persistent. Both replications behave in the same way, except that **adhoc** replications are automatically removed when their status changes to **stopped**. This will usually be on completion, but may also be as a result of user action).  
**Default** : `false`

boolean

**batch\_size**  
_optional_

**About**

The `batch_size` property specifies the number of changes to be included in a single batch during replication.

integer

**conflict\_resolution\_type**  
_optional_

**About**

The **`conflict_resolution_type`** property specifies the conflict resolution policy Sync Gateway will apply when resolving conflicting revisions.

The default behavior is that automatic conflict resolution policy is applied.

**Valid options**

\* `default`

\* `localWins`

\* `remoteWins`

\* `custom`

**Behavior**

\* _default_ \- Selecting `default` applies the following conflict resolution policy

\* Deletes always win (the delete with longest revision history wins if both revisions are deletes)

\* The revision with the longest revision history wins (so, the one with most changes and consequently the highest revision Id).

\* _localWins_ \- Selecting `localWins` will result in local revisions always being the winner in any conflict.

\* _remoteWins_ \- Selecting `remoteWins` will result in remote revisions always being the winner in any conflict.

\* _custom_ \- Selecting `custom` specifies that you want to handle conflict resolution with your own application logic. You **must** provide this logic as a Javascript function by specifying it in using the custom-conflict-resolver parameter.

**Example**

\---- "conflict\_resolution\_type":"remoteWins" ----

**Constraints**

\* Replications created prior to version 2.8 will default to `default`.  
**Default** : `"default"`

string

**continuous**  
_optional_

**About**

The `continuous` property specifies whether this replication runs in continuous, or single-shot, mode.

**Behavior**

\* `continuous=true`– In continuous mode, changes are immediately synced in accordance with the replication definition.

\* `continuous=false`– Detected changes are synced in accordance with the replication definition. The replication ceases once all revisions are processed.

**Constraints**

\* Optional for stops and removes  
**Default** : `false`

boolean

**custom\_conflict\_resolver**  
_optional_

**About**

The `custom_conflict_resolver` property specifies the Javascript function that will be used to resolve conflicts, if the custom conflict resolution type is specified in the `conflict_resolution_type`.

**Options**

The property is _mandatory_ when `conflict_resolution_type=custom` and will be ignored in all other cases.

**Using**

Provide the required logic in a Javascript function, as a string within backticks (see also the description for the `sync` function\`.

The function takes one parameter `struct` representing the conflict and comprising

\* the document id

\* the local document

\* the remote document

The function returns a document `struct` representing the winning revision.

**Example**

\---- "custom\_conflict\_resolver":\` function(conflict) { console.log("full remoteDoc doc: "+JSON.stringify(conflict.RemoteDocument)); return conflict.RemoteDocument; }\` ----

**Constraints**

Using complex `custom_conflict_resolver` functions can noticeably degrade performance. Use a built-in resolver whenever possible.  
**Default** : `"none"`

string

**direction**  
_optional_

**About**

The mandatory `direction` property indicates whether the replication is _push_, _pull_ or _pushAndPull_.

The property value is referenced by the **remote** property.

**Constraints**

Replications created prior to version 2.8 derive the _direction_ from the source/target url of the replication.

string

**enable\_delta\_sync**  
_optional_

**About**

The `enable_delta_sync` property specifies whether delta sync is, or is not, used for the replication.

**Options**

To use delta sync or not.

\* `enable_delta_sync=true` \- the replication runs using delta sync

\* `enable_delta_sync=false` \- the replication runs without delta sync

**Behavior**

The impact of this property is dependent on the `delta_sync.enabled` setting for the relevent databases as indicated here.

\* **If** `"delta_sync.enabled": true` for both databases involved in the replication, then this parameter enables or disables its use for this specific replication.

\* In all other cases it has no effect and the replication runs without delta-sync.

**Constraints**

\* Requires _Enterprise Edition_\* Replications created prior to version 2.8 run with `enable_delta_sync=false`  
**Default** : `false`

boolean

**filter**  
_optional_

**About**

Use the optional `filter` property to defines the function to be used to filter documents.

**Options**

A common value used when replicating from Sync Gateway is `sync_gateway/bychannel`. This option limits the pull replication to a specific set of channels. You can specify the required channels using `query_params`.

**Behavior**

Works in conjunction with `query_params` to control the documents processed by the replication.

**Example**

\---- "filter":"sync\_gateway/bychannel" ----

**Constraints**

OPTIONAL for stops and removes (even if defined during creation)

string

**initial\_state**  
_optional_

**About**

The optional `initial_state` property is used to specify that the replication must be launched in 'Stopped' mode

**Behavior**

All replications are configured to start on Sync Gateway launch. So, if omitted, the state defaults to 'Running'.

Constraints\* 

Replications created prior to version 2.8 will all default to a state of 'Running'.  
Default\*\* : `"Running"`

string

**max\_backoff\_time**  
_optional_

**About**

The **max\_backoff\_time** property indicates the time-period (in minutes) during which Sync Gateway will attempt to reconnect lost or unreachable _remote_ targets.

On disconnection, Sync Gateway will do an exponential backoff up to the specified value, after which it will attempt to reconnect indefinitely every _max\_backoff\_time_ minutes.

If the value is zero, Sync Gateway will do an exponential backoff up to an interval of five minutes before stopping the replication.

**Constrains**

This value defaults to five minutes for replications created prior to version 2.8.

integer

**password**  
_optional_

The `password`, forms part of the login credentials used to access the data.

All password data is redacted and is displayed as a string of ****\*.** 
**Default**\* : `"Mandatory"` 

string

**perf\_tuning\_params**  
_optional_

The perf\_tuning\_params are yet to be defined (subject to performance testing)

NOTE - This property replaces the 'changes\_feed\_limit' at version 2.8

object

**purge\_on\_removal**  
_optional_

**About**

The optional `purge_on_removal` property specifies, per replication, whether the removal of a `channel` triggers a purge.

**Options**\- `true` or `false`\- Default = false - Document removals are ignored by receiving end

**Behavior**

If `purge_on_removal=false`, then the removal of channels is ignored (not purged) by the receiving end.

**Constraints**

\* Applies only to PULL replications, including the PULL portion of a PUSHANDPULL replication.

\* Replications created prior to version 2.8 _must_ be run with `purge_on_removal=false`.  
**Default** : `false`

boolean

**query\_params**  
_optional_

**About**

The `query_params` property defines a set of key/value pairs used in the query string of the replication.

**Behavior**

This property works in conjunction with `filters` and `channels` to provide routing.

**Using**

You can use `` query_params’ _channels_ function to _pull_ from a specific set of `channels ``. To do so, you would also need to set the `filter` to `sync_gateway/bychannels`.

**Example**

\[source,json\] ---- "filter":"sync\_gateway/bychannel", "query\_params": { "channels":\["channel.user1"\] }, ----

**Constraints**

OPTIONAL for stops and removes (even if defined during creation)

< string > array

**remote**  
_optional_

**About**

The **remote** property represents a database URL for the remote Sync Gateway. That is, it identifies the remote Sync Gateway database that is the subject of this replication's push, pull or pushAndPull action.

**Behavior**

Dependent upon setting of **direction**. If **direction** is :

\* _pull_, this is the cluster _from_ which data is pulled

\* _push_, this is the cluster _to_ which data is pushed

\* _pushAndPull_, this is the cluste from which data is pushed.

**Example**

\---- "remote": "http://www.example.com:4984/db2name", ----

**Constraints**

\* You must specify the 'remote' database's url even if it is located on the same cluster as the replication's database.

\* OPTIONAL for stops and removes

string

**replication\_id**  
_optional_

**About**

The _replication\_id_ property indicates the ID that Sync Gateway assigned to the replication.

Sync Gateway assigns a random UUID if no `replication_id` is specified when the replication is created.

string

**username**  
_optional_

The `username` forms part of the credentials used to authenticate and approve access to data

This field is redacted a string of '****\*' is displayed in its place.** 
**Default**\* : `"Mandatory"`

string

### [](#%5Freplicationstatistics-sgr1)ReplicationStatistics-SGR1

This is the replication definition set returned in response to an ExpVars `GET` request.

| Name                    | Description                                                                                                                                                                                                                                                                                                 | Schema                                                |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| **replname** _optional_ | This object comprises the stats collected and recorded for the inter-sync-gateway replication named $replname (which equates to a replication\_id). The same structure is used to return statistics from inter-sync-gateway replications versions 1 and 2, but not all items are populated by each version. | [replname](#%5Freplicationstatistics-sgr1%5Freplname) |

**replname**

| Name                                                    | Description                                                                                                                                                                                                                                                                                                               | Schema  |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **sgr\_active** _optional_                              | Whether the replication is active at this time. **Deprecated @ 2.8**: used only by inter-sync-gateway replications version 1.                                                                                                                                                                                             | boolean |
| **sgr\_docs\_checked\_sent** _optional_                 | The total number of documents checked for changes since replication started. This represents the number of potential change notifications pushed by Sync Gateway. **Constraints**\- This is not necessarily the number of documents pushed, as a given target might already have the change. \* Used by versions 1 and 2. | integer |
| **sgr\_num\_attachment\_bytes\_transferred** _optional_ | The total number of attachment bytes transferred since replication started. **Deprecated @ 2.8**: used only by inter-sync-gateway replications version 1.                                                                                                                                                                 | integer |
| **sgr\_num\_attachments\_transferred** _optional_       | The total number of attachments transferred since replication started. **Deprecated @ 2.8**: used only by inter-sync-gateway replications version 1.                                                                                                                                                                      | integer |
| **sgr\_num\_docs\_failed\_to\_push** _optional_         | The total number of documents that failed to be pushed since replication started. Used by versions 1 and 2.                                                                                                                                                                                                               | integer |
| **sgr\_num\_docs\_pushed** _optional_                   | The total number of documents that were pushed since replication started. Used by versions 1 and 2.                                                                                                                                                                                                                       | integer |

### [](#%5Fview)View

| Name                 | Description                                                                                                     | Schema                    |
| -------------------- | --------------------------------------------------------------------------------------------------------------- | ------------------------- |
| **\_rev** _optional_ | Revision identifier of the parent revision the new one should replace. (Not used when creating a new document.) | string                    |
| **views** _optional_ | List of views to save on this design document.                                                                  | [views](#%5Fview%5Fviews) |

**views**

| Name                          | Description                      | Schema                                        |
| ----------------------------- | -------------------------------- | --------------------------------------------- |
| **my\_view\_name** _optional_ | The view's map/reduce functions. | [my\_view\_name](#%5Fview%5Fmy%5Fview%5Fname) |

**my\_view\_name**

| Name                  | Description                                          | Schema |
| --------------------- | ---------------------------------------------------- | ------ |
| **map** _optional_    | Inline JavaScript definition for the map function    | string |
| **reduce** _optional_ | Inline JavaScript definition for the reduce function | string |

---

##### 

## [](#related-content)Related Content

###### [](#-2)

API Topics

* [Public REST API](rest-api.md)
* [Admin REST API](rest-api-admin.md)
* [Metrics REST API](rest-api-metrics.md)

###### [](#-3)

Reference

* [Bootstrap](configuration-schema-bootstrap.md)
* [Database](configuration-schema-database.md)
* [Database Security](configuration-schema-db-security.md)
* [Access Control](configuration-schema-access-control.md)
* [Import Filter](configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)