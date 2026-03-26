---
title: Release Notes
description: Couchbase Lite on C
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.0/modules/c/pages/releasenotes.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.0@couchbase-lite:c:releasenotes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.0/c/releasenotes.html)

# Release Notes

> Description — _Couchbase Lite on C_  
> _Abstract — This content describes the key features and changes implemented by release 3.0 of Couchbase Lite on C_  
> Related Content — [What's New](#cbl-whatsnew.adoc) | [Compatibility](compatibility.md) | [Supported Platforms](supported-os.md)

## [](#maint-3-0-15)3.0.15 — November 2023

Version 3.0.15 for C delivers the following features and enhancements:

### [](#enhancements)Enhancements

* [CBL-3643: Upgrade to ICU 69+](https://issues.couchbase.com/browse/CBL-3643)

### [](#issues-and-resolutions)Issues and Resolutions

* [CBL-4839: Fix issue with deletion of Attachments/Blobs after compaction &re-sync](https://issues.couchbase.com/browse/CBL-4839)
* [CBL-4139: fix build error on Linux](https://issues.couchbase.com/browse/CBL-4139)
* [CBL-4111: Allow docs failed with property encryption/decryption to be retried](https://issues.couchbase.com/browse/CBL-4111)
* [CBL-3871: fix QueryParams decoding bool](https://issues.couchbase.com/browse/CBL-3871)

### [](#known-issues)Known Issues

None for this release

### [](#deprecations)Deprecations

None for this release

## [](#maint-3-0-12)3.0.12 — June 2023

Version 3.0.12 for C delivers the following features and enhancements:

### [](#enhancements-2)Enhancements

* [CBL-4573 - Generate API Doc](https://issues.couchbase.com/browse/CBL-4573)
* [CBL-4561 - Implement AcceptParentDomainCookies API](https://issues.couchbase.com/browse/CBL-4561)
* [CBL-4489 - Build XCFramework for iOS with Bitcode disabled](https://issues.couchbase.com/browse/CBL-4489)
* [CBL-4531 - Update PublicKey+Apple to use non deprecated keychain APIs](https://issues.couchbase.com/browse/CBL-4531)
* [CBL-4167 - SQL++ : COLLATE does not have a way to specify locale for UNICODE](https://issues.couchbase.com/browse/CBL-4167)
* [CBL-4024 - Change BuiltInWebSocket to do preemptive auth instead of challenge auth by default (Port)](https://issues.couchbase.com/browse/CBL-4024)
* [CBL-3903 - Assertion failure when stopping replicator while replicator is connecting](https://issues.couchbase.com/browse/CBL-3903)
* [CBL-4134 - Fix empty identity error when building LiteCoreCppTests&C4Tests using XCode 14](https://issues.couchbase.com/browse/CBL-4134)
* [CBL-3993 - FTS index table not have to be qualified by data source alias in query](https://issues.couchbase.com/browse/CBL-3993)

### [](#issues-and-resolutions-2)Issues and Resolutions

* [CBL-3671 - Fix slowdowns and storage overhead caused by document revision history not being pruned](https://issues.couchbase.com/browse/CBL-3671)
* [CBL-3929 - Crash when closing database shortly after remove listener token in query change (Port)](https://issues.couchbase.com/browse/CBL-3929)
* [CBLReplicatorConfiguration's property encryption callbacks](https://issues.couchbase.com/browse/CBL-4349)
* [CBL-4349 - Missing nullable marks in](https://issues.couchbase.com/browse/CBL-4349)
* [CBL-4529 - Error when saving documents with LiteCore error 17: must be called during a transaction](https://issues.couchbase.com/browse/CBL-4529)
* [CBL-4450 - Stop replicator could cause 'database is locked' error when saving a document](https://issues.couchbase.com/browse/CBL-4450)
* [CBL-4448 - Replicator may get stuck when there is an error of "Invalid delta"](https://issues.couchbase.com/browse/CBL-4448)
* [CBL-4418 - Replicator is stuck in busy state when there is an error thrown while applying delta to create full fleece doc](https://issues.couchbase.com/browse/CBL-4418)
* [CBL-4410 - Compaction could cause "database is locked" error when the replicator attempts to save its checkpoint at the same time](https://issues.couchbase.com/browse/CBL-4410)
* [CBL-4388 - The URL Scheme the HTTP Message is incorrect when using proxy](https://issues.couchbase.com/browse/CBL-4388)
* [CBL-4325 - Opening the upgraded database from 2.8 to 3.0.2 is slow](https://issues.couchbase.com/browse/CBL-4325)
* [CBL-4021 - Query parameters not being bound](https://issues.couchbase.com/browse/CBL-4021)
* [CBL-3715 - Query document expiration is failing](https://issues.couchbase.com/browse/CBL-3715)
* [CBL-4570 - URLEndpointListener.getURLs returns an empty list on Android v>=11](https://issues.couchbase.com/browse/CBL-4570)

### [](#known-issues-2)Known Issues

None for this release.

## [](#maint-3-0-11)3.0.11 — March 2023

Version 3.0.11 for C delivers the following features and enhancements:

### [](#enhancements-3)Enhancements

None for this release.

### [](#issues-and-resolutions-3)Issues and Resolutions

* [ CBL-4291 -- Fix crash when getting User-Agent on Android ](https://issues.couchbase.com/browse/CBL-4291)
* [ CBL-4238 -- Create SecTrust with certificate chain ](https://issues.couchbase.com/browse/CBL-4238)
* [ CBL-3965 -- Rebuild CBL-C Android with compiler optimizations ](https://issues.couchbase.com/browse/CBL-3965)

### [](#known-issues-3)Known Issues

None for this release.

## [](#maint-3-0-10)3.0.10 — February 2023

Version 3.0.10 for C delivers the following features and enhancements:

### [](#enhancements-4)Enhancements

None for this release.

### [](#issues-and-resolutions-4)Issues and Resolutions

* [ CBL-4191 -- Local sparse checkpoint has a bug ](https://issues.couchbase.com/browse/CBL-4191)
* [ CBL-4201 -- User-agent header key is incorrect ](https://issues.couchbase.com/browse/CBL-4201)
* [ CBL-3923 -- Add user-agent header to the replicator ](https://issues.couchbase.com/browse/CBL-3923)
* [ CBL-4136 -- Create query with SQL is slow on complex query ++](https://issues.couchbase.com/browse/CBL-4136)
* [ CBL-4097 -- Allow the doc to be re-sync after having a crypto failure from property encryption / decryption ](https://issues.couchbase.com/browse/CBL-4097)

### [](#known-issues-4)Known Issues

None for this release.

## [](#maint-3-0-2)3.0.2 — August 2022

Version 3.0.2 of Couchbase Lite for C delivers a number of fixes and enhancements.

### [](#enhancements-5)Enhancements

* [CBL-3034](https://issues.couchbase.com/browse/CBL-3034) — [Update zlib to the latest version](https://issues.couchbase.com/browse/CBL-3034)
* [CBL-2976](https://issues.couchbase.com/browse/CBL-2976) — [Implement enhanced pinned server certificate feature](https://issues.couchbase.com/browse/CBL-2976)

### [](#issues-and-resolutions-3-0-2)Issues and Resolutions

#### [](#fixed-issues)Fixed Issues

* [CBL-3358](https://issues.couchbase.com/browse/CBL-3358) — [32+ select items in the query fails](https://issues.couchbase.com/browse/CBL-3358)
* [CBL-3224](https://issues.couchbase.com/browse/CBL-3224) — [Call to c4socket\_closed causes native crash](https://issues.couchbase.com/browse/CBL-3224)
* [CBL-3090](https://issues.couchbase.com/browse/CBL-3090) — [Push large database test could fail](https://issues.couchbase.com/browse/CBL-3090)
* [CBL-3040](https://issues.couchbase.com/browse/CBL-3040) — [QueryParser wrong for a case of JOIN](https://issues.couchbase.com/browse/CBL-3040)
* [CBL-3036](https://issues.couchbase.com/browse/CBL-3036) — [Continuous replicator does not push docs which are being observed](https://issues.couchbase.com/browse/CBL-3036)
* [CBL-2942](https://issues.couchbase.com/browse/CBL-2942) — [LiveQuery could crash when removing the listener](https://issues.couchbase.com/browse/CBL-2942)
* [CBL-2884](https://issues.couchbase.com/browse/CBL-2884) — [evpos is missing in the changed attachment body when using delta sync](https://issues.couchbase.com/browse/CBL-2884)

#### [](#known-issues-5)Known Issues

## [](#maint-3-0-1)3.0.1 — March 2022

Version 3.0.1 of Couchbase Lite for C delivers a number of fixes and enhancements.

### [](#enhancements-6)Enhancements

* [CBL-2852](https://issues.couchbase.com/browse/CBL-2852) — [Missing FLDeepIterator\_GetParent symbol](https://issues.couchbase.com/browse/CBL-2852)

### [](#issues-and-resolutions-3-0-1)Issues and Resolutions

#### [](#fixed-issues-2)Fixed Issues

* [CBL-2808](https://issues.couchbase.com/browse/CBL-2808) — [EWOULDBLOCK (POSIX 35) causes connection to close](https://issues.couchbase.com/browse/CBL-2808)
* [CBL-2844](https://issues.couchbase.com/browse/CBL-2844) — [Cannot update the same field again after reopening the database](https://issues.couchbase.com/browse/CBL-2844)

#### [](#known-issues-6)Known Issues

None for this release.

## [](#major)3.0.15 — February 2022

_Quick Links_

[New Features](#new-features-3-0-0) **|** [Enhancements](#improvements-3-0-0) **|** [Known Issues](#lbl-know-issues-this-release) **|** [Fixed Issues](#lbl-fixed-this-release) **|** [Deprecated in this Release](#lbl-deprecated-this-release) **|** [Removed in this Release](#lbl-removed-this-release) **|** [Support Notices](#lbl-support-notices) **|** 

> [!IMPORTANT]
> On upgrading from a 2.x release, all Couchbase Lite databases will be automatically re-indexed on initial database open.  
> This can result in a delay before the database is usable.

### [](#new-features-3-0-0)New Features

#### [](#couchbase-lite-for-c)Couchbase Lite for C

_Couchbase Lite_ now has an officially supported **C API**, which builds on the success of the well-received engineering labs _C API for Couchbase Lite_.

The C API now includes support for Enterprise-grade features like database encryption. This optimized implementation is ensured feature parity with our other Couchbase Lite platforms and is supported on a wide-range of mobile and desktop platforms — see: [Supported Platforms](supported-os.md).

The ease of building language bindings on top of the C API means application developers can build for edge and embedded IoT devices using their preferred languages to harness the power of Couchbase Lite.

Read More . . . [Couchbase Lite for C](index.md)

#### [](#sqln1ql-query-strings)SQL++/N1QL Query Strings

Couchbase Lite's SQL++ for Mobile query API vastly simplifies the integration of Couchbase Lite within hybrid/cross platform apps.

N1QL for Mobile is an implementation of the emerging SQL-for-JSON query language specification (SQL++). It provides native, hybrid and cross-platform mobile app developers with a consistent, convenient and flexible interface to query JSON documents within the embedded database using a SQL-based syntax. This means developers can reuse queries across platforms, reducing development, testing and maintenance costs.

Read More . . . [SQL++ for Mobile](query-n1ql-mobile.md)

### [](#improvements-3-0-0)Enhancements

None for this release.

### [](#lbl-know-issues-this-release)Known Issues

None for this release.

### [](#lbl-fixed-this-release)Fixed Issues

None for this release.

### [](#lbl-deprecated-this-release)Deprecated in this Release

Items (features and-or functionality) are marked as deprecated when a more current, and usually enhanced, alternative is available.

Whilst the deprecated item will remain usable, it is no longer supported, and will be removed in a future release — see also: [Removed in this Release](#lbl-removed-this-release)You should plan to move to an alternative, supported, solution as soon as practical.

None for this release.

### [](#lbl-removed-this-release)Removed in this Release

None for this release.

### [](#lbl-support-notices)Support Notices

This section documents any support-related notes, constraints and changes.

#### [](#new)New

None specified in this release

#### [](#ongoing)Ongoing

None specified

## [](#related-content)Related Content

###### [](#)

Product Notes

* [Release Notes](releasenotes.md)
* [Compatibility](compatibility.md)
* [Supported Platforms](supported-os.md)
* [What's New](#cbl-whatsnew.adoc)

###### [](#-2)

Starting Points

* [Databases](database.md)
* [Documents](document.md)
* [Blobs](blob.md)
* [Remote Sync Gateway](replication.md)
* [Handling Data Conflicts](conflict.md)

###### [](#-3)

Tutorials

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)