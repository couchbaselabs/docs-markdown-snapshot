---
title: Upgrade Couchbase Lite
description: ""
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.4/modules/objc/pages/upgrade.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:3.4@couchbase-lite:objc:upgrade.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.4/objc/upgrade.html)

# Upgrade Couchbase Lite

> [!IMPORTANT]
> On upgrading from a 2.x release, all Couchbase Lite databases will be automatically re-indexed on initial database open.  
> This can result in a delay before the database is usable.

### [](#vector-search-extension)Vector Search Extension

Couchbase Lite 3.4.0 is compatible with Vector Search Extension 2.0.0 only. If your application uses Vector Search, update the Vector Search Extension to 2.0.0 when upgrading to Couchbase Lite 3.4.0.

## [](#3-2-3-upgrade)3.4.0 Upgrade

The action will take place automatically and can lead to some delay in the database becoming available for use in your application.

In addition, if you are syncing with a 3.4.0 Sync Gateway, you should be aware of the significant configuration enhancements introduced and their impact. See [Upgrading Sync Gateway](../../../sync-gateway/current/upgrading.md) for more details. This is a one-way conversion.

### [](#api-changes)API Changes

#### [](#removed-apis)Removed APIs

##### [](#resetcheckpoint)ResetCheckpoint

Alternative

`[replicator startWithReset:];`

Before

```objc
[replicator resetCheckpoint];
[replicator start];
```

After

```objc
[replicator startWithReset: YES];
```

##### [](#database-setloglevel)Database.setLogLevel

Alternative

`CBLDatabase.log.console`

Before

```objc
[CBLDatabase setLogLevel:kCBLLogLevelVerbose domain: kCBLLogDomainAll];
```

After

```objc
CBLDatabase.log.console.level = kCBLLogLevelVerbose;
CBLDatabase.log.console.domains = kCBLLogDomainAll;
```

##### [](#database-compact)Database.compact

Alternative

`[db performMaintenance:error:]`

Before

```objc
[testdb compact: &error];
```

After

```objc
[testdb performMaintenance:kCBLMaintenanceTypeCompact error:&error];
```

#### [](#deprecated-api)Deprecated API

##### [](#match)Match

Alternative

`[CBLQueryFullTextFunction matchWithIndexName: query:]`

Before

```objc
CBLQueryFullTextExpression* index = [CBLQueryFullTextExpression indexWithName: @"indexName"];
q = [CBLQueryBuilder select: @[[CBLQuerySelectResult expression: [CBLQueryMeta id]]]
                        from: [CBLQueryDataSource database: self.database]
                        where: [index match: @"'queryString'"]];
```

After

```objc
    q = [CBLQueryBuilder select: @[[CBLQuerySelectResult expression: [CBLQueryMeta id]]]
                           from: [CBLQueryDataSource database: self.database]
                          where: [CBLQueryFullTextFunction matchWithIndexName: @"indexName"
                                                                        query: @"'queryString'"]];
```

##### [](#isnullormissing-and-notnullormissing)isNullOrMissing and notNullOrMissing

Alternatives

```objc
[exp isValued];
[exp isNotValued];
```

Before

```objc
    q = [CBLQueryBuilder select: @[[CBLQuerySelectResult expression: [CBLQueryMeta id]]]
                           from: [CBLQueryDataSource database: self.database]
                          where: [[CBLQueryExpression property: @"missingProp"] isNullOrMissing]];

    q2 = [CBLQueryBuilder select: @[[CBLQuerySelectResult expression: [CBLQueryMeta id]]]
                            from: [CBLQueryDataSource database: self.database]
                           where: [[CBLQueryExpression property: @"notMissingProp"] notNullOrMissing]];
```

After

```objc
    q = [CBLQueryBuilder select: @[[CBLQuerySelectResult expression: [CBLQueryMeta id]]]
                           from: [CBLQueryDataSource database: self.database]
                          where: [[CBLQueryExpression property: @"missingProp"] isNotValued]];

    q2 = [CBLQueryBuilder select: @[[CBLQuerySelectResult expression: [CBLQueryMeta id]]]
                            from: [CBLQueryDataSource database: self.database]
                           where: [[CBLQueryExpression property: @"notMissingProp"] isValued]];
```

#### [](#updated-api)Updated API

##### [](#atan2)ATAN2

> [!CAUTION]
> Breaking change

`ATAN2(x, y)` now becomes `ATAN2(y, x)`

Before

