---
title: Release Notes
description: Couchbase Lite on Swift
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.1/modules/swift/pages/releasenotes.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:3.1@couchbase-lite:swift:releasenotes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.1/swift/releasenotes.html)

# Release Notes

## [](#maint-3-1-10)3.1.10 — November 2024

Version 3.1.10 for Swift delivers the following features and enhancements:

### [](#enhancements)Enhancements

None for this release

### [](#issues-and-resolutions)Issues and Resolutions

* [CBL-6282 — Replicator starts slowly for big databases](https://jira.issues.couchbase.com/browse/CBL-6282)
* [CBL-6194 — Client Side Proxy CONNECT request is broken](https://jira.issues.couchbase.com/browse/CBL-6194)

### [](#deprecations)Deprecations

None for this release

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 3.1, see [New in 3.1](../cbl-whatsnew.md)

## [](#maint-3-1-9)3.1.9 — August 2024

Version 3.1.9 for Swift delivers the following features and enhancements:

### [](#enhancements-2)Enhancements

* [CBL-6009 — You can now enable full sync in the database](https://issues.couchbase.com/browse/CBL-6009)

### [](#issues-and-resolutions-2)Issues and Resolutions

* [CBL-5221 — Fixed MutableDocument not usable before creating a database instance](https://issues.couchbase.com/browse/CBL-5221)
* [CBL-5329 — Fixed Replicatpr’s ListenerToken.remove() not removing the listener](https://issues.couchbase.com/browse/CBL-5329)
* [CBL-6023 — Fixed Live Query could become nil before is stopped](https://issues.couchbase.com/browse/CBL-6023)
* [CBL-6024 — Fixed Swift MutableDocument’s collection is not set when a new document is saved](https://issues.couchbase.com/browse/CBL-6024)
* [CBL-5791 — Fixed Socket was not called to close after receiving WebSocket PING Timeout](https://issues.couchbase.com/browse/CBL-5791)
* [CBL-5978 — LiteCore now holds the names of its log domains](https://issues.couchbase.com/browse/CBL-5978)

### [](#deprecations-2)Deprecations

None for this release

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 3.1, see [New in 3.1](../cbl-whatsnew.md)

## [](#maint-3-1-7)3.1.7 — May 2024

Version 3.1.7 for Swift delivers the following features and enhancements:

### [](#enhancements-3)Enhancements

* [CBL-5458 — Added missing Objective-C symbols in the exp file](https://issues.couchbase.com/browse/CBL-5458)
* [CBL-5544 — Added missing required keys to Privacy Manifest file](https://issues.couchbase.com/browse/CBL-5544)

### [](#issues-and-resolutions-3)Issues and Resolutions

* [CBL-5521 — Fixed N1QL Parser has exponential slowdown for redundant parentheses](https://issues.couchbase.com/browse/CBL-5521)
* [CBL-5569 — Fixed Text Log Files do not have date included in the log timestamp](https://issues.couchbase.com/browse/CBL-5569)
* [CBL-5631 — Fixed pthread\_mutex\_lock called on a destroyed mutex](https://issues.couchbase.com/browse/CBL-5631)
* [CBL-5642 — Fixed Null dereference crash in gotHTTPResponse](https://issues.couchbase.com/browse/CBL-5642)
* [CBL-5659 — Fixed invalidated context may be used in query observer callback](https://issues.couchbase.com/browse/CBL-5659)

### [](#known-issues)Known Issues

None for this release

### [](#deprecations-3)Deprecations

None for this release

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 3.1, see [New in 3.1](../cbl-whatsnew.md)

## [](#maint-3-1-6)3.1.6 — March 2024

Version 3.1.6 for Swift delivers the following features and enhancements:

### [](#enhancements-4)Enhancements

None for this release.

### [](#issues-and-resolutions-4)Issues and Resolutions

* [CBL-5074 — Fixed background logic to cover conflict resolution](https://issues.couchbase.com/browse/CBL-5074)
* [CBL-5077 — Fixed Close database race condition hanging](https://issues.couchbase.com/browse/CBL-5077)
* [CBL-5127 — Puller revoked docs now queue with other revs](https://issues.couchbase.com/browse/CBL-5127)
* [CBL-5254 — Sequence index now created on datafile open rather than lazily with replicator start to improve Upsert performance when number of docs increases](https://issues.couchbase.com/browse/CBL-5254)
* [CBL-5259 — Fixed crash in setting Housekeeper::\_doExpiration()](https://issues.couchbase.com/browse/CBL-5259)
* [CBL-5362 — Network streams are now disconnected before CBLWebsocket is deallocated](https://issues.couchbase.com/browse/CBL-5362)
* [CBL-5448 — Attachments flag is no longer dropped when applying delta to incoming revs](https://issues.couchbase.com/browse/CBL-5448)

### [](#known-issues-2)Known Issues

None for this release

### [](#deprecations-4)Deprecations

* [CBL-5492 — Deprecation of multiple supported platforms](https://issues.couchbase.com/browse/CBL-5492)

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 3.1, see [New in 3.1](../cbl-whatsnew.md)

## [](#maint-3-1-4)3.1.4 — January 2024

Version 3.1.4 for Swift delivers the following features and enhancements:

### [](#enhancements-5)Enhancements

None for this release.

### [](#issues-and-resolutions-5)Issues and Resolutions

* [CBL-4428 — Fixed crash when starting multiple live queries concurrently](https://issues.couchbase.com/browse/CBL-4428)

### [](#known-issues-3)Known Issues

None for this release

### [](#deprecations-5)Deprecations

None for this release

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 3.1, see [New in 3.1](../cbl-whatsnew.md)

## [](#maint-3-1-3)3.1.3 — November 2023

Version 3.1.3 for Swift delivers the following features and enhancements:

### [](#enhancements-6)Enhancements

* [CBL-4995 — Log the reason why a doc is purged](https://issues.couchbase.com/browse/CBL-4995)

### [](#issues-and-resolutions-6)Issues and Resolutions

* [CBL-4981 — Remap LiteCore log domain "Changes" to Database domain](https://issues.couchbase.com/browse/CBL-4981)
* [CBL-4789 — Properly handle continuation frames from websockets](https://issues.couchbase.com/browse/CBL-4789)
* [CBL-4705 — Fix cblite export command to work with collections](https://issues.couchbase.com/browse/CBL-4705)
* [CBL-4508 — Fix bug in FLTimestamp\_ToString()](https://issues.couchbase.com/browse/CBL-4508)

### [](#known-issues-4)Known Issues

None for this release

### [](#deprecations-6)Deprecations

None for this release

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 3.1, see [New in 3.1](../cbl-whatsnew.md)

## [](#maint-3-1-1)3.1.1 — July 2023

Version 3.1.1 for Swift delivers the following features and enhancements:

### [](#enhancements-7)Enhancements

* [CBL-4627 - Update iOS target version to 11.0](https://issues.couchbase.com/browse/CBL-4627)
* [CBL-4543 - Correct min target version for iOS and macOS](https://issues.couchbase.com/browse/CBL-4543)
* [CBL-4486 - Build release framework without bitcode enabled](https://issues.couchbase.com/browse/CBL-4486)
* [CBL-4665 - Better error message when getCollections returns error](https://issues.couchbase.com/browse/CBL-4665)
* [CBL-4631 - Update iOS target version to 11.0](https://issues.couchbase.com/browse/CBL-4631)
* [CBL-4625 - Set macOS target version to 10.14](https://issues.couchbase.com/browse/CBL-4625)
* [CBL-4414 - Enhance checkpoint resolution algorithm when local and remote checkpoint are mismatched](https://issues.couchbase.com/browse/CBL-4414)
* [CBL-4630 - Update iOS target version to 11.0](https://issues.couchbase.com/browse/CBL-4630)
* [CBL-4488 - Build release framework without bitcode enabled](https://issues.couchbase.com/browse/CBL-4488)
* [CBL-4633 - Update iOS target version to 11.0](https://issues.couchbase.com/browse/CBL-4633)

### [](#issues-and-resolutions-7)Issues and Resolutions

* [CBL-4581 - MutableDocument contains(key: String) returns wrong result](https://issues.couchbase.com/browse/CBL-4581)
* [CBL-4511 - Update Database API deprecation messages](https://issues.couchbase.com/browse/CBL-4511)
* [CBL-4443 - CBLCollection could be leaked if document listener token is not removed](https://issues.couchbase.com/browse/CBL-4443)
* [CBL-4438 - Collection.addDocumentChangeListener() can fatal crash](https://issues.couchbase.com/browse/CBL-4438)
* [CBL-4437 - Change Database removeChangeListener() deprecation message](https://issues.couchbase.com/browse/CBL-4437)
* [CBL-4623 - Use FTS match() in the WHERE clause of LEFT OUTER JOINS Not Returning Correct Result](https://issues.couchbase.com/browse/CBL-4623)
* [CBL-4535 - Error when saving documents with LiteCore error 17: must be called during a transaction](https://issues.couchbase.com/browse/CBL-4535)
* [CBL-4445 - Replicator is stuck in busy state when there is an error thrown while applying delta to create full fleece doc](https://issues.couchbase.com/browse/CBL-4445)

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 3.1, see [New in 3.1](../cbl-whatsnew.md)

## [](#maint-3-1-0)3.1.0 — March 2023

Version 3.1.0 for Swift delivers the following features and enhancements:

### [](#scopes-and-collections)Scopes and Collections

Couchbase Mobile’s cloud-to-edge support for scopes and collections allows application developers to organize and logically isolate data.

Independent lifecycle management and fine-grained security control simplifies the deployment of multi-tenant and high-application density cloud-to-edge applications at scale.

[Scopes and Collections](../android/scopes-collections-manage.md) are a first class concept, synced between Couchbase Lite and Sync Gateway, between Sync Gateways (Inter Sync Gateway Replication), between Couchbase Lite peers, as well as available offline-first on Couchbase Lite devices.

### [](#enhancements-8)Enhancements

* [CBL-4319 - New Scope and Collection API](https://issues.couchbase.com/browse/CBL-4319)
* [CBL-4318 - New ListenerToken.remove()](https://issues.couchbase.com/browse/CBL-4318)
* [CBL-4131 - SQL : Enhance COLLATE syntax to support locales for UNICODE Collator++](https://issues.couchbase.com/browse/CBL-4131)
* [CBL-4098 - Provide option to Save Cookie with Domain being a parent domain of the request](https://issues.couchbase.com/browse/CBL-4098)
* [CBL-4008 - New QueryBuilder's FullTextIndexExpression](https://issues.couchbase.com/browse/CBL-4008)
* [CBL-3949 - Support GCLB Cookies](https://issues.couchbase.com/browse/CBL-3949)
* [CBL-3651 - Only send port in HTTP Host header if non-standard](https://issues.couchbase.com/browse/CBL-3651)
* [CBL-2829 - New API for specifying network interface used by the replicator](https://issues.couchbase.com/browse/CBL-2829)
* [CBL-2691 - New Swift QuerySortOrder to avoid API ambiguous error from Xcode 13+](https://issues.couchbase.com/browse/CBL-2691)

### [](#issues-and-resolutions-8)Issues and Resolutions

* [CBL-3866 - Fix WebSocket error 1006, "connection closed abnormally" crash](https://issues.couchbase.com/browse/CBL-3866)
* [CBL-3626 - setDocumentExpiration hangs inside a batch transaction](https://issues.couchbase.com/browse/CBL-3626)
* [CBL-3624 - Double free of BLIPIO](https://issues.couchbase.com/browse/CBL-3624)
* [CBL-3612 - Sequence out of sync after out-of-memory error](https://issues.couchbase.com/browse/CBL-3612)
* [CBL-3384 - Worker::childChangedStatus may lose child after enqueued](https://issues.couchbase.com/browse/CBL-3384)
* [CBL-3218 - Enable F\_BARRIERFSYNC in SQLite](https://issues.couchbase.com/browse/CBL-3218)
* [CBL-3192 - Queries don't support result alias with dot](https://issues.couchbase.com/browse/CBL-3192)
* [CBL-3087 - ARRAY\_COUNT() returns incorrect result](https://issues.couchbase.com/browse/CBL-3087)
* [CBL-3075 - Database could be corrupted after being copied in linux platform](https://issues.couchbase.com/browse/CBL-3075)
* [CBL-3046 - Connection Timeout is set to 15000000 Milliseconds on Non Windows Platforms](https://issues.couchbase.com/browse/CBL-3046)
* [CBL-3043 - QueryParser wrong for a case of JOIN](https://issues.couchbase.com/browse/CBL-3043)
* [CBL-3013 - Continuous replicator does not push docs which are being observed](https://issues.couchbase.com/browse/CBL-3013)
* [CBL-2983 - Missing Objective-C Index Configuration Symbols](https://issues.couchbase.com/browse/CBL-2983)
* [CBL-2948 - revpos is missing in the changed attachment body when using delta sync (Port)](https://issues.couchbase.com/browse/CBL-2948)
* [CBL-2944 - LiveQuery could crash when removing the listener](https://issues.couchbase.com/browse/CBL-2944)
* [CBL-2867 - Cannot update the same field again after reopening the database (Port Fix)](https://issues.couchbase.com/browse/CBL-2867)
* [CBL-2826 - Losing \_attachment when pushing an updated doc to SG](https://issues.couchbase.com/browse/CBL-2826)
* [CBL-2779 - N1QL : Meta().<property> column name returned as $<num>](https://issues.couchbase.com/browse/CBL-2779)
* [CBL-2721 - Database is closed while replicator change listener is still executing](https://issues.couchbase.com/browse/CBL-2721)
* [CBL-2693 - LiveQuerier could be leaked as liveQuerierStopped() delegate might not be called](https://issues.couchbase.com/browse/CBL-2693)
* [CBL-2692 - Closing db with active live query causes crash](https://issues.couchbase.com/browse/CBL-2692)
* [CBL-2676 - 409 retry can result in invalid remote ancestor ID](https://issues.couchbase.com/browse/CBL-2676)
* [CBL-2637 - Replication unable to continue after termination between rev and ack](https://issues.couchbase.com/browse/CBL-2637)
* [CBL-2614 - Fix Memory leak when rapidly restarting replicator](https://issues.couchbase.com/browse/CBL-2614)
* [CBL-2610 - Cleanup bundle folder when creating a database fails](https://issues.couchbase.com/browse/CBL-2610)
* [CBL-2592 - Fix dereference of empty Optional](https://issues.couchbase.com/browse/CBL-2592)
* [CBL-2586 - LiveQuerier is running after having been stopped, causing a crash](https://issues.couchbase.com/browse/CBL-2586)
* [CBL-2563 - Unable to create N1QL Query with Newline](https://issues.couchbase.com/browse/CBL-2563)
* [CBL-2532 - Assertion failure when stopping replicator while replicator is connecting](https://issues.couchbase.com/browse/CBL-2532)
* [CBL-2501 - Replicator won't stop](https://issues.couchbase.com/browse/CBL-2501)
* [CBL-2477 - Tear down DBAccess on stopped instead of on release](https://issues.couchbase.com/browse/CBL-2477)
* [CBL-2460 - Different C4QueryObservers share the same C4QueryEnumerator](https://issues.couchbase.com/browse/CBL-2460)
* [CBL-2459 - A second, new Query observer should be notified immediately.](https://issues.couchbase.com/browse/CBL-2459)
* [CBL-2458 - Changing a Query's parameters should re-notify observers](https://issues.couchbase.com/browse/CBL-2458)
* [CBL-2374 - Slowness from reindexing the database when opening database](https://issues.couchbase.com/browse/CBL-2374)

### [](#known-issues-5)Known Issues

None for this release

### [](#deprecations-7)Deprecations

* [CBL-4316 - Replicator's getPendingDocumentIds() and isDocumentPending(String id) are deprecated](https://issues.couchbase.com/browse/CBL-4316)
* [CBL-4315 - ReplicatorConfiguration's filters and conflict resolver properties are deprecated](https://issues.couchbase.com/browse/CBL-4315)
* [CBL-4314 - ReplicatorConfiguration APIs with Database object are deprecated](https://issues.couchbase.com/browse/CBL-4314)
* [CBL-4313 - MessageEndpointListenerConfiguration APIs using Database object are deprecated](https://issues.couchbase.com/browse/CBL-4313)
* [CBL-4312 - URLEndpointListenerConfiguration APIs using Database object are deprecated](https://issues.couchbase.com/browse/CBL-4312)
* [CBL-4311 - QueryBuilder : isNullOrMissing() and notNullOrMissing() are deprecated](https://issues.couchbase.com/browse/CBL-4311)
* [CBL-4310 - QueryBuilder : FullTextFunction's rank(String index) and match(String index, String query) are deprecated](https://issues.couchbase.com/browse/CBL-4310)
* [CBL-4309 - QueryBuilder : DataSource's database() is deprecated](https://issues.couchbase.com/browse/CBL-4309)
* [CBL-4307 - DocumentChange's database property is deprecated](https://issues.couchbase.com/browse/CBL-4307)
* [CBL-4306 - DatabaseChange and DatabaseChangeListener are deprecated](https://issues.couchbase.com/browse/CBL-4306)
* [CBL-4305 - Database's removeChangeListener() is deprecated](https://issues.couchbase.com/browse/CBL-4305)
* [CBL-4304 - Database's Document APIs are deprecated](https://issues.couchbase.com/browse/CBL-4304)

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 3.1, see [New in 3.1](../cbl-whatsnew.md)