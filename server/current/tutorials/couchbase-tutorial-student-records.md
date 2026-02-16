[View original HTML](/server/current/tutorials/couchbase-tutorial-student-records.html)

> The Student Record System tutorial walks you through downloading and installing Couchbase, and then creating a database to store student records. 

## [](#introduction)Introduction

Couchbase is a schema-less JSON document database designed for high performance, scalability, and fast development. This tutorial teaches you about to the key concepts behind Couchbase and how they differ from traditional SQL database systems like MySQL and Oracle.

|  | This tutorial uses standalone or Docker installations of Couchbase Server. To get started with the Couchbase Capella Cloud service, see [Create a Free Account and Deploy Your Database](../../../cloud/get-started/create-account.md). |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#database-design)Data Model

Your data model consists of three record types:

| student    | Information about individual students, like name and date of birth.                                                                                                         |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| course     | Courses the students can take. Includes course name, faculty, and the number of credit points associated with the course. Students can take more than one course at a time. |
| enrollment | Information related to courses the students are taking. In a relational database, this is usually a link record that creates a relationship between a student and a course. |

### [](#relational-model)Relational Model

In a relational model, the database contains a list of students and a list of courses. Each student can enroll in multiple courses.

A student’s enrollment record is stored in a separate table called `enrollment`, which links that record to the courses they’re enrolling in.

![student-record-erd](_images/student-record-erd-0e190ebb29530e06a5d6984a70841b3ecd966c41.svg) 

The `enrollment` table highlights a challenge with the relational model: each table is based on a fixed schema that only supports a single data object type, which means you cannot store a student in the same table as their enrollment record.

### [](#document-model)Document Model

Couchbase uses a document model that stores each record as a JSON document. The document model:

* Contains simple scalar types and complex types, like nested records and arrays
* Lets you store complex types without decomposing them to a second table

In this tutorial, the document model stores the list of enrollment records with the student records. Each enrollment record contains a reference to the course that it relates to.

![student-document-database-design](_images/student-document-database-design-f437e457810966f04ff9fc2bc2ecdbb5327ce938.svg) 

With JSON, you can change the structure of the document without having to rebuild schemas. For example, you can add a new field to store students' email addresses without migrating existing data to a new schema.

In a document database, a student’s record and their course records can look similar to this:

Student record

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

Art History course record

```json
{
  "course-id": "ART-HISTORY-00003",
  "course-name": "art history",
  "faculty": "fine art",
  "credit-points" : 100
}
```

Graphic Design course record

```json
{
  "course-id": "GRAPHIC-DESIGN-00001",
  "course-name": "graphic design",
  "faculty": "media and communication",
  "credit-points" : 200
}
```

Hilary’s enrollment is stored in the same document as her student details, which means child information is stored with its parent. This structure lets you access and retrieve all of Hilary’s details with one search and without the need for complex table joins.

|  | You should not store a student with their course record as it can lead to data duplication and make it difficult to maintain your data. For example, you would need to access every single student record in your cluster to change the credit-points. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

## [](#next-steps)Next Steps

To complete this tutorial, follow these steps:

| Step 1 | [Install Couchbase Server](install-couchbase-server.md)                                  |
| ------ | ---------------------------------------------------------------------------------------- |
| Step 2 | [Implement a Data Model](buckets-scopes-and-collections.md)                              |
| Step 3 | [Set Up and Connect the Couchbase Java SDK](java-tutorial/install-couchbase-java-sdk.md) |
| Step 4 | [Create Student and Course Records](java-tutorial/create-records.md)                     |
| Step 5 | [Retrieve Records](java-tutorial/retrieving-documents.md)                                |
| Step 6 | [Add Course Enrollments](java-tutorial/adding-course-enrollments.md)                     |

For troubleshooting information, see the [troubleshooting page](java-tutorial/tutorial-troubleshooting.md).