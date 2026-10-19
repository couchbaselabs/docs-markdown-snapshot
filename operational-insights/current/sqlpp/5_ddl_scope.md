---
title: CREATE SCOPE Statements
description: This topic describes how you use the <code>CREATE</code> statement
  to create Operational Insights scopes.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/sqlpp/pages/5_ddl_scope.adoc
  xref: xref:enterprise-analytics:sqlpp:5_ddl_scope.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/sqlpp/5_ddl_scope.html)

# CREATE SCOPE Statements

> This topic describes how you use the `CREATE` statement to create Operational Insights scopes. 

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

If a single identifier is present, Operational Insights resolves it as a scope name and assumes that the database is Default.

For more information about how Operational Insights organizes entities into a `database.scope.database_object` hierarchy and resolves names, see [Entities](1a%5Fentities.md).

## [](#example)Example

The following example creates a scope with the name `myPlaylist` in the `music` database.

```SQL++
 CREATE SCOPE music.myPlaylist;
```