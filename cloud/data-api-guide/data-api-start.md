---
title: Get Started with the Data API
description: To get started with the Couchbase Capella Data API, you must create
  a cluster access credential and enable the Data API for the cluster.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/data-api-guide/pages/data-api-start.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:cloud:data-api-guide:data-api-start.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/data-api-guide/data-api-start.html)

# Get Started with the Data API

> To get started with the Couchbase Capella Data API, you must create a cluster access credential and enable the Data API for the cluster. 

## [](#introduction)Introduction

To access the Data API, you must first enable the Data API for the cluster. Couchbase Capella provides a unique base URL which you can use to access the Data API for that cluster.

### [](#cluster-access)Cluster Access

A [cluster access credential](../clusters/manage-database-users.md) authenticates and authorizes you to access the Data API. You can use an existing cluster access credential, or create a new one. The access privileges that you specify for the cluster access credential determine the buckets, scopes, and collections that you can access via the Data API.

### [](#private-networking)Private Networking

If you want to access the Data API over a VPC Peering connection, you must activate VPC Peering for the Data API when you enable the Data API itself. You must then set up VPC Peering in a separate step.

If you want to access the Data API through a private endpoint, do not activate VPC Peering for the Data API. Instead, enable the Data API, and set up a private endpoint for the Data API in a separate step.

### [](#ip-access-over-public-network)IP Access over Public Network

To use the Data API over a public network, you must specify which IP addresses can access the Couchbase Capella cluster. For security, it's recommended that clients should only be able to access the cluster from specific IP addresses.

For each cluster, you can grant access from:

