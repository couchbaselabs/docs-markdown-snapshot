---
title: Build and Run
description: Build and run a starter app to validate your install of Couchbase Lite on C
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.0/modules/c/pages/gs-build.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/couchbase-lite/current/c/gs-build.html)

# Build and Run

> Description — _Build and run a starter app to validate your install of Couchbase Lite on C_  

Steps in Getting Started

[Install](gs-install.md)| **Build**

## [](#verify-install)Verify Install

Now you have _Couchbase Lite for C_ installed, you can verify that your apps build correctly.

Enter the C code from [Example 1](#ex-c-starter) into your editor of choice and build it.

Running it will create a database, add a document, retrieve the document, update the document and then delete the document.

Example 1\. Sample code

```c
//  Purpose-- provide an overview of available crud  and sync functionality
//
// Get the database (and create it if it doesn't exist)
CBLError err{};
CBLDatabase* database = CBLDatabase_Open(FLSTR("mydb"), NULL, &err);
if(!database) {
    // Error handling.  For brevity, this is truncated in the rest of the snippet
    // and omitted in other doc code snippets
    fprintf(stderr, "Error opening database (%d / %d)\n", err.domain, err.code);
    FLSliceResult msg = CBLError_Message(&err);
    fprintf(stderr, "%.*s\n", (int)msg.size, (const char *)msg.buf);
    FLSliceResult_Release(msg);
    return;
}

// All CRUD operations must be carried out via a collection.
// Remember to release the collection using CBLCollection_Release() when done.
CBLCollection* collection = CBLDatabase_DefaultCollection(database, &err);

// The lack of 'const' indicates this document is mutable
// Create a new document (i.e. a record) in the database
CBLDocument* mutableDoc = CBLDocument_Create();
FLMutableDict properties = CBLDocument_MutableProperties(mutableDoc);
FLMutableDict_SetFloat(properties, FLSTR("version"), 3.0f);

// Save it to the database
if(!CBLCollection_SaveDocument(collection, mutableDoc, &err)) {
    // Failed to save, do error handling as above
    return;
}

// Since we will release the document, make a copy of the ID since it
// is an internal pointer.  Whenever we create or get an FLSliceResult
// or FLStringResult we will need to free it later too!
FLString id = CBLDocument_ID(mutableDoc);
CBLDocument_Release(mutableDoc);

// Update a document
mutableDoc = CBLCollection_GetMutableDocument(collection, id, &err);
if(!mutableDoc) {
    // Failed to retrieve, do error handling as above.  NOTE: error code 0 simply means
    // the document does not exist.
    return;
}

properties = CBLDocument_MutableProperties(mutableDoc);
FLMutableDict_SetString(properties, FLSTR("language"), FLSTR("C"));
if(!CBLCollection_SaveDocument(collection, mutableDoc, &err)) {
    // Failed to save, do error handling as above
    return;
}

// Note const here, means readonly
const CBLDocument* docAgain = CBLCollection_GetDocument(collection, id, &err);
if(!docAgain) {
    // Failed to retrieve, do error handling as above.  NOTE: error code 0 simply means
    // the document does not exist.
    return;
}

// No copy this time, so no release later (notice it is not FLStringResult this time)
FLString retrievedID = CBLDocument_ID(docAgain);
FLDict retrievedProperties = CBLDocument_Properties(docAgain);
FLString retrievedLanguage = FLValue_AsString(FLDict_Get(retrievedProperties, FLSTR("language")));
printf("Document ID :: %.*s\n", (int)retrievedID.size, (const char *)retrievedID.buf);
printf("Learning %.*s\n", (int)retrievedLanguage.size, (const char *)retrievedLanguage.buf);

CBLDocument_Release(mutableDoc);
CBLDocument_Release(docAgain);

// Create a query to fetch documents of type SDK
int errorPos;
CBLQuery* query = CBLDatabase_CreateQuery(
    database,
    kCBLN1QLLanguage,
    FLSTR("SELECT * FROM _ WHERE type = \"SDK\""), &errorPos, &err);
if(!query) {
    // Failed to create query, do error handling as above
    // Note that errorPos will contain the position in the N1QL string
    // that the parse failed, if applicable
    return;
}

CBLResultSet* result = CBLQuery_Execute(query, &err);
if(!result) {
    // Failed to run query, do error handling as above
    return;
}

CBLResultSet_Release(result);
CBLQuery_Release(query);

// Create replicator to push and pull changes to and from the cloud
CBLCollectionConfiguration collectionConfig = {0};
collectionConfig.collection = collection;

CBLEndpoint* targetEndpoint = CBLEndpoint_CreateWithURL(FLSTR("ws://localhost:4984/getting-started-db"), &err);
if(!targetEndpoint) {
    // Failed to create endpoint, do error handling as above
    return;
}

CBLReplicatorConfiguration replConfig = {0};
replConfig.collections = &collectionConfig;
replConfig.collectionCount = 1;
replConfig.endpoint = targetEndpoint;

CBLAuthenticator* basicAuth = CBLAuth_CreatePassword(FLSTR("john"), FLSTR("pass"));
replConfig.authenticator = basicAuth;

CBLReplicator* replicator = CBLReplicator_Create(&replConfig, &err);
CBLAuth_Free(basicAuth);
CBLEndpoint_Free(targetEndpoint);
if(!replicator) {
    // Failed to create replicator, do error handling as above
    return;
}

// Assume a function like the following sample
//
// static void getting_started_change_listener(void* context, CBLReplicator* repl, const CBLReplicatorStatus* status) {
//     if(status->error.code != 0) {
//         printf("Error %d / %d\n", status->error.domain, status->error.code);
//     }
// }

CBLListenerToken* token = CBLReplicator_AddChangeListener(replicator, getting_started_change_listener, NULL);

CBLReplicator_Start(replicator, false);

// Later, stop and release the replicator

// When finished release resources ... eg
CBLListener_Remove(token);

stop_replicator(replicator);

CBLCollection_Release(collection);
CBLDatabase_Release(database);
```

## [](#related-content)Related Content

###### [](#)

How to . . .

* [Install](gs-install.md)
* [Build and Run](gs-build.md)

.

###### [](#-2)

Learn more . . .

* [Databases](database.md)
* [Documents](document.md)
* [Blobs](blob.md)
* [Remote Sync Gateway](replication.md)
* [Handling Data Conflicts](conflict.md)

.

###### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.