---
title: Documents
description: Couchbase Lite concepts -- Data model -- Documents
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.0/modules/android/pages/document.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:3.0@couchbase-lite:android:document.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.0/android/document.html)

# Documents

> Description — _Couchbase Lite concepts — Data model — Documents_  
> Related Content — [Databases](database.md) | [Blobs](blob.md) | [Indexing](indexing.md) |

## [](#overview)Overview

### [](#document-structure)Document Structure

In _Couchbase Lite_ the term 'document' refers to an entry in the database. You can compare it to a record, or a row in a table.

Each document has an ID or unique identifier. This ID is similar to a primary key in other databases.

You can specify the ID programmatically. If you omit it, it will be automatically generated as a UUID.

> [!NOTE]
> the ID must be unique within the database. You cannot change it after you have written the document.

The document also has a value which contains the actual application data. This value is stored as a dictionary collection of key-value (k-v) pairs. The values can be made of up several different [Data Types](#data-types) such as numbers, strings, arrays, and nested objects.

### [](#data-encoding)Data Encoding

The document body is stored in an internal, efficient, binary form called [Fleece](https://github.com/couchbaselabs/fleece#readme). This internal form can be easily converted into a manageable native dictionary format for manipulation in applications.

Fleece data is stored in the smallest format that will hold the value whilst maintaining the integrity of the value.

### Fleece data encoding

When working with Android-Java, the Fleece encoding cycle can result in the Java type information being lost. Therefore care should be taken with non-explicit functions such as `toArray()` or `toMap()`, when storing and recovering data in a document, or converting that document to JSON and back.

Always use explicit creation of the expected type, whenever the type of result is not itself explicit. For example:

```Java
Map<String, Object> doc = db.getDocument(someDoc.getId()).toMap();
Long testVal = Long.valueOf(doc.get(“test”))
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

You can consider a document as the equivalent of a 'row' in a relational table, with each of the document’s attributes being equivalent to a 'column'.

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

* Kotlin
* Java

```Kotlin
// Initialize the Couchbase Lite system
CouchbaseLite.init(context)

// Get the database (and create it if it doesn’t exist).
DatabaseConfiguration config = new DatabaseConfiguration()

config.setDirectory(context.getFilesDir().getAbsolutePath())

Database database = new Database("getting-started", config)
```

```Java
// Initialize the Couchbase Lite system
CouchbaseLite.init(context);

// Get the database (and create it if it doesn’t exist).
DatabaseConfiguration config = new DatabaseConfiguration();

config.setDirectory(context.getFilesDir().getAbsolutePath());

Database database = new Database("getting-started", config);
```

See [Databases](database.md) for more information

### [](#create-a-document)Create a Document

Now create a new document to hold your application’s data.

Use the mutable form, so that you can add data to the document.

* Kotlin
* Java

```Kotlin
// Create your new document
// The lack of 'const' indicates this document is mutable
MutableDocument mutableDoc = new MutableDocument()
```

```Java
// Create your new document
// The lack of 'const' indicates this document is mutable
MutableDocument mutableDoc = new MutableDocument();
```

For more on using **Documents**, see [Document Initializers](#document-initializers) and [Mutability](#mutability).

### [](#create-a-dictionary)Create a Dictionary

Now create a mutable dictionary (`address`).

Each element of the dictionary value will be directly accessible via its own key.

* Kotlin
* Java

```Kotlin
// Create and populate mutable dictionary
// Create a new mutable dictionary and populate some keys/values
MutableDictionary address = new MutableDictionary()
address.setString("street", "1 Main st.")
address.setString("city", "San Francisco")
address.setString("state", "CA")
address.setString("country", "USA")
address.setString("code"), "90210")
```

```Java
// Create and populate mutable dictionary
// Create a new mutable dictionary and populate some keys/values
MutableDictionary address = new MutableDictionary();
address.setString("street", "1 Main st.");
address.setString("city", "San Francisco");
address.setString("state", "CA");
address.setString("country", "USA");
address.setString("code"), "90210");
```

Learn more about [Using Dictionaries](#using-dictionaries).

### [](#create-an-array)Create an Array

Since the hotel may have multiple contact numbers, provide a field (`phones`) as a mutable array.

* Kotlin
* Java

```Kotlin
// Create and populate mutable array
MutableArray phones = new MutableArray()
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

