---
title: RBAC Statements
description: Use `GRANT` and `REVOKE` statements to manage user privileges and
  role assignments across Operational Insights database objects.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/sqlpp/pages/5_ddl_rbac_statement.adoc
  xref: xref:enterprise-analytics:sqlpp:5_ddl_rbac_statement.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/sqlpp/5_ddl_rbac_statement.html)

# RBAC Statements

The GRANT statement supports the granting of privileges on resources to users or roles as well as the assignment of roles to users.

The REVOKE statement allows revoking previously granted RBAC privileges or roles from specific users. It's important to understand that REVOKE is the inverse of GRANT. Its purpose is to undo the effect of a prior GRANT.

You can use GRANT and REVOKE statements to manage privileges on the following Operational Insights objects: Databases, Scopes, Collections, Views, Indexes, Functions, Links, Roles, and Synonyms.

* [GRANT Statement](5%5Fddl%5Fgrant%5Fstatement.md)
* [REVOKE Statement](5%5Fddl%5Frevoke%5Fstatement.md)

## [](#see-also)See Also

* [System Defined Roles](../manage/manage-security/system-defined-roles.md) — pre-built roles you can GRANT or REVOKE without defining custom privilege sets.
* [Owner Concept](../manage/manage-security/owner-concept.md) — the implicit privileges a user already has on an object they created, without any GRANT statement.