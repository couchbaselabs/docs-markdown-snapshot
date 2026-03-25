---
title: Documents
description: Couchbase Lite concepts -- Data model -- Documents
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.1/modules/java/pages/document.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:3.1@couchbase-lite:java:document.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.1/java/document.html)

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

You can consider a document as the equivalent of a 'row' in a relational table, with each of the document’s attributes being equivalent to a 'column'.

Documents can contain nested structures. This allows developers to express many-to-many relationships without requiring a reference or join table, and is naturally expressive of hierarchical data.

Most apps will work with one or more documents, persisting them to a local database and optionally syncing them, either centrally or to the cloud.

In this section we provide an example of how you might create a `hotel` document, which provides basic contact details and price data.

Data Model

```Java
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

```Java
// Get the database (and create it if it doesn’t exist).
Database database = new Database("getting-started");
try (Collection collection = database.getCollection("myCollection")) {
    if (collection == null) { throw new IllegalStateException("collection not found"); }
```

See [Databases](database.md) for more information

### [](#create-a-document)Create a Document

Now create a new document to hold your application’s data.

Use the mutable form, so that you can add data to the document.

```Java
// Create your new document
MutableDocument mutableDoc = new MutableDocument();
```

For more on using **Documents**, see [Document Initializers](#document-initializers) and [Mutability](#mutability).

### [](#create-a-dictionary)Create a Dictionary

Now create a mutable dictionary (`address`).

Each element of the dictionary value will be directly accessible via its own key.

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

```Java
// Create and populate mutable array
MutableArray phones = new MutableArray();
phones.addString("650-000-0000");
phones.addString("650-000-0001");
```

Learn more about [Using Arrays](#using-arrays)

### [](#populate-a-document)Populate a Document

Now add your data to the mutable document created earlier. Each data item is stored as a key-value pair.

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

```Java
// Save the document changes (1)
collection.save(mutableDoc);
```

### [](#close-the-database)Close the Database

With your document saved, you can now close our Couchbase Lite database.

```Java
// Close the database (1)
database.close();
```

## [](#working-with-data)Working with Data

### [](#checking-a-documents-properties)Checking a Document’s Properties

To check whether a given property exists in the document, use the [\`Document.Contains(String key)](http://docs.couchbase.com/mobile/3.1.11/couchbase-lite-java/com/couchbase/lite/Document.html#contains-java.lang.String-) method.

If you try to access a property which doesn’t exist in the document, the call will return the default value for that getter method (0 for [Document.getInt()](http://docs.couchbase.com/mobile/3.1.11/couchbase-lite-java/com/couchbase/lite/Document.html#getInt-java.lang.String-) 0.0 for [Document.getFloat()](http://docs.couchbase.com/mobile/3.1.11/couchbase-lite-java/com/couchbase/lite/Document.html#getFloat-java.lang.String-) etc.).

### [](#date-accessors)Date accessors

Couchbase Lite offers _Date_ accessors as a convenience. Dates are a common data type, but JSON doesn’t natively support them, so the convention is to store them as strings in ISO-8601 format.

Example 1\. Date Getter

This example sets the date on the `createdAt` property and reads it back using the [Document.getDate()](http://docs.couchbase.com/mobile/3.1.11/couchbase-lite-java/com/couchbase/lite/Document.html#getDate-java.lang.String-) accessor method.

```Java
newTask.setValue("createdAt", new Date());
Date date = newTask.getDate("createdAt");
```

### [](#using-dictionaries)Using Dictionaries

API References

* [Dictionary](http://docs.couchbase.com/mobile/3.1.11/couchbase-lite-java/com/couchbase/lite/Dictionary.html)
* [MutableDictionary](http://docs.couchbase.com/mobile/3.1.11/couchbase-lite-java/com/couchbase/lite/MutableDictionary.html)

Example 2\. Read Only

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

* [Array](http://docs.couchbase.com/mobile/3.1.11/couchbase-lite-java/com/couchbase/lite/Array.html)
* [MutableArray](http://docs.couchbase.com/mobile/3.1.11/couchbase-lite-java/com/couchbase/lite/MutableArray.html)

Example 4\. Read Only

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

* Use the [MutableDocument()](http://docs.couchbase.com/mobile/3.1.11/couchbase-lite-java/com/couchbase/lite/MutableDocument.html#s:18CouchbaseLiteSwift15MutableDocumentCACycfc) initializer to create a new document where the document ID is randomly generated by the database.
* Use the [MutableDocument(String id)](http://docs.couchbase.com/mobile/3.1.11/couchbase-lite-java/com/couchbase/lite/MutableDocument.html#s:18CouchbaseLiteSwift15MutableDocumentC2idACSSSg%5Ftcfc) initializer to create a new document with a specific ID.
* Use the {url-api-method-collection-getdocument} method to get a document. If the document doesn’t exist in the collection, the method will return `null`. You can use this behavior to check if a document with a given ID already exists in the collection.

Example 6\. Persist a document

The following code example creates a document and persists it to the database.

```Java
MutableDocument newTask = new MutableDocument();
newTask.setString("type", "task");
newTask.setString("owner", "todo");
newTask.setDate("createdAt", new Date());
collection.save(newTask);
```

## [](#mutability)Mutability

By default, a document is immutable when it is read from the database. Use the [\`Document.toMutable()](http://docs.couchbase.com/mobile/3.1.11/couchbase-lite-java/com/couchbase/lite/Document.html#toMutable--) to create an updatable instance of the document.

Example 7\. Make a mutable document

Changes to the document are persisted to the database when the `save` method is called.

```Java
MutableDocument mutableDocument = collection.getDocument("xyz").toMutable();
mutableDocument.setString("name", "apples");
collection.save(mutableDocument);
```

> [!NOTE]
> Any user change to the value of reserved keys (`_id`, `_rev` or `_deleted`) will be detected when a document is saved and will result in an exception (Error Code 5 — `CorruptRevisionData`) — see also [Document Constraints](#lbl-doc-constraints).

## [](#batch-operations)Batch operations

If you’re making multiple changes to a database at once, it’s faster to group them together. The following example persists a few documents in batch.

Example 8\. Batch operations

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

At the **local** level this operation is still transactional: no other `Database` instances, including ones managed by the replicator can make changes during the execution of the block, and other instances will not see partial changes. But Couchbase Mobile is a distributed system, and due to the way replication works, there’s no guarantee that Sync Gateway or other devices will receive your changes all at once.

## [](#document-change-events)Document change events

You can register for document changes. The following example registers for changes to the document with ID `user.john` and prints the `verified_account` property when a change is detected.

Example 9\. Document change events

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

## [](#document-expiration)Document Expiration

Document expiration allows users to set the expiration date for a document. When the document expires, it is purged from the database. The purge is not replicated to Sync Gateway.

Example 10\. Set document expiration

This example sets the TTL for a document to 1 day from the current time.

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

* Initialize a 'MutableArrayObject' using data supplied as a JSON string. This is done using the `init(json)` constructor — see: [Example 4](#ex-array)
* Convert an `ArrayFragment` object to a JSON String
* Set data with a JSON string using `setJSON()`

Example 12\. Arrays as JSON strings

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

You can use `isBlob()` to check whether a given dictionary object is a blob or not — see [Example 13](#ex-blob).

Note that the blob object must first be saved to the database (generating the required metadata) before you can use the `toJSON` method.

Example 13\. Blobs as JSON strings

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

* Initialize a 'MutableDictionaryObject' using data supplied as a JSON string. This is done using the `init(json)` constructor-- see: [Example 14](#ex-dictionary)
* Set data with a JSON string using `setJSON()`

Example 14\. Dictionaries as JSON strings

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

* Initialize a 'MutableDocument' using data supplied as a JSON string. This is done using the `init(json)` or `init(id: json:)` constructor — see: [Example 15](#ex-document)
* Set data with a JSON string using `setJSON()`

Example 15\. Documents as JSON strings

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

Convert a `Query Result` to JSON using its `toJSON()` accessor method.

Example 16\. Using JSON Results

Use [Result.toJSON()](http://docs.couchbase.com/mobile/3.1.11/couchbase-lite-java/com/couchbase/lite/Result.html#toJSON--) to transform your result string into a JSON string, which can easily be serialized or used as required in your application. See <\> for a working example. 

```Java
        ObjectMapper mapper = new ObjectMapper();
        ArrayList<Hotel> hotels = new ArrayList<>();
        HashMap<String, Object> dictFromJSONstring;

        try (ResultSet resultSet = listQuery.execute()) {
            for (Result result: resultSet) {

                // Get result as JSON string
                String thisJsonString = result.toJSON(); (1)

                // Get Java  Hashmap from JSON string
                dictFromJSONstring =
                    mapper.readValue(thisJsonString, HashMap.class); (2)


                // Use created hashmap
                String hotelId = dictFromJSONstring.get("id").toString();
                String hotelType = dictFromJSONstring.get("type").toString();
                String hotelname = dictFromJSONstring.get("name").toString();


                // Get custom object from Native 'dictionary' object
                Hotel thisHotel =
                    mapper.readValue(thisJsonString, Hotel.class); (3)
                hotels.add(thisHotel);
            }
        }
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
    }

    public List<Map<String, Object>> docsOnlyQuerySyntaxN1QL(Database thisDb) throws CouchbaseLiteException {
        // For Documentation -- N1QL Query using parameters
        //  Declared elsewhere: Database thisDb
        Query thisQuery =
            thisDb.createQuery(
                "SELECT META().id AS thisId FROM _ WHERE type = \"hotel\""); (4)
        List<Map<String, Object>> results = new ArrayList<>();
        try (ResultSet rs = thisQuery.execute()) {
            for (Result result: rs) { results.add(result.toMap()); }
        }
        return results;
    }

    public List<Map<String, Object>> docsonlyQuerySyntaxN1QLParams(Database thisDb) throws CouchbaseLiteException {
        // For Documentation -- N1QL Query using parameters
        //  Declared elsewhere: Database thisDb

        Query thisQuery =
            thisDb.createQuery(
                "SELECT META().id AS thisId FROM _ WHERE type = $type"); // <.

        thisQuery.setParameters(
            new Parameters().setString("type", "hotel")); (5)

        List<Map<String, Object>> results = new ArrayList<>();
        try (ResultSet rs = thisQuery.execute()) {
            for (Result result: rs) { results.add(result.toMap()); }
        }
        return results;
    }
}

