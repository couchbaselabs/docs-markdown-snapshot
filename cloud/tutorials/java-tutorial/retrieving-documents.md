---
title: Retrieve Records
description: Retrieve records or documents from your collections using SQL++,
  Couchbase's SQL-based query language.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/tutorials/pages/java-tutorial/retrieving-documents.adoc
pubDate: 2026-06-25T05:47:47.215Z
link: xref:cloud:tutorials:java-tutorial/retrieving-documents.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/tutorials/java-tutorial/retrieving-documents.html)

# Retrieve Records

> Retrieve records or documents from your collections using SQL++, Couchbase's SQL-based query language. You can retrieve your records using the [query editor](#retrieve-with-query-editor) or the [SDK](#retrieve-with-sdk). 

## [](#prerequisites)Prerequisites

* You have created a Capella operational free tier cluster. For more information, see [Create and Deploy Your Free Tier Operational Cluster](../../get-started/create-account.md#getting-started).
* You have created the required bucket, scope, and collections. For more information, see [Implement the Data Model](../buckets-scopes-and-collections.md).
* You have installed the Java Software Development Kit (version 8, 11, 17, or 21).

  * The recommended version is the latest Java LTS release. Make sure to install the highest available patch for the LTS version.
* You have installed [Apache Maven](https://maven.apache.org/) (version 3+).
* You have connected the Java SDK to your free tier cluster. For more information, see [Set Up and Connect the Couchbase Java SDK](install-couchbase-java-sdk.md).
* You have created student and course records on your cluster. For more information, see [Create Student and Course Records](create-records.md).

## [](#retrieve-with-query-editor)With the Query Editor

To retrieve the records with the query editor, you must first define an index.

### [](#define-an-index)Define an Index

Before you can retrieve your records with the query editor, you must first define an index in your bucket. The index helps your cluster find specific data when you run a query.

To define an index:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for your free cluster.
2. Click the name of your free tier operational cluster.
3. Go to **Data Tools** **Query**.
4. [Set your bucket and scope context](../../clusters/query-service/query-workbench.md#specify-bucket-and-scope-context) to the `student-bucket` and `art-school-scope`.
5. Enter the following query into your query editor:  
```sqlpp  
create primary index course_idx on `course-record-collection`  
```
6. Click **Run** to create a single index called `course_idx` in your `course-record-collection`.

### [](#retrieve-your-records)Retrieve Your Records

You can use the query editor to retrieve all course records at once, or narrow your search to retrieve records based on specific criteria.

#### [](#retrieve-all-course-records)Retrieve All Course Records

To retrieve all of your course records:

1. Enter the following query into your query editor:  
```sqlpp  
select crc.* from `course-record-collection` crc  
```
2. Click **Run** to retrieve all course records.  
```json  
[  
  {  
    "course-name": "art history",  
    "credit-points": 100,  
    "faculty": "fine art"  
  },  
  {  
    "course-name": "fine art",  
    "credit-points": 50,  
    "faculty": "fine art"  
  },  
  {  
    "course-name": "graphic design",  
    "credit-points": 200,  
    "faculty": "media and communication"  
  }  
]  
```

#### [](#retrieve-course-records-with-less-than-200-credits)Retrieve Course Records with Less than 200 Credits

You can expand your query to narrow your search further. To retrieve only courses with less than 200 `credit-points`:

1. Enter the following query into your query editor:  
```sqlpp  
select crc.* from `course-record-collection` crc where crc.`credit-points` < 200  
```
2. Click **Run** to retrieve all courses with less than 200 credits.  
```json  
[  
  {  
    "course-name": "art history",  
    "credit-points": 100,  
    "faculty": "fine art"  
  },  
  {  
    "course-name": "fine art",  
    "credit-points": 50,  
    "faculty": "fine art"  
  }  
]  
```

### [](#retrieve-record-ids)Retrieve Record IDs

The `id` field is not automatically returned when you retrieve all of your course information.

The `id` is part of a document's meta structure, and to retrieve it you must adjust your SQL++ query and run it again:

1. Enter the following query into your query editor:  
```sqlpp  
select META().id, crc.* from `course-record-collection` crc where crc.`credit-points` < 200  
```  
The `META()` function call returns any property contained inside the document's metadata, including the ID.
2. Click **Run** to retrieve course records and their IDs.  
```json  
[  
  {  
    "course-name": "art history",  
    "credit-points": 100,  
    "faculty": "fine art",  
    "id": "ART-HISTORY-000001"  
  },  
  {  
    "course-name": "fine art",  
    "credit-points": 50,  
    "faculty": "fine art",  
    "id": "FINE-ART-000002"  
  }  
]  
```

## [](#retrieve-with-sdk)With the SDK

You can also use SQL++ queries to retrieve your records with the SDK. Unlike the query editor, you must include the name of the bucket and the scope to fully qualify the name of the collection in the SQL++ statement in your application. For example:

```sqlpp
select crc.* from `student-bucket`.`art-school-scope`.`course-record-collection` crc
```

### [](#retrieve-your-records-2)Retrieve Your Records

You can use the SDK to retrieve all course records at once, or narrow your search to retrieve records based on specific criteria.

#### [](#retrieve-all-course-records-2)Retrieve All Course Records

To retrieve all of your course records using the Java SDK:

1. In your `java` directory, create a new file called `ArtSchoolRetriever.java`.
2. Paste the following code block into your `ArtSchoolRetriever.java` file:  
```java  
import com.couchbase.client.core.error.CouchbaseException;  
import com.couchbase.client.java.Cluster;  
import com.couchbase.client.java.json.JsonObject;  
import com.couchbase.client.java.query.QueryResult;  
import com.couchbase.client.java.ClusterOptions;  
public class ArtSchoolRetriever {  
    public static void main(String[] args) {  
          
        String connectionString = "<<connection-string>>"; // Replace this with Connection String  
        String username = "<<username>>"; // Replace this with username from cluster access credentials  
        String password = "<<password>>"; // Replace this with password from cluster access credentials  
        Cluster cluster = Cluster.connect(connectionString, ClusterOptions.clusterOptions(username, password)  
                    .environment(env -> env.applyProfile("wan-development"))  
        );  
        retrieveCourses(cluster);  
        cluster.disconnect();  
    }  
    private static void retrieveCourses(Cluster cluster) {  
        try {  
            final QueryResult result = cluster.query("select crc.* from `student-bucket`.`art-school-scope`.`course-record-collection` crc");  
            for (JsonObject row : result.rowsAsObject()) {  
                System.out.println("Found row: " + row);  
            }  
        } catch (CouchbaseException ex) {  
            ex.printStackTrace();  
        }  
    }  
}  
```
3. In the `ArtSchoolRetriever.java` file, replace the `<<connection-string>>`, `<<username>>`, and `<<password>>` placeholders with your cluster's public connection string, and the username and password from your cluster access credentials.
4. Open a terminal window and navigate to your `student` directory.
5. Run the command `mvn install` to pull in all the dependencies and rebuild your application.
6. Run the following command to retrieve all course records:  
```sh  
mvn exec:java -Dexec.mainClass="ArtSchoolRetriever" -Dexec.cleanupDaemonThreads=false  
```  
If the retrieval is successful, the course information outputs in the console log.

#### [](#retrieve-course-records-with-less-than-200-credits-2)Retrieve Course Records with Less than 200 Credits

You can set parameters in your code to narrow your search further. To retrieve only courses with less than 200 `credit-points` using the Java SDK:

1. In your `java` directory, create a new file called `ArtSchoolRetrieverParameters.java`.
2. Paste the following code block into your `ArtSchoolRetrieverParameters.java` file:  
```java  
import com.couchbase.client.core.error.CouchbaseException;  
import com.couchbase.client.java.Cluster;  
import com.couchbase.client.java.json.JsonObject;  
import com.couchbase.client.java.query.QueryOptions;  
import com.couchbase.client.java.query.QueryResult;  
import com.couchbase.client.java.ClusterOptions;  
public class ArtSchoolRetrieverParameters {  
    public static void main(String[] args) {  
          
        String connectionString = "<<connection-string>>"; // Replace this with Connection String  
        String username = "<<username>>"; // Replace this with username from cluster access credentials  
        String password = "<<password>>"; // Replace this with password from cluster access credentials  
        Cluster cluster = Cluster.connect(connectionString, ClusterOptions.clusterOptions(username, password)  
                    .environment(env -> env.applyProfile("wan-development"))  
        );  
        retrieveCourses(cluster);  
        cluster.disconnect();  
    }  
    private static void retrieveCourses(Cluster cluster) {  
        try {  
            // This SQL++ statement takes the parameter `$creditPopints`,  
            // which is then substituted by the value in the second parameter when the statement is called.  
            final QueryResult result = cluster.query("select crc.* " +  
                            "from `student-bucket`.`art-school-scope`.`course-record-collection` crc " +  
                            "where crc.`credit-points` < $creditPoints",  
                      
                    // The second parameter in the function call, with a value that replaces `$creditPoints`.  
                    QueryOptions.queryOptions()  
                            .parameters(JsonObject.create().put("creditPoints", 200)));  
            for (JsonObject row : result.rowsAsObject()) {  
                System.out.println("Found row: " + row);  
            }  
        } catch (CouchbaseException ex) {  
            ex.printStackTrace();  
        }  
    }  
}  
```
3. In the `ArtSchoolRetrieverParameters.java` file, replace the `<<connection-string>>`, `<<username>>`, and `<<password>>` placeholders with your cluster's public connection string, and the username and password from your cluster access credentials.
4. Open a terminal window and navigate to your `student` directory.
5. Run the command `mvn install` to pull in all the dependencies and rebuild your application.
6. Run the following command to retrieve all course records:  
```sh  
mvn exec:java -Dexec.mainClass="ArtSchoolRetrieverParameters" -Dexec.cleanupDaemonThreads=false  
```  
If the retrieval is successful, the course information with your parameters outputs in the console log.

If you come across errors in your console, see [Troubleshooting the Developer Tutorial](tutorial-troubleshooting.md).

## [](#next-steps)Next Steps

After retrieving student and course records, you can [add enrollment details to the student records using the SDK](adding-course-enrollments.md).