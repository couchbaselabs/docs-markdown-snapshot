---
title: Supported Operating System Versions
description: Couchbase Lite on C#.Net -- the OS and SDK versions on which this
  framework is supported
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.1/modules/csharp/pages/supported-os.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:couchbase-lite:csharp:supported-os.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/current/csharp/supported-os.html)

# Supported Operating System Versions

> Description — _Couchbase Lite on C#.Net — the OS and SDK versions on which this framework is supported_  
> Related Content — [What's New](#cbl-whatsnew.adoc) | [Release Notes](releasenotes.md) | [Compatibility](compatibility.md)

## [](#officially-supported-versions)Officially Supported Versions

The following table identifies the supported platforms.

Run-times which have received more testing and are **officially** supported are shown in [Table 1](#supported-os-versions).

> [!NOTE]
> Newer .NET Runtime Versions
> 
> Later versions, including .NET 11 and higher, also work because .NET provides backward compatibility. Couchbase Lite is built to be compatible with newer .NET runtime versions as they're released. If you encounter any issues with a newer .NET version, submit a support ticket.

__Table 1\. Supported versions__
| .NET Runtime      | Minimum Runtime Version | Minimum OS version                  |
| ----------------- | ----------------------- | ----------------------------------- |
| .NET Framework    | 4.6.2                   | Windows 11(any Microsoft supported) |
| .NET Desktop      | 8.0                     | Windows 11(any Microsoft supported) |
| .NET Mac Catalyst | 10.0                    | MacOS 14                            |
| WinUI             | 10.0                    | 10.0.19041.0                        |
| .NET iOS          | 10.0                    | 15                                  |
| .NET Android      | 10.0                    | API 24                              |

## [](#not-officially-supported)Not Officially Supported

The following run-times are compatible but are not QE tested, and so are not officially supported.

| .NET Runtime | Minimum Runtime Version | Minimum OS version |
| ------------ | ----------------------- | ------------------ |
| .NET Mac     | 8.0                     | 14                 |
| .NET Linux   | 8.0                     | n/a                |

## [](#removed-versions)Removed Versions

| .NET Runtime | Version Removed | Deprecation Release |
| ------------ | --------------- | ------------------- |
| Windows 10   | 3.4 / 4.1       | 4.0                 |

## [](#removed-versions)Removed Versions

| .NET Runtime | Version Removed | Deprecation Release |
| ------------ | --------------- | ------------------- |
| Windows 10   | 4.1             | 4.0                 |