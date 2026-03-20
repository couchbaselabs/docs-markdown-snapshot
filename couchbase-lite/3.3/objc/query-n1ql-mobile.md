---
title: SQL++ Query Strings
description: How to use SQL++ Query Strings to build effective queries with
  Couchbase Lite on Objective-C
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.3/modules/objc/pages/query-n1ql-mobile.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:3.3@couchbase-lite:objc:query-n1ql-mobile.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.3/objc/query-n1ql-mobile.html)

# SQL++ Query Strings

> Description — _How to use SQL++ Query Strings to build effective queries with Couchbase Lite on Objective-C_  
> Related Content — [Predictive Queries](querybuilder.md#lbl-predquery) | [Live Queries](query-live.md) | [Indexing](indexing.md)

> [!NOTE]
> The examples used in this topic are based on the _Travel Sample_ app and data introduced in the [Couchbase Mobile Workshop](https://docs.couchbase.com/tutorials/mobile-travel-tutorial/introduction.html) tutorial

## [](#introduction)Introduction

Developers using Couchbase Lite for Objective-C can provide SQL++ query strings using the SQL++ Query API. This API uses query statements of the form shown in [Example 2](#ex-query-form).

The structure and semantics of the query format are based on that of Couchbase Server’s SQL++ query language — see [SQL++ Reference Guide](../../../server/current/n1ql/n1ql-language-reference/index.md) and [SQL++ Data Model](../../../server/current/learn/data/n1ql-versus-sql.md).

## [](#running)Running

The database can create a query object with the SQL++ string. See [Query Resultsets](query-resultsets.md) for how to work with result sets.

Example 1\. Running a SQL++ Query

```objc
NSString *queryString = @"SELECT * FROM _ WHERE type = \"hotel\""; (1)

CBLQuery *query = [self.database createQuery:queryString error: &error];

CBLQueryResultSet *results = [query execute:&error];
```

We are accessing the current database using the shorthand notation **`_`** — see the [FROM](#lbl-from) clause for more on data source selection and [Query Parameters](#lbl-query-params) for more on parameterized queries.

## [](#query-format)Query Format

The API uses query statements of the form shown in [Example 2](#ex-query-form).

Example 2\. Query Format

```SQL
SELECT ____
FROM 'data-source'
WHERE ____,
JOIN ____
GROUP BY ____
ORDER BY ____
LIMIT ____
OFFSET ____
```

Query Components

| Component                        | Description                                                                                                          |
| -------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| [SELECT statement](#lbl-select)  | The document properties that will be returned in the result set                                                      |
| [FROM](#lbl-from)                | The data source to be queried                                                                                        |
| [JOIN statement](#lbl-join)      | The criteria for joining multiple documents                                                                          |
| [WHERE statement](#lbl-where)    | The query criteriaThe \`SELECT\`ed properties of documents matching this criteria will be returned in the result set |
| [Array UNNEST](#lbl-unnest)      | The criteria used to unpack arrays within a document into individual rows                                            |
| [GROUP BY statement](#lbl-group) | The criteria used to group returned items in the result set                                                          |
| [ORDER BY statement](#lbl-order) | The criteria used to order the items in the result set                                                               |
| [LIMIT statement](#lbl-limit)    | The maximum number of results to be returned                                                                         |
| [OFFSET statement](#lbl-offset)  | The number of results to be skipped before starting to return results                                                |

> [!TIP]
> We recommend working through the [SQL++ Tutorials](https://query-tutorial.couchbase.com/tutorial/#1) to build your SQL++ skills.

## [](#lbl-select)SELECT statement

### [](#purpose)Purpose

Projects the result returned by the query, identifying the columns it will contain.

### [](#syntax)Syntax

Example 3\. SQL++ Select Syntax

```sql
select = SELECT _ ( DISTINCT | ALL )? selectResult (1)

selectResults = selectResult ( _ ',' _ selectResult )* (2)

selectResult = expression ( _ (AS)? columnAlias )? (3)

columnAlias = IDENTIFIER
```

### [](#arguments)Arguments

| **1** | The select clause begins with the SELECT keyword. The optional ALL argument is used to specify that the query should return ALL results (the default) The optional DISTINCT argument specifies that the query should remove duplicated results.                      |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | selectResults is a list of columns projected in the query result. Each column is an expression which could be a property expression or any expressions or functions. You can use the wildcard **\*** to select all columns — see [Select Wildcard](#select-wildcard) |
| **3** | Use the optional AS argument to provides an alias name for a property. Each property can be aliased by putting the AS <alias name> after the column name.                                                                                                            |

#### [](#select-wildcard)Select Wildcard

When using the `SELECT *` option the column name (key) of the SQL++ string is one of:

* The alias name if one was specified
* The data source name (or its alias if provided) as specified in the `FROM` clause.

This behavior is inline with that of Couchbase Server SQL++ — see example in [Table 1](#tbl-selstar).

__Table 1\. Example Column Names for SELECT **\***__
| Query                      | Column Name |
| -------------------------- | ----------- |
| SELECT \* AS data FROM \_  | data        |
| SELECT \* FROM \_          | \_          |
| SELECT \* FROM \_default   | \_default   |
| SELECT \* FROM db          | db          |
| SELECT \* FROM db AS store | store       |

### [](#example)Example

Example 4\. SELECT properties

```sql
SELECT * (1)

SELECT db.* AS data (2)

SELECT name fullName (3)

SELECT db.name fullName (4)

SELECT DISTINCT address.city (5)
```

| **1** | Use the \* wildcard to select all properties                                         |
| ----- | ------------------------------------------------------------------------------------ |
| **2** | Select all properties from the db data source. Give the object an alias name of data |
| **3** | Select pair of properties                                                            |
| **4** | Select a specific property from the db data source.                                  |
| **5** | Select the property item city from its parent property address.                      |

See: [Query Resultsets](query-resultsets.md) for more on processing query results.

## [](#lbl-from)FROM

### [](#purpose-2)Purpose

Specifies the data source, or sources, and optionally applies an alias ( `AS`). It is mandatory.

### [](#syntax-2)Syntax

```sql
FROM dataSource  (1)
      (optional JOIN joinClause )  (2)
```

### [](#datasource)Datasource

A datasource can be:

* < database-name > : default collection
* \_ (underscore) : default collection
* < scope-name >.< collection-name > : a collection in a scope
* < collection-name > : a collection in the default scope

### [](#arguments-2)Arguments

| **1** | Here dataSource is the database name against which the query is to run or the <scope>.<collection>. Use AS to give the database an alias you can use within the query.To use the current datasource without specifying a name, use \_ as the datasource. |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | JOIN joinclause — use this optional argument to link datasources — see [JOIN statement](#lbl-join)                                                                                                                                                       |

### [](#example-2)Example

Example 5\. FROM clause

```sql
SELECT name FROM db
SELECT name FROM scope.collection
SELECT store.name FROM db AS store
SELECT store.name FROM db store
SELECT name FROM _
SELECT store.name FROM _ AS store
SELECT store.name FROM _ store
```

## [](#lbl-join)JOIN statement

### [](#purpose-3)Purpose

The JOIN clause enables you to select data from multiple data sources linked by criteria specified in the JOIN statement.

Currently only self-joins are supported. For example to combine airline details with route details, linked by the airline id — see [Example 6](#ex-join).

### [](#syntax-3)Syntax

```sql
joinClause = ( join )*

join = joinOperator _ dataSource _  (constraint)? (1)

joinOperator = ( LEFT (OUTER)? | INNER | CROSS )? JOIN (2)

dataSource = databaseName ( ( AS | _ )? databaseAlias )?

constraint ( ON expression )? (3)
```

### [](#arguments-3)Arguments

| **1** | The join clause starts with a JOIN operator followed by the data source.                                                                                                           |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Five JOIN operators are supported:JOIN, LEFT JOIN, LEFT OUTER JOIN, INNER JOIN, and CROSS JOIN.Note: JOIN and INNER JOIN are the same, LEFT JOIN and LEFT OUTER JOIN are the same. |
| **3** | The join constraint starts with the ON keyword followed by the expression that defines the joining constraints.                                                                    |

### [](#example-3)Example

```sql
SELECT db.prop1, other.prop2 FROM db JOIN db AS other ON db.key = other.key

SELECT db.prop1, other.prop2 FROM db LEFT JOIN db other ON db.key = other.key

SELECT * FROM route r JOIN airline a ON r.airlineid = meta(a).id WHERE a.country = "France"
```

Example 6\. Using JOIN to Combine Document Details

This example JOINS the document of type `route` with documents of type `airline` using the document ID (_id) on the \_airline_ document and `airlineid` on the _route_ document. 

```sql
SELECT * FROM travel-sample r JOIN travel-sample a ON r.airlineid = a.meta.id WHERE a.country = "France"
```

## [](#lbl-unnest)Array UNNEST

### [](#purpose-4)Purpose

You can use `UNNEST` in queries to unpack arrays within a document into individual rows. This functionality makes it possible to join them with its parent object in the query.

`UNNEST` is used within the `FROM` clause and can be chained to perform multi-level `UNNEST`.

You can also use a new type of index, the [Array Index](indexing.md#array-indexing), to allow querying with `UNNEST` more efficiently.

> [!NOTE]
> Couchbase Lite currently supports inner `UNNEST` only.

### [](#syntax-4)Syntax

The syntax for `UNNEST` is shown below:

```sqlpp
unnestClause = UNNEST expr ( ‘AS’? alias)?
```

> [!CAUTION]
> `"unnest"` will be defined as a new keyword in the SQL++ syntax. You cannot use the term as an identifier for a property name or data source unless you escape it using backticks.

### [](#examples)Examples

For examples of using Array Indexes in conjunction with `UNNEST`, see [Array Index](indexing.md#array-indexing).

We are also accessing the current database using the shorthand notation **`_`** — see the [FROM](#lbl-from) clause for more on data source selection and [Query Parameters](#lbl-query-params) for more on parameterized queries.

The following examples will use the example JSON document below to query results from:

```JSON
{
   "Name":"Sam",
   "contacts":[
     {
       "type":"primary",
       "address":{"street":"1 St","city":"San Pedro","state":"CA"},
       "phones":[
         {"type":"home","number":"310-123-4567"},
         {"type":"mobile","number":"310-123-6789"}
       ]
     },
     {
       "type":"secondary",
       "address":{"street":"5 St","city":"Seattle","state":"WA"},
       "phones":[
         {"type":"home","number":"206-123-4567"},
         {"type":"mobile","number":"206-123-6789"}
       ]
     }
   ],
   "likes":["soccer","travel"]
 }
```

Using the document above we can perform queries on a single nested array like so:

```sqlpp
SELECT name, interest FROM _ UNNEST likes as interest WHERE interest = "travel"
```

The query above will produce the following output from the document:

```JSON
{"name": "Sam", "like": "travel"}
```

You can perform similar operations on nested arrays:

```sqlpp
SELECT name, contact.type, phone.number
FROM profiles
UNNEST contacts as contact
UNNEST contact.phones as phone
WHERE phone.type = "mobile"
```

The query above will then produce the following output:

```JSON
{"name": "Sam", "type": "primary", "number": "310-123-6789"}
{"name": "Sam", "type": "secondary", "number": "206-123-6789"}
```

The output demonstrates retrieval of both primary and secondary contact numbers listed as type `"mobile"`.

> [!IMPORTANT]
> Array literals are not supported in CBL 3.3.0\. Attempting to create a query with array literals will return an error.

## [](#lbl-where)WHERE statement

### [](#purpose-5)Purpose

Specifies the selection criteria used to filter results.

As with SQL, use the `WHERE` statement to choose which documents are returned by your query.

### [](#syntax-5)Syntax

```sql
where = WHERE expression (1)
```

### [](#arguments-4)Arguments

| **1** | WHERE evalates expression to a BOOLEAN value. You can chain any number of Expressions in order to implement sophisticated filtering capabilities. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------- |

See also — [Operators](#lbl-operators) for more on building expressions and [Query Parameters](#lbl-query-params) for more on parameterized queries.

### [](#examples-2)Examples

```sql
SELECT name FROM db WHERE department = ‘engineer’ AND group = ‘mobile
```

## [](#lbl-group)GROUP BY statement

### [](#purpose-6)Purpose

Use `group by` to arrange values in groups of one or more properties.

### [](#syntax-6)Syntax

```sql
groupBy = grouping _( having )? (1)

grouping = GROUP BY expression( _ ',' _ expression )* (2)

having = HAVING expression (3)
```

### [](#arguments-5)Arguments

| **1** | The group by clause starts with the GROUP BY keyword followed by one or more expressions.                            |
| ----- | -------------------------------------------------------------------------------------------------------------------- |
| **2** | Grouping The group by clause is normally used together with the aggregate functions (e.g. COUNT, MAX, MIN, SUM, AVG) |
| **3** | Having — allows you to filter the result based on aggregate functions — for example, HAVING count(empnum)>100        |

### [](#examples-3)Examples

```sql
SELECT COUNT(empno), city FROM db GROUP BY city

SELECT COUNT(empno), city FROM db GROUP BY city HAVING COUNT(empno) > 100

SELECT COUNT(empno), city FROM db GROUP BY city HAVING COUNT(empno) > 100 WHERE state = ‘CA’
```

## [](#lbl-order)ORDER BY statement

### [](#purpose-7)Purpose

Sort query results based on a given expression result.

### [](#syntax-7)Syntax

```sql
orderBy = ORDER BY ordering ( _ ',' _ ordering )* (1)

ordering = expression ( _ order )? (2)

order = ( ASC / DESC ) (3)
```

### [](#arguments-6)Arguments

| **1** | orderBy — The order by clause starts with the ORDER BY keyword followed by the ordering clause.                                                         |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Ordering — The ordering clause specifies the properties or expressions to use for ordering the results.                                                 |
| **3** | Order — In each ordering clause, the sorting direction is specified using the optional ASC (ascending) or DESC (descending) directives. Default is ASC. |

### [](#examples-4)Examples

Example 7\. Simple usage

```sql
SELECT name FROM db  ORDER BY name

SELECT name FROM db  ORDER BY name DESC

SELECT name, score FROM db  ORDER BY name ASC, score DESC
```

## [](#lbl-limit)LIMIT statement

### [](#purpose-8)Purpose

Specifies the maximum number of results to be returned by the query.

### [](#syntax-8)Syntax

```sql
limit = LIMIT expression (1)
```

### [](#arguments-7)Arguments

| **1** | The LIMIT clause starts with the LIMIT keyword followed by an expression that will be evaluated as a number. |
| ----- | ------------------------------------------------------------------------------------------------------------ |

### [](#examples-5)Examples

Example 8\. Simple usage

```sql
SELECT name FROM db LIMIT 10 (1)
```

| **1** | Return only 10 results |
| ----- | ---------------------- |

## [](#lbl-offset)OFFSET statement

### [](#purpose-9)Purpose

Specifies the number of results to be skipped by the query.

### [](#syntax-9)Syntax

```sql
offset = OFFSET expression (1)
```

### [](#arguments-8)Arguments

| **1** | The offset clause starts with the OFFSET keyword followed by an expression that will be evaluated as a number that represents the number of results ignored before the query begins returning results. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

### [](#examples-6)Examples

Example 9\. Simple usage

```sql
SELECT name FROM db OFFSET 10 (1)

SELECT name FROM db  LIMIT 10 OFFSET 10 (2)
```

| **1** | Ignore first 10 results                                 |
| ----- | ------------------------------------------------------- |
| **2** | Ignore first 10 results then return the next 10 results |

## [](#lbl-literals)Expressions

In this section

[Literals](#lbl-exp-literals) | [Identifiers](#lbl-exp-ident) | [Property Expressions](#lbl-exp-prop) | [Any and Every Expressions](#lbl-exp-any) | [Parameter Expressions](#lbl-exp-param) | [Parenthesis Expressions](#lbl-exp-paren)

Expressions are references to identifiers that resolve to values. Categories of expression comprise the elements covered in this section (see above), together with [Operators](#lbl-operators) and [Functions](#lbl-functions), which are covered in their own sections

### [](#lbl-exp-literals)Literals

[Boolean](#lbl-lit-bool) | [Numeric](#lbl-lit-numbers) | [String](#lbl-lit-string) | [NULL](#lbl-lit-null) | [MISSING](#lbl-lit-missing) | [Array](#lbl-lit-array) | [Dictionary](#lbl-lit-dict) | 

#### [](#lbl-lit-bool)Boolean

#### [](#purpose-10)Purpose

Represents a true or false value.

#### [](#syntax-10)Syntax

`TRUE | FALSE`

#### [](#example-4)Example

```sql
SELECT value FROM db  WHERE value = true
SELECT value FROM db  WHERE value = false
```

#### [](#lbl-lit-numbers)Numeric

#### [](#purpose-11)Purpose

Represents a numeric value. Numbers may be signed or unsigned digits. They have optional fractional and exponent components.

#### [](#syntax-11)Syntax

```sql
'-'? (('.' DIGIT+) | (DIGIT+ ('.' DIGIT*)?)) ( [Ee] [-+]? DIGIT+ )? WB

DIGIT = [0-9]
```

#### [](#example-5)Example

```sql
SELECT value FROM db  WHERE value = 10
SELECT value FROM db  WHERE value = 0
SELECT value FROM db WHERE value = -10
SELECT value FROM db WHERE value = 10.25
SELECT value FROM db WHERE value = 10.25e2
SELECT value FROM db WHERE value = 10.25E2
SELECT value FROM db WHERE value = 10.25E+2
SELECT value FROM db WHERE value = 10.25E-2
```

#### [](#lbl-lit-string)String

#### [](#purpose-12)Purpose

The string literal represents a string or sequence of characters.

#### [](#syntax-12)Syntax

```sql
“characters” |  ‘characters’ (1)
```

| **1** | The string literal can be double-quoted as well as single-quoted. |
| ----- | ----------------------------------------------------------------- |

#### [](#example-6)Example

```sql
SELECT firstName, lastName FROM db WHERE middleName = “middle”
SELECT firstName, lastName FROM db WHERE middleName = ‘middle’
```

#### [](#lbl-lit-null)NULL

#### [](#purpose-13)Purpose

The literal NULL represents an empty value.

#### [](#syntax-13)Syntax

```sql
NULL
```

#### [](#example-7)Example

```sql
SELECT firstName, lastName FROM db WHERE middleName IS NULL
```

#### [](#lbl-lit-missing)MISSING

#### [](#purpose-14)Purpose

The MISSING literal represents a missing name-value pair in a document.

#### [](#syntax-14)Syntax

```sql
MISSING
```

#### [](#example-8)Example

```sql
SELECT firstName, lastName FROM db WHERE middleName IS MISSING
```

#### [](#lbl-lit-array)Array

#### [](#purpose-15)Purpose

Represents an Array

#### [](#syntax-15)Syntax

```sql
arrayLiteral = '[' _ (expression ( _ ',' _ e2:expression )* )? ']'
```

#### [](#example-9)Example

```sql
SELECT [“a”, “b”, “c”] FROM _
SELECT [ property1, property2, property3] FROM _
```

#### [](#lbl-lit-dict)Dictionary

#### [](#purpose-16)Purpose

Represents a dictionary literal

#### [](#syntax-16)Syntax

```sql
dictionaryLiteral = '{' _ ( STRING_LITERAL ':' e:expression
  ( _ ',' _ STRING_LITERAL ':' _ expression )* )?
   '}'
```

#### [](#example-10)Example

```sql
SELECT { ‘name’: ‘James’, ‘department’: 10 } FROM db
SELECT { ‘name’: ‘James’, ‘department’: dept } FROM db
SELECT { ‘name’: ‘James’, ‘phones’: [‘650-100-1000’, ‘650-100-2000’] } FROM db
```

### [](#lbl-exp-ident)Identifiers

#### [](#purpose-17)Purpose

Identifiers provide symbolic references. Use them for example to identify: column alias names, database names, database alias names, property names, parameter names, function names, and FTS index names.

#### [](#syntax-17)Syntax

```sql
<[a-zA-Z_] [a-zA-Z0-9_$]*> _ | "`" ( [^`] | "``"   )* "`"  _ (1)
```

| **1** | The identifier allows a-z, A-Z, 0-9, \_ (underscore), and $ character.The identifier is case sensitive. |
| ----- | ------------------------------------------------------------------------------------------------------- |

> [!TIP]
> To use other characters in the identifier, surround the identifier with the backticks \` character.

#### [](#example-11)Example

Example 10\. Identifiers

```sql
SELECT * FROM _

SELECT * FROM `db-1` (1)

SELECT key FROM db

SELECT key$1 FROM db_1

SELECT `key-1` FROM db
```

| **1** | Use of backticks allows a hyphen as part of the identifier name. |
| ----- | ---------------------------------------------------------------- |

### [](#lbl-exp-prop)Property Expressions

#### [](#purpose-18)Purpose

The property expression is used to reference a property in a document

#### [](#syntax-18)Syntax

```sql
property = '*'| dataSourceName '.' _ '*'  | propertyPath (1)

propertyPath = propertyName (
    ('.' _ propertyName ) |  (2)
    ('[' _ INT_LITERAL _ ']' _  ) (3)
    )* (4)

propertyName = IDENTIFIER
```

| **1** | Prefix the property expression with the data source name or alias to indicate its origin                                       |
| ----- | ------------------------------------------------------------------------------------------------------------------------------ |
| **2** | Use dot syntax to refer to nested properties in the propertyPath.                                                              |
| **3** | Use bracket (\[index\]) syntax to refer to an item in an array.                                                                |
| **4** | Use the asterisk (\*) character to represents _all properties_. This can only be used in the result list of the SELECT clause. |

#### [](#example-12)Example

Example 11\. Property Expressions

```sql
SELECT *
  FROM db
  WHERE contact.name = "daniel"

SELECT db.*
  FROM db
  WHERE collection.contact.name = "daniel"

SELECT collection.contact.address.city
  FROM scope.collection
  WHERE collection.contact.name = "daniel"

SELECT contact.address.city
  FROM scope.collection
  WHERE contact.name = "daniel"

SELECT contact.address.city, contact.phones[0]
  FROM db
  WHERE contact.name = "daniel"
```

### [](#lbl-exp-any)Any and Every Expressions

#### [](#purpose-19)Purpose

Evaluates expressions over items in an array object.

#### [](#syntax-19)Syntax

```sql
arrayExpression = (1)
  anyEvery _ variableName (2)
     _ IN  _ expression (3)
       _ SATISFIES _ expression (4)
    END (5)

anyEvery = anyOrSome AND EVERY | anyOrSome | EVERY

anyOrSome = ANY | SOME
```

| **1** | The array expression starts with ANY/SOME, EVERY, or ANY/SOME AND EVERY, each of which has a different function as described below, and is terminated by END ANY/SOME : Returns TRUE if at least one item in the array satisfies the expression, otherwise returns FALSE.NOTE: ANY and SOME are interchangeable EVERY: Returns TRUE if all items in the array satisfies the expression, otherwise return FALSE. If the array is empty, returns TRUE. ANY/SOME AND EVERY: Same as EVERY but returns false if the array is empty. |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | The variable name represents each item in the array.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **3** | The IN keyword is used for specifying the array to be evaluated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **4** | The SATISFIES keyword is used for evaluating each item in the array.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **5** | END terminates the array expression.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

#### [](#example-13)Example

Example 12\. ALL and Every Expressions

```sql
SELECT name
  FROM db
  WHERE ANY v
          IN contacts
          SATISFIES v.city = ’San Mateo’
        END
```

### [](#lbl-exp-param)Parameter Expressions

#### [](#purpose-20)Purpose

Parameter expressions specify a value to be assigned from the parameter map presented when executing the query.

> [!NOTE]
> If parameters are specified in the query string, but the parameter and value mapping is not specified in the query object, an error will be thrown when executing the query.

#### [](#syntax-20)Syntax

```sql
$IDENTIFIER
```

#### [](#examples-7)Examples

Example 13\. Parameter Expression

```sql
SELECT name
  FROM db
  WHERE department = $department
```

Example 14\. Using a Parameter

```java
let q = Query(
          query: “SELECT name
                    WHERE department = $department”,
          database: db
        );

q.parameters =
      Parameters().setValue(“E001”, forName: "department"); (1)

let result = q.execute();
```

| **1** | The query resolves to SELECT name WHERE department = "E001" |
| ----- | ----------------------------------------------------------- |

### [](#lbl-exp-paren)Parenthesis Expressions

#### [](#purpose-21)Purpose

Use parentheses to group expressions together to make them more readable or to establish operator precedences.

#### [](#example-14)Example

Example 15\. Parenthesis Expression

```sql
SELECT (value1 + value2) * value 3 (1)
  FROM db

SELECT *
  FROM db
  WHERE ((value1 + value2) * value3) + value4 = 10

SELECT *
  FROM db
  WHERE (value1 = value2)
     OR (value3 = value4) (2)
```

| **1** | Establish the desired operator precedence; do the addition **before** the multiplication |
| ----- | ---------------------------------------------------------------------------------------- |
| **2** | Clarify the conditional grouping                                                         |

## [](#lbl-operators)Operators

In this section

[Binary Operators](#lbl-ops-binary) | [Unary Operators](#lbl-ops-unary) | [COLLATE Operators](#lbl-ops-coll) | [CONDITIONAL Operator](#lbl-ops-cond)

### [](#lbl-ops-binary)Binary Operators

[Maths](#lbl-ops-maths) | [Comparison Operators](#lbl-comp-ops) | [Logical Operators](#lbl-ops-logical) | [String Operator](#lbl-ops-string)

#### [](#lbl-ops-maths)Maths

__Table 2\. Maths Operators__
| Op | Desc                | Example             |
| -- | ------------------- | ------------------- |
| +  | Add                 | WHERE v1 + v2 = 10  |
| \- | Subtract            | WHERE v1 - v2 = 10  |
| \* | Multiply            | WHERE v1 \* v2 = 10 |
| /  | Divide — see note 1 | WHERE v1 / v2 = 10  |
| %  | Modulo              | WHERE v1 % v2 = 0   |

1 If both operands are integers, integer division is used, but if one is a floating number, then float division is used. This differs from Server SQL++, which performs float division regardless. Use `DIV(x, y)` to force float division in CBL SQL++

#### [](#lbl-comp-ops)Comparison Operators

#### [](#purpose-22)Purpose

The _comparison operators_ are used in the WHERE statement to specify the condition on which to match documents.

__Table 3\. Comparison Operators__
| Op             | Desc                                                                                                                                          | Example                                                                                                                                                                            |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \= or \==      | Equals                                                                                                                                        | WHERE v1 = v2WHERE v1 == v2                                                                                                                                                        |
| != or <>       | Not Equal to                                                                                                                                  | WHERE v1 != v2WHERE v1 <> v2                                                                                                                                                       |
| \>             | Greater than                                                                                                                                  | WHERE v1 > v2                                                                                                                                                                      |
| \>=            | Greater than or equal to                                                                                                                      | WHERE v1 >= v2                                                                                                                                                                     |
| \>             | Less than                                                                                                                                     | WHERE v1 < v2                                                                                                                                                                      |
| \>=            | Less than or equal to                                                                                                                         | WHERE v1 ⇐ v2                                                                                                                                                                      |
| IN             | Returns TRUE if the value is in the list or array of values specified by the right hand side expression; Otherwise returns FALSE.             | WHERE “James” IN contactsList                                                                                                                                                      |
| LIKE           | String wildcard pattern matching 2 comparison. Two wildcards are supported: % Matches zero or more characters. \_ Matches a single character. | WHERE name LIKE 'a%'WHERE name LIKE '%a'WHERE name LIKE '%or%'‘WHERE name LIKE 'a%o%'WHERE name LIKE '%\_r%'WHERE name LIKE '%a\_%'WHERE name LIKE '%a\_\_%'WHERE name LIKE 'aldo' |
| MATCH          | String matching using FTS see [Full Text Search Functions](#lbl-func-fts)                                                                     | WHERE v1-index MATCH "value"                                                                                                                                                       |
| BETWEEN        | Logically equivalent to v1>=X and v1⇐X+z                                                                                                      | WHERE v1 BETWEEN 10 and 100                                                                                                                                                        |
| IS 3 NULL      | Equal to null                                                                                                                                 | WHERE v1 IS NULL                                                                                                                                                                   |
| IS NOT NULL    | Not equal to null                                                                                                                             | WHERE v1 IS NOT NULL                                                                                                                                                               |
| IS MISSING     | Equal to MISSING                                                                                                                              | WHERE v1 IS MISSING                                                                                                                                                                |
| IS NOT MISSING | Not equal to MISSING                                                                                                                          | WHERE v1 IS NOT MISSING                                                                                                                                                            |
| IS VALUED      | IS NOT NULL AND MISSING                                                                                                                       | WHERE v1 IS VALUED                                                                                                                                                                 |
| IS NOT VALUED  | IS NULL OR MISSING                                                                                                                            | WHERE v1 IS NOT VALUED                                                                                                                                                             |

2 Matching is case-insensitive for ASCII characters, case-sensitive for non-ASCII.

3 Use of `IS` and `IS NOT` is limited to comparing `NULL` and `MISSING` values (this encompasses `VALUED`). This is different from QueryBuilder, in which they operate as equivalents of `==` and `!=`.

__Table 4\. Comparing NULL and MISSING values using IS.__
| OP             | NON-NULL Value | NULL  | MISSING |
| -------------- | -------------- | ----- | ------- |
| IS NULL        | FALSE          | TRUE  | MISSING |
| IS NOT NULL    | TRUE           | FALSE | MISSING |
| IS MISSING     | FALSE          | FALSE | TRUE    |
| IS NOT MISSING | TRUE           | TRUE  | FALSE   |
| IS VALUED      | TRUE           | FALSE | FALSE   |
| IS NOT VALUED  | FALSE          | TRUE  | TRUE    |

#### [](#lbl-ops-logical)Logical Operators

#### [](#purpose-23)Purpose

Logical operators combine expressions using the following Boolean Logic Rules:

* TRUE is TRUE, and FALSE is FALSE
* Numbers 0 or 0.0 are FALSE
* Arrays and dictionaries are FALSE
* String and Blob are TRUE if the values are casted as a non-zero or FALSE if the values are casted as 0 or 0.0
* NULL is FALSE
* MISSING is MISSING

> [!NOTE]
> This is different from Server SQL++, where:
> 
> * MISSING, NULL and FALSE are FALSE
> * Numbers 0 is FALSE
> * Empty strings, arrays, and objects are FALSE
> * All other values are TRUE
> 
> > [!TIP]
> > Use TOBOOLEAN(expr) function to convert a value based on Server SQL++ boolean value rules,

__Table 5\. Logical Operators__
| Op  | Description                                                                                                                                                                                                                                                                                                                                                   | Example                                              |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| AND | Returns TRUE if the operand expressions evaluate to TRUE; otherwise FALSE. If an operand is MISSING and the other is TRUE returns MISSING, if the other operand is FALSE it returns FALSE. If an operand is NULL and the other is TRUE returns NULL, if the other operand is FALSE it returns FALSE.                                                          | WHERE city = “San Francisco” AND status = true       |
| OR  | Returns TRUE if one of the operand expressions is evaluated to TRUE; otherwise returns FALSE. If an operand is MISSING, the operation will result in MISSING if the other operand is FALSE or TRUE if the other operand is TRUE. If an operand is NULL, the operation will result in NULL if the other operand is FALSE or TRUE if the other operand is TRUE. | WHERE city = “San Francisco” OR city = “Santa Clara” |

__Table 6\. Logical Operation Table__
| a       | b         | a AND b     | a OR b |
| ------- | --------- | ----------- | ------ |
| TRUE    | TRUE      | TRUE        | TRUE   |
| FALSE   | FALSE     | TRUE        |        |
| NULL    | FALSE 5-1 | TRUE        |        |
| MISSING | MISSING   | TRUE        |        |
| FALSE   | TRUE      | FALSE       | TRUE   |
| FALSE   | FALSE     | FALSE       |        |
| NULL    | FALSE     | FALSE 5-1   |        |
| MISSING | FALSE     | MISSING     |        |
| NULL    | TRUE      | FALSE 5-1   | TRUE   |
| FALSE   | FALSE     | FALSE 5-1   |        |
| NULL    | FALSE 5-1 | FALSE 5-1   |        |
| MISSING | FALSE 5-2 | MISSING 5-3 |        |
| MISSING | TRUE      | MISSING     | TRUE   |
| FALSE   | FALSE     | MISSING     |        |
| NULL    | FALSE 5-2 | MISSING 5-3 |        |
| MISSING | MISSING   | MISSING     |        |

> [!NOTE]
> This differs from Server SQL++ in the following instances:  
> 5-1 Server will return: NULL instead of FALSE  
> 5-2 Server will return: MISSING instead of FALSE  
> 5-3 Server will return: NULL instead of MISSING  

#### [](#lbl-ops-string)String Operator

#### [](#purpose-24)Purpose

A single string operator is provided. It enables string concatenation.

__Table 7\. String Operators__
| Op  | Description   | Example                                       |
| --- | ------------- | --------------------------------------------- |
| \|| | Concatenating | SELECT firstnm \|| lastnm AS fullname FROM db |

### [](#lbl-ops-unary)Unary Operators

#### [](#purpose-25)Purpose

Three unary operators are provided. They operate by modifying an expression, making it numerically positive or negative, or by logically negating its value (TRUE becomes FALSE).

#### [](#syntax-21)Syntax

```objc

```

__Table 8\. Unary Operators__
| Op  | Description                | Example                           |
| --- | -------------------------- | --------------------------------- |
| +   | Positive value             | WHERE v1 = +10                    |
| +   | Negative value             | WHERE v1 = -10                    |
| NOT | Logical Negate operator \* | WHERE "James" NOT IN contactsList |

\* The NOT operator is often used in conjunction with operators such as IN, LIKE, MATCH, and BETWEEN operators.  
NOT operation on NULL value returns NULL.  
NOT operation on MISSING value returns MISSING.

__Table 9\. NOT Operation TABLE__
| a       | NOT a   |
| ------- | ------- |
| TRUE    | FALSE   |
| FALSE   | TRUE    |
| NULL    | FALSE   |
| MISSING | MISSING |

### [](#lbl-ops-coll)COLLATE Operators

#### [](#purpose-26)Purpose

Collate operators specify how the string comparison is conducted.

#### [](#usage)Usage

The collate operator is used in conjunction with string comparison expressions and ORDER BY clauses. It allows for one or more collations.

If multiple collations are used, the collations need to be specified in a parenthesis. When only one collation is used, the parenthesis is optional.

> [!NOTE]
> Collate is not supported by Server SQL++

#### [](#syntax-22)Syntax

```sql
collate = COLLATE collation | '(' collation (_ collation )* ')'

collation = NO? (UNICODE | CASE | DIACRITICS) WB (1)
```

#### [](#arguments-9)Arguments

| **1** | The available collation options are: UNICODE: Conduct a Unicode comparison; the default is to do ASCII comparison. CASE: Conduct case-sensitive comparison DIACRITIC: Take account of accents and diacritics in the comparison; On by default. NO: This can be used as a prefix to the other collations, to disable them (for example: NOCASE to enable case-insensitive comparison) |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

#### [](#example-15)Example

```sql
SELECT department FROM db WHERE (name = "fred") COLLATE UNICODE
```

```sql
SELECT department FROM db WHERE (name = "fred")
COLLATE (UNICODE)
```

```sql
SELECT department FROM db WHERE (name = "fred") COLLATE (UNICODE CASE)
```

```sql
SELECT name FROM db ORDER BY name COLLATE (UNICODE DIACRITIC)
```

### [](#lbl-ops-cond)CONDITIONAL Operator

#### [](#purpose-27)Purpose

The Conditional (or `CASE`) operator evaluates conditional logic in a similar way to the IF/ELSE operator.

#### [](#syntax-23)Syntax

```sql
CASE (expression) (WHEN expression THEN expression)+ (ELSE expression)? END (1)

CASE (expression)? (!WHEN expression)?
  (WHEN expression THEN expression)+ (ELSE expression)? END (2)
```

Both _Simple Case_ and _Searched Case_ expressions are supported. The syntactic difference being that the _Simple Case_ expression has an expression after the CASE keyword.

| **1** | Simple Case Expression If the CASE expression is equal to the first WHEN expression, the result is the THEN expression. Otherwise, any subsequent WHEN clauses are evaluated in the same way. If no match is found, the result of the CASE expression is the ELSE expression, NULL if no ELSE expression was provided.           |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Searched Case Expression If the first WHEN expression is TRUE, the result of this expression is its THEN expression. Otherwise, subsequent WHEN clauses are evaluated in the same way. If no WHEN clause evaluate to TRUE, then the result of the expression is the ELSE expression, or NULL if no ELSE expression was provided. |

#### [](#example-16)Example

Example 16\. Simple Case

```sql
SELECT CASE state WHEN ‘CA’ THEN ‘Local’ ELSE ‘Non-Local’ END FROM DB
```

Example 17\. Searched Case

```sql
SELECT CASE WHEN shippedOn IS NOT NULL THEN ‘SHIPPED’ ELSE "NOT-SHIPPED" END FROM db
```

## [](#lbl-functions)Functions

In this section

[Aggregation Functions](#lbl-func-agg) | [Array Functions](#lbl-func-array) | [Conditional Functions](#lbl-func-cond) | [Date and Time Functions](#lbl-func-date) | [Full Text Search Functions](#lbl-func-fts) | [Maths Functions](#lbl-func-maths) | [Metadata Functions](#lbl-func-meta) | [Pattern Searching Functions](#lbl-func-pattern) | [String Functions](#lbl-func-string) | [Type Checking Functions](#lbl-func-typecheck) | [Type Conversion Functions](#lbl-func-typeconv)

### [](#purpose-28)Purpose

Functions are also expressions.

### [](#syntax-24)Syntax

The function syntax is the same as Java’s method syntax. It starts with the function name, followed by optional arguments inside parentheses.

```sql
function = functionName parenExprs

functionName  = IDENTIFIER

parenExprs = '(' ( expression (_ ',' _ expression )* )? ')'
```

### [](#lbl-func-agg)Aggregation Functions

__Table 10\. Aggregation Functions__
| Function    | Description                                             |
| ----------- | ------------------------------------------------------- |
| AVG(expr)   | Returns average value of the number values in the group |
| COUNT(expr) | Returns a count of all values in the group              |
| MIN(expr)   | Returns the minimum value in the group                  |
| MAX(expr)   | Returns the maximum value in the group                  |
| SUM(expr)   | Returns the sum of all number values in the group       |

### [](#lbl-func-array)Array Functions

__Table 11\. Array Functions__
| Function              | Description                                                                                      |
| --------------------- | ------------------------------------------------------------------------------------------------ |
| ARRAY\_AGG(expr)      | Returns an array of the non-MISSING group values in the input expression, including NULL values. |
| ARRAY\_AVG(expr)      | Returns the average of all non-NULL number values in the array; or NULL if there are none        |
| ARRAY\_CONTAINS(expr) | Returns TRUE if the value exists in the array; otherwise FALSE                                   |
| ARRAY\_COUNT(expr)    | Returns the number of non-null values in the array                                               |
| ARRAY\_IFNULL(expr)   | Returns the first non-null value in the array                                                    |
| ARRAY\_MAX(expr)      | Returns the largest non-NULL, non\_MISSING value in the array                                    |
| ARRAY\_MIN(expr)      | Returns the smallest non-NULL, non\_MISSING value in the array                                   |
| ARRAY\_LENGTH(expr)   | Returns the length of the array                                                                  |
| ARRAY\_SUM(expr)      | Returns the sum of all non-NULL numeric value in the array                                       |

### [](#lbl-func-cond)Conditional Functions

__Table 12\. Conditional Functions__
| Function                          | Description                                                                                                                                                                 |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IFMISSING(expr1, expr2, …​)       | Returns the first non-MISSING value, or NULL if all values are MISSING                                                                                                      |
| IFMISSINGRONULL(expr1, expr2, …​) | Returns the first non-NULL and non-MISSING value, or NULL if all values are NULL or MISSING                                                                                 |
| IFNULL(expr1, expr2, …​)          | Returns the first non-NULL, or NULL if all values are NULL                                                                                                                  |
| MISSINGIF(expr1, expr2)           | Returns MISSING when expr1 = expr2; otherwise returns expr1.Returns MISSING if either or both expressions are MISSING.Returns NULL if either or both expressions are NULL.+ |
| NULLF(expr1, expr2)               | Returns NULL when expr1 = expr2; otherwise returns expr1.Returns MISSING if either or both expressions are MISSING.Returns NULL if either or both expressions are NULL.+    |

### [](#lbl-func-date)Date and Time Functions

__Table 13\. Date and Time Functions__
| Function                                                                                                                                                                                                     | Arguments                                                                                                                                                                                                                                                                                                                  | Return Value                                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| STR\_TO\_MILLIS(date1) Coverts a date string to Epoch/UNIX milliseconds.                                                                                                                                     | date1 \- A valid date string.                                                                                                                                                                                                                                                                                              | Returns an integer containing the converted date string into Epoch/UNIX milliseconds.                                                                                                                                                                                 |
| STR\_TO\_UTC(date1) Converts a date string into the equivalent date in UTC.                                                                                                                                  | date1 \- A valid date string                                                                                                                                                                                                                                                                                               | Returns a date string representing the date string converted to UTC. The output date format follows the date format of the input date. Returns null if an invalid date format is provided.                                                                            |
| STR\_TO\_TZ(date1, tz) Converts a date string to it’s equivalent in the specified timezone.                                                                                                                  | date1 \- A valid date string. This is converted to UTC. tz \- An integer that represents minutes offset from UTC. For example, UTC-5 would be represented as \-300.                                                                                                                                                        | Returns a date string representing the date string converted to the specified timezone. Returns null if an invalid date format is provided.                                                                                                                           |
| MILLIS\_TO\_STR(date1) Converts an Epoch/UNIX timestamp into the specified date string format.                                                                                                               | date1 \- An integer representing an Epoch/UNIX timestamp in millseconds.                                                                                                                                                                                                                                                   | Returns a date string representing the local date. Returns null if an invalid timestamp is provided.                                                                                                                                                                  |
| MILLIS\_TO\_UTC(date1) Converts an Epoch/UNIX timestamp into a local time date string.                                                                                                                       | date1 \- An integer representing an Epoch/UNIX timestamp in millseconds.                                                                                                                                                                                                                                                   | Returns a date string representing the date in UTC. Returns null if an invalid timestamp is provided.                                                                                                                                                                 |
| MILLIS\_TO\_TZ(date1,tz, \[fmt\]) Converts an Epoch/UNIX timestamp into the specified time zone in the specified date string format.                                                                         | date1 \- An integer representing an Epoch/UNIX timestamp in milliseconds. tz \- An integer that represents minutes offset from UTC. For example, UTC-5 would be represented as \-300. fmt \- An optional string parameter representing a date format to output the result as.                                              | Returns a date string representing the date in the specified timezone in the specified format. If fmt is not specified, the output default to the combined full date and time.                                                                                        |
| DATE\_DIFF\_STR(date1, date2, part) Finds the elapsed time between two date strings. This is measured from date2 to date1.                                                                                   | date1 \- A valid date string. This is converted to UTC. date2 \- A valid date string. This is converted to UTC. part \- A string representing the date component units to return.                                                                                                                                          | Returns an integer representing the elapsed time measured from date2 to date1 (in units based on the specified part) between both dates. The value is positive if date1 is greater than date2, negative otherwise. Returns null if any of the parameters are invalid. |
| DATE\_DIFF\_MILLIS(date1, date2, part) Finds the elapsed time between two Epoch/UNIX timestamps.                                                                                                             | date1 \- An integer representing an Epoch/UNIX timestamp in milliseconds. date2 \- An integer representing an Epoch/UNIX timestamp in milliseconds. part \- A string representing the date component units to return.                                                                                                      | Returns an integer representing the elapsed time measured from date2 to date1 (in units based on the specified part) between both dates. The value is positive if date1 is greater than date2, negative otherwise. Returns null if any of the parameters are invalid. |
| DATE\_ADD\_STR(date1, n, part) Performs date arithmetic on a date string. For example DATE\_ADD\_STR("2024-03-20T15:43:01+0000", 3, "day") adds 3 days to the provided date.                                 | date1 \- A valid date string. This is converted to UTC. n \- An integer or expression that evaluates to an integer. A positive value will increment the date component whereas a negative value will decrement the date component. part \- A string representing the component of the date to increment.                   | Returns an integer representing the calculation result as an Epoch/UNIX timestamp in milliseconds. Returns null if any of the parameters are invalid.                                                                                                                 |
| DATE\_ADD\_MILLIS(date1, n, part) Performs date arithmetic on a particular component of an Epoch/UNIX timestamp value. For example DATE\_ADD\_STR(1710946158819, 3, 'day') adds 3 days to the provided date. | date1 \- An integer representing an Epoch/UNIX timestamp in milliseconds. n \- An integer or expression that evaluates to an integer. A positive value will increment the date component whereas a negative value will decrement the date component. part \- A string representing the component of the date to increment. | Returns an integer representing the calculation result as an Epoch/UNIX timestamp in milliseconds. Returns null if any of the parameters are invalid.                                                                                                                 |

### [](#lbl-func-fts)Full Text Search Functions

__Table 14\. FTS Functions__
| Function               | Description                                                                                                                                                               | Example                                                           |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| MATCH(indexName, term) | Returns TRUE if term expression matches the FTS indexed term. indexName identifies the FTS index, term expression to search for matching.                                 | WHERE MATCH (description, “couchbase”)                            |
| RANK(indexName)        | Returns a numeric value indicating how well the current query result matches the full-text query when performing the MATCH. indexName is an IDENTIFIER for the FTS index. | WHERE MATCH (description, “couchbase”) ORDER BY RANK(description) |

### [](#lbl-func-maths)Maths Functions

__Table 15\. Maths Functions__
| Function                            | Description                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| ABS(expr)                           | Returns the absolute value of a number.                                                                                                                                                                                                                                                                                                                            |
| ACOS(expr)                          | Returns the arc cosine in radians.                                                                                                                                                                                                                                                                                                                                 |
| ASIN(expr)                          | Returns the arcsine in radians.                                                                                                                                                                                                                                                                                                                                    |
| ATAN(expr)                          | Returns the arctangent in radians.                                                                                                                                                                                                                                                                                                                                 |
| ATAN2(expr1,expr2)                  | Returns the arctangent of expr1/expr2.                                                                                                                                                                                                                                                                                                                             |
| CEIL(expr)                          | Returns the smallest integer not less than the number.                                                                                                                                                                                                                                                                                                             |
| COS(expr)                           | Returns the cosine value of the expression.                                                                                                                                                                                                                                                                                                                        |
| DIV(expr1, expr2)                   | Returns float division of expr1 and expr2.Both expr1 and expr2 are cast to a double number before division.The returned result is always a double.                                                                                                                                                                                                                 |
| DEGREES(expr)                       | Converts radians to degrees.                                                                                                                                                                                                                                                                                                                                       |
| E()                                 | Returns base of natural logarithms.                                                                                                                                                                                                                                                                                                                                |
| EXP(expr)                           | Returns expr value                                                                                                                                                                                                                                                                                                                                                 |
| FLOOR(expr)                         | Returns largest integer not greater than the number.                                                                                                                                                                                                                                                                                                               |
| IDIV(expr1, expr2)                  | Returns integer division of expr1 and expr2.                                                                                                                                                                                                                                                                                                                       |
| LN(expr)                            | Returns log base e value.                                                                                                                                                                                                                                                                                                                                          |
| LOG(expr)                           | Returns log base 10 value.                                                                                                                                                                                                                                                                                                                                         |
| PI()                                | Return PI value.                                                                                                                                                                                                                                                                                                                                                   |
| POWER(expr1, expr2)                 | Returns expr1expr2 value.                                                                                                                                                                                                                                                                                                                                          |
| RADIANS(expr)                       | Returns degrees to radians.                                                                                                                                                                                                                                                                                                                                        |
| ROUND(expr (, digits\_expr)?)       | Returns the rounded value to the given number of integer digits to the right of the decimal point (left if digits is negative). Digits are 0 if not given.The function uses Rounding Away From Zero convention to round midpoint values to the next number away from zero (so, for example, ROUND(1.75) returns 1.8 but ROUND(1.85) returns 1.9\. \*               |
| ROUND\_EVEN(expr (, digits\_expr)?) | Returns rounded value to the given number of integer digits to the right of the decimal point (left if digits is negative). Digits are 0 if not given. The function uses _Rounding to Nearest Even_ (Banker’s Rounding) convention which rounds midpoint values to the nearest even number (for example, both ROUND\_EVEN(1.75) and ROUND\_EVEN(1.85) return 1.8). |
| SIGN(expr)                          | Returns -1 for negative, 0 for zero, and 1 for positive numbers.                                                                                                                                                                                                                                                                                                   |
| SIN(expr)                           | Returns sine value.                                                                                                                                                                                                                                                                                                                                                |
| SQRT(expr)                          | Returns square root value.                                                                                                                                                                                                                                                                                                                                         |
| TAN(expr)                           | Returns tangent value.                                                                                                                                                                                                                                                                                                                                             |
| TRUNC (expr (, digits, expr)?)      | Returns a truncated number to the given number of integer digits to the right of the decimal point (left if digits is negative). Digits are 0 if not given.                                                                                                                                                                                                        |

\* The behavior of the ROUND() function is different from Server SQL++ ROUND(), which rounds the midpoint values using _Rounding to Nearest Even_ convention.

### [](#lbl-func-meta)Metadata Functions

__Table 16\. Metadata Functions__
| Function              | Description                                                                                                                                                                                                                                                                                                                                                                                                | Example                                                                                                                                                                                                                            |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| META(dataSourceName?) | Returns a dictionary containing metadata properties including: id : document identifier sequence : document mutating sequence number deleted : flag indicating whether document is deleted or not expiration : document expiration date in timestamp format The optional dataSourceName identifies the database or the database alias name.To access a specific metadata property, use the dot expression. | SELECT META() FROM db SELECT META().id, META().sequence, META().deleted, META().expiration FROM db SELECT p.name, r.rating FROM product as p INNER JOIN reviews AS r ON META(r).id IN p.reviewList WHERE META(p).id = "product320" |

### [](#lbl-func-pattern)Pattern Searching Functions

__Table 17\. Pattern Searching Functions__
| Function                                     | Description                                                                                                                                                                            |
| -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| REGEXP\_CONTAINS(expr, pattern)              | Returns TRUE if the string value contains any sequence that matches the regular expression pattern.                                                                                    |
| REGEXP\_LIKE(expr, pattern)                  | Return TRUE if the string value exactly matches the regular expression pattern.                                                                                                        |
| REGEXP\_POSITION(expr, pattern)              | Returns the first position of the occurrence of the regular expression pattern within the input string expression. Return -1 if no match is found. Position counting starts from zero. |
| REGEXP\_REPLACE(expr, pattern, repl \[, n\]) | Returns new string with occurrences of pattern replaced with repl. If n is given, at the most n replacements are performed. If n is not given, all matching occurrences are replaced.  |

### [](#lbl-func-string)String Functions

__Table 18\. String Functions__
| Function                        | Description                                                                                          |
| ------------------------------- | ---------------------------------------------------------------------------------------------------- |
| CONTAINS(expr, substring\_expr) | Returns true if the substring exists within the input string, otherwise returns false.               |
| LENGTH(expr)                    | Returns the length of a string. The length is defined as the number of characters within the string. |
| LOWER(expr)                     | Returns the lowercase string of the input string.                                                    |
| LTRIM(expr)                     | Returns the string with all leading whitespace characters removed.                                   |
| RTRIM(expr)                     | Returns the string with all trailing whitespace characters removed.                                  |
| TRIM(expr)                      | Returns the string with all leading and trailing whitespace characters removed.                      |
| UPPER(expr)                     | Returns the uppercase string of the input string.                                                    |

### [](#lbl-func-typecheck)Type Checking Functions

__Table 19\. Type Checking Functions__
| Function        | Description                                                                                                                                    |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| ISARRAY(expr)   | Returns TRUE if expression is an array, otherwise returns MISSING, NULL or FALSE.                                                              |
| ISATOM(expr)    | Returns TRUE if expression is a Boolean, number, or string, otherwise returns MISSING, NULL or FALSE.                                          |
| ISBOOLEAN(expr) | Returns TRUE if expression is a Boolean, otherwise returns MISSING, NULL or FALSE.                                                             |
| ISNUMBER(expr)  | Returns TRUE if expression is a number, otherwise returns MISSING, NULL or FALSE.                                                              |
| ISOBJECT(expr)  | Returns TRUE if expression is an object (dictionary), otherwise returns MISSING, NULL or FALSE.                                                |
| ISSTRING(expr)  | Returns TRUE if expression is a string, otherwise returns MISSING, NULL or FALSE.                                                              |
| TYPE(expr)      | Returns one of the following strings, based on the value of expression: “missing” “null” “boolean” “number” “string” “array” “object” “binary” |

### [](#lbl-func-typeconv)Type Conversion Functions

__Table 20\. Type Conversion Functions__
| Function                                                                | Description                              |
| ----------------------------------------------------------------------- | ---------------------------------------- |
| TOARRAY(expr)                                                           | Returns MISSING if the value is MISSING. |
| Returns NULL if the value is NULL.                                      |                                          |
| Returns the array itself.                                               |                                          |
| Returns all other values wrapped in an array.                           |                                          |
| TOATOM(expr)                                                            | Returns MISSING if the value is MISSING. |
| Returns NULL if the value is NULL.                                      |                                          |
| Returns an array of a single item if the value is an array.             |                                          |
| Returns an object of a single key/value pair if the value is an object. |                                          |
| Returns boolean, numbers, or strings                                    |                                          |
| Returns NULL for all other values.                                      |                                          |
| TOBOOLEAN(expr)                                                         | Returns MISSING if the value is MISSING. |
| Returns NULL if the value is NULL.                                      |                                          |
| Returns FALSE if the value is FALSE.                                    |                                          |
| Returns FALSE if the value is 0 or NaN.                                 |                                          |
| Returns FALSE if the value is an empty string, array, and object.       |                                          |
| Return TRUE for all other values.                                       |                                          |
| TONUMBER(expr)                                                          | Returns MISSING if the value is MISSING. |
| Returns NULL if the value is NULL.                                      |                                          |
| Returns 0 if the value is FALSE.                                        |                                          |
| Returns 1 if the value is TRUE.                                         |                                          |
| Returns NUMBER if the value is NUMBER.                                  |                                          |
| Returns NUMBER parsed from the string value.                            |                                          |
| Returns NULL for all other values.                                      |                                          |
| TOOBJECT(expr)                                                          | Returns MISSING if the value is MISSING. |
| Returns NULL if the value is NULL.                                      |                                          |
| Returns the object if the value is an object.                           |                                          |
| Returns an empty object for all other values.                           |                                          |
| TOSTRING(expr)                                                          | Returns MISSING if the value is MISSING. |
| Returns NULL if the value is NULL.                                      |                                          |
| Returns “false” if the value is FALSE.                                  |                                          |
| Returns “true” if the value is TRUE.                                    |                                          |
| Returns NUMBER in String if the value is NUMBER.                        |                                          |
| Returns the string value if the value is a string.                      |                                          |
| Returns NULL for all other values.                                      |                                          |

## [](#querybuilder-differences)QueryBuilder Differences

Couchbase Lite SQL++ Query supports all QueryBuilder features, except _Predictive Query_ and _Index_. See [Table 21](#tbl-qbldr-diffs) for the features supported by SQL++ but not by QueryBuilder.

__Table 21\. QueryBuilder Differences__
| Category                   | Components                                                                             |
| -------------------------- | -------------------------------------------------------------------------------------- |
| Conditional Operator       | CASE(WHEN …​ THEN …​ ELSE ..)                                                          |
| Array Functions            | ARRAY\_AGG ARRAY\_AVG ARRAY\_COUNT ARRAY\_IFNULL ARRAY\_MAX ARRAY\_MIN ARRAY\_SUM      |
| Conditional Functions      | IFMISSING IFMISSINGORNULL IFNULL MISSINGIF NULLIF Match Functions DIV IDIV ROUND\_EVEN |
| Pattern Matching Functions | REGEXP\_CONTAINS REGEXP\_LIKE REGEXP\_POSITION REGEXP\_REPLACE                         |
| Type Checking Functions    | ISARRAY ISATOM ISBOOLEAN ISNUMBER ISOBJECT ISSTRING TYPE                               |
| Type Conversion Functions  | TOARRAY TOATOM TOBOOLEAN TONUMBER TOOBJECT TOSTRING                                    |

## [](#lbl-query-params)Query Parameters

You can provide runtime parameters to your SQL++ query to make it more flexible.

To specify substitutable parameters within your query string prefix the name with **`$`**, `$type` — see: [Example 18](#ex-sample-params).

Example 18\. Running a SQL++ Query

```objc
NSString *queryString = [NSString stringWithFormat:@"SELECT * FROM _ WHERE type = $type"]; (1)

CBLQuery *query = [self.database createQuery:queryString error: &error];

CBLQueryParameters *params = [[CBLQueryParameters alloc] init];
[params setString:@"hotel" forName:@"type"]; (2)
query.parameters = params;

CBLQueryResultSet *results =  [query execute:&error];
```

| **1** | Define a parameter placeholder $type |
| ----- | ------------------------------------ |
| **2** | Set the value of the $type parameter |

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Prerequisites](gs-prereqs.md)
* [Install](gs-install.md)
* [Build and Run](gs-build.md)

.

###### [](#-2)

Learn more . . .

* [Databases](database.md)
* [Documents](document.md)
* [Blobs](blob.md)
* [Remote Sync Gateway](replication.md)
* [Handling Data Conflicts](conflict.md)

.

###### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.