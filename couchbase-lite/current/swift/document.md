---
title: Documents
description: Couchbase Lite concepts -- Data model -- Documents
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.1/modules/swift/pages/document.adoc
  xref: xref:couchbase-lite:swift:document.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/current/swift/document.html)

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

```swift
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

```swift
// Get the database (and create it if it doesn’t exist).
let database = try Database(name: "hoteldb")
let collection = try database.createCollection(name: "hotel")
```

See [Databases](database.md) for more information

### [](#create-a-document)Create a Document

Now create a new document to hold your application's data.

Use the mutable form, so that you can add data to the document.

```swift
// Create your new document
let mutableDoc = MutableDocument(id: "doc1")
```

For more on using **Documents**, see [Document Initializers](#document-initializers) and [Mutability](#mutability).

### [](#create-a-dictionary)Create a Dictionary

Now create a mutable dictionary (`address`).

Each element of the dictionary value will be directly accessible via its own key.

```swift
// Create and populate mutable dictionary
// Create a new mutable dictionary and populate some keys/values
let address = MutableDictionaryObject()
address.setString("1 Main st.", forKey: "street")
address.setString("San Francisco", forKey: "city")
address.setString("CA", forKey: "state")
address.setString("USA", forKey: "country")
address.setString("90210", forKey: "code")
```

Learn more about [Using Dictionaries](#using-dictionaries).

### [](#create-an-array)Create an Array

Since the hotel may have multiple contact numbers, provide a field (`phones`) as a mutable array.

```swift
// Create and populate mutable array
let phones = MutableArrayObject()
phones.addString("650-000-0000")
phones.addString("650-000-0001")
```

Learn more about [Using Arrays](#using-arrays)

### [](#populate-a-document)Populate a Document

Now add your data to the mutable document created earlier. Each data item is stored as a key-value pair.

```swift
// Initialize and populate the document
// Add document type and hotel name as string
mutableDoc.setString("hotel", forKey:"type")
mutableDoc.setString("Hotel Java Mo", forKey:"name")

// Add average room rate (float)
mutableDoc.setFloat(121.75, forKey:"room_rate")

// Add address (dictionary)
mutableDoc.setDictionary(address, forKey: "address")

// Add phone numbers(array)
mutableDoc.setArray(phones, forKey:"phones")
```

> [!NOTE]
> Couchbase recommend using a `type` attribute to define each logical document type.

### [](#save-a-document)Save a Document

Now persist the populated document to your Couchbase Lite database. This will auto-generate the document id.

```swift
try! collection.save(document:mutableDoc)
```

### [](#close-the-database)Close the Database

With your document saved, you can now close our Couchbase Lite database.

```swift
do {
    try database.close()
} catch {
    print(error)
}
```

## [](#working-with-data)Working with Data

### [](#checking-a-documents-properties)Checking a Document's Properties

To check whether a given property exists in the document, use the [Document.Contains(key:)](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-swift/Classes/Document.html#/s:18CouchbaseLiteSwift8DocumentC8contains3keySbSS%5FtF) method.

If you try to access a property which doesn't exist in the document, the call will return the default value for that getter method (0 for [Document.int()](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-swift/Classes/Document.html#/s:18CouchbaseLiteSwift8DocumentC3int6forKeySiSS%5FtF) 0.0 for [Document.float()](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-swift/Classes/Document.html#/s:18CouchbaseLiteSwift8DocumentC5float6forKeySfSS%5FtF) etc.).

### [](#date-accessors)Date accessors

Couchbase Lite offers _Date_ accessors as a convenience. Dates are a common data type, but JSON doesn't natively support them, so the convention is to store them as strings in ISO-8601 format.

> [!CAUTION]
> Date precision
> 
> The `setDate()` function rounds to millisecond precision due to the underlying native Swift call. If you require greater precision, then use the `Double` type to store the date in microseconds.

Example 1\. Date Getter

This example sets the date on the `createdAt` property and reads it back using the [Document.date()](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-swift/Classes/Document.html#/s:18CouchbaseLiteSwift8DocumentC4date6forKey10Foundation4DateVSgSS%5FtF) accessor method.

```swift
let mutableDoc = MutableDocument(id: "xyz")
mutableDoc.setValue(Date(), forKey: "createdAt")

