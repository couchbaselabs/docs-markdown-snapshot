---
title: Configuring S3-Compatible Storage
description: You can set up Couchbase Operational Insights to use an
  S3-Compatible storage solution.
pubDate: 2026-10-19T14:21:08.937Z
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