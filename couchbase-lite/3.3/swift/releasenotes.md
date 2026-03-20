---
title: Couchbase Lite Release Notes
description: Couchbase Lite on Swift
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.3/modules/swift/pages/releasenotes.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:3.3@couchbase-lite:swift:releasenotes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.3/swift/releasenotes.html)

# Couchbase Lite Release Notes

## [](#maint-3-3-2)3.3.2 — February 2026

Version 3.3.2 for Swift delivers the following features and enhancements:

### [](#enhancements)Enhancements

* [CBL-7751 — Update mbedTLS to 3.6.5](https://jira.issues.couchbase.com/browse/CBL-7751)
* [CBL-7776 — Increase Replicator’s WebSocket PING / PONG timeout](https://jira.issues.couchbase.com/browse/CBL-7776)

### [](#fixed-issues)Fixed Issues

* [CBL-7762 — Increase Replicator Database Pool Borrow Timeout](https://jira.issues.couchbase.com/browse/CBL-7762)
* [CBL-7781 — Fix SQL++ parser failure for IN operator](https://jira.issues.couchbase.com/browse/CBL-7781)

### [](#known-issues)Known Issues

None for this release

### [](#deprecations)Deprecations

None for this release

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 3.3, see [New in 3.3](../cbl-whatsnew.md)

## [](#maint-3-3-1)3.3.1 — December 2025

Version 3.3.1 for Swift delivers the following features and enhancements:

### [](#enhancements-2)Enhancements

None for this release

### [](#fixed-issues-2)Fixed Issues

* [CBL-7657 — Peer IP resolution may time out when the service is discovered on an IPv6 link-local interface](https://jira.issues.couchbase.com/browse/CBL-7657)
* [CBL-7678 — Intermittent replicator crash during pusher destruction](https://jira.issues.couchbase.com/browse/CBL-7678)

### [](#known-issues-2)Known Issues

None for this release

### [](#breaking-changes)Breaking Changes

None for this release

### [](#deprecations-2)Deprecations

None for this release

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 3.3, see [New in 3.3](../cbl-whatsnew.md)

## [](#maint-3-3-0)3.3.0 — October 2025

Version 3.3.0 for Swift delivers the following features and enhancements:

### [](#enhancements-3)Enhancements

* [CBL-6733 — Multipeer Replicator for Peer-to-Peer Sync over Wi-Fi](https://jira.issues.couchbase.com/browse/CBL-6733)
* [CBL-7195 — Upgrade SQLite to 3.50.3](https://jira.issues.couchbase.com/browse/CBL-7195)
* [CBL-7360 — Update mbedTLS to 3.6.4](https://jira.issues.couchbase.com/browse/CBL-7360)
* [CBL-7409 — Improve conflict resolution with multiple remotes](https://jira.issues.couchbase.com/browse/CBL-7409)
* [CBL-7206 — Update Minimum Supported iOS to 15.0 and macOS to 13.0](https://jira.issues.couchbase.com/browse/CBL-7206)
* [CBL-7234 — Add API for creating ReplicatorConfiguration with collection configs and endpoint](https://jira.issues.couchbase.com/browse/CBL-7234)

### [](#fixed-issues-3)Fixed Issues

* [CBL-6791 — Starting a Live Query in the Background May Crash the App](https://jira.issues.couchbase.com/browse/CBL-6791)
* [CBL-6799 — Potential crash in URLEndpointListener due to accessing a NULL responseTimer during stop](https://jira.issues.couchbase.com/browse/CBL-6799)
* [CBL-7146 — UserAgent shows incorrect info](https://jira.issues.couchbase.com/browse/CBL-7146)
* [CBL-7167 — Getting non existing TLS Identity using label shouldn’t throw an error](https://jira.issues.couchbase.com/browse/CBL-7167)
* [CBL-7179 — Swift Codable skips nil values during encoding](https://jira.issues.couchbase.com/browse/CBL-7179)
* [CBL-7181 — Assertion Failure in URLEndpointListener Due to Collection Mismatch with Connected Replicator](https://jira.issues.couchbase.com/browse/CBL-7181)
* [CBL-7189 — Assertion failure caused by pull filter during replication](https://jira.issues.couchbase.com/browse/CBL-7189)
* [CBL-7429 — Swift Codable Result.data(as:) decoding fails for some ISO8601 formats](https://jira.issues.couchbase.com/browse/CBL-7429)
* [CBL-7468 — TLS ClientHello missing Server Name when network interface is specified](https://jira.issues.couchbase.com/browse/CBL-7468)

### [](#known-issues-3)Known Issues

None for this release

### [](#deprecations-3)Deprecations

* [CBL-6813 — Deprecate: removeChangeListenerWithToken for Replicator, Query and MessageEndpointListener](https://jira.issues.couchbase.com/browse/CBL-6813)
* [CBL-7008 — Deprecate: Create Identity API with Server Flag](https://jira.issues.couchbase.com/browse/CBL-7008)
* [CBL-7236 — Deprecate: ReplicatorConfiguration constructor with a target endpoint only](https://jira.issues.couchbase.com/browse/CBL-7236)
* [CBL-7238 — Deprecate: ReplicatorConfiguration API for managing collection configurations](https://jira.issues.couchbase.com/browse/CBL-7238)
* [CBL-7240 — Deprecate: CollectionConfiguration constructor without collection](https://jira.issues.couchbase.com/browse/CBL-7240)

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 3.3, see [New in 3.3](../cbl-whatsnew.md)