// Add document type and hotel name as string
mutable_doc.setString("type", "hotel"))
mutable_doc.setString("name", "Hotel Java Mo"))

// Add average room rate (float)
mutable_doc.setFloat("room_rate", 121.75f)

// Add address (dictionary)
mutable_doc.setDictionary("address", address)

// Add phone numbers(array)
mutable_doc.setArray("phones", phones)
```

```Java
// Initialize and populate the document

// Add document type and hotel name as string
mutable_doc.setString("type", "hotel"));
mutable_doc.setString("name", "Hotel Java Mo"));

// Add average room rate (float)
mutable_doc.setFloat("room_rate", 121.75f);

// Add address (dictionary)
mutable_doc.setDictionary("address", address);

// Add phone numbers(array)
mutable_doc.setArray("phones", phones);
```

> [!NOTE]
> Couchbase recommend using a `type` attribute to define each logical document type.

### [](#save-a-document)Save a Document

Now persist the populated document to your Couchbase Lite database. This will auto-generate the document id.

* Kotlin
* Java

```Kotlin
database.save(mutable_doc)
```

```Java
database.save(mutable_doc);
```

### [](#close-the-database)Close the Database

With your document saved, you can now close our Couchbase Lite database.

* Kotlin
* Java

```Kotlin
database.close()
```

```Java
database.close();
```

## [](#working-with-data)Working with Data

### [](#checking-a-documents-properties)Checking a Document’s Properties

To check whether a given property exists in the document, use the [\`Document.Contains(String key)](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/Document.html#contains-java.lang.String-) method.

If you try to access a property which doesn’t exist in the document, the call will return the default value for that getter method (0 for [Document.getInt()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/Document.html#getInt-java.lang.String-) 0.0 for [Document.getFloat()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/Document.html#getFloat-java.lang.String-) etc.).

> [!NOTE]
> Fleece data encoding
> 
> Care should be taken when storing and recovering data in a document or converting that document to JSON and back.  
> Data encoding (Fleece) can result in `Long` values being converted to `Float` instead of `Double`.  
> Interpreting data as boolean can also give inconsistent results.

### [](#date-accessors)Date accessors

Couchbase Lite offers _Date_ accessors as a convenience. Dates are a common data type, but JSON doesn’t natively support them, so the convention is to store them as strings in ISO-8601 format.

Example 1\. Date Getter

This example sets the date on the `createdAt` property and reads it back using the [Document.getDate()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/Document.html#getDate-java.lang.String-) accessor method.

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

* [Dictionary](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/Dictionary.html)
* [MutableDictionary](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/MutableDictionary.html)

Example 2\. Read Only

* Kotlin
* Java

```Kotlin
  val document = database!!.getDocument("doc1")

  // Getting a dictionary from the document's properties
  val dict = document?.getDictionary("address")

  // Access a value with a key from the dictionary
  val street = dict?.getString("street")

  // Iterate dictionary
  for (key in dict!!.keys) {
      println("Key ${key} = ${dict.getValue(key)}")
  }

// Create a mutable copy
val mutable_Dict = dict.toMutable()
```

```Java
Document document = database.getDocument("doc1");

// Getting a dictionary from the document's properties
Dictionary dict = document.getDictionary("address");

// Access a value with a key from the dictionary
String street = dict.getString("street");

// Iterate dictionary
for (String key : dict) {
    dict.getValue(key);
    Log.i("x", "Key %s, = %s", key, dict.getValue(key));
}

// Create a mutable copy
MutableDictionary mutable_Dict = dict.toMutable();
```

Example 3\. Mutable

* Kotlin
* Java

```Kotlin
// Create a new mutable dictionary and populate some keys/values
val mutable_dict = MutableDictionary()
mutable_dict.setString("street", "1 Main st.")
mutable_dict.setString("city", "San Francisco")

// Add the dictionary to a document's properties and save the document
val mutable_doc = MutableDocument("doc1")
mutable_doc.setDictionary("address", mutable_dict)
database!!.save(mutable_doc)
```

```Java
// Create a new mutable dictionary and populate some keys/values
MutableDictionary mutable_dict = new MutableDictionary();
mutable_dict.setString("street", "1 Main st.");
mutable_dict.setString("city", "San Francisco");

