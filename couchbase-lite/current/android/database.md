---
title: Databases
description: Working with Couchbase Lite on Android databases
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.0/modules/android/pages/database.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/couchbase-lite/current/android/database.html)

# Databases

> Description — _Working with Couchbase Lite on Android databases_  
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

You may not need to sync all the data related for a particular application. You can set up a scope that syncs data, and a second scope that doesn’t.

One reason for doing this is to store local configuration data (such as the preferred screen orientation or keyboard layout). Since this information only relates to a particular device, there is no need to sync it:

| local data scope   | Contains information pertaining to the device.                                                                           |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| syncing data scope | Contains information pertaining to the user, which can be synced back to the cloud for use on the web or another device. |

## [](#initializer)Initializer

Your first step in using the API must be to call its initializer. An exception is raised if any other API method is invoked before the initializer.

Example 1\. Initializer code

* Kotlin
* Java

```Kotlin
override fun onCreate() {
    super.onCreate()
    // Initialize the Couchbase Lite system
    CouchbaseLite.init(this)
}
```

```Java
@Override
public void onCreate() {
    super.onCreate();
    // Initialize the Couchbase Lite system
    CouchbaseLite.init(this);
}
```

## [](#open-db)Create or Open Database

You can create a new database and-or open an existing database, using the [Database](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-android/com/couchbase/lite/Database.html) class. Just pass in a database name and optionally a [DatabaseConfiguration](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-android/com/couchbase/lite/DatabaseConfiguration.html) — see [Example 2](#ex-dbopen).

Things to watch for include:

* If the named database does not exist in the specified, or default, location then a new one is created
* The database is created in a default location unless you specify a directory for it — see: [DatabaseConfiguration](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-android/com/couchbase/lite/DatabaseConfiguration.html) and [DatabaseConfiguration.setDirectory()](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-android/com/couchbase/lite/DatabaseConfiguration.html#setDirectory-java.lang.String-)  
Typically, the default location for Android is the application sandbox .  
See also [Finding a Database File](#lbl-find-db-loc).

Example 2\. Open or create a database

* Kotlin
* Java

```Kotlin
val database = Database("my-db") (1)
```

```Java
Database database = new Database(DB_NAME);
```

## [](#close-database)Close Database

You are advised to incorporate the closing of all open databases into your application workflow.

To close a database, use [Database.close()](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-android/com/couchbase/lite/Database.html#close--) — see: [Example 3](#ex-dbclose). This also closes \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]active replications, listeners and-or live queries connected to the database.

> [!NOTE]
> Closing a database soon after starting a replication involving it can cause an exception as the asynchronous `replicator (start)` may not yet be `connected`.

> [!TIP]
> Safely Closing a Database pre 2.8
> 
> Before closing, check that any attached listeners (query/replication/change) indicate they are at least at `connected` status before closing — see for example: [Monitor Status](replication.md#lbl-repl-mon).

Example 3\. Close a Database

* Kotlin
* Java

```Kotlin
database.close()
```

```Java
database.close();
```

## [](#database-full-sync)Database Full Sync

Database Full Sync will prevent the loss of transactional data due to an unexpected system crash or loss of power. This feature is not enabled by default and must be manually set in your database configuration.

> [!CAUTION]
> Database Full Sync is a safe method to prevent data loss but will incur a significant degredation of performance.

Example 4\. Enable Database Full Sync

* Kotlin
* Java

```Kotlin
val db = Database(
    "my-db",
    DatabaseConfigurationFactory.newConfig(
        fullSync = true
    )
)
```

```Java
config.setFullSync(true);
```

> [!NOTE]
> Once a Database is created, its configuration is immutable — modifying the `DatabaseConfiguration` property afterwards has no effect on the existing instance.

## [](#database-encryption)Database Encryption

> [!IMPORTANT]
> This is an [Enterprise Edition](https://www.couchbase.com/products/editions) feature.

_Couchbase Lite on Android_ includes the ability to encrypt Couchbase Lite databases. This allows mobile applications to secure the data at rest, when it is being stored on the device. The algorithm used to encrypt the database is 256-bit AES.

### [](#enabling)Enabling

To enable encryption, use [DatabaseConfiguration.setEncryptionKey()](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-android/com/couchbase/lite/DatabaseConfiguration.html#setEncryptionKey-com.couchbase.lite.EncryptionKey-) to set the encryption key of your choice. Provide this encryption key every time the database is opened — see [Example 5](#ex-sdb-encrypt).

Example 5\. Configure Database Encryption

* Kotlin
* Java

```Kotlin
val db = Database(
    "my-db",
    DatabaseConfigurationFactory.newConfig(
        encryptionKey = EncryptionKey("PASSWORD")
    )
)
```

```Java
DatabaseConfiguration config = new DatabaseConfiguration();
config.setEncryptionKey(new EncryptionKey("PASSWORD"));
Database database = new Database(DB_NAME, config);
```

### [](#persisting)Persisting

Couchbase Lite does not persist the key. It is the application’s responsibility to manage the key and store it in a platform-specific secure store such Android’s [Keystore](https://developer.android.com/training/articles/keystore).

### [](#opening)Opening

An encrypted database can only be opened with the same platform that was used to encrypt it in the first place. So a database encrypted using the Android SDK, and then exported, is readable only by the Android SDK.

### [](#changing)Changing

To change an existing encryption key, open the database using its existing encryption-key and use [Database.changeEncryptionKey()](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-android/com/couchbase/lite/Database.html#changeEncryptionKey%28com.couchbase.lite.EncryptionKey%29)to set the required new encryption-key value.

### [](#removing)Removing

To remove encryption, open the database using its existing encryption-key and use [Database.changeEncryptionKey()](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-android/com/couchbase/lite/Database.html#changeEncryptionKey%28com.couchbase.lite.EncryptionKey%29)with a null value as the encryption key.

### [](#upgrading)Upgrading

To upgrade an encrypted database see: [Upgrade 1.x databases](upgrade.md#lbl-db-upgrades)

## [](#lbl-find-db-loc)Finding a Database File

When the application is running on the Android emulator, you can locate the application’s data folder and access the database file by using the **adb** CLI tools. For example, to list the different databases on the emulator, you can run the following commands.

List

```bash
$ adb shell
$ su
$ cd /data/data/{APPLICATION_ID}/files
$ ls
```

The **adb pull** command can be used to pull a specific database to your host machine.

Example 6\. Pull using adb command

```bash
$ adb root
$ adb pull /data/data/{APPLICATION_ID}/files/{DATABASE_NAME}.cblite2 .
```

## [](#lbl-db-util)Database Maintenance

From time to time it may be necessary to perform certain maintenance activities on your database, for example to compact the database file, removing unused documents and blobs no longer referenced by any documents.

Couchbase Lite’s API provides the [Database.performMaintenance()](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-android/com/couchbase/lite/Database.html#performMaintenance-com.couchbase.lite.MaintenanceType-) method. The available maintenance operations, including `compact` are as shown in the enum [MaintenanceType](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-android/com/couchbase/lite/MaintenanceType.html) to accomplish this.

This is a resource intensive operation and is not performed automatically. It should be run on-demand using the API. If in doubt, consult Couchbase support.

## [](#cli-tool)Command Line Tool

`cblite` is a command-line tool for inspecting and querying Couchbase Lite databases.

You can download and build it from the couchbaselabs [GitHub repository](https://github.com/couchbaselabs/couchbase-mobile-tools/blob/master/README.cblite.md). Note that the `cblite` tool is not supported by the [Couchbase Support Policy](https://www.couchbase.com/support-policy).

## [](#troubleshooting)Troubleshooting

You should use console logs as your first source of diagnostic information. If the information in the default logging level is insufficient you can focus it on database errors and generate more verbose messages — see: [Example 7](#ex-logdb).

For more on using Couchbase logs — see: [Using Logs](new-logging-api.md).

Example 7\. Increase Level of Database Log Messages

* Kotlin
* Java

```Kotlin
LogSinks.get().console = ConsoleLogSink(LogLevel.WARNING) (1)
```

```Java
LogSinks.get().setConsole(new ConsoleLogSink(LogLevel.WARNING)); (1)
```

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

---

[1](#%5Ffootnoteref%5F1). Commencing with Release 2.8