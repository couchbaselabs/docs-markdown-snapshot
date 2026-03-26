---
title: Setting Up With Object Storage
description: This page describes how to set up Couchbase Enterprise Analytics
  with Object Storage.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/manage/pages/manage-nodes/object-storage.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.0@enterprise-analytics:manage:manage-nodes/object-storage.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.0/manage/manage-nodes/object-storage.html)

# Setting Up With Object Storage

## [](#object-storage-configuration)Object Storage Configuration

Enterprise Analytics employs compute-storage separation architecture that allows for scaling compute and storage independently. As a result, it requires an object store as its persistent storage. The certified supported object storage solutions are:

* AWS S3
* NetApp StorageGRID

You should configure an Enterprise Analytics cluster with an S3 bucket. Each node in an Enterprise Analytics cluster must have access to the configured bucket either using an AWS access policy or credentials file. Non-certified storage solutions may also be compatible, but need to be able to perform the S3 operations listed preceding.

## [](#configuring-netapp-storagegrid)Configuring NetApp StorageGRID

Enterprise Analytics works with NetApp StorageGRID v11.9.0.6 or later . Setting Enterprise Analytics with NetApp StorageGRID involves the following steps:

### [](#create-a-netapp-storagegrid-bucket)Create a NetApp StorageGRID bucket

Create a bucket in StorageGRID that Enterprise Analytics uses for storing data.

1. Click **Create Bucket** in the StorageGRID UI.
2. Enter a name for the bucket, for example, `samplebucket`.
3. Select region `us-east-1` or the region you want to use.
4. Click **Continue** to create the bucket.
5. Click **Create bucket**. The bucket is created.
6. In **Bucket options** tab, select **All**, this provides the highest guarantee of consistency.

### [](#configure-netapp-storagegrid-credentials)Configure NetApp StorageGRID credentials

Create the **Access key ID** and **Secret access key** for the bucket in StorageGRID. Enterprise Analytics uses these credentials to access the bucket.

1. In the **Create access key** page, **Do not set an expiration time** is selected by default.
2. Click **Create access key** to generate the access key.

### [](#configure-s3-access-credentials)Configure S3 Access Credentials

You should place the credentials file in the '.aws' directory in the 'Couchbase' user's home directory. For example, `/home/couchbase/.aws/credentials` & `chmod’d` to `600` as a security best practice. Make sure to enter the credentials under the default profile. For more details, refer to the [AWS credentials](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html). You can verify that each node was properly configured using AWS CLI:

```none
aws s3 ls s3://bucket/prefix/ --endpoint-url https://storagegrid-endpoint.com
```

### [](#configure-enterprise-analytics)Configure Enterprise Analytics

Use the Couchbase CLI or REST API to configure each Enterprise Analytics node to use the StorageGRID bucket as its object storage. Copy the **Access key ID** and **Secret access key** to the credentials file.

1. From the UI, choose "S3-Compatible Storage".
2. Specify the following:

  * StorageGrid Endpoint: for example, <http://mystoragegrid.example.com>
  * Bucket Name: `samplebucket`
  * Bucket Region: `us-east-1`
  * Optionally Bucket Path Prefix: for example, `sampleprefix/`
3. Make sure to check **Force Path Style**.
4. Click **Save & Finish** to save the configuration.

#### [](#required-object-storage-operations)Required Object Storage Operations

Other non-certified S3-compatible object storage solutions may be functional, and need to support the following operations:

* S3-compatible object storage that supports:

  * Strong, global consistency for bucket updates.
  * At least the following S3 operations:

    * GetObject
    * PutObject
    * DeleteObject
    * CopyObject
    * HeadObject
    * ListObjectsV2
    * UploadPart
    * CreateMultipartUpload
    * CompleteMultipartUpload
    * AbortMultipartUpload
    * GetBucketLocation

## [](#next-steps)Next Steps

* [Initialize a Node](initialize-node.md)