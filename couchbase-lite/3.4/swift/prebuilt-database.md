---
title: Pre-built Database
description: How to handle pre-built databases in your Couchbase Lite on Swift app
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.4/modules/swift/pages/prebuilt-database.adoc
  xref: xref:3.4@couchbase-lite:swift:prebuilt-database.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.4/swift/prebuilt-database.html)

# Pre-built Database

> Description — _How to handle pre-built databases in your Couchbase Lite on Swift app_  
> _Abstract — This content explains how to include a snapshot of a pre-built database in your package to shorten initial sync time and reduce bandwidth use_  

## [](#overview)Overview

_Couchbase Lite_ supports pre-built databases. You can pre-load your app with data instead of syncing it from \_pass:q,a\[Sync Gateway\_\] during startup to minimize consumer wait time (arising from data setup) on initial install and launch of the application.

Avoiding an initial bulk sync reduces startup time and network transfer costs.

It is typically more efficient to download bulk data using the http/ftp stream employed during the application installation than to install a smaller application bundle and then use a replicator to pull in the bulk data.

Pre-loaded data is typically public/shared, non-user-specific data that is static. Even if the data is not static, you can still benefit from preloading it and only syncing the changed documents on startup.

The initial sync of any pre-built database pulls in any content changes on the server that occurred after its incorporation into the app, updating the database.

To use a prebuilt database:

1. Create a new Couchbase Lite database with the required dataset — see [Creating Pre-built database](#crt-db)
2. Incorporate the pre-built database with your app bundle as an asset/resource — see [Bundle a Database with an Application](#bundle-db)
3. Adjust the start-up logic of your app to check for the presence of the required database.  
If the database doesn't already exist, create one using the bundled pre-built database. Initiate a sync to update the data — see [Using Pre-built Database on App Launch](#deploy-db)

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
> Don't, for instance, create a pre-built database against a staging Sync Gateway server and use it within a production app that syncs against a production Sync Gateway.  
You can use the cblite tool (`cblite cp`) for this — see: [cblite cp (export, import, push, pull)](https://github.com/couchbaselabs/couchbase-mobile-tools/blob/master/Documentation.md#cp-aka-export-import-push-pull) | [cblite on GitHub](https://github.com/couchbaselabs/couchbase-mobile-tools/blob/master/README.cblite.md)

**Alternatively** …​

  * You can write a simple CBL app to just initiate the required pull sync — see: [Remote Sync Gateway](replication.md)
  * A third party community Java app is available. It provides a UI to create a local Couchbase Lite database and pull data from a Sync Gateway database — see: [CouchbaseLite Tester](https://github.com/Infosys/CouchbaseLiteTester)  
  > [!NOTE]  
  > Couchbase accepts no responsibility for the ongoing availability, maintenance, or support of this third party community contribution, nor for the provision of support for issues arising from its use.
3. Create the **same** indexes the app will use (wait for the replication to finish before doing this).

## [](#bundle-db)Bundle a Database with an Application

Copy the database into your app package.

Put it in an appropriate place (for example, an assets or resource folder).

Where the platform permits you can zip the database.

**Alternatively** …​ rather than bundling the database within the app, the app could pull the database down from a CDN server on launch.

## [](#database-encryption)Database Encryption

> [!IMPORTANT]
> This is an [Enterprise Edition](https://www.couchbase.com/products/editions) feature.

If you are using an encrypted database, [Database.copy()](https://docs.couchbase.com/mobile/3.4.0/couchbase-lite-swift/Classes/Database.html#/s:18CouchbaseLiteSwift8DatabaseeC4copy8fromPath02toD010withConfigySS%5FSSAA0D13ConfigurationCSgtKFZ)does not change the encryption key. The encryption key specified in the config when opening the database is the encryption key used for both the original database and copied database.

If you copied an un-encrypted database and want to apply encryption to the copy, or if you want to change (or remove) the encryption key applied to the copy:

1. Provide the original encryption-key (if any) in the database copy's configuration using [DatabaseConfiguration.encryptionKey()](https://docs.couchbase.com/mobile/3.4.0/couchbase-lite-swift/Structs/DatabaseConfiguration.html#/s:18CouchbaseLiteSwift21DatabaseConfigurationV13encryptionKeyAA010EncryptionG0OSgvp)
2. Open the database copy
3. Use [Database.changeEncryptionKey()](https://docs.couchbase.com/mobile/3.4.0/couchbase-lite-swift/Classes/Database.html#/s:18CouchbaseLiteSwift8DatabaseC19changeEncryptionKeyyyAA0fG0OSgKF) on the database copy to set the required encryption key.  
NOTE: To remove encryption on the copy, provide a null encryption-key

## [](#deploy-db)Using Pre-built Database on App Launch

During the application start-up logic, check if database exists in the required location, and **if not**:

1. Locate the pre-packaged database (for example, in the assets or other resource folder)
2. Copy the pre-packaged database to the required location  
Use the API's [Database.copy()](https://docs.couchbase.com/mobile/3.4.0/couchbase-lite-swift/Classes/Database.html#/s:18CouchbaseLiteSwift8DatabaseeC4copy8fromPath02toD010withConfigySS%5FSSAA0D13ConfigurationCSgtKFZ) method — see: [Example 1](#lbl-code); this ensures that a UUID is generated for each copy  
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

```swift
// Note: Getting the path to a database is platform-specific.
// For iOS you need to get the path from the main bundle.
let path = Bundle.main.path(forResource: "travel-sample", ofType: "cblite2")!
if !Database.exists(withName: "travel-sample") {
    do {
        try Database.copy(fromPath: path, toDatabase: "travel-sample", withConfig: nil)
    } catch {
        fatalError("Could not load pre-built database")
    }
}
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