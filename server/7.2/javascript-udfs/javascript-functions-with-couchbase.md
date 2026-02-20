---
title: JavaScript Functions with Couchbase
description: Writing Couchbase extension functions in the JavaScript Language.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/javascript-udfs/pages/javascript-functions-with-couchbase.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:javascript-udfs:javascript-functions-with-couchbase.adoc[]
---

[View original HTML](/server/7.2/javascript-udfs/javascript-functions-with-couchbase.html)

# JavaScript Functions with Couchbase

> Writing Couchbase extension functions in the JavaScript Language. 

## [](#introduction)Introduction

SQL++ includes a large number of [operations and generic functions](../n1ql/n1ql-language-reference/index.md) that cover every aspect of data manipulation. In addition to the built-in functions, Couchbase also allows you to create your own extensions to the language.

Using User-Defined Functions, you can:

* Create reuseable, domain-specific functions for use in your applications.
* Execute complex logic that may be difficult to do in SQL++.
* Migrate from RDBMS stored procedures.

If you want to learn how to create JavaScript function libraries using the administration console and/or the REST-API then take a look at our [JavaScript UDF Guides](../guides/javascript-udfs.md).

## [](#added-constructs)Added Constructs

Javascript functions in Couchbase support most of the language constructs available in [ECMAScript](https://en.wikipedia.org/wiki/ECMAScript), though there are a number of restrictions related to the Couchbase environment. There are also additions that have been made to the language for working specifically with Couchbase.

### [](#sql-embedded-statements)SQL++ Embedded Statements

Top level SQL++ keywords, such as SELECT, UPDATE, INSERT and DELETE, are available as inline keywords in functions. Operations that return values such as SELECT are accessible through a returned iterable handle. SQL++ Query results, via a SELECT, are streamed in batches to the iterable handle as the iteration progresses through the result set.

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

| **1** | The SQL++ is written directly into the JavaScript code without having to be used as part of a function call. We can even provide parameters that can be used in the SQL++ statement. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **2** | A standard JavaScript iterator is used to access the values returned from the SQL++ statement.                                                                                       |

### [](#libraries-and-scopes)Libraries and Scopes

JavaScript functions are stored inside a _library_. A library can contain one or more functions, and can also be assigned to a scope, which allows libraries to be partitioned for logical grouping.

![Javascript UDFs Structure](_images/javascript-scopes-942a0479b50c9cb90c7c8053d318647b6b860056.svg) 

Figure 1\. Javascript UDFs Structure

As shown in [Figure 1](#javascript-scopes), a JavaScript function library can exist as:

* A global library accessible across the cluster.
* A library accessible within a scope.

> [!NOTE]
> You can find an introduction to scopes in our [Couchbase Tutorials](../tutorials/buckets-scopes-and-collections.md#scopes%5Fand%5Fcollections).

Furthermore, access restrictions can be applied to scopes, so that only certain groups of users will be able to access collections and libraries within that scope.

![Scopes for JavaScript Libraries](_images/udf-scopes-diagram-b6b9216c51680d8a8bcec3f3c5b132c20fa96eb4.svg) 

Figure 2\. Scopes for JavaScript Libraries

You do not call a JavaScript function directly — for example, `getBusinessDays(startDate, endDate)` as shown here. Instead, you must define a SQL++ User-Defined Function to act as a reference caller to the JavaScript function.

In Couchbase terminology, you would set the query context to `travel-sample.inventory` in order to run the functions in `my-library`.

## [](#unsupported-features)Unsupported Features

### [](#browser-extensions)Browser Extensions

Because JavaScript UDF functions do not execute in the context of a browser, the extensions that browsers add to the core language, such as window methods, DOM events etc. are not available.

### [](#global-state)Global State

All variables must be local to the function; global state is not permitted.

```javascript
var count = 0;                         // Not allowed - global variable.
function increment() {
    count++;
}
```

Along with global state, global [arrow functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow%5Ffunctions) are not supported. Arrow functions local to individual javascript functions are supported.

### [](#logging)Logging

Logging using the `console.log(..)` function is not supported.

In the rest of this section, we’re going to look at the concepts behind JavaScript User-Defined Functions:

* [Calling JavaScript from SQL++ User-Defined Functions](calling-javascript-from-n1ql.md)
* [Calling SQL++ from JavaScript](calling-n1ql-from-javascript.md)
* [Handling Errors in Javascript Functions](handling-errors-javascript-udf.md)