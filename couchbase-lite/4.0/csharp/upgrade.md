---
title: Upgrade
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.0/modules/csharp/pages/upgrade.adoc
  xref: xref:4.0@couchbase-lite:csharp:upgrade.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/4.0/csharp/upgrade.html)

# Upgrade

> [!IMPORTANT]
> On upgrading from a 3.x release, all Couchbase Lite databases automatically re-index on initial database open.  
> This can result in a delay before the database is usable.

## [](#4-0-0-upgrade)4.0.3 Upgrade

Couchbase Lite 4.0 introduces significant architectural changes, most notably the migration from revision trees to version vectors for document versioning. This upgrade requires understanding of the compatibility requirements.

The action takes place automatically and can lead to some delay in the database becoming available for use in your application.

In addition, if you're syncing with a 4.0.3 Sync Gateway, you should be aware of the significant configuration enhancements introduced and their effects. See [Upgrading Sync Gateway](../../../sync-gateway/current/upgrading.md) for more details. This is a one-way conversion.

### [](#major-changes-in-4-0-3)Major Changes in 4.0.3

**Version Vector Architecture**: CBL 4.0.3 replaces the revision tree system with version vectors, providing improved performance, scalability, and conflict resolution. Documents now use version-based revision IDs in the format `<timestamp>@<source-id>` instead of the previous `<generation>-<document-hash>` format.

**Enhanced Conflict Resolution**: The default conflict resolution strategy changes from `most active wins` to `last write wins` based on hybrid logical timestamps, providing more intuitive and predictable conflict resolution behavior.

**New Document Properties**: a new `Timestamp` property is available on Document objects, providing direct access to the document's logical timestamp as a `ulong` value representing nanoseconds since the Unix epoch.

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

#### [](#replicator-configuration)ReplicatorConfiguration

Couchbase Lite 4.0 introduces changes to the `ReplicatorConfiguration` class to improve API consistency across all Couchbase Lite platforms. The API no longer supports legacy collection management methods.

**Removed APIs:**\* `addCollection(s)` / `removeCollection(s)` / `getCollectionConfig()` methods \* `ReplicatorConfiguration(Database, Endpoint)` constructor that uses default collection

##### [](#before-replicator)Before (.NET 3.x)

```csharp
var collConfig = new CollectionConfiguration();
collConfig.Channels = new[] { "a", "b", "c" };

var replicatorConfig = new ReplicatorConfiguration(target: endpoint);
replicatorConfig.AddCollection(collectionA, collConfig);
```

##### [](#after-replicator)After (.NET 4.0.0)

```csharp
var collConfig = new CollectionConfiguration(collection: collectionA);
collConfig.Channels = new[] { "a", "b", "c" };

var replicatorConfig = new ReplicatorConfiguration(collections: new[] { collConfig }, target: endpoint);
```

> [!NOTE]
> This change provides API consistency across all CBL platforms and simplifies the implementation by requiring collections and configurations at construction time.

### [](#api-changes)API Changes

This content introduces the changes made to the Couchbase Lite for C#.Net API for release 4.0.3.

#### [](#breaking-change)Breaking Change

