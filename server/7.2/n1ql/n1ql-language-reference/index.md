---
title: SQL++ Language Reference
description: This reference guide describes the syntax and structure of the SQL++ language.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/n1ql/pages/n1ql-language-reference/index.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/n1ql/n1ql-language-reference/index.html)

# SQL++ Language Reference

> This reference guide describes the syntax and structure of the SQL++ language. It provides information about the basic elements which can be combined to build SQL++ statements. The Couchbase implementation of SQL++ was formerly known as [N1QL](https://www.couchbase.com/products/n1ql). 

The SQL++ language is composed of [statements](#statements), [expressions](#N1QL%5FExpressions), and [comments](#comments).

## [](#statements)Statements

SQL++ statements are categorized into the following groups:

* **Data Definition Language** (DDL) statements to [create indexes](createindex.md), [modify indexes](alterindex.md), and [drop indexes](dropindex.md).
* **Data Manipulation Language** (DML) statements to [select](selectintro.md), [insert](insert.md), [update](update.md), [delete](delete.md), and [upsert](upsert.md) data into JSON documents.

## [](#N1QL%5FExpressions)Expressions

The following are the different types of SQL++ expressions:

* [Literal values](literals.md)
* [Identifiers](identifiers.md)
* [Arithmetic terms](arithmetic.md)
* [Comparison terms](comparisonops.md)
* [Concatenation terms](stringops.md)
* [Logical terms](logicalops.md)
* [Conditional expressions](conditionalops.md)
* [Collection expressions](collectionops.md)
* [Construction expressions](constructionops.md)
* [Nested expressions](#nested-path-exp)
* [Function calls](functions.md)
* [Subqueries](subqueries.md)

### [](#nested-path-exp)Nested Path Expressions

In SQL++, _nested paths_ indicate an expression to access nested sub-documents within a JSON document or expression.

For example, in the document below, the latitude of an airport is stored within the `geo` sub-document, and can be addressed using the nested path `geo.lat`:

```json
[
  {
    "airportname": "Calais Dunkerque",
    "city": "Calais",
    "geo": {
      "alt": 12,
      "lat": 50.962097,
      "lon": 1.954764
    },
    "latitude": 51,
    // ...
  }
]
```

You can use [nested operators](nestedops.md) to access sub-document fields within a document.

## [](#comments)Comments

SQL++ supports _block comments_ and _line comments_.

### [](#block-comments)Block Comments

```ebnf
block-comment ::= '/*' ( text | newline )* '*/'
```

![Syntax diagram](../_images/n1ql-language-reference/block-comment.png) 

A block comment starts with `/*` and ends with `*/`. The query engine ignores the start and end markers `/* */`, and any text between them.

A block comment may start on a new line, or in the middle of a line after other SQL++ statements. A block comment may contain line breaks.

There may also be further SQL++ statements on the same line after the end of a block comment — the query engine does _not_ ignore these.

### [](#line-comments)Line Comments

```ebnf
line-comment ::=  '--' text?
```

![Syntax diagram](../_images/n1ql-language-reference/line-comment.png) 

You can use line comments in Couchbase Server 6.5 and later. A line comment starts with two hyphens `--`. The query engine ignores the two hyphens, and any text following them up to the end of the line.

A line comment may start on a new line, or in the middle of a line after other SQL++ statements. A line comment may not contain line breaks.

### [](#optimizer-hints)Optimizer Hints

You can supply hints to the optimizer within a specially-formatted _hint comment_. For further details, refer to [Optimizer Hints](optimizer-hints.md).