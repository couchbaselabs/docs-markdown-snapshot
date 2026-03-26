---
title: Documents
description: Couchbase Lite concepts -- Data model -- Documents
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.0/modules/objc/pages/document.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.0@couchbase-lite:objc:document.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.0/objc/document.html)

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

```objc
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

```objc
// Get the database (and create it if it doesn’t exist).

NSError *error;
CBLDatabase *database = [[CBLDatabase alloc] initWithName:@"hoteldb" error:&error];
```

See [Databases](database.md) for more information

### [](#create-a-document)Create a Document

Now create a new document to hold your application's data.

Use the mutable form, so that you can add data to the document.

```objc
// Create your new document
// The lack of 'const' indicates this document is mutable
CBLMutableDocument *mutableDoc = [[CBLMutableDocument alloc] init];
```

For more on using **Documents**, see [Document Initializers](#document-initializers) and [Mutability](#mutability).

### [](#create-a-dictionary)Create a Dictionary

Now create a mutable dictionary (`address`).

Each element of the dictionary value will be directly accessible via its own key.

```objc
// Create and populate mutable dictionary
// Create a new mutable dictionary and populate some keys/values
CBLMutableDictionary *address = [[CBLMutableDictionary alloc] init];
[address setString:@"1 Main st" forKey:@"street"];
[address setString:@"San Francisco" forKey:@"city"];
[address setString:@"CA" forKey:@"state"];
[address setString:@"USA" forKey:@"country"];
[address setString:@"90210" forKey:@"code"];
```

Learn more about [Using Dictionaries](#using-dictionaries).

### [](#create-an-array)Create an Array

Since the hotel may have multiple contact numbers, provide a field (`phones`) as a mutable array.

```objc
// Create and populate mutable array
CBLMutableArray *phones = [[CBLMutableArray alloc] init];
[phones addString:@"650-000-0000"];
[phones addString:@"650-000-0001"];
```

Learn more about [Using Arrays](#using-arrays)

### [](#populate-a-document)Populate a Document

Now add your data to the mutable document created earlier. Each data item is stored as a key-value pair.

```objc
// Initialize and populate the document

// Add document type and hotel name as string
[mutableDoc setString:@"hotel" forKey:@"type"];
[mutableDoc setString:@"Hotel Java Mo" forKey:@"name"];

// Add average room rate (float)
[mutableDoc setFloat:121.75 forKey:@"room_rate"];

// Add address (dictionary)
[mutableDoc setDictionary:address forKey:@"address"];

// Add phone numbers(array)
[mutableDoc setArray:phones forKey:@"phones"];
```

> [!NOTE]
> Couchbase recommend using a `type` attribute to define each logical document type.

### [](#save-a-document)Save a Document

Now persist the populated document to your Couchbase Lite database. This will auto-generate the document id.

```objc
[self.database saveDocument:mutableDoc error:&error];
```

### [](#close-the-database)Close the Database

With your document saved, you can now close our Couchbase Lite database.

```objc
if (![self.database close:&error])
    NSLog(@"Error closing db:%@", error);
```

## [](#working-with-data)Working with Data

### [](#date-accessors)Date accessors

Couchbase Lite offers _Date_ accessors as a convenience. Dates are a common data type, but JSON doesn't natively support them, so the convention is to store them as strings in ISO-8601 format.

Example 1\. Date Getter

This example sets the date on the `createdAt` property and reads it back using the [dateForKey:](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Protocols/CBLDictionary.html#/c:objc%28pl%29CBLDictionary%28im%29dateForKey:) accessor method.

```objc
[newTask setValue:[NSDate date] forKey:@"createdAt"];
NSDate *date = [newTask dateForKey:@"createdAt"];
```

### [](#using-dictionaries)Using Dictionaries

API References

* [CBLDictionary](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLDictionary.html)
* [CBLMutableDictionary](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLMutableDictionary.html)

Example 2\. Read Only

```objc
CBLDocument *document = [self.database documentWithID:@"doc1"];

// Getting a dictionary value from the document
CBLDictionary *dict = [document dictionaryForKey:@"address"];

// Access a value from the dictionary
NSString *street = [dict stringForKey:@"street"];
NSLog(@"Street:: %@", street);

// Iterate dictionary
for (NSString *key in dict) {
    id value = [dict valueForKey:key];
    NSLog(@"Value:: %@", value);
}

// Create a mutable copy
CBLMutableDictionary *mutableDict = [dict toMutable];
[mutableDict setString:@"1 Great sts" forKey:@"street"];
```

Example 3\. Mutable

```objc

// Create a new mutable dictionary and populate some keys/values
CBLMutableDictionary *dict = [[CBLMutableDictionary alloc] init];
[dict setString:@"1 Main st" forKey:@"street"];
[dict setString:@"San Francisco" forKey:@"city"];

