---
title: Upgrade
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.3/modules/android/pages/upgrade.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:3.3@couchbase-lite:android:upgrade.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.3/android/upgrade.html)

# Upgrade

> [!IMPORTANT]
> On upgrading from a 2.x release, all Couchbase Lite databases will be automatically re-indexed on initial database open.  
> This can result in a delay before the database is usable.

## [](#3-2-3-upgrade)3.3.0 Upgrade

The action will take place automatically and can lead to some delay in the database becoming available for use in your application.

In addition, if you are syncing with a 3.3.0 Sync Gateway, you should be aware of the significant configuration enhancements introduced and their impact. See [Upgrading Sync Gateway](../../../sync-gateway/current/upgrading.md) for more details. This is a one-way conversion.

### [](#api-changes)API Changes

This content introduces the changes made to the Couchbase Lite for Android API for release 3.3.0.

#### [](#removed)Removed

##### [](#resetcheckpoint)ResetCheckpoint

The method [Replicator.resetCheckpoint()](https://docs.couchbase.com/mobile/2.8.0/couchbase-lite-android/com/couchbase/lite/AbstractReplicator.html#resetCheckpoint--) has been removed.  
Instead, use [Replicator.resetCheckpoint(boolean reset)](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/AbstractReplicator.html#start-boolean-).

Before

```java
replicator.resetCheckpoint()
replicator.start()
```

After

```java
replicator.start(true)
```

##### [](#database-setloglevel)Database.setLogLevel

The method [Database.setLogLevel()](https://docs.couchbase.com/mobile/2.8.0/couchbase-lite-android/com/couchbase/lite/Database.html#setLogLevel-com.couchbase.lite.LogDomain-com.couchbase.lite.LogLevel-)has been removed.  
Instead:

1. Set the logging levels for loggers, individually
2. Set the domains to be logged by the console logger, explicitly.

Before

```java
Database.setLogLevel(LogDomain.ALL, LogLevel.VERBOSE)
```

After

```java
Database.log.getConsole().setDomains(LogDomain.ALL_DOMAINS)
Database.log.getConsole().setLevel(LogLevel.VERBOSE)
Database.log.getFile().setDomains(LogLevel.DEBUG)
```

##### [](#database-compact)Database.compact

The [Database.compact()](https://docs.couchbase.com/mobile/2.8.0/couchbase-lite-android/com/couchbase/lite/Database.html#compact--) method has been removed.  
It is replaced by the new [Database.performMaintenance(MaintenanceType)](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/Database.html#performMaintenance-com.couchbase.lite.MaintenanceType-) method, and the maintenance operations represented in the enum [MaintenanceType](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/MaintenanceType.html)

Before

```java
try testdb.compact()
```

After

```java
testdb.performMaintenance(MaintenanceType.COMPACT)
```

#### [](#deprecated-in-the-api)Deprecated in the API

##### [](#match)MATCH

The class, [FullTextExpression](https://docs.couchbase.com/mobile/2.8.0/couchbase-lite-android/com/couchbase/lite/FullTextExpression.html)has been deprecated.  
Use [FullTextFunction](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/FullTextFunction.html) instead.

Before

```java
FullTextExpression index = FullTextExpression.index("indexName")
Query q = QueryBuilder.select([SelectResult.expression(Meta.id)])
  .from(DataSource.database(testdb))
  .where(index.match(queryString))
```

After

```java
Query q = QueryBuilder.select([SelectResult.expression(Meta.id)])
  .from(DataSource.database(testdb))
  .where(FullTextFunction.match("indexName", queryString))
```

##### [](#isnullormissingnotnullormissing)isNullOrMissing/notNullOrMissing

The functions [Expression.isNullOrMissing](https://docs.couchbase.com/mobile/2.8.0/couchbase-lite-android/com/couchbase/lite/Expression.html#isNullOrMissing--) and [Expression.notNullOrMissing](https://docs.couchbase.com/mobile/2.8.0/couchbase-lite-android/com/couchbase/lite/Expression.html#notNullOrMissing--) have been deprecated.  
Use `isNotValued()` and-or `isValued()` instead.

Before

```java
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

```java
Query q = QueryBuilder.select([SelectResult.expression(Meta.id)])
  .from(DataSource.database(testdb))
  .where(Expression.property("missingProp").isNotValued())

Query q = QueryBuilder.select([SelectResult.expression(Meta.id)])
  .from(DataSource.database(testdb))
  .where(Expression.property("notMissingProp").isValued())
```

##### [](#abstractreplicatorconfiguration)AbstractReplicatorConfiguration

The enum [AbstractReplicatorConfiguration.ReplicatorType](https://docs.couchbase.com/mobile/2.8.0/couchbase-lite-android/com/couchbase/lite/ReplicatorConfiguration.html#setReplicatorType-com.couchbase.lite.AbstractReplicatorConfiguration.ReplicatorType-)and the methods [ReplicatorConfiguration.setReplicatorType](https://docs.couchbase.com/mobile/2.8.0/couchbase-lite-android/com/couchbase/lite/ReplicatorConfiguration.html#setReplicatorType--)and [ReplicatorConfiguration.getReplicatorType](https://docs.couchbase.com/mobile/2.8.0/couchbase-lite-android/com/couchbase/lite/ReplicatorConfiguration.html#getReplicatorType--)have all been deprecated.  
Instead, use the methods `ReplicatorConfiguration.setType` and `ReplicatorConfiguration.getType`, and the top level enum `ReplicatorType`.

Before

```java
ReplicatorConfiguration config =
  new ReplicatorConfiguration().setReplicatorType(ReplicatorConfiguration.ReplicatorType.PUSH_AND_PULL);
```

After

```java
ReplicatorConfiguration config =
  new ReplicatorConfiguration().setType(ReplicatorType.PUSH_AND_PULL);
```

#### [](#moved-in-the-api)Moved in the API

The enum [AbstractReplicator.ActivityLevel](https://docs.couchbase.com/mobile/2.8.0/couchbase-lite-android/com/couchbase/lite/AbstractReplicator.ActivityLevel.html) and the classes [AbstractReplicator.Progress](https://docs.couchbase.com/mobile/2.8.0/couchbase-lite-android/com/couchbase/lite/AbstractReplicator.Progress.html) and [AbstractReplicator.Status](https://docs.couchbase.com/mobile/2.8.0/couchbase-lite-android/com/couchbase/lite/AbstractReplicator.Status.html) have all been moved to be top level definitions.  
They are replaced by these definitions:

* [ReplicatorActivityLevel](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/ReplicatorActivityLevel.html)
* [ReplicatorProgress](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/ReplicatorProgress.html)
* [ReplicatorStatus](https://docs.couchbase.com/mobile/3.3.0/couchbase-lite-android/com/couchbase/lite/ReplicatorStatus.html)

Before

```java
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

```java
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

## [](#lbl-db-upgrades)1.x Databases Upgrades to 2.x

Databases created using Couchbase Lite 1.2 or later can still be used with Couchbase Lite 2.x; but will be automatically updated to the current 2.x version. This feature is only available for the default storage type (i.e., not a ForestDB database).

### [](#encrypted-databases)Encrypted Databases

The automatic migration feature does not support encrypted databases. So if the 1.x database is encrypted you will first need to disable encryption using the Couchbase Lite 1.x API (see the [1.x Database Guide](https://docs-archive.couchbase.com/couchbase-lite/1.4/Kotlin.html#database-encryption)).

Thus, to upgrade an encrypted 1.x database, you should do the following:

Upgrading Encrypted Databases

1. Disable encryption using the Couchbase Lite 1.x framework (see [1.x encryption guide](https://docs-archive.couchbase.com/couchbase-lite/1.4/android.html#database-encryption))
2. Open the database file with encryption enabled using the Couchbase Lite 2.x framework.

Since it is not possible to package Couchbase Lite 1.x and Couchbase Lite 2.x in the same application this upgrade path would require two successive upgrades.

If you are using Sync Gateway to synchronize the database content, it may be preferable to run a pull replication from a new 2.x database with encryption enabled and delete the 1.x local database.

### [](#handling-of-existing-conflicts)Handling of Existing Conflicts

If there are existing conflicts in the 1.x database, the automatic upgrade process copies the default winning revision to the new database and does NOT copy any conflicting revisions.

This functionality is related to the way conflicts are now being handled in Couchbase Lite — see [Handling Data Conflicts](conflict.md).

Optionally, existing conflicts in the 1.x database can be resolved with the [1.x API](https://docs-archive.couchbase.com/couchbase-lite/1.4/Kotlin.html#resolving-conflicts) prior to the database being upgraded.

### [](#handling-of-existing-attachments)Handling of Existing Attachments

Attachments persisted in a 1.x database are copied to the new database. NOTE: The relevant Couchbase Lite API is now called the `Blob` API not the `Attachments` API.

The functionally is identical but the internal schema for attachments has changed.

Blobs are stored anywhere in the document, just like other value types. Whereas in 1.x they were stored under the `_attachments` field.

The automatic upgrade functionality **does not** update the internal schema for attachments, so they remain accessible under the `_attachments` field. See [Example 1](#ex-get-att) for how to retrieve an attachment that was created in a 1.x database with a 2.x API.

Example 1\. Retrieve 1.x Attachment

* Kotlin
* Java

```Kotlin
val content = document.getDictionary("_attachments")?.getBlob("avatar")?.content
```

```Java
Dictionary attachments = document.getDictionary("_attachments");
Blob blob = attachments != null ? attachments.getBlob("avatar") : null;
byte[] content = blob != null ? blob.getContent() : null;
```

### [](#replication-compatibility)Replication Compatibility

The current replication protocol is not backwards compatible with the 1.x replication protocol. Therefore, to use replication with Couchbase Lite 2.x, the target Sync Gateway instance must also be upgraded to 2.x.

Sync Gateway 2.x will continue to accept clients that connect through the 1.x protocol.

It will automatically use the 1.x replication protocol when a Couchbase Lite 1.x client connects through http://localhost:4984/db and the 2.0 replication protocol when a Couchbase Lite 2.0 client connects through ws://localhost:4984/db.

This allows for a smoother transition to get all your user base onto a version of your application built with Couchbase Lite 2.x.

## [](#android-studio)Android Studio

The API changed in Couchbase Lite 2.0 and you will need to port any application that is using Couchbase Lite 1.x API to the latest Couchbase Lite API. To update an Android project built with Couchbase Lite 1.x:

* Remove the existing Couchbase Lite dependency from the Android Studio project.
* Install the Couchbase Lite framework in your project — see the [Getting Started](https://docs-archive.couchbase.com/couchbase-lite/1.4/java.html#getting-started). At this point, there will be many compiler warnings. Refer to the examples on this page to learn about the new API.
* Build & run your application.

## [](#downgrading-couchbase-lite)Downgrading Couchbase Lite

### [](#downgrading-between-major-releases)Downgrading Between Major Releases

**No Downgrade Support** \- Downgrades between major versions of Couchbase Lite (CBL) are not supported. Once you upgrade to a new major version, downgrading to a previous major version may lead to incompatibility issues.

For example, Upgrading from CBL 2.x.x to CBL 3.x.x does not guarantee the ability to revert to CBL 2.x.x.

### [](#downgrading-between-minor-releases)Downgrading Between Minor Releases

**Conditional Downgrade Support** \- Downgrade support for minor releases is considered on a case-by-case basis. The release notes for each minor version will clarify whether downgrades are supported.

For example, if a new minor version such as CBL 3.1.0 is released the release notes will specify whether downgrading to CBL 3.0.x is supported.

### [](#downgrading-between-patch-releases)Downgrading Between Patch Releases

**Full Downgrade Support** \- Downgrades between patch releases are supported. Users can safely downgrade between different patch versions within the same minor release.

For example, if you’re running CBL 3.1.6 you can downgrade to CBL 3.1.4 or CBL 3.1.3 without issues.

## [](#related-content)Related Content

### [](#)

How to . . .

* [Prerequisites](gs-prereqs.md)
* [Install](gs-install.md)
* [Build and Run](gs-build.md)

.

### [](#-2)

Learn more . . .

* [Databases](database.md)
* [Documents](document.md)
* [Blobs](blob.md)
* [Remote Sync Gateway](replication.md)
* [Handling Data Conflicts](conflict.md)

.

### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.