---
title: Build and Run
description: Build and run a starter app to validate your install of Couchbase
  Lite on Android
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.2/modules/android/pages/gs-build.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:3.2@couchbase-lite:android:gs-build.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/3.2/android/gs-build.html)

# Build and Run

> Description — _Build and run a starter app to validate your install of Couchbase Lite on Android_  
> _Abstract — This content provides sample code and instructions that enable you to test your Couchbase Lite for android installation._  

## [](#introduction)Introduction

The Getting Started app is a very basic Android app that uses a database manager singleton.

You can access the `GettingStarted` project on github here:  
[Kotlin](https://github.com/couchbase/docs-couchbase-lite/tree/release/3.1/modules/android/examples/GetStartedKotlin) | [Java](https://github.com/couchbase/docs-couchbase-lite/tree/release/3.1/modules/android/examples/GetStartedJava)

Quick Steps

1. Get the project and open it in Android Studio: [Kotlin](https://github.com/couchbase/docs-couchbase-lite/tree/release/3.1/modules/android/examples/GetStartedKotlin) | [Java](https://github.com/couchbase/docs-couchbase-lite/tree/release/3.1/modules/android/examples/GetStartedJava)
2. Build it
3. Run it
4. Push the "Run it!" Button
5. That's it.

If you had problems, or just want more information on the app, there's more below.

![getstarted output ktx](../_images/getstarted-output-ktx.png) 

Figure 1\. Logcat Output from Android Studio

## [](#getting-started-app)Getting Started App

The Getting Started app shows examples of the essential Couchbase for Android CRUD operations, including:

* Initialize the library
* Create database
* Create collection
* Create a document
* Retrieve a document
* Update a document
* Query documents
* Create and run a replicator

Whilst no exemplar of a real application, it will give you a good idea how to get started using Couchbase Lite.

## [](#add-the-app-to-your-own-project)Add the App to Your Own Project

1. Create a new 'empty activity' project in Android Studio
2. Create a new Application class, similar to the GettingStartedApplication class
3. Copy the DBManager class to your project
4. Create a ViewModel and an Activity, like the ones in the sample
5. Build and run.  
You should be able to create a document and persist it to the database.

### [](#sample-code-in-detail)Sample Code in Detail

* Kotlin
* Java

```Kotlin

    (1)
    // One-off initialization
    private fun init(context: Context) {
        CouchbaseLite.init(context)
        Log.i(TAG, "CBL Initialized")

    }

    (2)
    // Create a database
    fun createDb(dbName: String) {
        database = Database(dbName)
        Log.i(TAG, "Database created: $dbName")
    }

    (3)
    // Create a new named collection (like a SQL table)
    // in the database's default scope.
    fun createCollection(collName: String) {
        collection = database!!.createCollection(collName)
        Log.i(TAG, "Collection created: $collection")
    }

    (4)
    // Create a new document (i.e. a record)
    // and save it in a collection in the database.
    fun createDoc(): String {
        val mutableDocument = MutableDocument()
            .setFloat("version", 2.0f)
            .setString("language", "Java")
        collection?.save(mutableDocument)
        return mutableDocument.id
    }

    (5)
    // Retrieve immutable document and log the database generated
    // document ID and some document properties
    fun retrieveDoc(docId: String) {
        collection?.getDocument(docId)
            ?.let {
                Log.i(TAG, "Document ID :: ${docId}")
                Log.i(TAG, "Learning :: ${it.getString("language")}")
            }
            ?: Log.i(TAG, "No such document :: $docId")
    }

    (6)
    // Retrieve immutable document and update `language` property
    // document ID and some document properties
    fun updateDoc(docId: String) {
        collection?.getDocument(docId)?.let {
            collection?.save(
                it.toMutable().setString("language", "Kotlin")
            )
        }
    }

    (7)
    // Create a query to fetch documents with language == Kotlin.
    fun queryDocs() {
        val coll = collection ?: return
        val query: Query = QueryBuilder.select(SelectResult.all())
            .from(DataSource.collection(coll))
            .where(Expression.property("language").equalTo(Expression.string("Kotlin")))
        query.execute().use { rs ->
            Log.i(TAG, "Number of rows :: ${rs.allResults().size}")
        }
    }

    (8)
    // OPTIONAL -- if you have Sync Gateway Installed you can try replication too.
    // Create a replicator to push and pull changes to and from the cloud.
    // Be sure to hold a reference to the Replicator to prevent it from being GCed
    fun replicate(uri: String): Flow<ReplicatorChange>? {
        val coll = collection ?: return null

        val collConfig = CollectionConfiguration()
            .setPullFilter { doc, _ -> "Java" == doc.getString("language") }

        val repl = Replicator(
            ReplicatorConfigurationFactory.newConfig(
                target = URLEndpoint(URI(uri)),
                collections = mapOf(setOf(coll) to collConfig),
                type = ReplicatorType.PUSH_AND_PULL,
                authenticator = BasicAuthenticator("sync-gateway", "password".toCharArray())
            )
        )

        // Listen to replicator change events.
        val changes = repl.replicatorChangesFlow()

        // Start replication.
        repl.start()
        replicator = repl

        return changes
    }
```

```Java

    (1)
    // One-off initialization
    private void init() {
        CouchbaseLite.init(GettingStartedApplication.getAppContext());
        Log.i(TAG, "CBL Initialized");
    }

    (2)
    // Create a database
    public void createDb(String dbName) throws CouchbaseLiteException {
        database = new Database(dbName);
        Log.i(TAG, "Database created: " + dbName);
    }

    (3)
    // Create a new named collection (like a SQL table)
    // in the database's default scope.
    public void createCollection(String collName) throws CouchbaseLiteException {
        collection = database.createCollection(collName);
        Log.i(TAG, "Collection created: " + collection);
    }

    (4)
    // Create a new document (i.e. a record)
    // and save it in a collection in the database.
    public String createDoc() throws CouchbaseLiteException {
        MutableDocument mutableDocument = new MutableDocument()
            .setFloat("version", 2.0f)
            .setString("language", "Java");
        collection.save(mutableDocument);
        return mutableDocument.getId();
    }

    (5)
    // Retrieve immutable document and log the database generated
    // document ID and some document properties
    public void retrieveDoc(String docId) throws CouchbaseLiteException {
        Document document = collection.getDocument(docId);
        if (document == null) {
            Log.i(TAG, "No such document :: " + docId);
        }
        else {
            Log.i(TAG, "Document ID :: " + document.getId());
            Log.i(TAG, "Learning :: " + document.getString("language"));
        }
    }

    (6)
    // Retrieve and update a document.
    public void updateDoc(String docId) throws CouchbaseLiteException {
        Document document = collection.getDocument(docId);
        if (document != null) {
            collection.save(
                document.toMutable().setString("language", "Kotlin"));
        }
    }

    (7)
    // Create a query to fetch documents with language == Kotlin.
    public void queryDocs() throws CouchbaseLiteException {
        Query query = QueryBuilder.select(SelectResult.all())
            .from(DataSource.collection(collection))
            .where(Expression.property("language").equalTo(Expression.string("Kotlin")));

        try (ResultSet rs = query.execute()) {
            Log.i(TAG, "Number of rows :: " + rs.allResults().size());
        }
    }

    (8)
    // OPTIONAL -- if you have Sync Gateway Installed you can try replication too.
    // Create a replicator to push and pull changes to and from the cloud.
    // Be sure to hold a reference somewhere to prevent the Replicator from being GCed
    public ListenerToken replicate(String uri, ReplicatorChangeListener listener) throws URISyntaxException {
        CollectionConfiguration collConfig = new CollectionConfiguration()
            .setPullFilter((doc, flags) -> "Java".equals(doc.getString("language")));

        ReplicatorConfiguration replConfig =
            new ReplicatorConfiguration(
                new URLEndpoint(new URI(uri)))
                .addCollection(collection, collConfig)
                .setType(ReplicatorType.PUSH_AND_PULL)
                .setAuthenticator(new BasicAuthenticator("sync-gateway", "password".toCharArray()));

        replicator = new Replicator(replConfig);

        // Listen to replicator change events.
        // Use `token.remove()` to stop the listener

        ListenerToken token = replicator.addChangeListener(listener);

        // Start replication.
        replicator.start();

        return token;
    }
```

| **1** | Initialize the Library                                                        |
| ----- | ----------------------------------------------------------------------------- |
| **2** | Create a database                                                             |
| **3** | Create a collection                                                           |
| **4** | Create a new document                                                         |
| **5** | Retrieve document from the database collection and log it                     |
| **6** | Retrieve the document as mutable, change the language to Kotlin and update it |
| **7** | Query the collection for documents with language == "Java" and log the count  |
| **8** | Optionally, initiate a replication                                            |

## [](#snags-and-pitfalls)Snags and Pitfalls

Mostly around Gradle and versions. You may find you need to change IDE Build Tools settings to use Java 11 for Gradle, for instance.

Using this app with Sync Gateway and Couchbase Server obviously requires you have, or install, working versions of both. See also — [Install Sync Gateway](#sync-gateway::get-started-install.adoc)

## [](#minification)Minification

An application that enables minification must ensure that certain pieces of Couchbase Lite library code are not changed — see [Example 1](#ruleset) for a near-minimal rule set that retains the needed code:

Example 1\. Ruleset

```Kotlin
-keep class com.couchbase.lite.ConnectionStatus { <init>(...); }
-keep class com.couchbase.lite.LiteCoreException { static <methods>; }
-keep class com.couchbase.lite.internal.replicator.CBLTrustManager {
    public java.util.List checkServerTrusted(java.security.cert.X509Certificate[], java.lang.String, java.lang.String);
}
-keep class com.couchbase.lite.internal.ReplicationCollection {
    static <methods>;
    <fields>;
}
-keep class com.couchbase.lite.internal.core.C4* {
    static <methods>;
    <fields>;
    <init>(...);
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
* [Blobs](blob.md)
* [Remote Sync Gateway](replication.md)
* [Handling Data Conflicts](conflict.md)

.

###### [](#-3)

Dive Deeper . . .

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Tutorials](https://docs.couchbase.com/tutorials/)

.