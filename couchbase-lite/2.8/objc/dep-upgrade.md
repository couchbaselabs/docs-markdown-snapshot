---
title: Upgrade Couchbase Lite
description: Couchbase mobile database certificate pinning
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/objc/pages/dep-upgrade.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.8@couchbase-lite:objc:dep-upgrade.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/objc/dep-upgrade.html)

# Upgrade Couchbase Lite

> Couchbase mobile database certificate pinning 

## [](#xcode)Xcode

The API has changed in Couchbase Lite 2.0 and will require porting an application that is using Couchbase Lite 1.x API to the Couchbase Lite 2.0 API. To update an Xcode project built with Couchbase Lite 1.x:

* Remove the existing **CouchbaseLite.framework** dependency from the Xcode project.
* Remove all the Couchbase Lite 1.x dependencies (see the [1.x installation guide](https://docs-archive.couchbase.com/couchbase-lite/1.4/objc.html#getting-started)).
* Install the Couchbase Lite 2.0 framework in your project — see [Install](../../current/objc/gs-install.md). At this point, there will be many compiler warnings. Refer to the examples on this page to learn about the new API.
* Build & run your application.

## [](#database-upgrade)Database Upgrade

Databases that were created with Couchbase Lite 1.2 or later can be used with Couchbase Lite 2.0\. Upon detecting it is a 1.x database file, Couchbase Lite will automatically upgrade it to 2.0\. This feature is only available for the default storage type (i.e., not a ForestDB database). Additionally, the automatic migration feature does not support encrypted databases, so if the 1.x database is encrypted you will first need to disable encryption using the Couchbase Lite 1.x API (see the [1.x Database Guide](https://docs-archive.couchbase.com/couchbase-lite/1.4/objc.html#database-encryption)).

## [](#handling-of-existing-conflicts)Handling of Existing Conflicts

For conflicts in the 1.x database, the automatic upgrade process copies the default winning revision to the new 2.0 database and does NOT copy any conflicting revisions. This functionality is related to the way conflicts are being handled in Couchbase Lite 2.0 — see [Handling Data Conflicts](../../current/objc/conflict.md). Optionally, existing conflicts in the 1.x database can be resolved with the [1.x API](https://docs-archive.couchbase.com/couchbase-lite/1.4/objc.html#resolving-conflicts) prior to the database being upgraded to 2.0.

## [](#handling-of-existing-attachments)Handling of Existing Attachments

Attachments that were persisted in the 1.x database will be copied to the 2.0 database. In Couchbase Lite 2.0, the `Attachment` API has been renamed to `Blob` API. The functionally is identical but the internal schema for attachments has changed. In 1.x they were stored under the `_attachments` field and in Couchbase Lite 2.0 they are stored anywhere in the document like other value types. The automatic upgrade functionality will not update the internal schema for attachments, so they will still be accessible under the `_attachments` field. The following example shows how to retrieve an attachment that was created in a 1.x database with the 2.0 API.

```objc
CBLDictionary *attachments = [document dictionaryForKey:@"_attachments"];
CBLBlob *avatar = [attachments blobForKey:@"avatar"];
NSData *content = [avatar content];
```

## [](#replication-compatibility)Replication Compatibility

The replication protocol used in Couchbase Lite 2.0 has been re-designed from the ground up and it is not backwards compatible with the 1.x replication protocol. Therefore, to use replication with Couchbase Lite 2.x, the target Sync Gateway instance must also be upgraded to 2.x.

Sync Gateway 2.x will continue to accept clients that connect through the 1.x protocol. It will automatically use the 1.x replication protocol when a Couchbase Lite 1.x client connects through http://localhost:4984/db and the 2.0 replication protocol when a Couchbase Lite 2.0 client connects through ws://localhost:4984/db. This allows for a smoother transition to get all your user base onto a version of your application built with Couchbase Lite 2.x.