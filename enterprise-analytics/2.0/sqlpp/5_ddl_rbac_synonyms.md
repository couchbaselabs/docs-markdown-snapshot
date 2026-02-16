[View original HTML](/enterprise-analytics/2.0/sqlpp/5_ddl_rbac_synonyms.html)

## [](#grantrevoke-syntax-diagrams)Grant/Revoke Syntax Diagrams

**Grant Synonym Diagram** 

![GRANT](_images/grantsynonym.png) 

Example:

```sqlpp
GRANT CREATE, DROP SYNONYM TO USER user1, ROLE role1;
GRANT CREATE, DROP SYNONYM IN DATABASE db TO USER user1, ROLE role1;
GRANT CREATE, DROP SYNONYM IN SCOPE db.dv TO USER user1, ROLE role1;
```

**Revoke Synonym Diagram** 

![REVOKE](_images/revokesynonym.png) 

Example:

```sqlpp
REVOKE CREATE, DROP SYNONYM FROM USER user1, ROLE role1;
REVOKE CREATE, DROP SYNONYM IN DATABASE db FROM USER user1, ROLE role1;
REVOKE CREATE, DROP SYNONYM IN SCOPE db.dv FROM USER user1, ROLE role1;
```