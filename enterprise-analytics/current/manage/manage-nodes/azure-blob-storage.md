[View original HTML](/enterprise-analytics/current/manage/manage-nodes/azure-blob-storage.html)

> You can set up Couchbase Enterprise Analytics to use Azure Blob Storage as its storage solution. You can deploy Enterprise Analytics (EA) 2.1 on Azure Virtual Machines (VMs) and configure it to use Azure Blob Storage (ABS) for compute-storage separation. 

## [](#prerequisites)Prerequisites

* You have created an Azure Blob Storage (ABS) container on your Azure tenant. For more information, see [Create an Azure storage account](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-portal).
* You have configured all Azure Virtual Machines were you want to deploy Enterprise Analytics to have full read and write access to the ABS container. For more information, see [Assign Azure roles using the Azure portal](https://learn.microsoft.com/en-us/azure/role-based-access-control/role-assignments-portal).
* You have the installer for Enterprise Analytics version 2.1\. For more information, see [Installing Enterprise Analytics](#intro/introduction-linux-installation.adoc).

## [](#cluster-setup)Cluster Setup

Use the Couchbase CLI, UI or REST API to configure each Enterprise Analytics node to use the Azure Blob Storage as its object storage.

|  | You can only configure the blob storage settings during the initial cluster setup. |
|  | ---------------------------------------------------------------------------------- |

### [](#set-up-a-cluster-using-the-ui)Set Up a Cluster Using the UI

To set up Enterprise Analytics to use Azure Blob Storage from the UI:

1. Choose Azure Blob Storage as the Blob Storage Scheme.
2. Provide the following details:

  * Enter the **Blob service endpoint** for your Azure storage account. This is typically found in the Azure portal.
  * Enter the **Container (Bucket) Name** for the container that’s used within the specific storage account endpoint.
  * Enter the **Prefix** (Optional) within that container where EA stores all of its data.

### [](#set-up-a-cluster-using-the-rest-api)Set Up a Cluster Using the REST API

To configure Enterprise Analytics to use an Azure Blob Storage container from the REST API:

1. Set the Analytics blob configuration using the `/settings/analytics` endpoint and the `POST` method:  
```none  
curl --request POST \
  --url http://localhost:8091/settings/analytics \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data blobStorageScheme=azblob \
  --data blobStorageEndpoint=$BLOB_STORAGE_ENDPOINT \
  --data blobStorageBucket=$BLOB_STORAGE_BUCKET \
  --data blobStoragePrefix=$BLOB_STORAGE_PREFIX  
```  
Make sure to include the following `--data` parameters in your request:

  * `blobStorageScheme=azblob`: specifies Azure Blob Storage.
  * `blobStorageEndpoint`: the endpoint URL for your Azure storage account.
  * `blobStorageBucket`: the name of the Azure Blob Storage container.
  * `blobStoragePrefix`: the prefix within the container (optional).
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
Make sure to include the following parameters as part of your request:

  * `username` and `password`: Credentials for the cluster administrator.
  * `services`: The services to be configured (here, kv for Key-Value and cbas for Analytics).
  * `memoryQuota`: Memory allocation for the Key-Value service (in MB).
  * `cbasMemoryQuota`: Memory allocation for the Analytics Service (in MB).
  * `port`: Specifies the port configuration.

## [](#next-steps)Next Steps

* [Initialize a Node](initialize-node.md)