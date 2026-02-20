---
title: Analytics Library REST API
description: A description of the Library REST API for Couchbase Analytics.
editUrl: https://github.com/couchbaselabs/cb-swagger/edit/release/7.6/docs/modules/analytics-rest-library/pages/index.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.6@server:analytics-rest-library:index.adoc[]
---

[View original HTML](/server/7.6/analytics-rest-library/index.html)

# Analytics Library REST API

## [](#overview)Overview

The Analytics Library REST API is provided by the Analytics service. This API enables you to manage the libraries that are used to create SQL++ for Analytics user-defined functions.

### Version information

**Version:** 0.1

### Host information

{scheme}://{host}:{port}

The URL scheme, host, and port are as follows.

| Component  | Description                                                                                 |
| ---------- | ------------------------------------------------------------------------------------------- |
| **scheme** | The URL scheme. Use https for secure access. **Values:** http, https                        |
| **host**   | The host name or IP address of a node running the Analytics Service. **Example:** localhost |
| **port**   | The Analytics Service REST port. Use 18095 for secure access. **Values:** 8095, 18095       |

## [](#resources)Resources

This section describes the operations available with this REST API.

[Delete a Library](#delete%5Flibrary)  
[Read All Libraries](#get%5Fcollection)  
[Create or Update a Library](#post%5Flibrary)

### [](#delete%5Flibrary)Delete a Library

DELETE /analytics/library/{scope}/{library}

#### [](#delete%5Flibrary-description)Description

Deletes the specified library entirely.

Produces

* application/json

#### [](#delete%5Flibrary-parameters)Parameters

Path Parameters

| Name                | Description                                                                                                                                                                                               | Schema |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **library**required | The name of a library.                                                                                                                                                                                    | String |
| **scope**required   | The name of the Analytics scope containing the library. The scope name may contain one or two identifiers, separated by a slash (/). You must URL-encode this parameter to escape any special characters. | String |

#### [](#delete%5Flibrary-responses)Responses

| HTTP Code | Description                                                                                                                    | Schema            |
| --------- | ------------------------------------------------------------------------------------------------------------------------------ | ----------------- |
| 200       | The operation was successful.                                                                                                  | Object            |
| 404       | Not found. The library name in the path may be incorrect.                                                                      |                   |
| 500       | Internal server error. Incorrect path or port number, incorrect credentials, badly formatted parameters, or missing arguments. | [Errors](#Errors) |

#### [](#delete%5Flibrary-security)Security

| Type         | Name                              |
| ------------ | --------------------------------- |
| http (basic) | [Full Admin](#security-FullAdmin) |

#### [](#example-http-request)Example HTTP Request

The example below deletes the `mylib` library from the `travel-sample.inventory` scope.

curl request

```sh
curl -X DELETE \
http://localhost:8095/analytics/library/travel-sample%2Finventory/mylib \
-u Administrator:password
```

> [!NOTE]
> The dot separator within the scope name is converted to a slash (`/`), which is then URL-encoded as `%2F`.

### [](#get%5Fcollection)Read All Libraries

GET /analytics/library

#### [](#get%5Fcollection-description)Description

Returns all libraries and functions.

Produces

* application/json

#### [](#get%5Fcollection-responses)Responses

| HTTP Code | Description                                                                                                                    | Schema                        |
| --------- | ------------------------------------------------------------------------------------------------------------------------------ | ----------------------------- |
| 200       | Success. Returns an array of objects, each of which contains information about a single library.                               | [Libraries](#Libraries) array |
| 404       | Not found. The path may be missing its trailing slash.                                                                         |                               |
| 500       | Internal server error. Incorrect path or port number, incorrect credentials, badly formatted parameters, or missing arguments. | [Errors](#Errors)             |

#### [](#get%5Fcollection-security)Security

| Type         | Name                                        |
| ------------ | ------------------------------------------- |
| http (basic) | [Analytics Admin](#security-AnalyticsAdmin) |

#### [](#example-http-request-2)Example HTTP Request

The example below fetches all defined libraries.

curl request

```sh
curl -X GET \
http://localhost:8095/analytics/library/ \
-u Administrator:password
```

#### [](#example-http-response)Example HTTP Response

Response 200

```json
[ {
  "scope" : "travel-sample/inventory",
  "hash_md5" : "b0e764a12aa922de80b14bab9a7d2fb3",
  "name" : "mylib"
} ]
```

### [](#post%5Flibrary)Create or Update a Library

POST /analytics/library/{scope}/{library}

#### [](#post%5Flibrary-description)Description

Creates the specified library and its associated functions. If the specified library exists, the existing library is overwritten.

* To add a function to a library, update the library with all existing functions, plus the new function.
* To update a function, update the library with all existing functions, including the updated function definition.
* To delete a function from a library, update the library with all existing functions, without the deleted function.

Consumes

* multipart/form-data

Produces

* application/json

#### [](#post%5Flibrary-parameters)Parameters

Path Parameters

| Name                | Description                                                                                                                                                                                               | Schema |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **library**required | The name of a library.                                                                                                                                                                                    | String |
| **scope**required   | The name of the Analytics scope containing the library. The scope name may contain one or two identifiers, separated by a slash (/). You must URL-encode this parameter to escape any special characters. | String |

Form Parameters

| Name             | Description                                             | Schema        |
| ---------------- | ------------------------------------------------------- | ------------- |
| **data**required | The library and all its dependencies, packaged by shiv. | File (binary) |
| **type**required | The language of the library. **Values:** "python"       | String        |

#### [](#post%5Flibrary-responses)Responses

| HTTP Code | Description                                                                                                                    | Schema            |
| --------- | ------------------------------------------------------------------------------------------------------------------------------ | ----------------- |
| 200       | The operation was successful.                                                                                                  | Object            |
| 400       | Bad request. A parameter has an incorrect value.                                                                               | [Errors](#Errors) |
| 500       | Internal server error. Incorrect path or port number, incorrect credentials, badly formatted parameters, or missing arguments. | [Errors](#Errors) |

#### [](#post%5Flibrary-security)Security

| Type         | Name                              |
| ------------ | --------------------------------- |
| http (basic) | [Full Admin](#security-FullAdmin) |

#### [](#example-http-request-3)Example HTTP Request

The example below creates or updates a library called `mylib` in the `travel-sample.inventory` scope. The Python code is stored in a file called `lib.pyz`.

curl request

```sh
curl -X POST \
http://localhost:8095/analytics/library/travel-sample%2Finventory/mylib \
-u Administrator:password \
-d type=python
-d data=lib.pyz
```

> [!NOTE]
> The dot separator within the scope name is converted to a slash (`/`), which is then URL-encoded as `%2F`.

## [](#models)Definitions

This section describes the properties consumed and returned by this REST API.

[Errors](#Errors)  
[Libraries](#Libraries)

### [](#Errors)Errors

 Object

| Property          |                   | Schema |
| ----------------- | ----------------- | ------ |
| **error**required | An error message. | String |

### [](#Libraries)Libraries

 Object

| Property              |                                                                                                                                                                             | Schema |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **scope**optional     | The name of the Analytics scope containing the library. The scope name may contain one or two identifiers, separated by a slash (/). **Example:** "travel-sample/inventory" | String |
| **hash\_md5**optional | A MD5 hash of the library residing on the server.                                                                                                                           | String |
| **name**optional      | The name of the library. **Example:** "mylib"                                                                                                                               | String |

## [](#security)Security

The Analytics Library REST API supports HTTP basic authentication. Pass your credentials through HTTP headers.

### [](#security-FullAdmin)Full Admin

To [Create or Update a Library](#post%5Flibrary) or [Delete a Library](#delete%5Flibrary), users must have the Full Admin RBAC role.

**Type:** http

### [](#security-AnalyticsAdmin)Analytics Admin

To [Read All Libraries](#get%5Fcollection), users must have one of the following RBAC roles:

* Full Admin
* Cluster Admin
* Analytics Admin

**Type:** http

For more information, see [Roles](../learn/security/roles.md).