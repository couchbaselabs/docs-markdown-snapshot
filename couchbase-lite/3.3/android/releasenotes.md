---
title: Couchbase Lite Release Notes
description: Couchbase Lite on Android
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.3/modules/android/pages/releasenotes.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/couchbase-lite/3.3/android/releasenotes.html)

# Couchbase Lite Release Notes

## [](#maint-3-3-1)3.3.1 — December 2025

Version 3.3.1 for Android delivers the following features and enhancements:

### [](#enhancements)Enhancements

None for this release

### [](#issues-and-resolutions)Issues and Resolutions

#### [](#fixed-issues)Fixed Issues

* [CBL-7678 — Intermittent replicator crash during pusher destruction](https://jira.issues.couchbase.com/browse/CBL-7678)

### [](#known-issues)Known Issues

None for this release

### [](#breaking-changes)Breaking Changes

None for this release

### [](#deprecations)Deprecations

None for this release

## [](#maint-3-3-0)3.3.0 — October 2025

Version 3.3.0 for Android delivers the following features and enhancements:

### [](#enhancements-2)Enhancements

* [CBL-6733 — Multipeer Replicator for Peer-to-Peer Sync over Wi-Fi](https://jira.issues.couchbase.com/browse/CBL-6733)
* [CBL-7195 — Upgrade SQLite to 3.50.3](https://jira.issues.couchbase.com/browse/CBL-7195)
* [CBL-7214 — Update minimum supported API level to 24](https://jira.issues.couchbase.com/browse/CBL-7214)
* [CBL-7233 — Add API for creating ReplicatorConfiguration with collection configs and endpoint](https://jira.issues.couchbase.com/browse/CBL-7233)
* [CBL-7360 — Update mbedTLS to 3.6.4](https://jira.issues.couchbase.com/browse/CBL-7360)
* [CBL-7409 — Improve conflict resolution with multiple remotes](https://jira.issues.couchbase.com/browse/CBL-7409)

### [](#issues-and-resolutions-2)Issues and Resolutions

#### [](#fixed-issues-2)Fixed Issues

* [CBL-6791 — Starting a Live Query in the Background May Crash the App](https://jira.issues.couchbase.com/browse/CBL-6791)
* [CBL-6799 — Potential crash in URLEndpointListener due to accessing a NULL responseTimer during stop](https://jira.issues.couchbase.com/browse/CBL-6799)
* [CBL-7181 — Assertion Failure in URLEndpointListener Due to Collection Mismatch with Connected Replicator](https://jira.issues.couchbase.com/browse/CBL-7181)
* [CBL-7189 — Assertion failure caused by pull filter during replication](https://jira.issues.couchbase.com/browse/CBL-7189)

### [](#known-issues-2)Known Issues

None for this release

### [](#deprecations-2)Deprecations

* [CBL-7009 — Deprecate: Create Identity API with Server Flag](https://jira.issues.couchbase.com/browse/CBL-7009)
* [CBL-7235 — Deprecate: ReplicatorConfiguration constructor with a target endpoint only](https://jira.issues.couchbase.com/browse/CBL-7235)
* [CBL-7237 — Deprecate: ReplicatorConfiguration API for managing collection configurations](https://jira.issues.couchbase.com/browse/CBL-7237)
* [CBL-7239 — Deprecate: CollectionConfiguration constructors without collection](https://jira.issues.couchbase.com/browse/CBL-7239)
* [CBL-7421 — Deprecate: CollectionConfiguration’s API without collection (Kotlin)](https://jira.issues.couchbase.com/browse/CBL-7421)
* [CBL-7422 — Deprecate: WorkManagerReplicatorConfiguration.from(target: Endpoint) (Kotlin)](https://jira.issues.couchbase.com/browse/CBL-7422)
* [CBL-7423 — Deprecate: ReplicatorConfiguration’s newConfig with endpoint and collection map (Kotlin)](https://jira.issues.couchbase.com/browse/CBL-7423)

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 3.3.0, see [New in 3.3](../cbl-whatsnew.md)