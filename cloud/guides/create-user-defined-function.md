---
title: Create a User-Defined Function
description: How to create a user-defined function (UDF) to call an inline
  function or a JavaScript function.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/guides/pages/create-user-defined-function.adoc
  xref: xref:cloud:guides:create-user-defined-function.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/guides/create-user-defined-function.html)

# Create a User-Defined Function

> How to create a user-defined function (UDF) to call an inline function or a JavaScript function. 

## [](#introduction)Introduction

If you want to try out the examples in this section, follow the instructions given in [Create an Account and Deploy Your Free Tier Operational Cluster](../get-started/create-account.md) to create a free account, deploy a cluster, and load a sample dataset. Read the following for further information about the tools available for editing and executing queries:

* [cbq: The Command Line Shell for SQL++](../n1ql/n1ql-intro/cbq.md)
* [Query Tab](../clusters/query-service/query-workbench.md)

### [](#global-and-scoped-user-defined-functions)Global and Scoped User-Defined Functions

A user-defined function can be **global** or **scoped**.

* A **global** user-defined function is created within the `default:` namespace, at the same level as the buckets in your database. A global user-defined function is available to all clients.
* A **scoped** user-defined function is created within a scope, at the same level as the collections within the scope. A scoped user-defined function is only available to clients that have access to that bucket and scope.

The name of a user-defined function must be unique within the specified namespace or scope.

### [](#user-defined-function-parameters)User-Defined Function Parameters

When you create a user-defined function, you can specify a list of parameters for any values you need to process or use in your function. If you want to create a user-defined function that can take a variable length list of parameters, you can create a **variadic** function.

## [](#create-inline)Creating an Inline User-Defined Function

To create a user-defined function that uses inline SQL++, use the Query Tab or a SQL++ statement.

* Query Tab
* SQL++

To create an inline user-defined function:

1. On the **Operational Clusters** page, select the operational cluster where you want to create a user-defined function.
2. Go to **Data Tools** **Query**.
3. In the Data Insights area, to the left of the query editor, find the **Functions** section.
4. Next to the **Functions** section header, go to **Create (+)** **Function**.
5. In the **Function Name** field, enter a name for the user-defined function.
6. Choose the access level for your user-defined function:

  * Choose **Global** for a global function.
  * Choose **Specific** and select a bucket and scope for a scoped function.
7. In the **Parameters** field, enter a list of parameters separated by commas (`,`) or specify `...` for a variadic function.
8. Click the **Inline SQL++** tab.
9. Enter a SQL++ expression as the body of the function.

  * If you specified named parameters for the user-defined function, use the same named parameters as identifiers in the SQL++ expression.
  * If the user-defined function is variadic, any arguments are passed to the SQL++ expression in an array called `args`.
10. Click **Create Function**.

To create an inline user-defined function:

