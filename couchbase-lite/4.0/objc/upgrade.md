---
title: Upgrade Couchbase Lite
description: ""
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.0/modules/objc/pages/upgrade.adoc
  xref: xref:4.0@couchbase-lite:objc:upgrade.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/4.0/objc/upgrade.html)

# Upgrade Couchbase Lite

> [!IMPORTANT]
> On upgrading from a 2.x release, all Couchbase Lite databases automatically re-index on initial database open.  
> This can result in a delay before the database is usable.

## [](#4-0-0-upgrade)4.0.3 Upgrade

Couchbase Lite 4.0 introduces significant architectural changes, most notably the migration from revision trees to version vectors for document versioning. This upgrade requires careful planning and understanding of the compatibility requirements.

The action takes place automatically and can lead to some delay in the database becoming available for use in your application.

In addition, if you're syncing with a 4.0.3 Sync Gateway, you should be aware of the significant configuration enhancements introduced and their effect. See [Upgrading Sync Gateway](../../../sync-gateway/current/upgrading.md) for more details. This is a one-way conversion.

### [](#major-changes-in-4-0-3)Major Changes in 4.0.3

**Version Vector Architecture**: CBL 4.0.3 replaces the revision tree system with version vectors, providing improved performance, scalability, and conflict resolution. Documents now use version-based revision IDs in the format `<timestamp>@<source-id>` instead of the previous `<generation>-<document-hash>` format.

**Enhanced Conflict Resolution**: The default conflict resolution strategy changes from `most active wins` to `last write wins` based on hybrid logical timestamps, providing more intuitive and predictable conflict resolution behavior.

**New Document Properties**: a new `timestamp` property is available on Document objects, providing direct access to the document's logical timestamp as a `uint64_t` value representing nanoseconds since the Unix epoch.

### [](#database-compatibility-40)Database Compatibility

**Automatic Upgrade from 3.x**: CBL 4.0.3 databases are compatible with CBL 3.1 and 3.2 databases. When opening a 3.1 or 3.2 database with CBL 4.0.3, documents are automatically upgraded to use version vectors when they're updated and saved.

**No Configuration Required**: CBL 4.0.3 enables version vectors by default - the feature requires no API configuration.

### [](#synchronization-compatibility-40)Synchronization Compatibility

**Sync Gateway Requirements**: CBL 4.0.3 requires Sync Gateway 4.x or later for synchronization. Attempting to sync with Sync Gateway versions prior to 4.x results in replication errors with appropriate error messages indicating the incompatibility.

**Peer-to-Peer Compatibility**: CBL 4.0.3 can only perform peer-to-peer synchronization with other CBL 4.x instances using either `CBLURLEndpointListener` or `CBLMessageEndpointListener`. Sync attempts with CBL 3.x peers fail with appropriate error messages.

### [](#api-changes)API Changes

#### [](#removed-apis)Removed APIs

##### [](#resetcheckpoint)ResetCheckpoint

Alternative

```objc
`[replicator startWithReset:];`
```

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

### [](#replication-compatibility)Replication Compatibility

CBL 4.0 introduces strict replication compatibility requirements due to the version vector architecture changes.

**Sync Gateway Compatibility**: CBL 4.0 requires Sync Gateway 4.0 or later for synchronization. Attempting to sync with Sync Gateway versions prior to 4.0 results in replication errors with appropriate error messages indicating the incompatibility.

**Peer-to-Peer Compatibility**: CBL 4.0 can only perform peer-to-peer synchronization with other CBL 4.0+ instances. Sync attempts with CBL 3.x or earlier peers fails with appropriate error messages.

**No Backward Compatibility**: Unlike previous CBL versions, CBL 4.0 cannot sync with earlier versions of either Sync Gateway or other CBL instances due to the fundamental changes in document versioning architecture.

## [](#xcode)Xcode

The API has changed in Couchbase Lite 2.0 and requires porting an application that's using Couchbase Lite 1.x API to the Couchbase Lite 2.0 API. To update an Xcode project built with Couchbase Lite 1.x:

* Remove the existing **CouchbaseLite.framework** dependency from the Xcode project.
* Remove all the Couchbase Lite 1.x dependencies (see the [1.x installation guide](https://docs-archive.couchbase.com/couchbase-lite/1.4/objc.html#getting-started)).
* Install the Couchbase Lite 2.0 framework in your project — see [Install](gs-install.md). At this point, there are compiler warnings. See the examples on this page to learn about the new API.
* Build & run your application.

## [](#downgrading-couchbase-lite)Downgrading Couchbase Lite

### [](#downgrading-between-major-releases)Downgrading Between Major Releases

**No Downgrade Support** \- Couchbase Lite (CBL) does not support downgrades between major versions. Once you upgrade to a new major version, attempting to downgrade to a previous major version creates incompatibility issues. For example, upgrading from CBL 3.x.x to CBL 4.x does not allow you to revert to CBL 3.x.

### [](#downgrading-between-minor-releases)Downgrading Between Minor Releases

**Conditional Downgrade Support** \- Downgrade support for minor releases varies on a case-by-case basis. The release notes for each minor version clarify whether downgrades receive support.

For example, when a new minor version such as CBL 3.1.0 becomes available, the release notes specify whether reverting to CBL 3.0.x receives support.

### [](#downgrading-between-patch-releases)Downgrading Between Patch Releases

**Full Downgrade Support** \- Couchbase Lite supports downgrades between patch releases. Users can downgrade between different patch versions within the same minor release.

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