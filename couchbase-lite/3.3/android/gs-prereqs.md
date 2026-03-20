---
title: Preparing for Couchbase Lite on Android
description: Prerequisites for the installation of Couchbase Lite
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.3/modules/android/pages/gs-prereqs.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:3.3@couchbase-lite:android:gs-prereqs.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.3/android/gs-prereqs.html)

# Preparing for Couchbase Lite on Android

> Description — _Prerequisites for the installation of Couchbase Lite_  
> _Abstract — Laying out some of the pre-requisites and preparatory steps to be considered before installing Couchbase Lite for android_  

## [](#supported-versions)Supported Versions

The operating systems listed below refer to "Certified" versions of Android. We do not test against, nor guarantee support for, uncertified Android versions such as versions built from source.

| Platform | Runtime architectures | Minimum API Level |
| -------- | --------------------- | ----------------- |
| Android  | armeabi-v7a           | 22                |
| Android  | arm64-v8a             | 22                |
| Android  | x86                   | 22                |
| Android  | x86\_64               | 22                |

## [](#supported-versions-for-vector-search-3-3-0)Supported Versions for Vector Search 3.3.0

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