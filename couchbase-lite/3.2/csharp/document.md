---
title: Documents
description: Couchbase Lite concepts -- Data model -- Documents
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.2/modules/csharp/pages/document.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/couchbase-lite/3.2/csharp/document.html)

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

Couchbase Lite also provides for the direct handling of JSON data implemented in most cases by the provision of a `ToJSON()` method on appropriate API classes (for example, on MutableDocument, Dictionary, Blob and Array) — see [Working with JSON Data](#lbl-json-data).

## [](#constructing-a-document)Constructing a Document

An individual document often represents a single instance of an object in application code.

You can consider a document as the equivalent of a 'row' in a relational table, with each of the document’s attributes being equivalent to a 'column'.

Documents can contain nested structures. This allows developers to express many-to-many relationships without requiring a reference or join table, and is naturally expressive of hierarchical data.

Most apps will work with one or more documents, persisting them to a local database and optionally syncing them, either centrally or to the cloud.

In this section we provide an example of how you might create a `hotel` document, which provides basic contact details and price data.

Data Model

```C#
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

```C#
// Get the database (and create it if it doesn’t exist).
using var database = new Database("hoteldb");
var collection = database.GetDefaultCollection();
```

See [Databases](database.md) for more information

### [](#create-a-document)Create a Document

Now create a new document to hold your application’s data.

Use the mutable form, so that you can add data to the document.

```C#
// Create your new document
using var mutableDoc = new MutableDocument("hoteldoc");
```

For more on using **Documents**, see [Document Initializers](#document-initializers) and [Mutability](#mutability).

### [](#create-a-dictionary)Create a Dictionary

Now create a mutable dictionary (`address`).

Each element of the dictionary value will be directly accessible via its own key.

```C#
// Create and populate mutable dictionary
var address = new MutableDictionaryObject();
address.SetString("street", "1 Main st.");
address.SetString("city", "San Francisco");
address.SetString("state", "CA");
address.SetString("country", "USA");
address.SetString("code", "90210");
```

Learn more about [Using Dictionaries](#using-dictionaries).

### [](#create-an-array)Create an Array

Since the hotel may have multiple contact numbers, provide a field (`phones`) as a mutable array.

```C#
// Create and populate mutable array
var phones = new MutableArrayObject();
phones.AddString("650-000-0000");
phones.AddString("650-000-0001");
```

Learn more about [Using Arrays](#using-arrays)

### [](#populate-a-document)Populate a Document

Now add your data to the mutable document created earlier. Each data item is stored as a key-value pair.

```C#
// Initialize and populate the document

// Add document type and hotel name as string
mutableDoc.SetString("type", "hotel");
mutableDoc.SetString("name", "Hotel Java Mo");

// Add average room rate (float)
mutableDoc.SetFloat("room_rate", 121.75f);

// Add address (dictionary)
mutableDoc.SetDictionary("address", address);

// Add phone numbers(array)
mutableDoc.SetArray("phones", phones);
```

> [!NOTE]
> Couchbase recommend using a `type` attribute to define each logical document type.

### [](#save-a-document)Save a Document

Now persist the populated document to your Couchbase Lite database. This will auto-generate the document id.

```C#
collection.Save(mutableDoc);
```

### [](#close-the-database)Close the Database

With your document saved, you can now close our Couchbase Lite database.

```C#
database.Close();
```

## [](#working-with-data)Working with Data

### [](#checking-a-documents-properties)Checking a Document’s Properties

To check whether a given property exists in the document, use the [Document.Contains(String key)](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-net/api/Couchbase.Lite.Document.html#Couchbase%5FLite%5FDocument%5FContains%5FSystem%5FString%5F) method.

If you try to access a property which doesn’t exist in the document, the call will return the default value for that getter method (0 for [Document.GetInt()](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-net/api/Couchbase.Lite.Document.html#Couchbase%5FLite%5FDocument%5FGetInt%5FSystem%5FString%5F) 0.0 for [Document.GetFloat()](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-net/api/Couchbase.Lite.Document.html#Couchbase%5FLite%5FDocument%5FGetFloat%5FSystem%5FString%5F) etc.).

### [](#date-accessors)Date accessors

Couchbase Lite offers _Date_ accessors as a convenience. Dates are a common data type, but JSON doesn’t natively support them, so the convention is to store them as strings in ISO-8601 format.

Example 1\. Date Getter

This example sets the date on the `createdAt` property and reads it back using the [Document.GetDate()](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-net/api/Couchbase.Lite.Document.html#Couchbase%5FLite%5FDocument%5FGetDate%5FSystem%5FString%5F) accessor method.

```C#
mutableDoc.SetValue("createdAt", DateTimeOffset.UtcNow);
var date = mutableDoc.GetDate("createdAt");
```

### [](#using-dictionaries)Using Dictionaries

API References

* [DictionaryObject](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-net/api/Couchbase.Lite.DictionaryObject.html)
* [MutableDictionaryObject](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-net/api/Couchbase.Lite.MutableDictionaryObject.html)

Example 2\. Read Only

```C#
var doc = collection.GetDocument("doc1");

// Getting a dictionary from the document's properties
var dict = doc.GetDictionary("address");

// Access a value with a key from the dictionary
var street = dict.GetString("street");

// Iterate dictionary
foreach (var key in dict.Keys) {
    Console.WriteLine($"Key {key} = {dict.GetValue(key)}");
}

// Create a mutable copy
var mutableDict = dict.ToMutable();
```

Example 3\. Mutable

```C#
// Create a new mutable dictionary and populate some keys/values
var mutableDict = new MutableDictionaryObject();
mutableDict.SetString("street", "1 Main st.");
mutableDict.SetString("city", "San Francisco");

// Add the dictionary to a document's properties and save the document
using var mutableDoc = new MutableDocument("doc1");
mutableDoc.SetDictionary("address", mutableDict);
collection.Save(mutableDoc);
```

### [](#using-arrays)Using Arrays

API References

* [ArrayObject](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-net/api/Couchbase.Lite.ArrayObject.html)
* [MutableArrayObject](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-net/api/Couchbase.Lite.MutableArrayObject.html)

Example 4\. Read Only

```C#
var document = collection.GetDocument("doc1");

// Getting a phones array from the document's properties
var array = document.GetArray("phones");

// Get element count
var count = array.Count();

// Access an array element by index
if (count >= 0) { var phone = array[1]; }

// Iterate dictionary
for (int i = 0; i < count; i++) {
    Console.WriteLine($"Item {i.ToString()} = {array[i]}");
}

// Create a mutable copy
var mutableArray = array.ToMutable();
```

Example 5\. Mutable

```C#
// Create a new mutable array and populate data into the array
var mutableArray = new MutableArrayObject();
mutableArray.AddString("650-000-0000");
mutableArray.AddString("650-000-0001");

// Set the array to document's properties and save the document
using var mutableDoc = new MutableDocument("doc1");
mutableDoc.SetArray("phones", mutableArray);
collection.Save(mutableDoc);
```

### [](#using-blobs)Using Blobs

For more on working with blobs, see [Blobs](blob.md)

## [](#document-initializers)Document Initializers

You can use the following methods/initializers:

* Use the [MutableDocument()](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-net/api/Couchbase.Lite.MutableDocument.html#Couchbase%5FLite%5FMutableDocument%5F%5Fctor) initializer to create a new document where the document ID is randomly generated by the database.
* Use the [MutableDocument(String id)](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-net/api/Couchbase.Lite.MutableDocument.html#Couchbase%5FLite%5FMutableDocument%5FItem%5FSystem%5FString%5F) initializer to create a new document with a specific ID.
* Use the [Collection.GetDocument()](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-net/api/Couchbase.Lite.Collection.html#Couchbase%5FLite%5FCollection%5FGetDocument%5FSystem%5FString%5F) method to get a document. If the document doesn’t exist in the collection, the method will return `null`. You can use this behavior to check if a document with a given ID already exists in the collection.

Example 6\. Persist a document

The following code example creates a document and persists it to the database.

```C#
using var mutableDoc = new MutableDocument("xyz");
mutableDoc.SetString("type", "task")
    .SetString("owner", "todo")
    .SetDate("createdAt", DateTimeOffset.UtcNow);

collection.Save(mutableDoc);
```

## [](#mutability)Mutability

By default, a document is immutable when it is read from the database. Use the [Document.ToMutable()](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-net/api/Couchbase.Lite.Document.html#Couchbase%5FLite%5FDocument%5FToMutable) to create an updatable instance of the document.

Example 7\. Make a mutable document

Changes to the document are persisted to the database when the `save` method is called.

```C#
using var doc = collection.GetDocument("xyz");
using var mutableDoc = doc.ToMutable();
mutableDoc.SetString("name", "apples");
collection.Save(mutableDoc);
```

> [!NOTE]
> Any user change to the value of reserved keys (`_id`, `_rev` or `_deleted`) will be detected when a document is saved and will result in an exception (Error Code 5 — `CorruptRevisionData`) — see also [Document Constraints](#lbl-doc-constraints).

## [](#batch-operations)Batch operations

If you’re making multiple changes to a database at once, it’s faster to group them together. The following example persists a few documents in batch.

Example 8\. Batch operations

```C#
database.InBatch(() =>
{
    for (var i = 0; i < 10; i++) {
        using var mutableDoc = new MutableDocument();
        mutableDoc.SetString("type", "user");
        mutableDoc.SetString("name", $"user {i}");
        mutableDoc.SetBoolean("admin", false);
        collection.Save(mutableDoc);
        Console.WriteLine($"Saved user document {mutableDoc.GetString("name")}");
    }
});
```

At the **local** level this operation is still transactional: no other `Database` instances, including ones managed by the replicator can make changes during the execution of the block, and other instances will not see partial changes. But Couchbase Mobile is a distributed system, and due to the way replication works, there’s no guarantee that Sync Gateway or other devices will receive your changes all at once.

## [](#document-change-events)Document change events

You can register for document changes. The following example registers for changes to the document with ID `user.john` and prints the `verified_account` property when a change is detected.

Example 9\. Document change events

```C#
collection.AddDocumentChangeListener("user.john", (sender, args) =>
{
    using var doc = collection.GetDocument(args.DocumentID);
    Console.WriteLine($"Status :: {doc.GetString("verified_account")}");
});
```

## [](#document-expiration)Document Expiration

Document expiration allows users to set the expiration date for a document. When the document expires, it is purged from the database. The purge is not replicated to Sync Gateway.

Example 10\. Set document expiration

This example sets the TTL for a document to 1 day from the current time.

```C#
// Purge the document one day from now
var ttl = DateTimeOffset.UtcNow.AddDays(1);
collection.SetDocumentExpiration("doc123", ttl);

// Reset expiration
collection.SetDocumentExpiration("doc1", null);

// Query documents that will be expired in less than five minutes
var fiveMinutesFromNow = DateTimeOffset.UtcNow.AddMinutes(5).ToUnixTimeMilliseconds();
using var query = QueryBuilder
    .Select(SelectResult.Expression(Meta.ID))
    .From(DataSource.Collection(collection))
    .Where(Meta.Expiration.LessThan(Expression.Double(fiveMinutesFromNow)));
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

The `ToJSON()` typed-accessor means you can easily work with JSON data, native and Couchbase Lite objects.

### [](#lbl-array)Arrays

Convert an `ArrayObject` to and from JSON using the `ToJSON()` and `toArray` methods — see [Example 4](#ex-array).

Additionally you can:

* Initialize a 'MutableArrayObject' using data supplied as a JSON string. This is done using the `init(json)` constructor — see: [Example 4](#ex-array)
* Convert an `ArrayFragment` object to a JSON String
* Set data with a JSON string using `setJSON()`

Example 12\. Arrays as JSON strings

```C#
// JSON String -- an Array (3 elements. including embedded arrays)
var jsonString = "[{'id':'1000','type':'hotel','name':'Hotel Ted','city':'Paris','country':'France','description':'Undefined description for Hotel Ted'},{'id':'1001','type':'hotel','name':'Hotel Fred','city':'London','country':'England','description':'Undefined description for Hotel Fred'},                        {'id':'1002','type':'hotel','name':'Hotel Ned','city':'Balmain','country':'Australia','description':'Undefined description for Hotel Ned','features':['Cable TV','Toaster','Microwave']}]".Replace("'", "\"");

// Get JSON Array from JSON String
var jsonArray = JArray.Parse(jsonString);

// Create mutable array using JSON String Array
var mutableArray = new MutableArrayObject();
mutableArray.SetJSON(jsonString);

// Create a new document for each array element
for (int i = 0; i < mutableArray.Count; i++) {
    var dict = mutableArray.GetDictionary(i);
    var docid = mutableArray[i].Dictionary.GetString("id");
    var mutableDoc = new MutableDocument(docid, dict.ToDictionary());
    collection.Save(mutableDoc);
}

// Get one of the created docs and iterate through one of the embedded arrays
var extendedDoc = collection.GetDocument("1002");
var features = extendedDoc.GetArray("features");

// Print its elements
foreach (string feature in features) {
    Console.Write($"{feature} ");

    //process array item as required
}
var featuresJSON = extendedDoc.GetArray("features").ToJSON();
```

### [](#lbl-blob)Blobs

Convert a `Blob` to JSON using the `toJSON` method — see [Example 13](#ex-blob).

You can use `isBlob()` to check whether a given dictionary object is a blob or not — see [Example 13](#ex-blob).

Note that the blob object must first be saved to the database (generating the required metadata) before you can use the `toJSON` method.

Example 13\. Blobs as JSON strings

```C#
// Initialize base document for blob from a JSON string
var docId = "1002";
var jsonString = "{'ref':'hotel_1002','type':'hotel','name':'Hotel Ned'," +
    "'city':'Balmain','country':'Australia'," +
    "'description':'Undefined description for Hotel Ned'," +
    "'features':['Cable TV','Toaster','Microwave']}".Replace("'", "\"");
var mutableDoc = new MutableDocument(docId, jsonString);

// Get the content (an image), create blob and add to doc)
var defaultDirectory =
    Path.Combine(Service.GetInstance<IDefaultDirectoryResolver>()
                .DefaultDirectory(),
                    userName);
var imagePath = Path.Combine(defaultDirectory, "avatarimage.jpg");
var imageUri = new Uri(imagePath.ToString());
var imageBlob = new Blob("image/jpg", imageUri);
mutableDoc.SetBlob("avatar", imageBlob);

// This example generates a 'blob not saved' exception
try { 
    Console.WriteLine("myBlob (unsaved) as JSON = {0}", imageBlob.ToJSON()); 
} catch (Exception e) { 
    Console.WriteLine("Exception = {0}", e.Message); 
}

collection.Save(mutableDoc);

// Alternatively -- depending on use case
database.SaveBlob(new Blob("image/jpg", imageUri));

// Retrieve saved doc, get blob as JSON andheck its still a 'blob'
var sameDoc = collection.GetDocument(docId);
var reconstitutedBlob = new MutableDictionaryObject().
    SetDictionary("blobCOPY", new MutableDictionaryObject(sameDoc.GetBlob("avatar").ToJSON()));

if (Blob.IsBlob(
        reconstitutedBlob.GetDictionary("blobCOPY").ToDictionary())) {
    //... process accordingly
    Console.WriteLine("Its a Blob!!");
}
```

See also: [Blobs](blob.md)

### [](#lbl-dictionary)Dictionaries

Convert a `DictionaryObject` to and from JSON using the `toJSON` and `toDictionary` methods — see [Example 14](#ex-dictionary).

Additionally you can:

* Initialize a 'MutableDictionaryObject' using data supplied as a JSON string. This is done using the `init(json)` constructor-- see: [Example 14](#ex-dictionary)
* Set data with a JSON string using `setJSON()`

Example 14\. Dictionaries as JSON strings

```C#
// Get dictionary from JSONstring
var jsonString = "{'id':'1002','type':'hotel','name':'Hotel Ned','city':'Balmain','country':'Australia','description':'Undefined description for Hotel Ned','features':['Cable TV','Toaster','Microwave']}".Replace("'", "\"");
var mutableDict = new MutableDictionaryObject(json: jsonString);

// use dictionary to get name value
var name = mutableDict.GetString("name");

// Iterate through keys
foreach (string key in mutableDict.Keys) {
    Console.WriteLine("Data -- {0} = {1}", key, mutableDict.GetValue(key).ToString());

}
```

### [](#lbl-document)Documents

Convert a `Document` to and from JSON strings using the `ToJSON()` and `SetJSON()` methods — see [Example 15](#ex-document).

Additionally you can:

* Initialize a 'MutableDocument' using data supplied as a JSON string. This is done using the `init(json)` or `init(id: json:)` constructor — see: [Example 15](#ex-document)
* Set data with a JSON string using `setJSON()`

Example 15\. Documents as JSON strings

```C#
// Get a document
var doc = collection.GetDocument("hotel_10025");

// Get document data as JSON String
var docJSONString = doc?.ToJSON();

// Get Json Object from the Json String
JObject jsonObject = JObject.Parse(docJSONString);

// Get Native Object (anhotel) from JSON String
List<Hotel> hotels = new List<Hotel>();

var hotel = JsonConvert.DeserializeObject<Hotel>(docJSONString);
hotels.Add(hotel);

// Update the retrieved native object
hotel.Name = "A Copy of " + hotel.Name;
hotel.Id = "2001";

// Convert the updated object back to a JSON string
var newJsonString = JsonConvert.SerializeObject(hotel);

// Update new document with JSOn String
MutableDocument newhotel = doc.ToMutable();
newhotel.SetJSON(newJsonString);


foreach (string key in newhotel.ToDictionary().Keys) {
    Console.WriteLine("Data -- {0} = {1}",
        key, newhotel.GetValue(key));
}

collection.Save(newhotel);
var retrievedDoc = collection.GetDocument("2001").ToJSON();
Console.Write(retrievedDoc);
```

### [](#lbl-result)Query Results as JSON

Convert a `Query Result` to JSON using its {to-JSON} accessor method.

Example 16\. Using JSON Results

Use [Result.ToJson()](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-net/api/Couchbase.Lite.Query.Result.html#Couchbase%5FLite%5FQuery%5FResult%5FToJson) to transform your result string into a JSON string, which can easily be serialized or used as required in your application. See [Example 16](#ex-json) for a working example.

```C#
foreach (var result in query.Execute()) {

    // get the result into a JSON String
    var docJSONString = result.ToJSON();

    // Get a native dictionary object using the JSON string
    var dictFromJSONstring =
          JsonConvert.
            DeserializeObject<Dictionary<string, object>>
              (docJSONString);

    // use the created dictionary
    if (dictFromJSONstring != null) {
        var docID = dictFromJSONstring["id"].ToString();
        var docName = dictFromJSONstring["name"].ToString();
        var docCity = dictFromJSONstring["city"].ToString();
        var docType = dictFromJSONstring["type"].ToString();
    }

    //Get a custom object using the JSON string
    Hotel hotel =
        JsonConvert.DeserializeObject<Hotel>(docJSONString);

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

* [Prerequisites](#csharp:gs-prereqs.adoc)
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