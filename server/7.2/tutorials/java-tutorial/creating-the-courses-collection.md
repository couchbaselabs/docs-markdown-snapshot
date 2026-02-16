[View original HTML](/server/7.2/tutorials/java-tutorial/creating-the-courses-collection.html)

> Your first application created a single student record for the student collection. In this part, you’re going to populate the course collection. 

## [](#populating-the-course-details-collection)Populating the course details collection

You can use the same technique to build a store for the courses. Here’s a quick reminder of the course document structure:

* art history
* graphic design
* fine art

```json
{
  "course-name": "art history",
  "faculty": "fine art",
  "credit-points" : 100
}
```

```json
{
  "course-name": "graphic design",
  "faculty": "media and communication",
  "credit-points" : 200
}
```

```json
{
  "course-name": "fine art",
  "faculty": "fine art",
  "credit-points" : 50
}
```

The code should be familiar to you; there’s not much difference between writing to the course collection and writing to the student collection; you just have more records to deal with:

```java
Unresolved include directive in modules/tutorials/pages/java-tutorial/creating-the-courses-collection.adoc - include::java-sdk:student:example$InsertCourses.java[]
```

| **1** | Note that you’re now writing to a different collection. |
| ----- | ------------------------------------------------------- |

|  | Make sure that you’ve created the course-collection in the admin console before you attempt to run the program. |
|  | --------------------------------------------------------------------------------------------------------------- |

You can use maven to run the application:

```sh
mvn exec:java -Dexec.mainClass="InsertCourses" -Dexec.cleanupDaemonThreads=false
```

Use the admin console to make sure the documents have been created in the correct collection.

![Console showing the courses collection](../_images/new-course-collection.png) 

## [](#next-steps)Next steps

So you’ve created a cluster, a bucket, a scope and two collections. You’ve also populated your collections with documents. Well, a database isn’t much use until we can retrieve information from it, which is what you’re going to take a look at in the [next part](retrieving-documents.md).