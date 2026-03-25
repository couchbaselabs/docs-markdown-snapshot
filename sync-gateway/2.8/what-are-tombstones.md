---
title: Tombstones
description: About Sync Gateway <em>Tombstones</em>.
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/what-are-tombstones.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.8@sync-gateway::what-are-tombstones.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/what-are-tombstones.html)

# Tombstones

> About Sync Gateway _Tombstones_.  
> Here we introduce the concept of _Tombstones_ and their role in the _Sync Gateway_ revision process.

_Related concepts topics_: [Users](../current/access-control/users.md) | [Roles](../current/access-control/roles.md) | [Channels](../current/access-control/channels.md) | [Revisions](../current/manage/revisions.md) | Tombstones

## [](#what-tombstones-are)What tombstones are

A _tombstone_ is a persistent record that an item has been deleted.

Sync Gateway creates tombstones to ensure all synchronizing devices can identify that a previously existing document has now been deleted, this is particularly necessary in the case of devices that may not be online continuously and therefore not syncing regularly.

The actual tombstone artifact is a document revision comprising only:

* the (deleted) document ID
* a revision ID
* a key value pair `deleted:true`.

Example tombstone artefact

```json
{
  "_deleted": true,
  "_id": "foobar",
  "_rev": "3-db962c6d93c3f1720cc7d3b6e50ac9df"
}
```

## [](#the-tombstone-lifecycle)The tombstone lifecycle

The storage location of tombstones differs slightly depending on whether the Shared Bucket Access feature is enabled (`enable_shared_bucket_access: true`).

The table below describes those differences.

| enable\_shared\_bucket\_access: false           | enable\_shared\_bucket\_access: true                    |
| ----------------------------------------------- | ------------------------------------------------------- |
| **Mobile metadata storage location**            |                                                         |
| Persisted on the document (doc.\_sync)          | Persisted as system extended attributes (xattr.\_sync)  |
| **Tombstone storage location**                  |                                                         |
| Persisted on the document                       | Persisted as system extended attributes (xattr.\_sync). |
| **Additional user properties on a tombstone**   |                                                         |
| Persisted on the document                       | **Not persisted**                                       |
| **Additional system properties on a tombstone** |                                                         |
| Persisted on the document                       | **Not persisted**                                       |

Document operations also have a different impact on tombstones when Shared Bucket Access is enabled/disabled.

| enable\_shared\_bucket\_access: false                          | enable\_shared\_bucket\_access: true |
| -------------------------------------------------------------- | ------------------------------------ |
| **Deleting a document through Sync Gateway**                   |                                      |
| Creates a tombstone                                            | Creates a tombstone                  |
| **Purging a document through Sync Gateway**                    |                                      |
| Removes the document and metadata                              | Removes the document and metadata    |
| **Deleting a document body in the bucket (SDK, N1QL, expiry)** |                                      |
| Removes the document and metadata                              | Creates a tombstone                  |
| **Purging a document’s metadata (on Couchbase Server)**        |                                      |
| N/A                                                            | Removes the tombstone metadata       |

## [](#what-you-can-do-with-tombstones)What you can do with tombstones

Whether your synchronizations are purely sync gateway or you use Couchbase Lite, you wil need to manage tombstone artefacts (see [Working with tombstones](managing-tombstones.md)):

* Remove tombstones — you need to purge them, manually or automatically
* Clear Sync Gateway’s in-memory channel caches by ejecting

## [](#see-also)See also:

* [Managing Tombstones](../current/manage/managing-tombstones.md)
* [Metadata Purge Interval](sync-with-couchbase-server.md#metadata-purge-interval)
* [$dbname.enable\_shared\_bucket\_access](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-enable%5Fshared%5Fbucket%5Faccess)
* [Server Tombstones](../../server/current/learn/buckets-memory-and-storage/storage-settings.md#tombstones)

## [](#related-content)Related Content

###### [](#)

API Topics

* [Public REST API](../current/rest-api/rest-api.md)
* [Admin REST API](../current/rest-api/rest-api-admin.md)
* [Metrics REST API](../current/rest-api/rest-api-metrics.md)
* [Use the REST API?](#sync-gateway::rest-api-client-app.adoc)

###### [](#-2)

Reference

* [Configuration Properties](../current/configuration/configuration-properties-legacy.md)

###### [](#-3)

Community

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)