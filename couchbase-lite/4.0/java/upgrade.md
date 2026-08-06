---
title: Upgrade
description: ""
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.0/modules/java/pages/upgrade.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:4.0@couchbase-lite:java:upgrade.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/4.0/java/upgrade.html)

# Upgrade

> [!IMPORTANT]
> On upgrading from a 2.x release, all Couchbase Lite databases automatically re-index on initial database open.  
> This can result in a delay before the database is usable.

## [](#4-0-0-upgrade)4.0.3 Upgrade

Couchbase Lite 4.0 introduces significant architectural changes, most notably the migration from revision trees to version vectors for document versioning.

### [](#major-changes-in-4-0-3)Major Changes in 4.0.3

**Version Vector Architecture**: CBL 4.0.3 replaces the revision tree system with version vectors, providing improved performance, scalability, and conflict resolution. Documents now use version-based revision IDs in the format `<timestamp>@<source-id>` instead of the previous `<generation>-<document-hash>` format.

**Enhanced Conflict Resolution**: The default conflict resolution strategy changes from `most active wins` to `last write wins` based on hybrid logical timestamps, providing more intuitive and predictable conflict resolution behavior.

**New Document Properties**: a new `getTimestamp()` method is available on Document objects, providing direct access to the document's logical timestamp as a `long` value representing nanoseconds since the Unix epoch.

### [](#database-compatibility-40)Database Compatibility

**Automatic Upgrade from 3.x**: CBL 4.0.3 databases are compatible with CBL 3.1 and 3.2 databases. When opening a 3.1 or 3.2 database with CBL 4.0.3, documents are automatically upgraded to use version vectors when they're updated and saved.

**No Configuration Required**: CBL 4.0.3 enables version vectors by default - the feature requires no API configuration.

### [](#synchronization-compatibility-40)Synchronization Compatibility

**Sync Gateway Requirements**: CBL 4.0.3 requires Sync Gateway 4.x or later for synchronization. Attempting to sync with Sync Gateway versions prior to 4.x results in replication errors with appropriate error messages indicating the incompatibility.

**Peer-to-Peer Compatibility**: CBL 4.0.3 can only perform peer-to-peer synchronization with other CBL 4.x instances using either `URLEndpointListener` or `MessageEndpointListener`. Sync attempts with CBL 3.x peers fail with appropriate error messages.

### [](#replication-compatibility)Replication Compatibility

CBL 4.0 introduces strict replication compatibility requirements due to the version vector architecture changes.

**Sync Gateway Compatibility**: CBL 4.0 requires Sync Gateway 4.0 or later for synchronization. Attempting to sync with Sync Gateway versions prior to 4.0 results in replication errors with appropriate error messages indicating the incompatibility.

**Peer-to-Peer Compatibility**: CBL 4.0 can only perform peer-to-peer synchronization with other CBL 4.0+ instances. Sync attempts with CBL 3.x or earlier peers fails with appropriate error messages.

**No Backward Compatibility**: unlike previous CBL versions, CBL 4.0 cannot sync with earlier versions of either Sync Gateway or other CBL instances due to the fundamental changes in document versioning architecture.

### [](#api-changes)API Changes

This section introduces the changes made to the Couchbase Lite for Java API for release 4.0.3.

#### [](#removed)Removed

##### [](#resetcheckpoint)ResetCheckpoint

