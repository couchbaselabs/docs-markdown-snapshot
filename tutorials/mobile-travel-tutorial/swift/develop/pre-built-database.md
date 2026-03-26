---
title: Pre-built database
editUrl: https://github.com/couchbaselabs/mobile-travel-sample/edit/master/content/modules/mobile-travel-tutorial/pages/swift/develop/pre-built-database.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:tutorials:mobile-travel-tutorial:swift/develop/pre-built-database.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/tutorials/mobile-travel-tutorial/swift/develop/pre-built-database.html)

# Pre-built database

## [](#starting-with-prebuilt-database)Starting with Prebuilt Database

In this section, you will learn how to bundle a pre-built Couchbase Lite database in an application. It can be a lot more efficient to bundle static or semi-static content database in your application and install it on the first launch. Even if some of the content changes on the server after you create the app, the app's first pull replication will bring the database up to date. Here, you will use a pre-built database that contains only airport and hotel documents. The code below moves the pre-built database from the bundled location to the Application Support directory.

**Open the file** `DatabaseManager.swift` and navigate to the `openOrCreateDatabaseForUser` method.

This method first checks if a database file already exists. If it doesn't exist it loads the database from the app bundle.

[DatabaseManager.swift](https://github.com/couchbaselabs/mobile-travel-sample/blob/master/ios/TravelSample/TravelSample/Model/DatabaseManager.swift#L112)

```swift
 if Database.exists(kDBName, inDirectory: userFolderPath) == false {
  // Load prebuilt database from App Bundle and copy over to Applications support path
  if let prebuiltPath = Bundle.main.path(forResource: kDBName, ofType: "cblite2") {
       try Database.copy(fromPath: prebuiltPath, toDatabase: "\(kDBName)", config: options)

  }
```

Try it out

1. Log into the Travel Sample Mobile app as "demo" user and password as "password"
2. Tap on "+\`" button to make a flight reservation
3. In the "From" airport text field, enter "San"
4. Confirm that the first item in the dropdown list of "San Diego Intl"

![ios prebuilt](../../_images/ios_prebuilt.gif)