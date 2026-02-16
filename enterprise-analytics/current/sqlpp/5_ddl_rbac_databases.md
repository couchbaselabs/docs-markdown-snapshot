[View original HTML](/enterprise-analytics/current/sqlpp/5_ddl_rbac_databases.html)

## [](#grantrevoke-syntax-diagrams)Grant/Revoke Syntax Diagrams

**Grant Database Diagram** 

![GRANT](_images/grantdatabase.png) 

Example:

```sqlpp
GRANT CREATE, DROP DATABASE TO USER user1, ROLE role1;
```

**Revoke Database Diagram** 

![REVOKE](_images/revokedatabase.png) 

Example:

```sqlpp
REVOKE CREATE, DROP DATABASE FROM USER user1, ROLE role1;
```