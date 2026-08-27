---
title: Managing Tombstones
description: Sync Gateway's <em>Tombstones</em> are the means by which mobile
  clients are notified that a document has been deleted.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/managing-tombstones.adoc
  xref: xref:2.8@sync-gateway::managing-tombstones.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/managing-tombstones.html)

# Managing Tombstones

> Sync Gateway's _Tombstones_ are the means by which mobile clients are notified that a document has been deleted.  

## [](#purging-tombstones)Purging Tombstones

To remove tombstones, you need to purge them. The following tables describe how to purge tombstones (automatically or manually) and reset the Sync Gateway channel cache when Shared Bucket Access is enabled or disabled.

| **Automatic purging of tombstones**                                                                                                                                                                                                                                                                                                                                                                           |                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| enable\_shared\_bucket\_access: false                                                                                                                                                                                                                                                                                                                                                                         | enable\_shared\_bucket\_access: true                                                               |
| Tombstones are not automatically purged from the bucket. Tombstones can be purged by setting a server expiry on tombstone documents. This can be easily automated via Sync Gateway using the [expiry()](sync-function.md#expiry) function in the Sync Function. The expiry time should be sufficient (perhaps a week, or a month) to allow for all other devices to sync and receive the delete notification. | Tombstones are automatically purged from the bucket based on the server's metadata purge interval. |

| **Manually purging tombstones**                                                                                                                                                                           |                                                                                                                                                             |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| enable\_shared\_bucket\_access: false                                                                                                                                                                     | enable\_shared\_bucket\_access: true                                                                                                                        |
| Tombstones can be manually removed via Sync Gateway's [/{db}/\_purge](../current/rest-api/rest-api-admin.md#/document/post%5F%5Fdb%5F%5F%5Fpurge) endpoint, or deleting documents directly in the bucket. | Tombstones can be manually removed via Sync Gateway's [/{db}/\_purge](../current/rest-api/rest-api-admin.md#/document/post%5F%5Fdb%5F%5F%5Fpurge) endpoint. |

Purging of tombstones is also required on Couchbase Lite. For example, you might decide that if a document is deleted on a Couchbase Lite client, that you want to purge the document (on that device) as soon as the delete has been successfully replicated out to Sync Gateway.

## [](#cache-ejection)Cache Ejection

Deleted/expired tombstones aren't automatically ejected from Sync Gateway's in-memory channel caches. The following table describes how to eject Sync Gateway's cache.

| enable\_shared\_bucket\_access: false                                                        | enable\_shared\_bucket\_access: true                                                                                                                                                                                                        |
| -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **For tombstones purged on Couchbase Server**                                                |                                                                                                                                                                                                                                             |
| Restarting Sync Gateway will flush the cache                                                 | Restarting Sync Gateway will flush the cache. Starting in 2.1.1, running the [/{db}/\_compact](../current/rest-api/rest-api-admin.md#/database/post%5F%5Fdb%5F%5F%5Fcompact) endpoint will remove purged tombstones from the channel cache. |
| **For documents purged on Sync Gateway**                                                     |                                                                                                                                                                                                                                             |
| Restarting Sync Gateway will flush the cache. Starting in 2.1.1, this is done automatically. | Restarting Sync Gateway will flush the cache. Starting in 2.1.1, this is done automatically.                                                                                                                                                |

## [](#tombstone-lifecycle)Tombstone Lifecycle

The storage location of tombstones differs slightly depending on whether the Shared Bucket Access feature is enabled (`enable_shared_bucket_access: true`). The table below describes those differences.

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
| **Purging a document's metadata (on Couchbase Server)**        |                                      |
| N/A                                                            | Removes the tombstone metadata       |

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