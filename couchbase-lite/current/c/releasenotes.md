---
title: Couchbase Lite Release Notes
description: Couchbase Lite on C
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.0/modules/c/pages/releasenotes.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:couchbase-lite:c:releasenotes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/current/c/releasenotes.html)

# Couchbase Lite Release Notes

## [](#maint-4-0-3)4.0.3 — February 2026

Version 4.0.3 for C delivers the following features and enhancements:

### [](#enhancements)Enhancements

* [CBL-7750 — Update mbedTLS to 3.6.5](https://jira.issues.couchbase.com/browse/CBL-7750)
* [CBL-7775 — Increase Replicator's WebSocket PING / PONG timeout](https://jira.issues.couchbase.com/browse/CBL-7775)

### [](#fixed-issues)Fixed Issues

* [CBL-5298 — Fix SQL++ parser failure for IN operator](https://jira.issues.couchbase.com/browse/CBL-5298)
* [CBL-7661 — Increase Replicator Database Pool Borrow Timeout](https://jira.issues.couchbase.com/browse/CBL-7661)
* [CBL-7799 — "Invalid version string" exception from replicator when pulling a merged conflict version](https://jira.issues.couchbase.com/browse/CBL-7799)

### [](#known-issues)Known Issues

None for this release

### [](#deprecations)Deprecations

None for this release

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 4.0, see [New in 4.0](../cbl-whatsnew.md)

## [](#maint-4-0-2)4.0.2 — December 2025

Version 4.0.2 for C delivers the following features and enhancements:

### [](#enhancements-2)Enhancements

None for this release

### [](#fixed-issues-2)Fixed Issues

* [CBL-7681 — Crash with 'Can't retain immutable Value' Error after upgrading from 3.0.3 to 4.0.0](https://jira.issues.couchbase.com/browse/CBL-7681)

### [](#known-issues-2)Known Issues

None for this release

### [](#breaking-changes)Breaking Changes

None for this release

### [](#deprecations-2)Deprecations

None for this release

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 4.0, see [New in 4.0](../cbl-whatsnew.md)

## [](#maint-4-0-0)4.0.0 — October 2025

Version 4.0.0 for C delivers the following features and enhancements:

### [](#enhancements-3)Enhancements

* [CBL-7568 — New Version Vector Database](https://issues.couchbase.com/browse/CBL-7568)
* [CBL-6569 — Disabled SQLite's mmap by default](https://issues.couchbase.com/browse/CBL-6569)
* [CBL-7280 — Support timestamp property in Document](https://issues.couchbase.com/browse/CBL-7280)
* [CBL-7284 — Support Last-Write-Win as the default conflict resolution algorithm for Replicator](https://issues.couchbase.com/browse/CBL-7284)
* [CBL-7431 — Include native symbols in Android Released Binaries](https://issues.couchbase.com/browse/CBL-7431)

### [](#fixed-issues-3)Fixed Issues

* [CBL-6482 — Fixed unpackaged apps on net8.0-windows cannot create databases](https://issues.couchbase.com/browse/CBL-6482)
* [CBL-6504 — Fixed query parser regression related to brackets](https://issues.couchbase.com/browse/CBL-6504)
* [CBL-6513 — Fixed race creating the expiration column in a collection table](https://issues.couchbase.com/browse/CBL-6513)
* [CBL-7413 — Fixed wrong error shown when using mismatch collections in Replicator](https://issues.couchbase.com/browse/CBL-7413)
* [CBL-7463 — Fixed crash when creating Full-Text Index using Java Community Edition on Windows](https://issues.couchbase.com/browse/CBL-7463)
* [CBL-7557 — Fixed invalid CBLFileLogSink's directory value returned from CBLLogSinks\_File](https://issues.couchbase.com/browse/CBL-7557)

### [](#known-issues-3)Known Issues

* [CBL-7572 — Database.Copy() doesn't convert Self-Source-ID to the original Source ID](https://issues.couchbase.com/browse/CBL-7572)
* [CBL-7573 — Couchbase Lite 4.0 is allowed to connect to Sync Gateway 3.2.6/3.3.0](https://issues.couchbase.com/browse/CBL-7573)

### [](#breaking-changes-2)Breaking Changes

* [CBL-6596 — Vector Search Extension 2.0.0 Required for Couchbase Lite 4.0.0](https://jira.issues.couchbase.com/browse/CBL-6596)
* [CBL-7289 — Remove Deprecated Database APIs](https://issues.couchbase.com/browse/CBL-7289)
* [CBL-7301 — Remove Deprecated Replicator API](https://issues.couchbase.com/browse/CBL-7301)
* [CBL-7314 — Remove Deprecated Logging APIs](https://issues.couchbase.com/browse/CBL-7314)
* [CBL-7379 — Removed DatabaseConfiguration's mmapEnabled property](https://issues.couchbase.com/browse/CBL-7379)
* [CBL-7391 — Removed Deprecated Default Constants](https://issues.couchbase.com/browse/CBL-7391)
* [CBL-7399 — Restructure CBLReplicatorConfiguration member order to improve clarity and usability](https://issues.couchbase.com/browse/CBL-7399)

### [](#deprecations-3)Deprecations

* [CBL-7400 — Deprecate CBLReplicationCollection](https://issues.couchbase.com/browse/CBL-7400)

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 4.0, see [New in 4.0](../cbl-whatsnew.md)