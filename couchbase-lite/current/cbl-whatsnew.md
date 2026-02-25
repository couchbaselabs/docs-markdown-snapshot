---
title: New in 4.0
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.0/modules/ROOT/pages/cbl-whatsnew.adoc
pubDate: 2026-02-25T03:45:01.178Z
link: xref:couchbase-lite::cbl-whatsnew.adoc[]
---

[View original HTML](/couchbase-lite/current/cbl-whatsnew.html)

# New in 4.0

> [!NOTE]
> Couchbase Lite 4.0 introduces some breaking changes.  
> If you’re upgrading from 3.x, see the appropriate upgrade page — [Upgrading](#lbl-upgrade). You cannot downgrade from 4.0 to earlier versions of Couchbase Lite.

## [](#release-4-0-3-february-2026)Release 4.0.3 (February 2026)

Couchbase Lite Release 4.0.3 introduces fixes and enhancements for:

[Android](android/releasenotes.md#maint-latest)| [C](c/releasenotes.md#maint-latest)| [.NET](csharp/releasenotes.md#maint-latest)| [Java](java/releasenotes.md#maint-latest)| [Objective-C](objc/releasenotes.md#maint-latest)| [Swift](swift/releasenotes.md#maint-latest)

## [](#release-4-0-2-december-2025)Release 4.0.2 (December 2025)

Couchbase Lite Release 4.0.2 introduces fixes and enhancements for:

[Android](android/releasenotes.md#maint-4-0-2)| [C](c/releasenotes.md#maint-4-0-2)| [.NET](csharp/releasenotes.md#maint-4-0-2)| [Java](java/releasenotes.md#maint-4-0-2)| [Objective-C](objc/releasenotes.md#maint-4-0-2)| [Swift](swift/releasenotes.md#maint-4-0-2)

## [](#release-4-0-1-november-2025)Release 4.0.1 (November 2025)

Couchbase Lite Release 4.0.1 introduces fixes and enhancements for:

[Objective-C](objc/releasenotes.md#maint-4-0-1)| [Swift](swift/releasenotes.md#maint-4-0-1)

## [](#release-4-0-0-october-2025)Release 4.0.0 (October 2025)

Couchbase Lite Release 4.0 fundamentally transforms document versioning and conflict resolution by introducing version vectors, replacing the traditional revision tree approach. This architectural change enables superior conflict resolution, improved synchronization performance, and seamless data consistency.

### [](#new-features)New Features

[Version Vectors](#version-vectors) | [Mobile XDCR Coexistence](#mobile-xdcr-coexistence)

#### [](#version-vectors)Version Vectors

Couchbase Lite 4.0 replaces revision trees with version vectors for document versioning and conflict resolution. This change aligns Couchbase Lite with Couchbase Server and Sync Gateway, ensuring more consistent behavior in distributed and multi-cluster deployments.

Key changes include:

* **Revision IDs → Versions**: Each revision is now identified by a version in the format `<timestamp>@<source-id>`.
* **Revision Trees → Version Vectors**: A version vector is an ordered list of the latest versions from all sources that have modified a document. This uniquely identifies both the state and history of a document.
* **Hybrid Logical Clocks (HLCs)**: Timestamps are now based on hybrid logical clocks, enabling last-writer-wins conflict resolution and simpler pruning of old revisions.

For more information about version vectors, see:

* [Android - version vectors](android/version-vectors.md)
* [C - version vectors](c/version-vectors.md)
* [.NET - version vectors](csharp/version-vectors.md)
* [Java - version vectors](java/version-vectors.md)
* [Objective-C - version vectors](objc/version-vectors.md)
* [Swift - version vectors](swift/version-vectors.md)

#### [](#mobile-xdcr-coexistence)Mobile XDCR Coexistence

Couchbase Lite 4.0 version vector model brings it into alignment with Couchbase Server Cross Data Center Replication (XDCR) and Sync Gateway. This ensures that documents can sync seamlessly across:

* Mobile-to-Server replication.
* Multi-cluster Couchbase Server environments.
* Peer-to-peer topologies.

## [](#see-also)See Also

[What’s new in previous version 3.3](../3.3/cbl-whatsnew.md)

### [](#couchbase-lite-release-notes)Couchbase Lite Release Notes

[Android](android/releasenotes.md)| [C](c/releasenotes.md)| [.NET](csharp/releasenotes.md)| [Java](java/releasenotes.md)| [Objective-C](objc/releasenotes.md)| [Swift](swift/releasenotes.md)

### [](#vector-search-release-notes)Vector Search Release Notes

[Android](android/vs-releasenotes.md)| [C](c/vs-releasenotes.md)| [.NET](csharp/vs-releasenotes.md)| [Java](java/vs-releasenotes.md)| [Objective-C](objc/vs-releasenotes.md)| [Swift](swift/vs-releasenotes.md)

## [](#lbl-upgrade)Upgrading

[Android](android/upgrade.md)| [C](c/upgrade.md)| [.NET](csharp/upgrade.md)| [Java](java/upgrade.md)| [Objective-C](objc/upgrade.md)| [Swift](swift/upgrade.md)