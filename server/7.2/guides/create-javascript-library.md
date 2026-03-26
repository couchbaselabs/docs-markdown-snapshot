---
title: Creating a JavaScript Library
description: How to create a JavaScript library.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/guides/pages/create-javascript-library.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:7.2@server:guides:create-javascript-library.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/guides/create-javascript-library.html)

# Creating a JavaScript Library

> How to create a JavaScript library.  
> This guide is for Couchbase Server.

## [](#introduction)Introduction

In this guide you will learn how to create a library for storing JavaScript functions, and how to add a new function to the library.

If you want to try out the examples in this section, follow the instructions given in [Do a Quick Install](../getting-started/do-a-quick-install.md) to install Couchbase Server, configure a cluster, and load a sample dataset. Read the following for further information about the tools available for editing and executing queries:

* [cbq: The Command Line Shell for SQL++](../tools/cbq-shell.md)
* [Query Workbench](../tools/query-workbench.md)

## [](#creating-the-library-and-adding-your-first-function)Creating the Library and Adding Your First Function

You can use the Query Workbench UI or the REST API to create a library. The process for creating the library is as follows:

Sequence for Creating a JavaScript Library

@startuml
skinparam ComponentStyle rectangle
skinparam ActorStyle awesome

left to right direction

actor "developer" as user

note top of cAndA #Ivory
  The library and the first function
  are usually added in the same step.
end note

note right of cAndA #Ivory
  The library can be created in a global library
  which is accessible across the cluster,
  or it can be set to be accessible
  by users with access to a scope within a bucket.
end note

frame "Create library and add first function" as cAndA {
  [(1) Create library] as createLibrary
  [(2) Add the JavaScript function to the library] as addFunction
  createLibrary  --> addFunction
}

user --> createLibrary
[(3) Create SQL++ User-Defined Function] as createN1QL

addFunction --> createN1QL
createN1QL -->() end

note top of addFunction #Ivory
  The developer can add one or more
  functions to the library
end note
@enduml

**(1) Create library**

Create the library by creating the logical storage for the library.

**(2) Add the JavaScript function to the library**

Edit the library to add your JavaScript function.

**(3) Create SQL++ User-Defined Function**

The SQL++ User Defined Function is needed so that it can be called as part of SQL++ statements (such as `SELECT` and `EXECUTE FUNCTION`). Creating the SQL++ User-Defined Function is covered in [Creating a User-Defined Function](create-user-defined-function.md).

As shown in [Sequence for Creating a JavaScript Library](#create-library-udf-sequence), the library is created and the first function is added in the same step.

* Query Workbench
* REST API

1. Select **Query** to access the Query Workbench, then select **UDF** Query Workbench menu.  
![route to the user-defined functions screen](_images/javascript-udfs/navigate-to-udf-query.png)
2. Click on the **\+ add function library** link in the `Javascript Function Libraries` table to show the `Add Library` screen.
3. Select your `Namespace` from the drop-down lists. In this example, the namespace has been set to the `inventory` scope inside the `travel-sample` bucket. You also have the option of leaving the Namespace unset, which means the library will be accessible at the cluster level.  
![add scoped library](_images/javascript-udfs/add-scoped-library.png)  
A Note on Namespaces  
The `Namespace` defines the `scope` of the library within the containing bucket. (You can read about scopes [here](../tutorials/buckets-scopes-and-collections.md).) Setting the namespace means that functions in the library can only be called users who have their context set to the same scope.
4. Enter a name for the library in the `Library Name` field.
5. Add your own function to the library, for example:  
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
```
6. Save the library by pressing the **Save** button.  
> [!TIP]  
> You can, of course, create an empty library and add functions to it later.

1. Start a shell session.
2. Run a `curl` command to create a JavaScript library within a desired scope.  
```console  
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
The parameters in the URL denote that the function should reside in the `travel-sample` bucket, under the `inventory` scope within that bucket.

You have now created your JavaScript library. In the [next step](create-user-defined-function.md), you'll create an SQL++ User-Defined function that references your library function, so it can be called as part of any SQL++ statement.

## [](#further-reading)Further Reading

* [REST API: Create or Update Library](../n1ql/n1ql-rest-api/functions.md#%5Fpost%5Flibrary)
* [User-Defined Functions UI](../tools/udfs-ui.md)