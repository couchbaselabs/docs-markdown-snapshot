---
title: Build and Run
description: Build and run a starter app to validate your install of Couchbase Lite on C#
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.0/modules/csharp/pages/gs-build.adoc
  xref: xref:3.0@couchbase-lite:csharp:gs-build.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.0/csharp/gs-build.html)

# Build and Run

> Description — _Build and run a starter app to validate your install of Couchbase Lite on C#_  
> _Abstract — This content provides sample code and instructions that enable you to test your Couchbase Lite for csharp installation._  

## [](#starter-code)Starter code

Open **Main.cs** in Visual Studio and copy the following code in the `main` method. This snippet demonstrates how to run basic CRUD operations, a simple Query and running bi-directional replications with Sync Gateway.

```C#

    // using System;
    // using Couchbase.Lite;
    // using Couchbase.Lite.Query;
    // using Couchbase.Lite.Sync;

    // Get the database (and create it if it doesn't exist)
    var database = new Database("mydb");
    // Create a new document (i.e. a record) in the database
    string id = null;
    using (var mutableDoc = new MutableDocument())
    {
        mutableDoc.SetFloat("version", 2.0f)
            .SetString("type", "SDK");

        // Save it to the database
        database.Save(mutableDoc);
        id = mutableDoc.Id;
    }

    // Update a document
    using (var doc = database.GetDocument(id))
    using (var mutableDoc = doc.ToMutable())
    {
        mutableDoc.SetString("language", "C#");
        database.Save(mutableDoc);

        using (var docAgain = database.GetDocument(id))
        {
            Console.WriteLine($"Document ID :: {docAgain.Id}");
            Console.WriteLine($"Learning {docAgain.GetString("language")}");
        }
    }

    // Create a query to fetch documents of type SDK
    // i.e. SELECT * FROM database WHERE type = "SDK"
    using (var query = QueryBuilder.Select(SelectResult.All())
        .From(DataSource.Database(database))
        .Where(Expression.Property("type").EqualTo(Expression.String("SDK"))))
    {
        // Run the query
        var result = query.Execute();
        Console.WriteLine($"Number of rows :: {result.AllResults().Count}");
    }

    // Create replicator to push and pull changes to and from the cloud
    var targetEndpoint = new URLEndpoint(new Uri("ws://localhost:4984/getting-started-db"));
    var replConfig = new ReplicatorConfiguration(database, targetEndpoint);

    // Add authentication
    replConfig.Authenticator = new BasicAuthenticator("john", "pass");

    // Create replicator (make sure to add an instance or static variable
    // named _Replicator)
    var _Replicator = new Replicator(replConfig);
    _Replicator.AddChangeListener((sender, args) =>
    {
        if (args.Status.Error != null)
        {
            Console.WriteLine($"Error :: {args.Status.Error}");
        }
    });

    _Replicator.Start();

    // Later, stop and dispose the replicator *before* closing/disposing the
}
```

Build and run. You should see the document ID and property printed to the console. The document was successfully persisted to the database.

See also — [Install Sync Gateway](#sync-gateway::get-started-install.adoc)

## [](#related-content)Related Content

###### [](#)

How to

* [Passive Peer](p2psync-websocket-using-passive.md)
* [Active Peer](p2psync-websocket-using-active.md)

###### [](#-2)

Concepts

* [Peer-to-Peer Sync](#csharp:landing-p2psync.adoc)
* [API References](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-net)

###### [](#-3)

Community Resources …​

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

[Getting Started with Peer-to-Peer Synchronization](../../../tutorials/cbl-p2p-sync-websockets/swift/cbl-p2p-sync-websockets.md)