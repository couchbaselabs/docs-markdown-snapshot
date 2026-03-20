---
title: Manage Access to Cluster Data
description: Access control accounts provide granular, programmatic and
  application-level access to data on a cluster.
editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/admin/pages/auth/auth-data.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:analytics:admin:auth/auth-data.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/analytics/admin/auth/auth-data.html)

# Manage Access to Cluster Data

> Access control accounts provide granular, programmatic and application-level access to data on a cluster. 

You need an access control account to programmatically access data on a Capella Analytics cluster. Access control accounts for Capella Analytics are separate from Capella’s organization and project roles.

Access control accounts are not associated with a particular user. They do not control access to UI data tools like the Workbench.

## [](#prerequisites)Prerequisites

To create, modify, and delete access control accounts and roles, you need:

* One of the following Capella roles:

  * [Organization Owner](../../../cloud/organizations/organization-user-roles.md#organization-role-organization-owner)
  * [Project Owner](auth-ui.md#project-owner-role)

> [!NOTE]
> The [Project Viewer](auth-ui.md#project-cluster-viewer-role) role can view control accounts and roles, but cannot modify or create them.

## [](#create-an-access-control-account)Create an Access Control Account

1. In the Capella UI, select the **Capella Analytics** tab and then select a cluster.
2. Click **Settings** **Access Control**.
3. Click **Create Account**.
4. Enter the name and password for the new access control account.  
An access control account cannot have the same name as a role. You can change the password for an access control account at any time.
5. Assign roles:  
When creating an access control account, you can assign it system preset roles or [create new roles](#create-roles). Roles include a set of privileges that you can apply to multiple access control accounts for your cluster
6. Assign privileges:  
Instead of or in addition to roles, you can also assign privileges directly to an access account. Click **Assign Privileges** to show a list of all the privileges you can give to this access account.  
__Table 1\. Manage Access to Cluster Data__
| Object         | Implicit Privileges for Object Owner                                       |
| -------------- | -------------------------------------------------------------------------- |
| **Database**   | Create and Drop                                                            |
| **Scope**      | Create and Drop                                                            |
| **Collection** | Create, Drop, Select, Insert, Upsert, Delete, and Analyze                  |
| **View**       | Create, Drop, and Select                                                   |
| **Index**      | Create and Drop                                                            |
| **Function**   | Execute, Create, and Drop                                                  |
| **Link**       | Create, Drop, Alter, Connect, Disconnect, Copy To, Copy From, and DESCRIBE |
| **Role**       | Create and Drop                                                            |
| **Synonym**    | Create and Drop                                                            |  
To create an object, you must have the necessary roles or privileges. If you have the required `Create` privilege, and you create an object, you become the owner of the object. The object owner has an OWNERSHIP privilege, which allows you to perform any valid actions with the object. If you are not the owner of the object, explicit privileges must be granted.  
For greater control, you can narrow the scope of a privilege to specific databases, scopes, or links as applicable. Any privileges you apply directly to an account are on the management page for the access control account, where you can modify or remove them.
7. Click **Save**.

## [](#create-roles)Create Roles

A role is a group of privileges you can assign to one or more access control accounts in your Capella Analytics cluster. Using roles allows you to more easily create multiple access control accounts with the same privileges and rotate them.

Capella Analytics provides four preset roles that cover common use cases: `sys_data_admin`, `sys_data_reader`, `sys_external_stats_reader`, and `sys_view_reader`. You cannot delete these roles.

> [!NOTE]
> The new role you create must not start with `sys_`.

To create a new role:

1. In the Capella UI, select the **Capella Analytics** tab and then select a cluster.
2. Click **Settings** **Access Control** **Roles**.
3. Click **Create Role**.
4. Enter the name and an optional description for the new role.  
A role cannot have the same name as an access control account.
5. Click **Assign Privileges** to show a list of all the privileges you can give to this role. For greater control, you can narrow the scope of a privilege to specific databases, scopes, or links as applicable.
6. Click **Assign**.
7. Click **Create**.

## [](#next-steps)Next Steps

* To provide user access to the Capella UI and Capella Analytics clusters, see [Assign Roles for UI Access](auth-ui.md).