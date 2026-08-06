---
title: New in 4.1
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.1/modules/ROOT/pages/cbl-whatsnew.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:couchbase-lite::cbl-whatsnew.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/current/cbl-whatsnew.html)

# New in 4.1

> [!NOTE]
> Couchbase Lite 4.1 introduces some breaking changes.  
> If you're upgrading from 3.x or 4.0, see the appropriate upgrade page — [Upgrading](#lbl-upgrade). You cannot downgrade from 4.1 to earlier versions of Couchbase Lite.

## [](#release-4-1-0)Release 4.1.0

### [](#new-features)New Features

#### [](#ootb-support-for-peer-to-peer-sync-over-bluetooth-low-energy-ble-via-the-multipeer-replicator)OOTB Support for Peer-to-Peer Sync over Bluetooth Low Energy (BLE) via the Multipeer Replicator

Couchbase Lite 4.1 extends the Multipeer Replicator with Bluetooth Low Energy (BLE) as an additional transport alongside Wi-Fi. You can now configure the Multipeer Replicator to use Wi-Fi only, Bluetooth only, or both transports simultaneously.

When you enable both transports, the replicator automatically selects the best available transport for each peer and switches between them as network conditions change. The replicator prefers Wi-Fi when available. The replicator falls back to Bluetooth when Wi-Fi is unavailable and switches back to Wi-Fi when it becomes reachable again, without interrupting active replication.

BLE transport uses TLS encryption over L2CAP channels, providing the same security guarantees as Wi-Fi transport without requiring device pairing.

Platform requirements for Bluetooth transport:

* iOS 15 or later
* Android API 29 or later

This feature is available on Swift, Android (Kotlin/Java), and Objective-C.

For more information, see:

* [Swift Multipeer Replicator](swift/p2psync-multipeer.md)
* [Android Multipeer Replicator](android/p2psync-multipeer.md)
* [Objective-C Multipeer Replicator](objc/p2psync-multipeer.md)

> [!NOTE]
> Bluetooth has lower throughput and higher latency than Wi-Fi, and its reliability can decrease as more peers join the Bluetooth network. Use Wi-Fi as the primary transport for multipeer sync, with Bluetooth as a fallback.

#### [](#couchbase-lite-c-api-now-supported)Couchbase Lite C++ API Now Supported

Couchbase Lite 4.1 promotes the C++ wrapper API from volatile to a committed, supported API surface for Couchbase Lite C.

As of 4.1, the C++ API is a first-class, committed API with the following guarantees:

* Source compatibility across patch and minor releases within a major line
* Full availability across all Couchbase Lite C platforms, including iOS, Android, Windows, and Linux
* Inclusion in official QA coverage and release testing
* Documented deprecation policy for any future breaking changes

The cbl++ headers ship in all official Couchbase Lite C distributions. A small set of golden-path examples covering CRUD, query, replication, and logging is available in the documentation.

For more information, see [Couchbase Lite for C/C++](c/quickstart.md).

#### [](#windows-arm-support-for-couchbase-lite-c)Windows ARM Support for Couchbase Lite C

Couchbase Lite C 4.1 adds official support for Windows ARM64\. This enables developers targeting ARM-based Windows devices including laptops, tablets, and mini PCs to use Couchbase Lite C with full build and test coverage.

#### [](#replication-correlation-id)Replication Correlation ID

Couchbase Lite 4.1 exposes the Sync Gateway session correlation ID as a read-only property on the replicator. Sync Gateway generates and sends an `X-Correlation-ID` header during the WebSocket handshake that uniquely identifies each replication session. You can now read this ID from the replicator and include it in client-side logs to correlate them with Sync Gateway server-side logs when diagnosing replication issues.

This feature is available on all platforms: Swift, Objective-C, Android (Kotlin/Java), C, Java, and .NET.

For more information, see the Monitor section of the replication documentation for your platform:

* [Swift](swift/replication.md#lbl-repl-correlation-id)
* [Objective-C](objc/replication.md#lbl-repl-correlation-id)
* [Android](android/replication.md#lbl-repl-correlation-id)
* [C/C++](c/replication.md#lbl-repl-correlation-id)
* [Java](java/replication.md#lbl-repl-correlation-id)
* [.NET](csharp/replication.md#lbl-repl-correlation-id)

#### [](#kotlin-serialization-support-android)Kotlin Serialization Support (Android)

Couchbase Lite 4.1 for Android introduces native integration with `kotlinx.serialization`.

You can now decode Couchbase Lite `Document` and `Dictionary` types directly into `@Serializable` Kotlin data classes without reflection-based workarounds such as Gson or Jackson. The integration respects Kotlin nullability constraints and default property values during decoding.

This feature is Android-only.

For more information, see [Kotlin Serialization](android/kotlin-serialization.md).

## [](#see-also)See also

[What's new in previous version 4.0](../4.0/cbl-whatsnew.md)

### [](#couchbase-lite-release-notes)Couchbase Lite Release Notes

[Android](android/releasenotes.md)| [C](c/releasenotes.md)| [.NET](csharp/releasenotes.md)| [Java](java/releasenotes.md)| [Objective-C](objc/releasenotes.md)| [Swift](swift/releasenotes.md)

### [](#vector-search-release-notes)Vector Search Release Notes

[Android](android/vs-releasenotes.md)| [C](c/vs-releasenotes.md)| [.NET](csharp/vs-releasenotes.md)| [Java](java/vs-releasenotes.md)| [Objective-C](objc/vs-releasenotes.md)| [Swift](swift/vs-releasenotes.md)

## [](#lbl-upgrade)Upgrading

[Android](android/upgrade.md)| [C](c/upgrade.md)| [.NET](csharp/upgrade.md)| [Java](java/upgrade.md)| [Objective-C](objc/upgrade.md)| [Swift](swift/upgrade.md)