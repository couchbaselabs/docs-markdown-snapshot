---
title: Create Student and Course Records
description: Learn how to use the SDK to create student and course records.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/tutorials/pages/java-tutorial/create-records.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/cloud/tutorials/java-tutorial/create-records.html)

# Create Student and Course Records

> Learn how to use the SDK to create student and course records. 

## [](#prerequisites)Prerequisites

* You have created a Capella operational free tier cluster. For more information, see [Create and Deploy Your Free Tier Operational Cluster](../../get-started/create-account.md#getting-started).
* You have created the required bucket, scope, and collections. For more information, see [Implement the Data Model](../buckets-scopes-and-collections.md).
* You have installed the Java Software Development Kit (version 8, 11, 17, or 21).

  * The recommended version is the latest Java LTS release. Make sure to install the highest available patch for the LTS version.
* You have installed [Apache Maven](https://maven.apache.org/) (version 3+).
* You have connected the Java SDK to your free tier cluster. For more information, see [install-couchbase-java-sdk.adoc](#install-couchbase-java-sdk.adoc).

## [](#create-a-student-record)Create a Student Record

After connecting to your cluster, you can create a student record in the form of a JSON document inserted into the `student-record-collection`.

To create a student record:

1. In your `java` directory, create a new file called `InsertStudent.java`.
2. Paste the following code block into your `InsertStudent.java` file:  
```java  
import com.couchbase.client.java.Bucket;  
import com.couchbase.client.java.Cluster;  
import com.couchbase.client.java.Collection;  
import com.couchbase.client.java.Scope;  
import com.couchbase.client.java.json.JsonObject;  
import com.couchbase.client.java.ClusterOptions;  
import java.time.Duration;  
import java.time.LocalDate;  
import java.time.format.DateTimeFormatter;  
public class InsertStudent {  
    public static void main(String[] args) {  
        String connectionString = "<<connection-string>>"; // Replace this with Connection String  
        String username = "<<username>>"; // Replace this with username from cluster access credentials  
        String password = "<<password>>"; // Replace this with password from cluster access credentials  
          
        Cluster cluster = Cluster.connect(connectionString, ClusterOptions.clusterOptions(username, password)  
                    .environment(env -> env.applyProfile("wan-development"))  
        );  
        Bucket bucket = cluster.bucket("student-bucket");  
        bucket.waitUntilReady(Duration.ofSeconds(10));  
        Scope scope = bucket.scope("art-school-scope");  
        Collection student_records = scope.collection("student-record-collection");  
        // This `JsonObject` class creates and populates the student record.  
        JsonObject hilary = JsonObject.create()  
                .put("name", "Hilary Smith")  
                .put("date-of-birth",  
                        LocalDate.of(1980, 12, 21)  
                                .format(DateTimeFormatter.ISO_DATE));  
        // The `upsert` function inserts or updates documents in a collection.  
        // The first parameter is a unique ID for the document, similar to a primary key used in a relational database system.  
        // If the `upsert` call finds a document with a matching ID in the collection, it updates the document.  
        // If there is no matching ID, it creates a new document.  
        student_records.upsert("000001", hilary);  
        cluster.disconnect();  
    }  
}  
```
3. In the `InsertStudent.java` file, replace the `<<connection-string>>`, `<<username>>`, and `<<password>>` placeholders with your cluster’s public connection string, and the username and password from your cluster access credentials.
4. Open a terminal window and navigate to your `student` directory.
5. Run the command `mvn install` to pull in all the dependencies and rebuild your application.
6. Run the following command to insert the student record into the collection:  
```sh  
mvn exec:java -Dexec.mainClass="InsertStudent" -Dexec.cleanupDaemonThreads=false  
```
7. From the Capella UI, go to your free tier operational cluster and check the `student-record-collection` for the new student record you just added:

  1. Go to **Data Tools** **Documents**.
  2. Under **Get documents from**, select `student-bucket`, `art-school-scope`, and `student-record-collection`.
  3. Click **Get Documents**.

You should see the document in the list of documents in the `student-record-collection`.

## [](#create-course-records)Create Course Records

Creating course records is similar to creating student records. To create course records:

1. In your `java` directory, create a new file called `InsertCourses.java`.
2. Paste the following code block into your `InsertCourses.java` file:  
```java  
import com.couchbase.client.java.Bucket;  
import com.couchbase.client.java.Cluster;  
import com.couchbase.client.java.Collection;  
import com.couchbase.client.java.Scope;  
import com.couchbase.client.java.json.JsonObject;  
import com.couchbase.client.java.ClusterOptions;  
import java.time.Duration;  
public class InsertCourses {  
    public static void main(String[] args) {  
          
        String connectionString = "<<connection-string>>"; // Replace this with Connection String  
        String username = "<<username>>"; // Replace this with username from cluster access credentials  
        String password = "<<password>>"; // Replace this with password from cluster access credentials  
          
        Cluster cluster = Cluster.connect(connectionString, ClusterOptions.clusterOptions(username, password)  
                    .environment(env -> env.applyProfile("wan-development"))  
        );  
        Bucket bucket = cluster.bucket("student-bucket");  
        bucket.waitUntilReady(Duration.ofSeconds(10));  
        Scope scope = bucket.scope("art-school-scope");  
        // The code here is similar to creating a student record, but it writes to a different collection.  
        Collection course_records = scope.collection("course-record-collection");  
        addCourse(course_records, "ART-HISTORY-000001", "art history", "fine art", 100);  
        addCourse(course_records, "FINE-ART-000002", "fine art", "fine art", 50);  
        addCourse(course_records, "GRAPHIC-DESIGN-000003", "graphic design", "media and communication", 200);  
        cluster.disconnect();  
    }  
    private static void addCourse(Collection collection, String id, String name,  
                                  String faculty, int creditPoints) {  
        JsonObject course = JsonObject.create()  
                .put("course-name", name)  
                .put("faculty", faculty)  
                .put("credit-points", creditPoints);  
        collection.upsert(id, course);  
    }  
}  
```
3. In the `InsertCourses.java` file, replace the `<<connection-string>>`, `<<username>>`, and `<<password>>` placeholders with your cluster’s public connection string, and the username and password from your cluster access credentials.
4. Open a terminal window and navigate to your `student` directory.
5. Run the command `mvn install` to pull in all the dependencies and rebuild your application.
6. Run the following command to insert the student record into the collection:  
```sh  
mvn exec:java -Dexec.mainClass="InsertCourses" -Dexec.cleanupDaemonThreads=false  
```
7. From the Capella UI, go to your free tier operational cluster and check the `course-record-collection` for the new course records you just added.

If you come across errors in your console, see [Troubleshooting the Developer Tutorial](tutorial-troubleshooting.md).

## [](#next-steps)Next Steps

After adding course and student records to your cluster, you can [retrieve documents from your cluster](retrieving-documents.md) with SQL++.