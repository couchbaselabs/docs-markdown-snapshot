---
title: Configuring S3-Compatible Storage
description: You can set up Couchbase Enterprise Analytics to use an
  S3-Compatible storage solution.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/manage/pages/manage-nodes/s3-compatible-storage.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:2.1@enterprise-analytics:manage:manage-nodes/s3-compatible-storage.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.1/manage/manage-nodes/s3-compatible-storage.html)

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
> Enterprise Analytics has been certified with NetApp StorageGRID v11.9.0.6 or later.

Enterprise Analytics supports the following S3-compatible storage providers. Select your storage provider to view the configuration steps.

* NetApp StorageGRID
* OCI Object Storage

To use Enterprise Analytics with NetApp StorageGRID, you must:

1. [Create a NetApp StorageGRID bucket](#create-bucket).
2. [Configure NetApp StorageGRID credentials](#configure-storagegrid-credentials).
3. [Configure S3 Access Credentials](#configure-s3-credentials).
4. [Configure Enterprise Analytics](#configure-storagegrid-ea).

## Create a NetApp StorageGRID bucket

To create a bucket in StorageGRID that Enterprise Analytics uses for storing data:

1. Click **Create Bucket** in the StorageGRID UI.
2. Enter a name for the bucket, for example, `samplebucket`.
3. Select region `us-east-1` or the region you want to use.
4. Click **Continue** to create the bucket.
5. Click **Create bucket**.
6. In **Bucket options** tab, select **All**, this provides the highest guarantee of consistency.

## Configure NetApp StorageGRID credentials

Create the **Access key ID** and **Secret access key** for the bucket in StorageGRID. For more information about creating access keys, see the [NetApp StorageGRID documentation](https://docs.netapp.com/us-en/storagegrid/tenant/creating-your-own-s3-access-keys.html). Enterprise Analytics uses these credentials to connect to the bucket.

1. In the **Create access key** page, **Do not set an expiration time** is selected by default.
2. Click **Create access key** to generate the access key.

## Configure S3 Access Credentials

You should place the credentials file in the `.aws` directory in the `Couchbase` user's home directory. For example, `/home/couchbase/.aws/credentials` & `chmod’d` to `600` as a security best practice. Make sure to enter the credentials under the default profile. For more information about how to set configuration and credential files in the AWS command-line tool, see the [AWS documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html). You can verify that each node was properly configured using the AWS CLI:

```none
aws s3 ls s3://bucket/prefix/ --endpoint-url https://storagegrid-endpoint.com
```

If your credentials have not been properly configured, the AWS CLI returns:

```none
$ aws s3 ls s3://bucket/prefix/ --endpoint-url https://storagegrid-endpoint.com

Unable to locate credentials.
You can configure credentials by running "aws configure".
```

If the credentials are incorrect:

```none
$ aws s3 ls s3://bucket/prefix/ --endpoint-url https://storagegrid-endpoint.com

An error occurred (InvalidAccessKeyId) when calling the ListObjectsV2 operation.
The AWS Access Key Id you provided does not exist in our records.
```

If you have properly configured your credentials, you should see:

```none
$ aws s3 ls s3://bucket/prefix/ --endpoint-url https://storagegrid-endpoint.com
                           PRE subdir/
```

## Configure Enterprise Analytics

Use the Couchbase CLI or REST API to configure each Enterprise Analytics node to use the StorageGRID bucket as its object storage. Copy the **Access key ID** and **Secret access key** to the credentials file.

1. From the UI, choose **S3-Compatible Storage**.
2. Specify the following:

  * StorageGrid Endpoint: for example, <http://mystoragegrid.example.com>
  * Bucket Name: `samplebucket`
  * Bucket Region: `us-east-1`
  * (Optional) Bucket Path Prefix: for example, `sampleprefix/`
3. Make sure to select **Force Path Style**.
4. Click **Save & Finish** to save the configuration.

To use Enterprise Analytics with Oracle Cloud Infrastructure (OCI) Object Storage, you must:

1. [Create an OCI bucket](#create-oci-bucket).
2. [Configure OCI customer-generated keys](#configure-oci-keys).
3. [Configure Access Credentials](#configure-oci-credentials).
4. [Configure Enterprise Analytics](#configure-oci-ea).

## Create an OCI bucket

To create a bucket in OCI that Enterprise Analytics uses for storing data:

1. Go to **Storage** section of OCI, and select **Buckets** from the navigation pane.
2. Click **Create Bucket**. For more information, see the [OCI documentation](https://docs.oracle.com/en/learn/data%5Fobject%5Fstorage/index.html#step-1-create-a-bucket).
3. Enter a name for the bucket, for example, `samplebucket`.
4. Select **Standard** in **Default storage tier**.
5. Click **Create bucket**.

This creates the bucket in the currently selected region.

## Configure OCI customer-generated keys

For more information, see the [OCI S3 compatibility documentation](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/s3compatibleapi.htm).

1. Click the profile.
2. Go to **User settings**.
3. Select the **Token and keys** tab.
4. Navigate to **Customer secret keys**.
5. Click **Generate secret key**.
6. Enter the name of the key and press **Generate secret key** to generate the secret key.
7. Once copied, click **Close** to complete the secret generation.
8. The generated key is the S3 equivalent of **Secret access key**.
9. After creation, you can see a list of keys with **Access key** as a column.
10. Copy the **Access key** — this is the S3 equivalent of **Access Key**.

Make sure the group users belong to has the required permissions. For more information, see the [OCI permissions documentation](https://docs.oracle.com/en/cloud/saas/account-reconcile-cloud/suarc/setup%5Fobject%5Fstorage%5Fattachments%5Fconfig%5Foci.html#GUID-88661617-BB80-4B17-B537-C2F2DA89E6B9).

## Configure Access Credentials

Place the credentials file in the `.aws` directory in the `Couchbase` user's home directory. For example, `/home/couchbase/.aws/credentials` & `chmod’d` to `600` as a security best practice. Make sure to enter the credentials under the default profile. For more information about how to set configuration and credential files in the AWS CLI, see the [AWS documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html).

Since OCI uses a separate [S3 compatible endpoint](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/s3compatibleapi.htm), you must supply it explicitly via `--endpoint-url` when verifying your credentials with the AWS CLI. Following is the format for the endpoint:

```none
https://<namespace>.compat.objectstorage.<region>.oci.customer-oci.com
```

To find the namespace of the bucket, go to the bucket section and click the bucket name. This displays the bucket details.

You can verify that each node was properly configured using the AWS CLI:

```none
aws s3 ls \
  --endpoint-url https://iduq5wp7nui.compat.objectstorage.us-ashburn-1.oraclecloud.com \
  --region us-east-1
```

If your credentials have not been properly configured, the CLI returns:

```none
$ aws s3 ls \
  --endpoint-url https://iduq5wp7nui.compat.objectstorage.us-ashburn-1.oraclecloud.com \
  --region us-east-1

An error occurred (SignatureDoesNotMatch) when calling the ListBuckets operation: The secret key required to complete authentication could not be found.
The region must be specified if this is not the home region for the tenancy.
```

If the credentials are incorrect:

```none
$ aws s3 ls \
  --endpoint-url https://iduq5wp7nui.compat.objectstorage.us-ashburn-1.oraclecloud.com \
  --region us-east-1

An error occurred (SignatureDoesNotMatch) when calling the ListBuckets operation: The required information to complete authentication was not provided.
```

If you have properly configured your credentials, you should see:

```none
$ aws s3 ls \
  --endpoint-url https://iduq5wp7nui.compat.objectstorage.us-ashburn-1.oraclecloud.com \
  --region us-east-1
                           PRE subdir/
```

## Configure Enterprise Analytics

Use the Couchbase CLI or REST API to configure each Enterprise Analytics node to use the OCI bucket as its object storage. Copy the **Access key ID** and **Secret access key** to the credentials file.

1. From the UI, choose **S3-Compatible Storage**.
2. Specify the following:

  * OCI S3 compatible endpoint: for example, `<https://iduq5wp7nui.compat.objectstorage.us-ashburn-1.oraclecloud.com>`
  * Bucket Name: `samplebucket`
  * Bucket Region: `us-east-1`
  * (Optional) Bucket Path Prefix: for example, `sampleprefix/`
3. Make sure to select **Force Path Style**.
4. Click **Save & Finish** to save the configuration.

## [](#next-steps)Next Steps

* [Initialize a Node](initialize-node.md)
* [Create a Cluster](create-cluster.md)
* [Join a Cluster and Rebalance](join-cluster-and-rebalance.md)
* [Manage Nodes and Clusters](node-management-overview.md)
* [Setting Up With Object Storage](object-storage.md)