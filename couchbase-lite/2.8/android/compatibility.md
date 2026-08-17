---
title: Compatibility
description: Couchbase Lite framework and Sync Gateway compatibility
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/android/pages/compatibility.adoc
  xref: xref:2.8@couchbase-lite:android:compatibility.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/android/compatibility.html)

# Compatibility

> Description — _Couchbase Lite framework and Sync Gateway compatibility_  
> _Abstract — This content identifies the compatibility of Couchbase Lite on Android with Sync Gateway, together with the operating systems upon which it is supported._  
> Related Content — [What's New](../../current/cbl-whatsnew.md) | [Release Notes](#couchbase-lite:android:{cbl-pg-releasenotes}) | [Supported OS](../../current/android/supported-os.md)

## [](#couchbase-litesync-gateway-matrix)Couchbase Lite/Sync Gateway Matrix

The table below summarizes the compatible versions of Couchbase Lite with Sync Gateway.

__Table 1\. Sync Gateway and Couchbase Lite Compatibility Matrix__
| Sync Gateway Versions ↓                                                                                         | Couchbase Lite →                                 |     |     |           |   |
| --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ | --- | --- | --------- | - |
| 1.3\[[1](#%5Ffootnotedef%5F1 "View footnote.")\]\]                                                              | 1.4\[[1](#%5Ffootnotedef%5F1 "View footnote.")\] | 2.0 | 2.1 | 2.5 - 2.8 |   |
| Release 1.3\[[2](#%5Ffootnotedef%5F2 "View footnote.")\]                                                        | ✔                                                | ✖   | ✖   | ✖         | ✖ |
| Releases 1.4 \[[2](#%5Ffootnotedef%5F2 "View footnote.")\] and 1.5\[[3](#%5Ffootnotedef%5F3 "View footnote.")\] | ✔                                                | ✔   | ✖   | ✖         | ✖ |
| Releases 2.0 and 2.1                                                                                            | ✔                                                | ✔   | ✔   | ✔         | ✔ |
| Releases 2.5 to 2.8 with delta sync disabled                                                                    | ✔                                                | ✔   | ✔   | ✔         | ✔ |
| Releases 2.5 to 2.8 with delta sync enabled                                                                     | ✖                                                | ✖   | ✖   | ✖         | ✔ |

## [](#operating-system-sdk-support)Operating System SDK Support

The table below summarizes the Operating System SDK versions supported by Couchbase Lite.

__Table 2\. OS — SDK Support__
| OperatingSystem ↓ | Couchbase Lite versions →                                   |                                                             |                                                             |                                                             |                                                                    |                                   |
| ----------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------------ | --------------------------------- |
|                   | 2.0                                                         | 2.1                                                         | 2.5                                                         | 2.6                                                         | 2.7                                                                | 2.8                               |
| iOS               | [link](#2.0@couchbase-lite::swift.adoc#supported-versions)  | [link](#2.1@couchbase-lite::swift.adoc#supported-versions)  | [link](#2.5@couchbase-lite::swift.adoc#supported-versions)  | [link](#2.6@couchbase-lite::swift.adoc#supported-versions)  | [link](#2.7@couchbase-lite::swift.adoc#supported-versions)         | [link](../swift/supported-os.md)  |
| Java              | \-                                                          | \-                                                          | \-                                                          | \-                                                          | [link](#2.7@couchbase-lite::java-platform.adoc#supported-versions) | [link](../java/supported-os.md)   |
| Java (Android)    | [link](#2.0@couchbase-lite::java.adoc#supported-versions)   | [link](#2.1@couchbase-lite::java.adoc#supported-versions)   | [link](#2.5@couchbase-lite::java.adoc#supported-versions)   | [link](#2.6@couchbase-lite::java.adoc#supported-versions)   | [link](#2.7@couchbase-lite::java-android.adoc#supported-versions)  | [link](supported-os.md)           |
| Javascript        | \-                                                          | \-                                                          | \-                                                          | [link](#2.6@couchbase-lite::javascript.adoc)                | [link](#2.7@couchbase-lite::javascript.adoc)                       | [link](../javascript.md)          |
| .NET              | [link](#2.0@couchbase-lite::csharp.adoc#supported-versions) | [link](#2.1@couchbase-lite::csharp.adoc#supported-versions) | [link](#2.5@couchbase-lite::csharp.adoc#supported-versions) | [link](#2.6@couchbase-lite::csharp.adoc#supported-versions) | [link](#2.7@couchbase-lite::csharp.adoc#supported-versions)        | [link](../csharp/supported-os.md) |

Couchbase SDKs indicate the stability of an API through documentation. Since there are different meanings when developers mention stability, we mean **interface stability**: how likely the interface is to change or be removed entirely. A stable interface is one that is guaranteed not to change between versions, meaning that you may use an API of a given SDK version and be assured that the given API will retain the same parameters and behavior in subsequent versions. An unstable interface is one which may appear to work or behave in a specific way within a given SDK version, but may change in its behavior or arguments in future SDK versions, causing odd application behavior or compiler/API usage errors. **Implementation stability** is implied to be more reliable at higher levels, but all are tested to the level that is appropriate for their stability.

Couchbase uses three interface stability classifiers. You may find these classifiers appended as annotations or comments within documentation for each API:

* **Committed**: This stability level is used to indicate the most stable interfaces that are guaranteed to be supported and remain stable between SDK versions. This is the default — unless otherwise stated in the documentation, each API has **Committed** status.
* **Uncommitted**: This level is used to indicate APIs that are _unlikely_ to change, but _may_ still change as final consensus on their behavior has not yet been reached. _Uncommitted_ APIs usually end up becoming stable APIs.
* **Volatile**: This level is used to indicate experimental APIs that are still in flux and may likely be changed. It may also be used to indicate inherently private APIs that may be exposed, but "YMMV" (your mileage may vary) principles apply. _Volatile_ APIs typically end up being promoted to _Uncommitted_ after undergoing some modifications.

APIs that are marked as _Committed_ have a stable implementation. _Uncommitted_ and _Volatile_ APIs should be stable within the bounds of any known and often documented issues, but Couchbase has not made a commitment to these APIs and may not respond to reported defects with the same priority.

Additionally, take note of the following interface labels:

* **Deprecated**: Any API marked deprecated may be removed in the next major version released. Couchbase recommends migrating from the deprecated API to the replacement as soon as possible. In rare instances, deprecated API may be rendered non-functional in a dot-minor release when the API cannot continue to be supported.
* **Internal**: This level is used to indicate you should not rely on this API as it is not intended for use outside the module, even to other Couchbase components.

## [](#related-content)Related Content

###### [](#)

Product Notes

* [Release Notes](#couchbase-lite:android:{cbl-pg-releasenotes})
* [Compatibility](../../current/android/compatibility.md)
* [Supported OS](../../current/android/supported-os.md)
* [What's New](../../current/cbl-whatsnew.md)

###### [](#-2)

Starting Points

* [Databases](../../current/android/database.md)
* [Documents](../../current/android/document.md)
* [Blobs](../../current/android/blob.md)
* [Remote Sync using Sync Gateway](../../current/android/replication.md)
* [Handling Data Conflicts](../../current/android/conflict.md)

###### [](#-3)

Tutorials

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)

---

[1](#%5Ffootnoteref%5F1). This Couchbase Lite version is End of Support 

[2](#%5Ffootnoteref%5F2). This Sync Gateway version is End of Support 

[3](#%5Ffootnoteref%5F3). This Sync Gateway version is End of Life