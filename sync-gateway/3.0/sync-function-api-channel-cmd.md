---
title: channel()
description: Assigning Sync Gateway <em>channels</em>
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.0/modules/ROOT/pages/sync-function-api-channel-cmd.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:3.0@sync-gateway::sync-function-api-channel-cmd.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.0/sync-function-api-channel-cmd.html)

# channel()

> Assigning Sync Gateway _channels_  

_Related Topics_: [access()](sync-function-api-access-cmd.md) | channel() | [expiry()](sync-function-api-expiry-cmd.md) | [requireAccess()](sync-function-api-require-access-cmd.md) | [requireAdmin()](sync-function-api-require-admin-cmd.md) | [requireRole()](sync-function-api-require-role-cmd.md) | [requireUser()](sync-function-api-require-user-cmd.md) | [role()](sync-function-api-role-cmd.md) | [throw()](sync-function-api-throw-cmd.md)

## [](#function-call)Function Call

channel(channelname)

## [](#purpose)Purpose

Use the `channel()` function to route the document to the named channel(s).

## [](#arguments)Arguments

| Argument | Description                                                                                                                                                                                                                                                           |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| channels | Must be a string identifying a channel name, or an array of strings to specify multiple channel names (for example: (\['channel1', 'channel2'\]); the function is applied to each element in the array. If the value resolves to null the function result is a no-op. |

## [](#context)Context

The channel function can be called zero or more times from the sync function, for any document.

> [!NOTE]
> Channels don’t have to be predefined.  
> A channel implicitly comes into existence when a document is routed to it.

Routing changes have no effect until the document is actually saved in the database, so if the sync function first calls `channel()` or `access()`, but then rejects the update, the channel and access changes will not occur.

> [!TIP]
> As a convenience, it is legal to call `channel` with a `null` or `undefined` argument; it simply does nothing.  
> This allows you to do something like `channel(doc.channels)` without having to first check whether `doc.channels` exists.

## [](#use)Use

Example 1\. channel(channelname)

This example routes all "published" documents to the "public" channel:

```javascript
function (doc, oldDoc, meta) {
   if (doc.published) {
      channel("public");
   }
}
```

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