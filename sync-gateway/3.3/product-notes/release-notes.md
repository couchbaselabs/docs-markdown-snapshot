---
title: Release Notes
description: Couchbase Sync Gateway
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.3/modules/product-notes/pages/release-notes.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:3.3@sync-gateway:product-notes:release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.3/product-notes/release-notes.html)

# Release Notes

Quicklinks

[Release 3.2](../../3.2/release-notes.md) | [Release 3.1](#3.1@sync-gateway::release-notes.adoc) | [Release 3.0](#3.0@sync-gateway::release-notes.adoc) | [Release 2.8](#2.8@sync-gateway::release-notes.adoc) | [Archived documentation](https://docs-archive.couchbase.com/home/index.html)

> Couchbase Sync Gateway  
> This content describes the key features and changes implemented by release 3.3.2 of Couchbase Sync Gateway

> [!CAUTION]
> One Way Upgrade
> 
> The migration to 3.x configuration is a ONE WAY process — see: [Upgrading](../upgrading.md) for more.

## [](#maint-latest)3.3.3 — February 2026

### [](#fixed-issues)Fixed Issues

* [CBG-5015 — Panic in \_config?include\_runtime=true endpoint](https://jira.issues.couchbase.com/browse/CBG-5015)
* [CBG-5131 — Clients fetching a delta can panic when the revision cache is disabled](https://jira.issues.couchbase.com/browse/CBG-5131)

### [](#enhancements)Enhancements

* [CBG-4765 — Caching performance improvements](https://jira.issues.couchbase.com/browse/CBG-4765)
* [CBG-5093 — Increase websocket control frame timeouts](https://jira.issues.couchbase.com/browse/CBG-5093)

### [](#known-issues)Known Issues

None for this release.

### [](#deprecations)Deprecations

None for this release.

## [](#3-3-2december-2025)3.3.2 — December 2025

### [](#fixed-issues-2)Fixed Issues

* [CBG-5009 - \_ping (and all endpoints) acquire ServerContext.lock.RLock and blocks if the write lock is acquired](https://jira.issues.couchbase.com/browse/CBG-5009)
* [CBG-5028 - Have rev cache lock and rev cache value unlocks use defer where possible](https://jira.issues.couchbase.com/browse/CBG-5028)
* [CBG-5030 - Panic during memory based cache eviction can deadlock revision cache shard](https://jira.issues.couchbase.com/browse/CBG-5030)

### [](#enhancements-2)Enhancements

* [CBG-5034 - Synchronize Computation of Deltas](https://jira.issues.couchbase.com/browse/CBG-5034)

### [](#known-issues-2)Known Issues

None for this release.

### [](#deprecations-2)Deprecations

None for this release.

## [](#3-3-1november-2025)3.3.1 — November 2025

### [](#fixed-issues-3)Fixed Issues

* [CBG-4973 - Don’t set SameSite=None when no TLS is used](https://jira.issues.couchbase.com/browse/CBG-4973)
* [CBG-4941 - Couchbase Lite 4.0 is allowed to connect to Sync Gateway 3.3.0](https://jira.issues.couchbase.com/browse/CBG-4941)

### [](#enhancements-3)Enhancements

* [CBG-4970 - Allow cookieless auth from cbl-js](https://jira.issues.couchbase.com/browse/CBG-4970)

### [](#known-issues-3)Known Issues

None for this release.

### [](#deprecations-3)Deprecations

None for this release.

## [](#3-3-0august-2025)3.3.0 — August 2025

> [!WARNING]
> Do not deploy Eventing/Sync Gateway until all SGW nodes are at version 3.2 or later. For earlier Sync Gateway versions that do not write import XATTRs, Eventing functions experience infinite recursions and duplicate mutations if deployed in a mixed mode SGW environment. This can only happen when you deploy a new Eventing/Sync Gateway function during an upgrade, with some SGW nodes at version 3.2 or later, and others at an earlier version.

### [](#partitioned-indexes)Partitioned Indexes

Sync Gateway 3.3 introduces support for partitioned indexes. Partitioned indexes offer horizontal scalability for large deployments by sharding indexes across multiple nodes.

### [](#disable-the-public-all-docs-endpoint)Disable the Public All Docs Endpoint

Sync Gateway 3.3 introduces an option to disable the [GET /{keyspace}/\_all\_docs](../rest-api/rest%5Fapi%5Fpublic.md#tag/Document/operation/get%5Fkeyspace-%5Fall%5Fdocs) operation in the Public REST API.

### [](#interactive-admin-credentials-for-sg-collect-info)Interactive Admin Credentials for SG Collect Info

In Sync Gateway 3.3 and later, the `sgcollect_info` tool provides an interactive password prompt so that you can enter administrative credentials.

### [](#performance-improvements-for-larger-deployments)Performance Improvements for Larger Deployments

Sync Gateway 3.3 includes several performance enhancements for larger deployments.

For more information on new features and enhancements in this release, see [New In 3.3](../whatsnew.md).

Version 3.3.0 of Sync Gateway also delivers the following features and enhancements.

### [](#maint-3-3-0)Fixed Issues

* [CBG-3933 — rotated\_logs\_size\_limit not used by ConsoleLogger’s FileOutput](https://jira.issues.couchbase.com/browse/CBG-3933)
* [CBG-3935 — Documents with invalid inline \_sync metadata cause panic during import](https://jira.issues.couchbase.com/browse/CBG-3935)
* [CBG-3947 — make config polling more resilient to timeout errors](https://jira.issues.couchbase.com/browse/CBG-3947)
* [CBG-4067 — Timeout error will release document sequence as unused](https://jira.issues.couchbase.com/browse/CBG-4067)
* [CBG-4186 — ISGR replicators reaching max\_backoff with a reconnection error will not transition to stop](https://jira.issues.couchbase.com/browse/CBG-4186)
* [CBG-4216 — Pending unused sequences shouldn’t update high cache sequence](https://jira.issues.couchbase.com/browse/CBG-4216)
* [CBG-4236 — Default log file permissions changed from 644 to 600](https://jira.issues.couchbase.com/browse/CBG-4236)
* [CBG-4309 — Missing janitor kick in cbgt rollback](https://jira.issues.couchbase.com/browse/CBG-4309)
* [CBG-4322 — sgcollect\_info: logs duplicated or repeated](https://jira.issues.couchbase.com/browse/CBG-4322)
* [CBG-4371 — empty files for high memory heap profiles](https://jira.issues.couchbase.com/browse/CBG-4371)
* [CBG-4373 — http continuous changes requests no longer flush output](https://jira.issues.couchbase.com/browse/CBG-4373)
* [CBG-4387 — remove print debugging for GET /ks/\_all\_docs](https://jira.issues.couchbase.com/browse/CBG-4387)
* [CBG-4395 — remove debug logging for GetWithXattrs for multiple xattrs](https://jira.issues.couchbase.com/browse/CBG-4395)
* [CBG-4399 — remove confusing logging when importing a tombstone with non sync xattrs](https://jira.issues.couchbase.com/browse/CBG-4399)
* [CBG-4422 — Resync collections processing is nil while no documents have been processed](https://jira.issues.couchbase.com/browse/CBG-4422)
* [CBG-4453 — Increase index creation retry time](https://jira.issues.couchbase.com/browse/CBG-4453)
* [CBG-4462 — Leaking/duplicate status reporters across ISGR reconnection can cause 409 conflcts](https://jira.issues.couchbase.com/browse/CBG-4462)
* [CBG-4478 — Db state is stuck in starting after failure in StartOnlineProcesses](https://jira.issues.couchbase.com/browse/CBG-4478)
* [CBG-4512 — Sync Gateway 3.1.9+/3.2.x does not support buckets containing . characters](https://jira.issues.couchbase.com/browse/CBG-4512)
* [CBG-4536 — ISGR fatal connection errors will leak a stats reporter goroutine](https://jira.issues.couchbase.com/browse/CBG-4536)
* [CBG-4554 — import feed: not all DCP streams are open after pindex reconciliation](https://jira.issues.couchbase.com/browse/CBG-4554)
* [CBG-4562 — calling GET /db/\_session/sessionID returns invalidated session](https://jira.issues.couchbase.com/browse/CBG-4562)
* [CBG-4570 — Audit events for database audit are enabled when no per db audit logging config is set](https://jira.issues.couchbase.com/browse/CBG-4570)
* [CBG-4572 — Blip will leak nextFrameToSend goroutines if non ack’d messages are queued](https://jira.issues.couchbase.com/browse/CBG-4572)
* [CBG-4597 — caching dcp feed does not utilize network connstr option](https://jira.issues.couchbase.com/browse/CBG-4597)
* [CBG-4603 — Better handling of pushed deltas when a client doesn’t have access to its parent revision](https://jira.issues.couchbase.com/browse/CBG-4603)
* [CBG-4619 — Documents created with \_attachments property in value fail to sync](https://jira.issues.couchbase.com/browse/CBG-4619)
* [CBG-4654 — Server MgmtRequest panics on request failure](https://jira.issues.couchbase.com/browse/CBG-4654)
* [CBG-4662 — Resync performance degrades over time](https://jira.issues.couchbase.com/browse/CBG-4662)
* [CBG-4666 — Missing response Content-Type on GET /db/role/…​ endpoint](https://jira.issues.couchbase.com/browse/CBG-4666)
* [CBG-4670 — Document import should not write the document body back to bucket](https://jira.issues.couchbase.com/browse/CBG-4670)
* [CBG-4697 — Recover from panics when importing a document via DCP feed](https://jira.issues.couchbase.com/browse/CBG-4697)

### [](#enhancements-4)Enhancements

* [CBG-603 — Throttle changes notify broadcasts under high load to reduce CPU overhead and mutex contention](https://jira.issues.couchbase.com/browse/CBG-603)
* [CBG-2838 — Aggregate system:indexes lookups for collections](https://jira.issues.couchbase.com/browse/CBG-2838)
* [CBG-3692 — Log username for login attempt when user is disabled](https://jira.issues.couchbase.com/browse/CBG-3692)
* [CBG-3693 — Log username for login attempt when OIDC user doesn’t exist and auto-register is disabled](https://jira.issues.couchbase.com/browse/CBG-3693)
* [CBG-3694 — Log username for invalid POST /\_session login attempts](https://jira.issues.couchbase.com/browse/CBG-3694)
* [CBG-4006 — Increase retention time for stats logs](https://jira.issues.couchbase.com/browse/CBG-4006)
* [CBG-4017 — Update go-oidc and go-jose dependencies](https://jira.issues.couchbase.com/browse/CBG-4017)
* [CBG-4065 — Send User-Agent header with ISGR blipsync requests](https://jira.issues.couchbase.com/browse/CBG-4065)
* [CBG-4122 — Support audit log rotation via SIGHUP](https://jira.issues.couchbase.com/browse/CBG-4122)
* [CBG-4135 — Add new metric for rev cache utilization](https://jira.issues.couchbase.com/browse/CBG-4135)
* [CBG-4188 — Metrics related to audit logging](https://jira.issues.couchbase.com/browse/CBG-4188)
* [CBG-4273 — Remove internal BLIP/Websocket frame debug logging](https://jira.issues.couchbase.com/browse/CBG-4273)
* [CBG-4306 — Log which sequences are being abandoned](https://jira.issues.couchbase.com/browse/CBG-4306)
* [CBG-4348 — clarify logs around changes feed](https://jira.issues.couchbase.com/browse/CBG-4348)
* [CBG-4351 — Use skiplist for skipped sequence set](https://jira.issues.couchbase.com/browse/CBG-4351)
* [CBG-4441 — Optimize channel cache LogEntry struct size](https://jira.issues.couchbase.com/browse/CBG-4441)
* [CBG-4456 — Add user xattr key length limit](https://jira.issues.couchbase.com/browse/CBG-4456)
* [CBG-4473 — Reset resync progress when changing set of collections](https://jira.issues.couchbase.com/browse/CBG-4473)
* [CBG-4493 — Improve database startup time when indexes are already initialized and online](https://jira.issues.couchbase.com/browse/CBG-4493)
* [CBG-4510 — sgcollect\_info will throw an exception if -vv is passed](https://jira.issues.couchbase.com/browse/CBG-4510)
* [CBG-4548 — support partitioned indexes](https://jira.issues.couchbase.com/browse/CBG-4548)
* [CBG-4549 — Improve resync reset logging](https://jira.issues.couchbase.com/browse/CBG-4549)
* [CBG-4563 — Add an import\_processed stat to help identify when import is busy/idle](https://jira.issues.couchbase.com/browse/CBG-4563)
* [CBG-4565 — Support principal and partitioned index cleanup via /\_post\_upgrade](https://jira.issues.couchbase.com/browse/CBG-4565)
* [CBG-4587 — Add new async index init API to support zero downtime partitioned index creation](https://jira.issues.couchbase.com/browse/CBG-4587)
* [CBG-4607 — Support principal index creation via /db/\_index\_init](https://jira.issues.couchbase.com/browse/CBG-4607)
* [CBG-4614 — Support new principal indexes](https://jira.issues.couchbase.com/browse/CBG-4614)
* [CBG-4631 — Optimize channel cache ID usage](https://jira.issues.couchbase.com/browse/CBG-4631)
* [CBG-4632 — Optimize channel cache memory allocations (avoid slice growth alloc)](https://jira.issues.couchbase.com/browse/CBG-4632)
* [CBG-4633 — Optimize channel cache memory allocations (avoid redundant map allocs)](https://jira.issues.couchbase.com/browse/CBG-4633)
* [CBG-4634 — Move initialSequence in the cache outside cache mutex ](https://jira.issues.couchbase.com/browse/CBG-4634)
* [CBG-4635 — Reduce cache mutex churn for recent sequences in doc changed handling](https://jira.issues.couchbase.com/browse/CBG-4635)
* [CBG-4636 — Check skipped sequences from potential deduped entries in recent sequences](https://jira.issues.couchbase.com/browse/CBG-4636)
* [CBG-4658 — Prevent javascript stack overflow](https://jira.issues.couchbase.com/browse/CBG-4658)
* [CBG-4661 — Optimize DCP document key filtering](https://jira.issues.couchbase.com/browse/CBG-4661)
* [CBG-4664 — Add metrics for Resync](https://jira.issues.couchbase.com/browse/CBG-4664)
* [CBG-4669 — Reduce redundant info-level resync logging](https://jira.issues.couchbase.com/browse/CBG-4669)
* [CBG-4684 — sgcollect\_info: remove defunct -d flag](https://jira.issues.couchbase.com/browse/CBG-4684)
* [CBG-4688 — Bump Go version](https://jira.issues.couchbase.com/browse/CBG-4688)
* [CBG-4712 — Support non-default admin API port with /sgcollect\_info REST API](https://jira.issues.couchbase.com/browse/CBG-4712)

### [](#known-issues-4)Known Issues

None for this release.

### [](#deprecations-4)Deprecations

* [CBG-4575 — Set default value of allow\_conflicts to false](https://jira.issues.couchbase.com/browse/CBG-4575)
* [CBG-4617 — Allow public /\_all\_docs endpoint to be disabled](https://jira.issues.couchbase.com/browse/CBG-4617)

> [!NOTE]
> For an overview of the latest features offered in Sync Gateway 3.3, see [New In 3.3](../whatsnew.md).

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