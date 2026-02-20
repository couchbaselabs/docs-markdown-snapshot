---
title: Data Sync Locally on Device
description: Couchbase Lite Database Sync - Synchronize changes between
  databases on the same device
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.3/modules/java/pages/dbreplica.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:3.3@couchbase-lite:java:dbreplica.adoc[]
---

[View original HTML](/couchbase-lite/3.3/java/dbreplica.html)

# Data Sync Locally on Device

> Description — _Couchbase Lite Database Sync - Synchronize changes between databases on the same device_  
> Related Content — [Remote Sync Gateway](replication.md) | [Peer-to-Peer Sync](#java:landing-p2psync.adoc)

## [](#overview)Overview

Couchbase Lite supports replication between two local databases at the database, scope, or collection level. This allows a Couchbase Lite replicator to store data on secondary storage. It is useful in scenarios when a user’s device is damaged and its data is moved to a different device.

Example 1\. Replication between Local Databases

```Java
// This is an Enterprise feature:
// the code below will generate a compilation error
// if it's compiled against CBL Android Community Edition.
// Note: the target database must already contain the
//       source collections or the replication will fail.
final Replicator repl = new Replicator(
    new ReplicatorConfiguration(new DatabaseEndpoint(targetDb))
        .addCollections(srcCollections, null)
        .setType(ReplicatorType.PUSH));

// Start the replicator
// (be sure to hold a reference somewhere that will prevent it from being GCed)
repl.start();
thisReplicator = repl;
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