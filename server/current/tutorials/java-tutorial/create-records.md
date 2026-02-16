[View original HTML](/server/current/tutorials/java-tutorial/create-records.html)

> Use the SDK to create student and course records. 

## [](#create-a-student-record)Create a Student Record

After connecting to the cluster, you can create a student record in the form of a JSON document inserted into the `student-record-collection`.

To create a student record:

1. In your `java` directory, create a new file called `InsertStudent.java`.
2. Paste the following code block into your `InsertStudent.java` file:  
```java  
import com.couchbase.client.java.Bucket;  
import com.couchbase.client.java.Cluster;  
import com.couchbase.client.java.Collection;  
import com.couchbase.client.java.Scope;  
import com.couchbase.client.java.json.JsonObject;  
import java.time.Duration;  
import java.time.LocalDate;  
import java.time.format.DateTimeFormatter;  
public class InsertStudent {  
    public static void main(String[] args) {  
        Cluster cluster = Cluster.connect("localhost",  
                "username", "password");  
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
3. Open a terminal window and navigate to your `student` directory.
4. Run the command `mvn install` to pull in all the dependencies and rebuild your application.
5. Run the following command to insert the student record into the collection:  
```sh  
mvn exec:java -Dexec.mainClass="InsertStudent" -Dexec.cleanupDaemonThreads=false  
```
6. Go to your Couchbase cluster in your browser and check the `student-record-collection` for the new student record you just added:

  1. Go to **Documents** **Workbench**.
  2. Under **Keyspace**, select `student-bucket`, `art-school-scope`, and `student-record-collection`.  
  ![Student added to the student-record-collection in the cluster](../_images/new-student-record.png)

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
import java.time.Duration;  
public class InsertCourses {  
    public static void main(String[] args) {  
        Cluster cluster = Cluster.connect("localhost",  
                "username", "password");  
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
3. Open a terminal window and navigate to your `student` directory.
4. Run the command `mvn install` to pull in all the dependencies and rebuild your application.
5. Run the following command to insert the student record into the collection:  
```sh  
mvn exec:java -Dexec.mainClass="InsertCourses" -Dexec.cleanupDaemonThreads=false  
```
6. Go to your Couchbase cluster in your browser and check the `course-record-collection` for the new course records you just added.  
![Courses added to the course-record-collection in the cluster](../_images/new-course-records.png)

If you come across errors in your console, see the [troubleshooting page](tutorial-troubleshooting.md).

## [](#next-steps)Next Steps

After creating student and course records, you can [retrieve information from your cluster](retrieving-documents.md).