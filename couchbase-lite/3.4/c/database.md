---
title: Databases
description: Working with Couchbase Lite Databases
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.4/modules/c/pages/database.adoc
  xref: xref:3.4@couchbase-lite:c:database.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.4/c/database.html)

# Databases

> Description — _Working with Couchbase Lite Databases_  
> Related Content — [Blobs](blob.md) | [Documents](document.md) | [Indexing](indexing.md)

## [](#database-concepts)Database Concepts

Databases created on Couchbase Lite can share the same hierarchical structure as Capella databases. This makes it easier to sync data between mobile applications and applications built using Capella.

![Couchbase Lite Database Hierarchy](_images/diag-4f601aea7c3c7a95dfed50dc6cda87433165cb94.svg) 

Figure 1\. Couchbase Lite Database Hierarchy

Although the terminology is different, the structure can be mapped to relational database terms:

__Table 1\. Relational Database → Couchbase__
| Relational database | Couchbase  |
| ------------------- | ---------- |
| Database            | Database   |
| Schema              | Scope      |
| Table               | Collection |

This structure gives you plenty of choices when it comes to partitioning your data. The most basic structure is to use the single default scope with a single default collection; or you could opt for a structure that allow you to split your collections into logical scopes.

![Couchbase Lite Examples](_images/diag-9b99b7d1ca54ed2264d303108e1f8cf80af0988b.svg) 

Figure 2\. Couchbase Lite Examples

Storing local configuration

You may not need to sync all the data related for a particular application. You can set up a scope that syncs data, and a second scope that doesn't.

One reason for doing this is to store local configuration data (such as the preferred screen orientation or keyboard layout). Since this information only relates to a particular device, there is no need to sync it:

| local data scope   | Contains information pertaining to the device.                                                                           |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| syncing data scope | Contains information pertaining to the user, which can be synced back to the cloud for use on the web or another device. |

## [](#open-db)Create or Open Database

