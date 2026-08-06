---
title: Data Sync Locally on Device
description: Couchbase Lite Database Sync - Synchronize changes between
  databases on the same device
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.1/modules/objc/pages/dbreplica.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:couchbase-lite:objc:dbreplica.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/current/objc/dbreplica.html)

# Data Sync Locally on Device

> Description — _Couchbase Lite Database Sync - Synchronize changes between databases on the same device_  

> Description — _Couchbase Lite Database Sync - Synchronize changes between databases on the same device_  
> Related Content — [Remote Sync Gateway](replication.md) | [Peer-to-Peer Sync](p2psync-websocket.md)

## [](#overview)Overview

Couchbase Lite supports replication between two local databases at the database, scope, or collection level. This allows a Couchbase Lite replicator to store data on secondary storage. It's useful in scenarios when a user's device is damaged and its data is moved to a different device.

Example 1\. Replication between Local Databases

```objc
CBLDatabaseEndpoint *targetDatabase = [[CBLDatabaseEndpoint alloc] initWithDatabase:self.otherDB];

CBLCollectionConfiguration *collectionConfig = [[CBLCollectionConfiguration alloc] initWithCollection:self.collection];
CBLReplicatorConfiguration *replConfig = [[CBLReplicatorConfiguration alloc] initWithCollections:@[collectionConfig] target:targetDatabase];
replConfig.replicatorType = kCBLReplicatorTypePush;

self.replicator = [[CBLReplicator alloc] initWithConfig:replConfig];
[self.replicator start];
```

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Prerequisites](gs-prereqs.md)
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