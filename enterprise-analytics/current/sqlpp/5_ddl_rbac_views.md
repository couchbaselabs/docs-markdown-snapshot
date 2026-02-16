[View original HTML](/enterprise-analytics/current/sqlpp/5_ddl_rbac_views.html)

## [](#grantrevoke-syntax-diagrams)Grant/Revoke Syntax Diagrams

**Grant View Diagram** 

![GRANT](_images/grantview.png) 

Example:

```sqlpp
GRANT SELECT ON any VIEW TO USER user1, ROLE role1;
GRANT SELECT ON any VIEW IN DATABASE db TO USER user1, ROLE role1;
GRANT SELECT ON any VIEW IN SCOPE db.dv TO USER user1, ROLE role1;
GRANT SELECT ON VIEW view0 TO USER user1, ROLE role1;
GRANT CREATE, DROP VIEW IN DATABASE db TO USER user1, ROLE role1;
GRANT CREATE, DROP VIEW IN SCOPE db.dv TO USER user1, ROLE role1;
```

**Revoke View Diagram** 

![REVOKE](_images/revokeview.png) 

Example:

```sqlpp
REVOKE SELECT ON any VIEW FROM USER user1, ROLE role1;
REVOKE SELECT ON any VIEW IN DATABASE db FROM USER user1, ROLE role1;
REVOKE SELECT ON any VIEW IN SCOPE db.dv FROM USER user1, ROLE role1;
REVOKE SELECT ON VIEW view0 FROM USER user1, ROLE role1;
REVOKE CREATE, DROP VIEW IN DATABASE db FROM USER user1, ROLE role1;
REVOKE CREATE, DROP VIEW IN SCOPE db.dv FROM USER user1, ROLE role1;
```