---
title: Build and Run
description: Build and run a starter app to validate your install of Couchbase Lite on Java
pubDate: 2026-10-15T04:23:30.340Z
meta:
  component:
    title: Couchbase Lite
    version: "4.1"
antora:
  editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/4.1/modules/java/pages/gs-build.adoc
  xref: xref:couchbase-lite:java:gs-build.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/couchbase-lite/current/java/gs-build.html)

# Build and Run

> Description — _Build and run a starter app to validate your install of Couchbase Lite on Java_  
> _Abstract — This content provides sample code and instructions that enable you to test your Couchbase Lite for Java installation._  
> Related Content — [Install](gs-install.md) | [Prerequisites](gs-prereqs.md) | [Build and Run](gs-build.md) |

## [](#build-a-getting-started-app)Build a Getting Started App

This section explains how to validate your configured build environment by building a starter app that uses common Couchbase Lite features.

The GettingStarted app demonstrates how to use Couchbase Lite. Console and Web App versions are available.

Development-type Scenarios

* Desktop App
* Web App

> [!TIP]
> Make sure you added the Couchbase Lite dependency to your `build.gradle` file

Create, build, and run a new project using the following `GettingStarted.java` code:

```java

private void getStarted() throws CouchbaseLiteException, URISyntaxException {
    (1)
    // One-off initialization
    CouchbaseLite.init();
    System.out.println("CBL Initialized");

    (2)
    // Create a database
    Database database = new Database("mydb");
    System.out.println("Database created: mydb");

    (3)
    // Create a new collection (like a SQL table) in the database.
    Collection collection = database.createCollection("myCollection", "myScope");
    System.out.println("Collection created: " + collection);

    (4)
    // Create a new document (i.e. a record)
    // and save it in a collection in the database.
    MutableDocument mutableDoc = new MutableDocument()
        .setString("version", "2.0")
        .setString("language", "Java");
    collection.save(mutableDoc);

    (5)
    // Retrieve immutable document and log the database generated
    // document ID and some document properties
    Document document = collection.getDocument(mutableDoc.getId());
    if (document == null) {
        System.out.println("No such document :: " + mutableDoc.getId());
    }
    else {
        System.out.println("Document ID :: " + document.getId());
        System.out.println("Learning :: " + document.getString("language"));
    }

    (6)
    // Retrieve and update a document.
    document = collection.getDocument(mutableDoc.getId());
    if (document != null) {
        collection.save(document.toMutable().setString("language", "Kotlin"));
    }

    (7)
    // Create a query to fetch documents with language == "Kotlin"
    Query query = QueryBuilder.select(SelectResult.all())
        .from(DataSource.collection(collection))
        .where(Expression.property("language")
            .equalTo(Expression.string("Kotlin")));

    try (ResultSet rs = query.execute()) {
        System.out.println("Number of rows :: " + rs.allResults().size());
    }

    //  (8)
    // OPTIONAL -- if you have Sync Gateway Installed you can try replication too
    // Create a replicator to push and pull changes to and from the cloud.
    // Be sure to hold a reference somewhere to prevent the Replicator from being GCed
    if (SG_URI != null) { replicator = startRepl(SG_URI, collection); }
}

private Replicator startRepl(String uri, Collection collection) throws URISyntaxException {
    CollectionConfiguration collConfig = new CollectionConfiguration(collection)
        .setPullFilter((doc, flags) -> "Java".equals(doc.getString("language")));

    ReplicatorConfiguration replConfig = new ReplicatorConfiguration(
        Set.of(collConfig),
        new URLEndpoint(new URI(uri)))
        .setType(ReplicatorType.PUSH_AND_PULL)
        .setAuthenticator(new BasicAuthenticator("sync-gateway", "password".toCharArray()));

    Replicator repl = new Replicator(replConfig);

    // Listen to replicator change events.
    // Use `token.remove()` to stop the listener
    ListenerToken token = replicator.addChangeListener(change -> {
        System.out.println("Replicator state :: " + change.getStatus().getActivityLevel());
    });

    // Start replication.
    repl.start();

    return repl;
}
```

| **1** | Initialize the library                                                         |
| ----- | ------------------------------------------------------------------------------ |
| **2** | Create a database                                                              |
| **3** | Create a collection                                                            |
| **4** | Create a new document                                                          |
| **5** | Retrieve document and log its ID                                               |
| **6** | Retrieve the document as mutable and change the language to Kotlin and save it |
| **7** | Query the database output count and id to log                                  |
| **8** | Optionally, start a replication                                                |

When you run the app, the console displays the document ID and property. It also displays a query result showing the number of rows in the database.

This shows that the app persisted the document to the database.

