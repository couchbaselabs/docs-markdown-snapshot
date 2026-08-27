---
title: Documents
description: Couchbase Lite concepts -- Data model -- Documents
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.2/modules/c/pages/document.adoc
  xref: xref:3.2@couchbase-lite:c:document.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.2/c/document.html)

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

```c
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

```c
// Open or create DB if it doesn't exist
CBLError err{};
CBLDatabase* database = CBLDatabase_Open(FLSTR("mydb"), NULL, &err);

if(!database) {
    return;
}

// Get default collections
CBLCollection* collection = CBLDatabase_DefaultCollection(kDatabase, NULL);
```

See [Databases](database.md) for more information

### [](#create-a-document)Create a Document

Now create a new document to hold your application's data.

Use the mutable form, so that you can add data to the document.

```c
// Create your new document
// The lack of 'const' indicates this document is mutable
CBLDocument* mutableDoc = CBLDocument_Create();
FLMutableDict properties = CBLDocument_MutableProperties(mutableDoc);
```

For more on using **Documents**, see [Document Initializers](#document-initializers) and [Mutability](#mutability).

### [](#create-a-dictionary)Create a Dictionary

Now create a mutable dictionary (`address`).

Each element of the dictionary value will be directly accessible via its own key.

```c
// Create and populate mutable dictionary
FLMutableDict address = FLMutableDict_New();
FLMutableDict_SetString(address, FLSTR("street"), FLSTR("1 Main st."));
FLMutableDict_SetString(address, FLSTR("city"), FLSTR("San Francisco"));
FLMutableDict_SetString(address, FLSTR("state"), FLSTR("CA"));
FLMutableDict_SetString(address, FLSTR("country"), FLSTR("USA"));
FLMutableDict_SetString(address, FLSTR("code"), FLSTR("90210"));
```

Learn more about [Using Dictionaries](#using-dictionaries).

### [](#create-an-array)Create an Array

Since the hotel may have multiple contact numbers, provide a field (`phones`) as a mutable array.

```c
// Create and populate mutable array
FLMutableArray phones = FLMutableArray_New();
FLMutableArray_AppendString(phones, FLSTR("650-000-0000"));
FLMutableArray_AppendString(phones, FLSTR("650-000-0001"));
```

Learn more about [Using Arrays](#using-arrays)

### [](#populate-a-document)Populate a Document

Now add your data to the mutable document created earlier. Each data item is stored as a key-value pair.

```c
// Initialize and populate the document

// Add document type and hotel name as string
FLMutableDict_SetString(properties, FLSTR("type"), FLSTR("hotel"));
FLMutableDict_SetString(properties, FLSTR("hotel"), FLSTR(""));

// Add average room rate (float)
FLMutableDict_SetFloat(properties, FLSTR("room_rate"), 121.75f);

// Add address (dictionary)
FLMutableDict_SetDict(properties, FLSTR("address"), address);

// Add phone numbers(array)
FLMutableDict_SetArray(properties, FLSTR("phones"), phones);
```

> [!NOTE]
> Couchbase recommend using a `type` attribute to define each logical document type.

### [](#save-a-document)Save a Document

Now persist the populated document to your Couchbase Lite database. This will auto-generate the document id.

```c
CBLError err{};
CBLCollection_SaveDocument(collection, mutableDoc, &err);
```

### [](#close-the-database)Close the Database

With your document saved, you can now close our Couchbase Lite database.

```c
CBLError err{};
CBLDatabase_Close(database, &err);
```

### [](#release-resources)Release resources

Finally, release the resources.

```c
CBLDatabase_Release(database);
CBLDocument_Release(mutableDoc);
FLMutableDict_Release(address);
FLMutableArray_Release(phones);
```

## [](#working-with-data)Working with Data

### [](#using-dictionaries)Using Dictionaries

API References

* [Fleece Dictionaries](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html/group%5F%5Ff%5Fl%5Fdict.html)

Example 1\. Read Only

```c
CBLError err{};
const CBLDocument *doc = CBLCollection_GetDocument(collection, FLSTR("doc1"), &err);
FLDict properties = CBLDocument_Properties(doc);

// Getting a dictionary from the document's properties
FLValue dictValue = FLDict_Get(properties, FLSTR("address"));
FLDict dict = FLValue_AsDict(dictValue);