// Set the dictionary to a document and save the document
CBLMutableDocument *document = [[CBLMutableDocument alloc] init];
[document setDictionary:dict forKey:@"address"];
NSError *error;
[self.database saveDocument:document error:&error];
```

### [](#using-arrays)Using Arrays

API References

* [CBLArray](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLArray.html)
* [CBLMutableArray](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLMutableArray.html)

Example 4\. Read Only

```objc
CBLDocument *document = [self.database documentWithID:@"doc1"];

// Getting an array value from the document
CBLArray *array = [document arrayForKey:@"phones"];

// Get element count
NSUInteger count = array.count;
NSLog(@"Count:: %lu", (unsigned long)count);

// Access an array element by index
if (count > 0) {
    id value = [array valueAtIndex:0];
    NSLog(@"Value:: %@", value);
}

// Iterate the array
for (id value in array) {
    NSLog(@"Value:: %@", value);
}

// Create a mutable copy
CBLMutableArray *mutableArray = [array toMutable];
[mutableArray addString:@"650-000-0002"];
```

Example 5\. Mutable

```objc
// Create a new mutable array and populate data into the array
CBLMutableArray *array = [[CBLMutableArray alloc] init];
[array addString:@"650-000-0000"];
[array addString:@"650-000-0001"];

// Set the array to a document and save the document
CBLMutableDocument *document = [[CBLMutableDocument alloc] init];
[document setArray:array forKey:@"address"];
NSError *error;
[self.database saveDocument:document error:&error];
```

### [](#using-blobs)Using Blobs

For more on working with blobs, see [Blobs](blob.md)

## [](#document-initializers)Document Initializers

You can use the following methods/initializers:

* Use the [(nonnull instancetype)init;](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLMutableDocument.html#/c:objc%28cs%29CBLMutableDocument%28im%29init) initializer to create a new document where the document ID is randomly generated by the database.
* Use the [(nonnull instancetype)initWithID:(nullable NSString \*)documentID;](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLMutableDocument.html#/c:objc%28cs%29CBLMutableDocument%28im%29initWithID:) initializer to create a new document with a specific ID.
* Use the [(nullable CBLDocument \*)documentWithID:(nonnull NSString \*)id;](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLDatabase.html#/c:objc%28cs%29CBLDatabase%28im%29documentWithID:) method to get a document. If the document doesn't exist in the database, the method will return `null`. You can use this behavior to check if a document with a given ID already exists in the database.

Example 6\. Persist a document

The following code example creates a document and persists it to the database.

```objc
CBLMutableDocument *newTask = [[CBLMutableDocument alloc] init];
[newTask setString:@"task" forKey:@"task"];
[newTask setString:@"todo" forKey:@"owner"];
[newTask setString:@"task" forKey:@"createdAt"];
[self.database saveDocument:newTask error:&error];
```

## [](#mutability)Mutability

By default, a document is immutable when it is read from the database. Use the [(nonnull CBLMutableDocument \*)toMutable;](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLDocument.htmlc:objc%28cs%29CBLDocument%28im%29toMutable) to create an updatable instance of the document.

Example 7\. Make a mutable document

Changes to the document are persisted to the database when the `save` method is called.

```objc
CBLDocument *document = [self.database documentWithID:@"xyz"];
CBLMutableDocument *mutableDocument = [document toMutable];
[mutableDocument setString:@"apples" forKey:@"name"];
[self.database saveDocument:mutableDocument error:&error];
```

> [!NOTE]
> Any user change to the value of reserved keys (`_id`, `_rev` or `_deleted`) will be detected when a document is saved and will result in an exception (Error Code 5 — `CorruptRevisionData`) — see also [Document Constraints](#lbl-doc-constraints).

## [](#batch-operations)Batch operations

If you're making multiple changes to a database at once, it's faster to group them together. The following example persists a few documents in batch.

Example 8\. Batch operations

```objc
[self.database inBatch:&error usingBlock:^{
    for (int i = 0; i < 10; i++) {
        CBLMutableDocument *doc = [[CBLMutableDocument alloc] init];
        [doc setValue:@"user" forKey:@"type"];
        [doc setValue:[NSString stringWithFormat:@"user %d", i] forKey:@"name"];
        [doc setBoolean:NO forKey:@"admin"];

        NSError *err = nil;
        [self.database saveDocument:doc error:&err];
    }
}];
```

At the **local** level this operation is still transactional: no other `Database` instances, including ones managed by the replicator can make changes during the execution of the block, and other instances will not see partial changes. But Couchbase Mobile is a distributed system, and due to the way replication works, there's no guarantee that Sync Gateway or other devices will receive your changes all at once.

## [](#document-change-events)Document change events

You can register for document changes. The following example registers for changes to the document with ID `user.john` and prints the `verified_account` property when a change is detected.

Example 9\. Document change events

```objc
[self.database addDocumentChangeListenerWithID:@"user.john" listener:^(CBLDocumentChange  *change) {
    CBLDocument *document = [wSelf.database documentWithID:change.documentID];
    NSLog(@"Status ::%@)", [document stringForKey:@"verified_account"]);
}];
```

## [](#document-expiration)Document Expiration

Document expiration allows users to set the expiration date for a document. When the document expires, it is purged from the database. The purge is not replicated to Sync Gateway.

Example 10\. Set document expiration

This example sets the TTL for a document to 5 minutes from the current time.

```objc
// Purge the document one day from now
NSDate *ttl = [[NSCalendar currentCalendar] dateByAddingUnit:NSCalendarUnitDay
                                                       value:1
                                                      toDate:[NSDate date]
                                                     options:0];