You can create a new database and-or open an existing database, using the [CBLDatabase](https://docs.couchbase.com/mobile/3.4.0/couchbase-lite-c/C/html/group%5F%5Fdatabase.html) class. Just pass in a database name and optionally a [DatabaseConfiguration](https://docs.couchbase.com/mobile/3.4.0/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Fdatabase%5Fconfiguration.html) — see [Example 1](#ex-dbopen).

Things to watch for include:

* If the named database does not exist in the specified, or default, location then a new one is created
* The database is created in a default location unless you specify a directory for it — see: [DatabaseConfiguration](https://docs.couchbase.com/mobile/3.4.0/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Fdatabase%5Fconfiguration.html) and [CBLDatabaseConfiguration.directory()](https://docs.couchbase.com/mobile/3.4.0/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Fdatabase%5Fconfiguration.html#a844a5e7d02dd4ceb072dff39c7e88591)  
Typically, the default location for C is the application sandbox or current working directory .  
See also [Finding a Database File](#lbl-find-db-loc).

Example 1\. Open or create a database

* C
* C++

```c
// NOTE: No error handling, for brevity (see getting started)
CBLError err = {};
CBLDatabase* db = CBLDatabase_Open(FLSTR("my-database"), NULL, &err);
```

```cpp
// NOTE: No error handling, for brevity (see getting started)
cbl::Database db("my-database");
```

## [](#close-database)Close Database

You are advised to incorporate the closing of all open databases into your application workflow.

To close a database, use [CBLDatabase\_Close()](https://docs.couchbase.com/mobile/3.4.0/couchbase-lite-c/C/html/group%5F%5Fdatabase.html#ga4d448b2d6809d6f9633d810d3ac6dcfa) — see: [Example 2](#ex-dbclose). This also closes active replications, listeners and-or live queries connected to the database.

> [!NOTE]
> Closing a database soon after starting a replication involving it can cause an exception as the asynchronous `replicator (start)` may not yet be `connected`.

Example 2\. Close a Database

* C
* C++

```c
// NOTE: No error handling, for brevity (see getting started)
CBLError err = {};
CBLDatabase_Close(db, &err);
```

```cpp
// NOTE: No error handling, for brevity (see getting started)
db.close();
```

## [](#database-full-sync)Database Full Sync

Database Full Sync prevents the loss of transactional data due to an unexpected system crash or loss of power. This feature is not enabled by default and must be manually set in your database configuration.

> [!CAUTION]
> Database Full Sync is a safe method to prevent data loss but will incur a significant degredation of performance.

Example 3\. Enable Database Full Sync

* C
* C++

```c
// this enables full sync
config.fullSync = true;
```

```cpp
// this enables full sync
config.fullSync = true;
```

> [!NOTE]
> It's' not possible to change the configuration of a Database after instantiating the Database with the configuration by updating its `DatabaseConfiguration` property.

## [](#database-encryption)Database Encryption

> [!IMPORTANT]
> This is an [Enterprise Edition](https://www.couchbase.com/products/editions) feature.

_Couchbase Lite on C_ includes the ability to encrypt Couchbase Lite databases. This allows mobile applications to secure the data at rest, when it is being stored on the device. The algorithm used to encrypt the database is 256-bit AES.

### [](#enabling)Enabling

To enable encryption, use [CBLDatabaseConfiguration.encryptionKey()](https://docs.couchbase.com/mobile/3.4.0/couchbase-lite-c/C/html/struct%5Fc%5Fb%5Fl%5Fdatabase%5Fconfiguration.html#aaab04fb9d092ff02693eea611efefc55) to set the encryption key of your choice. Provide this encryption key every time the database is opened — see [Example 4](#ex-sdb-encrypt).

Example 4\. Configure Database Encryption

* C
* C++

```c
// NOTE: No error handling, for brevity (see getting started)

CBLDatabaseConfiguration config = CBLDatabaseConfiguration_Default();

// This returns a boolean, so check it in production code
CBLEncryptionKey_FromPassword(&config.encryptionKey, FLSTR("password"));

CBLError err = {};
CBLDatabase* db = CBLDatabase_Open(FLSTR("seekrit"), &config, &err);

// Change the encryption key (or add encryption if the DB is unencrypted)
CBLEncryptionKey betterKey;
CBLEncryptionKey_FromPassword(&betterKey, FLSTR("betterpassw0rd"));
CBLDatabase_ChangeEncryptionKey(db, &betterKey, &err);

// Remove encryption
CBLDatabase_ChangeEncryptionKey(db, NULL, &err);
```

```cpp
// NOTE: No error handling, for brevity (see getting started)

cbl::DatabaseConfiguration config{};

// Derive an AES-256 key from a password and set it on the configuration
config.encryptionKey = cbl::EncryptionKey("password");

cbl::Database db("seekrit", config);

// Change the encryption key (or add encryption if the DB is unencrypted)
cbl::EncryptionKey betterKey("betterpassw0rd");
db.changeEncryptionKey(&betterKey);

// Remove encryption
db.changeEncryptionKey(nullptr);
```

### [](#persisting)Persisting

Couchbase Lite does not persist the key. It is the application's responsibility to manage the key and store it in a platform-specific secure store such Android's [Keystore](https://developer.android.com/training/articles/keystore).

### [](#opening)Opening

An encrypted database can only be opened with the same platform that was used to encrypt it in the first place. So a database encrypted using the C SDK, and then exported, is readable only by the C SDK.

### [](#changing)Changing

To change an existing encryption key, open the database using its existing encryption-key and use [CBLDatabase\_ChangeEncryptionKey()](https://docs.couchbase.com/mobile/3.4.0/couchbase-lite-c/C/html/group%5F%5Fdatabase.html#ga76a603bc678ceae18c9610b8a8274a09)to set the required new encryption-key value.

### [](#removing)Removing

To remove encryption, open the database using its existing encryption-key and use [CBLDatabase\_ChangeEncryptionKey()](https://docs.couchbase.com/mobile/3.4.0/couchbase-lite-c/C/html/group%5F%5Fdatabase.html#ga76a603bc678ceae18c9610b8a8274a09)with a null value as the encryption key.

### [](#upgrading)Upgrading

To upgrade an encrypted database see: [Upgrade 1.x databases](dep-upgrade.md#lbl-db-upgrades)

## [](#lbl-find-db-loc)Finding a Database File

When the application is running on the iOS simulator, you can locate the application's sandbox directory using the [SimPholders](https://simpholders.com/3/) utility.

## [](#lbl-db-util)Database Maintenance

From time to time it may be necessary to perform certain maintenance activities on your database, for example to compact the database file, removing unused documents and blobs no longer referenced by any documents.

Couchbase Lite's API provides the [CBLDatabase\_PerformMaintenance()](https://docs.couchbase.com/mobile/3.4.0/couchbase-lite-c/C/html/group%5F%5Fdatabase.html#gaa4b06dcb7427cafeabde8486f5f03f10) method. The available maintenance operations, including `compact` are as shown in the enum [CBLMaintenanceType](https://docs.couchbase.com/mobile/3.4.0/couchbase-lite-c/C/html/group%5F%5Fdatabase.html#gaace029f966f053946a52f837c285f156) to accomplish this.

This is a resource intensive operation and is not performed automatically. It should be run on-demand using the API. If in doubt, consult Couchbase support.

## [](#cli-tool)Command Line Tool

`cblite` is a command-line tool for inspecting and querying Couchbase Lite databases.

You can download and build it from the couchbaselabs [GitHub repository](https://github.com/couchbaselabs/couchbase-mobile-tools/blob/master/README.cblite.md). Note that the `cblite` tool is not supported by the [Couchbase Support Policy](https://www.couchbase.com/support-policy).

## [](#related-content)Related Content

### [](#)

How to . . .

* [Prerequisites](#c:gs-prereqs.adoc)
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