---
title: Crash Logs
description: Couchbase Lite on C# -- Using symbolicate to decode crash logs
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/csharp/pages/troubleshooting-crashes.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.8@couchbase-lite:csharp:troubleshooting-crashes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/csharp/troubleshooting-crashes.html)

# Crash Logs

> Description — _Couchbase Lite on C# — Using symbolicate to decode crash logs_  
> Related Content — [Using Logs](../../current/csharp/troubleshooting-logs.md) | [Troubleshooting Queries](../../current/csharp/troubleshooting-queries.md)

## [](#symbolication)Symbolication

In order to make sense of a crash report you will need to translate the crash log's memory addresses with human-readable function names and line numbers; this process is called _symbolication_.

To do this you will need to have debug symbol (`.dSYM`) files for the application and for Couchbase Lite on C#.Net's framework.

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Prerequisites](#couchbase-lite:csharp:gs-prereqs.adoc)
* [Install](../../current/csharp/gs-install.md)
* [Build and Run](../../current/csharp/gs-build.md)

###### [](#-2)

Learn more . . .

* [Databases](../../current/csharp/database.md)
* [Documents](../../current/csharp/document.md)
* [Blobs](../../current/csharp/blob.md)
* [Remote Sync using Sync Gateway](../../current/csharp/replication.md)
* [Handling Data Conflicts](../../current/csharp/conflict.md)

###### [](#-3)

Dive Deeper . . .

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)