// Access a value with a key from the dictionary
FLValue streetVal = FLDict_Get(dict, FLSTR("street"));
FLString street = FLValue_AsString(streetVal);

// Iterate dictionary
FLDictIterator iter;
FLDictIterator_Begin(dict, &iter);
FLValue value;
while (NULL != (value = FLDictIterator_GetValue(&iter))) {
    FLString key = FLDictIterator_GetKeyString(&iter);
    FLString strValue = FLValue_AsString(value);
    printf("Key :: %.*s\n", (int)key.size, (const char *)key.buf);
    printf("Value :: %.*s\n", (int)strValue.size, (const char *)strValue.buf);
    // ...
    FLDictIterator_Next(&iter);
}

// Create a mutable copy.
// kFLDefaultCopy is shallow which means the nested dictionaries and arrays will be
// referenced but not copied. Use kFLDeepCopyImmutables for the deep copy.
FLMutableDict mutableDict = FLDict_MutableCopy(dict, kFLDefaultCopy);

// Release when finish using it
FLMutableDict_Release(mutableDict);
```

Example 2\. Mutable

```c
// Create a new mutable dictionary and populate some keys/values
FLMutableDict dict = FLMutableDict_New();
FLMutableDict_SetString(dict, FLSTR("street"), FLSTR("1 Main st."));
FLMutableDict_SetString(dict, FLSTR("city"), FLSTR("San Francisco"));

// Set the dictionary to document's properties and save the document
CBLDocument *doc = CBLDocument_Create();
FLMutableDict properties = CBLDocument_MutableProperties(doc);
FLMutableDict_SetDict(properties, FLSTR("address"), dict);
CBLError err{};
CBLCollection_SaveDocument(collection, doc, &err);
CBLDocument_Release(doc);

// Release when finish using it
FLMutableDict_Release(dict);
```

### [](#using-arrays)Using Arrays

API References

* [Fleece Arrays](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html/group%5F%5F%5Ff%5Fl%5Farray.html)

Example 3\. Read Only

```c
CBLError err{};
const CBLDocument *doc = CBLCollection_GetDocument(collection, FLSTR("doc1"), &err);
FLDict properties = CBLDocument_Properties(doc);

// Getting a phones array from the document's properties
FLValue arrayValue = FLDict_Get(properties, FLSTR("phones"));
FLArray array = FLValue_AsArray(arrayValue);

// Get element count
int count = FLArray_Count(array);
printf("Count :: %d\n", count);

// Access an array element by index
if (!FLArray_IsEmpty(array)) {
    FLValue phoneVal = FLArray_Get(array, 0);
    FLString phone = FLValue_AsString(phoneVal);
    printf("Value :: %.*s\n", (int)phone.size, (const char *)phone.buf);
}

// Iterate array
FLArrayIterator iter;
FLArrayIterator_Begin(array, &iter);
FLValue val;
while (NULL != (val = FLArrayIterator_GetValue(&iter)))
{
    FLString str = FLValue_AsString(val);
    printf("Value :: %.*s\n", (int)str.size, (const char *)str.buf);
    FLArrayIterator_Next(&iter);
}
```

Example 4\. Mutable

```c
// Create a new mutable array and populate data into the array
FLMutableArray phones = FLMutableArray_New();
FLMutableArray_AppendString(phones, FLSTR("650-000-0000"));
FLMutableArray_AppendString(phones, FLSTR("650-000-0001"));

// Set the array to document's properties and save the document
CBLDocument *doc = CBLDocument_Create();
FLMutableDict properties = CBLDocument_MutableProperties(doc);
FLMutableDict_SetArray(properties, FLSTR("phones"), phones);
CBLError err{};
CBLCollection_SaveDocument(collection, doc, &err);
CBLDocument_Release(doc);

