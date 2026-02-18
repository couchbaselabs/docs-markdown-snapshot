---
title: Database
description: The `GRANT` statement supports the granting of privileges on
  resources to users or roles as well as the assignment of roles to users.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/sqlpp/pages/5_ddl_rbac_databases.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/enterprise-analytics/2.0/sqlpp/5_ddl_rbac_databases.html)

# Database

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