---
title: Configuring S3-Compatible Storage
description: You can set up Couchbase Enterprise Analytics to use an
  S3-Compatible storage solution.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/manage/pages/manage-nodes/s3-compatible-storage.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/enterprise-analytics/current/manage/manage-nodes/s3-compatible-storage.html)

# Configuring S3-Compatible Storage

> You can set up Couchbase Enterprise Analytics to use an S3-Compatible storage solution. While AWS S3 is fully supported, third-party storage systems that implement the S3 API may also work with Enterprise Analytics. However, compatibility is not guaranteed for all S3-compatible solutions, as they must properly implement all required S3 operations. 

To be compatible with Enterprise Analytics, S3-compatible object storage must have strong and global consistency for bucket updates and support the following operations:

* [GetObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API%5FGetObject.html)
* [PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API%5FPutObject.html)
* [DeleteObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API%5FDeleteObject.html)
* [DeleteObjects](https://docs.aws.amazon.com/AmazonS3/latest/API/API%5FDeleteObjects.html)
* [CopyObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API%5FCopyObject.html)
* [HeadObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API%5FHeadObject.html)
* [ListObjectsV2](https://docs.aws.amazon.com/AmazonS3/latest/API/API%5FListObjectsV2.html)
* [CreateMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API%5FCreateMultipartUpload.html)
* [UploadPart](https://docs.aws.amazon.com/AmazonS3/latest/API/API%5FUploadPart.html)
* [CompleteMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API%5FCompleteMultipartUpload.html)
* [AbortMultipartUpload](https://docs.aws.amazon.com/AmazonS3/latest/API/API%5FAbortMultipartUpload.html)
* [GetBucketLocation](https://docs.aws.amazon.com/AmazonS3/latest/API/API%5FGetBucketLocation.html)

> [!IMPORTANT]
> Enterprise Analytics has been certified with NetApp StorageGRID v11.9.0.6 or later. Other S3-compatible storage has not yet been verified.

To use Enterprise Analytics with NetApp StorageGRID, you must:

1. [Create a NetApp StorageGRID bucket](#create-bucket).
2. [Configure NetApp StorageGRID credentials](#configure-storagegrid-credentials).
3. [Configure S3 Access Credentials](#configure-s3-credentials).
4. [Configure Enterprise Analytics](#configure-ea).

## [](#create-bucket)Create a NetApp StorageGRID bucket

To create a bucket in StorageGRID that Enterprise Analytics uses for storing data:

1. Click **Create Bucket** in the StorageGRID UI.
2. Enter a name for the bucket, for example, `samplebucket`.
3. Select region `us-east-1` or the region you want to use.
4. Click **Continue** to create the bucket.
5. Click **Create bucket**.
6. In **Bucket options** tab, select **All**, this provides the highest guarantee of consistency.

## [](#configure-storagegrid-credentials)Configure NetApp StorageGRID credentials

Create the **Access key ID** and **Secret access key** for the bucket in StorageGRID. For more information about creating access keys, see the [NetApp StorageGRID documentation](https://docs.netapp.com/us-en/storagegrid/tenant/creating-your-own-s3-access-keys.html). Enterprise Analytics uses these credentials to access the bucket.

1. In the **Create access key** page, **Do not set an expiration time** is selected by default.
2. Click **Create access key** to generate the access key.

## [](#configure-s3-credentials)Configure S3 Access Credentials

You should place the credentials file in the `.aws` directory in the `Couchbase` user’s home directory. For example, `/home/couchbase/.aws/credentials` & `chmod’d` to `600` as a security best practice. Make sure to enter the credentials under the default profile. For more information about how to set configuration and credential files in the AWS CLI, see the [AWS documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html). You can verify that each node was properly configured using AWS CLI:

```none
aws s3 ls s3://bucket/prefix/ --endpoint-url https://storagegrid-endpoint.com
```

If your credentials have not been correctly configured, the CLI returns:

```none
$ aws s3 ls s3://bucket/prefix/ --endpoint-url https://storagegrid-endpoint.com

Unable to locate credentials.
You can configure credentials by running "aws configure".
```

If the credentials are incorrect:

```none
$ aws s3 ls s3://bucket/prefix/ --endpoint-url https://storagegrid-endpoint.com

An error occurred (InvalidAccessKeyId) when calling the ListObjectsV2 operation. The AWS Access Key Id you provided does not exist in our records.
```

If you correctly configured your credentials, you should see:

```none
$ aws s3 ls s3://bucket/prefix/ --endpoint-url https://storagegrid-endpoint.com
                           PRE subdir/
```

## [](#configure-ea)Configure Enterprise Analytics

Use the Couchbase CLI or REST API to configure each Enterprise Analytics node to use the StorageGRID bucket as its object storage. Copy the **Access key ID** and **Secret access key** to the credentials file.

1. From the UI, choose **S3-Compatible Storage**.
2. Specify the following:

  * StorageGrid Endpoint: for example, <http://mystoragegrid.example.com>
  * Bucket Name: `samplebucket`
  * Bucket Region: `us-east-1`
  * (Optional) Bucket Path Prefix: for example, `sampleprefix/`
3. Make sure to check **Force Path Style**.
4. Click **Save & Finish** to save the configuration.

## [](#next-steps)Next Steps

* [Initialize a Node](initialize-node.md)