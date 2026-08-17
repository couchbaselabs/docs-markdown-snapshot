---
title: Data Sync Locally on Device
description: Couchbase Lite Database Sync - Synchronize changes between
  databases on the same device
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/swift/pages/dbreplica.adoc
  xref: xref:2.8@couchbase-lite:swift:dbreplica.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/swift/dbreplica.html)

# Data Sync Locally on Device

> Description — _Couchbase Lite Database Sync - Synchronize changes between databases on the same device_  
> Related Content — [Remote Sync using Sync Gateway](../../current/swift/replication.md) | [Landing P2Psync](#couchbase-lite:swift:landing-p2psync.adoc)

## [](#overview)Overview

Couchbase Lite supports replication between two local databases. This allows a Couchbase Lite replicator to store data on secondary storage. It is especially useful in scenarios where a user's device may be damaged and its data moved to a different device.

Example 1\. Replication between Local Databases

```swift
let targetDatabase = DatabaseEndpoint(database: database2)
let config = ReplicatorConfiguration(database: database, target: targetDatabase)
config.replicatorType = .push

self.replicator = Replicator(config: config)
self.replicator.start()
```

Note: The code does not compile in Couchbase Lite _Community Edition_.

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Prerequisites](../../current/swift/gs-prereqs.md)
* [Install](../../current/swift/gs-install.md)
* [Build and Run](../../current/swift/gs-build.md)

###### [](#-2)

Learn more . . .

* [Databases](../../current/swift/database.md)
* [Documents](../../current/swift/document.md)
* [Blobs](../../current/swift/blob.md)
* [Remote Sync using Sync Gateway](../../current/swift/replication.md)
* [Handling Data Conflicts](../../current/swift/conflict.md)

###### [](#-3)

Dive Deeper . . .

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)