---
title: Supported Operating System Versions
description: Couchbase Lite on C#.Net -- the OS and SDK versions on which this
  framework is supported
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.1/modules/csharp/pages/supported-os.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.1@couchbase-lite:csharp:supported-os.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.1/csharp/supported-os.html)

# Supported Operating System Versions

> Description — _Couchbase Lite on C#.Net — the OS and SDK versions on which this framework is supported_  
> Related Content — [What's New](#cbl-whatsnew.adoc) | [Release Notes](releasenotes.md) | [Compatibility](compatibility.md)

## [](#officially-supported-versions)Officially Supported Versions

The following table identifies the supported platforms.

Run-times which have received more testing and are **officially** supported are shown in [Table 1](#supported-os-versions):

> [!IMPORTANT]
> Deprecation Notice
> 
> Support for the following will be deprecated in this release and will be removed in a future release:
> 
> * Xamarin Android - All Versions
> * Xamarin iOS - All Versions
> * .Net6 - iOS, Android, Mac Catalyst, WinUI
> 
> Please plan to migrate your apps to use an appropriate alternative version.

__Table 1\. Supported versions__
| .NET Runtime      | Minimum Runtime Version | Minimum OS version                  |
| ----------------- | ----------------------- | ----------------------------------- |
| .NET Win          | 6.0                     | Windows 10(any Microsoft supported) |
| .NET Framework    | 4.6.2                   | Windows 10(any Microsoft supported) |
| .NET Mac Catalyst | 6.0                     | Mac OS 10.15                        |
| WinUI             | 6.0.1                   | 10.0.19041.0                        |
| Xamarin iOS       | 10+                     | 10+                                 |
| Xamarin Android   | 10                      | 5.1/API 22                          |
| .NET iOS          | 6.0                     | 14.2                                |
| .NET Android      | 6.0                     | 5.1/API 22                          |

## [](#not-officially-supported)Not Officially Supported

The following run-times are compatible but are not QE tested, and so are not officially supported.

| .NET Runtime | Minimum Runtime Version | Minimum OS version |
| ------------ | ----------------------- | ------------------ |
| .NET Mac     | 6.0                     | 10.15              |
| .NET Linux   | 6.0                     | n/a\*              |

\* There are many different variants of Linux, and we don't have the resources to test all of them. They are tested on Ubuntu 20.04, but have been shown to work on CentOS, and in theory work on any distro supported by .NET.