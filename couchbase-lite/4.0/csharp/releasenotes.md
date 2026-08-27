---
title: Couchbase Lite Release Notes
description: Couchbase Lite on C#.Net
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.0/modules/csharp/pages/releasenotes.adoc
  xref: xref:4.0@couchbase-lite:csharp:releasenotes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/4.0/csharp/releasenotes.html)

# Couchbase Lite Release Notes

Unresolved include directive in modules/csharp/pages/releasenotes.adoc - include::partial$release-notes/couchbase-mobile-csharp-release-note.4.0.4.adoc\[\]

## [](#maint-4-0-3)4.0.3 — February 2026

Version 4.0.3 for C#.Net delivers the following features and enhancements:

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

Version 4.0.2 for C#.Net delivers the following features and enhancements:

### [](#enhancements-2)Enhancements

None for this release

### [](#fixed-issues-2)Fixed Issues

* [CBL-7681 — Crash with 'Can't retain immutable Value' Error after upgrading from 3.0.3 to 4.0.0](https://jira.issues.couchbase.com/browse/CBL-7681)
* [CBL-7731 — WinUI has no console logging implementation registered](https://jira.issues.couchbase.com/browse/CBL-7731)

### [](#known-issues-2)Known Issues

None for this release

### [](#breaking-changes)Breaking Changes

None for this release

### [](#deprecations-2)Deprecations

None for this release

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 4.0, see [New in 4.0](../cbl-whatsnew.md)

## [](#maint-4-0-0)4.0.0 — November 2025

Version 4.0.0 for C#.Net delivers the following features and enhancements:

### [](#enhancements-3)Enhancements

* [CBL-5368 — Support Proxy Authenticator API for .NET Android](https://jira.issues.couchbase.com/browse/CBL-5368)
* [CBL-6569 — Disabled SQLite's mmap by default](https://jira.issues.couchbase.com/browse/CBL-6569)
* [CBL-7281 — Support timestamp property in Document](https://jira.issues.couchbase.com/browse/CBL-7281)
* [CBL-7285 — Support Last-Write-Win as the default conflict resolution algorithm for Replicator](https://jira.issues.couchbase.com/browse/CBL-7285)
* [CBL-7330 — Add API for creating ReplicatorConfiguration with collection configs and endpoint](https://jira.issues.couchbase.com/browse/CBL-7330)
* [CBL-7416 — Update Database APIs to Return or Throw NotOpen Error for Closed Database Cases](https://jira.issues.couchbase.com/browse/CBL-7416)
* [CBL-7568 — New Version Vector Database](https://jira.issues.couchbase.com/browse/CBL-7568)

### [](#fixed-issues-3)Fixed Issues

* [CBL-6482 — Unpackaged apps on net8.0-windows cannot create databases](https://jira.issues.couchbase.com/browse/CBL-6482)
* [CBL-6504 — Query parser regression related to brackets](https://jira.issues.couchbase.com/browse/CBL-6504)
* [CBL-6513 — Race creating the expiration column in a collection table](https://jira.issues.couchbase.com/browse/CBL-6513)
* [CBL-6798 — Release c4log\_getDomain C# string bytes](https://jira.issues.couchbase.com/browse/CBL-6798)
* [CBL-7413 — FWrong error shown when using mismatch collections in Replicator](https://jira.issues.couchbase.com/browse/CBL-7413)

### [](#known-issues-3)Known Issues

* [CBL-7572 — Database.Copy() doesn't convert Self-Source-ID to the original Source ID](https://jira.issues.couchbase.com/browse/CBL-7572)
* [CBL-7573 — Couchbase Lite 4.0 is allowed to connect to Sync Gateway 3.2.6/3.3.0](https://jira.issues.couchbase.com/browse/CBL-7573)

### [](#breaking-changes-2)Breaking Changes

* [CBL-1946 — Enhanced .NET Configuration API with Init-Only and Required Properties](https://jira.issues.couchbase.com/browse/CBL-1946)
* [CBL-6596 — Vector Search Extension 2.0.0 Required for Couchbase Lite 4.0.0](https://jira.issues.couchbase.com/browse/CBL-6596)
* [CBL-7290 — Removed : Deprecated Database APIs](https://jira.issues.couchbase.com/browse/CBL-7290)
* [CBL-7294 — Removed : Deprecated Remove Change Listener APIs](https://jira.issues.couchbase.com/browse/CBL-7294)
* [CBL-7298 — Removed : Deprecated QueryBuilder APIs](https://jira.issues.couchbase.com/browse/CBL-7298)
* [CBL-7302 — Removed : Collection Management API from ReplicatorConfiguration](https://jira.issues.couchbase.com/browse/CBL-7302)
* [CBL-7341 — Removed : CollectionConfiguration's constructor without collection](https://jira.issues.couchbase.com/browse/CBL-7341)
* [CBL-7342 — Removed : ReplicatorConfiguration API for managing collection configurations](https://jira.issues.couchbase.com/browse/CBL-7342)
* [CBL-7343 — Removed : ReplicatorConfiguration's constructor with a target endpoint only](https://jira.issues.couchbase.com/browse/CBL-7343)
* [CBL-7380 — Removed : DatabaseConfiguration's mmapEnabled property](https://jira.issues.couchbase.com/browse/CBL-7380)
* [CBL-7392 — Removed : Deprecated Default Constants](https://jira.issues.couchbase.com/browse/CBL-7392)
* [CBL-7570 — Removed : Deprecated Replicator and Listener API](https://jira.issues.couchbase.com/browse/CBL-7570)

### [](#deprecations-3)Deprecations

* [CBL-7306 — Deprecate TLSIdentity.createIdentity() with isServer boolean flag](https://jira.issues.couchbase.com/browse/CBL-7306)

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 4.0, see [New in 4.0](../cbl-whatsnew.md)