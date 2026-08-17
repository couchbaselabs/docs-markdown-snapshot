---
title: Analytics Service REST API
description: A description of the Service REST API for Couchbase Analytics.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/analytics-rest-service/pages/index.adoc
  xref: xref:enterprise-analytics:analytics-rest-service:index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/analytics-rest-service/index.html)

# Analytics Service REST API

* postRequest
* getRead-Only Request
* getRequest Status
* getRetrieve Request Result
* delDiscard Request Result

[API docs by Redocly](https://redocly.com/redoc/)

# Enterprise Analytics Request REST API (2.2)

Download OpenAPI specification:

This API enables you to run Enterprise Analytics Service requests and set request-level parameters.

## [](#operation/post%5Fservice)Request 

Enables you to execute a SQL++ for Enterprise Analytics statement. This method allows you to run queries and modifying statements, and specify query parameters.

##### Authorizations:

_AnalyticsManageAnalyticsAccess_

##### Request Body schema: 

application/jsonapplication/x-www-form-urlencodedapplication/json

required

An object specifying one or more query parameters.

| statementrequired                  | string Specifies at least one valid SQL++ for Enterprise Analytics statement to run.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| client\_context\_id                | string An identifier passed by the client that is returned verbatim in the query response. Useful for matching a particular query to a specific caller.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| format                             | string Default: "JSON" Value: "JSON" Desired format for the query results. Note that the only possible format is JSON.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| pretty                             | boolean Default: false If true, the result is indented.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| query\_context                     | string Default: "default:Default.Default" A scope for the statement. The value of this parameter must start with default:, followed by a scope name. The default: prefix is a dummy and is ignored when resolving a collection name or synonym name.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| readonly                           | boolean Default: false If true, then DDL statements are not allowed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| scan\_consistency                  | string Default: "not\_bounded" Enum: "not\_bounded" "request\_plus" The consistency guarantee constraint for index scanning. If not\_bounded, the query is executed immediately. If request\_plus, the required collections are updated with data available from the Data service at the time of the request before the query is executed.                                                                                                                                                                                                                                                                                                                                                       |
| scan\_wait                         | string Default: "" The maximum time to wait for collections to be updated before the query is executed. The format includes an amount and a unit: ns, us, ms, s, m, or h. The default is "" (no timeout).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| timeout                            | string Default: "" Maximum time to spend on the request before timing out. The format includes an amount and a unit: ns, us, ms, s, m, or h. The default is "" (no timeout).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| mode                               | string Default: "immediate" Enum: "immediate" "async" The execution mode of the request. If immediate, the request is executed and the result is returned immediately. If async, the request is executed asynchronously and the client can retrieve the result later. All async requests can be viewed using the [Open Requests](../analytics-rest-admin/index.html#operation/open%5Frequests) endpoint, or going to the Open requests under the monitor page in UI workbench. The status and result of an async request can be retrieved using the endpoints described in [Request Status](#operation/get%5Frequest%5Fstatus) and [Retrieve Request Result](#operation/get%5Frequest%5Fresult). |
| result-ttl                         | string Default: "" Maximum time to retain the result of an async request. The format includes an amount and a unit: ns, us, ms, s, m, or h. The default is "" (use system default).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| args                               | Array of any An array of positional parameter values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| plan-format                        | string Default: "JSON" Enum: "JSON" "STRING" The plan format.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| logical-plan                       | boolean Default: false If true, the logical plan is included in the query response.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| optimized-logical-plan             | boolean Default: true If true, the optimized logical plan is included in the query response.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| expression-tree                    | boolean Default: false If true, the expression tree is included in the query response.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| rewritten-expression-tree          | boolean Default: false If true, the rewritten expression tree is included in the query response.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| job                                | boolean Default: false If true, the job details are included in the query response.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| max-warnings                       | integer <int32\> Default: 0 An integer specifying the maximum number of warning messages to be included in the query response.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| property name\*additional property | any A named parameter value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

### Responses

**200** 

The operation was successful.

**400** 

Bad request. A parameter has an incorrect value.

**401** 

Unauthorized. The user name or password may be incorrect.

post/api/v1/request

The URL scheme, host, and port are as follows.

{scheme}://{host}:{port}/api/v1/request

### Request samples 

* Payload

Content type

application/jsonapplication/x-www-form-urlencodedapplication/json

Copy

 Expand all  Collapse all 

`{
* "statement": "string",
* "client_context_id": "string",
* "format": "JSON",
* "pretty": false,
* "query_context": "default:Default.Default",
* "readonly": false,
* "scan_consistency": "not_bounded",
* "scan_wait": "",
* "timeout": "",
* "mode": "immediate",
* "result-ttl": "",
* "args": [
  * null  
],
* "property1": null,
* "property2": null,
* "plan-format": "JSON",
* "logical-plan": false,
* "optimized-logical-plan": true,
* "expression-tree": false,
* "rewritten-expression-tree": false,
* "job": false,
* "max-warnings": 0
}`

### Response samples 

* 200
* 400
* 401

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "requestID": "string",
* "handle": "string",
* "clientContextID": "string",
* "signature": { },
* "results": [
  * null  
],
* "status": "success",
* "errors": [
  * {
    * "code": 0,
    * "msg": "string"  
  }  
],
* "warnings": [
  * {
    * "code": 0,
    * "msg": "string"  
  }  
],
* "metrics": {
  * "elapsedTime": "string",
  * "compileTime": "string",
  * "queueWaitTime": "string",
  * "executionTime": "string",
  * "resultCount": 0,
  * "resultSize": 0,
  * "errorCount": 0,
  * "warningCount": 0,
  * "processedObjects": 0  
},
* "plans": {
  * "logicalPlan": { },
  * "optimizedLogicalPlan": { },
  * "rewrittenExpressionTree": "string",
  * "expressionTree": "string",
  * "job": { }  
}
}`

## [](#operation/get%5Fservice)Read-Only Request 

Enables you to execute a SQL++ for Enterprise Analytics statement. This method only allows you to run queries and specify query parameters. It does not allow you to run modifying statements.

This is intended for situations where use of the `POST` method is restricted.

##### Authorizations:

_AnalyticsManageAnalyticsAccess_

##### query Parameters

| bodyrequired | object (Query Parameters) Specify the parameters in the query URL in URL-encoded format. |
| ------------ | ---------------------------------------------------------------------------------------- |

### Responses

**200** 

The operation was successful.

**400** 

Bad request. A parameter has an incorrect value.

**401** 

Unauthorized. The user name or password may be incorrect.

get/api/v1/request

The URL scheme, host, and port are as follows.

{scheme}://{host}:{port}/api/v1/request

### Response samples 

* 200
* 400
* 401

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "requestID": "string",
* "handle": "string",
* "clientContextID": "string",
* "signature": { },
* "results": [
  * null  
],
* "status": "success",
* "errors": [
  * {
    * "code": 0,
    * "msg": "string"  
  }  
],
* "warnings": [
  * {
    * "code": 0,
    * "msg": "string"  
  }  
],
* "metrics": {
  * "elapsedTime": "string",
  * "compileTime": "string",
  * "queueWaitTime": "string",
  * "executionTime": "string",
  * "resultCount": 0,
  * "resultSize": 0,
  * "errorCount": 0,
  * "warningCount": 0,
  * "processedObjects": 0  
},
* "plans": {
  * "logicalPlan": { },
  * "optimizedLogicalPlan": { },
  * "rewrittenExpressionTree": "string",
  * "expressionTree": "string",
  * "job": { }  
}
}`

## [](#operation/get%5Frequest%5Fstatus)Request Status 

Enables you to get the status of a request that was executed in `async` mode.

##### Authorizations:

_AnalyticsManageAnalyticsAccess_

##### path Parameters

| request\_idrequired | string <UUID\> The unique identifier of the request.          |
| ------------------- | ------------------------------------------------------------- |
| job\_idrequired     | string The identifier of the job associated with the request. |

### Responses

**200** 

The operation was successful.

**400** 

Bad request. A parameter has an incorrect value.

**401** 

Unauthorized. The user name or password may be incorrect.

**404** 

Not found. The specified request ID or job ID does not exist, or the result has expired.

get/api/v1/request/status/{request\_id}/{job\_id}

The URL scheme, host, and port are as follows.

{scheme}://{host}:{port}/api/v1/request/status/{request\_id}/{job\_id}

### Response samples 

* 200

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "status": "success",
* "handle": "string",
* "resultCount": 0,
* "partitions": [
  * {
    * "handle": "string",
    * "resultCount": 0  
  }  
],
* "resultSetOrdered": true,
* "errors": [
  * {
    * "code": 0,
    * "msg": "string"  
  }  
],
* "warnings": [
  * {
    * "code": 0,
    * "msg": "string"  
  }  
],
* "metrics": {
  * "elapsedTime": "string",
  * "compileTime": "string",
  * "queueWaitTime": "string",
  * "executionTime": "string",
  * "resultCount": 0,
  * "resultSize": 0,
  * "errorCount": 0,
  * "warningCount": 0,
  * "processedObjects": 0  
},
* "createdAt": "2019-08-24T14:15:22Z"
}`

## [](#operation/get%5Frequest%5Fresult)Retrieve Request Result 

Enables you to retrieve the result of a request that was executed in `async` mode.

##### Authorizations:

_AnalyticsManageAnalyticsAccess_

##### path Parameters

| request\_idrequired | string <UUID\> The unique identifier of the request.          |
| ------------------- | ------------------------------------------------------------- |
| job\_idrequired     | string The identifier of the job associated with the request. |

### Responses

**200** 

The operation was successful.

**400** 

Bad request. A parameter has an incorrect value.

**401** 

Unauthorized. The user name or password may be incorrect.

**404** 

Not found. The specified request ID or job ID does not exist, or the result has expired.

get/api/v1/request/result/{request\_id}/{job\_id}

The URL scheme, host, and port are as follows.

{scheme}://{host}:{port}/api/v1/request/result/{request\_id}/{job\_id}

### Response samples 

* 200

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "results": [
  * { }  
],
* "metrics": {
  * "elapsedTime": "string",
  * "compileTime": "string",
  * "queueWaitTime": "string",
  * "executionTime": "string",
  * "resultCount": 0,
  * "resultSize": 0,
  * "errorCount": 0,
  * "warningCount": 0,
  * "processedObjects": 0  
},
* "profile": { },
* "createdAt": "2019-08-24T14:15:22Z"
}`

## [](#operation/delete%5Frequest%5Fresult)Discard Request Result 

Enables you to discard the result of a request that was executed in `async` mode.

##### Authorizations:

_AnalyticsManageAnalyticsAccess_

##### path Parameters

| request\_idrequired | string <UUID\> The unique identifier of the request.          |
| ------------------- | ------------------------------------------------------------- |
| job\_idrequired     | string The identifier of the job associated with the request. |

### Responses

**202** 

The operation was accepted.

**400** 

Bad request. A parameter has an incorrect value.

**401** 

Unauthorized. The user name or password may be incorrect.

**404** 

Not found. The specified request ID or job ID does not exist, or the result has expired.

delete/api/v1/request/result/{request\_id}/{job\_id}

The URL scheme, host, and port are as follows.

{scheme}://{host}:{port}/api/v1/request/result/{request\_id}/{job\_id}