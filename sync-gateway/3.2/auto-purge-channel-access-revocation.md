---
title: Auto-Purge on Channel Access Revocation
description: Auto-purge behavior on loss of access to document channels
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.2/modules/ROOT/pages/auto-purge-channel-access-revocation.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:3.2@sync-gateway::auto-purge-channel-access-revocation.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.2/auto-purge-channel-access-revocation.html)

# Auto-Purge on Channel Access Revocation

> Auto-purge behavior on loss of access to document channels  

_Related Topics_: [Concepts](access-control-concepts.md) | [How-to](access-control-how.md) | [Sync Function](#sync-function-overview.adoc) | [Use XATTRs for Access Grants](access-control-how-use-xattrs-for-access-grants.md)

## [](#overview)Overview

Users may lose access to documents for many reasons, including:

* The User loses direct access to channel
* The User is removed from a role
* A role the user belongs to is revoked access to channel

Sync Gateway will take the configured action whenever this happens. By default:

* Sync Gateway syncs will auto-purge documents the user has lost access to — see [Sync Gateway](#lbl-sgw-cbl)
* Inter-Sync Gateway replications will not auto-purge documents the user has lost access to — [Inter-Sync Gateway](#lbl-isgr)

## [](#lbl-sgw-cbl)Sync Gateway

> [!CAUTION]
> Breaking Change
> 
> In _Sync Gateway_ 2.x these documents remain in the local database on channel access loss.

By default, when a user loses access to a channel, the next Couchbase Lite Pull replication auto-purges all documents in the channel from local Couchbase Lite databases (on devices belonging to the user) **unless** they belong to any of the user’s other channels — see: [Couchbase Lite Replication — Auto Purge on Channel Access Revocation](../../couchbase-lite/current/android/replication.md#anchor-auto-purge-on-revoke).

## [](#lbl-isgr)Inter-Sync Gateway

### [](#access-revoked)Access Revoked

> [!NOTE]
> This behavior is the **reverse** of that between Sync Gateway and Couchbase Lite — see: [Sync Gateway](#lbl-sgw-cbl).

By default, documents are **not** auto purged on the active sync gateway even if the user on the passive sync gateway loses channel access.

You can opt-in to auto-purge behavior using the replicator level option `purge_on_removal` in the REST API — see: [replication-purge\_on\_removal](configuration-schema-isgr.md#replication-purge%5Fon%5Fremoval).

Documents will then **be** auto-purged — on active Sync Gateway nodes that have opted-in — if they do not belong to **any** of the replicating user’s \[[1](#%5Ffootnotedef%5F1 "View footnote.")\] channels — see: [Example 1](#lbl-isgr-revoke-behaviors).

If you turn it on during an existing replication, **no** revocations occurring prior to that point are retro-actively purged. To have this done, execute a reset for ISGR (on Couchbase Lite a reset checkpoint must be carried out).

Example 1\. Access Revocation behavior

Access control policies are only enforced at the remote cluster.

Here the Active Sync Gateway (Local) is running as an admin user with `purge_on_removal=true`

| Direction   | Passive Sync Gateway (Remote)                                                 | Expected Sync behavior                                                                                                                                                     |
| ----------- | ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pull        | User revoked access to channel                                                | Previously synced documents are auto purged on local                                                                                                                       |
| Push        | User revoked access to channel                                                | Revocation has no impact during a 'push'. No purging will occur.                                                                                                           |
| PushAndPull | User revoked access to channelSync Function includes requireAccess(“channel”) | When access is revoked on remote, the previously synced documents for User2 are auto-purged on local. Local changes continue to be pushed to remote but rejected by remote |

### [](#access-regained)Access Regained

If a user subsequently regains access to a lost channel then any previously auto-purged documents still assigned to any of their channels are automatically pulled down by the active Sync Gateway — see: [Example 2](#lbl-isgr-regain-behaviors).

If you want to control whether to sync previous auto purged versions of documents (rather than pull down purged documents) then you must also move the documents out of all of the users' channels so they are not synced down again.

Example 2\. Access Regained behavior

Access control policies are only enforced at the remote cluster.

Here the Active Sync Gateway (Local) is running as an admin user with `purge_on_removal=true`

| Direction   | Passive Sync Gateway (Remote)                                                              | Expected Sync behavior                                                                                                                                                                                                                          |
| ----------- | ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pull        | User REASSIGNED access to channel Sync Function includes requireAccess( reassignedChannel) | Previously purged documents are automatically pulled by local                                                                                                                                                                                   |
| Push        | User REASSIGNED access to channel Sync Function includes requireAccess(“channel”)          | Config option has no impact. Local changes previously rejected by remote are pushed again with reset action on replicator. Subsequent changes to previously rejected documents are automatically pushed up.                                     |
| PushAndPull | User REASSIGNED access to channel Sync Function includes requireAccess(“channel”)          | Documents auto purged on local are automatically pulled again Local changes previously rejected by remote can be pushed again with reset action on replicator. Subsequent changes to previously rejected documents are automatically pushed up. |

## [](#ex-sync-function-auto-purge)Sync Function Examples

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

[1](#%5Ffootnoteref%5F1). The _replicating user_ is the user on the _passive_ sync gateway cluster; the user specified in the replication definition.