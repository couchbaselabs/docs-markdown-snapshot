[View original HTML](/server/7.2/analytics/rest-library.html)

## [](#%5Foverview)Overview

The Analytics Library REST API is provided by the Analytics service. This API enables you to manage the libraries that are used to create SQL++ for Analytics user-defined functions.

The API schemes and host URLs are as follows:

* <http://localhost:8095/>
* <https://localhost:18095/> (for secure access)

Note that this API is only available on the loopback interface of a node running the Analytics service.

### [](#version-information)Version information

_Version_ : 0.1

### [](#consumes)Consumes

* `multipart/form-data`

### [](#produces)Produces

* `application/json`

## [](#%5Fpaths)Paths

This section describes the operations available with this REST API.

* [Read All Libraries](#%5Fget%5Fcollection)
* [Create or Update a Library](#%5Fpost%5Flibrary)
* [Delete a Library](#%5Fdelete%5Flibrary)

### [](#%5Fget%5Fcollection)Read All Libraries

GET /analytics/library/

#### [](#description)Description

Returns all libraries and functions.

#### [](#responses)Responses

| HTTP Code | Description                                                                                                                    | Schema                                |
| --------- | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------- |
| **200**   | Success. Returns an array of objects, each of which contains information about a single library.                               | < [Libraries](#%5Flibraries) \> array |
| **404**   | Not found. The path may be missing its trailing slash.                                                                         | No Content                            |
| **500**   | Internal server error. Incorrect path or port number, incorrect credentials, badly formatted parameters, or missing arguments. | [Errors](#%5Ferrors)                  |

#### [](#security)Security

| Type      | Name                                         |
| --------- | -------------------------------------------- |
| **basic** | **[Analytics Admin](#%5Fanalytics%5Fadmin)** |

#### [](#example-http-request)Example HTTP request

The example below fetches all defined libraries.

Curl request

```sh
curl -X GET \
http://localhost:8095/analytics/library/ \
-u Administrator:password
```

#### [](#example-http-response)Example HTTP response

Response 200

```json
[ {
  "scope" : "travel-sample/inventory",
  "hash_md5" : "b0e764a12aa922de80b14bab9a7d2fb3",
  "name" : "mylib"
} ]
```

### [](#%5Fpost%5Flibrary)Create or Update a Library

POST /analytics/library/{scope}/{library}

#### [](#description-2)Description

Creates the specified library and its associated functions. If the specified library exists, the existing library is overwritten.

* To add a function to a library, update the library with all existing functions, plus the new function.
* To update a function, update the library with all existing functions, including the updated function definition.
* To delete a function from a library, update the library with all existing functions, without the deleted function.

#### [](#parameters)Parameters

| Type         | Name                   | Description                                                                                                                                                                                               | Schema        |
| ------------ | ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| **Path**     | **library** _required_ | The name of a library.                                                                                                                                                                                    | string        |
| **Path**     | **scope** _required_   | The name of the Analytics scope containing the library. The scope name may contain one or two identifiers, separated by a slash (/). You must URL-encode this parameter to escape any special characters. | string        |
| **FormData** | **data** _required_    | The library and all its dependencies, packaged by shiv.                                                                                                                                                   | file          |
| **FormData** | **type** _required_    | The language of the library.                                                                                                                                                                              | enum (python) |

#### [](#responses-2)Responses

| HTTP Code | Description                                                                                                                    | Schema               |
| --------- | ------------------------------------------------------------------------------------------------------------------------------ | -------------------- |
| **200**   | The operation was successful.                                                                                                  | object               |
| **400**   | Bad request. A parameter has an incorrect value.                                                                               | [Errors](#%5Ferrors) |
| **500**   | Internal server error. Incorrect path or port number, incorrect credentials, badly formatted parameters, or missing arguments. | [Errors](#%5Ferrors) |

#### [](#security-2)Security

| Type      | Name                               |
| --------- | ---------------------------------- |
| **basic** | **[Full Admin](#%5Ffull%5Fadmin)** |

#### [](#example-http-request-2)Example HTTP request

The example below creates or updates a library called `mylib` in the `travel-sample.inventory` scope. The Python code is stored in a file called `lib.pyz`.

Curl request

```sh
curl -X POST \
http://localhost:8095/analytics/library/travel-sample%2Finventory/mylib \
-u Administrator:password \
-d type=python
-d data=lib.pyz
```

|  | The dot separator within the scope name is converted to a slash (/), which is then URL-encoded as %2F. |
|  | ------------------------------------------------------------------------------------------------------ |

### [](#%5Fdelete%5Flibrary)Delete a Library

DELETE /analytics/library/{scope}/{library}

#### [](#description-3)Description

Deletes the specified library entirely.

#### [](#parameters-2)Parameters

| Type     | Name                   | Description                                                                                                                                                                                               | Schema |
| -------- | ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **Path** | **library** _required_ | The name of a library.                                                                                                                                                                                    | string |
| **Path** | **scope** _required_   | The name of the Analytics scope containing the library. The scope name may contain one or two identifiers, separated by a slash (/). You must URL-encode this parameter to escape any special characters. | string |

#### [](#responses-3)Responses

| HTTP Code | Description                                                                                                                    | Schema               |
| --------- | ------------------------------------------------------------------------------------------------------------------------------ | -------------------- |
| **200**   | The operation was successful.                                                                                                  | object               |
| **404**   | Not found. The library name in the path may be incorrect.                                                                      | string               |
| **500**   | Internal server error. Incorrect path or port number, incorrect credentials, badly formatted parameters, or missing arguments. | [Errors](#%5Ferrors) |

#### [](#security-3)Security

| Type      | Name                               |
| --------- | ---------------------------------- |
| **basic** | **[Full Admin](#%5Ffull%5Fadmin)** |

#### [](#example-http-request-3)Example HTTP request

The example below deletes the `mylib` library from the `travel-sample.inventory` scope.

Curl request

```sh
curl -X DELETE \
http://localhost:8095/analytics/library/travel-sample%2Finventory/mylib \
-u Administrator:password
```

|  | The dot separator within the scope name is converted to a slash (/), which is then URL-encoded as %2F. |
|  | ------------------------------------------------------------------------------------------------------ |

## [](#%5Fdefinitions)Definitions

This section describes the properties returned by this REST API.

* [Libraries](#%5Flibraries)
* [Errors](#%5Ferrors)

### [](#%5Flibraries)Libraries

| Name                     | Description                                                                                                                                                                  | Schema |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **scope** _optional_     | The name of the Analytics scope containing the library. The scope name may contain one or two identifiers, separated by a slash (/). **Example** : "travel-sample/inventory" | string |
| **hash\_md5** _optional_ | A MD5 hash of the library residing on the server.                                                                                                                            | string |
| **name** _optional_      | The name of the library. **Example** : "mylib"                                                                                                                               | string |

### [](#%5Ferrors)Errors

| Name                 | Description       | Schema |
| -------------------- | ----------------- | ------ |
| **error** _required_ | An error message. | string |

## [](#%5Fsecurityscheme)Security

The Analytics Library REST API supports HTTP basic authentication. Credentials can be passed via HTTP headers.

### [](#%5Ffull%5Fadmin)Full Admin

To [Create or Update a Library](#%5Fpost%5Flibrary) or [Delete a Library](#%5Fdelete%5Flibrary), users must have the Full Admin RBAC role.

_Type_ : basic

### [](#%5Fanalytics%5Fadmin)Analytics Admin

To [Read All Libraries](#%5Fget%5Fcollection), users must have one of the following RBAC roles:

* Full Admin
* Cluster Admin
* Analytics Admin

_Type_ : basic

Refer to [Roles](../learn/security/roles.md) for more details.