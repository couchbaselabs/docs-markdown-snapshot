---
title: Channels
description: About Sync Gateway <em>Channels</em> and their part in data routing
  and access control for secure cloud-to-edge enterprise data synchronization.
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.3/modules/access-control/pages/channels.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/sync-gateway/3.3/access-control/channels.html)

# Channels

> About Sync Gateway _Channels_ and their part in data routing and access control for secure cloud-to-edge enterprise data synchronization.  

_Related Concepts_: [Access Control Model](access-control-model.md) | [Channels](channels.md) | [Roles](roles.md) | [Sync Function](sync-function/sync-function.md) | [Users](users.md)

## [](#concept)Concept

Sync Gateway uses _Channels_ defined at collection level to make it easy to share a database’s documents across a large user base whilst retaining effective access control. They serve as a security conduit between the document and a user:

## [](#overview)Overview

Channels are defined at the collection level, which means that specific channels can be associated with individual collections of documents. This system allows users with access to a specific channel to access all documents assigned to that channel within that collection.

By defining channels at the collection level, it’s possible to implement detailed access control for different types of data within the database.

You typically will use channels to:

* Control who can access what
* Partition your data set
* Enable users to access just the documents they need
* Minimize the amount of data synced to mobile devices

Sync Gateway provides two special channels and a channel wildcard character.

## [](#ex-sync-function-examples)Sync Function Examples

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

## [](#lbl-usecase)Use Case

Imagine a database containing a collection of customer data. Within this collection, channels can be established to provide varying customer data access levels. For example, one channel may provide access to general customer information, while another may allow access to sensitive customer information. Users can then be granted access to one or both channels based on their need to access the associated data.

## [](#lbl-config)Configuration

* Version 3.x
* legacy

![Access Control Points 3.x](../_images/channel-access-grant-3.0.png) 

| **1** | Using the Admin REST API:You can provide the admin\_channels property within the collection\_access property using the **Admin REST API** endpoint ([/{db}/\_user/{name}](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Security/operation/put%5Fdb-%5Fuser-name)).                                                                                                                                                                                                                                          |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Programmatically using Access Grant Document:The [Sync Function](sync-function/sync-function.md) provides a flexible and secure method for controlling document access and routing. You can program it to derive appropriate access and channel routing information from document properties.Optionally, the access grant can be specified via a designated extended attribute (XATTR) — see: [Use XATTRs for Access Grants](access-control-how-use-xattrs-for-access-grants.md) for how to define the XATTR. |

![Access Control Points pre 3.x](../_images/channel-access-grant-pre3.0.png) 

