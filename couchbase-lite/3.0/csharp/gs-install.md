---
title: Installing Couchbase Lite on .Net
description: How to install Couchbase Lite on .Net
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.0/modules/csharp/pages/gs-install.adoc
  xref: xref:3.0@couchbase-lite:csharp:gs-install.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.0/csharp/gs-install.html)

# Installing Couchbase Lite on .Net

> Description — _How to install Couchbase Lite on .Net_  
> _Abstract — Using Nuget to install Couchbase Lite on csharp_  

Quick Steps

For experienced developers, this is all you need to add _Couchbase Lite for C#.Net 3.0.15_ to your application projects.

1. Create or open an existing Visual Studio project
2. Install either of the following packages from Nuget.

  * Community Edition — `Couchbase.Lite` package for 3.0.15
  * Enterprise Edition — `Couchbase.Lite.Enterprise` package for 3.0.15
3. Within your Android app, include a call to the relevant `Activate()` function inside of the class that is included in the support assembly, passing in a `context` argument (typically the `ApplicationContext` property on your app class).

That's it!  
You should be ready to build you app using this version. The rest of this content contains more detail, for those who want tp know more about the install or who encountered issues

## [](#install-methods)Install Methods

Nuget packages can be installed via _PackageReference_ or _packages.config_.

### [](#package-reference)Package Reference

This is the recommended method of dependency management because it supports the strict version requirement between the core _Couchbase Lite for .Net_ package and its dependent Support library, which comprises:

`Couchbase.Lite.Enterprise`

* `Couchbase.Lite.Enterprise.Support.UWP`
* `Couchbase.Lite.Enterprise.Support.ios`
* `Couchbase.Lite.Enterprise.Support.android`
* `Couchbase.Lite.Enterprise.Support.NetDesktop`

`Couchbase.Lite`

* `Couchbase.Lite.Support.UWP`
* `Couchbase.Lite.Support.ios`
* `Couchbase.Lite.Support.android`
* `Couchbase.Lite.Support.NetDesktop`

### [](#package-config)Package Config

If you are using `packages.config`, you must take extra care when upgrading the package to make sure that the support libraries you require are also updated to the exact same version.

> [!NOTE]
> Versions that are not the same are incompatible with each other — see: [Comparative Table](https://www.couchbase.com/products/editions)

## [](#activating-on-android-platform-only)Activating (on Android platform only)

Couchbase Lite must be activated before any other calls can be made.  
Within your Android app, include a call to the relevant `Activate()` function inside of the class that is included in the support assembly.

There is only one public class in each support assembly, and the support assembly itself is a nuget dependency.

On Android, this method takes a `context` argument — typically the `ApplicationContext` property on your app class.

For example:  
`Couchbase.Lite.Support.Android.Activate(this.ApplicationContext)`

The `Activate()` function is required for applications using .NET on the Android platform only. It is not required, and the function does not exist, for iOS or UWP.

Currently the support assemblies provide dependency injected mechanisms for default directory logic, and platform specific logging (So, C# will log to logcat with correct log levels and tags. No more "mono-stdout" always at info level.)

## [](#related-content)Related Content

###### [](#)

How to

* [Passive Peer](p2psync-websocket-using-passive.md)
* [Active Peer](p2psync-websocket-using-active.md)

###### [](#-2)

Concepts

* [Peer-to-Peer Sync](#csharp:landing-p2psync.adoc)
* [API References](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-net)

###### [](#-3)

Community Resources …​

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

[Getting Started with Peer-to-Peer Synchronization](../../../tutorials/cbl-p2p-sync-websockets/swift/cbl-p2p-sync-websockets.md)