//
// Copyright (c) 2023 Couchbase, Inc All rights reserved.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
// http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//
package com.couchbase.codesnippets;

import androidx.annotation.NonNull;

import java.net.URI;
import java.net.URISyntaxException;
import java.security.KeyStore;
import java.security.KeyStoreException;
import java.security.cert.X509Certificate;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;

import com.couchbase.codesnippets.utils.Logger;
import com.couchbase.lite.BasicAuthenticator;
import com.couchbase.lite.Collection;
import com.couchbase.lite.CollectionConfiguration;
import com.couchbase.lite.CouchbaseLiteException;
import com.couchbase.lite.Database;
import com.couchbase.lite.DatabaseEndpoint;
import com.couchbase.lite.DocumentFlag;
import com.couchbase.lite.Endpoint;
import com.couchbase.lite.ListenerToken;
import com.couchbase.lite.ReplicatedDocument;
import com.couchbase.lite.Replicator;
import com.couchbase.lite.ReplicatorConfiguration;
import com.couchbase.lite.ReplicatorProgress;
import com.couchbase.lite.ReplicatorStatus;
import com.couchbase.lite.ReplicatorType;
import com.couchbase.lite.SessionAuthenticator;
import com.couchbase.lite.URLEndpoint;


@SuppressWarnings({"unused"})
public class ReplicationExamples {
    private Replicator thisReplicator;
    private ListenerToken thisToken;

