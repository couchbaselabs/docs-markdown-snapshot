---
title: Channels
description: About Sync Gateway <em>Channels</em> and their part in data routing
  and access control for secure cloud-to-edge enterprise data synchronization.
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.0/modules/ROOT/pages/channels.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.0@sync-gateway::channels.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.0/channels.html)

# Channels

> About Sync Gateway _Channels_ and their part in data routing and access control for secure cloud-to-edge enterprise data synchronization.  

_Related Concepts_: [Access Control Model](access-control-model.md) | Channels | [Roles](roles.md) | [Sync Function](sync-function-overview.md) | [Users](users.md)

## [](#concept)Concept

Sync Gateway uses _Channels_ to make it easy to share a database's documents across a large user base whilst retaining effective access control. They serve as a security conduit between the document and a user:

## [](#overview)Overview

Every document in the database is assigned a list of channels it is distributed to. Every user (or role) is granted access to a list of channels. This dual-purpose is reflected in the way you use channels:

* By granting a user access to a channel, you are imposing access control
* By assigning a document to a channel you are imposing document routing

You typically will use channels to:

* Control who can access what
* Partition your data set
* Enable users to access just the documents they need
* Minimize the amount of data synced to mobile devices

Sync Gateway provides two special channels and a channel wildcard character.

## [](#lbl-usecase)Use Case

Consider the case where two users require, and are allowed, access to a private set of documents and one shared set of documents — see [Figure 1](#fig-channel-example).

![Access Control using Channels](_images/channels-example-all.png) 

Figure 1\. Channels in Access Control

In this case, each user is assigned to a private channel with a subset of documents that only the user can access and a shared channel that contains common documents. The users in this example could be replaced by roles.

An example of this model could be a retail chain, where every store corresponds to a Sync Gateway User. Each store has a store specific channel that contains documents that are store specific like pricing, promotions, inventory etc. In addition, all the stores may need to have access to a common set of documents like retail locations, product catalog that are stored in a common shared channel.

## [](#lbl-config)Configuration

* Version 3.x
* legacy

![Access Control Points 3.x](_images/channel-access-grant-3.0.png) 

| **1** | Using the Admin REST API:You can provide the admin\_channels property using the **Admin REST API** endpoint ([/{db}/\_user/{name}](rest-api-admin.md#/user/post\%5F%5Fdb%5F%5F%5Fuser%5Fname%5F)).                                                                                                                                                                                                                                                                                              |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Programmatically using Access Grant Document:The [Sync Function](sync-function.md) provides a flexible and secure method for controlling document access and routing. You can program it to derive appropriate access and channel routing information from document properties.Optionally, the access grant can be specified via a designated extended attribute (XATTR) — see: [Use XATTRs for Access Grants](access-control-how-use-xattrs-for-access-grants.md) for how to define the XATTR. |

![Access Control Points pre 3.x](_images/channel-access-grant-pre3.0.png) 

| **1** | Using the Admin REST API : You can provide the admin\_channels property using the **Admin REST API** endpoint ([/{db}/\_user/{name}](rest-api-admin.md#/user/post\%5F%5Fdb%5F%5F%5Fuser%5Fname%5F)).                                                                                                                                                                                                                              |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Programmatically using Access Grant Document: The [Sync Function](sync-function.md) provides a flexible and secure method for controlling document access and routing.You can program it to derive appropriate access and channel routing information from data embedded within document properties.                                                                                                                              |
| **3** | File-based Configuration Properties: This is only available in 3.x and is typically used for dev/test environments. You can do it in the Sync Gateway JSON Configuration File ([Database Configuration](configuration-schema-database.md) ) by adding the appropriate channel to the user's admin\_channels property — see: [user admin\_channels](configuration-schema-database.md#database-users-this%5Fuser-admin%5Fchannels). |

## [](#lbl-syschan)System Channels

### [](#lbl-public-channel)Public Channel

The [Public Channel](#lbl-public-channel) ('**!**') — is a channel for publicly available documents. It is ideal for use in making information available across the user community.

You assign a document to the _public_ (**!**) channel using the [channel()](sync-function-api-channel-cmd.md) function.

Documents assigned to this channel can be accessed by all users; even users assigned no specific channel access.

New users are automatically granted access to the channel.

### [](#lbl-alldocs-channel)All Documents Channel

The [All Documents Channel](#lbl-alldocs-channel) ('**\***') \[[1](#%5Ffootnotedef%5F1 "View footnote.")\] — is a single, internal channel, comprising all documents from all channels.

Assignment to this channel is automatic and implicit. You cannot explicitly assign documents to the channel or remove documents from it.

This channel should not be confused with the use of the [All Channels Wildcard](#lbl-all-channels) in access grants.

### [](#lbl-all-channels)All Channels Wildcard

The [All Channels Wildcard](#lbl-all-channels) ('**\***') — used when granting user access, this wildcard grants access to any document in any channel.

You make dynamic user access grants in the sync function using the [access()](sync-function-api-access-cmd.md) method.

Granting a user access with the _all channels_ wildcard gives them access to any channel, and any document in any channel, including those from private channels.

Replications by users with _all channels_ wildcard access will pull **all** documents. Because of this potential for syncing large volumes of data (sync pulls all documents in the bucket), users with _all channels_ wildcard access should use a channel filter to explicitly name the channel(s) to be sync'd.

**Note:** Users granted access using the _all channels_ wildcard **do not** inherit [requireAccess()](sync-function-api-require-access-cmd.md) rights to any specific channel.

> [!TIP]
> Always use a filter in conjunction with the _all channels_ wildcard, to avoid sync unnecessarily pulling large numbers of documents to mobile devices.

You assign documents to channels in the [Sync Function](sync-function.md).

Channels are created as documents are assigned to them.

Valid channel names consist of text letters \[`A–Z`, `a–z`\], digits \[`0–9`\], and a few special characters \[`= + / . , _ @`\]. Channel names are case-sensitive. Channels with no documents assigned to them are empty.

## [](#lbl-chan-limits)Channel Limits

__Table 1\. Guidance on Channel Assignment Limits__
| Element               | Limiting factor                                                                                                                                                                                                                                 | Guidance Limit (Channels) |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| Channels per document | The amount of memory consumed by the combined number of channels and access grants must fit within the maximum 1Mb xattr size limit — see: [Table 2](#tbl-metadata-size).                                                                       | 50                        |
| Channels per user     | The amount of memory consumed by channels must fit within the 20 MB available on Couchbase Server docs for storing metadata — see: [Table 2](#tbl-metadata-size)Note that the memory is retained for as long as the replication remains active. | 1,000                     |

## [](#lbl-metda-limits)Sync Metadata Limits

Every time a document is assigned to a new channel, the channel name is appended to that document's sync metadata.

Therefore, a document's set of channels is limited by the allowed sync metadata size described in [Table 2](#tbl-metadata-size).

__Table 2\. Size Limits for Sync Metadata__
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

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Sync Function](sync-function-overview.md)
* [Import filter](import-filter.md)
* [Access Control](configuration-schema-access-control.md)
* [Add/Update Sync Function](#rest-api-admin.html#/Access%5FControl/update%5Fsync%5Ffunction)
* [Sync Function Overview](sync-function-overview.md)

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