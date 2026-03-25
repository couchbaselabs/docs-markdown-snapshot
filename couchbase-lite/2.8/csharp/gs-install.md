---
title: Installing Couchbase Lite on .Net
description: How to install Couchbase Lite on .Net
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/csharp/pages/gs-install.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.8@couchbase-lite:csharp:gs-install.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/csharp/gs-install.html)

# Installing Couchbase Lite on .Net

> Description — _How to install Couchbase Lite on .Net_  
> _Abstract — Using Nuget to install Couchbase Lite on csharp_  

## [](#visual-studio-project)Visual Studio Project

Create or open an existing Visual Studio project and install Couchbase Lite using the following method.

## [](#nuget)Nuget

1. Install either of the following packages from Nuget.  
Couchbase Lite Community Edition  
Install the `Couchbase.Lite` package.  
Couchbase Lite Enterprise Edition  
Install the `Couchbase.Lite.Enterprise` package.  
> [!NOTE]  
> Nuget packages can be installed via `PackageReference` or `packages.config`. It is recommended to use the `PackageReference` style of dependency management because there is a strict version requirement between Couchbase Lite and its dependent Support library (`Couchbase.Lite.Support.<Platform>` and `Couchbase.Lite.Enterprise.Support.<Platform>` for Community and Enterprise respectively). If you are using `packages.config`, you must take extra care when upgrading the package to make sure that the support library is also updated to the exact same version. Versions that are not the same are incompatible with each other.  
[Comparative Table](https://www.couchbase.com/products/editions)
2. Your app must call the relevant `Activate()` function inside of the class that is included in the support assembly. There is only one public class in each support assembly, and the support assembly itself is a nuget dependency.  
For example, UWP looks like `Couchbase.Lite.Support.UWP.Activate()`. Currently the support assemblies provide dependency injected mechanisms for default directory logic, and platform specific logging (i.e., csharp will log to logcat with correct log levels and tags. No more "mono-stdout" always at info level.)

## [](#related-content)Related Content

###### [](#)

How to

* [Passive Peer](../../current/csharp/p2psync-websocket-using-passive.md)
* [Active Peer](../../current/csharp/p2psync-websocket-using-active.md)

###### [](#-2)

Concepts

* [Landing P2Psync](#couchbase-lite:csharp:landing-p2psync.adoc)
* [API References](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-net).

###### [](#-3)

Community Resources …​

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)

* [Getting Started with Peer-to-Peer Synchronization](../../../tutorials/cbl-p2p-sync-websockets/swift/cbl-p2p-sync-websockets.md)