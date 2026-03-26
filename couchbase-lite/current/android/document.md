---
title: Documents
description: Couchbase Lite concepts -- Data model -- Documents
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.0/modules/android/pages/document.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:couchbase-lite:android:document.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/current/android/document.html)

# Documents

> Description — _Couchbase Lite concepts — Data model — Documents_  
> Related Content — [Databases](database.md) | [Blobs](blob.md) | [Indexing](indexing.md) |

## [](#overview)Overview

### [](#document-structure)Document Structure

In _Couchbase Lite_ the term 'document' refers to an entry in the database. You can compare it to a record, or a row in a table.

Each document has an ID or unique identifier. This ID is similar to a primary key in other databases.

You can specify the ID programmatically. If you omit it, it will be automatically generated as a UUID.

> [!NOTE]
> Couchbase documents are assigned to a [Collection](database.md#database-concepts). The ID of a document must be unique within the Collection it is written to. You cannot change it after you have written the document.

The document also has a value which contains the actual application data. This value is stored as a dictionary of key-value (k-v) pairs. The values can be made of up several different [Data Types](#data-types) such as numbers, strings, arrays, and nested objects.

### [](#data-encoding)Data Encoding

The document body is stored in an internal, efficient, binary form called [Fleece](https://github.com/couchbaselabs/fleece#readme). This internal form can be easily converted into a manageable native dictionary format for manipulation in applications.

Fleece data is stored in the smallest format that will hold the value whilst maintaining the integrity of the value.

### [](#fleece-data-encoding)Fleece data encoding

When working with Android-Java, the Fleece encoding cycle can result in the Java type information being lost. Therefore care should be taken with non-explicit functions such as `toArray()` or `toMap()`, when storing and recovering data in a document, or converting that document to JSON and back.

Always use explicit creation of the expected type, whenever the type of result is not itself explicit. For example:

* Java
* Kotlin

```Java
Document doc = collection.getDocument(someDoc.getId());
// force longVal to be type Long, even if it could be represented as an int.
long longVal = doc.getLong("test");
```

```Kotlin
val doc = collection.getDocument (someDoc.id)
// force longVal to be type Long, even if it could be represented as an Int.
val longVal = doc?.getLong(("test"))
```

Similarly, interpreting data not stored as `boolean` as a boolean value can give inconsistent results.

### [](#data-types)Data Types

The `Document` class offers a set of property accessors for various scalar types, such as:

* Boolean
* Date
* Double
* Float
* Int
* Long
* String

These accessors take care of converting to/from JSON encoding, and make sure you get the type you expect.

In addition to these basic data types Couchbase Lite provides for the following:

Dictionary

represents a read-only key-value pair collection

MutableDictionary

represents a writeable key-value pair collection

Array

represents a readonly ordered collection of objects

MutableArray

represents a writeable collection of objects

Blob

represents an arbitrary piece of binary data

### [](#json)JSON

Couchbase Lite also provides for the direct handling of JSON data implemented in most cases by the provision of a `toJSON()` method on appropriate API classes (for example, on MutableDocument, Dictionary, Blob and Array) — see [Working with JSON Data](#lbl-json-data).

## [](#constructing-a-document)Constructing a Document

An individual document often represents a single instance of an object in application code.

You can consider a document as the equivalent of a 'row' in a relational table, with each of the document's attributes being equivalent to a 'column'.

Documents can contain nested structures. This allows developers to express many-to-many relationships without requiring a reference or join table, and is naturally expressive of hierarchical data.

Most apps will work with one or more documents, persisting them to a local database and optionally syncing them, either centrally or to the cloud.

In this section we provide an example of how you might create a `hotel` document, which provides basic contact details and price data.

Data Model

```Kotlin
hotel: {
  type: string (value = `hotel`)
  name: string
  address: dictionary {
    street: string
    city: string
    state: string
    country: string
    code: string
  }
  phones: array
  rate: float
}
```

### [](#ex-usage)Open a Database

First open your database. If the database does not already exist, Couchbase Lite will create it for you.

Couchbase documents are assigned to a [Collection](database.md#database-concepts). All the CRUD examples in this document operate on a `collection` object (here, the Default Collection).

* Kotlin
* Java

```Kotlin
// Initialize the Couchbase Lite system
CouchbaseLite.init(context)

// Get the database (and create it if it doesn’t exist).
val database = Database("getting-started")
val collection = database.getCollection("myCollection")
    ?: throw IllegalStateException("collection not found")
```

```Java
// Get the database (and create it if it doesn’t exist).
Database database = new Database("getting-started");
try (Collection collection = database.getCollection("myCollection")) {
    if (collection == null) { throw new IllegalStateException("collection not found"); }
```

See [Databases](database.md) for more information

### [](#create-a-document)Create a Document

Now create a new document to hold your application's data.

Use the mutable form, so that you can add data to the document.

* Kotlin
* Java

```Kotlin
// Create your new document
val mutableDoc = MutableDocument()
```

```Java
// Create your new document
MutableDocument mutableDoc = new MutableDocument();
```

For more on using **Documents**, see [Document Initializers](#document-initializers) and [Mutability](#mutability).

### [](#create-a-dictionary)Create a Dictionary

Now create a mutable dictionary (`address`).

Each element of the dictionary value will be directly accessible via its own key.

* Kotlin
* Java

```Kotlin
// Create a new mutable dictionary and populate some keys/values
val address = MutableDictionary()
address.setString("street", "1 Main st.")
address.setString("city", "San Francisco")
address.setString("state", "CA")
address.setString("country", "USA")
address.setString("code", "90210")
```

```Java
// Create a new mutable dictionary and populate some keys/values
MutableDictionary address = new MutableDictionary();
address.setString("street", "1 Main st.");
address.setString("city", "San Francisco");
address.setString("state", "CA");
address.setString("country", "USA");
address.setString("code", "90210");
```

Learn more about [Using Dictionaries](#using-dictionaries).

### [](#create-an-array)Create an Array

Since the hotel may have multiple contact numbers, provide a field (`phones`) as a mutable array.

* Kotlin
* Java

```Kotlin
// Create and populate mutable array
val phones = MutableArray()
phones.addString("650-000-0000")
phones.addString("650-000-0001")
```

```Java
// Create and populate mutable array
MutableArray phones = new MutableArray();
phones.addString("650-000-0000");
phones.addString("650-000-0001");
```

Learn more about [Using Arrays](#using-arrays)

### [](#populate-a-document)Populate a Document

Now add your data to the mutable document created earlier. Each data item is stored as a key-value pair.

* Kotlin
* Java

```Kotlin
// Initialize and populate the document

// Add document type to document properties (1)
mutableDoc.setString("type", "hotel")

// Add hotel name string to document properties (2)
mutableDoc.setString("name", "Hotel Java Mo")

// Add float to document properties (3)
mutableDoc.setFloat("room_rate", 121.75f)

// Add dictionary to document's properties (4)
mutableDoc.setDictionary("address", address)

// Add array to document's properties (5)
mutableDoc.setArray("phones", phones)
```

```Java
// Initialize and populate the document

// Add document type to document properties (1)
mutableDoc.setString("type", "hotel");

// Add hotel name string to document properties (2)
mutableDoc.setString("name", "Hotel Java Mo");

// Add float to document properties (3)
mutableDoc.setFloat("room_rate", 121.75F);

// Add dictionary to document's properties (4)
mutableDoc.setDictionary("address", address);

// Add array to document's properties (5)
mutableDoc.setArray("phones", phones);
```

> [!NOTE]
> Couchbase recommend using a `type` attribute to define each logical document type.

### [](#save-a-document)Save a Document

Now persist the populated document to your Couchbase Lite database. This will auto-generate the document id.

* Kotlin
* Java

```Kotlin
// Save the document changes (1)
collection.save(mutableDoc)
```

```Java
// Save the document changes (1)
collection.save(mutableDoc);
```

### [](#close-the-database)Close the Database

With your document saved, you can now close our Couchbase Lite database.

* Kotlin
* Java

```Kotlin
// Close the database (1)
database.close()
```

```Java
// Close the database (1)
database.close();
```

## [](#working-with-data)Working with Data

### [](#checking-a-documents-properties)Checking a Document's Properties

To check whether a given property exists in the document, use the [\`Document.Contains(String key)](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-android/com/couchbase/lite/Document.html#contains-java.lang.String-) method.

If you try to access a property which doesn't exist in the document, the call will return the default value for that getter method (0 for [Document.getInt()](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-android/com/couchbase/lite/Document.html#getInt-java.lang.String-) 0.0 for [Document.getFloat()](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-android/com/couchbase/lite/Document.html#getFloat-java.lang.String-) etc.).

> [!NOTE]
> Fleece data encoding
> 
> Care should be taken when storing and recovering data in a document or converting that document to JSON and back.  
> Data encoding (Fleece) can result in `Long` values being converted to `Integer`, and `Double` values to `Float`.  
> Interpreting data as boolean can also give inconsistent results.

### [](#date-accessors)Date accessors

Couchbase Lite offers _Date_ accessors as a convenience. Dates are a common data type, but JSON doesn't natively support them, so the convention is to store them as strings in ISO-8601 format.

Example 1\. Date Getter

This example sets the date on the `createdAt` property and reads it back using the [Document.getDate()](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-android/com/couchbase/lite/Document.html#getDate-java.lang.String-) accessor method.

* Kotlin
* Java

```Kotlin
doc.setValue("createdAt", Date())
val date = doc.getDate("createdAt")
```

```Java
newTask.setValue("createdAt", new Date());
Date date = newTask.getDate("createdAt");
```

### [](#using-dictionaries)Using Dictionaries

API References

* [Dictionary](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-android/com/couchbase/lite/Dictionary.html)
* [MutableDictionary](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-android/com/couchbase/lite/MutableDictionary.html)

Example 2\. Read Only

* Kotlin
* Java

```Kotlin
// NOTE: No error handling, for brevity (see getting started)
val document = collection.getDocument("doc1")

// Getting a dictionary from the document's properties
val dict = document?.getDictionary("address")

// Access a value with a key from the dictionary
val street = dict?.getString("street")

// Iterate dictionary
dict?.forEach { println("$it -> ${dict.getValue(it)}") }

// Create a mutable copy
val mutableDict = dict?.toMutable()
```

```Java
// NOTE: No error handling, for brevity (see getting started)
Document document = collection.getDocument("doc1");
if (document == null) { return; }

// Getting a dictionary from the document's properties
Dictionary dict = document.getDictionary("address");
if (dict == null) { return; }

// Access a value with a key from the dictionary
String street = dict.getString("street");

// Iterate dictionary
for (String key: dict.getKeys()) {
    System.out.println("Key " + key + " = " + dict.getValue(key));
}

// Create a mutable copy
MutableDictionary mutableDict = dict.toMutable();
```

Example 3\. Mutable

* Kotlin
* Java

```Kotlin
// NOTE: No error handling, for brevity (see getting started)

// Create a new mutable dictionary and populate some keys/values
val mutableDict = MutableDictionary()
mutableDict.setString("street", "1 Main st.")
mutableDict.setString("city", "San Francisco")

// Add the dictionary to a document's properties and save the document
val mutableDoc = MutableDocument("doc1")
mutableDoc.setDictionary("address", mutableDict)
collection.save(mutableDoc)
```

```Java
// NOTE: No error handling, for brevity (see getting started)

// Create a new mutable dictionary and populate some keys/values
MutableDictionary mutableDict = new MutableDictionary();
mutableDict.setString("street", "1 Main st.");
mutableDict.setString("city", "San Francisco");

// Add the dictionary to a document's properties and save the document
MutableDocument mutableDoc = new MutableDocument("doc1");
mutableDoc.setDictionary("address", mutableDict);
collection.save(mutableDoc);
```

### [](#using-arrays)Using Arrays

API References

* [Array](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-android/com/couchbase/lite/Array.html)
* [MutableArray](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-android/com/couchbase/lite/MutableArray.html)

Example 4\. Read Only

* Kotlin
* Java

```Kotlin
// NOTE: No error handling, for brevity (see getting started)

val document = collection.getDocument("doc1")

// Getting a phones array from the document's properties
val array = document?.getArray("phones")

// Get element count
val count = array?.count()

// Access an array element by index
val phone = array?.getString(1)

// Iterate array
array?.forEachIndexed { index, item -> println("Row  $index = $item") }

// Create a mutable copy
val mutableArray = array?.toMutable()
```

```Java
// NOTE: No error handling, for brevity (see getting started)

Document document = collection.getDocument("doc1");
if (document == null) { return; }

// Getting a phones array from the document's properties
Array array = document.getArray("phones");
if (array == null) { return; }

// Get element count
int count = array.count();

// Access an array element by index
String phone = array.getString(1);

// Iterate array
for (int i = 0; i < count; i++) {
    System.out.println("Row  " + i + " = " + array.getString(i));
}

// Create a mutable copy
MutableArray mutableArray = array.toMutable();
```

Example 5\. Mutable

* Kotlin
* Java

```Kotlin
// NOTE: No error handling, for brevity (see getting started)

// Create a new mutable array and populate data into the array
val mutableArray = MutableArray()
mutableArray.addString("650-000-0000")
mutableArray.addString("650-000-0001")

// Set the array to document's properties and save the document
val mutableDoc = MutableDocument("doc1")
mutableDoc.setArray("phones", mutableArray)
collection.save(mutableDoc)
```

```Java
// NOTE: No error handling, for brevity (see getting started)

// Create a new mutable array and populate data into the array
MutableArray mutableArray = new MutableArray();
mutableArray.addString("650-000-0000");
mutableArray.addString("650-000-0001");

// Set the array to document's properties and save the document
MutableDocument mutableDoc = new MutableDocument("doc1");
mutableDoc.setArray("phones", mutableArray);
collection.save(mutableDoc);
```

### [](#using-blobs)Using Blobs

For more on working with blobs, see [Blobs](blob.md)

## [](#document-initializers)Document Initializers

You can use the following methods/initializers:

* Use the [MutableDocument()](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-android/com/couchbase/lite/MutableDocument.html#s:18CouchbaseLiteSwift15MutableDocumentMutableDocument--) initializer to create a new document where the document ID is randomly generated by the database.
* Use the [MutableDocument(String id)](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-android/com/couchbase/lite/MutableDocument.html#s:18CouchbaseLiteSwift15MutableDocument}MutableDocument-java.lang.String-) initializer to create a new document with a specific ID.
* Use the {url-api-method-collection-getdocument} method to get a document. If the document doesn't exist in the collection, the method will return `null`. You can use this behavior to check if a document with a given ID already exists in the collection.

Example 6\. Persist a document

The following code example creates a document and persists it to the database.

* Kotlin
* Java

```Kotlin
val doc = MutableDocument()
doc.let {
    it.setString("type", "task")
    it.setString("owner", "todo")
    it.setDate("createdAt", Date())
}
collection.save(doc)
```

```Java
MutableDocument newTask = new MutableDocument();
newTask.setString("type", "task");
newTask.setString("owner", "todo");
newTask.setDate("createdAt", new Date());
collection.save(newTask);
```

## [](#mutability)Mutability

By default, a document is immutable when it is read from the database. Use the [\`Document.toMutable()](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-android/com/couchbase/lite/Document.html#toMutable--) to create an updatable instance of the document.

Example 7\. Make a mutable document

Changes to the document are persisted to the database when the `save` method is called.

* Kotlin
* Java

```Kotlin
collection.getDocument("xyz")?.toMutable()?.let {
    it.setString("name", "apples")
    collection.save(it)
}
```

```Java
MutableDocument mutableDocument = collection.getDocument("xyz").toMutable();
mutableDocument.setString("name", "apples");
collection.save(mutableDocument);
```

> [!NOTE]
> Any user change to the value of reserved keys (`_id`, `_rev` or `_deleted`) will be detected when a document is saved and will result in an exception (Error Code 5 — `CorruptRevisionData`) — see also [Document Constraints](#lbl-doc-constraints).

## [](#batch-operations)Batch operations

If you're making multiple changes to a database at once, it's faster to group them together. The following example persists a few documents in batch.

Example 8\. Batch operations

* Kotlin
* Java

```Kotlin
database.inBatch(UnitOfWork {
    for (i in 0..9) {
        val doc = MutableDocument()
        doc.let {
            it.setValue("type", "user")
            it.setValue("name", "user $i")
            it.setBoolean("admin", false)
        }
        log("saved user document: ${doc.getString("name")}")
    }
})
```

```Java
database.inBatch(() -> {
    for (int i = 0; i < 10; i++) {
        MutableDocument doc = new MutableDocument();
        doc.setValue("type", "user");
        doc.setValue("name", "user " + i);
        doc.setBoolean("admin", false);
        collection.save(doc);
    }
});
```

At the **local** level this operation is still transactional: no other `Database` instances, including ones managed by the replicator can make changes during the execution of the block, and other instances will not see partial changes. But Couchbase Mobile is a distributed system, and due to the way replication works, there's no guarantee that Sync Gateway or other devices will receive your changes all at once.

## [](#document-change-events)Document change events

You can register for document changes. The following example registers for changes to the document with ID `user.john` and prints the `verified_account` property when a change is detected.

Example 9\. Document change events

* Kotlin
* Java

```Kotlin
collection.addDocumentChangeListener("user.john") { change ->
    collection.getDocument(change.documentID)?.let {
        log("Status: ${it.getString("verified_account")}")
    }
}
```

```Java
collection.addDocumentChangeListener(
    "user.john",
    change -> {
        String docId = change.getDocumentID();
        try {
            Document doc = collection.getDocument(docId);
            if (doc != null) {
                Logger.log("Status: " + doc.getString("verified_account"));
            }
        }
        catch (CouchbaseLiteException e) {
            Logger.log("Failed getting doc : " + docId);
        }
    });
```

### [](#using-kotlin-flows-and-livedata)Using Kotlin Flows and LiveData

Kotlin users can also take advantage of Flows and LiveData to monitor for changes.

The following methods show how to watch for document changes in a given collection or for changes to a specific document.

* Collection Changes
* Document Changes

```Kotlin
        return collection.collectionChangeFlow(null)
            .map { it.documentIDs }
            .asLiveData()
```

```Kotlin
        return collection.documentChangeFlow("1001")
            .mapNotNull { change ->
                change.takeUnless {
                    collection.getDocument(it.documentID)?.getString("owner").equals(owner)
                }
            }
            .asLiveData()
```

## [](#document-expiration)Document Expiration

Document expiration allows users to set the expiration date for a document. When the document expires, it is purged from the database. The purge is not replicated to Sync Gateway.

Example 10\. Set document expiration

This example sets the TTL for a document to 1 day from the current time.

* Kotlin
* Java

```Kotlin
// Purge the document one day from now
collection.setDocumentExpiration(
    "doc123",
    Date(System.currentTimeMillis() + (1000 * 60 * 60 * 24))
)

// Reset expiration
collection.setDocumentExpiration("doc1", null)

// Query documents that will be expired in less than five minutes
val query = QueryBuilder
    .select(SelectResult.expression(Meta.id))
    .from(DataSource.collection(collection))
    .where(
        Meta.expiration.lessThan(
            Expression.longValue(System.currentTimeMillis() + (1000 * 60 * 5))
        )
    )
```

```Java
// Purge the document one day from now
Instant ttl = Instant.now().plus(1, ChronoUnit.DAYS);
collection.setDocumentExpiration("doc123", new Date(ttl.toEpochMilli()));

// Reset expiration
collection.setDocumentExpiration("doc1", null);

// Query documents that will be expired in less than five minutes
Instant fiveMinutesFromNow = Instant.now().plus(5, ChronoUnit.MINUTES);
Query query = QueryBuilder
    .select(SelectResult.expression(Meta.id))
    .from(DataSource.collection(collection))
    .where(Meta.expiration.lessThan(Expression.doubleValue(fiveMinutesFromNow.toEpochMilli())));
```

You can set expiration for a whole Collection

## [](#lbl-doc-constraints)Document Constraints

Couchbase Lite APIs do not explicitly disallow the use of attributes with the underscore prefix at the top level of document. This is to facilitate the creation of documents for use either in _local only_ mode where documents are not synced, or when used exclusively in peer-to-peer sync.

> [!NOTE]
> "\_id", :"\_rev" and "\_sequence" are reserved keywords and must not be used as top-level attributes — see [Example 11](#res-keys).

Users are cautioned that any attempt to sync such documents to Sync Gateway will result in an error. To be future proof, you are advised to avoid creating such documents. Use of these attributes for user-level data may result in undefined system behavior.

For more guidance — see: [Sync Gateway - data modeling guidelines](../../../sync-gateway/current/data-modeling.md)

Example 11\. Reserved Keys List

* \_attachments
* \_deleted \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]
* \_id \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]
* \_removed
* \_rev \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]
* \_sequence

## [](#lbl-json-data)Working with JSON Data

In this section

[Arrays](#lbl-array)| [Blobs](#lbl-blob)| [Dictionaries](#lbl-dictionary)| [Documents](#lbl-document)| [Query Results as JSON](#lbl-result)

The `toJSON()` typed-accessor means you can easily work with JSON data, native and Couchbase Lite objects.

### [](#lbl-array)Arrays

Convert an `ArrayObject` to and from JSON using the `toJSON()` and `toArray` methods — see [Example 4](#ex-array).

Additionally you can:

* Initialize a 'MutableArrayObject' using data supplied as a JSON string. This is done using the `init(json)` constructor
* Convert an `ArrayFragment` object to a JSON String
* Set data with a JSON string using `setJSON()`

Example 12\. Arrays as JSON strings

* Kotlin
* Java

```Kotlin
// github tag=tojson-array
val mArray = MutableArray(JSON) (1)
for (i in 0 until mArray.count()) {
    mArray.getDictionary(i)?.apply {
        log(getString("name") ?: "unknown")
        collection.save(MutableDocument(getString("id"), toMap()))
    } (2)
}

collection.getDocument("1002")?.getArray("features")?.apply {
    for (feature in toList()) {
        log("$feature")
    } (3)
    log(toJSON())
} (4)
```

```Java
// github tag=tojson-array
final MutableArray mArray = new MutableArray(JSON); (1)

for (int i = 0; i < mArray.count(); i++) { (2)
    final Dictionary dict = mArray.getDictionary(i);
    Logger.log(dict.getString("name"));
    collection.save(new MutableDocument(dict.getString("id"), dict.toMap()));
}

final Array features = collection.getDocument("1002").getArray("features");
for (Object feature: features.toList()) { Logger.log(feature.toString()); }
Logger.log(features.toJSON()); (3)
```

### [](#lbl-blob)Blobs

Convert a `Blob` to JSON using the `toJSON` method — see [Example 13](#ex-blob).

You can use `isBlob()` to check whether a given dictionary object is a blob or not.

Note that the blob object must first be saved to the database (generating the required metadata) before you can use the `toJSON` method.

Example 13\. Blobs as JSON strings

* Kotlin
* Java

```Kotlin
// github tag=tojson-blob
val thisBlob = collection.getDocument("thisdoc-id")!!.toMap()
if (!Blob.isBlob(thisBlob)) {
    return
}
val blobType = thisBlob["content_type"].toString()
val blobLength = thisBlob["length"] as Number?
```

```Java
// github tag=tojson-blob
final Map<String, ?> thisBlob = collection.getDocument("thisdoc-id").toMap();
if (!Blob.isBlob(thisBlob)) { return; }

final String blobType = thisBlob.get("content_type").toString();
final Number blobLength = (Number) thisBlob.get("length");
```

See also: [Blobs](blob.md)

### [](#lbl-dictionary)Dictionaries

Convert a `DictionaryObject` to and from JSON using the `toJSON` and `toDictionary` methods — see [Example 14](#ex-dictionary).

Additionally you can:

* Initialize a `MutableDictionaryObject` using data supplied as a JSON string. This is done using the `init(json)` constructor
* Set data with a JSON string using `setJSON()`

Example 14\. Dictionaries as JSON strings

* Kotlin
* Java

```Kotlin
// github tag=tojson-dictionary
val mDict = MutableDictionary(JSON) (1)
log("$mDict")
log("Details for: ${mDict.getString("name")}")
mDict.keys.forEach { key ->
    log(key + " => " + mDict.getValue(key))
}
```

```Java
// github tag=tojson-dictionary
final MutableDictionary mDict = new MutableDictionary(JSON); (1)
Logger.log(mDict.toString());

Logger.log("Details for: " + mDict.getString("name"));
for (String key: mDict.getKeys()) {
    Logger.log(key + " => " + mDict.getValue(key));
}
```

### [](#lbl-document)Documents

Convert a `Document` to and from JSON strings using the `toJSON()` and `setJSON()` methods — see [Example 15](#ex-document).

Additionally you can:

* Initialize a `MutableDocument` using data supplied as a JSON string. This is done using the `init(json)` or `init(id: json:)` constructor.
* Set data with a JSON string using `setJSON()`

Example 15\. Documents as JSON strings

* Kotlin
* Java

```Kotlin
QueryBuilder
    .select(SelectResult.expression(Meta.id).`as`("metaId"))
    .from(DataSource.collection(srcColl))
    .execute()
    .forEach {
        it.getString("metaId")?.let { thisId ->
            srcColl.getDocument(thisId)?.toJSON()?.let { json -> (1)
                log("JSON String = $json")
                val hotelFromJSON = MutableDocument(thisId, json) (2)
                dstColl.save(hotelFromJSON)
                dstColl.getDocument(thisId)?.toMap()?.forEach { e ->
                    log("$e.key => $e.value")
                } (3)
            }
        }
    }
```

```Java
// github tag=tojson-document
final Query listQuery = QueryBuilder
    .select(SelectResult.expression(Meta.id).as("metaId"))
    .from(DataSource.collection(srcColl));

try (ResultSet results = listQuery.execute()) {
    for (Result row: results) {
        final String thisId = row.getString("metaId");

        final String json = srcColl.getDocument(thisId).toJSON(); (1)
        Logger.log("JSON String = " + json);

        final MutableDocument hotelFromJSON = new MutableDocument(thisId, json); (2)

        dstColl.save(hotelFromJSON);

        for (Map.Entry<String, Object> entry: dstColl.getDocument(thisId).toMap().entrySet()) {
            Logger.log(entry.getKey() + " => " + entry.getValue()); (3)
        }
    }
}
```

### [](#lbl-result)Query Results as JSON

Convert a `Query Result` to JSON using its {to-JSON} accessor method.

Example 16\. Using JSON Results

Use [Result.toJSON()](https://docs.couchbase.com/mobile/4.0.3/couchbase-lite-android/com/couchbase/lite/Result.html#toJSON--) to transform your result string into a JSON string, which can easily be serialized or used as required in your application.

* Kotlin
* Java

```Kotlin
// Uses Jackson JSON processor
val mapper = ObjectMapper()
val hotels = mutableListOf<Hotel>()

listQuery.execute().use { rs ->
    rs.forEach {

        // Get result as JSON string
        val json = it.toJSON() (1)

        // Get Hashmap from JSON string
        val dictFromJSONstring = mapper.readValue(json, HashMap::class.java) (2)

        // Use created hashmap
        val hotelId = dictFromJSONstring["id"].toString() //
        val hotelType = dictFromJSONstring["type"].toString()
        val hotelname = dictFromJSONstring["name"].toString()

        // Get custom object from JSON string
        val thisHotel = mapper.readValue(json, Hotel::class.java) (3)
        hotels.add(thisHotel)
    }
}
```

```Java
// Uses Jackson JSON processor
ObjectMapper mapper = new ObjectMapper();
List<Hotel> hotels = new ArrayList<>();

try (ResultSet rs = listQuery.execute()) {
    for (Result result: rs) {
        String json = result.toJSON();
        Map<String, String> dictFromJSONstring = mapper.readValue(json, HashMap.class);

        String hotelId = dictFromJSONstring.get("id");
        String hotelType = dictFromJSONstring.get("type");
        String hotelname = dictFromJSONstring.get("name");

        // Get custom object from JSON string
        Hotel thisHotel = mapper.readValue(json, Hotel.class);
        hotels.add(thisHotel);
    }
}
```

JSON String Format

If your query selects ALL then the JSON format will be:

```JSON
{
  database-name: {
    key1: "value1",
    keyx: "valuex"
  }
}
```

If your query selects a sub-set of available properties then the JSON format will be:

```JSON
{
  key1: "value1",
  keyx: "valuex"
}
```

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

---

[1](#%5Ffootnoteref%5F1). Any change to this reserved key will be detected when it is saved and will result in a Couchbase exception (Error Code 5 — `CorruptRevisionData`)