// Release the created dictionary
FLMutableArray_Release(phones);
```

### [](#using-blobs)Using Blobs

For more on working with blobs, see [Blobs](blob.md)

## [](#document-initializers)Document Initializers

You can use the following methods/initializers:

* Use the [CBLDocument\_Create()](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html/group%5F%5Fdocuments.html#ga226f555fffb7543558048af20b18b737) initializer to create a new document where the document ID is randomly generated by the database.
* Use the [CBLDocument\_CreateWithID()](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html/group%5F%5Fdocuments.html#gaec41cf2eab4e3ac490f11007f665a35e) initializer to create a new document with a specific ID.
* Use the {url-api-method-collection-getdocument} method to get a document. If the document doesn't exist in the collection, the method will return `null`. You can use this behavior to check if a document with a given ID already exists in the collection.

Example 5\. Persist a document

The following code example creates a document and persists it to the database.

```c
CBLDocument* doc = CBLDocument_CreateWithID(FLSTR("xyz"));
FLMutableDict properties = CBLDocument_MutableProperties(doc);
FLMutableDict_SetString(properties, FLSTR("type"), FLSTR("task"));
FLMutableDict_SetString(properties, FLSTR("owner"), FLSTR("todo"));

// Storing time in millisecond, bluntly
FLMutableDict_SetUInt(properties, FLSTR("createdAt"), time(NULL) * 1000);

CBLError err{};
CBLCollection_SaveDocument(collection, doc, &err);
CBLDocument_Release(doc);
```

## [](#mutability)Mutability

Couchbase Lite for C's `CBLDocument*` objects can be either mutable or immutable. Reference an immutable document using a `const` pointer and a mutable document using a non-const pointer to prevent developers from accidentally calling a mutable-document function on an immutable document.

To make an immutable document mutable, use [CBLDocument\_MutableCopy()](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html/group%5F%5Fdocuments.html#ga0356b98d2f1798adc8f549510d3eef67).

```c
CBLDocument* CBLDocument_MutableCopy(const CBLDocument* doc _cbl_nonnull)
_cbl_warn_unused _cbl_returns_nonnull;
```

Example 6\. Make a mutable document

Changes to the document are persisted to the database when the `save` method is called.

```c
CBLError err{};
CBLDocument* mutableDoc = CBLCollection_GetMutableDocument(collection, FLSTR("xyz"), &err);
FLMutableDict properties = CBLDocument_MutableProperties(mutableDoc);
FLMutableDict_SetString(properties, FLSTR("name"), FLSTR("apples"));
CBLCollection_SaveDocument(collection, mutableDoc, &err);
CBLDocument_Release(mutableDoc);
```

> [!NOTE]
> Any user change to the value of reserved keys (`_id`, `_rev` or `_deleted`) will be detected when a document is saved and will result in an exception (Error Code 5 — `CorruptRevisionData`) — see also [Document Constraints](#lbl-doc-constraints).

## [](#batch-operations)Batch operations

If you're making multiple changes to a database at once, it's faster to group them together. The following example persists a few documents in batch.

Example 7\. Batch operations

```c
CBLError err{};
CBLDatabase_BeginTransaction(database, &err);
char buffer[7];
for(int i = 0; i < 10; i++) {
    CBLDocument* doc = CBLDocument_Create();
    FLMutableDict properties = CBLDocument_MutableProperties(doc);
    FLMutableDict_SetString(properties, FLSTR("type"), FLSTR("user"));
    sprintf(buffer, "user %d", i);
    FLMutableDict_SetString(properties, FLSTR("name"), FLStr(buffer));
    FLMutableDict_SetBool(properties, FLSTR("admin"), false);
    CBLCollection_SaveDocument(collection, doc, &err);
    CBLDocument_Release(doc);
    printf("Saved user document %s\n", buffer);
}

CBLDatabase_EndTransaction(database, true, &err);
```

At the **local** level this operation is still transactional: no other `Database` instances, including ones managed by the replicator can make changes during the execution of the block, and other instances will not see partial changes. But Couchbase Mobile is a distributed system, and due to the way replication works, there's no guarantee that Sync Gateway or other devices will receive your changes all at once.

## [](#document-change-events)Document change events

You can register for document changes. The following example registers for changes to the document with ID `user.john` and prints the `verified_account` property when a change is detected.

Example 8\. Document change events

```c
CBLListenerToken* token = CBLCollection_AddDocumentChangeListener(collection, FLSTR("user.john"),
    document_listener, NULL);
```

## [](#document-expiration)Document Expiration

Document expiration allows users to set the expiration date for a document. When the document expires, it is purged from the database. The purge is not replicated to Sync Gateway.

Example 9\. Set document expiration

This example sets the TTL for a document to 1 day from the current time.

```c
// Purge the document one day from now.
// Overly simplistic for example purposes.
// NOTE: API takes milliseconds
time_t ttl = time(NULL) + 24 * 60 * 60;
ttl *= 1000;

