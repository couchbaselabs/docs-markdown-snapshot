---
title: User-Defined Functions for Queries
description: How to extend the SQL++ query language by adding your own
  user-defined functions.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/guides/pages/javascript-udfs.adoc
  xref: xref:7.6@server:guides:javascript-udfs.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/guides/javascript-udfs.html)

# User-Defined Functions for Queries

> How to extend the SQL++ query language by adding your own user-defined functions. 

## [](#introduction)Introduction

SQL++ includes built-in operations and functions for data manipulation. User-defined functions enable you to create your own extensions to the language.

With user-defined functions, you can:

* Create reusable, domain-specific functions for use in your applications.
* Execute complex logic that may be difficult to do in SQL++.
* Migrate from Relational Database Management System (RDBMS) stored procedures.

## [](#user-defined-functions-in-couchbase-server)User-Defined Functions in Couchbase Server

User-defined functions can be categorized based on the language used to define them, and the location where the function definitions are stored.

| Type                                                                      | Language   | Stored                  |
| ------------------------------------------------------------------------- | ---------- | ----------------------- |
| [Inline SQL++ Functions](#inline-functions)                               | SQL++      | Internally              |
| [SQL++ Managed JavaScript Functions](#sqlpp-managed-javascript-functions) | JavaScript | Internally              |
| [JavaScript Library Functions](#library-functions)                        | JavaScript | In JavaScript libraries |

User-defined functions written in JavaScript support the [ECMAScript](https://en.wikipedia.org/wiki/ECMAScript) standard, with some restrictions and extensions. For more information, see [JavaScript Functions for Query Reference](../javascript-udfs/javascript-functions-with-couchbase.md).

After you create your user-defined functions, you can call them like any other SQL++ function. For more information, see [Call a User-Defined Function](call-user-defined-function.md).

### [](#inline-functions)Inline SQL++ Functions

An inline SQL++ function is a user-defined function that executes a SQL++ expression. The SQL++ expression is stored internally by the Query Service.

For more information, see [Create an Inline User-Defined Function](create-user-defined-function.md#create-inline).

### [](#sqlpp-managed-javascript-functions)SQL++ Managed JavaScript Functions

A SQL++ managed JavaScript function is a user-defined function that executes a JavaScript function. The JavaScript function is stored internally by the Query Service. You do not need to create a JavaScript library to create and use SQL++ managed JavaScript functions.

If you create a user-defined function this way, you cannot group related functions or change access restrictions for multiple related functions at once.

For more information, see [Creating a User-Defined Function with SQL++ Managed JavaScript](create-user-defined-function.md#create-sqlpp-managed-external-udf).

### [](#library-functions)JavaScript Library Functions

A JavaScript library function is a user-defined function that executes a JavaScript function. The JavaScript function is stored in a JavaScript library.

A JavaScript library is a collection of JavaScript functions. JavaScript libraries keep your JavaScript functions organized and allow you to set access controls across multiple functions at once.

To create a JavaScript library function, you must first create a JavaScript library and add JavaScript functions to that library. For more information, see [Create a JavaScript Library](create-javascript-library.md).

After you create a JavaScript library, you must create user-defined functions to use the JavaScript functions in that library. The user-defined function creates a link between the JavaScript function in your library and SQL++, letting you call your JavaScript code. For more information, see [Creating a User-Defined Function with a JavaScript Library](create-user-defined-function.md#creating-the-n1ql-udf-function).

## [](#next-steps)Next Steps

User-defined function guides:

* [Create a JavaScript Library](create-javascript-library.md)
* [Create a User-Defined Function](create-user-defined-function.md)
* [Call a User-Defined Function](call-user-defined-function.md)