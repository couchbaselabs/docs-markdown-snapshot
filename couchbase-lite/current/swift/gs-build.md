---
title: Build and Run
description: Build and run a starter app to validate your install of Couchbase Lite on Swift
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.1/modules/swift/pages/gs-build.adoc
  xref: xref:couchbase-lite:swift:gs-build.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/current/swift/gs-build.html)

# Build and Run

> Description — _Build and run a starter app to validate your install of Couchbase Lite on Swift_  

## [](#quick-steps)Quick Steps

1. Create a new Swift project as outlined in [Install](gs-install.md)
2. Open the new project's **ViewController.swift** module in Xcode
3. Replace the boiler-plate code with the code shown in [Example 1](#ex-starter-code)
4. Build and run the 'app'  
You should see — [Figure 1](#img-starter-code) — the document ID and property printed to the 'console log', indicating that a document was created successfully persisted to the database, updated and queried.

![getting started ios](_images/getting-started-ios.png) 

Figure 1\. Example app output

Example 1\. Code snippet

This snippet demonstrates how to run basic CRUD operations, a simple Query and optionally running bi-directional replications with Sync Gateway.

```swift
//
//  Getting-Started.swift
//  code-snippets
//
//  Copyright © 2025 couchbase. All rights reserved.
//

import UIKit
import CouchbaseLiteSwift

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.

        try! getStartedWithReplication(replication: false)
}

    func getStartedWithReplication (replication: Bool) throws {
        // Get the database (and create it if it doesn’t exist).
        let database = try Database(name: "mydb")
        let defaultCol = try database.defaultCollection()

        // Create a new document (i.e. a record) in the database.
        var mutableDoc = MutableDocument()
            .setFloat(2.0, forKey: "version")
            .setString("SDK", forKey: "type")

        // Save document to default collection.
        try defaultCol.save(document: mutableDoc)
        print("Created document id type \(mutableDoc.id)? with type = \(mutableDoc.string(forKey: "type")!)")
        
        // Update a document.
        mutableDoc = try defaultCol.document(id: mutableDoc.id)!.toMutable()
        mutableDoc.setString("Swift", forKey: "language")
        try defaultCol.save(document: mutableDoc)
        let document = try defaultCol.document(id: mutableDoc.id)
        assert(document!.string(forKey: "language") == "Swift",
               "Updated document id \(document!.id), adding language \(document!.string(forKey: "language")!)")

        // Create a query to fetch documents of type SDK.
        print("Querying Documents of type=SDK")
        let query = QueryBuilder
            .select(SelectResult.all())
            .from(DataSource.collection(defaultCol))
            .where(Expression.property("type").equalTo(Expression.string("SDK")))

        // Run the query.
        do {
            let result = try query.execute()
            print("Number of rows :: \(result.allResults().count)")
        } catch {
            fatalError("Error running the query")
        }

        if replication {
            // Create replicators to push and pull changes to and from the cloud.
            let targetEndpoint = URLEndpoint(url: URL(string: "ws://localhost:4984/getting-started-db")!)
            
            // Create Collection configuration.
            let colConfig = CollectionConfiguration(collection: defaultCol)
            
            // Create replicator configuration with the target endpoint and collection configuration.
            var replConfig = ReplicatorConfiguration(collections: [colConfig], target: targetEndpoint)
            replConfig.replicatorType = .pushAndPull
            
            // Add authentication.
            replConfig.authenticator = BasicAuthenticator(username: "john", password: "pass")
            
            // Create replicator (make sure to add an instance or static variable named replicator)
            let replicator = Replicator(config: replConfig)

            // Listen to replicator change events.
            replicator.addChangeListener { (change) in
                if let error = change.status.error as NSError? {
                    print("Error code :: \(error.code)")
                }
            }

            // Start replication.
            replicator.start()
        } else {
            print("Not running replication")
        }
    }
}
```

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Prerequisites](gs-prereqs.md)
* [Install](gs-install.md)
* [Build and Run](gs-build.md)

.

###### [](#-2)

Learn more . . .

* [Databases](database.md)
* [Documents](document.md)
* [Blobs](blob.md)
* [Remote Sync Gateway](replication.md)
* [Handling Data Conflicts](conflict.md)

.

###### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.