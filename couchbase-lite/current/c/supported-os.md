---
title: Supported Operating System Versions
description: Couchbase Lite on C -- the OS and SDK versions on which this
  framework is supported
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.1/modules/c/pages/supported-os.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:couchbase-lite:c:supported-os.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/current/c/supported-os.html)

# Supported Operating System Versions

> Description — _Couchbase Lite on C — the OS and SDK versions on which this framework is supported_  
> Related Content — [What's New](#cbl-whatsnew.adoc) | [Release Notes](releasenotes.md) | [Compatibility](compatibility.md)

## [](#officially-supported-versions)Officially Supported Versions

Couchbase Lite for C is available on the platforms shown in the tables below.

> [!IMPORTANT]
> Deprecation Notice
> 
> Support for the following will be deprecated in this release and will be removed in a future release:
> 
> * Windows 10
> * Debian Linux 11 (Bullseye)
> 
> Please plan to migrate your apps to use an appropriate alternative version.

### [](#android)Android

> [!IMPORTANT]
> These requirements are for the **C/C++ SDK** on Android. Use the C/C++ SDK when using Qt or other C++ frameworks.
> 
> If you're developing with the **Java/Kotlin SDK** on Android, see [Couchbase Lite for Android - Supported OS Versions](../android/supported-os.md#officially-supported-versions).

| API | x86                        | x64                        | ARM 32                     | ARM 64                     |
| --- | -------------------------- | -------------------------- | -------------------------- | -------------------------- |
| 24+ | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |

### [](#ios)iOS

| Version | x86                        | x64                        | ARM 32                     | ARM 64                     |
| ------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- |
| 15      | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |

### [](#macos)macOS

| Version            | x64                        | ARM 64                     |
| ------------------ | -------------------------- | -------------------------- |
| macOS 15 (Sequoia) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| macOS 14 (Sonoma)  | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |

### [](#linux)Linux

| Distro          | Version                    | x64                        | ARM 32                     | ARM 64                     |
| --------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- |
| Debian          | 11 (Bullseye) (Deprecated) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 12 (Bookworm)   | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |                            |
| 13 (Trixie)     | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |                            |
| Raspberry Pi OS | 11 (Bullseye)              |                            | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 12 (Bookworm)   |                            | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |                            |
| 13 (Trixie)     |                            | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |                            |
| Ubuntu          | 22.04 LTS                  | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 24.04 LTS       | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |                            |

### [](#embedded-linux)Embedded Linux

| Distro          | Version                    | x64                        | ARM 32                     | ARM 64                     |
| --------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- |
| Debian          | 11 (Bullseye) (Deprecated) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 12 (Bookworm)   | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |                            |
| 13 (Trixie)     | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |                            |
| Raspberry Pi OS | 11 (Bullseye)              |                            | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 12 (Bookworm)   |                            | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |                            |
| 13 (Trixie)     |                            | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |                            |
| Ubuntu          | 22.04 LTS                  | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 24.04 LTS       | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |                            |

### [](#windows)Windows

|         | Version | x64                        |
| ------- | ------- | -------------------------- |
| Desktop | 10      | ![yes](../_images/yes.png) |
| Desktop | 11+     | ![yes](../_images/yes.png) |