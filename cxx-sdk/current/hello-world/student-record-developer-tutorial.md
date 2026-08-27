---
title: "Couchbase Tutorial: A Student Record System"
description: A short tutorial that will guide the developer in downloading and
  installing Couchbase, then creating a database to store student records.
pubDate: 2026-08-22T04:32:17.641Z
antora:
  editUrl: https://github.com/couchbase/docs-sdk-cxx/edit/release/1.4/modules/hello-world/pages/student-record-developer-tutorial.adoc
  xref: xref:cxx-sdk:hello-world:student-record-developer-tutorial.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cxx-sdk/current/hello-world/student-record-developer-tutorial.html)

# Couchbase Tutorial: A Student Record System

> A short tutorial that will guide the developer in downloading and installing Couchbase, then creating a database to store student records. 

This tutorial introduces Couchbase and working with a document database, as well as the C++ SDK — if you just want a quick start at using the C++ SDK, then hop over to the [Getting Started](start-using-sdk.md) page.

## [](#introduction)Introduction

Couchbase is a schema-less document database engine designed for high performance, scalability, and rapid development. During this tutorial, we'll introduce you to some key concepts behind Couchbase and how they differ from traditional SQL database systems such as MySQL and Oracle. We're going to examine the advantages of a schema-less engine by building a document database for storing student records.

## [](#database-design)The Data Model

The model will consist of three record types:

| **student**    | Holds the information about individual students such as name and date of birth.                                                                                                                                                                                                                                     |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **course**     | The courses that the student can take. You will need to store the course name, faculty, and the number of credit points associated with the course. Against each student you will somehow need to record which of the courses they are taking. Bear in mind that a student can take more than one course at a time. |
| **enrollment** | Holds the information related to the course that the student is taking. In a relational database, this is usually a link record that provides a relationship between the student and the course.                                                                                                                    |

So what would this database look like under a relational compared to a document model?

### [](#relational-model)Relational model

Unresolved include directive in modules/hello-world/pages/student-record-developer-tutorial.adoc - include::partial$diagrams/student-record-erd.puml[]

Nothing too dramatic: the database contains a list of students and a list of courses. Each student can enrol on any number of courses, and the record of each of the student's enrollments is stored in a separate table called `enrollment`, which links to the student's record and the courses they are enrolling on.

The `enrollment` table highlights one of the problems with the relational database model: each table is based on a fixed schema that can only support a single data object type. You cannot store, for example, the enrollment records in the same table as the student, even though it may more natural to do so; after all, an `enrollment` cannot exist without a `student`, so why not store them together?

### [](#document-model)Document model

The document model gives you the same decomposition advantages as the relational model, but additionally, it also supports complex types which allows for a much more flexible design.

Unresolved include directive in modules/hello-world/pages/student-record-developer-tutorial.adoc - include::partial$diagrams/student-document-database-design.puml[]

Here's how the student record system might look as a document database:

Student Record

```json
{
  "student-id": "000001",
  "name": "Hilary Smith",
  "date-of-birth": "21-12-1980",
  "enrollments": [
    {
      "course-id": "ART-HISTORY-00003",
      "date-enrolled": "07-9-2021"
    },
    {
      "course-id": "GRAPHIC-DESIGN-00001",
      "date-enrolled": "15-9-2021"
    }
  ]
}
```

The document is stored in JSON format, which allows for the storage of complex types such as arrays without decomposing them to a second table. JSON also allows the flexibility to change the structure of the document without having to rebuild schemas (as you would in a relational database system). A new field, let's say to store email addresses, could be added to new documents without having to migrate existing data to a new schema. In this case, the list of `enrollment` records is stored with the student record. Each `enrollment` record holds a reference to the course it relates to.

> [!TIP]
> It would be a very bad idea to store the course record with each student:
> 
> 1. It would lead to massive data duplication.
> 2. It would make it very difficult to maintain the data. If the `credit-points` for a course needed to be changed, then you would need to access every student record to make the change.

Art History Course Record

```json
{
  "course-id": "ART-HISTORY-00003",
  "course-name": "art history",
  "faculty": "fine art",
  "credit-points" : 100
}
```

Graphic Design Course Record

```json
{
  "course-id": "GRAPHIC-DESIGN-00001",
  "course-name": "graphic design",
  "faculty": "media and communication",
  "credit-points" : 200
}
```

