---
title: Pre-built Database
description: How to handle pre-built databases in your Couchbase Lite on Android app
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.0/modules/android/pages/prebuilt-database.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/couchbase-lite/current/android/prebuilt-database.html)

# Pre-built Database

> Description — _How to handle pre-built databases in your Couchbase Lite on Android app_  
> _Abstract — This content explains how to include a snapshot of a pre-built database in your package to shorten initial sync time and reduce bandwidth use_  

## [](#when-to-use)When to Use Pre-built Databases

Pre-built databases solve the "slow initial sync" problem for applications that require large datasets to be available on first launch.

### [](#typical-use-cases)Typical Use Cases

Use pre-built databases when your app has:

* Large reference datasets that users need faster access to, such as:

  * Product catalogs with hundreds of thousands of items.
  * Geographic or mapping data.
  * Medical or pharmaceutical references.
  * Legal or regulatory documentation.
  * Educational content libraries.
* Unacceptably long initial sync times from Sync Gateway (for example, 30+ minutes for large datasets).
* Bandwidth-constrained users with limited, expensive, or unreliable network connectivity.
* Offline-first requirements where the app must function before any network sync completes.

### [](#problem-solved)Problem Solved

Without pre-built databases, users must wait while your app syncs the entire dataset from Sync Gateway on first launch. For large datasets, this can mean wait times of 30-40 minutes or longer, depending on dataset size, document complexity, and network conditions.

**Example scenario:** a field service application includes a product catalog with hundreds of thousands of items. Without a pre-built database, each user would need to sync the entire catalog on first launch—potentially taking 30-40 minutes or more over cellular networks.

By bundling a pre-built database with the app, users have immediate access to the catalog. On first launch, the app only syncs items that changed after the build process, potentially reducing the wait time to under a minute

### [](#key-benefits)Key Benefits

* **Dramatically reduced initial sync time:** Users can begin using your app instead of waiting for large initial sync to complete.
* **Lower bandwidth consumption:** Only document changes sync across the network, not the entire dataset.
* **Better offline experience:** Full dataset available even before first sync.
* **Improved user experience:** Users are not blocked by lengthy data downloads on first launch.

### [](#when-not-to-use-pre-built-databases)When NOT to Use Pre-built Databases

Pre-built databases may not be appropriate when:

* Small datasets where initial sync completes in seconds or minutes.
* Highly dynamic data where most documents change frequently between app releases.
* User-specific data that varies per user (pre-built databases are for shared, non-user-specific data).
* Strict app size constraints where adding the database impacts your app bundle size.
* Frequent app updates where the effort of rebuilding and bundling the database outweighs the sync time savings.

## [](#overview)Overview

Couchbase Lite supports pre-built databases. You can pre-load your app with data instead of syncing it from Sync Gateway during startup to minimize consumer wait time (arising from data setup) on initial install and launch of the application.

Avoiding an initial bulk sync reduces startup time and network transfer costs.

It’s typically more efficient to download bulk data using the http/ftp stream employed during the application installation than to install a smaller application bundle and then use a replicator to pull in the bulk data.

Pre-loaded data is typically public/shared, non-user-specific data that’s static. Even if the data is not static, you can still benefit from preloading it and only syncing the changed documents on startup.

The initial sync of any pre-built database pulls in any content changes on the server that occurred after its incorporation into the app, updating the database.

To use a prebuilt database:

