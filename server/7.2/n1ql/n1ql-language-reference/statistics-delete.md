---
title: Delete Statistics
description: You can use the UPDATE STATISTICS statement to delete statistics.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/n1ql/pages/n1ql-language-reference/statistics-delete.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:n1ql:n1ql-language-reference/statistics-delete.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/n1ql/n1ql-language-reference/statistics-delete.html)

# Delete Statistics

> You can use the UPDATE STATISTICS statement to delete statistics. 

## [](#purpose)Purpose

The `UPDATE STATISTICS` statement provides a syntax which enables you to delete statistics for a set of index expressions, or for an entire keyspace.

Since the [cost-based optimizer](cost-based-optimizer.md) uses statistics for cost calculations, deleting statistics for a set of index expressions effectively turns off the cost-based optimizer for queries which utilize predicates on those expressions. Deleting all statistics for a keyspace turns off the cost-based optimizer for all queries referencing that keyspace.

## [](#syntax)Syntax

```ebnf
update-statistics-delete ::= ( 'UPDATE' 'STATISTICS' 'FOR'? |
                               'ANALYZE' ( 'KEYSPACE' | 'COLLECTION')? )
                               keyspace-ref delete-clause
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/update-statistics-delete.png) 

For this syntax, `UPDATE STATISTICS` and `ANALYZE` are synonyms. The statement must begin with one of these alternatives.

When using the `UPDATE STATISTICS` keywords, the `FOR` keyword is optional. Including this keyword makes no difference to the operation of the statement.

When using the `ANALYZE` keyword, the `COLLECTION` or `KEYSPACE` keywords are optional. Including either of these keywords makes no difference to the operation of the statement.

| keyspace-ref  | [Keyspace Reference](#keyspace-ref) |
| ------------- | ----------------------------------- |
| delete-clause | [DELETE Clause](#delete-clause)     |

### [](#keyspace-ref)Keyspace Reference

```ebnf
keyspace-ref ::= keyspace-path | keyspace-partial
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/keyspace-ref.png) 

```ebnf
keyspace-path ::= ( namespace ':' )? bucket ( '.' scope '.' collection )?
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/keyspace-path.png) 

```ebnf
keyspace-partial ::= collection
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/keyspace-partial.png) 

The simple name or fully-qualified name of the keyspace for which you want to delete statistics. Refer to the [CREATE INDEX](createindex.md#keyspace-ref) statement for details of the syntax.

### [](#delete-clause)DELETE Clause

```ebnf
delete-clause ::= 'DELETE' ( delete-expr | delete-all )
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/delete-clause.png) 

The `DELETE` clause enables you to provide a comma-separated list of index expressions for which you want to delete statistics, or to specify that you want to delete all statistics for the keyspace.

| delete-expr | [Delete Expressions](#delete-expressions) |
| ----------- | ----------------------------------------- |
| delete-all  | [Delete All Statistics](#delete-all)      |

#### [](#delete-expressions)Delete Expressions

```ebnf
delete-expr ::= 'STATISTICS'? '(' index-key ( ',' index-key )* ')'
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/delete-expr.png) 

Constraint: if you used the `UPDATE STATISTICS` keywords at the beginning of the statement, you may not use the `STATISTICS` keyword in this clause.

Conversely, if you used the `ANALYZE` keyword at the beginning of the statement, you must include the `STATISTICS` keyword in this clause.

| index-key | \[Required\] The expression for which you want to delete statistics. This may be any expression that is supported as an index key, including, but not limited to: A SQL++ [expression](index.md) over any fields in the document, as used in a secondary index. An [array expression](indexing-arrays.md#array-expr), as used when creating an array index. An [expression with the META() function](indexing-meta-info.md#metakeyspace%5Fexpr-property), as used in a metadata index. |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

#### [](#delete-all)Delete All Statistics

```ebnf
delete-all ::= 'ALL' | 'STATISTICS'
```

![Syntax diagram: refer to source code listing](../_images/n1ql-language-reference/delete-all.png) 

Constraint: If you used the `UPDATE STATISTICS` keywords at the beginning of the statement, you must use the `ALL` keyword in this clause.

Conversely, if you used the `ANALYZE` keyword at the beginning of the statement, you must use the `STATISTICS` keyword in this clause.

## [](#result)Result

The statement returns an empty array.

## [](#examples)Examples

To try the examples in this section, set the query context to the `inventory` scope in the travel sample dataset. For more information, see [Query Context](../n1ql-intro/queriesandresults.md#query-context).

Example 1\. Delete statistics with UPDATE STATISTICS

```sqlpp
UPDATE STATISTICS FOR hotel
DELETE (city, country, free_breakfast);
```

Example 2\. Delete statistics with ANALYZE

```sqlpp
ANALYZE KEYSPACE hotel
DELETE STATISTICS (city, country, free_breakfast);
```

This query is equivalent to the query in [Example 1](#ex-1).

Example 3\. Delete all statistics with UPDATE STATISTICS

```sqlpp
UPDATE STATISTICS FOR airport DELETE ALL;
```

Example 4\. Delete all statistics with ANALYZE

```sqlpp
ANALYZE KEYSPACE airport DELETE STATISTICS;
```

This query is equivalent to the query in [Example 3](#ex-3).

## [](#related-links)Related Links

* [UPDATE STATISTICS](updatestatistics.md) overview
* [Updating Statistics for Index Expressions](statistics-expressions.md)
* [Updating Statistics for a Single Index](statistics-index.md)
* [Updating Statistics for Multiple Indexes](statistics-indexes.md)
* [Cost-Based Optimizer](cost-based-optimizer.md)