* Any IP address.
* Individual IP addresses.
* Blocks of IP addresses using [CIDR notation](https://en.wikipedia.org/wiki/Classless%5FInter-Domain%5FRouting#CIDR%5Fnotation).

Permitted IP addresses and address ranges must be in [IPv4](https://en.wikipedia.org/wiki/IPv4) format.

If you're accessing the Data API via a VPC Peering connection or a private endpoint, you do not need to permit access from the peered range of private IP addresses.

## [](#prerequisites)Prerequisites

The procedures on this page assume the following:

* You have [configured cluster access](../clusters/manage-database-users.md#create-database-credentials) by creating a cluster access credential. You'll need the username and password for the cluster credential to connect to the Data API.
* You have [added your IP address](../clusters/allow-ip-address.md#accessing-allowed-ips-in-the-capella-ui) to the cluster's list of allowed IPs, if required.
* You're not connecting from an IPv6-only environment — you need to be able to use the IPv4 records published for Capella clusters.

You can do all of this from a single location using the Connect page in the Capella UI, or the Management API.

## [](#examples-on-this-page)Examples on this Page

In the Management API examples on this page:

* `$organizationId` is the organization ID.
* `$projectId` is the project ID.
* `$clusterId` is the cluster ID.
* `$apiKeySecret` is the API key secret, used as the Bearer token.

The endpoints described on this page all have the same base path: `/v4/organizations/{organizationId}/projects/{projectId}/clusters/{clusterId}`. For clarity, this is not shown in the instructions, but it's included in the examples.

For details, see [Manage Deployments with the Capella Operational Management API](../management-api-guide/management-api-intro.md).

## [](#enable-the-data-api)Enable the Data API

You can enable the Data API using the Capella UI or the Management API.

* Capella UI
* Management API

1. On the **Operational Clusters** page, click on the cluster that you want to connect to.
2. Go to **Connect** **Data API**.
3. If necessary, follow the instructions on screen to enter an allowed IP address range.
4. If necessary, follow the instructions on screen to create a new cluster user.
5. Click **Enable Data API**. When prompted, type `Yes` and click **Confirm**.
6. Wait for Couchbase Capella to deploy the Data API. This may take several minutes.
7. When the Data API is deployed, copy the **Data API Endpoint** — this is the base URL you'll need to connect to the cluster.
8. If required, select **Enable Data API over VPC Peered Network**. This will incur extra charges.
9. To get started with the Data API, choose a cluster user from the drop-down, and then copy the generated sample code. Replace `<<password>>` with the password you specified when you created the cluster access user.

1. If necessary, use [POST /allowedcidrs](../management-api-reference/index.md#tag/Allowed-CIDRs-%28Cluster%29/operation/postAllowedCidrs) to enter an allowed IP address range.  
```sh  
curl -X POST "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/allowedcidrs" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer $apiKeySecret" \
  -d '{  
  "cidr": "6.60.28.100/32",  
  "comment": "Allows access from my local developer machine",  
  "expiresAt": "2026-05-14T21:49:58.465Z"  
}'  
```
2. If necessary, use [POST /users](../management-api-reference/index.md#tag/Database-Credentials/operation/postDatabaseCredential) to create a cluster user.  
```sh  
curl -X POST "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/users" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer $apiKeySecret" \
  -d '{  
  "name": "WriteAccessForAllBuckets",  
  "access": [  
    {  
      "privileges": [  
        "data_writer"  
      ]  
    }  
  ]  
}'  
```
3. Use [PUT /dataAPI](../management-api-reference/index.md#tag/Data-API/operation/updateDataApiAndPeering) to enable the Data API, and optionally enable VPC peering for the Data API.

  * To enable the Data API, pass `"enableDataAPI": true` in the request body.
  * To enable VPC peering for the Data API, pass `"enableNetworkPeering": true` in the request body. This will incur extra charges.  
```sh  
curl -X PUT "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/dataAPI" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer $apiKeySecret" \
  -d '{  
  "enableDataApi": true,  
  "enableNetworkPeering": true  
}'  
```
4. Use [GET /dataAPI](../management-api-reference/index.md#tag/Data-API/operation/getDataAPIStatus) to check the status of the Data API. It may take several minutes to deploy the Data API.  
```sh  
curl -X GET "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/dataAPI" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer $apiKeySecret"  
```
5. Copy the connection string returned by [GET /dataAPI](../management-api-reference/index.md#tag/Data-API/operation/getDataAPIStatus) — this is the base URL you'll need to connect to the cluster.

## [](#disable-the-data-api)Disable the Data API

You can disable the Data API using the Capella UI or the Management API.

* Capella UI
* Management API

1. On the **Operational Clusters** page, click on the cluster that you want to connect to.
2. Go to **Connect** **Data API**.
3. Click **Disable Data API**. When prompted, click **Confirm**.

1. Use [PUT /dataAPI](../management-api-reference/index.md#tag/Data-API/operation/updateDataApiAndPeering) to disable VPC peering for the Data API, or disable the Data API altogether.

  * To disable VPC peering for the Data API, pass `"enableNetworkPeering": false` in the request body.
  * To disable the Data API altogether, pass `"enableDataAPI": false` in the request body.  
```sh  
curl -X PUT "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/dataAPI" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer $apiKeySecret" \
  -d '{  
  "enableDataApi": false,  
  "enableNetworkPeering": false  
}'  
```
2. Use [GET /dataAPI](../management-api-reference/index.md#tag/Data-API/operation/getDataAPIStatus) to check the status of the Data API.  
```sh  
curl -X GET "https://cloudapi.cloud.couchbase.com/v4/organizations/$organizationId/projects/$projectId/clusters/$clusterId/dataAPI" \
  -H "Accept: application/json" \
  -H "Authorization: Bearer $apiKeySecret"  
```

## [](#next-steps)Next Steps

* To set up a private endpoint for the Data API, see [Add Private Endpoints for the Data API](data-api-private.md).
* To set up VPC peering, see [Configure a VPC Peering Connection](../clouds/private-network.md).
* To make an API call, see [Make an API Call with the Data API](data-api-use.md).
* To understand when to use the Data API, see [Data API vs. Couchbase SDKs](data-api-sdks.md).
* For a full reference guide, see [Data API Reference](../data-api-reference/index.md).