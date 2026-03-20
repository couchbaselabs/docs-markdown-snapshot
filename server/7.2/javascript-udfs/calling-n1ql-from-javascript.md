---
title: Calling SQL++ from JavaScript
description: Executing SQL++ statements from Javascript functions.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/javascript-udfs/pages/calling-n1ql-from-javascript.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:javascript-udfs:calling-n1ql-from-javascript.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/javascript-udfs/calling-n1ql-from-javascript.html)

# Calling SQL++ from JavaScript

> Executing SQL++ statements from Javascript functions. 

## [](#introduction)Introduction

As well as being able to call JavaScript functions from SQL++, you can also call SQL++ statements from inside your Javascript functions.

## [](#calling-statements-inline)Calling SQL++ statements inline

You can embed a SQL++ statement directly in your Javascript code:

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

## [](#executing-sql-statements-using-the-n1ql-call)Executing SQL++ statements using the N1QL() call

In addition, you can also execute a SQL++ statement by calling it from the `N1QL(…)` function.

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
> Behind the scenes, the inline call method will generate the equivalent `SQL++` call, so whichever you choose to use will come down to personal preference.

## [](#side-effects)Side Effects

Functions executed as part of expressions cannot have side effects that will change data stored by the Couchbase engine. For example, this statement:

```sqlpp
SELECT "true" AS response WHERE AddAirline() = "missing";
```

will generate an error because the `AddAirline()` function will attempt to alter data, which the caller may be unaware of.

> [!IMPORTANT]
> Functions that change data must be called using the `EXECUTE FUNCTION` statement.

## [](#returning-values-from-sql-statements)Returning values from SQL++ statements

As shown in the [examples above](#calling-statements-inline), embedded SQL++ statements return values which can be used later on in your code.

The values returned from the statement calls are Javascript [iterators](https://www.w3schools.com/js/js%5Fobject%5Fiterables.asp): lists of values or documents returned from the database. In the next example, we’re going to retrieve a list of the hotels stored in the `travel-sample` database:

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

| **1** | The SQL++ statement returns an iterator containing the items retrieved by the query.    |
| ----- | --------------------------------------------------------------------------------------- |
| **2** | Using the standard Javascript iterator pattern to loop through the items returned in q. |
| **3** | Add the current document from the iterator to the result array res.                     |
| **4** | Once all the items have been retrieved, return the result array.                        |

> [!IMPORTANT]
> If an inline statement/SQL++ call does not return a value, then the associated SQL++ statement is executed as part of a synchronous operation. i.e. the runtime will wait until the statement completes before moving on to the next line of Javascript.
> 
> If the inline statement/SQL++ call returns a value then it is executed _asynchronously_: execution continues before the iterator is returned. Each document is fetched from the bucket as it requested by the iterator.
> 
> ![inline-call-sequence](_images/inline-call-sequence-519984698fa53bcd24f4a50467d4acdeb4ec8965.svg)

## [](#passing-parameters-to-sql-statements)Passing Parameters to SQL++ statements

You can pass parameters from your Javascript to your SQL++ statements. Parameters can either be _positional_ or _named_.

Positional

The parameters are applied to the statement in the order they appear in the list.

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

The parameters are given a mnemonic name attached to the value, so they can be included directly in the SQL++ statement.

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

> [!NOTE]
> The names of the parameters passed into the Javascript function are used in the SQL++ statement without any need to assign the parameters in a separate step.

SQL++ calls support both _named_ and _positional_ parameters. Inline calls only support named parameters.

| Call         | Named Parameters | Positional Parameters |
| ------------ | ---------------- | --------------------- |
| SQL++ calls  | ✔️               | ✔                     |
| Inline Calls | ✔️               | ❌                     |

## [](#transactions)Transactions

Transactions are supported from SQL++ statements called from Javascript functions.

* The function can run statements in a transaction that was started before the function was executed.
* The function can run a statement that starts the transaction.
* The function can run a statement that rolls back a transaction.

> [!NOTE]
> A SQL++ statement and its corresponding iterator must live entirely within the scope of a transaction. If a transaction is started during the iteration process, then the transaction cannot be rolled back entirely.
> 
> ![transactions-and-iterators](_images/transactions-and-iterators-e7a0ef29da863605ec653086aaa015f5fb6002f3.svg)

## [](#role-based-access-control)Role-Based Access Control

In order to execute SQL++ statements as part of a Javascript function, the user executing the function must have the appropriate privileges to perform the action on any objects referenced in the SQL++ statement.

## [](#executing-sql-statements-that-call-functions)Executing SQL++ statements that call functions

It is often the case that Javascript function will call a SQL++ statement that may itself call another Javascript function. However, it is important to be aware that each Javascript function call executed from a parent call will use a new Javascript worker process to run. The deeper the calls are nested, the fewer Javascript workers are available to run, so the calling chain will eventually fail and throw an error. This can be demonstrated using a recursive call sequence as shown below:

```javascript
function doRecursion() {
    
    var q = N1QL("EXECUTE FUNCTION doRecursion()")
    
}
```

Then executing the function:

```sqlpp
EXECUTE FUNCTION doRecursion();
```

returns the following result:

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

| **1** | The call failed after 10 nested call, which exhausted the number of Javascript workers available during the call sequence. |
| ----- | -------------------------------------------------------------------------------------------------------------------------- |

> [!NOTE]
> The JavaScript workers are created when the Couchbase server is started up.
> 
> \\$"Number of JavaScript Workers" = 4 xx "Number of CPUs"\\$
> 
> The service will automatically prevent recursive calls if there are less than 50% javascript workers available

## [](#further-reading)Further Reading

* [SELECT Clause](../n1ql/n1ql-language-reference/selectclause.md)
* [EXECUTE FUNCTION](../n1ql/n1ql-language-reference/execfunction.md)
* [Transactions](../learn/data/transactions.md)
* [Role-Based Access Control (RBAC)](../rest-api/rbac.md)