[View original HTML](/enterprise-analytics/2.0/sqlpp/5_ddl_rbac_links.html)

## [](#grantrevoke-syntax-diagrams)Grant/Revoke Syntax Diagrams

**Grant Link Diagram** 

![GRANT](_images/grantlink.png) 

Example:

```sqlpp
GRANT CREATE, DROP, ALTER LINK TO USER user1, ROLE role1;
GRANT CONNECT, DISCONNECT ON any LINK TO USER user1, ROLE role1;
GRANT DISCONNECT ON any LINK link0 TO USER user1, ROLE role1;
```

**Revoke Link Diagram** 

![REVOKE](_images/revokelink.png) 

Example:

```sqlpp
REVOKE CREATE, DROP, ALTER LINK FROM USER user1, ROLE role1;
REVOKE CONNECT, DISCONNECT ON any LINK FROM USER user1, ROLE role1;
REVOKE DISCONNECT ON any LINK link0 FROM USER user1, ROLE role1;
```