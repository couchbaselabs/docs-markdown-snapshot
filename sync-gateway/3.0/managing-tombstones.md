---
title: Tombstones
description: Sync Gateway's <em>Tombstones</em> are the means by which mobile
  clients are notified that a document has been deleted.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.0/modules/ROOT/pages/managing-tombstones.adoc
  xref: xref:3.0@sync-gateway::managing-tombstones.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.0/managing-tombstones.html)

# Tombstones

> Sync Gateway's _Tombstones_ are the means by which mobile clients are notified that a document has been deleted.  
> Here we introduce the concept of _Tombstones_ and their role in the _Sync Gateway_ revision process.

## [](#tombstone-objects)Tombstone Objects

A _tombstone_ is a persistent record that an item has been deleted.

Sync Gateway creates tombstones to ensure all synchronizing devices can identify that a previously existing document has now been deleted. This is particularly necessary in the case of devices that may not be online continuously and therefore are not syncing regularly.

The actual tombstone artefact is a document revision comprising only:

* The (deleted) document ID
* A revision ID
* A key value pair `deleted:true`.

Example 1\. Example tombstone artifact

```json
{
  "_deleted": true,
  "_id": "foobar",
  "_rev": "3-db962c6d93c3f1720cc7d3b6e50ac9df"
}
```

## [](#sync)Sync

When mobile tombstones sync with a Couchbase Server (that is, when `enable_shared_bucket_access: true`) they become server tombstones. The document body is deleted, and only the mobile sync metadata required to replicate the tombstone is retained in the mobile extended attribute.

The server's `metadata purge interval` becomes an important consideration for sync'd mobile deployments. Because, when the server purges a tombstone (based on the `metadata purge interval`), that tombstone is no longer replicated to mobile clients.

So, users should set the server's `metadata purge interval` based on their expected client replication frequency, to ensure that clients are notified of the tombstone prior to that tombstone being purged.

> [!NOTE]
> The default `metadata purge interval` is set to 3 days which can potentially result in tombstones being purged before all clients have had a chance to be notified.

For how to tune the `metadata purge interval` on Couchbase Server, see the server documentation on:

* Bucket settings \[on server UI\] — [Auto Compaction with UI](../../server/current/manage/manage-settings/configure-compact-settings.md#configure-auto-compaction-with-the-ui)
* Bucket endpoint \[on the REST API\] — [Creating and Editing Buckets](../../server/current/rest-api/rest-bucket-create.md)

No matter how you sync, you will need to manage tombstone artifacts to:

* Remove tombstones (manually or automatically) — see [Purging](#lbl-tomb-purge)
* Clear Sync Gateway's in-memory channel caches — see [Cache Ejection](#lbl-tomb-cache)

### [](#storage-location)Storage Location

The storage location of tombstones differs slightly depending on whether the Shared Bucket Access feature is enabled (`enable_shared_bucket_access: true`) — see, [Table 1](#tbl-tomb-storage) for those differences.

__Table 1\. Tombstone locations__
| Type of data                                | Value of enable\_shared\_bucket\_access\` |                                                         |
| ------------------------------------------- | ----------------------------------------- | ------------------------------------------------------- |
| false                                       | true                                      |                                                         |
| Mobile metadata                             | Persisted on the document (doc.\_sync)    | Persisted as system extended attributes (xattr.\_sync)  |
| Tombstone                                   | Persisted on the document                 | Persisted as system extended attributes (xattr.\_sync). |
| Additional user properties on a tombstone\* | Persisted on the document                 | Not persisted                                           |
| Additional system properties on a tombstone | Persisted on the document                 | Not persisted                                           |

### [](#document-operations)Document Operations

Document operations have a different impact on tombstones when Shared Bucket Access is enabled/disabled.

| Location                      | Activity                                                   | Value of enable\_shared\_bucket\_access\` |                     |
| ----------------------------- | ---------------------------------------------------------- | ----------------------------------------- | ------------------- |
| false                         | true                                                       |                                           |                     |
| Sync Gateway                  | Deleting a document                                        | Creates a tombstone                       | Creates a tombstone |
| Purging a document            | Removes the document and metadata                          | Removes the document and metadata         |                     |
| Couchbase Server              | Deleting a document body in the bucket (SDK, N1QL, expiry) | Removes the document and metadata         | Creates a tombstone |
| Purging a document's metadata | N/A                                                        | Removes the tombstone metadata            |                     |

## [](#lbl-tomb-purge)Purging

To remove tombstones, you need to purge them. The table at [Table 2](#tbl-tomb-purge) shows when tombstones are purged automatically and how to manually purge them.

__Table 2\. Purging tombstones__
|           | Value of enable\_shared\_bucket\_access\`                                                                                                                                                                                                                                                                                                                                                                            |                                                                                                                                         |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| false     | true                                                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                                                                         |
| Automatic | Tombstones are not automatically purged from the bucket. Tombstones can be purged by setting a server expiry on tombstone documents. This can be easily automated via Sync Gateway. Use the [expiry()](sync-function-api-expiry-cmd.md) function in the Sync Function. Set the expiry time to be sufficient to allow for all other devices to sync and receive the delete notification — perhaps a week, or a month. | Tombstones are automatically purged from the bucket based on the server's metadata purge interval.                                      |
| Manual    | Tombstones can be manually removed via Sync Gateway's [/{db}/\_purge](rest-api-admin.md#/document/post%5F%5Fdb%5F%5F%5Fpurge) endpoint, or deleting documents directly in the bucket.                                                                                                                                                                                                                                | Tombstones can be manually removed via Sync Gateway's [/{db}/\_purge](rest-api-admin.md#/document/post%5F%5Fdb%5F%5F%5Fpurge) endpoint. |

Purging of tombstones is also required on Couchbase Lite. For example, you might decide that if a document is deleted on a Couchbase Lite client, that you want to purge the document (on that device) as soon as the delete has been successfully replicated to Sync Gateway.

## [](#lbl-tomb-cache)Cache Ejection

Deleted/expired tombstones aren't automatically ejected from Sync Gateway's in-memory channel caches. See [Table 3](#tbl-tomb-cache), which shows when channel caches are ejected.

__Table 3\. Flushing Sync Gateway channel caches__
| TombstonePurged On | Value of enable\_shared\_bucket\_access\`                                                    |                                                                                                                                                                                                                                                                                                          |
| ------------------ | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| false              | true                                                                                         |                                                                                                                                                                                                                                                                                                          |
| Couchbase Server   | Restarting Sync Gateway will flush the cache                                                 | Restarting Sync Gateway will flush the cache Running the [/{db}/\_compact](rest-api-admin.md#/database/post%5F%5Fdb%5F%5F%5Fcompact) endpoint will remove purged tombstones from the channel cache \[[1](#%5Ffootnotedef%5F1 "View footnote.")\] [1](#%5Ffootnoteref%5F1). Commencing with release 2.1.1 |
| Sync Gateway       | Restarting Sync Gateway will flush the cache. Starting in 2.1.1, this is done automatically. | Restarting Sync Gateway will flush the cache. Starting in 2.1.1, this is done automatically.                                                                                                                                                                                                             |

---

##### 

## [](#related-content)Related Content

###### [](#-2)

API Topics

* [Public REST API](rest-api.md)
* [Admin REST API](rest-api-admin.md)
* [Metrics REST API](rest-api-metrics.md)

###### [](#-3)

Reference

* [Bootstrap](configuration-schema-bootstrap.md)
* [Database](configuration-schema-database.md)
* [Database Security](configuration-schema-db-security.md)
* [Access Control](configuration-schema-access-control.md)
* [Import Filter](configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)