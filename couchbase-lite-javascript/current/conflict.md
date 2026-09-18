---
title: Handling Data Conflicts
description: Couchbase Lite JavaScript -- Handling conflict between data changes
pubDate: 2026-09-18T04:31:08.992Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-js/edit/release/1.0/modules/ROOT/pages/conflict.adoc
  xref: xref:couchbase-lite-javascript::conflict.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite-javascript/current/conflict.html)

# Handling Data Conflicts

> Description — _Couchbase Lite JavaScript — Handling conflict between data changes_  
> Related Content — [Remote Sync Gateway](replication.md) | [CORS Configuration](cors-configuration.md)

## [](#causes-of-conflicts)Causes of Conflicts

Document conflicts can occur if multiple changes are made to the same version of a document by multiple peers in a distributed system. For Couchbase Mobile, this can be a Couchbase Lite or Sync Gateway database instance.

Such conflicts can occur after either of the following events:

* **A replication saves a document change** — in which case the change with the _most-revisions wins_ (unless one change is a delete). See [Case 1: Conflicts when a replication is in progress](#lbl-conflicts-when-replicating)
* **An application saves a document change directly to a database instance** — in which case, _last write wins_, unless one change is a delete — see [Case 2: Conflicts when saving a document](#conflicts-when-saving)

> [!NOTE]
> **_Deletes_ always win.** So, in either of the above cases, if one of the changes was a _Delete_ then that change wins.

The following sections discuss each scenario in more detail.

> [!TIP]
> Dive deeper …​
> 
> Read more about [Document Conflicts and Automatic Conflict Resolution in Couchbase Mobile](https://blog.couchbase.com/document-conflicts-couchbase-mobile).

## [](#lbl-conflicts-when-replicating)Conflicts when Replicating

There's no practical way to prevent a conflict when incompatible changes to a document are made in multiple instances of an app. The conflict is realized only when replication propagates the incompatible changes to each other.

Example 1\. A typical cause of replication conflicts:

1. Alice uses her device to create _DocumentA_.
2. Replication syncs _DocumentA_ to Bob's device.
3. Alice uses her device to apply _ChangeX_ to _DocumentA_.
4. Bob uses his device to make a different change, _ChangeY_, to _DocumentA_.
5. Replication syncs _ChangeY_ to Alice's device.  
This device already has _ChangeX_ putting the local document in conflict.
6. Replication syncs _ChangeX_ to Bob's device.  
This device already has _ChangeY_ and now Bob's local document is in conflict.

### [](#automatic-conflict-resolution)Automatic Conflict Resolution

> [!NOTE]
> The rules only apply to conflicts caused by replication. Conflict resolution takes place exclusively during pull replication, while push replication remains unaffected.

Couchbase Lite uses the following rules to handle conflicts such as those described in [Example 1](#typical-conflict-scenario):

* If one of the changes is a deletion:  
A deleted document (that is, a _tombstone_) always wins over a document update.
* If both changes are document changes:  
The change with the most revisions wins. If both have the same number of revisions, a deterministic algorithm is used to pick a winner.

The result is saved internally by the Couchbase Lite replicator. Those rules describe the internal behavior of the replicator. For additional control over the handling of conflicts, including when a replication is in progress, see [Custom Conflict Resolution](#custom-conflict-resolution).

### [](#custom-conflict-resolution)Custom Conflict Resolution

Application developers who want more control over how document conflicts are handled can use custom logic to select the winner between conflicting revisions of a document.

If a custom conflict resolver is not provided, the system will automatically resolve conflicts as discussed in [Automatic Conflict Resolution](#automatic-conflict-resolution).

> [!CAUTION]
> Custom conflict handlers should be optimized and fast. Time-consuming conflict resolution can slow down the replication process significantly.

To implement custom conflict resolution during replication, you create a conflict resolver function and configure it on the replicator.

#### [](#conflict-resolver)Conflict Resolver

Apps have the following strategies for resolving conflicts:

* **Local Wins:** The current revision in the database wins.
* **Remote Wins:** The revision pulled from the remote endpoint through replication wins.
* **Merge:** Merge the content of the conflicting revisions.

Example 2\. Conflict Resolution Strategies

* Local Wins
* Remote Wins
* Merge
* Delete

```javascript
const localWinsResolver: PullConflictResolver = async (local, remote) => {
    return local;
};
```

```javascript
const remoteWinsResolver: PullConflictResolver = async (local, remote) => {
    return remote;
};
```

```javascript
const mergeResolver: PullConflictResolver = async (local, remote) => {
    if (local && remote) {
        return { ...local, ...remote } as CBLDocument;
    } else {
        return local ?? remote;
    }
};
```

```javascript
const deleteResolver: PullConflictResolver = async (local, remote) => {
    return null;
};
```

When `null` is returned by the resolver, the conflict is resolved as a document deletion.

## [](#conflicts-when-saving)Conflicts when Saving

When updating a document, you need to consider the possibility of update conflicts. Update conflicts can occur when you try to update a document that's been updated since you read it.

Example 3\. How Updating May Cause Conflicts

Here's a typical sequence of events that would create an update conflict:

1. Your code reads the document's current properties, and constructs a modified copy to save.
2. Another thread (perhaps the replicator) updates the document, creating a new revision with different properties.
3. Your code updates the document with its modified properties using the save operation.

### [](#automatic-conflict-resolution-2)Automatic Conflict Resolution

In Couchbase Lite, by default, the conflict is automatically resolved and only one document update is stored in the database. The Last-Write-Win (LWW) algorithm is used to pick the winning update. So in effect, the changes from step 2 would be overwritten and lost.

If the probability of update conflicts is high in your app and you wish to avoid the possibility of overwritten data, you can use a custom save handler with concurrency control.

### [](#save-with-conflict-handler)Save with Conflict Handler

Implement a conflict handler when saving documents to handle conflicts during save operations:

Example 4\. Save with Conflict Handler

```javascript
// Use my changes
await tasks.save(doc, (_mine, _theirs /* conflicting */) => {
    return 'replace';
});

// Discard my change
await tasks.save(doc, (_mine, _theirs /* conflicting */) => {
    return 'revert';
});

// Abort with an error
await tasks.save(doc, (_mine, _theirs /* conflicting */) => {
    return 'fail';
});
```

The conflict handler receives:

* `document` \- The document being saved
* `conflicting` \- The current document in the database (that conflicts)

The handler should return:

* The resolved document to save
* `null` to cancel the save operation

#### [](#custom-merge-on-save)Custom Merge on Save

Implement property-level merging when saving:

Example 5\. Custom merge on save

```javascript
// Use my changes
await tasks.save(doc, (mine, theirs /* conflicting */) => {
    // Delete always wins
    if (!theirs) return 'revert';

    // Custom merge
    mine.title = `${mine.title} and ${theirs.title}`;
    mine.completed = !!(mine.completed && theirs.completed);
    mine.priority = Math.min(mine.priority, theirs.priority);
    mine.createdAt = new Date().toISOString();
    return 'replace';
});
```

## [](#related-content)Related Content

### [](#)

How to . . .

* [Prerequisites](gs-prereqs.md)
* [Install](gs-install.md)

.

### [](#-2)

Learn more . . .

* [Remote Sync Gateway](replication.md)
* [CORS Configuration](cors-configuration.md)
* [Databases](database.md)
* [Documents](document.md)

.

### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.