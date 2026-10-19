---
title: DDL Statements
description: This section describes the SQL++ for Operational Insights Cloud
  Data Definition Language (DDL) statements.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Capella
    version: ""
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/sqlpp/pages/5_ddl.adoc
  xref: xref:analytics:sqlpp:5_ddl.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights-cloud/sqlpp/5_ddl.html)

# DDL Statements

> This section describes the SQL++ for Operational Insights Cloud Data Definition Language (DDL) statements. 

## [](#Statements)Statements

In addition to [queries](3%5Fquery.md), SQL++ for Operational Insights Cloud supports statements for data definition.

> [!TIP]
> In Operational Insights, the keyword `ANALYTICS` is optional in DDL statements.

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

* [Entities in Operational Insights Services](1a%5Fentities.md)
* [Access and Organize Data in Operational Insights Services](../sources/database-objects.md)