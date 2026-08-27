---
title: Databases&#8201;&#8212;&#8201;Data Model
description: Working with Couchbase Lite on Android databases
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/android/pages/database.adoc
  xref: xref:2.8@couchbase-lite:android:database.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/android/database.html)

# Databases&#8201;&#8212;&#8201;Data Model

> Description — _Working with Couchbase Lite on Android databases_  
> Related Content — [Blobs](../../current/android/blob.md) | [Documents](../../current/android/document.md) | [Indexing](../../current/android/indexing.md)

## [](#initializer)Initializer

Your first step in using the API must be to call its initializer. An exception is raised if any other API method is invoked before the initializer.

Example 1\. Initializer code

```Java
// Initialize the Couchbase Lite system
CouchbaseLite.init(context);
```

## [](#open-db)Create or Open Database

You can create a new database and-or open and existing database, using the [Database](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-android/com/couchbase/lite/Database.html) class. Just pass in a database name and optionally a [DatabaseConfiguration](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-android/com/couchbase/lite/DatabaseConfiguration.html) — see [Example 2](#ex-dbopen).

Things to watch for include:

* Opening/Creating a database is an asynchronous process
* If the named database does not exist in the specified, or default, location then a new one is created
* The database is created in a default location unless you specify a directory for it — see: [DatabaseConfiguration](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-android/com/couchbase/lite/DatabaseConfiguration.html) and [DatabaseConfiguration.setDirectory()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-android/com/couchbase/lite/DatabaseConfiguration.html#setDirectory-java.lang.String-)  
> [!TIP]  
> Best Practice is to always specify the path to the database explicitly.  
Typically, the default location for Android is the application sandbox.  
See also [Finding a Database File](#lbl-find-db-loc).

Example 2\. Open or create a database

```Java
final DatabaseConfiguration config = new DatabaseConfiguration();
config.setDirectory(context.getFilesDir().getAbsolutePath()); (1)

Database database = new Database("my-database", config);
```

| **1** | Here we are specifying the database directory path. |
| ----- | --------------------------------------------------- |

## [](#close-database)Close Database

You are advised to incorporate the closing of all open databases into your application workflow.

Closing a database is a simple, just use [Database.close()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-android/com/couchbase/lite/Database.html#close--) — see: [Example 3](#ex-dbclose).  
However, there are a number of things to be aware of:

* Closing a database is a **synchronous** operation, it is effective immediately
* You cannot close a database that is not open.  
Remember that opening (or creating) a database is asynchronous. So issuing a close immediately after initiating an open/create, may result in an error if that process has not completed.
* Closing a database \[[1](#%5Ffootnotedef%5F1 "View footnote.")\] also closes any active replications, listeners and-or live queries attached to the database.  
Closing a database immediately after kicking-off a replication could cause the sync to generate an exception.  
For example:  
`IllegalStateException: Attempt to perform an operation on a closed database`

Example 3\. Close a Database

```Java
database.close()
```

## [](#database-encryption)Database Encryption

> [!IMPORTANT]
> This is an [Enterprise Edition](https://www.couchbase.com/products/editions) feature.

_Couchbase Lite on Android_ includes the ability to encrypt Couchbase Lite databases. This allows mobile applications to secure the data at rest, when it is being stored on the device. The algorithm used to encrypt the database is 256-bit AES.

To enable encryption, you must set the `DatabaseConfiguration.encryptionKey` property to the encryption key of your choice. Provide this encryption key every time the database is opened.

```Java
DatabaseConfiguration config = new DatabaseConfiguration();
config.setEncryptionKey(new EncryptionKey("PASSWORD"));
Database database = new Database("mydb", config);
```

Couchbase Lite does not persist the key. It is the application's responsibility to manage the key and store it in a platform specific secure store such as Apple's [Keychain](https://developer.apple.com/documentation/security/keychain%5Fservices) or Android's [Keystore](https://developer.android.com/training/articles/keystore).

An encrypted database can only be opened with the same language SDK that was used to encrypt it in the first place (Swift, C#, Java, Java (Android) or Objective-C). For example, if a database is encrypted with the Swift SDK and then exported, it will only be readable with the Swift SDK.

#### [](#upgrading-from-1-x-when-encryption-is-enabled)Upgrading from 1.x when Encryption is Enabled

If you're migrating an application from Couchbase Lite 1.x to 2.x, note that the [automatic database upgrade](#database-upgrade) functionality is **not supported** for encrypted databases. Thus, to upgrade an encrypted 1.x database, you should do the following:

1. Disable encryption using the Couchbase Lite 1.x framework (see [1.x encryption guide](https://docs-archive.couchbase.com/couchbase-lite/1.4/java-android.html#database-encryption))
2. Open the database file with encryption enabled using the Couchbase Lite 2.x framework.

Since it is not possible to package Couchbase Lite 1.x and Couchbase Lite 2.x in the same application this upgrade path would require two successive upgrades. If you are using Sync Gateway to synchronize the database content, it may be preferable to run a pull replication from a new 2.x database with encryption enabled and delete the 1.x local database.

## [](#lbl-find-db-loc)Finding a Database File

When the application is running on the Android emulator, you can locate the application's data folder and access the database file by using the **adb** CLI tools. For example, to list the different databases on the emulator, you can run the following commands.

List

```{console}
$ adb shell
$ su
$ cd /data/data/{APPLICATION_ID}/files
$ ls
```

The **adb pull** command can be used to pull a specific database to your host machine.

Example 4\. Pull using adb command

```{console}
$ adb root
$ adb pull /data/data/{APPLICATION_ID}/files/{DATABASE_NAME}.cblite2 .
```

## [](#lbl-db-util)Database Maintenance

From time to time it may be necessary to perform certain maintenance activities on your database, for example to compact the database file, removing unused documents and blobs no longer referenced by any documents.

Couchbase Lite's API provides the [Database.performMaintenance()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-android/com/couchbase/lite/Database.html#performMaintenance-com.couchbase.lite.MaintenanceType-) method. The available maintenance operations, including `compact` are as shown in the enum [MaintenanceType](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-android/com/couchbase/lite/MaintenanceType.html) to accomplish this.

This is a resource intensive operation and is not performed automatically. It should be run on-demand using the API. If in doubt, consult Couchbase support.

## [](#cli-tool)Command Line Tool

`cblite` is a command-line tool for inspecting and querying Couchbase Lite 2.x databases.

You can download and build it from the couchbaselabs [GitHub repository](https://github.com/couchbaselabs/couchbase-mobile-tools/blob/master/README.cblite.md). Note that the `cblite` tool is not supported by the [Couchbase Support Policy](https://www.couchbase.com/support-policy).

## [](#troubleshooting)Troubleshooting

You should use Couchbase's console logs as your first source of diagnostic information. If the information in the default logging level is insufficient you can focus it on database errors and generate more verbose messages — see: [Example 5](#ex-logdb).

For more on using Couchbase logs — see: [Using Logs](#couchbase-lite:android:troubleshooting-logs.adoc).

Example 5\. Increase Level of Database Log Messages

```Java
Database.log.getConsole().setDomain(LogDomain.DATABASE);
```

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Prerequisites](../../current/android/gs-prereqs.md)
* [Install](../../current/android/gs-install.md)
* [Build and Run](../../current/android/gs-build.md)

###### [](#-2)

Learn more . . .

* [Databases](../../current/android/database.md)
* [Documents](../../current/android/document.md)
* [Blobs](../../current/android/blob.md)
* [Remote Sync using Sync Gateway](../../current/android/replication.md)
* [Handling Data Conflicts](../../current/android/conflict.md)

###### [](#-3)

Dive Deeper . . .

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)

---

[1](#%5Ffootnoteref%5F1). Commencing with Release 2.8