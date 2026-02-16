[View original HTML](/analytics/sqlpp/5_ddl.html)

> This section describes the SQL++ for Capella Analytics Data Definition Language (DDL) statements. 

## [](#Statements)Statements

In addition to [queries](3%5Fquery.md), SQL++ for Capella Analytics supports statements for data definition.

|  | In Capella Analytics, the keyword ANALYTICS is optional in DDL statements. |
|  | -------------------------------------------------------------------------- |

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

* [Entities in Capella Analytics Services](1a%5Fentities.md)
* [Access and Organize Data in Capella Analytics Services](../sources/database-objects.md)