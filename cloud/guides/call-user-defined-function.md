---
title: Call a User-Defined Function
description: How to call a user-defined function from SQL++ statements.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/guides/pages/call-user-defined-function.adoc
  xref: xref:cloud:guides:call-user-defined-function.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/guides/call-user-defined-function.html)

# Call a User-Defined Function

> How to call a user-defined function from SQL++ statements. 

## [](#introduction)Introduction

A user-defined function can be called like any other SQL++ function.

If you want to try out the examples in this section, follow the instructions given in [Create an Account and Deploy Your Free Tier Operational Cluster](../get-started/create-account.md) to create a free account, deploy a cluster, and load a sample dataset. Read the following for further information about the tools available for editing and executing queries:

* [cbq: The Command Line Shell for SQL++](../n1ql/n1ql-intro/cbq.md)
* [Query Tab](../clusters/query-service/query-workbench.md)

### [](#global-and-scoped-user-defined-functions)Global and Scoped User-Defined Functions

A user-defined function can be **global** or **scoped**.

* When you call a **global** function, any partial keyspace references within the function definition are resolved against the `default:` namespace, regardless of the current [query context](../n1ql/n1ql-intro/queriesandresults.md#query-context).
* When you call a **scoped** function, any partial keyspace references within the function definition are resolved against the function's bucket and scope, regardless of the current [query context](../n1ql/n1ql-intro/queriesandresults.md#query-context).

## [](#executing-a-sql-user-defined-function)Executing a SQL++ User-Defined Function

To execute a user-defined function:

1. If required, [set the query context](select.md#query-context) for a scoped function, or unset the context for a global function.
2. Use the `EXECUTE FUNCTION` statement and specify the name of the function.
3. Specify the function parameters within parentheses `()`.

The following query executes a function called `GetBusinessDays`, which was created in the current query context.

```sqlpp
EXECUTE FUNCTION GetBusinessDays("02/14/2025", "04/16/2025");
```

## [](#calling-a-sql-user-defined-function)Calling a SQL++ User-Defined Function

The SQL++ user-defined function can be used in any SQL++ statement in exactly the same way as a standard built-in function.

To call a user-defined function in any SQL++ statement:

1. If required, [set the query context](select.md#query-context) for a scoped function, or unset the context for a global function.
2. Specify the name of the function.
3. Specify the function parameters within parentheses `()`.

The following query calls the `GetBusinessDays` function, which was created in the current query context, from a `SELECT` statement.

```sqlpp
SELECT CASE
  WHEN GetBusinessDays('02/14/2025', '4/16/2025') > 40 THEN "late"
  ELSE "on time"
END
AS response; (1)
```

For more information and examples, see [User-Defined Functions](../n1ql/n1ql-language-reference/userfun.md).

## [](#related-links)Related Links

Reference:

* [JavaScript Functions for Query Reference](../javascript-udfs/javascript-functions-with-couchbase.md)
* [CREATE FUNCTION](../n1ql/n1ql-language-reference/createfunction.md)
* [EXECUTE FUNCTION](../n1ql/n1ql-language-reference/execfunction.md)
* [EXPLAIN FUNCTION](../n1ql/n1ql-language-reference/explainfunction.md)
* [DROP FUNCTION](../n1ql/n1ql-language-reference/dropfunction.md)
* [User-Defined Functions](../n1ql/n1ql-language-reference/userfun.md) — using user-defined functions (UDFs) in SQL++ statements

Administrator guides:

* [Monitor Functions](../n1ql/n1ql-intro/sysinfo.md#sys-functions)