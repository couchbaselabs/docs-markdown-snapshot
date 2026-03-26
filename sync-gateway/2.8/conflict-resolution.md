---
title: Conflict Resolution
description: Couchbase Sync Gateway's conflict resolution approach
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/conflict-resolution.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.8@sync-gateway::conflict-resolution.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/conflict-resolution.html)

# Conflict Resolution

> Couchbase Sync Gateway's conflict resolution approach  

Related _Sync_ topics: [Conflict Resolution](../current/sync/sync-inter-syncgateway-conflict-resolution.md) | [Configuration Properties](../current/configuration/configuration-properties-legacy.md)

Conflicts are automatically resolved \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]. The functionality aims to simplify the default behavior of conflict handling and save disk space (conflicting revisions are no longer be stored in the database).

The Couchbase Lite SDK guides describe how the automatic conflict resolution works:  
[Swift](../../couchbase-lite/current/swift/conflict.md) | [Java](../../couchbase-lite/current/java/conflict.md) | [Java (Android)](../../couchbase-lite/current/android/conflict.md) | [C#](../../couchbase-lite/current/csharp/conflict.md) | [Objective-C](../../couchbase-lite/current/objc/conflict.md)

For conflict resolution on 1.x clients — see: [Conflict Resolution 1.x Clients](#sync-gateway::resolving-conflicts.adoc).

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

---

[1](#%5Ffootnoteref%5F1). Since Couchbase Lite 2.0