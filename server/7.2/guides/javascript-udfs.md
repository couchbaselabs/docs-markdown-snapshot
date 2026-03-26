---
title: User-defined Functions with JavaScript
description: How to extend the SQL++ query language by adding your own functions
  written in JavaScript.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/guides/pages/javascript-udfs.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:7.2@server:guides:javascript-udfs.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/guides/javascript-udfs.html)

# User-defined Functions with JavaScript

> How to extend the SQL++ query language by adding your own functions written in JavaScript.  
> This guide is for Couchbase Server.

## [](#introduction)Introduction

SQL++ includes a large number of [operations and generic functions](../n1ql/n1ql-language-reference/index.md) that cover every aspect of data manipulation. In addition to the built-in functions, Couchbase also allows you to create your own extensions to the language.

Using User-Defined Functions, you can:

* Create reuseable, domain-specific functions for use in your applications.
* Execute complex logic that may be difficult to do in SQL++.
* Migrate from RDBMS stored procedures.

## [](#user-defined-functions-with-javascript)User-Defined Functions with JavaScript

JavaScript supported in Couchbase shares the same constructs of the [ECMAScript](https://en.wikipedia.org/wiki/ECMAScript). However, you should be aware of the restrictions and extensions that come with the Couchbase implementation. These are covered in [JavaScript Functions with Couchbase](../javascript-udfs/javascript-functions-with-couchbase.md)

## [](#next-steps)Next Steps

If you're looking to create your own JavaScript libraries, then there are a number of guides to get you started.

* [Creating a JavaScript Library](create-javascript-library.md)
* [Calling a User-Defined Function](call-user-defined-function.md)

If you wish to look into the constructs and available in the language itself, then you can have a look through the following pages:

* [JavaScript Functions with Couchbase](../javascript-udfs/javascript-functions-with-couchbase.md)
* [Calling JavaScript from SQL++ User-Defined Functions](../javascript-udfs/calling-javascript-from-n1ql.md)
* [Calling SQL++ from JavaScript](../javascript-udfs/calling-n1ql-from-javascript.md)
* [Handling Errors in Javascript Functions](../javascript-udfs/handling-errors-javascript-udf.md)