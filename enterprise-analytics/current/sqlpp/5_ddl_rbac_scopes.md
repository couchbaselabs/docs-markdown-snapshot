[View original HTML](/enterprise-analytics/current/sqlpp/5_ddl_rbac_scopes.html)

## [](#grantrevoke-syntax-diagrams)Grant/Revoke Syntax Diagrams

**Grant Scope Diagram** 

![GRANT](_images/grantscope.png) 

Example:

```sqlpp
GRANT CREATE, DROP SCOPE TO USER user1, ROLE role1;
GRANT CREATE, DROP SCOPE IN DATABASE db TO USER user1, ROLE role1;
```

**Revoke Scope Diagram** 

![REVOKE](_images/revokescope.png) 

Example:

```sqlpp
REVOKE CREATE, DROP SCOPE FROM USER user1, ROLE role1;
REVOKE CREATE, DROP SCOPE IN DATABASE db FROM USER user1, ROLE role1;
```