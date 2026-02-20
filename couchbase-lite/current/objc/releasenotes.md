---
title: Couchbase Lite Release Notes
description: Couchbase Lite on Objective-C
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.0/modules/objc/pages/releasenotes.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:couchbase-lite:objc:releasenotes.adoc[]
---

[View original HTML](/couchbase-lite/current/objc/releasenotes.html)

# Couchbase Lite Release Notes

## [](#maint-4-0-1)4.0.1 — November 2025

Version 4.0.1 for Objective-C delivers the following features and enhancements:

## [](#couchbase-lite-release-notes)Couchbase Lite Release Notes

### [](#enhancements)Enhancements

None for this release

### [](#issues-and-resolutions)Issues and Resolutions

#### [](#fixed-issues)Fixed Issues

* [CBL-7660 — Resolved an issue in MultipeerReplicator.](https://jira.issues.couchbase.com/browse/CBL-7660)
* [CBL-7658 — Peer IP resolution may time out when the service is discovered on an IPv6 link-local interface](https://jira.issues.couchbase.com/browse/CBL-7658)

#### [](#known-issues)Known Issues

None for this release

### [](#breaking-changes)Breaking Changes

None for this release

### [](#deprecations)Deprecations

None for this release

## [](#maint-4-0-0)4.0.0 — October 2025

Version 4.0.0 for Objective-C delivers the following features and enhancements:

## [](#couchbase-lite-release-notes-2)Couchbase Lite Release Notes

### [](#enhancements-2)Enhancements

* [CBL-7568 — New Version Vector Database](https://issues.couchbase.com/browse/CBL-7568)
* [CBL-6569 — Disabled SQLite’s mmap by default](https://issues.couchbase.com/browse/CBL-6569)
* [CBL-7279 — Support timestamp property in Document](https://issues.couchbase.com/browse/CBL-7279)
* [CBL-7283 — Support Last-Write-Wins as the default Conflict Resolver for Replicator](https://issues.couchbase.com/browse/CBL-7283)
* [CBL-7348 — Update Database APIs to Return or Throw NotOpen Error for Closed Database Cases](https://issues.couchbase.com/browse/CBL-7348)

### [](#issues-and-resolutions-2)Issues and Resolutions

#### [](#fixed-issues-2)Fixed Issues

* [CBL-6504 — Query parser regression related to brackets](https://issues.couchbase.com/browse/CBL-6504)
* [CBL-6513 — Race creating the expiration column in a collection table](https://issues.couchbase.com/browse/CBL-6513)
* [CBL-7413 — Wrong error shown when using mismatch collections in Replicator](https://issues.couchbase.com/browse/CBL-7413)
* [CBL-7467 — TLS ClientHello missing Server Name when network interface is specified](https://issues.couchbase.com/browse/CBL-7467)

#### [](#known-issues-2)Known Issues

* [CBL-7572 — Database.Copy() doesn’t convert Self-Source-ID to the original Source ID](https://issues.couchbase.com/browse/CBL-7572)
* [CBL-7573 — Couchbase Lite 4.0 is allowed to connect to Sync Gateway 3.2.6/3.3.0](https://issues.couchbase.com/browse/CBL-7573)

### [](#breaking-changes-2)Breaking Changes

* [CBL-6596 — Vector Search Extension 2.0.0 Required for Couchbase Lite 4.0.0](https://jira.issues.couchbase.com/browse/CBL-6596)
* [CBL-7288 — Remove Deprecated Database APIs](https://issues.couchbase.com/browse/CBL-7288)
* [CBL-7292 — Removed: Deprecated Remove Change Listener APIs](https://issues.couchbase.com/browse/CBL-7292)
* [CBL-7296 — Removed: Deprecated QueryBuilder APIs](https://issues.couchbase.com/browse/CBL-7296)
* [CBL-7300 — Remove Deprecated Collection Management API in ReplicatorConfiguration](https://issues.couchbase.com/browse/CBL-7300)
* [CBL-7304 — Removed: Deprecated TLSIdentity’s createIdentity with isServer boolean flag](https://issues.couchbase.com/browse/CBL-7304)
* [CBL-7313 — Removed: Deprecated Logging APIs](https://issues.couchbase.com/browse/CBL-7313)
* [CBL-7378 — Removed: DatabaseConfiguration’s mmapEnabled property](https://issues.couchbase.com/browse/CBL-7378)
* [CBL-7390 — Removed: Deprecated Default Constants](https://issues.couchbase.com/browse/CBL-7390)
* [CBL-7571 — Removed Deprecated Replicator and Listener APIs](https://issues.couchbase.com/browse/CBL-7571)
* [CBL-7654 — MultipeerCertificateAuthenticator created with root certs fails to validate peer certificates](https://jira.issues.couchbase.com/browse/CBL-7654)

### [](#deprecations-2)Deprecations

None for this release

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 4.0.0, see [New in 4.0](../cbl-whatsnew.md)