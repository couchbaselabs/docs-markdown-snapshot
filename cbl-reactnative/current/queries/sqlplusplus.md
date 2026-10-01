---
title: SQL&#43;&#43; for Mobile
pubDate: 2026-10-01T04:32:27.613Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-react-native/edit/release/1.1/modules/queries/pages/sqlplusplus.adoc
  xref: xref:cbl-reactnative:queries:sqlplusplus.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cbl-reactnative/current/queries/sqlplusplus.html)

# SQL&#43;&#43; for Mobile

> Description - _How to use SQL++ Query Strings to build effective queries with Couchbase Lite for React Native_   
> Related Content - [Live Queries](live-queries.md) | [Indexes](../indexes.md)

> [!NOTE]
> N1QL is Couchbase's implementation of the developing SQL++ standard. As such the terms N1QL and SQL++ are used interchangeably in all Couchbase documentation unless explicitly stated otherwise.

## [](#introduction)Introduction

Developers using Couchbase Lite for React Native can provide SQL++ query strings using the SQL++ Query API. This API uses query statements of the form shown in [Example 1](#example-1-running-a-sql-query). The structure and semantics of the query format are based on that of Couchbase Server's SQL++ query language - see [SQL++ Reference Guide](https://docs.couchbase.com/server/current/n1ql/n1ql-language-reference/index.html) and [SQL++ Data Model](https://docs.couchbase.com/server/current/learn/data/n1ql-versus-sql.html).

## [](#running)Running

Use `Database.createQuery` to define a query through an SQL++ string. Then run the query using the `Query.execute()` method.

#### Example 1\. Running a SQL++ Query

```typescript
const query = database.createQuery('SELECT META().id AS thisId FROM inventory.hotel WHERE city="Medway"');
const resultSet = await query.execute();
```

## [](#query-format)Query Format

The API uses query statements of the form shown in [Example 2](#example-2-query-format).

#### Example 2\. Query Format

```sql
SELECT ____
FROM ____
JOIN ____
WHERE ____
GROUP BY ____
ORDER BY ____
LIMIT ____
OFFSET ____
```

### [](#query-components)Query Components

1. The `SELECT` clause specifies the data to be returned in the result set.
2. The `FROM` clause specifies the collection to query the documents from.
3. The `JOIN` clause specifies the criteria for joining multiple documents.
4. The `WHERE` clause specifies the query criteria. The `SELECT`ed properties of documents matching this criteria will be returned in the result set.
5. The `GROUP BY` clause specifies the criteria used to group returned items in the result set.
6. The `ORDER BY` clause specifies the criteria used to order the items in the result set.
7. The `LIMIT` clause specifies the maximum number of results to be returned.
8. The `OFFSET` clause specifies the number of results to be skipped before starting to return results.

> [!TIP]
> We recommend working through the [SQL++ Tutorials](https://query-tutorial.couchbase.com/tutorial/#1) as a good way to build your SQL++ skills.

## [](#select-clause)SELECT Clause

### [](#purpose)Purpose

Projects the result returned by the query, identifying the columns it will contain.

### [](#syntax)Syntax

#### [](#example-3-sql-select-syntax)Example 3\. SQL++ Select Syntax

```sql
select        = SELECT _ ( ( DISTINCT | ALL ) _ )? selectResults
selectResults = selectResult ( _? ',' _? selectResult )*
selectResult  = expression ( ( _ AS )? _ columnAlias )?
columnAlias   = IDENTIFIER
```

### [](#arguments)Arguments

1. The select clause begins with the `SELECT` keyword.

  * The optional `ALL` argument is used to specify that the query should return `ALL` results (the default).
  * The optional `DISTINCT` argument is used to specify that the query should return distinct results.
2. `selectResults` is a list of columns projected in the query result. Each column is an expression which could be a property expression or any expression or function. You can use the `*` expression, to select all columns.
3. Use the optional `AS` argument to provides an alias for a column. Each column can be aliased by putting the alias name after the column name.

#### [](#select-wildcard)SELECT Wildcard

When using the `*` expression, the column name is one of:

* The alias name, if one was specified.
* The data source name(or its alias if provided) as specified in the [FROM clause](https://cbl-dart.dev/queries/sqlplusplus-mobile/#from-clause).

This behavior is inline with that of SQL++ for Server - see example in [Table 1](#table-1-example-column-names-for-select).

#### [](#table-1-example-column-names-for-select)Table 1\. Example Column Names for SELECT \*

| Query                        | Column Name |
| ---------------------------- | ----------- |
| SELECT \* AS data FROM \_    | data        |
| SELECT \* FROM \_            | \_          |
| SELECT \* FROM \_default     | \_default   |
| SELECT \* FROM users         | users       |
| SELECT \* FROM users AS user | user        |

### [](#example)Example

#### [](#example-4-select-examples)Example 4\. SELECT Examples

```sql
SELECT * ...;
SELECT user.* AS data ...;
SELECT name fullName ...;
SELECT user.name ...;
SELECT DISTINCT address.city ...;
```

1. Use the `*` expression to select all columns.
2. Select all properties from the `user` data source. Give the object an alias of `data`.
3. Select a pair of properties.
4. Select a specific property from the `user` data source.
5. Select the property `city` from the `address` data source.

## [](#from-clause)FROM Clause

### [](#purpose-2)Purpose

Specifies the data source and optionally applies an alias (`AS`). It is mandatory.

### [](#syntax-2)Syntax

#### [](#example-5-from-syntax)Example 5\. FROM Syntax

```sql
from             = FROM _ dataSource
dataSource       = collectionName ( ( _ AS )? _ collectionAlias )?
collectionName   = IDENTIFIER
collectionAlias  = IDENTIFIER
```

Here `dataSource` is the collection name against which the query is to run. Use `AS` to give the collection an alias you can use within the query. To use the default collection, without specifying a name, use `_` as the data source.

### [](#example-2)Example

#### [](#example-6-from-examples)Example 6\. FROM Examples

```sql
SELECT name FROM testScope.user;
SELECT user.name FROM testScope.users AS user;
SELECT user.name FROM testScope.users user;
-- These queries use the default scope and default collection (_default._default) in Couchbase.
SELECT name FROM _default._default;
SELECT user.name FROM _default._default AS user;
SELECT user.name FROM _default._default user;
```

## [](#join-clause)JOIN Clause

### [](#purpose-3)Purpose

The `JOIN` clause enables you to select data from multiple data sources linked by criteria specified in the ON constraint. Currently only self-joins are supported. For example to combine airline details with route details, linked by the airline id - see Example 7.

### [](#syntax-3)Syntax

#### [](#example-7-join-syntax)Example 7\. JOIN Syntax

```sql
join            = joinOperator _ dataSource ( _ constraint )?
joinOperator    = ( ( LEFT ( _ OUTER )? | INNER | CROSS ) _ )? JOIN
dataSource      = collectionName ( ( _ AS )? _ collectionAlias )?
constraint      = ON _ expression
collectionName  = IDENTIFIER
collectionAlias = IDENTIFIER
```

### [](#arguments-2)Arguments

1. The `JOIN` clause starts with a `JOIN` operator followed by the data source.
2. Five `JOIN` operators are supported:

  * `JOIN`, `LEFT JOIN`, `LEFT OUTER JOIN`, `INNER JOIN`, and `CROSS JOIN`.
  * NOTE: `JOIN` and `INNER JOIN` are the same, and `LEFT JOIN` and `LEFT OUTER JOIN` are the same.
3. The `JOIN` constraint starts with the `ON` keyword followed by the expression that defines the joining constraints.

### [](#example-3)Example

#### [](#example-8-join-examples)Example 8\. JOIN Examples

```sql
SELECT users.prop1, other.prop2
FROM testScope.users
JOIN users AS other ON users.key = other.key;

SELECT users.prop1, other.prop2
FROM testScope.users
LEFT JOIN users AS other ON users.key = other.key;
```

#### [](#example-9-using-join-to-combine-document-details)Example 9\. Using JOIN to Combine Document Details

This example joins the documents from the `routes` collections with documents from the `airlines` collection using the document ID (`id`) of the _airline_ document and the `airlineId` property of the _route_ document.

```sql
SELECT *
FROM inventory.routes r
JOIN airlines a ON r.airlineId = META(a).id
WHERE a.country = "France";
```

## [](#where-clause)WHERE Clause

### [](#purpose-4)Purpose

Specifies the selection criteria used to filter results. As with SQL, use the `WHERE` clause to choose which results are returned by your query.

### [](#syntax-4)Syntax

#### [](#example-10-where-syntax)Example 10\. WHERE Syntax

```sql
where = WHERE _ expression
```

### [](#arguments-3)Arguments

1. `WHERE` evalates the expression to a `BOOLEAN` value. You can combine any number of expressions through logical operators, in order to implement sophisticated filtering capabilities.

### [](#example-4)Example

#### [](#example-11-where-examples)Example 11\. WHERE Examples

```sql
SELECT name
FROM testScope.employees
WHERE department = "engineer" AND group = "mobile"
```

## [](#group-by-clause)GROUP BY Clause

### [](#purpose-5)Purpose

Use `GROUP BY` to group results for aggreation, based on one or more expressions.

### [](#syntax-5)Syntax

#### [](#example-12-group-by-syntax)Example 12\. GROUP BY Syntax

```sql
groupBy  = grouping ( _ having )?
grouping = GROUP BY _ expression ( _? ',' _? expression )*
having   = HAVING _ expression
```

### [](#arguments-4)Arguments

1. The `GROUP BY` clause starts with the `GROUP BY` keyword followed by one or more expressions.
2. The `GROUP BY` clause is normally used together with aggregate functions (e.g. `COUNT`, `MAX`, `MIN`, `SUM`, `AVG`).
3. The `HAVING` clause allows you to filter the results based on aggregate functions - for example, `HAVING COUNT(airlineId) > 100`.

### [](#example-5)Example

#### [](#example-13-group-by-examples)Example 13\. GROUP BY Examples

```sql
SELECT COUNT(airlineId), destination
FROM inventory.routes
GROUP BY destination;

SELECT COUNT(airlineId), destination
FROM inventory.routes
GROUP BY destination
HAVING COUNT(airlineId) > 100;

SELECT COUNT(airlineId), destination
FROM inventory.routes
WHERE destinationState = "CA"
GROUP BY destination
HAVING COUNT(airlineId) > 100;
```

## [](#order-by-clause)ORDER BY Clause

### [](#purpose-6)Purpose

Sort query results based on a expression.

### [](#syntax-6)Syntax

#### [](#example-14-order-by-syntax)Example 14\. ORDER BY Syntax

```sql
orderBy  = ORDER BY _ ordering ( _? ',' _? ordering )*
ordering = expression ( _ order )?
order    = ( ASC | DESC )
```

### [](#arguments-5)Arguments

1. The `ORDER BY` clause starts with the `ORDER BY` keyword followed by one or more ordering expressions.
2. An ordering expression specifies an expressions to use for ordering the results.
3. For each ordering expression, the sorting direction can be specified using the optional `ASC` (ascending) or `DESC` (descending) directives. Default is `ASC`.

### [](#example-6)Example

#### [](#example-15-order-by-examples)Example 15\. ORDER BY Examples

```sql
SELECT name
FROM testScope.users
ORDER BY name;

SELECT name
FROM testScope.users
ORDER BY name DESC;

SELECT name, score
FROM testScope.users
ORDER BY name ASC, score DESC;
```

## [](#limit-clause)LIMIT Clause

### [](#purpose-7)Purpose

Specifies the maximum number of results to be returned by the query.

### [](#syntax-7)Syntax

#### [](#example-16-linit-syntax)Example 16\. LINIT Syntax

```sql
limit = LIMIT _ expression
```

### [](#arguments-6)Arguments

1. The `LIMIT` clause starts with the `LIMIT` keyword followed by an expression that will be evaluated as a number.

### [](#example-7)Example

#### [](#example-17-limit-examples)Example 17\. LIMIT Examples

```sql
SELECT name
FROM testScope.users
LIMIT 10;
```

## [](#offset-clause)OFFSET Clause

### [](#purpose-8)Purpose

Specifies the number of results to be skipped by the query.

### [](#syntax-8)Syntax

#### [](#example-18-offset-syntax)Example 18\. OFFSET syntax

offset = OFFSET _ expression

### [](#arguments-7)Arguments

1. The offset clause starts with the `OFFSET` keyword followed by an expression that will be evaluated as a number that represents the number of results to be skipped before the query begins returning results.

### [](#example-8)Example

#### [](#example-19-offset-examples)Example 19\. OFFSET Examples

```sql
SELECT name
FROM testScope.users
OFFSET 10;

SELECT name
FROM testScope.users
LIMIT 10
OFFSET 10;
```

## [](#expressions)Expressions

An expression is a specification for a value that is resolved when executing a query. This section, together with [Operators](#operators) and [Functions](#functions), which are covered in their own sections, covers all the available types of expressions.

### [](#literals)Literals

#### [](#boolean)Boolean

##### [](#purpose-9)Purpose

Represents a true or false value.

##### [](#syntax-9)Syntax

#### [](#example-20-boolean-syntax)Example 20\. Boolean Syntax

boolean = ( TRUE | FALSE )

##### [](#example-9)Example

#### [](#example-21-boolean-examples)Example 21\. Boolean Examples

```sql
SELECT value
FROM testScope.testCollection
WHERE value = true;

SELECT value
FROM testScope.testCollection
WHERE value = false;
```

#### [](#numeric)Numeric

##### [](#purpose-10)Purpose

Represents a numeric value. Numbers may be signed or unsigned digits. They have optional fractional and exponent components.

##### [](#syntax-10)Syntax

#### [](#example-22-numeric-syntax)Example 22\. Numeric Syntax

numeric = -? ( ( . digit+ ) | ( digit+ ( . digit* )? ) ) ( ( E | e ) ( - | + )? digit+ )?
digit   = /[0-9]/

##### [](#example-10)Example

#### [](#example-23-numeric-examples)Example 23\. Numeric Examples

```sql
SELECT
  10,
  0,
  -10,
  10.25,
  10.25e2,
  10.25E2,
  10.25E+2,
  10.25E-2
FROM testScope.testCollection;
```

#### [](#string)String

##### [](#purpose-11)Purpose

The string literal represents a string or sequence of characters.

##### [](#syntax-11)Syntax

#### [](#example-24-string-syntax)Example 24\. String Syntax

string         = ( " character* " | ' character* ' )
character      = ( escapeSequence | any codepoint except ", ' or control characters )
escapeSequence = \ ( " | ' | \ | / | b | f | n | r | t | u hex hex hex hex )
hex            = hexDigit hexDigit
hexDigit       = /[0-9a-fA-F]/

> [!NOTE]
> The string literal can be double-quoted as well as single-quoted.

##### [](#example-11)Example

#### [](#example-25-string-examples)Example 25\. String Examples

```sql
SELECT firstName, lastName
FROM crm.customer
WHERE contact.middleName = "middle" AND contact.lastName = 'last';
```

#### [](#null)NULL

##### [](#purpose-12)Purpose

Represents the absence of a value.

##### [](#syntax-12)Syntax

#### [](#example-26-null-syntax)Example 26\. NULL Syntax

null = NULL

##### [](#example-12)Example

#### [](#example-27-null-examples)Example 27\. NULL Examples

```sql
SELECT firstName, lastName
FROM crm.customer
WHERE contact.middleName IS NULL;
```

#### [](#missing)MISSING

##### [](#purpose-13)Purpose

Represents a missing name-value pair in a dictionary.

##### [](#syntax-13)Syntax

#### [](#example-28-missing-syntax)Example 28\. MISSING Syntax

missing = MISSING

##### [](#example-13)Example

#### [](#example-29-missing-examples)Example 29\. MISSING Examples

```sql
SELECT firstName, lastName
FROM crm.customer
WHERE contact.middleName IS MISSING;
```

#### [](#array)Array

##### [](#purpose-14)Purpose

Represents an array.

##### [](#syntax-14)Syntax

#### [](#example-30-array-syntax)Example 30\. ARRAY Syntax

array = [ ( _? expression ( _? ',' _? expression )* _? )? ]

##### [](#example-14)Example

#### [](#example-31-array-examples)Example 31\. ARRAY examples

```sql
SELECT ["a", "b", "c"]
FROM testScope.testCollection

SELECT [property1, property2, property3]
FROM testScope.testCollection
```

#### [](#dictionary)Dictionary

##### [](#purpose-15)Purpose

Represents a dictionary.

##### [](#syntax-15)Syntax

#### [](#example-32-dictionary-syntax)Example 32\. Dictionary Syntax

dictionary = { ( _? string _? : _? expression ( _? , _? string _? : _? expression )* _? )? }

##### [](#example-15)Example

#### [](#example-33-dictionary-examples)Example 33\. Dictionary Examples

```sql
SELECT { 'name': 'James', 'department': 10 }
FROM testScope.testCollection;

SELECT { 'name': 'James', 'department': dept }
FROM testScope.testCollection;

SELECT { 'name': 'James', 'phones': ['650-100-1000', '650-100-2000'] }
FROM testScope.testCollection;
```

### [](#identifier)Identifier

#### [](#purpose-16)Purpose

An identifier references an entity by its symbolic name. Use an identifier for example to identify:

* Column alias names
* Database names
* Database alias names
* Property names
* Parameter names
* Function names
* FTS index names

#### [](#syntax-16)Syntax

#### [](#example-34-identifier-syntax)Example 34\. Identifier Syntax

identifier       = ( plainIdentifier | quotedIdentifier )
plainIdentifier  = /[a-zA-Z_][a-zA-Z0-9_$]*/
quotedIdentifier = /`[^`]+`/

> [!TIP]
> To use other than basic characters in the identifier, surround the identifier with the backticks \` character. For example, to use a hyphen (-) in an identifier, use backticks to surround the identifier.
> 
> Please note that backticks are commonly used for string literals/interpolation in TypeScript/JavaScript. Therefore, you should be aware that backticks need to be escaped properly to function correctly in TypeScript/JavaScript. For more information, refer to [Template Literal Types in TypeScript](https://www.typescriptlang.org/docs/handbook/2/template-literal-types.html).

#### [](#example-16)Example

#### [](#example-35-identifier-examples)Example 35\. Identifier Examples

```sql
-- This query uses the default scope and default collection (_default._default) in Couchbase.
SELECT *
FROM _default._default;

SELECT *
FROM test-scope.test-collection;

SELECT key
FROM testScope.testCollection;

SELECT key$1
FROM test_Scope.test_Collection;

SELECT `key-1`
FROM testScope.testCollection;
```

### [](#property-expression)Property Expression

#### [](#purpose-17)Purpose

The property expression is used to reference a property of a dictionary.

#### [](#syntax-17)Syntax

#### [](#example-36-property-expression-syntax)Example 36\. Property Expression Syntax

property     = ( * | dataSourceName . _? * | propertyPath )
propertyPath = propertyName ( ( . _? propertyName ) | ( [ _? numeric _? ] _? ) )*
propertyName = IDENTIFIER

1. Prefix the property expression with the data source name or alias to indicate its origin.
2. Use dot syntax to refer to nested properties in the propertyPath.
3. Use bracket (`[index]`) syntax to refer to an item in an array.
4. Use the asterisk (`*`) character to represents all properties. This can only be used in the result list of the `SELECT` clause.

#### [](#example-17)Example

#### [](#example-37-property-expressions-examples)Example 37\. Property Expressions Examples

```sql
SELECT *
FROM crm.customer
WHERE contact.firstName = 'daniel';

SELECT crm.customer.*
FROM crm.customer
WHERE contact.firstName = 'daniel';

SELECT crm.customer.contact.address.city
FROM crm.customer
WHERE contact.firstName = 'daniel';

SELECT contact.address.city, contact.phones[0]
FROM crm.customer
WHERE contact.firstName = 'daniel';
```

### [](#any-and-every-expression)Any and Every Expression

#### [](#purpose-18)Purpose

Evaluates expressions over items in an array.

#### [](#syntax-18)Syntax

#### [](#example-38-any-and-every-expression-syntax)Example 38\. Any and Every Expression Syntax

```sql
arrayExpression = anyEvery _ variableName _ IN _ expression _ SATISFIES _ expression _ END
anyEvery        = ( anyOrSome AND EVERY | anyOrSome | EVERY )
anyOrSome       = ( ANY | SOME )
variableName    = IDENTIFIER
```

1. The array expression starts with `anyEvery`, where each possible combination has a different function as described below, and is terminated by `END`.

  * `ANY` or `SOME`: Returns `TRUE` if at least one item in the array satisfies the expression, otherwise returns `FALSE`.  
  > [!NOTE]  
  > \+ `ANY` and `SOME` are interchangeable.  
  >  
  > +
  * `EVERY`: Returns `TRUE` if all items in the array satisfies the expression, otherwise returns `FALSE`. If the array is empty, returns `TRUE`.
  * `( ANY | SOME ) AND EVERY`: Same as `EVERY` but returns `FALSE` if the array is empty.
2. The `variableName` represents each item in the array.
3. The `IN` keyword is used to specify the array to be evaluated.
4. The `SATISFIES` keyword is used to specify the expression to evaluate for each item in the array.
5. `END` terminates the array expression.

#### [](#example-18)Example

#### [](#example-39-any-and-every-expression-examples)Example 39\. Any and Every Expression Examples

```sql
SELECT firstName, lastName
FROM crm.customer
WHERE
  ANY contact IN contacts
    SATISFIES contact.city = 'San Mateo'
  END;
```

### [](#parameter-expression)Parameter Expression

#### [](#purpose-19)Purpose

A parameter expression references a value from the `api|Parameters` assigned to the query before execution.

> [!NOTE]
> If a parameter is specified in the query string, but no value has been provided, an error will be thrown when executing the query.

#### [](#syntax-19)Syntax

#### [](#example-40-parameter-expression-syntax)Example 40\. Parameter Expression Syntax

parameter = $ IDENTIFIER

#### [](#example-19)Example

#### [](#example-41-parameter-expression-examples)Example 41\. Parameter Expression Examples

```sql
SELECT *
FROM crm.customer
WHERE contact.firstName = $firstName;
```

#### [](#example-42-using-a-parameter)Example 42\. Using a Parameter

```typescript
const query = database.createQuery('SELECT * FROM crm.customer WHERE contact.firstName = $firstName');
const params = new Parameters();
params.setValue('firstName', 'daniel');
query.parameters = params;
const resultSet = await query.execute();
```

### [](#parenthesis-expression)Parenthesis Expression

#### [](#purpose-20)Purpose

Use parentheses to group expressions together to make them more readable or to establish operator precedence.

#### [](#example-20)Example

#### [](#example-43-parenthesis-expression-examples)Example 43\. Parenthesis Expression Examples

```sql
SELECT (value1 + value2) * value 3
FROM testScope.testCollection

SELECT *
FROM testScope.testCollection
WHERE ((value1 + value2) * value3) + value4 = 10;

SELECT *
FROM testScope.testCollection
WHERE (value1 = value2)
   OR (value3 = value4);
```

## [](#operators)Operators

### [](#binary-operators)Binary Operators

#### [](#maths)Maths

#### [](#table-2-maths-operators)Table 2\. Maths Operators

| Op | Description    | Example               |
| -- | -------------- | --------------------- |
| +  | Add            | WHERE v1 + v2 = 10    |
| \- | Subtract       | WHERE v1 - v2 = 10    |
| \* | Multiply       | WHERE v1 \\\* v2 = 10 |
| /  | Divide - see 1 | WHERE v1 / v2 = 10    |
| %  | Modulus        | WHERE v1 % v2 = 0     |

1. If both operands are integers, integer division is used, but if one is a floating number, then float division is used. This differs from SQL++ for Server, which performs float division regardless. Use `DIV(x, y)` to force float division in SQL++ for Mobile.

#### [](#comparison-operators)Comparison Operators

##### [](#purpose-21)Purpose

The comparison operators can for example be used in the `WHERE` clause to specify the condition on which to match documents.

#### [](#table-3-comparison-operators)Table 3\. Comparison Operators

| Op | Description | Example | | ------------ | ---------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | | `=` or `==` | Equals | `WHERE v1 = v2<br/> WHERE v1 == v2` | | `!=` or &#60&#62 | Not Equal to | `WHERE v1 != v2<br/> WHERE v1 &#60&#62 v2` | | `>` | Greater than | `WHERE v1 > v2` | | `>=` | Greater than or equal to | `WHERE v1 >= v2` | | `<` | Less than | `WHERE v1 < v2` | | `<=` | Less than or equal to | `WHERE v1 <= v2` | | `IN` | Returns `TRUE` if the value is in the list or array of values specified by the right hand side expression; Otherwise returns `FALSE`. | `WHERE 'James' IN contactsList` | | `LIKE` | String wildcard pattern matching, comparison - see 2\. Two wildchards are supported:  
• `%` Matches zero or more characters.  
• _` Matches a single character. | `WHERE name LIKE 'a%'` <br/> `WHERE name LIKE '%a'` <br/> `WHERE name LIKE '%or%'` <br/> `WHERE name LIKE 'a%o%'` <br/> `WHERE name LIKE '%\_r%'` <br/> `WHERE name LIKE '%a_%'` <br/> `WHERE name LIKE '%a\_\_%'` <br/> `WHERE name LIKE 'aldo'` <br/> | | `MATCH` | String matching using FTS | `WHERE v1-index MATCH "value"` | | `BETWEEN` | Logically equivalent to `v1 >= start AND v1 <= end` | `WHERE v1 BETWEEN 10 AND 100` | | `IS NULL` - see 3 | Equal to `null` | `WHERE v1 IS NULL` | | `IS NOT NULL` | Not equal to `null` | `WHERE v1 IS NOT NULL` | | `IS MISSING` | Equal to MISSING | `WHERE v1 IS MISSING` | | `IS NOT MISSING` | Not equal to MISSING | `WHERE v1 IS NOT MISSING` | | `IS VALUED` | Logically equivalent to `IS NOT NULL AND MISSING` | `WHERE v1 IS VALUED` | | `IS NOT VALUED` | Logically equivalent to `IS NULL OR MISSING` | `WHERE v1 IS NOT VALUED\` |

1. Matching is case-insensitive for ASCII characters, case-sensitive for non-ASCII.
2. Use of `IS` and `IS NOT` is limited to comparing `NULL` and `MISSING` values (this encompasses `VALUED`). This is different from `api|QueryBuilder`, in which they operate as equivalents of `==` and `!=`.

#### [](#table-4-comparing-null-and-missing-values-using-is)Table 4\. Comparing NULL and MISSING values using IS

| Op             | Non-NULL Value | NULL  | MISSING |
| -------------- | -------------- | ----- | ------- |
| IS NULL        | FALSE          | TRUE  | MISSING |
| IS NOT NULL    | TRUE           | FALSE | MISSING |
| IS MISSING     | FALSE          | FALSE | TRUE    |
| IS NOT MISSING | TRUE           | TRUE  | FALSE   |
| IS VALUED      | TRUE           | FALSE | FALSE   |
| IS NOT VALUED  | FALSE          | TRUE  | TRUE    |

#### [](#logical-operators)Logical Operators

##### [](#purpose-22)Purpose

Logical operators combine expressions using the following boolean logic rules:

* `TRUE` is `TRUE`, and `FALSE` is `FALSE`.
* Numbers `0` or `0.0` are `FALSE`.
* Arrays and dictionaries are `FALSE`.
* Strings and Blobs are `TRUE` if the values are casted as a non-zero or `FALSE`if the values are casted as `0` or `0.0`.
* `NULL` is `FALSE`.
* `MISSING` is `MISSING`.

> [!NOTE]
> This is different from SQL++ for Server, where:
> 
> * `MISSING`, `NULL` and `FALSE` are `FALSE`.
> * Numbers `0` is `FALSE`.
> * Empty strings, arrays, and objects are `FALSE`.
> * All other values are `TRUE`.

> [!TIP]
> Use the `TOBOOLEAN(expr)` function to convert a value based on SQL++ for Server boolean value rules.

#### [](#table-5-logical-operators)Table 5\. Logical Operators

| Op  | Description                                                                                                                                                                                                                                                                                                                                                  | Example                                              |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------- |
| AND | Returns TRUE if the operand expressions evaluate to TRUE; otherwise FALSE. If an operand is MISSING and the other is TRUE returns MISSING, if the other operand is FALSE it returns FALSE. If an operand is NULL and the other is TRUE returns NULL, if the other operand is FALSE it returns FALSE.                                                         | WHERE city = 'San Francisco' AND status = TRUE       |
| OR  | Returns TRUE if one of the operand expressions is evaluated to TRUE; otherwise returns FALSE If an operand is MISSING, the operation will result in MISSING if the other operand is FALSE or TRUE if the other operand is TRUE. If an operand is NULL, the operation will result in NULL if the other operand is FALSE or TRUE if the other operand is TRUE. | WHERE city = 'San Francisco' OR city = 'Santa Clara' |

#### [](#table-6-logical-operators-table)Table 6\. Logical Operators Table

| a       | b       | a AND b      | a OR b         |
| ------- | ------- | ------------ | -------------- |
| TRUE    | TRUE    | TRUE         | TRUE           |
|         | FALSE   | FALSE        | TRUE           |
|         | NULL    | FALSE, see 5 | TRUE           |
|         | MISSING | MISSING      | TRUE           |
| FALSE   | TRUE    | FALSE        | TRUE           |
|         | FALSE   | FALSE        | FALSE          |
|         | NULL    | FALSE        | FALSE, see 5   |
|         | MISSING | FALSE        | MISSING        |
| NULL    | TRUE    | FALSE, see 5 | TRUE           |
|         | FALSE   | FALSE        | FALSE, see 5   |
|         | NULL    | FALSE, see 5 | FALSE, see 5   |
|         | MISSING | FALSE, see 6 | MISSING, see 7 |
| MISSING | TRUE    | MISSING      | TRUE           |
|         | FALSE   | FALSE        | MISSING        |
|         | NULL    | FALSE, see 6 | FALSE, see 7   |
|         | MISSING | MISSING      | MISSING        |

This differs from SQL++ for Server in the following instances:

* 1. Server will return: `NULL` instead of `FALSE`.
* 1. Server will return: `MISSING` instead of `FALSE`.
* 1. Server will return: `NULL` instead of `MISSING`.

#### [](#string-operators)String Operators

##### [](#purpose-23)Purpose

A single string operator is provided. It enables string concatenation.

#### [](#table-7-string-operators)Table 7\. String Operators

| Op         | Description   | Example                                                                        |
| ---------- | ------------- | ------------------------------------------------------------------------------ |
| &#124&#124 | Concatenating | SELECT firstName &#124&#124 lastName AS fullName FROM testScope.testCollection |

### [](#unary-operators)Unary Operators

#### [](#purpose-24)Purpose

Three unary operators are provided. They operate by modifying an expression, making it numerically positive or negative, or by logically negating its value (`TRUE` becomes `FALSE`).

#### [](#syntax-20)Syntax

#### [](#example-44-unary-operators-syntax)Example 44\. Unary Operators Syntax

```sql
unaryOperator = ( + | - | NOT ) _ expression
```

#### [](#table-8-unary-operators)Table 8\. Unary Operators

| Op  | Description                    | Example                           |
| --- | ------------------------------ | --------------------------------- |
| +   | Positive value                 | WHERE v1 = +10                    |
| \-  | Negative value                 | WHERE v1 = -10                    |
| NOT | Logical Negate operator, see 8 | WHERE "James" NOT IN contactsList |

1. The `NOT` operator is often used in conjunction with operators such as `IN`, `LIKE`, `MATCH`, and `BETWEEN` operators.

  * `NOT` operation on `NULL` value returns `NULL`.
  * `NOT` operation on `MISSING` value returns `MISSING`.

#### [](#table-9-not-operators)Table 9\. NOT Operators

| a       | NOT a   |
| ------- | ------- |
| TRUE    | FALSE   |
| FALSE   | TRUE    |
| NULL    | FALSE   |
| MISSING | MISSING |

### [](#collate-operator)`COLLATE` Operator

#### [](#purpose-25)Purpose

Collate operators specify how a string comparison is conducted.

#### [](#usage)Usage

The collate operator is used in conjunction with string comparison expressions and `ORDER BY` clauses. It allows for one or more collations. If multiple collations are used, the collations need to be specified in a parenthesis. When only one collation is used, the parenthesis is optional.

> [!NOTE]
> Collation is not supported by SQL++ for Server.

#### [](#syntax-21)Syntax

#### [](#example-45-collate-operator-syntax)Example 45\. COLLATE Operator Syntax

```sql
collate   = COLLATE _ ( collation | '(' collation ( _ collation )+ ')' )
collation = NO? (UNICODE | CASE | DIACRITICS)
```

#### [](#arguments-8)Arguments

1. The available collation options are:

  * `UNICODE`: Conduct a Unicode comparison; the default is to do ASCII comparison.
  * `CASE`: Conduct case-sensitive comparison
  * `DIACRITIC`: Take accents and diacritics into account in the comparison; On by default.
  * `NO`: This can be used as a prefix to the other collations, to disable them. For example, use `NOCASE` to enable case-insensitive comparison.

#### [](#example-21)Example

#### [](#example-46-collate-operator-example)Example 46\. COLLATE Operator Example

```sql
SELECT contact
FROM crm.customer
WHERE contact.firstName = "fred" COLLATE UNICODE;

SELECT contact
FROM crm.customer
WHERE contact.firstName = "fred" COLLATE (UNICODE CASE);

SELECT firstName, lastName
FROM crm.customer
ORDER BY firstName COLLATE (UNICODE DIACRITIC), lastName COLLATE (UNICODE DIACRITIC);
```

### [](#conditional-operator)Conditional Operator

#### [](#purpose-26)Purpose

The conditional (or `CASE`) operator evaluates conditional logic in a similar way to the `IF`/`ELSE` operator.

#### [](#syntax-22)Syntax

#### [](#example-47-conditional-operators-syntax)Example 47\. Conditional Operators Syntax

case = CASE _ ( expression _ )?
       ( WHEN _ expression _ THEN _ expression _ )+
       ( ELSE _ expression _)?
       END

Both _Simple Case_ and _Searched Case_ expressions are supported. The syntactic difference being that the _Simple Case_ expression has an expression after the `CASE` keyword.

1. Simple Case Expression

  * If the `CASE` expression is equal to the first `WHEN` expression, the result is the `THEN` expression.
  * Otherwise, any subsequent `WHEN` clauses are evaluated in the same way.
  * If no match is found, the result of the `CASE` expression is the `ELSE`expression, or `NULL` if no `ELSE` expression was provided.
2. Searched Case Expression

  * If the first `WHEN` expression is `TRUE`, the result of this expression is its `THEN` expression.
  * Otherwise, subsequent `WHEN` clauses are evaluated in the same way.
  * If no `WHEN` clause evaluate to `TRUE`, then the result of the expression is the `ELSE` expression, or `NULL` if no `ELSE` expression was provided.

#### [](#examples)Examples

#### [](#example-48-simple-case)Example 48\. Simple Case

```sql
SELECT
  CASE state
    WHEN 'CA'
      THEN 'Local'
    ELSE 'Non-Local'
  END
FROM testScope.testCollection;
```

#### [](#examples-2)Examples

#### [](#example-49-searched-case)Example 49\. Searched Case

```sql
SELECT
  CASE
    WHEN shippedOn IS NOT NULL
      THEN 'SHIPPED'
    ELSE 'NOT-SHIPPED'
  END
FROM testScope.testCollection;
```

## [](#functions)Functions

### [](#purpose-27)Purpose

Functions provide specialised operations through a generalized syntax.

### [](#syntax-23)Syntax

#### [](#example-50-functions-syntax)Example 50\. Functions Syntax

The function syntax is the same as C-style language function syntax. It starts with the function name, followed by optional arguments inside parentheses.

function      = functionName _? '(' ( _? expression ( _? ',' _? expression )* _? )? ')'
functionName  = IDENTIFIER

### [](#aggregation-functions)Aggregation Functions

#### [](#table-10-aggregation-functions)Table 10\. Aggregation Functions

| Function     | Description                                             |
| ------------ | ------------------------------------------------------- |
| AVG(value)   | Returns the average of all numeric values in the group. |
| COUNT(value) | Returns the count of all values in the group.           |
| MIN(value)   | Returns the minimum numeric value in the group.         |
| MAX(value)   | Returns the maximum numeric value in the group.         |
| SUM(value)   | Returns the sum of all numeric values in the group.     |

### [](#array-functions)Array Functions

#### [](#table-11-array-functions)Table 11\. Array Functions

| Function               | Description                                                                                      |
| ---------------------- | ------------------------------------------------------------------------------------------------ |
| ARRAY\_AGG(value)      | Returns an array of the non-MISSING group values in the input expression, including NULL values. |
| ARRAY\_AVG(value)      | Returns the average of all non-NULL number values in the array; or NULL if there are none.       |
| ARRAY\_CONTAINS(value) | Returns TRUE if the value exists in the array; otherwise FALSE.                                  |
| ARRAY\_COUNT(value)    | Returns the number of non-NULL values in the array.                                              |
| ARRAY\_IFNULL(value)   | Returns the first non-NULL value in the array.                                                   |
| ARRAY\_MAX(value)      | Returns the largest non-NULL, non\_MISSING value in the array.                                   |
| ARRAY\_MIN(value)      | Returns the smallest non-NULL, non\_MISSING value in the array.                                  |
| ARRAY\_LENGTH(value)   | Returns the length of the array.                                                                 |
| ARRAY\_SUM(value)      | Returns the sum of all non-NULL numeric value in the array.                                      |

### [](#conditional-functions)Conditional Functions

#### [](#table-12-conditional-functions)Table 12\. Conditional Functions

| Function                    | Description                                                                                                                                                                |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IFMISSING(value, ...)       | Returns the first non-MISSING value, or NULL if all values are MISSING.                                                                                                    |
| IFMISSINGORNULL(value, ...) | Returns the first non-NULL and non-MISSING value, or NULL if all values are NULL or MISSING.                                                                               |
| IFNULL(value, ...)          | Returns the first non-NULL, or NULL if all values are NULL.                                                                                                                |
| MISSINGIF(value, other)     | Returns MISSING when value = other; otherwise returns value.Returns MISSING if either or both expressions are MISSING.Returns NULL if either or both expressions are NULL. |
| NULLIF(value, other)        | Returns NULL when value = other; otherwise returns value.Returns MISSING if either or both expressions are MISSING.Returns NULL if either or both expressions are NULL.    |

### [](#date-and-time-functions)Date and Time Functions

#### [](#table-13-date-and-time-functions)Table 13\. Date and Time Functions

| Function               | Description                                                                                                                       |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| STR\_TO\_MILLIS(value) | Returns the number of milliseconds since the unix epoch of the given ISO 8601 date input string.                                  |
| STR\_TO\_UTC(value)    | Returns the ISO 8601 UTC date time string of the given ISO 8601 date input string.                                                |
| MILLIS\_TO\_STR(value) | Returns a ISO 8601 date time string in device local timezone of the given number of milliseconds since the unix epoch expression. |
| MILLIS\_TO\_UTC(value) | Returns the UTC ISO 8601 date time string of the given number of milliseconds since the unix epoch expression.                    |

### [](#full-text-search-functions)Full Text Search Functions

#### [](#table-14-fts-functions)Table 14\. FTS Functions

| Function                                                                                                                                              | Description                                                                                                                                                               | Example                                                          |  |
| ----------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |  |
| MATCH(indexName, term) \| Returns TRUE if term expression matches the FTS indexed document. indexName identifies the FTS index to search for matches. | WHERE MATCH(description, 'couchbase')\`                                                                                                                                   |                                                                  |  |
| RANK(indexName)                                                                                                                                       | Returns a numeric value indicating how well the current query result matches the full-text query when performing the MATCH. indexName is an IDENTIFIER for the FTS index. | WHERE MATCH(description, 'couchbase') ORDER BY RANK(description) |  |

### [](#maths-functions)Maths Functions

#### [](#table-15-maths-functions)Table 15\. Maths Functions

| Function                       | Description                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ABS(value)                     | Returns the absolute value of a number.                                                                                                                                                                                                                                                                                                                          |
| ACOS(value)                    | Returns the arc cosine in radians.                                                                                                                                                                                                                                                                                                                               |
| ASIN(value)                    | Returns the arcsine in radians.                                                                                                                                                                                                                                                                                                                                  |
| ATAN(value)                    | Returns the arctangent in radians.                                                                                                                                                                                                                                                                                                                               |
| ATAN2(a, b)                    | Returns the arctangent of a / b.                                                                                                                                                                                                                                                                                                                                 |
| CEIL(value)                    | Returns the smallest integer not less than the number.                                                                                                                                                                                                                                                                                                           |
| COS(value)                     | Returns the cosine of an angle in radians.                                                                                                                                                                                                                                                                                                                       |
| DIV(a, b)                      | Returns float division of a and b. Both a and b are cast to a double number before division. The returned result is always a double.                                                                                                                                                                                                                             |
| DEGREES(value)                 | Converts radians to degrees.                                                                                                                                                                                                                                                                                                                                     |
| E()                            | Returns the e constant, which is the base of natural logarithms.                                                                                                                                                                                                                                                                                                 |
| EXP(value)                     | Returns the natural exponential of a number.                                                                                                                                                                                                                                                                                                                     |
| FLOOR(value)                   | Returns largest integer not greater than the number.                                                                                                                                                                                                                                                                                                             |
| IDIV(a, b)                     | Returns integer division of a and b.                                                                                                                                                                                                                                                                                                                             |
| LN(value)                      | Returns log base e.                                                                                                                                                                                                                                                                                                                                              |
| LOG(value)                     | Returns log base 10.                                                                                                                                                                                                                                                                                                                                             |
| PI()                           | Returns the pi constant.                                                                                                                                                                                                                                                                                                                                         |
| POWER(a, b)                    | Returns a to the bth power.                                                                                                                                                                                                                                                                                                                                      |
| RADIANS(value)                 | Converts degrees to radians.                                                                                                                                                                                                                                                                                                                                     |
| ROUND(value (, digits)?)       | Returns the rounded value to the given number of integer digits to the right of the decimal point (left if digits is negative). Digits are 0 if not given. The function uses Rounding Away From Zero convention to round midpoint values to the next number away from zero (so, for example, ROUND(1.75) returns 1.8 but ROUND(1.85) returns 1.9.                |
| ROUND\_EVEN(value (, digits)?) | Returns rounded value to the given number of integer digits to the right of the decimal point (left if digits is negative). Digits are 0 if not given. The function uses Rounding to Nearest Even (Banker's Rounding) convention which rounds midpoint values to the nearest even number (for example, both ROUND\_EVEN(1.75) and ROUND\_EVEN(1.85) return 1.8). |
| SIGN(value)                    | Returns -1 for negative, 0 for zero, and 1 for positive numbers.                                                                                                                                                                                                                                                                                                 |
| SIN(value)                     | Returns sine of an angle in radians.                                                                                                                                                                                                                                                                                                                             |
| SQRT(value)                    | Returns the square root.                                                                                                                                                                                                                                                                                                                                         |
| TAN(value)                     | Returns tangent of an angle in radians.                                                                                                                                                                                                                                                                                                                          |
| TRUNC(value (, digits)?)       | Returns a truncated number to the given number of integer digits to the right of the decimal point (left if digits is negative). Digits are 0 if not given.                                                                                                                                                                                                      |

> [!NOTE]
> The behavior of the `ROUND()` function is different from SQL++ for Server `ROUND()`, which rounds the midpoint values using Rounding to Nearest Even convention.

### [](#pattern-searching-functions)Pattern Searching Functions

#### [](#table-16-pattern-searching-functions)Table 16\. Pattern Searching Functions

| Function                                      | Description                                                                                                                                                                              |
| --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| REGEXP\_CONTAINS(value, pattern)              | Returns TRUE if the string value contains any sequence that matches the regular expression pattern.                                                                                      |
| REGEXP\_LIKE(value, pattern)                  | Return TRUE if the string value exactly matches the regular expression pattern.                                                                                                          |
| REGEXP\_POSITION(value, pattern)              | Returns the first position of the occurrence of the regular expression pattern within the input string expression. Returns \-1 if no match is found. Position counting starts from zero. |
| REGEXP\_REPLACE(value, pattern, repl \[, n\]) | Returns a new string with occurrences of pattern replaced with repl. If n is given, at the most n replacements are performed. If n is not given, all matching occurrences are replaced.  |

### [](#string-functions)String Functions

#### [](#table-17-string-functions)Table 17\. String Functions

| Function                   | Description                                                                                          |
| -------------------------- | ---------------------------------------------------------------------------------------------------- |
| CONTAINS(value, substring) | Returns TRUE if the substring exists within the input string, otherwise returns FALSE.               |
| LENGTH(value)              | Returns the length of a string. The length is defined as the number of characters within the string. |
| LOWER(value)               | Returns the lower-case string of the input string.                                                   |
| LTRIM(value)               | Returns the string with all leading whitespace characters removed.                                   |
| RTRIM(value)               | Returns the string with all trailing whitespace characters removed.                                  |
| TRIM(value)                | Returns the string with all leading and trailing whitespace characters removed.                      |
| UPPER(value)               | Returns the upper-case string of the input string.                                                   |

### [](#type-checking-functions)Type Checking Functions

#### [](#table-18-type-checking-functions)Table 18\. Type Checking Functions

| Function         | Description                                                                                                                                       |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| ISARRAY(value)   | Returns TRUE if value is an array, otherwise returns MISSING, NULL or FALSE.                                                                      |
| ISATOM(value)    | Returns TRUE if value is a boolean, number, or string, otherwise returns MISSING, NULL or FALSE.                                                  |
| ISBOOLEAN(value) | Returns TRUE if value is a boolean, otherwise returns MISSING, NULL or FALSE.                                                                     |
| ISNUMBER(value)  | Returns TRUE if value is a number, otherwise returns MISSING, NULL or FALSE.                                                                      |
| ISOBJECT(value)  | Returns TRUE if value is an object (dictionary), otherwise returns MISSING, NULL or FALSE.                                                        |
| ISSTRING(value)  | Returns TRUE if value is a string, otherwise returns MISSING, NULL or FALSE.                                                                      |
| TYPE(value)      | Returns one of the following strings, based on the value of value:• "missing"• "null"• "boolean"• "number"• "string"• "array"• "object"• "binary" |

### [](#type-conversion-functionsunctions)Type Conversion Functionsunctions

#### [](#table-19-type-conversion-functions)Table 19\. Type Conversion Functions

| Function         | Description                                                                                                                                                                                                                                                                                     |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TOARRAY(value)   | Returns MISSING if the value is MISSING.Returns NULL if the value is NULL.Returns an array value as is.Returns all other values wrapped in an array.                                                                                                                                            |
| TOATOM(value)    | Returns MISSING if the value is MISSING.Returns NULL if the value is NULL.Returns an array of a single item if the value is an array.Returns an object of a single key/value pair if the value is an object.Returns a boolean, number, or string value as is.Returns NULL for all other values. |
| TOBOOLEAN(value) | Returns MISSING if the value is MISSING.Returns NULL if the value is NULL.Returns FALSE if the value is FALSE.Returns FALSE if the value is 0 or NaN.Returns FALSE if the value is an empty string, array, and object.Return TRUE for all other values.                                         |
| TONUMBER(value)  | Returns MISSING if the value is MISSING.Returns NULL if the value is NULL.Returns 0 if the value is FALSE.Returns 1 if the value is TRUE.Returns a number value as is.Parses a string value in to a number.Returns NULL for all other values.                                                   |
| TOOBJECT(value)  | Returns MISSING if the value is MISSING.Returns NULL if the value is NULL.Returns an object value as is.Returns an empty object for all other values.                                                                                                                                           |
| TOSTRING(value)  | Returns MISSING if the value is MISSING.Returns NULL if the value is NULL.Returns "false" if the value is FALSE.Returns "true" if the value is TRUE.Returns a string representation of a number value.Returns a string value as is.Returns NULL for all other values.                           |

## [](#querybuilder-differences)QueryBuilder Differences

SQL++ for Mobile queries support all `QueryBuilder` features. See <<,Table 20>> for the features supported by SQL++ for Mobile but not by `QueryBuilder`.

#### Table 20\. QueryBuilder Differences

| Category                   | Components                                                                                 |
| -------------------------- | ------------------------------------------------------------------------------------------ |
| Conditional Operator       | CASE(WHEN ... THEN ... ELSE ...)                                                           |
| Array Functions            | ARRAY\_AGG, ARRAY\_AVG, ARRAY\_COUNT, ARRAY\_IFNULL, ARRAY\_MAX, ARRAY\_MIN, ARRAY\_SUM    |
| Conditional Functions      | IFMISSING, IFMISSINGORNULL, IFNULL, MISSINGIF, NULLIF, MATCH, RANK, DIV, IDIV, ROUND\_EVEN |
| Pattern Matching Functions | REGEXP\_CONTAINS, REGEXP\_LIKE, REGEXP\_POSITION, REGEXP\_REPLACE                          |
| Type Checking Functions    | ISARRAY, ISATOM, ISBOOLEAN, ISNUMBER, ISOBJECT, ISSTRING, TYPE                             |
| Type Conversion Functions  | TOARRAY, TOATOM, TOBOOLEAN, TONUMBER, TOOBJECT, TOSTRING                                   |

## [](#query-parameters)Query Parameters

You can provide runtime parameters to your SQL++ query to make it more flexible. To specify substitutable parameters within your query string prefix the name with `$` \- see: [Example 51](#example-51-running-a-sql-query).

#### Example 51\. Running a SQL++ Query

You can provide runtime parameters to your SQL++ query to make it more flexible. To specify substitutable parameters within your query string prefix the name with $ - see: [Example 51](#example-51-running-a-sql-query).

```typescript
const query = await database.createQuery(
  'SELECT META().id AS docId FROM hotel WHERE country = $country'
);

const params = new Parameters();
params.setString('country','France')
query.parameters = params;
const resultSet = await query.execute();
```

1. Define a parameter placeholder `$country`.
2. Set the value of the `country` parameter.