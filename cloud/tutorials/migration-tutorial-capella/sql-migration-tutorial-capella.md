---
title: "Migration Tutorial: Migrate your Data from MySQL to Couchbase Capella"
description: Using MySQL as a starting point, this guide demonstrates how to
  migrate your existing data from SQL tables to a Couchbase Capella instance.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-devex/edit/capella/modules/tutorials/pages/migration-tutorial-capella/sql-migration-tutorial-capella.adoc
  xref: xref:cloud:tutorials:migration-tutorial-capella/sql-migration-tutorial-capella.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/tutorials/migration-tutorial-capella/sql-migration-tutorial-capella.html)

# Migration Tutorial: Migrate your Data from MySQL to Couchbase Capella

> Using MySQL as a starting point, this guide demonstrates how to migrate your existing data from SQL tables to a Couchbase Capella instance. 

## [](#introduction)Introduction

In this tutorial, you will make use of `cbimport` to migrate an example test database from MySQL to Couchbase Capella.

## [](#prerequisites)Prerequisites

Before you make a start, you will need a Capella instance to run the tutorial. If you do not currently have an instance, then you can create a Capella trial here ⇒ [Capella Trial](https://www.couchbase.com/downloads/?family=capella)

You will also need to download and install the Server Development Tools package, which includes the `cbimport` command line application. You will find installation instructions for the Server Development Tools package here ⇒ [Server Development Tools package](../../../server/current/cli/cli-intro.md#server-developer-tools-package)

If you're running through the examples, then you will also need an existing MySQL installation with the preexisting table structure defined in [the following section](#student-record-sql-database-section).

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

Fortunately, MySQL has a number of SQL functions that make working with JSON data fairly straightforward, so we'll start by migrating the `course` table into a JSON file:

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
> Strictly speaking, the JSON output is not a well-formed JSON document because it isn't structured as an array. Nevertheless, `cbimport` will read each line as a separate record.

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

## [](#create-your-cluster-bucket-scope-and-collections)Create your cluster, bucket, scope, and collections

Working on your Capella instance, you must first create the cluster (or use an existing cluster if you have one available). We will assume that you are creating a cluster from scratch. You will also need to create the bucket, scope, and collections to accept the student data.

---

Create the cluster.

1. Sign in to the Capella UI.
2. Go to **Projects**.
3. Click **Create Project**. This will take you to a dialog from where you can fill in the name of your new project.  
![create project](../_images/create-project.png)
4. Enter a name for your project, then press **Create Project**
5. Capella will create a new project for you and then switch back to the Project List. You can navigate to your project by clicking on the link in the top left of the screen.  
> [!TIP]  
> You can also navigate to your project by finding it in the Project List and clicking on its link.
6. On your project page, click on **Create Cluster**  
![create cluster](../_images/create-cluster.png)
7. Select your cluster options (you may use the _free_ option if it's available), then press **Create Cluster**. After a short interval, your new cluster will be provisioned.  
![new cluster](../_images/new-cluster.png)

---

Create a bucket, scope, and collection for each cluster

Now that we have created the cluster, we need to add a location to hold the migrated data.

1. Click on the name of your cluster from the Operational Clusters page. This will take you to the Cluster details page.  
![cluster details](../_images/cluster-details.png)
2. From here, click on the **Import Data** button. This will take you to the **Data Tools** page.  
![data tools](../_images/data-tools.png)
3. Select **Load with cbimport** in the central panel.
4. Click on the **+Create** button in the panel on the left. You will now be presented with a dialog for creating a bucket.  
![create bucket](../_images/create-bucket.png)
5. Fill in `student-bucket` for the name of your bucket.
6. Fill in `art-school-scope` for the scope.
7. Fill in `student-record-collection` for the collection inside the scope.
8. Click on **Create**
9. We still need to create another collection to hold the course records, so press **+Create** again.  
![add course record collection](../_images/add-course-record-collection.png)
10. Make sure that you are adding to an _existing_ bucket (`student-bucket`) and scope (`art-school-scope`). Now add another collection: `course-record-collectiomn`.

---

Allow your IP Address

Before running `cbimport` from your local machine, you need to add your machine's IP address to Capella's allowed list. Navigate to your cluster's security settings and add your IP to the "Allowed IP addresses" list.

1. Click on **Settings** from the top level menu.  
![settings menu](../_images/settings-menu.png)
2. From the left-hand menu, select **Networking** **Allowed IP Addresses**
3. Click the **\+ Add Allowed IP** button.
4. From the **Allowed IP** screen, click on **Add Current IP address**, then click **Add Allowed IP**  
![capella add allowed ip address](../_images/capella-add-allowed-ip-address.png)

---

Set up cluster access credentials

When running `cbimport`, authentication credentials are required, which you can set up from **Security** in Capella.

1. From the **Settings** page, select **Security** **Cluster Access**
2. Click on the **\+ Create Cluster Access** button.  
![new cluster access](../_images/new-cluster-access.png)
3. Type `import` into the `Cluster Access Name` field with.
4. Add a password.
5. In the `Bucket Level Access` section, select `student-bucket` for the bucket, `All Scopes` for the scope, and `Read/Write` for Access:  
![completed access page](../_images/completed-access-page.png)
6. Click on **Create Cluster Access** when you're done.

---

Download your security certificate

To run `cbimport`, you will need to supply the security certificate for your Capella instance, which you can download from the **settings** page.

1. From the top menu, click on **Settings**  
![settings menu](../_images/settings-menu.png)
2. Now, from the **Cluster Settings** screen, click on **Security** **Security Certificates** in the left-hand menu.  
![access security certificate](../_images/access-security-certificate.png)
3. On the **Security Certificate** page, click on **Download** to download your security certificate for the local machine.  
> [!TIP]  
> Make a note of the location where you stored it.
4. Return to the **Data Tools** page by clicking on the link in the top level menu.

## [](#generate-and-execute-your-cbimport-command)Generate and execute your `cbimport` command.

The data tooling page can generate a correctly formatted `cbimport` command line based on your import data. All you need to do is copy the command to your command line environment and fill in details such as your access password and the location of your security certificate.

---

Create the `cbimport` command.

1. From the **Data Tools** page, click on **Load with cbimport** in the central panel.  
![select cbimport](../_images/select-cbimport.png)
2. Locate the `courses` JSON file you created in the [Extract your Course data from MySQL](#extract-sql-data) section, then drag it into the `Upload Sample File` section in the central panel.  
> [!TIP]  
> Alternatively, you can click on `Choose a file` and load the file directly from the file chooser.
3. In the `Choose your target` section, select the `student-bucket`, `art-school-scope`, and the `course-record-collection`.
4. For `Document keys`, select `Field`, then pick the `course-id` field from the dropdown list.

---

The `Copy generated command` field will contain the `cbimport` statement you will need to execute the import:

`cbimport` command

```shell
cbimport json --format lines --cluster couchbases://cb.wrrmzje92urkkyn.customsubdomain.nonprod-project-avengers.com --username <<username>> --password '<<password>>' --bucket "student-bucket" --scope-collection-exp "art-school-scope.course-record-collection" --dataset 'file://<<path>>/courses.json' --generate-key '%`course-id`%' --cacert <<path to downloaded cert file>>
```

Before you can run the command, you will need to fill in the placeholders with information from your cluster:

* Username and password. These are the details you created in the [Set up cluster access credentials](#set-up-cluster-access-credentials) section.
* the full path to your input source (`courses.json`)
* the full path to your downloaded security certificate, which you downloaded in the [Download your security certificate](#download-security-certificate) section.

Your command should resemble the following:

```shell
./cbimport json --format lines \
--cluster couchbases://cb.wrrmzje92urkkyn.customsubdomain.nonprod-project-avengers.com \
--username import --password 'Password' \
--bucket "student-bucket" --scope-collection-exp "art-school-scope.course-record-collection" \
--dataset 'file:///Users/test/courses.json' \
--generate-key '%`course-id`%' \
--cacert /Users/test/Cluster-1-root-certificate.txt
```

You can repeat the same process to generate and run a `cbimport` command for the `students.json` file. Remember to:

1. Change the `--scope-collection-exp` parameter to point to `art-school-scope.student-record-collection`.
2. Set the `--dataset` parameter to point to the `students.json` file.
3. Set the `--generate-key` parameter to `` '%`course-id`%' ``

## [](#check-your-data)Check your data

You can use Capella's **Data Tools** to check your data has been imported correctly.

![view data](../_images/view-data.png)