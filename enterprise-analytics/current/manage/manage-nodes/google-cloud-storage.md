---
title: Configuring Google Cloud Storage (GCS)
description: You can set up Couchbase Enterprise Analytics to use Google Cloud
  Storage as its storage solution.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/manage/pages/manage-nodes/google-cloud-storage.adoc
  xref: xref:enterprise-analytics:manage:manage-nodes/google-cloud-storage.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/manage/manage-nodes/google-cloud-storage.html)

# Configuring Google Cloud Storage (GCS)

> You can set up Couchbase Enterprise Analytics to use Google Cloud Storage as its storage solution. You can deploy Enterprise Analytics (EA) 2.2 and later on Google Cloud Platform (GCP) and configure it to use Google Cloud Storage (GCS) for compute-storage separation. 

## [](#prerequisites)Prerequisites

* You have created a GCS bucket on your Google Cloud project. For more information, see [Create buckets](https://cloud.google.com/storage/docs/creating-buckets) in the Google Cloud documentation.
* You have created a GCP Service Account with read and write permissions to the GCS bucket, and attached it to each VM where you want to deploy Enterprise Analytics. The VM automatically discovers the Service Account credentials from the GCP metadata server — no credentials file is required on the VM. For more information, see [Service accounts overview](https://cloud.google.com/iam/docs/service-account-overview) and [Create and enable service accounts for instances](https://cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances) in the Google Cloud documentation.
* You have the installer for Enterprise Analytics version 2.2\. For more information, see [Installing Enterprise Analytics](#intro:introduction-linux-installation.adoc).

## [](#cluster-setup)Cluster Setup

Use the Couchbase UI or REST API to configure Enterprise Analytics to use Google Cloud Storage as its object storage.

> [!NOTE]
> You can only configure the blob storage settings during the initial cluster setup.

### [](#set-up-a-cluster-using-the-ui)Set Up a Cluster Using the UI

To set up Enterprise Analytics to use Google Cloud Storage from the UI:

1. Choose **Google Cloud Storage** as the Blob Storage Scheme.
2. Provide the following details:

  * Enter the **Bucket Name** for the GCS bucket where EA stores all of its data.
  * Enter the **Prefix** (optional) within that bucket where EA stores all of its data.

### [](#set-up-a-cluster-using-the-rest-api)Set Up a Cluster Using the REST API

To configure Enterprise Analytics to use a GCS bucket from the REST API:

1. Set the Analytics blob configuration using the `/settings/analytics` endpoint and the `POST` method:  
```none  
curl --request POST \
  --url http://localhost:8091/settings/analytics \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data blobStorageScheme=gs \
  --data blobStorageBucket=$GCS_BUCKET_NAME \
  --data blobStoragePrefix=$GCS_BUCKET_PREFIX  
```  
You must include the following `--data` parameters in your request:

  * `blobStorageScheme=gs`: specifies Google Cloud Storage.
  * `blobStorageBucket`: the name of the GCS bucket.
  * `blobStoragePrefix`: the prefix within the bucket (optional).
2. Initialize the cluster using the `POST` method on the `/clusterInit` endpoint. For example:  
```none  
curl -X POST http://localhost:8091/clusterInit \
-d 'username=$ADMIN_USERNAME' \
-d 'password=$ADMIN_PASSWORD' \
-d 'services=kv,cbas' \
-d 'memoryQuota=$MEMORY_QUOTA' \
-d 'cbasMemoryQuota=$CBAS_MEMORY_QUOTA' \
-d 'port=SAME'  
```  
You must include the following parameters as part of your request:

  * `username` and `password`: Credentials for the cluster administrator.
  * `services`: The services to be configured (here, `kv` for Key-Value and `cbas` for Analytics).
  * `memoryQuota`: Memory allocation for the Key-Value service (in MB). Recommended to set it to 100 MB.
  * `cbasMemoryQuota`: Memory allocation for the Analytics Service (in MB).
  * `port`: Specifies the port configuration.

## [](#next-steps)Next Steps

* [Initialize a Node](initialize-node.md)