---
title: DROP FUNCTION
description: The <code>DROP FUNCTION</code> statement enables you to delete a
  user-defined function.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/n1ql/pages/n1ql-language-reference/dropfunction.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:cloud:n1ql:n1ql-language-reference/dropfunction.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/n1ql/n1ql-language-reference/dropfunction.html)

# DROP FUNCTION

> The `DROP FUNCTION` statement enables you to delete a user-defined function. 

## [](#prerequisites)Prerequisites

* To manage user-defined functions on your operational cluster, you must have the [Project Owner](../../projects/project-roles.md#project-owner-role) or the [Cluster Data Reader/Writer](../../projects/project-roles.md#project-cluster-data-reader-writer) role.

## [](#syntax)Syntax

```ebnf
drop-function ::= 'DROP' 'FUNCTION' function ( 'IF' 'EXISTS' )?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/drop-function.png) 

| function | [Function Name](#name) |
| -------- | ---------------------- |

### [](#name)Function Name

```ebnf
function ::= ( namespace ':' ( bucket '.' scope '.' )? )? identifier
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/function.png) 

The name of the function. This is usually an unqualified identifier, such as `func1` or `` `func-1` ``. In this case, the path to the function is determined by the current [query context](../n1ql-intro/queriesandresults.md#query-context).

To delete a global function in a particular namespace, the function name must be a qualified identifier with a namespace, such as `default:func1`. Similarly, to delete a scoped function in a particular scope, the function name must be a qualified identifier with the full path to a scope, such as `` default:`travel-sample`.inventory.func1 ``. Refer to [Global Functions and Scoped Functions](createfunction.md#context) for more information.

You cannot have 2 functions with the same name in the same scope. You can have 2 functions in the same name across different scopes.

> [!NOTE]
> The name of a user-defined function _is_ case-sensitive, unlike that of a built-in function. You must delete the user-defined function using the same case that was used when it was created.

### [](#if-exists-clause)IF EXISTS Clause

The optional `IF EXISTS` clause enables the statement to complete successfully when the specified function doesn’t exist.

When the function does not exist within the specified context: \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]

* If this clause is not present, an error is generated.
* If this clause is present, the statement does nothing and completes without error.

## [](#usage)Usage

When you drop a user-defined function whose definition is stored in a UDF library, the library and function on which the user-defined function depended are not deleted. This enables you to create a new user-defined function with a different name, or a different number of parameters, using the same UDF library and JavaScript function.

To change or delete a UDF library or the JavaScript function code, see [Delete a User-Defined Function Library](../../guides/create-javascript-library.md#delete-udf).

When you drop an inline SQL++ user-defined function, the associated JavaScript function code is deleted also.

## [](#examples)Examples

Example 1\. Drop an inline function

This statement deletes an inline function called `celsius`.

```sqlpp
DROP FUNCTION celsius;
```

You can run the following query to check that the function is no longer available.

```sqlpp
SELECT * FROM system:functions;
```

Example 2\. Drop a SQL++ managed user-defined function

This statement deletes an inline SQL++ user-defined function called `add100`.

```sqlpp
DROP FUNCTION add100 IF EXISTS;
```

You can run the following query to check that the function is no longer available.

```sqlpp
SELECT * FROM system:functions;
```

Example 3\. Drop a UDF library function

These statements delete two UDF library functions:

1. A function called `geohash`, which depends on the JavaScript `encodeGeoHash` function in the `geohash-js` library;
2. A function called `adjacent`, which depends on the JavaScript `calculateAdjacent` function in the `geohash-js` library.

```sqlpp
DROP FUNCTION geohash;

DROP FUNCTION adjacent;
```

---

[1](#%5Ffootnoteref%5F1). That is, you are dropping a global function, and the function does not exist within the specified namespace; or, you are dropping a scoped function, and the function does not exist within the specified scope.