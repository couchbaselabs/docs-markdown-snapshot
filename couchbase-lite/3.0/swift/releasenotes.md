---
title: Release Notes
description: Couchbase Lite on Swift
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.0/modules/swift/pages/releasenotes.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.0@couchbase-lite:swift:releasenotes.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.0/swift/releasenotes.html)

# Release Notes

## [](#maint-3-0-15)3.0.15 — November 2023

Version 3.0.15 for Swift delivers the following features and enhancements:

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

Version 3.0.12 for Swift delivers the following features and enhancements:

### [](#enhancements-2)Enhancements

* [CBL-4580 - MutableDocument contains(key: String) returns wrong result](https://issues.couchbase.com/browse/CBL-4580)
* [CBL-4487 - Build release framework without bitcode enabled](https://issues.couchbase.com/browse/CBL-4487)
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

* [CBL-637 — Java Console app doesn't exit](https://issues.couchbase.com/browse/CBL-637)

## [](#maint-3-0-2)3.0.2 — August 2022

Version 3.0.2 of Couchbase Lite for Swift delivers a number of fixes and enhancements.

### [](#enhancements-3)Enhancements

* [CBL-3034](https://issues.couchbase.com/browse/CBL-3034) — [Update zlib to the latest version](https://issues.couchbase.com/browse/CBL-3034)
* [CBL-2973](https://issues.couchbase.com/browse/CBL-2973) — [Implement enhanced pinned server certificate feature](https://issues.couchbase.com/browse/CBL-2973)

### [](#issues-and-resolutions-3-0-2)Issues and Resolutions

#### [](#fixed-issues)Fixed Issues

* [CBL-3351](https://issues.couchbase.com/browse/CBL-3351) — [32+ select items in the query fails to get column name](https://issues.couchbase.com/browse/CBL-3351)
* [CBL-3224](https://issues.couchbase.com/browse/CBL-3224) — [Call to c4socket\_closed causes native crash](https://issues.couchbase.com/browse/CBL-3224)
* [CBL-3222](https://issues.couchbase.com/browse/CBL-3222) — [Enable F\_BARRIERFSYNC in SQLite](https://issues.couchbase.com/browse/CBL-3222)
* [CBL-3090](https://issues.couchbase.com/browse/CBL-3090) — [Push large database test could fail](https://issues.couchbase.com/browse/CBL-3090)
* [CBL-3040](https://issues.couchbase.com/browse/CBL-3040) — [QueryParser wrong for a case of JOIN](https://issues.couchbase.com/browse/CBL-3040)
* [CBL-3017](https://issues.couchbase.com/browse/CBL-3017) — [Cookies set in Headers are replaced with Session Authenticator's cookies](https://issues.couchbase.com/browse/CBL-3017)
* [CBL-2884](https://issues.couchbase.com/browse/CBL-2884) — [evpos is missing in the changed attachment body when using delta sync](https://issues.couchbase.com/browse/CBL-2884)

#### [](#known-issues-3)Known Issues

None in this release

## [](#maint-3-0-1)3.0.1 — March 2022

Version 3.0.1 of Couchbase Lite for Swift delivers a number of fixes and enhancements.

### [](#enhancements-4)Enhancements

Highlights

Couchbase Lite for Swift provides an enhancement to the Replicator Configuration API, which now allows you to specify the network interface to use for connecting to the remote target — see: [Configure Network Interface](replication.md#lbl-network-interface).

References

* [CBL-2832](https://issues.couchbase.com/browse/CBL-2832) — [Implement the API to specify network interface used by the replicator](https://issues.couchbase.com/browse/CBL-2832)

### [](#issues-and-resolutions-3-0-1)Issues and Resolutions

#### [](#fixed-issues-2)Fixed Issues

* [CBL-2825](https://issues.couchbase.com/browse/CBL-2825) — [Missing \_attachments metadata when pushing updated docs to Sync Gateway](https://issues.couchbase.com/browse/CBL-2825)

#### [](#known-issues-4)Known Issues

None for this release.

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

* [CBL-2633](https://issues.couchbase.com//browse/CBL-2633) — [Update support level and message note of Database'saveBlob() and getBlob() API](https://issues.couchbase.com//browse/CBL-2633)
* [CBL-2628](https://issues.couchbase.com//browse/CBL-2628) — [Change away from using SELECT when open socket](https://issues.couchbase.com//browse/CBL-2628)
* [CBL-2549](https://issues.couchbase.com//browse/CBL-2549) — [Expose BlobType, BlobContentType, BlobDigest keys in Swift](https://issues.couchbase.com//browse/CBL-2549)
* [CBL-2546](https://issues.couchbase.com//browse/CBL-2546) — [CBLError description is missing](https://issues.couchbase.com//browse/CBL-2546)
* [CBL-2483](https://issues.couchbase.com//browse/CBL-2483) — [Change database.createQuery(String query) signature to throw CouchbaseLiteException](https://issues.couchbase.com//browse/CBL-2483)
* [CBL-2452](https://issues.couchbase.com//browse/CBL-2452) — [Update Swift Database.createQuery(query: String) API](https://issues.couchbase.com//browse/CBL-2452)
* [CBL-2437](https://issues.couchbase.com//browse/CBL-2437) — [Add note about notification when disabling autoPurge](https://issues.couchbase.com//browse/CBL-2437)
* [CBL-2408](https://issues.couchbase.com//browse/CBL-2408) — [Add kFLUndefinedValue constant in Fleece.h](https://issues.couchbase.com//browse/CBL-2408)
* [CBL-2383](https://issues.couchbase.com//browse/CBL-2383) — [Increase kOtherDBCloseTimeoutSecs to allow enough time for all db open connections to be closed](https://issues.couchbase.com//browse/CBL-2383)
* [CBL-2379](https://issues.couchbase.com//browse/CBL-2379) — [Improve logging message when copying database using a wrong encryption key](https://issues.couchbase.com//browse/CBL-2379)
* [CBL-2376](https://issues.couchbase.com//browse/CBL-2376) — [Provide note about copying encrypted database in API doc](https://issues.couchbase.com//browse/CBL-2376)
* [CBL-2358](https://issues.couchbase.com//browse/CBL-2358) — [Add function for creating FLMutableDict/Array from JSON](https://issues.couchbase.com//browse/CBL-2358)
* [CBL-2292](https://issues.couchbase.com//browse/CBL-2292) — [Update mobile n1ql test suite](https://issues.couchbase.com//browse/CBL-2292)
* [CBL-2064](https://issues.couchbase.com//browse/CBL-2064) — [Implement Encrypted Property Feature](https://issues.couchbase.com//browse/CBL-2064)
* [CBL-2043](https://issues.couchbase.com//browse/CBL-2043) — [Implement Maintenance's Optimize Options](https://issues.couchbase.com//browse/CBL-2043)
* [CBL-2038](https://issues.couchbase.com//browse/CBL-2038) — [Change QueryBuilder's ATAN2(X, Y) to ATAN2(Y, X)](https://issues.couchbase.com//browse/CBL-2038)
* [CBL-1976](https://issues.couchbase.com//browse/CBL-1976) — [Set EnableAutoPurge to C4Replicator options](https://issues.couchbase.com//browse/CBL-1976)
* [CBL-1972](https://issues.couchbase.com//browse/CBL-1972) — [Channel Access Revocation](https://issues.couchbase.com//browse/CBL-1972)
* [CBL-1941](https://issues.couchbase.com//browse/CBL-1941) — [maxRetries should now count attempts instead of retries](https://issues.couchbase.com//browse/CBL-1941)
* [CBL-1935](https://issues.couchbase.com//browse/CBL-1935) — [Remove Deprecated LiteCore Methods](https://issues.couchbase.com//browse/CBL-1935)
* [CBL-1910](https://issues.couchbase.com//browse/CBL-1910) — [Implement the Revised Retry Logic and Heartbeat Config API](https://issues.couchbase.com//browse/CBL-1910)
* [CBL-1893](https://issues.couchbase.com//browse/CBL-1893) — [Remove deprecated APIs](https://issues.couchbase.com//browse/CBL-1893)
* [CBL-1872](https://issues.couchbase.com//browse/CBL-1872) — [Enhanced Configuration API](https://issues.couchbase.com//browse/CBL-1872)
* [CBL-1852](https://issues.couchbase.com//browse/CBL-1852) — [Explore Module Initialization](https://issues.couchbase.com//browse/CBL-1852)
* [CBL-1842](https://issues.couchbase.com//browse/CBL-1842) — [Remove replicator.resetCheckpoint() API](https://issues.couchbase.com//browse/CBL-1842)
* [CBL-1791](https://issues.couchbase.com//browse/CBL-1791) — [Change to QueryBuilder API](https://issues.couchbase.com//browse/CBL-1791)
* [CBL-1786](https://issues.couchbase.com//browse/CBL-1786) — [Ignore unknown-warning-option warning from clang](https://issues.couchbase.com//browse/CBL-1786)
* [CBL-1763](https://issues.couchbase.com//browse/CBL-1763) — [kErrTruncatedJSON is returning kFLNoError](https://issues.couchbase.com//browse/CBL-1763)
* [CBL-1757](https://issues.couchbase.com//browse/CBL-1757) — [CBL SQL++ Functionality](https://issues.couchbase.com//browse/CBL-1757)
* [CBL-1744](https://issues.couchbase.com//browse/CBL-1744) — [Fix Fire Timer at Same Time Test](https://issues.couchbase.com//browse/CBL-1744)
* [CBL-1714](https://issues.couchbase.com//browse/CBL-1714) — [Refactor POSIX error domain codes to be platform independent](https://issues.couchbase.com//browse/CBL-1714)
* [CBL-1710](https://issues.couchbase.com//browse/CBL-1710) — [Update to use setProgressLevel API in Replicator](https://issues.couchbase.com//browse/CBL-1710)
* [CBL-1666](https://issues.couchbase.com//browse/CBL-1666) — [Allow apps to trigger SQLite index optimization directly](https://issues.couchbase.com//browse/CBL-1666)
* [CBL-1650](https://issues.couchbase.com//browse/CBL-1650) — [CBL doesn't purge channel removals when removal revision already exists in CBL](https://issues.couchbase.com//browse/CBL-1650)
* [CBL-1584](https://issues.couchbase.com//browse/CBL-1584) — [Replicator Retry Logic](https://issues.couchbase.com//browse/CBL-1584)
* [CBL-1581](https://issues.couchbase.com//browse/CBL-1581) — [Reserve Property Keys](https://issues.couchbase.com//browse/CBL-1581)
* [CBL-1567](https://issues.couchbase.com//browse/CBL-1567) — [Ensure c4log\_enableFatalExceptionBacktrace is called](https://issues.couchbase.com//browse/CBL-1567)
* [CBL-1522](https://issues.couchbase.com//browse/CBL-1522) — [SQL++ : Add NULL OR MISSING literal](https://issues.couchbase.com//browse/CBL-1522)
* [CBL-1453](https://issues.couchbase.com//browse/CBL-1453) — [Failure testDeleteWithActiveLiveQueriesAndReplicators ](https://issues.couchbase.com//browse/CBL-1453)
* [CBL-1395](https://issues.couchbase.com//browse/CBL-1395) — [ERROR: AddressSanitizer: stack-use-after-return on address](https://issues.couchbase.com//browse/CBL-1395)
* [CBL-1350](https://issues.couchbase.com//browse/CBL-1350) — [Deprecate Replicator.resetCheckpoint() API](https://issues.couchbase.com//browse/CBL-1350)
* [CBL-1267](https://issues.couchbase.com//browse/CBL-1267) — [Jenkins unit test failures](https://issues.couchbase.com//browse/CBL-1267)
* [CBL-1232](https://issues.couchbase.com//browse/CBL-1232) — [Support function to change the kC4ReplicatorOptionProgressLevel](https://issues.couchbase.com//browse/CBL-1232)
* [CBL-1049](https://issues.couchbase.com//browse/CBL-1049) — [Zero fleece options when replicator is freed](https://issues.couchbase.com//browse/CBL-1049)
* [CBL-911](https://issues.couchbase.com//browse/CBL-911) — [Couchbase Lite Java replication hangs when using DEBUG console + file logging on Windows](https://issues.couchbase.com//browse/CBL-911)
* [CBL-429](https://issues.couchbase.com//browse/CBL-429) — [Create way to log methods queued to an actor](https://issues.couchbase.com//browse/CBL-429)
* [CBL-278](https://issues.couchbase.com//browse/CBL-278) — [Swift Codables support](https://issues.couchbase.com//browse/CBL-278)
* [CBL-111](https://issues.couchbase.com//browse/CBL-111) — [Build multi-platform XCFramework for Xcode 11+](https://issues.couchbase.com//browse/CBL-111)

### [](#lbl-api-changes)API Changes

#### [](#removed-apis)Removed APIs

##### [](#resetcheckpoint)ResetCheckpoint

Alternative

`replicator.start(reset:)`

Before

```swift
replicator.resetCheckpoint()
replicator.start()
```

After

```swift
replicator.start(true)
```

##### [](#database-setloglevel)Database.setLogLevel

Alternative

`Database.log.console`

Before

```swift
Database.setLogLevel(.verbose, domain: .all)
```

After

```swift
Database.log.console.domain = .all
Database.log.console.level = .verbose
```

##### [](#database-compact)Database.compact

Alternative

[Database.performMaintenance(type:)](https://docs.couchbase.com/mobile/3.0.0-beta02/couchbase-lite-swift/Classes/Database.html#/s:18CouchbaseLiteSwift8DatabaseC18performMaintenance4typeyAA0F4TypeO%5FtKF)

Before

```swift
try testdb.compact()
```

After

```swift
try testdb.performMaintenance(type: .compact)
```

#### [](#deprecated-api)Deprecated API

##### [](#match)Match

Alternative

`FullTextFunction.match(indexName:)`

Before

```swift
let index = FullTextExpression.index ("indexName")
let q = QueryBuilder.select([SelectResult.
expression(Meta.id)])
            .from(DataSource.database(testdb)) +
            .where(index.match("'queryString'"))
```

After

```swift
let q = QueryBuilder.select([SelectResult.expression(Meta.id)])
            .from(DataSource.database(testdb))
            .where(FullTextFunction.match(indexName: "indexName", query: "'queryString'"))
```

##### [](#isnullormissing-and-notnullormissing)isNullOrMissing and notNullOrMissing

Alternatives

`isNotValued()`  
`isValued()`

Before

```swift
|let q1 = QueryBuilder.select([SelectResult.expression(Meta.id)])
            .from(DataSource.database(testdb))
            .where(Expression.property("missingProp").isNullOrMissing())

let q2 = QueryBuilder.select([SelectResult.expression(Meta.id)])
            .from(DataSource.database(testdb))
            .where(Expression.property("notMissingProp").notNullOrMissing())
```

After

```swift
let q1 = QueryBuilder.select([SelectResult.expression(Meta.id)])
            .from(DataSource.database(testdb))
            .where(Expression.property("missingProp").isNotValued())

let q2 = QueryBuilder.select([SelectResult.expression(Meta.id)])
            .from(DataSource.database(testdb))
            .where(Expression.property("notMissingProp").isValued())
```

#### [](#updated-api)Updated API

##### [](#configuration)Configuration

The following classes are changed to Swift struct.

* DatabaseConfiguration
* ReplicatorConfiguration
* URLEndpointListenerConfiguration

Before

```swift
// use of let won't stop from editing instance later)

let config = DatabaseConfiguration()
config.encryptionKey = EncryptionKey.password(password!)

let config = ReplicatorConfiguration(database: db, target: target)
config.continuous = true
```

After

```swift
var config = DatabaseConfiguration()
config.encryptionKey = EncryptionKey.password(password!)

var config = ReplicatorConfiguration(database: db, target: target)
config.continuous = true
```

##### [](#atan2)ATAN2

> [!CAUTION]
> Breaking change

`ATAN2(x, y)` now becomes `ATAN2(y, x)`

Before

```swift
let p = Expression.property("number")
let q = QueryBuilder.select([SelectResult.expression(Function.atan2(x: Expression.int(90), y: p))])
            .from(DataSource.database(testdb))
```

After

```swift
let q = QueryBuilder.select([SelectResult.expression(Function.atan2(y: Expression.int(90), x: p))])
            .from(DataSource.database(testdb))
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
* [CBL-2192](https://issues.couchbase.com//browse/CBL-2192) — [kHasAttachments flag may be lost in Conflict Resolver](https://issues.couchbase.com//browse/CBL-2192)
* [CBL-2182](https://issues.couchbase.com//browse/CBL-2182) — [Crash in assertion](https://issues.couchbase.com//browse/CBL-2182)
* [CBL-2168](https://issues.couchbase.com//browse/CBL-2168) — [Warning : Linking against a dylib which is not safe for use in application extensions ](https://issues.couchbase.com//browse/CBL-2168)
* [CBL-1920](https://issues.couchbase.com//browse/CBL-1920) — [Crash when a query is destructed and unregistered from the database](https://issues.couchbase.com//browse/CBL-1920)
* [CBL-1908](https://issues.couchbase.com//browse/CBL-1908) — [Add cookie using setValue instead of addValue](https://issues.couchbase.com//browse/CBL-1908)
* [CBL-1743](https://issues.couchbase.com//browse/CBL-1743) — [\[p2p](https://issues.couchbase.com//browse/CBL-1743)seeing Network ERROR :Unexpected or unclean socket disconnect! , when server is disconnected \]
* [CBL-1722](https://issues.couchbase.com//browse/CBL-1722) — [POSIX 32 (Broken Pipe) appears to crash application](https://issues.couchbase.com//browse/CBL-1722)
* [CBL-1660](https://issues.couchbase.com//browse/CBL-1660) — [Not all debug logging is compiled out of release builds](https://issues.couchbase.com//browse/CBL-1660)
* [CBL-1438](https://issues.couchbase.com//browse/CBL-1438) — [WSA codes not properly handled by bio\_return\_value](https://issues.couchbase.com//browse/CBL-1438)
* [CBL-1362](https://issues.couchbase.com//browse/CBL-1362) — [Harmless unused property in ReplicatorConfiguration](https://issues.couchbase.com//browse/CBL-1362)
* [CBL-1225](https://issues.couchbase.com//browse/CBL-1225) — [Testfest : unshare the docs does not replicate to CBL](https://issues.couchbase.com//browse/CBL-1225)
* [CBL-862](https://issues.couchbase.com//browse/CBL-862) — [CBL 2.7 and later doesn't catch Illegal top-level key like "\_id"](https://issues.couchbase.com//browse/CBL-862)
* [CBL-708](https://issues.couchbase.com//browse/CBL-708) — [Conflicting revision bodies are not removed after resolution](https://issues.couchbase.com//browse/CBL-708)
* [CBL-462](https://issues.couchbase.com//browse/CBL-462) — [Continuous push attempts to replicate purged documents](https://issues.couchbase.com//browse/CBL-462)
* [CBL-220](https://issues.couchbase.com//browse/CBL-220) — [Windows cannot handle dates before 1970 with C API](https://issues.couchbase.com//browse/CBL-220)
* [CBL-49](https://issues.couchbase.com//browse/CBL-49) — [Need a way to distinguish boolean types](https://issues.couchbase.com//browse/CBL-49)

### [](#lbl-deprecated-this-release)Deprecated in this Release

Items (features and-or functionality) are marked as deprecated when a more current, and usually enhanced, alternative is available.

Whilst the deprecated item will remain usable, it is no longer supported, and will be removed in a future release — see also: [Removed in this Release](#lbl-removed-this-release)You should plan to move to an alternative, supported, solution as soon as practical.

* [CBL-2274](https://issues.couchbase.com//browse/CBL-2274) — [Deprecate QueryBuilder APIs](https://issues.couchbase.com//browse/CBL-2274)
* The \[Database.compact()\] method is deprecated (as of 2.8), instead use [Database.performMaintenance()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-swift/Classes/Database.html#/s:18CouchbaseLiteSwift8DatabaseC18performMaintenance4typeyAA0F4TypeO%5FtKF).

#### [](#previously-deprecated)Previously Deprecated

Support for iOS 9.0 is deprecated in version 2.6.

Support for macOS 10.9 and 10.10 is deprecated in version 2.5.

### [](#lbl-removed-this-release)Removed in this Release

* [CBL-1842](https://issues.couchbase.com//browse/CBL-1842) — [Remove replicator.resetCheckpoint() API](https://issues.couchbase.com//browse/CBL-1842)
* [CBL-1350](https://issues.couchbase.com//browse/CBL-1350) — [Deprecate Replicator.resetCheckpoint() API](https://issues.couchbase.com//browse/CBL-1350)

### [](#lbl-support-notices)Support Notices

This section documents any support-related notes, constraints and changes.

#### [](#new)New

None specified in this release

#### [](#ongoing)Ongoing

Apple's macOS is supported ONLY for testing and development purposes.

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