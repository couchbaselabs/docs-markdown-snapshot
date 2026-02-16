[View original HTML](/enterprise-analytics/2.0/analytics-rest-service/index.html)

* postRequest
* getRead-Only Request

[API docs by Redocly](https://redocly.com/redoc/)

# Enterprise Analytics Request REST API (2.0)

Download OpenAPI specification:

This API enables you to run Enterprises Analytics Service requests and set request-level parameters.

## [](#operation/post%5Fservice)Request 

Enables you to execute a SQL++ for Enteprise Analytics statement. This method allows you to run queries and modifying statements, and specify query parameters.

##### Authorizations:

_AnalyticsManageAnalyticsAccess_

##### Request Body schema: 

application/jsonapplication/x-www-form-urlencodedapplication/json

required

An object specifying one or more query parameters.

| statementrequired                  | string Specifies at least one valid SQL++ for Enterprise Analytics statement to run.                                                                                                                                                                                                                                                    |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| client\_context\_id                | string An identifier passed by the client that is returned verbatim in the query response. Useful for matching a particular query to a specific caller.                                                                                                                                                                                 |
| format                             | string Default: "JSON" Value: "JSON" Desired format for the query results. Note that the only possible format is JSON.                                                                                                                                                                                                                  |
| pretty                             | boolean Default: false If true, the result is indented.                                                                                                                                                                                                                                                                                 |
| query\_context                     | string Default: "default:Default" A scope for the statement. The value of this parameter must start with default:, followed by a scope name. The default: prefix is a dummy and is ignored when resolving a collection name or synonym name.                                                                                            |
| readonly                           | boolean Default: false If true, then DDL statements are not allowed.                                                                                                                                                                                                                                                                    |
| scan\_consistency                  | string Default: "not\_bounded" Enum: "not\_bounded" "request\_plus" The consistency guarantee constraint for index scanning. If not\_bounded, the query is executed immediately. If request\_plus, the required datasets are updated with data available from the Data service at the time of the request before the query is executed. |
| scan\_wait                         | string Default: "" The maximum time to wait for datasets to be updated before the query is executed. The format includes an amount and a unit: ns, us, ms, s, m, or h. The default is "" (no timeout).                                                                                                                                  |
| timeout                            | string Default: "" Maximum time to spend on the request before timing out. The format includes an amount and a unit: ns, us, ms, s, m, or h. The default is "" (no timeout).                                                                                                                                                            |
| args                               | Array of any An array of positional parameter values.                                                                                                                                                                                                                                                                                   |
| plan-format                        | string Default: "JSON" Enum: "JSON" "STRING" The plan format.                                                                                                                                                                                                                                                                           |
| logical-plan                       | boolean Default: false If true, the logical plan is included in the query response.                                                                                                                                                                                                                                                     |
| optimized-logical-plan             | boolean Default: true If true, the optimized logical plan is included in the query response.                                                                                                                                                                                                                                            |
| expression-tree                    | boolean Default: false If true, the expression tree is included in the query response.                                                                                                                                                                                                                                                  |
| rewritten-expression-tree          | boolean Default: false If true, the rewritten expression tree is included in the query response.                                                                                                                                                                                                                                        |
| job                                | boolean Default: false If true, the job details are included in the query response.                                                                                                                                                                                                                                                     |
| max-warnings                       | integer <int32\> Default: 0 An integer specifying the maximum number of warning messages to be included in the query response.                                                                                                                                                                                                          |
| property name\*additional property | any A named parameter value.                                                                                                                                                                                                                                                                                                            |

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
* "query_context": "default:Default",
* "readonly": false,
* "scan_consistency": "not_bounded",
* "scan_wait": "",
* "timeout": "",
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