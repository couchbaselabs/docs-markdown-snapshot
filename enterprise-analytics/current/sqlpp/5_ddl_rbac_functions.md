[View original HTML](/enterprise-analytics/current/sqlpp/5_ddl_rbac_functions.html)

## [](#grantrevoke-syntax-diagrams)Grant/Revoke Syntax Diagrams

**Grant Function Diagram** 

![GRANT](_images/grantfunction.png) 

Example:

```sqlpp
GRANT EXECUTE ON any FUNCTION TO USER user1, ROLE role1;
GRANT EXECUTE ON any FUNCTION IN DATABASE db TO USER user1, ROLE role1;
GRANT EXECUTE ON any FUNCTION IN SCOPE db.dv TO USER user1, ROLE role1;
GRANT EXECUTE ON FUNCTION func TO USER user1, ROLE role1;
GRANT CREATE, DROP FUNCTION TO USER user1, ROLE role1;
GRANT CREATE, DROP FUNCTION IN DATABASE db TO USER user1, ROLE role1;
GRANT CREATE, DROP FUNCTION IN SCOPE db.dv TO USER user1, ROLE role1;
```

**Revoke Function Diagram** 

![REVOKE](_images/revokefunction.png) 

Example:

```sqlpp
REVOKE EXECUTE ON any FUNCTION FROM USER user1, ROLE role1;
REVOKE EXECUTE ON any FUNCTION IN DATABASE db FROM USER user1, ROLE role1;
REVOKE EXECUTE ON any FUNCTION IN SCOPE db.dv FROM USER user1, ROLE role1;
REVOKE EXECUTE ON FUNCTION func FROM USER user1, ROLE role1;
REVOKE CREATE, DROP FUNCTION FROM USER user1, ROLE role1;
REVOKE CREATE, DROP FUNCTION IN DATABASE db FROM USER user1, ROLE role1;
REVOKE CREATE, DROP FUNCTION IN SCOPE db.dv FROM USER user1, ROLE role1;
```