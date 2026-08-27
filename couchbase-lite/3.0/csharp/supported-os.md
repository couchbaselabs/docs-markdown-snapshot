---
title: Supported Operating System Versions
description: Couchbase Lite on C#.Net -- the OS and SDK versions on which this
  framework is supported
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.0/modules/csharp/pages/supported-os.adoc
  xref: xref:3.0@couchbase-lite:csharp:supported-os.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.0/csharp/supported-os.html)

# Supported Operating System Versions

> Description — _Couchbase Lite on C#.Net — the OS and SDK versions on which this framework is supported_  
> Related Content — [What's New](#cbl-whatsnew.adoc) | [Release Notes](releasenotes.md) | [Compatibility](compatibility.md)

## [](#officially-supported-versions)Officially Supported Versions

Couchbase Lite .NET is a .NET Core 3.1 library. The following table identifies the supported platforms.

Run-times which have received more testing and are **officially** supported are shown in [Table 1](#supported-os-versions):

__Table 1\. Supported versions__
| .NET Runtime    | Minimum Runtime Version | Minimum OS version                  |
| --------------- | ----------------------- | ----------------------------------- |
| .NET Core Win   | 3.1                     | Windows 10(any Microsoft supported) |
| .NET Framework  | 4.6.1                   | Windows 10(any Microsoft supported) |
| UWP             | 6.0.1                   | 10.0.16299                          |
| Xamarin iOS     | 10+                     | 10+                                 |
| Xamarin Android | 8                       | 5.1/API 22                          |

> [!NOTE]
> Support for API 19, API 20and API 21 is deprecated and will be removed in a future release; you should plan to migrate as soon as possible.

## [](#not-officially-supported)Not Officially Supported

The following run-times are compatible but are not QE tested, and so are not officially supported.

| .NET Runtime    | Minimum Runtime Version | Minimum OS version |
| --------------- | ----------------------- | ------------------ |
| .NET Core Mac   | 3.0                     | 10.12              |
| .NET Core Linux | 3.1                     | n/a\*              |

\* There are many different variants of Linux, and we don't have the resources to test all of them. They are tested on Ubuntu 16.04, but have been shown to work on CentOS, and in theory work on any distro supported by .NET Core.

Comparing this to the [supported versions](https://docs-archive.couchbase.com/couchbase-lite/1.4/csharp..html#supported-versions) in 1.x you can see we've traded some lower obsolete versions for new platform support.