    public void activeReplicatorExample(Set<Collection> collections)
        throws URISyntaxException {
        // Create replicator
        // Consider holding a reference somewhere
        // to prevent the Replicator from being GCed
        Replicator repl = new Replicator( (6)

            // initialize the replicator configuration
            new ReplicatorConfiguration(new URLEndpoint(new URI("wss://listener.com:8954"))) (7)
                .addCollections(collections, null)

                // Set replicator type
                .setType(ReplicatorType.PUSH_AND_PULL)

                // Configure Sync Mode
                .setContinuous(false) // default value


                // set auto-purge behavior
                // (here we override default)
                .setAutoPurgeEnabled(false) (8)


                // Configure Server Authentication --
                // only accept self-signed certs
                .setAcceptOnlySelfSignedServerCertificate(true) (9)

                // Configure the credentials the
                // client will provide if prompted
                .setAuthenticator(new BasicAuthenticator("Our Username", "Our Password".toCharArray())) (10)

        );

        // Optionally add a change listener (11)
        ListenerToken token = repl.addChangeListener(change -> {
            CouchbaseLiteException err = change.getStatus().getError();
            if (err != null) { Logger.log("Error code :: " + err.getCode(), err); }
        });

        // Start replicator
        repl.start(false); (12)


        thisReplicator = repl;
        thisToken = token;

    }

