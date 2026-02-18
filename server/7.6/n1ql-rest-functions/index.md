---
title: Query Functions REST API
editUrl: https://github.com/couchbaselabs/cb-swagger/edit/release/7.6/docs/modules/n1ql-rest-functions/pages/index.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.6/n1ql-rest-functions/index.html)

# Query Functions REST API

## [](#overview)Overview

The Query Functions REST API is a secondary API provided by the Query service. This API enables you to manage the JavaScript libraries and objects that are used to create SQL++ user-defined functions.

### Version information

**Version:** 7.6

### Host information

{scheme}://{host}:{port}

The URL scheme, host, and port are as follows.

| Component  | Description                                                                             |
| ---------- | --------------------------------------------------------------------------------------- |
| **scheme** | The URL scheme. Use https for secure access. **Values:** http, https                    |
| **host**   | The host name or IP address of a node running the Query Service. **Example:** localhost |
| **port**   | The Query Service REST port. Use 18093 for secure access. **Values:** 8093, 18093       |

### Examples on this page

In the HTTP request examples:

* `$BASEPATH` is the URL scheme, host, and port for a node running the Query Service.
* `$USER` is the user name of an authorized user — see [Security](#security).
* `$PASSWORD` is the password to connect to Couchbase Server.

## [](#resources)Resources

This section describes the operations available with this REST API.

[Delete a Library](#delete%5Flibrary)  
[Read All Libraries](#get%5Fcollection)  
[Read a Library](#get%5Flibrary)  
[Create or Update a Library](#post%5Flibrary)

### [](#delete%5Flibrary)Delete a Library

DELETE /evaluator/v1/libraries/{library}

#### [](#delete%5Flibrary-description)Description

Deletes the specified library entirely.

By default, this operation deletes a global library. For a scoped library, you must specify the bucket and scope.

> [!NOTE]
> Before you can delete a library, you must first drop all SQL++ external user-defined functions which point to any of the JavaScript functions within that library. For more information, see [DROP FUNCTION](../n1ql/n1ql-language-reference/dropfunction.md).

#### [](#delete%5Flibrary-parameters)Parameters

Path Parameters

| Name                | Description            | Schema |
| ------------------- | ---------------------- | ------ |
| **library**required | The name of a library. | String |

Query Parameters

| Name               | Description                                                           | Schema |
| ------------------ | --------------------------------------------------------------------- | ------ |
| **bucket**optional | For scoped libraries only. The bucket in which the library is stored. | String |
| **scope**optional  | For scoped libraries only. The scope in which the library is stored.  | String |

> [!NOTE]
> To delete a scoped library, you must specify both the `bucket` and `scope` parameters. You cannot specify one without the other.

#### [](#delete%5Flibrary-responses)Responses

| HTTP Code | Description                                                                                                     | Schema |
| --------- | --------------------------------------------------------------------------------------------------------------- | ------ |
| 200       | The operation was successful.                                                                                   |        |
| 400       | Bad request. The path may not conform to the schema.                                                            |        |
| 404       | Not found. The library name in the path may be incorrect, or the bucket and scope may be specified incorrectly. |        |

#### [](#delete%5Flibrary-security)Security

| Type         | Name                       |
| ------------ | -------------------------- |
| http (basic) | [Scope](#security-Scope)   |
| http (basic) | [Global](#security-Global) |

#### [](#example-http-request)Example HTTP Request

Request 1: Delete a global library entirely.

curl request

```sh
curl -X DELETE \
"$BASEPATH/evaluator/v1/libraries/math" \
-u $USER:$PASSWORD
```

Request 2: Delete a scoped library entirely.

curl request

```sh
curl -X DELETE \
"$BASEPATH/evaluator/v1/libraries/science?bucket=travel-sample&scope=inventory" \
-u $USER:$PASSWORD
```

### [](#get%5Fcollection)Read All Libraries

GET /evaluator/v1/libraries

#### [](#get%5Fcollection-description)Description

Returns all libraries and functions.

By default, this operation returns all global libraries and functions, and all scoped libraries and functions. To return all the libraries and functions in a single scope, specify a bucket and scope.

Produces

* application/json

#### [](#get%5Fcollection-parameters)Parameters

Query Parameters

| Name               | Description                                                          | Schema |
| ------------------ | -------------------------------------------------------------------- | ------ |
| **bucket**optional | For scoped libraries only. The bucket from which to fetch libraries. | String |
| **scope**optional  | For scoped libraries only. The scope from which to fetch libraries.  | String |

> [!NOTE]
> To fetch libraries from a scope, you must specify both the `bucket` and `scope` parameters. You cannot specify one without the other.

#### [](#get%5Fcollection-responses)Responses

| HTTP Code | Description                                                          | Schema                      |
| --------- | -------------------------------------------------------------------- | --------------------------- |
| 200       | An array of objects, each giving information about a single library. | [Library](#Libraries) array |
| 400       | Bad request. The path may not conform to the schema.                 |                             |

#### [](#get%5Fcollection-security)Security

| Type         | Name                       |
| ------------ | -------------------------- |
| http (basic) | [Scope](#security-Scope)   |
| http (basic) | [Global](#security-Global) |

#### [](#example-http-request-2)Example HTTP Request

Request 3: Fetch all defined libraries.

curl request

```sh
curl -X GET \
"$BASEPATH/evaluator/v1/libraries" \
-u $USER:$PASSWORD
```

Request 4: Fetch all defined libraries in the specified scope.

curl request

```sh
curl -X GET \
"$BASEPATH/evaluator/v1/libraries?bucket=travel-sample&scope=inventory" \
-u $USER:$PASSWORD
```

#### [](#get%5Fcollection-ex-response)Example HTTP Response

Response 200

All Libraries

```json
[ {
  "name" : "math",
  "bucket" : "",
  "scope" : "",
  "code" : "function add(a, b) { return a + b; } function mul(a, b) { return a * b; }"
}, {
  "name" : "science",
  "bucket" : "travel-sample",
  "scope" : "inventory",
  "code" : "function f2c(f) { return (5/9)*(f-32); }"
} ]
```

Scoped Libraries

```json
[ {
  "name" : "science",
  "bucket" : "travel-sample",
  "scope" : "inventory",
  "code" : "function f2c(f) { return (5/9)*(f-32); }"
} ]
```

### [](#get%5Flibrary)Read a Library

GET /evaluator/v1/libraries/{library}

#### [](#get%5Flibrary-description)Description

Returns a library with all its functions.

By default, this operation returns a global library. For a scoped library, you must specify the bucket and scope.

Produces

* application/json

#### [](#get%5Flibrary-parameters)Parameters

Path Parameters

| Name                | Description            | Schema |
| ------------------- | ---------------------- | ------ |
| **library**required | The name of a library. | String |

Query Parameters

| Name               | Description                                                           | Schema |
| ------------------ | --------------------------------------------------------------------- | ------ |
| **bucket**optional | For scoped libraries only. The bucket in which the library is stored. | String |
| **scope**optional  | For scoped libraries only. The scope in which the library is stored.  | String |

> [!NOTE]
> To read a scoped library, you must specify both the `bucket` and `scope` parameters. You cannot specify one without the other.

#### [](#get%5Flibrary-responses)Responses

| HTTP Code | Description                                                                                                     | Schema                  |
| --------- | --------------------------------------------------------------------------------------------------------------- | ----------------------- |
| 200       | An object with a single property, giving information about the specified library.                               | [Functions](#Functions) |
| 400       | Bad request. The path may not conform to the schema.                                                            |                         |
| 404       | Not found. The library name in the path may be incorrect, or the bucket and scope may be specified incorrectly. |                         |

#### [](#get%5Flibrary-security)Security

| Type         | Name                       |
| ------------ | -------------------------- |
| http (basic) | [Scope](#security-Scope)   |
| http (basic) | [Global](#security-Global) |

#### [](#example-http-request-3)Example HTTP Request

Request 5: Get all functions in the specified global library.

curl request

```sh
curl -X GET \
"$BASEPATH/evaluator/v1/libraries/math" \
-u $USER:$PASSWORD
```

Request 6: Get all functions in the specified scoped library.

curl request

```sh
curl -X GET \
"$BASEPATH/evaluator/v1/libraries/science?bucket=travel-sample&scope=inventory" \
-u $USER:$PASSWORD
```

#### [](#get%5Flibrary-ex-response)Example HTTP Response

Response 200

Global Library

```json
{
  "math" : "function add(a, b) { return a + b; } function mul(a, b) { return a * b; }"
}
```

Scoped Library

```json
{
  "science" : "function f2c(f) { return (5/9)*(f-32); }"
}
```

### [](#post%5Flibrary)Create or Update a Library

POST /evaluator/v1/libraries/{library}

#### [](#post%5Flibrary-description)Description

Creates the specified library and its associated functions. If the specified library exists, the existing library is overwritten.

By default, this operation creates or updates a global library. For a scoped library, you must specify the bucket and scope.

> [!NOTE]
> * To add a function to a library, update the library with all existing functions, plus the new function.
> * To update a function, update the library with all existing functions, including the updated function definition.
> * To delete a function from a library, update the library with all existing functions, without the deleted function.

Consumes

* application/json

#### [](#post%5Flibrary-parameters)Parameters

Path Parameters

| Name                | Description            | Schema |
| ------------------- | ---------------------- | ------ |
| **library**required | The name of a library. | String |

Query Parameters

| Name               | Description                                                           | Schema |
| ------------------ | --------------------------------------------------------------------- | ------ |
| **bucket**optional | For scoped libraries only. The bucket in which the library is stored. | String |
| **scope**optional  | For scoped libraries only. The scope in which the library is stored.  | String |

Body Parameter

| Name             | Description                                           | Schema |
| ---------------- | ----------------------------------------------------- | ------ |
| **Body**required | The JavaScript code for all functions in the library. | String |

> [!NOTE]
> To create or update a scoped library, you must specify both the `bucket` and `scope` parameters. You cannot specify one without the other.

#### [](#post%5Flibrary-responses)Responses

| HTTP Code | Description                                                                                                     | Schema |
| --------- | --------------------------------------------------------------------------------------------------------------- | ------ |
| 200       | The operation was successful.                                                                                   |        |
| 400       | Bad request. The body of the request may be incorrect, or the path may not conform to the schema.               |        |
| 404       | Not found. The library name in the path may be incorrect, or the bucket and scope may be specified incorrectly. |        |

#### [](#post%5Flibrary-security)Security

| Type         | Name                       |
| ------------ | -------------------------- |
| http (basic) | [Scope](#security-Scope)   |
| http (basic) | [Global](#security-Global) |

#### [](#example-http-request-4)Example HTTP Request

Request 7: Create or update a global library called `math`. The library contains two functions, `add` and `sub`.

curl request

```sh
curl -X POST \
"$BASEPATH/evaluator/v1/libraries/math" \
-u $USER:$PASSWORD \
-H 'content-type: application/json' \
-d 'function add(a, b) { let data = a + b; return data; }
    function sub(a, b) { let data = a - b; return data; }'
```

Request 8: Add a function called `mul` to the global library, leaving the other functions unchanged.

curl request

```sh
curl -X POST \
"$BASEPATH/evaluator/v1/libraries/math" \
-u $USER:$PASSWORD \
-H 'content-type: application/json' \
-d 'function add(a, b) { let data = a + b; return data; }
    function sub(a, b) { let data = a - b; return data; }
    function mul(a, b) { let data = a * b; return data; }'
```

Request 9: Edit the function called `sub` to use a helper function called `helper`, leaving the other functions unchanged.

curl request

```sh
curl -X POST \
"$BASEPATH/evaluator/v1/libraries/math" \
-u $USER:$PASSWORD \
-H 'content-type: application/json' \
-d 'function add(a, b) { let data = a + b; return data; }
    function mul(a, b) { let data = a * b; return data; }
    function sub(a, b) { return helper(a, b); }
    function helper(a, b) { return a - b; }'
```

Request 10: Remove the function called `sub` and the helper function called `helper`, leaving the other functions unchanged.

curl request

```sh
curl -X POST \
"$BASEPATH/evaluator/v1/libraries/math" \
-u $USER:$PASSWORD \
-H 'content-type: application/json' \
-d 'function add(a, b) { let data = a + b; return data; }
    function mul(a, b) { let data = a * b; return data; }'
```

Request 11: Create or update a scoped library called `science`. The library contains one function, `f2c`.

curl request

```sh
curl -X POST \
"$BASEPATH/evaluator/v1/libraries/science?bucket=travel-sample&scope=inventory" \
-u $USER:$PASSWORD \
-H 'content-type: application/json' \
-d 'function f2c(f) { return (5/9)*(f-32); }'
```

## [](#models)Definitions

This section describes the properties consumed and returned by this REST API.

[Functions](#Functions)  
[Library](#Libraries)

### [](#Functions)Functions

 Object

| Property                        |                                                                                                                                                                                                      | Schema |
| ------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **<library>**additionalproperty | The JavaScript code for all functions in the library. The name of the property is the name of the library. **Example:** "function add(a, b) { return a + b; } function mul(a, b) { return a \* b; }" | String |

### [](#Libraries)Library

 Object

| Property           |                                                                                                                                                 | Schema |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **name**required   | The name of a library. **Example:** "math"                                                                                                      | String |
| **bucket**required | For scoped libraries, the bucket in which the library is stored. For global libraries, this string is empty. **Example:** "travel-sample"       | String |
| **scope**required  | For scoped libraries, the scope in which the library is stored. For global libraries, this string is empty. **Example:** "inventory"            | String |
| **code**required   | The JavaScript code for all functions in the library. **Example:** "function add(a, b) { return a + b; } function mul(a, b) { return a \* b; }" | String |

## [](#security)Security

The Functions API supports admin credentials. Pass your credentials through HTTP headers (HTTP basic authentication).

### [](#security-Global)Global

To manage global libraries, users must have the _Manage Global External Functions_ RBAC role.

This role enables you to create, read, update, or delete any global library, but does not give you access to any scoped libraries.

**Type:** http

### [](#security-Scope)Scope

To manage scoped libraries, users must have the _Manage Scope External Functions_ RBAC role, with permissions on the specified bucket and scope.

This role enables you to create, read, update, or delete any library in the scope to which you have access, but does not give you access to any other scoped libraries. In addition, this role enables you to read any global library, but not to create, update, or delete them.

**Type:** http

For more information, see [Roles](../learn/security/roles.md).