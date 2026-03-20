---
title: Calling SQL++ from JavaScript
description: You can run SQL++ statements from inside the JavaScript code you
  use for a user-defined function.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/javascript-udfs/pages/calling-n1ql-from-javascript.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.6@server:javascript-udfs:calling-n1ql-from-javascript.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/javascript-udfs/calling-n1ql-from-javascript.html)

# Calling SQL++ from JavaScript

> You can run SQL++ statements from inside the JavaScript code you use for a user-defined function. 

User-defined functions support calling JavaScript and executing SQL++ statements together.

For more information about user-defined functions in Couchbase Server, see [User-Defined Functions for Queries](../guides/javascript-udfs.md).

## [](#calling-statements-inline)Calling SQL++ Statements Inline

You can embed a SQL++ statement directly in your JavaScript code:

```javascript
function addAirline() {
    var q = insert into airport values("1200", 
        {"id": 1200, 
            "type": "airline", 
            "name": "Couch Air", 
            "ca1": "Q5", "icao": "MLA", 
            "callsign": "COUCH-AIR", 
            "country": "United States"});
}
```

## [](#executing-sql-statements-using-the-n1ql-call)Executing SQL++ Statements Using the N1QL() Call

You can also execute a SQL++ statement by calling it from the `N1QL(…)` function.

```javascript
function addAirline() {
    var q = N1QL("insert into airport values(1200, " +
        "{\"id\": 1200," +
        " \"type\": \"airline\"," +
        " \"name\": \"Couch Air\"," +
        " \"ca1\": \"Q5\"," +
        " \"icao\": \"MLA\"," +
        " \"callsign\": \"COUCH-AIR\"," +
        " \"country\": \"United States\"})")
}
```

