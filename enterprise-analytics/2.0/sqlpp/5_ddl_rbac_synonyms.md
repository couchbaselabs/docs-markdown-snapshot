---
title: Synonyms
description: Use `GRANT` and `REVOKE` statements to manage synonym creation and
  deletion privileges for users and roles within databases and scopes.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/sqlpp/pages/5_ddl_rbac_synonyms.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:2.0@enterprise-analytics:sqlpp:5_ddl_rbac_synonyms.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.0/sqlpp/5_ddl_rbac_synonyms.html)

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