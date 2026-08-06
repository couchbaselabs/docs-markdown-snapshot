---
title: Supported Operating System Versions
description: Couchbase Lite on Android -- the OS and SDK versions on which this
  framework is supported
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.1/modules/android/pages/supported-os.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:couchbase-lite:android:supported-os.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/current/android/supported-os.html)

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
> Bluetooth Low Energy (BLE) transport for the Multipeer Replicator requires **Android API 29 (Android 10) or later**, due to the availability of BLE L2CAP support on that API level.
> 
> Devices running API 24—​28 can still use Couchbase Lite with all non-Bluetooth features, including Wi-Fi-based Multipeer replication. If your application targets API 24—​28, do not include `.bluetooth` in your `MultipeerReplicatorConfiguration.transports` set.

## [](#feature-requirements)Feature Requirements

Some features require a greater minimum API level than the general CBL requirement.

__Table 2\. Multipeer Replicator API level requirements__
| Feature                                              | Minimum Android API | Notes                                                                                                                                                                    |
| ---------------------------------------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Multipeer Replicator: Wi-Fi transport                | API 24              | Peers must connect to the same Wi-Fi network.                                                                                                                            |
| Multipeer Replicator: Bluetooth Low Energy transport | API 29              | Requires additional manifest permissions and runtime permission requests. See [Bluetooth Platform Configuration](p2psync-multipeer.md#bluetooth-platform-configuration). |