> [!NOTE]
> The `N1QL()` function generates the equivalent SQL++ call. You can choose to use either method and get the same results. The `N1QL()` function changes your available parameter support. See [Passing Parameters to SQL++ Statements](#pass-parameters).

## [](#side-effects)Side Effects

If you choose to use a SQL++ statement inside a JavaScript function, that function cannot have side effects that change data stored by Couchbase Server.

For example, in this SQL++ statement, the `AddAirline()` function attempts to alter data, which may be an unintended side effect. The statement returns an error:

```sqlpp
SELECT "true" AS response WHERE AddAirline() = "missing";
```

> [!IMPORTANT]
> Functions that change data must be called using the `EXECUTE FUNCTION` statement.

## [](#returning-values-from-sql-statements)Returning Values from SQL++ Statements

An embedded SQL++ statement can return values that you can use later in your JavaScript code for a user-defined function.

The values returned from statement calls are JavaScript [iterators](https://www.w3schools.com/js/js%5Fobject%5Fiterables.asp). Iterators are lists of values or documents returned from your operational cluster.

In the following example, the function `selectHotels()` retrieves a list of hotels stored in the `travel-sample`.`inventory`.`hotel` collection. It returns the list of hotels as an iterator. The iterator is stored in the variable, `q`. The function then iterates through each item in `q` to create and return a new result array, `res`:

```javascript
function selectHotels() {
    
    var q = SELECT * FROM `travel-sample`.`inventory`.`hotel`;    (1)
    var res = [];

    for (const doc of q) {   (2)
        
        res.push(doc);      (3)
        
    }
    
    return res;    (4)
    
}
```

> [!IMPORTANT]
> If an inline statement or SQL++ call does not return a value, then the associated SQL++ statement is executed as part of a synchronous operation. This means the runtime will wait until the statement completes before moving on to the next line of JavaScript.
> 
> If the inline statement or SQL++ call returns a value, then it’s executed asynchronously. Execution of the JavaScript continues before the iterator is returned. Each document is fetched from the bucket as it’s requested by the iterator.
> 
> ![inline-call-sequence](_images/inline-call-sequence-519984698fa53bcd24f4a50467d4acdeb4ec8965.svg)

## [](#pass-parameters)Passing Parameters to SQL++ Statements

You can pass parameters from your JavaScript code to your SQL++ statements. Parameters can either be **positional** or **named**.

Positional

The parameters are applied to the statement in the order they appear in the list. For example, in the following `addAirlineWithPositionalParameters` function, the `id` would be set as `1600`, type as `airline`, `name` to the supplied value of the `name` variable, and so on:

```javascript
function addAirlineWithPositionalParameters(name, callsign, country) {
    var q = N1QL("insert into `travel-sample`.`inventory`.`airport` values(\"1600\", " +
        "{\"id\": $1, " +
        "\"type\": $2, " +
        "\"name\": $3, " +
        "\"ca1\": $4, " +
        "\"icao\": $5, " +
        "\"callsign\": $6, " +
        "\"country\": $7})", 
        [1600, "airline", name, "Q5", "MLA", callsign, country])
}
```

Named

The parameters are given a mnemonic name attached to the value, so they can be included directly in the SQL++ statement. For example, in the following `addAirlineWithNamedParameters` function, the names of the parameters passed into the JavaScript function are used in the SQL++ statement, without needing to assign the parameters in a separate step. The parameters are assigned by prefixing the parameter names with a `$`:

```javascript
function addAirlineWithNamedParameters(name, callsign, country) {
    var q = insert into `travel-sample`.`inventory`.`airport` values("1700", 
        {"id": 1700, 
            "type": "airline", 
            "name": $name, 
            "ca1": "Q5", 
            "icao": "MLA", 
            "callsign": $callsign, 
            "country": $country});
}
```

Calling SQL++ from the `N1QL()` function supports both **named** and **positional** parameters. Calling a SQL++ statement or expression inline supports only **named** parameters.

| Call                       | Named Parameters | Positional Parameters |
| -------------------------- | ---------------- | --------------------- |
| Calling SQL++ using N1QL() | ✔️               | ✔️                    |
| Inline Calls               | ✔️               | ❌                     |

## [](#transactions)Transactions

Transactions are supported from SQL++ statements called from JavaScript functions.

Functions can:

* Run statements in a transaction that was started before the function was executed.
* Run a statement that starts the transaction.
* Run a statement that rolls back a transaction.

> [!NOTE]
> A SQL++ statement and its corresponding iterator must live entirely within the scope of a transaction. If a transaction is started during the iteration process, then the transaction cannot be rolled back entirely.
> 
> ![transactions-and-iterators](_images/transactions-and-iterators-e7a0ef29da863605ec653086aaa015f5fb6002f3.svg)

## [](#role-based-access-control-and-functions)Role-Based Access Control and Functions

To execute a SQL++ statement from a JavaScript function, you must have the correct permissions on your account to perform actions on any objects referenced in the SQL++ statement.

For more information about roles that control data access in Couchbase Server, see [Authorization](../learn/security/authorization-overview.md).

## [](#executing-sql-statements-that-call-functions)Executing SQL++ Statements That Call Functions

You can also create a JavaScript function that calls a SQL++ statement, which then calls another JavaScript function.

Be careful when nesting calls to multiple JavaScript functions. Each function call executed from a parent call uses a new JavaScript worker process to run. The deeper you nest your calls, the fewer JavaScript workers you will have available to execute those calls. Your calling chain will eventually fail and throw an error.

For example, if you used the following user-defined function, `doRecursion()`:

```javascript
function doRecursion() {
    
    var q = N1QL("EXECUTE FUNCTION doRecursion()")
    
}
```

Executing the function with the `EXECUTE FUNCTION` call would start an infinite recursion:

```sqlpp
EXECUTE FUNCTION doRecursion();
```

The function call would eventually return the following result, stopping the call after too many nested function calls exhausted the JavaScript workers:

```json
[
  {
    "code": 10109,
    "msg": "Error executing function 'doRecursion' (my-library:doRecursion)",
    "reason": {
      "details": {
        "Code": "    var q = N1QL(\"EXECUTE FUNCTION doRecursion()\")",
        "Exception": {
          "caller": "javascript:133",
          "code": 10112,
          "key": "function.nested.error",
          "message": "Error executing function 'doRecursion': 10 nested javascript calls"    (1)
        },
        "Location": "functions/my-library.js:30",
        "Stack": "   at doRecursion (functions/my-library.js:30:13)"
      },
      "type": "Exceptions from JS code"
    }
  }
]
```

> [!NOTE]
> JavaScript workers are created on your Couchbase cluster based on the following formula:
> 
> \\$"Number of JavaScript Workers" = 4 xx "Number of CPUs"\\$
> 
> Couchbase Server will automatically prevent recursive calls if there are fewer than 50% of the total JavaScript workers available.

## [](#see-also)See Also

* [Call JavaScript from SQL++](calling-javascript-from-n1ql.md)
* [Handling Errors in JavaScript Functions](handling-errors-javascript-udf.md)
* [EXECUTE FUNCTION](../n1ql/n1ql-language-reference/execfunction.md)
* [SQL++ for Query Reference](../n1ql/n1ql-language-reference/index.md)
* [Create Couchbase Transactions with SQL++](../guides/transactions.md)