---
title: Analytics Administration REST APIs
description: A description of the Administration REST APIs for Couchbase Analytics.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/cb-swagger/edit/release/8.0/docs/modules/analytics-rest-admin/pages/index.adoc
  xref: xref:server:analytics-rest-admin:index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/analytics-rest-admin/index.html)

# Analytics Administration REST APIs

## [](#overview)Overview

The Analytics Administration REST APIs are provided by the Analytics Service. These APIs enables you to manage and monitor the Analytics Service.

### Version information

**Version:** 8.0

### Host information

{scheme}://{host}:{port}

The URL scheme, host, and port are as follows.

| Component  | Description                                                                                 |
| ---------- | ------------------------------------------------------------------------------------------- |
| **scheme** | The URL scheme. Use https for secure access. **Values:** http, https                        |
| **host**   | The host name or IP address of a node running the Analytics Service. **Example:** localhost |
| **port**   | The Analytics Service REST port. Use 18095 for secure access. **Values:** 8095, 18095       |

## [](#resources)Resources

This section describes the operations available with this REST API.

[Request Cancellation](#cancel%5Frequest)  
[Cluster Status](#cluster%5Fstatus)  
[Completed Requests](#completed%5Frequests)  
[Ingestion Status](#ingestion%5Fstatus)  
[Pending Mutations](#monitor%5Fnode)  
[Cluster Restart](#restart%5Fcluster)  
[Node Restart](#restart%5Fnode)  
[Active Requests](#return%5Factive%5Frequests)

### [](#cancel%5Frequest)Request Cancellation

DELETE /analytics/admin/active_requests

#### [](#cancel%5Frequest-description)Description

Cancels an active request.

Consumes

* application/x-www-form-urlencoded

Produces

* application/json

#### [](#cancel%5Frequest-parameters)Parameters

Form Parameters

| Name                            | Description                                                                                | Schema |
| ------------------------------- | ------------------------------------------------------------------------------------------ | ------ |
| **client\_context\_id**required | Identifier passed by the client that's used to identify an active request to be cancelled. | String |

#### [](#cancel%5Frequest-responses)Responses

| HTTP Code | Description                                                                                                                                                                               | Schema |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| 200       | The operation was successful.                                                                                                                                                             |        |
| 400       | Bad request. Incorrect parameter or missing value.                                                                                                                                        |        |
| 401       | Unauthorized. The user name or password may be incorrect. Returns an object containing an error message. For more information, see [Error Codes](/server/8.0/analytics/error-codes.html). | Object |
| 404       | Not found. The path may be incorrect, or there is no active request with the specified identifier.                                                                                        |        |

#### [](#cancel%5Frequest-security)Security

| Type         | Name                                                                            |
| ------------ | ------------------------------------------------------------------------------- |
| http (basic) | [Analytics Manage / Analytics Select](#security-AnalyticsManageAnalyticsSelect) |

#### [](#example-http-request)Example HTTP Request

The example below uses the `client_context_id` used in the [Query Service](#rest-service.adoc#query-service) example to identify the request.

curl request

```sh
curl -v -u Administrator:password -X DELETE \
     http://localhost:8095/analytics/admin/active_requests \
     -d client_context_id=xyz
```

### [](#cluster%5Fstatus)Cluster Status

GET /analytics/cluster

#### [](#cluster%5Fstatus-description)Description

Shows various details about the current status of the Analytics Service, such as the service state, the state of each node partition, and the replicas of each partition.

Produces

* application/json

#### [](#cluster%5Fstatus-responses)Responses

| HTTP Code | Description                                                                                                                                                                               | Schema            |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| 200       | Success. Returns an object giving the current status of the Analytics Service.                                                                                                            | [Status](#Status) |
| 401       | Unauthorized. The user name or password may be incorrect. Returns an object containing an error message. For more information, see [Error Codes](/server/8.0/analytics/error-codes.html). | Object            |
| 404       | Not found. The path may be incorrect.                                                                                                                                                     |                   |

#### [](#cluster%5Fstatus-security)Security

| Type         | Name                                                        |
| ------------ | ----------------------------------------------------------- |
| http (basic) | [Cluster Read / Pools Read](#security-ClusterReadPoolsRead) |

#### [](#example-http-request-2)Example HTTP Request

curl request

```sh
curl -v -u Administrator:password http://localhost:8095/analytics/cluster
```

#### [](#example-http-response)Example HTTP Response

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

### [](#completed%5Frequests)Completed Requests

GET /analytics/admin/completed_requests

#### [](#completed%5Frequests-description)Description

Gets a list of all completed analytic requests.

Produces

* application/json

#### [](#completed%5Frequests-responses)Responses

| HTTP Code | Description                                                                                                                                                                               | Schema                    |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| 200       | Success. Returns a list of all completed analytic requests.                                                                                                                               | [Request](#Request) array |
| 401       | Unauthorized. The user name or password may be incorrect. Returns an object containing an error message. For more information, see [Error Codes](/server/8.0/analytics/error-codes.html). | Object                    |
| 404       | Not found. The path may be incorrect.                                                                                                                                                     |                           |

#### [](#completed%5Frequests-security)Security

| Type         | Name                                                                            |
| ------------ | ------------------------------------------------------------------------------- |
| http (basic) | [Analytics Manage / Analytics Select](#security-AnalyticsManageAnalyticsSelect) |

#### [](#example-http-request-3)Example HTTP Request

curl request

```sh
curl -v -u Administrator:password -X GET \
     http://localhost:8095/analytics/admin/completed_requests
```

#### [](#example-http-response-2)Example HTTP Response

Response 200

```json
[
  {
    "cancellable": true,
    "clientContextID": "92e62399-1bc2-49a3-87e6-5dd88b463045",
    "elapsedTime": 0.021,
    "jobId": null,
    "jobQueueTime": 1716926862,
    "jobRequiredCPUs": 0,
    "jobRequiredMemory": 0,
    "jobStatus": "null",
    "node": "172.20.0.2:8095",
    "remoteAddr": "172.20.0.2:53612",
    "requestTime": "2024-05-28T19:44:07.730",
    "scanConsistency": "not_bounded",
    "state": "completed",
    "statement": "select count(*) from hotel_endoresement_view;",
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
    "users": "Administrator",
    "uuid": "9ea68a11-31f3-4ea5-9455-2686fa499b8d"
  },
  {
    "cancellable": true,
    "clientContextID": "28379d60-7139-44d6-b57a-95935540b586",
    "elapsedTime": 0.228,
    "jobCreateTime": "2024-05-28T19:47:02.512",
    "jobEndTime": "2024-05-28T19:47:02.638",
    "jobId": "JID:0.14",
    "jobQueueTime": 0,
    "jobRequiredCPUs": 1,
    "jobRequiredMemory": 34013184,
    "jobStartTime": "2024-05-28T19:47:02.514",
    "jobStatus": "TERMINATED",
    "node": "172.20.0.2:8095",
    "plan": "{\n   \"operator\" : \"distribute-result\",\n   \"expressions\" : [ \"$$84\" ],\n   \"operatorId\" :
    . . .
    \n            } ]\n         } ]\n      } ]\n   } ]\n}",
    "remoteAddr": "172.20.0.2:53612",
    "requestTime": "2024-05-28T19:47:02.412",
    "scanConsistency": "not_bounded",
    "state": "completed",
    "statement": "select count(*) from hotel_endorsement_view;",
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
    "users": "Administrator",
    "uuid": "91f60338-a3e0-4163-9287-5e723fda29ef"
  }

]
```

### [](#ingestion%5Fstatus)Ingestion Status

GET /analytics/status/ingestion

#### [](#ingestion%5Fstatus-description)Description

Shows the progress of ingestion by the Analytics Service, for each Analytics collection.

Produces

* application/json

#### [](#ingestion%5Fstatus-responses)Responses

| HTTP Code | Description                                                                                                                                                                               | Schema                  |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| 200       | Success. Returns an object giving the ingestion status of each Analytics collection.                                                                                                      | [Ingestion](#Ingestion) |
| 401       | Unauthorized. The user name or password may be incorrect. Returns an object containing an error message. For more information, see [Error Codes](/server/8.0/analytics/error-codes.html). | Object                  |
| 404       | Not found. The path may be incorrect.                                                                                                                                                     |                         |

#### [](#ingestion%5Fstatus-security)Security

| Type         | Name                                                                            |
| ------------ | ------------------------------------------------------------------------------- |
| http (basic) | [Analytics Manage / Analytics Select](#security-AnalyticsManageAnalyticsSelect) |

#### [](#example-http-request-4)Example HTTP Request

curl request

```sh
curl -v -u Administrator:password http://localhost:8095/analytics/status/ingestion
```

#### [](#example-http-response-3)Example HTTP Response

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

### [](#monitor%5Fnode)Pending Mutations

GET /analytics/node/agg/stats/remaining

> [!CAUTION]
> This operation is deprecated, and will be removed in a future release.

#### [](#monitor%5Fnode-description)Description

Shows the number of mutations in the DCP queue that have not yet been ingested by the Analytics Service, for each Analytics collection.

NOTE: This endpoint may not return meaningful results in Couchbase Server 7.0 and later. The reported number of mutations may be different to the actual number of mutations in the Analytics collection. For this reason, this endpoint has been deprecated, and you should use the [Ingestion Status](#ingestion%5Fstatus) endpoint instead.

Produces

* application/json

#### [](#monitor%5Fnode-responses)Responses

| HTTP Code | Description                                                                                                                                                                               | Schema                  |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| 200       | Success. Returns an object giving the number of pending mutations for each Analytics collection.                                                                                          | [Mutations](#Mutations) |
| 401       | Unauthorized. The user name or password may be incorrect. Returns an object containing an error message. For more information, see [Error Codes](/server/8.0/analytics/error-codes.html). | Object                  |
| 404       | Not found. The path may be incorrect.                                                                                                                                                     |                         |

#### [](#monitor%5Fnode-security)Security

| Type         | Name                                                                            |
| ------------ | ------------------------------------------------------------------------------- |
| http (basic) | [Analytics Manage / Analytics Select](#security-AnalyticsManageAnalyticsSelect) |

#### [](#example-http-request-5)Example HTTP Request

curl request

```sh
curl -v -u Administrator:password http://localhost:8095/analytics/node/agg/stats/remaining
```

#### [](#example-http-response-4)Example HTTP Response

Response 200

```json
{
  "Commerce": {
    "orders": 0,
    "customers": 0
  }
}
```

### [](#restart%5Fcluster)Cluster Restart

POST /analytics/cluster/restart

#### [](#restart%5Fcluster-description)Description

Restarts all Analytics Service nodes in the cluster.

Produces

* application/json

#### [](#restart%5Fcluster-responses)Responses

| HTTP Code | Description                                                                                                                                                                               | Schema |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| 202       | Accepted. Returns an object showing the status of the cluster.                                                                                                                            | Object |
| 401       | Unauthorized. The user name or password may be incorrect. Returns an object containing an error message. For more information, see [Error Codes](/server/8.0/analytics/error-codes.html). | Object |
| 404       | Not found. The path may be incorrect.                                                                                                                                                     |        |

#### [](#restart%5Fcluster-security)Security

| Type         | Name                                          |
| ------------ | --------------------------------------------- |
| http (basic) | [Analytics Manage](#security-AnalyticsManage) |

#### [](#example-http-request-6)Example HTTP Request

curl request

```sh
curl -v -u Administrator:password -X POST http://localhost:8095/analytics/cluster/restart
```

#### [](#example-http-response-5)Example HTTP Response

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

### [](#restart%5Fnode)Node Restart

POST /analytics/node/restart

#### [](#restart%5Fnode-description)Description

Restarts the specified Analytics Service node.

Produces

* application/json

#### [](#restart%5Fnode-responses)Responses

| HTTP Code | Description                                                                                                                                                                               | Schema |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| 202       | Accepted. Returns an object showing the status of the node.                                                                                                                               | Object |
| 401       | Unauthorized. The user name or password may be incorrect. Returns an object containing an error message. For more information, see [Error Codes](/server/8.0/analytics/error-codes.html). | Object |
| 404       | Not found. The path may be incorrect.                                                                                                                                                     |        |

#### [](#restart%5Fnode-security)Security

| Type         | Name                                          |
| ------------ | --------------------------------------------- |
| http (basic) | [Analytics Manage](#security-AnalyticsManage) |

#### [](#example-http-request-7)Example HTTP Request

curl request

```sh
curl -v -u Administrator:password -X POST http://localhost:8095/analytics/node/restart
```

#### [](#example-http-response-6)Example HTTP Response

Response 202

```json
{"status": "restarting node"}
```

### [](#return%5Factive%5Frequests)Active Requests

GET /analytics/admin/active_requests

#### [](#return%5Factive%5Frequests-description)Description

Gets a list of the analytic requests that are running.

Produces

* application/json

#### [](#return%5Factive%5Frequests-responses)Responses

| HTTP Code | Description                                                                                                                                                                               | Schema                    |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| 200       | Success. Returns an array id details on the running requests.                                                                                                                             | [Request](#Request) array |
| 401       | Unauthorized. The user name or password may be incorrect. Returns an object containing an error message. For more information, see [Error Codes](/server/8.0/analytics/error-codes.html). | Object                    |
| 404       | Not found. The path may be incorrect.                                                                                                                                                     |                           |

#### [](#return%5Factive%5Frequests-security)Security

| Type         | Name                                                                            |
| ------------ | ------------------------------------------------------------------------------- |
| http (basic) | [Analytics Manage / Analytics Select](#security-AnalyticsManageAnalyticsSelect) |

#### [](#example-http-request-8)Example HTTP Request

curl request

```sh
curl -v -u Administrator:password -X GET \
     http://localhost:8095/analytics/admin/active_requests
```

#### [](#example-http-response-7)Example HTTP Response

Response 200

```json
[
  {
    "cancellable": true,
    "clientContextID": "28379d60-7139-44d6-b57a-95935540b586",
    "elapsedTime": 0.126,
    "jobCreateTime": "2024-05-28T19:47:02.512",
    "jobId": "JID:0.14",
    "jobQueueTime": 0,
    "jobRequiredCPUs": 1,
    "jobRequiredMemory": 34013184,
    "jobStartTime": "2024-05-28T19:47:02.514",
    "jobStatus": "RUNNING",
    "node": "172.20.0.2:8095",
    "remoteAddr": "172.20.0.2:53612",
    "requestTime": "2024-05-28T19:47:02.412",
    "scanConsistency": "not_bounded",
    "state": "running",
    "statement": "select count(*) from hotel_endorsement_view;",
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
    "users": "Administrator",
    "uuid": "91f60338-a3e0-4163-9287-5e723fda29ef"
  }
]
```

## [](#models)Definitions

This section describes the properties consumed and returned by this REST API.

[Ingestion](#Ingestion)  
[Links](#IngestionLink)  
[States](#IngestionLinkState)  
[State Scopes](#IngestionLinkStateScope)  
[State Collections](#IngestionLinkStateScopeColl)  
[Mutations](#Mutations)  
[Collections](#MutationsColl)  
[Request](#Request)  
[Status](#Status)  
[Nodes](#StatusNodes)  
[Partitions](#StatusPartitions)  
[Partition Topology](#StatusTopology)  
[Partition States](#StatusTopologyState)  
[Replicas](#StatusTopologyStateReplicas)

### [](#Ingestion)Ingestion

 Object

| Property          |                                                                                     | Schema                        |
| ----------------- | ----------------------------------------------------------------------------------- | ----------------------------- |
| **links**optional | An array of objects, each giving information about a single linked Analytics scope. | [Links](#IngestionLink) array |

#### Links

 Object

| Property           |                                                                                                                                                                                                           | Schema                              |
| ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| **name**optional   | The name of the link. **Example:** "Local"                                                                                                                                                                | String                              |
| **scope**optional  | The name of the Analytics scope. **Example:** "travel-sample/inventory"                                                                                                                                   | String                              |
| **status**optional | The status of the Analytics scope. **Values:** "healthy", "stopped", "unhealthy", "suspended" **Example:** "healthy"                                                                                      | String                              |
| **state**optional  | An array of objects, each giving the ingestion state of one or more Analytics collections. Analytics collections which have the same ingestion state within this Analytics scope are aggregated together. | [States](#IngestionLinkState) array |

#### States

 Object

| Property                   |                                                                                                                                                                                                                                                                                   | Schema                                         |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **timestamp**required      | The time since epoch that this sample was calculated, in milliseconds. **Example:** 1631273689161                                                                                                                                                                                 | Integer                                        |
| **progress**required       | The percentage (fraction from 0 to 1) of ingestion progress at the current time. **Minimum:** 0 **Maximum:** 1 **Example:** 0                                                                                                                                                     | Double (double)                                |
| **timeLag**optional        | The estimated time that the ingestion lags behind the Data service, in milliseconds. Only displayed for Analytics collections that are not fully ingested. **Example:** 9744                                                                                                      | Integer                                        |
| **itemsProcessed**optional | The number of items ingested since last connect; in other words, the total number of mutations and deletions processed. Only displayed for Analytics collections that are not fully ingested. This value is reset on connect, so it may appear to get smaller. **Example:** 12301 | Integer                                        |
| **seqnoAdvances**optional  | The change in sequence number (seqno) since last connect. Only displayed for Analytics collections that are not fully ingested. **Example:** 61                                                                                                                                   | Integer                                        |
| **scopes**required         | An array of objects, each one giving information about a single Analytics scope.                                                                                                                                                                                                  | [State Scopes](#IngestionLinkStateScope) array |

#### State Scopes

 Object

| Property                |                                                                                       | Schema                                                  |
| ----------------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| **name**required        | The name of the Analytics scope. **Example:** "travel-sample/inventory"               | String                                                  |
| **collections**required | An array of objects, each one giving information about a single Analytics collection. | [State Collections](#IngestionLinkStateScopeColl) array |

#### State Collections

 Object

| Property         |                                                            | Schema |
| ---------------- | ---------------------------------------------------------- | ------ |
| **name**required | The name of the Analytics collection. **Example:** "route" | String |

### [](#Mutations)Mutations

An object containing one or more nested scope objects, one for each available Analytics scope.

 Object

| Property                      |                                                                                                                                                                                                                                         | Schema                        |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| **<scope>**additionalproperty | An object containing one or more collection properties, one for each Analytics collection in the Analytics scope. The name of the object is the name of the Analytics scope, in display form. For example, \`travel-sample\`.inventory. | [Collections](#MutationsColl) |

#### Collections

 Object

| Property                           |                                                                                                                                             | Schema  |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **<collection>**additionalproperty | The number of mutations in the DCP queue that have not yet been ingested. The name of the property is the name of the Analytics collection. | Integer |

### [](#Request)Request

 Object

| Property                      |                                                                                                                                                                 | Schema     |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **cancellable**optional       | Whether this request can be cancelled.                                                                                                                          | Boolean    |
| **clientContextID**optional   | A context ID for debugging purposes. **Example:** "28379d60-7139-44d6-b57a-95935540b586"                                                                        | String     |
| **elapsedTime**optional       | How long the request has been running in seconds. **Example:** 0.126                                                                                            | BigDecimal |
| **jobCreateTime**optional     | The date and time when the request's job was created. **Example:** "2024-05-28T19:47:02.512"                                                                    | String     |
| **jobId**optional             | The request's job ID. This value can be null if request did not run (for example, due to an error). **Example:** "JID:0.14"                                     | String     |
| **jobQueueTime**optional      | How long the request's job has been in the queue waiting to run in seconds. **Example:** 0                                                                      | BigDecimal |
| **jobRequiredCPUs**optional   | The number of CPU cores required to run this request. **Example:** 1                                                                                            | Integer    |
| **jobRequiredMemory**optional | The bytes of RAM being used to process this request. **Example:** 34013184                                                                                      | Integer    |
| **jobStartTime**optional      | The date and time the request's job began running. **Example:** "2024-05-28T19:47:02.514"                                                                       | String     |
| **jobStatus**optional         | The state of the request's job. **Values:** "PENDING", "RUNNING", "TERMINATED", "FAILURE", "FAILURE\_BEFORE\_EXECUTION", "null" **Example:** "RUNNING"          | String     |
| **plan**optional              | The query plan for this request.                                                                                                                                | String     |
| **node**optional              | The Analytics node that received the request. **Example:** "172.20.0.2:8095"                                                                                    | String     |
| **remoteAddr**optional        | The network address and port of the client that made the request. **Example:** "172.20.0.123:53612"                                                             | String     |
| **requestTime**optional       | The date and time the request was received. **Example:** "2024-05-28T19:44:07.730"                                                                              | String     |
| **scanConsistency**optional   | The Scan Consistency setting used for the request's query. **Example:** "not\_bounded"                                                                          | String     |
| **state**optional             | The state of the request. **Values:** "received", "running", "cancelled", "completed" **Example:** "running"                                                    | String     |
| **statement**optional         | The SQL++ query statement being run by the request. **Example:** "select count(\*) from hotel\_endorsement\_view;"                                              | String     |
| **userAgent**optional         | The user agent string of the browser that made the request. **Example:** "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0" | String     |
| **users**optional             | The user who made the request. **Example:** "Administrator"                                                                                                     | String     |
| **uuid**optional              | The unique identifier for this request. **Example:** "91f60338-a3e0-4163-9287-5e723fda29ef"                                                                     | String     |

### [](#Status)Status

 Object

| Property                          |                                                                                                                                                                      | Schema                                |
| --------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| **authorizedNodes**optional       | An array of strings, each of which is the ID of an authorized Analytics node. **Example:** \["86586a966202b5aa4aed31633f330aba","948fb3af810a9b7bc6c76e2a69ba35d9"\] | String array                          |
| **ccNodeId**optional              | The ID of the cluster controller node. **Example:** "86586a966202b5aa4aed31633f330aba"                                                                               | String                                |
| **nodeConfigUri**optional         | The path of the Analytics Node Configuration REST API. **Example:** "/analytics/config/node"                                                                         | String                                |
| **nodeDiagnosticsUri**optional    | The path of the Analytics Node Diagnostics REST API. For internal use only. **Example:** "/analytics/node/diagnostics"                                               | String                                |
| **nodeRestartUri**optional        | The path of the Analytics Node Restart REST API. **Example:** "/analytics/node/restart"                                                                              | String                                |
| **nodeServiceUri**optional        | The path of the Analytics Query Service REST API. **Example:** "/analytics/service"                                                                                  | String                                |
| **serviceConfigUri**optional      | The path of the Analytics Service Configuration REST API. **Example:** "/analytics/config/service"                                                                   | String                                |
| **serviceDiagnosticsUri**optional | The full URI of the Analytics Service Diagnostics REST API. For internal use only. **Example:** "http://localhost:8095/analytics/cluster/diagnostics"                | String                                |
| **serviceRestartUri**optional     | The full URI of the Analytics Cluster Restart REST API. **Example:** "http://localhost:8095/analytics/cluster/restart"                                               | String                                |
| **state**optional                 | The state of the Analytics Service. **Values:** "ACTIVE", "REBALANCE\_REQUIRED", "UNUSABLE", "SHUTTING\_DOWN" **Example:** "ACTIVE"                                  | String                                |
| **nodes**optional                 | An array of objects, each giving information about one Analytics node.                                                                                               | [Nodes](#StatusNodes) array           |
| **partitions**optional            | An array of objects, each giving information about one Analytics partition.                                                                                          | [Partitions](#StatusPartitions) array |
| **partitionsTopology**optional    | An object giving information about the partition topology.                                                                                                           | [Partition Topology](#StatusTopology) |

#### Nodes

 Object

| Property                 |                                                                                                                                        | Schema |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **apiBase**optional      | The URI scheme, host, and port for HTTP access to Analytics REST APIs on this node. **Example:** "http://192.168.8.101:8095"           | String |
| **apiBaseHttps**optional | The URI scheme, host, and port for secure HTTPS access to Analytics REST APIs on this node. **Example:** "https://192.168.8.101:18095" | String |
| **nodeId**optional       | The ID of the node. **Example:** "86586a966202b5aa4aed31633f330aba"                                                                    | String |
| **nodeName**optional     | The name or IP address of the node, including the cluster administration port. **Example:** "192.168.8.101:8091"                       | String |

#### Partitions

 Object

| Property                      |                                                                                                              | Schema  |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------ | ------- |
| **active**optional            | Indicates whether this partition is active. **Example:** true                                                | Boolean |
| **activeNodeId**optional      | The ID of the node where this partition is currently active. **Example:** "86586a966202b5aa4aed31633f330aba" | String  |
| **iodeviceNum**optional       | The number of the IO Device where this partition is located. **Example:** 0                                  | Integer |
| **nodeId**optional            | The ID of the node where this partition originated. **Example:** "86586a966202b5aa4aed31633f330aba"          | String  |
| **partitionId**optional       | The ID of this partition. **Example:** 0                                                                     | Integer |
| **path**optional              | The path of the IO Device where this partition is located. **Example:** "/data/@analytics/v\_iodevice\_0"    | String  |
| **pendingActivation**optional | Indicates whether this partition is waiting to become active. **Example:** false                             | Boolean |

#### Partition Topology

 Object

| Property                      |                                                                                          | Schema                                         |
| ----------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **balanced**optional          | Indicates whether the Analytics nodes are balanced. **Example:** true                    | Boolean                                        |
| **ccNodeId**optional          | The ID of the cluster controller node. **Example:** "86586a966202b5aa4aed31633f330aba"   | String                                         |
| **metadataPartition**optional | The ID of the metadata partition. **Example:** \-1                                       | Integer                                        |
| **numReplicas**optional       | The number of Analytics replicas. **Example:** 1                                         | Integer                                        |
| **revision**optional          | The revision number of the partition topology. **Example:** 1                            | Integer                                        |
| **version**optional           | The version number of the partition topology. **Example:** 1                             | Integer                                        |
| **partitions**optional        | An array of objects, each giving information about the state of one Analytics partition. | [Partition States](#StatusTopologyState) array |

#### Partition States

 Object

| Property             |                                                                                                             | Schema                                         |
| -------------------- | ----------------------------------------------------------------------------------------------------------- | ---------------------------------------------- |
| **id**optional       | The partition ID. **Example:** 0                                                                            | Integer                                        |
| **master**optional   | The ID of the node where the partition is currently active. **Example:** "86586a966202b5aa4aed31633f330aba" | String                                         |
| **origin**optional   | The ID of the node where the partition originated. **Example:** "86586a966202b5aa4aed31633f330aba"          | String                                         |
| **replicas**optional | An array of objects, each giving information about the state of one Analytics replica.                      | [Replicas](#StatusTopologyStateReplicas) array |

#### Replicas

 Object

| Property                 |                                                                                                                                                      | Schema          |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| **location**optional     | The name or IP address of the node where this replica is located, including the Analytics replication port. **Example:** "192.168.8.102:9120"        | String          |
| **nodeId**optional       | The ID of the node where this replica is located. **Example:** "948fb3af810a9b7bc6c76e2a69ba35d9"                                                    | String          |
| **status**optional       | The synchronization status of the replica. **Values:** "IN\_SYNC", "CATCHING\_UP", "DISCONNECTED" **Example:** "IN\_SYNC"                            | String          |
| **syncProgress**optional | The percentage (fraction from 0 to 1) of synchronization progress for this replica at the current time. **Minimum:** 0 **Maximum:** 1 **Example:** 1 | Double (double) |

## [](#security)Security

The Analytics Administration REST APIs support HTTP basic authentication. Pass your credentials through HTTP headers.

### [](#security-AnalyticsManageAnalyticsSelect)Analytics Manage / Analytics Select

For the [Active Requests](#return%5Factive%5Frequests), [Request Cancellation](#cancel%5Frequest), [Completed Requests](#completed%5Frequests), [Ingestion Status](#ingestion%5Fstatus), and [Pending Mutations](#monitor%5Fnode) operations, users must have one of the following access roles:

* Full Admin
* Cluster Admin
* Analytics Manager
* Analytics Reader
* Analytics Select
* Analytics Admin

**Type:** http

### [](#security-ClusterReadPoolsRead)Cluster Read / Pools Read

For the [Cluster Status](#cluster%5Fstatus) operation, users must have one of the following access roles:

* Full Admin
* Cluster Admin
* Read-Only Admin
* Analytics Admin

**Type:** http

### [](#security-AnalyticsManage)Analytics Manage

For the [Cluster Restart](#restart%5Fcluster) and [Node Restart](#restart%5Fnode) operations, users must have one of the following RBAC roles:

* Full Admin
* Cluster Admin
* Analytics Admin

**Type:** http

For more information, see [Roles](../learn/security/roles.md).