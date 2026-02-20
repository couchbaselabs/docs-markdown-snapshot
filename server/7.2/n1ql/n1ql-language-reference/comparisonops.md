---
title: Comparison Operators
description: Comparison operators enable you to compare expressions.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/n1ql/pages/n1ql-language-reference/comparisonops.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:n1ql:n1ql-language-reference/comparisonops.adoc[]
---

[View original HTML](/server/7.2/n1ql/n1ql-language-reference/comparisonops.html)

# Comparison Operators

Comparison operators enable you to compare expressions.

The following tables describe each comparison operator and its return values.

## [](#relational-operators)Relational Operators

```ebnf
relational-expr ::= expr '=' expr |
                    expr '==' expr |
                    expr '!=' expr |
                    expr '<>' expr |
                    expr '>' expr |
                    expr '>=' expr |
                    expr '<' expr |
                    expr '<=' expr
```

![Syntax diagram](../_images/n1ql-language-reference/relational-expr.png) 

| Operator | Description                                                                         | Returns       |
| -------- | ----------------------------------------------------------------------------------- | ------------- |
| \=       | Equal to. Functionally equivalent to == for compatibility with other languages.     | TRUE or FALSE |
| \==      | Equal to. Functionally equivalent to = for compatibility with other languages.      | TRUE or FALSE |
| !=       | Not equal to. Functionally equivalent to <> for compatibility with other languages. | TRUE or FALSE |
| <>       | Not equal to. Functionally equivalent to != for compatibility with other languages. | TRUE or FALSE |
| \>       | Greater than.                                                                       | TRUE or FALSE |
| \>=      | Greater than or equal to.                                                           | TRUE or FALSE |
| <        | Less than.                                                                          | TRUE or FALSE |
| <=       | Less than or equal to.                                                              | TRUE or FALSE |

## [](#between)BETWEEN

```ebnf
between-expr ::= expr 'NOT'? 'BETWEEN' start-expr 'AND' end-expr
```

![Syntax diagram](../_images/n1ql-language-reference/between-expr.png) 

| Operator    | Description                                                                                                                                                             | Returns       |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| BETWEEN     | Search criteria for a query where the value is between two values, including the end values specified in the range. Values can be numbers, text, or dates.              | TRUE or FALSE |
| NOT BETWEEN | Search criteria for a query where the value is outside the range of two values, including the end values specified in the range. Values can be numbers, text, or dates. | TRUE or FALSE |

## [](#like)LIKE

```ebnf
like-expr ::= expr 'NOT'? 'LIKE' expr
```

![Syntax diagram](../_images/n1ql-language-reference/like-expr.png) 

| Operator | Description                                                                                                                                                                                                                                                                                     | Returns       |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| LIKE     | Match string with a wildcard expression. Use % for zero or more wildcards and \_ to match any character at this place in a string. The wildcard characters can be escaped by preceding them with a backslash (\\). Backslash itself can also be escaped by preceding it with another backslash. | TRUE or FALSE |
| NOT LIKE | Inverse of LIKE. Return TRUE if string is not similar to given string.                                                                                                                                                                                                                          | TRUE or FALSE |

## [](#is)IS

The IS family of operators lets you specify conditions based on the existence (or absence) of attributes in a data set.

```ebnf
is-expr ::= expr 'IS' 'NOT'? 'NULL' |
            expr 'IS' 'NOT'? 'MISSING' |
            expr 'IS' 'NOT'? 'VALUED'
```

![Syntax diagram](../_images/n1ql-language-reference/is-expr.png) 

| Operator       | Description                                              | Returns       |
| -------------- | -------------------------------------------------------- | ------------- |
| IS NULL        | Field has value of NULL.                                 | TRUE or FALSE |
| IS NOT NULL    | Field has value or is missing.                           | TRUE or FALSE |
| IS MISSING     | No value for field found.                                | TRUE or FALSE |
| IS NOT MISSING | Value for field found or value is NULL.                  | TRUE or FALSE |
| IS VALUED      | Value for field found. Value is neither missing nor NULL | TRUE or FALSE |
| IS NOT VALUED  | Value for field not found. Value is NULL.                | TRUE or FALSE |

Example 1\. IS NULL

Query

```sqlpp
 SELECT fname, children
    FROM tutorial
       WHERE children IS NULL
```

Returns

```json
{
  "results": [
    {
      "children": null,
      "fname": "Fred"
    }
  ]
}
```

Example 2\. IS MISSING

Query

```sqlpp
    SELECT fname, children
       FROM tutorial
          WHERE children IS MISSING
```

Returns

```json
    {
  "results": [
    {
      "fname": "Harry"
    },
    {
      "fname": "Jane"
    }
  ]
}
```

## [](#comparison-of-data-types)Comparison of Data Types

### [](#strings)Strings

String comparison is done using a raw-byte collation of UTF-8 encoded strings — sometimes referred to as binary, C, or memcmp. This collation is case sensitive. Case-insensitive comparisons can be performed using the UPPER() or LOWER() functions. See [String Functions](stringfun.md) for more information.

### [](#arrays-and-objects)Arrays and Objects

Arrays are compared element-wise. Objects are first compared by length; objects of equal length are compared pairwise, with the pairs sorted by name.

### [](#null-and-missing)NULL and MISSING

Except when using the IS family of operators, comparison of the MISSING or NULL data types produces the following results.

* If either operand in a comparison is MISSING, the result is MISSING.
* If either operand in a comparison is NULL, the result is NULL.
* If either operand is MISSING or NULL, the result is MISSING or NULL.