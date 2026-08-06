---
title: USE Statements
description: This topic describes how a <code>USE</code> statement sets the
  database name, scope name, or both for the statement that follows.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/sqlpp/pages/5_ddl_use.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:2.1@enterprise-analytics:sqlpp:5_ddl_use.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.1/sqlpp/5_ddl_use.html)

# USE Statements

> This topic describes how a `USE` statement sets the database name, scope name, or both for the statement that follows. 

When you provide a `USE` statement, you do not need to explicitly specify a database and a scope in the statement that follows it.

For information about how Enterprise Analytics organizes entities into a `database.scope.database_object` hierarchy and resolves names, see [Entities in Enterprise Analytics](1a%5Fentities.md).

## [](#syntax)Syntax

**UseStmnt EBNF** 

```EBNF
UseStmnt ::= "USE" DatabaseAndScopeName
```

**UseStmnt Diagram** 

!["USE" DatabaseAndScopeName](_images/UseStmnt.png) 

The `USE` statement only works in a conjunction with another statement in a single request.

## [](#example)Example

This example sets `travel-sample` to be the database and `inventory` to be the scope for whatever statement follows if it omits that information.

```SQL++
 USE `travel-sample`.inventory;
```