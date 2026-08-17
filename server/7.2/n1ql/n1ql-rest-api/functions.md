---
title: Functions REST API
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/n1ql/pages/n1ql-rest-api/functions.adoc
  xref: xref:7.2@server:n1ql:n1ql-rest-api/functions.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/n1ql/n1ql-rest-api/functions.html)

# Functions REST API

## [](#%5Foverview)Overview

The Functions REST API is a secondary API provided by the Query service. This API enables you to manage the JavaScript libraries and objects that are used to create SQL++ user-defined functions.

The base URL schemes for this API are as follows:

* <http://node:8093/>
* <https://node:18093/> (for secure access)

where `node` is the host name or IP address of a computer running the Query service.

### [](#version-information)Version information

_Version_ : 7.2

### [](#uri-scheme)URI scheme

_Host_ : localhost:8093  
_Schemes_ : HTTP

### [](#consumes)Consumes

* `application/json`

### [](#produces)Produces

* `application/json`

## [](#%5Fpaths)Paths

**Table of Contents**

* [Read All Libraries](#%5Fget%5Fcollection)
* [Read a Library](#%5Fget%5Flibrary)
* [Create or Update a Library](#%5Fpost%5Flibrary)
* [Delete a Library](#%5Fdelete%5Flibrary)

### [](#%5Fget%5Fcollection)Read All Libraries

GET /evaluator/v1/libraries

#### [](#description)Description

Returns all libraries and functions.

By default, this operation returns all global libraries and functions, and all scoped libraries and functions. To return all the libraries and functions in a single scope, specify a bucket and scope.

#### [](#parameters)Parameters

| Type      | Name                  | Description                                                          | Schema |
| --------- | --------------------- | -------------------------------------------------------------------- | ------ |
| **Query** | **bucket** _optional_ | For scoped libraries only. The bucket from which to fetch libraries. | string |
| **Query** | **scope** _optional_  | For scoped libraries only. The scope from which to fetch libraries.  | string |

> [!NOTE]
> To fetch libraries from a scope, you must specify both the `bucket` and `scope` parameters. You cannot specify one without the other.

#### [](#responses)Responses

| HTTP Code | Description                                                          | Schema                                |
| --------- | -------------------------------------------------------------------- | ------------------------------------- |
| **200**   | An array of objects, each giving information about a single library. | < [Libraries](#%5Flibraries) \> array |
| **400**   | Bad request. The path may not conform to the schema.                 | string                                |

#### [](#security)Security

| Type      | Name                     |
| --------- | ------------------------ |
| **basic** | **[Global](#%5Fglobal)** |
| **basic** | **[Scope](#%5Fscope)**   |

#### [](#example-http-request)Example HTTP request

Request 1: Fetch all defined libraries.

Curl request

```sh
curl -X GET \
"http://localhost:8093/evaluator/v1/libraries" \
-u Administrator:password
```

Request 2: Fetch all defined libraries in the specified scope.

Curl request

```sh
curl -X GET \
"http://localhost:8093/evaluator/v1/libraries?bucket=travel-sample&scope=inventory" \
-u Administrator:password
```

#### [](#example-http-response)Example HTTP response

Result of [request 1](#collection-example-1).

Response 200

```json
[
  {
    "name": "math",
    "bucket": "",
    "scope": "",
    "code": "function add(a, b) { return a + b; } function mul(a, b) { return a * b; }"
  },
  {
    "name": "science",
    "bucket": "travel-sample",
    "scope": "inventory",
    "code": "function f2c(f) { return (5/9)*(f-32); }"
  }
]
```

Result of [request 2](#collection-example-2).

Response 200

```json
[
  {
    "name": "science",
    "bucket": "travel-sample",
    "scope": "inventory",
    "code": "function f2c(f) { return (5/9)*(f-32); }"
  }
]
```

### [](#%5Fget%5Flibrary)Read a Library

GET /evaluator/v1/libraries/{library}

#### [](#description-2)Description

Returns a library with all its functions.

By default, this operation returns a global library. For a scoped library, you must specify the bucket and scope.

#### [](#parameters-2)Parameters

| Type      | Name                   | Description                                                           | Schema |
| --------- | ---------------------- | --------------------------------------------------------------------- | ------ |
| **Path**  | **library** _required_ | The name of a library.                                                | string |
| **Query** | **bucket** _optional_  | For scoped libraries only. The bucket in which the library is stored. | string |
| **Query** | **scope** _optional_   | For scoped libraries only. The scope in which the library is stored.  | string |

> [!NOTE]
> To read a scoped library, you must specify both the `bucket` and `scope` parameters. You cannot specify one without the other.

#### [](#responses-2)Responses

| HTTP Code | Description                                                                                                     | Schema                     |
| --------- | --------------------------------------------------------------------------------------------------------------- | -------------------------- |
| **200**   | An object with a single property, giving information about the specified library.                               | [Functions](#%5Ffunctions) |
| **400**   | Bad request. The path may not conform to the schema.                                                            | string                     |
| **404**   | Not found. The library name in the path may be incorrect, or the bucket and scope may be specified incorrectly. | string                     |

#### [](#security-2)Security

| Type      | Name                     |
| --------- | ------------------------ |
| **basic** | **[Global](#%5Fglobal)** |
| **basic** | **[Scope](#%5Fscope)**   |

#### [](#example-http-request-2)Example HTTP request

Request 3: Get all functions in the specified global library.

Curl request

```sh
curl -X GET \
"http://localhost:8093/evaluator/v1/libraries/math" \
-u Administrator:password
```

Request 4: Get all functions in the specified scoped library.

Curl request

```sh
curl -X GET \
"http://localhost:8093/evaluator/v1/libraries/science?bucket=travel-sample&scope=inventory" \
-u Administrator:password
```

#### [](#example-http-response-2)Example HTTP response

Result of [request 3](#library-example-1).

Response 200

```json
{
  "math": "function add(a, b) { return a + b; } function mul(a, b) { return a * b; }"
}
```

Result of [request 4](#library-example-2).

Response 200

```json
{
  "science": "function f2c(f) { return (5/9)*(f-32); }"
}
```

### [](#%5Fpost%5Flibrary)Create or Update a Library

POST /evaluator/v1/libraries/{library}

#### [](#description-3)Description

Creates the specified library and its associated functions. If the specified library exists, the existing library is overwritten.

By default, this operation creates or updates a global library. For a scoped library, you must specify the bucket and scope.

> [!NOTE]
> * To add a function to a library, update the library with all existing functions, plus the new function.
> * To update a function, update the library with all existing functions, including the updated function definition.
> * To delete a function from a library, update the library with all existing functions, without the deleted function.

#### [](#parameters-3)Parameters

| Type      | Name                     | Description                                                           | Schema |
| --------- | ------------------------ | --------------------------------------------------------------------- | ------ |
| **Path**  | **library** _required_   | The name of a library.                                                | string |
| **Query** | **bucket** _optional_    | For scoped libraries only. The bucket in which the library is stored. | string |
| **Query** | **scope** _optional_     | For scoped libraries only. The scope in which the library is stored.  | string |
| **Body**  | **functions** _required_ | The JavaScript code for all functions in the library.                 | string |

> [!NOTE]
> To create or update a scoped library, you must specify both the `bucket` and `scope` parameters. You cannot specify one without the other.

#### [](#responses-3)Responses

| HTTP Code | Description                                                                                                     | Schema |
| --------- | --------------------------------------------------------------------------------------------------------------- | ------ |
| **200**   | The operation was successful.                                                                                   | string |
| **400**   | Bad request. The body of the request may be incorrect, or the path may not conform to the schema.               | string |
| **404**   | Not found. The library name in the path may be incorrect, or the bucket and scope may be specified incorrectly. | string |

#### [](#security-3)Security

| Type      | Name                     |
| --------- | ------------------------ |
| **basic** | **[Global](#%5Fglobal)** |
| **basic** | **[Scope](#%5Fscope)**   |

#### [](#example-http-request-3)Example HTTP request

Request 5: Create or update a global library called `math`. The library contains two functions, `add` and `sub`.

Curl request

```sh
curl -X POST \
"http://localhost:8093/evaluator/v1/libraries/math" \
-u Administrator:password \
-H 'content-type: application/json' \
-d 'function add(a, b) { let data = a + b; return data; }
    function sub(a, b) { let data = a - b; return data; }'
```

Request 6: Add a function called `mul` to the global library, leaving the other functions unchanged.

Curl request

```sh
curl -X POST \
"http://localhost:8093/evaluator/v1/libraries/math" \
-u Administrator:password \
-H 'content-type: application/json' \
-d 'function add(a, b) { let data = a + b; return data; }
    function sub(a, b) { let data = a - b; return data; }
    function mul(a, b) { let data = a * b; return data; }'
```

Request 7: Edit the function called `sub` to use a helper function called `helper`, leaving the other functions unchanged.

Curl request

```sh
curl -X POST \
"http://localhost:8093/evaluator/v1/libraries/math" \
-u Administrator:password \
-H 'content-type: application/json' \
-d 'function add(a, b) { let data = a + b; return data; }
    function mul(a, b) { let data = a * b; return data; }
    function sub(a, b) { return helper(a, b); }
    function helper(a, b) { return a - b; }'
```

Request 8: Remove the function called `sub` and the helper function called `helper`, leaving the other functions unchanged.

Curl request

```sh
curl -X POST \
"http://localhost:8093/evaluator/v1/libraries/math" \
-u Administrator:password \
-H 'content-type: application/json' \
-d 'function add(a, b) { let data = a + b; return data; }
    function mul(a, b) { let data = a * b; return data; }'
```

Request 9: Create or update a scoped library called `science`. The library contains one function, `f2c`.

Curl request

```sh
curl -X POST \
"http://localhost:8093/evaluator/v1/libraries/science?bucket=travel-sample&scope=inventory" \
-u Administrator:password \
-H 'content-type: application/json' \
-d 'function f2c(f) { return (5/9)*(f-32); }'
```

### [](#%5Fdelete%5Flibrary)Delete a Library

DELETE /evaluator/v1/libraries/{library}

#### [](#description-4)Description

Deletes the specified library entirely.

By default, this operation deletes a global library. For a scoped library, you must specify the bucket and scope.

> [!NOTE]
> Before you can delete a library, you must first drop all SQL++ external user-defined functions which point to any of the JavaScript functions within that library. For further details, refer to [DROP FUNCTION](../n1ql-language-reference/dropfunction.md).

#### [](#parameters-4)Parameters

| Type      | Name                   | Description                                                           | Schema |
| --------- | ---------------------- | --------------------------------------------------------------------- | ------ |
| **Path**  | **library** _required_ | The name of a library.                                                | string |
| **Query** | **bucket** _optional_  | For scoped libraries only. The bucket in which the library is stored. | string |
| **Query** | **scope** _optional_   | For scoped libraries only. The scope in which the library is stored.  | string |

> [!NOTE]
> To delete a scoped library, you must specify both the `bucket` and `scope` parameters. You cannot specify one without the other.

#### [](#responses-4)Responses

| HTTP Code | Description                                                                                                     | Schema |
| --------- | --------------------------------------------------------------------------------------------------------------- | ------ |
| **200**   | The operation was successful.                                                                                   | string |
| **400**   | Bad request. The path may not conform to the schema.                                                            | string |
| **404**   | Not found. The library name in the path may be incorrect, or the bucket and scope may be specified incorrectly. | string |

#### [](#security-4)Security

| Type      | Name                     |
| --------- | ------------------------ |
| **basic** | **[Global](#%5Fglobal)** |
| **basic** | **[Scope](#%5Fscope)**   |

#### [](#example-http-request-4)Example HTTP request

Request 10: Delete a global library entirely.

Curl request

```sh
curl -X DELETE \
"http://localhost:8093/evaluator/v1/libraries/math" \
-u Administrator:password
```

Request 11: Delete a scoped library entirely.

Curl request

```sh
curl -X DELETE \
"http://localhost:8093/evaluator/v1/libraries/science?bucket=travel-sample&scope=inventory" \
-u Administrator:password
```

## [](#%5Fdefinitions)Definitions

**Table of Contents**

* [Libraries](#%5Flibraries)
* [Functions](#%5Ffunctions)

### [](#%5Flibraries)Libraries

| Name                  | Description                                                                                                                                      | Schema |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ------ |
| **name** _required_   | The name of a library. **Example** : "math"                                                                                                      | string |
| **bucket** _required_ | For scoped libraries, the bucket in which the library is stored. For global libraries, this string is empty. **Example** : "travel-sample"       | string |
| **scope** _required_  | For scoped libraries, the scope in which the library is stored. For global libraries, this string is empty. **Example** : "inventory"            | string |
| **code** _required_   | The JavaScript code for all functions in the library. **Example** : "function add(a, b) { return a + b; } function mul(a, b) { return a \* b; }" | string |

### [](#%5Ffunctions)Functions

| Name                     | Description                                                                                                                                                                                           | Schema |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **_library_** _required_ | The JavaScript code for all functions in the library. The name of the property is the name of the library. **Example** : "function add(a, b) { return a + b; } function mul(a, b) { return a \* b; }" | string |

## [](#%5Fsecurityscheme)Security

The Functions API supports admin credentials. Credentials can be passed via HTTP headers (HTTP basic authentication).

### [](#%5Fglobal)Global

To manage global libraries, users must have the _Manage Global External Functions_ RBAC role.

This role enables you to create, read, update, or delete any global library, but does not give you access to any scoped libraries.

_Type_ : basic

### [](#%5Fscope)Scope

To manage scoped libraries, users must have the _Manage Scope External Functions_ RBAC role, with permissions on the specified bucket and scope.

This role enables you to create, read, update, or delete any library in the scope to which you have access, but does not give you access to any other scoped libraries. In addition, this role enables you to read any global library, but not to create, update, or delete them.

_Type_ : basic

Refer to [Roles](../../learn/security/roles.md) for more details.