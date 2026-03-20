---
title: Supported Operating System Versions
description: Couchbase Lite on C#.Net -- the OS and SDK versions on which this
  framework is supported
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.2/modules/csharp/pages/supported-os.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:3.2@couchbase-lite:csharp:supported-os.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.2/csharp/supported-os.html)

# Supported Operating System Versions

> Description — _Couchbase Lite on C#.Net — the OS and SDK versions on which this framework is supported_  
> Related Content — [What’s New](#cbl-whatsnew.adoc) | [Release Notes](releasenotes.md) | [Compatibility](compatibility.md)

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
> * .NET Desktop - 6
> 
> Please plan to migrate your apps to use an appropriate alternative version.

__Table 1\. Supported versions__
| .NET Runtime      | Minimum Runtime Version | Minimum OS version                  |
| ----------------- | ----------------------- | ----------------------------------- |
| .NET Framework    | 4.6.2                   | Windows 10(any Microsoft supported) |
| .NET Desktop      | 6.0                     | Windows 10(any Microsoft supported) |
| .NET Mac Catalyst | 8.0                     | MacOS 12                            |
| WinUI             | 8.0                     | 10.0.19041.0                        |
| .NET iOS          | 8.0                     | 12+ (14+ for MAUI support)          |
| .NET Android      | 8.0                     | API 22+                             |
| Xamarin Android   | 10+                     | API 22                              |
| Xamarin iOS       | 10+                     | 10                                  |

## [](#not-officially-supported)Not Officially Supported

The following run-times are compatible but are not QE tested, and so are not officially supported.

| .NET Runtime | Minimum Runtime Version | Minimum OS version |
| ------------ | ----------------------- | ------------------ |
| .NET Mac     | 6.0                     | 12                 |
| .NET Linux   | 6.0                     | n/a\*              |

\* There are many different variants of Linux, and we don’t have the resources to test all of them. They are tested on Ubuntu 20.04, but have been shown to work on CentOS, and in theory work on any distro supported by .NET.