guard let doc = try collection.document(id: "xyz") else { return }
let date = doc.date(forKey: "createdAt")
```

### [](#using-dictionaries)Using Dictionaries

API References

* [property accessors](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-swift/Classes/DictionaryObject.html)
* [MutableDictionaryObject](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-swift/Classes/MutableDictionaryObject.html)

Example 2\. Read Only

```swift
guard let doc = try self.collection.document(id:"doc1") else { return }

// Getting a dictionary from the document's properties
guard let dict = doc.dictionary(forKey: "address") else { return }

// Access a value with a key from the dictionary
guard let street = dict.string(forKey: "street") else { return }

// Iterate dictionary
for key in dict.keys {
    print("Key \(key) = \(dict.value(forKey:key) ?? "--")")
}

// Create a mutable copy
let mutableDict = dict.toMutable()
```

Example 3\. Mutable

```swift
// Create a new mutable dictionary and populate some keys/values
let mutableDict = MutableDictionaryObject()
mutableDict.setString("1 Main st.", forKey: "street")
mutableDict.setString("San Francisco", forKey: "city")

// Add the dictionary to a document's properties and save the document
let mutableDoc = MutableDocument(id: "doc1")
mutableDoc.setDictionary(mutableDict, forKey: "address")
try self.collection.save(document:mutableDoc)
```

### [](#using-arrays)Using Arrays

API References

* [ArrayObject](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-swift/Classes/ArrayObject.html)
* [MutableArrayObject](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-swift/Classes/MutableArrayObject.html)

Example 4\. Read Only

```swift
var phone = "--"
guard let doc = try self.collection.document(id:"doc1") else { return }

// Getting a phones array from the document's properties
guard let array = doc.array(forKey: "phones") else { return }

// Access an array element by index
if array.count >= 0, let val = array.string(at: 0) {
    phone = val
}

// Iterate dictionary
for (index, element) in array.enumerated() {
    print("Index \(index) = \(element)")
}

// Create a mutable copy
let mutableArray = array.toMutable()
```

Example 5\. Mutable

```swift
// Create a new mutable array and populate data into the array
let mutableArray = MutableArrayObject()
mutableArray.addString("650-000-0000")
mutableArray.addString("650-000-0001")

// Set the array to document's properties and save the document
let mutableDoc = MutableDocument(id: "doc1")
mutableDoc.setArray(mutableArray, forKey:"phones")
try self.collection.save(document:mutableDoc)
```

### [](#using-blobs)Using Blobs

For more on working with blobs, see [Blobs](blob.md)

## [](#document-initializers)Document Initializers

You can use the following methods/initializers:

* Use the [MutableDocument()](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-swift/Classes/MutableDocument.html#/s:18CouchbaseLiteSwift15MutableDocumentCACycfc) initializer to create a new document where the document ID is randomly generated by the database.
* Use the [MutableDocument(String id)](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-swift/Classes/MutableDocument.html#/s:18CouchbaseLiteSwift15MutableDocumentC2idACSSSg%5Ftcfc) initializer to create a new document with a specific ID.
* Use the {url-api-method-collection-getdocument} method to get a document. If the document doesn't exist in the collection, the method will return `null`. You can use this behavior to check if a document with a given ID already exists in the collection.

Example 6\. Persist a document

The following code example creates a document and persists it to the database.

```swift
let doc = MutableDocument()
    .setString("task", forKey: "type")
    .setString("todo", forKey: "owner")
    .setDate(Date(), forKey: "createdAt")
