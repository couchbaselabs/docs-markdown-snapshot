---
title: User-Defined Functions with JavaScript
description: How to extend the SQL++ query language by adding your own functions
  written in JavaScript.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/guides/pages/javascript-udfs.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:guides:javascript-udfs.adoc[]
---

[View original HTML](/server/current/guides/javascript-udfs.html)

# User-Defined Functions with JavaScript

> How to extend the SQL++ query language by adding your own functions written in JavaScript. 

## [](#introduction)Introduction

SQL++ includes a large number of built-in operations and functions that cover every aspect of data manipulation. User-defined functions enable you to create your own extensions to the language.

Using user-defined functions, you can:

* Create reuseable, domain-specific functions for use in your applications.
* Execute complex logic that may be difficult to do in SQL++.
* Migrate from RDBMS stored procedures.

## [](#user-defined-functions-with-javascript)User-Defined Functions with JavaScript

JavaScript supported in Couchbase shares the same constructs of the [ECMAScript](https://en.wikipedia.org/wiki/ECMAScript). However, you should be aware of the restrictions and extensions that come with the Couchbase implementation. These are covered in [JavaScript Functions for Query Reference](../javascript-udfs/javascript-functions-with-couchbase.md)

## [](#next-steps)Next Steps

If you’re looking to create your own JavaScript libraries, then there are a number of guides to get you started.

* [Creating a JavaScript Library](create-javascript-library.md)
* [Calling a User-Defined Function](call-user-defined-function.md)

If you wish to look into the constructs and available in the language itself, then you can have a look through the following pages:

* [JavaScript Functions for Query Reference](../javascript-udfs/javascript-functions-with-couchbase.md)
* [Calling JavaScript from SQL++](../javascript-udfs/calling-javascript-from-n1ql.md)
* [Calling SQL++ from JavaScript](../javascript-udfs/calling-n1ql-from-javascript.md)
* [Handling Errors in JavaScript Functions](../javascript-udfs/handling-errors-javascript-udf.md)