The function [ATAN2(x, y)](https://docs.couchbase.com/mobile/2.8.0/couchbase-lite-net/api/Couchbase.Lite.Query.Function.html#Couchbase%5FLite%5FQuery%5FFunction%5FAtan2%5FCouchbase%5FLite%5FQuery%5FIExpression%5FCouchbase%5FLite%5FQuery%5FIExpression%5F), which returns the principal value of the arc tangent of y/x, now becomes [ATAN2(y, x)](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-net/api/Couchbase.Lite.Query.Function.html#Couchbase%5FLite%5FQuery%5FFunction%5FAtan2%5FCouchbase%5FLite%5FQuery%5FIExpression%5FCouchbase%5FLite%5FQuery%5FIExpression%5F); that's, the arguments reverses in line with common notation.

#### [](#removed)Removed

##### [](#activate)Activate

The method `Activate()` has been removed from **all** platform support libraries **except** `Support.Android` (Xamarin Android)

##### [](#enabletextlogging)EnableTextLogging()

The obsolete method `EnableTextLogging()` is no longer supported in any platform support libraries.

##### [](#resetcheckpoint)ResetCheckpoint

The method [ResetCheckpoint()](https://docs.couchbase.com/mobile/2.8.0/couchbase-lite-net/api/Couchbase.Lite.Sync.Replicator.html#Couchbase%5FLite%5FSync%5FReplicator%5FResetCheckpoint)has been removed. Use the `reset:` argument when starting the replicator instead.

##### [](#before)Before

```java
replicator.ResetCheckpoint();
replicator.Start();
```

##### [](#after)After

```java
replicator.Start(true) (1)
```

| **1** | Set the reset: argument true to initiate a replicator checkpoint reset |
| ----- | ---------------------------------------------------------------------- |

##### [](#setloglevel)SetLogLevel()

We have removed the method [Database.setLogLevel()](https://docs.couchbase.com/mobile/2.8.0/couchbase-lite-net/api/Couchbase.Lite.Database.html#Couchbase%5FLite%5FDatabase%5FSetLogLevel%5FCouchbase%5FLite%5FLogging%5FLogDomain%5FCouchbase%5FLite%5FLogging%5FLogLevel%5F)  
Use [Database.log.console](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-net/api/Couchbase.Lite.Logging.Log.html#Couchbase%5FLite%5FLogging%5FLog%5FConsole)instead:

##### [](#before-2)Before

```java
Database.SetLogLevel(LogDomain.Replicator, LogLevel.Verbose);
Database.SetLogLevel(LogDomain.Query, LogLevel.Verbose);
```

##### [](#after-2)After

```java
Database.Log.Console.Domains = LogDomain.All;
Database.Log.Console.LogLevel = LogLevel.Verbose;
```

#### [](#database-compact)Database.Compact

We have removed the method [Database.compact()](https://docs.couchbase.com/mobile/2.8.0/couchbase-lite-net/api/Couchbase.Lite.Database.html#Couchbase%5FLite%5FDatabase%5FCompact).  
Use the method [Database.PerformMaintenance()](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-net/api/Couchbase.Lite.Database.html#Couchbase%5FLite%5FDatabase%5FPerformMaintenance%5FCouchbase%5FLite%5FMaintenanceType%5F) and the enum [MaintenanceType](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-net/api/Couchbase.Lite.MaintenanceType.html)instead

##### [](#before-3)Before

```java
var db = new Database("thisdb");
db.Compact()
```

##### [](#after-3)After

```java
var db = new Database("thisdb");

db.PerformMaintenance(MaintenanceType.Compact)
```

#### [](#deprecated-api)Deprecated API

##### [](#match)Match

We're removing [Match](https://docs.couchbase.com/mobile/2.8.0/couchbase-lite-net/api/Couchbase.Lite.Query.IFullTextExpression.html#Couchbase%5FLite%5FQuery%5FIFullTextExpression%5FMatch%5FSystem%5FString%5F)at the next major release.  
You should plan to switch to using the alternative [FullTextFunction.match(indexName:)](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-net/api/Couchbase.Lite.Query.FullTextFunction.html#Couchbase%5FLite%5FQuery%5FFullTextFunction%5FMatch%5FSystem%5FString%5FSystem%5FString%5F)at the earliest opportunity.

##### [](#before-4)Before

```java
var whereClause =
        FullTextExpression.Index("nameFTSIndex").Match("'querystring'");
using (var query = QueryBuilder.Select(SelectResult.Expression(Meta.ID))
    .From(DataSource.Database(db))
    .Where(whereClause)) {
    foreach (var result in query.Execute()) {
        Console.WriteLine($"Document id {result.GetString(0)}");
    }
}
```

##### [](#after-4)After

```java
var whereClause =
      FullTextFunction.Match("nameFTSIndex"),"'querystring'"); (1)
using (var query =
    QueryBuilder.Select(SelectResult.Expression(Meta.ID))
      .From(DataSource.Database(db))
      .Where(whereClause)) {
      foreach (var result in query.Execute()) {
        Console.WriteLine($"Document id {result.GetString(0)}");
      }
  }
```

| **1** | Here we use [FullTextFunction.match(indexName:)](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-net/api/Couchbase.Lite.Query.FullTextFunction.htmlFullTextFunction.match%28indexName:%29)to build the query |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

##### [](#isnullormissing)IsNullOrMissing

We're removing [isNullOrMissing](https://docs.couchbase.com/mobile/2.8.0/couchbase-lite-net/api/Couchbase.Lite.Query.IExpression.html#Couchbase%5FLite%5FQuery%5FIExpression%5FIsNullOrMissing)  
You should plan to switch to using the alternative [IsNotValued()](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-net/api/Couchbase.Lite.Query.IExpression.html#Couchbase%5FLite%5FQuery%5FIExpression%5FIsNotValued)

at the earliest opportunity.

##### [](#before-5)Before

```java
var query = QueryBuilder.Select(SelectResult.All())
    .From(DataSource.Database(db))
    .Where(Expression.Property("missingprop").IsNullOrMissing())
```

##### [](#after-5)After

```java
var query = QueryBuilder.Select(SelectResult.All())
    .From(DataSource.Database(db))
    .Where(Expression.Property("missingprop").IsNotValued())
```

##### [](#notnullormissing)NotNullOrMissing

We are removing [notNullOrMissing](https://docs.couchbase.com/mobile/2.8.0/couchbase-lite-net/api/Couchbase.Lite.Query.IExpression.html#Couchbase%5FLite%5FQuery%5FIExpression%5FNotNullOrMissing).  
You should plan to switch to using the alternative [isValued()](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-net/api/Couchbase.Lite.Query.IExpression.html#Couchbase%5FLite%5FQuery%5FIExpression%5FIsValued)at the earliest opportunity.

| isNotValued()

##### [](#before-6)Before

```java
var query = QueryBuilder.Select(SelectResult.All())
    .From(DataSource.Database(db))
    .Where(Expression.Property("notmissingprop").NotNullOrMissing())
```

##### [](#after-6)After

```java
var query = QueryBuilder.Select(SelectResult.All())
    .From(DataSource.Database(db))
    .Where(Expression.Property("notmissingprop").IsValued())
```

## [](#visual-studio)Visual Studio

The public facing API has completely changed in Couchbase Lite 2.0 and will require a re-write to upgrade an application that is using Couchbase Lite 1.x. To update an Xcode project built with Couchbase Lite 1.x:

* Remove the existing Couchbase Lite nuget package from the Visual Studio project.
* Remove all the Couchbase Lite 1.x dependencies — see the [1.x installation guide](https://docs-archive.couchbase.com/couchbase-lite/1.4/csharp.html#getting-started).
* Install the Couchbase Lite 2.0 framework in your project — see [Install](gs-install.md). At this point, there will be many compiler warnings. See the examples on this page to learn about the new API.
* Build & run your application.

## [](#downgrading-couchbase-lite)Downgrading Couchbase Lite

### [](#downgrading-between-major-releases)Downgrading Between Major Releases

**No Downgrade Support** \- Couchbase Lite (CBL) does not support downgrades between major versions. Once you upgrade to a new major version, attempting to downgrade to a previous major version creates incompatibility issues. For example, upgrading from CBL 3.x.x to CBL 4.x.x does not allow you to revert to CBL 3.x.x.

### [](#downgrading-between-minor-releases)Downgrading Between Minor Releases

**Conditional Downgrade Support** \- Downgrade support for minor releases is considered on a case-by-case basis. The release notes for each minor version clarify whether downgrades receive support.

For example, when a new minor version such as CBL 3.1.0 becomes available, the release notes specify whether reverting to CBL 3.0.x receives support.

### [](#downgrading-between-patch-releases)Downgrading Between Patch Releases

**Full Downgrade Support** \- Downgrades between patch releases are supported. Users can safely downgrade between different patch versions within the same minor release.

For example, if you're running CBL 3.1.6 you can downgrade to CBL 3.1.4 or CBL 3.1.3 without issues.

## [](#related-content)Related Content

### [](#)

How to

* [Prerequisites](#csharp:gs-prereqs.adoc)
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