---
title: Add Course Enrollments
description: Add enrollment information to the student records using the Couchbase SDK.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/tutorials/pages/java-tutorial/adding-course-enrollments.adoc
  xref: xref:server:tutorials:java-tutorial/adding-course-enrollments.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/tutorials/java-tutorial/adding-course-enrollments.html)

# Add Course Enrollments

> Add enrollment information to the student records using the Couchbase SDK. 

## [](#add-enrollment-details)Add Enrollment Details

To add enrollment details to a student record:

1. In your `java` directory, create a new file called `AddEnrollments.java`.
2. Paste the following code block into your `AddEnrollments.java` file:  
```java  
import com.couchbase.client.core.error.CouchbaseException;  
import com.couchbase.client.java.Bucket;  
import com.couchbase.client.java.Cluster;  
import com.couchbase.client.java.Collection;  
import com.couchbase.client.java.Scope;  
import com.couchbase.client.java.json.JsonArray;  
import com.couchbase.client.java.json.JsonObject;  
import com.couchbase.client.java.query.QueryOptions;  
import com.couchbase.client.java.query.QueryResult;  
import com.couchbase.client.java.query.QueryScanConsistency;  
import java.time.Duration;  
import java.time.LocalDate;  
import java.time.format.DateTimeFormatter;  
public class AddEnrollments {  
    public static void main(String[] args) {  
        // Calls `Cluster.connect` to create a channel to the named server and supplies your username and password to authenticate the connection.  
        Cluster cluster = Cluster.connect("localhost",  
                "username", "password");  
        // Retrieves the bucket you set up when you installed Couchbase Server.  
        Bucket bucket = cluster.bucket("student-bucket");  
        // Forces the application to wait until the bucket is ready.  
        bucket.waitUntilReady(Duration.ofSeconds(10));  
        // Retrieves the `art-school-scope` collection from the scope.  
        Scope scope = bucket.scope("art-school-scope");  
        Collection student_records = scope.collection("student-record-collection");  
        // Retrieves Hilary's student record, the `graphic design` course record, and the `art history` course record.  
        // Each method uses a SQL++ call to retrieve a single record from each collection.  
        JsonObject hilary = retrieveStudent(cluster,"Hilary Smith");  
        JsonObject graphic_design = retrieveCourse(cluster, "graphic design");  
        JsonObject art_history = retrieveCourse(cluster, "art history");  
        // Couchbase does not have a native date type, so the common practice is to store dates as strings.  
        String currentDate = LocalDate.now().format(DateTimeFormatter.ISO_DATE);  
        // Stores the `enrollments` inside the student record as an array.  
        // `JsonArray.create()` creates an empty list structure.  
        JsonArray enrollments = JsonArray.create();  
        // Adds two JSON elements to the `enrollments` array: the course that the enrollment relates to, and the date that the student enrolled in the course.  
        // To avoid repeating data all over the cluster, you store a reference to the course instead of the entire course record itself in this field.  
        // This means that you do not have to search through every single record if the course details change.  
        enrollments.add(JsonObject.create()  
                .put("course-id", graphic_design.getString("id"))  
                .put("date-enrolled", currentDate));  
        enrollments.add(JsonObject.create()  
                .put("course-id", art_history.getString("id"))  
                .put("date-enrolled", currentDate));  
        // Adds the `enrollments` array to Hilary's student record.  
        hilary.put("enrollments", enrollments);  
        // Commits the changes to the collection.  
        // The `upsert` function call takes the key of the record you want to insert or update and the record itself as parameters.  
        // If the `upsert` call finds a document with a matching ID in the collection, it updates the document.  
        // If there is no matching ID, it creates a new document.  
        student_records.upsert(hilary.getString("id"), hilary);  
        cluster.disconnect();  
    }  
    private static JsonObject retrieveStudent(Cluster cluster, String name) throws CouchbaseException {  
        QueryOptions studentQueryOptions = QueryOptions.queryOptions();  
        studentQueryOptions.parameters(JsonObject.create().put("name", name));  
        studentQueryOptions.scanConsistency(QueryScanConsistency.REQUEST_PLUS);  
        final QueryResult result = cluster.query("select META().id, src.* " +  
                        "from `student-bucket`.`art-school-scope`.`student-record-collection` src " +  
                        "where src.`name` = $name", studentQueryOptions);  
        return result.rowsAsObject().get(0);  
    }  
    private static JsonObject retrieveCourse(Cluster cluster, String course) throws CouchbaseException {  
        QueryOptions courseQueryOptions = QueryOptions.queryOptions();  
        courseQueryOptions.parameters(JsonObject.create().put("courseName", course));  
        courseQueryOptions.scanConsistency(QueryScanConsistency.REQUEST_PLUS);  
        final QueryResult result = cluster.query("select META().id, crc.* " +  
                        "from `student-bucket`.`art-school-scope`.`course-record-collection` crc " +  
                        "where crc.`course-name` = $courseName", courseQueryOptions);  
        return result.rowsAsObject().get(0);  
    }  
}  
```  
> [!NOTE]  
> Because this is a tutorial, you do not need to add an error check to make sure that your collection has returned an item. In a live application, though, error checks must be made to prevent errors and keep the application running.
3. Open a terminal window and navigate to your `student` directory.
4. Run the command `mvn install` to pull in all the dependencies and rebuild your application.
5. Run the following command to insert the student record into the collection:  
```sh  
mvn exec:java -Dexec.mainClass="AddEnrollments" -Dexec.cleanupDaemonThreads=false  
```
6. Go to your Couchbase cluster in your browser.
7. Go to the `student-record-collection` and click the **Edit** icon or the document ID to see the new information you just added to Hilary's student record.  
![Updated student record with course enrollment](../_images/updated-student-record.png)

If you come across errors in your console, see the [troubleshooting page](tutorial-troubleshooting.md).

## [](#next-steps)Next Steps

Now that you have finished following the Student Record System tutorial, you can explore more of Couchbase by checking out the rest of the [developer documentation](../../develop/intro.md).