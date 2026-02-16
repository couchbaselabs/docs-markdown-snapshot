[View original HTML](/enterprise-analytics/2.0/sqlpp/5_ddl_rbac_roles.html)

## [](#grantrevoke-syntax-diagrams)Grant/Revoke Syntax Diagrams

**Grant Role Diagram** 

![GRANT](_images/grantrole.png) 

Example:

```sqlpp
GRANT CREATE, DROP ROLE TO USER user1, ROLE role1;
```

**Revoke Role Diagram** 

![REVOKE](_images/revokerole.png) 

Example:

```sqlpp
REVOKE CREATE, DROP ROLE FROM USER user1, ROLE role1;
```