The method [Replicator.resetCheckpoint()](https://docs.couchbase.com/mobile/2.8.0/couchbase-lite-java/com/couchbase/lite/AbstractReplicator.html#resetCheckpoint--) method has been removed.  
Instead, use [Replicator.resetCheckpoint(boolean reset)](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-java/com/couchbase/lite/AbstractReplicator.html#start-boolean-).

Before

```Java
replicator.resetCheckpoint()
replicator.start()
```

After

```Java
replicator.start(true)
```

##### [](#database-setloglevel)Database.setLogLevel

The method [Database.setLogLevel()](https://docs.couchbase.com/mobile/2.8.0/couchbase-lite-java/com/couchbase/lite/Database.html#setLogLevel-com.couchbase.lite.LogDomain-com.couchbase.lite.LogLevel-)has been removed.  
Instead:

1. Set the logging levels for loggers, individually
2. Explicitly set the domains that the console logger logs.

Before

```Java
Database.setLogLevel(LogDomain.ALL, LogLevel.VERBOSE)
```

After

```Java
Database.log.getConsole().setDomains(LogDomain.ALL_DOMAINS)
Database.log.getConsole().setLevel(LogLevel.VERBOSE)
Database.log.getFile().setDomains(LogLevel.DEBUG)
```

##### [](#database-compact)Database.compact

The [Database.compact()](https://docs.couchbase.com/mobile/2.8.0/couchbase-lite-java/com/couchbase/lite/Database.html#compact--) method has been removed.  
It's replaced by the new [Database.performMaintenance(MaintenanceType)](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-java/com/couchbase/lite/Database.html#performMaintenance-com.couchbase.lite.MaintenanceType-) method, and the maintenance operations represented in the enum [MaintenanceType](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-java/com/couchbase/lite/MaintenanceType.html)

Before

```Java
try testdb.compact()
```

After

```Java
testdb.performMaintenance(MaintenanceType.COMPACT)
```

#### [](#deprecated-in-the-api)Deprecated in the API

##### [](#match)MATCH

The class, [FullTextExpression](https://docs.couchbase.com/mobile/2.8.0/couchbase-lite-java/com/couchbase/lite/FullTextExpression.html)has been deprecated.  
Use [FullTextFunction](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-java/com/couchbase/lite/FullTextFunction.html) instead.

Before

```Java
FullTextExpression index = FullTextExpression.index("indexName")
Query q = QueryBuilder.select([SelectResult.expression(Meta.id)])
  .from(DataSource.database(testdb))
  .where(index.match(queryString))
```

After

```Java
Query q = QueryBuilder.select([SelectResult.expression(Meta.id)])
  .from(DataSource.database(testdb))
  .where(FullTextFunction.match("indexName", queryString))
```

##### [](#isnullormissingnotnullormissing)isNullOrMissing/notNullOrMissing

The functions [Expression.isNullOrMissing](https://docs.couchbase.com/mobile/2.8.0/couchbase-lite-java/com/couchbase/lite/Expression.html#isNullOrMissing--) and [Expression.notNullOrMissing](https://docs.couchbase.com/mobile/2.8.0/couchbase-lite-java/com/couchbase/lite/Expression.html#notNullOrMissing--) have been deprecated.  
Use `isNotValued()` and-or `isValued()` instead.

Before

```Java
Query q =
  QueryBuilder
    .select([SelectResult.expression(Meta.id)])
    .from(DataSource.database(testdb))
    .where(
      Expression.property("missingProp").isNullOrMissing())

Query q =
  QueryBuilder
    .select([SelectResult.expression(Meta.id)])
    .from(DataSource.database(testdb))
    .where(Expression.property("notMissingProp").notNullOrMissing())
```

After

```Java
Query q = QueryBuilder.select([SelectResult.expression(Meta.id)])
  .from(DataSource.database(testdb))
  .where(Expression.property("missingProp").isNotValued())

Query q = QueryBuilder.select([SelectResult.expression(Meta.id)])
  .from(DataSource.database(testdb))
  .where(Expression.property("notMissingProp").isValued())
```

##### [](#abstractreplicatorconfiguration)AbstractReplicatorConfiguration

The enum [AbstractReplicatorConfiguration.ReplicatorType](https://docs.couchbase.com/mobile/2.8.0/couchbase-lite-java/com/couchbase/lite/ReplicatorConfiguration.html#setReplicatorType-com.couchbase.lite.AbstractReplicatorConfiguration.ReplicatorType-)and the methods [ReplicatorConfiguration.setReplicatorType](https://docs.couchbase.com/mobile/2.8.0/couchbase-lite-java/com/couchbase/lite/ReplicatorConfiguration.html#setReplicatorType--)and [ReplicatorConfiguration.getReplicatorType](https://docs.couchbase.com/mobile/2.8.0/couchbase-lite-java/com/couchbase/lite/ReplicatorConfiguration.html#getReplicatorType--)have all been deprecated.  
Instead, use the methods `ReplicatorConfiguration.setType` and `ReplicatorConfiguration.getType`, and the top level enum `ReplicatorType`.

Before

```Java
ReplicatorConfiguration config =
  new ReplicatorConfiguration().setReplicatorType(ReplicatorConfiguration.ReplicatorType.PUSH_AND_PULL);
```

After

```Java
ReplicatorConfiguration config =
  new ReplicatorConfiguration().setType(ReplicatorType.PUSH_AND_PULL);
```

#### [](#moved-in-the-api)Moved in the API

The enum [AbstractReplicator.ActivityLevel](https://docs.couchbase.com/mobile/2.8.0/couchbase-lite-java/com/couchbase/lite/AbstractReplicator.ActivityLevel.html) and the classes [AbstractReplicator.Progress](https://docs.couchbase.com/mobile/2.8.0/couchbase-lite-java/com/couchbase/lite/AbstractReplicator.Progress.html) and [AbstractReplicator.Status](https://docs.couchbase.com/mobile/2.8.0/couchbase-lite-java/com/couchbase/lite/AbstractReplicator.Status.html) have all been moved to be top level definitions.  
They are replaced by these definitions:

* [ReplicatorActivityLevel](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-java/com/couchbase/lite/ReplicatorActivityLevel.html)
* [ReplicatorProgress](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-java/com/couchbase/lite/ReplicatorProgress.html)
* [ReplicatorStatus](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-java/com/couchbase/lite/ReplicatorStatus.html)

Before

```Java
ListenerToken token =
  replicator.addChangeListener(
    testSerialExecutor,
    change -> {
      final AbstractReplicator.Status status = change.getStatus()
      if (status.getActivityLevel() == AbstractReplicator.ActivityLevel.BUSY)
      { AbstractReplicator.Progress progress =
          status.getProgress(); Logger.log("Progress: " + progress.completed + "/" progress.total);
      }
    });
```

After

```Java
ListenerToken token =
  replicator.addChangeListener(
    testSerialExecutor,
    change -> {
      final ReplicatorStatus status = change.getStatus()
      if (status.getActivityLevel() == ReplicatorActivityLevel.BUSY)
      { ReplicatorProgress progress =
          status.getProgress(); Logger.log("Progress: " + progress.completed + "/" progress.total);
      }
    });
```

## [](#downgrading-couchbase-lite)Downgrading Couchbase Lite

### [](#downgrading-between-major-releases)Downgrading Between Major Releases

**No Downgrade Support** \- Couchbase Lite (CBL) does not support downgrades between major versions. Upgrading to a new major version creates incompatibility issues when attempting to downgrade to a previous major version. For example, upgrading from CBL 3.x.x to CBL 4.x.x does not allow you to revert to CBL 3.x.x.

### [](#downgrading-between-minor-releases)Downgrading Between Minor Releases

**Conditional Downgrade Support** \- Downgrade support for minor releases is considered on a case-by-case basis. The release notes for each minor version clarify whether downgrades receive support.

For example, when a new minor version such as CBL 3.1.0 becomes available, the release notes specify whether reverting to CBL 3.0.x receives support.

### [](#downgrading-between-patch-releases)Downgrading Between Patch Releases

**Full Downgrade Support** \- Downgrades between patch releases are supported. Users can safely downgrade between different patch versions within the same minor release.

For example, if you're running CBL 3.1.6 you can downgrade to CBL 3.1.4 or CBL 3.1.3 without issues.

## [](#related-content)Related Content

### [](#)

How to

* [Prerequisites](gs-prereqs.md)
* [Install](gs-install.md)
* [Build and Run](gs-build.md)

.

### [](#-2)

Learn more

* [Databases](database.md)
* [Documents](document.md)
* [Version Vectors](version-vectors.md)
* [Blobs](blob.md)
* [Remote Sync Gateway](replication.md)
* [Handling Data Conflicts](conflict.md)

.

### [](#-3)

Dive Deeper

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.