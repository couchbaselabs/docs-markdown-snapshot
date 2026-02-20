---
title: Couchbase Lite Release Notes
description: Couchbase Lite on C
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.0/modules/c/pages/releasenotes.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:couchbase-lite:c:releasenotes.adoc[]
---

[View original HTML](/couchbase-lite/current/c/releasenotes.html)

# Couchbase Lite Release Notes

## [](#maint-4-0-0)4.0.0 — October 2025

Version 4.0.0 for C delivers the following features and enhancements:

## [](#couchbase-lite-release-notes)Couchbase Lite Release Notes

### [](#enhancements)Enhancements

* [CBL-7568 — New Version Vector Database](https://issues.couchbase.com/browse/CBL-7568)
* [CBL-6569 — Disabled SQLite’s mmap by default](https://issues.couchbase.com/browse/CBL-6569)
* [CBL-7280 — Support timestamp property in Document](https://issues.couchbase.com/browse/CBL-7280)
* [CBL-7284 — Support Last-Write-Win as the default conflict resolution algorithm for Replicator](https://issues.couchbase.com/browse/CBL-7284)
* [CBL-7431 — Include native symbols in Android Released Binaries](https://issues.couchbase.com/browse/CBL-7431)

### [](#issues-and-resolutions)Issues and Resolutions

#### [](#fixed-issues)Fixed Issues

* [CBL-6482 — Fixed unpackaged apps on net8.0-windows cannot create databases](https://issues.couchbase.com/browse/CBL-6482)
* [CBL-6504 — Fixed query parser regression related to brackets](https://issues.couchbase.com/browse/CBL-6504)
* [CBL-6513 — Fixed race creating the expiration column in a collection table](https://issues.couchbase.com/browse/CBL-6513)
* [CBL-7413 — Fixed wrong error shown when using mismatch collections in Replicator](https://issues.couchbase.com/browse/CBL-7413)
* [CBL-7463 — Fixed crash when creating Full-Text Index using Java Community Edition on Windows](https://issues.couchbase.com/browse/CBL-7463)
* [CBL-7557 — Fixed invalid CBLFileLogSink’s directory value returned from CBLLogSinks\_File](https://issues.couchbase.com/browse/CBL-7557)

#### [](#known-issues)Known Issues

* [CBL-7572 — Database.Copy() doesn’t convert Self-Source-ID to the original Source ID](https://issues.couchbase.com/browse/CBL-7572)
* [CBL-7573 — Couchbase Lite 4.0 is allowed to connect to Sync Gateway 3.2.6/3.3.0](https://issues.couchbase.com/browse/CBL-7573)

### [](#breaking-changes)Breaking Changes

* [CBL-6596 — Vector Search Extension 2.0.0 Required for Couchbase Lite 4.0.0](https://jira.issues.couchbase.com/browse/CBL-6596)
* [CBL-7289 — Remove Deprecated Database APIs](https://issues.couchbase.com/browse/CBL-7289)
* [CBL-7301 — Remove Deprecated Replicator API](https://issues.couchbase.com/browse/CBL-7301)
* [CBL-7314 — Remove Deprecated Logging APIs](https://issues.couchbase.com/browse/CBL-7314)
* [CBL-7379 — Removed DatabaseConfiguration’s mmapEnabled property](https://issues.couchbase.com/browse/CBL-7379)
* [CBL-7391 — Removed Deprecated Default Constants](https://issues.couchbase.com/browse/CBL-7391)
* [CBL-7399 — Restructure CBLReplicatorConfiguration member order to improve clarity and usability](https://issues.couchbase.com/browse/CBL-7399)

### [](#deprecations)Deprecations

* [CBL-7400 — Deprecate CBLReplicationCollection](https://issues.couchbase.com/browse/CBL-7400)

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 4.0.0, see [New in 4.0](../cbl-whatsnew.md)