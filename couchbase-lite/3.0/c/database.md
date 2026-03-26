---
title: Databases
description: Working with Couchbase Lite Databases
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.0/modules/c/pages/database.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.0@couchbase-lite:c:database.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.0/c/database.html)

# Databases

> Description — _Working with Couchbase Lite Databases_  
> Related Content — [Blobs](blob.md) | [Documents](document.md) | [Indexing](indexing.md)

## [](#open-db)Create or Open Database

You can create a new database and-or open an existing database, using the [CBLDatabase](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-c/C/html/group%5F%5Fdatabase.html) class. Just pass in a database name and optionally a [DatabaseConfiguration](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Fdatabase%5Fconfiguration.html) — see [Example 1](#ex-dbopen).

Things to watch for include:

* If the named database does not exist in the specified, or default, location then a new one is created
* The database is created in a default location unless you specify a directory for it — see: [DatabaseConfiguration](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Fdatabase%5Fconfiguration.html) and [CBLDatabaseConfiguration.directory()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Fdatabase%5Fconfiguration.html#a844a5e7d02dd4ceb072dff39c7e88591)  
> [!TIP]  
> Best Practice is to always specify the path to the database explicitly.  
Typically, the default location for C is the application sandbox or current working directory .  
See also [Finding a Database File](#lbl-find-db-loc).

Example 1\. Open or create a database

```c
// NOTE: No error handling, for brevity (see getting started)

CBLError err;
CBLDatabase* db = CBLDatabase_Open(FLSTR("my-database"), NULL, &err);
```

## [](#close-database)Close Database

You are advised to incorporate the closing of all open databases into your application workflow.

Closing a database is simple, just use [CBLDatabase\_Close()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-c/C/html/group%5F%5Fdatabase.html#ga4d448b2d6809d6f9633d810d3ac6dcfa) — see: [Example 2](#ex-dbclose). This also closes active replications, listeners and-or live queries connected to the database.

> [!NOTE]
> Closing a database soon after starting a replication involving it can cause an exception as the asynchronous `replicator (start)` may not yet be `connected`.

Example 2\. Close a Database

```c
// NOTE: No error handling, for brevity (see getting started)

CBLError err;
CBLDatabase_Close(db, &err);
```

## [](#database-encryption)Database Encryption

> [!IMPORTANT]
> This is an [Enterprise Edition](https://www.couchbase.com/products/editions) feature.

_Couchbase Lite on C_ includes the ability to encrypt Couchbase Lite databases. This allows mobile applications to secure the data at rest, when it is being stored on the device. The algorithm used to encrypt the database is 256-bit AES.

### [](#enabling)Enabling

To enable encryption, use [CBLDatabaseConfiguration.encryptionKey()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Fdatabase%5Fconfiguration.html#aaab04fb9d092ff02693eea611efefc55) to set the encryption key of your choice. Provide this encryption key every time the database is opened — see [Example 3](#ex-sdb-encrypt).

Example 3\. Configure Database Encryption

```c
// NOTE: No error handling, for brevity (see getting started)

CBLDatabaseConfiguration config = CBLDatabaseConfiguration_Default();

// This returns a boolean, so check it in production code
CBLEncryptionKey_FromPassword(&config.encryptionKey, FLSTR("password"));

CBLError err;
CBLDatabase* db = CBLDatabase_Open(FLSTR("seekrit"), &config, &err);

// Change the encryption key (or add encryption if the DB is unencrypted)
CBLEncryptionKey betterKey;
CBLEncryptionKey_FromPassword(&betterKey, FLSTR("betterpassw0rd"));
CBLDatabase_ChangeEncryptionKey(db, &betterKey, &err);

// Remove encryption
CBLDatabase_ChangeEncryptionKey(db, NULL, &err);
```

### [](#persisting)Persisting

Couchbase Lite does not persist the key. It is the application's responsibility to manage the key and store it in a platform specific secure store such as Apple's [Keychain](https://developer.apple.com/documentation/security/keychain%5Fservices) or Android's [Keystore](https://developer.android.com/training/articles/keystore).

### [](#opening)Opening

An encrypted database can only be opened with the same language SDK that was used to encrypt it in the first place. So a database encrypted using the C SDK, and then exported, is readable only by the C SDK.

### [](#changing)Changing

To change an existing encryption key, open the database using its existing encryption-key and use [CBLDatabase\_ChangeEncryptionKey()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-c/C/html/group%5F%5Fdatabase.html#ga76a603bc678ceae18c9610b8a8274a09)to set the required new encryption-key value.

### [](#removing)Removing

To remove encryption, open the database using its existing encryption-key and use [CBLDatabase\_ChangeEncryptionKey()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-c/C/html/group%5F%5Fdatabase.html#ga76a603bc678ceae18c9610b8a8274a09)with a null value as the encryption key.

### [](#upgrading)Upgrading

To upgrade an encrypted database see: [Upgrade 1.x databases](dep-upgrade.md#lbl-db-upgrades)

## [](#lbl-find-db-loc)Finding a Database File

When the application is running on the iOS simulator, you can locate the application's sandbox directory using the [SimPholders](https://simpholders.com/3/) utility.

## [](#lbl-db-util)Database Maintenance

From time to time it may be necessary to perform certain maintenance activities on your database, for example to compact the database file, removing unused documents and blobs no longer referenced by any documents.

Couchbase Lite's API provides the [CBLDatabase\_PerformMaintenance()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-c/C/html/group%5F%5Fdatabase.html#gaa4b06dcb7427cafeabde8486f5f03f10) method. The available maintenance operations, including `compact` are as shown in the enum [CBLMaintenanceType](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-c/C/html/group%5F%5Fdatabase.html#gaace029f966f053946a52f837c285f156) to accomplish this.

This is a resource intensive operation and is not performed automatically. It should be run on-demand using the API. If in doubt, consult Couchbase support.

## [](#cli-tool)Command Line Tool

`cblite` is a command-line tool for inspecting and querying Couchbase Lite databases.

You can download and build it from the couchbaselabs [GitHub repository](https://github.com/couchbaselabs/couchbase-mobile-tools/blob/master/README.cblite.md). Note that the `cblite` tool is not supported by the [Couchbase Support Policy](https://www.couchbase.com/support-policy).

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