---
title: Set Up and Connect the Couchbase Java SDK
description: Set up the Couchbase Java SDK to connect and interact with your
  student cluster.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/tutorials/pages/java-tutorial/install-couchbase-java-sdk.adoc
  xref: xref:7.6@server:tutorials:java-tutorial/install-couchbase-java-sdk.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/tutorials/java-tutorial/install-couchbase-java-sdk.html)

# Set Up and Connect the Couchbase Java SDK

> Set up the Couchbase Java SDK to connect and interact with your student cluster. 

## [](#prerequisites)Prerequisites

Before continuing this tutorial, you must first:

* [Run Couchbase Server](../install-couchbase-server.md)
* [Implement the data model](../buckets-scopes-and-collections.md)
* Install the Java Software Development Kit (version 8, 11, 17, or 21)
* Install Apache Maven (version 3+)

> [!TIP]
> The easiest way to install and manage Java SDKs and Maven on your machine is through [SDKMan](https://sdkman.io/install).
> 
> After following the instructions to install SDKMan, open a terminal window and run the commands `sdk install java` and `sdk install maven` to install the latest versions of Java and Maven.

For more information about the Java SDK installation, see the [full installation page](../../../../java-sdk/current/project-docs/sdk-full-installation.md).

## [](#set-up-the-java-sdk)Set Up the Java SDK

To set up the Java SDK:

1. Create the following directory structure on your computer:  
📂 ~ (your home directory)  
  📂 student  
    📂 src  
      📂 main  
        📂 java
2. In the `student` directory, create a new file called `pom.xml`.  
📂 ~ (your home directory)  
  📂 student  
  📃 pom.xml ⬅ here!  
  📂 src  
    📂 main  
      📂 java
3. Paste the following code block into your `pom.xml` file:  
```xml  
<?xml version="1.0" encoding="UTF-8"?>  
<project xmlns="http://maven.apache.org/POM/4.0.0"  
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">  
    <modelVersion>4.0.0</modelVersion>  
    <groupId>org.example</groupId>  
    <artifactId>couchbase-java</artifactId>  
    <version>1.0-SNAPSHOT</version>  
    <properties>  
        <maven.compiler.source>16</maven.compiler.source>  
        <maven.compiler.target>16</maven.compiler.target>  
        <encoding>UTF-8</encoding>  
        <project.build.sourceEncoding>${encoding}</project.build.sourceEncoding>  
        <project.reporting.outputEncoding>${encoding}</project.reporting.outputEncoding>  
        <project.resources.sourceEncoding>${encoding}</project.resources.sourceEncoding>  
        <archetype.encoding>${encoding}</archetype.encoding>  
    </properties>  
    <!-- The `<dependencies>` section of the code block lists all the libraries required to build your application. In the case of the student record tutorial, you only need the Couchbase client SDK. -->  
    <dependencies>  
        <dependency>  
            <groupId>com.couchbase.client</groupId>  
            <artifactId>java-client</artifactId>  
            <version>3.6.0</version>  
        </dependency>  
    </dependencies>  
</project>  
```
4. Open a terminal window and navigate to your `student` directory.
5. Run the command `mvn install` to pull in all the dependencies and finish your SDK setup.

You can now connect your Java SDK to your cluster.

## [](#connect-to-the-cluster)Connect the SDK to Your Cluster

To connect to the cluster:

1. In your `java` directory, create a new file called `ConnectStudent.java`.  
📂 ~ (your home directory)  
  📂 student  
    📃 pom.xml  
    📂 src  
      📂 main  
        📂 java  
          📃 ConnectStudent.java ⬅ here!
2. Paste the following code block into your `ConnectStudent.java` file:  
```java  
import com.couchbase.client.java.Bucket;  
import com.couchbase.client.java.Cluster;  
import com.couchbase.client.java.Collection;  
import com.couchbase.client.java.Scope;  
import java.time.Duration;  
public class ConnectStudent {  
    public static void main(String[] args) {  
        // Calls `Cluster.connect` to create a channel to the named server  
        // (in this case, `localhost` is running on your local machine)  
        // and supplies your username and password to authenticate the connection.  
        Cluster cluster = Cluster.connect("localhost",  
                "username", "password");  
        // The `cluster.bucket` retrieves the bucket you set up when you installed Couchbase Server.  
        Bucket bucket = cluster.bucket("student-bucket");  
        // Most of the Couchbase APIs are non-blocking.  
        // When you call one of them, your application carries on and continues to perform other actions while the function you called executes.  
        // When the function has finished executing, it sends a notification to the caller and the output of the call is processed.  
        // While this usually works, in this code sample the application carries on without waiting for the bucket retrieval to complete after you make the call to `cluster.bucket`.  
        // This means that you now have to try to retrieve the scope from a bucket object that has not been fully initialized yet.  
        // To fix this, you can use the `waitUntilReady` call.  
        // This call forces the application to wait until the bucket object is ready.  
        bucket.waitUntilReady(Duration.ofSeconds(10));  
        // The `bucket.scope` retrieves the `art-school-scope` from the bucket.  
        Scope scope = bucket.scope("art-school-scope");  
        // The `scope.collection` retrieves the student collection from the scope.  
        Collection student_records = scope.collection("student-record-collection");  
        // A check to make sure the collection is connected and retrieved when you run the application.  
        // You can see the output using maven.  
        System.out.println("The name of this collection is " + student_records.name());  
        // Like with all database systems, it's good practice to disconnect from the Couchbase cluster after you have finished working with it.  
        cluster.disconnect();  
    }  
}  
```  
> [!IMPORTANT]  
> You must re-run `mvn install` in your `student` directory whenever you make a change to a java file to rebuild your application.
3. Open a terminal window and navigate to your `student` directory.
4. Run the command `mvn install` to pull in all the dependencies and rebuild your application.
5. Run the following command to check that the connection works:  
```sh  
mvn exec:java -Dexec.mainClass="ConnectStudent" -Dexec.cleanupDaemonThreads=false  
```  
If the connection is successful, the collection name outputs in the console log.  
![Console showing successful connection to server](../_images/student-record-collection-console-output.png)

If you come across errors in your console, see the [troubleshooting page](tutorial-troubleshooting.md).

## [](#next-steps)Next Steps

After setting up and connecting the Java SDK, you can [add student and course records to your cluster](create-records.md).