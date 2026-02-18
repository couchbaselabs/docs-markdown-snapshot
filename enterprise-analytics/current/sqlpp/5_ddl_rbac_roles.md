---
title: Roles
description: Use `GRANT` and `REVOKE` statements to manage role creation and
  deletion privileges, and assign roles to users and other roles.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/sqlpp/pages/5_ddl_rbac_roles.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

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