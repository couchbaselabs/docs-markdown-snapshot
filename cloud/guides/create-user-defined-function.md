---
title: Create a User-Defined Function
description: Create a user-defined function (UDF) to call an inline function or
  a specific JavaScript function stored in a library.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/guides/pages/create-user-defined-function.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:guides:create-user-defined-function.adoc[]
---

[View original HTML](/cloud/guides/create-user-defined-function.html)

# Create a User-Defined Function

> Create a user-defined function (UDF) to call an inline function or a specific JavaScript function stored in a library. 

For more information about how to create a UDF library, see [Create a User-Defined Function Library](create-javascript-library.md).

## [](#prerequisites)Prerequisites

* If you want to use cbq to create your user-defined function, you must complete the prerequisites for using cbq. For more information, see [Prerequisites](../n1ql/n1ql-intro/cbq.md#prerequisites).
* If you want to use libraries to organize your user-defined functions, you need to create a UDF library and add a JavaScript function. For more information, see [Create a User-Defined Function Library](create-javascript-library.md).

## [](#creating-the-n1ql-udf-function)Create a User-Defined Function From a UDF Library

To create a user-defined function that references a JavaScript function from a UDF library:

* Use the Query Tab.
* Use the SQL++ [CREATE FUNCTION](../n1ql/n1ql-language-reference/createfunction.md) statement, and reference the UDF library and JavaScript function.

* Query Tab
* SQL++

1. On the **Operational Clusters** page, select the operational cluster where you want to create a user-defined function from a UDF library.
2. Go to **Data Tools** **Query**.
3. In the Data Insights area, to the left of the query editor, find the **Functions** section.
4. Next to the **Functions** section header, go to **Create (+)** **Function**.
5. In the **Function Name** field, enter a name for your function.
6. Choose the access level for your user-defined function:

  1. Choose **Global** to allow all buckets and scopes on this cluster to use this function.
  2. Choose **Specific** to choose a specific bucket and scope on this cluster that can use this function.  
  > [!TIP]  
  > Choose the same access level and namespace as your UDF library for your user-defined function. Your function name must be unique in your selected namespace. Users must set this bucket and scope as their [query context](../n1ql/n1ql-intro/queriesandresults.md#query-context) to use this function later.
7. In the **Parameters** field, enter a list of parameters, separated by commas (`,`) for any values you need to process or use in your function.  
For example, if you created a JavaScript function that has a variable named `a`, you should add a parameter `a`.  
> [!TIP]  
> If you want to create a user-defined function that can take a variable length list of parameters, rather than a comma separated list of parameters, add `…​` as a parameter. Your function will accept an array of values as a parameter, and assign each value it receives to the named variables in your function.
8. Click the **UDF Library** tab.
9. Choose the UDF library and specific JavaScript function you want to assign to this user-defined function.
10. Click **Create Function**.

Execute a `CREATE FUNCTION` statement in cbq to create a user-defined function:

```sqlpp
CREATE FUNCTION default:`travel-sample`.`inventory`.GetBusinessDays(...) LANGUAGE JAVASCRIPT as "getBusinessDays" AT "travel-sample/inventory/my-library";
```

> [!TIP]
> Set the same namespace as your UDF library for your user-defined function. Your function name must be unique in your selected namespace. Users must set this bucket and scope as their [query context](../n1ql/n1ql-intro/queriesandresults.md#query-context) to use this function later.

For more information on the `CREATE FUNCTION` statement, see [CREATE FUNCTION](../n1ql/n1ql-language-reference/createfunction.md).

## [](#create-inline)Create an Inline User-Defined Function

To create a user-defined function that uses inline JavaScript or SQL++:

* Use the Query Tab.
* Use the SQL++ [CREATE FUNCTION](../n1ql/n1ql-language-reference/createfunction.md) statement.

* Query Tab
* SQL++

1. On the **Operational Clusters** page, select the operational cluster where you want to create a user-defined function.
2. Go to **Data Tools** **Query**.
3. In the Data Insights area, to the left of the query editor, find the **Functions** section.
4. Next to the **Functions** section header, go to **Create (+)** **Function**.
5. In the **Function Name** field, enter a name for your function.
6. Choose the access level for your user-defined function:

  1. Choose **Global** to allow all buckets and scopes on this cluster to use this function.
  2. Choose **Specific** to choose a specific bucket and scope on this cluster that can use this function.  
  > [!TIP]  
  > Your function name must be unique in your selected namespace. Users must set this bucket and scope as their [query context](../n1ql/n1ql-intro/queriesandresults.md#query-context) to use this function later.
7. In the **Parameters** field, enter a list of parameters, separated by commas (`,`) for any values you need to process or use in your function.  
For example, if you created a JavaScript function that has a variable named `a`, you should add a parameter `a`.  
> [!TIP]  
> If you want to create a user-defined function that can take a variable length list of parameters, rather than a comma separated list of parameters, add `…​` as a parameter. Your function will accept an array of values as a parameter, and assign each value it receives to the named variables in your function. You can also define your function with a variable length parameter list, by adding a variable to your function definition that starts with `…​` \- such as `…​ args`.
8. Click the **Inline SQL++** or **Inline JavaScript** tab.
9. Enter a SQL++ expression or JavaScript function.
10. Click **Create Function**.

Execute a `CREATE FUNCTION` statement in cbq to create an inline user-defined function:

Inline JavaScript

```sqlpp
CREATE FUNCTION celsius(...) LANGUAGE INLINE AS (args[0] - 32) * 5/9;
```

Inline SQL++

```sqlpp
CREATE FUNCTION locations(vActivity) { (
  SELECT id, name, address, city
  FROM landmark
  WHERE activity = vActivity) };
```

You cannot create 2 functions with the same name inside the same namespace.

For more information about the `CREATE FUNCTION` statement, see [CREATE FUNCTION](../n1ql/n1ql-language-reference/createfunction.md).

## [](#next-steps)Next Steps

* To use your new user-defined function from SQL++, see [Call a User-Defined Function](call-user-defined-function.md).