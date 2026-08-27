---
title: Data Sync Locally on Device
description: Couchbase Lite Database Sync - Synchronize changes between
  databases on the same device
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.0/modules/java/pages/dbreplica.adoc
  xref: xref:3.0@couchbase-lite:java:dbreplica.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.0/java/dbreplica.html)

# Data Sync Locally on Device

> Description — _Couchbase Lite Database Sync - Synchronize changes between databases on the same device_  
> Related Content — [Remote Sync Gateway](replication.md) | [Peer-to-Peer Sync](#java:landing-p2psync.adoc)

## [](#overview)Overview

Couchbase Lite supports replication between two local databases. This allows a Couchbase Lite replicator to store data on secondary storage. It is especially useful in scenarios where a user's device may be damaged and its data moved to a different device.

Example 1\. Replication between Local Databases

```Java
DatabaseEndpoint targetDatabase = new DatabaseEndpoint(database2);
ReplicatorConfiguration replicatorConfig = new ReplicatorConfiguration(database1, targetDatabase);
replicatorConfig.setReplicatorType(ReplicatorConfiguration.ReplicatorType.PUSH);

// Create replicator (be sure to hold a reference somewhere that will prevent the Replicator from being GCed)
replicator = new Replicator(replicatorConfig);
replicator.start();
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