---
title: Supported Versions
description: Supported Versions Couchbase Lite for {param-platform}
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/csharp/pages/gs-supported-os.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.8@couchbase-lite:csharp:gs-supported-os.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/csharp/gs-supported-os.html)

# Supported Versions

> Description — _Supported Versions Couchbase Lite for {param-platform}_  
> _Abstract — Couchbase Lite .NET is a .NET Standard 2.0 library and this content identifies the supported platforms._  

Couchbase Lite .NET is a .NET Standard 2.0 library. The following tables list out the supported platforms.

## [](#officially-supported)Officially Supported

Runtimes which have received more testing and are **officially** supported are:

| .NET Runtime   | Minimum Runtime Version | Minimum OS version                 |
| -------------- | ----------------------- | ---------------------------------- |
| .NET Core Win  | 2.0                     | 10 (any Microsoft supported)       |
| .NET Framework | 4.6.1                   | 10 (any Microsoft supported)       |
| UWP            | 6.0.1                   | 10.0.16299                         |
| Xamarin iOS    | 10.14                   | 10.3.1                             |
| Xamarin csharp | API 26                  | API 22 API 19,20,21 \[DEPRECATED\] |

> [!NOTE]
> Deprecation
> 
> Support for API 19 and API 21 is deprecated in version 2.6\.

## [](#not-officially-supported)Not Officially Supported

The following runtimes are also compatible but are not QE tested. So they are not officially supported.

| .NET Runtime    | Minimum Runtime Version | Minimum OS version |
| --------------- | ----------------------- | ------------------ |
| .NET Core Mac   | 2.0                     | 10.12              |
| .NET Core Linux | 2.0                     | n/a\*              |

\* There are many different variants of Linux, and we don’t have the resources to test all of them. They are tested on Ubuntu 16.04, but have been shown to work on CentOS, and in theory work on any distro supported by .NET Core.

Comparing this to the [supported versions](https://docs-archive.couchbase.com/couchbase-lite/1.4/csharp..html#supported-versions) in 1.x you can see we’ve traded some lower obsolete versions for new platform support.

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