// Add the dictionary to a document's properties and save the document
MutableDocument mutable_doc = new MutableDocument("doc1");
mutable_doc.setDictionary("address", mutable_dict);
database.save(mutable_doc);
```

### [](#using-arrays)Using Arrays

API References

* [Array](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/Array.html)
* [MutableArray](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/MutableArray.html)

Example 4\. Read Only

* Kotlin
* Java

```Kotlin
val document = database?.getDocument("doc1")

// Getting a phones array from the document's properties
val array = document?.getArray("phones")

// Get element count
val count = array?.count()

// Access an array element by index
val phone = array?.getString(1)

// Iterate array
for ( (index, item) in array!!) {
    println("Row  ${index} = ${item}")
}

// Create a mutable copy
val mutable_array = array.toMutable()
```

```Java
Document document = database.getDocument("doc1");

// Getting a phones array from the document's properties
Array array = document.getArray("phones");

// Get element count
int count = array.count();

// Access an array element by index
if (count >= 0) { String phone = array.getString(1); }

// Iterate dictionary
for (int i = 0; i < count; i++)
{
    Log.i("tag", "Item %d = %s", i, array.getString(i));
}

// Create a mutable copy
MutableArray mutable_array = array.toMutable();
```

Example 5\. Mutable

* Kotlin
* Java

```Kotlin
// Create a new mutable array and populate data into the array
val mutable_array = MutableArray()
mutable_array.addString("650-000-0000")
mutable_array.addString("650-000-0001")

// Set the array to document's properties and save the document
val mutable_doc = MutableDocument("doc1")
mutable_doc.setArray("phones", mutable_array)
database?.save(mutable_doc)
```

```Java
// Create a new mutable array and populate data into the array
MutableArray mutable_array = new MutableArray();
mutable_array.addString("650-000-0000");
mutable_array.addString("650-000-0001");

// Set the array to document's properties and save the document
MutableDocument mutable_doc = new MutableDocument("doc1");
mutable_doc.setArray("phones", mutable_array);
database.save(mutable_doc);
```

### [](#using-blobs)Using Blobs

For more on working with blobs, see [Blobs](blob.md)

## [](#document-initializers)Document Initializers

You can use the following methods/initializers:

* Use the [MutableDocument()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/MutableDocument.html#s:18CouchbaseLiteSwift15MutableDocumentMutableDocument--) initializer to create a new document where the document ID is randomly generated by the database.
* Use the [MutableDocument(String id)](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/MutableDocument.html#s:18CouchbaseLiteSwift15MutableDocument}MutableDocument-java.lang.String-) initializer to create a new document with a specific ID.
* Use the [Database.getDocument()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/Database.html#getDocument-java.lang.String-) method to get a document. If the document doesn’t exist in the database, the method will return `null`. You can use this behavior to check if a document with a given ID already exists in the database.

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
database.save(doc)
```

```Java
MutableDocument newTask = new MutableDocument();
newTask.setString("type", "task");
newTask.setString("owner", "todo");
newTask.setDate("createdAt", new Date());
try {
    database.save(newTask);
} catch (CouchbaseLiteException e) {
    Log.e(TAG, e.toString());
}
```

## [](#mutability)Mutability

