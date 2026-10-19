---
title: Certified Solutions
description: Operational Insights has been certified with the following
  S3-compatible object storage solutions.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/manage/pages/manage-nodes/certified-solutions.adoc
  xref: xref:enterprise-analytics:manage:manage-nodes/certified-solutions.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/manage/manage-nodes/certified-solutions.html)

# Certified Solutions

> Operational Insights has been certified with the following S3-compatible object storage solutions. 

This page lists the S3-compatible object storage solutions that Operational Insights has certified.

## [](#netapp-storagegrid)NetApp StorageGRID

Operational Insights has been certified with NetApp StorageGRID v11.9.0.6 or later.

To use Operational Insights with NetApp StorageGRID, you must:

1. [Create a NetApp StorageGRID bucket](#create-bucket).
2. [Configure NetApp StorageGRID credentials](#configure-storagegrid-credentials).
3. [Configure S3 Access Credentials](#configure-s3-credentials).
4. [Configure Operational Insights](#configure-operational-insights).

### [](#create-bucket)Create a NetApp StorageGRID bucket

To create a bucket in StorageGRID that Operational Insights uses for storing data:

1. Click **Create Bucket** in the StorageGRID UI.
2. Enter a name for the bucket, for example, `samplebucket`.
3. Select region `us-east-1` or the region you want to use.
4. Click **Continue** to create the bucket.
5. Click **Create bucket**.
6. In **Bucket options** tab, select **All**, this provides the highest guarantee of consistency.

### [](#configure-storagegrid-credentials)Configure NetApp StorageGRID credentials

Create the **Access key ID** and **Secret access key** for the bucket in StorageGRID. For more information about creating access keys, see the [NetApp StorageGRID documentation](https://docs.netapp.com/us-en/storagegrid/tenant/creating-your-own-s3-access-keys.html). Operational Insights uses these credentials to access the bucket.

1. In the **Create access key** page, **Do not set an expiration time** is selected by default.
2. Click **Create access key** to generate the access key.

### [](#configure-s3-credentials)Configure S3 Access Credentials

You should place the credentials file in the `.aws` directory in the `Couchbase` user's home directory. For example, `/home/couchbase/.aws/credentials` & `chmod’d` to `600` as a security best practice. Make sure to enter the credentials under the default profile. For more information about how to set configuration and credential files in the AWS CLI, see the [AWS documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html). You can verify that each node was properly configured using AWS CLI:

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

### [](#configure-operational-insights)Configure Operational Insights

Use the Couchbase CLI or REST API to configure each Operational Insights node to use the StorageGRID bucket as its object storage. Copy the **Access key ID** and **Secret access key** to the credentials file.

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