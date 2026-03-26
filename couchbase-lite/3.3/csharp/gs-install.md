---
title: Installing Couchbase Lite on .Net
description: How to install Couchbase Lite on .Net
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.3/modules/csharp/pages/gs-install.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.3@couchbase-lite:csharp:gs-install.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.3/csharp/gs-install.html)

# Installing Couchbase Lite on .Net

> Description — _How to install Couchbase Lite on .Net_  
> _Abstract — Using Nuget to install Couchbase Lite on csharp_  

Quick Steps

For experienced developers, this is all you need to add _Couchbase Lite for C#.Net 3.2.4_ to your application projects.

1. Create or open an existing Visual Studio project
2. Install either of the following packages from Nuget.

  * Community Edition — `Couchbase.Lite` package for 3.2.4
  * Enterprise Edition — `Couchbase.Lite.Enterprise` package for 3.2.4

    * Vector Search Extension — `Couchbase.Lite.VectorSearch` package for 1.0.1
3. Within your app, include a call to the relevant `Activate()` function inside of the class that is included in the support assembly.

> [!IMPORTANT]
> To use Vector Search, you must have Couchbase Lite installed and add the Vector Search extension to your Couchbase Lite application. Vector Search is available only for 64-bit architectures and Intel processors that support the Advanced Vector Extensions 2 (AVX2) instruction set. To verify whether your device supports the AVX2 instructions set, [follow these instructions.](https://www.intel.com/content/www/us/en/support/articles/000090473/processors/intel-core-processors.html)

That's it!  
You should be ready to build you app using this version. The rest of this content contains more detail, for those who want to know more about the install or who encountered issues

## [](#install-methods)Install Methods

Couchbase recommends installing Nuget packages via _PackageReference_.

### [](#package-reference)Package Reference

This is the recommended method of dependency management because it supports the strict version requirement between the core _Couchbase Lite for .Net_ package and its dependent Support library, which comprises:

`Couchbase.Lite.Enterprise`

* `Couchbase.Lite.Enterprise.Support.ios`
* `Couchbase.Lite.Enterprise.Support.Android`
* `Couchbase.Lite.Enterprise.Support.NetDesktop`
* `Couchbase.Lite.Enterprise.Support.WinUI`

`Couchbase.Lite`

* `Couchbase.Lite.Support.ios`
* `Couchbase.Lite.Support.Android`
* `Couchbase.Lite.Support.NetDesktop`
* `Couchbase.Lite.Support.WinUI`

### [](#installing-vector-search)Installing Vector Search

Couchbase recommends installing Nuget packages via _PackageReference_.

> [!IMPORTANT]
> To use Vector Search, you must have Couchbase Lite installed and add the Vector Search extension to your Couchbase Lite application. Vector Search is available only for 64-bit architectures and Intel processors that support the Advanced Vector Extensions 2 (AVX2) instruction set. To verify whether your device supports the AVX2 instructions set, [follow these instructions.](https://www.intel.com/content/www/us/en/support/articles/000090473/processors/intel-core-processors.html)

#### [](#vector-search-package-reference)Vector Search Package Reference

This is the recommended method of dependency management for the Vector Search extension because it supports the strict version requirement between the core _Couchbase Lite for .Net_ package and its dependent Support library. You can manage your dependencies by following the steps below:

1. Add the `Couchbase.Lite.Enterprise` packages.
2. Add the `Couchbase.Lite.VectorSearch` package.

## [](#activating-on-android-platform-only)Activating (on Android platform only)

> [!IMPORTANT]
> Couchbase Lite must be activated before any other calls can be made.

Within your Android app, include a call to the relevant `Activate()` function inside of the class that is included in the support assembly.

There is only one public class in each support assembly, and the support assembly itself is a nuget dependency.

For example:  
`Couchbase.Lite.Support.Droid.Activate()`

> [!NOTE]
> The `Activate()` function is required for applications using .NET on the Android platform in general. This includes Couchbase Lite and the Vector Search extension.

Currently the support assemblies provide dependency injected mechanisms for default directory logic, and platform specific logging (So, C# will log to logcat with correct log levels and tags. No more "mono-stdout" always at info level.)

### [](#activating-with-maui)Activating with MAUI

To activate with .NET MAUI, you must override the `OnCreate()` method in the `MainActivity.cs` file to ensure activation at the beginning of the application lifecyle.

Below is an example of how you can override the `OnCreate()` method.

```csharp
public class MainActivity : MauiAppCompatActivity
{
    protected override void OnCreate(Bundle savedInstanceState)
    {
        base.OnCreate(savedInstanceState);
        Couchbase.Lite.Support.Droid.Activate(this);
    }
}
```

### [](#activating-vector-search)Activating Vector Search

If you have the `Couchbase.Lite.VectorSearch` package installed, you can activate it by calling the following:

1. For the Android platform  
`Extension.Enable(new VectorSearchExtension(androidContext));`
2. For other platforms  
```csharp  
            Extension.Enable(new VectorSearchExtension());  
```

## [](#related-content)Related Content

###### [](#)

How to

* [Passive Peer](p2psync-websocket-using-passive.md)
* [Active Peer](p2psync-websocket-using-active.md)

.

###### [](#-2)

Concepts

* [Peer-to-Peer Sync](#csharp:landing-p2psync.adoc)
* [API References](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-net)

.

###### [](#-3)

Community Resources …​

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

. [Getting Started with Peer-to-Peer Synchronization](../../../tutorials/cbl-p2p-sync-websockets/swift/cbl-p2p-sync-websockets.md)