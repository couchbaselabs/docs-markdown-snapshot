---
title: JavaScript Functions for Query Reference
description: This reference guide describes how to write extension functions for
  SQL++ for Query using the JavaScript language.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/javascript-udfs/pages/javascript-functions-with-couchbase.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/current/javascript-udfs/javascript-functions-with-couchbase.html)

# JavaScript Functions for Query Reference

> This reference guide describes how to write extension functions for SQL++ for Query using the JavaScript language. 

## [](#introduction)Introduction

There are two types of user-defined function in SQL++ for Query:

* Inline functions are defined using SQL++ expressions. They enable you to name and reuse complex or repetitive expressions, including subqueries, in order to simplify your queries.
* External functions are defined using an external language. They enable you to create functions that may be difficult or impossible to define using built-in SQL++ expressions. The only supported language is JavaScript.

This reference includes details of external functions using JavaScript.

### [](#libraries-and-scopes)External Libraries

You can store JavaScript functions in external libraries. This enables you to share external function code for use in more than one SQL++ user-defined function. A library can contain one or more JavaScript functions.

You must create the external library and the external function code using the [Query Workbench](../tools/udfs-ui.md) or the SQL++ [Functions REST API](../n1ql-rest-functions/index.md).

You do not call the external function code directly from SQL++. Instead, when you have created an external library and added a JavaScript function to it, you must define a SQL++ user-defined function to call the JavaScript function.

External libraries, like SQL++ user-defined functions, may be scoped or global. This enables you to keep the code for external functions separate where required.

![Global and scoped external libraries](_images/javascript-scopes-d2be9d48307d11d2ed9dfe25c52f4ffd387a18ac.svg) 

Figure 1\. Global and scoped external libraries

