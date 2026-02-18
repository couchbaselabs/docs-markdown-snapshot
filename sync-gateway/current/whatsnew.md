---
title: New In 4.0
description: Couchbase Sync Gateway -- What's new in the latest release
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.0/modules/ROOT/pages/whatsnew.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/sync-gateway/current/whatsnew.html)

# New In 4.0

> Couchbase Sync Gateway — What’s new in the latest release  
> This content covers the new features introduced in Sync Gateway 4.0

> [!CAUTION]
> Sync Gateway 4.0 introduces some breaking changes. If you’re upgrading from 3.x, see [Upgrading Sync Gateway](upgrading.md).

## [](#overview-of-sync-gateway-4-0)Overview of Sync Gateway 4.0

Sync Gateway 4.0 represents a major architectural evolution, transitioning from revision trees to [version vectors](server-compatibility/server-compatibility-xdcr-mobile.md#version-vectors) as the foundation for document revision tracking.

This architectural change enables true active-active mobile cluster deployments with bidirectional Cross Data Center Replication (XDCR) while maintaining data consistency and conflict resolution capabilities.

## [](#cross-data-center-replication-xdcr-interoperability)Cross Data Center Replication (XDCR) Interoperability

* **Bi-directional XDCR between mobile clusters**Sync Gateway now supports two way active-active replication using Couchbase Server’s XDCR across mobile clusters. This enables active-active deployments with high availability and no downtime during fail over or disaster recovery.
* **Unified versioning of documents compatible with both XDCR and Mobile products**. Allows for new deployment architectures and consistent conflict resolution.

For more information, see [XDCR — Server Compatibility](server-compatibility/server-compatibility-xdcr.md) and [Bi-directional XDCR Between Mobile Clusters](server-compatibility/server-compatibility-xdcr-mobile.md).

## [](#conflict-resolution-with-version-vectors)Conflict Resolution with Version Vectors

* Sync Gateway 4.0 leverages version vector–based conflict resolution for XDCR.
* By default, Sync Gateway resolves conflicts using `Last Write Wins` (LWW), with the option to use Couchbase Server’s custom conflict resolution (CCR).
* Developers can extend with custom conflict resolvers to meet application-specific needs.

This ensures consistency across mobile and server data while maintaining performance during high-volume replication.

For more information, see [Version vectors](server-compatibility/server-compatibility-xdcr-mobile.md#version-vectors).

## [](#compatibility)Compatibility

* Requires Couchbase Server 7.6.6+ for XDCR interoperability.
* Couchbase Lite 4.0 provides full compatibility with Sync Gateway 4.0, including the ability to switch between clusters while maintaining consistency.
* Earlier Couchbase Lite versions (3.x and 2.x) can synchronize with Sync Gateway 4.0 but cannot switch between clusters without potential consistency issues.

> [!WARNING]
> **Couchbase Lite 4.0 with Sync Gateway 3.2.0 and 3.3.0 is unsupported.**
> 
> Connecting Couchbase Lite 4.0 to Sync Gateway versions before 4.0 is not supported. Use Sync Gateway 4.0 for Couchbase Lite 4.0 compatibility. Fixes for SGW 3.2.0 and 3.3.0 will be available in versions 3.2.7 and 3.3.1.

## [](#performance-improvements)Performance improvements

Sync Gateway 4.0.3 optimizes channel cache processing to improve throughput in high-load scenarios.

## [](#see-also)See Also

[What’s new in previous version 3.3](../3.3/whatsnew.md).

### [](#sync-gateway-release-notes)Sync Gateway Release Notes

[Read the full 4.0 release notes here](product-notes/release-notes.md).

## [](#upgrading)Upgrading

[Upgrading Sync Gateway](upgrading.md).

> [!IMPORTANT]
> Upgrading to version 4.0 is a one way process.

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Sync Function](access-control/sync-function/sync-function.md)
* [Import filter](sync/import-processing.md)

###### [](#-3)

Reference material …​

* [Public REST API](rest-api/rest-api.md)
* [Admin REST API](rest-api/rest-api-admin.md)
* [Metrics REST API](rest-api/rest-api-metrics.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)