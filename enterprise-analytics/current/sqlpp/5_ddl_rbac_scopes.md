---
title: Scopes
description: Use `GRANT` and `REVOKE` statements to control scope creation and
  deletion privileges for users and roles in Enterprise Analytics databases.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/sqlpp/pages/5_ddl_rbac_scopes.adoc
  xref: xref:enterprise-analytics:sqlpp:5_ddl_rbac_scopes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/sqlpp/5_ddl_rbac_scopes.html)

# Scopes

## [](#grantrevoke-syntax-diagrams)Grant/Revoke Syntax Diagrams

**Grant Scope Diagram** 

![GRANT](_images/grantscope.png) 

Example:

```sqlpp
GRANT CREATE, DROP SCOPE TO USER user1, ROLE role1;
GRANT CREATE, DROP SCOPE IN DATABASE db TO USER user1, ROLE role1;
```

**Revoke Scope Diagram** 

![REVOKE](_images/revokescope.png) 

Example:

```sqlpp
REVOKE CREATE, DROP SCOPE FROM USER user1, ROLE role1;
REVOKE CREATE, DROP SCOPE IN DATABASE db FROM USER user1, ROLE role1;
```