---
title: Read Access
description: How to handle read-access
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/read-access.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.8@sync-gateway::read-access.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/read-access.html)

# Read Access

> How to handle read-access  
> The sync function API provides several methods that you can use to validate user access.

_Related access-control topics_: [Sync function](../current/access-control/sync-function/sync-function.md) | Read access | [Write access](#sync-gateway::{write-access-page})

## [](#introduction)Introduction

Every _user_ and _role_ has a set of channels that they are allowed to read.

A user can only read documents that are in at least one of the user’s channels (or the channels of roles that user has.)

After a user is granted access to a new channel, the changes feed incorporates all existing documents in that channel, even those from earlier sequences than the current request’s `since` parameter. That way the next pull request retrieves all documents to which the user now has access.

## [](#add-access)Add Access

User and-or role channel access can be assigned:

* Directly through the admin API
* In the configuration file
* Dynamically, in the Sync Function when a document is accessed

The Sync Function is the preferred method for granting access to channels programmatically.

### [](#sync-function)Sync Function

Calling [access(user, channel)](#{sgw-pg-def-sync-function}.adoc#accessusername-channelname) grants a user access to a channel. This allows documents to act as membership lists or access-control lists.

A typical example is a document that represents a shared resource (like a chat room or photo gallery) — see: [Example 1](#ex-helper).

Example 1\. Using the Access helper function

```javascript
function (doc) {
  if (doc.type == "chatroom") {  (1)
    access(doc.members, (2)
      doc.channel_id);  (3)
  }
}
```

In this example:

| **1** | A chat room is represented by a document with a type property set to chatroom.                        |
| ----- | ----------------------------------------------------------------------------------------------------- |
| **2** | The channel\_id property names the associated channel, with which the actual chat messages are tagged |
| **3** | The members property lists the users who have access to that channel.                                 |

The `access()` function can also operate on roles. If a user name string begins with `role:` then the remainder of the string is interpreted as a role name. There’s no ambiguity here, because ":" is an illegal character in a user or role name.

Because anonymous requests are authenticated as the user "GUEST", you can make a channel and its documents public by calling `access` with a username of `GUEST`.

### [](#configuration-file)Configuration File

A user can be granted access to a channel through the [admin\_channels](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-users-this%5Fuser-admin%5Fchannels) property in the configuration file.

### [](#admin-rest-api)Admin REST API

A user can be granted access to a channel through the `admin_channels` property on the [/{db}/user/{name}](../current/rest-api/rest-api-admin.md#/user/put%5F%5Fdb%5F%5F%5Fuser%5F%5Fname%5F) admin REST API endpoint.

## [](#revoke-access)Revoke Access

Revoking access to a channel can cause a user to lose access to documents, if s/he no longer has access to any channels those documents are in.

However, the replicator does _not_ currently delete such documents that have already been synced to a user’s device (although future changes to those documents will not be replicated.) This is a design limitation of Sync Gateway that may be resolved in the future.

* A GET request to a document not assigned to one or more of the user’s available channels fails with a 403 error.
* The `_all_docs` property is filtered to return only documents that are visible to the user.
* The `_changes` property ignores requests (via the `channels` parameter) for channels not visible to the user.

## [](#inspect-read-access)Inspect Read Access

You can use the admin REST API to see what channels a user has access to. Issue an [/{db}/\_user/{name}](../current/rest-api/rest-api-admin.md#/database/get
%5F%5Fdb%5F%5F%5Fall%5Fdocs) request. Here’s an example of the response. The output shows that the user `pupshaw` has access to channels `all` and `hoopy`.

```json
{
    "admin_channels": [
        "all"
    ],
    "admin_roles": [
        "froods"
    ],
    "all_channels": [
        "all",
        "hoopy"
    ],
    "name": "pupshaw",
    "roles": [
        "froods"
    ]
}
```

The `all_channels` property of a user account determines which channels the user can access. Its value is derived from the union of:

* The user’s `admin_channels` property, which is settable via the admin REST API.
* The channels that user has been given access to by `access()` calls from sync functions invoked for current revisions of documents.
* The `all_channels` properties of all roles the user belongs to, which are themselves computed according to the above two rules.

## [](#replication)Replication

By default, Couchbase Lite gets all the channels to which the configured user account has access. This behavior is suitable for most apps that rely on [User Authentication](../current/security/authentication-users.md) and the [Sync Function](../current/access-control/sync-function/sync-function.md) to specify which data to pull for each user.

Optionally, a Couchbase Lite "pull" replication can also specify a comma-separated list of channel names to receive documents from. In this case, the replication from Sync Gateway will only pull documents tagged with those channels. Client apps can use this ability to intelligently sync with a subset of the available documents from the database.

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