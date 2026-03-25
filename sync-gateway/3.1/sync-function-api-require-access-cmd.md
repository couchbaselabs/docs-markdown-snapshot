---
title: requireAccess()
description: Enabling Sync Gateway data access
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.1/modules/ROOT/pages/sync-function-api-require-access-cmd.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:3.1@sync-gateway::sync-function-api-require-access-cmd.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.1/sync-function-api-require-access-cmd.html)

# requireAccess()

> Enabling Sync Gateway data access  

_Related Topics_: [access()](sync-function-api-access-cmd.md) | [channel()](sync-function-api-channel-cmd.md) | [expiry()](sync-function-api-expiry-cmd.md) | requireAccess() | [requireAdmin()](sync-function-api-require-admin-cmd.md) | [requireRole()](sync-function-api-require-role-cmd.md) | [requireUser()](sync-function-api-require-user-cmd.md) | [role()](sync-function-api-role-cmd.md) | [throw()](sync-function-api-throw-cmd.md)

Function

requireAccess(channels)

## [](#purpose)Purpose

Use the `requireAccess()` function to reject document updates that are not made by the a user with access to at least one of the given channels, as shown in [Example 1](#ex-requireaccess)

## [](#arguments)Arguments

| Argument | Description                                                                                                                                                                                                                                                           |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| channels | Must be a string identifying a channel name, or an array of strings to specify multiple channel names (for example: (\['channel1', 'channel2'\]); the function is applied to each element in the array. If the value resolves to null the function result is a no-op. |

## [](#context)Context

The function signals rejection by throwing an exception, so the rest of the sync function will not be run.

Note that `requireAccess()` will only recognize grants made explicitly using a channel name (not by a wildcard).

So, if a user was granted access using only the [all channels wildcard](channels.md#lbl-all-channels)\] (`*`), then `requireAccess('anychannelname')'` will fail because the user wasn’t granted access to that channel (only to the `*` channel).

## [](#use)Use

Example 1\. requireAccess(channels)

```javascript
requireAccess("events"); (1)

if (oldDoc) {
    requireAccess(oldDoc.channels); (2)
}
```

| **1** | Throw an exception unless the user has access to read the "events" channel:                                   |
| ----- | ------------------------------------------------------------------------------------------------------------- |
| **2** | Throw an exception unless the user can read one of the channels in the previous revision’s channels property: |

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