```objc
q = [CBLQueryBuilder select: @[[CBLQuerySelectResult expression: [CBLQueryFunction atan2: p y: [CBLQueryExpression integer: 90]]]]
                            from: [CBLQueryDataSource database: self.database]];
```

After

```objc
q = [CBLQueryBuilder select: @[[CBLQuerySelectResult expression: [CBLQueryFunction atan2: [CBLQueryExpression integer: 90] x: p]]]
                           from: [CBLQueryDataSource database: self.database]];
```

## [](#lbl-db-upgrades)1.x Databases Upgrades to 2.x

Databases created using Couchbase Lite 1.2 or later can still be used with Couchbase Lite 2.x; but will be automatically updated to the current 2.x version. This feature is only available for the default storage type (i.e., not a ForestDB database).

### [](#encrypted-databases)Encrypted Databases

The automatic migration feature does not support encrypted databases. So if the 1.x database is encrypted you will first need to disable encryption using the Couchbase Lite 1.x API (see the [1.x Database Guide](https://docs-archive.couchbase.com/couchbase-lite/1.4/objc.html#database-encryption)).

Thus, to upgrade an encrypted 1.x database, you should do the following:

Upgrading Encrypted Databases

1. Disable encryption using the Couchbase Lite 1.x framework (see [1.x encryption guide](https://docs-archive.couchbase.com/couchbase-lite/1.4/objc.html#database-encryption))
2. Open the database file with encryption enabled using the Couchbase Lite 2.x framework.

Since it is not possible to package Couchbase Lite 1.x and Couchbase Lite 2.x in the same application this upgrade path would require two successive upgrades.

If you are using Sync Gateway to synchronize the database content, it may be preferable to run a pull replication from a new 2.x database with encryption enabled and delete the 1.x local database.

### [](#handling-of-existing-conflicts)Handling of Existing Conflicts

If there are existing conflicts in the 1.x database, the automatic upgrade process copies the default winning revision to the new database and does NOT copy any conflicting revisions.

This functionality is related to the way conflicts are now being handled in Couchbase Lite — see [Handling Data Conflicts](conflict.md).

Optionally, existing conflicts in the 1.x database can be resolved with the [1.x API](https://docs-archive.couchbase.com/couchbase-lite/1.4/objc.html#resolving-conflicts) prior to the database being upgraded.

### [](#handling-of-existing-attachments)Handling of Existing Attachments

Attachments persisted in a 1.x database are copied to the new database. NOTE: The relevant Couchbase Lite API is now called the `Blob` API not the `Attachments` API.

The functionally is identical but the internal schema for attachments has changed.

Blobs are stored anywhere in the document, just like other value types. Whereas in 1.x they were stored under the `_attachments` field.

The automatic upgrade functionality **does not** update the internal schema for attachments, so they remain accessible under the `_attachments` field. See [Example 1](#ex-get-att) for how to retrieve an attachment that was created in a 1.x database with a 2.x API.

Example 1\. Retrieve 1.x Attachment

```objc
CBLDictionary *attachments = [doc dictionaryForKey:@"_attachments"];
CBLBlob *avatar = [attachments blobForKey:@"avatar"];
NSData *content = [avatar content];
```

### [](#replication-compatibility)Replication Compatibility

The current replication protocol is not backwards compatible with the 1.x replication protocol. Therefore, to use replication with Couchbase Lite 2.x, the target Sync Gateway instance must also be upgraded to 2.x.

Sync Gateway 2.x will continue to accept clients that connect through the 1.x protocol.

It will automatically use the 1.x replication protocol when a Couchbase Lite 1.x client connects through http://localhost:4984/db and the 2.0 replication protocol when a Couchbase Lite 2.0 client connects through ws://localhost:4984/db.

This allows for a smoother transition to get all your user base onto a version of your application built with Couchbase Lite 2.x.

## [](#xcode)Xcode

The API has changed in Couchbase Lite 2.0 and will require porting an application that is using Couchbase Lite 1.x API to the Couchbase Lite 2.0 API. To update an Xcode project built with Couchbase Lite 1.x:

* Remove the existing **CouchbaseLite.framework** dependency from the Xcode project.
* Remove all the Couchbase Lite 1.x dependencies (see the [1.x installation guide](https://docs-archive.couchbase.com/couchbase-lite/1.4/objc.html#getting-started)).
* Install the Couchbase Lite 2.0 framework in your project — see [Install](gs-install.md). At this point, there will be many compiler warnings. Refer to the examples on this page to learn about the new API.
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

For example, if you're running CBL 3.1.6 you can downgrade to CBL 3.1.4 or CBL 3.1.3 without issues.

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