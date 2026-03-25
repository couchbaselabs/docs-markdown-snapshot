---
title: Crash Logs
description: Couchbase Lite on Android -- Using symbolicate to decode crash logs
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/android/pages/troubleshooting-crashes.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.8@couchbase-lite:android:troubleshooting-crashes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/android/troubleshooting-crashes.html)

# Crash Logs

> Description — _Couchbase Lite on Android — Using symbolicate to decode crash logs_  
> Related Content — [Using Logs](#couchbase-lite:android:troubleshooting-logs.adoc) | [Troubleshooting Queries](../../current/android/troubleshooting-queries.md)

## [](#symbolication)Symbolication

In order to make sense of a crash report you will need to translate the crash log’s memory addresses with human-readable function names and line numbers; this process is called _symbolication_.

To do this you will need to have debug symbol (`.dSYM`) files for the application and for Couchbase Lite on Android’s framework.

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Prerequisites](../../current/android/gs-prereqs.md)
* [Install](../../current/android/gs-install.md)
* [Build and Run](../../current/android/gs-build.md)

###### [](#-2)

Learn more . . .

* [Databases](../../current/android/database.md)
* [Documents](../../current/android/document.md)
* [Blobs](../../current/android/blob.md)
* [Remote Sync using Sync Gateway](../../current/android/replication.md)
* [Handling Data Conflicts](../../current/android/conflict.md)

###### [](#-3)

Dive Deeper . . .

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)