---
title: Databases
description: Working with Couchbase Lite on Android databases
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.0/modules/android/pages/database.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:3.0@couchbase-lite:android:database.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.0/android/database.html)

# Databases

> Description — _Working with Couchbase Lite on Android databases_  
> Related Content — [Blobs](blob.md) | [Documents](document.md) | [Indexing](indexing.md)

## [](#initializer)Initializer

Your first step in using the API must be to call its initializer. An exception is raised if any other API method is invoked before the initializer.

Example 1\. Initializer code

* Kotlin
* Java

```Kotlin
// Initialize the Couchbase Lite system
CouchbaseLite.init(context)
```

```Java
// Initialize the Couchbase Lite system
CouchbaseLite.init(context);
```

## [](#open-db)Create or Open Database

You can create a new database and-or open an existing database, using the [Database](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/Database.html) class. Just pass in a database name and optionally a [DatabaseConfiguration](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/DatabaseConfiguration.html) — see [Example 2](#ex-dbopen).

Things to watch for include:

* If the named database does not exist in the specified, or default, location then a new one is created
* The database is created in a default location unless you specify a directory for it — see: [DatabaseConfiguration](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/DatabaseConfiguration.html) and [DatabaseConfiguration.setDirectory()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/DatabaseConfiguration.html#setDirectory-java.lang.String-)  
> [!TIP]  
> Best Practice is to always specify the path to the database explicitly.  
Typically, the default location for Android is the application sandbox .  
See also [Finding a Database File](#lbl-find-db-loc).

Example 2\. Open or create a database

* Kotlin
* Java

```Kotlin
val database = Database(
    "my-db",
    DatabaseConfigurationFactory.create(
        context.filesDir.absolutePath
    )
) (1)
```

```Java
final DatabaseConfiguration config = new DatabaseConfiguration();
config.setDirectory(context.getFilesDir().getAbsolutePath()); (1)

Database database = new Database("my-database", config);
```

## [](#close-database)Close Database

You are advised to incorporate the closing of all open databases into your application workflow.

Closing a database is simple, just use [Database.close()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/Database.html#close--) — see: [Example 3](#ex-dbclose). This also closes \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]active replications, listeners and-or live queries connected to the database.

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

## [](#database-encryption)Database Encryption

> [!IMPORTANT]
> This is an [Enterprise Edition](https://www.couchbase.com/products/editions) feature.

_Couchbase Lite on Android_ includes the ability to encrypt Couchbase Lite databases. This allows mobile applications to secure the data at rest, when it is being stored on the device. The algorithm used to encrypt the database is 256-bit AES.

### [](#enabling)Enabling

To enable encryption, use [DatabaseConfiguration.setEncryptionKey()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/DatabaseConfiguration.html#setEncryptionKey-com.couchbase.lite.EncryptionKey-) to set the encryption key of your choice. Provide this encryption key every time the database is opened — see [Example 4](#ex-sdb-encrypt).

Example 4\. Configure Database Encryption

* Kotlin
* Java

```Kotlin
val db = Database(
    "my-db",
    DatabaseConfigurationFactory.create(
        encryptionKey = EncryptionKey("PASSWORD")
    )
)
```

```Java
DatabaseConfiguration config = new DatabaseConfiguration();
config.setEncryptionKey(new EncryptionKey("PASSWORD"));
Database database = new Database("mydb", config);
```

### [](#persisting)Persisting

Couchbase Lite does not persist the key. It is the application’s responsibility to manage the key and store it in a platform specific secure store such as Apple’s [Keychain](https://developer.apple.com/documentation/security/keychain%5Fservices) or Android’s [Keystore](https://developer.android.com/training/articles/keystore).

### [](#opening)Opening

An encrypted database can only be opened with the same language SDK that was used to encrypt it in the first place. So a database encrypted using the Android SDK, and then exported, is readable only by the Android SDK.

### [](#changing)Changing

To change an existing encryption key, open the database using its existing encryption-key and use [Database.changeEncryptionKey()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/Database.html#changeEncryptionKey%28com.couchbase.lite.EncryptionKey%29)to set the required new encryption-key value.

### [](#removing)Removing

To remove encryption, open the database using its existing encryption-key and use [Database.changeEncryptionKey()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/Database.html#changeEncryptionKey%28com.couchbase.lite.EncryptionKey%29)with a null value as the encryption key.

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

Example 5\. Pull using adb command

```bash
$ adb root
$ adb pull /data/data/{APPLICATION_ID}/files/{DATABASE_NAME}.cblite2 .
```

## [](#lbl-db-util)Database Maintenance

From time to time it may be necessary to perform certain maintenance activities on your database, for example to compact the database file, removing unused documents and blobs no longer referenced by any documents.

Couchbase Lite’s API provides the [Database.performMaintenance()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/Database.html#performMaintenance-com.couchbase.lite.MaintenanceType-) method. The available maintenance operations, including `compact` are as shown in the enum [MaintenanceType](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/MaintenanceType.html) to accomplish this.

This is a resource intensive operation and is not performed automatically. It should be run on-demand using the API. If in doubt, consult Couchbase support.

## [](#cli-tool)Command Line Tool

`cblite` is a command-line tool for inspecting and querying Couchbase Lite databases.

You can download and build it from the couchbaselabs [GitHub repository](https://github.com/couchbaselabs/couchbase-mobile-tools/blob/master/README.cblite.md). Note that the `cblite` tool is not supported by the [Couchbase Support Policy](https://www.couchbase.com/support-policy).

## [](#troubleshooting)Troubleshooting

You should use console logs as your first source of diagnostic information. If the information in the default logging level is insufficient you can focus it on database errors and generate more verbose messages — see: [Example 6](#ex-logdb).

For more on using Couchbase logs — see: [Using Logs](troubleshooting-logs.md).

Example 6\. Increase Level of Database Log Messages

* Kotlin
* Java

```Kotlin
Database.log.console.domains = EnumSet.of(LogDomain.DATABASE) (1)
```

```Java
Database.log.getConsole().setDomain(LogDomain.DATABASE);
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