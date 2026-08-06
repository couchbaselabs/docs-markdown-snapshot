---
title: Kotlin Serialization
description: Couchbase Lite for Android -- Using native Kotlin serialization to
  save, retrieve, and query domain model objects
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.4/modules/android/pages/kotlin-serialization.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:3.4@couchbase-lite:android:kotlin-serialization.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.4/android/kotlin-serialization.html)

# Kotlin Serialization

> Description — _Couchbase Lite for Android — Using native Kotlin serialization to save, retrieve, and query domain model objects_  
> Related Content — [Documents](document.md) | [SQL++ for Mobile](query-n1ql-mobile.md) | [Query Resultsets](query-resultsets.md)

Couchbase Lite 3.4 for Android adds native support for `kotlinx.serialization`, allowing you to read and write domain model objects directly without manual field-by-field mapping.

## [](#define-document-model)Define a Document Model

A model class must implement `DocumentModel` and be annotated with `@Serializable`. The `documentMeta` property is managed by Couchbase Lite and must be marked `@Transient`.

Example 1\. Document model

```Kotlin
import com.couchbase.lite.DocumentMeta
import com.couchbase.lite.DocumentModel
import kotlinx.serialization.Serializable
import kotlinx.serialization.Transient

@Serializable
data class Profile(
    var name: String,
    var email: String,
    var city: String? = null,
    var interests: List<String> = emptyList()
) : DocumentModel {
    @Transient
    override var documentMeta: DocumentMeta? = null
}
```

## [](#save-document-model)Save a Document Model

Use `Collection.save()` with an optional document ID to save a model instance. After saving, Couchbase Lite populates `documentMeta` with the document ID and revision.

Example 2\. Save a model

```Kotlin
val profile = Profile(
    name = "Jane Doe",
    email = "jane@email.com",
    city = "San Francisco",
    interests = listOf("photography", "travel")
)

collection.save(profile, docID = "profile1")
```

## [](#get-document-model)Get a Document Model

Use `Collection.getDocumentAs<T>()` to retrieve and deserialize a document by ID. Returns `null` if the document does not exist.

Example 3\. Get a model

```Kotlin
val profile: Profile? =
    collection.getDocumentAs<Profile>("profile1")
```

## [](#decode-query-results)Decode Query Results

Use `ResultSet.data<T>()` to decode query result rows directly into model instances.

### [](#decode-query-results-column-match)From Column-Named Results

When the selected column names match your model property names, call `ResultSet.data<T>()` with no alias argument.

Example 4\. Decode results by column name

```Kotlin
val query = db.createQuery(
    "SELECT name, email, city, interests FROM $collectionName"
)

val profiles: List<Profile> =
    query.execute().use { rs ->
        rs.data<Profile>().toList()
    }
```

### [](#decode-query-results-select-star)From SELECT \* Results

When querying with `SELECT * AS <alias>`, pass the alias to `ResultSet.data<T>()` so Couchbase Lite knows which result column to deserialize.

Example 5\. Decode results from SELECT \*

```Kotlin
val query = db.createQuery(
    "SELECT * AS profile FROM $collectionName"
)

val profiles: List<Profile> =
    query.execute().use { rs ->
        rs.data<Profile>("profile").toList()
    }
```

### [](#decode-query-results-with-meta)With Document Metadata

To retrieve document models that can be modified and saved back to the collection, include `meta() AS <alias>` in the query. Pass both the document body alias and the metadata alias to `ResultSet.data<T>()`. Couchbase Lite populates `documentMeta` with the document ID and revision.

Example 6\. Decode results including document metadata

```Kotlin
val query = db.createQuery(
    "SELECT * AS profile, meta() AS meta FROM $collectionName"
)

val profilesWithMeta: List<Profile> =
    query.execute().use { rs ->
        rs.data<Profile>("profile", "meta").toList()
    }
```

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Prerequisites](gs-prereqs.md)
* [Install](gs-install.md)
* [Build and Run](gs-build.md)

.

###### [](#-2)

Learn more . . .

* [Databases](database.md)
* [Documents](document.md)
* [SQL++ for Mobile](query-n1ql-mobile.md)
* [Query Resultsets](query-resultsets.md)

.

###### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.