Couchbase uses a document model which stores each database record as a JSON document. The document can contain both simple scalar types, and complex types such as nested records and arrays.

Hilary's enrollments are stored in the same document as her student details. As well as being a more natural way to store child information with its parent, this structure allows for all of Hilary's details (enrollments included) in one search, without the need for complex table joins to retrieve the enrollment information.

## [](#creating-your-database)Creating Your Database

In the next part of the tutorial, you're going to begin your exploration of Couchbase by signing up for Capella and deploying a free tier operational cluster. Capella is the simplest way of using Couchbase; should you wish to try a local Docker installation instead, you can adjust the connection steps in the tutorial below — but we strongly recommend Capella as the easiest way of getting started.

With free tier you'll get a forever free operational cluster of three nodes, featuring the Data Service, Query Service, and Index Service — all that you need to follow along with this tutorial.

### [](#capella-installation)Capella Installation

Sign up to [the Couchbase Capella cloud service](https://www.couchbase.com/products/capella) and deploy a free tier operational cluster. With your account and free cluster, you can then run through the tutorials for [Getting Started with Couchbase Capella](../../../cloud/get-started/create-account.md).

Make a note of the database endpoint, and any user names and passwords that you set up. You will use these to access your Capella database from the C++ SDK.

The next thing to do is create the bucket where you're going to store your documents. You will also learn other ways in which Couchbase allows you to logically partition your data.

### [](#so-what-is-a-bucket-exactly)So What is a Bucket Exactly?

If you think in RDBMS terms, a Couchbase Bucket is analogous to a database: it's the data store where you're going to store and retrieve related information about the students.

You can click on the **Dashboard** **Buckets** link to access the Buckets page, then click on **Add Bucket**.

In this dialog, enter `student-bucket` in the **Name** box.

![Adding student bucket to Couchbase](add-student-bucket.png) 

Once you have entered the bucket name, press the **Add Bucket** button to return to the main bucket list.

### [](#scopes%5Fand%5Fcollections)Scopes and Collections

In all but the simplest cases, it's better to provide some kind of separation between documents of different types. Couchbase has a simple hierarchy model which allows for such separation:

Unresolved include directive in modules/hello-world/pages/student-record-developer-tutorial.adoc - include::partial$diagrams/couchbase-hierarchy.puml[]

You're already familiar with clusters, nodes, and buckets. Inside a bucket you can also have any number of _scopes_ (up to a thousand), and inside a scope you can have any number of _collections_ (again, up to a thousand).

| **scopes**      | Acts as a parent to a collection. When you create a new bucket, Couchbase will provide you with a default scope called \_default. You can use the default scope to store                             |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **collections** | A collection can contain a set of documents. A default collection (\_default) is provided, but it is recommended that you create your own collection named to reflect the documents store inside it. |

Rather than have our student records stored in the default collection, we're going to add two collections: one will be used to store the student records, the other will be used to store the course details.

Now looking again at the relational design of our student database:

Unresolved include directive in modules/hello-world/pages/student-record-developer-tutorial.adoc - include::partial$diagrams/student-record-erd.puml[]

We can see that our equivalent document-based system could do with a little decomposition:

Unresolved include directive in modules/hello-world/pages/student-record-developer-tutorial.adoc - include::partial$diagrams/student-document-database-design.puml[]

So, inside our `student-bucket` we've set up a scope called `art-school-scope`. Perhaps we have a number of schools and we want to restrict access to the school based on the role of the user; using scopes is the ideal way to do it.

Within the `scope` we set up two collections:

| **student-record-collection** | Contains the student records, and within each student record we carry a list of all their enrollments. Again, this moves away from the standard relational decomposition since we're actually storing the enrollments as part of the student's record, instead of implementing it as a link table between the students and the courses. |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **course-record-collection**  | The enrollment records will carry a link to the course record it applies to, so we can retrieve other details such as the full name of the course and the number of credit points the student receives for completing it.                                                                                                               |

> [!NOTE]
> Of course, it's possible to just add the details of the course to the student's enrollment records, but this may have downsides. Changing the credit points on the course, for example, would involve running through every student's enrollments and changing the credit details on each one. This is why the document model and relational model are used in conjunction to get the best combination of robust design and performance.

Now that you understand the basics of scopes and collections, return to your administration screen so we can add them to your bucket.

### [](#adding-the-student-scope)Adding the Student Scope

Return to the `Buckets` screen and click the **Scopes & Collections** link.

![Examining the scopes and collections](click-scopes-and-collections.png) 

Although the bucket is created with a default scope, for this example, you're going to create your own. Click on the **Add Scope** link.

On the next dialog, create your `art-school-scope`.

![Dialog to create a new scope](create-scope.png) 

Press **Save** to save the new scope and return to the bucket screen. The new scope should be showing in the list.

## [](#adding-the-collections)Adding the collections

Next, we're going to add two collections for the new scope. Click the **Add Collection** link for the\`art-school-scope'.

![Adding a new collection](add-collection-link.png) 

When the collection dialog is displayed, fill in the name of the first collection: `student-record-collection`; then press **Save**.

Now do the same again to create the `course-record-collection`.

You should now have the `art-school-scope` containing your two collections.

![Screen showing new collections added](completed-art-school-scope.png) 

> [!TIP]
> We're sticking with the Capella GUI for this stage of the tutorial, but management options for creating resources are available through the SDK, the command line, the REST API, or through Infrastructure-as-Code (IAC) with Terraform.

## [](#writing-your-first-app)Writing Your First App

Now you have your cluster, bucket, scope, and collections set up and ready to be populated. Next, you'll set up your system to write your first Couchbase application.

### [](#prerequisites)Prerequisites

To keep things as light as possible, we're not going to worry about building a web front end or REST service, just a few methods to read/write our documents to the database.

You will need a few things installed on your machine before you begin:

* The Java Software Development Kit (8, 11, 17, or 21)
* Apache Maven (version 3+)

> [!TIP]
> [SDKMan](https://sdkman.io/) is the easiest way to install and manage JDKs and Maven on your host machine.

### [](#installing-the-sdk)Installing the SDK

More details of the installation process are in the [full installation guide](../project-docs/sdk-full-installation.md).

[CPM.cmake](https://github.com/cpm-cmake/CPM.cmake) is the recommended way to include the library in your project. You need to include the following command in your `CMakeLists.txt`.

```cmake
CPMAddPackage(
  NAME
  couchbase_cxx_client
  GIT_TAG
  1.4.0
  VERSION
  1.4.0
  GITHUB_REPOSITORY
  "couchbase/couchbase-cxx-client"
  OPTIONS
  "COUCHBASE_CXX_CLIENT_STATIC_BORINGSSL ON")
```

### [](#set-up)Set up

Create the following directory structure on your machine:

Unresolved include directive in modules/hello-world/pages/student-record-developer-tutorial.adoc - include::partial$student-mvn-directory-structure.adoc\[\]

Create a new file in the directory called `pom.xml` in the `student` directory. The pom file should be populated as follows:

pom.xml

```xml
Unresolved directive in student-record-developer-tutorial.adoc - include::{java-sample-location}pom.xml[]
```

| **1** | The dependencies section lists all the libraries required to build the application. In our case, we only need the Couchbase client SDK (version 1.4.0, in this case). |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Unresolved include directive in modules/hello-world/pages/student-record-developer-tutorial.adoc - include::partial$student-mvn-directory-structure.adoc\[\]

You can test the setup is correct by opening a terminal window and changing to the `student` directory. Run the build script to pull in all the dependencies.

```sh
mvn install
```

You're now ready to write your first Couchbase application.

## [](#sdk-introduction)SDK Introduction

Working with any database SDK usually involves the following operations:

1. Connect to the database.
2. Carry out CRUD (Create, Read, Update, Delete) operations.
3. Disconnect from the database (important for resource cleanup).

Fortunately, the Couchbase SDK follows the same pattern, so the first thing you're going to do is write the code to connect to your document store.

### [](#connecting-to-the-database)Connecting to the database

Earlier, you created a directory structure to hold your application. Create the file `student.java` in the `java` directory as shown below.

Unresolved include directive in modules/hello-world/pages/student-record-developer-tutorial.adoc - include::partial$student-mvn-directory-structure.adoc\[\]

Add the following content to the `ConnectStudent.java` file:

```java
Unresolved directive in student-record-developer-tutorial.adoc - include::{java-sample-location}ConnectStudent.java[]
```

If you're familiar with the JDBC API then connecting to a Couchbase server is not that different:

| **1** | A call to Cluster.connect creates a channel to the named server (localhost running on your local machine in this case), supplying your username and password to authenticate the connection.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **2** | The retrieved cluster is used to retrieve the bucket set up in [install-couchbase-server.adoc](#install-couchbase-server.adoc).                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **3** | {why-waitUntilReady} Once the function has finished, it sends a notification to its caller, which will then process the output of the call.Now this usually works very well in practice, but in our simple example there is a problem: after we make the call to cluster.bucket, the program will carry on without waiting for the bucket retrieval to be complete. This means we're now trying to retrieve the scope from a bucket object that hasn't been fully initialised.This is where the waitUntilReady call comes in. This will force the program to wait until the bucket object is fully prepared. |
| **4** | Retrieves the art-school-scope from the bucket.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **5** | Retrieves the student collection from the scope.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **6** | The next line is just a check to make sure we have connected and retrieved the collection when the program is run. You can see the output by running it through maven:                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **7** | And as with all database systems, it's good practise to disconnect from the Couchbase cluster once you've finished working with it.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

```sh
mvn exec:java -Dexec.mainClass="ConnectStudent" -Dexec.cleanupDaemonThreads=false
```

Somewhere in the output, you'll find the line containing the name of the collection you've successfully retrieved:

![Console showing successful connection to server](connect-to-cluster-console-output.png) 

> [!TIP]
> As an experiment, try commenting out the `bucket.waitUntilReady` call, then run the program again. What happens?

Okay, so you've connected to the cluster and retrieved your collection. Unfortunately, there's nothing in there to see at the moment, so the next thing to do is create a few records.

## [](#populating-the-student-collection)Populating the student collection

Remember that Couchbase is a [document store](#couchbase-tutorial-student-records.adoc#database-design), not a relational database in the traditional sense. Rather than storing data in tables, you're going to create a document in JSON and insert it into the `student-record-collection`. Here's Hilary Smith's student record (minus the enrollment details –- we'll come to that later):

```json
Unresolved include directive in modules/hello-world/pages/student-record-developer-tutorial.adoc - include::example$hilary-smith-basic.json[]
```

Start by creating the file `InsertStudent.java` in the `java` directory:

```java
Unresolved directive in student-record-developer-tutorial.adoc - include::{java-sample-location}InsertStudent.java[]
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

![Student record showing in the web console](hilarys-record-in-admin-console.png) 

And there it is: a single document with an id of `000001` belonging to Hilary Smith.

Before carrying on to the next section, change your program so you can add a student record for `Ashley Jones`.

## [](#courses-collection)Courses Collection

In the next section, you're going to build another short program for populating the course collection.

## [](#populating-the-course-details-collection)Populating the course details collection

You can use the same technique to build a store for the courses. Here's a quick reminder of the course document structure:

* Art History
* Graphic Design
* Fine Art

```json
Unresolved include directive in modules/hello-world/pages/student-record-developer-tutorial.adoc - include::example$art-history-course.json[]
```

```json
Unresolved include directive in modules/hello-world/pages/student-record-developer-tutorial.adoc - include::example$graphic-design-course.json[]
```

```json
Unresolved include directive in modules/hello-world/pages/student-record-developer-tutorial.adoc - include::example$fine-art-course.json[]
```

The code should be familiar to you; there's not much difference between writing to the course collection and writing to the student collection, you just have more records to deal with:

```java
Unresolved directive in student-record-developer-tutorial.adoc - include::{java-sample-location}InsertCourses.java[]
```

| **1** | Note that you're now writing to a different collection. |
| ----- | ------------------------------------------------------- |

> [!IMPORTANT]
> Make sure that you've created the `course-collection` in the admin console before you attempt to run the program.

You can use maven to run the application:

```sh
mvn exec:java -Dexec.mainClass="InsertCourses" -Dexec.cleanupDaemonThreads=false
```

Use the admin console to make sure the documents have been created in the correct collection.

![Console showing the courses collection](new-course-collection.png) 

## [](#next-steps)Next steps

So you've created a cluster, a bucket, a scope and two collections. You've also populated your collections with documents. Well, a database isn't much use until we can retrieve information from it, which is what you're going to take a look at in the next part.

# [](#using-the-query-editor)Using the Query Editor

Return to the admin console, and click on the **Query** item on the left-hand menu.

This will take you to the query workbench. The workbench has a few filter fields that'll make it much easier to narrow down our search criteria.

![The console query editor](set-query-filters.png) 

Use the two dropdown items to select the `student-bucket` and the `art-school-scope`. This narrows the scope of the queries, meaning you don't have to add the name of the bucket and the scope to your queries.

Okay, let's try a simple query to retrieve all the course in our collection.

Type the following query into the query editor field:

```sqlpp
select crc.* from `course-record-collection` crc
```

> [!NOTE]
> SQL++ is very similar to standard SQL. Once you have mastered the document database model, you'll find it very easy to adapt.

![Query to retrieve the course collection](attempt-first-query.png) 

What happens when you hit **Execute**?

You get an error message returned from the cluster:

```json
[
  {
    "code": 4000,     (1)
    "msg": "No index available on keyspace `default`:`student-bucket`.`art-school-scope`.`course-record-collection` that matches your query. Use CREATE PRIMARY INDEX ON `default`:`student-bucket`.`art-school-scope`.`course-record-collection` to create a primary index, or check that your expected index is online.",    (2)
    "query": "select * from `course-record-collection`"    (3)
  }
]
```

| **1** | The internal Couchbase code for the message.                                                                                                                                   |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **2** | A plain text description telling you what happened. In this case, the problem is that there no index defined on our bucket, so the search couldn't locate any key information. |
| **3** | The JSON message also returns the original query.                                                                                                                              |

## [](#creating-an-index)Creating an index

Fortunately, you can use the same query editor to add an index to the bucket. To do this, enter the following command into the editor and press **Enter**.

```sqlpp
create primary index course_idx on `course-record-collection`
```

This will create a single index (`course_idx`) on your `course-record-collection`.

> [!TIP]
> The error message returned from the search statement provides an example command for creating the primary index. You can copy the example command and run it in the query editor to create your primary index.

Okay, now if you run the `select` query again …

```sqlpp
select crc.* from `course-record-collection` crc
```

Now you should get a result:

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

Okay, now try something else: returning the courses with `credit-points` of less than 200:

```sqlpp
select crc.* from `course-record-collection` crc where crc.`credit-points` < 200
```

which will bring back:

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

### [](#but-what-about-the-primary-id-field)But what about the primary id field?

Good question. You may want to get hold of `id` field, which as you can see, isn't returned with the document, even if we're asking for all the fields in the call. The primary key exists as part of the document's "meta" structure, which can be interrogated along with the rest of the document. Make the following small adjustment to the `SQL++` statement and run the query again:

```sqlpp
select META().id, crc.* from `course-record-collection` crc where crc.`credit-points` < 200
```

The `META()` function call will return any property contained in the document's metadata, including its id:

```json
[
  {
    "course-name": "art history",
    "credit-points": 100,
    "faculty": "fine art",
    "id": "ART-HISTORY-000001"    (1)
  },
  {
    "course-name": "fine art",
    "credit-points": 50,
    "faculty": "fine art",
    "id": "FINE-ART-000002"    (1)
  }
]
```

| **1** | id fields added to the returned document. |
| ----- | ----------------------------------------- |

You can find a full rundown of the SQL++ language here: [n1ql:n1ql-language-reference/index.adoc](#n1ql:n1ql-language-reference/index.adoc).

## [](#using-the-sdk)Using the SDK

Of course, you can also retrieve documents using the SDK. In this section, you're going to use the same SQL++ queries as part of a small Java application. Let's start with a basic record retrieval:

```java
Unresolved directive in student-record-developer-tutorial.adoc - include::{java-sample-location}ArtSchoolRetriever.java[]
```

If you build and run this program:

```sh
mvn exec:java -Dexec.mainClass="ArtSchoolRetriever" -Dexec.cleanupDaemonThreads=false
```

Then you'll get a list of the classes in the output.

![Terminal window showing course records retrieved with the Java SDK](retrieve-courses-cli.png) 

You may have noticed a difference between the SQL statement we used in the web console, and the statement used as part of the application:

```sqlpp
select crc.* from `student-bucket`.`art-school-scope`.`course-record-collection` crc
```

The name of the collection in the SQL++ statement has to be fully qualified, including the name of the bucket as well as the containing scope.

You can, of course, set parameters as part of your query, as shown in the next example:

```java
Unresolved directive in student-record-developer-tutorial.adoc - include::{java-sample-location}ArtSchoolRetrieverParameters.java[]
```

| **1** | The SQL++ statement takes a parameters $creditPoints which will be substituted with a correctly typed value when the statement is called.                                                                                    |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | The value to substitute is provided in the QueryOptions given as the second parameter in the call. The value of the map entry is the actual parameter value (in this case, 200 which we're using to test the credit-points). |

You can use `maven` to run the program:

```sh
mvn exec:java -Dexec.mainClass="ArtSchoolRetrieverParameters" -Dexec.cleanupDaemonThreads=false
```

## [](#next-steps-2)Next steps

Now you can add and search for records, the next section will consolidate what you've learned so far by demonstrating how to amend existing records by adding enrollment details. So when you're ready carry on to [java-tutorial/adding-course-enrollments.adoc](#java-tutorial/adding-course-enrollments.adoc).

## [](#introduction-2)Introduction

A quick recap: here's the structure of our document store:

Unresolved include directive in modules/hello-world/pages/student-record-developer-tutorial.adoc - include::partial$diagrams/student-document-database-design.puml[]

At this point, you should have a student records for Hilary Smith and Ashley Jones, along with records for three courses. You're now going to write a short program that will add enrollment details to the student records.

You're going to create another program in the same working directory that will bring together all the concepts you've learned so far.

At the end of the exercise, you should have changed Hilary's student record to store the enrollment details in an array:

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

So, let's begin with the Java program that will change Hilary's record.

```java
Unresolved directive in student-record-developer-tutorial.adoc - include::{java-sample-location}AddEnrollments.java[]
```

| **1**  | As you'll remember from our [first example](#java-tutorial/creating-the-students-collection.adoc#connecting-to-the-database), the application first has to connect to the Couchbase cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2**  | Then it picks up the correct Bucket from the cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **3**  | Do you remember why we need this waitUntilReady function is needed when connecting to the server? Answer {why-waitUntilReady}                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **4**  | Here again, we pick up the student collection from the art-school-scope; you'll need it later to change Hilary's record and write it back to the collection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **5**  | There are three method calls here: Retrieve Hilary's student record. Retrieve the graphic design course record. Retrieve the art history course record. Each method uses a SQL++ call to retrieve a single record from its respective collection. This is just a demonstration, so there is no error checking to ensure that an item from the collection has been returned. In a live system, checks would have to be made to prevent possible errors while the program is running.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **6**  | Remember that Couchbase doesn't have a native date type, so it's common practice to store the dates as strings.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **7**  | The enrollments inside the student record are stored as an array; since JSON is the native data format for Couchbase, it's not surprising that each SDK has a host of functions for processing data in JSON. In this case, the call JsonArray.create() will create an empty list structure.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **8**  | Now JSON elements are added to the enrollments array. Looking back at the [data structure](#enrollments-structure) for enrollments, we need store just two items: the course that the enrollment relates to, and the date the student enrolled. enrollments.add(JsonObject.create().put("course-id", graphic\_design.getString("id"))     .put("date-enrolled", currentDate)); The course-id uses the id of the course record retrieved from the database. We could, of course, store the whole record in this field. Why _wouldn't_ we want to do that? Answer This goes back to our relational model, and the idea of normalising the data model so that we don't have repeating data items all over the place. Here, you're just storing a reference to the course, not the course record itself. So if the course details change (such as the number of credit points assigned to it), then you don't have to search through every single record that includes its own version. |
| **9**  | The array of enrollments is built, so now you add them to Hilary's record. This is where the document database model shines; there is no need to change a database schema and rebuild the database. Just add the data and you're done.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **10** | Finally, the changes need to be committed to the collection. For this, use the upsert function, which takes the key of the record you wish to insert or update and the record itself as parameters. If they key exists in the collection then the record is updated. If the key does not exist then it's a fresh document, so the item is inserted.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

As always, use maven to run the program.

```sh
mvn exec:java -Dexec.mainClass="AddEnrollments" -Dexec.cleanupDaemonThreads=false
```

And check your results in administrator console.

## [](#great-job)Great Job!

You've reached the end of the beginners' tutorial. You can explore the documentation site to learn more about Couchbase.