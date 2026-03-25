---
title: Working with Blobs
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/2.8/modules/swift/pages/save-blob.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.8@couchbase-lite:swift:save-blob.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/2.8/swift/save-blob.html)

# Working with Blobs

## [](#overview)Overview

A `Blob` is an object that can appear in a document as a property value. Just instantiate a `Blob` and set it as the value of a property. Then later get the property value, which will be a `Blob` object.

The following code example adds a blob to the document under the `avatar` property.

```swift
let appleImage = UIImage(named: "avatar.jpg")!
let imageData = UIImageJPEGRepresentation(appleImage, 1)!

let blob = Blob(contentType: "image/jpeg", data: imageData)
newTask.setBlob(blob, forKey: "avatar")
try database.saveDocument(newTask)

if let taskBlob = newTask.blob(forKey: "image") {
    image = UIImage(data: taskBlob.content!)
}
```

The `Blob` API lets you access the contents as in-memory data (a `Data` object) or as a `InputStream`. It also supports an optional `type` property that by convention stores the MIME type of the contents.

In the example above, "image/jpeg" is the MIME type and "avatar" is the key which references that `Blob`. That key can be used to retrieve the `Blob` object at a later time.

On Couchbase Lite, blobs can be arbitrarily large, and are only read on demand, not when you load a `Document` object. On Sync Gateway, the maximum content size is 20 MB per blob. If a document’s blob is over 20 MB, the document will be replicated but not the blob.

When a document is synchronized, the Couchbase Lite replicator will add an `_attachments` dictionary to the document’s properties if it contains a blob. A random access name will be generated for each `Blob` which is different to the "avatar" key that was used in the example above. On the image below, the document now contains the `_attachments` dictionary when viewed in the Couchbase Server Admin Console.

![attach replicated](../_images/attach-replicated.png) 

A blob also has properties such as `"digest"` (a SHA-1 digest of the data), `"length"` (the length in bytes), and optionally `"content_type"` (the MIME type). The data is not stored in the document, but in a separate content-addressable store, indexed by the digest.

This `Blob` can be retrieved on the Sync Gateway REST API at http://localhost:4984/justdoit/user.david/blob\_1\. Notice that the blob identifier in the URL path is "blob\_1" (not "avatar").