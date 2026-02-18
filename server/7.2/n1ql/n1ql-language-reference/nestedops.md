---
title: Nested Operators and Expressions
description: In SQL++, nested operators and paths indicate expressions to access
  nested sub-documents within a JSON document or expression.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/n1ql/pages/n1ql-language-reference/nestedops.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/n1ql/n1ql-language-reference/nestedops.html)

# Nested Operators and Expressions

In SQL++, nested operators and paths indicate expressions to access nested sub-documents within a JSON document or expression.

A nested expression may contain field selection operators, element selection operators, and array slicing operators.

```ebnf
nested-expr ::= field-expr | element-expr | slice-expr
```

![Syntax diagram](../_images/n1ql-language-reference/nested-expr.png) 

These special operators are needed to access the data because Couchbase documents can have nested objects and embedded arrays. A field selection operator is used to refer to a field in an object, and an element selection operator is used to refer to an element in an array. You can use a combination of these operators to access nested data at any depth in a document.

## [](#field-selection)Field Selection

Field selection operators use the dot notation `.` to refer to a child field, that is, a field one level down in a nested object.

### [](#syntax)Syntax

```ebnf
field-expr ::= expr '.' ( identifier | ( ( escaped-identifier | '[' name-expr ']' ) 'i'? ) )
```

![Syntax diagram](../_images/n1ql-language-reference/field-expr.png) 

### [](#arguments)Arguments

expr

An expression resolving to an object.

identifier

escaped-identifier

An identifier which specifies the name of a field in the object.

name-expr

An expression resolving to a string which specifies the name of a field in the object.

By default, field names are case sensitive. To access a field case-insensitively, include the trailing `i`.

### [](#return-value)Return Value

The value of the specified field.

### [](#example)Example

Given the following data:

```json
{
  "address": {
    "city": "Mountain View"
  },
  "revisions": [2013, 2012, 2011, 2010]
}
```

The following expressions all evaluate to `"Mountain View"`.

`address.city`, `` address.`CITY`i ``, `address.["city"]`, and `address.["CITY"]i`

## [](#element-selection)Element Selection

Element selection operators use the bracket notation `[ ]` to access an element inside a nested array.

### [](#syntax-2)Syntax

```ebnf
element-expr ::= expr '[' position ']'
```

![Syntax diagram](../_images/n1ql-language-reference/element-expr.png) 

### [](#arguments-2)Arguments

expr

An expression resolving to an array.

position

A numeric expression specifying the position of an element in the array, counting from 0\. Negative positions are counted backwards from the end of the array.

### [](#return-value-2)Return Value

The value of the specified element.

### [](#example-2)Example

Given the following data:

```json
{
    "address": {
    "city": "Mountain View"
    },
    "revisions": [2013, 2012, 2011, 2010]
}
```

The expression `revisions[0]` evaluates to `2013`. The expression `revision[-1]` evaluates to `2010`.

## [](#array-slicing)Array Slicing

The array slicing operator enables you to get subsets or segments of an array.

### [](#syntax-3)Syntax

```ebnf
slice-expr ::= expr '[' start-expr ':' end-expr? ']'
```

![Syntax diagram](../_images/n1ql-language-reference/slice-expr.png) 

### [](#arguments-3)Arguments

expr

An expression resolving to an array.

start-expr

A numeric expression specifying a start position in the array, counting from 0\. Negative positions are counted backwards from the end of the array.

end-expr

\[Optional\] A numeric expression specifying an end position in the array, counting from 0\. Negative positions are counted backwards from the end of the array.

### [](#return-value-3)Return Value

A new subset of the source array, containing the elements from the start position to the end position minus 1\. The element at the start position is included, while the element at the end position is not.

If the end position is omitted, all elements from the start position to the end of the source array are included.

### [](#example-3)Example

Given the following data:

```json
{
  "address": {
       "city": "Mountain View"
  },
  "revisions": [2013, 2012, 2011, 2010]
}
```

The expression `revisions[1:3]` evaluates to the array value `[2012, 2011]`.

The expression `revisions[1:]` evaluates to the array value `[2012, 2011, 2010]`.