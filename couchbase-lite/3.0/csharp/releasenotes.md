---
title: Release Notes
description: Couchbase Lite on C#.Net
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.0/modules/csharp/pages/releasenotes.adoc
  xref: xref:3.0@couchbase-lite:csharp:releasenotes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.0/csharp/releasenotes.html)

# Release Notes

## [](#maint-3-0-15)3.0.15 — November 2023

Version 3.0.15 for C#.Net delivers the following features and enhancements:

### [](#enhancements)Enhancements

* [CBL-3643: Upgrade to ICU 69+](https://issues.couchbase.com/browse/CBL-3643)

### [](#issues-and-resolutions)Issues and Resolutions

* [CBL-4839: Fix issue with deletion of Attachments/Blobs after compaction & re-sync](https://issues.couchbase.com/browse/CBL-4839)
* [CBL-4139: fix build error on Linux](https://issues.couchbase.com/browse/CBL-4139)
* [CBL-3871: fix QueryParams decoding bool](https://issues.couchbase.com/browse/CBL-3871)

### [](#known-issues)Known Issues

None for this release

### [](#deprecations)Deprecations

None for this release

## [](#maint-3-0-12)3.0.12 — June 2023

Version 3.0.12 for C#.Net delivers the following features and enhancements:

### [](#enhancements-2)Enhancements

* [CBL-4550 - Make IReachability interface public](https://issues.couchbase.com/browse/CBL-4550)
* [CBL-4531 - Update PublicKey+Apple to use non deprecated keychain APIs](https://issues.couchbase.com/browse/CBL-4531)
* [CBL-4167 - SQL++ : COLLATE does not have a way to specify locale for UNICODE](https://issues.couchbase.com/browse/CBL-4167)
* [CBL-4024 - Change BuiltInWebSocket to do preemptive auth instead of challenge auth by default (Port)](https://issues.couchbase.com/browse/CBL-4024)
* [CBL-3903 - Assertion failure when stopping replicator while replicator is connecting](https://issues.couchbase.com/browse/CBL-3903)
* [CBL-4134 - Fix empty identity error when building LiteCoreCppTests&C4Tests using XCode 14](https://issues.couchbase.com/browse/CBL-4134)
* [CBL-3993 - FTS index table not have to be qualified by data source alias in query](https://issues.couchbase.com/browse/CBL-3993)

### [](#issues-and-resolutions-2)Issues and Resolutions

* [CBL-3671 - Fix slowdowns and storage overhead caused by document revision history not being pruned](https://issues.couchbase.com/browse/CBL-3671)
* [CBL-4303 - Replication failure on MacOs Ventura](https://issues.couchbase.com/browse/CBL-4303)
* [CBL-4528 - Query parameters not being bound](https://issues.couchbase.com/browse/CBL-4528)
* [CBL-4529 - Error when saving documents with LiteCore error 17: must be called during a transaction](https://issues.couchbase.com/browse/CBL-4529)
* [CBL-4450 - Stop replicator could cause 'database is locked' error when saving a document](https://issues.couchbase.com/browse/CBL-4450)
* [CBL-4448 - Replicator may get stuck when there is an error of "Invalid delta"](https://issues.couchbase.com/browse/CBL-4448)
* [CBL-4418 - Replicator is stuck in busy state when there is an error thrown while applying delta to create full fleece doc](https://issues.couchbase.com/browse/CBL-4418)
* [CBL-4410 - Compaction could cause "database is locked" error when the replicator attempts to save its checkpoint at the same time](https://issues.couchbase.com/browse/CBL-4410)
* [CBL-4388 - The URL Scheme the HTTP Message is incorrect when using proxy](https://issues.couchbase.com/browse/CBL-4388)
* [CBL-4325 - Opening the upgraded database from 2.8 to 3.0.2 is slow](https://issues.couchbase.com/browse/CBL-4325)
* [CBL-4021 - Query parameters not being bound](https://issues.couchbase.com/browse/CBL-4021)
* [CBL-3715 - Query document expiration is failing](https://issues.couchbase.com/browse/CBL-3715)
* [CBL-4570 - URLEndpointListener.getURLs returns an empty list on Android v>=11](https://issues.couchbase.com/browse/CBL-4570)

### [](#known-issues-2)Known Issues

None for this release.

## [](#maint-3-0-8)3.0.8 — February 2023

Version 3.0.8 for C#.Net delivers the following features and enhancements:

### [](#enhancements-3)Enhancements

* [ CBL-4142 -- Implement AcceptParentDomainCookies API ](https://issues.couchbase.com/browse/CBL-4142)
* [ CBL-4141 -- Provide option to Save Cookie with Domain being a parent domain of the request ](https://issues.couchbase.com/browse/CBL-4141)
* [ CBL-4133 -- Network change listener re-work ](https://issues.couchbase.com/browse/CBL-4133)

### [](#issues-and-resolutions-3)Issues and Resolutions

None for this release.

### [](#known-issues-3)Known Issues

None for this release.

## [](#maint-3-0-2)3.0.2 — August 2022

Version 3.0.2 of Couchbase Lite for C#.Net delivers a number of fixes and enhancements.

### [](#enhancements-4)Enhancements

* [CBL-3038](https://issues.couchbase.com/browse/CBL-3038) — [Cookies set in Headers are replaced with Session Authenticator's cookies](https://issues.couchbase.com/browse/CBL-3038)
* [CBL-2975](https://issues.couchbase.com/browse/CBL-2975) — [Implement enhanced pinned server certificate feature](https://issues.couchbase.com/browse/CBL-2975)

### [](#issues-and-resolutions-3-0-2)Issues and Resolutions

#### [](#fixed-issues)Fixed Issues

#### [](#known-issues-4)Known Issues

None in this release

## [](#major)3.0.15 — February 2022

_Quick Links_

[New Features](#new-features-3-0-0) **|** [Enhancements](#improvements-3-0-0) **|** [API Changes](#lbl-api-changes) **|** [Known Issues](#lbl-know-issues-this-release) **|** [Fixed Issues](#lbl-fixed-this-release) **|** [Deprecated in this Release](#lbl-deprecated-this-release) **|** [Removed in this Release](#lbl-removed-this-release) **|** [Support Notices](#lbl-support-notices) **|** 

> [!IMPORTANT]
> On upgrading from a 2.x release, all Couchbase Lite databases will be automatically re-indexed on initial database open.  
> This can result in a delay before the database is usable.

### [](#new-features-3-0-0)New Features

#### [](#sqln1ql-query-strings)SQL++/N1QL Query Strings

Couchbase Lite's SQL++ for Mobile query API vastly simplifies the integration of Couchbase Lite within hybrid/cross platform apps.

N1QL for Mobile is an implementation of the emerging SQL-for-JSON query language specification (SQL++). It provides native, hybrid and cross-platform mobile app developers with a consistent, convenient and flexible interface to query JSON documents within the embedded database using a SQL-based syntax. This means developers can reuse queries across platforms, reducing development, testing and maintenance costs.

Read More . . . [SQL++ for Mobile](query-n1ql-mobile.md)

### [](#improvements-3-0-0)Enhancements

#### [](#auto-purge-on-channel-access-revocation)Auto-purge on Channel Access Revocation

An auto-purge feature is introduced for loss of access to channels and the documents in them. This is important for enforcement of data governance and data retention policies.

Channels are the fundamental mechanism for enforcement of access control using Sync Gateway. They guarantee that only users with access to a specific channel can access documents in that channel.

When a user loses access to a channel (_and so to its documents_) Couchbase Lite clients will auto purge all local documents on devices that belong to the revoked channel (during Pull or PushAndPull replication), unless the user has access to the document via some other channel.

Read More . . . [Auto-purge on Channel Access Revocation](replication.md#anchor-auto-purge-on-revoke)

#### [](#document-api-support-for-json-data)Document API Support for JSON Data

The Couchbase Lite API now offers out-of-the box support for document data in JSON format. This will make it easier for developers' applications to store, transform and manipulate JSON data in the database.

The API offers JSON support for Documents, MutableDocuments, Arrays, MutableArrays, Dictionaries, MutableDictionaries and Query Results.

Read More . . . [Documents](document.md) | [Blobs](blob.md)

#### [](#replicator-change-listeners)Replicator Change Listeners

The API is enhanced to allow replicator listeners to be added at any point without requiring a replicator restart.

### [](#other-enhancements)Other Enhancements

* [CBL-2635](https://issues.couchbase.com//browse/CBL-2635) — [Update support level and message note of Database'saveBlob() and getBlob() API](https://issues.couchbase.com//browse/CBL-2635)
* [CBL-2628](https://issues.couchbase.com//browse/CBL-2628) — [Change away from using SELECT when open socket](https://issues.couchbase.com//browse/CBL-2628)
* [CBL-2482](https://issues.couchbase.com//browse/CBL-2482) — [Change database.createQuery(String query) signature to throw CouchbaseLiteException](https://issues.couchbase.com//browse/CBL-2482)
* [CBL-2456](https://issues.couchbase.com//browse/CBL-2456) — [Update Database's createQuery() to return an error or throw CouchbaseLiteException (Beta 3)](https://issues.couchbase.com//browse/CBL-2456)
* [CBL-2438](https://issues.couchbase.com//browse/CBL-2438) — [Add note about notification when disabling autoPurge](https://issues.couchbase.com//browse/CBL-2438)
* [CBL-2408](https://issues.couchbase.com//browse/CBL-2408) — [Add kFLUndefinedValue constant in Fleece.h](https://issues.couchbase.com//browse/CBL-2408)
* [CBL-2383](https://issues.couchbase.com//browse/CBL-2383) — [Increase kOtherDBCloseTimeoutSecs to allow enough time for all db open connections to be closed](https://issues.couchbase.com//browse/CBL-2383)
* [CBL-2379](https://issues.couchbase.com//browse/CBL-2379) — [Improve logging message when copying database using a wrong encryption key](https://issues.couchbase.com//browse/CBL-2379)
* [CBL-2377](https://issues.couchbase.com//browse/CBL-2377) — [Provide note about copying encrypted database in API doc](https://issues.couchbase.com//browse/CBL-2377)
* [CBL-2358](https://issues.couchbase.com//browse/CBL-2358) — [Add function for creating FLMutableDict/Array from JSON](https://issues.couchbase.com//browse/CBL-2358)
* [CBL-2319](https://issues.couchbase.com//browse/CBL-2319) — [Confusing copyDatabase API when used with encryptionKey](https://issues.couchbase.com//browse/CBL-2319)
* [CBL-2292](https://issues.couchbase.com//browse/CBL-2292) — [Update mobile n1ql test suite](https://issues.couchbase.com//browse/CBL-2292)
* [CBL-2064](https://issues.couchbase.com//browse/CBL-2064) — [Implement Encrypted Property Feature](https://issues.couchbase.com//browse/CBL-2064)
* [CBL-1954](https://issues.couchbase.com//browse/CBL-1954) — [Use POSIX Error Codes](https://issues.couchbase.com//browse/CBL-1954)
* [CBL-1941](https://issues.couchbase.com//browse/CBL-1941) — [maxRetries should now count attempts instead of retries](https://issues.couchbase.com//browse/CBL-1941)
* [CBL-1935](https://issues.couchbase.com//browse/CBL-1935) — [Remove Deprecated LiteCore Methods](https://issues.couchbase.com//browse/CBL-1935)
* [CBL-1905](https://issues.couchbase.com//browse/CBL-1905) — [Passing in progress level via configuration is deprecated; use the setProgressLevel API](https://issues.couchbase.com//browse/CBL-1905)
* [CBL-1865](https://issues.couchbase.com//browse/CBL-1865) — [Enhanced Configuration API](https://issues.couchbase.com//browse/CBL-1865)
* [CBL-1854](https://issues.couchbase.com//browse/CBL-1854) — [Update SQL++ API Spec](https://issues.couchbase.com//browse/CBL-1854)
* [CBL-1793](https://issues.couchbase.com//browse/CBL-1793) — [Change to QueryBuilder API](https://issues.couchbase.com//browse/CBL-1793)
* [CBL-1790](https://issues.couchbase.com//browse/CBL-1790) — [CBL - Create Query with SQL++ String](https://issues.couchbase.com//browse/CBL-1790)
* [CBL-1786](https://issues.couchbase.com//browse/CBL-1786) — [Ignore unknown-warning-option warning from clang](https://issues.couchbase.com//browse/CBL-1786)
* [CBL-1781](https://issues.couchbase.com//browse/CBL-1781) — [API : Revise ReplicatorProgress API](https://issues.couchbase.com//browse/CBL-1781)
* [CBL-1763](https://issues.couchbase.com//browse/CBL-1763) — [kErrTruncatedJSON is returning kFLNoError](https://issues.couchbase.com//browse/CBL-1763)
* [CBL-1761](https://issues.couchbase.com//browse/CBL-1761) — [Updating CBL .Net Core 3.1 PR Validation and Jenkins job](https://issues.couchbase.com//browse/CBL-1761)
* [CBL-1757](https://issues.couchbase.com//browse/CBL-1757) — [CBL SQL++ Functionality](https://issues.couchbase.com//browse/CBL-1757)
* [CBL-1744](https://issues.couchbase.com//browse/CBL-1744) — [Fix Fire Timer at Same Time Test](https://issues.couchbase.com//browse/CBL-1744)
* [CBL-1716](https://issues.couchbase.com//browse/CBL-1716) — [Update CBL .Net Core to .Net Core 3.1 (Local)](https://issues.couchbase.com//browse/CBL-1716)
* [CBL-1714](https://issues.couchbase.com//browse/CBL-1714) — [Refactor POSIX error domain codes to be platform independent](https://issues.couchbase.com//browse/CBL-1714)
* [CBL-1711](https://issues.couchbase.com//browse/CBL-1711) — [API: Add MaintenanceType for Query Optimization](https://issues.couchbase.com//browse/CBL-1711)
* [CBL-1692](https://issues.couchbase.com//browse/CBL-1692) — [Add UWP PR validation Part 2 (build everything from source and make a GitHub action)](https://issues.couchbase.com//browse/CBL-1692)
* [CBL-1666](https://issues.couchbase.com//browse/CBL-1666) — [Allow apps to trigger SQLite index optimization directly](https://issues.couchbase.com//browse/CBL-1666)
* [CBL-1650](https://issues.couchbase.com//browse/CBL-1650) — [CBL doesn't purge channel removals when removal revision already exists in CBL](https://issues.couchbase.com//browse/CBL-1650)
* [CBL-1584](https://issues.couchbase.com//browse/CBL-1584) — [Replicator Retry Logic](https://issues.couchbase.com//browse/CBL-1584)
* [CBL-1583](https://issues.couchbase.com//browse/CBL-1583) — [JSON Results](https://issues.couchbase.com//browse/CBL-1583)
* [CBL-1582](https://issues.couchbase.com//browse/CBL-1582) — [Configurable Replicator Level](https://issues.couchbase.com//browse/CBL-1582)
* [CBL-1581](https://issues.couchbase.com//browse/CBL-1581) — [Reserve Property Keys](https://issues.couchbase.com//browse/CBL-1581)
* [CBL-1565](https://issues.couchbase.com//browse/CBL-1565) — [Ensure c4log\_enableFatalExceptionBacktrace is called](https://issues.couchbase.com//browse/CBL-1565)
* [CBL-1522](https://issues.couchbase.com//browse/CBL-1522) — [SQL++ : Add NULL OR MISSING literal](https://issues.couchbase.com//browse/CBL-1522)
* [CBL-1505](https://issues.couchbase.com//browse/CBL-1505) — [Use c4address\_fromURL](https://issues.couchbase.com//browse/CBL-1505)
* [CBL-1350](https://issues.couchbase.com//browse/CBL-1350) — [Deprecate Replicator.resetCheckpoint() API](https://issues.couchbase.com//browse/CBL-1350)
* [CBL-1311](https://issues.couchbase.com//browse/CBL-1311) — [Use Builder pattern for Configuration](https://issues.couchbase.com//browse/CBL-1311)
* [CBL-1308](https://issues.couchbase.com//browse/CBL-1308) — [Allow to remove query listener or any listeners directly from token](https://issues.couchbase.com//browse/CBL-1308)
* [CBL-1232](https://issues.couchbase.com//browse/CBL-1232) — [Support function to change the kC4ReplicatorOptionProgressLevel](https://issues.couchbase.com//browse/CBL-1232)
* [CBL-1118](https://issues.couchbase.com//browse/CBL-1118) — [Update SimpleInjector to version 5 and edit nuspec to restrict it's version < 6](https://issues.couchbase.com//browse/CBL-1118)
* [CBL-1049](https://issues.couchbase.com//browse/CBL-1049) — [Zero fleece options when replicator is freed](https://issues.couchbase.com//browse/CBL-1049)
* [CBL-911](https://issues.couchbase.com//browse/CBL-911) — [Couchbase Lite Java replication hangs when using DEBUG console + file logging on Windows](https://issues.couchbase.com//browse/CBL-911)
* [CBL-790](https://issues.couchbase.com//browse/CBL-790) — [API: Fix database directory setup](https://issues.couchbase.com//browse/CBL-790)
* [CBL-718](https://issues.couchbase.com//browse/CBL-718) — [API: Arg to Database.inBatch should be able to throw](https://issues.couchbase.com//browse/CBL-718)
* [CBL-680](https://issues.couchbase.com//browse/CBL-680) — [Public API for SQL++ array\_agg() aggregation function](https://issues.couchbase.com//browse/CBL-680)

### [](#lbl-api-changes)API Changes

This content introduces the changes made to the Couchbase Lite for C#.Net API for release 3.0.15.

Starting from this release Couchbase Lite for C#.Net requires _Visual Studio 2019+_ and uses .Net Core 3.1 (updating from .Net Core 2.0).

#### [](#breaking-change)Breaking Change

The function [ATAN2(x, y)](https://docs.couchbase.com/mobile/2.8.0/couchbase-lite-net/api/Couchbase.Lite.Query.Function.html#Couchbase%5FLite%5FQuery%5FFunction%5FAtan2%5FCouchbase%5FLite%5FQuery%5FIExpression%5FCouchbase%5FLite%5FQuery%5FIExpression%5F), which returns the principal value of the arc tangent of y/x, now becomes [ATAN2(y, x)](https://docs.couchbase.com/mobile/3.0.15/couchbase-lite-net/api/Couchbase.Lite.Query.Function.html#Couchbase%5FLite%5FQuery%5FFunction%5FAtan2%5FCouchbase%5FLite%5FQuery%5FIExpression%5FCouchbase%5FLite%5FQuery%5FIExpression%5F); that is, the arguments are reversed in line with common notation.

#### [](#removed)Removed

##### [](#activate)Activate

We have removed the method `Activate()` from **all** platform support libraries **except** `Support.Android` (Xamarin Android)

##### [](#enabletextlogging)EnableTextLogging()

We have removed the obsolete method `EnableTextLogging()` from all the platform support libraries.

##### [](#resetcheckpoint)ResetCheckpoint

The method [ResetCheckpoint()](https://docs.couchbase.com/mobile/2.8.0/couchbase-lite-net/api/Couchbase.Lite.Sync.Replicator.html#Couchbase%5FLite%5FSync%5FReplicator%5FResetCheckpoint)has been removed. Use the `reset:` argument when starting the replicator instead.

###### [](#before)Before

```java
replicator.ResetCheckpoint();
replicator.Start();
```

###### [](#after)After

```java
replicator.Start(true) (1)
```

| **1** | Set the reset: argument true to initiate a replicator checkpoint reset |
| ----- | ---------------------------------------------------------------------- |

##### [](#setloglevel)SetLogLevel()

We have removed the method [Database.setLogLevel()](https://docs.couchbase.com/mobile/2.8.0/couchbase-lite-net/api/Couchbase.Lite.Database.html#Couchbase%5FLite%5FDatabase%5FSetLogLevel%5FCouchbase%5FLite%5FLogging%5FLogDomain%5FCouchbase%5FLite%5FLogging%5FLogLevel%5F)  
Use [Database.log.console](https://docs.couchbase.com/mobile/3.0.15/couchbase-lite-net/api/Couchbase.Lite.Logging.Log.html#Couchbase%5FLite%5FLogging%5FLog%5FConsole)instead:

###### [](#before-2)Before

```java
Database.SetLogLevel(LogDomain.Replicator, LogLevel.Verbose);
Database.SetLogLevel(LogDomain.Query, LogLevel.Verbose);
```

###### [](#after-2)After

```java
Database.Log.Console.Domains = LogDomain.All;
Database.Log.Console.LogLevel = LogLevel.Verbose;
```

#### [](#database-compact)Database.Compact

We have removed the method [Database.compact()](https://docs.couchbase.com/mobile/2.8.0/couchbase-lite-net/api/Couchbase.Lite.Database.html#Couchbase%5FLite%5FDatabase%5FCompact).  
Use the method [Database.PerformMaintenance()](https://docs.couchbase.com/mobile/3.0.15/couchbase-lite-net/api/Couchbase.Lite.Database.html#Couchbase%5FLite%5FDatabase%5FPerformMaintenance%5FCouchbase%5FLite%5FMaintenanceType%5F) and the enum [MaintenanceType](https://docs.couchbase.com/mobile/3.0.15/couchbase-lite-net/api/Couchbase.Lite.MaintenanceType.html)instead

###### [](#before-3)Before

```java
var db = new Database("thisdb");
db.Compact()
```

###### [](#after-3)After

```java
var db = new Database("thisdb");

db.PerformMaintenance(MaintenanceType.Compact)
```

#### [](#deprecated-api)Deprecated API

##### [](#match)Match

We will remove [Match](https://docs.couchbase.com/mobile/2.8.0/couchbase-lite-net/api/Couchbase.Lite.Query.IFullTextExpression.html#Couchbase%5FLite%5FQuery%5FIFullTextExpression%5FMatch%5FSystem%5FString%5F)at the next major release.  
You should plan to switch to using the alternative [FullTextFunction.match(indexName:)](https://docs.couchbase.com/mobile/3.0.15/couchbase-lite-net/api/Couchbase.Lite.Query.FullTextFunction.html#Couchbase%5FLite%5FQuery%5FFullTextFunction%5FMatch%5FSystem%5FString%5FSystem%5FString%5F)at the earliest opportunity.

###### [](#before-4)Before

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

###### [](#after-4)After

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

| **1** | Here we use [FullTextFunction.match(indexName:)](https://docs.couchbase.com/mobile/3.0.15/couchbase-lite-net/api/Couchbase.Lite.Query.FullTextFunction.htmlFullTextFunction.match%28indexName:%29)to build the query |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

##### [](#isnullormissing)IsNullOrMissing

We will remove [isNullOrMissing](https://docs.couchbase.com/mobile/2.8.0/couchbase-lite-net/api/Couchbase.Lite.Query.IExpression.html#Couchbase%5FLite%5FQuery%5FIExpression%5FIsNullOrMissing)  
You should plan to switch to using the alternative [IsNotValued()](https://docs.couchbase.com/mobile/3.0.15/couchbase-lite-net/api/Couchbase.Lite.Query.IExpression.html#Couchbase%5FLite%5FQuery%5FIExpression%5FIsNotValued)

at the earliest opportunity.

###### [](#before-5)Before

```java
var query = QueryBuilder.Select(SelectResult.All())
    .From(DataSource.Database(db))
    .Where(Expression.Property("missingprop").IsNullOrMissing())
```

###### [](#after-5)After

```java
var query = QueryBuilder.Select(SelectResult.All())
    .From(DataSource.Database(db))
    .Where(Expression.Property("missingprop").IsNotValued())
```

##### [](#notnullormissing)NotNullOrMissing

We will remove [notNullOrMissing](https://docs.couchbase.com/mobile/2.8.0/couchbase-lite-net/api/Couchbase.Lite.Query.IExpression.html#Couchbase%5FLite%5FQuery%5FIExpression%5FNotNullOrMissing).  
You should plan to switch to using the alternative [isValued()](https://docs.couchbase.com/mobile/3.0.15/couchbase-lite-net/api/Couchbase.Lite.Query.IExpression.html#Couchbase%5FLite%5FQuery%5FIExpression%5FIsValued)at the earliest opportunity.

| isNotValued()

###### [](#before-6)Before

```java
var query = QueryBuilder.Select(SelectResult.All())
    .From(DataSource.Database(db))
    .Where(Expression.Property("notmissingprop").NotNullOrMissing())
```

###### [](#after-6)After

```java
var query = QueryBuilder.Select(SelectResult.All())
    .From(DataSource.Database(db))
    .Where(Expression.Property("notmissingprop").IsValued())
```

### [](#lbl-know-issues-this-release)Known Issues

None for this release.

### [](#lbl-fixed-this-release)Fixed Issues

* [CBL-2583](https://issues.couchbase.com//browse/CBL-2583) — [Replication unable to continue after termination between rev and ack](https://issues.couchbase.com//browse/CBL-2583)
* [CBL-2579](https://issues.couchbase.com//browse/CBL-2579) — [409 retry can result in invalid remote ancestor ID](https://issues.couchbase.com//browse/CBL-2579)
* [CBL-2512](https://issues.couchbase.com//browse/CBL-2512) — [Replicator won't stop](https://issues.couchbase.com//browse/CBL-2512)
* [CBL-2478](https://issues.couchbase.com//browse/CBL-2478) — [Tear down DBAccess on stopped instead of on release](https://issues.couchbase.com//browse/CBL-2478)
* [CBL-2405](https://issues.couchbase.com//browse/CBL-2405) — [Hung in call to c4socket\_closed](https://issues.couchbase.com//browse/CBL-2405)
* [CBL-2325](https://issues.couchbase.com//browse/CBL-2325) — [REST \_replicate throws errro](https://issues.couchbase.com//browse/CBL-2325)
* [CBL-2313](https://issues.couchbase.com//browse/CBL-2313) — [HTTPS test fails](https://issues.couchbase.com//browse/CBL-2313)
* [CBL-2304](https://issues.couchbase.com//browse/CBL-2304) — [CBL core fleece exception: incompatible duplicate scope](https://issues.couchbase.com//browse/CBL-2304)
* [CBL-2243](https://issues.couchbase.com//browse/CBL-2243) — [memory leak, couchbase-lite-core issue#1221](https://issues.couchbase.com//browse/CBL-2243)
* [CBL-2212](https://issues.couchbase.com//browse/CBL-2212) — [Exception can leak out of C4](https://issues.couchbase.com//browse/CBL-2212)
* [CBL-2210](https://issues.couchbase.com//browse/CBL-2210) — [RESTListener synchronous response may hang](https://issues.couchbase.com//browse/CBL-2210)
* [CBL-2208](https://issues.couchbase.com//browse/CBL-2208) — [REST API \_replicate lacks authentication](https://issues.couchbase.com//browse/CBL-2208)
* [CBL-2191](https://issues.couchbase.com//browse/CBL-2191) — [kHasAttachments flag may be lost in Conflict Resolver](https://issues.couchbase.com//browse/CBL-2191)
* [CBL-2182](https://issues.couchbase.com//browse/CBL-2182) — [Crash in assertion](https://issues.couchbase.com//browse/CBL-2182)
* [CBL-2102](https://issues.couchbase.com//browse/CBL-2102) — [Memory leak when calling MutableArrayObject.AddBlob](https://issues.couchbase.com//browse/CBL-2102)
* [CBL-2094](https://issues.couchbase.com//browse/CBL-2094) — [Fix memory leak in WebSocketWrapper](https://issues.couchbase.com//browse/CBL-2094)
* [CBL-1977](https://issues.couchbase.com//browse/CBL-1977) — [SetPrivateKey failed in .Net Framework ](https://issues.couchbase.com//browse/CBL-1977)
* [CBL-1722](https://issues.couchbase.com//browse/CBL-1722) — [POSIX 32 (Broken Pipe) appears to crash application](https://issues.couchbase.com//browse/CBL-1722)
* [CBL-1660](https://issues.couchbase.com//browse/CBL-1660) — [Not all debug logging is compiled out of release builds](https://issues.couchbase.com//browse/CBL-1660)
* [CBL-1438](https://issues.couchbase.com//browse/CBL-1438) — [WSA codes not properly handled by bio\_return\_value](https://issues.couchbase.com//browse/CBL-1438)
* [CBL-1354](https://issues.couchbase.com//browse/CBL-1354) — [finding euclidean distance, square euclidean distance rounding the precision value ](https://issues.couchbase.com//browse/CBL-1354)
* [CBL-1310](https://issues.couchbase.com//browse/CBL-1310) — [app crashing while fetching the prediction query result](https://issues.couchbase.com//browse/CBL-1310)
* [CBL-1225](https://issues.couchbase.com//browse/CBL-1225) — [Testfest : unshare the docs does not replicate to CBL](https://issues.couchbase.com//browse/CBL-1225)
* [CBL-862](https://issues.couchbase.com//browse/CBL-862) — [CBL 2.7 and later doesn't catch Illegal top-level key like "\_id"](https://issues.couchbase.com//browse/CBL-862)
* [CBL-708](https://issues.couchbase.com//browse/CBL-708) — [Conflicting revision bodies are not removed after resolution](https://issues.couchbase.com//browse/CBL-708)
* [CBL-462](https://issues.couchbase.com//browse/CBL-462) — [Continuous push attempts to replicate purged documents](https://issues.couchbase.com//browse/CBL-462)
* [CBL-220](https://issues.couchbase.com//browse/CBL-220) — [Windows cannot handle dates before 1970 with C API](https://issues.couchbase.com//browse/CBL-220)
* [CBL-49](https://issues.couchbase.com//browse/CBL-49) — [Need a way to distinguish boolean types](https://issues.couchbase.com//browse/CBL-49)

### [](#lbl-deprecated-this-release)Deprecated in this Release

Items (features and-or functionality) are marked as deprecated when a more current, and usually enhanced, alternative is available.

Whilst the deprecated item will remain usable, it is no longer supported, and will be removed in a future release — see also: [Removed in this Release](#lbl-removed-this-release)You should plan to move to an alternative, supported, solution as soon as practical.

None for this release.

* The \[Database.Compact()\] method is deprecated (as of 2.8), instead use [Database.PerformMaintenance()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-net/api/Couchbase.Lite.Database.html#Couchbase%5FLite%5FDatabase%5FPerformMaintenance-com.couchbase.lite.MaintenanceType-).

#### [](#previously-deprecated)Previously Deprecated

None specified

### [](#lbl-removed-this-release)Removed in this Release

* [CBL-1350](https://issues.couchbase.com//browse/CBL-1350) — [Deprecate Replicator.resetCheckpoint() API](https://issues.couchbase.com//browse/CBL-1350)

### [](#lbl-support-notices)Support Notices

This section documents any support-related notes, constraints and changes.

#### [](#new)New

None specified in this release

#### [](#ongoing)Ongoing

None specified

## [](#related-content)Related Content

###### [](#)

Product Notes

* [Release Notes](releasenotes.md)
* [Compatibility](compatibility.md)
* [Supported Platforms](supported-os.md)
* [What's New](#cbl-whatsnew.adoc)

###### [](#-2)

Starting Points

* [Databases](database.md)
* [Documents](document.md)
* [Blobs](blob.md)
* [Remote Sync Gateway](replication.md)
* [Handling Data Conflicts](conflict.md)

###### [](#-3)

Tutorials

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)