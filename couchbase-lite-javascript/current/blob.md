---
title: Blobs
description: Couchbase Lite database data model concepts - blobs
editUrl: https://github.com/couchbaselabs/docs-couchbase-lite-js/edit/release/1.0/modules/ROOT/pages/blob.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:couchbase-lite-javascript::blob.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite-javascript/current/blob.html)

# Blobs

> Description — _Couchbase Lite database data model concepts - blobs_  
> Related Content — [Databases](database.md) | [Documents](document.md) | [Indexing](indexing.md) |

## [](#introduction)Introduction

Couchbase Lite for JavaScript uses _blobs_ to store the contents of images, other media files and similar format files as binary objects.

The blob itself is not stored in the document. It is held in a separate content-addressable store indexed from the document and retrieved only on-demand.

When a document is synchronized, the Couchbase Lite replicator adds an `_attachments` dictionary to the document's properties if it contains a blob.

## [](#blob-objects)Blob Objects

The blob as an object appears in a document as a dictionary property.

Other properties include `length` (the length in bytes), and optionally `contentType` (typically, its MIME type).

The blob's data (an image, audio or video content) is not stored in the document, but in a separate content-addressable store, indexed by the `digest` property — see [Using Blobs](#lbl-using).

### [](#constraints)Constraints

* Couchbase Lite  
Blobs can be arbitrarily large. They are only read on demand, not when you load the _document_.
* Sync Gateway  
The maximum content size is 20 MB per blob. If a document's blob is over 20 MB, the document will be replicated but not the blob.

## [](#lbl-using)Using Blobs

The `Blob` class in Couchbase Lite JavaScript provides methods to work with binary data. You can create blobs from various sources including File objects, ArrayBuffers, or URLs.

The code in [Example 1](#ex-blob) shows how you might add a blob to a document and save it to the database. Here we use `avatar` as the property key and an image file as the blob data.

Example 1\. Working with blobs

```javascript
// Create the blob from a File object
const fileInput = document.getElementById('avatarFile') as HTMLInputElement;
if (!fileInput?.files || fileInput.files.length === 0) {
    throw new Error('Please choose an image file first.');
}
const file = fileInput.files[0];
const buffer = new Uint8Array(await file.arrayBuffer());
const blob = new NewBlob(buffer, 'image/jpeg'); (1)

// Add the blob to a document
const user: CBLDictionary = {
    type: 'user',
    username: 'jane',
    email: 'jane@email.com',
    role: 'engineer',
    avatar: blob
};

// Create a document and save
const users = database.getCollection('users');
const doc = users.createDocument(DocID("profile1"), user);
const saved = await users.save(doc);
```

| **1** | Here we prepare a document to use for the example                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Create the blob from a File object (from a file input or drag-and-drop).Here we set image/jpeg as the blob MIME type.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **3** | Add the blob to a document, using avatar as the property keySaving the document generates a random access key for each blob stored in digest, a SHA-1 encrypted property — see: [\[img-blob\]](#img-blob).We can use the avatar key to retrieve the blob object later. Note, this is the identity of the blob assigned by us; the replication auto-generates a blob for attachments and assigns its own name to it (for example, blob\_1) — see [\[img-blob\]](#img-blob). The digest key will be the same as generated when we saved the blob document. |

## [](#creating-blobs)Creating Blobs

You can create blobs from different sources in the browser:

### [](#from-file-input)From File Input

Example 2\. Create blob from file input

```javascript
const fileInput = document.getElementById('avatarFile') as HTMLInputElement;
if (!fileInput?.files || fileInput.files.length === 0) {
    throw new Error('Please choose an image file first.');
}
const file = fileInput.files[0];
const buffer = new Uint8Array(await file.arrayBuffer());
const blob = new NewBlob(buffer, 'image/jpeg');
```

### [](#from-fetch)From Fetch API

Example 3\. Create blob from fetched data

```javascript
const response = await fetch('https://couchbase-example.com/images/avatar.jpg');
if (!response.ok) {
    throw new Error(`Failed to fetch image: ${response.status}`);
}

// Convert the response into binary data
const data = await response.arrayBuffer();

// Create a blob from the downloaded data
const buffer = new Uint8Array(await response.arrayBuffer());
const blob = new NewBlob(buffer, 'image/jpeg');
```

## [](#retrieving-blobs)Retrieving Blobs

Once a blob is saved in a document, you can retrieve it and access its content.

Example 4\. Retrieve and use blob

```javascript
const users = database.getCollection('users');
const doc = await users.getDocument(DocID("profile1"));
if (doc) {
    // Note: Import as { Blob as CBLBlob } from â€˜@couchbase/lite-jsâ€™ to
    // avoid conflict with the standard Blob type.
    const blob = doc.avatar as CBLBlob;
    if (blob instanceof CBLBlob) {
        const contentType = blob.content_type ?? "None";
        const length = blob.length ?? 0;
        const digest = blob.digest;
        console.log(`Blob info:
            Content-Type: ${contentType}
            Length: ${length} bytes
            Digest: ${digest}`
        );
        const content = await blob.getContents();
        // Use content as needed
    }
} else {
    console.log('User not found');
}
```

## [](#blob-properties)Blob Properties

Blob objects have several properties that provide information about the binary data:

* `contentType` \- The MIME type of the blob (e.g., "image/jpeg", "video/mp4")
* `length` \- The size of the blob in bytes
* `digest` \- The SHA-1 hash of the content, used for content-addressable storage
* `properties` \- Additional metadata stored with the blob

Example 5\. Access blob properties

```javascript
const contentType = blob.content_type ?? "None";
const length = blob.length ?? 0;
const digest = blob.digest;
console.log(`Blob info:
    Content-Type: ${contentType}
    Length: ${length} bytes
    Digest: ${digest}`
);
```

## [](#typescript-blobs)TypeScript Support

When using TypeScript, you can define document interfaces that include blob properties:

Example 6\. Type-safe blobs

```typescript
// Note: Import as { Blob as CBLBlob } from '@couchbase/lite-js'
// to avoid conflict with the standard Blob type.
interface UserSchema {
    type: 'user';
    username: string;
    email: string;
    role: string;
    avatar: CBLBlob | null;
}

const users = database.collections.users;
const doc = await users.getDocument(DocID("profile1"));
if (doc) {
    const blob = doc.avatar;
    if (blob) {
        const content = await blob.getContents();
        // Use content as needed
    }
}
```

## [](#syncing)Syncing

When a document containing a blob object is synchronized, the Couchbase Lite replicator generates an `_attachments` dictionary with an auto-generated name for each blob attachment. This is different to the `avatar` key and is used internally to access the blob content.

## [](#blob-metadata)Blob Metadata

Blobs in Couchbase Lite follow a specific metadata structure that allows the system to identify and retrieve binary content:

Blob metadata structure

```json
{
  "@type": "blob",
  "content_type": "image/jpeg",
  "length": 45678,
  "digest": "sha1-s1KdHLHCQqn/34fFxZqQRMHrQGk="
}
```

The `@type` property identifies this object as a blob rather than a regular nested object. The replicator uses this metadata to handle blob synchronization separately from document data.

## [](#related-content)Related Content

### [](#)

How to . . .

* [Prerequisites](gs-prereqs.md)
* [Install](gs-install.md)

.

### [](#-2)

Learn more . . .

* [Databases](database.md)
* [Documents](document.md)
* [Blobs](#)
* [Remote Sync Gateway](replication.md)
* [Handling Data Conflicts](conflict.md)

.

### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.