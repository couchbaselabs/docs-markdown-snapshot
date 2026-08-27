---
title: User-Defined Functions
description: In SQL++ for Capella Analytics, user-defined functions enable you
  to name and reuse complex or repetitive expressions, including subqueries, in
  order to simplify your queries.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/sqlpp/pages/9_udf.adoc
  xref: xref:analytics:sqlpp:9_udf.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/analytics/sqlpp/9_udf.html)

# User-Defined Functions

> In SQL++ for Capella Analytics, user-defined functions enable you to name and reuse complex or repetitive expressions, including subqueries, in order to simplify your queries. 

Each user-defined function belongs to a scope. Within a scope, a function is uniquely identified by its function signature: that is, its name and the number of parameters it takes. You can create more than one function with the same name in the same scope, as long as each function has a different number of parameters.

You can query the `Function` collection within the `System.Metadata` scope to get metadata about all existing user-defined functions.

> [!TIP]
> FUNCTION is a reserved keyword, so you need to delimit the identifier for the `Function` collection with backticks (``` `` ```).

## [](#creating-a-function)Creating a Function

##### CreateFunction

The `CREATE FUNCTION` command enables you to create a user-defined function. At present, Couchbase supports Internal Functions, which use SQL++ expressions to build functions, rather than using an external language such as Python.

!["CREATE" ( "OR" "REPLACE" )? "ANALYTICS"? "FUNCTION" QualifiedName "(" FunctionParameters? ")" ("IF" "NOT" "EXISTS")? "{" Query "}"](_images/CreateInternalFunction.png) 

This syntax enables you to create an internal user-defined function. You can think of this kind of SQL++ user-defined function as being a parameterized view.

### [](#function-name)Function Name

##### QualifiedName

![(DatabaseAndScopeName ".")? Identifier](_images/QualifiedName.png) 

##### DatabaseAndScopeName

![(Identifier ".")? Identifier](_images/DatabaseAndScopeName.png) 

The `QualifiedName` specifies the name of the function to create.

For information about how Capella Analytics organizes entities into a `database.scope.database_object` hierarchy and resolves names, see [Entities in Capella Analytics Services](1a%5Fentities.md).

### [](#parameter-list)Parameter List

##### FunctionParameters

![Identifier ( "," Identifier )* | "…​"](_images/FunctionParameters.png) 

The parameter list specifies parameters for the function. You delimit the list with parentheses `()`. You can specify named parameters for the function using a comma-separated list of identifiers.

If you specify named parameters for the function, then you must call the function with exactly the same number of arguments in your queries. If you specify no parameters, then you must call the function with no arguments.

To create a variadic function, that is, a function that you can call with any number of arguments or none, specify `...` as the only parameter.

### [](#function-body)Function Body

##### Query

![Expr | Selection](_images/Query.png) 

The function body defines the function. You delimit the function body with braces `{}`. It can contain any valid expression or subquery.

If you specified named parameters for the function, you can use them in the function body to represent arguments passed to the function at execution time. If the function is variadic, an array named `args` holds any arguments passed to the function at execution time.

The function body can refer to other collections or views, or to other functions in the same or other scopes. If a scope name was explicitly specified when creating the function, then that scope is the default scope for function calls or collection references within the function body.

Recursive function invocation is not permitted. The function body cannot refer to itself or to another user-defined function that calls this function indirectly.

### [](#checking-for-an-existing-function-and-replacing-a-function)Checking for an Existing Function and Replacing a Function

The optional `IF NOT EXISTS` keywords enable you to verify whether a user-defined function exists before creating it, and the optional `OR REPLACE` keywords enable you to redefine the function.

If a function with the same signature already exists within the specified scope, then:

* If the `OR REPLACE` keywords are present, replace the existing function.
* If the `OR REPLACE` keywords are not present, then:

  * If the `IF NOT EXISTS` keywords are present, the statement does nothing and completes without error.
  * If the `IF NOT EXISTS` keywords are not present, generate an error.

If the statement contains both the `OR REPLACE` keywords and the `IF NOT EXISTS` keywords, an error results.

### [](#user-defined-function-examples)User-Defined Function Examples

For simplicity, none of these examples implement any data validation.

##### Example 1: Function with expression body

This statement creates a function called `rstr`, which returns the specified number of characters from the right of a string. The function expects two named arguments: `vString`, which is the string to work with, and `vLen`, which is the number of characters to return. The body of the function is an expression based on the two arguments.

```SQL++
  CREATE FUNCTION rstr(vString, vLen)
     { substr(vString, length(vString) - vLen, vLen) };
```

**Test**

```SQL++
  rstr("Couchbase", 4);
```

