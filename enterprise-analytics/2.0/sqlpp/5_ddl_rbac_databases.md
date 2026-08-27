---
title: Database
description: The `GRANT` statement supports the granting of privileges on
  resources to users or roles as well as the assignment of roles to users.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/sqlpp/pages/5_ddl_rbac_databases.adoc
  xref: xref:2.0@enterprise-analytics:sqlpp:5_ddl_rbac_databases.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
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