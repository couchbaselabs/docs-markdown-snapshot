---
title: User-Defined Functions
description: A description of user-defined functions in Couchbase SQL++ for Analytics.
editUrl: https://github.com/couchbase/docs-analytics/edit/release/7.2/modules/analytics/pages/9_udf.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:7.2@server:analytics:9_udf.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/analytics/9_udf.html)

# User-Defined Functions

In SQL++ for Analytics, user-defined functions enable you to name and reuse complex or repetitive expressions, including subqueries, in order to simplify your queries.

Each user-defined function belongs to an Analytics scope. Within an Analytics scope, a function is uniquely identified by its _function signature_: that is, its name and the number of parameters it takes. You can create more than one function with the same name in the same Analytics scope, as long as each function has a different number of parameters.

You can query the `Function` Analytics collection within the `Metadata` Analytics scope to get metadata about all existing user-defined functions. Note that FUNCTION is a reserved keyword, so you need to delimit the name of the `Function` collection with backticks (\`).

You can't create a function in the `Metadata` scope.

## [](#creating-a-function)Creating a Function

##### CreateFunction

![CreateInternalFunction | CreateExternalFunction](_images/diagrams/CreateFunction.png) 

The CREATE ANALYTICS FUNCTION command enables you to create a user-defined function. There are two types of user-defined function: _internal_ functions, which are defined using SQL++ for Analytics expressions; and _external_ functions, which are defined using an external language.

### [](#internal-functions)Internal Functions

##### CreateInternalFunction

!["CREATE" ( "OR" "REPLACE" )? "ANALYTICS" "FUNCTION" QualifiedName "(" FunctionParameters? ")" ("IF" "NOT" "EXISTS")? "{" Query "}"](_images/diagrams/CreateInternalFunction.png) 

This syntax enables you to create an internal user-defined function.

### [](#function-name)Function Name

##### QualifiedName

![(ScopeName ".")? Identifier](_images/diagrams/QualifiedName.png) 

##### ScopeName

![(Identifier ".")? Identifier](_images/diagrams/ScopeName.png) 

The `QualifiedName` specifies the name of the function to create. It consists of an optional scope name, followed by an identifier which represents the local name of the function.

The optional `ScopeName` specifies the Analytics scope where the function is located. It may consist of one or two identifiers, separated by a dot.

If you don't specify an Analytics scope, then the scope containing the function is resolved according to the following rules:

1. If there is a preceding USE statement, the function is located in the Analytics scope specified by the USE statement.
2. Otherwise, if the [query\_context](appendix%5F3%5Fresolution.md#Query%5Fcontext) parameter is set, the function is located in the Analytics scope specified by the query context.
3. Otherwise, the function is located in the `Default` Analytics scope.

### [](#parameter-list)Parameter List

##### FunctionParameters

![Identifier ( "," Identifier )* | "…​"](_images/diagrams/FunctionParameters.png) 

The parameter list specifies parameters for the function. It is delimited by parentheses `()`. You can specify named parameters for the function using a comma-separated list of identifiers.

If you specify named parameters for the function, then you must call the function with exactly the same number of arguments at execution time. If you specify no parameters, then you must call the function with no arguments.

To create a variadic function, that is, a function which you can call with any number of arguments or none, specify `...` as the only parameter.

### [](#function-body)Function Body

##### Query

![Expr | Selection](_images/diagrams/Query.png) 

The function body defines the function. It is delimited by braces `{}`. It may contain any valid expression or subquery.

If you specified named parameters for the function, you can use these in the function body to represent arguments which are passed to the function at execution time. If you specified that the function is variadic, any arguments passed to the function at execution time are held in an array named `args`.

The function body may refer to other Analytics collections, or to other functions in the same or other Analytics scopes. If an Analytics scope name was explicitly specified when creating the function, then that scope is the default scope for function calls or collection references within the function body.

Note that recursive function invocation is not permitted. The function body may not refer to itself, nor to another user-defined function which calls this function indirectly.

### [](#checking-for-an-existing-function-and-replacing-a-function)Checking for an Existing Function and Replacing a Function

The optional `IF NOT EXISTS` keywords enable you to check whether a user-defined function exists before creating it, and the optional `OR REPLACE` keywords enable you to redefine the function.

If a function with the same signature already exists within the specified Analytics scope, then:

* If the `OR REPLACE` keywords are present, the existing function is replaced.
* If the `OR REPLACE` keywords are not present, then:

  * If the `IF NOT EXISTS` keywords are present, the statement does nothing and completes without error.
  * If the `IF NOT EXISTS` keywords are not present, an error is generated.

Note that if the statement contains both the `OR REPLACE` keywords and the `IF NOT EXISTS` keywords, an error is generated.

### [](#internal-function-examples)Internal Function Examples

For simplicity, none of these examples implement any data validation.

##### Example 1: Function with expression body

This statement creates a function called `rstr`, which returns the specified number of characters from the right of a string. The function expects two named arguments: `vString`, which is the string to work with, and `vLen`, which is the number of characters to return. The body of the function is an expression based on the two arguments.

CREATE ANALYTICS FUNCTION rstr(vString, vLen)
   { substr(vString, length(vString) - vLen, vLen) };

Test

rstr("Couchbase", 4);

Result

[
  "base"
]

##### Example 2: Function with subquery body

This statement creates a function called `total_spending` based on the `Commerce` data in Appendix 4\. The function takes one parameter, a customer id. Using a subquery, the function returns the total spending of all orders placed by that customer.

CREATE ANALYTICS FUNCTION total_spending(id)
   { SELECT VALUE SUM(i.qty * i.price)
     FROM orders AS o UNNEST o.items AS i
     WHERE o.custid = id
   };

Test

total_spending("C13");

Result

[
  13036.8
]

##### Example 3: Variadic function with expression body

This statement creates a function that can take any number of arguments. Using an expression, the function returns the number of arguments that are passed to it.

CREATE ANALYTICS FUNCTION count_my_args( ... )
   { array_count(args) }

Test

count_my_args("Hello", "Goodbye");

Result

[
  2
]

##### Example 4: Variadic function containing a subquery

The body of this function is an expression that contains a subquery. The function takes a variable number of strings and returns the total length of all the strings.

CREATE ANALYTICS FUNCTION total_length(...)
   { array_sum(
       (SELECT VALUE length(a) FROM args AS a)
     )
   };

Test

total_length("Hello", "Goodbye");

Result

[
  12
]

##### Example 5: Function with no parameters

This statement creates a function which returns the mathematical constant φ. The function takes no arguments.

CREATE ANALYTICS FUNCTION phi() { 2 * sin(radians(54)) };

Test

phi();

Result

[
  1.618033988749895
]

##### Example 6: Replace a function

The following statement redefines the function so that it calculates φ using a different method.

CREATE OR REPLACE ANALYTICS FUNCTION phi() { (1 + sqrt(5)) / 2 };

Test

phi();

Result

[
  1.618033988749895
]

### [](#external-functions)External Functions

Developer Preview

In Couchbase Server 7.0 you can create external user-defined functions using Python code. This is a Developer Preview feature. For further details see [Appendix 5: Python UDFs](appendix%5F5%5Fpython.md).

##### CreateExternalFunction

!["CREATE" ( "OR" "REPLACE" )? "ANALYTICS" "FUNCTION" QualifiedName "(" FunctionParameters? ")" ("IF" "NOT" "EXISTS")? "AS" StringLiteral("," StringLiteral)* "AT" QualifiedName("WITH" ObjectConstructor)? ](_images/diagrams/CreateExternalFunction.png) 

The syntax for the function name, the parameter list, and the `OR REPLACE` and `IF NOT EXISTS` keywords is the same as for [creating an internal function](#internal-functions).

##### StringLiteral

The external language specific identifier for the function to be bound to the created SQL++ for Analytics function. For example, a function name or part of a fully qualified method name. The exact usage will depend on each external language's features and requirements.

##### QualifiedName

The name of a previously created SQL++ for Analytics library created via the Libraries REST API. This is parsed as an identifier and should not be quoted.

##### ObjectConstructor

An object constructor with one or more of the following keys and values:

* `null-call`: `true` if the function should be called if one or more arguments are `unknown`, `false` otherwise. Defaults to `false`.
* `deterministic`: `true` if the function returns the same output for the same input always and as such can be cached. `false` if it should be computed every time. Defaults to `true`.

Python UDFs allow you to utilize your Python code from SQL++ for Analytics as a normal function. Each Python function is defined from within a Library. Libraries belong to Scopes and are created by uploads to the UDF API endpoint. They contain a set of Python modules along with the dependencies of those modules.

### [](#external-function-examples)External Function Examples

Developer Preview

##### Example 7: Create an external Python function

Python UDFs use an identifier in the form of `module`, `function` or `module`, `class.method`. This example is of the latter form.

CREATE ANALYTICS FUNCTION sentiment(a)
  AS "sentiment_mod", "sent_model.sentiment" AT pylib;

Test

sentiment("beef");

Result

[
  "eh"
]

##### Example 8: Create an external Python function with options

The same example as above, but with `null-call` set to `true`.

CREATE ANALYTICS FUNCTION sentiment(a)
  AS "sentiment_mod", "sent_model.sentiment" AT pylib;
  WITH { "null-call": true }

Test

sentiment(null);

Result

[
  null
]

## [](#calling-a-function)Calling a Function

##### OrdinaryFunctionCall

![](_images/diagrams/OrdinaryFunctionCall.png) 

You can invoke a user-defined function in the same way as any other ordinary function. You may optionally prefix the name of the function with the `ScopeName` of the Analytics scope containing the function.

If you don't specify an Analytics scope when calling a function, then the scope containing the function is resolved according to the following rules:

1. If the function call is enclosed within the function body of another user-defined function, the scope is that of the enclosing function.
2. Otherwise, if there is a preceding USE statement, the Analytics scope is specified by the USE statement.
3. Otherwise, if the [query\_context](appendix%5F3%5Fresolution.md#Query%5Fcontext) parameter is set, the Analytics scope is specified by the query context.
4. Otherwise, use the `Default` Analytics scope.

Having determined the scope, Analytics tries to find a user-defined function with the same function signature within that scope. If a user-defined function cannot be found, Analytics tries to find a built-in function with the same function name. If a built-in function cannot be found, the function call fails.

### [](#examples)Examples

The examples in this section assume that you are using an Analytics scope called `Commerce`. Refer to [Appendix 4: Example Data](appendix%5F4%5Fexamples.md) to install this example data.

You can use the [USE statement](5%5Fddl.md#Use%5Fstatements)to set the default scope for the statement immediately following.

Example

USE Commerce;

Alternatively, use the **query context**drop-down list at the top right of the Query Editor to select `Commerce` as the default scope for the following examples.

![The query context drop-down menu with 'Commerce' selected](_images/workbench-context-set.png) 

##### Example 9: Function with subquery

The following statement creates a function called `nameSearch`, which selects the customer name from all documents with the specified ID in the `customers` collection.

CREATE ANALYTICS FUNCTION nameSearch(customerId) {
  (SELECT VALUE c.name
  FROM customers AS c
  WHERE c.custid = customerId)[0]
}

Test

SELECT VALUE nameSearch("C25");

Result

[
  "M. Sinclair"
]

##### Example 10: Call a user-defined function

The following query uses the `nameSearch` function as a projection expression in a SELECT query. Compare this with example Q3.29 in the section on [Subqueries](3%5Fquery.md#Subqueries).

SELECT o.orderno, o.custid,
      nameSearch(o.custid) AS name
FROM orders AS o, o.items AS i
WHERE i.itemno = 120;

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

## [](#dropping-a-function)Dropping a Function

##### DropFunction

!["DROP" "ANALYTICS" "FUNCTION" QualifiedName "(" FunctionParameters? ")" ( "IF" "EXISTS" )?](_images/diagrams/DropFunction.png) 

The DROP ANALYTICS FUNCTION statement enables you to delete a user-defined function.

You cannot delete a user-defined function if there are any other user-defined functions which call this function, in this Analytics scope or any other Analytics scope.

### [](#function-name-2)Function Name

##### QualifiedName

![(ScopeName ".")? Identifier](_images/diagrams/QualifiedName.png) 

##### ScopeName

![(Identifier ".")? Identifier](_images/diagrams/ScopeName.png) 

The `QualifiedName` specifies the name of the function to delete. It consists of an optional scope name, followed by an identifier which represents the local name of the function.

The optional `ScopeName` specifies the Analytics scope where the function is located. It may consist of one or two identifiers, separated by a dot.

If you don't specify an Analytics scope, then the scope containing the function is resolved according to the same rules that are used when creating a user-defined function.

### [](#parameter-list-2)Parameter List

##### FunctionParameters

![Identifier ( "," Identifier )* | "…​"](_images/diagrams/FunctionParameters.png) 

When you drop a function, you must specify the same number of parameters that you specified when you created the function, or specify `...` if you are dropping a variadic function.

### [](#checking-for-an-existing-function)Checking for an Existing Function

The optional `IF EXISTS` keywords enable you to check whether the specified function or scope exists before dropping it. If these keywords are present, and the function scope or function name are unknown, the statement does nothing and completes without error.

If these keywords are not present, and the function scope or function name are unknown, an error is generated.

### [](#examples-2)Examples

Again, the examples in this section assume that you are using an Analytics scope called `Commerce`. Refer to [Appendix 4: Example Data](appendix%5F4%5Fexamples.md) to install this example data.

You can use the [USE statement](5%5Fddl.md#Use%5Fstatements)to set the default scope for the statement immediately following.

Example

USE Commerce;

Alternatively, use the **query context**drop-down list at the top right of the Query Editor to select `Commerce` as the default scope for the following example.

![The query context drop-down menu with 'Commerce' selected](_images/workbench-context-set.png) 

##### Example 11: Drop a Function

This statement drops the function named `nameSearch`, if it exists.

DROP ANALYTICS FUNCTION nameSearch(customerId) IF EXISTS;

You can run the following query to check that the function is no longer available.

SELECT * FROM Metadata.`Function`;