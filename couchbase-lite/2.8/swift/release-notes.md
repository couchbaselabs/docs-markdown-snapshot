---
title: Release Notes
description: Couchbase Lite on Swift
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/swift/pages/release-notes.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.8@couchbase-lite:swift:release-notes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/swift/release-notes.html)

# Release Notes

> Description — _Couchbase Lite on Swift_  
> _Abstract — This content describes the key features and changes implemented by release 2.8 of Couchbase Lite on Swift_  
> Related Content — [What’s New](../../current/cbl-whatsnew.md) | [Compatibility](../../current/swift/compatibility.md) | [Supported OS](../../current/swift/supported-os.md)

## [](#maint-2)2.8.4 — March 2021

Version 2.8.4 of Couchbase Lite for Swift delivers a number of enhancements and bug fixes.

### [](#enhancements)Enhancements

Enhancement highlights include the ability to vary the replicator heartbeat, which keeps continuous replication connections alive when idle — see: [Remote Sync Gateway — Set heartbeat](replication.md#lbl-cfg-htbt)

Couchbase Lite for Swift will now support Apple Silicon (M1) and Mac Catalyst .

* [CBL-1474](https://issues.couchbase.com/browse/CBL-1474) — [Support Apple Silicon](https://issues.couchbase.com/browse/CBL-1474)
* [CBL-1580](https://issues.couchbase.com/browse/CBL-1580) — [Replication Heartbeat](https://issues.couchbase.com/browse/CBL-1580)

### [](#issues-and-resolutions-2-8-4)Issues and Resolutions

#### [](#known-issues)Known Issues

* [CBL-49](https://issues.couchbase.com/browse/CBL-49) — [Need a way to distinguish boolean types](https://issues.couchbase.com/browse/CBL-49)
* [CBL-95](https://issues.couchbase.com/browse/CBL-95) — [Pending conflicts could be resolved by a wrong replicator](https://issues.couchbase.com/browse/CBL-95)
* [CBL-216](https://issues.couchbase.com/browse/CBL-216) — [Ordering null values inconsistent with N1QL expectations](https://issues.couchbase.com/browse/CBL-216)

#### [](#fixed-issues)Fixed Issues

* [CBL-1439](https://issues.couchbase.com/browse/CBL-1439) — [Memory Leak in c4\_setTempDir](https://issues.couchbase.com/browse/CBL-1439)
* [CBL-1513](https://issues.couchbase.com/browse/CBL-1513) — [Stopping status should not be leaked](https://issues.couchbase.com/browse/CBL-1513)
* [CBL-1515](https://issues.couchbase.com/browse/CBL-1515) — [Standardize URL when calculating replication checkpoint](https://issues.couchbase.com/browse/CBL-1515)
* [CBL-1547](https://issues.couchbase.com/browse/CBL-1547) — [Deprecate Replicator.resetCheckpoint() API](https://issues.couchbase.com/browse/CBL-1547)
* [CBL-1663](https://issues.couchbase.com/browse/CBL-1663) — [Poller enters infinite loop at EOF](https://issues.couchbase.com/browse/CBL-1663)

* [CBL-399](https://issues.couchbase.com/browse/CBL-399) — [CouchbaseLite Mac Catalyst compatible build](https://issues.couchbase.com/browse/CBL-399)
* [CBL-1477](https://issues.couchbase.com/browse/CBL-1477) — [AcceptOnlySelfSigned may accept non-self-signed certificates](https://issues.couchbase.com/browse/CBL-1477)

## [](#maint-2)2.8.1 — November 2020

Version 2.8.1 of Couchbase Lite for Swift comprises a number of fixes. It supersedes version 2.8.0 released earlier this year.

**If you have already upgraded to 2.8.0 we strongly recommend that you upgrade to version 2.8.1 at the earliest opportunity.**

### [](#issues-and-resolutions-2-8-1-ios)Issues and Resolutions

#### [](#known-issues-2)Known Issues

* [CBL-216](https://issues.couchbase.com/browse/CBL-216) — Ordering null values inconsistent with N1QL expectations
* [CBL-95](https://issues.couchbase.com/browse/CBL-95) — Pending conflicts could be resolved by a wrong replicator
* [CBL-49](https://issues.couchbase.com/browse/CBL-49) — Need a way to distinguish boolean types

#### [](#fixed-issues-2)Fixed Issues

* [CBL-1423](https://issues.couchbase.com/browse/CBL-1423) — Fixes Carthage build failure \[[ENTERPRISE EDITION](https://www.couchbase.com/products/editions)\]
* [CBL-1403](https://issues.couchbase.com/browse/CBL-1403) — Compiling an app archive for distribution with the `Rebuild from Bitcode` option enabled will result in compiler errors.

## [](#major)2.8.0 — October 2020

_Quick Links_: [New Features](#new-features-2-8-0) **|** [Improvements](#improvements-2-8-0) **|** [Issues and Resolutions](#issues-and-resolutions-2-8-0) **|** [Support Notices](#support-notices-2-8-0) **|** [Related Content](#related-content)

### [](#new-features-2-8-0)New Features

#### [](#peer-to-peer-synchronization)Peer-to-Peer Synchronization

Using Couchbase Lite’s Peer-to-Peer Synchronization solution, you can build offline-first applications on edge devices that directly collaborate in secure bi-directional database synchronization without depending on centralized cloud-based control.

The solution provides an out-of-the-box implementation of a websocket based listener for use in peer-to-peer applications communicating over in IP-based networks.

Read More . . . [Landing P2Psync](#couchbase-lite:swift:landing-p2psync.adoc)

### [](#improvements-2-8-0)Improvements

#### [](#feature-changes)Feature Changes

None specified in this release

#### [](#other-enhancements)Other Enhancements

* [CBL-991](https://issues.couchbase.com/browse/CBL-991) — Add Maintenance API.
* [CBL-954](https://issues.couchbase.com/browse/CBL-954) — Return 403 for forbidden listener requests

#### [](#api-changes)API Changes

The API has been enhanced with the following changes:

* The _[Database.close()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-swift/Classes/Database.html#/s:18CouchbaseLiteSwift8DatabaseC5closeyyKF)_ method now automatically handles stopping open replicators, closing peer-to-peer websocket listener and removing observers for live queries.
* The _[Database.delete()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-swift/Classes/Database.html#/s:18CouchbaseLiteSwift8DatabaseC6deleteyyKF:)_ method now automatically handles stopping open replicators, closing peer-to-peer websocket listener and removing observers for live queries.
* The _[Replicator.isDocumentPending()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-swift/Classes/Replicator.html#/s:18CouchbaseLiteSwift10ReplicatorC17isDocumentPendingySbSSKF)_ method checks whether or not the document with the given ID has any pending revisions to push
* The _[Replicator.pendingDocumentIds()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-swift/Classes/Replicator.html#/s:18CouchbaseLiteSwift10ReplicatorC18pendingDocumentIdsShySSGyKF)_ method gets the Ids of all documents currently pending push
* _[Meta.revisionID](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-swift/Classes/Meta.html#/s:18CouchbaseLiteSwift4MetaC10revisionIDAA0D18ExpressionProtocol%5FpvpZ)_ property is now available as a metadata property, which can be accessed directly in queries

### [](#issues-and-resolutions-2-8-0)Issues and Resolutions

#### [](#known-issues-3)Known Issues

* [CBL-1403](https://issues.couchbase.com/browse/CBL-1403) — Compiling an app archive for distribution with the `Rebuild from Bitcode` option enabled will result in compiler errors. Disable `bitcode` to allow your compilation to proceed
* [CBL-1362](https://issues.couchbase.com/browse/CBL-1362) — Harmless unused property in ReplicatorConfiguration
* [CBL-216](https://issues.couchbase.com/browse/CBL-216) — Ordering null values inconsistent with N1QL expectations
* [CBL-95](https://issues.couchbase.com/browse/CBL-95) — Pending conflicts could be resolved by a wrong replicator
* [CBL-49](https://issues.couchbase.com/browse/CBL-49) — Need a way to distinguish boolean types

#### [](#fixed-issues-3)Fixed Issues

* [CBL-1141](https://issues.couchbase.com/browse/CBL-1141) — Android cannot use unlinked files
* [CBL-1107](https://issues.couchbase.com/browse/CBL-1107) — Properties beginning with dollar sign not handled correctly
* [CBL-1045](https://issues.couchbase.com/browse/CBL-1045) — Data race in log rollover
* [CBL-978](https://issues.couchbase.com/browse/CBL-978) — Math errors with float → int implicit fleece conversion
* [CBL-977](https://issues.couchbase.com/browse/CBL-977) — Full text search with Left Outer Join causes fields to be null
* [CBL-859](https://issues.couchbase.com/browse/CBL-859) — ChangeEncryptionKey() and save document after creating a brand new Database throws CouchbaseLiteException (SQLiteDomain / 21): bad parameter or other API misuse.
* [CBL-789](https://issues.couchbase.com/browse/CBL-789) — Crash when accessing `connection→name()`
* [CBL-745](https://issues.couchbase.com/browse/CBL-745) — Save fails when NSDate inserted with \[CBLMutableDocument setData\]
* [CBL-707](https://issues.couchbase.com/browse/CBL-707) — Compaction is ineffective (auto\_vacuum not enabled)
* [CBL-624](https://issues.couchbase.com/browse/CBL-624) — Revision flags get cleared while saving resolved document in iOS
* [CBL-614](https://issues.couchbase.com/browse/CBL-614) — Closing a read only database causes errors
* [CBL-609](https://issues.couchbase.com/browse/CBL-609) — Fleece thinks a boolean is a Long
* [CBL-594](https://issues.couchbase.com/browse/CBL-594) — Local to Local replication duplicates remote ID
* [CBL-590](https://issues.couchbase.com/browse/CBL-590) — Investigate handling of BLIP 500 errors
* [CBL-578](https://issues.couchbase.com/browse/CBL-578) — Receive rev#1 after rev#2 is saved to DB
* [CBL-565](https://issues.couchbase.com/browse/CBL-565) — Crashes apparently caused by attempting to log after failure
* [CBL-564](https://issues.couchbase.com/browse/CBL-564) — Property alias not working under certain cases
* [CBL-530](https://issues.couchbase.com/browse/CBL-530) — Certain keys in a query can cause segmentation faults
* [CBL-529](https://issues.couchbase.com/browse/CBL-529) — Cannot create an offset query without limit
* [CBL-384](https://issues.couchbase.com/browse/CBL-384) — Platform WebSocket code should manage HTTP cookies
* [CBL-358](https://issues.couchbase.com/browse/CBL-358) — xsockets doesn’t account for POSIX variations

### [](#support-notices-2-8-0)Support Notices

This section documents any support-related notes, constraints and changes

#### [](#deprecation-notices)Deprecation Notices

Items (features and-or functionality) are marked as deprecated when a more current, and usually enhanced, alternative is available.

Whilst the deprecated item will remain usable, it is no longer supported, and will be removed in a future release. You should plan to move to an alternative, supported, solution as soon as practical.

##### [](#this-release)This Release

* [CBL-1010](https://issues.couchbase.com/browse/CBL-1010) — The `resetCheckpoint()` API is deprecated at version 2.8\. Use `Replicator.start(reset)`, where reset is a boolean value.
* The [Database.compact()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-swift/Classes/Database.html#/s:18CouchbaseLiteSwift8DatabaseC7compactyyKF) method is deprecated at 2.8 — instead use [Database.performMaintenance()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-swift/Classes/Database.html#/s:18CouchbaseLiteSwift8DatabaseC18performMaintenance4typeyAA0F4TypeO%5FtKF).

##### [](#ongoing)Ongoing

Support for iOS 9.0 is deprecated in version 2.6.

Support for macOS 10.9 and 10.10 is deprecated in version 2.5.

#### [](#other-notices)Other Notices

##### [](#new)New

None specified in this release

##### [](#ongoing-2)Ongoing

Apple’s macOS is supported ONLY for testing and development purposes.

## [](#related-content)Related Content

###### [](#)

Product Notes

* [Release Notes](#couchbase-lite:swift:{cbl-pg-releasenotes})
* [Compatibility](../../current/swift/compatibility.md)
* [Supported OS](../../current/swift/supported-os.md)
* [What’s New](../../current/cbl-whatsnew.md)

###### [](#-2)

Starting Points

* [Databases](../../current/swift/database.md)
* [Documents](../../current/swift/document.md)
* [Blobs](../../current/swift/blob.md)
* [Remote Sync using Sync Gateway](../../current/swift/replication.md)
* [Handling Data Conflicts](../../current/swift/conflict.md)

###### [](#-3)

Tutorials

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)