---
title: Views
description: Use `GRANT` and `REVOKE` statements to manage view privileges
  including SELECT operations and view creation/deletion rights for users and
  roles.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/sqlpp/pages/5_ddl_rbac_views.adoc
  xref: xref:2.1@enterprise-analytics:sqlpp:5_ddl_rbac_views.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.1/sqlpp/5_ddl_rbac_views.html)

# Views

## [](#grantrevoke-syntax-diagrams)Grant/Revoke Syntax Diagrams

**Grant View Diagram** 

![GRANT](_images/grantview.png) 

Example:

```sqlpp
GRANT SELECT ON any VIEW TO USER user1, ROLE role1;
GRANT SELECT ON any VIEW IN DATABASE db TO USER user1, ROLE role1;
GRANT SELECT ON any VIEW IN SCOPE db.dv TO USER user1, ROLE role1;
GRANT SELECT ON VIEW view0 TO USER user1, ROLE role1;
GRANT CREATE, DROP VIEW IN DATABASE db TO USER user1, ROLE role1;
GRANT CREATE, DROP VIEW IN SCOPE db.dv TO USER user1, ROLE role1;
```

**Revoke View Diagram** 

![REVOKE](_images/revokeview.png) 

Example:

```sqlpp
REVOKE SELECT ON any VIEW FROM USER user1, ROLE role1;
REVOKE SELECT ON any VIEW IN DATABASE db FROM USER user1, ROLE role1;
REVOKE SELECT ON any VIEW IN SCOPE db.dv FROM USER user1, ROLE role1;
REVOKE SELECT ON VIEW view0 FROM USER user1, ROLE role1;
REVOKE CREATE, DROP VIEW IN DATABASE db FROM USER user1, ROLE role1;
REVOKE CREATE, DROP VIEW IN SCOPE db.dv FROM USER user1, ROLE role1;
```