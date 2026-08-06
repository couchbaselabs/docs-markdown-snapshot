---
title: RBAC Statements
description: Use `GRANT` and `REVOKE` statements to manage user privileges and
  role assignments across Enterprise Analytics database objects.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/sqlpp/pages/5_ddl_rbac_statement.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:enterprise-analytics:sqlpp:5_ddl_rbac_statement.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/sqlpp/5_ddl_rbac_statement.html)

# RBAC Statements

The GRANT statement supports the granting of privileges on resources to users or roles as well as the assignment of roles to users.

The REVOKE statement allows revoking previously granted RBAC privileges or roles from specific users. It's important to understand that REVOKE is the inverse of GRANT. Its purpose is to undo the effect of a prior GRANT.

You can use GRANT/REVOKE statements to create the following Enterprise Analytics objects:

* [Database](5%5Fddl%5Frbac%5Fdatabases.md)
* [Scopes](5%5Fddl%5Frbac%5Fscopes.md)
* [Collections](5%5Fddl%5Frbac%5Fcollections.md)
* [Views](5%5Fddl%5Frbac%5Fviews.md)
* [Indexes](5%5Fddl%5Frbac%5Findexes.md)
* [Functions](5%5Fddl%5Frbac%5Ffunctions.md)
* [Links](5%5Fddl%5Frbac%5Flinks.md)
* [Roles](5%5Fddl%5Frbac%5Froles.md)
* [Synonyms](5%5Fddl%5Frbac%5Fsynonyms.md)