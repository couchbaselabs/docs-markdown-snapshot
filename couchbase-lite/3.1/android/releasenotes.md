---
title: Release Notes
description: Couchbase Lite on Android
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.1/modules/android/pages/releasenotes.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:3.1@couchbase-lite:android:releasenotes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.1/android/releasenotes.html)

# Release Notes

## [](#maint-3-1-11)3.1.11 — March 2025

Version 3.1.11 for Android delivers the following features and enhancements:

### [](#enhancements)Enhancements

None for this release

### [](#issues-and-resolutions)Issues and Resolutions

* [CBL-6822 - Replicator may hang while stopping the housekeeper task during stop](https://jira.issues.couchbase.com/browse/CBL-6822)

### [](#deprecations)Deprecations

None for this release

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 3.1, see [New in 3.1](../cbl-whatsnew.md)

## [](#maint-3-1-10)3.1.10 — November 2024

Version 3.1.10 for Android delivers the following features and enhancements:

### [](#enhancements-2)Enhancements

None for this release

### [](#issues-and-resolutions-2)Issues and Resolutions

* [CBL-6282 — Replicator starts slowly for big databases](https://jira.issues.couchbase.com/browse/CBL-6282)

### [](#deprecations-2)Deprecations

None for this release

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 3.1, see [New in 3.1](../cbl-whatsnew.md)

## [](#maint-3-1-9)3.1.9 — August 2024

Version 3.1.9 for Android delivers the following features and enhancements:

### [](#enhancements-3)Enhancements

* [CBL-6009 — You can now enable full sync in the database](https://issues.couchbase.com/browse/CBL-6009)

### [](#issues-and-resolutions-3)Issues and Resolutions

* [CBL-5841 — Fixed Java FLSliceResult memory leak](https://issues.couchbase.com/browse/CBL-5841)
* [CBL-5846 — Fixed dates in Parameters cannot be encoded](https://issues.couchbase.com/browse/CBL-5846)
* [CBL-6124 — Fixed call to c4stream\_write with critical array may cause crash](https://issues.couchbase.com/browse/CBL-6124)
* [CBL-5791 — Fixed Socket was not called to close after receiving WebSocket PING Timeout](https://issues.couchbase.com/browse/CBL-5791)
* [CBL-5978 — LiteCore now holds the names of its log domains](https://issues.couchbase.com/browse/CBL-5978)

### [](#deprecations-3)Deprecations

None for this release

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 3.1, see [New in 3.1](../cbl-whatsnew.md)

## [](#maint-3-1-8)3.1.8 — May 2024

Version 3.1.8 for Android delivers the following features and enhancements:

### [](#enhancements-4)Enhancements

None for this release

### [](#issues-and-resolutions-4)Issues and Resolutions

* [CBL-5723 — Ensured replicator syncs do not restart from the beginning when using prebuilt databases synced from Sync Gateway](https://issues.couchbase.com/browse/CBL-5723)

### [](#deprecations-4)Deprecations

None for this release

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 3.1, see [New in 3.1](../cbl-whatsnew.md)

## [](#maint-3-1-7)3.1.7 — May 2024

Version 3.1.7 for Android delivers the following features and enhancements:

### [](#enhancements-5)Enhancements

* [CBL-5645 — Allow to close the socket while connecting to the remote server](https://issues.couchbase.com/browse/CBL-5645)

### [](#issues-and-resolutions-5)Issues and Resolutions

* [CBL-5521 — Fixed N1QL Parser has exponential slowdown for redundant parentheses](https://issues.couchbase.com/browse/CBL-5521)
* [CBL-5569 — Fixed Text Log Files do not have date included in the log timestamp](https://issues.couchbase.com/browse/CBL-5569)
* [CBL-5631 — Fixed pthread\_mutex\_lock called on a destroyed mutex](https://issues.couchbase.com/browse/CBL-5631)
* [CBL-5642 — Fixed Null dereference crash in gotHTTPResponse](https://issues.couchbase.com/browse/CBL-5642)
* [CBL-5652 — Fixed HELIUM: toJSON should throw unchecked exception](https://issues.couchbase.com/browse/CBL-5652)
* [CBL-5653 — Fixed HELIUM: Client Task executor should not fail on RejectedExecution](https://issues.couchbase.com/browse/CBL-5653)
* [CBL-5655 — Fixed HELIUM: Native crash in objects derived from ResultSet](https://issues.couchbase.com/browse/CBL-5655)
* [CBL-5657 — Fixed HELIUM: NativeC4QueryObserver.free should disable the listener before freeing it](https://issues.couchbase.com/browse/CBL-5657)

### [](#known-issues)Known Issues

None for this release

### [](#deprecations-5)Deprecations

None for this release

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 3.1, see [New in 3.1](../cbl-whatsnew.md)

## [](#maint-3-1-6)3.1.6 — March 2024

Version 3.1.6 for Android delivers the following features and enhancements:

### [](#enhancements-6)Enhancements

None for this release

### [](#issues-and-resolutions-6)Issues and Resolutions

* [CBL-5127 — Puller revoked docs now queue with other revs](https://issues.couchbase.com/browse/CBL-5127)
* [CBL-5224 — ReplicatedDocument getters now comply with spec](https://issues.couchbase.com/browse/CBL-5224)
* [CBL-5254 — Sequence index now created on datafile open rather than lazily with replicator start to improve Upsert performance when number of docs increases](https://issues.couchbase.com/browse/CBL-5254)
* [CBL-5259 — Fixed crash in setting Housekeeper::\_doExpiration()](https://issues.couchbase.com/browse/CBL-5259)
* [CBL-5296 — Fixed error messages WARN\_WRONG\_ID and WARN\_WRONG\_COLLECTION](https://issues.couchbase.com/browse/CBL-5296)
* [CBL-5309 — Iterator behavior is now consistent over Documents, Dictionaries and Arrays](https://issues.couchbase.com/browse/CBL-5309)
* [CBL-5401 — JNI LocalRefs are now released on callbacks](https://issues.couchbase.com/browse/CBL-5401)
* [CBL-5448 — Attachments flag is no longer dropped when applying delta to incoming revs](https://issues.couchbase.com/browse/CBL-5448)

### [](#known-issues-2)Known Issues

None for this release

### [](#deprecations-6)Deprecations

* [CBL-5492 — Deprecation of multiple supported platforms](https://issues.couchbase.com/browse/CBL-5492)

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 3.1, see [New in 3.1](../cbl-whatsnew.md)

## [](#maint-3-1-3)3.1.3 — November 2023

Version 3.1.3 for Android delivers the following features and enhancements:

### [](#enhancements-7)Enhancements

* [CBL-4995 — Log the reason why a doc is purged](https://issues.couchbase.com/browse/CBL-4995)

### [](#issues-and-resolutions-7)Issues and Resolutions

* [CBL-5038 — Allow empty Domain list for Console Logger](https://issues.couchbase.com/browse/CBL-5038)
* [CBL-4991 — Fix issue where createC4DocumentChange returned null if called with a null revId. Null is legal and now correctly causes the associated doc to be reported as changed](https://issues.couchbase.com/browse/CBL-4991)
* [CBL-4989 — fix handling of nulls in CollectionChangeNotifier.getChanges()](https://issues.couchbase.com/browse/CBL-4989)
* [CBL-4987 — Remap LiteCore log domain "Changes" to Database domain](https://issues.couchbase.com/browse/CBL-4987)
* [CBL-4950 — fix handling of nulls in ManagedC4Database.finalize()](https://issues.couchbase.com/browse/CBL-4950)
* [CBL-4842 — Fix Logic bug in Conflict Resolver](https://issues.couchbase.com/browse/CBL-4842)
* [CBL-4836 — Lower the max size on the ClientTask thread pool in order to prevent possible Out of Memory condition](https://issues.couchbase.com/browse/CBL-4836)
* [CBL-4789 — Properly handle continuation frames from websockets](https://issues.couchbase.com/browse/CBL-4789)
* [CBL-4705 — Fix cblite export command to work with collections](https://issues.couchbase.com/browse/CBL-4705)
* [CBL-4508 — Fix bug in FLTimestamp\_ToString()](https://issues.couchbase.com/browse/CBL-4508)

### [](#known-issues-3)Known Issues

None for this release

### [](#deprecations-7)Deprecations

None for this release

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 3.1, see [New in 3.1](../cbl-whatsnew.md)

## [](#maint-3-1-2)3.1.2 — September 2023

Version 3.1.2 for Android delivers the following features and enhancements:

### [](#enhancements-8)Enhancements

* [CBL-4836 — The clientTask thread pool has had max size reduced, to remove the risk of an OOM failure.](https://issues.couchbase.com/browse/CBL-4836)
* [CBL-4873 — Some debugging information has been removed from the binaies to reduce their size.](https://issues.couchbase.com/browse/CBL-4873)

### [](#issues-and-resolutions-8)Issues and Resolutions

* [CBL-4894 — A logic bug in Conflict Resolver was causing nearly all replications to be scheduled for conflict resolution. This has been fixed.](https://issues.couchbase.com/browse/CBL-4894)

### [](#known-issues-4)Known Issues

None for this release

### [](#deprecations-8)Deprecations

None for this release

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 3.1, see [New in 3.1](../cbl-whatsnew.md)

## [](#maint-3-1-1)3.1.1 — July 2023

Version 3.1.1 for Android delivers the following features and enhancements:

### [](#enhancements-9)Enhancements

* [CBL-4622 - Remove extraneous logging](https://issues.couchbase.com/browse/CBL-4622)
* [CBL-4665 - Better error message when getCollections returns error](https://issues.couchbase.com/browse/CBL-4665)
* [CBL-4414 - Enhance checkpoint resolution algorithm when local and remote checkpoint are mismatched](https://issues.couchbase.com/browse/CBL-4414)

### [](#issues-and-resolutions-9)Issues and Resolutions

* [CBL-4666 - Proguard rules are not sufficient](https://issues.couchbase.com/browse/CBL-4666)
* [CBL-4664 - Backport to 3.1.1: Client code should not require Spotbugs annotations](https://issues.couchbase.com/browse/CBL-4664)
* [CBL-4643 - Failure in OkHttp authenticator](https://issues.couchbase.com/browse/CBL-4643)
* [CBL-4484 - Workaround for hung db.close()](https://issues.couchbase.com/browse/CBL-4484)
* [CBL-4666 - Proguard rules are not sufficient](https://issues.couchbase.com/browse/CBL-4666)
* [CBL-4623 - Use FTS match() in the WHERE clause of LEFT OUTER JOINS Not Returning Correct Result](https://issues.couchbase.com/browse/CBL-4623)
* [CBL-4535 - Error when saving documents with LiteCore error 17: must be called during a transaction](https://issues.couchbase.com/browse/CBL-4535)
* [CBL-4445 - Replicator is stuck in busy state when there is an error thrown while applying delta to create full fleece doc](https://issues.couchbase.com/browse/CBL-4445)

### [](#issues-and-resolutions-10)Issues and Resolutions

None for this release

### [](#known-issues-5)Known Issues

None for this release

### [](#deprecations-9)Deprecations

None for this release

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 3.1, see [New in 3.1](../cbl-whatsnew.md)

## [](#maint-3-1-0)3.1.0 — March 2023

Version 3.1.0 for Android delivers the following features and enhancements:

### [](#scopes-and-collections)Scopes and Collections

Couchbase Mobile’s cloud-to-edge support for scopes and collections allows application developers to organize and logically isolate data.

Independent lifecycle management and fine-grained security control simplifies the deployment of multi-tenant and high-application density cloud-to-edge applications at scale.

[Scopes and Collections](scopes-collections-manage.md) are a first class concept, synced between Couchbase Lite and Sync Gateway, between Sync Gateways (Inter Sync Gateway Replication), between Couchbase Lite peers, as well as available offline-first on Couchbase Lite devices.

### [](#enhancements-10)Enhancements

* [CBL-4319 - New Scope and Collection API](https://issues.couchbase.com/browse/CBL-4319)
* [CBL-4131 - SQL : Enhance COLLATE syntax to support locales for UNICODE Collator++](https://issues.couchbase.com/browse/CBL-4131)
* [CBL-4121 - Implement AcceptParentDomainCookies API](https://issues.couchbase.com/browse/CBL-4121)
* [CBL-4098 - Provide option to Save Cookie with Domain being a parent domain of the request](https://issues.couchbase.com/browse/CBL-4098)
* [CBL-4009 - New QueryBuilder's FullTextIndexExpression](https://issues.couchbase.com/browse/CBL-4009)
* [CBL-3949 - Support GCLB Cookies](https://issues.couchbase.com/browse/CBL-3949)
* [CBL-3945 - Kotlin/Java: Support GCLB Cookies](https://issues.couchbase.com/browse/CBL-3945)
* [CBL-3916 - Report invalid / unknown network interface using kC4NetErrUnknownInterface](https://issues.couchbase.com/browse/CBL-3916)
* [CBL-3651 - Only send port in HTTP Host header if non-standard](https://issues.couchbase.com/browse/CBL-3651)
* [CBL-3573 - Add info about enhanced certificate pinning](https://issues.couchbase.com/browse/CBL-3573)
* [CBL-3450 - Make FullTextIndex.language and ignoreAccent Getter Public API](https://issues.couchbase.com/browse/CBL-3450)
* [CBL-3414 - Update message for error code CBLErrorNotOpen](https://issues.couchbase.com/browse/CBL-3414)
* [CBL-3211 - Stop mallocing stuff](https://issues.couchbase.com/browse/CBL-3211)
* [CBL-3144 - Remove jetifier, if possible](https://issues.couchbase.com/browse/CBL-3144)
* [CBL-3135 - Correct/document DB operations allowed in a batch transaction](https://issues.couchbase.com/browse/CBL-3135)
* [CBL-3121 - Add ListenerToken.remove()](https://issues.couchbase.com/browse/CBL-3121)
* [CBL-3093 - Add DB closed recommendation to docs for Database.close](https://issues.couchbase.com/browse/CBL-3093)
* [CBL-3085 - Make SSLException a recoverable error in AbstractCBLWebSocket: 3.1](https://issues.couchbase.com/browse/CBL-3085)
* [CBL-2974 - Implement enhanced pinned server certificate feature](https://issues.couchbase.com/browse/CBL-2974)
* [CBL-2970 - Implement the API to specify network interface used by the replicator](https://issues.couchbase.com/browse/CBL-2970)
* [CBL-2509 - Enhance pinned server cert to support matching with parent certs](https://issues.couchbase.com/browse/CBL-2509)
* [CBL-2359 - Convert android.support.annotations to androidx.annotations](https://issues.couchbase.com/browse/CBL-2359)
* [CBL-2270 - Explicitly close c4Documents](https://issues.couchbase.com/browse/CBL-2270)
* [CBL-1960 - Design and implement v30+ file system use](https://issues.couchbase.com/browse/CBL-1960)
* [CBL-1794 - Make better use of C4DocContentLevel](https://issues.couchbase.com/browse/CBL-1794)
* [CBL-1240 - URL listener starts with ugly (but unimportant) KeyStore exception](https://issues.couchbase.com/browse/CBL-1240)
* [CBL-80 - Android specific replication using WorkManager](https://issues.couchbase.com/browse/CBL-80)

### [](#issues-and-resolutions-11)Issues and Resolutions

* [CBL-3866 - Fix WebSocket error 1006, "connection closed abnormally" crash](https://issues.couchbase.com/browse/CBL-3866)
* [CBL-3810 - ReplicatorConfigurationFactory.create() defaults enabledAutoPurge to false](https://issues.couchbase.com/browse/CBL-3810)
* [CBL-3626 - setDocumentExpiration hangs inside a batch transaction](https://issues.couchbase.com/browse/CBL-3626)
* [CBL-3624 - Double free of BLIPIO](https://issues.couchbase.com/browse/CBL-3624)
* [CBL-3612 - Sequence out of sync after out-of-memory error](https://issues.couchbase.com/browse/CBL-3612)
* [CBL-3384 - Worker::childChangedStatus may lose child after enqueued](https://issues.couchbase.com/browse/CBL-3384)
* [CBL-3218 - Enable F\_BARRIERFSYNC in SQLite](https://issues.couchbase.com/browse/CBL-3218)
* [CBL-3192 - Queries don't support result alias with dot](https://issues.couchbase.com/browse/CBL-3192)
* [CBL-3087 - ARRAY\_COUNT() returns incorrect result](https://issues.couchbase.com/browse/CBL-3087)
* [CBL-3075 - Database could be corrupted after being copied in linux platform](https://issues.couchbase.com/browse/CBL-3075)
* [CBL-3055 - Malformed hostname can cause a crash.](https://issues.couchbase.com/browse/CBL-3055)
* [CBL-3046 - Connection Timeout is set to 15000000 Milliseconds on Non Windows Platforms](https://issues.couchbase.com/browse/CBL-3046)
* [CBL-3043 - QueryParser wrong for a case of JOIN](https://issues.couchbase.com/browse/CBL-3043)
* [CBL-3013 - Continuous replicator does not push docs which are being observed](https://issues.couchbase.com/browse/CBL-3013)
* [CBL-2994 - c4DbChanges in AbstractDatabase.postDatabaseChanged may contain nulls](https://issues.couchbase.com/browse/CBL-2994)
* [CBL-2948 - revpos is missing in the changed attachment body when using delta sync (Port)](https://issues.couchbase.com/browse/CBL-2948)
* [CBL-2944 - LiveQuery could crash when removing the listener](https://issues.couchbase.com/browse/CBL-2944)
* [CBL-2940 - Replicator stopped with WebSocket 1008 / SocketTimeoutException when disable WiFi](https://issues.couchbase.com/browse/CBL-2940)
* [CBL-2867 - Cannot update the same field again after reopening the database (Port Fix)](https://issues.couchbase.com/browse/CBL-2867)
* [CBL-2779 - N1QL : Meta().<property> column name returned as $<num>](https://issues.couchbase.com/browse/CBL-2779)
* [CBL-2736 - Incorrect key for SQL Query: "SELECT \* FROM \_default"++](https://issues.couchbase.com/browse/CBL-2736)
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
* [CBL-2417 - Cookies set in Headers are replaced with Session Authenticator's cookies](https://issues.couchbase.com/browse/CBL-2417)
* [CBL-2374 - Slowness from reindexing the database when opening database](https://issues.couchbase.com/browse/CBL-2374)

### [](#known-issues-6)Known Issues

None for this release

### [](#deprecations-10)Deprecations

* [CBL-4324 - Replace database oriented Factory methods with collection oriented equvalents](https://issues.couchbase.com/browse/CBL-4324)
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