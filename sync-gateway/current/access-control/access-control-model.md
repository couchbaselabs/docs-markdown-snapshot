---
title: Access Control Model
description: An introduction to access control in Sync Gateway
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.0/modules/access-control/pages/access-control-model.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:sync-gateway:access-control:access-control-model.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/current/access-control/access-control-model.html)

# Access Control Model

> An introduction to access control in Sync Gateway  

_Related Concepts_: [Access Control Model](access-control-model.md) | [Channels](channels.md) | [Roles](roles.md) | [Sync Function](sync-function/sync-function.md) | [Users](users.md)

## [](#concept)Concept

You control document access by routing it to a channel and by making that channel accessible to the users or roles you want to be able to access documents of that type.

## [](#model)Model

In the Couchbase Mobile ecosystem access to documents is governed by three key entities: [users](users.md), [roles](roles.md) and [channels](channels.md).

Access Control Model

![Access](access-control-triangle.png)

Conceptually, the _channel_ can be considered as a _tag_ associated with a document. Every document processed by the Sync Gateway is assigned to a channel (user-defined or system-defined). A channel is the fundamental way to segregate documents and for enforcing access control.

Every Sync Gateway user is granted access to zero, one or more channels. It is the channels membership that determines the documents users can access — as illustrated in [Access Control Model](#img-access-control-model)

A Sync Gateway role is a way of logically grouping users. Like the channel, a role is granted access to zero, one or more channels.

A user can only read documents that are in at least one of their assigned channels; whether directly or as part of an assigned role.

## [](#ex-sync-function-model)Sync Function Examples

Couchbase Sync Gateway defines a Sync Function at the `collection` level. Defining at this level helps simplify data management and improve data reliability. Each collection in the system allows for only one Sync Function, which enables the specification of Access Control rules.

Example 1\. Default Sync Function

```javascript
function (doc, oldDoc, meta) {
   channel(CollectionName);

}
```

Here the function then calls the `channel` and passes in the name of the collection `(CollectionsName)` as an argument.

By default, every document in the collection is automatically assigned to a channel with the same name as the collection. This system automatically creates a channel with the collection’s name. The assignment of all documents to the collection channel is functionally similar to assigning them to the [All Documents Channel](access-control-concepts.md#lbl-alldocs-channel).

To override this, use a custom sync function or a Specified Default Sync Function.

Example 2\. Upgraded Default Sync Function

```javascript
function (doc, oldDoc, meta) {
   channel(doc.channels);

}
```

Here is the default Sync Function when you have upgraded; it remains the same as the previous version.

## [](#context)Context

You control document access by routing it to a channel and by making that channel accessible to the users or roles you want to be able to access documents of that type.

### [](#sync-gateway)Sync Gateway

All users can implicitly access any document in the public channel. In addition, there can be user-defined channels that users can be assigned to.

Once a user is granted access to a new channel, the next replication pull request from the client will retrieve all documents to which the user now has access.

Revoking access to a channel means that users who previously used the channel to get replicated documents will no longer see any synced updates.

Note that access grants neither confer, nor constrain, the **type** of access. Instead you can explicitly implement write access controls within the Sync Function; perhaps restricting updates to specific users or roles — for more on this see [Control Write Access](access-control-how-control-document-access.md).

### [](#couchbase-lite)Couchbase Lite

By default, Couchbase Lite gets all the channels to which the configured user account has access. Optionally, a Couchbase Lite "pull" replication can also specify a comma-separated list of channel names to receive documents from. In this case, the replication from Sync Gateway will only pull documents tagged with those channels. Client apps can use this ability to intelligently sync with a subset of the available documents from the database.

## [](#lbl-access-revocation)Channel Access Revocation

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

## [](#provisioning)Provisioning

* [Channel](channels.md) — the channels topic discusses how channels are created and how documents can be assigned to channels.
* [User](users.md) — the user topic discusses provisioning of users and providing users access to channels.
* [Role](roles.md) — the role topic discusses roles, assignment of users to roles created and providing roles access to channels.

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Sync Function](sync-function/sync-function.md)
* [Import filter](../sync/import-processing.md)

###### [](#-3)

Reference material …​

* [Public REST API](../rest-api/rest-api.md)
* [Admin REST API](../rest-api/rest-api-admin.md)
* [Metrics REST API](../rest-api/rest-api-metrics.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)