1. If required, [set the query context](select.md#query-context) for a scoped function, or unset the context for a global function.
2. Use the `CREATE FUNCTION` statement and specify a name for the function.
3. Specify a list of parameter names separated by commas (`,`) or specify `...` for a variadic function.
4. Use the braces syntax `{}` or the `LANGUAGE INLINE AS` clause to specify a SQL++ expression as the body of the function.

  * If you specified named parameters for the user-defined function, use the same named parameters as identifiers in the SQL++ expression.
  * If the user-defined function is variadic, any arguments are passed to the SQL++ expression in an array called `args`.

---

Queries

The following query creates an inline SQL++ function in the current query context, using the braces syntax.

```sqlpp
CREATE FUNCTION rstr(vString, vLen) { SUBSTR(vString, LENGTH(vString) - vLen, vLen) };
```

The following query creates an inline SQL++ function in the current query context, using the `LANGUAGE INLINE` syntax.

```sqlpp
CREATE FUNCTION lstr(vString, vLen) LANGUAGE INLINE AS SUBSTR(vString, 0, vLen);
```

For more information, see [CREATE FUNCTION](../n1ql/n1ql-language-reference/createfunction.md).

## [](#create-sqlpp-managed-external-udf)Creating a User-Defined Function with SQL++ Managed JavaScript

To create a user-defined function that uses SQL++ managed JavaScript, use the Query Tab or a SQL++ statement.

* Query Tab
* SQL++

To create a user-defined function with SQL++ managed JavaScript:

1. On the **Operational Clusters** page, select the operational cluster where you want to create a user-defined function.
2. Go to **Data Tools** **Query**.
3. In the Data Insights area, to the left of the query editor, find the **Functions** section.
4. Next to the **Functions** section header, go to **Create (+)** **Function**.
5. In the **Function Name** field, enter a name for the user-defined function.
6. Choose the access level for your user-defined function:

  * Choose **Global** for a global function.
  * Choose **Specific** and select a bucket and scope for a scoped function.
7. In the **Parameters** field, enter a list of parameters separated by commas (`,`) or specify `...` for a variadic function.
8. Click the **Inline JavaScript** tab.
9. Enter a JavaScript function. The JavaScript function must have the same name as the SQL++ user-defined function.

  * If the user-defined function has named parameters, specify the same number of parameters for the JavaScript function.
  * If the user-defined function is variadic, specify a rest parameter for the JavaScript function, such as `... args`.
10. Click **Create Function**.

To create a user-defined function with SQL++ managed JavaScript:

1. If required, [set the query context](select.md#query-context) for a scoped function, or unset the context for a global function.
2. Use the `CREATE FUNCTION` statement and specify a name for the function.
3. Specify a list of parameter names separated by commas (`,`) or specify `...` for a variadic function.
4. Use the `LANGUAGE JAVASCRIPT AS` clause to define a JavaScript function. The JavaScript function must have the same name as the SQL++ user-defined function.

  * If the user-defined function has named parameters, specify the same number of parameters for the JavaScript function.
  * If the user-defined function is variadic, specify a rest parameter for the JavaScript function, such as `... args`.

---

Queries

The following query creates a SQL++ managed JavaScript function in the current query context.

```sqlpp
CREATE FUNCTION add100(num) LANGUAGE JAVASCRIPT AS
"function add100(param1) {return param1+100;}";
```

For more information, see [CREATE FUNCTION](../n1ql/n1ql-language-reference/createfunction.md).

## [](#creating-the-n1ql-udf-function)Creating a User-Defined Function with a JavaScript Library

If you have created a JavaScript function in a JavaScript library (see [Create a JavaScript Library](create-javascript-library.md)), you must create a SQL++ user-defined function to reference it.

If the JavaScript library is scoped, create a scoped user-defined function in the same scope as the library.

To create a user-defined function that references a JavaScript library, use the Query Tab or a SQL++ statement.

* Query Tab
* SQL++

To create a user-defined function that references a JavaScript library:

1. On the **Operational Clusters** page, select the operational cluster where you want to create a user-defined function.
2. Go to **Data Tools** **Query**.
3. In the Data Insights area, to the left of the query editor, find the **Functions** section.
4. Next to the **Functions** section header, go to **Create (+)** **Function**.
5. In the **Function Name** field, enter a name for the user-defined function.
6. Choose the access level for your user-defined function:

  * Choose **Global** for a global function.
  * Choose **Specific** to select a bucket and scope for a scoped function.
7. In the **Parameters** field, enter a list of parameters separated by commas (`,`) or specify `...` for a variadic function.
8. Click the **UDF Library** tab.
9. Choose the JavaScript library and the specific JavaScript function you want to assign to this user-defined function.

  * If the user-defined function has named parameters, the JavaScript function should accept the same number of parameters.
  * If the user-defined function is variadic, the JavaScript function should accept a rest parameter, such as `... args`.
10. Click **Create Function**.

To create a user-defined function that references a JavaScript library:

1. If required, [set the query context](select.md#query-context) for a scoped function, or unset the context for a global function.
2. Use the `CREATE FUNCTION` statement and specify a name for the function.
3. Specify a list of parameter names separated by commas (`,`) or specify `...` for a variadic function.
4. Use the `LANGUAGE JAVASCRIPT AS` clause to specify the name of the JavaScript function.

  * If the user-defined function has named parameters, the JavaScript function should accept the same number of parameters.
  * If the user-defined function is variadic, the JavaScript function should accept a rest parameter, such as `... args`.
5. Use the `AT` keyword to specify the library which contains the JavaScript function.

---

Queries

The following query creates a user-defined function within the current query context that references a global JavaScript library.

```sqlpp
CREATE FUNCTION GetBusinessDays(startDate, endDate)
LANGUAGE JAVASCRIPT as "getBusinessDays"
AT "my-library";
```

The following query creates a user-defined function within the current query context that references a scoped JavaScript library in the same query context.

```sqlpp
CREATE FUNCTION GetBusinessDays(startDate, endDate)
LANGUAGE JAVASCRIPT as "getBusinessDays"
AT "./my-library";
```

For more information, see [CREATE FUNCTION](../n1ql/n1ql-language-reference/createfunction.md).

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