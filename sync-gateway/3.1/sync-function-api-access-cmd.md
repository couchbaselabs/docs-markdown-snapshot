---
title: Access()
description: Enabling Sync Gateway data access
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.1/modules/ROOT/pages/sync-function-api-access-cmd.adoc
  xref: xref:3.1@sync-gateway::sync-function-api-access-cmd.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.1/sync-function-api-access-cmd.html)

# Access()

> Enabling Sync Gateway data access  

_Related Topics_: **access()** | [channel()](sync-function-api-channel-cmd.md) | [expiry()](sync-function-api-expiry-cmd.md) | [requireAccess()](sync-function-api-require-access-cmd.md) | [requireAdmin()](sync-function-api-require-admin-cmd.md) | [requireRole()](sync-function-api-require-role-cmd.md) | [requireUser()](sync-function-api-require-user-cmd.md) | [role()](sync-function-api-role-cmd.md) | [throw()](sync-function-api-throw-cmd.md)

Function

access(username, channelname)

## [](#purpose)Purpose

Use the `access()` function to grant a user access to a channel.

## [](#arguments)Arguments

| Argument | Description                                                                                                                                                                                                                                                           |
| -------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| username | Must be a string identifying a user, or an array of strings identifying multiple users; the function is applied to each user in the array. If the value resolves to null the function result is a no-op.                                                              |
| channels | Must be a string identifying a channel name, or an array of strings to specify multiple channel names (for example: (\['channel1', 'channel2'\]); the function is applied to each element in the array. If the value resolves to null the function result is a no-op. |

> [!NOTE]
> As a convenience, the resolved value of either argument may be `null` or `undefined`, in which case nothing happens.

## [](#context)Context

You can invoke this function multiple times from within your Sync Function.

> [!TIP]
> Prefix the `username` argument value with `role:` to apply this function to a role rather than a user. This grants access to the specified channel(s) for all users assigned that role.

The effects of all access calls by all active documents are effectively combined in a union, so if _any_ document grants a user access to a channel, that user has access to the channel.

You can use the _all channels_ wildcard ('**\***') to grant the user access to all documents in all channels.

## [](#use)Use

Example 1\. access(username, channel)

This example shows some valid ways to call `access()`:

```javascript
access ("jchris", "mtv"); (1)
access ("jchris", ["mtv", "mtv2", "vh1"]); (2)
access (["snej", "jchris", "role:admin"], "vh1"); (3)
access (["snej", "jchris"], ["mtv", "mtv2", "vh1"]); (4)
access (null, "hbo");  (5)
access ("snej", null);
```

| **1** | Allow access of single channel to single user       |
| ----- | --------------------------------------------------- |
| **2** | Allow access of multiple channels to single user    |
| **3** | Allow access of single channel to multiple users    |
| **4** | Allow access of multiple channels to multiple users |
| **5** | The null arguments mean these are treated as no-ops |

> [!WARNING]
> If you invoke the `access()` function multiple times to grant the same user access to the same channel, you could see negative performance effects, such as large fetches or request timeouts.

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