    public void replicatorSimpleExample(Set<Collection> collections) throws URISyntaxException {
        Endpoint theListenerEndpoint
            = new URLEndpoint(new URI("wss://10.0.2.2:4984/db")); (13)

        ReplicatorConfiguration thisConfig =
            new ReplicatorConfiguration(theListenerEndpoint) (14)
                .addCollections(collections, null) // default configuration

                .setAcceptOnlySelfSignedServerCertificate(true) (15)
                .setAuthenticator(new BasicAuthenticator(
                    "valid.user",
                    "valid.password".toCharArray())); (16)

        Replicator repl = new Replicator(thisConfig); (17)
        // Start the replicator
        repl.start(); (18)
        // (be sure to hold a reference somewhere that will prevent it from being GCed)
        thisReplicator = repl;

    }

    public void replicationBasicAuthenticationExample(
        Set<Collection> collections,
        CollectionConfiguration collectionConfig)
        throws URISyntaxException {

        // Create replicator (be sure to hold a reference somewhere that will prevent the Replicator from being GCed)
        Replicator repl = new Replicator(
            new ReplicatorConfiguration(new URLEndpoint(new URI("ws://localhost:4984/mydatabase")))
                .addCollections(collections, collectionConfig)
                .setAuthenticator(new BasicAuthenticator("username", "password".toCharArray())));

        repl.start();
        thisReplicator = repl;
    }


    public void replicationSessionAuthenticationExample(
        Set<Collection> collections,
        CollectionConfiguration collectionConfig)
        throws URISyntaxException {

        // Create replicator (be sure to hold a reference somewhere that will prevent the Replicator from being GCed)
        Replicator repl = new Replicator(
            new ReplicatorConfiguration(new URLEndpoint(new URI("ws://localhost:4984/mydatabase")))
                .addCollections(collections, collectionConfig)
                .setAuthenticator(new SessionAuthenticator("904ac010862f37c8dd99015a33ab5a3565fd8447")));

        repl.start();
        thisReplicator = repl;
    }

