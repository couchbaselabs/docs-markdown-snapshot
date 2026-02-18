---
title: Preparing for Couchbase Lite on Android
description: Prerequisites for the installation of Couchbase Lite
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.0/modules/android/pages/gs-prereqs.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/couchbase-lite/current/android/gs-prereqs.html)

# Preparing for Couchbase Lite on Android

> Description — _Prerequisites for the installation of Couchbase Lite_  
> _Abstract — Laying out some of the pre-requisites and preparatory steps to be considered before installing Couchbase Lite for android_  

## [](#supported-versions)Supported Versions

> [!IMPORTANT]
> The requirements listed below are for the **Java/Kotlin SDK** on Android (Minimum API Level **22**).
> 
> If you’re developing with the **C/C++ SDK** on Android, the minimum API Level is **24**. For C/C++ SDK requirements, see [Couchbase Lite for C - Android Requirements](../c/supported-os.md#android).

The [Supported OS Versions](supported-os.md#supported-os-versions) lists certified Android versions. Couchbase does not test against, nor guarantee support for, uncertified Android versions such as versions built from source.

| Platform | Runtime architectures | Minimum API Level |
| -------- | --------------------- | ----------------- |
| Android  | armeabi-v7a           | 22                |
| Android  | arm64-v8a             | 22                |
| Android  | x86                   | 22                |
| Android  | x86\_64               | 22                |

## [](#supported-versions-for-vector-search-4-0-0)Supported Versions for Vector Search 4.0.0

> [!IMPORTANT]
> To use Vector Search, you must have Couchbase Lite installed and add the Vector Search extension to your Couchbase Lite application. Vector Search is available only for 64-bit architectures and Intel processors that support the Advanced Vector Extensions 2 (AVX2) instruction set. To verify whether your device supports the AVX2 instructions set, [follow these instructions.](https://www.intel.com/content/www/us/en/support/articles/000090473/processors/intel-core-processors.html)

| Platform | Runtime architectures | Minimum API Level |
| -------- | --------------------- | ----------------- |
| Android  | arm64-v8a             | 23                |
| Android  | x86\_64               | 23                |

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Prerequisites](gs-prereqs.md)
* [Install](gs-install.md)
* [Build and Run](gs-build.md)

.

###### [](#-2)

Learn more . . .

* [Databases](database.md)
* [Documents](document.md)
* [Blobs](blob.md)
* [Remote Sync Gateway](replication.md)
* [Handling Data Conflicts](conflict.md)

.

###### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.