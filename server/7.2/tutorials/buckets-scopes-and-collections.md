---
title: Buckets, Scopes and Collections
description: In this section, you'll learn how to logically partition your data
  in Couchbase using buckets, scopes and collections.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.2/modules/tutorials/pages/buckets-scopes-and-collections.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:tutorials:buckets-scopes-and-collections.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/tutorials/buckets-scopes-and-collections.html)

# Buckets, Scopes and Collections

> In this section, you’ll learn how to logically partition your data in Couchbase using buckets, scopes and collections. 

## [](#so-what-is-a-bucket-exactly)So What is a Bucket Exactly?

If you think in database terms, a Couchbase Bucket is analogous to a database: it’s the data store where you’re going to store and retrieve related information about the students.

You can click on the **Dashboard** **Buckets** link to access the Buckets page, then click on **Add Bucket**.

In this dialog, enter `student-bucket` in the **Name** box.

![Adding student bucket to Couchbase](_images/add-student-bucket.png) 

Once you have entered the bucket name, press the **Add Bucket** button to return to the main bucket list.

## [](#scopes%5Fand%5Fcollections)Scopes and Collections

In all but the simplest cases, it’s better to provide some kind of separation between documents of different types. Couchbase has a simple hierarchy model which allows for such separation:

![couchbase-hierarchy](_images/couchbase-hierarchy-bd5860c2c8827ac8529789bf2d70ce507f186962.svg) 

You’re already familiar with clusters, nodes, and buckets. Inside a bucket you can also have any number of _scopes_, and inside a scope you can have any number of _collections_.

| **scopes**      | acts as a parent to a collection. When you create a new bucket, Couchbase will provide you with a default scope called \_default. You can use the default scope to store                             |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **collections** | a collection can contain a set of documents. A default collection (\_default) is provided, but it is recommended that you create your own collection named to reflect the documents store inside it. |

Rather than have our student records stored in the default collection, we’re going to add two collections: one will be used to store the student records, the other will be used to store the course details.

Now looking again at the relational design of our student database:

![student-record-erd](_images/student-record-erd-107b1252fd5db120a096e289c8c7f238150b57f0.svg) 

We can see that our equivalent document-based system could do with a little decomposition:

![student-document-database-design](_images/student-document-database-design-f437e457810966f04ff9fc2bc2ecdbb5327ce938.svg) 

So, inside our `student-bucket` we’ve set up a scope called `art-school-scope`. Perhaps we have a number of schools and we want to restrict access to the school based on the role of the user; using scopes is the ideal way to do it.

Within the `scope` we set up two collections:

| **student-record-collection** | contains the student records, and within each student record we carry a list of all their enrollments. Again, this moves away from the standard relational decomposition since we’re actually storing the enrollments as part of the student’s record, instead of implementing it as a link table between the students and the courses. |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **course-record-collection**  | The enrollment records will carry a link to the course record it applies to, so we can retrieve other details such as the full name of the course and the number of credit points the student receives for completing it.                                                                                                               |

> [!NOTE]
> Of course, it’s possible to just add the details of the course to the student’s enrollment records, but this may have downsides. Changing the credit points on the course, for example, would involve running through every student’s enrollments and changing the credit details on each one. This is why the document model and relational model are used in conjunction to get the best combination of robust design and performance.

Now that you understand the basics of scopes and collections, return to your administration screen so we can add them to your bucket.

### [](#adding-the-student-scope)Adding the Student Scope

Return to the `Buckets` screen and click the **Scopes & Collections** link.

![Examining the scopes and collections](_images/click-scopes-and-collections.png) 

Although the bucket is created with a default scope, for this example, you’re going to create your own. Click on the **Add Scope** link.

On the next dialog, create your `art-school-scope`.

![Dialog to create a new scope](_images/create-scope.png) 

Press **Save** to save the new scope and return to the bucket screen. The new scope should be showing in the list.

## [](#adding-the-collections)Adding the collections

Next, we’re going to add two collections for the new scope. Click the **Add Collection** link for the \`art-school-scope'.

![Adding a new collection](_images/add-collection-link.png) 

When the collection dialog is displayed, fill in the name of the first collection: `student-record-collection`; then press **Save**.

Now do the same again to create the `course-record-collection`.

You should now have the `art-school-scope` containing your two collections.

![Screen showing new collections added](_images/completed-art-school-scope.png) 

## [](#select-your-language)Next steps

So you have your cluster, bucket, scope and collections set up and ready to be populated. In the next section, you’ll set up your system to write your first Couchbase application.