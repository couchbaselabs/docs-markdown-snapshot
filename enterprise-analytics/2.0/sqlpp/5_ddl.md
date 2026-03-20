---
title: DDL Statements
description: This section describes the SQL++ for Enterprise Analytics Data
  Definition Language (DDL) statements.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/sqlpp/pages/5_ddl.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:2.0@enterprise-analytics:sqlpp:5_ddl.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.0/sqlpp/5_ddl.html)

# DDL Statements

> This section describes the SQL++ for Enterprise Analytics Data Definition Language (DDL) statements. 

## [](#Statements)Statements

In addition to [queries](3%5Fquery.md), SQL++ for Enterprise Analytics supports statements for data definition.

> [!TIP]
> In Enterprise Analytics, the keyword `ANALYTICS` is optional in DDL statements.

## [](#syntax)Syntax

**Stmnt EBNF** 

```EBNF
Stmnt::= (SingleStmnt ";")+ EOF
```

**Stmnt Diagram** 

![(SingleStmnt ";")+ EOF](_images/Stmnt.png) 

**SingleStmnt Diagram** 

![UseStmnt | Query | CreateStmnt | DropStmnt |  ConnectStmnt | DisconnectStmt](_images/SingleStmnt.png) 

## [](#see-also)See Also

* [Entities in Enterprise Analytics](1a%5Fentities.md)
* [Access and Organize Data in Enterprise Analytics](../sources/database-objects.md)