---
title: Couchbase Lite Release Notes
description: Couchbase Lite on Android
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.0/modules/android/pages/releasenotes.adoc
  xref: xref:4.0@couchbase-lite:android:releasenotes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/4.0/android/releasenotes.html)

# Couchbase Lite Release Notes

## [](#maint-4-0-4)4.0.4 — May 2026

Version 4.0.4 for Android delivers the following features and enhancements:

### [](#enhancements)Enhancements

* [CBL-7989 — Upgrade SQLite to 3.53.0](https://jira.issues.couchbase.com/browse/CBL-7989)
* [CBL-8076 — Improve replicator WebSocket close completion when the server fails to acknowledge close](https://jira.issues.couchbase.com/browse/CBL-8076)
* [CBL-8183 — Upgrade mbedTLS to 3.6.6](https://jira.issues.couchbase.com/browse/CBL-8183)

### [](#fixed-issues)Fixed Issues

* [CBL-7992 — Partial value index creation failing when using compound expressions in WHERE clause](https://jira.issues.couchbase.com/browse/CBL-7992)
* [CBL-8162 — Crash when accessing the peer ID or neighbor peers on a stopped MultipeerReplicator](https://jira.issues.couchbase.com/browse/CBL-8162)
* [CBL-8165 — MultipeerReplicator.getPeerInfo(PeerId) incorrectly marked as NonNull](https://jira.issues.couchbase.com/browse/CBL-8165)
* [CBL-8172 — MultipeerReplicator not posting notifications on the specified Executor](https://jira.issues.couchbase.com/browse/CBL-8172)
* [CBL-8246 — MultipeerReplicator not applying push/pull filters](https://jira.issues.couchbase.com/browse/CBL-8246)

### [](#known-issues)Known Issues

None for this release

### [](#deprecations)Deprecations

None for this release

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 4.0, see [New in 4.0](../cbl-whatsnew.md)

## [](#maint-4-0-3)4.0.3 — February 2026

Version 4.0.3 for Android delivers the following features and enhancements:

### [](#enhancements-2)Enhancements

* [CBL-7750 — Update mbedTLS to 3.6.5](https://jira.issues.couchbase.com/browse/CBL-7750)
* [CBL-7775 — Increase Replicator's WebSocket PING / PONG timeout](https://jira.issues.couchbase.com/browse/CBL-7775)

### [](#fixed-issues-2)Fixed Issues

* [CBL-5298 — Fix SQL++ parser failure for IN operator](https://jira.issues.couchbase.com/browse/CBL-5298)
* [CBL-7661 — Increase Replicator Database Pool Borrow Timeout](https://jira.issues.couchbase.com/browse/CBL-7661)
* [CBL-7799 — "Invalid version string" exception from replicator when pulling a merged conflict version](https://jira.issues.couchbase.com/browse/CBL-7799)
* [CBL-7886 — Fix remoteDocument content invalidation when calling toMutable() in Conflict Resolver](https://issues.couchbase.com/browse/CBL-7886)

### [](#known-issues-2)Known Issues

None for this release

### [](#deprecations-2)Deprecations

None for this release

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 4.0, see [New in 4.0](../cbl-whatsnew.md)

## [](#maint-4-0-2)4.0.2 — December 2025

Version 4.0.2 for Android delivers the following features and enhancements:

### [](#enhancements-3)Enhancements

None for this release

### [](#fixed-issues-3)Fixed Issues

* [CBL-7681 — Crash with 'Can't retain immutable Value' Error after upgrading from 3.0.3 to 4.0.0](https://jira.issues.couchbase.com/browse/CBL-7681)

### [](#known-issues-3)Known Issues

None for this release

### [](#breaking-changes)Breaking Changes

None for this release

### [](#deprecations-3)Deprecations

None for this release

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 4.0, see [New in 4.0](../cbl-whatsnew.md)

## [](#maint-4-0-0)4.0.0 — October 2025

Version 4.0.0 for Android delivers the following features and enhancements:

### [](#enhancements-4)Enhancements

* [CBL-7568 — New Version Vector Database](https://issues.couchbase.com/browse/CBL-7568)
* [CBL-6569 — Disabled SQLite's mmap by default](https://issues.couchbase.com/browse/CBL-6569)
* [CBL-7282 — Support timestamp property in Document](https://issues.couchbase.com/browse/CBL-7282)
* [CBL-7286 — Support Last-Write-Win as the default conflict resolution algorithm for Replicator](https://issues.couchbase.com/browse/CBL-7286)
* [CBL-7415 — Update Database APIs to Return or Throw NotOpen Error for Closed Database Cases](https://issues.couchbase.com/browse/CBL-7415)

### [](#fixed-issues-4)Fixed Issues

* [CBL-6504 — Query parser regression related to brackets](https://issues.couchbase.com/browse/CBL-6504)
* [CBL-6513 — Race creating the expiration column in a collection table](https://issues.couchbase.com/browse/CBL-6513)
* [CBL-7413 — Wrong error shown when using mismatch collections in Replicator](https://issues.couchbase.com/browse/CBL-7413)

### [](#known-issues-4)Known Issues

* [CBL-7572 — Database.Copy() doesn't convert Self-Source-ID to the original Source ID](https://issues.couchbase.com/browse/CBL-7572)
* [CBL-7573 — Couchbase Lite 4.0 is allowed to connect to Sync Gateway 3.2.6/3.3.0](https://issues.couchbase.com/browse/CBL-7573)

### [](#breaking-changes-2)Breaking Changes

* [CBL-6596 — Vector Search Extension 2.0.0 Required for Couchbase Lite 4.0.0](https://jira.issues.couchbase.com/browse/CBL-6596)
* [CBL-7291 — Remove Deprecated Database APIs](https://issues.couchbase.com/browse/CBL-7291)
* [CBL-7295 — Removed Deprecated Remove Change Listener APIs](https://issues.couchbase.com/browse/CBL-7295)
* [CBL-7299 — Removed Deprecated QueryBuilder APIs](https://issues.couchbase.com/browse/CBL-7299)
* [CBL-7303 — Removed Deprecated Collection Management API from ReplicatorConfiguration](https://issues.couchbase.com/browse/CBL-7303)
* [CBL-7307 — Removed Deprecated TLSIdentity's createIdentity with isServer boolean flag](https://issues.couchbase.com/browse/CBL-7307)
* [CBL-7316 — Removed Deprecated Logging APIs](https://issues.couchbase.com/browse/CBL-7316)
* [CBL-7381 — Removed DatabaseConfiguration's mmapEnabled property](https://issues.couchbase.com/browse/CBL-7381)
* [CBL-7393 — Removed Deprecated Default Constants](https://issues.couchbase.com/browse/CBL-7393)
* [CBL-7569 — Removed Deprecated Replicator and Listener APIs](https://issues.couchbase.com/browse/CBL-7569)

### [](#deprecations-4)Deprecations

No new deprecations for this release.

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 4.0, see [New in 4.0](../cbl-whatsnew.md)