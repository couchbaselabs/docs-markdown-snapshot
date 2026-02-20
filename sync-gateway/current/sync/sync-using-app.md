---
title: Sync with Couchbase Lite
description: Use Sync Gateway to sync with Couchbase Lite apps.
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.0/modules/sync/pages/sync-using-app.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:sync-gateway:sync:sync-using-app.adoc[]
---

[View original HTML](/sync-gateway/current/sync/sync-using-app.html)

# Sync with Couchbase Lite

> Use Sync Gateway to sync with Couchbase Lite apps.  

## [](#syncing-with-couchbase-lite-apps)Syncing with Couchbase Lite Apps

Couchbase Lite client applications use a Replicator process to synchronize their local database, through a Sync Gateway database, to a remote Couchbase Server database (server- or cloud-based) — see: [Figure 1](#fig-sync-diag).

![svr sgw cbl](../_images/svr-sgw-cbl.png) 

Figure 1\. Sync from Cloud/Server to Edge

Pull Replication

This is the process by which clients running Couchbase Lite download database changes from the remote (server) source database to the local target database

Push Replication

This is the process by which clients running Couchbase Lite upload database changes from the local source database to the remote (server) target database

For more on how to build Couchbase Lite applications that use Sync Gateway replication, see the documentation for the appropriate language:

Related Couchbase Lite content

[Android](../../../couchbase-lite/current/android/replication.md) | [C](../../../couchbase-lite/current/c/replication.md) | [C#](../../../couchbase-lite/current/csharp/replication.md) | [Java](../../../couchbase-lite/current/java/replication.md) | [Objective-C](../../../couchbase-lite/current/objc/replication.md) | [Swift](../../../couchbase-lite/current/swift/replication.md)

---

##### 

## [](#related-content)Related Content

###### [](#-2)

API Topics

* [Public REST API](../rest-api/rest-api.md)
* [Admin REST API](../rest-api/rest-api-admin.md)
* [Metrics REST API](../rest-api/rest-api-metrics.md)

###### [](#-3)

Reference

* [Bootstrap](../configuration/configuration-schema-bootstrap.md)
* [Database](../configuration/configuration-schema-database.md)
* [Database Security](../configuration/configuration-schema-db-security.md)
* [Access Control](../configuration/configuration-schema-access-control.md)
* [Import Filter](../configuration/configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](../configuration/configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](../configuration/configuration-properties-legacy.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)