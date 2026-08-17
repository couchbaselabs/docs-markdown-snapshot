---
title: Pre-built Database
description: How to handle pre-built databases in your Couchbase Lite on Android app
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.0/modules/android/pages/prebuilt-database.adoc
  xref: xref:3.0@couchbase-lite:android:prebuilt-database.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.0/android/prebuilt-database.html)

# Pre-built Database

> Description — _How to handle pre-built databases in your Couchbase Lite on Android app_  
> _Abstract — This content explains how to include a snapshot of a pre-built database in your package to shorten initial sync time and reduce bandwidth use_  

## [](#overview)Overview

_Couchbase Lite_\_'s\_ support for pre-built databases means you can pre-load your app with data instead of syncing it down from _Sync Gateway_ during startup. This might benefit, for example, a mobile application developer striving to minimize consumer wait time (arising from data setup) on initial install and launch of the application.

Avoiding an initial bulk sync will help reduce startup time and network transfer costs, leading to a better consumer experience. It is typically more efficient to download bulk data using the http/ftp stream employed during the application installation than to install a smaller application bundle and then have to use a replicator to pull-in the bulk data.

This prepackaging of the data typically applies to public/shared, non-user specific data that is mostly static. Even if the data is not static, you can still benefit from preloading it and only syncing the changed documents on startup

The initial sync of any pre-built database will pull-in any content changes on the server that occurred after its incorporation into the app, quickly bringing the database up to date.

To use a prebuilt database:

