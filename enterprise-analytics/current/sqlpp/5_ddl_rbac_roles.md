---
title: Roles
description: Use `GRANT` and `REVOKE` statements to manage role creation and
  deletion privileges, and assign roles to users and other roles.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/sqlpp/pages/5_ddl_rbac_roles.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:enterprise-analytics:sqlpp:5_ddl_rbac_roles.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/sqlpp/5_ddl_rbac_roles.html)

# Roles

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