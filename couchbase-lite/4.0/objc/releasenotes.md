---
title: Couchbase Lite Release Notes
description: Couchbase Lite on Objective-C
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.0/modules/objc/pages/releasenotes.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:4.0@couchbase-lite:objc:releasenotes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/4.0/objc/releasenotes.html)

# Couchbase Lite Release Notes

## [](#maint-4-0-4)4.0.4 — May 2026

Version 4.0.4 for Objective-C delivers the following features and enhancements:

### [](#enhancements)Enhancements

* [CBL-7989 — Upgrade SQLite to 3.53.0](https://jira.issues.couchbase.com/browse/CBL-7989)
* [CBL-8076 — Improve replicator WebSocket close completion when the server fails to acknowledge close](https://jira.issues.couchbase.com/browse/CBL-8076)
* [CBL-8183 — Upgrade mbedTLS to 3.6.6](https://jira.issues.couchbase.com/browse/CBL-8183)

### [](#fixed-issues)Fixed Issues

* [CBL-7992 — Partial value index creation failing when using compound expressions in WHERE clause](https://jira.issues.couchbase.com/browse/CBL-7992).
* [CBL-8159 — Result.data(as:dataKey:) dropping optional properties when using dataKey](https://jira.issues.couchbase.com/browse/CBL-8159)

### [](#known-issues)Known Issues

None for this release

### [](#deprecations)Deprecations

None for this release

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 4.0, see [New in 4.0](../cbl-whatsnew.md)

## [](#maint-4-0-3)4.0.3 — February 2026

Version 4.0.3 for Objective-C delivers the following features and enhancements:

### [](#enhancements-2)Enhancements

* [CBL-7750 — Update mbedTLS to 3.6.5](https://jira.issues.couchbase.com/browse/CBL-7750)
* [CBL-7775 — Increase Replicator's WebSocket PING / PONG timeout](https://jira.issues.couchbase.com/browse/CBL-7775)

### [](#fixed-issues-2)Fixed Issues

* [CBL-5298 — Fix SQL++ parser failure for IN operator](https://jira.issues.couchbase.com/browse/CBL-5298)
* [CBL-7661 — Increase Replicator Database Pool Borrow Timeout](https://jira.issues.couchbase.com/browse/CBL-7661)
* [CBL-7799 — "Invalid version string" exception from replicator when pulling a merged conflict version](https://jira.issues.couchbase.com/browse/CBL-7799)

### [](#known-issues-2)Known Issues

None for this release

### [](#deprecations-2)Deprecations

None for this release

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 4.0, see [New in 4.0](../cbl-whatsnew.md)

## [](#maint-4-0-2)4.0.2 — December 2025

Version 4.0.2 for Objective-C delivers the following features and enhancements:

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

## [](#maint-4-0-1)4.0.1 — November 2025

Version 4.0.1 for Objective-C delivers the following features and enhancements:

### [](#enhancements-4)Enhancements

None for this release

### [](#fixed-issues-4)Fixed Issues

* [CBL-7658 — Peer IP resolution may time out when the service is discovered on an IPv6 link-local interface](https://jira.issues.couchbase.com/browse/CBL-7658)
* [CBL-7660 — Resolved an issue in MultipeerReplicator.](https://jira.issues.couchbase.com/browse/CBL-7660)

### [](#known-issues-4)Known Issues

None for this release

### [](#breaking-changes-2)Breaking Changes

None for this release

### [](#deprecations-4)Deprecations

None for this release

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 4.0, see [New in 4.0](../cbl-whatsnew.md)

## [](#maint-4-0-0)4.0.0 — October 2025

Version 4.0.0 for Objective-C delivers the following features and enhancements:

### [](#enhancements-5)Enhancements

* [CBL-7568 — New Version Vector Database](https://issues.couchbase.com/browse/CBL-7568)
* [CBL-6569 — Disabled SQLite's mmap by default](https://issues.couchbase.com/browse/CBL-6569)
* [CBL-7279 — Support timestamp property in Document](https://issues.couchbase.com/browse/CBL-7279)
* [CBL-7283 — Support Last-Write-Wins as the default Conflict Resolver for Replicator](https://issues.couchbase.com/browse/CBL-7283)
* [CBL-7348 — Update Database APIs to Return or Throw NotOpen Error for Closed Database Cases](https://issues.couchbase.com/browse/CBL-7348)

### [](#fixed-issues-5)Fixed Issues

* [CBL-6504 — Query parser regression related to brackets](https://issues.couchbase.com/browse/CBL-6504)
* [CBL-6513 — Race creating the expiration column in a collection table](https://issues.couchbase.com/browse/CBL-6513)
* [CBL-7413 — Wrong error shown when using mismatch collections in Replicator](https://issues.couchbase.com/browse/CBL-7413)
* [CBL-7467 — TLS ClientHello missing Server Name when network interface is specified](https://issues.couchbase.com/browse/CBL-7467)

### [](#known-issues-5)Known Issues

* [CBL-7572 — Database.Copy() doesn't convert Self-Source-ID to the original Source ID](https://issues.couchbase.com/browse/CBL-7572)
* [CBL-7573 — Couchbase Lite 4.0 is allowed to connect to Sync Gateway 3.2.6/3.3.0](https://issues.couchbase.com/browse/CBL-7573)

### [](#breaking-changes-3)Breaking Changes

* [CBL-6596 — Vector Search Extension 2.0.0 Required for Couchbase Lite 4.0.0](https://jira.issues.couchbase.com/browse/CBL-6596)
* [CBL-7288 — Remove Deprecated Database APIs](https://issues.couchbase.com/browse/CBL-7288)
* [CBL-7292 — Removed: Deprecated Remove Change Listener APIs](https://issues.couchbase.com/browse/CBL-7292)
* [CBL-7296 — Removed: Deprecated QueryBuilder APIs](https://issues.couchbase.com/browse/CBL-7296)
* [CBL-7300 — Remove Deprecated Collection Management API in ReplicatorConfiguration](https://issues.couchbase.com/browse/CBL-7300)
* [CBL-7304 — Removed: Deprecated TLSIdentity's createIdentity with isServer boolean flag](https://issues.couchbase.com/browse/CBL-7304)
* [CBL-7313 — Removed: Deprecated Logging APIs](https://issues.couchbase.com/browse/CBL-7313)
* [CBL-7378 — Removed: DatabaseConfiguration's mmapEnabled property](https://issues.couchbase.com/browse/CBL-7378)
* [CBL-7390 — Removed: Deprecated Default Constants](https://issues.couchbase.com/browse/CBL-7390)
* [CBL-7571 — Removed Deprecated Replicator and Listener APIs](https://issues.couchbase.com/browse/CBL-7571)
* [CBL-7654 — MultipeerCertificateAuthenticator created with root certs fails to validate peer certificates](https://jira.issues.couchbase.com/browse/CBL-7654)

### [](#deprecations-5)Deprecations

None for this release

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 4.0, see [New in 4.0](../cbl-whatsnew.md)