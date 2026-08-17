---
title: Create a JavaScript Library
description: How to create a JavaScript library to store and organize your
  JavaScript functions.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/guides/pages/create-javascript-library.adoc
  xref: xref:server:guides:create-javascript-library.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/guides/create-javascript-library.html)

# Create a JavaScript Library

> How to create a JavaScript library to store and organize your JavaScript functions. 

## [](#introduction)Introduction

You can create a JavaScript library for storing JavaScript functions. Creating a JavaScript library for your JavaScript functions is optional, but simplifies organization and access control for user-defined functions.

If you want to try out the examples in this section, follow the instructions given in [Do a Quick Install](../getting-started/do-a-quick-install.md) to install Couchbase Server, configure a cluster, and load a sample dataset.

### [](#global-and-scoped-javascript-libraries)Global and Scoped JavaScript Libraries

A JavaScript library can be **global** or **scoped**.

* A **global** library is created within the `default:` namespace, at the same level as the buckets in your database. A global library is available to all users.
* A **scoped** library is created within a scope, at the same level as the collections within the scope. A scoped library is only available to users who have access to that bucket and scope. Use a scoped JavaScript library to keep the code for user-defined functions separate.

The name of a JavaScript library must be unique within the specified namespace or scope.

### [](#javascript-functions)JavaScript Functions

A JavaScript library can contain one or more JavaScript functions. The name of a JavaScript function must be unique within the JavaScript library.

For each JavaScript function, specify named parameters for any values you need to process or use. If you want your JavaScript function to take a variable length list of parameters, specify a rest parameter for the JavaScript function, such as `... args`.

After you create a JavaScript library and add JavaScript functions, you must create SQL++ user-defined functions to reference the JavaScript functions in the library, so they can be called as part of any SQL++ statement. A SQL++ user-defined function passes each argument it receives to the parameters in the JavaScript function.

## [](#creating-the-library-and-adding-your-first-function)Creating a JavaScript Library and Adding JavaScript Code

When you create a JavaScript library, you can add JavaScript functions to the library at the same time.

You can create a JavaScript library with the Couchbase Web Console or a REST API call.

* Couchbase Web Console
* REST API

To create a JavaScript library:

1. In the Couchbase Web Console, go to **Query** **UDF**.
2. Under **JavaScript Function Libraries**, click **\+ add function library**. The **Add Library** dialog is displayed.
3. In the **Namespace** drop-down list, select **(global)** for a global library, or select a bucket and scope for a scoped library.
4. In the **Library Name** box, enter a name for the library.
5. Specify **Parameters** for the function.
6. Edit the library to add your own JavaScript functions.
7. Click **Save**.

---

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

To create a JavaScript library with the Query Functions REST API:

1. Use the [POST /evaluator/v1/libraries/{library}](../n1ql-rest-functions/index.md#post%5Flibrary) endpoint.
2. Pass the name of the library as a path parameter.
3. To create a scoped library, pass the bucket and scope as query parameters.
4. Pass a string containing the JavaScript code for all functions in the library as the request body.

---

The following request creates a JavaScript library in the `inventory` scope within the `travel-sample` bucket.

```sh
curl -v -X POST  'http://localhost:8093/evaluator/v1/libraries/my-library?bucket=travel-sample&scope=inventory' \
 -u Administrator:password \
 -d 'function getBusinessDays(startDate, endDate) {
          let count = 0;
          const curDate = new Date(new Date(startDate).getTime());
          while (curDate <= new Date(endDate)) {
              const dayOfWeek = curDate.getDay();
              if(dayOfWeek !== 0 && dayOfWeek !== 6)
                  count++;
              curDate.setDate(curDate.getDate() + 1);
          }
          return count;
      }' 
```

## [](#add-functions-later)Updating an Existing JavaScript Library

You can add or edit functions in an existing JavaScript library with the Couchbase Web Console or a REST API call.

* Couchbase Web Console
* REST API

To add or edit functions in an existing JavaScript library:

1. In the Couchbase Web Console, go to **Query** **UDF**.
2. Under **JavaScript Function Libraries**, click **edit** next to the library that you want to update. The **Edit Library** dialog is displayed.
3. Update the library to add new JavaScript functions, edit existing JavaScript functions, or both.
4. Click **Save**.

---

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

To update an existing JavaScript library with the Query Functions REST API:

1. Use the [POST /evaluator/v1/libraries/{library}](../n1ql-rest-functions/index.md#post%5Flibrary) endpoint.
2. Pass the name of the library as a path parameter.
3. To update a scoped library, pass the bucket and scope as query parameters.
4. Pass a string containing the JavaScript code for all functions, including the added or edited functions, as the request body.

---

The following request updates a JavaScript library in the `inventory` scope within the `travel-sample` bucket.

```sh
curl -v -X POST 'http://localhost:8093/evaluator/v1/libraries/my-library?bucket=travel-sample&scope=inventory' \
 -u Administrator:password \
 -d 'function getBusinessDays(startDate, endDate) {
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
          args.forEach(value => sum = sum + value);
       return sum;
      }'
```

## [](#delete-udf)Deleting a JavaScript Library

Before you can delete a library, you must first drop all SQL++ user-defined functions which point to any of the JavaScript functions within that library. For more information, see [DROP FUNCTION](../n1ql/n1ql-language-reference/dropfunction.md).

You can delete a JavaScript library with the Couchbase Web Console or a REST API call.

* Couchbase Web Console
* REST API

To delete a JavaScript library:

1. In the Couchbase Web Console, go to **Query** **UDF**.
2. Under **JavaScript Function Libraries**, click **drop** next to the library that you want to delete. The **Confirm Drop Function Library** dialog is displayed.
3. Click **OK**.

To delete a JavaScript library with the Query Functions REST API:

1. Use the [DELETE /evaluator/v1/libraries/{library}](../n1ql-rest-functions/index.md#delete%5Flibrary) endpoint.
2. Pass the name of the library as a path parameter.
3. To delete a scoped library, pass the bucket and scope as query parameters.

---

The following request deletes a JavaScript library in the `inventory` scope within the `travel-sample` bucket.

```sh
curl -X DELETE 'http://localhost:8093/evaluator/v1/libraries/my-library?bucket=travel-sample&scope=inventory' \
-u Administrator:password
```

## [](#related-links)Related Links

Reference:

* [JavaScript Functions for Query Reference](../javascript-udfs/javascript-functions-with-couchbase.md)
* [Query Functions REST API](../n1ql-rest-functions/index.md)