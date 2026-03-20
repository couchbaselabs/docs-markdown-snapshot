---
title: Adding Course Enrollments
description: In this section, you're going to add enrollment details to the
  student records using the Couchbase SDK
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/tutorials/pages/java-tutorial/adding-course-enrollments.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:tutorials:java-tutorial/adding-course-enrollments.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/tutorials/java-tutorial/adding-course-enrollments.html)

# Adding Course Enrollments

> In this section, you’re going to add enrollment details to the student records using the Couchbase SDK 

## [](#introduction)Introduction

A quick recap: here’s the structure of our document store:

![student-document-database-design](../_images/student-document-database-design-f437e457810966f04ff9fc2bc2ecdbb5327ce938.svg) 

At this point, you should have a student records for Hilary Smith and Ashley Jones, along with records for three courses. You’re now going to write a short program that will add enrollment details to the student records.

You’re going to create another program in the same working directory that will bring together all the concepts you’ve learned so far.

At the end of the exercise, you should have changed Hilary’s student record to store the enrollment details in an array:

```json
{
  "name": "Hilary Smith",
  "enrollments": [
    {
      "course-id": "GRAPHIC-DESIGN-000003",
      "date-enrolled": "2021-10-14"
    },
    {
      "course-id": "ART-HISTORY-000001",
      "date-enrolled": "2021-10-14"
    }
  ],
  "id": "000001",
  "date-of-birth": "1980-12-21"
}
```

So, let’s begin with the Java program that will change Hilary’s record.

```java
Unresolved include directive in modules/tutorials/pages/java-tutorial/adding-course-enrollments.adoc - include::java-sdk:student:example$AddEnrollments.java[]
```

| **1**  | As you’ll remember from our [first example](creating-the-students-collection.md#connecting-to-the-database), the application first has to connect to the Couchbase cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2**  | Then it picks up the correct Bucket from the cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **3**  | Do you remember why we need this waitUntilReady function is needed when connecting to the server? Answer As discussed earlier in [Couchbase Tutorial: A Student Record System](../couchbase-tutorial-student-records.md), Couchbase has been designed from the ground up to be scalable and performant, and an important part of this design is the architecture behind the APIs. Most of the APIs are non-blocking, which means that once you call them, your program is free to carry on and do other things while the called function executes.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **4**  | Here again, we pick up the student collection from the art-school-scope; you’ll need it later to change Hilary’s record and write it back to the collection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **5**  | There are three method calls here: Retrieve Hilary’s student record. Retrieve the graphic design course record. Retrieve the art history course record. Each method uses a SQL++ call to retrieve a single record from its respective collection. This is just a demonstration, so there is no error checking to ensure that an item from the collection has been returned. In a live system, checks would have to be made to prevent possible errors while the program is running.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **6**  | Remember that Couchbase doesn’t have a native date type, so it’s common practice to store the dates as strings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **7**  | The enrollments inside the student record are stored as an array; since JSON is the native data format for Couchbase, it’s not surprising that each SDK has a host of functions for processing data in JSON. In this case, the call JsonArray.create() will create an empty list structure.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **8**  | Now JSON elements are added to the enrollments array. Looking back at the [data structure](#enrollments-structure) for enrollments, we need store just two items: the course that the enrollment relates to, and the date the student enrolled. enrollments.add(JsonObject.create().put("course-id", graphic\_design.getString("id"))     .put("date-enrolled", currentDate)); The course-id uses the id of the course record retrieved from the database. We could, of course, store the whole record in this field. Why _wouldn’t_ we want to do that? Answer This goes back to our relational model, and the idea of normalising the data model so that we don’t have repeating data items all over the place. Here, you’re just storing a reference to the course, not the course record itself. So if the course details change (such as the number of credit points assigned to it), then you don’t have to search through every single record that includes its own version. |
| **9**  | The array of enrollments is built, so now you add them to Hilary’s record. This is where the document database model shines; there is no need to change a database schema and rebuild the database. Just add the data and you’re done.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **10** | Finally, the changes need to be committed to the collection. For this, use the upsert function, which takes the key of the record you wish to insert or update and the record itself as parameters. If they key exists in the collection then the record is updated. If the key does not exist then it’s a fresh document, so the item is inserted.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

As always, use maven to run the program.

```sh
mvn exec:java -Dexec.mainClass="AddEnrollments" -Dexec.cleanupDaemonThreads=false
```

And check your results in administrator console.

## [](#great-job)Great Job!

You’ve reached the end of the beginners' tutorial. You can explore the documentation site to learn more about Couchbase.