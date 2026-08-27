---
title: DROP FUNCTION
description: The <code>DROP FUNCTION</code> statement enables you to delete a
  user-defined function.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/n1ql/pages/n1ql-language-reference/dropfunction.adoc
  xref: xref:server:n1ql:n1ql-language-reference/dropfunction.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/n1ql/n1ql-language-reference/dropfunction.html)

# DROP FUNCTION

> The `DROP FUNCTION` statement enables you to delete a user-defined function. 

## [](#prerequisites)Prerequisites

| To manage …​              | You must have …​                                                                              |
| ------------------------- | --------------------------------------------------------------------------------------------- |
| Global inline functions   | **Manage Global Functions** role.                                                             |
| Scoped inline functions   | **Manage Scope Functions** role, with permissions on the specified bucket and scope.          |
| Global external functions | **Manage Global External Functions** role.                                                    |
| Scoped external functions | **Manage Scope External Functions** role, with permissions on the specified bucket and scope. |

For more information about user roles, see [Authorization](../../learn/security/authorization-overview.md).

## [](#syntax)Syntax

```ebnf
drop-function ::= 'DROP' 'FUNCTION' function ( 'IF' 'EXISTS' )?
```

![Syntax diagram: see source code listing](../_images/n1ql-language-reference/drop-function.png) 

| function | [Function Name](#name) |
| -------- | ---------------------- |

### [](#name)Function Name

```ebnf
function ::= ( namespace ':' ( bucket '.' scope '.' )? )? identifier
```

![Syntax diagram: see source code listing](../_images/n1ql-language-reference/function.png) 

The name of the function. This is usually an unqualified identifier, such as `func1` or `` `func-1` ``. In this case, the path to the function is determined by the current [query context](../n1ql-intro/queriesandresults.md#query-context).

To delete a global function in a particular namespace, the function name must be a qualified identifier with a namespace, such as `default:func1`. Similarly, to delete a scoped function in a particular scope, the function name must be a qualified identifier with the full path to a scope, such as `` default:`travel-sample`.inventory.func1 ``. For more information, see [Global Functions and Scoped Functions](createfunction.md#context).

> [!NOTE]
> The name of a user-defined function is case-sensitive, unlike that of a built-in function. You must delete the user-defined function using the same case that was used when it was created.

### [](#if-exists-clause)IF EXISTS Clause

The optional `IF EXISTS` clause enables the statement to complete successfully when the specified function does not exist.

When the function does not exist within the specified context: \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]

* If this clause is not present, an error is generated.
* If this clause is present, the statement does nothing and completes without error.

## [](#usage)Usage

When you drop a user-defined function whose definition is stored in a JavaScript library, the JavaScript library and function on which the user-defined function depended are not deleted. This enables you to create a new user-defined function with a different name, or a different number of parameters, using the same JavaScript library and function.

To change or delete a JavaScript library or the JavaScript function code, you must use the [Couchbase Web Console](../../guides/javascript-udfs.md) or the SQL++ [Functions REST API](../../n1ql-rest-functions/index.md).

When you drop a SQL++ managed JavaScript function, the associated JavaScript function code is also deleted.

## [](#examples)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Example 1\. Drop an inline function

This statement deletes an inline function called `celsius`.

```sqlpp
DROP FUNCTION celsius;
```

You can run the following query to check that the function is no longer available.

```sqlpp
SELECT * FROM system:functions;
```

Example 2\. Drop a SQL++ managed JavaScript function

This statement deletes a SQL++ managed JavaScript function called `add100`.

```sqlpp
DROP FUNCTION add100 IF EXISTS;
```

You can run the following query to check that the function is no longer available.

```sqlpp
SELECT * FROM system:functions;
```

Example 3\. Drop an external function

These statements delete two external functions:

1. A function called `geohash`, which depends on the JavaScript `encodeGeoHash` function in the `geohash-js` library;
2. A function called `adjacent`, which depends on the JavaScript `calculateAdjacent` function in the `geohash-js` library.

```sqlpp
DROP FUNCTION geohash;

DROP FUNCTION adjacent;
```

You can run the following command to check that the JavaScript `geohash-js` library and the `encodeGeoHash` and `calculateAdjacent` functions are still available.

```sh
curl -v -X GET \
http://localhost:8093/evaluator/v1/libraries/geohash-js \
-u Administrator:password
```

## [](#related-links)Related Links

* For an introduction to user-defined functions, see [User-Defined Functions for Queries](../../guides/javascript-udfs.md).
* For more information about JavaScript functions, see [JavaScript Functions for Query Reference](../../javascript-udfs/javascript-functions-with-couchbase.md).
* To manage JavaScript libraries, see [Query Functions REST API](../../n1ql-rest-functions/index.md).
* To create user-defined functions, see [CREATE FUNCTION](createfunction.md).
* To execute a user-defined function, see [EXECUTE FUNCTION](execfunction.md).
* To see the execution plan for a user-defined function, see [EXPLAIN FUNCTION](explainfunction.md).
* To include a user-defined function in an expression, see [User-Defined Functions](userfun.md).
* To monitor user-defined functions, see [Monitor Functions](../n1ql-intro/sysinfo.md#sys-functions).

---

[1](#%5Ffootnoteref%5F1). In other words, you're dropping a global function, and the function does not exist within the specified namespace; or, you're dropping a scoped function, and the function does not exist within the specified scope.