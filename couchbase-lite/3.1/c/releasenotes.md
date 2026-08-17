---
title: Release Notes
description: Couchbase Lite on C
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.1/modules/c/pages/releasenotes.adoc
  xref: xref:3.1@couchbase-lite:c:releasenotes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.1/c/releasenotes.html)

# Release Notes

> Description — _Couchbase Lite on C_  
> _Abstract — This content describes the key features and changes implemented by release 3.1 of Couchbase Lite on C_  
> Related Content — [What's New](#cbl-whatsnew.adoc) | [Compatibility](compatibility.md) | [Supported Platforms](supported-os.md)

## [](#maint-3-1-10)3.1.10 — November 2024

Version 3.1.10 for C delivers the following features and enhancements:

### [](#enhancements)Enhancements

None for this release

### [](#issues-and-resolutions)Issues and Resolutions

* [CBL-6282 — Replicator starts slowly for big databases](https://jira.issues.couchbase.com/browse/CBL-6282)
* [CBL-6427 — Fixed crash when calling onWebSocketGotTLSCertificate callback after the connection is closed](https://jira.issues.couchbase.com/browse/CBL-6427)

### [](#deprecations)Deprecations

None for this release

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 3.1, see [New in 3.1](../cbl-whatsnew.md)

## [](#maint-3-1-9)3.1.9 — August 2024

Version 3.1.9 for C delivers the following features and enhancements:

### [](#enhancements-2)Enhancements

* [CBL-6009 — You can now enable full sync in the database](https://issues.couchbase.com/browse/CBL-6009)

### [](#issues-and-resolutions-2)Issues and Resolutions

* [CBL-5791 — Fixed Socket was not called to close after receiving WebSocket PING Timeout](https://issues.couchbase.com/browse/CBL-5791)
* [CBL-5978 — LiteCore now holds the names of its log domains](https://issues.couchbase.com/browse/CBL-5978)

### [](#deprecations-2)Deprecations

None for this release

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 3.1, see [New in 3.1](../cbl-whatsnew.md)

## [](#maint-3-1-7)3.1.7 — May 2024

Version 3.1.7 for C delivers the following features and enhancements:

### [](#enhancements-3)Enhancements

None for this release

### [](#issues-and-resolutions-3)Issues and Resolutions

* [CBL-5521 — Fixed N1QL Parser has exponential slowdown for redundant parentheses](https://issues.couchbase.com/browse/CBL-5521)
* [CBL-5569 — Fixed Text Log Files do not have date included in the log timestamp](https://issues.couchbase.com/browse/CBL-5569)
* [CBL-5606 — Fixed save document could be blocked when using database change listener](https://issues.couchbase.com/browse/CBL-5606)
* [CBL-5631 — Fixed pthread\_mutex\_lock called on a destroyed mutex](https://issues.couchbase.com/browse/CBL-5631)
* [CBL-5642 — Fixed Null dereference crash in gotHTTPResponse](https://issues.couchbase.com/browse/CBL-5642)
* [CBL-5661 — Fixed invalidated context may be used in query observer callback](https://issues.couchbase.com/browse/CBL-5661)

### [](#known-issues)Known Issues

None for this release

### [](#deprecations-3)Deprecations

None for this release

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 3.1, see [New in 3.1](../cbl-whatsnew.md)

## [](#maint-3-1-6)3.1.6 — March 2024

Version 3.1.6 for C delivers the following features and enhancements:

### [](#enhancements-4)Enhancements

None for this release

### [](#issues-and-resolutions-4)Issues and Resolutions

* [CBL-5127 — Puller revoked docs now queue with other revs](https://issues.couchbase.com/browse/CBL-5127)
* [CBL-5254 — Sequence index now created on datafile open rather than lazily with replicator start to improve Upsert performance when number of docs increases](https://issues.couchbase.com/browse/CBL-5254)
* [CBL-5259 — Fixed crash in setting Housekeeper::\_doExpiration()](https://issues.couchbase.com/browse/CBL-5259)
* [CBL-5448 — Attachments flag is no longer dropped when applying delta to incoming revs](https://issues.couchbase.com/browse/CBL-5448)

### [](#known-issues-2)Known Issues

None for this release

### [](#deprecations-4)Deprecations

* [CBL-5492 — Deprecation of multiple supported platforms](https://issues.couchbase.com/browse/CBL-5492)

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 3.1, see [New in 3.1](../cbl-whatsnew.md)

## [](#maint-3-1-3)3.1.3 — November 2023

Version 3.1.3 for C delivers the following features and enhancements:

### [](#enhancements-5)Enhancements

* [CBL-4995 — Log the reason why a doc is purged](https://issues.couchbase.com/browse/CBL-4995)

### [](#issues-and-resolutions-5)Issues and Resolutions

* [CBL-4789 — Properly handle continuation frames from websockets](https://issues.couchbase.com/browse/CBL-4789)
* [CBL-4705 — Fix cblite export command to work with collections](https://issues.couchbase.com/browse/CBL-4705)
* [CBL-4508 — Fix bug in FLTimestamp\_ToString()](https://issues.couchbase.com/browse/CBL-4508)

### [](#known-issues-3)Known Issues

None for this release

### [](#deprecations-5)Deprecations

None for this release

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 3.1, see [New in 3.1](../cbl-whatsnew.md)

## [](#maint-3-1-1)3.1.1 — July 2023

Version 3.1.1 for C delivers the following features and enhancements:

### [](#enhancements-6)Enhancements

* [CBL-4574 - Generate API Doc](https://issues.couchbase.com/browse/CBL-4574)
* [CBL-4665 - Better error message when getCollections returns error](https://issues.couchbase.com/browse/CBL-4665)
* [CBL-4414 - Enhance checkpoint resolution algorithm when local and remote checkpoint are mismatched](https://issues.couchbase.com/browse/CBL-4414)

### [](#issues-and-resolutions-6)Issues and Resolutions

* [CBL-4623 - Use FTS match() in the WHERE clause of LEFT OUTER JOINS Not Returning Correct Result](https://issues.couchbase.com/browse/CBL-4623)
* [CBL-4535 - Error when saving documents with LiteCore error 17: must be called during a transaction](https://issues.couchbase.com/browse/CBL-4535)
* [CBL-4445 - Replicator is stuck in busy state when there is an error thrown while applying delta to create full fleece doc](https://issues.couchbase.com/browse/CBL-4445)

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 3.1, see [New in 3.1](../cbl-whatsnew.md)

## [](#maint-3-1-0)3.1.0 — March 2023

Version 3.1.0 for C delivers the following features and enhancements:

### [](#scopes-and-collections)Scopes and Collections

Couchbase Mobile's cloud-to-edge support for scopes and collections allows application developers to organize and logically isolate data.

Independent lifecycle management and fine-grained security control simplifies the deployment of multi-tenant and high-application density cloud-to-edge applications at scale.

[Scopes and Collections](../android/scopes-collections-manage.md) are a first class concept, synced between Couchbase Lite and Sync Gateway, between Sync Gateways (Inter Sync Gateway Replication), between Couchbase Lite peers, as well as available offline-first on Couchbase Lite devices.

### [](#enhancements-7)Enhancements

* [CBL-4319 - New Scope and Collection API](https://issues.couchbase.com/browse/CBL-4319)
* [CBL-4131 - SQL : Enhance COLLATE syntax to support locales for UNICODE Collator++](https://issues.couchbase.com/browse/CBL-4131)
* [CBL-4098 - Provide option to Save Cookie with Domain being a parent domain of the request](https://issues.couchbase.com/browse/CBL-4098)
* [CBL-3949 - Support GCLB Cookies](https://issues.couchbase.com/browse/CBL-3949)
* [CBL-3914 - Support Android's Logcat for Console Log](https://issues.couchbase.com/browse/CBL-3914)
* [CBL-3651 - Only send port in HTTP Host header if non-standard](https://issues.couchbase.com/browse/CBL-3651)
* [CBL-3450 - Make FullTextIndex.language and ignoreAccent Getter Public API](https://issues.couchbase.com/browse/CBL-3450)
* [CBL-2838 - Enable logs for all domains](https://issues.couchbase.com/browse/CBL-2838)
* [CBL-2509 - Enhance pinned server cert to support matching with parent certs](https://issues.couchbase.com/browse/CBL-2509)

### [](#issues-and-resolutions-7)Issues and Resolutions

* [CBL-4285 - Fix crash in when generating user-agent on Android](https://issues.couchbase.com/browse/CBL-4285)
* [CBL-4172 - Allow docs failed with property encryption / decryption to be retried](https://issues.couchbase.com/browse/CBL-4172)
* [CBL-3866 - Fix WebSocket error 1006, "connection closed abnormally" crash](https://issues.couchbase.com/browse/CBL-3866)
* [CBL-3626 - setDocumentExpiration hangs inside a batch transaction](https://issues.couchbase.com/browse/CBL-3626)
* [CBL-3624 - Double free of BLIPIO](https://issues.couchbase.com/browse/CBL-3624)
* [CBL-3612 - Sequence out of sync after out-of-memory error](https://issues.couchbase.com/browse/CBL-3612)
* [CBL-3609 - Replicator does not retry conflict resolution for preexisting conflicted documents](https://issues.couchbase.com/browse/CBL-3609)
* [CBL-3384 - Worker::childChangedStatus may lose child after enqueued](https://issues.couchbase.com/browse/CBL-3384)
* [CBL-3218 - Enable F\_BARRIERFSYNC in SQLite](https://issues.couchbase.com/browse/CBL-3218)
* [CBL-3192 - Queries don't support result alias with dot](https://issues.couchbase.com/browse/CBL-3192)
* [CBL-3087 - ARRAY\_COUNT() returns incorrect result](https://issues.couchbase.com/browse/CBL-3087)
* [CBL-3075 - Database could be corrupted after being copied in linux platform](https://issues.couchbase.com/browse/CBL-3075)
* [CBL-3046 - Connection Timeout is set to 15000000 Milliseconds on Non Windows Platforms](https://issues.couchbase.com/browse/CBL-3046)
* [CBL-3043 - QueryParser wrong for a case of JOIN](https://issues.couchbase.com/browse/CBL-3043)
* [CBL-3013 - Continuous replicator does not push docs which are being observed](https://issues.couchbase.com/browse/CBL-3013)
* [CBL-2948 - revpos is missing in the changed attachment body when using delta sync (Port)](https://issues.couchbase.com/browse/CBL-2948)
* [CBL-2944 - LiveQuery could crash when removing the listener](https://issues.couchbase.com/browse/CBL-2944)
* [CBL-2868 - EWOULDBLOCK (POSIX 35) causes connection to close](https://issues.couchbase.com/browse/CBL-2868)
* [CBL-2867 - Cannot update the same field again after reopening the database (Port Fix)](https://issues.couchbase.com/browse/CBL-2867)
* [CBL-2802 - Missing FLDeepIterator\_GetParent symbol](https://issues.couchbase.com/browse/CBL-2802)
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
* [CBL-2572 - Database getIndexNames() returns invalid data](https://issues.couchbase.com/browse/CBL-2572)
* [CBL-2563 - Unable to create N1QL Query with Newline](https://issues.couchbase.com/browse/CBL-2563)
* [CBL-2532 - Assertion failure when stopping replicator while replicator is connecting](https://issues.couchbase.com/browse/CBL-2532)
* [CBL-2501 - Replicator won't stop](https://issues.couchbase.com/browse/CBL-2501)
* [CBL-2477 - Tear down DBAccess on stopped instead of on release](https://issues.couchbase.com/browse/CBL-2477)
* [CBL-2460 - Different C4QueryObservers share the same C4QueryEnumerator](https://issues.couchbase.com/browse/CBL-2460)
* [CBL-2459 - A second, new Query observer should be notified immediately.](https://issues.couchbase.com/browse/CBL-2459)
* [CBL-2458 - Changing a Query's parameters should re-notify observers](https://issues.couchbase.com/browse/CBL-2458)
* [CBL-2374 - Slowness from reindexing the database when opening database](https://issues.couchbase.com/browse/CBL-2374)

### [](#known-issues-4)Known Issues

None for this release

### [](#deprecations-6)Deprecations

* [CBL-4316 - Replicator's getPendingDocumentIds() and isDocumentPending(String id) are deprecated](https://issues.couchbase.com/browse/CBL-4316)
* [CBL-4315 - ReplicatorConfiguration's filters and conflict resolver properties are deprecated](https://issues.couchbase.com/browse/CBL-4315)
* [CBL-4314 - ReplicatorConfiguration APIs with Database object are deprecated](https://issues.couchbase.com/browse/CBL-4314)
* [CBL-4306 - DatabaseChange and DatabaseChangeListener are deprecated](https://issues.couchbase.com/browse/CBL-4306)
* [CBL-4304 - Database's Document APIs are deprecated](https://issues.couchbase.com/browse/CBL-4304)

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 3.1, see [New in 3.1](../cbl-whatsnew.md)