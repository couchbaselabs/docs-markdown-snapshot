---
title: Pre-built Database
description: How to handle pre-built databases in your Couchbase Lite on Swift app
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/swift/pages/prebuilt-database.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.8@couchbase-lite:swift:prebuilt-database.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/swift/prebuilt-database.html)

# Pre-built Database

> Description — _How to handle pre-built databases in your Couchbase Lite on Swift app_  
> _Abstract — This content explains how to include a snapshot of a pre-built database in your package to shorten initial sync time and reduce bandwidth use_  

## [](#overview)Overview

Couchbase Lite’s support for pre-built databases means you can pre-load your app with data instead of syncing it down from Sync Gateway during startup. This might benefit, for example, a mobile application developer striving to minimize consumer wait time (arising from data setup) on initial install and launch of the application.

Avoiding an initial bulk sync will help reduce startup time and network transfer costs, leading to a better consumer experience. It is typically more efficient to download bulk data using the http/ftp stream employed during the application installation than to install a smaller application bundle and then have to use a replicator to pull-in the bulk data.

This prepackaging of the data typically applies to public/shared, non-user specific data that is mostly static. Even if the data is not static, you can still benefit from preloading it and only syncing the changed documents on startup

The initial sync of any pre-built database will pull-in any content changes on the server that occurred after its incorporation into the app, quickly bringing the database up to date.

**To use a prebuilt database:**

* Create a new Couchbase Lite database with the required data set — see [Creating Pre-built database](#crt-db)
* Incorporate the pre-built database with your app bundle as an asset/resource — see [Bundle Database with Application](#bundle-db)
* Adjust the start-up logic of your app to check for the presence of the required database. If it doesn’t already exist, it should create one using the bundled pre-built database, before initiating a sync to update the data — see [Using Pre-built Database on App Launch](#deploy-db)

## [](#crt-db)Creating Pre-built database

These steps would typically be part of your build and release process:

1. Create a fresh Couchbase Lite database (every time)  
> [!IMPORTANT]  
> **Always start with a fresh database for each app version**; this ensures there are no [checkpoint](../../current/swift/refer-glossary.md#checkpoint) issues  
>  
> **Otherwise:** You will invalidate the cached [checkpoint](../../current/swift/refer-glossary.md#checkpoint) in the packaged database, and instead reuse the same database in your build process (for subsequent app versions).
2. Pull the data from Sync Gateway into the new Couchbase Lite database  
> [!IMPORTANT]  
> Ensure the replication used to populate Couchbase Lite database **uses the exact same remote URL and replication config parameters (channels and filters)** as those your app will use when it is running.  
>  
> **Otherwise:** …​ there will be a [checkpoint](../../current/swift/refer-glossary.md#checkpoint) mismatch and the app will attempt to pull the data down again  
>  
> So don’t, for instance, create a pre-built database against a staging Sync Gateway server and try to use that within a production app that syncs against a production Sync Gateway.  
You can use the cblite tool (`cblite cp`) for this — see: [cblite cp (export, import, push, pull)](https://github.com/couchbaselabs/couchbase-mobile-tools/blob/master/Documentation.md#cp-aka-export-import-push-pull) | [cblite on GitHub](https://github.com/couchbaselabs/couchbase-mobile-tools/blob/master/README.cblite.md)

**Alternatively** …​

  * You can write a simple CBL app to just initiate the required pull sync — see: [starting a Sync Gateway Replication](../../current/swift/replication.md#starting-a-replication)
  * A third party community Java app is available. It provides a UI to create a local Couchbase Lite database and pull data from a Sync Gateway database — see: [CouchbaseLite Tester](https://github.com/Infosys/CouchbaseLiteTester)  
  > [!NOTE]  
  > Couchbase accepts no responsibility for the ongoing availability, maintenance or support of this third party community contribution, nor for the provision of support for issues arising from its use.
3. Create the **same** indexes the app will use (wait for the replication to finish before doing this).

## [](#bundle-db)Bundle Database with Application

Copy the database into your app package.

Put it in an appropriate place (for example, an assets or resource folder).

Where the platform permits you can zip the database.

**Alternatively** …​ rather than bundling the database within the app, the app could pull the database down from a CDN server on launch.

## [](#deploy-db)Using Pre-built Database on App Launch

During the application start-up logic, check if database exists in the required location, and **if not**:

1. Locate the pre-packaged database (for example, in the assets or other resource folder)
2. Copy the pre-packaged database to the required location  
Use the API’s [Database.copy()](http://docs.couchbase.com/mobile/2.8.4/couchbase-lite-swift/Classes/Database.html#/s:18CouchbaseLiteSwift8DatabaseeC4copy8fromPath02toD010withConfigySS%5FSSAA0D13ConfigurationCSgtKFZ) method; this ensures that a UUID is generated for each copy — see: [Code Example 1](#copy-db)  
> [!IMPORTANT]  
> **Do not copy the database using any other method**  
>  
> **Otherwise:** Each copy of the app will invalidate the other apps’ [checkpoints](../../current/swift/refer-glossary.md#checkpoint) because a new UUID was not generated.  
Code Example 1\. Copy database using API  
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
3. Open the database; you can now start querying the data and using it
4. Start a pull replication, to sync any changes  
The replicator uses the pre-built database’s [checkpoint](../../current/swift/refer-glossary.md#checkpoint) as the timestamp to sync from; only documents changed since then are synced  
> [!IMPORTANT]  
> If you used cblite to pull the data **without including a port number with the URL** and are replicating in a Java or iOS (swift/ObjC) app — **you must include the port number in the URL provided to the replication** (port 443 for `wss://` or 80 for `ws://`).  
>  
> **Otherwise:** You will get a [checkpoint](../../current/swift/refer-glossary.md#checkpoint) mismatch.  
> This is caused by a URL discrepancy, which arises because `cblite` automatically adds the default port number when none is specified, **but** the Java and iOS (swift/ObjC) replicators DO NOT.  
> [!NOTE]  
> Start your normal application logic immediately, unless it is essential to have the absolute up-to-date data set to begin. That way the user is not kept hanging around watching a progress indicator. They can begin interacting with your app whilst any out-of-data data is being updated.

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Prerequisites](../../current/swift/gs-prereqs.md)
* [Install](../../current/swift/gs-install.md)
* [Build and Run](../../current/swift/gs-build.md)

###### [](#-2)

Learn more . . .

* [Databases](../../current/swift/database.md)
* [Documents](../../current/swift/document.md)
* [Blobs](../../current/swift/blob.md)
* [Remote Sync using Sync Gateway](../../current/swift/replication.md)
* [Handling Data Conflicts](../../current/swift/conflict.md)

###### [](#-3)

Dive Deeper . . .

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)