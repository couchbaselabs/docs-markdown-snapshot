---
title: Call JavaScript from SQL++
description: You can use user-defined functions (UDFs) to call JavaScript code
  from SQL++ queries.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/javascript-udfs/pages/calling-javascript-from-n1ql.adoc
pubDate: 2026-02-26T03:43:25.790Z
link: xref:7.6@server:javascript-udfs:calling-javascript-from-n1ql.adoc[]
---

[View original HTML](/server/7.6/javascript-udfs/calling-javascript-from-n1ql.html)

# Call JavaScript from SQL++

> You can use user-defined functions (UDFs) to call JavaScript code from SQL++ queries. 

For more information about user-defined functions in Capella, see [User-Defined Functions with JavaScript](../guides/javascript-udfs.md).

## [](#create-a-scoped-user-defined-function-with-sql)Create a Scoped User-Defined Function with SQL++

For example, the following JavaScript function calculates the number of business days between a given start date and end date:

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

You could define this JavaScript function as part of an [external library](../guides/create-javascript-library.md) or as a [SQL++ managed user-defined function](../guides/create-user-defined-function.md#create-inline).

If the JavaScript is already defined in an external library, you can [create the user-defined function](../guides/create-user-defined-function.md) from the Query tab or by running a SQL++ statement.

The following SQL++ statement creates the `GetBusinessDays` function inside the `travel-sample`.`inventory` namespace.

It references the `GetBusinessDays` function stored inside the `my-library` UDF library, also stored in `travel-sample`.`inventory`. `GetBusinessDays` becomes a **Scoped** function:

```sqlpp
CREATE FUNCTION default:`travel-sample`.`inventory`.GetBusinessDays(startDate, endDate) (1)
LANGUAGE JAVASCRIPT as "getBusinessDays" (2)
AT "travel-sample/inventory/my-library"; (3)
```

If you created this function, you cannot create another function called `GetBusinessDays` inside the `travel-sample`.`inventory`.`my-library` scope.

### [](#create-a-global-user-defined-function-with-sql)Create a Global User-Defined Function with SQL++

You can also define **Global** user-defined functions from the Query Workbench using SQL++. Any function added globally will be accessible across your cluster:

```sqlpp
CREATE FUNCTION GetBusinessDays(startDate, endDate)
LANGUAGE JAVASCRIPT as "getBusinessDays"
AT "my-library";  (1)
```

If you do not add a prefix before the library name in your SQL++ statement, the user-defined function will be created as a **Global** function. You cannot create another global function called `GetBusinessDays` on your cluster, but you can create a scoped function called `GetBusinessDays`.

### [](#create-a-user-defined-function-with-sql-and-a-relative-library-path)Create a User-Defined Function with SQL++ and a Relative Library Path

You can also use SQL++ and define a relative path for your external library location. If you use a relative path, the library location will resolve based on the current [query context](../n1ql/n1ql-intro/queriesandresults.md#query-context).

For example, the following SQL++ statement creates the user-defined function in `my-library`, relative to the current query context:

```sqlpp
CREATE FUNCTION GetBusinessDays(startDate, endDate)
LANGUAGE JAVASCRIPT as "getBusinessDays"
AT "./my-library";  (1)
```

Based on the current query context, you would not be able to create another function called `GetBusinessDays` in that scope.

## [](#call-a-user-defined-function-with-sql)Call a User-Defined Function with SQL++

After you create your user-defined function, you can call it like any built-in SQL++ function.

For example, you could use the following to call the `GetBusinessDays` function:

Query

```sqlpp
SELECT GetBusinessDays('02/14/2022', '4/16/2022');
```

The function would return the following result, in JSON format:

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

Or, you can call a function as part of a complex statement:

```n1ql
SELECT CASE 
  WHEN  GetBusinessDays('02/14/2022', '4/16/2022') > 44 THEN "true" 
  ELSE "false" 
  END 
  AS response;    (1)
```

## [](#variadic-parameters)Create and Call Functions with a Variadic Parameter

You can define user-defined functions with a **variadic parameter**. Variadic parameters accept a list of values, which they pass to your defined JavaScript function.

For example, you could define the `GetBusinessDays` function to use a variadic parameter, instead of setting both the `startDate` and `endDate` parameters:

```sqlpp
CREATE FUNCTION GetBusinessDays(...)
LANGUAGE JAVASCRIPT as "getBusinessDays"
AT "my-library";
```

You can add a variadic parameter to any user-defined function by using 3 periods (…​) instead of a list of parameters. The 3 periods indicate a variable length parameter list.

If you use a user-defined function that has a variadic parameter list, but the original JavaScript function has named variables, the JavaScript function still references the variadic parameter list as named variables:

```javascript
function getBusinessDays(startDate, endDate) {
   
  // Do calculations  

}
```

When you define your JavaScript function, you can also use a variable length parameter list.

For example, the following function iterates through a variadic parameter list, and returns the sum of all the numbers it contains:

```javascript
function sumListOfNumbers(... args) {    (1)
    
    var sum = 0;
    
    args.forEach(value => sum = sum  + value);    (2)
    
    return sum;
    
}
```

Then, you can create a user-defined function that takes a variable length list of numbers as an argument:

```sqlpp
CREATE FUNCTION SumListOfNumbers(...)
LANGUAGE JAVASCRIPT as "sumListOfNumbers"
AT "my-library";
```

You can then call the user-defined function in a query, with a variable length list of numbers as a parameter:

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