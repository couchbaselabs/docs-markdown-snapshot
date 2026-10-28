---
title: Configuring S3-Compatible Storage
description: You can set up Couchbase Operational Insights to use an
  S3-Compatible storage solution.
pubDate: 2026-10-28T04:21:06.350Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/manage/pages/manage-nodes/s3-compatible-storage.adoc
  xref: xref:enterprise-analytics:manage:manage-nodes/s3-compatible-storage.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/manage/manage-nodes/s3-compatible-storage.html)

# Configuring S3-Compatible Storage

> You can set up Couchbase Operational Insights to use an S3-Compatible storage solution. While AWS S3 is fully supported, third-party storage systems that implement the S3 API may also work with Operational Insights. However, compatibility is not guaranteed for all S3-compatible solutions, as they must properly implement all required S3 operations. 

To be compatible with Operational Insights, S3-compatible object storage must have strong and global consistency for bucket updates and support the following operations:

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

  * For solutions Operational Insights has certified, and step-by-step setup instructions, see [Certified Solutions](certified-solutions.md).
  * For other S3-compatible solutions that implement the required operations but are not certified, see [Compatible Solutions](compatible-solutions.md).

## [](#cluster-setup)Cluster Setup

Use the Couchbase UI or REST API to configure Operational Insights to use an S3-compatible storage service as its object storage. Before you start, configure the S3 access credentials on each node, as described in [Configuring AWS S3 Storage](aws-s3.md). When you verify the credentials, use the `--endpoint-url` option of the AWS CLI to point to your storage service.

> [!NOTE]
> You can only configure the blob storage settings during the initial cluster setup.

### [](#set-up-a-cluster-using-the-ui)Set Up a Cluster Using the UI

To set up Operational Insights to use S3-compatible storage from the UI:

1. Choose **S3-Compatible Storage** as the **Storage Scheme**.
2. Provide the following details:

  * Enter the **Storage Endpoint** URL of your S3-compatible storage service.
  * Enter the **Bucket Name** for the bucket where Operational Insights stores all of its data.
  * Enter the **Bucket Region** of the bucket.
  * Enter the **Bucket Path Prefix** (optional) within that bucket where Operational Insights stores all of its data.
3. Click **Use Path-Style Addressing** if your storage service requires path-style addressing.

### [](#set-up-a-cluster-using-the-rest-api)Set Up a Cluster Using the REST API

To configure Operational Insights to use S3-compatible storage from the REST API:

1. Configure the object storage using the `/settings/operationalInsights` endpoint and the `POST` method:  
```none  
curl --request POST \
  --url http://localhost:8091/settings/operationalInsights \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data blobStorageScheme=s3 \
  --data blobStorageEndpoint=$BLOB_STORAGE_ENDPOINT \
  --data blobStorageBucket=$BLOB_STORAGE_BUCKET \
  --data blobStorageRegion=$BLOB_STORAGE_REGION \
  --data blobStoragePrefix=$BLOB_STORAGE_PREFIX \
  --data blobStoragePathStyleAddressing=true  
```  
You must include the following `--data` parameters in your request:

  * `blobStorageScheme=s3`: specifies S3 or S3-compatible storage.
  * `blobStorageEndpoint`: the endpoint URL of your S3-compatible storage service.
  * `blobStorageBucket`: the name of the bucket.
  * `blobStorageRegion`: the region of the bucket.
  * `blobStoragePrefix`: the prefix within the bucket (optional).
  * `blobStoragePathStyleAddressing`: set to `true` if your storage service requires path-style addressing (optional).  
  If your storage service uses a certificate signed by a private certificate authority, supply it with the `blobStorageCertificates` parameter.
2. Initialize the cluster using the `POST` method on the `/clusterInit` endpoint. For example:  
```none  
curl -X POST http://localhost:8091/clusterInit \
-d 'username=$ADMIN_USERNAME' \
-d 'password=$ADMIN_PASSWORD' \
-d 'memoryQuota=100' \
-d 'cbasMemoryQuota=$CBAS_MEMORY_QUOTA' \
-d 'port=SAME'  
```  
You must include the following parameters as part of your request:

  * `username` and `password`: Credentials for the cluster administrator.
  * `memoryQuota`: A memory quota, in MiB. Operational Insights fixes this quota at 100 MiB, so always set it to `100`. If you omit it, the node uses a quota based on its total memory instead.
  * `cbasMemoryQuota`: Memory allocation for the Analytics Service, in MiB.
  * `port`: Specifies the port configuration.

## [](#next-steps)Next Steps

* [Initialize a Node](initialize-node.md)