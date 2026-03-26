---
title: Write Security
description: How to manage write-access in Sync Gateway to ensure secure
  cloud-to-edge synchronization of enterprize data.
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/write-access.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.8@sync-gateway::write-access.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/write-access.html)

# Write Security

> How to manage write-access in Sync Gateway to ensure secure cloud-to-edge synchronization of enterprize data.  
> The Sync Function API provides several methods that you can use to validate document creation, updates and deletions.

_Related access-control topics_: [Sync function](../current/access-control/sync-function/sync-function.md) | [Read access](#sync-gateway::read-access.adoc) | [Write access](#sync-gateway::{write-access-page})

## [](#introduction)Introduction

You should use the _Sync Function_ to validate any changes and to authorize document writes.

## [](#access-old-document)Access Old Document

Before you can validate a document update, you often need to know which user is changing it, and sometimes you need to compare the old and new revisions. The Sync Function makes it easy to access any pre-revision document content — see [Example 1](#ex-old-doc):

Example 1\. Access Pre-revision Document Content\]

```javascript
function(doc, oldDoc) { ... } (1)
```

| **1** | Here in the Sync Function header, the oldDoc contains the document content prior to any changes. It is empty if this is a new document. |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------- |

## [](#validate-document-changes)Validate Document Changes

For document schema validation, you can write your own rules in the Sync Function. Use it to validate any document changes made before writing them.

When a document is deemed invalid, you can simply call the built-in JavaScript [throw()](sync-function.md#throw) function to raise an exception and reject the revision — see [Example 2](#ex-reject).

Rejected documents are not saved to the Sync Gateway database, so no access changes take effect. Instead an error code (usually 403 Forbidden) is returned to Couchbase Lite's replicator.

Any other exception (including implicit ones thrown by the JavaScript runtime, like array bounds exceptions) will also prevent the document update. These will cause the gateway to return an HTTP `500 — Internal Error` status.

Example 2\. Rejecting Invalid Documents

```javascript
throw ({forbidden: "error message"}) (1)
```

| **1** | A 403 — Forbidden status and the given error string is returned to the client. |
| ----- | ------------------------------------------------------------------------------ |

## [](#check-for-write-access)Check for Write Access

Use the Sync Function's helper functions such as [requireUser()](sync-function.md#requireuserusername) or [requireRole()](sync-function.md#requirerolerolename) to specify the user(s) allowed to write a document — see [Example 3](#ex-check-write-access)

Example 3\. Checking the User to Allow Write Access

In this example, our simple Sync Function validates whether the user modifying a document is a valid owner by checking if they are recorded as an owner of the old document:

```javascript
function (doc, oldDoc) {
  if (oldDoc) {
    requireUser(oldDoc.owner); // may throw({forbidden: "wrong user"})
  }
}
```

If the user or role making the change is not in that list, an exception is thrown and the update is rejected with an error.

Similarly, [requireAccess()](sync-function.md#requireaccesschannels) requires that the user making the change has access to any of the listed channels — see [Example 4](#ex-helpers) for more helper function usage.

> [!NOTE]
> The Sync Function executes with admin privileges for changes made using the [Admin REST API](../current/rest-api/rest-api-admin.md). So, `requireUser`, `requireAccess` and `requireRole` are no-ops; they will always be successful.

Example 4\. Helper Function examples

This example shows how to use some of the helper functions:

```javascript
requireUser("snej") (1)

requireUser(["snej", "jchris", "tleyden"]) (2)

requireRole("admin") (3)

requireRole(["admin", "old-timer"]) (4)

requireAccess("events") (5)

requireAccess(["events", "messages"]) (6)
```

| **1** | throw an error if username is not "snej"                               |
| ----- | ---------------------------------------------------------------------- |
| **2** | throw if username is not in the list                                   |
| **3** | throw an error unless the user has the "admin" role                    |
| **4** | throw an error unless the user has one of those roles                  |
| **5** | throw an error unless the user has access to read the "events" channel |
| **6** | throw an error unless the can read one of these channels               |

When sending a change to Sync Gateway through the [Admin REST API](../current/rest-api/rest-api-admin.md), the Sync Function is executed with admin privileges: calls to `requireUser`, `requireAccess` and `requireRole` are no-ops (that is, they will always be successful).

> [!TIP]
> To create and manage user accounts, refer to [Users](../current/access-control/users.md).

## [](#related-content)Related Content

###### [](#)

Learn more …​

* [Sync Function](../current/access-control/sync-function/sync-function.md)
* [Import filter](../current/sync/import-processing.md)
* [Inter-Sync Gateway Replication](../current/sync/sync-inter-syncgateway-overview.md)
* [Sync with Couchbase Server](../current/sync/sync-with-couchbase-server.md)

###### [](#-2)

Reference material …​

* [Public REST API](../current/rest-api/rest-api.md)
* [Admin REST API](../current/rest-api/rest-api-admin.md)
* [Metrics REST API](../current/rest-api/rest-api-metrics.md)
* [Use the REST API?](#sync-gateway::rest-api-client-app.adoc)

###### [](#-3)

Community

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)

Sync Function Blogs

* [Using roles in sync functions](https://blog.couchbase.com/augment-your-sync-function-with-roles-in-couchbase-sync-gateway/)
* [Tutorial: Getting Started with Data Synchronization using Couchbase Mobile for Offline-First Apps](https://blog.couchbase.com/data-synchronization-offline-first-apps-couchbase/)
* [Sync Function (category)](https://blog.couchbase.com/tag/sync-function/)