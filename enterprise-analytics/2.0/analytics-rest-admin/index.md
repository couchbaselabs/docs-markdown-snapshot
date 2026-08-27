---
title: Analytics Administration REST API
description: A description of the Administration REST APIs for Couchbase
  Enterprise Analytics.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/analytics-rest-admin/pages/index.adoc
  xref: xref:2.0@enterprise-analytics:analytics-rest-admin:index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.0/analytics-rest-admin/index.html)

# Analytics Administration REST API

* delRequest Cancellation
* getActive Requests
* getCompleted Requests
* getService Status
* postService Restart
* postNode Restart
* getIngestion Status

[API docs by Redocly](https://redocly.com/redoc/)

# Enterprise Analytics Administration REST APIs (2.0)

Download OpenAPI specification:

These APIs enable you to manage and monitor the Enterprise Analytics Service.

## [](#operation/cancel%5Frequest)Request Cancellation 

Cancels an active request.

##### Authorizations:

_AnalyticsManageAnalyticsAccess_

##### Request Body schema: application/x-www-form-urlencoded

| client\_context\_idrequired | string Identifier passed by the client that's used to identify an active request to be cancelled. |
| --------------------------- | ------------------------------------------------------------------------------------------------- |

### Responses

**200** 

The operation was successful.

**400** 

Bad request. Incorrect parameter or missing value.

**401** 

Unauthorized. The user name or password may be incorrect.

Returns an object containing an error message. Refer to [Error Codes](/server/7.6/analytics/error-codes.html).

**404** 

Not found. The path may be incorrect, or there is no active request with the specified identifier.

delete/api/v1/active\_requests

The URL scheme, host, and port are as follows.

{scheme}://{host}:{port}/api/v1/active\_requests

### Response samples 

* 401

Content type

application/json

Copy

`{ }`

## [](#operation/return%5Factive%5Frequests)Active Requests 

Gets a list of the requests that are running.

##### Authorizations:

_AnalyticsManageAnalyticsAccess_

### Responses

**200** 

Success. Returns an array id details on the running requests.

**401** 

Unauthorized. The user name or password may be incorrect.

Returns an object containing an error message. Refer to [Error Codes](/server/7.6/analytics/error-codes.html).

**404** 

Not found. The path may be incorrect.

get/api/v1/active\_requests

The URL scheme, host, and port are as follows.

{scheme}://{host}:{port}/api/v1/active\_requests

### Response samples 

* 200
* 401

Content type

application/json

Copy

 Expand all  Collapse all 

`[
* {
  * "cancellable": true,
  * "clientContextID": "28379d60-7139-44d6-b57a-95935540b586",
  * "elapsedTime": 0.126,
  * "jobCreateTime": "2024-05-28T19:47:02.512",
  * "jobId": "JID:0.14",
  * "jobQueueTime": 0,
  * "jobRequiredCPUs": 1,
  * "jobRequiredMemory": 34013184,
  * "jobStartTime": "2024-05-28T19:47:02.514",
  * "jobStatus": "RUNNING",
  * "plan": "string",
  * "node": "172.20.0.2:8095",
  * "remoteAddr": "172.20.0.123:53612",
  * "requestTime": "2024-05-28T19:44:07.730",
  * "scanConsistency": "not_bounded",
  * "state": "running",
  * "statement": "select count(*) from hotel_endorsement_view;",
  * "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
  * "users": "Administrator",
  * "uuid": "91f60338-a3e0-4163-9287-5e723fda29ef"  
}
]`

## [](#operation/completed%5Frequests)Completed Requests 

Gets a list of all completed requests.

##### Authorizations:

_AnalyticsManageAnalyticsAccess_

### Responses

**200** 

Success. Returns a list of all completed requests.

**401** 

Unauthorized. The user name or password may be incorrect.

Returns an object containing an error message. Refer to [Error Codes](/server/7.6/analytics/error-codes.html).

**404** 

Not found. The path may be incorrect.

get/api/v1/completed\_requests

The URL scheme, host, and port are as follows.

{scheme}://{host}:{port}/api/v1/completed\_requests

### Response samples 

* 200
* 401

Content type

application/json

Copy

 Expand all  Collapse all 

`[
* {
  * "cancellable": true,
  * "clientContextID": "28379d60-7139-44d6-b57a-95935540b586",
  * "elapsedTime": 0.126,
  * "jobCreateTime": "2024-05-28T19:47:02.512",
  * "jobId": "JID:0.14",
  * "jobQueueTime": 0,
  * "jobRequiredCPUs": 1,
  * "jobRequiredMemory": 34013184,
  * "jobStartTime": "2024-05-28T19:47:02.514",
  * "jobStatus": "RUNNING",
  * "plan": "string",
  * "node": "172.20.0.2:8095",
  * "remoteAddr": "172.20.0.123:53612",
  * "requestTime": "2024-05-28T19:44:07.730",
  * "scanConsistency": "not_bounded",
  * "state": "running",
  * "statement": "select count(*) from hotel_endorsement_view;",
  * "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
  * "users": "Administrator",
  * "uuid": "91f60338-a3e0-4163-9287-5e723fda29ef"  
}
]`

## [](#operation/service%5Fstatus)Service Status 

Shows various details about the current status of the Enterprise Analytics Service, such as the service state, and the state of each node partition.

##### Authorizations:

_ClusterReadPoolsRead_

### Responses

**200** 

Success. Returns an object giving the current status of the Analytics Service.

**401** 

Unauthorized. The user name or password may be incorrect.

Returns an object containing an error message. Refer to [Error Codes](/server/7.6/analytics/error-codes.html).

**404** 

Not found. The path may be incorrect.

get/api/v1/status/service

The URL scheme, host, and port are as follows.

{scheme}://{host}:{port}/api/v1/status/service

### Response samples 

* 200
* 401

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "authorizedNodes": [
  * "86586a966202b5aa4aed31633f330aba",
  * "948fb3af810a9b7bc6c76e2a69ba35d9"  
],
* "ccNodeId": "86586a966202b5aa4aed31633f330aba",
* "nodeConfigUri": "/api/v1/config/node",
* "nodeDiagnosticsUri": "/api/v1/node/diagnostics",
* "nodeRestartUri": "/api/v1/node/restart",
* "serviceRequestUri": "/api/v1/request",
* "serviceConfigUri": "/api/v1/config/service",
* "serviceRestartUri": "/api/v1/service/restart",
* "state": "ACTIVE",
* "nodes": [
  * {
    * "apiBase": "<http://192.168.8.101:8095>",
    * "apiBaseHttps": "<https://192.168.8.101:18095>",
    * "nodeId": "86586a966202b5aa4aed31633f330aba",
    * "nodeName": "192.168.8.101:8091"  
  }  
],
* "partitions": [
  * {
    * "active": true,
    * "activeNodeId": "86586a966202b5aa4aed31633f330aba",
    * "iodeviceNum": 0,
    * "nodeId": "86586a966202b5aa4aed31633f330aba",
    * "partitionId": 0,
    * "path": "/data/@analytics/v_iodevice_0",
    * "pendingActivation": false  
  }  
],
* "partitionsTopology": {
  * "balanced": true,
  * "ccNodeId": "86586a966202b5aa4aed31633f330aba",
  * "metadataPartition": -1,
  * "numReplicas": 1,
  * "revision": 1,
  * "version": 1,
  * "partitions": [
    * {
      * "id": 0,
      * "master": "86586a966202b5aa4aed31633f330aba",
      * "origin": "86586a966202b5aa4aed31633f330aba"  
      }  
  ]  
}
}`

## [](#operation/restart%5Fservice)Service Restart 

Restarts the Enterprise Analytics Service in all nodes in the cluster.

##### Authorizations:

_AnalyticsManage_

### Responses

**202** 

Accepted. Returns an object showing the status of the cluster.

**401** 

Unauthorized. The user name or password may be incorrect.

Returns an object containing an error message. Refer to [Error Codes](/server/7.6/analytics/error-codes.html).

**404** 

Not found. The path may be incorrect.

post/api/v1/service/restart

The URL scheme, host, and port are as follows.

{scheme}://{host}:{port}/api/v1/service/restart

### Response samples 

* 202
* 401

Content type

application/json

Copy

`{ }`

## [](#operation/restart%5Fnode)Node Restart 

Restarts the Enterprise Analytics Service on the target node.

##### Authorizations:

_AnalyticsManage_

### Responses

**202** 

Accepted. Returns an object showing the status of the node.

**401** 

Unauthorized. The user name or password may be incorrect.

Returns an object containing an error message. Refer to [Error Codes](/server/7.6/analytics/error-codes.html).

**404** 

Not found. The path may be incorrect.

post/api/v1/node/restart

The URL scheme, host, and port are as follows.

{scheme}://{host}:{port}/api/v1/node/restart

### Response samples 

* 202
* 401

Content type

application/json

Copy

`{ }`

## [](#operation/ingestion%5Fstatus)Ingestion Status 

Shows the progress of ingestion for each collection.

##### Authorizations:

_AnalyticsManageAnalyticsAccess_

### Responses

**200** 

Success. Returns an object giving the ingestion status of each collection.

**401** 

Unauthorized. The user name or password may be incorrect.

Returns an object containing an error message. Refer to [Error Codes](/server/7.6/analytics/error-codes.html).

**404** 

Not found. The path may be incorrect.

get/api/v1/status/ingestion

The URL scheme, host, and port are as follows.

{scheme}://{host}:{port}/api/v1/status/ingestion

### Response samples 

* 200
* 401

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "links": [
  * {
    * "name": "Local",
    * "status": "healthy",
    * "state": [
      * {
        * "timestamp": 1631273689161,
        * "progress": 0,
        * "timeLag": 9744,
        * "itemsProcessed": 12301,
        * "seqnoAdvances": 61,
        * "scopes": [
          * {
            * "name": "travel-sample/inventory",
            * "collections": [
              * {
                * "name": "route"  
                                                        }  
                                          ]  
                              }  
                    ]  
            }  
      ],
    * "scope": "travel-sample/inventory"  
  }  
]
}`