---
title: Cloud Read/Write Permissions for GCS
description: This page outlines the required read and write permissions when
  copying data to or from external cloud providers.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/sources/pages/required-permissions-gcs.adoc
  xref: xref:analytics:sources:required-permissions-gcs.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/analytics/sources/required-permissions-gcs.html)

# Cloud Read/Write Permissions for GCS

> This page outlines the required read and write permissions when copying data to or from external cloud providers. 

Exclusive permissions are required when reading from cloud storage using External Collections or writing to cloud storage using COPY TO statements.

## [](#prerequisites)Prerequisites

Before granting permissions, ensure you have the following:

* A Google Cloud Platform (GCP) account with the necessary administrative privileges.
* Access to the Google Cloud Console.
* The name of the GCS bucket you want to access.

## [](#read-permissions)Read Permissions

You need Read permissions when reading from cloud storage using External Collections.

To grant read permissions to your GCP cloud storage:

1. [Create a Role](#create-role-read).
2. [Add the Role to the Bucket](#add-to-bucket-read).

### [](#create-role-read)Create a Role

To create a new role with the required read permissions:

1. Go to the Google Cloud console.
2. From the **Dashboard**, go to **IAM and Admin** and select **Roles**.
3. Select **Create Role**.
4. Fill in the information (Title, Description, … etc).
5. Select **Add Permissions**.
6. Select the following permissions:

  * `storage.objects.get`
  * `storage.objects.list`
7. Select **Add**.
8. Select **Create**.

### [](#add-to-bucket-read)Add the Role to the Bucket

Add the Google Cloud Platform (GCP) Service Account you want to use with Capella Analytics to the bucket and assign it the role you created:

1. Go to the Google Cloud console.
2. From the **Dashboard**, go to **Cloud Storage** and select **Buckets**.
3. Select the desired bucket.
4. From the **Bucket** page, select the **Permissions** tab.
5. Under **View by Principals**, select **Grant Access**.
6. Under **Add Principal**, add the desired **Service Account**.
7. Under **Assign Roles**, select the **Role** created in the previous steps.

## [](#read-and-write-permissions)Read and Write Permissions

Read and write permissions are needed when writing to cloud storage using COPY TO statements. To grant read and write permissions to your GCP cloud storage:

1. [Create a Role](#create-role-write).
2. [Add the Role to the Bucket](#add-to-bucket-write).

### [](#create-role-write)Create a Role

To create a new role with the required read and write permissions:

1. Go to the Google Cloud console.
2. From the **Dashboard**, go to **IAM and Admin** and select **Roles**.
3. Select **Create Role**.
4. Fill in the information (Title, Description, … etc).
5. Select **Add Permissions**.
6. Select the following permissions:

  * `storage.objects.get`
  * `storage.objects.list`
  * `storage.objects.create`
  * `storage.objects.delete`
7. Select **Add**.
8. Select **Create**.

### [](#add-to-bucket-write)Add the Role to the Bucket

Next, add the Google Cloud Platform (GCP) Service Account to the bucket and assign it the created role:

1. Go to the Google Cloud console.
2. From the **Dashboard**, go to **Cloud Storage** and select **Buckets**.
3. Select the desired bucket.
4. From the **Bucket** page, select the **Permissions** tab.
5. Under **View by Principals**, select **Grant Access**.
6. Under **Add Principal**, add the desired **Service Account**.
7. Under **Assign Roles**, select the **Role** created in the previous steps.

## [](#see-also)See Also

* [Query and Explore with the Workbench](../query/workbench.md)
* [Access and Organize Data in Capella Analytics Services](database-objects.md)
* [Set Up Google Cloud Storage (GCS) External Source](setup-gcs-external-source.md)