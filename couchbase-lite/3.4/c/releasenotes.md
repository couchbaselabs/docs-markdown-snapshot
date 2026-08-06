---
title: Couchbase Lite Release Notes
description: Couchbase Lite on C
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.4/modules/c/pages/releasenotes.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:3.4@couchbase-lite:c:releasenotes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.4/c/releasenotes.html)

# Couchbase Lite Release Notes

## [](#maint-3-4-0)3.4.0 — June 2026

Version 3.4.0 for C delivers the following features and enhancements:

### [](#enhancements)Enhancements

* [CBL-7926 — Include the C++ API headers in the iOS XCFramework](https://jira.issues.couchbase.com/browse/CBL-7926)
* [CBL-7968 — Improve COUNT query performance on the default collection](https://jira.issues.couchbase.com/browse/CBL-7968)
* [CBL-7970 — Improve checkpoint resolution for non-numeric (compound) Sync Gateway sequences](https://jira.issues.couchbase.com/browse/CBL-7970)
* [CBL-7971 — API to access the Replicator's correlation ID](https://jira.issues.couchbase.com/browse/CBL-7971)
* [CBL-7972 — The C++ API is now officially supported](https://jira.issues.couchbase.com/browse/CBL-7972)
* [CBL-7973 — Add support for Windows on ARM64](https://jira.issues.couchbase.com/browse/CBL-7973)

### [](#fixed-issues)Fixed Issues

* [CBL-7766 — SQL++ fails to parse the IN operator](https://jira.issues.couchbase.com/browse/CBL-7766)
* [CBL-7960 — Purging a deleted document does not trigger query change listener events](https://jira.issues.couchbase.com/browse/CBL-7960)
* [CBL-7985 — MultipeerReplicator may crash when registering a replication task while stopping](https://jira.issues.couchbase.com/browse/CBL-7985)
* [CBL-8363 — Crash due to buffer overrun in Encoder::snip while saving a Version Vector document](https://jira.issues.couchbase.com/browse/CBL-8363)
* [CBL-8380 — A peer connection that closes before the TLS handshake completes may hang the MultipeerReplicator](https://jira.issues.couchbase.com/browse/CBL-8380)
* [CBL-8475 — Use-after-free crash (EXC\_BAD\_ACCESS) when a replicator is torn down](https://jira.issues.couchbase.com/browse/CBL-8475)
* [CBL-8515 — A stalled inbound P2P TLS handshake can wedge the MultipeerReplicator](https://jira.issues.couchbase.com/browse/CBL-8515)
* [CBL-8561 — Replicator may time out when replicating a large number of collections](https://jira.issues.couchbase.com/browse/CBL-8561)

### [](#known-issues)Known Issues

None for this release.

### [](#deprecations)Deprecations

None for this release.

> [!NOTE]
> For an overview of the latest features offered in Couchbase Lite 3.4, see [New in 3.4](../cbl-whatsnew.md).