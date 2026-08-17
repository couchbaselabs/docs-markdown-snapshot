---
title: requireAdmin()
description: Requiring Sync Gateway admin user
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.1/modules/ROOT/pages/sync-function-api-require-admin-cmd.adoc
  xref: xref:3.1@sync-gateway::sync-function-api-require-admin-cmd.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.1/sync-function-api-require-admin-cmd.html)

# requireAdmin()

> Requiring Sync Gateway admin user  

_Related Topics_: [access()](sync-function-api-access-cmd.md) | [channel()](sync-function-api-channel-cmd.md) | [expiry()](sync-function-api-expiry-cmd.md) | [requireAccess()](sync-function-api-require-access-cmd.md) | requireAdmin() | [requireRole()](sync-function-api-require-role-cmd.md) | [requireUser()](sync-function-api-require-user-cmd.md) | [role()](sync-function-api-role-cmd.md) | [throw()](sync-function-api-throw-cmd.md)

Function

requireAdmin()

## [](#purpose)Purpose

Use the `requireAdmin()` function to reject document updates that are not made by the Sync Gateway Admin REST API.

## [](#arguments)Arguments

There are no arguments.

## [](#use)Use

Example 1\. requireadmin

```javascript
requireAdmin(); (1)
```

| **1** | Throw an exception unless the request is sent to the Admin REST API |
| ----- | ------------------------------------------------------------------- |

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Sync Function](#sync-function-overview.adoc)
* [Import filter](import-processing.md)

###### [](#-3)

Reference material …​

* [Public REST API](rest-api.md)
* [Admin REST API](rest-api-admin.md)
* [Metrics REST API](rest-api-metrics.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)