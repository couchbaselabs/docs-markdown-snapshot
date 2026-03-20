---
title: Data Sync Locally on Device
description: Couchbase Lite Database Sync - Synchronize changes between
  databases on the same device
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.0/modules/csharp/pages/dbreplica.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:couchbase-lite:csharp:dbreplica.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/current/csharp/dbreplica.html)

# Data Sync Locally on Device

> Description — _Couchbase Lite Database Sync - Synchronize changes between databases on the same device_  
> Related Content — [Remote Sync Gateway](replication.md) | [Peer-to-Peer Sync](#csharp:landing-p2psync.adoc)

## [](#overview)Overview

Couchbase Lite supports replication between two local databases at the database, scope, or collection level. This allows a Couchbase Lite replicator to store data on secondary storage. It is useful in scenarios when a user’s device is damaged and its data is moved to a different device.

Example 1\. Replication between Local Databases

```C#
var targetDatabase = new DatabaseEndpoint(database2);
var collectionConfig =  CollectionConfiguration.FromCollections(collection);
var config = new ReplicatorConfiguration(collectionConfig, targetDatabase)
{
    ReplicatorType = ReplicatorType.Push
};

var replicator = new Replicator(config);
replicator.Start();
```

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Prerequisites](#csharp:gs-prereqs.adoc)
* [Install](gs-install.md)
* [Build and Run](gs-build.md)

.

###### [](#-2)

Learn more . . .

* [Databases](database.md)
* [Documents](document.md)
* [Blobs](blob.md)
* [Remote Sync Gateway](replication.md)
* [Handling Data Conflicts](conflict.md)

.

###### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.