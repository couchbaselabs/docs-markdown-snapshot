---
title: Supported Operating System Versions
description: Couchbase Lite on C#.Net -- the OS and SDK versions on which this
  framework is supported
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.0/modules/csharp/pages/supported-os.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:couchbase-lite:csharp:supported-os.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/current/csharp/supported-os.html)

# Supported Operating System Versions

> Description — _Couchbase Lite on C#.Net — the OS and SDK versions on which this framework is supported_  
> Related Content — [What’s New](#cbl-whatsnew.adoc) | [Release Notes](releasenotes.md) | [Compatibility](compatibility.md)

## [](#officially-supported-versions)Officially Supported Versions

The following table identifies the supported platforms.

Run-times which have received more testing and are **officially** supported are shown in [Table 1](#supported-os-versions):

> [!IMPORTANT]
> Deprecation Notice
> 
> Couchbase Lite 4.0 deprecates Windows 10 support and will remove it in a future release. Plan to migrate your apps to use an appropriate alternative version.

> [!NOTE]
> Newer .NET Runtime Versions
> 
> The **Minimum Runtime Version** column specifies the minimum required version for each .NET runtime. Later versions, including .NET 10 and higher, also work because .NET provides backward compatibility. Couchbase Lite is built to be compatible with newer .NET runtime versions as they’re released. If you encounter any issues with a newer .NET version, submit a support ticket.

__Table 1\. Supported versions__
| .NET Runtime      | Minimum Runtime Version (and newer) | Minimum OS version                  |
| ----------------- | ----------------------------------- | ----------------------------------- |
| .NET Framework    | 4.6.2                               | Windows 10(any Microsoft supported) |
| .NET Desktop      | 8.0                                 | Windows 10(any Microsoft supported) |
| .NET Mac Catalyst | 9.0                                 | MacOS 13                            |
| WinUI             | 9.0                                 | 10.0.19041.0                        |
| .NET iOS          | 9.0                                 | 15                                  |
| .NET Android      | 9.0                                 | API 24                              |

## [](#not-officially-supported)Not Officially Supported

The following run-times are compatible but are not QE tested, and so are not officially supported.

| .NET Runtime | Minimum Runtime Version | Minimum OS version |
| ------------ | ----------------------- | ------------------ |
| .NET Mac     | 8.0                     | 13                 |
| .NET Linux   | 8.0                     | n/a                |