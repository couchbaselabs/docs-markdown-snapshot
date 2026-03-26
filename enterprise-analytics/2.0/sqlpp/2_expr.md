---
title: Expressions
description: A description of SQL++ for Enterprise Analytics expressions.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/sqlpp/pages/2_expr.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.0@enterprise-analytics:sqlpp:2_expr.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.0/sqlpp/2_expr.html)

# Expressions

> A description of SQL++ for Enterprise Analytics expressions. 

An expression is a language fragment that SQL++ evaluates to return a value. For example, the expression 2 + 3 returns the value 5\. You use expressions as building blocks for constructing queries. SQL++ for Enterprise Analytics supports nearly all of the kinds of expressions in SQL, and adds some new kinds as well.

SQL++ is an orthogonal language, which means that expressions can serve as operands of higher-level expressions. By nesting expressions inside other expressions, you can build up complex queries. You can enclose any expression in parentheses to establish operator precedence.

This topic introduces the SQL++ for Enterprise Analytics expressions.

##### Expr

![Expr](_images/Expr.png) 

## [](#Operator%5Fexpressions)Operator Expressions

Operators perform a specific operation on the input values or expressions. The syntax of an operator expression follows.

##### OperatorExpr

![OperatorExpr](_images/OperatorExpr.png) 

SQL++ for Enterprise Analytics provides a full set of operators that you can use in statements. Operators are categorized as follows:

