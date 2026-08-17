---
title: Do a Quick Install
description: First-time users can get Enterprise Analytics running simply and
  rapidly by using Docker. Once you install Docker, you can use a single command
  to download and install Enterprise Analytics on your computer.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/intro/pages/do-a-quick-install.adoc
  xref: xref:enterprise-analytics:intro:do-a-quick-install.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/intro/do-a-quick-install.html)

# Do a Quick Install

> First-time users can get Enterprise Analytics running simply and rapidly by using Docker. Once you install Docker, you can use a single command to download and install Enterprise Analytics on your computer. 

## [](#install-enterprise-analytics-using-docker-and-s3mock)Install Enterprise Analytics using Docker and S3Mock

This guide walks you through running Couchbase Enterprise Analytics in Docker and configuring it to use [Adobe S3Mock](https://github.com/adobe/S3Mock) as its blob storage backend — ideal for local development and testing without relying on real AWS S3 infrastructure or appliance.

Prerequisites:

* Docker Desktop installed (macOS, Windows, or Linux)
* No other services using ports `8091` or `8095`
* No existing Docker containers named `s3mock` or `ea`
* No existing Docker network named `ea`

### [](#step-by-step-setup)Step-by-Step Setup

#### [](#1-create-a-docker-network)1\. Create a Docker Network

docker network create ea

This command creates the `ea` network, enabling communication between the Enterprise Analytics and S3Mock containers.

#### [](#2-create-the-s3mock-container)2\. Create the S3Mock Container

We use S3Mock to emulate AWS S3 behavior locally.

docker run -d --name s3mock --network ea \
  -e COM_ADOBE_TESTING_S3MOCK_STORE_INITIAL_BUCKETS=cloud-storage-container \
  -e COM_ADOBE_TESTING_S3MOCK_STORE_ROOT=fs \
  -e COM_ADOBE_TESTING_S3MOCK_STORE_RETAIN_FILES_ON_EXIT=true \
  adobe/s3mock

This starts the S3Mock container with a pre-created persistent bucket named `cloud-storage-container` for Enterprise Analytics to use, configured to communicate over the `ea` network.

#### [](#3-create-the-couchbase-enterprise-analytics-container)3\. Create the Couchbase Enterprise Analytics Container

docker run -d --name ea --network ea \
  -p 8091:8091 -p 8095:8095 \
  couchbase/enterprise-analytics:2.2.0

This exposes the Enterprise Analytics UI and REST APIs on ports `8091` and `8095` respectively.

#### [](#4-configure-blob-storage-settings)4\. Configure Blob Storage Settings

Once Enterprise Analytics is online, configure it to use the local S3Mock container as its blob storage:

curl -X POST http://localhost:8091/settings/analytics \
  -d blobStorageScheme=s3 \
  -d blobStorageBucket=cloud-storage-container \
  -d blobStorageRegion=us-east-1 \
  -d blobStorageEndpoint=http://s3mock:9090 \
  -d blobStorageAnonymousAuth=true \
  -d blobStoragePathStyleAddressing=true \
  -d numStoragePartitions=16

Explanation of settings:

* `blobStorageScheme`: Use S3 (S3Mock is S3-compatible)
* `blobStorageBucket`: Bucket name created in S3Mock
* `blobStorageRegion`: Region name (arbitrary for S3Mock)
* `blobStorageEndpoint`: The local S3Mock container's URL
* `blobStorageAnonymousAuth=true`: Required, since S3Mock does not use IAM
* `blobStoragePathStyleAddressing=true`: Required, as S3Mock does not support virtual-host-style addressing, which is the default for AWS S3
* `numStoragePartitions`: Number of storage partitions (the default of 128 adds unnecessary overhead for a local quick start cluster)

#### [](#5-initialize-the-enterprise-analytics-cluster)5\. Initialize the Enterprise Analytics Cluster

Finally, complete the standalone initialization of the Enterprise Analytics cluster:

curl -X POST http://localhost:8091/clusterInit \
  -d username=Administrator \
  -d password=password \
  -d port=SAME \
  -d memoryQuota=100 \
  -d clusterName="EA Quick Start Cluster"

You can now:

* Log in at <http://localhost:8091> using `Administrator`/`password`
* Install the `travel-sample` dataset
* Use the Workbench in the UI to run SQL++ queries, etc.
* Provision additional nodes (e.g. docker containers) as desired, by repeating step 3 above, selecting unique container names and bind ports from the `ea` container, and joining them to the cluster using the UI or REST API. See [Add a Node and Rebalance](../manage/manage-nodes/add-node-and-rebalance.md) for details.

## [](#next-steps)Next Steps

* [Connecting to Data Sources](connecting-to-data-sources.md)

## [](#other-destinations)Other Destinations

* [Create a Cluster](../manage/manage-nodes/create-cluster.md): Provides a detailed explanation of how to provision a Enterprise Analytics-node, and thereby create Enterprise Analytics cluster. This is the procedure you'll certainly use in production as well as for testing different configurations. The available options include use of the Enterprise Analytics Web Console, the Couchbase REST API, and the Couchbase Command Line Interface.
* [Start and Stop Enterprise Analytics](../install/start-stop-cb-enterprise-analytics.md): Explains how to start and stop the service and application using the commands that are specific to your underlying platform.