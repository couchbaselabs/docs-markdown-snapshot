[View original HTML](/couchbase-lite/3.3/swift/blob.html)

> Description — _Couchbase Lite database data model concepts - blobs_  
> Related Content — [Databases](database.md) | [Documents](document.md) | [Indexing](indexing.md) |

## [](#introduction)Introduction

Couchbase Lite for Swift uses _blobs_ to store the contents of images, other media files and similar format files as binary objects.

The blob itself is not stored in the document. It is held in a separate content-addressable store indexed from the document and retrieved only on-demand.

When a document is synchronized, the Couchbase Lite replicator adds an `_attachments` dictionary to the document’s properties if it contains a blob — see [Figure 1](#img-blob).

## [](#blob-objects)Blob Objects

The blob as an object appears in a document as dictionary property — see, for example _avatar_ in [Figure 1](#img-blob).

Other properties include `length` (the length in bytes), and optionally `content_type` (typically, its MIME type).

The blob’s data (an image, audio or video content) is not stored in the document, but in a separate content-addressable store, indexed by the `digest` property — see [Using Blobs](#lbl-using).

### [](#constraints)Constraints

* Couchbase Lite  
Blobs can be arbitrarily large. They are only read on demand, not when you load a the _document_.
* sync gateway  
The maximum content size is 20 MB per blob. If a document’s blob is over 20 MB, the document will be replicated but not the blob.

## [](#lbl-using)Using Blobs

The `Blob` API lets you access the blob’s data content as in-memory data (a `Data` object) or as an `InputStream`.

The code in [Example 1](#ex-blob) shows how you might add a blob to a document and save it to the database. Here we use `avatar` as the property key and a jpeg file as the blob data.

Example 1\. Working with blobs

```swift
let appleImage = UIImage(named: "avatar.jpg")!
let imageData = UIImageJPEGRepresentation(appleImage, 1)! (1)

let blob = Blob(contentType: "image/jpeg", data: imageData) (2)
newTask.setBlob(blob, forKey: "avatar") (3)
try collection.save(document:newTask)

if let taskBlob = newTask.blob(forKey: "image") {
    image = UIImage(data: taskBlob.content!)
}
```

| **1** | Here we prepare a document to use for the example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Create the blob using the retrieved image.Here we set image/jpg as the blob MIME type.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **3** | Add the blob to a document, using avatar as the property keySaving the document generates a random access key for each blob stored in digest a SHA-1 encrypted property — see: [Figure 1](#img-blob).We can use the avatar key to retrieve the blob object later. Note, this is the identity of the blob assigned by us; the replication auto-generates a blob for attachments and assigns its own name to it (for example, blob\_1) — see [Figure 1](#img-blob). The digest key will be the same as generated when we saved the blob document. |

## [](#syncing)Syncing

When a document containing a blob object is synchronized, the Couchbase Lite replicator generates an `_attachments` dictionary with an auto-generated name for each blob attachment. This is different to the `avatar` key and is used internally to access the blob content.

If you view a sync’d blob document in {cbs} Admin Console, you will see something similar to [Figure 1](#img-blob), which shows the document with its generated `_attachments` dictionary, including the `digest`.

![attach replicated](../_images/attach-replicated.png) 

Figure 1\. Sample Blob Document

## [](#related-content)Related Content

### [](#)

How to . . .

* [Prerequisites](gs-prereqs.md)
* [Install](gs-install.md)
* [Build and Run](gs-build.md)

.

### [](#-2)

Learn more . . .

* [Databases](database.md)
* [Documents](document.md)
* [Blobs](blob.md)
* [Remote Sync Gateway](replication.md)
* [Handling Data Conflicts](conflict.md)

.

### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.