try collection.save(document: doc)
```

## [](#mutability)Mutability

By default, a document is immutable when it is read from the database. Use the [Document.toMutable()](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-swift/Classes/Document.html#/s:18CouchbaseLiteSwift8DocumentC9toMutableAA0fD0CyF) to create an updatable instance of the document.

Example 7\. Make a mutable document

Changes to the document are persisted to the database when the `save` method is called.

```swift
guard let doc = try collection.document(id: "xyz") else { return }
let mutableDocument = doc.toMutable()
mutableDocument.setString("apples", forKey: "name")
try collection.save(document: mutableDocument)
```

> [!NOTE]
> Any user change to the value of reserved keys (`_id`, `_rev` or `_deleted`) will be detected when a document is saved and will result in an exception (Error Code 5 — `CorruptRevisionData`) — see also [Document Constraints](#lbl-doc-constraints).

## [](#document-conversion)Document Conversion

You can convert a `Document` to a plain dictionary type and/or to a JSON string. This can often be useful to pass the document contents as a plain object to another method.

Example 8\. Convert document

```swift
guard let doc = try collection.document(id: "xyz") else { return }
print(doc.toDictionary())
guard let doc = try collection.document(id: "xyz") else { return }
print(doc.toJSON())
```

## [](#batch-operations)Batch operations

If you're making multiple changes to a database at once, it's faster to group them together. The following example persists a few documents in batch.

Example 9\. Batch operations

```swift
do {
    try self.database.inBatch {
        for i in 0...10 {
            let doc = MutableDocument()
            doc.setValue("user", forKey: "type")
            doc.setValue("user \(i)", forKey: "name")
            doc.setBoolean(false, forKey: "admin")
            try self.collection.save(document: doc)
            print("saved user document \(doc.string(forKey: "name")!)")
        }
    }
} catch let error {
    print(error.localizedDescription)
}
```

At the **local** level this operation is still transactional: no other `Database` instances, including ones managed by the replicator can make changes during the execution of the block, and other instances will not see partial changes. But Couchbase Mobile is a distributed system, and due to the way replication works, there's no guarantee that Sync Gateway or other devices will receive your changes all at once.

## [](#document-change-events)Document change events

You can register for document changes. The following example registers for changes to the document with ID `user.john` and prints the `verified_account` property when a change is detected.

Example 10\. Document change events

```swift
weak var wCollection = collection
let token = collection.addDocumentChangeListener(id: "user.john") { (change) in
    if let doc = try? wCollection?.document(id: change.documentID) {
        print("Status :: \(doc?.string(forKey: "verified_account") ?? "--")")
    }
}
```

## [](#document-expiration)Document Expiration

Document expiration allows users to set the expiration date for a document. When the document expires, it is purged from the database. The purge is not replicated to Sync Gateway.

Example 11\. Set document expiration

This example sets the TTL for a document to 1 day from the current time.

```swift
// Purge the document one day from now
let ttl = Calendar.current.date(byAdding: .day, value: 1, to: Date())
try collection.setDocumentExpiration(id: "doc123", expiration: ttl)

// Reset expiration
try collection.setDocumentExpiration(id: "doc1", expiration: nil)

// Query documents that will be expired in less than five minutes
let fiveMinutesFromNow = Date(timeIntervalSinceNow: 60 * 5).timeIntervalSince1970
let query = QueryBuilder
    .select(SelectResult.expression(Meta.id))
    .from(DataSource.collection(self.collection))
    .where(
        Meta.expiration.lessThan(
            Expression.double(fiveMinutesFromNow)
        )
    )
```

You can set expiration for a whole Collection

## [](#lbl-doc-constraints)Document Constraints

Couchbase Lite APIs do not explicitly disallow the use of attributes with the underscore prefix at the top level of document. This is to facilitate the creation of documents for use either in _local only_ mode where documents are not synced, or when used exclusively in peer-to-peer sync.

> [!NOTE]
> "\_id", :"\_rev" and "\_sequence" are reserved keywords and must not be used as top-level attributes — see [Example 12](#res-keys).

Users are cautioned that any attempt to sync such documents to Sync Gateway will result in an error. To be future proof, you are advised to avoid creating such documents. Use of these attributes for user-level data may result in undefined system behavior.

For more guidance — see: [Sync Gateway - data modeling guidelines](../../../sync-gateway/current/data-modeling.md)

Example 12\. Reserved Keys List

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

Example 13\. Arrays as JSON strings

```swift
let doc = MutableDocument()
let json = "[\"1000\",\"1001\",\"1002\",\"1003\"]"