    public void replicationCustomHeaderExample(
        Set<Collection> collections,
        CollectionConfiguration collectionConfig)
        throws URISyntaxException {
        Map<String, String> headers = new HashMap<>();
        headers.put("CustomHeaderName", "Value");

        // Create replicator (be sure to hold a reference somewhere that will prevent the Replicator from being GCed)
        Replicator repl = new Replicator(
            new ReplicatorConfiguration(new URLEndpoint(new URI("ws://localhost:4984/mydatabase")))
                .addCollections(collections, collectionConfig)
                .setHeaders(headers));

        repl.start();
        thisReplicator = repl;
    }

    public void replicationPushFilterExample(Set<Collection> collections) throws URISyntaxException {
        CollectionConfiguration collectionConfig = new CollectionConfiguration()
            .setPushFilter((document, flags) -> flags.contains(DocumentFlag.DELETED)); (1)

        // Create replicator (be sure to hold a reference somewhere that will prevent the Replicator from being GCed)
        Replicator repl = new Replicator(
            new ReplicatorConfiguration(new URLEndpoint(new URI("ws://localhost:4984/mydatabase")))
                .addCollections(collections, collectionConfig));

        repl.start();
        thisReplicator = repl;
    }


    public void replicationPullFilterExample(Set<Collection> collections) throws URISyntaxException {
        CollectionConfiguration collectionConfig = new CollectionConfiguration()
            .setPullFilter((document, flags) -> "draft".equals(document.getString("type"))); (1)

        // Create replicator (be sure to hold a reference somewhere that will prevent the Replicator from being GCed)
        Replicator repl = new Replicator(
            new ReplicatorConfiguration(new URLEndpoint(new URI("ws://localhost:4984/mydatabase")))
                .addCollections(collections, collectionConfig));

        repl.start();
        thisReplicator = repl;
    }

    public void replicationResetCheckpointExample(Set<Collection> collections) throws URISyntaxException {
        // Create replicator (be sure to hold a reference somewhere that will prevent the Replicator from being GCed)
        Replicator repl = new Replicator(
            new ReplicatorConfiguration(new URLEndpoint(new URI("ws://localhost:4984/mydatabase")))
                .addCollections(collections, null));

        repl.start(true);

        // ... at some later time

        repl.stop();
    }

    public void handlingNetworkErrorsExample(Set<Collection> collections) throws URISyntaxException {
        // Create replicator (be sure to hold a reference somewhere that will prevent the Replicator from being GCed)
        Replicator repl = new Replicator(
            new ReplicatorConfiguration(new URLEndpoint(new URI("ws://localhost:4984/mydatabase")))
                .addCollections(collections, null));

        repl.addChangeListener(change -> {
            CouchbaseLiteException error = change.getStatus().getError();
            if (error != null) { Logger.log("Error code:: " + error); }
        });
        repl.start();
        thisReplicator = repl;
    }

    public void certificatePinningExample(Set<Collection> collections, String keyStoreName, String certAlias)
        throws URISyntaxException, KeyStoreException {
        // Create replicator (be sure to hold a reference somewhere that will prevent the Replicator from being GCed)
        Replicator repl = new Replicator(
            new ReplicatorConfiguration(new URLEndpoint(new URI("ws://localhost:4984/mydatabase")))
                .addCollections(collections, null)
                .setPinnedServerX509Certificate(
                    (X509Certificate) KeyStore.getInstance(keyStoreName).getCertificate(certAlias)));

        repl.start();
        thisReplicator = repl;
    }

    public void replicatorConfigExample(Set<Collection> collections) throws URISyntaxException {
        // initialize the replicator configuration
        ReplicatorConfiguration thisConfig = new ReplicatorConfiguration(
            new URLEndpoint(new URI("wss://10.0.2.2:8954/travel-sample"))) (19)
            .addCollections(collections, null);
    }


    public void p2pReplicatorStatusExample(Replicator repl) {
        ReplicatorStatus status = repl.getStatus();
        ReplicatorProgress progress = status.getProgress();
        Logger.log(
            "The Replicator is " + status.getActivityLevel()
                + "and has processed " + progress.getCompleted()
                + " of " + progress.getTotal() + " changes");
    }


