---
title: Troubleshooting
description: Couchbase mobile database peer-to-peer (P2P)  synchronization concepts
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/csharp/pages/troubleshooting.adoc
  xref: xref:2.8@couchbase-lite:csharp:troubleshooting.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/csharp/troubleshooting.html)

# Troubleshooting

> Description — _Couchbase mobile database peer-to-peer (P2P) synchronization concepts_  

As always, when there is a problem with replication, logging is your friend. The following example increases the log output for activity related to replication with Sync Gateway.

```csharp
// deprecated
Database.SetLogLevel(LogDomain.Replicator, LogLevel.Verbose);
Database.SetLogLevel(LogDomain.Network, LogLevel.Verbose);
```

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