**Result**

[
  "base"
]

##### Example 2: Function with subquery body

This statement creates a function called `total_spending` based on the `Commerce` [example data](../intro/examples.md). The function takes one parameter, a customer id. Using a subquery, the function returns the total spending of all orders placed by that customer.

```SQL++
  CREATE FUNCTION total_spending(id)
     { SELECT VALUE SUM(i.qty * i.price)
       FROM orders AS o UNNEST o.items AS i
       WHERE o.custid = id
     };
```

**Test**

```SQL++
  total_spending("C13");
```

**Result**

[
  13036.8
]

##### Example 3: Variadic function with expression body

This statement creates a function that can take any number of arguments. Using an expression, the function returns the number of arguments that are passed to it.

```SQL++
  CREATE FUNCTION count_my_args( ... )
     { array_count(args) };
```

**Test**

```SQL++
  count_my_args("Hello", "Goodbye");
```

Result

[
  2
]

##### Example 4: Variadic function containing a subquery

The body of this function is an expression that contains a subquery. The function takes a variable number of strings and returns the total length of all the strings.

```SQL++
  CREATE FUNCTION total_length(...)
     { array_sum(
         (SELECT VALUE length(a) FROM args AS a)
       )
     };
```

**Test**

```SQL++
  total_length("Hello", "Goodbye");
```

**Result**

[
  12
]

##### Example 5: Function with no parameters

This statement creates a function which returns the mathematical constant φ. The function takes no arguments.

```SQL++
 CREATE FUNCTION phi() { 2 * sin(radians(54)) };
```

Test

```SQL++
 phi();
```

Result

[
  1.618033988749895
]

##### Example 6: Replace a function

The following statement redefines the function so that it calculates φ using a different method.

```SQL++
 CREATE OR REPLACE FUNCTION phi() { (1 + sqrt(5)) / 2 };
```

Test

```SQL++
 phi();
```

Result

[
  1.618033988749895
]

## [](#transform-function)TRANSFORM FUNCTION

Capella Analytics supports lightweight transformations on incoming data destined for remote collections. You can use SQL++ `TRANSFORM` User-Defined Functions (UDFs) to declaratively transform data objects before they're stored in remote collections. The supported common transformations through UDFs include:

* Field operations and record filtering, such as:

  * Renaming fields.
  * Adding fields with static values.
  * Excluding specific fields.
  * Filtering records.
  * Flattening nested structures, using single-row nested aggregation.
* Value conversions, such as:

  * Type conversions including string to integer and timestamp formatting.
  * String manipulations including concatenation, lower/upper case, and substring.
  * Arithmetic transformations and creation of derived fields.

### [](#create-transform-function)Create TRANSFORM FUNCTION

A `TRANSFORM FUNCTION` is a specialized type of user-defined function (UDF) that's created using the `CREATE TRANSFORM FUNCTION` statement. Its purpose is to perform an automatic, on-the-fly transformation of incoming data.

For an UDF to be a valid `TRANSFORM FUNCTION`, you must have the following conditions:

* Only has a single argument: this argument is the incoming document, received from the data service/Kafka, which is passed to the function.
* Returns at most one value: the function should return at most one value for each input document. If for an input document, the function does not return any value, that document is skipped. In case the function returns a value, the value should be a valid document. The returned/transformed document is stored.
* Does not touch any collection/view: the function works only with the input document.

See the following examples:

Example

```sqlpp
CREATE TRANSFORM FUNCTION project_fields(input) {
	SELECT VALUE doc FROM (
	SELECT d.name, d.address FROM [input] d
) as doc
}
```

This function extracts only the `name` and `address` fields from each incoming document. The transformed document contains only these two fields.

Example

```sqlpp
CREATE OR REPLACE TRANSFORM FUNCTION CustomerTransform (cust)
{
SELECT VALUE doc FROM (
SELECT c.*,
         (c.address.street || ', ' || c.address.city || ', ' || c.address.zipcode) AS location
  FROM [cust] AS c ) as doc
};
```

This function transforms the customers mailing address into a single-line string. The transformed document contains all the original fields, plus a new field called `location`.

### [](#applying-transform-function-to-collections)Applying TRANSFORM FUNCTION to Collections

A `TRANSFORM FUNCTION` is applied to a remote collection to automatically process data as it is ingested from an external source. You do this by adding the `APPLY FUNCTION` clause to the `CREATE COLLECTION` statement.

See the following example:

Example

```sqlpp
CREATE COLLECTION remote_hotel ON hotel AT my_remote_link APPLY FUNCTION project_fields;
```

