---
title: Comparison Operators
description: Comparison operators enable you to compare expressions.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/n1ql/pages/n1ql-language-reference/comparisonops.adoc
  xref: xref:server:n1ql:n1ql-language-reference/comparisonops.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/n1ql/n1ql-language-reference/comparisonops.html)

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

| Operator | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Returns       |
| -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| LIKE     | Matches a string against a pattern. Returns TRUE if they match. The pattern can include regular characters and the following wildcards: Percent sign (%): Matches zero or more characters. Underscore (\_): Matches a single character at that specific position in the string. To match a literal wildcard character, use an escape character. The default escape character is the backslash (\\). To define a custom escape character, use the ESCAPE clause. For example, to use hash (#) as an escape character to match the string "abc%def", use the following: LIKE "abc#%def" ESCAPE "#". To match the escape character itself, escape it with another escape character (for example, \\\\). An empty pattern matches only an empty string. To match any string, including an empty string, use %. | TRUE or FALSE |
| NOT LIKE | Inverse of LIKE. Returns TRUE if the string does not match the given pattern.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | TRUE or FALSE |

### [](#examples)Examples

Example 1\. Match strings using LIKE

Query

```sqlpp
SELECT "hello world" LIKE "h_llo%" AS match_1,
       "hello world" NOT LIKE "h_llo%" AS match_2,
       "hello world" LIKE "h%world" AS match_3,
       "hello world" LIKE "h%z%" AS match_4,
       "hello% world" LIKE "hello#% world" ESCAPE "#" AS match_5;
```

Returns

```json
[
  {
    "match_1": true,
    "match_2": false,
    "match_3": true,
    "match_4": false,
    "match_5": true
  }
]
```

## [](#is)IS

The IS family of operators lets you specify conditions based on the existence (or absence) of attributes in a data set.

```ebnf
is-expr ::= expr 'IS' 'NOT'? 'NULL' |
            expr 'IS' 'NOT'? 'MISSING' |
            expr 'IS' 'NOT'? 'VALUED' |
            expr 'IS' 'NOT'? 'UNKNOWN' |
            expr 'IS' 'NOT'? 'DISTINCT' 'FROM' expr
```

![Syntax diagram](../_images/n1ql-language-reference/is-expr.png) 

| Operator             | Description                                                                                   | Returns                                                                                                                                                                                                                      |
| -------------------- | --------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| IS NULL              | Field has value of NULL.                                                                      | TRUE or FALSE                                                                                                                                                                                                                |
| IS NOT NULL          | Field has value or is missing.                                                                | TRUE or FALSE                                                                                                                                                                                                                |
| IS MISSING           | No value for field found.                                                                     | TRUE or FALSE                                                                                                                                                                                                                |
| IS NOT MISSING       | Value for field found or value is NULL.                                                       | TRUE or FALSE                                                                                                                                                                                                                |
| IS VALUED            | Value for field found. Value is neither missing nor NULL.                                     | TRUE or FALSE                                                                                                                                                                                                                |
| IS NOT VALUED        | Value for field not found. Value is NULL.                                                     | TRUE or FALSE                                                                                                                                                                                                                |
| IS UNKNOWN           | Value for field is unknown, NULL, or missing.Equivalent to IS NOT VALUED/IS NOT KNOWN.        | TRUE OR FALSE                                                                                                                                                                                                                |
| IS NOT UNKNOWN       | Value for field is known. Value is neither NULL nor missing.Equivalent to IS VALUED/IS KNOWN. | TRUE OR FALSE                                                                                                                                                                                                                |
| IS DISTINCT FROM     | Compares two values to determine if they're distinct.                                         | TRUE or FALSE TRUE if one value is NULL and the other is non-NULL. FALSE if both values are NULL. MISSING if either value is MISSING. The result of the comparison expr != expr if both values are non-NULL and non-MISSING. |
| IS NOT DISTINCT FROM | Compares two values to determine if they're not distinct.                                     | TRUE or FALSE FALSE if one value is NULL and the other is non-NULL. TRUE if both values are NULL. MISSING if either value is MISSING. The result of the comparison expr == expr if both values are non-NULL and non-MISSING. |

### [](#examples-2)Examples

Example 2\. IS NULL

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

Example 3\. IS MISSING

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

Example 4\. IS UNKNOWN

Query

```sqlpp
SELECT NULL IS UNKNOWN,
       NULL IS NOT UNKNOWN,
       missing IS UNKNOWN,
       missing IS NOT UNKNOWN,
       "Harry" IS UNKNOWN,
       "Harry" IS NOT UNKNOWN
```

Returns

```json
{
  "results": [
    {
    "$1": true,
    "$2": false,
    "$3": true,
    "$4": false,
    "$5": false,
    "$6": true
  }
 ]
}
```

Example 5\. IS DISTINCT FROM

Query

```sqlpp
SELECT 1 IS DISTINCT FROM 1,
       1 IS DISTINCT FROM 2,
       NULL IS DISTINCT FROM NULL,
       NULL IS DISTINCT FROM 1,
       1 IS DISTINCT FROM MISSING,
       1 IS NOT DISTINCT FROM 1,
       1 IS NOT DISTINCT FROM 2,
       NULL IS NOT DISTINCT FROM NULL,
       NULL IS NOT DISTINCT FROM 1,
       1 IS NOT DISTINCT FROM MISSING;
```

Returns

```json
[
  {
    "$1": false,
    "$2": true,
    "$3": false,
    "$4": true,
    "$5": true,
    "$6": true,
    "$7": false,
    "$8": true,
    "$9": false,
    "$10": false
  }
]
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