| **1** | Using the Admin REST API : You can provide the admin\_channels property using the **Admin REST API** endpoint ([/{db}/\_user/{name}](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Security/operation/put%5Fdb-%5Fuser-name)).                                                                                                                                                                                                                                     |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Programmatically using Access Grant Document: The [Sync Function](sync-function/sync-function.md) provides a flexible and secure method for controlling document access and routing.You can program it to derive appropriate access and channel routing information from data embedded within document properties.                                                                                                                                                  |
| **3** | File-based Configuration Properties: This is only available in 3.x and is typically used for dev/test environments. You can do it in the Sync Gateway JSON Configuration File ([Database Configuration](../configuration/configuration-schema-database.md) ) by adding the appropriate channel to the user’s admin\_channels property — see: [user admin\_channels](../configuration/configuration-schema-database.md#database-users-this%5Fuser-admin%5Fchannels). |

## [](#lbl-syschan)System Channels

### [](#lbl-public-channel)Public Channel

The [Public Channel](#lbl-public-channel) ('**!**') — is a channel for publicly available documents. It is ideal for use in making information available across the user community.

You assign a document to the _public_ (**!**) channel using the [channel()](sync-function/sync-function-api-channel-cmd.md) function.

Documents assigned to this channel can be accessed by all users; even users assigned no specific channel access.

New users are automatically granted access to the channel.

### [](#lbl-alldocs-channel)All Documents Channel

The [All Documents Channel](#lbl-alldocs-channel) ('**\***') \[[1](#%5Ffootnotedef%5F1 "View footnote.")\] — is a single, internal channel, comprising all documents from all channels.

Assignment to this channel is automatic and implicit. You cannot explicitly assign documents to the channel or remove documents from it.

This channel should not be confused with the use of the [All Channels Wildcard](#lbl-all-channels) in access grants.

### [](#lbl-all-channels)All Channels Wildcard

The [All Channels Wildcard](#lbl-all-channels) ('**\***') — used when granting user access, this wildcard grants access to any document in any channel.

You make dynamic user access grants in the sync function using the [access()](sync-function/sync-function-api-access-cmd.md) method.

Granting a user access with the _all channels_ wildcard gives them access to any channel, and any document in any channel, including those from private channels.

Replications by users with _all channels_ wildcard access will pull **all** documents. Because of this potential for syncing large volumes of data (sync pulls all documents in the bucket), users with _all channels_ wildcard access should use a channel filter to explicitly name the channel(s) to be sync’d.

**Note:** Users granted access using the _all channels_ wildcard **do not** inherit [requireAccess()](sync-function/sync-function-api-require-access-cmd.md) rights to any specific channel.

> [!TIP]
> Always use a filter in conjunction with the _all channels_ wildcard, to avoid sync unnecessarily pulling large numbers of documents to mobile devices.

You assign documents to channels in the [Sync Function](sync-function/sync-function.md).

Channels are created as documents are assigned to them.

Valid channel names consist of text letters \[`A–Z`, `a–z`\], digits \[`0–9`\], and a few special characters \[`= + / . , _ @`\]. Channel names are case-sensitive. Channels with no documents assigned to them are empty.

## [](#lbl-chan-limits)Channel Limits

__Table 1\. Guidance on Channel Assignment Limits__
| Element               | Limiting factor                                                                                                                                                                                                                                 | Guidance Limit (Channels) |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| Channels per document | The amount of memory consumed by the combined number of channels and access grants must fit within the maximum 1Mb xattr size limit — see: [Table 2](#tbl-metadata-size).                                                                       | 50                        |
| Channels per user     | The amount of memory consumed by channels must fit within the 20 MB available on Couchbase Server docs for storing metadata — see: [Table 2](#tbl-metadata-size)Note that the memory is retained for as long as the replication remains active. | 1,000                     |

## [](#lbl-metda-limits)Sync Metadata Limits

Every time a document is assigned to a new channel, the channel name is appended to that document’s sync metadata.

Therefore, a document’s set of channels is limited by the allowed sync metadata size described in [Table 2](#tbl-metadata-size).

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
* Lower the [revs\_limit](../configuration/configuration-schema-database.md#database-revs%5Flimit) value. Indeed, a copy of channel metadata is retained for each revision of a document.

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Sync Function](sync-function/sync-function.md)
* [Import filter](../sync/import-processing.md)
* [Access Control](../configuration/configuration-schema-access-control.md)
* [Add/Update Sync Function](../rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Configuration/operation/put%5Fkeyspace-%5Fconfig-sync)
* [Sync Function Overview](sync-function/sync-function.md)

###### [](#-3)

Reference material …​

* [Public REST API](../rest-api/rest-api.md)
* [Admin REST API](../rest-api/rest-api-admin.md)
* [Metrics REST API](../rest-api/rest-api-metrics.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)

Sync Function Blogs

* [Using roles in sync functions](https://blog.couchbase.com/augment-your-sync-function-with-roles-in-couchbase-sync-gateway/)
* [Tutorial: Getting Started with Data Synchronization using Couchbase Mobile for Offline-First Apps](https://blog.couchbase.com/data-synchronization-offline-first-apps-couchbase/)
* [Sync Function (category)](https://blog.couchbase.com/tag/sync-function/)

---

[1](#%5Ffootnoteref%5F1). Sometimes referred to as the **star** channel