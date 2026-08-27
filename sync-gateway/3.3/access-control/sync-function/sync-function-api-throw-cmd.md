---
title: throw()
description: Rejecting a document change in Sync Gateway
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.3/modules/access-control/pages/sync-function/sync-function-api-throw-cmd.adoc
  xref: xref:3.3@sync-gateway:access-control:sync-function/sync-function-api-throw-cmd.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.3/access-control/sync-function/sync-function-api-throw-cmd.html)

# throw()

> Rejecting a document change in Sync Gateway  

_Related Topics_: [access()](sync-function-api-access-cmd.md) | [channel()](sync-function-api-channel-cmd.md) | [expiry()](sync-function-api-expiry-cmd.md) | [requireAccess()](sync-function-api-require-access-cmd.md) | [requireAdmin()](sync-function-api-require-admin-cmd.md) | [requireRole()](sync-function-api-require-role-cmd.md) | [requireUser()](sync-function-api-require-user-cmd.md) | [role()](sync-function-api-role-cmd.md) | [throw()](sync-function-api-throw-cmd.md)

Function

throw()

## [](#purpose)Purpose

Use `throw()` to prevent a document from persisting or syncing to any other users.

## [](#arguments)Arguments

No arguments

## [](#context)Context

You enforce the validity of document structure by checking the necessary constraints and throwing an exception if they're not met.

In validating a document, you'll often need to compare the new revision to the old one, to check for illegal changes in state. For example, some properties may be immutable after the document is created, or may be changeable only by certain users, or may only be allowed to change in certain ways. That's why the current document contents are given to the sync function, as the `oldDoc` parameter.

We recommend that you not create invalid documents in the first place. As much as possible, your app logic and validation function should prevent invalid documents from being created locally. The server-side sync function validation should be seen as a fail-safe and a guard against malicious access.

## [](#use)Use

Example 1\. throw(forbidden:)

In this example the sync function disallows all writes to the database it is in.

```javascript
function(doc) {

   throw({forbidden: "read only!"}) (1)

}
```

| **1** | The document update will be rejected with an HTTP 403 "Forbidden" error code, with the value of the forbidden: property being the HTTP status message.This is the preferred way to reject an update. |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

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