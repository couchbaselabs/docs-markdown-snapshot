---
title: CREATE DATABASE Statements
description: This topic describes how you use the <code>CREATE</code> statement
  to create Enterprise Analytics databases.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/sqlpp/pages/5_ddl_database.adoc
  xref: xref:enterprise-analytics:sqlpp:5_ddl_database.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/sqlpp/5_ddl_database.html)

# CREATE DATABASE Statements

> This topic describes how you use the `CREATE` statement to create Enterprise Analytics databases. 

For general `CREATE` statement syntax, see [CREATE Statements](5%5Fddl%5Fcreate.md).

## [](#syntax)Syntax

**CreateDatabase EBNF** 

```EBNF
CreateDatabase ::= "CREATE" "DATABASE" Identifier ("IF" "NOT" "EXISTS")?
```

**CreateDatabase Diagram** 

![CREATE](_images/CreateDatabase.png) 

For information about specifying a database name, see [Entities in Enterprise Analytics](1a%5Fentities.md).

## [](#example)Example

```SQL++
  CREATE DATABASE music;
```