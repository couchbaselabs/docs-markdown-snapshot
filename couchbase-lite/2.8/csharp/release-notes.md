---
title: Release Notes
description: Couchbase Lite on C#.Net
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/csharp/pages/release-notes.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.8@couchbase-lite:csharp:release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/csharp/release-notes.html)

# Release Notes

> Description — _Couchbase Lite on C#.Net_  
> _Abstract — This content describes the key features and changes implemented by release 2.8 of Couchbase Lite on C#.Net_  
> Related Content — [What's New](../../current/cbl-whatsnew.md) | [Compatibility](../../current/csharp/compatibility.md) | [Supported OS](../../current/csharp/supported-os.md)

## [](#maint-2)2.8.6 — August 2021

Version 2.8.6 of Couchbase Lite for C#.Net delivers fixes that improve security and performance; specifically resolving memory leak issues.

### [](#issues-and-resolutions-2-8-6-net)Issues and Resolutions

#### [](#fixed-issues)Fixed Issues

* [CBL-2108](https://issues.couchbase.com/browse/CBL-2108) — [Backport — Fix memory leak in WebSocketWrapper](https://issues.couchbase.com/browse/CBL-2108)
* [CBL-2109](https://issues.couchbase.com/browse/CBL-2109) — [Backport — SetPrivateKey failed in .Net Framework ](https://issues.couchbase.com/browse/CBL-2109)
* [CBL-2110](https://issues.couchbase.com/browse/CBL-2110) — [Backport — Memory leak when calling MutableArrayObject.AddBlob](https://issues.couchbase.com/browse/CBL-2110)
* [CBL-2120](https://issues.couchbase.com/browse/CBL-2120) — [Retain c4socket when WebSocket starts and a release c4socket after c4socket is closed](https://issues.couchbase.com/browse/CBL-2120)

#### [](#known-issues)Known Issues

* [CBL-95](https://issues.couchbase.com/browse/CBL-95) — [Pending conflicts could be resolved by a wrong replicator](https://issues.couchbase.com/browse/CBL-95)

## [](#maint-2)2.8.4 — March 2021

Version 2.8.4 of Couchbase Lite for C#.Net delivers a number of enhancements and bug fixes.

### [](#enhancements)Enhancements

Enhancement highlights include the ability to vary the replicator heartbeat, which keeps continuous replication connections alive when idle — see: [Remote Sync Gateway — Set heartbeat](replication.md#lbl-cfg-htbt)

* [CBL-1579](https://issues.couchbase.com/browse/CBL-1579) — [Add replication heartbeat](https://issues.couchbase.com/browse/CBL-1579)

### [](#issues-and-resolutions-2-8-4)Issues and Resolutions

#### [](#known-issues-2)Known Issues

* [CBL-49](https://issues.couchbase.com/browse/CBL-49) — [Need a way to distinguish boolean types](https://issues.couchbase.com/browse/CBL-49)
* [CBL-95](https://issues.couchbase.com/browse/CBL-95) — [Pending conflicts could be resolved by a wrong replicator](https://issues.couchbase.com/browse/CBL-95)
* [CBL-216](https://issues.couchbase.com/browse/CBL-216) — [Ordering null values inconsistent with N1QL expectations](https://issues.couchbase.com/browse/CBL-216)

#### [](#fixed-issues-2)Fixed Issues

* [CBL-1439](https://issues.couchbase.com/browse/CBL-1439) — [Memory Leak in c4\_setTempDir](https://issues.couchbase.com/browse/CBL-1439)
* [CBL-1513](https://issues.couchbase.com/browse/CBL-1513) — [Stopping status should not be leaked](https://issues.couchbase.com/browse/CBL-1513)
* [CBL-1515](https://issues.couchbase.com/browse/CBL-1515) — [Standardize URL when calculating replication checkpoint](https://issues.couchbase.com/browse/CBL-1515)
* [CBL-1547](https://issues.couchbase.com/browse/CBL-1547) — [Deprecate Replicator.resetCheckpoint() API](https://issues.couchbase.com/browse/CBL-1547)
* [CBL-1663](https://issues.couchbase.com/browse/CBL-1663) — [Poller enters infinite loop at EOF](https://issues.couchbase.com/browse/CBL-1663)

* [CBL-1476](https://issues.couchbase.com/browse/CBL-1476) — [Add Support For DNS Proxy Addresses](https://issues.couchbase.com/browse/CBL-1476)

## [](#maint-2)2.8.2 — November 2020

Version 2.8.2 of Couchbase Lite for C#.Net comprises a number of fixes. It supersedes version 2.8.0 released earlier this year.

**If you have already upgraded to 2.8.0 we strongly recommend that you upgrade to version 2.8.1 at the earliest opportunity.**

### [](#issues-and-resolutions-2-8-2)Issues and Resolutions

#### [](#known-issues-3)Known Issues

* [CBL-216](https://issues.couchbase.com/browse/CBL-216) — Ordering null values inconsistent with N1QL expectations
* [CBL-95](https://issues.couchbase.com/browse/CBL-95) — Pending conflicts could be resolved by a wrong replicator
* [CBL-49](https://issues.couchbase.com/browse/CBL-49) — Need a way to distinguish boolean types

#### [](#fixed-issues-3)Fixed Issues

* [CBL-1400](https://issues.couchbase.com/browse/CBL-1400) TestAcceptOnlySelfSignedCertMode test failed on Win32
* [CBL-1437](https://issues.couchbase.com/browse/CBL-1437)TlsCertificateException thrown with "A non self-signed certificate was received in self-signed mode." with P2P default TLS on Xamarin iOS 12.x

## [](#major)2.8.0 — October 2020

_Quick Links_: [New Features](#new-features-2-8-0) **|** [Improvements](#improvements-2-8-0) **|** [Issues and Resolutions](#issues-and-resolutions-2-8-0) **|** [Support Notices](#support-notices-2-8-0) **|** [Related Content](#related-content)

### [](#new-features-2-8-0)New Features

#### [](#peer-to-peer-synchronization)Peer-to-Peer Synchronization

Using Couchbase Lite's Peer-to-Peer Synchronization solution, you can build offline-first applications on edge devices that directly collaborate in secure bi-directional database synchronization without depending on centralized cloud-based control.

The solution provides an out-of-the-box implementation of a websocket based listener for use in peer-to-peer applications communicating over in IP-based networks.

Read More . . . [Landing P2Psync](#couchbase-lite:csharp:landing-p2psync.adoc)

### [](#improvements-2-8-0)Improvements

#### [](#feature-changes)Feature Changes

None specified in this release

#### [](#other-enhancements)Other Enhancements

* [CBL-992](https://issues.couchbase.com/browse/CBL-992) — Add Maintenance API.
* [CBL-954](https://issues.couchbase.com/browse/CBL-954) — Return 403 for forbidden listener requests
* [CBL-891](https://issues.couchbase.com/browse/CBL-891) — API: Overload AbstractReplicator.start to take resetCheckpoint argument
* [CBL-740](https://issues.couchbase.com/browse/CBL-740) — P2P listener API
* [CBL-638](https://issues.couchbase.com/browse/CBL-638) — Support RevisionID in queries via Meta
* [CBL-405](https://issues.couchbase.com/browse/CBL-405) — Pending document IDs
* [CBL-320](https://issues.couchbase.com/browse/CBL-320) — Public Database.close method
* [CBL-191](https://issues.couchbase.com/browse/CBL-191) — HTTP auth for P2P Listener

#### [](#api-changes)API Changes

The API has been enhanced with the following changes:

* The _[Database.Close()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Database.html#Couchbase%5FLite%5FDatabase%5FClose)_ method now automatically handles stopping open replicators, closing peer-to-peer websocket listener and removing observers for live queries.
* The _[Database.Delete()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Database.html#Couchbase%5FLite%5FDatabase%5FDelete)_ method now automatically handles stopping open replicators, closing peer-to-peer websocket listener and removing observers for live queries.
* The _[Replicator.IsDocumentPending()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.Replicator.html#Couchbase%5FLite%5FSync%5FReplicator%5FIsDocumentPending%5FSystem%5FString%5F)_ method checks whether or not the document with the given ID has any pending revisions to push
* The _[Replicator.GetPendingDocumentIDs()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Sync.Replicator.html#Couchbase%5FLite%5FSync%5FReplicator%5FGetPendingDocumentIDs)_ method gets the Ids of all documents currently pending push
* _[Meta.revisionID](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Query.Meta.html#Couchbase%5FLite%5FQuery%5FMeta%5FRevisionID)_ property is now available as a metadata property, which can be accessed directly in queries

### [](#issues-and-resolutions-2-8-0)Issues and Resolutions

#### [](#known-issues-4)Known Issues

* [CBL-216](https://issues.couchbase.com/browse/CBL-216) — Ordering null values inconsistent with N1QL expectations
* [CBL-95](https://issues.couchbase.com/browse/CBL-95) — Pending conflicts could be resolved by a wrong replicator
* [CBL-49](https://issues.couchbase.com/browse/CBL-49) — Need a way to distinguish boolean types

#### [](#fixed-issues-4)Fixed Issues

* [CBL-1215](https://issues.couchbase.com/browse/CBL-1215) — Xamarin android takes longer to re-establish the replication connection switch from offline to online the 2nd + time
* [CBL-1141](https://issues.couchbase.com/browse/CBL-1141) — Android cannot use unlinked files
* [CBL-1107](https://issues.couchbase.com/browse/CBL-1107) — Properties beginning with dollar sign not handled correctly
* [CBL-1045](https://issues.couchbase.com/browse/CBL-1045) — Data race in log rollover
* [CBL-978](https://issues.couchbase.com/browse/CBL-978) — Math errors with float → int implicit fleece conversion
* [CBL-977](https://issues.couchbase.com/browse/CBL-977) — Full text search with Left Outer Join causes fields to be null
* [CBL-859](https://issues.couchbase.com/browse/CBL-859) — ChangeEncryptionKey() and save document after creating a brand new Database throws CouchbaseLiteException (SQLiteDomain / 21): bad parameter or other API misuse.
* [CBL-789](https://issues.couchbase.com/browse/CBL-789) — Crash when accessing `connection→name()`
* [CBL-707](https://issues.couchbase.com/browse/CBL-707) — Compaction is ineffective (auto\_vacuum not enabled)
* [CBL-614](https://issues.couchbase.com/browse/CBL-614) — Closing a read only database causes errors
* [CBL-609](https://issues.couchbase.com/browse/CBL-609) — Fleece thinks a boolean is a Long
* [CBL-594](https://issues.couchbase.com/browse/CBL-594) — Local to Local replication duplicates remote ID
* [CBL-590](https://issues.couchbase.com/browse/CBL-590) — Investigate handling of BLIP 500 errors
* [CBL-578](https://issues.couchbase.com/browse/CBL-578) — Receive rev#1 after rev#2 is saved to DB
* [CBL-565](https://issues.couchbase.com/browse/CBL-565) — Crashes apparently caused by attempting to log after failure
* [CBL-564](https://issues.couchbase.com/browse/CBL-564) — Property alias not working under certain cases
* [CBL-530](https://issues.couchbase.com/browse/CBL-530) — Certain keys in a query can cause segmentation faults
* [CBL-529](https://issues.couchbase.com/browse/CBL-529) — Cannot create an offset query without limit
* [CBL-396](https://issues.couchbase.com/browse/CBL-396) — Platform WebSocket code should manage HTTP cookies - .NET
* [CBL-358](https://issues.couchbase.com/browse/CBL-358) — xsockets doesn't account for POSIX variations

### [](#support-notices-2-8-0)Support Notices

This section documents any support-related notes, constraints and changes

#### [](#deprecation-notices)Deprecation Notices

Items (features and-or functionality) are marked as deprecated when a more current, and usually enhanced, alternative is available.

Whilst the deprecated item will remain usable, it is no longer supported, and will be removed in a future release. You should plan to move to an alternative, supported, solution as soon as practical.

##### [](#this-release)This Release

* [CBL-1009](https://issues.couchbase.com/browse/CBL-1009) — The `Replicator.ResetCheckpoint()` API is deprecated at version 2.8\. Use `Replicator.Start(reset)`, where reset is a boolean value
* The [Database.Compact()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Database.html#Couchbase%5FLite%5FDatabase%5FCompact) method is deprecated at 2.8 — instead use [Database.PerformMaintenance()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net/api/Couchbase.Lite.Database.html#Couchbase%5FLite%5FDatabase%5FPerformMaintenance-com.couchbase.lite.MaintenanceType-).

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

* [Release Notes](#couchbase-lite:csharp:{cbl-pg-releasenotes})
* [Compatibility](../../current/csharp/compatibility.md)
* [Supported OS](../../current/csharp/supported-os.md)
* [What's New](../../current/cbl-whatsnew.md)

###### [](#-2)

Starting Points

* [Databases](../../current/csharp/database.md)
* [Documents](../../current/csharp/document.md)
* [Blobs](../../current/csharp/blob.md)
* [Remote Sync using Sync Gateway](../../current/csharp/replication.md)
* [Handling Data Conflicts](../../current/csharp/conflict.md)

###### [](#-3)

Tutorials

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)