1. Create a new Couchbase Lite database with the required data set — see [Creating Pre-built database](#crt-db)
2. Incorporate the pre-built database with your app bundle as an asset/resource — see [Bundle a Database with an Application](#bundle-db)
3. Adjust the start-up logic of your app to check for the presence of the required database.  
If the database doesn't already exist, create one using the bundled pre-built database. Then initiate a sync to update the data — see [Using Pre-built Database on App Launch](#deploy-db)

## [](#crt-db)Creating Pre-built database

These steps should form part of your build and release process:

1. Create a fresh Couchbase Lite database (every time)  
> [!IMPORTANT]  
> **Always start with a fresh database for each app version**; this ensures there are no [checkpoint](refer-glossary.md#checkpoint) issues  
>  
> **Otherwise:** You will invalidate the cached [checkpoint](refer-glossary.md#checkpoint) in the packaged database, and instead reuse the same database in your build process (for subsequent app versions).
2. Pull the data from Sync Gateway into the new Couchbase Lite database  
> [!IMPORTANT]  
> Ensure the replication used to populate Couchbase Lite database **uses the exact same remote URL and replication config parameters (channels and filters)** as those your app will use when it is running.  
>  
> **Otherwise:** …​ there will be a [checkpoint](refer-glossary.md#checkpoint) mismatch and the app will attempt to pull the data down again  
>  
> So don't, for instance, create a pre-built database against a staging Sync Gateway server and try to use that within a production app that syncs against a production Sync Gateway.  
You can use the cblite tool (`cblite cp`) for this — see: [cblite cp (export, import, push, pull)](https://github.com/couchbaselabs/couchbase-mobile-tools/blob/master/Documentation.md#cp-aka-export-import-push-pull) | [cblite on GitHub](https://github.com/couchbaselabs/couchbase-mobile-tools/blob/master/README.cblite.md)

**Alternatively** …​

  * You can write a simple CBL app to just initiate the required pull sync — see: [Remote Sync Gateway](replication.md)
  * A third party community Java app is available. It provides a UI to create a local Couchbase Lite database and pull data from a Sync Gateway database — see: [CouchbaseLite Tester](https://github.com/Infosys/CouchbaseLiteTester)  
  > [!NOTE]  
  > Couchbase accepts no responsibility for the ongoing availability, maintenance or support of this third party community contribution, nor for the provision of support for issues arising from its use.
3. Create the **same** indexes the app will use (wait for the replication to finish before doing this).

## [](#bundle-db)Bundle a Database with an Application

Copy the database into your app package.

Put it in an appropriate place (for example, an assets or resource folder).

Where the platform permits you can zip the database.

**Alternatively** …​ rather than bundling the database within the app, the app could pull the database down from a CDN server on launch.

## [](#database-encryption)Database Encryption

> [!IMPORTANT]
> This is an [Enterprise Edition](https://www.couchbase.com/products/editions) feature.

If you are using en encrypted database, note that [Database.copy()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/Database.html#copy%28java.io.File,java.lang.String,com.couchbase.lite.DatabaseConfiguration%29)does not change the encryption key. The encryption key specified in the config when opening the database is the encryption key used for both the original database and copied database.

If you copied an un-encrypted database and want to apply encryption to the copy, or if you want to change (or remove) the encryption key applied to the copy:

1. Provide the original encryption-key (if any) in the database copy's configuration using [DatabaseConfiguration.setEncryptionKey()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/DatabaseConfiguration.html#setEncryptionKey-com.couchbase.lite.EncryptionKey-)
2. Open the database copy
3. Use [Database.changeEncryptionKey()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/Database.html#changeEncryptionKey%28com.couchbase.lite.EncryptionKey%29) on the database copy to set the required encryption key.  
NOTE: To remove encryption on the copy, provide a null encryption-key

## [](#deploy-db)Using Pre-built Database on App Launch

During the application start-up logic, check if database exists in the required location, and **if not**:

1. Locate the pre-packaged database (for example, in the assets or other resource folder)
2. Copy the pre-packaged database to the required location  
Use the API's [Database.copy()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/Database.html#copy%28java.io.File,java.lang.String,com.couchbase.lite.DatabaseConfiguration%29) method — see: [Example 1](#lbl-code); this ensures that a UUID is generated for each copy  
> [!IMPORTANT]  
> **Do not copy the database using any other method**  
> **Otherwise:** Each copy of the app will invalidate the other apps' [checkpoints](refer-glossary.md#checkpoint) because a new UUID was not generated.
3. Open the database; you can now start querying the data and using it
4. Start a pull replication, to sync any changes  
The replicator uses the pre-built database's [checkpoint](refer-glossary.md#checkpoint) as the timestamp to sync from; only documents changed since then are synced  
> [!IMPORTANT]  
> If you used cblite to pull the data **without including a port number with the URL** and are replicating in a Java or iOS (swift/ObjC) app — **you must include the port number in the URL provided to the replication** (port 443 for `wss://` or 80 for `ws://`).  
>  
> **Otherwise:** You will get a [checkpoint](refer-glossary.md#checkpoint) mismatch.  
> This is caused by a URL discrepancy, which arises because `cblite` automatically adds the default port number when none is specified, **but** the Java and iOS (swift/ObjC) replicators DO NOT.  
> [!NOTE]  
> Start your normal application logic immediately, unless it is essential to have the absolute up-to-date data set to begin. That way the user is not kept hanging around watching a progress indicator. They can begin interacting with your app whilst any out-of-data data is being updated.

Example 1\. Copy database using API

* Kotlin
* Java

```Kotlin
// Note: Getting the path to a database is platform-specific.
// For Android you need to extract the database from your assets
// to a temporary directory and then copy it, using Database.copy()
if (Database.exists("travel-sample", context.filesDir)) {
    return
}
ZipUtils.unzip(PlatformUtils.getAsset("travel-sample.cblite2.zip"), context.filesDir)
Database.copy(
    File(context.filesDir, "travel-sample"),
    "travel-sample",
    DatabaseConfiguration()
)
```

```Java
// Note: Getting the path to a database is platform-specific.
// For Android you need to extract it from your
// assets to a temporary directory and then pass that path to Database.copy()
DatabaseConfiguration configuration = new DatabaseConfiguration();
if (!Database.exists("travel-sample", context.getFilesDir())) {
      ZipUtils.unzip(getAsset("travel-sample.cblite2.zip"), context.getFilesDir());
      File path = new File(context.getFilesDir(), "travel-sample");
      try {
          Database.copy(path, "travel-sample", configuration);
      } catch (CouchbaseLiteException e) {
          e.printStackTrace();
      }
  }
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