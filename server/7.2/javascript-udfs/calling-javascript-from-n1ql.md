---
title: Calling JavaScript from SQL++ User-Defined Functions
description: Using a SQL++ User-Defined Function to call JavaScript functions.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/javascript-udfs/pages/calling-javascript-from-n1ql.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:7.2@server:javascript-udfs:calling-javascript-from-n1ql.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/javascript-udfs/calling-javascript-from-n1ql.html)

# Calling JavaScript from SQL++ User-Defined Functions

> Using a SQL++ User-Defined Function to call JavaScript functions. 

## [](#introduction)Introduction

Before you can call a JavaScript function, you must first create a SQL++ User-Defined Function to call it. The process to do this is explained in the [Creating the SQL++ User-Defined Function](../guides/create-user-defined-function.md#creating-the-n1ql-udf-function) section of our [User-defined Functions with JavaScript](../guides/javascript-udfs.md) guide.

If you are unfamiliar with creating User-Defined Functions to call JavaScript, then the [guide](../guides/javascript-udfs.md) is the best place to start.

In this section, we're going to take a closer look at concepts around SQL++ User-Defined Functions, such as variadic parameter lists.

## [](#scopes-and-sql-user-defined-functions)Scopes and SQL++ User-Defined Functions

A JavaScript function can be [created through the WorkBench or through the REST API](../guides/create-javascript-library.md#creating-the-library-and-adding-your-first-function).

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

And the corresponding SQL++ User-Defined Function can be created through the [Query Workbench](../guides/create-user-defined-function.md#creating-the-n1ql-udf-function) or by executing a SQL++ statement:

```sqlpp
CREATE FUNCTION default:`travel-sample`.`inventory`.GetBusinessDays(startDate, endDate) (1)
LANGUAGE JAVASCRIPT as "getBusinessDays" (2)
AT "travel-sample/inventory/my-library"; (3)
```

| **1** | The new SQL++ User-Defined Function is called GetBusinessDays and takes the inventory scope inside the travel-sample bucket. As well as providing a logical separation between JavaScript libraries, using scopes provides a means of securing access to the library: a user must have a context that matches the scope of the library in order to access it. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | This function will reference the getBusinessDays JavaScript function …                                                                                                                                                                                                                                                                                        |
| **3** | … in a library called my-library which is set to the inventory scope within the travel-sample bucket.                                                                                                                                                                                                                                                         |

### [](#global-library-path)Global Library Path

Of course, you can define the library at the cluster level, where it will be accessible to anyone who has access rights to the cluster. Functions in the global library are accessible across the cluster.

Creating a SQL++ User-Defined Function to access the JavaScript function in the global library

```sqlpp
CREATE FUNCTION GetBusinessDays(startDate, endDate)
LANGUAGE JAVASCRIPT as "getBusinessDays"
AT "my-library";  (1)
```

| **1** | There is no prefix path before my-library which means the library is a globally accessible library defined at the cluster level. |
| ----- | -------------------------------------------------------------------------------------------------------------------------------- |

### [](#relative-library-path)Relative Library Path

You can also use relative paths for the library location:

```sqlpp
CREATE FUNCTION GetBusinessDays(startDate, endDate)
LANGUAGE JAVASCRIPT as "getBusinessDays"
AT "./my-library";  (1)
```

| **1** | In this case, the User-Defined Function will be created for the JavaScript function under the current [query context](../tools/query-workbench.md#query-context). |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#calling-the-function)Calling the Function

Once the SQL++ User-Defined Function is defined, it can be called as if it were a built-in SQL++ function:

Query

```sqlpp
SELECT GetBusinessDays('02/14/2022', '4/16/2022');
```

which will return the following result:

Result

```json
[
  {
    "$1": 45
  }
]
```

You can also use the `EXECUTE FUNCTION` statement to execute the function:

```sqlpp
EXECUTE FUNCTION GetBusinessDays("02/14/2022", "04/16/2022");
```

or as part of a complex statement:

```n1ql
SELECT CASE 
  WHEN  GetBusinessDays('02/14/2022', '4/16/2022') > 44 THEN "true" 
  ELSE "false" 
  END 
  AS response;    (1)
```

## [](#variadic-parameters)Variadic Parameters

You can define a SQL++ User-Defined Function with a variadic parameter, which means that the parameter will accept a list of values which it will pass to the JavaScript function it references. We can create the `GetBusinessDays` function using a variadic parameter rather than the `startDate` and `endDate` parameters:

```sqlpp
CREATE FUNCTION GetBusinessDays(...)
LANGUAGE JAVASCRIPT as "getBusinessDays"
AT "my-library";
```

Note that the statement used three dots (…​) rather than a list of parameter list. This indicates a variable length parameter list. The underlying JavaScript function will reference the parameter list as named variables:

```javascript
function getBusinessDays(startDate, endDate) {
   
  // Do calculations  

}
```

You can also use a variable length parameter list in the JavaScript function itself:

```javascript
function sumListOfNumbers(... args) {    (1)
    
    var sum = 0;
    
    args.forEach(value => sum = sum  + value);    (2)
    
    return sum;
    
}
```

| **1** | JavaScript uses three dots (…​) followed by a parameter name to denote a parameter that is an array of values. |
| ----- | -------------------------------------------------------------------------------------------------------------- |
| **2** | Scans through the variadic parameter list, summing all the numbers it contains.                                |

A SQL++ User-Defined Function can now be created that takes a variable length list of numbers as an argument:

```sqlpp
CREATE FUNCTION SumListOfNumbers(...)
LANGUAGE JAVASCRIPT as "sumListOfNumbers"
AT "my-library";
```

which can then be called with a variable length list of numbers as a parameter

Query

```sqlpp
EXECUTE FUNCTION SumListOfNumbers(1, 2, 4, 8, 16, 32, 64);
```

Result

```json
[
  127
]
```