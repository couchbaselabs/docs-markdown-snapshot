---
title: Quick Start with Docker
description: First-time users can get Operational Insights running simply and
  rapidly by using Docker. Once you install Docker, you can use a single command
  to download and install Operational Insights on your computer.
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/intro/pages/do-a-quick-install.adoc
  xref: xref:enterprise-analytics:intro:do-a-quick-install.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/intro/do-a-quick-install.html)

# Quick Start with Docker

> First-time users can get Operational Insights running simply and rapidly by using Docker. Once you install Docker, you can use a single command to download and install Operational Insights on your computer. 

## [](#install-operational-insights-using-docker-and-versity-s3-gateway)Install Operational Insights using Docker and Versity S3 Gateway

This guide walks you through running Couchbase Operational Insights in Docker and configuring it to use [Versity S3 Gateway](https://github.com/versity/versitygw) as its blob storage backend — ideal for local development and testing without relying on real AWS S3 infrastructure or appliance.

Prerequisites:

* Docker Desktop installed (macOS, Windows, or Linux)
* No other services using ports `8091` or `8095`
* No existing Docker containers named `versitygw` or `insights`
* No existing Docker network named `insights-net`

### [](#step-by-step-setup)Step-by-Step Setup

#### [](#1-create-a-docker-network)1\. Create a Docker Network

docker network create insights-net

This command creates the `insights-net` network, enabling communication between the Operational Insights and Versity S3 Gateway containers.

#### [](#2-create-the-versity-s3-gateway-container)2\. Create the Versity S3 Gateway Container

We use Versity S3 Gateway to provide S3-compatible storage locally.

docker run -d --name versitygw --network insights-net \
  -v insights-s3-data:/data \
  versity/versitygw --access Administrator --secret password posix /data

Then create a bucket named `insights-storage` for Operational Insights to use:

docker exec versitygw versitygw admin --access Administrator --secret password \
  --endpoint-url http://localhost:7070 \
  create-bucket --bucket insights-storage --owner Administrator

The `insights-s3-data` named volume keeps the stored data when the container is removed or re-created, for example to upgrade the image; without it, the data lives only as long as the container does. The gateway also needs `/data` to exist, which the volume provides: for a throwaway trial without one, serve from a directory already in the image, such as `posix /tmp`. Use a named volume rather than a host directory: on macOS, a bind-mounted folder needs extra gateway options and treats object keys as case-insensitive. Replace `Administrator` / `password` with credentials of your own, here and in step 4.

#### [](#3-create-the-couchbase-operational-insights-container)3\. Create the Couchbase Operational Insights Container

docker run -d --name insights --network insights-net \
  -p 8091:8091 -p 8095:8095 \
  -v insights-data:/opt/couchbase/var/lib/couchbase/data \
  couchbase/operational-insights

This exposes the Operational Insights UI and REST APIs on ports `8091` and `8095` respectively.

The `insights-data` named volume is optional for a quick trial, but needed if you want the node's data to survive re-creating the container, for example to upgrade the image. Without it, Docker gives each new container a fresh, empty anonymous volume, and the old data is left orphaned.

#### [](#4-configure-blob-storage-settings)4\. Configure Blob Storage Settings

Once Operational Insights is online, configure it to use the local Versity S3 Gateway container as its blob storage:

curl -X POST http://localhost:8091/settings/operationalInsights \
  -d blobStorageScheme=s3 \
  -d blobStorageBucket=insights-storage \
  -d blobStorageRegion=us-east-1 \
  -d blobStorageEndpoint=http://versitygw:7070 \
  -d blobStorageAccessKeyId=Administrator \
  -d blobStorageSecretAccessKey=password \
  -d blobStoragePathStyleAddressing=true \
  -d numStoragePartitions=16

Explanation of settings:

* `blobStorageScheme`: Use S3 (Versity S3 Gateway is S3-compatible)
* `blobStorageBucket`: Bucket name created in Versity S3 Gateway
* `blobStorageRegion`: Region name (arbitrary for Versity S3 Gateway)
* `blobStorageEndpoint`: The local Versity S3 Gateway container's URL
* `blobStorageAccessKeyId`, `blobStorageSecretAccessKey`: The credentials the gateway was started with
* `blobStoragePathStyleAddressing=true`: Required, as the gateway is addressed by container name rather than by a virtual-host-style bucket subdomain, which is the default for AWS S3
* `numStoragePartitions`: Number of storage partitions (the default of 128 adds unnecessary overhead for a local quick start cluster)

#### [](#5-initialize-the-operational-insights-cluster)5\. Initialize the Operational Insights Cluster

Finally, complete the standalone initialization of the Operational Insights cluster:

curl -X POST http://localhost:8091/clusterInit \
  -d username=Administrator \
  -d password=password \
  -d port=SAME \
  -d memoryQuota=100 \
  -d clusterName="Operational Insights Quick Start"

You can now:

* Log in at <http://localhost:8091> using `Administrator`/`password`
* Install the `travel-sample` dataset
* Use the Workbench in the UI to run SQL++ queries, etc.
* Provision additional nodes (e.g. docker containers) as desired, by repeating step 3 above, selecting unique container names and bind ports from the `insights` container, and joining them to the cluster using the UI or REST API. See [Add a Node and Rebalance](../manage/manage-nodes/add-node-and-rebalance.md) for details.

## [](#next-steps)Next Steps

* [Quick Start Tutorial](connecting-to-data-sources.md)

## [](#other-destinations)Other Destinations

* [Create a Cluster](../manage/manage-nodes/create-cluster.md): Provides a detailed explanation of how to provision an Operational Insights node, and thereby create Operational Insights cluster. This is the procedure you'll certainly use in production as well as for testing different configurations. The available options include use of the Operational Insights Web Console, the Couchbase REST API, and the Couchbase Command Line Interface.
* [Start and Stop Operational Insights](../install/start-stop-cb-operational-insights.md): Explains how to start and stop the service and application using the commands that are specific to your underlying platform.