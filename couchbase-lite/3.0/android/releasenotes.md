---
title: Release Notes
description: Couchbase Lite on Android
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.0/modules/android/pages/releasenotes.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:3.0@couchbase-lite:android:releasenotes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.0/android/releasenotes.html)

# Release Notes

## [](#maint-3-0-15)3.0.15 — November 2023

Version 3.0.15 for Android delivers the following features and enhancements:

### [](#enhancements)Enhancements

* [CBL-3643: Upgrade to ICU 69+](https://issues.couchbase.com/browse/CBL-3643)

### [](#issues-and-resolutions)Issues and Resolutions

* [CBL-4922: Fix issue in in OkHttp authenticator](https://issues.couchbase.com/browse/CBL-4922)
* [CBL-4921: Lower the max size on the ClientTask thread pool to 8](https://issues.couchbase.com/browse/CBL-4921)
* [CBL-4839: Fix issue with deletion of Attachments/Blobs after compaction &re-sync](https://issues.couchbase.com/browse/CBL-4839)
* [CBL-4799: Database.exists now supports the default directory](https://issues.couchbase.com/browse/CBL-4799)
* [CBL-4139: fix build error on Linux](https://issues.couchbase.com/browse/CBL-4139)
* [CBL-3871: fix QueryParams decoding bool](https://issues.couchbase.com/browse/CBL-3871)

### [](#known-issues)Known Issues

None for this release

### [](#deprecations)Deprecations

None for this release

## [](#maint-3-0-12)3.0.12 — June 2023

Version 3.0.12 for Android delivers the following features and enhancements:

### [](#enhancements-2)Enhancements

* [CBL-4531 - Update PublicKey+Apple to use non deprecated keychain APIs](https://issues.couchbase.com/browse/CBL-4531)
* [CBL-4167 - SQL++ : COLLATE does not have a way to specify locale for UNICODE](https://issues.couchbase.com/browse/CBL-4167)
* [CBL-4024 - Change BuiltInWebSocket to do preemptive auth instead of challenge auth by default (Port)](https://issues.couchbase.com/browse/CBL-4024)
* [CBL-3903 - Assertion failure when stopping replicator while replicator is connecting](https://issues.couchbase.com/browse/CBL-3903)
* [CBL-4134 - Fix empty identity error when building LiteCoreCppTests&C4Tests using XCode 14](https://issues.couchbase.com/browse/CBL-4134)
* [CBL-3993 - FTS index table not have to be qualified by data source alias in query](https://issues.couchbase.com/browse/CBL-3993)

### [](#issues-and-resolutions-2)Issues and Resolutions

* [CBL-3671 - Fix slowdowns and storage overhead caused by document revision history not being pruned](https://issues.couchbase.com/browse/CBL-3671)
* [CBL-4529 - Error when saving documents with LiteCore error 17: must be called during a transaction](https://issues.couchbase.com/browse/CBL-4529)
* [CBL-4528 - Query parameters not being bound](https://issues.couchbase.com/browse/CBL-4528)
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

## [](#maint-3-0-5)3.0.5 — November 2022

Version 3.0.5 for Android delivers the following features and enhancements:

### [](#enhancements-3)Enhancements

None for this release.

### [](#issues-and-resolutions-3)Issues and Resolutions

* [CBL-3807 — Server Certificate can disappear during authentication](https://issues.couchbase.com/browse/CBL-3807)
* [CBL-3738 — \[Lithium\] Multiple network failures can cause exception: android.net.ConnectivityManager$TooManyRequestsException: null](https://issues.couchbase.com/browse/CBL-3738)
* [CBL-3716 — ArrayIndexOutOfBoundsException in the AbstractDatabase.postDatabaseChanged](https://issues.couchbase.com/browse/CBL-3716)
* [CBL-3420 — ReplicatorConfigurationFactory.create() defaults enabledAutoPurge to false](https://issues.couchbase.com/browse/CBL-3420)

### [](#known-issues-3)Known Issues

None for this release.

## [](#maint-3-0-2)3.0.2 — August 2022

Version 3.0.2 of Couchbase Lite for Android delivers a number of fixes and enhancements.

### [](#enhancements-4)Enhancements

* [CBL-3361](https://issues.couchbase.com/browse/CBL-3361) — [As of Kotlin 1.6, Coroutines are no longer experimental](https://issues.couchbase.com/browse/CBL-3361)
* [CBL-3274](https://issues.couchbase.com/browse/CBL-3274) — [Expose the IndexConfiguration class](https://issues.couchbase.com/browse/CBL-3274)
* [CBL-3084](https://issues.couchbase.com/browse/CBL-3084) — [Make SSLException a recoverable error in AbstractCBLWebSocket](https://issues.couchbase.com/browse/CBL-3084)
* [CBL-2999](https://issues.couchbase.com/browse/CBL-2999) — [Implement enhanced pinned server certificate feature](https://issues.couchbase.com/browse/CBL-2999)

### [](#issues-and-resolutions-3-0-2)Issues and Resolutions

#### [](#fixed-issues)Fixed Issues

* [CBL-3301](https://issues.couchbase.com/browse/CBL-3301) — [FullTextIndex.setLanguage() should accept null parameter](https://issues.couchbase.com/browse/CBL-3301)
* [CBL-3299](https://issues.couchbase.com/browse/CBL-3299) — [Fix NPE in finalizer](https://issues.couchbase.com/browse/CBL-3299)
* [CBL-3224](https://issues.couchbase.com/browse/CBL-3224) — [Call to c4socket\_closed causes native crash](https://issues.couchbase.com/browse/CBL-3224)
* [CBL-3136](https://issues.couchbase.com/browse/CBL-3136) — [Malformed hostname can cause a crash](https://issues.couchbase.com/browse/CBL-3136)
* [CBL-3092](https://issues.couchbase.com/browse/CBL-3092) — [BLIPConnection.hh related crash](https://issues.couchbase.com/browse/CBL-3092)
* [CBL-3090](https://issues.couchbase.com/browse/CBL-3090) — [Push large database test could fail](https://issues.couchbase.com/browse/CBL-3090)
* [CBL-3074](https://issues.couchbase.com/browse/CBL-3074) — [Database could be corrupted after being copied in linux platform](https://issues.couchbase.com/browse/CBL-3074)
* [CBL-3000](https://issues.couchbase.com/browse/CBL-3000) — [c4DbChanges in AbstractDatabase.postDatabaseChanged may contain nulls](https://issues.couchbase.com/browse/CBL-3000)
* [CBL-2998](https://issues.couchbase.com/browse/CBL-2998) — [Replicator stopped with WebSocket 1008 / SocketTimeoutException when disable Wi-Fi](https://issues.couchbase.com/browse/CBL-2998)
* [CBL-2996](https://issues.couchbase.com/browse/CBL-2996) — [Several bad tests in ReplicatorLocal2LocalTest suite](https://issues.couchbase.com/browse/CBL-2996)
* [CBL-2995](https://issues.couchbase.com/browse/CBL-2995) — [Cookies set in Headers are replaced with Session Authenticator’s cookies](https://issues.couchbase.com/browse/CBL-2995)
* [CBL-2962](https://issues.couchbase.com/browse/CBL-2962) — [URLEndpointListenerTest fixes](https://issues.couchbase.com/browse/CBL-2962)
* [CBL-2884](https://issues.couchbase.com/browse/CBL-2884) — [evpos is missing in the changed attachment body when using delta sync](https://issues.couchbase.com/browse/CBL-2884)

#### [](#known-issues-4)Known Issues

None in this release

## [](#major)3.0.15 — February 2022

_Quick Links_

[New Features](#new-features-3-0-0) **|** [Enhancements](#improvements-3-0-0) **|** [API Changes](#lbl-api-changes) **|** [Known Issues](#lbl-know-issues-this-release) **|** [Fixed Issues](#lbl-fixed-this-release) **|** [Deprecated in this Release](#lbl-deprecated-this-release) **|** [Removed in this Release](#lbl-removed-this-release) **|** [Support Notices](#lbl-support-notices) **|** 

> [!IMPORTANT]
> On upgrading from a 2.x release, all Couchbase Lite databases will be automatically re-indexed on initial database open.  
> This can result in a delay before the database is usable.

### [](#new-features-3-0-0)New Features

#### [](#kotlin-support-in-android)Kotlin Support in Android

_Couchbase Lite for Android_ delivers an idiomatic Kotlin API out-of-the-box. This enables seamless integration with Android apps developed in Kotlin without the need for custom extensions.

Kotlin developers can now build apps using [common Kotlin Patterns](https://developer.android.com/kotlin/common-patterns) and use familiar Kotlin features such as:

* Nullability annotations
* Named parameters
* Kotlin Flows

Java support and functionality continues for Android. You can choose whether to use the Kotlin extensions API or continue using the Java api.

Read More . . . [Couchbase Lite for Kotlin](kotlin.md)

#### [](#sqln1ql-query-strings)SQL++/N1QL Query Strings

Couchbase Lite’s SQL++ for Mobile query API vastly simplifies the integration of Couchbase Lite within hybrid/cross platform apps.

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

* [CBL-2645](https://issues.couchbase.com//browse/CBL-2645) — [Update Lithium to RC-1 LiteCore](https://issues.couchbase.com//browse/CBL-2645)
* [CBL-2634](https://issues.couchbase.com//browse/CBL-2634) — [Update support level and message note of Database’saveBlob() and getBlob() API](https://issues.couchbase.com//browse/CBL-2634)
* [CBL-2630](https://issues.couchbase.com//browse/CBL-2630) — [Update to latest LiteCore](https://issues.couchbase.com//browse/CBL-2630)
* [CBL-2628](https://issues.couchbase.com//browse/CBL-2628) — [Change away from using SELECT when open socket](https://issues.couchbase.com//browse/CBL-2628)
* [CBL-2551](https://issues.couchbase.com//browse/CBL-2551) — [Include description of error codes](https://issues.couchbase.com//browse/CBL-2551)
* [CBL-2481](https://issues.couchbase.com//browse/CBL-2481) — [Change database.createQuery(String query) signature to throw CouchbaseLiteException](https://issues.couchbase.com//browse/CBL-2481)
* [CBL-2456](https://issues.couchbase.com//browse/CBL-2456) — [Update Database’s createQuery() to return an error or throw CouchbaseLiteException (Beta 3)](https://issues.couchbase.com//browse/CBL-2456)
* [CBL-2439](https://issues.couchbase.com//browse/CBL-2439) — [Add note about notification when disabling autoPurge](https://issues.couchbase.com//browse/CBL-2439)
* [CBL-2408](https://issues.couchbase.com//browse/CBL-2408) — [Add kFLUndefinedValue constant in Fleece.h](https://issues.couchbase.com//browse/CBL-2408)
* [CBL-2383](https://issues.couchbase.com//browse/CBL-2383) — [Increase kOtherDBCloseTimeoutSecs to allow enough time for all db open connections to be closed](https://issues.couchbase.com//browse/CBL-2383)
* [CBL-2379](https://issues.couchbase.com//browse/CBL-2379) — [Improve logging message when copying database using a wrong encryption key](https://issues.couchbase.com//browse/CBL-2379)
* [CBL-2358](https://issues.couchbase.com//browse/CBL-2358) — [Add function for creating FLMutableDict/Array from JSON](https://issues.couchbase.com//browse/CBL-2358)
* [CBL-2319](https://issues.couchbase.com//browse/CBL-2319) — [Confusing copyDatabase API when used with encryptionKey](https://issues.couchbase.com//browse/CBL-2319)
* [CBL-2292](https://issues.couchbase.com//browse/CBL-2292) — [Update mobile n1ql test suite](https://issues.couchbase.com//browse/CBL-2292)
* [CBL-2099](https://issues.couchbase.com//browse/CBL-2099) — [Add Kotlin Flowables](https://issues.couchbase.com//browse/CBL-2099)
* [CBL-2064](https://issues.couchbase.com//browse/CBL-2064) — [Implement Encrypted Property Feature](https://issues.couchbase.com//browse/CBL-2064)
* [CBL-2040](https://issues.couchbase.com//browse/CBL-2040) — [Change QueryBuilder’s ATAN2(X, Y) to ATAN2(Y, X)](https://issues.couchbase.com//browse/CBL-2040)
* [CBL-2006](https://issues.couchbase.com//browse/CBL-2006) — [Annotate methods and returns for nullability](https://issues.couchbase.com//browse/CBL-2006)
* [CBL-1979](https://issues.couchbase.com//browse/CBL-1979) — [Support Android v30](https://issues.couchbase.com//browse/CBL-1979)
* [CBL-1948](https://issues.couchbase.com//browse/CBL-1948) — [Make objects with native companions AutoClosable](https://issues.couchbase.com//browse/CBL-1948)
* [CBL-1941](https://issues.couchbase.com//browse/CBL-1941) — [maxRetries should now count attempts instead of retries](https://issues.couchbase.com//browse/CBL-1941)
* [CBL-1935](https://issues.couchbase.com//browse/CBL-1935) — [Remove Deprecated LiteCore Methods](https://issues.couchbase.com//browse/CBL-1935)
* [CBL-1873](https://issues.couchbase.com//browse/CBL-1873) — [Enhanced Configuration API](https://issues.couchbase.com//browse/CBL-1873)
* [CBL-1854](https://issues.couchbase.com//browse/CBL-1854) — [Update SQL++ API Spec](https://issues.couchbase.com//browse/CBL-1854)
* [CBL-1792](https://issues.couchbase.com//browse/CBL-1792) — [Implement SQL++ Query API](https://issues.couchbase.com//browse/CBL-1792)
* [CBL-1789](https://issues.couchbase.com//browse/CBL-1789) — [CBL - Create Query with SQL++ String](https://issues.couchbase.com//browse/CBL-1789)
* [CBL-1786](https://issues.couchbase.com//browse/CBL-1786) — [Ignore unknown-warning-option warning from clang](https://issues.couchbase.com//browse/CBL-1786)
* [CBL-1781](https://issues.couchbase.com//browse/CBL-1781) — [API : Revise ReplicatorProgress API](https://issues.couchbase.com//browse/CBL-1781)
* [CBL-1763](https://issues.couchbase.com//browse/CBL-1763) — [kErrTruncatedJSON is returning kFLNoError](https://issues.couchbase.com//browse/CBL-1763)
* [CBL-1757](https://issues.couchbase.com//browse/CBL-1757) — [CBL SQL++ Functionality](https://issues.couchbase.com//browse/CBL-1757)
* [CBL-1744](https://issues.couchbase.com//browse/CBL-1744) — [Fix Fire Timer at Same Time Test](https://issues.couchbase.com//browse/CBL-1744)
* [CBL-1714](https://issues.couchbase.com//browse/CBL-1714) — [Refactor POSIX error domain codes to be platform independent](https://issues.couchbase.com//browse/CBL-1714)
* [CBL-1711](https://issues.couchbase.com//browse/CBL-1711) — [API: Add MaintenanceType for Query Optimization](https://issues.couchbase.com//browse/CBL-1711)
* [CBL-1666](https://issues.couchbase.com//browse/CBL-1666) — [Allow apps to trigger SQLite index optimization directly](https://issues.couchbase.com//browse/CBL-1666)
* [CBL-1650](https://issues.couchbase.com//browse/CBL-1650) — [CBL doesn’t purge channel removals when removal revision already exists in CBL](https://issues.couchbase.com//browse/CBL-1650)
* [CBL-1584](https://issues.couchbase.com//browse/CBL-1584) — [Replicator Retry Logic](https://issues.couchbase.com//browse/CBL-1584)
* [CBL-1583](https://issues.couchbase.com//browse/CBL-1583) — [JSON Results](https://issues.couchbase.com//browse/CBL-1583)
* [CBL-1582](https://issues.couchbase.com//browse/CBL-1582) — [Configurable Replicator Level](https://issues.couchbase.com//browse/CBL-1582)
* [CBL-1581](https://issues.couchbase.com//browse/CBL-1581) — [Reserve Property Keys](https://issues.couchbase.com//browse/CBL-1581)
* [CBL-1522](https://issues.couchbase.com//browse/CBL-1522) — [SQL++ : Add NULL OR MISSING literal](https://issues.couchbase.com//browse/CBL-1522)
* [CBL-1359](https://issues.couchbase.com//browse/CBL-1359) — [Remove deprecated Replicator.resetCheckpoint() and de-deprecate Replicator.start()](https://issues.couchbase.com//browse/CBL-1359)
* [CBL-1358](https://issues.couchbase.com//browse/CBL-1358) — [Remove deprecated LogDomain.ALL (replaced by LogDomain.ALL\_DOMAINS)](https://issues.couchbase.com//browse/CBL-1358)
* [CBL-1357](https://issues.couchbase.com//browse/CBL-1357) — [Remove deprecated Database.compact()](https://issues.couchbase.com//browse/CBL-1357)
* [CBL-1356](https://issues.couchbase.com//browse/CBL-1356) — [Remove deprecated constructor BasicAuthenticator(String, String)](https://issues.couchbase.com//browse/CBL-1356)
* [CBL-1350](https://issues.couchbase.com//browse/CBL-1350) — [Deprecate Replicator.resetCheckpoint() API](https://issues.couchbase.com//browse/CBL-1350)
* [CBL-1311](https://issues.couchbase.com//browse/CBL-1311) — [Use Builder pattern for Configuration](https://issues.couchbase.com//browse/CBL-1311)
* [CBL-1308](https://issues.couchbase.com//browse/CBL-1308) — [Allow to remove query listener or any listeners directly from token](https://issues.couchbase.com//browse/CBL-1308)
* [CBL-1232](https://issues.couchbase.com//browse/CBL-1232) — [Support function to change the kC4ReplicatorOptionProgressLevel](https://issues.couchbase.com//browse/CBL-1232)
* [CBL-1049](https://issues.couchbase.com//browse/CBL-1049) — [Zero fleece options when replicator is freed](https://issues.couchbase.com//browse/CBL-1049)
* [CBL-1011](https://issues.couchbase.com//browse/CBL-1011) — [Remove deprecated Replicator.resetCheckpoint()](https://issues.couchbase.com//browse/CBL-1011)

### [](#lbl-api-changes)API Changes

This content introduces the changes made to the Couchbase Lite for Android API for release 3.0.15.

#### [](#removed)Removed

##### [](#resetcheckpoint)ResetCheckpoint

The method [Replicator.resetCheckpoint()](https://docs.couchbase.com/mobile/2.8.0/couchbase-lite-android/com/couchbase/lite/AbstractReplicator.html#resetCheckpoint--) has been removed.  
Instead, use [Replicator.resetCheckpoint(boolean reset)](https://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/AbstractReplicator.html#start-boolean-).

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
It is replaced by the new [Database.performMaintenance(MaintenanceType)](https://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/Database.html#performMaintenance-com.couchbase.lite.MaintenanceType-) method, and the maintenance operations represented in the enum [MaintenanceType](https://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/MaintenanceType.html)

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
Use [FullTextFunction](https://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/FullTextFunction.html) instead.

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

* [ReplicatorActivityLevel](https://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/ReplicatorActivityLevel.html)
* [ReplicatorProgress](https://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/ReplicatorProgress.html)
* [ReplicatorStatus](https://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/ReplicatorStatus.html)

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

### [](#lbl-know-issues-this-release)Known Issues

None for this release.

### [](#lbl-fixed-this-release)Fixed Issues

* [CBL-2583](https://issues.couchbase.com//browse/CBL-2583) — [Replication unable to continue after termination between rev and ack](https://issues.couchbase.com//browse/CBL-2583)
* [CBL-2579](https://issues.couchbase.com//browse/CBL-2579) — [409 retry can result in invalid remote ancestor ID](https://issues.couchbase.com//browse/CBL-2579)
* [CBL-2512](https://issues.couchbase.com//browse/CBL-2512) — [Replicator won’t stop](https://issues.couchbase.com//browse/CBL-2512)
* [CBL-2478](https://issues.couchbase.com//browse/CBL-2478) — [Tear down DBAccess on stopped instead of on release](https://issues.couchbase.com//browse/CBL-2478)
* [CBL-2436](https://issues.couchbase.com//browse/CBL-2436) — [Lithium beta 2: Confirm LiteCore request for close, before connection is opened.](https://issues.couchbase.com//browse/CBL-2436)
* [CBL-2405](https://issues.couchbase.com//browse/CBL-2405) — [Hung in call to c4socket\_closed](https://issues.couchbase.com//browse/CBL-2405)
* [CBL-2325](https://issues.couchbase.com//browse/CBL-2325) — [REST \_replicate throws errro](https://issues.couchbase.com//browse/CBL-2325)
* [CBL-2320](https://issues.couchbase.com//browse/CBL-2320) — [BlobInputStream read() returns negative values](https://issues.couchbase.com//browse/CBL-2320)
* [CBL-2313](https://issues.couchbase.com//browse/CBL-2313) — [HTTPS test fails](https://issues.couchbase.com//browse/CBL-2313)
* [CBL-2304](https://issues.couchbase.com//browse/CBL-2304) — [CBL core fleece exception: incompatible duplicate scope](https://issues.couchbase.com//browse/CBL-2304)
* [CBL-2243](https://issues.couchbase.com//browse/CBL-2243) — [memory leak, couchbase-lite-core issue#1221](https://issues.couchbase.com//browse/CBL-2243)
* [CBL-2212](https://issues.couchbase.com//browse/CBL-2212) — [Exception can leak out of C4](https://issues.couchbase.com//browse/CBL-2212)
* [CBL-2210](https://issues.couchbase.com//browse/CBL-2210) — [RESTListener synchronous response may hang](https://issues.couchbase.com//browse/CBL-2210)
* [CBL-2208](https://issues.couchbase.com//browse/CBL-2208) — [REST API \_replicate lacks authentication](https://issues.couchbase.com//browse/CBL-2208)
* [CBL-2182](https://issues.couchbase.com//browse/CBL-2182) — [Crash in assertion](https://issues.couchbase.com//browse/CBL-2182)
* [CBL-2180](https://issues.couchbase.com//browse/CBL-2180) — [Conflict resolver doesn’t sync blob](https://issues.couchbase.com//browse/CBL-2180)
* [CBL-1748](https://issues.couchbase.com//browse/CBL-1748) — [X509TrustManager.checkServerTrusted with X509TrustManagerExtensions.checkServerTrusted](https://issues.couchbase.com//browse/CBL-1748)
* [CBL-1722](https://issues.couchbase.com//browse/CBL-1722) — [POSIX 32 (Broken Pipe) appears to crash application](https://issues.couchbase.com//browse/CBL-1722)
* [CBL-1718](https://issues.couchbase.com//browse/CBL-1718) — [Handle db close in inBatch](https://issues.couchbase.com//browse/CBL-1718)
* [CBL-1660](https://issues.couchbase.com//browse/CBL-1660) — [Not all debug logging is compiled out of release builds](https://issues.couchbase.com//browse/CBL-1660)
* [CBL-1438](https://issues.couchbase.com//browse/CBL-1438) — [WSA codes not properly handled by bio\_return\_value](https://issues.couchbase.com//browse/CBL-1438)
* [CBL-1401](https://issues.couchbase.com//browse/CBL-1401) — [API: Remove LogLevel.getValue](https://issues.couchbase.com//browse/CBL-1401)
* [CBL-1225](https://issues.couchbase.com//browse/CBL-1225) — [Testfest : unshare the docs does not replicate to CBL](https://issues.couchbase.com//browse/CBL-1225)
* [CBL-862](https://issues.couchbase.com//browse/CBL-862) — [CBL 2.7 and later doesn’t catch Illegal top-level key like "\_id"](https://issues.couchbase.com//browse/CBL-862)
* [CBL-708](https://issues.couchbase.com//browse/CBL-708) — [Conflicting revision bodies are not removed after resolution](https://issues.couchbase.com//browse/CBL-708)
* [CBL-462](https://issues.couchbase.com//browse/CBL-462) — [Continuous push attempts to replicate purged documents](https://issues.couchbase.com//browse/CBL-462)
* [CBL-220](https://issues.couchbase.com//browse/CBL-220) — [Windows cannot handle dates before 1970 with C API](https://issues.couchbase.com//browse/CBL-220)
* [CBL-49](https://issues.couchbase.com//browse/CBL-49) — [Need a way to distinguish boolean types](https://issues.couchbase.com//browse/CBL-49)

### [](#lbl-deprecated-this-release)Deprecated in this Release

Items (features and-or functionality) are marked as deprecated when a more current, and usually enhanced, alternative is available.

Whilst the deprecated item will remain usable, it is no longer supported, and will be removed in a future release — see also: [Removed in this Release](#lbl-removed-this-release)You should plan to move to an alternative, supported, solution as soon as practical.

* [CBL-1727](https://issues.couchbase.com//browse/CBL-1727) — [Improved naming for AbstractReplicatorConfiguration.ReplicatorType](https://issues.couchbase.com//browse/CBL-1727)
* The \[Database.compact()\] method is deprecated (as of 2.8), instead use [Database.performMaintenance()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/Database.html#performMaintenance-com.couchbase.lite.MaintenanceType-).

#### [](#previously-deprecated)Previously Deprecated

None specified

### [](#lbl-removed-this-release)Removed in this Release

* [CBL-2257](https://issues.couchbase.com//browse/CBL-2257) — [Rename ReplicatedDocument attributes for Kotlin](https://issues.couchbase.com//browse/CBL-2257)
* [CBL-1844](https://issues.couchbase.com//browse/CBL-1844) — [Remove replicator.resetCheckpoint() API](https://issues.couchbase.com//browse/CBL-1844)
* [CBL-1401](https://issues.couchbase.com//browse/CBL-1401) — [API: Remove LogLevel.getValue](https://issues.couchbase.com//browse/CBL-1401)
* [CBL-1359](https://issues.couchbase.com//browse/CBL-1359) — [Remove deprecated Replicator.resetCheckpoint() and de-deprecate Replicator.start()](https://issues.couchbase.com//browse/CBL-1359)
* [CBL-1358](https://issues.couchbase.com//browse/CBL-1358) — [Remove deprecated LogDomain.ALL (replaced by LogDomain.ALL\_DOMAINS)](https://issues.couchbase.com//browse/CBL-1358)
* [CBL-1357](https://issues.couchbase.com//browse/CBL-1357) — [Remove deprecated Database.compact()](https://issues.couchbase.com//browse/CBL-1357)
* [CBL-1356](https://issues.couchbase.com//browse/CBL-1356) — [Remove deprecated constructor BasicAuthenticator(String, String)](https://issues.couchbase.com//browse/CBL-1356)
* [CBL-1350](https://issues.couchbase.com//browse/CBL-1350) — [Deprecate Replicator.resetCheckpoint() API](https://issues.couchbase.com//browse/CBL-1350)
* [CBL-1011](https://issues.couchbase.com//browse/CBL-1011) — [Remove deprecated Replicator.resetCheckpoint()](https://issues.couchbase.com//browse/CBL-1011)

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
* [What’s New](#cbl-whatsnew.adoc)

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