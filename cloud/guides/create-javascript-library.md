---
title: Create a User-Defined Function Library
description: Create an user-defined function (UDF) library to store and organize
  your JavaScript functions.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/guides/pages/create-javascript-library.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:guides:create-javascript-library.adoc[]
---

[View original HTML](/cloud/guides/create-javascript-library.html)

# Create a User-Defined Function Library

> Create an user-defined function (UDF) library to store and organize your JavaScript functions. 

To create a UDF library that you can use to [Create a User-Defined Function](create-user-defined-function.md):

1. [Create a User-Defined Function (UDF) Library](#creating-the-library-and-adding-your-first-function)
2. [Add Functions to a New User-Defined Function (UDF) Library](#add-functions-now)

Or, you can [Add Functions to an Existing User-Defined Function (UDF) Library](#add-functions-later).

## [](#creating-the-library-and-adding-your-first-function)Create a User-Defined Function (UDF) Library

To create a new UDF library from the Query Tab:

1. On the **Operational Clusters** page, select the operational cluster where you want to work with user-defined functions.
2. Go to **Data Tools** **Query**.
3. In the Data Insights area, to the left of the query editor, find the **Functions** section.
4. Next to the **Functions** section header, go to **Create (+)** **Library**.
5. In the **Library Name** field, enter a name for your new UDF library.
6. Choose the access level for your UDF library:

  1. Choose **Global** to allow all buckets and scopes on this cluster to use functions in this library.
  2. Choose **Specific** to choose a specific bucket and scope on this cluster that can use this library.  
  Use this bucket and scope as the namespace for [your user-defined function](create-user-defined-function.md) to use this library and its functions later.
7. (Optional) Add functions to your UDF library.  
> [!TIP]  
> Function names must be unique within your selected scope. You cannot have 2 functions with the same name inside your library. See [Add Functions to a New User-Defined Function (UDF) Library](#add-functions-now).
8. Click **Create**.

## [](#add-functions-now)Add Functions to a New User-Defined Function (UDF) Library

To add functions to your new UDF library while you create your library:

1. Do one of the following:

  1. To manually define functions for your library, on the **Define Functions** tab, enter the code for each function.
  2. To import a `.js` file that contains function definitions, on the **Import Library** tab, drag and drop or choose your `.js` file.  
  > [!TIP]  
  > Each function should have a unique assigned name inside your library’s chosen scope and follow the [ECMAScript](https://en.wikipedia.org/wiki/ECMAScript) standard.

## [](#add-functions-later)Add Functions to an Existing User-Defined Function (UDF) Library

To add or edit functions in an existing UDF library:

1. On the **Operational Clusters** page, select the operational cluster where you want to work with user-defined functions.
2. Go to **Data Tools** **Query**.
3. In the Data Insights area, to the left of the query editor, find the **Functions** section.
4. Next to the user-defined library where you want to add a function, go to **More Options (⋮)** **Edit**.
5. Do one of the following:

  1. To manually define functions for your library, on the **Create Functions** tab, enter or edit the code for each function.
  2. To import a `.js` file that contains function definitions, on the **Import Library** tab, drag and drop or choose your `.js` file.  
  > [!TIP]  
  > Each function should have aunique assigned name inside your library’s chosen scope and follow the [ECMAScript](https://en.wikipedia.org/wiki/ECMAScript) standard.
6. Click **Update**.

## [](#creating-functions-with-variable-length-parameter-lists)Creating Functions with Variable Length Parameter Lists

If you want to create a JavaScript function that can take a variable length list of parameters, rather than a fixed number of parameters:

1. Add a variable that starts with `…​` to your function - such as `…​ args`.
2. Define your user-defined function with a `…​` parameter.

You can then pass a variable length list of parameters from your user-defined function to your JavaScript function.

If you define your JavaScript function with all named variables but still want to use a variable length of parameters in your user-defined function:

1. Define your user-defined function with a `…​` parameter.

Your user-defined function will accept an array of values as a parameter. The user-defined function assigns each value it receives to the named variables in your JavaScript function.

For more information and examples, see [Variadic Parameters](../javascript-udfs/calling-javascript-from-n1ql.md#variadic-parameters).

## [](#delete-udf)Delete a User-Defined Function (UDF) Library

To delete an existing UDF library:

1. On the **Operational Clusters** page, select the operational cluster where you want to delete a UDF library.
2. Go to **Data Tools** **Query**.
3. In the Data Insights area, to the left of the query editor, find the **Functions** section.
4. Next to the user-defined library where you want to add a function, go to **More Options (⋮)** **Delete**.
5. Confirm that you want to delete your UDF library.
6. Click **Delete Library**.

## [](#next-steps)Next Steps

To use your JavaScript functions from SQL++ after you have added them to a library, see [Create a User-Defined Function](create-user-defined-function.md).