---
title: Manage Service Roles with the UI
description: Use the <strong>Service RBAC</strong> tab of the
  <strong>Security</strong> screen to view, create, and drop service roles, and
  to grant and revoke privileges, without writing SQL++.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: guide
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/manage/pages/manage-security/manage-service-roles.adoc
  xref: xref:enterprise-analytics:manage:manage-security/manage-service-roles.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/manage/manage-security/manage-service-roles.html)

# Manage Service Roles with the UI

> Use the **Service RBAC** tab of the **Security** screen to view, create, and drop service roles, and to grant and revoke privileges, without writing SQL++. 

## [](#platform-and-service-roles)Platform Roles and Service Roles

Operational Insights authorizes users at two levels:

* _Platform roles_, assigned on the **Users & Groups** tab, decide who can reach the service at all, and who can administer the cluster. See [Users, Groups, and Roles](manage-users-and-roles.md).
* _Service roles_ and _privileges_, managed on the **Service RBAC** tab, decide what a user can do once they reach the service: which databases, scopes, collections, views, links, catalogs, libraries, and functions they can read, write, create, or drop.

A platform role that can manage the service, such as Full Admin, bypasses service roles entirely.

The **Service RBAC** tab is a view onto the same roles and privileges that the [GRANT](../../sqlpp/5%5Fddl%5Fgrant%5Fstatement.md) and [REVOKE](../../sqlpp/5%5Fddl%5Frevoke%5Fstatement.md) statements, and [CREATE ROLE and DROP ROLE](user-defined-role.md), manage. Before you grant, revoke, assign, or drop, the dialog shows the SQL++ statement it will run.

## [](#prerequisites)Prerequisites

Any user who can access the service can open the **Service RBAC** tab. What the tab offers depends on the user's roles:

* To make changes, you need either a platform role that can manage the service, or the **Service Root** or **Service RBAC Admin** service role.
* Other users see the tab read-only, with no actions. The service decides what each user can see, so a read-only view may not list every role.

## [](#open-the-tab)Open the Service RBAC Tab

1. In the Web Console, click **Security** in the navigation bar.
2. Click the **Service RBAC** tab.

The tab has two tables: **Service Roles** and **Users**. Click **REFRESH**, at the upper right, to reload both.

If the service cannot be reached, the tab says so and shows no tables. Nothing has changed; click **REFRESH** once the service is available again.

## [](#service-roles-table)The Service Roles Table

The **Service Roles** table lists every role you are entitled to see, with:

* **role**: the role's name. Built-in roles show a display name, followed by the identifier that SQL++ statements use. Hover over a built-in role for a description.
* **type**: **built-in** or **custom**.
* **privileges**: how many privileges the role holds, including those it inherits from roles it includes.
* **granted to**: how many users and roles hold the role.

Use the **filter by role name** field to narrow the list.

Click a role to expand it. The expanded row lists each privilege, the object it applies to, and, for an inherited privilege, the role it comes **through**. It also lists the roles the role **includes** and the users and roles it is **granted to**.

Ownership, which the service records for whoever created an object, is not listed. See [Owner Concept](owner-concept.md).

### [](#built-in-roles)Built-In Roles

The built-in roles correspond to the [system defined roles](system-defined-roles.md):

| Display name        | Identifier           | Allows                                                                                                                                                                                                        |
| ------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Service Root        | sys\_root            | Everything that Service Data Admin and Service RBAC Admin allow, plus the service's own diagnostic functions.                                                                                                 |
| Service RBAC Admin  | sys\_security\_admin | Create and drop service roles, and grant and revoke privileges. Cannot grant Service Root, which needs a platform role that can manage the service; nor Service RBAC Admin, which needs that or Service Root. |
| Service Data Admin  | sys\_data\_admin     | Create, alter, and drop databases, scopes, collections, views, indexes, functions, links, and catalogs, and write their data. Includes Service Data Reader.                                                   |
| Service Data Reader | sys\_data\_reader    | Read collections and describe links. Includes Service View Reader.                                                                                                                                            |
| Service View Reader | sys\_view\_reader    | Read views.                                                                                                                                                                                                   |

A built-in role's privileges are fixed, and it cannot be dropped. It can still be granted to users.

## [](#users-table)The Users Table

The **Users** table lists cluster users with the service roles and privileges they hold:

