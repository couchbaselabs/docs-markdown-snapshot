---
title: Data Sync Locally on Device
description: Couchbase Lite Database Sync - Synchronize changes between
  databases on the same device
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/csharp/pages/dbreplica.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.8@couchbase-lite:csharp:dbreplica.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/csharp/dbreplica.html)

# Data Sync Locally on Device

> Description — _Couchbase Lite Database Sync - Synchronize changes between databases on the same device_  
> Related Content — [Remote Sync using Sync Gateway](../../current/csharp/replication.md) | [Landing P2Psync](#couchbase-lite:csharp:landing-p2psync.adoc)

## [](#overview)Overview

Couchbase Lite supports replication between two local databases. This allows a Couchbase Lite replicator to store data on secondary storage. It is especially useful in scenarios where a user's device may be damaged and its data moved to a different device.

Example 1\. Replication between Local Databases

```C#
var targetDatabase = new DatabaseEndpoint(database2);
var config = new ReplicatorConfiguration(db, targetDatabase)
{
    ReplicatorType = ReplicatorType.Push
};

var replicator = new Replicator(config);
replicator.Start();
```

Note: The code does not compile in Couchbase Lite _Community Edition_.

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