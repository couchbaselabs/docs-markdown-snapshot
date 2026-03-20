---
title: requireUser()
description: Requiring Sync Gateway user
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.0/modules/access-control/pages/sync-function/sync-function-api-require-user-cmd.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:sync-gateway:access-control:sync-function/sync-function-api-require-user-cmd.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/current/access-control/sync-function/sync-function-api-require-user-cmd.html)

# requireUser()

> Requiring Sync Gateway user  

_Related Topics_: [access()](sync-function-api-access-cmd.md) | [channel()](sync-function-api-channel-cmd.md) | [expiry()](sync-function-api-expiry-cmd.md) | [requireAccess()](sync-function-api-require-access-cmd.md) | [requireAdmin()](sync-function-api-require-admin-cmd.md) | [requireRole()](sync-function-api-require-role-cmd.md) | [requireUser()](sync-function-api-require-user-cmd.md) | [role()](sync-function-api-role-cmd.md) | [throw()](sync-function-api-throw-cmd.md)

Function

requireUser(username)

## [](#purpose)Purpose

Use the `requireUser()` function to reject document updates that are not made by the specified user or users.

## [](#arguments)Arguments

| Argument | Description                                                                                                                                                                                              |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| username | Must be a string identifying a user, or an array of strings identifying multiple users; the function is applied to each user in the array. If the value resolves to null the function result is a no-op. |

## [](#context)Context

The function signals rejection by throwing an exception, so the rest of the sync function will not be run.

When validating a document, you should treat all properties of the `doc` parameter as _untrusted_. That is because it **is** the object that you’re validating. This may sound obvious, but it can be easy to make mistakes, like calling `requireUser(doc.owners)` instead of `requireUser(oldDoc.owners)`.

When using one document property to validate another, look up that property in `oldDoc`, not `doc`!

## [](#use)Use

Example 1\. requireUser(username)

```javascript
requireUser("snej"); (1)

requireUser(["snej", "jchris", "tleyden"]); (2)
```

| **1** | Throw an error if the user is not "snej":                 |
| ----- | --------------------------------------------------------- |
| **2** | Throw an error if user’s name is not in the list username |

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