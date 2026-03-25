---
title: Prerequisites&#8201;&#8212;&#8201;Couchbase Lite for C
description: Prerequisites for the installation of Couchbase Lite
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.0/modules/c/pages/gs-prereqs.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:3.0@couchbase-lite:c:gs-prereqs.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.0/c/gs-prereqs.html)

# Prerequisites&#8201;&#8212;&#8201;Couchbase Lite for C

> Description — _Prerequisites for the installation of Couchbase Lite_  

## [](#couchbase-lite-framework-size)Couchbase Lite Framework Size

Steps in Getting Started

[Install](gs-install.md)| [Build and Run](gs-build.md)

Couchbase Lite for C is provided as an `xcframework`.

The xcframework download size is between 100 and 140 MB. This include includes a "fat" binary that contains slices for both device (`armv7`, `arm64`) and simulator (`i386` and `x86_64`) CPU architectures. The fat binary allows you to link your app to the same xcframework and run your app on the simulator or a real device.

In addition, the bitcode that is included contributes to the majority of the download size. [Bitcode](https://help.apple.com/xcode/mac/current/#/devbbdc5ce4f) is an intermediate code representation that allows Apple to recompile the app after App submission and to deliver a thin version of the app specific to the device architecture.

Although you can disable bitcode within your app and strip away bitcode from the Couchbase Lite framework, it is not necessary to do so. In fact, it is probably best to leave it enabled to be future proof. This is because the bitcode is never downloaded by the user even though it is uploaded during App submission.

More information on App size is available on this [Apple Q&A](https://developer.apple.com/library/archive/qa/qa1795/%5Findex.html) page.

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Prerequisites](gs-prereqs.md)
* [Install](gs-install.md)
* [Build and Run](gs-build.md)

###### [](#-2)

Learn more . . .

* [Databases](database.md)
* [Documents](document.md)
* [Blobs](blob.md)
* [Remote Sync Gateway](replication.md)
* [Handling Data Conflicts](conflict.md)

###### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)