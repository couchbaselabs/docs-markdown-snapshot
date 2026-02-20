---
title: Analytics Administration REST APIs
description: A description of the Administration REST APIs for Couchbase Analytics.
editUrl: https://github.com/couchbase/docs-analytics/edit/release/7.2/modules/analytics/pages/rest-admin.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:analytics:rest-admin.adoc[]
---

[View original HTML](/server/7.2/analytics/rest-admin.html)

# Analytics Administration REST APIs

## [](#%5Foverview)Overview

The Analytics Administration REST APIs are provided by the Analytics service. These APIs enables you to manage and monitor the Analytics service.

The API schemes and host URLs are as follows:

* <http://node:8095/>
* <https://node:18095/> (for secure access)

where `node` is the host name or IP address of a node running the Analytics service.

### [](#version-information)Version information

_Version_ : 7.2

### [](#consumes)Consumes

* `application/x-www-form-urlencoded`

### [](#produces)Produces

* `application/json`

## [](#%5Fpaths)Paths

This section describes the operations available with these REST APIs.

* [Request Cancellation](#%5Fcancel%5Frequest)
* [Cluster Status](#%5Fcluster%5Fstatus)
* [Cluster Restart](#%5Frestart%5Fcluster)
* [Node Restart](#%5Frestart%5Fnode)
* [Ingestion Status](#%5Fingestion%5Fstatus)
* [Pending Mutations](#%5Fmonitor%5Fnode)

### [](#%5Fcancel%5Frequest)Request Cancellation

DELETE /analytics/admin/active_requests

#### [](#description)Description

Cancels an active request.

#### [](#parameters)Parameters

| Type         | Name                               | Description                                                                                 | Schema |
| ------------ | ---------------------------------- | ------------------------------------------------------------------------------------------- | ------ |
| **FormData** | **client\_context\_id** _required_ | Identifier passed by the client that is used to identify an active request to be cancelled. | string |

#### [](#responses)Responses

| HTTP Code | Description                                                                                                                                        | Schema     |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **200**   | The operation was successful.                                                                                                                      | No Content |
| **400**   | Bad request. Incorrect parameter or missing value.                                                                                                 | No Content |
| **401**   | Unauthorized. The user name or password may be incorrect. Returns an object containing an error message. Refer to [Error Codes](error-codes.html). | object     |
| **404**   | Not found. The path may be incorrect, or there is no active request with the specified identifier.                                                 | No Content |

#### [](#security)Security

| Type      | Name                                                                                   |
| --------- | -------------------------------------------------------------------------------------- |
| **basic** | **[Analytics Manage / Analytics Select](#%5Fanalytics%5Fmanage%5Fanalytics%5Fselect)** |

#### [](#example-http-request)Example HTTP request

The example below uses the `client_context_id` used in the [Query Service](rest-service.md#query-service) example to identify the request.

Curl request

```sh
curl -v -u Administrator:password -X DELETE \
     http://localhost:8095/analytics/admin/active_requests \
     -d client_context_id=xyz
```

### [](#%5Fcluster%5Fstatus)Cluster Status

GET /analytics/cluster

#### [](#description-2)Description

Shows various details about the current status of the Analytics Service, such as the service state, the state of each node partition, and the replicas of each partition.

#### [](#responses-2)Responses

| HTTP Code | Description                                                                                                                                        | Schema               |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- |
| **200**   | Success. Returns an object giving the current status of the Analytics Service.                                                                     | [Status](#%5Fstatus) |
| **401**   | Unauthorized. The user name or password may be incorrect. Returns an object containing an error message. Refer to [Error Codes](error-codes.html). | object               |
| **404**   | Not found. The path may be incorrect.                                                                                                              | No Content           |

#### [](#security-2)Security

| Type      | Name                                                               |
| --------- | ------------------------------------------------------------------ |
| **basic** | **[Cluster Read / Pools Read](#%5Fcluster%5Fread%5Fpools%5Fread)** |

#### [](#example-http-request-2)Example HTTP request

Curl request

```sh
curl -v -u Administrator:password http://localhost:8095/analytics/cluster
```

#### [](#example-http-response)Example HTTP response

Response 200

```json
{
  "authorizedNodes": [
    "86586a966202b5aa4aed31633f330aba",
    "948fb3af810a9b7bc6c76e2a69ba35d9"
  ],
  "ccNodeId": "86586a966202b5aa4aed31633f330aba",
  "nodeConfigUri": "/analytics/config/node",
  "nodeDiagnosticsUri": "/analytics/node/diagnostics",
  "nodeRestartUri": "/analytics/node/restart",
  "nodeServiceUri": "/analytics/service",
  "nodes": [
    {
      "apiBase": "http://192.168.8.101:8095",
      "apiBaseHttps": "https://192.168.8.101:18095",
      "nodeId": "86586a966202b5aa4aed31633f330aba",
      "nodeName": "192.168.8.101:8091"
    },
    {
      "apiBase": "http://192.168.8.102:8095",
      "apiBaseHttps": "https://192.168.8.102:18095",
      "nodeId": "948fb3af810a9b7bc6c76e2a69ba35d9",
      "nodeName": "192.168.8.102:8091"
    }
  ],
  "partitions": [
    {
      "active": true,
      "activeNodeId": "86586a966202b5aa4aed31633f330aba",
      "iodeviceNum": 0,
      "nodeId": "86586a966202b5aa4aed31633f330aba",
      "partitionId": 0,
      "path": "/data/@analytics/v_iodevice_0",
      "pendingActivation": false
    },
    {
      "active": true,
      "activeNodeId": "948fb3af810a9b7bc6c76e2a69ba35d9",
      "iodeviceNum": 0,
      "nodeId": "948fb3af810a9b7bc6c76e2a69ba35d9",
      "partitionId": 1,
      "path": "/data/@analytics/v_iodevice_0",
      "pendingActivation": false
    }
  ],
  "partitionsTopology": {
    "balanced": true,
    "ccNodeId": "86586a966202b5aa4aed31633f330aba",
    "metadataPartition": -1,
    "numReplicas": 1,
    "partitions": [
      {
        "id": "0",
        "master": "86586a966202b5aa4aed31633f330aba",
        "origin": "86586a966202b5aa4aed31633f330aba",
        "replicas": [
          {
            "location": "192.168.8.102:9120",
            "nodeId": "948fb3af810a9b7bc6c76e2a69ba35d9",
            "status": "IN_SYNC",
            "syncProgress": "1"
          }
        ]
      },
      {
        "id": "1",
        "master": "948fb3af810a9b7bc6c76e2a69ba35d9",
        "origin": "948fb3af810a9b7bc6c76e2a69ba35d9",
        "replicas": [
          {
            "location": "192.168.8.101:9120",
            "nodeId": "86586a966202b5aa4aed31633f330aba",
            "status": "IN_SYNC",
            "syncProgress": "1"
          }
        ]
      },
      {
        "id": "-1",
        "master": "86586a966202b5aa4aed31633f330aba",
        "origin": "86586a966202b5aa4aed31633f330aba",
        "replicas": [
          {
            "location": "192.168.8.102:9120",
            "nodeId": "948fb3af810a9b7bc6c76e2a69ba35d9",
            "status": "IN_SYNC",
            "syncProgress": "1"
          }
        ]
      }
    ],
    "revision": 1,
    "version": 1
  },
  "serviceConfigUri": "/analytics/config/service",
  "serviceDiagnosticsUri": "http://localhost:8095/analytics/cluster/diagnostics",
  "serviceRestartUri": "http://localhost:8095/analytics/cluster/restart",
  "state": "ACTIVE"
}
```

### [](#%5Frestart%5Fcluster)Cluster Restart

POST /analytics/cluster/restart

#### [](#description-3)Description

Restarts all Analytics Service nodes in the cluster.

#### [](#responses-3)Responses

| HTTP Code | Description                                                                                                                                        | Schema     |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **202**   | Accepted. Returns an object showing the status of the cluster.                                                                                     | object     |
| **401**   | Unauthorized. The user name or password may be incorrect. Returns an object containing an error message. Refer to [Error Codes](error-codes.html). | object     |
| **404**   | Not found. The path may be incorrect.                                                                                                              | No Content |

#### [](#security-3)Security

| Type      | Name                                           |
| --------- | ---------------------------------------------- |
| **basic** | **[Analytics Manage](#%5Fanalytics%5Fmanage)** |

#### [](#example-http-request-3)Example HTTP request

Curl request

```sh
curl -v -u Administrator:password -X POST http://localhost:8095/analytics/cluster/restart
```

#### [](#example-http-response-2)Example HTTP response

Response 202

```json
{
  "cluster" : {
    "metadata_node" : "edfb6de9c91d7fb36399fea3ce620c5c",
    "ncs" : [ {
      "node_id" : "edfb6de9c91d7fb36399fea3ce620c5c",
      "partitions" : [ {
        "active" : true,
        "partition_id" : "partition_0"
      } ],
      "pid" : 5763,
      "state" : "ACTIVE"
    } ],
    "state" : "ACTIVE"
  },
  "date" : "Wed Oct 10 15:35:56 BST 2018",
  "status" : "SHUTTING_DOWN"
}
```

### [](#%5Frestart%5Fnode)Node Restart

POST /analytics/node/restart

#### [](#description-4)Description

Restarts the specified Analytics Service node.

#### [](#responses-4)Responses

| HTTP Code | Description                                                                                                                                        | Schema     |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **202**   | Accepted. Returns an object showing the status of the node.                                                                                        | object     |
| **401**   | Unauthorized. The user name or password may be incorrect. Returns an object containing an error message. Refer to [Error Codes](error-codes.html). | object     |
| **404**   | Not found. The path may be incorrect.                                                                                                              | No Content |

#### [](#security-4)Security

| Type      | Name                                           |
| --------- | ---------------------------------------------- |
| **basic** | **[Analytics Manage](#%5Fanalytics%5Fmanage)** |

#### [](#example-http-request-4)Example HTTP request

Curl request

```sh
curl -v -u Administrator:password -X POST http://localhost:8095/analytics/node/restart
```

#### [](#example-http-response-3)Example HTTP response

Response 202

```json
{"status": "restarting node"}
```

### [](#%5Fingestion%5Fstatus)Ingestion Status

GET /analytics/status/ingestion

#### [](#description-5)Description

Shows the progress of ingestion by the Analytics service, for each Analytics collection.

#### [](#responses-5)Responses

| HTTP Code | Description                                                                                                                                        | Schema                     |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| **200**   | Success. Returns an object giving the ingestion status of each Analytics collection.                                                               | [Ingestion](#%5Fingestion) |
| **401**   | Unauthorized. The user name or password may be incorrect. Returns an object containing an error message. Refer to [Error Codes](error-codes.html). | object                     |
| **404**   | Not found. The path may be incorrect.                                                                                                              | No Content                 |

#### [](#security-5)Security

| Type      | Name                                                                                   |
| --------- | -------------------------------------------------------------------------------------- |
| **basic** | **[Analytics Manage / Analytics Select](#%5Fanalytics%5Fmanage%5Fanalytics%5Fselect)** |

#### [](#example-http-request-5)Example HTTP request

Curl request

```sh
curl -v -u Administrator:password http://localhost:8095/analytics/status/ingestion
```

#### [](#example-http-response-4)Example HTTP response

Response 200

```json
{
  "links": [
    {
      "name": "Local",
      "scope": "travel-sample/tenant_agent_02",
      "status": "healthy",
      "state": [
        {
          "timestamp": 1631107234921,
          "progress": 1,
          "scopes": [
            {
              "collections": [
                {
                  "name": "users"
                }
              ],
              "name": "travel-sample/tenant_agent_02"
            }
          ]
        }
      ]
    },
    {
      "name": "Local",
      "scope": "travel-sample/inventory",
      "status": "healthy",
      "state": [
        {
          "timestamp": 1631107234921,
          "progress": 1,
          "scopes": [
            {
              "collections": [
                {
                  "name": "airport"
                },
                {
                  "name": "landmark"
                }
              ],
              "name": "travel-sample/inventory"
            }
          ]
        },
        {
          "timestamp": 1631107234921,
          "progress": 0.9821428571428571,
          "timeLag": 4840,
          "itemsProcessed": 23595,
          "seqnoAdvances": 49129,
          "scopes": [
            {
              "collections": [
                {
                  "name": "route"
                }
              ],
              "name": "travel-sample/inventory"
            }
          ]
        }
      ]
    }
  ]
}
```

### [](#%5Fmonitor%5Fnode)Pending Mutations

GET /analytics/node/agg/stats/remaining

> [!CAUTION]
> operation.deprecated

#### [](#description-6)Description

Shows the number of mutations in the DCP queue that have not yet been ingested by the Analytics service, for each Analytics collection.

> [!NOTE]
> This endpoint may not return meaningful results in Couchbase Server 7.0 and later. The reported number of mutations may be different to the actual number of mutations in the Analytics collection. For this reason, this endpoint has been deprecated, and you should use the [Ingestion Status](#%5Fingestion%5Fstatus) endpoint instead.

#### [](#responses-6)Responses

| HTTP Code | Description                                                                                                                                        | Schema                     |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| **200**   | Success. Returns an object giving the number of pending mutations for each Analytics collection.                                                   | [Mutations](#%5Fmutations) |
| **401**   | Unauthorized. The user name or password may be incorrect. Returns an object containing an error message. Refer to [Error Codes](error-codes.html). | object                     |
| **404**   | Not found. The path may be incorrect.                                                                                                              | No Content                 |

#### [](#security-6)Security

| Type      | Name                                                                                   |
| --------- | -------------------------------------------------------------------------------------- |
| **basic** | **[Analytics Manage / Analytics Select](#%5Fanalytics%5Fmanage%5Fanalytics%5Fselect)** |

#### [](#example-http-request-6)Example HTTP request

Curl request

```sh
curl -v -u Administrator:password http://localhost:8095/analytics/node/agg/stats/remaining
```

#### [](#example-http-response-5)Example HTTP response

Response 200

```json
{
  "Commerce": {
    "orders": 0,
    "customers": 0
  }
}
```

## [](#%5Fdefinitions)Definitions

This section describes the properties returned by these REST APIs.

* [Status](#%5Fstatus)
* [Ingestion](#%5Fingestion)
* [Mutations](#%5Fmutations)

### [](#%5Fstatus)Status

An object giving information about the status of the Analytics service.

| Name                                 | Description                                                                                                                                                              | Schema                                                       |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------ |
| **authorizedNodes** _optional_       | An array of strings, each of which is the ID of an authorized Analytics node. **Example** : \[ "86586a966202b5aa4aed31633f330aba", "948fb3af810a9b7bc6c76e2a69ba35d9" \] | < string > array                                             |
| **ccNodeId** _optional_              | The ID of the cluster controller node. **Example** : "86586a966202b5aa4aed31633f330aba"                                                                                  | string                                                       |
| **nodeConfigUri** _optional_         | The path of the Analytics Node Configuration REST API. **Example** : "/analytics/config/node"                                                                            | string                                                       |
| **nodeDiagnosticsUri** _optional_    | The path of the Analytics Node Diagnostics REST API. For internal use only. **Example** : "/analytics/node/diagnostics"                                                  | string                                                       |
| **nodeRestartUri** _optional_        | The path of the Analytics Node Restart REST API. **Example** : "/analytics/node/restart"                                                                                 | string                                                       |
| **nodeServiceUri** _optional_        | The path of the Analytics Query Service REST API. **Example** : "/analytics/service"                                                                                     | string                                                       |
| **serviceConfigUri** _optional_      | The path of the Analytics Service Configuration REST API. **Example** : "/analytics/config/service"                                                                      | string                                                       |
| **serviceDiagnosticsUri** _optional_ | The full URI of the Analytics Service Diagnostics REST API. For internal use only. **Example** : "http://localhost:8095/analytics/cluster/diagnostics"                   | string                                                       |
| **serviceRestartUri** _optional_     | The full URI of the Analytics Cluster Restart REST API. **Example** : "http://localhost:8095/analytics/cluster/restart"                                                  | string                                                       |
| **state** _optional_                 | The state of the Analytics Service. **Example** : "ACTIVE"                                                                                                               | enum (ACTIVE, REBALANCE\_REQUIRED, UNUSABLE, SHUTTING\_DOWN) |
| **nodes** _optional_                 | An array of objects, each giving information about one Analytics node.                                                                                                   | < [Nodes](#%5Fnodes) \> array                                |
| **partitions** _optional_            | An array of objects, each giving information about one Analytics partition.                                                                                              | < [Partitions](#%5Fpartitions) \> array                      |
| **partitionsTopology** _optional_    | An object giving information about the partition topology.                                                                                                               | [Partition Topology](#%5Fpartition%5Ftopology)               |

**Nodes**

| Name                        | Description                                                                                                                             | Schema |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **apiBase** _optional_      | The URI scheme, host, and port for HTTP access to Analytics REST APIs on this node. **Example** : "http://192.168.8.101:8095"           | string |
| **apiBaseHttps** _optional_ | The URI scheme, host, and port for secure HTTPS access to Analytics REST APIs on this node. **Example** : "https://192.168.8.101:18095" | string |
| **nodeId** _optional_       | The ID of the node. **Example** : "86586a966202b5aa4aed31633f330aba"                                                                    | string |
| **nodeName** _optional_     | The name or IP address of the node, including the cluster administration port. **Example** : "192.168.8.101:8091"                       | string |

**Partitions**

| Name                             | Description                                                                                                   | Schema  |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------- |
| **active** _optional_            | Indicates whether this partition is active. **Example** : true                                                | boolean |
| **activeNodeId** _optional_      | The ID of the node where this partition is currently active. **Example** : "86586a966202b5aa4aed31633f330aba" | string  |
| **iodeviceNum** _optional_       | The number of the IO Device where this partition is located. **Example** : 0                                  | integer |
| **nodeId** _optional_            | The ID of the node where this partition originated. **Example** : "86586a966202b5aa4aed31633f330aba"          | string  |
| **partitionId** _optional_       | The ID of this partition. **Example** : 0                                                                     | integer |
| **path** _optional_              | The path of the IO Device where this partition is located. **Example** : "/data/@analytics/v\_iodevice\_0"    | string  |
| **pendingActivation** _optional_ | Indicates whether this partition is waiting to become active. **Example** : false                             | boolean |

**Partition Topology**

| Name                             | Description                                                                              | Schema                                                |
| -------------------------------- | ---------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| **balanced** _optional_          | Indicates whether the Analytics nodes are balanced. **Example** : true                   | boolean                                               |
| **ccNodeId** _optional_          | The ID of the cluster controller node. **Example** : "86586a966202b5aa4aed31633f330aba"  | string                                                |
| **metadataPartition** _optional_ | The ID of the metadata partition. **Example** : \-1                                      | integer                                               |
| **numReplicas** _optional_       | The number of Analytics replicas. **Example** : 1                                        | integer                                               |
| **revision** _optional_          | The revision number of the partition topology. **Example** : 1                           | integer                                               |
| **version** _optional_           | The version number of the partition topology. **Example** : 1                            | integer                                               |
| **partitions** _optional_        | An array of objects, each giving information about the state of one Analytics partition. | < [Partition States](#%5Fpartition%5Fstates) \> array |

**Partition States**

| Name                    | Description                                                                                                  | Schema                              |
| ----------------------- | ------------------------------------------------------------------------------------------------------------ | ----------------------------------- |
| **id** _optional_       | The partition ID. **Example** : 0                                                                            | integer                             |
| **master** _optional_   | The ID of the node where the partition is currently active. **Example** : "86586a966202b5aa4aed31633f330aba" | string                              |
| **origin** _optional_   | The ID of the node where the partition originated. **Example** : "86586a966202b5aa4aed31633f330aba"          | string                              |
| **replicas** _optional_ | An array of objects, each giving information about the state of one Analytics replica.                       | < [Replicas](#%5Freplicas) \> array |

**Replicas**

| Name                        | Description                                                                                                                                                           | Schema                                      |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
| **location** _optional_     | The name or IP address of the node where this replica is located, including the Analytics replication port. **Example** : "192.168.8.102:9120"                        | string                                      |
| **nodeId** _optional_       | The ID of the node where this replica is located. **Example** : "948fb3af810a9b7bc6c76e2a69ba35d9"                                                                    | string                                      |
| **status** _optional_       | The synchronization status of the replica. **Example** : "IN\_SYNC"                                                                                                   | enum (IN\_SYNC, CATCHING\_UP, DISCONNECTED) |
| **syncProgress** _optional_ | The percentage (fraction from 0 to 1) of synchronization progress for this replica at the current time. **Minimum value** : 0 **Maximum value** : 1 **Example** : 1.0 | number (double)                             |

### [](#%5Fingestion)Ingestion

An object containing a single links property.

| Name                 | Description                                                                         | Schema                        |
| -------------------- | ----------------------------------------------------------------------------------- | ----------------------------- |
| **links** _optional_ | An array of objects, each giving information about a single linked Analytics scope. | < [Links](#%5Flinks) \> array |

**Links**

| Name                  | Description                                                                                                                                                                                               | Schema                                        |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **name** _optional_   | The name of the link. **Example** : "Local"                                                                                                                                                               | string                                        |
| **scope** _optional_  | The name of the Analytics scope. **Example** : "travel-sample/inventory"                                                                                                                                  | string                                        |
| **status** _optional_ | The status of the Analytics scope. **Example** : "healthy"                                                                                                                                                | enum (healthy, stopped, unhealthy, suspended) |
| **state** _optional_  | An array of objects, each giving the ingestion state of one or more Analytics collections. Analytics collections which have the same ingestion state within this Analytics scope are aggregated together. | < [States](#%5Fstates) \> array               |

**States**

| Name                          | Description                                                                                                                                                                                                                                                                           | Schema                                        |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **timestamp** _required_      | The time since epoch that this sample was calculated, in milliseconds. **Example** : 1631273689161                                                                                                                                                                                    | integer                                       |
| **progress** _required_       | The percentage (fraction from 0 to 1) of ingestion progress at the current time. **Minimum value** : 0 **Maximum value** : 1 **Example** : 0.0                                                                                                                                        | number (double)                               |
| **timeLag** _optional_        | The estimated time that the ingestion lags behind the Data service, in milliseconds. Only displayed for Analytics collections that are not fully ingested. **Example** : 9744                                                                                                         | integer                                       |
| **itemsProcessed** _optional_ | The number of items ingested since last connect; that is, the total number of mutations and deletions processed. Only displayed for Analytics collections that are not fully ingested. Note that this value is reset on connect, so it may appear to get smaller. **Example** : 12301 | integer                                       |
| **seqnoAdvances** _optional_  | The change in sequence number (seqno) since last connect. Only displayed for Analytics collections that are not fully ingested. **Example** : 61                                                                                                                                      | integer                                       |
| **scopes** _required_         | An array of objects, each one giving information about a single Analytics scope.                                                                                                                                                                                                      | < [State Scopes](#%5Fstate%5Fscopes) \> array |

**State Scopes**

| Name                       | Description                                                                           | Schema                                                  |
| -------------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| **name** _required_        | The name of the Analytics scope. **Example** : "travel-sample/inventory"              | string                                                  |
| **collections** _required_ | An array of objects, each one giving information about a single Analytics collection. | < [State Collections](#%5Fstate%5Fcollections) \> array |

**State Collections**

| Name                | Description                                                 | Schema |
| ------------------- | ----------------------------------------------------------- | ------ |
| **name** _required_ | The name of the Analytics collection. **Example** : "route" | string |

### [](#%5Fmutations)Mutations

An object containing one or more nested scope objects, one for each available Analytics scope.

| Name                   | Description                                                                                                                                                                                   | Schema                         |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------ |
| **_scope_** _optional_ | An object containing one or more collection properties, one for each Analytics collection in the Analytics scope. The name of the object is the name of the Analytics scope, in display form. | [Collections](#%5Fcollections) |

**Collections**

| Name                        | Description                                                                                                                                 | Schema  |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **_collection_** _optional_ | The number of mutations in the DCP queue that have not yet been ingested. The name of the property is the name of the Analytics collection. | integer |

## [](#%5Fsecurityscheme)Security

The Analytics Administration REST APIs support HTTP basic authentication. Credentials can be passed via HTTP headers.

### [](#%5Fanalytics%5Fmanage%5Fanalytics%5Fselect)Analytics Manage / Analytics Select

For the [Request Cancellation](#%5Fcancel%5Frequest), [Ingestion Status](#%5Fingestion%5Fstatus), and [Pending Mutations](#%5Fmonitor%5Fnode) operations, users must have one of the following access roles:

* Full Admin
* Cluster Admin
* Analytics Manager
* Analytics Reader
* Analytics Select
* Analytics Admin

_Type_ : basic

### [](#%5Fcluster%5Fread%5Fpools%5Fread)Cluster Read / Pools Read

For the [Cluster Status](#%5Fcluster%5Fstatus) operation, users must have one of the following access roles:

* Full Admin
* Cluster Admin
* Read-Only Admin
* Analytics Admin

_Type_ : basic

### [](#%5Fanalytics%5Fmanage)Analytics Manage

For the [Cluster Restart](#%5Frestart%5Fcluster) and [Node Restart](#%5Frestart%5Fnode) operations, users must have one of the following RBAC roles:

* Full Admin
* Cluster Admin
* Analytics Admin

_Type_ : basic

Refer to [Roles](../learn/security/roles.md) for more details.