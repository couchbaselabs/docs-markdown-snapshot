---
title: CREATE SCOPE Statements
description: This topic describes how you use the <code>CREATE</code> statement
  to create Enterprise Analytics scopes.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/sqlpp/pages/5_ddl_scope.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:enterprise-analytics:sqlpp:5_ddl_scope.adoc[]
---

[View original HTML](/enterprise-analytics/current/sqlpp/5_ddl_scope.html)

# CREATE SCOPE Statements

> This topic describes how you use the `CREATE` statement to create Enterprise Analytics scopes. 

For general `CREATE` statement syntax, see [CREATE Statements](5%5Fddl%5Fcreate.md).

## [](#syntax)Syntax

**CreateScope EBNF** 

```EBNF
CreateScope ::= "CREATE" "ANALYTICS"? "SCOPE" DatabaseAndScopeName ("IF" "NOT" "EXISTS")?
```

Synonym for `SCOPE`: `DATAVERSE`

**CreateScope Diagram** 

![CREATE](_images/CreateScope.png) 

**DatabaseAndScopeName Diagram** 

![(Identifier](_images/DatabaseAndScopeName.png) 

DatabaseAndScopeName

The `DatabaseAndScopeName` represents two identifiers separated by a dot character `.`, where the first identifier is the database name and the second identifier is the scope name.

If a single identifier is present, Enterprise Analytics resolves it as a scope name and assumes that the database is Default.

For more information about how Enterprise Analytics organizes entities into a `database.scope.database_object` hierarchy and resolves names, see [Entities in Enterprise Analytics](1a%5Fentities.md).

## [](#example)Example

The following example creates a scope with the name `myPlaylist` in the `music` database.

```SQL++
 CREATE SCOPE music.myPlaylist;
```