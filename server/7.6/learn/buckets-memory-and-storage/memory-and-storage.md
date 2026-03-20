---
title: Memory and Storage
description: To facilitate high-speed data-access, Couchbase Server provides a
  caching layer and tunable disk I/O priorities.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/learn/pages/buckets-memory-and-storage/memory-and-storage.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.6@server:learn:buckets-memory-and-storage/memory-and-storage.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/learn/buckets-memory-and-storage/memory-and-storage.html)

# Memory and Storage

> To facilitate high-speed data-access, Couchbase Server provides a caching layer and tunable disk I/O priorities. 

## [](#caching-and-persistence)Caching and Persistence

Couchbase Server provides a fully integrated _caching layer_, which provides high-speed data-access. Couchbase Server automatically manages the caching layer, ensuring that sufficient memory is available in relation to occupied disk-space, in order to maintain optimal performance. Data associated with _Couchbase_ (as opposed to _Ephemeral_) buckets is also maintained _persistently_, on disk. Such items, when they come into the caching layer, are placed on the disk queue, to be written to disk; and at the same time, if appropriate, are placed on a replication queue, so that one or more replica buckets can be created or updated.

Memory quotas, established by the Full Administrator when the server is configured, are automatically managed by Couchbase Server with reference to _watermarks_, which specify how much free memory should be consistently maintained within the caching layer. Consequently, infrequently used items are written to disk; and are then removed from memory in order to free up space. This process, referred to as _ejection_, is managed asynchronously, while the server continues to service active requests. Items ejected from _Couchbase_ buckets can subsequently be re-acquired from disk, as necessary. A _working-set_ of most frequently used data is tracked and maintained, and the items kept in memory to ensure high performance. The priority of disk I/O is configurable per bucket.

## [](#saving-new-items)Saving New Items

When a new item, such as a document, is saved by an application, it is saved in memory only, if the item is contained by an _Ephemeral_ bucket; and is saved both in memory and on disk, if the item is contained by a _Couchbase_ bucket. If the bucket (either Ephemeral or Couchbase) has been _replicated_ one or more times, a copy of the new item is saved in each replica.

The following sequence illustrates how a new document is created by an application and saved in a Couchbase bucket. It is assumed that the bucket has at least one replica on the cluster.

1. The application creates a new document.  
![createDocSequence1](../_images/buckets-memory-and-storage/createDocSequence1.png)
2. The application saves the document on Couchbase Server. The document is received in memory.  
![createDocSequence2](../_images/buckets-memory-and-storage/createDocSequence2.png)
3. Couchbase Server places a compressed copy of the document onto the _Disk Queue_ so that the document can be written to the disk; and a further copy onto the _Replication Queue_, so that the document can be written to the replica bucket. (The copy placed on the Replication Queue may or may not be compressed, depending on the _compression mode_ configured for the bucket.)  
![createDocSequence3](../_images/buckets-memory-and-storage/createDocSequence3.png)
4. Once written, the new document resides both in the memory and on the disk of the node. It will also reside in the memory and on the disk of whichever other nodes maintain the replicas of its buckets.  
![createDocSequence4](../_images/buckets-memory-and-storage/createDocSequence4.png)  
On each node containing the bucket or a replica, the document remains in memory; unless it is _ejected_ at some point, after which it remains on disk.

## [](#updating-items)Updating Items

Items that reside in the memory of Couchbase Server can be updated. If the item belongs to a Couchbase bucket, the item is also updated on disk. If the item is not currently in memory, but resides on disk, Couchbase Server retrieves the item, so that it can be updated. This is demonstrated by the following sequence.

1. The application provides an update to an existing document.  
![updateDocSequence1](../_images/buckets-memory-and-storage/updateDocSequence1.png)
2. Since the document is not currently in memory, Couchbase Server seeks it on disk, where is resides in compressed form.  
![updateDocSequence2](../_images/buckets-memory-and-storage/updateDocSequence2.png)
3. The compressed document is retrieved, brought into memory, and decompressed.  
![updateDocSequence3](../_images/buckets-memory-and-storage/updateDocSequence3.png)
4. The application’s updates are applied to the uncompressed document.  
![updateDocSequence4](../_images/buckets-memory-and-storage/updateDocSequence4.png)
5. The updated document is placed (in either compressed or uncompressed form, as appropriate) on the replication queue, so that replicas can be updated. The updated document is also re-compressed, and written to disk locally.  
![updateDocSequence5](../_images/buckets-memory-and-storage/updateDocSequence5.png)
6. The updated document is now retained locally on disk and in memory. The document remains in memory unless it is ejected at some point, after which it continues to reside on disk.  
![updateDocSequence6](../_images/buckets-memory-and-storage/updateDocSequence6.png)