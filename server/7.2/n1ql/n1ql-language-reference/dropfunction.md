[View original HTML](/server/7.2/n1ql/n1ql-language-reference/dropfunction.html)

> The `DROP FUNCTION` statement enables you to delete a user-defined function. 

## [](#rbac-privileges)RBAC Privileges

To manage global internal functions, you must have the **Manage Global Functions** role. To manage scoped internal functions, you must have the **Manage Scope Functions** role, with permissions on the specified bucket and scope.

To manage global external functions, you must have the **Manage Global External Functions** role. To manage scoped external functions, you must have the **Manage Scope External Functions** role, with permissions on the specified bucket and scope.

For more details about user roles, see [Authorization](../../learn/security/authorization-overview.md).

## [](#syntax)Syntax

```ebnf
drop-function ::= 'DROP' 'FUNCTION' function ( 'IF' 'EXISTS' )?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/drop-function.png) 

function

(Required) Refer to [Function Name](#name) below.

### [](#name)Function Name

```ebnf
function ::= ( namespace ':' ( bucket '.' scope '.' )? )? identifier
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/function.png) 

The name of the function. This is usually an unqualified identifier, such as `func1` or `` `func-1` ``. In this case, the path to the function is determined by the current [query context](../n1ql-intro/queriesandresults.md#query-context).

To delete a global function in a particular namespace, the function name must be a qualified identifier with a namespace, such as `default:func1`. Similarly, to delete a scoped function in a particular scope, the function name must be a qualified identifier with the full path to a scope, such as `` default:`travel-sample`.inventory.func1 ``. Refer to [Global Functions and Scoped Functions](createfunction.md#context) for more information.

|  | The name of a user-defined function _is_ case-sensitive, unlike that of a built-in function. You must delete the user-defined function using the same case that was used when it was created. |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#if-exists-clause)IF EXISTS Clause

The optional `IF EXISTS` clause enables the statement to complete successfully when the specified function doesn’t exist.

When the function does not exist within the specified context: \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]

* If this clause is not present, an error is generated.
* If this clause is present, the statement does nothing and completes without error.

## [](#usage)Usage

When you drop an external user-defined function, the JavaScript library and function on which the user-defined function depended are not deleted. This enables you to create a new user-defined function with a different name, or a different number of parameters, using the same JavaScript library and function.

To change or delete the JavaScript library and the JavaScript function, you must use the SQL++ Functions REST API. For details, refer to [Functions REST API](../n1ql-rest-api/functions.md).

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

Example 2\. Drop an external function

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

* To create user-defined functions, refer to [CREATE FUNCTION](createfunction.md).
* To execute user-defined functions, refer to [EXECUTE FUNCTION](execfunction.md).
* To include user-defined functions in an expression, refer to [User-Defined Functions](userfun.md).
* To view user-defined functions, refer to [Monitor Queries](../../manage/monitor/monitoring-n1ql-query.md#sys-functions).

---

[1](#%5Ffootnoteref%5F1). That is, you are dropping a global function, and the function does not exist within the specified namespace; or, you are dropping a scoped function, and the function does not exist within the specified scope.