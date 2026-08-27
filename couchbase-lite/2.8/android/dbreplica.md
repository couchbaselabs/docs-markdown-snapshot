---
title: Data Sync Locally on Device
description: Couchbase Lite Database Sync - Synchronize changes between
  databases on the same device
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/android/pages/dbreplica.adoc
  xref: xref:2.8@couchbase-lite:android:dbreplica.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/android/dbreplica.html)

# Data Sync Locally on Device

> Description — _Couchbase Lite Database Sync - Synchronize changes between databases on the same device_  
> Related Content — [Remote Sync using Sync Gateway](../../current/android/replication.md) | [Landing P2Psync](#couchbase-lite:android:landing-p2psync.adoc)

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

Note: The code does not compile in Couchbase Lite _Community Edition_.

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