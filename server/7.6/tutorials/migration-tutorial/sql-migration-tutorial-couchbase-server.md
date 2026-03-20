---
title: Migrating your Data from MySQL to Couchbase Server
description: Using MySQL as a starting point, this guide demonstrates how to
  migrate your existing data from SQL tables to documents stored in a Couchbase
  bucket.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/7.6/modules/tutorials/pages/migration-tutorial/sql-migration-tutorial-couchbase-server.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.6@server:tutorials:migration-tutorial/sql-migration-tutorial-couchbase-server.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/tutorials/migration-tutorial/sql-migration-tutorial-couchbase-server.html)

# Migrating your Data from MySQL to Couchbase Server

> Using MySQL as a starting point, this guide demonstrates how to migrate your existing data from SQL tables to documents stored in a Couchbase bucket. 

## [](#introduction)Introduction

Couchbase offers a number of strategies for migrating your existing data; in this example, we will begin with a sample student record database stored in MySQL, and use the Couchbase server tool `cbimport` to copy the data into a Couchbase cluster.

## [](#prerequisites)Prerequisites

Before you begin this exercise, you should have installed and set up a Couchbase cluster on your local machine. You will find instructions for creating a fresh cluster here ⇒ [Couchbase Server Installation](../../getting-started/do-a-quick-install.md)

To use `cbimport`, you will need to install the Couchbase `CLI` package. You will find the location of the package and instructions for installing it, here ⇒ [CLI Reference](../../cli/cli-intro.md)

