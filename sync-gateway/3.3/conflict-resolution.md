[View original HTML](/sync-gateway/3.3/conflict-resolution.html)

> Couchbase Sync Gateway’s conflict resolution approach  

Related _Sync_ topics: [Conflict Resolution](conflict-resolution.md) | [Bootstrap Configuration](configuration/configuration-schema-bootstrap.md)

Conflicts are automatically resolved \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]. The functionality aims to simplify the default behavior of conflict handling and save disk space (conflicting revisions are no longer be stored in the database).

The Couchbase Lite SDK guides describe how the automatic conflict resolution works:  
[Swift](../../couchbase-lite/current/swift/conflict.md) | [Java](../../couchbase-lite/current/java/conflict.md) | [Java (Android)](../../couchbase-lite/current/android/conflict.md) | [C#](../../couchbase-lite/current/csharp/conflict.md) | [Objective-C](../../couchbase-lite/current/objc/conflict.md)

For conflict resolution on 1.x clients — see : [Conflict Resolution 1.x Clients](#resolving-conflicts.adoc).

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Sync Function](access-control/sync-function/sync-function.md)
* [Import filter](sync/import-processing.md)
* [Access Control](configuration/configuration-schema-access-control.md)
* [Add/Update Sync Function](rest-api/rest%5Fapi%5Fadmin.md#tag/Database-Configuration/operation/put%5Fkeyspace-%5Fconfig-sync)
* [Sync Function Overview](access-control/sync-function/sync-function.md)

###### [](#-3)

Reference material …​

* [Public REST API](rest-api/rest-api.md)
* [Admin REST API](rest-api/rest-api-admin.md)
* [Metrics REST API](rest-api/rest-api-metrics.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)

Sync Function Blogs

* [Using roles in sync functions](https://blog.couchbase.com/augment-your-sync-function-with-roles-in-couchbase-sync-gateway/)
* [Tutorial: Getting Started with Data Synchronization using Couchbase Mobile for Offline-First Apps](https://blog.couchbase.com/data-synchronization-offline-first-apps-couchbase/)
* [Sync Function (category)](https://blog.couchbase.com/tag/sync-function/)

---

[1](#%5Ffootnoteref%5F1). Since Couchbase Lite 2.0