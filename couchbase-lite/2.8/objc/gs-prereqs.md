---
title: Prerequisites&#8201;&#8212;&#8201;Couchbase Lite for Objective-C
description: Prerequisites for the installation of Couchbase Lite
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/objc/pages/gs-prereqs.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.8@couchbase-lite:objc:gs-prereqs.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/objc/gs-prereqs.html)

# Prerequisites&#8201;&#8212;&#8201;Couchbase Lite for Objective-C

> Description — _Prerequisites for the installation of Couchbase Lite_  

## [](#couchbase-lite-framework-size)Couchbase Lite Framework Size

Although the size of the Couchbase Lite framework that is downloaded is around 50MB, note that the framework would add only around 3.5MB to the size of the app when it is installed from the App Store. This is because when the user installs your app from the App Store, only the bits that are relevant to the device architecture are delivered.

### [](#why-is-the-original-size-so-large)Why is the original size so large?

The Couchbase Lite framework includes a "fat" binary that contains slices for both device (`armv7`, `arm64`) and simulator (`i386` and `x86_64`) CPU architectures. The fat binary allows you to link your app to the same framework and run your app on the simulator or a real device. In addition, the bitcode that is included with the framework contributes to the majority of the download size. [Bitcode](https://help.apple.com/xcode/mac/current/#/devbbdc5ce4f) is an intermediate code representation that allows Apple to recompile the app after App submission and to deliver a thin version of the app specific to the device architecture.

### [](#architecture-stripping)Architecture Stripping

When submitting a build of your application to the App Store you must ensure that it doesn't contain any simulator architecture otherwise the upload will fail with the error message "Unsupported Architecture. Your executable contains unsupported architecture '\[x86\_64, i386\]'."

The steps to remove the simulator architecture (x86\_64) from **CouchbaseLite.framework** are outlined below in [Remove simulator architecture](#ex-rmvsimarc). They depend on the method you chose to install Couchbase Lite:

Remove simulator architecture

* Frameworks
* Carthage

The Couchbase Lite framework available on the [Couchbase Downloads page](https://www.couchbase.com/downloads/?family=mobile) contains a build for both the simulator (x86\_64) and iOS devices (ARM). The following steps describe how to set up a build phase in Xcode to do this automatically.

1. In Xcode, open the **Build Phases** tab, then select the **+** \> **Add Run Script Build Phase** option.  
![run script phase](_images/run-script-phase.png)
2. Copy the contents of [strip\_framework.sh](https://raw.githubusercontent.com/couchbase/couchbase-lite-ios/master/Scripts/strip%5Fframeworks.sh) in the **Run Script** editor window.  
![run script copy](_images/run-script-copy.png)

That's it, now every time you build and run your application, Xcode will remove binary architectures that do not match the target's architecture type (emulator or device).

The [following link](https://github.com/Carthage/Carthage/blob/5fd867c4895b4f59d70181dec169a1644f4430e3/README.md#adding-frameworks-to-an-application) describes how to set up a build phase in Xcode and run a Carthage script in order to remove the simulator architecture (x86\_64).

### [](#lbl-tgtinterr)Target Integrity Error

You may encounter a `Target Integrity Error` when building for iOS Simulator(or iOS). This is because the embedded framework `CouchbaseLiteSwift.framework` was built for iOS + iOS Simulator.

> [!TIP]
> Using XCFrameworks will ensure that the binaries used have the right architectures for the different platforms you target.

As a workaround, you are recommended to strip the unnecessary architecture from the fat binary as described in [Example 1](#ex-wkaround)

Example 1\. Thinning the Framework

Within the folder containing the framework, use the `lipo` command to convert the universal binary to a single architecture file.

* Simulator
* Device

```bash
lipo CouchbaseLiteSwift.framework/CouchbaseLiteSwift -thin x86_64 -output  CouchbaseLiteSwift.framework/CouchbaseLiteSwift
```

```bash
lipo CouchbaseLiteSwift.framework/CouchbaseLiteSwift -thin arm64 -output  CouchbaseLiteSwift.framework/CouchbaseLiteSwift
```

### [](#should-you-disable-bitcode)Should you disable bitcode?

Although you can disable bitcode within your app and strip away bitcode from the Couchbase Lite framework, it is not necessary to do so. In fact, it is probably best to leave it enabled to be future proof. This is because the bitcode is never downloaded by the user even though it is uploaded during App submission.

### [](#other-resource-to-reduce-the-size-of-your-app)Other resource to reduce the size of your app

More information is available on this [Apple Q&A](https://developer.apple.com/library/archive/qa/qa1795/%5Findex.html) page.

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Prerequisites](../../current/objc/gs-prereqs.md)
* [Install](../../current/objc/gs-install.md)
* [Build and Run](../../current/objc/gs-build.md)

###### [](#-2)

Learn more . . .

* [Databases](../../current/objc/database.md)
* [Documents](../../current/objc/document.md)
* [Blobs](../../current/objc/blob.md)
* [Remote Sync using Sync Gateway](../../current/objc/replication.md)
* [Handling Data Conflicts](../../current/objc/conflict.md)

###### [](#-3)

Dive Deeper . . .

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)