---
title: CREATE DATABASE Statements
description: This topic describes how you use the <code>CREATE</code> statement
  to create Operational Insights databases.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/sqlpp/pages/5_ddl_database.adoc
  xref: xref:enterprise-analytics:sqlpp:5_ddl_database.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/sqlpp/5_ddl_database.html)

# CREATE DATABASE Statements

> This topic describes how you use the `CREATE` statement to create Operational Insights databases. 

## [](#syntax)Syntax

**CreateDatabase EBNF** 

```EBNF
CreateDatabase ::= "CREATE" "DATABASE" Identifier ("IF" "NOT" "EXISTS")?
```

**CreateDatabase Diagram** 

![CREATE](_images/CreateDatabase.png) 

For information about specifying a database name, see [Entities](1a%5Fentities.md).

## [](#example)Example

```SQL++
  CREATE DATABASE music;
```