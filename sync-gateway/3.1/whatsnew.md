---
title: New in 3.1
description: Couchbase Sync Gateway -- What's new in the latest release
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.1/modules/ROOT/pages/whatsnew.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.1@sync-gateway::whatsnew.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.1/whatsnew.html)

# New in 3.1

> Couchbase Sync Gateway — What's new in the latest release  
> This content covers the new features introduced in Sync Gateway 3.1

> [!CAUTION]
> Sync Gateway 3.0.x introduces some breaking changes. If you are upgrading from 2.x, please refer to the [Upgrading](upgrading.md) page. Users should be able to upgrade to 3.1.x from 3.0.x without manual intervention.

* **New support for Scopes and Collections**  
Couchbase has introduced support for Scopes and Collections for self-managed cloud-to-edge deployments only in [Couchbase Lite 3.1.0](../../couchbase-lite/current/index.md) and [Sync Gateway 3.1.0](introduction.md). This release won't cause any issues with existing apps, as it's compatible with older versions. If you have an app that uses bucket-based APIs, you can still upgrade to 3.1, but please note that this API is now deprecated. For more information, see [Scopes and Collections Configuration for Sync Gateway](scopes-and-collections-config.md).
* **Improved Data Organization and Access Control for Scopes and Collections**  
Couchbase Mobile now offers Scopes and Collections, allowing more efficient and scalable data organisation within a bucket. This also introduces an improved method of defining and enforcing data [Access Control](access-control-concepts.md) more granularly. Multi-tenant apps will also experience better scalability and independent data lifecycle management.
* **Improved metadata isolation for Scopes and Collections**  
Sync Gateway 3.1.0 has improved metadata isolation. The system data maintained by Sync Gateway is now stored in the `_default` Scope/Collection, while both the `_default` and user-defined Scope/Collection can be used for application data. For more information, examples and use cases, see [Scopes and Collections Support in Couchbase Mobile for Edge Applications](https://www.couchbase.com/blog/scopes-collections-couchbase-mobile/).
* **Collection-Level Sync Functions and Scoped User Associations**  
The [Sync Functions](sync-function.md) now work on a Collection level, and additional optional fields have been added to the database configurations to support this update. Each database is designed to support only one Scope. Users can be associated with that Scope and shared across multiple Collections.
* **Enhanced Collection Synchronization and Local Data Storage with Couchbase Lite Client**  
With Couchbase Lite client replications, you can synchronize one or multiple Collections within a specific scope. The Couchbase Lite client also will store data locally in a scope not synchronized with the remote Sync Gateway.

> [!NOTE]
> You can define 1 custom scope per database with up to 1000 custom collections. If you don't specify a custom scope and collection, any documents you create will be saved in the default scope and collection.

Read the full [3.1 release notes](release-notes.md).

See more details of [what's new in the previous 3.0 release.](../3.0/whatsnew.md)

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Sync Function](#sync-function-overview.adoc)
* [Import filter](import-processing.md)

###### [](#-3)

Reference material …​

* [Public REST API](rest-api.md)
* [Admin REST API](rest-api-admin.md)
* [Metrics REST API](rest-api-metrics.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)