By default, a document is immutable when it is read from the database. Use the [\`Document.toMutable()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/Document.html#toMutable--) to create an updatable instance of the document.

Example 7\. Make a mutable document

Changes to the document are persisted to the database when the `save` method is called.

* Kotlin
* Java

```Kotlin
database.getDocument("xyz")?.toMutable()?.let {
    it.setString("name", "apples")
    database.save(it)
}
```

```Java
Document document = database.getDocument("xyz");
MutableDocument mutableDocument = document.toMutable();
mutableDocument.setString("name", "apples");
try {
    database.save(mutableDocument);
} catch (CouchbaseLiteException e) {
    Log.e(TAG, e.toString());
}
```

> [!NOTE]
> Any user change to the value of reserved keys (`_id`, `_rev` or `_deleted`) will be detected when a document is saved and will result in an exception (Error Code 5 — `CorruptRevisionData`) — see also [Document Constraints](#lbl-doc-constraints).

## [](#batch-operations)Batch operations

If you’re making multiple changes to a database at once, it’s faster to group them together. The following example persists a few documents in batch.

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
        database.save(doc)
        Log.i(TAG, "saved user document: ${doc.getString("name")}")
    }
})
```

```Java
try {
    database.inBatch(() -> {
        for (int i = 0; i < 10; i++) {
            MutableDocument doc = new MutableDocument();
            doc.setValue("type", "user");
            doc.setValue("name", "user " + i);
            doc.setBoolean("admin", false);
            try {
                database.save(doc);
            } catch (CouchbaseLiteException e) {
                Log.e(TAG, e.toString());
            }
            Log.i(TAG, String.format("saved user document %s", doc.getString("name")));
        }
    });
} catch (CouchbaseLiteException e) {
    Log.e(TAG, e.toString());
}
```

At the **local** level this operation is still transactional: no other `Database` instances, including ones managed by the replicator can make changes during the execution of the block, and other instances will not see partial changes. But Couchbase Mobile is a distributed system, and due to the way replication works, there’s no guarantee that Sync Gateway or other devices will receive your changes all at once.

## [](#document-change-events)Document change events

You can register for document changes. The following example registers for changes to the document with ID `user.john` and prints the `verified_account` property when a change is detected.

Example 9\. Document change events

* Kotlin
* Java

```Kotlin
database.addDocumentChangeListener("user.john") { change ->
    database.getDocument(change.documentID)?.let {
        Toast.makeText(
            context,
            "Status: ${it.getString("verified_account")}",
            Toast.LENGTH_SHORT
        ).show()
    }
}
```

```Java
database.addDocumentChangeListener(
    "user.john",
    change -> {
        Document doc = database.getDocument(change.getDocumentID());
        if (doc != null) {
            Toast.makeText(context, "Status: " + doc.getString("verified_account"), Toast.LENGTH_SHORT).show();
        }
    });
```

### [](#using-kotlin-flows-and-livedata)Using Kotlin Flows and LiveData

Kotlin users can also take advantage of Flows and LiveData to monitor for changes.

The following methods show how to watch for document changes in a given database or for changes to a specific document.

* Database Changes
* Document Changes

```Kotlin
    val dbChanges: LiveData<MutableList<String>> = argDb.databaseChangeFlow()
        .map { it.documentIDs }
        .asLiveData()
```

```Kotlin
    val docChanges: LiveData<DocumentChange?> = argDb.documentChangeFlow("1001")
        .map {
            it.takeUnless {
                it.database.getDocument(it.documentID)?.getString("owner").equals(argDocOwner)
            }
        }
        .asLiveData()
```

## [](#document-expiration)Document Expiration

Document expiration allows users to set the expiration date for a document. When the document expires, it is purged from the database. The purge is not replicated to Sync Gateway.

Example 10\. Set document expiration

This example sets the TTL for a document to 5 minutes from the current time.

* Kotlin
* Java

```Kotlin
// Purge the document one day from now
database.setDocumentExpiration(
    "doc123",
    Date(Instant.now().plus(1, ChronoUnit.DAYS).toEpochMilli())
)

// Reset expiration
database.setDocumentExpiration("doc1", null)

// Query documents that will be expired in less than five minutes
val query = QueryBuilder
    .select(SelectResult.expression(Meta.id))
    .from(DataSource.database(database))
    .where(
        Meta.expiration.lessThan(
            Expression.longValue(Instant.now().plus(5, ChronoUnit.MINUTES).toEpochMilli())
        )
    )
```

```Java
// Purge the document one day from now
Instant ttl = Instant.now().plus(1, ChronoUnit.DAYS);
database.setDocumentExpiration("doc123", new Date(ttl.toEpochMilli()));

// Reset expiration
database.setDocumentExpiration("doc1", null);

// Query documents that will be expired in less than five minutes
Instant fiveMinutesFromNow = Instant.now().plus(5, ChronoUnit.MINUTES);
Query query = QueryBuilder
    .select(SelectResult.expression(Meta.id))
    .from(DataSource.database(database))
    .where(Meta.expiration.lessThan(Expression.doubleValue(fiveMinutesFromNow.toEpochMilli())));
```

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

* Initialize a 'MutableArrayObject' using data supplied as a JSON string. This is done using the `init(json)` constructor — see: [Example 4](#ex-array)
* Convert an `ArrayFragment` object to a JSON String
* Set data with a JSON string using `setJSON()`

Example 12\. Arrays as JSON strings

* Kotlin
* Java

```Kotlin
// initialize array from JSON string
val mArray = MutableArray(JSON)

// Create and save new document using the array
for (i in 0 until mArray.count()) {
    mArray.getDictionary(i)?.apply {
        Log.i(TAG, getString("name") ?: "unknown")
        db.save(MutableDocument(getString("id"), toMap()))
    }
}

// Get an array from the document as a JSON string
db.getDocument("1002")?.getArray("features")?.apply {
    // Print its elements
    for (feature in toList()) {
        Log.i(TAG, "$feature")
    }
    Log.i(TAG, toJSON())
}
```

```Java
// initialize array from JSON string
final MutableArray mArray = new MutableArray(JSON);

// Create and save new document using the array
for (int i = 0; i < mArray.count(); i++) {
  final Dictionary dict = mArray.getDictionary(i);
  Log.i(TAG, dict.getString("name"));
  db.save(new MutableDocument(dict.getString("id"), dict.toMap()));
}

// Get an array from the document as a JSON string
final Array features = db.getDocument("1002").getArray("features");
// Print its elements
for (Object feature: features.toList()) {
    Log.i(TAG, feature.toString());
}
Log.i(TAG, features.toJSON());
```

### [](#lbl-blob)Blobs

Convert a `Blob` to JSON using the `toJSON` method — see [Example 13](#ex-blob).

You can use `isBlob()` to check whether a given dictionary object is a blob or not — see [Example 13](#ex-blob).

Note that the blob object must first be saved to the database (generating the required metadata) before you can use the `toJSON` method.

Example 13\. Blobs as JSON strings

* Kotlin
* Java

```Kotlin
val thisBlob = db.getDocument("thisdoc-id")!!.toMap()
if (!Blob.isBlob(thisBlob)) {
  return
}
val blobType = thisBlob["content_type"].toString()
val blobLength = thisBlob["length"] as Number?
```

```Java
final Map<String, ?> thisBlob = db.getDocument("thisdoc-id").toMap();
if (!Blob.isBlob(thisBlob)) { return; }

final String blobType = thisBlob.get("content_type").toString();
final Number blobLength = (Number) thisBlob.get("length");
```

See also: [Blobs](blob.md)

### [](#lbl-dictionary)Dictionaries

Convert a `DictionaryObject` to and from JSON using the `toJSON` and `toDictionary` methods — see [Example 14](#ex-dictionary).

Additionally you can:

* Initialize a 'MutableDictionaryObject' using data supplied as a JSON string. This is done using the `init(json)` constructor-- see: [Example 14](#ex-dictionary)
* Set data with a JSON string using `setJSON()`

Example 14\. Dictionaries as JSON strings

* Kotlin
* Java

```Kotlin
val mDict = MutableDictionary(JSON)
Log.i(TAG, "$mDict")
Log.i(TAG, "Details for: ${mDict.getString("name")}")
for (key in mDict.keys) {
  Log.i(TAG, key + " => " + mDict.getValue(key))
}
```

```Java
final MutableDictionary mDict = new MutableDictionary(JSON);
Log.i(TAG, mDict.toString());

Log.i(TAG, "Details for: " + mDict.getString("name"));
for (String key: mDict.getKeys()) {
  Log.i(TAG, key + " => " + mDict.getValue(key));
}
```

### [](#lbl-document)Documents

Convert a `Document` to and from JSON strings using the `toJSON()` and `setJSON()` methods — see [Example 15](#ex-document).

Additionally you can:

* Initialize a 'MutableDocument' using data supplied as a JSON string. This is done using the `init(json)` or `init(id: json:)` constructor — see: [Example 15](#ex-document)
* Set data with a JSON string using `setJSON()`

Example 15\. Documents as JSON strings

* Kotlin
* Java

```Kotlin
QueryBuilder
.select(SelectResult.expression(Meta.id).as("metaId"))
.from(DataSource.database(srcDb))
.execute()
.forEach {
  it.getString("metaId")?.let { thisId ->
    // Get a document as a JSON string
    srcDb.getDocument(thisId)?.toJSON()?.let { json ->
      Log.i(TAG, "JSON String = $json")
      
      // Initialize a MutableDocument using the JSON string and save to a separate database
      val hotelFromJSON = MutableDocument(thisId, json)
      dstDb.save(hotelFromJSON)
      
      // Retrieve the document created from JSON and print values
      dstDb.getDocument(thisId)?.toMap()?.forEach { e ->
        Log.i(TAG, "$e.key => $e.value")
      }
    }
  }
}
```

```Java
final Query listQuery = QueryBuilder
.select(SelectResult.expression(Meta.id).as("metaId"))
.from(DataSource.database(srcDb));

for (Result row: listQuery.execute()) {
  final String thisId = row.getString("metaId");

// Get a document as a JSON string
  final String json = srcDb.getDocument(thisId).toJSON();
  Log.i(TAG, "JSON String = " + json);

  // Initialize a MutableDocument using the JSON string and save to a separate database
  final MutableDocument hotelFromJSON = new MutableDocument(thisId, json);
  dstDb.save(hotelFromJSON);

  // Retrieve the document created from JSON and print values
  for (Map.Entry entry: dstDb.getDocument(thisId).toMap().entrySet()) {
    Log.i(TAG, entry.getKey() + " => " + entry.getValue());
  }
}
```

### [](#lbl-result)Query Results as JSON

Convert a `Query Result` to JSON using its `toJSON()` accessor method.

Example 16\. Using JSON Results

Use [Result.toJSON()](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-android/com/couchbase/lite/Result.html#toJSON--) to transform your result string into a JSON string, which can easily be serialized or used as required in your application. See <\> for a working example. 

* Kotlin
* Java

```Kotlin
// Uses Jackson JSON processor
val mapper = ObjectMapper()
val hotels: ArrayList<Hotel> = ArrayList()

for (result in listQuery.execute()) {

    // Get result as JSON string
    val json = result.toJSON()

    // Get Hashmap from JSON string
    val dictFromJSONstring = mapper.readValue(json, HashMap::class.java)

    // Use created hashmap
    val hotelId = dictFromJSONstring["id"].toString() //
    val hotelType = dictFromJSONstring["type"].toString()
    val hotelname = dictFromJSONstring["name"].toString()


    // Get custom object from JSON string
    val thisHotel = mapper.readValue(json, Hotel::class.java)
    hotels.add(thisHotel)
}
```

```Java
// Uses Jackson JSON processor

ArrayList<Hotel> hotels = new ArrayList<Hotel>();
HashMap<String, Object> dictFromJSONstring;
for (Result result : listQuery.execute()) {

  // Get result as JSON string
  String thisJsonString = result.toJSON();

  // Get Java  Hashmap from JSON string
  HashMap<String, Object> dictFromJSONstring =
          mapper.readValue(thisJsonString, HashMap.class);


  // Use created hashmap
  String hotelId = dictFromJSONstring.get("id").toString();
  String hotelType = dictFromJSONstring.get("type").toString();
  String hotelname = dictFromJSONstring.get("name").toString();


  // Get custom object from JSON string
  Hotel thisHotel =
          mapper.readValue(thisJsonString, Hotel.class);
  hotels.add(thisHotel);
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

###### [](#)

How to . . .

* [Prerequisites](gs-prereqs.md)
* [Install](gs-install.md)
* [Build and Run](gs-build.md)

###### [](#-2)

Learn more . . .

* [Databases](database.md)
* [Documents](document.md)
* [Blobs](blob.md)
* [Remote Sync Gateway](replication.md)
* [Handling Data Conflicts](conflict.md)

###### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

---

[1](#%5Ffootnoteref%5F1). Any change to this reserved key will be detected when it is saved and will result in a Couchbase exception (Error Code 5 — \`CorruptRevisionData\`)