[self.database setDocumentExpirationWithID:@"doc123" expiration:ttl error:&error];

// Reset expiration
[self.database setDocumentExpirationWithID:@"doc1" expiration:nil error:&error];

// Query documents that will be expired in less than five minutes
NSTimeInterval fiveMinutesFromNow = [[NSDate dateWithTimeIntervalSinceNow:60 * 5] timeIntervalSince1970];
CBLQuery *query = [CBLQueryBuilder select:@[[CBLQuerySelectResult expression:[CBLQueryMeta id]]]
                                     from:[CBLQueryDataSource database:self.database]
                                    where:[[CBLQueryMeta expiration]
                                            lessThan:[CBLQueryExpression double:fiveMinutesFromNow]]];
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

```objc
NSString *json = @"[\"1000\",\"1001\",\"1002\",\"1003\"]";

CBLMutableArray *myArray = [[CBLMutableArray alloc] initWithJSON:json error:&error];

for (NSString *item in myArray) {
    NSLog(@"%@", item);
}
```

### [](#lbl-blob)Blobs

Convert a `Blob` to JSON using the `toJSON` method — see [Example 13](#ex-blob).

You can use `isBlob()` to check whether a given dictionary object is a blob or not — see [Example 13](#ex-blob).

Note that the blob object must first be saved to the database (generating the required metadata) before you can use the `toJSON` method.

Example 13\. Blobs as JSON strings

```objc

CBLDocument *doc = [self.database documentWithID:@"doc-1000"];
CBLBlob *blob = [doc blobForKey:@"avatar"];
NSString *json = [blob toJSON];
NSLog(@"json string is %@", json);
```

See also: [Blobs](blob.md)

### [](#lbl-dictionary)Dictionaries

Convert a `DictionaryObject` to and from JSON using the `toJSON` and `toDictionary` methods — see [Example 14](#ex-dictionary).

Additionally you can:

* Initialize a 'MutableDictionaryObject' using data supplied as a JSON string. This is done using the `init(json)` constructor-- see: [Example 14](#ex-dictionary)
* Set data with a JSON string using `setJSON()`

Example 14\. Dictionaries as JSON strings

```objc
NSString *aJSONstring = @"{\"id\":\"1002\",\"type\":\"hotel\",\"name\":\"Hotel Ned\","
"\"city\":\"Balmain\",\"country\":\"Australia\",\"description\":\"Undefined description for Hotel Ned\"}";


CBLMutableDictionary *myDict = [[CBLMutableDictionary alloc] initWithJSON:aJSONstring
                                                                    error:&error];

NSString *name = [myDict stringForKey:@"name"];

for (NSString *key in myDict) {
    NSLog(@"%@ %@", key, [myDict valueForKey:key]);
}
```

### [](#lbl-document)Documents

Convert a `Document` to and from JSON strings using the `toJSON()` and `setJSON()` methods — see [Example 15](#ex-document).

Additionally you can:

* Initialize a 'MutableDocument' using data supplied as a JSON string. This is done using the `init(json)` or `init(id: json:)` constructor — see: [Example 15](#ex-document)
* Set data with a JSON string using `setJSON()`

Example 15\. Documents as JSON strings

```objc

CBLDocument *doc = [self.database documentWithID:@"doc-1000"];
NSString *json = [doc toJSON];
NSLog(@"json %@", json);
```

### [](#lbl-result)Query Results as JSON

Convert a `Query Result` to JSON using its `toJSON()` accessor method.

Example 16\. Using JSON Results

Use [CBLResult.toJSON](http://docs.couchbase.com/mobile/3.0.15/couchbase-lite-objc/Classes/CBLQueryResult.html#/c:objc%28cs%29CBLQueryResult%28im%29toJSON) to transform your result string into a JSON string, which can easily be serialized or used as required in your application. See <\> for a working example. 

```objc
CBLQueryResultSet *rs = [query execute:&error];
for (CBLQueryResult *result in rs) {

    // Get result as a JSON string
    NSString *json = [result toJSON];

    // Get an native Obj-C object from the Json String
    NSDictionary *dict = [NSJSONSerialization JSONObjectWithData:[json dataUsingEncoding:NSUTF8StringEncoding]
                                                                     options:NSJSONReadingAllowFragments
                                                                       error:&error];

    // Log generated Json and Native objects
    // For demo/example purposes
    NSLog(@"Json String %@", json);
    NSLog(@"Native Object %@", dict);

}; // end for
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