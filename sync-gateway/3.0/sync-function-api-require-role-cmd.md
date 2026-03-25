---
title: requireRole()
description: Requiring Sync Gateway role
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.0/modules/ROOT/pages/sync-function-api-require-role-cmd.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:3.0@sync-gateway::sync-function-api-require-role-cmd.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.0/sync-function-api-require-role-cmd.html)

# requireRole()

> Requiring Sync Gateway role  

_Related Topics_: [access()](sync-function-api-access-cmd.md) | [channel()](sync-function-api-channel-cmd.md) | [expiry()](sync-function-api-expiry-cmd.md) | [requireAccess()](sync-function-api-require-access-cmd.md) | [requireAdmin()](sync-function-api-require-admin-cmd.md) | requireRole() | [requireUser()](sync-function-api-require-user-cmd.md) | [role()](sync-function-api-role-cmd.md) | [throw()](sync-function-api-throw-cmd.md)

Function

requireRole(rolename)

## [](#purpose)Purpose

Use the `requireRole()` function to reject document updates that are not made by user with the specified role or roles, as shown in [Example 1](#ex-requirerole).

## [](#arguments)Arguments

| Argument | Description                                                                                                                                                                                                                                                                                                                               |
| -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| rolename | Must be a string identifying a role, or an array of strings identifying multiple roles; the function is applied to each role in the array. If the value resolves to null the function result is a no-op. **Note** — Role names must always be prefixed with role:; an exception is thrown if a role name doesn’t conform with this rule.. |

## [](#context)Context

The function requires that the user has at least one of the specified roles. If that is not the case it signals rejection by throwing an exception. The rest of the sync function will not be run.

## [](#use)Use

Example 1\. requireRole(rolename)

```javascript
requireRole("admin"); (1)

requireRole(["admin", "old-timer"]); (2)
```

| **1** | Throw an error unless the user has the "admin" role:           |
| ----- | -------------------------------------------------------------- |
| **2** | Throw an error unless the user has one or more of those roles: |

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Sync Function](sync-function-overview.md)
* [Import filter](import-filter.md)

###### [](#-3)

Reference material …​

* [Public REST API](rest-api.md)
* [Admin REST API](rest-api-admin.md)
* [Metrics REST API](rest-api-metrics.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)