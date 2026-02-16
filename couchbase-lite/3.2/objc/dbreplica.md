[View original HTML](/couchbase-lite/3.2/objc/dbreplica.html)

> Description — _Couchbase Lite Database Sync - Synchronize changes between databases on the same device_  

> Description — _Couchbase Lite Database Sync - Synchronize changes between databases on the same device_  
> Related Content — [Remote Sync Gateway](replication.md) | [Peer-to-Peer Sync](#objc:landing-p2psync.adoc)

## [](#overview)Overview

Couchbase Lite supports replication between two local databases at the database, scope, or collection level. This allows a Couchbase Lite replicator to store data on secondary storage. It is useful in scenarios when a user’s device is damaged and its data is moved to a different device.

Example 1\. Replication between Local Databases

```objc
CBLDatabaseEndpoint *targetDatabase = [[CBLDatabaseEndpoint alloc] initWithDatabase:self.otherDB];
CBLReplicatorConfiguration *replConfig = [[CBLReplicatorConfiguration alloc] initWithTarget:targetDatabase];
replConfig.replicatorType = kCBLReplicatorTypePush;

NSError* error = nil;
CBLCollection *collection = [database collectionWithName:@"collection1" scope:@"scope1" error:&error];
[replConfig addCollection:collection config:nil];

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