* A global library is created within a [namespace](../n1ql/n1ql-intro/queriesandresults.md#logical-hierarchy), at the same level as the buckets within the namespace.
* A scoped library is created within a [scope](../n1ql/n1ql-intro/queriesandresults.md#logical-hierarchy), at the same level as the collections within a scope.

You can apply access restrictions to scopes, so that only certain groups of users will be able to access collections and libraries within that scope.

Code which is stored in a scoped library is private to users of that scope, and is not visible or available to users of another scope. Code which is stored in a global library is available to users of all scopes.

A global library may have the same name as a scoped library, and scoped libraries may have the same name as each other. For example, you may have a global `math` library, and a `math` library in each scope.

![Calling a function in a scoped external library](_images/udf-scopes-diagram-3c4a25786bbff6f64ee29380a93b4b65796da01e.svg) 

Figure 2\. Calling a function in a scoped external library

In order to use a SQL++ user-defined function which calls external JavaScript code in a scoped library, you must set the [query context](../n1ql/n1ql-intro/queriesandresults.md#query-context) to the same bucket and scope as the scoped library.

### [](#sql-managed-user-defined-functions)SQL++ Managed User-Defined Functions

In Couchbase Server 7.6 and later, you can create the code for an external function and the corresponding SQL++ user-defined function in a single operation. This means that you don’t have to specify an external library and create the code for the external function, before creating the SQL++ user-defined function.

With a SQL++ managed user-defined function, the external function code is stored inline, along with the SQL++ user-defined function. You cannot share this external function code with other user-defined functions, or access it from any external libraries.

## [](#added-constructs)Added Constructs

JavaScript functions in SQL++ for Query support most of the language constructs available in [ECMAScript](https://en.wikipedia.org/wiki/ECMAScript), though there are a number of restrictions related to the Couchbase environment. There are also additions that have been made to the language for working specifically with Couchbase.

### [](#sql-embedded-statements)SQL++ Embedded Statements

Top level SQL++ keywords, such as SELECT, UPDATE, INSERT and DELETE, are available as inline keywords in functions. Operations that return values such as SELECT are accessible through a returned iterable handle. SQL++ Query results, via a SELECT, are streamed in batches to the iterable handle as the iteration progresses through the result set.

Example 1\. JavaScript code with embedded SQL++ statements

```javascript
function selectAirline(country) {

    var q = SELECT name as airline_name, callsign as airline_callsign 
    FROM `travel-sample`.`inventory`.`airline` 
    WHERE country = $country;  (1)

    var res = [];

    for (const doc of q) {

        var airline = {}
        airline.name = doc.airline_name  (2)
        airline.callsign = doc.airline_callsign  (2)
        res.push(airline);

    }

    return res;

}
```

| **1** | The SQL++ is written directly into the JavaScript code without having to be used as part of a function call. You can even provide parameters that can be used in the SQL++ statement. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | A standard JavaScript iterator is used to access the values returned from the SQL++ statement.                                                                                        |

For more details, see [Calling SQL++ from JavaScript](calling-n1ql-from-javascript.md).

## [](#unsupported-features)Unsupported Features

The following features are not supported in JavaScript functions for Query.

### [](#browser-extensions)Browser Extensions

Because JavaScript functions in SQL++ for Query do not execute in the context of a browser, the extensions that browsers add to the core language, such as window methods, DOM events, and so on, are not available.

### [](#global-state)Global State

All variables must be local to the function; global state is not permitted.

Example 2\. JavaScript code with global variable

```javascript
var count = 0;                         // Not allowed - global variable.
function increment() {
    count++;
}
```

Along with global state, global [arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow%5Ffunctions) are not supported. Arrow functions local to individual JavaScript functions are supported.

### [](#logging)Logging

Logging using the `console.log(..)` function is not supported.

## [](#restricted-features)Restricted Features

The following features are restricted in JavaScript functions for Query.

### [](#code-injection)Code Injection

JavaScript constructs that may allow for code injection have been removed:

* The `eval` symbol has been removed.
* The `Function` construct has been removed.

Example 3\. JavaScript code with the `eval` symbol

The following example does not compile as it uses the `eval` symbol.

```javascript
function evaluate() {
    var q = select jscode from <bucket> where meta().id = <docid>;
    let iter = q[Symbol.iterator]();
    let code = iter.next();
    let result = eval(code);
}
```

Example 4\. JavaScript code with the `Function` construct

The following example does not compile as it uses the `Function` construct.

```javascript
function dynamicfunction() {
var q = select jscode from <bucket> where meta().id = <docid>;
    let iter = q[Symbol.iterator]();
    let code = iter.next();
  return new Function("inject", code);
}

function evaluate() {
    dynamicfunction();
}
```

### [](#date-granularity)Date Granularity

The granularity of the `Date` object has been reduced to 1 second. This is to prevent a potential attacker from easily measuring the difference between a CPU cache miss and cache hit, hence taking advantage of side-channel attacks or speculative execution attacks.

Example 5\. JavaScript code with timestamp

The following example executes a SQL++ query to insert a document with a field containing the current timestamp. The timestamp is returned to the last second, rather than the most recent millisecond.

```javascript
function addOrder() {
    let curr = Date.now();
    N1QL('INSERT INTO orders VALUES (uuid(),{"time":'+ curr +'})')
}
```

Example 6\. JavaScript code with date comparison

The following example simulates sleep by blocking execution by the number of milliseconds passed as a function parameter. Since the `Date.Now()` function does not return the current time with millisecond granularity, the function may not work as expected.

```javascript
function sleep(milliseconds) {
  let init = Date.now();
  let curr = null;
  do {
     curr = Date.now();
   } while (curr - init < milliseconds);
}
```

## [](#see-also)See Also

User-Defined Function Guides

* [User-Defined Functions with JavaScript](../guides/javascript-udfs.md)
* [Monitor Functions](../n1ql/n1ql-intro/sysinfo.md#sys-functions)

SQL++ User-Defined Function Commands

* [CREATE FUNCTION](../n1ql/n1ql-language-reference/createfunction.md)
* [EXPLAIN FUNCTION](../n1ql/n1ql-language-reference/explainfunction.md)
* [EXECUTE FUNCTION](../n1ql/n1ql-language-reference/execfunction.md)
* [DROP FUNCTION](../n1ql/n1ql-language-reference/dropfunction.md)
* [User-Defined Functions](../n1ql/n1ql-language-reference/userfun.md)

External Libraries

* [User-Defined Functions UI](../tools/udfs-ui.md)
* [Query Functions REST API](../n1ql-rest-functions/index.md)

JavaScript Functions

* [Calling JavaScript from SQL++](calling-javascript-from-n1ql.md)
* [Calling SQL++ from JavaScript](calling-n1ql-from-javascript.md)
* [Handling Errors in JavaScript Functions](handling-errors-javascript-udf.md)