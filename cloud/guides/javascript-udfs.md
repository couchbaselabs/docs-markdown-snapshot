---
title: User-Defined Functions with JavaScript
description: Couchbase Capella lets you extend the SQL++ query language by
  adding your own functions written in JavaScript.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/guides/pages/javascript-udfs.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/cloud/guides/javascript-udfs.html)

# User-Defined Functions with JavaScript

> Couchbase Capella lets you extend the SQL++ query language by adding your own functions written in JavaScript. 

On its own, SQL++ includes built-in operations and functions for data manipulation. You can use user-defined functions to create your own extensions to the language.

With user-defined functions, you can:

* Create reusable, domain-specific functions for use in your applications.
* Execute complex logic that may be difficult to do in SQL++.
* Migrate from Relational Database Management System (RDBMS) stored procedures.

Couchbase Capella’s user-defined functions are defined with JavaScript, specifically the [ECMAScript](https://en.wikipedia.org/wiki/ECMAScript) standard, with some restrictions and extensions. For more information, see [JavaScript Functions for Query Reference](../javascript-udfs/javascript-functions-with-couchbase.md).

## [](#using-user-defined-functions-in-capella)Using User-Defined Functions in Capella

You cannot call JavaScript code directly from a SQL++ query. You must create a user-defined function to call JavaScript code in your queries.

You can create 2 types of user-defined functions:

* [Inline SQL++ or JavaScript functions](#inline-functions).
* [User-defined function (UDF) library functions](#library-functions).

Creating a UDF library for your JavaScript functions is optional, but simplifies organization and access control for user-defined functions.

After you have created your user-defined functions, you can [Call a User-Defined Function](call-user-defined-function.md) like any other SQL++ function.

### [](#inline-functions)Inline Functions

You can create a user-defined function that executes inline SQL++ commands or inline JavaScript. You do not need to create a UDF library before you can create and use inline functions.

If you create a user-defined function this way, you cannot group related functions or change cluster access restrictions for multiple related functions at once.

For more information about how to create inline functions, see [Create an Inline User-Defined Function](create-user-defined-function.md#create-inline).

### [](#library-functions)Functions From User-Defined Function (UDF) Libraries

A UDF library is a collection of JavaScript functions. UDF libraries keep your JavaScript functions organized and allow you to set access controls across multiple functions at once.

You can define functions [while creating a library](create-javascript-library.md#add-functions-now) or [add them to an existing library](create-javascript-library.md#add-functions-later).

After you have [created a UDF library](create-javascript-library.md), you must [create user-defined functions](create-user-defined-function.md) to use the JavaScript functions in that library. The user-defined function creates a link between the JavaScript function in your library and SQL++, letting you call your JavaScript code.

## [](#next-steps)Next Steps

* To get started with a UDF library, see [Create a User-Defined Function Library](create-javascript-library.md).
* To create inline functions, see [Create a User-Defined Function](create-user-defined-function.md).
* To start using your functions in the Query Tab, see [Call a User-Defined Function](call-user-defined-function.md).

For more information about the specifics of JavaScript for user-defined functions in Capella, see:

* [JavaScript Functions for Query Reference](../javascript-udfs/javascript-functions-with-couchbase.md)
* [Call JavaScript from SQL++](../javascript-udfs/calling-javascript-from-n1ql.md)
* [Calling SQL++ from JavaScript](../javascript-udfs/calling-n1ql-from-javascript.md)
* [Handling Errors in JavaScript Functions](../javascript-udfs/handling-errors-javascript-udf.md)