---
title: Supported Operating System Versions
description: Couchbase Lite on C#.Net -- the OS and SDK versions on which this
  framework is supported
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/csharp/pages/supported-os.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.8@couchbase-lite:csharp:supported-os.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/csharp/supported-os.html)

# Supported Operating System Versions

> Description — _Couchbase Lite on C#.Net — the OS and SDK versions on which this framework is supported_  
> Related Content — [What’s New](../../current/cbl-whatsnew.md) | [Release Notes](#couchbase-lite:csharp:{cbl-pg-releasenotes}) | [Compatibility](../../current/csharp/compatibility.md)

## [](#officially-supported-versions)Officially Supported Versions

Couchbase Lite .NET is a .NET Standard 2.0 library. The following table identifies the supported platforms.

Runtimes which have received more testing and are **officially** supported are:

| .NET Runtime    | Minimum Runtime Version | Minimum OS version           |
| --------------- | ----------------------- | ---------------------------- |
| .NET Core Win   | 2.0                     | 10 (any Microsoft supported) |
| .NET Framework  | 4.6.1                   | 10 (any Microsoft supported) |
| UWP             | 6.0.1                   | 10.0.16299                   |
| Xamarin iOS     | 10.14                   | 10.3.1                       |
| Xamarin Android | 8                       | 5.1/API 22                   |

> [!NOTE]
> Support for API 19, API 20 and API 21 is deprecated in this release. Support will be removed within two (non-maintenance) releases following the deprecation announcement.

## [](#not-officially-supported)Not Officially Supported

The following run times are also compatible but are not QE tested. So they are not officially supported.

| .NET Runtime    | Minimum Runtime Version | Minimum OS version |
| --------------- | ----------------------- | ------------------ |
| .NET Core Mac   | 2.0                     | 10.12              |
| .NET Core Linux | 2.0                     | n/a\*              |

\* There are many different variants of Linux, and we don’t have the resources to test all of them. They are tested on Ubuntu 16.04, but have been shown to work on CentOS, and in theory work on any distro supported by .NET Core.

Comparing this to the [supported versions](https://docs-archive.couchbase.com/couchbase-lite/1.4/csharp..html#supported-versions) in 1.x you can see we’ve traded some lower obsolete versions for new platform support.

## [](#related-content)Related Content

###### [](#)

Product Notes

* [Release Notes](#couchbase-lite:csharp:{cbl-pg-releasenotes})
* [Compatibility](../../current/csharp/compatibility.md)
* [Supported OS](../../current/csharp/supported-os.md)
* [What’s New](../../current/cbl-whatsnew.md)

###### [](#-2)

Starting Points

* [Databases](../../current/csharp/database.md)
* [Documents](../../current/csharp/document.md)
* [Blobs](../../current/csharp/blob.md)
* [Remote Sync using Sync Gateway](../../current/csharp/replication.md)
* [Handling Data Conflicts](../../current/csharp/conflict.md)

###### [](#-3)

Tutorials

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)