* **username**, labeled **you** for the signed-in user.
* **domain**: **Couchbase** for a local user, **External** for one authenticated externally.
* **service roles**: the roles the user holds.
* **direct privileges**: how many privileges are granted to the user directly, rather than through a role.

Use the **filter by username** field to narrow the list. Click a user to expand the row and see their roles and direct privileges in full.

Users are created and deleted on the **Users & Groups** tab, not here.

## [](#create-a-role)Create a Service Role

1. Click **ADD SERVICE ROLE**, at the upper right.
2. In the **Role Name** field, enter a name. Role names are global across the instance, and must not match an existing role.
3. Click **Add Role**.

The role starts with no privileges. Grant them as described in [Grant a Privilege](#grant-a-privilege).

## [](#grant-a-privilege)Grant a Privilege

You can grant a privilege to a custom role, or directly to a user. A privilege granted to a user applies only to that user; where several users need the same access, grant it to a role they hold instead.

1. Expand the custom role or the user in its table, and click **Grant Privilege**.
2. In **Applies To**, select the kind of object: **Collection**, **View**, **Database**, **Scope**, **Link**, **Linked catalog**, **Function**, **Library**, **Index**, **Synonym**, or **Role**.
3. Under **Privileges**, select one or more privileges. The list depends on the kind of object. Privileges marked _on objects not yet created_, such as CREATE, apply to objects that do not exist yet. They cannot be granted together with privileges on existing objects; grant them separately.
4. In **Scope**, select where the privilege applies:

  * **Everywhere**: every object of that kind, including objects created later.
  * **In a database** or **In a scope**: then select the **Database**, and the **Scope** if needed.
  * **One object**: then select the database and scope, if the object has them, and enter its **Name**. For a function, you can also enter the **Number of Arguments**, because each overload of a function is a separate object. Leave it empty for any number.  
The options offered depend on the kind of object and the privileges selected.
5. Review the SQL++ shown under **Statement**, and click **Grant**.

## [](#revoke-a-privilege)Revoke a Privilege

1. Expand the role or user that holds the privilege.
2. Click **revoke** beside the privilege, and confirm.

Only a privilege the role holds itself can be revoked from it. A privilege it inherits must be revoked from the role it comes through.

## [](#assign-roles)Assign Service Roles to a User

1. In the **Users** table, expand the user, and click **Edit Service Roles**.
2. Select the roles the user should hold, and clear those they should not.
3. Review the SQL++ shown under **Statement**, and click **Save**.

To remove a single role, you can also click **revoke** beside it in the user's expanded row.

## [](#drop-a-role)Drop a Service Role

1. Expand the custom role in the **Service Roles** table.
2. Click **Drop Role**, and confirm.

A role cannot be dropped while it is in use: that is, while it is both granted to at least one user or role, and conveys privileges to them. A role conveys privileges if privileges are granted to it directly, or if it holds another role that does, at any depth, or if it holds a built-in role. Such a drop fails with error code 24341, and nothing changes. The role's expanded row shows both what it is **granted to** and the privileges it holds, including those it inherits. To drop the role, first revoke it from its holders, or revoke the privileges and roles that it holds.

Otherwise, the drop succeeds. It also removes any remaining grants of the role, the privileges granted to it, and its own holdings of other roles. Built-in roles cannot be dropped.

## [](#orphaned-grants)Purge Orphaned Grants

The service identifies a user by an internal ID, not by name. If a user is deleted while still holding service roles or privileges, those grants remain in the service's metadata, but they grant nothing. A new user created with the same name does not inherit them.

The **Users** table labels such entries:

* **orphaned**: no cluster user matches the grantee.
* **former account**: the grants belong to an earlier, deleted account with the same name as a current user. The current user does not hold them.

To remove them:

1. Expand the entry in the **Users** table.
2. Click **Purge Orphaned Grants**, and confirm.

Purging removes only the grants made to the deleted account. A current user with the same name is not affected.

## [](#see-also)See Also

* [Role-Based Access Control](rbac-overview.md)
* [System Defined Roles](system-defined-roles.md)
* [User Defined Roles](user-defined-role.md)
* [GRANT Statement](../../sqlpp/5%5Fddl%5Fgrant%5Fstatement.md)
* [REVOKE Statement](../../sqlpp/5%5Fddl%5Frevoke%5Fstatement.md)