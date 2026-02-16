[View original HTML](/enterprise-analytics/current/sqlpp/5_ddl.html)

> This section describes the SQL++ for Enterprise Analytics Data Definition Language (DDL) statements. 

## [](#Statements)Statements

In addition to [queries](3%5Fquery.md), SQL++ for Enterprise Analytics supports statements for data definition.

|  | In Enterprise Analytics, the keyword ANALYTICS is optional in DDL statements. |
|  | ----------------------------------------------------------------------------- |

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