1. Create a new Couchbase Lite database with the required dataset — see [Creating Pre-built database](#crt-db)
2. Incorporate the pre-built database with your app bundle as an asset/resource — see [Bundle a Database with an Application](#bundle-db)
3. Adjust the start-up logic of your app to check for the presence of the required database.  
If the database does not already exist, create one using the bundled pre-built database. Start a sync to update the data — see [Using Pre-built Database on App Launch](#deploy-db).

## [](#crt-db)Creating Pre-built database

These steps should form part of your build and release process:

1. Create a fresh Couchbase Lite database (every time).  
> [!IMPORTANT]  
> Always start with a fresh database for each app version as this ensures there are no [checkpoint](refer-glossary.md#checkpoint) issues.  
>  
> **Otherwise:** you invalidate the cached [checkpoint](refer-glossary.md#checkpoint) in the packaged database, and instead reuse the same database in your build process (for subsequent app versions).
2. Pull the data from Sync Gateway into the new Couchbase Lite database.  
> [!IMPORTANT]  
> Ensure the replication used to populate Couchbase Lite database **uses the exact same remote URL and replication config parameters (channels and filters)** as those your app uses when it’s running.  
>  
> **Otherwise:** …​ there is a [checkpoint](refer-glossary.md#checkpoint) mismatch and the app attempts to pull the data again.  
>  
> Do not create a pre-built database against a staging Sync Gateway server and use it within a production app that syncs against a production Sync Gateway.  
You can use the `cblite cp` tool for this — see: [cblite cp (export, import, push, pull)](https://github.com/couchbaselabs/couchbase-mobile-tools/blob/master/Documentation.md#cp-aka-export-import-push-pull) | [cblite on GitHub](https://github.com/couchbaselabs/couchbase-mobile-tools/blob/master/README.cblite.md).

**Alternatively**

  * You can write a simple CBL app to start a pull sync — see: [Remote Sync Gateway](replication.md).
  * A third party community Java app is available. It provides a UI to create a local Couchbase Lite database and pull data from a Sync Gateway database — see: [CouchbaseLite Tester](https://github.com/Infosys/CouchbaseLiteTester).  
  > [!NOTE]  
  > Couchbase accepts no responsibility for the ongoing availability, maintenance, or support of this third party community contribution, nor for the provision of support for issues arising from its use.
3. Create the **same** indexes the app uses (wait for the replication to finish before doing this).

## [](#bundle-db)Bundle a Database with an Application

Copy the database into your app package.

You can zip the database where the platform permits.

Alternatively you can pull the database from a CDN on launch instead of bundling it within the app.

## [](#database-encryption)Database Encryption

> [!IMPORTANT]
> This is an [Enterprise Edition](https://www.couchbase.com/products/editions) feature.

If you’re using an encrypted database, [Database.copy()](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-android/com/couchbase/lite/Database.html#copy%28java.io.File,java.lang.String,com.couchbase.lite.DatabaseConfiguration%29)does not change the encryption key. The encryption key specified in the config when opening the database is the encryption key used for both the original database and copied database.

If you copied an un-encrypted database and want to apply encryption to the copy, or if you want to change (or remove) the encryption key applied to the copy:

1. Provide the original encryption-key (if any) in the database copy’s configuration using [DatabaseConfiguration.setEncryptionKey()](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-android/com/couchbase/lite/DatabaseConfiguration.html#setEncryptionKey-com.couchbase.lite.EncryptionKey-)
2. Open the database copy
3. Use [Database.changeEncryptionKey()](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-android/com/couchbase/lite/Database.html#changeEncryptionKey%28com.couchbase.lite.EncryptionKey%29) on the database copy to set the required encryption key.  
NOTE: To remove encryption on the copy, provide a null encryption-key

## [](#deploy-db)Using Pre-built Database on App Launch

During the application start-up logic, check if database exists in the required location, and **if not**:

1. Locate the pre-packaged database (for example, in the assets or other resource folder)
2. Copy the pre-packaged database to the required location  
Use the API’s [Database.copy()](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-android/com/couchbase/lite/Database.html#copy%28java.io.File,java.lang.String,com.couchbase.lite.DatabaseConfiguration%29) method — see: [Example 1](#lbl-code). This ensures that a UUID is generated for each copy.  
> [!IMPORTANT]  
> **Do not copy the database using any other method**  
> **Otherwise:** Each copy of the app invalidates the other apps' [checkpoints](refer-glossary.md#checkpoint) because a new UUID was not generated.
3. Open the database, you can now start querying the data and using it.
4. Start a pull replication, to sync any changes.  
The replicator uses the pre-built database’s [checkpoint](refer-glossary.md#checkpoint) as the timestamp to sync from, syncing only documents changed since then.  
> [!IMPORTANT]  
> If you used cblite to pull the data **without including a port number with the URL** and are replicating in a Java or iOS (swift/ObjC) app — **you must include the port number in the URL provided to the replication** (port 443 for `wss://` or 80 for `ws://`).  
>  
> **Otherwise:** you get a [checkpoint](refer-glossary.md#checkpoint) mismatch.  
> This is caused by a URL discrepancy, which arises because `cblite` automatically adds the default port number when none is specified, **but** the Java and iOS (swift/ObjC) replicators DO NOT.  
> [!NOTE]  
> Start your normal application logic immediately, unless it’s essential to have the absolute up-to-date data set to begin. That way the user is not kept hanging around watching a progress indicator. They can begin interacting with your app while any out-of-date data is being updated.

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
ZipUtils.unzip(getAsset("travel-sample.cblite2.zip"), context.filesDir)
Database.copy(
    File(context.filesDir, "travel-sample"),
    "travel-sample",
    DatabaseConfiguration()
)
```

```Java
// Note: Getting the path to a database is platform-specific.
if (!Database.exists("travel-sample", appDbDir)) {
    File tmpDir = new File(System.getProperty("java.io.tmpdir"));
    ZipUtils.unzip(Utils.getAsset("travel-sample.cblite2.zip"), tmpDir);
    File path = new File(tmpDir, "travel-sample");
    Database.copy(path, "travel-sample", new DatabaseConfiguration());
}
```

## [](#troubleshooting)Troubleshooting

### [](#initial-sync-still-takes-too-long)Initial Sync Still Takes Too Long

If you’re using a pre-built database but initial sync is still slow:

**Check checkpoint matching:**

* Ensure the pre-built database was created using the exact same Sync Gateway URL, including port number (`:80` or `:443`)
* Verify replication config parameters (channels, filters) match exactly between database creation and app usage
* Confirm you’re using `Database.copy()` API, not manual file copy, to preserve the database UUID

**Verify database freshness:**

* If your pre-built database is many weeks or months old, a large number of documents may have changed since you created it
* Consider rebuilding your pre-built database more frequently (for example, with each app release or monthly)

**Evaluate your dataset:**

* If most documents change frequently between releases, pre-built databases provide less benefit
* Consider whether channel filtering could reduce your dataset size

### [](#users-report-long-wait-times-on-first-launch)Users Report Long Wait Times on First Launch

If users still experience delays despite using pre-built databases:

Do not block on sync completion:

* Start your app UI immediately after copying the pre-built database
* Let sync happen in the background while users interact with the (already available) data
* Show "Checking for updates…​" rather than "Loading data…​"

**Optimize the database copy operation:**

* Make sure adequate storage space is available
* Consider device performance characteristics (older devices with slower storage)

### [](#app-bundle-size-too-large)App Bundle Size Too Large

If bundling the database makes your app too large:

* **Compress the database:** Zip the database file before bundling (if your platform permits)
* **Use CDN delivery:** Download the pre-built database from a CDN on first launch instead of bundling in the app
* **Evaluate data necessity:** Can you reduce the pre-loaded dataset? Consider loading only critical data pre-built and lazily syncing less critical data

## [](#related-content)Related Content

### [](#)

How to . . .

* [Prerequisites](gs-prereqs.md)
* [Install](gs-install.md)
* [Build and Run](gs-build.md)

### [](#-2)

Learn more . . .

* [Databases](database.md)
* [Documents](document.md)
* [Blobs](blob.md)
* [Remote Sync Gateway](replication.md)
* [Handling Data Conflicts](conflict.md)

### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)