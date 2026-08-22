---
title: Compatibility
description: Couchbase Lite framework and Sync Gateway compatibility
pubDate: 2026-08-22T04:32:17.641Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.1/modules/android/pages/compatibility.adoc
  xref: xref:couchbase-lite:android:compatibility.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/current/android/compatibility.html)

# Compatibility

> Description — _Couchbase Lite framework and Sync Gateway compatibility_  
> _Abstract — This content identifies the compatibility of Couchbase Lite on Android with Sync Gateway, together with the operating systems upon which it is supported._  
> Related Content — [What's New](../cbl-whatsnew.md) | [Release Notes](releasenotes.md) | [Supported Platforms](supported-os.md)

## [](#couchbase-litesync-gateway-matrix)Couchbase Lite/Sync Gateway Matrix

The table below summarizes the compatible versions of Couchbase Lite with Sync Gateway.

__Table 1\. Sync Gateway and Couchbase Lite Compatibility Matrix__
| Sync Gateway Versions ↓            | Couchbase Lite →           |                            |                            |                            |                            |                            |                            |                            |                            |
| ---------------------------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- |
| 2.0                                | 2.1                        | 2.5 - 2.8                  | 3.0.0                      | 3.1.0                      | 3.2.0                      | 3.3.0                      | 4.0.0                      | 4.1.0                      |                            |
| 2.0 and 2.1                        | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![no](../_images/no.png)   | ![no](../_images/no.png)   |
| 2.5 to 2.8with delta sync disabled | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![no](../_images/no.png)   | ![no](../_images/no.png)   |
| 2.5 to 2.8with delta sync enabled  | ![no](../_images/no.png)   | ![no](../_images/no.png)   | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![no](../_images/no.png)   | ![no](../_images/no.png)   |
| 3.0.0                              | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![no](../_images/no.png)   | ![no](../_images/no.png)   |
| 3.1.0                              | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![no](../_images/no.png)   | ![no](../_images/no.png)   |
| 3.2.0                              | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![no](../_images/no.png)   | ![no](../_images/no.png)   |
| 3.3.0                              | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![no](../_images/no.png)   | ![no](../_images/no.png)   |
| 4.0.0                              | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |

## [](#operating-system-sdk-support)Operating System SDK Support

The table below summarizes the Operating System SDK versions supported by Couchbase Lite.

__Table 2\. OS — SDK Support__
|                               | 2.1                                                                | 2.5                                                                | 2.6                                                                | 2.7                                                                | 2.8                                                                | 3.0                                                  | 3.1                                              | 3.2                                              | 3.3                                              | 4.0                                              | 4.1                                              |
| ----------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ---------------------------------------------------- | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| Android                       | [archive link](https://docs-archive.couchbase.com/home/index.html) | [archive link](https://docs-archive.couchbase.com/home/index.html) | [archive link](https://docs-archive.couchbase.com/home/index.html) | [archive link](https://docs-archive.couchbase.com/home/index.html) | [link](#2.8@couchbase-lite:android:supported-os.adoc)              | [link](../../3.0/android/supported-os.md)            | [link](../../3.1/android/supported-os.md)        | [link](../../3.2/android/supported-os.md)        | [link](../../3.3/android/supported-os.md)        | [link](../../4.0/android/supported-os.md)        | [link](supported-os.md)                          |
| C                             | \-                                                                 | \-                                                                 | \-                                                                 | \-                                                                 | \-                                                                 | [link](../../3.0/c/supported-os.md)                  | [link](../../3.1/c/supported-os.md)              | [link](../../3.2/c/supported-os.md)              | [link](../../3.3/c/supported-os.md)              | [link](../../4.0/c/supported-os.md)              | [link](../c/supported-os.md)                     |
| iOS                           | [archive link](https://docs-archive.couchbase.com/home/index.html) | [archive link](https://docs-archive.couchbase.com/home/index.html) | [archive link](https://docs-archive.couchbase.com/home/index.html) | [archive link](https://docs-archive.couchbase.com/home/index.html) | [link](#2.8@couchbase-lite:swift:supported-os.adoc)                | [link](../../3.0/swift/supported-os.md)              | [link](../../3.1/swift/supported-os.md)          | [link](../../3.2/swift/supported-os.md)          | [link](../../3.3/swift/supported-os.md)          | [link](../../4.0/swift/supported-os.md)          | [link](../swift/supported-os.md)                 |
| Java                          | \-                                                                 | \-                                                                 | \-                                                                 | [archive link](https://docs-archive.couchbase.com/home/index.html) | [link](#2.8@couchbase-lite:java:supported-os.adoc)                 | [link](../../3.0/java/supported-os.md)               | [link](../../3.1/java/supported-os.md)           | [link](../../3.2/java/supported-os.md)           | [link](../../3.3/java/supported-os.md)           | [link](../../4.0/java/supported-os.md)           | [link](../java/supported-os.md)                  |
| JavaScript                    | \-                                                                 | \-                                                                 | \-                                                                 | [archive link](https://docs-archive.couchbase.com/home/index.html) | [archive link](https://docs-archive.couchbase.com/home/index.html) | [link](#2.8@couchbase-lite:ROOT:javascript.adoc)     | [link](#3.0@couchbase-lite:ROOT:javascript.adoc) | [link](#3.1@couchbase-lite:ROOT:javascript.adoc) | [link](#3.2@couchbase-lite:ROOT:javascript.adoc) | [link](#3.3@couchbase-lite:ROOT:javascript.adoc) | [link](#4.0@couchbase-lite:ROOT:javascript.adoc) |
| [link](#ROOT:javascript.adoc) | .NET                                                               | [archive link](https://docs-archive.couchbase.com/home/index.html) | [archive link](https://docs-archive.couchbase.com/home/index.html) | [archive link](https://docs-archive.couchbase.com/home/index.html) | [archive link](https://docs-archive.couchbase.com/home/index.html) | [link](#2.8@couchbase-lite:csharp:supported-os.adoc) | [link](../../3.0/csharp/supported-os.md)         | [link](../../3.1/csharp/supported-os.md)         | [link](../../3.2/csharp/supported-os.md)         | [link](../../3.3/csharp/supported-os.md)         | [link](../../4.0/csharp/supported-os.md)         |

## [](#related-content)Related Content

###### [](#)

Product Notes

* [Release Notes](releasenotes.md)
* [Compatibility](compatibility.md)
* [Supported Platforms](supported-os.md)
* [What's New](#cbl-whatsnew.adoc)

.

###### [](#-2)

Starting Points

* [Databases](database.md)
* [Documents](document.md)
* [Blobs](blob.md)
* [Remote Sync Gateway](replication.md)
* [Handling Data Conflicts](conflict.md)

.

###### [](#-3)

Tutorials

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.