---
title: Owner Concept
description: Understand object ownership in Operational Insights and how owners
  automatically receive privileges to manage their objects.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/manage/pages/manage-security/owner-concept.adoc
  xref: xref:enterprise-analytics:manage:manage-security/owner-concept.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/manage/manage-security/owner-concept.html)

# Owner Concept

> Understand object ownership in Operational Insights and how owners automatically receive privileges to manage their objects. 

Operational Insights uses the concept of an `OWNER` to manage object ownership and associated privileges. An `OWNER` is a user who creates an object in the system, such as a database, collection, view, function, or other entities.

When a user creates an object, the user is granted the `OWNERSHIP` privilege implicitly. This information is stored in the `Metadata`.`Privilege` collection.

## [](#object-privileges-table)Implicit Privileges

The following table shows the implicit privileges granted to owners for each object type:

__Table 1\. Implicit Privileges__
| Object Type | Implicit Privileges                                  |
| ----------- | ---------------------------------------------------- |
| Database    | DROP                                                 |
| Scope       | DROP                                                 |
| Collection  | SELECT, INSERT, UPSERT, DELETE, ALTER, DROP, ANALYZE |
| Index       | DROP                                                 |
| Link        | CONNECT, DISCONNECT, COPY TO, COPY FROM, DROP, ALTER |
| Role        | DROP                                                 |
| Synonym     | DROP                                                 |
| Function    | DROP, EXECUTE                                        |
| View        | SELECT, DROP                                         |

## [](#see-also)See Also

* [Role-Based Access Control (RBAC)](rbac-overview.md)
* [User Role Privileges](user-roles-privileges.md)
* [RBAC Statements](../../sqlpp/5%5Fddl%5Frbac%5Fstatement.md)