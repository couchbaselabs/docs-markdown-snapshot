---
title: Data Sync Locally on Device
description: Couchbase Lite Database Sync - Synchronize changes between
  databases on the same device
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.0/modules/swift/pages/dbreplica.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:couchbase-lite:swift:dbreplica.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/current/swift/dbreplica.html)

# Data Sync Locally on Device

> Description — _Couchbase Lite Database Sync - Synchronize changes between databases on the same device_  
> Related Content — [Remote Sync Gateway](replication.md) | [Peer-to-Peer Sync](#swift:landing-p2psync.adoc)

## [](#overview)Overview

Couchbase Lite supports replication between two local databases at the database, scope, or collection level. This allows a Couchbase Lite replicator to store data on secondary storage. It is useful in scenarios when a user’s device is damaged and its data is moved to a different device.

Example 1\. Replication between Local Databases

```swift
let targetDatabase = DatabaseEndpoint(database: database2)

guard let collection1 = try self.database.collection(name: "collection1", scope: "scope1") else { return }

let colConfig = CollectionConfiguration(collection: collection1)
var config = ReplicatorConfiguration(collections: [colConfig], target: targetDatabase)
config.replicatorType = .push

self.replicator = Replicator(config: config)
self.replicator.start()
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