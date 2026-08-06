---
title: Functions
description: Use `GRANT` and `REVOKE` statements to manage function execution
  privileges and function creation/deletion rights for users and roles.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/sqlpp/pages/5_ddl_rbac_functions.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:2.1@enterprise-analytics:sqlpp:5_ddl_rbac_functions.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.1/sqlpp/5_ddl_rbac_functions.html)

# Functions

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