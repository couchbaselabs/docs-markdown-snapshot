---
title: role()
description: Assigning Sync Gateway <em>roles</em>
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.0/modules/access-control/pages/sync-function/sync-function-api-role-cmd.adoc
  xref: xref:4.0@sync-gateway:access-control:sync-function/sync-function-api-role-cmd.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/4.0/access-control/sync-function/sync-function-api-role-cmd.html)

# role()

> Assigning Sync Gateway _roles_  

_Related Topics_: [access()](sync-function-api-access-cmd.md) | [channel()](sync-function-api-channel-cmd.md) | [expiry()](sync-function-api-expiry-cmd.md) | [requireAccess()](sync-function-api-require-access-cmd.md) | [requireAdmin()](sync-function-api-require-admin-cmd.md) | [requireRole()](sync-function-api-require-role-cmd.md) | [requireUser()](sync-function-api-require-user-cmd.md) | [role()](sync-function-api-role-cmd.md) | [throw()](sync-function-api-throw-cmd.md)

Function

role(username, rolename)

## [](#lbl-role)Purpose

Use the `role()` function to add a role to a user. This indirectly gives them access to any channels assigned to that role.

> [!NOTE]
> Roles, like users, have to be explicitly created by an administrator.

## [](#arguments)Arguments

| Argument | Description                                                                                                                                                                                                                                                                                                                               |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| rolename | Must be a string identifying a role, or an array of strings identifying multiple roles; the function is applied to each role in the array. If the value resolves to null the function result is a no-op. **Note** — Role names must always be prefixed with role:; an exception is thrown if a role name doesn't conform with this rule.. |
| username | Must be a string identifying a user, or an array of strings identifying multiple users; the function is applied to each user in the array. If the value resolves to null the function result is a no-op.                                                                                                                                  |

## [](#context)Context

This function affects the user's ability to revise documents, if the access function requires role membership to validate certain types of changes. Its use is similar to `access`.

Nonexistent roles don't cause an error, but have no effect on the user's access privileges.

> [!TIP]
> You can create roles retrospectively. As soon as a role is created, any pre-existing references to it take effect.

## [](#use)Use

Example 1\. role(username, rolename)

```javascript
role ("jchris", "role:admin"); (1)
role ("jchris", ["role:portlandians", "role:portlandians-owners"]); (2)
role (["snej", "jchris", "traun"], "role:mobile"); (3)
role ("ed", null);  (4)
```

| **1** | The role admin is assigned to the user             |
| ----- | -------------------------------------------------- |
| **2** | Both the named roles are assigned to the user      |
| **3** | The role mobile is assigned to all the named users |
| **4** | No op                                              |

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Sync Function](sync-function.md)
* [Import filter](../../sync/import-processing.md)

###### [](#-3)

Reference material …​

* [Public REST API](../../rest-api/rest-api.md)
* [Admin REST API](../../rest-api/rest-api-admin.md)
* [Metrics REST API](../../rest-api/rest-api-metrics.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)