let initArray = try MutableArrayObject(json: json)

let setArray = MutableArrayObject()
try setArray.setJSON(json)
```

### [](#lbl-blob)Blobs

Convert a `Blob` to JSON using the `toJSON` method — see [Example 14](#ex-blob).

You can use `isBlob()` to check whether a given dictionary object is a blob or not.

Note that the blob object must first be saved to the database (generating the required metadata) before you can use the `toJSON` method.

Example 14\. Blobs as JSON strings

```swift
// Get a document
if let doc = try collection.document(id: "1000") {
    guard let blob = doc.blob(forKey: "avatar") else {
        return
    }
    let json = blob.toJSON()
    print(json)
    
    let maybeBlob = doc.toDictionary()
    print(Blob.isBlob(properties: maybeBlob))
}
```

See also: [Blobs](blob.md)

### [](#lbl-dictionary)Dictionaries

Convert a `DictionaryObject` to and from JSON using the `toJSON` and `toDictionary` methods — see [Example 15](#ex-dictionary).

Additionally you can:

* Initialize a `MutableDictionaryObject` using data supplied as a JSON string. This is done using the `init(json)` constructor
* Set data with a JSON string using `setJSON()`

Example 15\. Dictionaries as JSON strings

```swift
let json = """
{
    "id": "1002",
    "type": "hotel",
    "name": "Hotel Ned",
    "city": "Balmain",
    "country": "Australia",
    "description": "Undefined description for Hotel Ned"
}
"""
// Create dictionary from JSON
let initDictionary = try MutableDictionaryObject(json: json)

// Create a new dictionary using JSON
let setDictionary = MutableDictionaryObject()
try setDictionary.setJSON(json)

if let doc = try collection.document(id: "1002") {
    guard let dictionary = doc.dictionary(forKey: "dictionary") else {
        return
    }

    let json = dictionary.toJSON()
    print(json)
}
```

### [](#lbl-document)Documents

Convert a `Document` to and from JSON strings using the `toJSON()` and `setJSON()` methods — see [Example 16](#ex-document).

Additionally you can:

* Initialize a `MutableDocument` using data supplied as a JSON string. This is done using the `init(json)` or `init(id: json:)` constructor
* Set data with a JSON string using `setJSON()`

Example 16\. Documents as JSON strings

```swift
if let doc = try collection.document(id: "doc-id") {
    let json = doc.toJSON()
    print(json)
}
```

### [](#lbl-result)Query Results as JSON

Convert a `Query Result` to JSON using its {to-JSON} accessor method.

Example 17\. Using JSON Results

Use [result.toJSON()](https://docs.couchbase.com/mobile/4.1.0/couchbase-lite-swift/Classes/Result.html#/s:18CouchbaseLiteSwift6ResultC6toJSONSSyF) to transform your result string into a JSON string, which can easily be serialized or used as required in your application.

```swift
// In this example the Hotel class is defined using Codable
//
// class Hotel : Codable {
//   var id : String = "undefined"
//   var type : String = "hotel"
//   var name : String = "undefined"
//   var city : String = "undefined"
//   var country : String = "undefined"
//   var description : String? = ""
//   var text : String? = ""
//   ... other class content
// }

results = try query.execute()
for row in  results {

    // get the result into a JSON String
    let jsonString = row.toJSON()

    let thisJsonObj:Dictionary =
    try (JSONSerialization.jsonObject(
        with: jsonString.data(using: .utf8)!,
        options: .allowFragments)
         as? [String: Any])!

    // Use Json Object to populate Native object
    // Use Codable class to unpack JSON data to native object
    var this_hotel: Hotel = try JSONDecoder().decode(Hotel.self, from:jsonString.data(using: .utf8)!) (1)

    // ALTERNATIVELY unpack in steps
    this_hotel.id = thisJsonObj["id"] as! String
    this_hotel.name = thisJsonObj["name"] as? String
    this_hotel.type = thisJsonObj["type"] as? String
    this_hotel.city = thisJsonObj["city"] as? String
    hotels[this_hotel.id] = this_hotel
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