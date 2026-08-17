---
title: Supported Operating System Versions
description: Couchbase Lite on Android -- the OS and SDK versions on which this
  framework is supported
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.4/modules/android/pages/supported-os.adoc
  xref: xref:3.4@couchbase-lite:android:supported-os.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.4/android/supported-os.html)

# Supported Operating System Versions

> Description — _Couchbase Lite on Android — the OS and SDK versions on which this framework is supported_  
> Related Content — [What's New](#cbl-whatsnew.adoc) | [Release Notes](releasenotes.md) | [Compatibility](compatibility.md)

## [](#officially-supported-versions)Officially Supported Versions

> [!IMPORTANT]
> The requirements listed below are for the **Java/Kotlin SDK** on Android.
> 
> If you're developing with the **C/C++ SDK** on Android, the minimum API Level is **24**. For C/C++ SDK requirements, see [Couchbase Lite for C - Android Requirements](../c/supported-os.md#android).

The operating systems listed in [Table 1](#supported-os-versions) are certified Android versions. Couchbase does not test against, nor guarantee support for, uncertified Android versions such as versions built from source.

__Table 1\. Supported versions__
| Platform | Runtime architectures | Minimum API Level |
| -------- | --------------------- | ----------------- |
| Android  | armeabi-v7a           | 24                |
| Android  | arm64-v8a             | 24                |
| Android  | x86                   | 24                |
| Android  | x86\_64               | 24                |

## [](#bluetooth-transport-requirements)Bluetooth Transport Requirements

> [!NOTE]
> Bluetooth Low Energy (BLE) transport for the [Multipeer P2P Replicator](p2psync-multipeer.md) requires **Android API 29 (Android 10) or later**, due to the availability of BLE L2CAP support on that API level. This requirement applies only to Multipeer P2P Replication, not to general data sync.
> 
> Devices running API 24—​28 can still use Couchbase Lite 3.4 with all non-Bluetooth features, including Wi-Fi-based Multipeer replication. If your application targets API 24—​28, do not include `.bluetooth` in your `MultipeerReplicatorConfiguration.transports` set.

| Feature                             | Minimum API Level |
| ----------------------------------- | ----------------- |
| Couchbase Lite core                 | 24                |
| Multipeer Replicator (Wi-Fi)        | 24                |
| Multipeer Replicator (Bluetooth LE) | 29                |