    public void p2pReplicatorStopExample(Replicator repl) {
        // Stop replication.
        repl.stop(); (20)
    }


    public void customRetryConfigExample(Set<Collection> collections) throws URISyntaxException {
        Replicator repl = new Replicator(
            new ReplicatorConfiguration(new URLEndpoint(new URI("ws://localhost:4984/mydatabase")))
                .addCollections(collections, null)
                //  other config as required . . .
                .setHeartbeat(150) (21)
                .setMaxAttempts(20) (22)
                .setMaxAttemptWaitTime(600)); (23)

        repl.start();
        thisReplicator = repl;
    }

    public void replicatorDocumentEventExample(Set<Collection> collections) throws URISyntaxException {
        // Create replicator (be sure to hold a reference somewhere that will prevent the Replicator from being GCed)
        Replicator repl = new Replicator(
            new ReplicatorConfiguration(new URLEndpoint(new URI("ws://localhost:4984/mydatabase")))
                .addCollections(collections, null));


        ListenerToken token = repl.addDocumentReplicationListener(replication -> {
            Logger.log("Replication type: " + ((replication.isPush()) ? "push" : "pull"));
            for (ReplicatedDocument document: replication.getDocuments()) {
                Logger.log("Doc ID: " + document.getID());

                CouchbaseLiteException err = document.getError();
                if (err != null) {
                    // There was an error
                    Logger.log("Error replicating document: ", err);
                    return;
                }

                if (document.getFlags().contains(DocumentFlag.DELETED)) {
                    Logger.log("Successfully replicated a deleted document");
                }
            }
        });


        repl.start();
        thisReplicator = repl;

        token.remove();
    }

    public void replicationPendingDocumentsExample(Collection collection)
        throws CouchbaseLiteException, URISyntaxException {
        Replicator repl = new Replicator(
            new ReplicatorConfiguration(new URLEndpoint(new URI("ws://localhost:4984/mydatabase")))
                .addCollection(collection, null)
                .setType(ReplicatorType.PUSH));

        Set<String> pendingDocs = repl.getPendingDocumentIds(collection);

        if (!pendingDocs.isEmpty()) {
            Logger.log("There are " + pendingDocs.size() + " documents pending");

            final String firstDoc = pendingDocs.iterator().next();

            repl.addChangeListener(change -> {
                Logger.log("Replicator activity level is " + change.getStatus().getActivityLevel());
                try {
                    if (!repl.isDocumentPending(firstDoc, collection)) {
                        Logger.log("Doc ID " + firstDoc + " has been pushed");
                    }
                }
                catch (CouchbaseLiteException err) {
                    Logger.log("Failed getting pending docs", err);
                }
            });

            repl.start();
            this.thisReplicator = repl;
        }
    }

    public void databaseReplicatorExample(@NonNull Set<Collection> srcCollections, @NonNull Database targetDb) {
        // This is an Enterprise feature:
        // the code below will generate a compilation error
        // if it's compiled against CBL Android Community Edition.
        // Note: the target database must already contain the
        //       source collections or the replication will fail.
        final Replicator repl = new Replicator(
            new ReplicatorConfiguration(new DatabaseEndpoint(targetDb))
                .addCollections(srcCollections, null)
                .setType(ReplicatorType.PUSH));

        // Start the replicator
        // (be sure to hold a reference somewhere that will prevent it from being GCed)
        repl.start();
        thisReplicator = repl;
    }

    public void replicationWithCustomConflictResolverExample(Set<Collection> srcCollections, URI targetUri) {
        Replicator repl = new Replicator(
            new ReplicatorConfiguration(new URLEndpoint(targetUri))
                .addCollections(
                    srcCollections,
                    new CollectionConfiguration()
                        .setConflictResolver(new LocalWinConflictResolver())));

        // Start the replicator
        // (be sure to hold a reference somewhere that will prevent it from being GCed)
        repl.start();
        thisReplicator = repl;
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