> [!NOTE]
> You cannot modify or drop a `TRANSFORM FUNCTION` while it's applied to any collection.

## [](#calling-a-function)Calling a Function

##### OrdinaryFunctionCall

![(DatabaseAndScopeName ".")? Identifier "(" Expr ("," Expr)* ")"](_images/OrdinaryFunctionCall.png) 

You can invoke a user-defined function in the same way as any other ordinary function. You can optionally prefix the name of the function with the names of the database and scope containing the function.

For information about how Capella Analytics organizes entities into a `database.scope.database_object` hierarchy and resolves names, see [Entities in Capella Analytics Services](1a%5Fentities.md).

After determining the database and scope, Capella Analytics tries to find a user-defined function with the same function signature within that scope. If a user-defined function cannot be found, Capella Analytics tries to find a built-in function with the same function name. If Capella Analytics cannot find a built-in function, the function call fails.

### [](#examples)Examples

The examples in this section assume that you're using the database and scope `sampleAnalytics.Commerce`. See [Example Data](../intro/examples.md) to install the Commerce dataset.

You can use [USE Statements](5%5Fddl%5Fuse.md) to set the default scope for the statement that follows it.

Example

```SQL++
  USE sampleAnalytics.Commerce;
```

If you're using the Capella Analytics UI, you can alternatively use the query editor's **Query Context** lists to set the database and scope.

![The Query Context lists](_images/workbench-context-set.png) 

Select `sampleAnalytics` as the database and `Commerce` as the scope for the following examples.

##### Example 9: Function with subquery

The following statement creates a function called `nameSearch`, which selects the customer name from all documents with the specified ID in the `customers` collection.

```SQL++
 CREATE FUNCTION nameSearch(customerId) {
   (SELECT VALUE c.name
   FROM customers AS c
   WHERE c.custid = customerId)[0]
 };
```

Test

```SQL++
 SELECT VALUE nameSearch("C25");
```

Result

[
  "M. Sinclair"
]

##### Example 10: Call a user-defined function

The following query uses the `nameSearch` function as a projection expression in a SELECT query. Compare this with example Q3.29 in the section on [Subqueries](3%5Fquery.html#Subqueries).

```SQL++
 SELECT o.orderno, o.custid,
       nameSearch(o.custid) AS name
 FROM orders AS o, o.items AS i
 WHERE i.itemno = 120;
```

Result

[
    {
        "orderno": 1003,
        "custid": "C31",
        "name": "B. Pruitt"
    },
    {
        "orderno": 1006,
        "custid": "C41",
        "name": "R. Dodge"
    }
]

## [](#dropfunction)Dropping a Function

##### DropFunction

!["DROP" "ANALYTICS"? "FUNCTION" QualifiedName "(" FunctionParameters? ")" ( "IF" "EXISTS" )?](_images/DropFunction.png) 

The `DROP FUNCTION` statement enables you to delete a user-defined function.

You cannot delete a user-defined function if there are any other user-defined functions that call this function, in this scope or any other scope.

### [](#function-name-2)Function Name

##### QualifiedName

![(DatabaseAndScopeName ".")? Identifier](_images/QualifiedName.png) 

##### DatabaseAndScopeName

![(Identifier ".")? Identifier](_images/DatabaseAndScopeName.png) 

The `QualifiedName` specifies the name of the function to delete.

For information about how Capella Analytics organizes entities into a `database.scope.database_object` hierarchy and resolves names, see [Entities in Capella Analytics Services](1a%5Fentities.md).

### [](#parameter-list-2)Parameter List

##### FunctionParameters

![Identifier ( "," Identifier )* | "…​"](_images/FunctionParameters.png) 

When you drop a function, you must specify the same number of parameters that you specified when you created the function. When dropping a variadic function, specify `...`.

### [](#checking-for-an-existing-function)Checking for an Existing Function

The optional `IF EXISTS` keywords enable you to verify whether the specified function or scope exists before dropping it.

* If you include these keywords, and the function name or scope is not found, the statement does nothing and completes without error.
* If you do not include these keywords, and the function name or scope is not found, Capella Analytics generates an error.

### [](#examples-2)Examples

The examples that follow assume that you have set `sampleAnalytics.Commerce` as the default database and scope.

##### Example 11: Drop a Function

This statement drops the function named `nameSearch`, if it exists.

```SQL++
 DROP FUNCTION nameSearch(customerId) IF EXISTS;
```

Run the following query to verify the availability of a function:

```SQL++
 SELECT * FROM Metadata.`Function`;
```

## [](#see-also)See Also

* [Entities in Capella Analytics Services](1a%5Fentities.md)
* [Access Data](../intro/examples.md)