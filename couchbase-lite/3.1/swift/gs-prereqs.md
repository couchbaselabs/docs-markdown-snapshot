---
title: Prerequisites for Couchbase Lite on Swift
description: Prerequisites for the installation of Couchbase Lite
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.1/modules/swift/pages/gs-prereqs.adoc
  xref: xref:3.1@couchbase-lite:swift:gs-prereqs.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.1/swift/gs-prereqs.html)

# Prerequisites for Couchbase Lite on Swift

> Description — _Prerequisites for the installation of Couchbase Lite_  

## [](#couchbase-lite-framework-size)Couchbase Lite Framework Size

Couchbase Lite for Swift is provided as an `xcframework`.

The xcframework download size is between 100 and 140 MB. This include includes a "fat" binary that contains slices for both device (`armv7`, `arm64`) and simulator (`i386` and `x86_64`) CPU architectures. The fat binary allows you to link your app to the same xcframework and run your app on the simulator or a real device.

In addition, the bitcode that is included contributes to the majority of the download size. [Bitcode](https://help.apple.com/xcode/mac/current/#/devbbdc5ce4f) is an intermediate code representation that allows Apple to recompile the app after App submission and to deliver a thin version of the app specific to the device architecture.

Although you can disable bitcode within your app and strip away bitcode from the Couchbase Lite framework, it is not necessary to do so. In fact, it is probably best to leave it enabled to be future proof. This is because the bitcode is never downloaded by the user even though it is uploaded during App submission.

More information on App size is available on this [Apple Q&A](https://developer.apple.com/library/archive/qa/qa1795/%5Findex.html) page.

See also: [Supported Versions](supported-os.md)

> [!CAUTION]
> Deprecation Notice — Apple Mac OS
> 
> Support for Mac OS 10.12 was deprecated in release 3.0 and will be removed in a future release
> 
> _Action:_ Please plan to migrate your apps to use an appropriate alternative version.

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