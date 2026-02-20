---
title: Synonyms
description: Use `GRANT` and `REVOKE` statements to manage synonym creation and
  deletion privileges for users and roles within databases and scopes.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/sqlpp/pages/5_ddl_rbac_synonyms.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:enterprise-analytics:sqlpp:5_ddl_rbac_synonyms.adoc[]
---

[View original HTML](/enterprise-analytics/current/sqlpp/5_ddl_rbac_synonyms.html)

# Synonyms

## [](#grantrevoke-syntax-diagrams)Grant/Revoke Syntax Diagrams

**Grant Synonym Diagram** 

![GRANT](_images/grantsynonym.png) 

Example:

```sqlpp
GRANT CREATE, DROP SYNONYM TO USER user1, ROLE role1;
GRANT CREATE, DROP SYNONYM IN DATABASE db TO USER user1, ROLE role1;
GRANT CREATE, DROP SYNONYM IN SCOPE db.dv TO USER user1, ROLE role1;
```

**Revoke Synonym Diagram** 

![REVOKE](_images/revokesynonym.png) 

Example:

```sqlpp
REVOKE CREATE, DROP SYNONYM FROM USER user1, ROLE role1;
REVOKE CREATE, DROP SYNONYM IN DATABASE db FROM USER user1, ROLE role1;
REVOKE CREATE, DROP SYNONYM IN SCOPE db.dv FROM USER user1, ROLE role1;
```