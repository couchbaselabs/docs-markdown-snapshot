---
title: Implement the Data Model
description: Create a cluster and use buckets, scopes, and collections to
  partition your data.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/tutorials/pages/buckets-scopes-and-collections.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:server:tutorials:buckets-scopes-and-collections.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/tutorials/buckets-scopes-and-collections.html)

# Implement the Data Model

> Create a cluster and use buckets, scopes, and collections to partition your data. 

## [](#buckets-scopes-and-collections)Buckets, Scopes, and Collections

To organize and manage your data in Couchbase, you can create buckets, scopes, and collections inside your cluster.

A bucket is equivalent to a database in a relational database management system, while scopes and collections are used to provide separation between documents of different types. A bucket can hold any number of scopes, and a scope can hold any number of collections.

![couchbase-hierarchy](_images/couchbase-hierarchy-616d213da117013c9d357f6e3c393437d0649ddb.svg) 

| bucket     | Stores and retrieves data in the server.                                                                        |
| ---------- | --------------------------------------------------------------------------------------------------------------- |
| scope      | Stores collections. When you create a new bucket, Couchbase provides you with a default scope called \_default. |
| collection | Contains a set of documents. Couchbase provides you with a default collection called \_default.                 |

To continue this tutorial, you must create a bucket to hold all student data, a scope to narrow down the data into only data related to an art school, and two collections to narrow it down further into art school students and art school courses.

For more information about scopes and collections, see [Scopes and Collections](../learn/data/scopes-and-collections.md).

## [](#create-a-bucket)Create a Bucket

To create a bucket:

1. In the Couchbase Web Console, go to **Buckets**.
2. Click **Add Bucket**.
3. For the bucket name, enter `student-bucket`.
4. Click **Add Bucket** to create your bucket.

## [](#create-a-scope)Create a Scope

To create a scope:

1. In the list of buckets, next to `student-bucket`, click **Scopes & Collections**.
2. Click **Add Scope**.
3. For the scope name, enter `art-school-scope`.
4. Click **Save** to create your scope.

## [](#create-collections)Create Collections

For this tutorial, create two collections: one to store student records, and one to store course details.

To create a collection:

1. In the list of scopes and collections, next to `art-school-scope`, click **Add Collection**.
2. Click **Add Collection** next to `art-school-scope`.
3. For the collection name, enter `student-record-collection`.
4. Click **Save** to create your first collection.

To create the second collection, follow the previous steps but name the collection `course-record-collection`.

The two collections allow you to use the relational model and the document model at the same time to achieve the best design and performance possible.

The `student-record-collection` contains student records, and each student record contains a list of that student's enrollments. Unlike the standard relational model decomposition where a link table is created between students and courses, a document model stores the enrollments as part of the student records.

The `course-record-collection`, on the other hand, uses the relational model to link the enrollment records to the course records they apply to. This allows you to retrieve other details like the full title of the course or the number of credits students receive upon completing the course.

## [](#next-steps)Next Steps

After implementing the data model, you can [set up a Couchbase SDK and connect it to your cluster to write your first application](java-tutorial/install-couchbase-java-sdk.md).