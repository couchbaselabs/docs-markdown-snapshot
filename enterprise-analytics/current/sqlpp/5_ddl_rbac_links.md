---
title: Links
description: Use `GRANT` and `REVOKE` statements to manage link privileges
  including CONNECT, DISCONNECT, COPY operations, and link creation/deletion
  rights for users and roles.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/sqlpp/pages/5_ddl_rbac_links.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/enterprise-analytics/current/sqlpp/5_ddl_rbac_links.html)

# Links

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