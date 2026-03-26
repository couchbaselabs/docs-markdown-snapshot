---
title: Creating the Students Collection
description: Following on from
  xref:java-tutorial/install-couchbase-java-sdk.adoc[], this tutorial will show
  you how to connect to Couchbase and add records to the database using the SDK.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/tutorials/pages/java-tutorial/creating-the-students-collection.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:7.2@server:tutorials:java-tutorial/creating-the-students-collection.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/tutorials/java-tutorial/creating-the-students-collection.html)

# Creating the Students Collection

> Following on from [Installing the Couchbase Java SDK](install-couchbase-java-sdk.md), this tutorial will show you how to connect to Couchbase and add records to the database using the SDK. 

## [](#introduction)Introduction

Working with any database SDK usually involves the following operations:

1. Connect to the database
2. Carry out CRUD\[[1](#%5Ffootnotedef%5F1 "View footnote.")\] operations
3. Disconnect from the database (important for resource cleanup)

Fortunately, the Couchbase SDK follows the same pattern, so the first thing you're going to do is write the code to connect to your document store.

## [](#connecting-to-the-database)Connecting to the database

In the [Installing the Couchbase Java SDK](install-couchbase-java-sdk.md) tutorial, you created a directory structure to hold your application. Create the file `student.java` in the `java` directory as shown below.

📂 ~ (your home directory)
  📂 student
    📃 pom.xml
    📂 src
      📂 main
        📂 java
          📃 ConnectStudent.java ⬅ here!

Add the following content to the `ConnectStudent.java` file.

```java
Unresolved include directive in modules/tutorials/pages/java-tutorial/creating-the-students-collection.adoc - include::java-sdk:student:example$ConnectStudent.java[]
```

If you're familiar with the JDBC API then connecting to a Couchbase server is not that different:

| **1** | A call to Cluster.connect creates a channel to the named server (localhost running on your local machine in this case), supplying your username and password to authenticate the connection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | The retrieved cluster is used to retrieve the bucket set up in [Install or provision the Couchbase server](../install-couchbase-server.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **3** | As discussed earlier in [Couchbase Tutorial: A Student Record System](../couchbase-tutorial-student-records.md), Couchbase has been designed from the ground up to be scalable and performant, and an important part of this design is the architecture behind the APIs. Most of the APIs are non-blocking, which means that once you call them, your program is free to carry on and do other things while the called function executes. Once the function has finished, it sends a notification to its caller, which will then process the output of the call.Now this usually works very well in practice, but in our simple example there is a problem: after we make the call to cluster.bucket, the program will carry on without waiting for the bucket retrieval to be complete. This means we're now trying to retrieve the scope from a bucket object that hasn't been fully initialised.This is where the waitUntilReady call comes in. This will force the program to wait until the bucket object is fully prepared. |
| **4** | Retrieves the art-school-scope from the bucket.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **5** | Retrieves the student collection from the scope.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **6** | The next line is just a check to make sure we have connected and retrieved the collection when the program is run. You can see the output by running it through maven:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **7** | And as with all database systems, it's good practise to disconnect from the Couchbase cluster once you've finished working with it.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

```sh
mvn exec:java -Dexec.mainClass="ConnectStudent" -Dexec.cleanupDaemonThreads=false
```

Somewhere in the output, you'll find the line containing the name of the collection you've successfully retrieved:

![Console showing successful connection to server](../_images/connect-to-cluster-console-output.png) 

> [!TIP]
> As an experiment, try commenting out the `bucket.waitUntilReady` call, then run the program again. What happens?

Okay, so you've connected to the cluster and retrieved your collection. Unfortunately, there's nothing in there to see at the moment, so the next thing to do is create a few records.

## [](#populating-the-student-collection)Populating the student collection

Remember that Couchbase is a [document store](../couchbase-tutorial-student-records.md#database-design), not a relational database in the traditional sense. Rather than storing data in tables, you're going to create a document in JSON and insert it into the `student-record-collection`. Here's Hilary Smith's student record (minus the enrollment details – we'll come to that later):

```json
{
  "name": "Hilary Smith",
  "date-of-birth": "21-12-1980"
}
```

Start by creating the file `InsertStudent.java` in the `java` directory:

```java
Unresolved include directive in modules/tutorials/pages/java-tutorial/creating-the-students-collection.adoc - include::java-sdk:student:example$InsertStudent.java[]
```

| **1** | Up to this point, it's pretty much the same as the ConnectStudent class: mainly the boilerplate code to connect to the cluster and access the collection.                                                                                                                                                                                                                                                                                                                                            |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | Since Couchbase is primarily a store for JSON documents, it makes sense to include a whole class of functionality for creating and manipulating data in the JSON format. In this case, use the JsonObject class to create and populate Hilary's student record. JSON doesn't have its own date type, and so Couchbase doesn't have a native data type either. The recommended way of dealing with dates is to store them as [ISO-8601](https://en.wikipedia.org/wiki/ISO%5F8601)\-formatted strings. |
| **3** | The upsert function is used to insert or update documents in a collection. The first parameter is a unique identifier for the document (much like the primary key used in relational database systems). If upsert call finds a document with a matching identifier in the collection, then the document is updated. If there is no existing identifer, then a new record is created.                                                                                                                 |

When you run the program:

```sh
mvn exec:java -Dexec.mainClass="InsertStudent" -Dexec.cleanupDaemonThreads=false
```

nothing much happens. You can return to the Couchbase administrator's console and examine the contents of the `student-record-collection`.

![Student record showing in the web console](../_images/hilarys-record-in-admin-console.png) 

And there it is: a single document with an id of `000001` belonging to Hilary Smith.

Before carrying on to the next section, change your program so you can add a student record for `Ashley Jones`.

## [](#next-steps)Next steps

In the next section, you're going to build another short program for [populating the course collection](creating-the-courses-collection.md) .

---

[1](#%5Ffootnoteref%5F1). Create Read Update Delete