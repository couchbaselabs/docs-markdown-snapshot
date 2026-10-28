---
title: Configuring AWS S3 Storage
description: You can set up Couchbase Operational Insights to use Amazon S3 as
  its storage solution.
pubDate: 2026-10-28T04:21:06.350Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/manage/pages/manage-nodes/aws-s3.adoc
  xref: xref:enterprise-analytics:manage:manage-nodes/aws-s3.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/manage/manage-nodes/aws-s3.html)

# Configuring AWS S3 Storage

> You can set up Couchbase Operational Insights to use Amazon S3 as its storage solution. Your Operational Insights cluster can then read and store data from an Amazon S3 bucket. Each node in an Operational Insights cluster must have access to the configured bucket either using an AWS access policy or credentials file. 

## [](#configure-s3-access-credentials)Configure S3 Access Credentials

To enable Operational Insights nodes to access your S3 bucket, you need to set up proper authentication credentials. For each node on your cluster:

1. Place the credentials file in the `.aws` directory in the Couchbase user's home directory. For example, `/home/couchbase/.aws/credentials` & `chmod’d` to `600` as a security best practice.
2. Make sure to enter the credentials under the default profile. For more information about how to set configuration and credential files in the AWS CLI, see the [AWS documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html).
3. Use the AWS CLI to confirm that each node was properly configured:  
```console  
aws s3 ls s3://bucket/prefix/  
```

If your credentials have not been correctly configured, the CLI returns:

```none
$ aws s3 ls s3://bucket/prefix/
Unable to locate credentials.
You can configure credentials by running "aws configure".
```

If the credentials are incorrect:

```none
$ aws s3 ls s3://bucket/prefix/

An error occurred (InvalidAccessKeyId) when calling the ListObjectsV2 operation. The AWS Access Key Id you provided does not exist in our records.
```

If you correctly configured your credentials, you should see:

```none
$ aws s3 ls s3://bucket/prefix/
                           PRE subdir/
```

## [](#cluster-setup)Cluster Setup

Use the Couchbase UI or REST API to configure Operational Insights to use Amazon S3 as its object storage.

> [!NOTE]
> You can only configure the blob storage settings during the initial cluster setup.

### [](#set-up-a-cluster-using-the-ui)Set Up a Cluster Using the UI

To set up Operational Insights to use Amazon S3 from the UI:

1. Choose **AWS S3** as the **Storage Scheme**.
2. Provide the following details:

  * Enter the **Bucket Name** for the S3 bucket where Operational Insights stores all of its data.
  * Enter the **Bucket Region** of the S3 bucket.
  * Enter the **Bucket Path Prefix** (optional) within that bucket where Operational Insights stores all of its data.

### [](#set-up-a-cluster-using-the-rest-api)Set Up a Cluster Using the REST API

To configure Operational Insights to use an S3 bucket from the REST API:

1. Configure the object storage using the `/settings/operationalInsights` endpoint and the `POST` method:  
```none  
curl --request POST \
  --url http://localhost:8091/settings/operationalInsights \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data blobStorageScheme=s3 \
  --data blobStorageBucket=$S3_BUCKET_NAME \
  --data blobStorageRegion=$S3_BUCKET_REGION \
  --data blobStoragePrefix=$S3_BUCKET_PREFIX  
```  
You must include the following `--data` parameters in your request:

  * `blobStorageScheme=s3`: specifies Amazon S3.
  * `blobStorageBucket`: the name of the S3 bucket.
  * `blobStorageRegion`: the AWS region of the S3 bucket.
  * `blobStoragePrefix`: the prefix within the bucket (optional).  
  If you do not use a credentials file or an AWS access policy, you can instead supply static credentials with the `blobStorageAccessKeyId` and `blobStorageSecretAccessKey` parameters.
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