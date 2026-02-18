---
title: Release Notes
description: Couchbase Sync Gateway
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.0/modules/product-notes/pages/release-notes.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/sync-gateway/current/product-notes/release-notes.html)

# Release Notes

Quicklinks

[Release 3.3](../../3.3/product-notes/release-notes.md) | [Release 3.2](../../3.2/release-notes.md) | [Release 3.1](#3.1@sync-gateway::release-notes.adoc) | [Release 3.0](#3.0@sync-gateway::release-notes.adoc) | [Archived documentation](https://docs-archive.couchbase.com/home/index.html)

> Couchbase Sync Gateway  
> This content describes the key features and changes implemented by release 4.0.0 of Couchbase Sync Gateway

> [!CAUTION]
> One Way Upgrade
> 
> The migration to a 4.x configuration is a ONE WAY process — see: [Upgrading](../upgrading.md) for more.

## [](#maint-latest)4.0.3 — February 2026

### [](#maint-4-0-3)Fixed Issues

* [CBG-4949 — Duplicate conflict logging during legacy rev processing](https://jira.issues.couchbase.com/browse/CBG-4949)
* [CBG-4998 — Import feed panics for docs with CV in \_sync.rev.ver but no \_vv xattr](https://jira.issues.couchbase.com/browse/CBG-4998)
* [CBG-5016 — Panic in \_config?include\_runtime=true endpoint when database has failed to start](https://jira.issues.couchbase.com/browse/CBG-5016)
* [CBG-5042 — Couchbase Server timeout error causes panic in GetUser](https://jira.issues.couchbase.com/browse/CBG-5042)
* [CBG-5055 — Non-integer sequence numbers are incorrectly encoded for norev messages for CBL](https://jira.issues.couchbase.com/browse/CBG-5055)
* [CBG-5068 — Corrupted document metadata causes unchecked subslice panic in sendRevision→toHistory(docRev.History)](https://jira.issues.couchbase.com/browse/CBG-5068)
* [CBG-5107 — Channel information unavailable for non-current revisions](https://jira.issues.couchbase.com/browse/CBG-5107)
* [CBG-5108 — Rev cache can associate stale body with cv or revtreeID when loading revision body backups for non-current revs](https://jira.issues.couchbase.com/browse/CBG-5108)
* [CBG-5132 — Clients fetching a delta can panic when the revision cache is disabled](https://jira.issues.couchbase.com/browse/CBG-5132)
* [CBG-5135 — Current revision attachments can be loaded when loading backup rev by CV](https://jira.issues.couchbase.com/browse/CBG-5135)
* [CBG-5136 — Backup revs loaded from bucket in CV pathway incorrectly assigning deleted status to document revision](https://jira.issues.couchbase.com/browse/CBG-5136)
* [CBG-5146 — replacement revs never utilized for unfiltered replications](https://jira.issues.couchbase.com/browse/CBG-5146)

### [](#enhancements)Enhancements

* [CBG-4765 — Caching performance improvements](https://jira.issues.couchbase.com/browse/CBG-4765)
* [CBG-5092 — Increase websocket control frame timeouts](https://jira.issues.couchbase.com/browse/CBG-5092)

### [](#known-issues)Known Issues

None for this release.

### [](#deprecations)Deprecations

None for this release.

## [](#4-0-2december-2025)4.0.2 — December 2025

### [](#maint-4-0-2)Fixed Issues

* [CBG-5007 — \_ping (and all endpoints) acquire ServerContext.lock.RLock and blocks if the write lock is acquired](https://jira.issues.couchbase.com/browse/CBG-5007)
* [CBG-5026 — Resync on documents last mutated prior to Sync Gateway 4.0 will fail](https://jira.issues.couchbase.com/browse/CBG-5026)
* [CBG-5027 — Have rev cache lock and rev cache value unlocks use defer where possible](https://jira.issues.couchbase.com/browse/CBG-5027)
* [CBG-5029 — Panic during memory based cache eviction can deadlock revision cache shard](https://jira.issues.couchbase.com/browse/CBG-5029)

### [](#enhancements-2)Enhancements

* [CBG-5034 — Synchronize Computation of Deltas](https://jira.issues.couchbase.com/browse/CBG-5034)

### [](#known-issues-2)Known Issues

None for this release.

### [](#deprecations-2)Deprecations

None for this release.

## [](#4-0-1november-2025)4.0.1 — November 2025

### [](#maint-4-0-1)Fixed Issues

* [CBG-4972 — Don’t set SameSite=None when no TLS is used](https://jira.issues.couchbase.com/browse/CBG-4972)

### [](#enhancements-3)Enhancements

* [CBG-4969 — Allow cookieless auth from cbl-js](https://jira.issues.couchbase.com/browse/CBG-4969)

### [](#known-issues-3)Known Issues

None for this release.

### [](#deprecations-3)Deprecations

None for this release.

## [](#4-0-0october-2025)4.0.0 — October 2025

### [](#maint-4-0-0)Fixed Issues

* [CBG-4767 - Make raw doc endpoint return persisted state of document](https://jira.issues.couchbase.com/browse/CBG-4767)
* [CBG-4768 - Silence logging for Admin API expvar requests](https://jira.issues.couchbase.com/browse/CBG-4768)

### [](#enhancements-4)Enhancements

* [CBG-3203 - Shrink revision tree storage by removing channel information](https://jira.issues.couchbase.com/browse/CBG-3203)
* [CBG-4206 - Store attachment metadata in \_globalSync xattr](https://jira.issues.couchbase.com/browse/CBG-4206)
* [CBG-4729 - Add metrics for deleted documents](https://jira.issues.couchbase.com/browse/CBG-4729)
* [CBG-4737 - Disallow basic auth command line flags](https://jira.issues.couchbase.com/browse/CBG-4737)
* [CBG-4754 - Silence debug logging for ping and metrics endpoints](https://jira.issues.couchbase.com/browse/CBG-4754)
* [CBG-4757 - Improve ISGR reconnect logging](https://jira.issues.couchbase.com/browse/CBG-4757)

### [](#known-issues-4)Known Issues

* [CBG-4772 - User xattr only update results in new HLV entry](https://jira.issues.couchbase.com/browse/CBG-4772)
* [CBG-4844 - Attachment audit events do not show CV, only RevTree ID](https://jira.issues.couchbase.com/browse/CBG-4844)
* [CBG-4887 - Orphaned attachments can be left in bucket after removal](https://jira.issues.couchbase.com/browse/CBG-4887)
* [CBG-4939 - Couchbase Lite 4.0 with Sync Gateway versions before 4.0 is unsupported](https://jira.issues.couchbase.com/browse/CBG-4939)

### [](#deprecations-4)Deprecations

* [CBG-3796 - Disallow enable\_star\_channel=false](https://jira.issues.couchbase.com/browse/CBG-3796)
* [CBG-4316 - Disallow allow\_conflicts=true](https://jira.issues.couchbase.com/browse/CBG-4316)
* [CBG-4726 - Disallow enable\_shared\_bucket\_access=false](https://jira.issues.couchbase.com/browse/CBG-4726)

> [!NOTE]
> For an overview of the latest features offered in Sync Gateway 4.0.0, see [New in 4.0](../whatsnew.md).

## [](#upgrading)Upgrading

For more on upgrading — see: [Upgrading](../upgrading.md)

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