---
title: Databases
description: Working with Couchbase Lite Databases
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.0/modules/objc/pages/database.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:3.0@couchbase-lite:objc:database.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.0/objc/database.html)

# Databases

> Description — _Working with Couchbase Lite Databases_  
> Related Content — [Blobs](blob.md) | [Documents](document.md) | [Indexing](indexing.md)

## [](#open-db)Create or Open Database

You can create a new database and-or open an existing database, using the [CBLDatabase](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLDatabase.html) class. Just pass in a database name and optionally a [CBLDatabaseConfiguration](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLDatabaseConfiguration.html) — see [Example 1](#ex-dbopen).

Things to watch for include:

* If the named database does not exist in the specified, or default, location then a new one is created
* The database is created in a default location unless you specify a directory for it — see: [CBLDatabaseConfiguration](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLDatabaseConfiguration.html) and [CBLDatabaseConfiguration.directory()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLDatabaseConfiguration.html#/c:objc%28cs%29CBLDatabaseConfiguration%28py%29directory)  
> [!TIP]  
> Best Practice is to always specify the path to the database explicitly.  
Typically, the default location for Objective-C is the application sandbox .  
See also [Finding a Database File](#lbl-find-db-loc).

Example 1\. Open or create a database

```objc
NSError *error;
CBLDatabase *database = [[CBLDatabase alloc] initWithName:@"my-database" error:&error];
if (!database) {
    NSLog(@"Cannot open the database:%@", error);
}
self.database = database;
```

## [](#close-database)Close Database

You are advised to incorporate the closing of all open databases into your application workflow.

Closing a database is simple, just use [CBLDatabase.Close()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLDatabase.html#/c:objc%28cs%29CBLDatabase%28im%29close:) — see: [Example 2](#ex-dbclose). This also closes \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]active replications, listeners and-or live queries connected to the database.

> [!NOTE]
> Closing a database soon after starting a replication involving it can cause an exception as the asynchronous `replicator (start)` may not yet be `connected`.

> [!TIP]
> Safely Closing a Database pre 2.8
> 
> Before closing, check that any attached listeners (query/replication/change) indicate they are at least at `connected` status before closing — see for example: [Monitor Status](replication.md#lbl-repl-mon).

Example 2\. Close a Database

```objc
if (![self.database close:&error])
    NSLog(@"Error closing db:%@", error);
```

## [](#database-encryption)Database Encryption

> [!IMPORTANT]
> This is an [Enterprise Edition](https://www.couchbase.com/products/editions) feature.

_Couchbase Lite on Objective-C_ includes the ability to encrypt Couchbase Lite databases. This allows mobile applications to secure the data at rest, when it is being stored on the device. The algorithm used to encrypt the database is 256-bit AES.

### [](#enabling)Enabling

To enable encryption, use [CBLDatabaseConfiguration.encryptionKey()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLDatabaseConfiguration.html#/c:objc%28cs%29CBLDatabaseConfiguration%28py%29encryptionKey) to set the encryption key of your choice. Provide this encryption key every time the database is opened — see [Example 3](#ex-sdb-encrypt).

Example 3\. Configure Database Encryption

```objc
CBLDatabaseConfiguration *config = [[CBLDatabaseConfiguration alloc] init];
config.encryptionKey = [[CBLEncryptionKey alloc] initWithPassword:@"secretpassword"];

NSError *error;
self.database = [[CBLDatabase alloc] initWithName:@"my-database" config:config error:&error];
if (!self.database) {
    NSLog(@"Cannot open the database:%@", error);
}
```

### [](#persisting)Persisting

Couchbase Lite does not persist the key. It is the application’s responsibility to manage the key and store it in a platform specific secure store such as Apple’s [Keychain](https://developer.apple.com/documentation/security/keychain%5Fservices) or Android’s [Keystore](https://developer.android.com/training/articles/keystore).

### [](#opening)Opening

An encrypted database can only be opened with the same language SDK that was used to encrypt it in the first place. So a database encrypted using the Objective-C SDK, and then exported, is readable only by the Objective-C SDK.

### [](#changing)Changing

To change an existing encryption key, open the database using its existing encryption-key and use [CBLDatabase.changeEncryptionKey()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLDatabase.html#/c:objc%28cs%29CBLDatabase%28im%29changeEncryptionKey:error:)to set the required new encryption-key value.

### [](#removing)Removing

To remove encryption, open the database using its existing encryption-key and use [CBLDatabase.changeEncryptionKey()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLDatabase.html#/c:objc%28cs%29CBLDatabase%28im%29changeEncryptionKey:error:)with a null value as the encryption key.

### [](#upgrading)Upgrading

To upgrade an encrypted database see: [Upgrade 1.x databases](upgrade.md#lbl-db-upgrades)

## [](#lbl-find-db-loc)Finding a Database File

When the application is running on the iOS simulator, you can locate the application’s sandbox directory using the [SimPholders](https://simpholders.com/3/) utility.

## [](#lbl-db-util)Database Maintenance

From time to time it may be necessary to perform certain maintenance activities on your database, for example to compact the database file, removing unused documents and blobs no longer referenced by any documents.

Couchbase Lite’s API provides the [CBLDatabase.performMaintenance()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLDatabase.html#/c:objc%28cs%29CBLDatabase%28im%29performMaintenance:error:) method. The available maintenance operations, including `compact` are as shown in the enum [CBLMaintenanceType](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Enums/CBLMaintenanceType.html) to accomplish this.

This is a resource intensive operation and is not performed automatically. It should be run on-demand using the API. If in doubt, consult Couchbase support.

## [](#cli-tool)Command Line Tool

`cblite` is a command-line tool for inspecting and querying Couchbase Lite databases.

You can download and build it from the couchbaselabs [GitHub repository](https://github.com/couchbaselabs/couchbase-mobile-tools/blob/master/README.cblite.md). Note that the `cblite` tool is not supported by the [Couchbase Support Policy](https://www.couchbase.com/support-policy).

## [](#troubleshooting)Troubleshooting

You should use console logs as your first source of diagnostic information. If the information in the default logging level is insufficient you can focus it on database errors and generate more verbose messages — see: [Example 4](#ex-logdb).

For more on using Couchbase logs — see: [Using Logs](troubleshooting-logs.md).

Example 4\. Increase Level of Database Log Messages

```objc
CBLDatabase.log.console.domains = kCBLLogDomainAll;
```

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Prerequisites](gs-prereqs.md)
* [Install](gs-install.md)
* [Build and Run](gs-build.md)

###### [](#-2)

Learn more . . .

* [Databases](database.md)
* [Documents](document.md)
* [Blobs](blob.md)
* [Remote Sync Gateway](replication.md)
* [Handling Data Conflicts](conflict.md)

###### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

---

[1](#%5Ffootnoteref%5F1). Commencing with Release 2.8