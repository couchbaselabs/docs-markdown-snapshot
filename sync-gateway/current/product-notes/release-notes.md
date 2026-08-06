---
title: Release Notes
description: Couchbase Sync Gateway
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.1/modules/product-notes/pages/release-notes.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:sync-gateway:product-notes:release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/current/product-notes/release-notes.html)

# Release Notes

Quicklinks

[Release 4.0](../../4.0/product-notes/release-notes.md) | [Release 3.3](../../3.3/product-notes/release-notes.md) | [Release 3.2](../../3.2/release-notes.md) | [Release 3.1](../../3.1/release-notes.md) | [Release 3.0](../../3.0/release-notes.md) | [Archived documentation](https://docs-archive.couchbase.com/home/index.html)

> Couchbase Sync Gateway  
> This content describes the key features and changes implemented by release 4.1 of Couchbase Sync Gateway

> [!CAUTION]
> One Way Upgrade
> 
> The migration to a 4.x configuration is a ONE WAY process — see: [Upgrading](../upgrading.md) for more.

## [](#maint-4-1-1)4.1.1 — July 2026

> [!IMPORTANT]
> If you use Sync Gateway 4.1.0, upgrade to this release to receive critical fixes.

Version 4.1 of Sync Gateway delivers the following features and enhancements.

### [](#non-disruptive-rolling-upgrades)Non-Disruptive Rolling Upgrades

Sync Gateway 4.1 introduces cluster compatibility version, enabling node-by-node upgrades without downtime, with a safe rollback path throughout the upgrade window.

For more information, see [Cluster Compatibility Version](../cluster-compatibility-version.md).

### [](#distributed-resync)Distributed Resync

Sync Gateway 4.1 redesigns resync to distribute work in parallel across all cluster nodes, replacing the previous single-node sequential approach.

For more information, see [Resync](../manage/resync.md).

### [](#channel-history-management)Channel History Management

Sync Gateway 4.1 introduces Admin REST API endpoints for retrieving and pruning channel history on both user records and documents, reducing metadata bloat and unnecessary revocation messages during zero-checkpoint replications.

For more information, see [Channel History Management](../manage/channel-history.md).

### [](#metadata-isolation-migrate-to-system-collection)Metadata Isolation: Migrate to System Collection

Sync Gateway 4.1 introduces an opt-in migration that moves Sync Gateway internal metadata from `_default._default` to `_system._mobile`, isolating it from user application data. The migration is never applied automatically at upgrade and cannot be reversed.

For more information, see [Migrate Metadata to System Collection](../migrate-metadata-system-collection.md).

For a full overview of new features in this release, see [New in 4.1](../whatsnew.md).

### [](#fixed-issues)Fixed Issues

* [CBG-3214 — Unhandled cbgt panic after removing database](https://jira.issues.couchbase.com/browse/CBG-3214)
* [CBG-4345 — Couchbase Server timeout error causes panic in GetUser](https://jira.issues.couchbase.com/browse/CBG-4345)
* [CBG-4939 — Couchbase Lite 4.0 is allowed to connect to Sync Gateway 3.2.6/3.3.0](https://jira.issues.couchbase.com/browse/CBG-4939)
* [CBG-5006 — /\_ping (and all endpoints) acquire ServerContext.lock.RLock and blocks if the write lock is acquired](https://jira.issues.couchbase.com/browse/CBG-5006)
* [CBG-5020 — Panic during memory based cache eviction can deadlock revision cache shard](https://jira.issues.couchbase.com/browse/CBG-5020)
* [CBG-5051 — Non-integer sequence numbers are incorrectly encoded for norev messages for CBL](https://jira.issues.couchbase.com/browse/CBG-5051)
* [CBG-5133 — Backup revs loaded from bucket in CV pathway incorrectly assigning deleted status to document revision](https://jira.issues.couchbase.com/browse/CBG-5133)
* [CBG-5134 — Current revision attachments can be loaded when loading backup rev by CV](https://jira.issues.couchbase.com/browse/CBG-5134)
* [CBG-5145 — Replacement revs never utilized for unfiltered replications](https://jira.issues.couchbase.com/browse/CBG-5145)
* [CBG-5262 — \_changes feeds with active\_only=true and limit parameters can miss expected changes with revocations](https://jira.issues.couchbase.com/browse/CBG-5262)
* [CBG-5355 — Panic in revoked feed handling](https://jira.issues.couchbase.com/browse/CBG-5355)
* [CBG-5365 — Problem with channel removal macro expansion when channel names have . in them](https://jira.issues.couchbase.com/browse/CBG-5365)
* [CBG-5381 — Resync regenerate sequences will not set \_default metadata id when finished](https://jira.issues.couchbase.com/browse/CBG-5381)
* [CBG-5436 — Subdoc operation failure on multiple channel removal](https://jira.issues.couchbase.com/browse/CBG-5436)
* [CBG-5541 — Metadata migration never reaches 'completed' state with non-metadata \_sync: docs stored in the \_default](https://jira.issues.couchbase.com/browse/CBG-5541)
* [CBG-5552 — activeOnly replication can miss documents for channels over the pagination limit](https://jira.issues.couchbase.com/browse/CBG-5552)

### [](#enhancements)Enhancements

* [CBG-3848 — Distributed resync via sharding for improved throughput and HA](https://jira.issues.couchbase.com/browse/CBG-3848)
* [CBG-4363 — Enable xattr only DCP stream for Sync Gateway caching feed](https://jira.issues.couchbase.com/browse/CBG-4363)
* [CBG-4542 — Skip revcache insertion on all write operations](https://jira.issues.couchbase.com/browse/CBG-4542)
* [CBG-4651 — Support persistent-config cluster-wide operation via /db/\_offline](https://jira.issues.couchbase.com/browse/CBG-4651)
* [CBG-4966 — Allow cookieless auth from cbl-js](https://jira.issues.couchbase.com/browse/CBG-4966)
* [CBG-4967 — Don't set SameSite=None when no TLS is used](https://jira.issues.couchbase.com/browse/CBG-4967)
* [CBG-5091 — Increase websocket control frame timeouts](https://jira.issues.couchbase.com/browse/CBG-5091)
* [CBG-5143 — Support EdDSA tokens for OIDC/JWTs](https://jira.issues.couchbase.com/browse/CBG-5143)
* [CBG-5203 — Silently handle cbl-js ping blip requests](https://jira.issues.couchbase.com/browse/CBG-5203)
* [CBG-5206 — Cluster Compatibility and Rolling Upgrade Enhancements](https://jira.issues.couchbase.com/browse/CBG-5206)
* [CBG-5221 — System scoped metadata and online migration process](https://jira.issues.couchbase.com/browse/CBG-5221)
* [CBG-5253 — REST endpoint for pruning user channel history](https://jira.issues.couchbase.com/browse/CBG-5253)
* [CBG-5254 — REST endpoint for pruning document channel history](https://jira.issues.couchbase.com/browse/CBG-5254)

### [](#known-issues)Known Issues

None for this release.

### [](#deprecations)Deprecations

None for this release.

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