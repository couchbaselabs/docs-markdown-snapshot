[View original HTML](/couchbase-lite/3.3/c/compatibility.html)

> Description — _Couchbase Lite framework and Sync Gateway compatibility_  
> _Abstract — This content identifies the compatibility of Couchbase Lite on C with Sync Gateway, together with the operating systems upon which it is supported._  
> Related Content — [What’s New](#cbl-whatsnew.adoc) | [Release Notes](releasenotes.md) | [Supported Platforms](supported-os.md)

## [](#couchbase-litesync-gateway-matrix)Couchbase Lite/Sync Gateway Matrix

The table below summarizes the compatible versions of Couchbase Lite with Sync Gateway.

__Table 1\. Sync Gateway and Couchbase Lite Compatibility Matrix__
| Sync Gateway Versions ↓                                                                                         | Couchbase Lite →           |                            |                            |                            |                            |                            |                            |                            |
| --------------------------------------------------------------------------------------------------------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- |
| 1.4 **\[[1](#%5Ffootnotedef%5F1 "View footnote.")\]\]**                                                         | 2.0                        | 2.1                        | 2.5 - 2.8                  | 3.0.0                      | 3.1.0                      | 3.2.0                      | 3.3.0                      |                            |
| 1.4 **\[[2](#%5Ffootnotedef%5F2 "View footnote.")\]** and 1.5 **\[[3](#%5Ffootnotedef%5F3 "View footnote.")\]** | ![yes](../_images/yes.png) | ![no](../_images/no.png)   | ![no](../_images/no.png)   | ![no](../_images/no.png)   | ![no](../_images/no.png)   | ![no](../_images/no.png)   | ![no](../_images/no.png)   | ![no](../_images/no.png)   |
| 2.0 and 2.1                                                                                                     | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 2.5 to 2.8with delta sync disabled                                                                              | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 2.5 to 2.8with delta sync enabled                                                                               | ![no](../_images/no.png)   | ![no](../_images/no.png)   | ![no](../_images/no.png)   | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 3.0.0                                                                                                           | ![no](../_images/no.png)   | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 3.1.0                                                                                                           | ![no](../_images/no.png)   | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 3.2.0                                                                                                           | ![no](../_images/no.png)   | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 3.3.0                                                                                                           | ![no](../_images/no.png)   | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |

## [](#operating-system-sdk-support)Operating System SDK Support

The table below summarizes the Operating System SDK versions supported by Couchbase Lite.

__Table 2\. OS — SDK Support__
|            | 2.0                                                                | 2.1                                                                | 2.5                                                                | 2.6                                                                | 2.7                                                                | 2.8                                                   | 3.0                                                   | 3.1                                                   | 3.2                                              | 3.3                                              |
| ---------- | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ------------------------------------------------------------------ | ----------------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | ------------------------------------------------ | ------------------------------------------------ |
| Android    | [archive link](https://docs-archive.couchbase.com/home/index.html) | [archive link](https://docs-archive.couchbase.com/home/index.html) | [archive link](https://docs-archive.couchbase.com/home/index.html) | [archive link](https://docs-archive.couchbase.com/home/index.html) | [archive link](https://docs-archive.couchbase.com/home/index.html) | [link](#2.8@couchbase-lite:android:supported-os.adoc) | [link](#3.0@couchbase-lite:android:supported-os.adoc) | [link](#3.1@couchbase-lite:android:supported-os.adoc) | [link](../../3.2/android/supported-os.md)        | [link](../android/supported-os.md)               |
| C          | \-                                                                 | \-                                                                 | \-                                                                 | \-                                                                 | \-                                                                 | \-                                                    | [link](#3.0@couchbase-lite:c:supported-os.adoc)       | [link](#3.1@couchbase-lite:c:supported-os.adoc)       | [link](../../3.2/c/supported-os.md)              | [link](supported-os.md)                          |
| iOS        | [archive link](https://docs-archive.couchbase.com/home/index.html) | [archive link](https://docs-archive.couchbase.com/home/index.html) | [archive link](https://docs-archive.couchbase.com/home/index.html) | [archive link](https://docs-archive.couchbase.com/home/index.html) | [archive link](https://docs-archive.couchbase.com/home/index.html) | [link](#2.8@couchbase-lite:swift:supported-os.adoc)   | [link](#3.0@couchbase-lite:swift:supported-os.adoc)   | [link](#3.1@couchbase-lite:swift:supported-os.adoc)   | [link](../../3.2/swift/supported-os.md)          | [link](../swift/supported-os.md)                 |
| Java       | \-                                                                 | \-                                                                 | \-                                                                 | \-                                                                 | [archive link](https://docs-archive.couchbase.com/home/index.html) | [link](#2.8@couchbase-lite:java:supported-os.adoc)    | [link](#3.0@couchbase-lite:java:supported-os.adoc)    | [link](#3.1@couchbase-lite:java:supported-os.adoc)    | [link](../../3.2/java/supported-os.md)           | [link](../java/supported-os.md)                  |
| Javascript | \-                                                                 | \-                                                                 | \-                                                                 | [archive link](https://docs-archive.couchbase.com/home/index.html) | [archive link](https://docs-archive.couchbase.com/home/index.html) | [link](#2.8@couchbase-lite:ROOT:javascript.adoc)      | [link](#3.0@couchbase-lite:ROOT:javascript.adoc)      | [link](#3.1@couchbase-lite:ROOT:javascript.adoc)      | [link](#3.2@couchbase-lite:ROOT:javascript.adoc) | [link](#3.3@couchbase-lite:ROOT:javascript.adoc) |
| .NET       | [archive link](https://docs-archive.couchbase.com/home/index.html) | [archive link](https://docs-archive.couchbase.com/home/index.html) | [archive link](https://docs-archive.couchbase.com/home/index.html) | [archive link](https://docs-archive.couchbase.com/home/index.html) | [archive link](https://docs-archive.couchbase.com/home/index.html) | [link](#2.8@couchbase-lite:csharp:supported-os.adoc)  | [link](#3.0@couchbase-lite:csharp:supported-os.adoc)  | [link](#3.1@couchbase-lite:csharp:supported-os.adoc)  | [link](../../3.2/csharp/supported-os.md)         | [link](../csharp/supported-os.md)                |

## [](#related-content)Related Content

###### [](#)

Product Notes

* [Release Notes](releasenotes.md)
* [Compatibility](compatibility.md)
* [Supported Platforms](supported-os.md)
* [What’s New](#cbl-whatsnew.adoc)

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

---

[1](#%5Ffootnoteref%5F1). This Couchbase Lite version is End of Support 

[2](#%5Ffootnoteref%5F2). This Sync Gateway version is End of Support 

[3](#%5Ffootnoteref%5F3). This Sync Gateway version is End of Life