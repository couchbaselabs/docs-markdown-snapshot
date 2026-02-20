---
title: Implement the Data Model
description: Learn how to logically partition your data in Capella Operational
  using buckets, scopes, and collections.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/tutorials/pages/buckets-scopes-and-collections.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:cloud:tutorials:buckets-scopes-and-collections.adoc[]
---

[View original HTML](/cloud/tutorials/buckets-scopes-and-collections.html)

# Implement the Data Model

> Learn how to logically partition your data in Capella Operational using buckets, scopes, and collections. 

To organize and manage your data in Couchbase, you can create buckets, scopes, and collections inside your cluster.

A bucket is equivalent to a database in a relational database management system, while scopes and collections are used to provide separation between documents of different types.

For more information, see [Buckets, Scopes, and Collections](../clusters/data-service/about-buckets-scopes-collections.md).

## [](#prerequisites)Prerequisites

* You have created a Capella operational free tier cluster. For more information, see [Create and Deploy Your Free Tier Operational Cluster](../get-started/create-account.md#getting-started).

## [](#create-a-bucket-scope-and-collections)Create a Bucket, Scope, and Collections

In the next part of this tutorial, you’ll create:

* A bucket to hold all student data
* A scope to separate the data into only data related to an art school
* 2 collections to separate the data further into art school students and art school courses

To create the data model from the Capella UI:

1. On the **Operational** tab, click the name of your free tier operational cluster.
2. Click the **Data Tools** tab.
3. In the cluster schema browser, click **\+ Create**.
4. Under **Bucket**, select **New** and enter the name `student-bucket`. Keep the default 100 MiB memory quota.
5. Under **Scope**, enter the name `art-school-scope`.
6. Under **Collection**, enter the name `student-record-collection` for your first collection.
7. Click **Create**.

To create the second collection, follow the above steps but use the existing `student-bucket` and `art-school-scope`, and then create a collection with the name `course-record-collection`.

The 2 collections allow you to use the relational model and the document model at the same time.

The `student-record-collection` contains student records, and each student record contains a list of that student’s enrollments. Unlike the standard relational model decomposition where a link table is created between students and courses, a document model stores the enrollments as part of the student records.

The `course-record-collection`, on the other hand, uses the relational model to link the enrollment records to the course records they apply to. This allows you to retrieve other details like the full title of the course or the number of credits students receive upon completing the course.

## [](#next-steps)Next Steps

After implementing the data model, you can [set up a Couchbase SDK and connect it to your cluster to write your first application](java-tutorial/install-couchbase-java-sdk.md).