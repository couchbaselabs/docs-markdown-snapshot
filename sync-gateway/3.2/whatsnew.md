---
title: New In 3.2
description: Couchbase Sync Gateway -- What's new in the latest release
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.2/modules/ROOT/pages/whatsnew.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:3.2@sync-gateway::whatsnew.adoc[]
---

[View original HTML](/sync-gateway/3.2/whatsnew.html)

# New In 3.2

> Couchbase Sync Gateway — What’s new in the latest release  
> This content covers the new features introduced in Sync Gateway 3.2

> [!WARNING]
> Do not deploy Eventing/Sync Gateway until all SGW nodes are at version 3.2\. For earlier Sync Gateway versions that do not write import XATTRs, Eventing functions may encounter infinite recursions and duplicate mutations if deployed in a mixed mode SGW environment. This occurs if you have a mixed installation consisting of Sync Gateway 3.2 and an earlier version, and you deploy a new Eventing or Sync Gateway function during an upgrade.

## [](#release-3-2-6-july-2025)Release 3.2.6 (July 2025)

Sync Gateway 3.2.6 is a maintenance release.

For more information about all changes within this maintenance release, see [3.2 release notes](release-notes.md).

## [](#release-3-2-5-june-2025)Release 3.2.5 (June 2025)

Sync Gateway 3.2.5 is a maintenance release.

For more information about all changes within this maintenance release, see [3.2 release notes](release-notes.md).

## [](#release-3-2-4-april-2025)Release 3.2.4 (April 2025)

Sync Gateway 3.2.4 is a maintenance release.

For more information about all changes within this maintenance release, see [3.2 release notes](release-notes.md).

## [](#release-3-2-3-march-2025)Release 3.2.3 (March 2025)

Sync Gateway 3.2.3 is a maintenance release.

For more information about all changes within this maintenance release, see [3.2 release notes](release-notes.md).

## [](#release-3-2-2-february-2025)Release 3.2.2 (February 2025)

Sync Gateway 3.2.2 is a maintenance release that addresses the following:

* Fixes and improvements to revcache on-demand imports.
* Improving cleanup processes during rollback of the import feed.
* Additional stats to track background N1QL queries.

For more information about all changes within this maintenance release, see [3.2 release notes](release-notes.md).

## [](#release-3-2-1-october-2024)Release 3.2.1 (October 2024)

### [](#additional-rev-cache-configuration-option)Additional Rev Cache Configuration Option

You can now specify a memory limit on your rev cache with the `rev_cache.max_memory_count_mb` configuration option. You can use this option alongside existing configurable limits to the number of documents in the rev cache to reduce the risk of Out of Memory (OOM) issues.

For more information, see [Rev Cache Max Memory Count Config Option](configuration-schema-database.md#cache-rev%5Fcache-max%5Fmemory%5Fcount%5Fmb).

## [](#release-3-2-0-september-2024)Release 3.2.0 (September 2024)

### [](#eventing-support-with-sync-gateway-3-2-0-and-couchbase-server-7-6-3)Eventing Support with Sync Gateway 3.2.0+ and Couchbase Server 7.6.3+

Sync Gateway 3.2.0 now supports improved interoperability with Eventing from Couchbase Server version 7.6.3+.

You can now create Eventing functions with read-write bindings with the source bucket associated with a Sync Gateway database. You can use Eventing to handle data changes that happen when applications interact and to integrate with other Couchbase services such as Data, Query and Full Text Search.

For more information, see [Eventing — Server Compatibility](server-compatibility-eventing.md)

### [](#audit-logging-support)Audit Logging Support

Couchbase now provides Audit Logging support for Sync Gateway. Audit Logging provides tools for administrators to track operational irregularities and to support regulatory and security compliance standards, such as [HIPAA](https://www.hhs.gov/hipaa/index.html) and [SOC-2](https://soc2.co.uk/soc2). For more information, see [Audit Logging](audit-logging.md).

## [](#see-also)See Also

[What’s new in previous version 3.1](#3.1@sync-gateway:ROOT:whatsnew.adoc).

### [](#sync-gateway-release-notes)Sync Gateway Release Notes

[Read the full 3.2 release notes here](release-notes.md).

## [](#upgrading)Upgrading

[Upgrading Sync Gateway](upgrading.md).

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