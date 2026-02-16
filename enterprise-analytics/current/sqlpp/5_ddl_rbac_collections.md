[View original HTML](/enterprise-analytics/current/sqlpp/5_ddl_rbac_collections.html)

## [](#grantrevoke-syntax-diagrams)Grant/Revoke Syntax Diagrams

**Grant Collection Diagram** 

![GRANT](_images/grantcollection.png) 

Example:

```sqlpp
GRANT SELECT, INSERT ON any COLLECTION TO USER user1, ROLE role1;
GRANT SELECT, INSERT ON any COLLECTION IN DATABASE db TO USER user1, ROLE role1;
GRANT SELECT, INSERT ON any COLLECTION IN SCOPE db.dv TO USER user1, ROLE role1;
GRANT SELECT, INSERT ON COLLECTION col1 TO USER user1, ROLE role1;
GRANT CREATE, DROP COLLECTION IN DATABASE db TO USER user1, ROLE role1;
GRANT CREATE, DROP COLLECTION IN SCOPE db.dv TO USER user1, ROLE role1;
```

**Revoke Collection Diagram** 

![REVOKE](_images/revokecollection.png) 

Example:

```sqlpp
REVOKE SELECT, INSERT ON any COLLECTION FROM USER user1, ROLE role1;
REVOKE SELECT, INSERT ON any COLLECTION IN DATABASE db FROM USER user1, ROLE role1;
REVOKE SELECT, INSERT ON any COLLECTION IN SCOPE db.dv FROM USER user1, ROLE role1;
REVOKE SELECT, INSERT ON COLLECTION col1 FROM USER user1, ROLE role1;
REVOKE CREATE, DROP COLLECTION IN DATABASE db FROM USER user1, ROLE role1;
REVOKE CREATE, DROP COLLECTION IN SCOPE db.dv FROM USER user1, ROLE role1;
```