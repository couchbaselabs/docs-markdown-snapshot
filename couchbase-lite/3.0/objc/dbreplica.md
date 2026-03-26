---
title: Data Sync Locally on Device
description: Couchbase Lite Database Sync - Synchronize changes between
  databases on the same device
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.0/modules/objc/pages/dbreplica.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.0@couchbase-lite:objc:dbreplica.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.0/objc/dbreplica.html)

# Data Sync Locally on Device

> Description — _Couchbase Lite Database Sync - Synchronize changes between databases on the same device_  

> Description — _Couchbase Lite Database Sync - Synchronize changes between databases on the same device_  
> Related Content — [Remote Sync Gateway](replication.md) | [Peer-to-Peer Sync](#objc:landing-p2psync.adoc)

## [](#overview)Overview

Couchbase Lite supports replication between two local databases. This allows a Couchbase Lite replicator to store data on secondary storage. It is especially useful in scenarios where a user's device may be damaged and its data moved to a different device.

Example 1\. Replication between Local Databases

```objc
CBLDatabaseEndpoint *targetDatabase = [[CBLDatabaseEndpoint alloc] initWithDatabase:self.otherDB];
CBLReplicatorConfiguration *config = [[CBLReplicatorConfiguration alloc] initWithDatabase:self.database target:targetDatabase];
config.replicatorType = kCBLReplicatorTypePush;

self.replicator = [[CBLReplicator alloc] initWithConfig:config];
[self.replicator start];
```

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Prerequisites](gs-prereqs.md)
* [Install](gs-install.md)
* [Build and Run](gs-build.md)

###### [](#-2)

Learn more . . .

* [Databases](database.md)
* [Documents](document.md)
* [Blobs](blob.md)
* [Remote Sync Gateway](replication.md)
* [Handling Data Conflicts](conflict.md)

###### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)