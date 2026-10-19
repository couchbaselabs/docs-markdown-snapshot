---
title: DDL Statements
description: This section describes the SQL++ for Operational Insights Data
  Definition Language (DDL) statements.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/sqlpp/pages/5_ddl.adoc
  xref: xref:enterprise-analytics:sqlpp:5_ddl.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/sqlpp/5_ddl.html)

# DDL Statements

> This section describes the SQL++ for Operational Insights Data Definition Language (DDL) statements. 

## [](#Statements)Statements

In addition to [queries](3%5Fquery.md), SQL++ for Operational Insights supports statements for data definition.

To get information about a remote or external link, use a [DESCRIBE LINK](5%5Fdml%5Fdescribe.md) statement.

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

* [Entities](1a%5Fentities.md)
* [Data Model & Hierarchy](../sources/database-objects.md)