* [Arithmetic Operators](#Arithmetic%5Foperators) perform basic mathematical operations
* [Collection Operators](#Collection%5Foperators) evaluate expressions on collections or objects
* [Comparison Operators](#Comparison%5Foperators) compare two expressions
* [Logical Operators](#Logical%5Foperators) combine operators using Boolean logic

The following table summarizes the precedence, in descending order, of the major unary and binary operators:

| Operator                                                                                               | Operation                                  |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------ |
| EXISTS, NOT EXISTS                                                                                     | Collection emptiness testing               |
| ^                                                                                                      | Exponentiation                             |
| \*, /, DIV, MOD (%)                                                                                    | Multiplication, division, modulo           |
| +, -                                                                                                   | Addition, subtraction                      |
| \||                                                                                                    | String concatenation                       |
| IS NULL, IS NOT NULL, IS MISSING, IS NOT MISSING, IS UNKNOWN, IS NOT UNKNOWN, IS VALUED, IS NOT VALUED | Unknown value comparison                   |
| BETWEEN, NOT BETWEEN                                                                                   | Range comparison (inclusive on both sides) |
| \=, !=, <>, <, >, <=, >=, LIKE, NOT LIKE, IN, NOT IN, IS DISTINCT FROM, IS NOT DISTINCT FROM           | Comparison                                 |
| NOT                                                                                                    | Logical negation                           |
| AND                                                                                                    | Conjunction                                |
| OR                                                                                                     | Disjunction                                |

In general, if any operand evaluates to a `MISSING` value, the enclosing operator returns `MISSING`. If none of the operands evaluates to a `MISSING` value but there is an operand that evaluates to a `NULL` value, the enclosing operator returns `NULL`. For information about exceptions to these results, see [comparison operators](#Comparison%5Foperators) and [logical operators](#Logical%5Foperators).

### [](#Arithmetic%5Foperators)Arithmetic Operators

You use arithmetic operators to add, subtract, multiply, divide, and exponentiate numeric values, or to concatenate string values.

| Operator | Purpose                                                      | Example                                            |
| -------- | ------------------------------------------------------------ | -------------------------------------------------- |
| +, -     | As unary operators, denote a positive or negative expression | SELECT VALUE -1; returns \[ -1 \]                  |
| +, -     | As binary operators, add or subtract                         | SELECT VALUE 1 + 2; returns \[ 3 \]                |
| \*       | Multiply                                                     | SELECT VALUE 4 \* 2; returns \[ 8 \]               |
| /        | Float division, returns a value of type double               | SELECT VALUE 5 / 2; returns \[ 2.5 \]              |
| DIV      | Integer division, returns a value of type bigint             | SELECT VALUE 5 DIV 2; returns \[ 2 \]              |
| MOD (%)  | Modulo, returns the remainder of a division                  | SELECT VALUE 5 % 2; returns \[ 1 \]                |
| ^        | Exponentiation                                               | SELECT VALUE 2^3; returns \[ 8 \]                  |
| \||      | String concatenation                                         | SELECT VALUE "ab"\||"c"||"d"; returns \[ "abcd" \] |

### [](#Collection%5Foperators)Collection Operators

You use collection operators for membership tests (IN, NOT IN) or empty collection tests (EXISTS, NOT EXISTS).

| Operator   | Purpose                                 | Example                                                                          |
| ---------- | --------------------------------------- | -------------------------------------------------------------------------------- |
| IN         | Membership test                         | FROM customers AS cWHERE c.address.zipcode IN \["02340", "02115"\]SELECT \*;     |
| NOT IN     | Non-membership test                     | FROM customers AS cWHERE c.address.zipcode NOT IN \["02340", "02115"\]SELECT \*; |
| EXISTS     | Check whether a collection is not empty | FROM orders AS oWHERE EXISTS o.itemsSELECT \*;                                   |
| NOT EXISTS | Check whether a collection is empty     | FROM orders AS oWHERE NOT EXISTS o.itemsSELECT \*;                               |

### [](#Comparison%5Foperators)Comparison Operators

You use comparison operators to compare values. The comparison operators fall into one of two sub-categories: missing value comparisons and regular value comparisons.

In an object, SQL++ for Enterprise Analytics can represent missing information in two different ways:

* The presence of the field with a NULL for its value, as in SQL.
* The absence of the field, as permitted by JSON.

For example, the first of the following objects represents Jack, who has a friend, Jill. In the other objects, Jake is friendless in SQL fashion, with a `friend` field with a value of NULL, while Joe is friendless in JSON fashion: by not having a `friend` field at all.

Examples

{"name": "Jack", "friend": "Jill"}
{"name": "Jake", "friend": NULL}
{"name": "Joe"}

The following table lists all of the comparison operators available in SQL++ for Enterprise Analytics.

| Operator                     | Purpose                                                                                                                                        | Example                                                                         |  |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |  |
| IS NULL                      | Test if a value is NULL                                                                                                                        | FROM customers AS cWHERE c.name IS NULLSELECT \*;                               |  |
| IS NOT NULL                  | Test if a value is not NULL                                                                                                                    | FROM customers AS cWHERE c.name IS NOT NULLSELECT \*;                           |  |
| IS MISSING                   | Test if a value is MISSING                                                                                                                     | FROM customers AS cWHERE c.name IS MISSINGSELECT \*;                            |  |
| IS NOT MISSING               | Test if a value is not MISSING                                                                                                                 | FROM customers AS cWHERE c.name IS NOT MISSINGSELECT \*;                        |  |
| IS UNKNOWN                   | Test if a value is NULL or MISSING                                                                                                             | FROM customers AS cWHERE c.name IS UNKNOWNSELECT \*;                            |  |
| IS NOT UNKNOWN               | Test if a value is neither NULL nor MISSING                                                                                                    | FROM customers AS cWHERE c.name IS NOT UNKNOWNSELECT \*;                        |  |
| IS KNOWN (IS VALUED)         | Test if a value is neither NULL nor MISSING                                                                                                    | FROM customers AS cWHERE c.name IS KNOWNSELECT \*;                              |  |
| IS NOT KNOWN (IS NOT VALUED) | Test if a value is NULL or MISSING                                                                                                             | FROM customers AS cWHERE c.name IS NOT KNOWNSELECT \*;                          |  |
| BETWEEN                      | Test if a value is between a start value and an end value, inclusive of both the start and end values.                                         | FROM customers AS c WHERE c.rating BETWEEN 600 AND 700 SELECT \*;               |  |
| \=                           | Equality test                                                                                                                                  | FROM customers AS cWHERE c.rating = 640SELECT \*;                               |  |
| !=                           | Inequality test                                                                                                                                | FROM customers AS cWHERE c.rating != 640SELECT \*;                              |  |
| <>                           | Inequality test                                                                                                                                | FROM customers AS cWHERE c.rating <> 640SELECT \*;                              |  |
| <                            | Less than                                                                                                                                      | FROM customers AS cWHERE c.rating < 640SELECT \*;                               |  |
| \>                           | Greater than                                                                                                                                   | FROM customers AS cWHERE c.rating > 640SELECT \*;                               |  |
| <=                           | Less than or equal to                                                                                                                          | FROM customers AS cWHERE c.rating <= 640SELECT \*;                              |  |
| \>=                          | Greater than or equal to                                                                                                                       | FROM customers AS cWHERE c.rating >= 640SELECT \*;                              |  |
| LIKE                         | Test if the left side matches a pattern defined on the right side; in the pattern, % matches any string while \_ matches any character.        | FROM customers AS c WHERE c.name LIKE "%Dodge%" SELECT \*;                      |  |
| NOT LIKE                     | Test if the left side does not match a pattern defined on the right side; in the pattern, % matches any string while \_ matches any character. | FROM customers AS c WHERE c.name NOT LIKE "%Dodge%" SELECT \*;                  |  |
| IS DISTINCT FROM             | Inequality test that treats NULL values as equal to each other and MISSING values as equal to each other                                       | FROM orders AS oWHERE o.order\_date IS DISTINCT FROM o.ship\_dateSELECT \*;     |  |
| IS NOT DISTINCT FROM         | Equality test that treats NULL values as equal to each other and MISSING values as equal to each other                                         | FROM orders AS oWHERE o.order\_date IS NOT DISTINCT FROM o.ship\_dateSELECT \*; |  |

The following table summarizes how the missing value comparison operators work.

| Operator                     | Non-NULL/Non-MISSING value | NULL value | MISSING value |
| ---------------------------- | -------------------------- | ---------- | ------------- |
| IS NULL                      | FALSE                      | TRUE       | MISSING       |
| IS NOT NULL                  | TRUE                       | FALSE      | MISSING       |
| IS MISSING                   | FALSE                      | FALSE      | TRUE          |
| IS NOT MISSING               | TRUE                       | TRUE       | FALSE         |
| IS UNKNOWN                   | FALSE                      | TRUE       | TRUE          |
| IS NOT UNKNOWN               | TRUE                       | FALSE      | FALSE         |
| IS KNOWN (IS VALUED)         | TRUE                       | FALSE      | FALSE         |
| IS NOT KNOWN (IS NOT VALUED) | FALSE                      | TRUE       | TRUE          |

### [](#Logical%5Foperators)Logical Operators

Logical operators perform logical `NOT`, `AND`, and `OR` operations over Boolean values (`TRUE` and `FALSE`) plus `NULL` and `MISSING`.

| Operator | Purpose                                                                   | Example                                    |
| -------- | ------------------------------------------------------------------------- | ------------------------------------------ |
| NOT      | Returns true if the following condition is false, otherwise returns false | SELECT VALUE NOT 1 = 1;Returns FALSE       |
| AND      | Returns true if both branches are true, otherwise returns false           | SELECT VALUE 1 = 2 AND 1 = 1;Returns FALSE |
| OR       | Returns true if one branch is true, otherwise returns false               | SELECT VALUE 1 = 2 OR 1 = 1;Returns TRUE   |

The truth table for `AND` and `OR` follows.

| A       | B       | A AND B | A OR B  |
| ------- | ------- | ------- | ------- |
| TRUE    | TRUE    | TRUE    | TRUE    |
| TRUE    | FALSE   | FALSE   | TRUE    |
| TRUE    | NULL    | NULL    | TRUE    |
| TRUE    | MISSING | MISSING | TRUE    |
| FALSE   | FALSE   | FALSE   | FALSE   |
| FALSE   | NULL    | FALSE   | NULL    |
| FALSE   | MISSING | FALSE   | MISSING |
| NULL    | NULL    | NULL    | NULL    |
| NULL    | MISSING | MISSING | NULL    |
| MISSING | MISSING | MISSING | MISSING |

The following table demonstrates the results of `NOT` on all possible inputs.

| A       | NOT A   |
| ------- | ------- |
| TRUE    | FALSE   |
| FALSE   | TRUE    |
| NULL    | NULL    |
| MISSING | MISSING |

## [](#Quantified%5Fexpressions)Quantified Expressions

##### QuantifiedExpr

![QuantifiedExpr](_images/QuantifiedExpr.png) 

Synonym for `SOME`: `ANY`

You use quantified expressions to express existential or universal predicates involving the elements of a collection.

In the following examples, quantified expressions test whether every element in a set of integers is less than 3, and then whether some of the elements are less than 3.

Examples

EVERY x IN [ 1, 2, 3 ] SATISFIES x < 3 -- ➊
SOME x IN [ 1, 2, 3 ] SATISFIES x < 3  -- ➋

➀ Returns `FALSE`  
➁ Returns `TRUE`

If the set in these examples is empty `[ ]`, the first expression yields `TRUE` because every value in an empty set satisfies the condition of less than 3\. The second expression yields `FALSE` because there are no values in the set, there aren't some, or any, values that are less than 3\. To express a universal predicate that yields `FALSE` with the empty set, you use the quantifier `SOME AND EVERY` in place of `EVERY`.

A quantified expression returns `NULL` or `MISSING` if the first expression in it evaluates to `NULL` or `MISSING`. Otherwise, a type error results if the first expression in a quantified expression does not return a collection.

## [](#Path%5Fexpressions)Path Expressions

##### PathExpr

![PathExpr](_images/PathExpr.png) 

You use path expressions to access the components of complex types in the data model. You can apply path access to the result of a query expression that yields an instance of a complex type, for example, an object or an array instance.

For objects, path access is based on field names, and it accesses the field with the specified name.

For arrays, path access is based on zero-based array-style indexing. You can use array indexes to retrieve either a single element from an array or a whole subset of an array.

* To access a single element you provide a single index argument (zero-based element position).
* To obtain a subset of an array, you provide the `start` and `end` (zero-based) index positions. The returned subset is from position `start` to position `end - 1`. The `end` position argument is optional. If you supply a negative position argument, SQL++ for Enterprise Analytics counts the element position from the end of the array: `-1` addresses the last element, `-2` next to last, and so on.

Multisets have similar behavior to arrays, except for retrieving arbitrary items as the order of items is not fixed in multisets.

Attempts to access non-existent fields or out-of-bound array elements produce the special value `MISSING`. Inappropriate use of a path expression, such as applying a field accessor to a numeric value, results in a type error.

The following examples show field access for an object, index-based element access or subset retrieval of an array, and also a composition thereof.

Examples

({"name": "MyABCs", "array": [ "a", "b", "c"]}).array    -- ➊
(["a", "b", "c"])[2]                                     -- ➋
(["a", "b", "c"])[-1]                                    -- ➌
({"name": "MyABCs", "array": [ "a", "b", "c"]}).array[2] -- ➍
(["a", "b", "c"])[0:2]                                   -- ➎
(["a", "b", "c"])[0:]                                    -- ➏
(["a", "b", "c"])[-2:-1]                                 -- ➐

➀ Returns `[["a", "b", "c"]]`  
➁ Returns `["c"]`  
➂ Returns `["c"]`  
➃ Returns `["c"]`  
➄ Returns `[["a", "b"]]`  
➅ Returns `[["a", "b", "c"]]`  
➆ Returns `[["b"]]`

## [](#Primary%5Fexpressions)Primary Expressions

##### PrimaryExpr

![PrimaryExpr](_images/PrimaryExpr.png) 

The most basic building block for any expression in SQL++ for Enterprise Analytics is Primary Expression. This can be a simple literal (constant) value, a reference to a query variable that is in scope, a parenthesized expression, a function call, or a newly constructed instance of the data model (such as a newly constructed object, array, or multiset of data model instances).

### [](#Literals)Literals

##### Literal

![Literal](_images/Literal.png) 

The simplest kind of expression is a literal that directly represents a value in JSON format. Examples follow.

-42
"Hello"
true
false
null

Numeric literals can include a sign and an optional decimal point. You can also write them in exponential notation, like this:

5e2
-4.73E-2

You enclose string literals in either single `' '` or double `" "` quotes. For a string literal that includes single or double quote characters, you must escape the character with a backward slash `\`, as in these examples:

"I read \"War and Peace\" today."
'I don\'t believe everything I read.'

The table that follows shows how to escape characters in SQL++ for Enterprise Analytics.

| Character Name | Escape Method |
| -------------- | ------------- |
| Single Quote   | \\'           |
| Double Quote   | \\"           |
| Backslash      | \\\\          |
| Slash          | \\/           |
| Backspace      | \\b           |
| Formfeed       | \\f           |
| Newline        | \\n           |
| CarriageReturn | \\r           |
| EscapeTab      | \\t           |

### [](#Variable%5Freferences)Identifiers and Variable References

Like SQL, SQL++ makes use of a language construct called an identifier. See the [Requirements for Identifiers](1a%5Fentities.md#names). To use an identifier that is the same as a [reserved keyword](reserved%5Fkeywords.md) in a query, you must escape that identifier with backtick (``` `` ```) characters. Identifiers enclosed by backticks are known as delimited identifiers.

You use identifiers in variable names, path expressions, and in other places in SQL++ for Enterprise Analytics syntax. Examples of identifiers follow.

X
customer_name
`SELECT`
`spaces in here`
`@&#`

A very simple kind of SQL++ for Enterprise Analytics expression is a variable, which is simply an identifier. As in SQL, a variable can be bound to a value, which can be an input dataset, some intermediate result during processing of a query, or the final result of a query. For more information about variables, see [SELECT Statements](3%5Fquery.md).

> [!NOTE]
> SQL++ for Enterprise Analytics has different rules for delimiting strings and identifiers than the SQL rules. In SQL, you use single quotes to enclose strings, and double quotes to enclose delimited identifiers.

### [](#Parameter%5Freferences)Parameter References

A parameter reference is an external variable. You provide its value using the query options feature in the UI. See [Set Query Options](../query/options.md).

Parameter references come in two forms, named parameter references and positional parameter references.

* Named parameter references consist of the `$` symbol followed by an identifier or delimited identifier.
* Positional parameter references can be either a `$` symbol followed by one or more digits or a `?` symbol. If numbered, positional parameters start at 1\. SQL++ for Enterprise Analytics interprets `?` parameters as $1 to $N based on the order in which they appear in the statement.

Parameter references can appear as shown in the following examples:

Examples

$id
$1
?

An error results if the parameter is not bound at query execution time.

### [](#Parenthesized%5Fexpressions)Parenthesized Expressions

##### ParenthesizedExpr

![ParenthesizedExpr](_images/ParenthesizedExpr.png) 

##### Subquery

![Subquery](_images/Subquery.png) 

You can parenthesize an expression to control the precedence order or otherwise clarify a query. You can also enclose a [subquery](3%5Fquery.html#Subqueries) (nested [selection](3%5Fquery.html#Union%5Fall)) in parentheses.

The following expression evaluates to the value 2.

Example

( 1 + 1 )

### [](#Function%5Fcall%5Fexpressions)Function Calls

##### FunctionCall

![FunctionCall](_images/FunctionCall.png) 

##### OrdinaryFunctionCall

![OrdinaryFunctionCall](_images/OrdinaryFunctionCall.png) 

##### AggregateFunctionCall

![Identifier "(" ("DISTINCT")? Expr ")" ("FILTER" "(" "WHERE" Expr ")")?](_images/AggregateFunctionCall.png) 

##### DatabaseAndScopeName

![(Identifier ".")? Identifier](_images/DatabaseAndScopeName.png) 

SQL++ for Enterprise Analytics, like most languages, provides functions to package or componentize complicated or reusable computations. A function call is a legal query expression that represents the value resulting from the evaluation of its body expression with the given parameter bindings. The parameter value bindings can themselves be any expressions in SQL++ for Enterprise Analytics.

* Window functions, and aggregate functions used as window functions, have a more complex syntax. See [Window Queries](3%5Fquery.html#Over%5Fclauses).
* You can only specify FILTER expressions when calling [Aggregation Pseudo-Functions](3%5Fquery.html#Aggregation%5FPseudoFunctions).

In the following example, the value of the function call expression is 8.

Example

length('a string')

### [](#Case%5Fexpressions)Case Expressions

##### CaseExpr

![CaseExpr](_images/CaseExpr.png) 

##### SimpleCaseExpr

![SimpleCaseExpr](_images/SimpleCaseExpr.png) 

##### SearchedCaseExpr

![SearchedCaseExpr](_images/SearchedCaseExpr.png) 

In an uncomplicated `CASE` expression, the query evaluator searches for the first `WHEN` …​ `THEN` pair in which the `WHEN` expression is equal to the expression following `CASE` and returns the expression following `THEN`. If none of the `WHEN` …​ `THEN` pairs meet this condition, and an `ELSE` branch exists, it returns the `ELSE` expression. Otherwise, it returns `NULL`.

In a searched CASE expression, the query evaluator searches from left to right until it finds a `WHEN` expression that evaluates to `TRUE`, and then returns its corresponding `THEN` expression. If no condition evaluates to `TRUE`, and an `ELSE` branch exists, it returns the `ELSE` expression. Otherwise, it returns `NULL`.

The following example illustrates the form of a case expression.

Example

CASE (2 < 3) WHEN true THEN "yes" ELSE "no" END

### [](#Constructors)Constructors

##### Constructor

![Constructor](_images/Constructor.png) 

##### ObjectConstructor

![ObjectConstructor](_images/ObjectConstructor.png) 

##### ArrayConstructor

![ArrayConstructor](_images/ArrayConstructor.png) 

##### MultisetConstructor

![MultisetConstructor](_images/MultisetConstructor.png) 

You can use constructors to represent structured JSON values, as in these examples:

{ "name": "Bill", "age": 42 } -- ➊
[ 1, 2, "Hello", null ]       -- ➋

➀ An object  
➁ An array

In a constructed object:

* The names of the fields must be either literal strings or computed strings
* An object cannot contain any duplicate names

Structured literals can be nested, as in this example:

[ {"name": "Bill",
   "address":
      {"street": "25 Main St.",
       "city": "Cincinnati, OH"
      }
  },
  {"name": "Mary",
   "address":
      {"street": "107 Market St.",
       "city": "St. Louis, MO"
      }
   }
]

You can use expressions to represent the array items in an array constructor and the field-names and field-values in an object constructor.

For example, suppose that the variables firstname, lastname, salary, and bonus are bound to appropriate values. You might construct structured values by the following expressions:

An object:

{
  "name": firstname || " " || lastname,
  "income": salary + bonus
}

An array:

["1984", lastname, salary + bonus, null]

If only one expression is specified instead of the field-name/field-value pair in an object constructor then this expression is supposed to provide the field value. The field name is then automatically generated based on the kind of the value expression as in the example that follows:

* If it is a variable reference expression then the generated field name is the name of that variable.
* If it is a field access expression then the generated field name is the last identifier in that expression.
* For all other cases, a compilation error results.

##### Example

FROM customers AS c
WHERE c.custid = "C47"
SELECT VALUE {c.name, c.rating};

This query returns:

[
    {
        "name": "S. Logan",
        "rating": 625
    }
]

## [](#see-also)See Also

* [Requirements for Identifiers](1a%5Fentities.md#names)
* [Reserved Keywords](reserved%5Fkeywords.md)
* [Set Query Options](../query/options.md)