---
title: Supported Operating System Versions
description: Couchbase Lite on Java -- the OS and SDK versions on which this
  framework is supported
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.0/modules/java/pages/supported-os.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.0@couchbase-lite:java:supported-os.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.0/java/supported-os.html)

# Supported Operating System Versions

> Description — _Couchbase Lite on Java — the OS and SDK versions on which this framework is supported_  
> Related Content — [What's New](#cbl-whatsnew.adoc) | [Release Notes](releasenotes.md) | [Compatibility](compatibility.md)

## [](#officially-supported-versions)Officially Supported Versions

Couchbase Lite on Java is supported on x86 64-bit platforms. The targeted OS versions are given in [Table 1](#supported-os-versions)

__Table 1\. Supported versions__
| OS                           | Version                                | Type                                   |
| ---------------------------- | -------------------------------------- | -------------------------------------- |
| RHEL                         | 8                                      | Desktop & Web Service/Servlet (Tomcat) |
| 7                            | Desktop & Web Service/Servlet (Tomcat) |                                        |
| centOS                       | 8                                      | Desktop & Web Service/Servlet (Tomcat) |
| 7                            | Desktop & Web Service/Servlet (Tomcat) |                                        |
| Ubuntu                       | 20.04 LTS                              | Desktop & Web Service/Servlet (Tomcat) |
| 18.04 LTS                    | Desktop & Web Service/Servlet (Tomcat) |                                        |
| 16.04 LTS                    | Deprecated                             |                                        |
| Debian                       | GNU/Linux 9GNU/Linux 8                 | Desktop & Web Service/Servlet (Tomcat) |
| Microsoft Server             | Windows Server 2019 (64-bit)           | Web Service/Servlet (Tomcat)           |
| Windows Server 2016 (64-bit) | Web Service/Servlet (Tomcat)           |                                        |
| Windows Server 2012 (64-bit) | Deprecated                             |                                        |
| Microsoft                    | Windows 10                             | Desktop                                |
| Apple                        | OSX 11 (Big Sur)                       | Desktop                                |
| OSX v10.15 (Catalina)        | Desktop                                |                                        |
| OSX v10.14 (Mojave)          | Desktop                                |                                        |

> [!IMPORTANT]
> Deprecation Notice — Linux platforms
> 
> Support for centOS 6 was deprecated in release 2.8 and will be removed in a future release
> 
> _Action:_ Please plan to migrate your apps to use an appropriate alternative version.