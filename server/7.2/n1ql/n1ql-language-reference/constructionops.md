---
title: Construction Operators
description: SQL++ supports array and object construction operators.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/n1ql/pages/n1ql-language-reference/constructionops.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:n1ql:n1ql-language-reference/constructionops.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/n1ql/n1ql-language-reference/constructionops.html)

# Construction Operators

SQL++ supports array and object construction operators.

## [](#array-construction)Array Constructors

Arrays are ordered lists with 0 or more values. Arrays are enclosed in square brackets `[ ]`. Commas separate each value.

### [](#syntax)Syntax

```ebnf
array ::= '[' ( expr ( ',' expr )* )? ']'
```

![Syntax diagram](../_images/n1ql-language-reference/array.png) 

### [](#arguments)Arguments

expr

An expression resolving to any supported JSON data type.

### [](#example)Example

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Example 1\. Simple array construction

Query

```sqlpp
SELECT ["one", "two", "three"], [1, 2, 3];
```

Results

```json
[
  {
    "$1": [
      "one",
      "two",
      "three"
    ],
    "$2": [
      1,
      2,
      3
    ]
  }
]
```

Example 2\. Dynamic array construction

This example constructs a new array using the `address`, `city`, and `country` fields in the data source.

Query

```sqlpp
SELECT [ address, city, country ] AS location
FROM hotel LIMIT 3;
```

Results

```json
[
  {
    "location": [
      "Capstone Road, ME7 3JE",
      "Medway",
      "United Kingdom"
    ]
  },
  {
    "location": [
      "57-59 Balmoral Road, ME7 4NT",
      "Gillingham",
      "United Kingdom"
    ]
  },
  {
    "location": [
      "6 rue aux Juifs",
      "Giverny",
      "France"
    ]
  }
]
```

## [](#object-construction)Object Constructors

Objects contain name-value pairs or attributes. Objects are enclosed in curly braces `{` `}`. Commas separate each attribute. The colon (`:`) character separates the key or name from its value within each attribute.

### [](#syntax-2)Syntax

```ebnf
object ::= '{' ( ( name-expr ':' )? expr (',' ( name-expr ':' )? expr)* )? '}'
```

![Syntax diagram](../_images/n1ql-language-reference/object.png) 

### [](#arguments-2)Arguments

name-expr

\[Optional\] An expression resolving to a string, which specifies the name of the attribute. All names must be distinct from each other within the object.

If a name does not evaluate to a string, the result of the object construction is NULL.

expr

An expression resolving to any supported JSON data type, which specifies the value of the attribute.

> [!NOTE]
> Dynamic names
> 
> If the `expr` argument is an identifier referring to a named field in the data source, then you can omit the `name-expr` argument. In this case, the name of the field in the data source will be used as the name of the attribute in the output object.

### [](#examples)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Example 3\. Simple object construction

Query

```sqlpp
SELECT { UPPER("foo") : 1, "foo" || "bar" : 2 };
```

Results

```json
[
  {
    "$1": {
      "FOO": 1,
      "foobar": 2
    }
  }
]
```

Example 4\. Dynamic object construction

This example constructs a new object using the `address`, `city`, and `country` fields in the data source.

Query

```sqlpp
SELECT { "street": address, city, country } AS location
FROM hotel LIMIT 3;
```

Notice we have provided a new name for the `street` attribute, but the `city` and `country` attributes are named dynamically.

Results

```json
[
  {
    "location": {
      "city": "Medway",
      "country": "United Kingdom",
      "street": "Capstone Road, ME7 3JE"
    }
  },
  {
    "location": {
      "city": "Gillingham",
      "country": "United Kingdom",
      "street": "57-59 Balmoral Road, ME7 4NT"
    }
  },
  {
    "location": {
      "city": "Giverny",
      "country": "France",
      "street": "6 rue aux Juifs"
    }
  }
]
```

## [](#related-links)Related Links

Refer to [Range Transformations](collectionops.md#range-xform) for a more sophisticated way to generate arrays and objects from a data source.