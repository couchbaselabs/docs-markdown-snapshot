---
title: Working with Blobs&#8201;&#8212;&#8201;Data Model
description: Couchbase Lite database data model concepts - blobs
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/android/pages/blob.adoc
  xref: xref:2.8@couchbase-lite:android:blob.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/android/blob.html)

# Working with Blobs&#8201;&#8212;&#8201;Data Model

> Description — _Couchbase Lite database data model concepts - blobs_  
> Related Content — [Databases](../../current/android/database.md) | [Documents](../../current/android/document.md) | [Indexing](../../current/android/indexing.md) |

A `Blob` is an object that can appear in a document as a property value. Just instantiate a `Blob` and set it as the value of a property. Then later get the property value, which will be a `Blob` object.

The following code example adds a blob to the document under the `avatar` property.

Example 1\. blob code

```Java
InputStream is = getAsset("avatar.jpg");
if (is == null) { return; }
try {
    Blob blob = new Blob("image/jpeg", is);
    newTask.setBlob("avatar", blob);
    database.save(newTask);

    Blob taskBlob = newTask.getBlob("avatar");
    byte[] bytes = taskBlob.getContent();
} catch (CouchbaseLiteException e) {
    Log.e(TAG, e.toString());
} finally {
    try { is.close(); }
    catch (IOException ignore) { }
}
```

The `Blob` API lets you access the contents as in-memory data (a `Data` object) or as a `InputStream`. It also supports an optional `type` property that by convention stores the MIME type of the contents.

In the example above, "image/jpeg" is the MIME type and "avatar" is the key which references that `Blob`. That key can be used to retrieve the `Blob` object at a later time.

On Couchbase Lite, blobs can be arbitrarily large, and are only read on demand, not when you load a `Document` object. On Sync Gateway, the maximum content size is 20 MB per blob. If a document's blob is over 20 MB, the document will be replicated but not the blob.

When a document is synchronized, the Couchbase Lite replicator will add an `_attachments` dictionary to the document's properties if it contains a blob. A random access name will be generated for each `Blob` which is different to the "avatar" key that was used in the example above. On the image below, the document now contains the `_attachments` dictionary when viewed in the Couchbase Server Admin Console.

![attach replicated](../_images/attach-replicated.png) 

A blob also has properties such as `"digest"` (a SHA-1 digest of the data), `"length"` (the length in bytes), and optionally `"content_type"` (the MIME type). The data is not stored in the document, but in a separate content-addressable store, indexed by the digest.

This `Blob` can be retrieved on the Sync Gateway REST API at http://localhost:4984/justdoit/user.david/blob\_1\. Notice that the blob identifier in the URL path is "blob\_1" (not "avatar").

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Prerequisites](../../current/android/gs-prereqs.md)
* [Install](../../current/android/gs-install.md)
* [Build and Run](../../current/android/gs-build.md)

###### [](#-2)

Learn more . . .

* [Databases](../../current/android/database.md)
* [Documents](../../current/android/document.md)
* [Blobs](../../current/android/blob.md)
* [Remote Sync using Sync Gateway](../../current/android/replication.md)
* [Handling Data Conflicts](../../current/android/conflict.md)

###### [](#-3)

Dive Deeper . . .

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)