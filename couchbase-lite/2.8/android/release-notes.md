---
title: Release Notes
description: Couchbase Lite on Android
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/android/pages/release-notes.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.8@couchbase-lite:android:release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/android/release-notes.html)

# Release Notes

> Description — _Couchbase Lite on Android_  
> _Abstract — This content describes the key features and changes implemented by release 2.8 of Couchbase Lite on Android_  
> Related Content — [What’s New](../../current/cbl-whatsnew.md) | [Compatibility](../../current/android/compatibility.md) | [Supported OS](../../current/android/supported-os.md)

## [](#maint-2)2.8.6 — July 2021

Version 2.8.6 of Couchbase Lite for Android delivers:

* Added support for Android 11 - API v30
* Fixes that improve security and performance.

### [](#enhancements)Enhancements

* [CBL-2001](https://issues.couchbase.com/browse/CBL-2001) — Android v30 compatibility

### [](#issues-and-resolutions-2-8-6)Issues and Resolutions

#### [](#fixed-issues)Fixed Issues

* [CBL-1984](https://issues.couchbase.com/browse/CBL-1984) — Support domain specific server authentication
* [CBL-2037](https://issues.couchbase.com/browse/CBL-2037) — Core pool size is too small

#### [](#known-issues)Known Issues

* [CBL-95](https://issues.couchbase.com/browse/CBL-95) — [Pending conflicts could be resolved by a wrong replicator](https://issues.couchbase.com/browse/CBL-95)

## [](#maint-2)2.8.5 — March 2021

Version 2.8.5 of Couchbase Lite for Android delivers a fix that resolves an issue introduced in the 2.8.4 POM file, which incorrectly listed Kotlin as a dependency. The 2.8.5 release has the corrected POM file.

### [](#issues-and-resolutions-2-8-5)Issues and Resolutions

#### [](#fixed-issues-2)Fixed Issues

* [CBL-1746](https://issues.couchbase.com/browse/CBL-1746) — [Remove extraneous dependency from CBL-Android POM](https://issues.couchbase.com/browse/CBL-1746)

#### [](#known-issues-2)Known Issues

* [CBL-216](https://issues.couchbase.com/browse/CBL-216) — Ordering null values inconsistent with N1QL expectations
* [CBL-95](https://issues.couchbase.com/browse/CBL-95) — Pending conflicts could be resolved by a wrong replicator
* [CBL-49](https://issues.couchbase.com/browse/CBL-49) — Need a way to distinguish boolean types

## [](#maint-2)2.8.4 — March 2021

Version 2.8.4 of Couchbase Lite for Android delivers a number of enhancements and bug fixes.

### [](#enhancements-2)Enhancements

Enhancement highlights include the ability to vary the replicator heartbeat, which keeps continuous replication connections alive when idle — see: [Remote Sync Gateway — Set heartbeat](replication.md#lbl-cfg-htbt)

* [CBL-370](https://issues.couchbase.com/browse/CBL-370) — [API: Kotlin unable to import ReplicatorType. Now resolved](https://issues.couchbase.com/browse/CBL-370)
* [CBL-1549](https://issues.couchbase.com/browse/CBL-1549) — [Handle unrecognized Core states reasonably.](https://issues.couchbase.com/browse/CBL-1549)
* [CBL-1703](https://issues.couchbase.com/browse/CBL-1703) — [Replication retries upto 3 times (at 2 second intervals) after an EOFException fail](https://issues.couchbase.com/browse/CBL-1703)

### [](#issues-and-resolutions-2-8-4)Issues and Resolutions

#### [](#known-issues-3)Known Issues

* [CBL-49](https://issues.couchbase.com/browse/CBL-49) — [Need a way to distinguish boolean types](https://issues.couchbase.com/browse/CBL-49)
* [CBL-95](https://issues.couchbase.com/browse/CBL-95) — [Pending conflicts could be resolved by a wrong replicator](https://issues.couchbase.com/browse/CBL-95)
* [CBL-216](https://issues.couchbase.com/browse/CBL-216) — [Ordering null values inconsistent with N1QL expectations](https://issues.couchbase.com/browse/CBL-216)

#### [](#fixed-issues-3)Fixed Issues

* [CBL-1439](https://issues.couchbase.com/browse/CBL-1439) — [Memory Leak in c4\_setTempDir](https://issues.couchbase.com/browse/CBL-1439)
* [CBL-1513](https://issues.couchbase.com/browse/CBL-1513) — [Stopping status should not be leaked](https://issues.couchbase.com/browse/CBL-1513)
* [CBL-1515](https://issues.couchbase.com/browse/CBL-1515) — [Standardize URL when calculating replication checkpoint](https://issues.couchbase.com/browse/CBL-1515)
* [CBL-1547](https://issues.couchbase.com/browse/CBL-1547) — [Deprecate Replicator.resetCheckpoint() API](https://issues.couchbase.com/browse/CBL-1547)
* [CBL-1663](https://issues.couchbase.com/browse/CBL-1663) — [Poller enters infinite loop at EOF](https://issues.couchbase.com/browse/CBL-1663)

* [CBL-1051](https://issues.couchbase.com/browse/CBL-1051) — [finalizers that attempt to seize locks may timeout](https://issues.couchbase.com/browse/CBL-1051)
* [CBL-1440](https://issues.couchbase.com/browse/CBL-1440) — [FLSliceResult leaks memory](https://issues.couchbase.com/browse/CBL-1440)
* [CBL-1441](https://issues.couchbase.com/browse/CBL-1441) — [Bindings throw exception when Replicator is in STOPPING state](https://issues.couchbase.com/browse/CBL-1441)
* [CBL-1491](https://issues.couchbase.com/browse/CBL-1491) — [Android replicator appears to hang after a few minutes: Root cause](https://issues.couchbase.com/browse/CBL-1491)
* [CBL-1495](https://issues.couchbase.com/browse/CBL-1495) — ["Replicator is stuck in ""connecting"" state: Root cause"](https://issues.couchbase.com/browse/CBL-1495)
* [CBL-1527](https://issues.couchbase.com/browse/CBL-1527) — [Replicator hang or delay updating websocket state](https://issues.couchbase.com/browse/CBL-1527)
* [CBL-1537](https://issues.couchbase.com/browse/CBL-1537) — [Replicator.start() should not be deprecated](https://issues.couchbase.com/browse/CBL-1537)
* [CBL-1566](https://issues.couchbase.com/browse/CBL-1566) — [Ensure c4log\_enableFatalExceptionBacktrace is called](https://issues.couchbase.com/browse/CBL-1566)
* [CBL-1591](https://issues.couchbase.com/browse/CBL-1591) — [Closing a CBLWebsocket while it is CONNECTING causes a crash](https://issues.couchbase.com/browse/CBL-1591)
* [CBL-1624](https://issues.couchbase.com/browse/CBL-1624) — [Core to platform log level set incorrectly.](https://issues.couchbase.com/browse/CBL-1624)

## [](#maint-2)2.8.1 — November 2020

Version 2.8.1 of Couchbase Lite for Android supersedes version 2.8.0 released earlier this year. **If you have already upgraded to 2.8.0 we strongly recommend that you upgrade to version 2.8.1 at the earliest opportunity.**

Couchbase Lite for Android 2.8.1 addresses a backward-compatibility issue ([CBL-1406](https://issues.couchbase.com/browse/CBL-1406)).

### [](#issues-and-resolutions-2-8-1)Issues and Resolutions

#### [](#known-issues-4)Known Issues

* [CBL-370](https://issues.couchbase.com/browse/CBL-370) — API: Kotlin unable to import ReplicatorType
* [CBL-216](https://issues.couchbase.com/browse/CBL-216) — Ordering null values inconsistent with N1QL expectations
* [CBL-95](https://issues.couchbase.com/browse/CBL-95) — Pending conflicts could be resolved by a wrong replicator
* [CBL-49](https://issues.couchbase.com/browse/CBL-49) — Need a way to distinguish boolean types

#### [](#fixed-issues-4)Fixed Issues

* [CBL-1406](https://issues.couchbase.com/browse/CBL-1406) — Couchbase Lite 2.8 apps require you specify the database path explicitly when connecting to pre-2.8 databases (`config.setDirectory()`) — see: [Open database](database.md#open-db)

## [](#major)2.8.0 — October 2020

_Quick Links_: [New Features](#new-features-2-8-0) **|** [Improvements](#improvements-2-8-0) **|** [Issues and Resolutions](#issues-and-resolutions-2-8-0) **|** [Support Notices](#support-notices-2-8-0) **|** [Related Content](#related-content)

### [](#new-features-2-8-0)New Features

#### [](#peer-to-peer-synchronization)Peer-to-Peer Synchronization

Using Couchbase Lite’s Peer-to-Peer Synchronization solution, you can build offline-first applications on edge devices that directly collaborate in secure bi-directional database synchronization without depending on centralized cloud-based control.

The solution provides an out-of-the-box implementation of a websocket based listener for use in peer-to-peer applications communicating over in IP-based networks.

Read More . . . [Landing P2Psync](#couchbase-lite:android:landing-p2psync.adoc)

### [](#improvements-2-8-0)Improvements

#### [](#feature-changes)Feature Changes

None specified in this release

#### [](#other-enhancements)Other Enhancements

* [CBL-1358](https://issues.couchbase.com/browse/CBL-1358) — Deprecate LogDomain.ALL in favor of LogDomain.ALL\_DOMAINS
* [CBL-1357](https://issues.couchbase.com/browse/CBL-1357) — Deprecate Database.compact() in favor of Database.performMaintenance(MaintenanceType.COMPACT)
* [CBL-1356](https://issues.couchbase.com/browse/CBL-1356) — Add constructor BasicAuthenticator(String, char-2-8-0\[\]) and deprecate
* [CBL-989](https://issues.couchbase.com/browse/CBL-989) — Add Maintenance API.
* [CBL-954](https://issues.couchbase.com/browse/CBL-954) — Return 403 for forbidden listener requests
* [CBL-940](https://issues.couchbase.com/browse/CBL-940) — Implement Replicator.start(reset) and deprecate resetCheckpoint()
* [CBL-891](https://issues.couchbase.com/browse/CBL-891) — API: Overload AbstractReplicator.start to take resetCheckpoint argument
* [CBL-773](https://issues.couchbase.com/browse/CBL-773) — Implement new Close and Delete Database (Java)
* [CBL-740](https://issues.couchbase.com/browse/CBL-740) — P2P listener API
* [CBL-638](https://issues.couchbase.com/browse/CBL-638) — Support RevisionID in queries via Meta
* [CBL-441](https://issues.couchbase.com/browse/CBL-441) — Use common error messages
* [CBL-405](https://issues.couchbase.com/browse/CBL-405) — Pending document IDs
* [CBL-394](https://issues.couchbase.com/browse/CBL-394) — Platform WebSocket code should manage HTTP cookies - Android
* [CBL-320](https://issues.couchbase.com/browse/CBL-320) — Public Database.close method
* [CBL-191](https://issues.couchbase.com/browse/CBL-191) — HTTP auth for P2P Listener
* [CBL-164](https://issues.couchbase.com/browse/CBL-164) — CouchbaseLite.getExecutionService() should not be public API
* [CBL-25](https://issues.couchbase.com/browse/CBL-25) — Some (?) ReplicatorChange CouchbaseLiteExceptions contain no message

#### [](#api-changes)API Changes

The API has been enhanced with the following changes:

* The _[Database.close()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-android/com/couchbase/lite/Database.html#close--)_ method now automatically handles stopping open replicators, closing peer-to-peer websocket listener and removing observers for live queries.
* The _[Database.delete()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-android/com/couchbase/lite/Database.html#delete--)_ method now automatically handles stopping open replicators, closing peer-to-peer websocket listener and removing observers for live queries.
* The _[Replicator.isDocumentPending()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-android/com/couchbase/lite/AbstractReplicator.html#isDocumentPending-java.lang.String-)_ method checks whether or not the document with the given ID has any pending revisions to push
* The _[Replicator.getPendingDocumentIds()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-android/com/couchbase/lite/AbstractReplicator.html#getPendingDocumentIds--)_ method gets the Ids of all documents currently pending push
* _[Meta.revisionID](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-android/com/couchbase/lite/Meta.html#revisionID)_ property is now available as a metadata property, which can be accessed directly in queries

### [](#issues-and-resolutions-2-8-0)Issues and Resolutions

#### [](#known-issues-5)Known Issues

* [CBL-1406](https://issues.couchbase.com/browse/CBL-1406) — Couchbase Lite 2.8 apps require you specify the database path explicitly when connecting to pre-2.8 databases (`config.setDirectory()`) — see: [Open database](database.md#open-db)
* [CBL-370](https://issues.couchbase.com/browse/CBL-370) — API: Kotlin unable to import ReplicatorType
* [CBL-216](https://issues.couchbase.com/browse/CBL-216) — Ordering null values inconsistent with N1QL expectations
* [CBL-95](https://issues.couchbase.com/browse/CBL-95) — Pending conflicts could be resolved by a wrong replicator
* [CBL-49](https://issues.couchbase.com/browse/CBL-49) — Need a way to distinguish boolean types

#### [](#fixed-issues-5)Fixed Issues

* [CBL-1141](https://issues.couchbase.com/browse/CBL-1141) — Android cannot use unlinked files
* [CBL-1107](https://issues.couchbase.com/browse/CBL-1107) — Properties beginning with dollar sign not handled correctly
* [CBL-1045](https://issues.couchbase.com/browse/CBL-1045) — Data race in log rollover
* [CBL-978](https://issues.couchbase.com/browse/CBL-978) — Math errors with float → int implicit fleece conversion
* [CBL-977](https://issues.couchbase.com/browse/CBL-977) — Full text search with Left Outer Join causes fields to be null
* [CBL-859](https://issues.couchbase.com/browse/CBL-859) — ChangeEncryptionKey() and save document after creating a brand new Database throws CouchbaseLiteException (SQLiteDomain / 21): bad parameter or other API misuse.
* [CBL-791](https://issues.couchbase.com/browse/CBL-791) — Make resetCheckpoint an argument to Replicator.start
* [CBL-789](https://issues.couchbase.com/browse/CBL-789) — Crash when accessing `connection→name()`
* [CBL-707](https://issues.couchbase.com/browse/CBL-707) — Compaction is ineffective (auto\_vacuum not enabled)
* [CBL-623](https://issues.couchbase.com/browse/CBL-623) — Revision flags get cleared while saving resolved document in Java
* [CBL-614](https://issues.couchbase.com/browse/CBL-614) — Closing a read only database causes errors
* [CBL-609](https://issues.couchbase.com/browse/CBL-609) — Fleece thinks a boolean is a Long
* [CBL-608](https://issues.couchbase.com/browse/CBL-608) — Blob missing content file
* [CBL-594](https://issues.couchbase.com/browse/CBL-594) — Local to Local replication duplicates remote ID
* [CBL-590](https://issues.couchbase.com/browse/CBL-590) — Investigate handling of BLIP 500 errors
* [CBL-578](https://issues.couchbase.com/browse/CBL-578) — Receive rev#1 after rev#2 is saved to DB
* [CBL-565](https://issues.couchbase.com/browse/CBL-565) — Crashes apparently caused by attempting to log after failure
* [CBL-564](https://issues.couchbase.com/browse/CBL-564) — Property alias not working under certain cases
* [CBL-530](https://issues.couchbase.com/browse/CBL-530) — Certain keys in a query can cause segmentation faults
* [CBL-529](https://issues.couchbase.com/browse/CBL-529) — Cannot create an offset query without limit
* [CBL-505](https://issues.couchbase.com/browse/CBL-505) — Android bindings should manage the size of the CCR thread pool
* [CBL-496](https://issues.couchbase.com/browse/CBL-496) — Should not attempt to open the default tmp directory in DBConfig constructor
* [CBL-358](https://issues.couchbase.com/browse/CBL-358) — xsockets doesn’t account for POSIX variations

### [](#support-notices-2-8-0)Support Notices

This section documents any support-related notes, constraints and changes

#### [](#deprecation-notices)Deprecation Notices

Items (features and-or functionality) are marked as deprecated when a more current, and usually enhanced, alternative is available.

Whilst the deprecated item will remain usable, it is no longer supported, and will be removed in a future release. You should plan to move to an alternative, supported, solution as soon as practical.

##### [](#this-release)This Release

* [CBL-1358](https://issues.couchbase.com/browse/CBL-1358) — Deprecate LogDomain.ALL in favor of LogDomain.ALL\_DOMAINS
* [CBL-1357](https://issues.couchbase.com/browse/CBL-1357) — Deprecate Database.compact() in favor of Database.performMaintenance(MaintenanceType.COMPACT)
* [CBL-1356](https://issues.couchbase.com/browse/CBL-1356) — `BasicAuthenticator(String username, String password)` is deprecated — use `BasicAuthenticator(String username, char-2-8-0[] password)`
* [CBL-1350](https://issues.couchbase.com/browse/CBL-1350) — The `Replicator.resetCheckpoint()` API is deprecated — instead, use `Replicator.start(reset)`, where reset is a boolean value
* [CBL-1011](https://issues.couchbase.com/browse/CBL-1011) — Remove deprecated Replicator.resetCheckpoint()
* [CBL-994](https://issues.couchbase.com/browse/CBL-994) — deprecated resetCheckPoint() doesn’t throw exception when replicator is active
* [CBL-791](https://issues.couchbase.com/browse/CBL-791) — Make resetCheckpoint an argument to Replicator.start. `Replicator.start()` API is deprecated — instead, use `Replicator.start(reset)`, where reset is a boolean value
* The [Database.compact()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-android/com/couchbase/lite/Database.html#compact--) method is deprecated at 2.8 — instead use [Database.performMaintenance()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-android/com/couchbase/lite/Database.html#performMaintenance-com.couchbase.lite.MaintenanceType-).

##### [](#ongoing)Ongoing

Support for API 19 and API 21 is deprecated in version 2.6.

#### [](#other-notices)Other Notices

##### [](#new)New

None specified in this release

##### [](#ongoing-2)Ongoing

None specified

## [](#related-content)Related Content

###### [](#)

Product Notes

* [Release Notes](#couchbase-lite:android:{cbl-pg-releasenotes})
* [Compatibility](../../current/android/compatibility.md)
* [Supported OS](../../current/android/supported-os.md)
* [What’s New](../../current/cbl-whatsnew.md)

###### [](#-2)

Starting Points

* [Databases](../../current/android/database.md)
* [Documents](../../current/android/document.md)
* [Blobs](../../current/android/blob.md)
* [Remote Sync using Sync Gateway](../../current/android/replication.md)
* [Handling Data Conflicts](../../current/android/conflict.md)

###### [](#-3)

Tutorials

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)