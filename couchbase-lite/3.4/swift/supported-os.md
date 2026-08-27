---
title: Supported Operating System Versions
description: Couchbase Lite for Swift -- the OS and SDK versions on which this
  framework is supported
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.4/modules/swift/pages/supported-os.adoc
  xref: xref:3.4@couchbase-lite:swift:supported-os.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.4/swift/supported-os.html)

# Supported Operating System Versions

> Description — _Couchbase Lite for Swift — the OS and SDK versions on which this framework is supported_  
> Related Content — [What's New](#cbl-whatsnew.adoc) | [Release Notes](releasenotes.md) | [Compatibility](compatibility.md)

## [](#officially-supported-versions)Officially Supported Versions

The following table identifies the [supported platforms](#supported-os-versions).

__Table 1\. Supported versions__
| Platform | Minimum OS version        |
| -------- | ------------------------- |
| iOS      | 15.0+                     |
| macOS    | 14 (Sonoma), 15 (Sequoia) |

> [!NOTE]
> Couchbase Lite for Swift provides native support for both Mac Catalyst and M1\.

## [](#feature-specific-platform-support)Feature Specific Platform Support

The following table lists platform requirements for features that support a subset of the [Table 1](#supported) platforms.

### [](#multipeer-p2p-platform-requirements)Multipeer Peer-to-Peer Replicator

The Multipeer Peer-to-Peer Replicator has the following requirements in addition to the platform requirements above.

__Table 2\. Minimum iOS version by transport__
| Transport       | Minimum iOS Version | Notes                                                                               |
| --------------- | ------------------- | ----------------------------------------------------------------------------------- |
| Wi-Fi / LAN     | iOS 15              |                                                                                     |
| Bluetooth (BLE) | iOS 15              | See [Bluetooth Platform Configuration](p2psync-multipeer.md#platform-configuration) |

## [](#deprecated-versions)Deprecated Versions

| Operating System | Version      | Deprecation Release |
| ---------------- | ------------ | ------------------- |
| macOS            | 13 (Ventura) | 3.3.0               |

## [](#removed-versions)Removed Versions

| Operating System | Version  | Removed | Deprecation Release |
| ---------------- | -------- | ------- | ------------------- |
| iOS              | iOS 10   | 3.1.1   | 3.1.0               |
| iOS 11           | 3.2.0    | 3.1.1   |                     |
| iOS 12           | 3.3.0    | 3.3.0   |                     |
| iOS 13 & 14      | 3.2.0    | 3.3.0   |                     |
| macOS            | macOS 12 | 3.3.0   | 3.2.0               |
| macOS 11         | 3.2.0    | 3.1.0   |                     |
| OSX 10.15        | 3.2.0    | 3.1.0   |                     |
| OSX 10.14        | 3.2.0    | 3.1.0   |                     |