---
title: New in 3.3
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.3/modules/ROOT/pages/cbl-whatsnew.adoc
pubDate: 2026-06-12T16:31:57.907Z
link: xref:3.3@couchbase-lite::cbl-whatsnew.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.3/cbl-whatsnew.html)

# New in 3.3

> [!NOTE]
> Couchbase Lite 3.0 introduces some breaking changes.  
> If you're upgrading from 2.x, refer to the appropriate upgrade page — see: [Upgrading](#lbl-upgrade).  
> You should be able to upgrade from 3.2.x to 3.3.x without manual intervention.

## [](#release-3-3-3-may-2026)Release 3.3.3 (May 2026)

Couchbase Lite Release 3.3.3 introduces fixes and enhancements for:

[Android](android/releasenotes.md#maint-3-3-3)| [Java](java/releasenotes.md#maint-3-3-3)| [Objective-C](objc/releasenotes.md#maint-latest)| [Swift](swift/releasenotes.md#maint-latest)

## [](#release-3-3-2-february-2026)Release 3.3.2 (February 2026)

Couchbase Lite Release 3.3.2 introduces fixes and enhancements for:

[Android](android/releasenotes.md#maint-latest)| [Objective-C](objc/releasenotes.md#maint-latest)| [Swift](swift/releasenotes.md#maint-latest)

## [](#release-3-3-1-december-2025)Release 3.3.1 (December 2025)

Couchbase Lite Release 3.3.1 introduces fixes and enhancements for:

[Android](android/releasenotes.md#maint-3-3-1)| [Objective-C](objc/releasenotes.md#maint-3-3-1)| [Swift](swift/releasenotes.md#maint-3-3-1)

## [](#release-3-3-0-october-2025)Release 3.3.0 (October 2025)

### [](#new-features)New Features

#### [](#multipeer-replicator)Multipeer Replicator

Couchbase Lite 3.3.0 introduces the new Multipeer Replicator API for bidirectional peer-to-peer synchronization in both Swift and Kotlin platforms. This replicator enables secure, direct synchronization between devices without the need for a centralized Sync Gateway.

The Multipeer Replicator supports:

* Peer discovery using DNS-SD (Bonjour) over a shared Wi-Fi network
* Encrypted TLS connections with certificate-based authentication
* Automatic mesh formation and replication routing between peers
* Real-time updates using continuous, push-and-pull replication

Each device advertises itself using a shared group ID, discovers others, and forms an optimized mesh network for efficient data sync. Multipeer Replicator performs authentication using client/server certificates, and applications can configure custom filters, conflict resolvers, and listeners for fine-grained control.

For more information about Multipeer Replicator, see:

* [Swift Multipeer Replicator](swift/p2psync-multipeer.md)
* [Android Multipeer Replicator](android/p2psync-multipeer.md)

> [!NOTE]
> This feature supports only continuous, push-and-pull replication. Version 3.3.0 disables Delta Sync by default.

## [](#see-also)See also

[What's new in previous version 3.2](../3.2/cbl-whatsnew.md)

### [](#couchbase-lite-release-notes)Couchbase Lite Release Notes

[Android](android/releasenotes.md)| [C](c/releasenotes.md)| [.NET](csharp/releasenotes.md)| [Java](java/releasenotes.md)| [Objective-C](objc/releasenotes.md)| [Swift](swift/releasenotes.md)

### [](#vector-search-release-notes)Vector Search Release Notes

[Android](android/vs-releasenotes.md)| [C](c/vs-releasenotes.md)| [.NET](csharp/vs-releasenotes.md)| [Java](java/vs-releasenotes.md)| [Objective-C](objc/vs-releasenotes.md)| [Swift](swift/vs-releasenotes.md)

## [](#lbl-upgrade)Upgrading

[Android](android/upgrade.md)| [C](c/upgrade.md)| [.NET](csharp/upgrade.md)| [Java](java/upgrade.md)| [Objective-C](objc/upgrade.md)| [Swift](swift/upgrade.md)