---
title: User Defined Roles
description: Learn how to create custom roles in Operational Insights to
  implement granular access control that matches your organization's specific
  security requirements.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/manage/pages/manage-security/user-defined-role.adoc
  xref: xref:enterprise-analytics:manage:manage-security/user-defined-role.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/manage/manage-security/user-defined-role.html)

# User Defined Roles

> Learn how to create custom roles in Operational Insights to implement granular access control that matches your organization's specific security requirements. 

Operational Insights allows you to create custom roles tailored to your organization's specific access control needs. Create user-defined roles to group privileges logically and assign them to multiple users for consistent security management across your database environment.

This information is stored in the `Metadata`.`Role` collection.

## [](#create-role)Create Role

The `CREATE ROLE` statement creates a new role for use within an Operational Insights instance.

**Create Role Diagram** 

![create_role ::= 'CREATE' 'ROLE' role](../../sqlpp/_images/create_role.png) 

Role names are global within an Operational Insights instance. They must be unique across databases and scopes or else the create attempt fails.

You can also create and drop roles, and grant privileges to them, from the **Service RBAC** tab of the Web Console. See [Manage Service Roles with the UI](manage-service-roles.md).

## [](#drop-role)Drop Role

The `DROP ROLE` statement drops an existing role from an Operational Insights instance.

**Drop Role Diagram** 

![drop_role ::= ](../../sqlpp/_images/drop_role.png) 

A role cannot be dropped while it is in use: that is, while it is both granted to at least one user or role, and conveys privileges to them. A role conveys privileges if privileges are granted to it directly, or if it holds another role that does, at any depth, or if it holds a built-in role. Such a drop fails with error code 24341, and nothing changes. To drop the role, first revoke it from its holders, or revoke the privileges and roles that it holds.

Otherwise, the drop succeeds. It also removes any remaining grants of the role, the privileges granted to it, and its own holdings of other roles. Built-in roles cannot be dropped.

## [](#example)Example

The following example creates a user-defined role named `roleName` with specific privileges:

```sqlpp
CREATE ROLE roleName;
DROP ROLE roleName
```