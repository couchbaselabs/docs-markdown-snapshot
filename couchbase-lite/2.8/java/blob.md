---
title: Blobs
description: Working with Couchbase Lite's data model -- handling data store
  attachments blobs's
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/java/pages/blob.adoc
  xref: xref:2.8@couchbase-lite:java:blob.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/java/blob.html)

# Blobs

> Description — _Working with Couchbase Lite's data model — handling data store attachments blobs's_  
> Related Content — [Databases](../../current/java/database.md) | [Documents](../../current/java/document.md) | [Indexing](../../current/java/indexing.md)

## [](#what-are-blobs)What Are Blobs?

We've renamed "attachments" to "blobs". The new behavior should be clearer too, as a `Blob` is now a normal object that can appear in a document as a property value.

## [](#using-blobs)Using Blobs

So to uses a `blob`, you just instantiate it and set it as the value of a property. Later you can get the property value, which will be a `Blob` object.

Example 1\. Add a blob to a document

This example shows code that adds a blob to the document under the `avatar` property.

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

The `Blob` API lets you access the contents as an in-memory byte array ( `public byte[] getContent()`) or as an `InputStream` (`public InputStream getContentStream()`). It also supports an optional `type` property that by convention stores the MIME type of the contents.

In [Example 1](#add-a-blob), "image/jpeg" is the MIME type and "avatar" is the key which references that `Blob`. That key can be used to retrieve the `Blob` object at a later time.

## [](#synchronization-behaviour)Synchronization Behaviour

When a document is synchronized, the Couchbase Lite replicator will add an `_attachments` dictionary to the document's properties if it contains a blob.

A random access name will be generated for each `Blob` which is different to the "avatar" key that was used in the example above.

On the image below, the document now contains the `_attachments` dictionary when viewed in the Couchbase Server Admin Console.

![attach replicated](../_images/attach-replicated.png) 

This `Blob` can be retrieved on the Sync Gateway REST API at http://localhost:4984/justdoit/user.david/blob\_1\. Notice that the blob identifier in the URL path is "blob\_1" (not "avatar").

## [](#properties)Properties

A blob also has properties such as `"digest"` (a SHA-1 digest of the data), `"length"` (the length in bytes), and optionally `"content_type"` (the MIME type). The data is not stored in the document, but in a separate content-addressable store, indexed by the digest.

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Prerequisites](../../current/java/gs-prereqs.md)
* [Install](../../current/java/gs-install.md)
* [Build and Run](../../current/java/gs-build.md)

###### [](#-2)

Learn more . . .

* [Databases](../../current/java/database.md)
* [Documents](../../current/java/document.md)
* [Blobs](../../current/java/blob.md)
* [Remote Sync using Sync Gateway](../../current/java/replication.md)
* [Handling Data Conflicts](../../current/java/conflict.md)

###### [](#-3)

Dive Deeper . . .

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)