---
title: Build and Run
description: Build and run a starter app to validate your install of Couchbase Lite on C#
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.4/modules/csharp/pages/gs-build.adoc
  xref: xref:3.4@couchbase-lite:csharp:gs-build.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.4/csharp/gs-build.html)

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
var collection = database.GetDefaultCollection();

// Create a new document (i.e. a record) in the database
var id = default(string);
using var createdDoc = new MutableDocument();
createdDoc.SetFloat("version", 2.0f)
    .SetString("type", "SDK");

// Save it to the database
collection.Save(createdDoc);
id = createdDoc.Id;

// Update a document
using var doc = collection.GetDocument(id);
using var mutableDoc = doc.ToMutable();
createdDoc.SetString("language", "C#");
collection.Save(createdDoc);

using var docAgain = collection.GetDocument(id);
Console.WriteLine($"Document ID :: {docAgain.Id}");
Console.WriteLine($"Learning {docAgain.GetString("language")}");


// Create a query to fetch documents of type SDK
// i.e. SELECT * FROM database WHERE type = "SDK"
using var query = QueryBuilder.Select(SelectResult.All())
    .From(DataSource.Collection(collection))
    .Where(Expression.Property("type").EqualTo(Expression.String("SDK")));

// Run the query
var result = query.Execute();
Console.WriteLine($"Number of rows :: {result.AllResults().Count}");

// Create replicator to push and pull changes to and from the cloud
var targetEndpoint = new URLEndpoint(new Uri("ws://localhost:4984/getting-started-db"));
var replConfig = new ReplicatorConfiguration(targetEndpoint);
replConfig.AddCollection(database.GetDefaultCollection());

// Add authentication
replConfig.Authenticator = new BasicAuthenticator("john", "pass");

// Create replicator (make sure to add an instance or static variable
// named _Replicator)
var replicator = new Replicator(replConfig);
replicator.AddChangeListener((sender, args) =>
{
    if (args.Status.Error != null) {
        Console.WriteLine($"Error :: {args.Status.Error}");
    }
});

replicator.Start();

// Later, stop and dispose the replicator *before* closing/disposing the database
```

Build and run. You should see the document ID and property printed to the console. The document was successfully persisted to the database.

See also — [Install Sync Gateway](#sync-gateway::get-started-install.adoc)

### [](#building-with-vector-search)Building With Vector Search

To build your Couchbase Lite application with Vector Search, you must add the following to your existing Couchbase Lite application:

1. Add the Vector Search import statement  
```csharp  
using Couchbase.Lite.Extensions;  
```
2. Load the extension.  
```csharp  
// For Android applications  
Extension.Load(new VectorSearchExtension(Context));  
// For non-Android applications  
Extension.Load(new VectorSearchExtension());  
```

## [](#related-content)Related Content

###### [](#)

How to

* [Passive Peer](p2psync-websocket-using-passive.md)
* [Active Peer](p2psync-websocket-using-active.md)

.

###### [](#-2)

Concepts

* [Peer-to-Peer Sync](#csharp:landing-p2psync.adoc)
* [API References](https://docs.couchbase.com/mobile/3.4.1/couchbase-lite-net)

.

###### [](#-3)

Community Resources …​

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

. [Getting Started with Peer-to-Peer Synchronization](../../../tutorials/cbl-p2p-sync-websockets/swift/cbl-p2p-sync-websockets.md)