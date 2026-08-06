---
title: Document Expiry
description: Setting an expiry lets you control how long Couchbase keeps a document.
editUrl: https://github.com/couchbase/docs-sdk-kotlin/edit/temp/3.12/modules/howtos/pages/document-expiry.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:kotlin-sdk:howtos:document-expiry.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/kotlin-sdk/current/howtos/document-expiry.html)

# Document Expiry

> Setting an expiry lets you control how long Couchbase keeps a document. 

A document's "expiry" is the time when Couchbase should delete the document.

Normally, a document does not expire. It stays in a collection until you remove it. \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]This is good if you need to keep the document forever, or if you don't know how long you need to keep the document.

You can tell Couchbase a document should expire after some time. This is good for temporary data, like a cache or a user's web session. This can also help you follow privacy laws that say you must delete old data about users.

There are different ways to set a document's expiry.

## [](#prerequisites)Before You Start

You should know [how to do Key Value operations](kv-operations.md).

## [](#set-a-documents-expiry)Set a document's expiry

A CRUD operation that changes a document can set the document's expiry. Here is an upsert operation that tells Couchbase to delete the document 3 hours in the future:

Upserting a document that expires 3 hours in the future

```kotlin
collection.upsert(
    id = "alice",
    content = mapOf("favoriteColor" to "red"),
    expiry = Expiry.of(3.hours), (1)
)
```

| **1** | 3.hours is a kotlin.time.Duration. You can say seconds, minutes, hours, or days. |
| ----- | -------------------------------------------------------------------------------- |

### [](#touch)Set expiry without changing the document

The `touch` method sets a document's expiry, but does not change the document content. This is good for making a temporary document live longer.

Set a document's expiry

```kotlin
try {
    collection.touch(
        id = "alice",
        expiry = Expiry.of(3.hours),
    )
} catch (t: DocumentNotFoundException) {
    println("Touch failed because the document does not exist.")
}
```

The `getAndTouch` method reads a document and sets its expiry at the same time. This is more efficient than calling `get` and `touch` separately.

Read a document and set its expiry at the same time

```kotlin
try {
    val result: GetResult = collection.getAndTouch(
        id = "alice",
        expiry = Expiry.of(3.hours), (1)
    )
    val content = result.contentAs<Map<String, Any?>>()
    println("The character's favorite color is ${content["favoriteColor"]}")
} catch (t: DocumentNotFoundException) {
    println("GetAndTouch failed because the document does not exist.")
}
```

| **1** | This line is the only difference from the [get](kv-operations.md#get) example. |
| ----- | ------------------------------------------------------------------------------ |

### [](#get-expiry)Get a document's expiry

To get a document's expiry, call the `get` method and pass `withExpiry = true`. The `get` method returns a `GetResult` object. The result's `expiry` property tells you when the document expires.

> [!CAUTION]
> If you do not pass `withExpiry = true`, the result's `expiry` is `Expiry.Unknown`. The SDK only gets the expiry if you ask for it, because it's faster to not get the expiry.

If the expiry is an instance of `Expiry.None`, the document does not expire. If the expiry is an instance of `Expiry.Absolute`, the expiry's `instant` property is when the document expires.

Getting a document's expiry

```kotlin
val result: GetResult = collection.get(
    id = "alice",
    withExpiry = true, (1)
)

when (val expiry = result.expiry) {
    is Expiry.None -> println("Document does not expire.")
    is Expiry.Absolute -> println("Document expires at ${expiry.instant}.")
    else -> println("Oops, forgot to pass `withExpiry = true`.")
}
```

| **1** | If you do not say withExpiry = true, then result.expiry is Expiry.Unknown. |
| ----- | -------------------------------------------------------------------------- |

## [](#preserve-expiry)Change a document, but keep the old expiry

By default, changing a document also changes its expiry. If you do not pass a value for `expiry`, the document does not expire, _even if the document previously had an expiry_. If this is not what you want, you must tell Couchbase to keep the document's expiry.

If you use Couchbase 7 or newer, this is easy. If you use an older version of Couchbase, it's more work.

* Couchbase 7 or newer
* Before Couchbase 7

```kotlin
collection.replace(
    id = "alice",
    content = mapOf("favoriteColor" to "red"),
    preserveExpiry = true,
)
```

> [!CAUTION]
> This example just shows how to use the `preserveExpiry` parameter. When you replace a document, it's usually good to use [optimistic locking](kv-operations.md#optimistic-locking). Otherwise, changes might get lost if two threads or computers change the same document at the same time.

Copy the `Collection.mutate` extension function from the [optimistic locking](kv-operations.md#collection-mutate) section. This function has a `preserveExpiry` parameter that works with any version of Couchbase Server.

> [!TIP]
> A query that changes a document also removes the document expiry. If you use Couchbase Server 7.1 or later, you can change this behavior by passing `preserveExpiry = true` when calling the `query` method.

## [](#bucket-and-collection-maximum-time-to-live-ttl)Bucket and Collection Maximum Time-To-Live (TTL)

A bucket or collection can have a "maximum time-to-live" (Max TTL).

When a document is changed in a bucket or collection with a Max TTL, the document's expiry is set to the Max TTL, unless you say the document should expire sooner than the Max TTL.

You can set the Max TTL when you create the bucket or collection in the Couchbase Admin web interface, command-line interface, or Bucket Management API.

## [](#summary)Summary

You can tell Couchbase to delete a document in the future by assigning an expiry to the document.

Changing a document changes its expiry, unless you [tell Couchbase to preserve the existing expiry](#preserve-expiry). If you do not specify an expiry when changing a document, the document never expires, _even if it previously had an expiry_.

The expiry is included in a `GetResult`, but only if you pass `withExpiry = true` when calling `get`.

---

[1](#%5Ffootnoteref%5F1). When you create a bucket, you can choose how the bucket stores your documents. One choice is to make an "ephemeral" bucket. An ephemeral bucket is like a cache. It stores documents only in memory, not on disk. If there's not enough memory to put a new document in an ephemeral bucket, Couchbase removes old documents even if they haven't expired yet.