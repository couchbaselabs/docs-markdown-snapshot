---
title: Access Control Concepts
description: An introduction to the key concepts behind the provision of
  effective access control in Sync Gateway
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.2/modules/ROOT/pages/access-control-concepts.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/sync-gateway/3.2/access-control-concepts.html)

# Access Control Concepts

> An introduction to the key concepts behind the provision of effective access control in Sync Gateway  
> The sync function API provides several methods that you can use to validate and control user access to databases and documents.

_Related Concepts_: [Access Control Model](access-control-model.md) | [Channels](channels.md) | [Roles](roles.md) | [Sync Function](#sync-function-overview.adoc) | [Users](users.md)

## [](#lbl-access)Access Control Model

### [](#concept)Concept

You control document access by routing it to a channel and by making that channel accessible to the users or roles you want to be able to access documents of that type.

### [](#model)Model

In the Couchbase Mobile ecosystem access to documents is governed by three key entities: [users](users.md), [roles](roles.md) and [channels](channels.md).

Access Control Model

![Access](_images/access-control-triangle.png)

Conceptually, the _channel_ can be considered as a _tag_ associated with a document. Every document processed by the Sync Gateway is assigned to a channel (user-defined or system-defined). A channel is the fundamental way to segregate documents and for enforcing access control.

Every Sync Gateway user is granted access to zero, one or more channels. It is the channels membership that determines the documents users can access — as illustrated in [Access Control Model](#img-access-control-model)

A Sync Gateway role is a way of logically grouping users. Like the channel, a role is granted access to zero, one or more channels.

A user can only read documents that are in at least one of their assigned channels; whether directly or as part of an assigned role.

### [](#ex-sync-function-model)Sync Function Examples

Couchbase Sync Gateway defines a Sync Function at the `collection` level. Defining at this level helps simplify data management and improve data reliability. Each collection in the system allows for only one Sync Function, which enables the specification of Access Control rules.

Example 1\. Default Sync Function

```javascript
function (doc, oldDoc, meta) {
   channel(CollectionName);

}
```

Here the function then calls the `channel` and passes in the name of the collection `(CollectionsName)` as an argument.

By default, every document in the collection is automatically assigned to a channel with the same name as the collection. This system automatically creates a channel with the collection’s name. The assignment of all documents to the collection channel is functionally similar to assigning them to the [Star Channel](#2.7@sync-gateway-channels.adoc#star-channel).

To override this, use a custom sync function or a Specified Default Sync Function.

Example 2\. Upgraded Default Sync Function

```javascript
function (doc, oldDoc, meta) {
   channel(doc.channels);

}
```

Here is the default Sync Function when you have upgraded; it remains the same as the previous version.

### [](#context)Context

You control document access by routing it to a channel and by making that channel accessible to the users or roles you want to be able to access documents of that type.

#### [](#sync-gateway)Sync Gateway

All users can implicitly access any document in the public channel. In addition, there can be user-defined channels that users can be assigned to.

Once a user is granted access to a new channel, the next replication pull request from the client will retrieve all documents to which the user now has access.

Revoking access to a channel means that users who previously used the channel to get replicated documents will no longer see any synced updates.

Note that access grants neither confer, nor constrain, the **type** of access. Instead you can explicitly implement write access controls within the Sync Function; perhaps restricting updates to specific users or roles — for more on this see [Control Write Access](access-control-how-control-document-access.md).

#### [](#couchbase-lite)Couchbase Lite

By default, Couchbase Lite gets all the channels to which the configured user account has access. Optionally, a Couchbase Lite "pull" replication can also specify a comma-separated list of channel names to receive documents from. In this case, the replication from Sync Gateway will only pull documents tagged with those channels. Client apps can use this ability to intelligently sync with a subset of the available documents from the database.

### [](#lbl-access-revocation)Channel Access Revocation

> [!NOTE]
> 3.0 Breaking Change
> 
> Whenever a user loses access to a channel (or channels) all document in the channel(s) are auto-purged from local Couchbase Lite databases.  
> In _Sync Gateway_ 2.x these documents remain in the local database on channel access loss.

Users may lose access to documents for many reasons, including:

* The User loses direct access to channel
* The User is removed from a role
* A role the user belongs to is revoked access to channel

By default, when a user loses access to a channel, the next Couchbase Lite Pull replication auto-purges all documents in the channel from local Couchbase Lite databases (on devices belonging to the user) **unless** they belong to any of the user’s other channels — see: [Table 1](#tbl-sgw-behavior).

__Table 1\. Sync Gateway behavior following access revocation__
| System State     | Impact on Sync                                                                        |                                                                                                                                               |
| ---------------- | ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Replication Type | Access Control on Sync Gateway                                                        | Expected behavior (auto-purge enabled- default)                                                                                               |
| Pull only        | User revoked access to channel. Sync Function includes requireAccess(revokedChannel)  | Previously synced documents are auto purged on local                                                                                          |
| Push only        | User revoked access to channel. Sync Function includes requireAccess(revokedChannel)  | No impact of auto-purge Documents get pushed but will be rejected by Sync Gateway                                                             |
| Push-pull        | User revoked access to channel Sync Function includes requireAccess(revokedChannel)\` | Previously synced documents are auto purged on Couchbase Lite. Local changes continue to be pushed to remote but are rejected by Sync Gateway |

### [](#provisioning)Provisioning

* [Channel](channels.md) — the channels topic discusses how channels are created and how documents can be assigned to channels.
* [User](users.md) — the user topic discusses provisioning of users and providing users access to channels.
* [Role](roles.md) — the role topic discusses roles, assignment of users to roles created and providing roles access to channels.

## [](#lbl-channels)Channels

### [](#concept-2)Concept

Sync Gateway uses _Channels_ defined at collection level to make it easy to share a database’s documents across a large user base whilst retaining effective access control. They serve as a security conduit between the document and a user:

### [](#overview)Overview

Channels are defined at the collection level, which means that specific channels can be associated with individual collections of documents. This system allows users with access to a specific channel to access all documents assigned to that channel within that collection.

By defining channels at the collection level, it’s possible to implement detailed access control for different types of data within the database.

You typically will use channels to:

* Control who can access what
* Partition your data set
* Enable users to access just the documents they need
* Minimize the amount of data synced to mobile devices

Sync Gateway provides two special channels and a channel wildcard character.

### [](#ex-sync-function-examples)Sync Function Examples

Couchbase Sync Gateway defines a Sync Function at the `collection` level. Defining at this level helps simplify data management and improve data reliability. Each collection in the system allows for only one Sync Function, which enables the specification of Access Control rules.

Example 3\. Default Sync Function

```javascript
function (doc, oldDoc, meta) {
   channel(CollectionName);
}
```

Here the function then calls the `channel` and passes in the name of the collection `(CollectionsName)` as an argument.

By default, every document in the collection is automatically assigned to a channel with the same name as the collection. This system automatically creates a channel with the collection’s name. The assignment of all documents to the collection channel is functionally similar to assigning them to the [Star Channel](#2.7@sync-gateway-channels.adoc#star-channel).

To override this, use a custom sync function or a Specified Default Sync Function.

Example 4\. Upgraded Default Sync Function

```javascript
function (doc, oldDoc, meta) {
   channel(doc.channels);
}
```

Here is the default Sync Function when you have upgraded; it remains the same as the previous version.

### [](#lbl-usecase)Use Case

Imagine a database containing a collection of customer data. Within this collection, channels can be established to provide varying customer data access levels. For example, one channel may provide access to general customer information, while another may allow access to sensitive customer information. Users can then be granted access to one or both channels based on their need to access the associated data.

### [](#lbl-config)Configuration

* Version 3.x
* legacy

![Access Control Points 3.x](_images/channel-access-grant-3.0.png) 

| **1** | Using the Admin REST API:You can provide the admin\_channels property within the collection\_access property using the **Admin REST API** endpoint ([/{db}/\_user/{name}](rest%5Fapi%5Fadmin.md#tag/Database-Security/operation/put%5Fdb-%5Fuser-name)).                                                                                                                                                                                                                                        |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Programmatically using Access Grant Document:The [Sync Function](sync-function.md) provides a flexible and secure method for controlling document access and routing. You can program it to derive appropriate access and channel routing information from document properties.Optionally, the access grant can be specified via a designated extended attribute (XATTR) — see: [Use XATTRs for Access Grants](access-control-how-use-xattrs-for-access-grants.md) for how to define the XATTR. |

![Access Control Points pre 3.x](_images/channel-access-grant-pre3.0.png) 

| **1** | Using the Admin REST API : You can provide the admin\_channels property using the **Admin REST API** endpoint ([/{db}/\_user/{name}](rest%5Fapi%5Fadmin.md#tag/Database-Security/operation/put%5Fdb-%5Fuser-name)).                                                                                                                                                                                                               |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Programmatically using Access Grant Document: The [Sync Function](sync-function.md) provides a flexible and secure method for controlling document access and routing.You can program it to derive appropriate access and channel routing information from data embedded within document properties.                                                                                                                              |
| **3** | File-based Configuration Properties: This is only available in 3.x and is typically used for dev/test environments. You can do it in the Sync Gateway JSON Configuration File ([Database Configuration](configuration-schema-database.md) ) by adding the appropriate channel to the user’s admin\_channels property — see: [user admin\_channels](configuration-schema-database.md#database-users-this%5Fuser-admin%5Fchannels). |

### [](#lbl-syschan)System Channels

#### [](#lbl-public-channel)Public Channel

The [Public Channel](#lbl-public-channel) ('**!**') — is a channel for publicly available documents. It is ideal for use in making information available across the user community.

You assign a document to the _public_ (**!**) channel using the [channel()](sync-function-api-channel-cmd.md) function.

Documents assigned to this channel can be accessed by all users; even users assigned no specific channel access.

New users are automatically granted access to the channel.

#### [](#lbl-alldocs-channel)All Documents Channel

The [All Documents Channel](#lbl-alldocs-channel) ('**\***') \[[1](#%5Ffootnotedef%5F1 "View footnote.")\] — is a single, internal channel, comprising all documents from all channels.

Assignment to this channel is automatic and implicit. You cannot explicitly assign documents to the channel or remove documents from it.

This channel should not be confused with the use of the [All Channels Wildcard](#lbl-all-channels) in access grants.

#### [](#lbl-all-channels)All Channels Wildcard

The [All Channels Wildcard](#lbl-all-channels) ('**\***') — used when granting user access, this wildcard grants access to any document in any channel.

You make dynamic user access grants in the sync function using the [access()](sync-function-api-access-cmd.md) method.

Granting a user access with the _all channels_ wildcard gives them access to any channel, and any document in any channel, including those from private channels.

Replications by users with _all channels_ wildcard access will pull **all** documents. Because of this potential for syncing large volumes of data (sync pulls all documents in the bucket), users with _all channels_ wildcard access should use a channel filter to explicitly name the channel(s) to be sync’d.

**Note:** Users granted access using the _all channels_ wildcard **do not** inherit [requireAccess()](sync-function-api-require-access-cmd.md) rights to any specific channel.

> [!TIP]
> Always use a filter in conjunction with the _all channels_ wildcard, to avoid sync unnecessarily pulling large numbers of documents to mobile devices.

You assign documents to channels in the [Sync Function](sync-function.md).

Channels are created as documents are assigned to them.

Valid channel names consist of text letters \[`A–Z`, `a–z`\], digits \[`0–9`\], and a few special characters \[`= + / . , _ @`\]. Channel names are case-sensitive. Channels with no documents assigned to them are empty.

### [](#lbl-chan-limits)Channel Limits

__Table 2\. Guidance on Channel Assignment Limits__
| Element               | Limiting factor                                                                                                                                                                                                                                 | Guidance Limit (Channels) |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| Channels per document | The amount of memory consumed by the combined number of channels and access grants must fit within the maximum 1Mb xattr size limit — see: [Table 3](#tbl-metadata-size).                                                                       | 50                        |
| Channels per user     | The amount of memory consumed by channels must fit within the 20 MB available on Couchbase Server docs for storing metadata — see: [Table 3](#tbl-metadata-size)Note that the memory is retained for as long as the replication remains active. | 1,000                     |

### [](#lbl-metda-limits)Sync Metadata Limits

Every time a document is assigned to a new channel, the channel name is appended to that document’s sync metadata.

Therefore, a document’s set of channels is limited by the allowed sync metadata size described in [Table 3](#tbl-metadata-size).

__Table 3\. Size Limits for Sync Metadata__
| Value of enable\_shared\_bucket\_access | Size (Mb per Document) |
| --------------------------------------- | ---------------------- |
| false                                   | 20                     |
| true                                    | 1                      |

Sync Gateway will assign a document to a new channel as long as the sync metadata remains under the allowed limit.

**What to do when your channel count exceeds the usable space for sync metadata?**

In order to lower the sync metadata size per document, you can do one of the following:

* Lower the number of channels per document.
* Shorten the channel names. A shorter channel name will occupy less space ("customer==0030169303" vs "cs==0030169303").
* Lower the [revs\_limit](configuration-schema-database.md#database-revs%5Flimit) value. Indeed, a copy of channel metadata is retained for each revision of a document.

## [](#lbl-users)Users

### [](#concept-3)Concept

Users are one of the cornerstone concepts of access control. You can restrict document access to specific users and-or to users with specific roles.

As an entity a _user_ comprises a name, password, list of [Roles](roles.md) and a list of [Channels](channels.md).

### [](#lbl-sgw-users)Sync Gateway Users

Sync Gateway users and roles have no relationship to [Couchbase Server’s _RBAC (Role-based Access Control) users_](#lbl-rbac-users). They are created and operate solely within the _Sync Gateway_ ecosphere to govern access to replication data and to the Public API.

Granting access to a channel in Couchbase Sync Gateway allows users to access all documents assigned to that channel, which are part of specific collections. If granting users access to admin channels statically, it is necessary to specify both the corresponding collection and channel.

Users can also be assigned to zero or more [Roles](roles.md). A user inherits the channel access of all roles it belongs to. This is very much like Unix groups, except that roles do not form a hierarchy.

Sync Gateway user credentials can be used to authenticate access to the Public API; RBAC users are required for access to other API.

### [](#lbl-rbac-users)RBAC Users

Couchbase Server _RBAC user_ credentials are required to authenticate and authorize access to the Admin and Metrics API. You will need to create these users on Couchbase server in order to enable access — see: [Create RBAC users](get-started-prepare.md#step-2create-rbac-user) for how to and [Security Authorization Overview](../../server/current/learn/security/authorization-overview.md) for more on RBAC user authentication.

## [](#roles)Roles

### [](#concept-4)Concept

Roles are named collections of [Channels](channels.md). They enable the grouping together of [Users](users.md) with similar characteristics, which makes the management of large user populations easier.

A Role and a user assigned to a role is granted to access to a channel, which is associated with a specific collection. The user can then access all documents assigned to that channel. When granting user access to admin channels statically, the user must specify the collection and corresponding channel.

As an entity, roles comprise a name and a list of channels.

Any user associated with a role inherits the right to access any of the channels in the role’s list. This provides a convenient way to associate multiple channels with multiple users.

> [!TIP]
> Roles have a separate namespace from users, so it’s possible to have a user and a role with the same name.

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Sync Function](#sync-function-overview.adoc)
* [Import filter](import-processing.md)
* [Access Control](configuration-schema-access-control.md)
* [Add/Update Sync Function](rest%5Fapi%5Fadmin.md#tag/Database-Configuration/operation/put%5Fkeyspace-%5Fconfig-sync)
* [Sync Function Overview](#sync-function-overview.adoc)

###### [](#-3)

Reference material …​

* [Public REST API](rest-api.md)
* [Admin REST API](rest-api-admin.md)
* [Metrics REST API](rest-api-metrics.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)

Sync Function Blogs

* [Using roles in sync functions](https://blog.couchbase.com/augment-your-sync-function-with-roles-in-couchbase-sync-gateway/)
* [Tutorial: Getting Started with Data Synchronization using Couchbase Mobile for Offline-First Apps](https://blog.couchbase.com/data-synchronization-offline-first-apps-couchbase/)
* [Sync Function (category)](https://blog.couchbase.com/tag/sync-function/)

---

[1](#%5Ffootnoteref%5F1). Sometimes referred to as the **star** channel