If you’re running through the examples, then you will also need an existing MySQL installation with the preexisting table structure defined in [the following section](#student-record-sql-database-section).

> [!IMPORTANT]
> This tutorial makes use of the MySQL JSON functions that were introduced in version `5.7.22`. Make sure you have installed MySQL version `5.7.22` or later.

## [](#student-record-sql-database-section)Student Record database

The database we will convert will consist of a relational structure with three tables:

![Student records SQL database](../_images/student-record-erd-0e190ebb29530e06a5d6984a70841b3ecd966c41.svg) 

Figure 1\. Student records SQL database

We will convert this table structure to a document model suitable for storage in our Couchbase bucket:

![Student document model](../_images/student-document-database-design-e67ab09d4aad1dcf88a82921ef9c2058e3dea374.svg) 

Figure 2\. Student document model

You will see that our document model is not an exact mapping of the SQL database: we have taken the `enrollments` records and added them directly as a list of sub-documents within each student record:

```json
[
{"student-id": 1,
"enrollments": [{"course-id": 3, "final-score": null, "date-enrolled": "2024-04-18", "date-completed": null}, {"course-id": 1, "final-score": null, "date-enrolled": "2025-03-05", "date-completed": null}], "student-name": "Harriet Hill", "date-of-birth": "1970-03-06"},
{"student-id": 2, "enrollments": [{"course-id": 1, "final-score": null, "date-enrolled": "2025-03-01", "date-completed": null}], "student-name": "Steven Morris", "date-of-birth": "1984-03-05"},
{"student-id": 3, "enrollments": [{"course-id": null, "final-score": null, "date-enrolled": null, "date-completed": null}], "student-name": "Jenny Mills", "date-of-birth": "1969-11-06"}
]
```

## [](#extract-sql-data)Extract your Course data from MySQL

The first stage of your migration is to extract the data a file format that the `cbimport` utility can work with. `cbimport` can work with comma-separated value files or JSON-formatted files. Because we already know that we will be embedding our `enrollment` records into the record for each student, makes sense to use the more versatile JSON structure.

Fortunately, MySQL has a number of SQL functions that make working with JSON data fairly straightforward, so we’ll start by migrating the `course` table into a JSON file:

Extract the `course` table

```mysql
SELECT JSON_OBJECT(
       'course-id', course.`course-id`,
       'course-name', course.`course-name`,
       'faculty', course.faculty,
       'credit-points', course.`credit-points`
       ) FROM course
INTO OUTFILE '/var/lib/mysql-files/courses.json'
```

> [!NOTE]
> for Windows users.
> 
> When setting out the `OUTFILE` portion of the query, remember to use forward slashes (\\) in the file path name.

Using the `JSON_OBJECT` function, the command will `SELECT` every record in the table and output it to a file. Each line of the file will correspond to a single record:

```jsonlines
{"faculty": "Art", "course-id": 1, "course-name": "Art History", "credit-points": 50}
{"faculty": "Art", "course-id": 2, "course-name": "Fine Art", "credit-points": 30}
{"faculty": "Design", "course-id": 3, "course-name": "Graphic Design", "credit-points": 70}
{"faculty": "English", "course-id": 4, "course-name": "Creative Writing", "credit-points": 70}
```

> [!NOTE]
> Strictly speaking, the JSON output is not a well-formed JSON document because it isn’t structured as an array. Nevertheless, `cbimport` will read each line as a separate record.

## [](#extract-your-student-data-from-mysql)Extract your Student data from MySQL

This case is slightly different because we want to include the enrollment details with each student record

We can handle this JSON structure by using a more involved SELECT: As well as extracting the student records, we can simultaneously pull in the enrollments for each student:

Extract `students` and their `enrollments`.

```mysql
SELECT JSON_OBJECT(
               'student-id', student.`student-id`,
               'student-name', student.name,
               'date-of-birth', student.`date-of-birth`,
               'enrollments', IF (COUNT(enrollment.`course-id`) = 0, JSON_ARRAY(), JSON_ARRAYAGG(
                       JSON_OBJECT(
                               'course-id', enrollment.`course-id`,
                               'date-enrolled', enrollment.`date-enrolled`,
                               'date-completed', enrollment.`date-completed`,
                               'final-score', enrollment.`score`
                       )
                              ))
       )
FROM student
         LEFT OUTER JOIN enrollment ON enrollment.`student-id` = student.`student-id`
GROUP BY student.`student-id`
INTO OUTFILE '/var/lib/mysql-files/students.json';
```

In addition to the `JSON_OBJECT` function call that extracts the student details, we are also using the `JSON_ARRAYAGG` function to build an array within each student record. The data for this list is retrieved through the `LEFT OUTER JOIN`which provides the foreign key link between the student and the enrollment record.

We also use the `` IF (COUNT(enrollment.`course-id`) = 0 `` statement to ensure that there are existing enrollment records attached to the current student. If there are no enrollment records, then that portion of the query uses `JSON_ARRAY()` to return an empty list.

```jsonlines
{"student-id": 1, "enrollments": [{"course-id": 3, "final-score": 0, "date-enrolled": "2025-03-10", "date-completed": null}, {"course-id": 1, "final-score": 0, "date-enrolled": "2025-03-10", "date-completed": null}], "student-name": "Hilary Wells", "date-of-birth": "1990-08-09"}
{"student-id": 2, "enrollments": [{"course-id": 2, "final-score": 0, "date-enrolled": "2025-03-10", "date-completed": null}], "student-name": "Ashley Matthews", "date-of-birth": "1987-07-01"}
{"student-id": 3, "enrollments": [{"course-id": 1, "final-score": 0, "date-enrolled": "2025-03-10", "date-completed": null}], "student-name": "Boregard Johnson", "date-of-birth": "1985-03-23"}
{"student-id": 4, "enrollments": [], "student-name": "Toni Jones", "date-of-birth": "1984-10-02"}
```

## [](#create-your-bucket-scope-and-collections)Create your bucket, scope, and collections.

You will need to create the bucket, scope, and collections to hold the data on your Couchbase cluster.

For information on creating buckets, scopes, and collections, read the sections on [Managing Buckets](../../manage/manage-buckets/bucket-management-overview.md)and [Managing Scopes and Collections](../../manage/manage-scopes-and-collections/manage-scopes-and-collections.md)

---

Set up your cluster

1. Using the Couchbase admin console, the command line tool, or the REST API, create a new bucket on your cluster called `student-bucket`.
2. Create a new scope called `art-school-scope` within `student-bucket`.
3. Create two new collections (`student-record-collection` and `course-record-collection`) inside `art-school-scope`.

## [](#import-your-data)Import your data

In this step, you will use `cbimport` to load your two JSON files into your cluster.

---

Import the course data

Use the following command to import `courses.json` into your cluster.

```console
./cbimport json --cluster 127.0.0.1:8091 \
 --username Administrator --password password \
 --bucket student-bucket \
 --dataset file:///var/lib/mysql-files/courses.json \
 --format lines \
 --generate-key %course-id% \
 --scope-collection-exp art-school-scope.course-record-collection
```

The parameters used are as follows:

| \--cluster              | The address and port of the Couchbase cluster receiving the imported data.                                                                                                                                                                                                                                                                                         |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| \--username             | A valid admin-level user to log on to the cluster                                                                                                                                                                                                                                                                                                                  |
| \--bucket               | The name of the destination bucket for the imported data.                                                                                                                                                                                                                                                                                                          |
| \--dataset              | The full path of the JSON file where the import data can be found. Remember to include the file::// prefix.                                                                                                                                                                                                                                                        |
| \--format               | This is the of the JSON data that cbimport is importing. The value can be lines or lists. For this exercise, the value should be set to lines. For a detailed explanation of the \--format, see [Dataset formats](../../tools/cbimport-json.md#DATASET%5FFORMATS).                                                                                                 |
| \--generate-key         | This tells cbimport how to generate the key for the imported data. You can use any combination of fields in the data to generate the key. In this exercise, we simply set the key to match the course-id field in the imported data.                                                                                                                               |
| \--scope-collection-exp | This defines an expression that tells cbimport which scope and collection the data will be imported to. The expression can be a static value (as we have used above), or a combination of field identifiers from the import data. For more information, see the section on the [Scope/Collection Parser](../../tools/cbimport-json.md#SCOPE%5FCOLLECTION%5FPARSER) |

---

Import the student data

The student JSON file can be imported in much the same way:

```console
./cbimport json --cluster 127.0.0.1:8091 \
--username Administrator \
--password password \
--bucket student-bucket \
--dataset file:///var/lib/mysql-files/students.json \
--format lines \
--generate-key %student-id% \
--scope-collection-exp art-school-scope.student-record-collection
```

## [](#check-your-data)Check your data

Use the web admin console to examine your imported records to make sure they are correct.

![cbimported data](../_images/cbimported-data.png) 

## [](#further-reading)Further reading

For more information about `cbimport`, read the [cbimport guide](../../tools/cbimport.md).

If you would like to know more about MySQL JSON functions, then you will find a comprehensive reference [here](https://dev.mysql.com/doc/refman/9.2/en/json-function-reference.html).