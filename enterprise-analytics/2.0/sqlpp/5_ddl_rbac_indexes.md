[View original HTML](/enterprise-analytics/2.0/sqlpp/5_ddl_rbac_indexes.html)

## [](#grantrevoke-syntax-diagrams)Grant/Revoke Syntax Diagrams

**Grant Index Diagram** 

![GRANT](_images/grantindex.png) 

Example:

```sqlpp
GRANT CREATE, DROP INDEX ON any COLLECTION TO USER user1, ROLE role1;
GRANT CREATE, DROP INDEX ON any COLLECTION IN DATABASE db TO USER user1, ROLE role1;
GRANT CREATE, DROP INDEX ON any COLLECTION IN SCOPE db.dv TO USER user1, ROLE role1;
GRANT CREATE, DROP INDEX ON COLLECTION col1 TO USER user1, ROLE role1;
```

**Revoke Index Diagram** 

![REVOKE](_images/revokeindex.png) 

Example:

```sqlpp
REVOKE CREATE, DROP INDEX ON any COLLECTION FROM USER user1, ROLE role1;
REVOKE CREATE, DROP INDEX ON any COLLECTION IN DATABASE db FROM USER user1, ROLE role1;
REVOKE CREATE, DROP INDEX ON any COLLECTION IN SCOPE db.dv FROM USER user1, ROLE role1;
REVOKE CREATE, DROP INDEX ON COLLECTION col1 FROM USER user1, ROLE role1;
```