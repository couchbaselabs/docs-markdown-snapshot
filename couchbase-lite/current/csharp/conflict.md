---
title: Handling Data Conflicts
description: Couchbase Lite Database Sync -- Handling conflict between data changes
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.0/modules/csharp/pages/conflict.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:couchbase-lite:csharp:conflict.adoc[]
---

[View original HTML](/couchbase-lite/current/csharp/conflict.html)

# Handling Data Conflicts

> Description — _Couchbase Lite Database Sync — Handling conflict between data changes_  

## [](#causes-of-conflicts)Causes of Conflicts

Document conflicts can occur if multiple changes are made to the same version of a document by multiple peers in a distributed system. For Couchbase Mobile, this can be a Couchbase Lite or Sync Gateway database instance.

Such conflicts can occur after either of the following events:

* **A replication saves a document change** — in which case the change with the _most-revisions wins_ (unless one change is a delete). See the example [Case 1: Conflicts when a replication is in progress](#lbl-conflicts-when-replicating)
* **An application saves a document change directly to a database instance** — in which case, _last write wins_, unless one change is a delete — see [Case 2: Conflicts when saving a document](#conflicts-when-saving)

> [!NOTE]
> **_Deletes_ always win.** So, in either of the above cases, if one of the changes was a _Delete_ then that change wins.

The following sections discuss each scenario in more detail.

> [!TIP]
> Dive deeper …​
> 
> Read more about [Document Conflicts and Automatic Conflict Resolution in Couchbase Mobile](https://blog.couchbase.com//document-conflicts-couchbase-mobile).

## [](#lbl-conflicts-when-replicating)Conflicts when Replicating

There’s no practical way to prevent a conflict when incompatible changes to a document are be made in multiple instances of an app. The conflict is realized only when replication propagates the incompatible changes to each other. 

Example 1\. A typical cause of replication conflicts:

1. Molly uses her device to create _DocumentA_.
2. Replication syncs _DocumentA_ to Naomi’s device.
3. Molly uses her device to apply _ChangeX_ to _DocumentA_.
4. Naomi uses her device to make a different change, _ChangeY_, to _DocumentA_.
5. Replication syncs _ChangeY_ to Molly’s device.  
This device already has _ChangeX_ putting the local document in conflict.
6. Replication syncs _ChangeX_ to Naomi’s device.  
This device already has _ChangeY_ and now Naomi’s local document is in conflict.

### [](#automatic-conflict-resolution)Automatic Conflict Resolution

> [!NOTE]
> The rules only apply to conflicts caused by replication. Conflict resolution takes place exclusively during pull replication, while push replication remains unaffected.

Couchbase Lite uses the following rules to handle conflicts such as those described in [A typical replication conflict scenario](#bmkRepConScene):

* If one of the changes is a deletion:  
A deleted document (that is, a _tombstone_) always wins over a document update.
* If both changes are document changes:  
The change with the most revisions will win.  
Since each change creates a revision with an ID prefixed by an incremented version number, the winner is the change with the highest version number.

The result is saved internally by the Couchbase Lite replicator. Those rules describe the internal behavior of the replicator. For additional control over the handling of conflicts, including when a replication is in progress, see [Custom Conflict Resolution](#custom-conflict-resolution).

### [](#custom-conflict-resolution)Custom Conflict Resolution

Starting in Couchbase Lite 2.6, application developers who want more control over how document conflicts are handled can use custom logic to select the winner between conflicting revisions of a document.

If a custom conflict resolver is not provided, the system will automatically resolve conflicts as discussed in [Automatic Conflict Resolution](#automatic-conflict-resolution), and as a consequence there will be no conflicting revisions in the database.

> [!CAUTION]
> While this is true of any user defined functions, app developers must be strongly cautioned against writing sub-optimal custom conflict handlers that are time consuming and could slow down the client’s save operations.

To implement custom conflict resolution during replication, you must implement the following steps.

1. [Conflict Resolver](#conflict-resolver)
2. [Configure the Replicator](#configure-the-replicator)

### [](#conflict-resolver)Conflict Resolver

Apps have the following strategies for resolving conflicts:

* **Local Wins:** The current revision in the database wins.
* **Remote Wins:** The revision pulled from the remote endpoint through replication wins.
* **Merge:** Merge the content bodies of the conflicting revisions.

Example 2\. Using conflict resolvers

* Local Wins
* Remote Wins
* Merge

```C#
internal class LocalWinConflictResolver : IConflictResolver
{
    public Document? Resolve(Conflict conflict)
    {
        return conflict.LocalDocument;
    }
}
```

```C#
internal class RemoteWinConflictResolver : IConflictResolver
{
    public Document? Resolve(Conflict conflict)
    {
        return conflict.RemoteDocument;
    }
}
```

```C#
internal class MergeConflictResolver : IConflictResolver
{
    public Document? Resolve(Conflict conflict)
    {
        var localDict = conflict.LocalDocument?.ToDictionary();
        var remoteDict = conflict.RemoteDocument?.ToDictionary();
        var result = localDict;
        if (localDict == null) {
            result = remoteDict;
        } else if (remoteDict != null) {
            result = localDict.Concat(remoteDict)
                .GroupBy(kv => kv.Key)
                .ToDictionary(g => g.Key, g => g.First().Value);
        }

        return result != null ? new MutableDocument(conflict.DocumentID, result) : null;
    }
}
```

When a null document is returned by the resolver, the conflict will be resolved as a document deletion.

### [](#important-guidelines-and-best-practices)Important Guidelines and Best Practices

Points of Note:

* If you have multiple replicators, it is recommended that instead of distinct resolvers, you should use a unified conflict resolver across all replicators. Failure to do so could potentially lead to data loss under exception cases or if the app is terminated (by the user or an app crash) while there are pending conflicts.
* If the document ID of the document returned by the resolver does not correspond to the document that is in conflict then the replicator will log a warning message.  
> [!IMPORTANT]  
> Developers are encouraged to review the warnings and fix the resolver to return a valid document ID.
* If a document from a different database is returned, the replicator will treat it as an error. A [document replication event](#replication-events) will be posted with an error and an error message will be logged.  
> [!IMPORTANT]  
> Apps are encouraged to observe such errors and take appropriate measures to fix the resolver function.
* When the replicator is stopped, the system will attempt to resolve outstanding and pending conflicts before stopping. Hence apps should expect to see some delay when attempting to stop the replicator depending on the number of outstanding documents in the replication queue and the complexity of the resolver function.
* If there is an exception thrown in the `resolve()` method, the exception will be caught and handled:

  * The conflict to resolve will be skipped. The pending conflicted documents will be resolved when the replicator is restarted.
  * The exception will be reported in the warning logs.
  * The exception will be reported in the [document replication event](#replication-events).  
  > [!IMPORTANT]  
  > While the system will handle exceptions in the manner specified above, it is strongly encouraged for the resolver function to catch exceptions and handle them in a way appropriate to their needs.

### [](#configure-the-replicator)Configure the Replicator

The implemented custom conflict resolver can be registered on the replicator configuration object. The default value of the conflictResolver is `null`. When the value is `null`, the default conflict resolution will be applied.

Example 3\. A Conflict Resolver

```C#
var target = new URLEndpoint(new Uri("ws://localhost:4984/mydatabase"));
var collectionConfig = new CollectionConfiguration(collection)
{
    ConflictResolver = new LocalWinConflictResolver()
};

var replConfig = new ReplicatorConfiguration([collectionConfig], target);

var replicator = new Replicator(replConfig);
replicator.Start();
```

## [](#conflicts-when-saving)Conflicts when Updating

When updating a document, you need to consider the possibility of update conflicts. Update conflicts can occur when you try to update a document that’s been updated since you read it.

Example 4\. How Updating May Cause Conflicts

Here’s a typical sequence of events that would create an update conflict:

1. Your code reads the document’s current properties, and constructs a modified copy to save.
2. Another thread (perhaps the replicator) updates the document, creating a new revision with different properties.
3. Your code updates the document with its modified properties, for example using [Database.Save(MutableDocument)](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-net/api/Couchbase.Lite.Database.html#Couchbase%5FLite%5FDatabase%5FSave%5FCouchbase%5FLite%5FMutableDocument%5F).

### [](#automatic-conflict-resolution-2)Automatic Conflict Resolution

In Couchbase Lite, by default, the conflict is automatically resolved and only one document update is stored in the database. The Last-Write-Win (LWW) algorithm is used to pick the winning update. So in effect, the changes from step 2 would be overwritten and lost.

If the probability of update conflicts is high in your app and you wish to avoid the possibility of overwritten data, the `save` and `delete` APIs provide additional method signatures with concurrency control:

Example 5\. Currency Control Signatures

Save operations

[Database.Save(MutableDocument, ConcurrencyControl)](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-net/api/Couchbase.Lite.Database.html#Couchbase%5FLite%5FDatabase%5FSave%5FCouchbase%5FLite%5FMutableDocument%5FCouchbase%5FLite%5FConcurrencyControl%5F) — attempts to save the document with a concurrency control.

The concurrency control parameter has two possible values:

* `lastWriteWins` (default): The last operation wins if there is a conflict.
* `failOnConflict`: The operation will fail if there is a conflict.  
In this case, the app can detect the error that is being thrown, and handle it by re-reading the document, making the necessary conflict resolution, then trying again.

Delete operations

As with save operations, delete operation also have two method signatures, which specify how to handle a possible conflict:

* [Database.Delete(Document)](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-net/api/Couchbase.Lite.Database.html#Couchbase%5FLite%5FDatabase%5FDelete%5FCouchbase%5FLite%5FDocument%5F): The last write will win if there is a conflict.
* [Database.Delete(Document, ConcurrencyControl)](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-net/api/Couchbase.Lite.Database.html#Couchbase%5FLite%5FDatabase%5FDelete%5FCouchbase%5FLite%5FDocument%5FCouchbase%5FLite%5FConcurrencyControl%5F): attempts to delete the document with a concurrency control.

The concurrency control parameter has two possible values:

* `lastWriteWins` (default): The last operation wins if there is a conflict.
* `failOnConflict`: The operation will fail if there is a conflict. In this case, the app can detect the error that is being thrown, and handle it by re-reading the document, making the necessary conflict resolution, then trying again.

### [](#custom-conflict-handlers)Custom Conflict Handlers

Developers can hook a conflict handler when saving a document so they can easily handle the conflict in a single save method call.

To implement custom conflict resolution when saving a document, apps must call the `save` method with a conflict handler block ( [Database.Save(MutableDocument, Func<MutableDocument, Document, Boolean>)](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-net/api/Couchbase.Lite.Database.html#Couchbase%5FLite%5FDatabase%5FSave%5FCouchbase%5FLite%5FMutableDocument%5FSystem%5FFunc%5FCouchbase%5FLite%5FMutableDocument%5FCouchbase%5FLite%5FDocument%5FSystem%5FBoolean%5F%5F)).

The following code snippet shows an example of merging properties from the existing document (`current`) into the one being saved (`new`). In the event of conflicting keys, it will pick the key value from `new`.

Example 6\. Merging document properties

```C#
using var doc = collection.GetDocument("xyz");
using var mutableDoc = doc?.ToMutable();
Debug.Assert(mutableDoc != null);
mutableDoc.SetString("name", "apples");
collection.Save(mutableDoc, (updated, current) =>
{
    var currentDict = current?.ToDictionary() ?? new();
    var newDict = updated.ToDictionary();
    var result = newDict.Concat(currentDict)
        .GroupBy(kv => kv.Key)
        .ToDictionary(g => g.Key, g => g.First().Value);
    updated.SetData(result);
    return true;
});
```

## [](#related-content)Related Content

### [](#)

How to

* [Passive Peer](p2psync-websocket-using-passive.md)
* [Active Peer](p2psync-websocket-using-active.md)

.

### [](#-2)

Concepts

* [Peer-to-Peer Sync](#csharp:landing-p2psync.adoc)
* [API References](https://docs.couchbase.com/mobile/4.0.0/couchbase-lite-net)

.

### [](#-3)

Community Resources …​

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

. [Getting Started with Peer-to-Peer Synchronization](../../../tutorials/cbl-p2p-sync-websockets/swift/cbl-p2p-sync-websockets.md)