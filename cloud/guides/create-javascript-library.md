---
title: Create a JavaScript Library
description: How to create a JavaScript library to store and organize your
  JavaScript functions.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/guides/pages/create-javascript-library.adoc
pubDate: 2026-03-21T03:36:33.505Z
link: xref:cloud:guides:create-javascript-library.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/guides/create-javascript-library.html)

# Create a JavaScript Library

> How to create a JavaScript library to store and organize your JavaScript functions. 

## [](#introduction)Introduction

You can create a JavaScript library for storing JavaScript functions. Creating a JavaScript library for your JavaScript functions is optional, but simplifies organization and access control for user-defined functions.

A JavaScript library can be **global** or **scoped**.

* A **global** library is created within the `default:` namespace, at the same level as the buckets in your database. A global library is available to all clients.
* A **scoped** library is created within a scope, at the same level as the collections within the scope. A scoped library is only available to clients that have access to that bucket and scope. Use a scoped JavaScript library to keep the code for user-defined functions separate.

The name of a JavaScript library must be unique within the specified namespace or scope.

If you want to try out the examples in this section, follow the instructions given in [Create an Account and Deploy Your Free Tier Operational Cluster](../get-started/create-account.md) to create a free account, deploy a cluster, and load a sample dataset.

## [](#creating-the-library-and-adding-your-first-function)Creating a JavaScript Library and Adding JavaScript Code

When you create a JavaScript library, you can add JavaScript functions to the library at the same time.

To create a JavaScript library:

1. On the **Operational Clusters** page, select the operational cluster where you want to work with user-defined functions.
2. Go to **Data Tools** **Query**.
3. In the Data Insights area, to the left of the query editor, find the **Functions** section.
4. Next to the **Functions** section header, go to **Create (+)** **Library**.
5. In the **Library Name** field, enter a name for your new JavaScript library.
6. Choose the access level for your JavaScript library:

  * Choose **Global** for a global library.
  * Choose **Specific** and select a bucket and scope for a scoped library.
7. (Optional) Add functions to your JavaScript library.

  * To manually define functions for your library, on the **Define Functions** tab, enter the code for each function.
  * To import a `.js` file that contains function definitions, on the **Import Library** tab, drag and drop or choose your `.js` file.
8. Click **Create**.

The following library contains a JavaScript function called `getBusinessDays`.

```javascript
function getBusinessDays(startDate, endDate) {
    let count = 0;
    const curDate = new Date(new Date(startDate).getTime());
    while (curDate <= new Date(endDate)) {
        const dayOfWeek = curDate.getDay();
        if(dayOfWeek !== 0 && dayOfWeek !== 6)
            count++;
        curDate.setDate(curDate.getDate() + 1);
    }
    return count;    (1)
}
```

After you create a JavaScript library and add JavaScript code, you must create a SQL++ user-defined function to reference the JavaScript code in the library, so it can be called as part of any SQL++ statement.

## [](#add-functions-later)Updating an Existing JavaScript Library

To add or edit functions in an existing JavaScript library:

1. On the **Operational Clusters** page, select the operational cluster where you want to work with user-defined functions.
2. Go to **Data Tools** **Query**.
3. In the Data Insights area, to the left of the query editor, find the **Functions** section.
4. Next to the user-defined library that you want to update, go to **More Options (⋮)** **Edit**.
5. Update the library to add new JavaScript functions, edit existing JavaScript functions, or both.

  * To manually define functions for your library, on the **Create Functions** tab, enter or edit the code for each function.
  * To import a `.js` file that contains function definitions, on the **Import Library** tab, drag and drop or choose your `.js` file.
6. Click **Update**.

The following library contains JavaScript functions called `getBusinessDays` and `sumListOfNumbers`.

```javascript
function getBusinessDays(startDate, endDate) {
  let count = 0;
  const curDate = new Date(new Date(startDate).getTime());
  while (curDate <= new Date(endDate)) {
      const dayOfWeek = curDate.getDay();
      if(dayOfWeek !== 0 && dayOfWeek !== 6)
          count++;
      curDate.setDate(curDate.getDate() + 1);
  }
  return count;
}

function sumListOfNumbers(... args) {
  var sum = 0;
  args.forEach(value => sum = sum  + value);
  return sum;
}
```

## [](#delete-udf)Deleting a JavaScript Library

Before you can delete a library, you must first drop all SQL++ user-defined functions which point to any of the JavaScript functions within that library. For more information, see [DROP FUNCTION](../n1ql/n1ql-language-reference/dropfunction.md).

To delete a JavaScript library:

1. On the **Operational Clusters** page, select the operational cluster where you want to delete a JavaScript library.
2. Go to **Data Tools** **Query**.
3. In the Data Insights area, to the left of the query editor, find the **Functions** section.
4. Next to the JavaScript library that you want to delete, go to **More Options (⋮)** **Delete**.
5. Confirm that you want to delete your JavaScript library.
6. Click **Delete Library**.

## [](#related-links)Related Links

Reference:

* [JavaScript Functions for Query Reference](../javascript-udfs/javascript-functions-with-couchbase.md)