CBLError err{};
CBLCollection_SetDocumentExpiration(collection, FLSTR("doc123"), ttl, &err);

// Reset expiration
CBLCollection_SetDocumentExpiration(collection, FLSTR("doc1"), 0, &err);

// Query documents that will be expired in less than five minutes
time_t fiveMinutesFromNow = time(NULL) + 5 * 60;
fiveMinutesFromNow *= 1000;
FLMutableDict parameters = FLMutableDict_New();
FLMutableDict_SetInt(parameters, FLSTR("five_minutes"), fiveMinutesFromNow);

CBLQuery* query = CBLDatabase_CreateQuery(database, kCBLN1QLLanguage,
    FLSTR("SELECT meta().id FROM _ WHERE meta().expiration < $five_minutes"), NULL, &err);
CBLQuery_SetParameters(query, parameters);
FLMutableDict_Release(parameters);
```

You can set expiration for a whole Collection

## [](#lbl-doc-constraints)Document Constraints

Couchbase Lite APIs do not explicitly disallow the use of attributes with the underscore prefix at the top level of document. This is to facilitate the creation of documents for use either in _local only_ mode where documents are not synced, or when used exclusively in peer-to-peer sync.

> [!NOTE]
> "\_id", :"\_rev" and "\_sequence" are reserved keywords and must not be used as top-level attributes — see [Example 10](#res-keys).

Users are cautioned that any attempt to sync such documents to Sync Gateway will result in an error. To be future proof, you are advised to avoid creating such documents. Use of these attributes for user-level data may result in undefined system behavior.

For more guidance — see: [Sync Gateway - data modeling guidelines](../../../sync-gateway/current/data-modeling.md)

Example 10\. Reserved Keys List

* \_attachments
* \_deleted \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]
* \_id \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]
* \_removed
* \_rev \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]
* \_sequence

## [](#lbl-json-data)Working with JSON Data

In this section

[Arrays](#lbl-array)| [Dictionaries](#lbl-dictionary)| [Documents](#lbl-document)| [Query Results as JSON](#lbl-result)

The `toJSON()` typed-accessor means you can easily work with JSON data, native and Couchbase Lite objects.

### [](#lbl-array)Arrays

Convert an `ArrayObject` to and from JSON using the `toJSON()` and `toArray` methods — see [Example 3](#ex-array).

Additionally you can:

* Initialize a 'MutableArrayObject' using data supplied as a JSON string. This is done using the `init(json)` constructor — see: [Example 3](#ex-array)
* Convert an `ArrayFragment` object to a JSON String
* Set data with a JSON string using `setJSON()`

Example 11\. Arrays as JSON strings

```c
FLString json = FLSTR("[\"Hotel Ned\", \"Hotel Ted\"]");

// Create an array from the JSON string
FLError err;
FLSliceResult jsonData1 = FLData_ConvertJSON(json, &err);
FLArray hotels = FLValue_AsArray(FLValue_FromData(FLSliceResult_AsSlice(jsonData1), kFLTrusted));

// Iterate through the array
FLArrayIterator iter;
FLArrayIterator_Begin(hotels, &iter);
FLValue value;
while (NULL != (value = FLArrayIterator_GetValue(&iter))) {
    FLString hotel = FLValue_AsString(value);
    printf("Hotel :: %.*s\n", (int)hotel.size, (const char *)hotel.buf);
    FLArrayIterator_Next(&iter);
}

// Convert the array to JSON
FLSliceResult jsonData2 = FLValue_ToJSON((FLValue)hotels);
printf("Hotels in JSON :: %.*s\n", (int)jsonData2.size, (const char *)jsonData2.buf);

// Release JSON data after finish using it
FLSliceResult_Release(jsonData1);
FLSliceResult_Release(jsonData2);
```

### [](#lbl-dictionary)Dictionaries

Convert a `DictionaryObject` to and from JSON using the `toJSON` and `toDictionary` methods — see [Example 12](#ex-dictionary).

Additionally you can:

* Initialize a 'MutableDictionaryObject' using data supplied as a JSON string. This is done using the `init(json)` constructor-- see: [Example 12](#ex-dictionary)
* Set data with a JSON string using `setJSON()`

Example 12\. Dictionaries as JSON strings

```c
FLString json = FLSTR("{\"id\":\"1002\",\"type\":\"hotel\",\"name\":\"Hotel Ned\",\"city\":\"Balmain\",\"country\":\"Australia\"}");