See [About the Getting Started App](#about-the-getting-started-app) for more on the app itself.

This section explains how to configure a build project to create Couchbase Lite web apps using Gradle and IntelliJ IDEA.

**Steps**

1. Create a new project folder and add a `build.gradle` file similar to this one.  
```groovy  
include::example$GetStartedWS/build.gradle.sample  
```
2. Within IntelliJ IDEA, open the new project folder.  
If you do not have auto-import enabled, accept the **Import from Gradle** prompt.
3. Create a Java class `DBManager` using this code:  
```java  
(1)  
// One-off initialization  
private void init() {  
    CouchbaseLite.init();  
}  
(2)  
// Create a database  
public Database createDb(String dbName) throws CouchbaseLiteException {  
    return new Database(dbName);  
}  
(3)  
// Create a new named collection (like a SQL table)  
// in the database's default scope.  
public Collection createCollection(Database database, String collName) throws CouchbaseLiteException {  
    return database.createCollection(collName);  
}  
(4)  
// Create a new document (i.e. a record)  
// and save it in a collection in the database.  
public String createDoc(Collection collection) throws CouchbaseLiteException {  
    MutableDocument mutableDocument = new MutableDocument()  
        .setFloat("version", 2.0f)  
        .setString("language", "Java");  
    collection.save(mutableDocument);  
    return mutableDocument.getId();  
}  
(5)  
// Retrieve immutable document and log the database generated  
// document ID and some document properties  
public Document retrieveDoc(Collection collection, String docId) throws CouchbaseLiteException {  
    return collection.getDocument(docId);  
}  
(6)  
// Retrieve and update a document.  
public void updateDoc(Collection collection, String docId) throws CouchbaseLiteException {  
    Document document = collection.getDocument(docId);  
    if (document != null) {  
        collection.save(  
            document.toMutable().setString("language", "Kotlin"));  
    }  
}  
(7)  
// Create a query to fetch documents with language == Kotlin.  
public List<Map<String, Object>> queryDocs(Collection collection) throws CouchbaseLiteException {  
    Query query = QueryBuilder.select(SelectResult.all())  
        .from(DataSource.collection(collection))  
        .where(Expression.property("language").equalTo(Expression.string("Kotlin")));  
    List<Map<String, Object>> results = new ArrayList<>();  
    try (ResultSet rs = query.execute()) {  
        for (Result result: rs) { results.add(result.toMap()); }  
    }  
    return results;  
}  
(8)  
// OPTIONAL -- if you have Sync Gateway Installed you can try replication too.  
// Create a replicator to push and pull changes to and from the cloud.  
// Be sure to hold a reference somewhere to prevent the Replicator from being GCed  
public Replication startReplicator(Collection collection, ReplicatorChangeListener listener)  
    throws URISyntaxException {  
    CollectionConfiguration collConfig = new CollectionConfiguration(collection)  
        .setPullFilter((doc, flags) -> "Java".equals(doc.getString("language")));  
    ReplicatorConfiguration replConfig =  
        new ReplicatorConfiguration(  
            Set.of(collConfig),  
            new URLEndpoint(new URI("ws://localhost:4984/getting-started-db")))  
            .setType(ReplicatorType.PUSH_AND_PULL)  
            .setAuthenticator(new BasicAuthenticator("sync-gateway", "password".toCharArray()));  
    Replicator replicator = new Replicator(replConfig);  
    // Listen to replicator change events.  
    // Use `token.remove()` to stop the listener  
    ListenerToken token = replicator.addChangeListener(listener);  
    // Start replication.  
    replicator.start();  
    return new Replication(replicator, token);  
}  
```
4. Create a Servlet similar to the one found in the example `GettingStartedServlet`.
5. Create an `index.html` file in `src/main/webapp` with the following content:  
```html  
include::example$GetStartedWS/src/main/webapp/index.html  
```
6. Create a `showDbItems.jsp` file in `src/main/webapp` with the following content:  
```html  
include::example$GetStartedWS/src/main/webapp/showDbItems.jsp  
```
7. Build, deploy, and run the app using `jettyRun`  
![GradleMenuWebApp](_images/GradleMenuWebApp.png)  

  1. Point your browser to: `localhost:8080/`  
  This opens the browser at your `index.html` page.
  2. Select the **here** link  
  This launches the servlet and displays the results in `showDbItems.jsp`.

## [](#about-the-getting-started-app)About the Getting Started App

The GettingStarted app does the following:

* Create a database  
The app creates its database in the `/getting-started.cblite2` directory relative to its root location when run. See [Finding a Database File](database.md#lbl-find-db-loc).  
> [!TIP]  
> Explicitly state your required database location when creating your database. For more information, see [Finding a Database File](database.md#lbl-find-db-loc).
* Add content to the DB
* Run a query counting the DB rows
* Start a one-shot, bidirectional replication using Sync Gateway and Couchbase Server
* Produce a report on the DB contents  
![cblOutput](_images/cblOutput.png)

> [!NOTE]
> Before starting your app, make sure you have started both your Couchbase Server and Sync Gateway instances.