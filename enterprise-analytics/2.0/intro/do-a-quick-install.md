---
title: Do a Quick Install
description: First-time users can get Enterprise Analytics running simply and
  rapidly by using Docker. Once you install Docker, you can use a single command
  to download and install Enterprise Analytics on your computer.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/intro/pages/do-a-quick-install.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.0@enterprise-analytics:intro:do-a-quick-install.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.0/intro/do-a-quick-install.html)

# Do a Quick Install

> First-time users can get Enterprise Analytics running simply and rapidly by using Docker. Once you install Docker, you can use a single command to download and install Enterprise Analytics on your computer. 

## [](#install-enterprise-analytics-using-docker)Install Enterprise Analytics using Docker

This guide walks you through running Couchbase Enterprise Analytics in Docker and configuring it to use [Adobe S3Mock](https://github.com/adobe/S3Mock) as its blob storage backend — ideal for local development and testing without relying on real AWS S3 infrastructure or appliance.

Prerequisites:

* Docker Desktop installed (macOS, Windows, or Linux)
* No other services using ports `8091`, `8095`, or `9190`
* No existing Docker containers named `s3mock` or `ea`

### [](#step-by-step-setup)Step-by-Step Setup

#### [](#1-start-the-s3mock-container)1\. Start the S3Mock Container

We use S3Mock to emulate AWS S3 behavior locally. This container exposes an S3-compatible REST API on port `9090`.

docker run -d --rm --name s3mock \
  -p 9090:9090 \
  -e initialBuckets=cloud-storage-container \
  adobe/s3mock

This creates a bucket named cloud-storage-container for Enterprise Analytics to use.

#### [](#2-start-the-couchbase-enterprise-analytics-container)2\. Start the Couchbase Enterprise Analytics Container

docker run -d --rm -p 8091:8091 -p 8095:8095 --name ea couchbase/enterprise-analytics:2.0.0

This exposes the Enterprise Analytics UI and REST APIs on ports `8091` and `8095` respectively.

#### [](#3-configure-blob-storage-settings)3\. Configure Blob Storage Settings

Once Enterprise Analytics is online, configure it to use the local S3Mock container as its blob storage:

curl -X POST http://localhost:8091/settings/analytics \
  -d blobStorageScheme=s3 \
  -d blobStorageBucket=cloud-storage-container \
  -d blobStorageRegion=us-east-1 \
  -d blobStoragePrefix=cbas/ \
  -d blobStorageEndpoint=http://host.docker.internal:9090 \
  -d numStoragePartitions=16 \
  -d blobStorageAnonymousAuth=true \
  -d blobStoragePathStyleAddressing=true

Explanation of settings:

* `blobStorageScheme`: Use s3 (S3Mock is S3-compatible)
* `blobStorageBucket`: Bucket name created in S3Mock
* `blobStorageEndpoint`: The local S3Mock container's host
* `blobStorageAnonymousAuth=true`: Required, since S3Mock does not use IAM
* `blobStoragePathStyleAddressing=true`: Required, as S3Mock does not support virtual-host-style addressing

##### [](#note-on-blobstorageendpoint-for-linux-users)Note on blobStorageEndpoint for Linux users

The hostname `host.docker.internal` in the command above is not available by default on Linux.

You must replace it with your Docker host's IP address, which you can find with the command:

docker network inspect bridge --format='{{(index .IPAM.Config 0).Gateway}}'

For example, if the command returns 172.17.0.1, set:

-d blobStorageEndpoint=http://172.17.0.1:9090

##### [](#note-on-blobstorageendpoint-for-windows-users)Note on blobStorageEndpoint for Windows users

The command to obtain the Docker host's IP address is:

docker network inspect nat --format='{{(index .IPAM.Config 0).Gateway}}'

#### [](#4-initialize-the-enterprise-analytics-cluster)4\. Initialize the Enterprise Analytics Cluster

Finally, complete the standalone initialization of the Enterprise Analytics cluster:

curl -X POST http://localhost:8091/clusterInit \
  -d username=Administrator \
  -d password=password \
  -d port=SAME

You can now:

* Log in at <http://localhost:8091> using `Administrator`/`password`
* Install the `travel-sample` dataset
* Use the Workbench in the UI to run SQL++ queries, etc.

## [](#setting-up-object-storage)Setting up Object Storage

Enterprise Analytics employs compute-storage separation architecture that allows for scaling compute and storage independently. This section describes how to configure object storage backends like AWS S3 or compatible services for your Enterprise Analytics deployment. See [Object Storage Configuration](../manage/manage-nodes/object-storage.md) for details on setting up certified object storage solutions like AWS S3 or NetApp StorageGRID.

## [](#configure-enterprise-analytics)Configure Enterprise Analytics

For simplicity when getting started, you provision a single node cluster from the Enterprise Analytics Web Console. Access the Web console over the network at <http://<machine-ip-address>:8091/> or <http://<machine-hostname>:8091/>. You can access it locally from the machine where you installed Enterprise Analytics at <http://localhost:8091>.

Once you have connected, the Welcome screen appears.

1. Click **Setup New Cluster** and provide a name for your cluster. For the purpose of getting started, set the full administrator credentials to `Administrator` and `password`.
2. Accept the Terms and Conditions and click **Save and Finish** to complete configuration with default values. You can also choose to **Configure Disk, Memory, Blob Storage** to select only a subset of services for the purpose of this getting started.
3. When you have finished entering your configuration-details, click the **Save & Finish** button, at the lower right. This configures the server accordingly, and brings up the Enterprise Analytics Web Console Dashboard, for the first time.

For more information about configuring Enterprise Analytics, refer to [Configure Enterprise Analytics](../manage/manage-nodes/create-cluster.md#configure-couchbase-server).

## [](#load-the-sample-dataset)Load the Sample Dataset

You must load the sample `travel-sample` dataset to work through the rest of the _Getting Started_ topics.

On the initial screen of the Enterprise Analytics Web Console Workbench, click **Samples** tab.

On the **Samples** screen, select the checkbox for `travel-sample` and then click **Load Sample Data**. The `travel-sample` dataset is now displayed as an available sample dataset.

To learn more about the `travel-sample` dataset and data ingestion from diverse sources, refer to [Connecting to Data Sources](connecting-to-data-sources.md).

## [](#other-destinations)Other Destinations

* [Create a Cluster](../manage/manage-nodes/create-cluster.md): Provides a detailed explanation of how to provision a Enterprise Analytics-node, and thereby create Enterprise Analytics cluster. This is the procedure you'll certainly use in production as well as for testing different configurations. The available options include use of the Enterprise Analytics Web Console, the Couchbase REST API, and the Couchbase Command Line Interface.
* [Start and Stop Enterprise Analytics](../install/start-stop-cb-enterprise-analytics.md): Explains how to start and stop the service and application using the commands that are specific to your underlying platform.