// Create a dictionary from the JSON string
FLError err;
FLSliceResult jsonData1 = FLData_ConvertJSON(json, &err);
FLDict hotel = FLValue_AsDict(FLValue_FromData(FLSliceResult_AsSlice(jsonData1), kFLTrusted));

// Iterate through the dictionary
FLDictIterator iter;
FLDictIterator_Begin(hotel, &iter);
FLValue value;
while (NULL != (value = FLDictIterator_GetValue(&iter))) {
    FLString key = FLDictIterator_GetKeyString(&iter);
    FLString strValue = FLValue_AsString(value);
    printf("%.*s :: %.*s\n", (int)key.size, (const char*)key.buf, (int)strValue.size, (const char*)strValue.buf);
    FLDictIterator_Next(&iter);
}

// Convert the dictionary to JSON
FLSliceResult jsonData2 = FLValue_ToJSON((FLValue)hotel);
printf("Hotel in JSON :: %.*s\n", (int)jsonData2.size, (const char *)jsonData2.buf);

// Release JSON data after finish using it
FLSliceResult_Release(jsonData1);
FLSliceResult_Release(jsonData2);
```

### [](#lbl-document)Documents

Convert a `Document` to and from JSON strings using the `toJSON()` and `setJSON()` methods — see [Example 13](#ex-document).

Additionally you can:

* Initialize a 'MutableDocument' using data supplied as a JSON string. This is done using the `init(json)` or `init(id: json:)` constructor — see: [Example 13](#ex-document)
* Set data with a JSON string using `setJSON()`

Example 13\. Documents as JSON strings

```c
FLString json = FLSTR("{\"id\":\"1002\",\"type\":\"hotel\",\"name\":\"Hotel Ned\",\"city\":\"Balmain\",\"country\":\"Australia\"}");

// Create a document and set the JSON data to the document
CBLError err{};
CBLDocument* newDoc = CBLDocument_CreateWithID(FLSTR("hotel_1002"));
CBLDocument_SetJSON(newDoc, json, &err);

// Save the document to the database
CBLCollection_SaveDocument(collection, newDoc, &err);

// Release created doc after using it
CBLDocument_Release(newDoc);

// Get the document from the database
const CBLDocument* doc = CBLCollection_GetDocument(collection, FLSTR("hotel_1002"), &err);

// Get document body as JSON
FLSliceResult docJson = CBLDocument_CreateJSON(doc);
printf("Document in JSON :: %.*s\n", (int)docJson.size, (const char *)docJson.buf);

// Release JSON data after using it
FLSliceResult_Release(docJson);

// Release doc read from the database after using it
CBLDocument_Release(doc);
```

### [](#lbl-result)Query Results as JSON

Convert a `Query Result` to JSON using its {to-JSON} accessor method.

Example 14\. Using JSON Results

Use [FLValue\_ToJSON()](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-c/C/html/group%5F%5Fjson.html#ga3450acc0690101545d75986b91e4080) to transform your result string into a JSON string, which can easily be serialized or used as required in your application. See [Example 14](#ex-json) for a working example.

```c
CBLResultSet* results = CBLQuery_Execute(query, &err);
while(CBLResultSet_Next(results)) {
    FLDict result = CBLResultSet_ResultDict(results);
    FLStringResult json = FLValue_ToJSON((FLValue)result);
    printf("JSON Result :: %.*s\n", (int)json.size, (const char *)json.buf);
    FLSliceResult_Release(json);
}
CBLResultSet_Release(results);
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

* [Prerequisites](#c:gs-prereqs.adoc)
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

## [](#related-content-2)Related Content

### [](#-4)

How to . . .

* [Prerequisites](#c:gs-prereqs.adoc)
* [Install](gs-install.md)
* [Build and Run](gs-build.md)

.

### [](#-5)

Learn more . . .

* [Databases](database.md)
* [Documents](document.md)
* [Blobs](blob.md)
* [Remote Sync Gateway](replication.md)
* [Handling Data Conflicts](conflict.md)

.

### [](#-6)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.

---

[1](#%5Ffootnoteref%5F1). Any change to this reserved key will be detected when it is saved and will result in a Couchbase exception (Error Code 5 — `CorruptRevisionData`)