[View original HTML](/server/current/analytics-rest-service/index.html)

## [](#overview)Overview

The Analytics Service REST API is provided by the Analytics service. This API enables you to run Analytics queries and set request-level parameters.

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

[Read-Only Query Service (Alternative)](#get%5Fquery)  
[Read-Only Query Service](#get%5Fservice)  
[Query Service (Alternative)](#post%5Fquery)  
[Query Service](#post%5Fservice)

### [](#get%5Fquery)Read-Only Query Service (Alternative)

GET /query/service

#### [](#get%5Fquery-description)Description

An alternative endpoint for the [Read-Only Query Service](#get%5Fservice), provided for tools compatibility.

Produces

* application/json

#### [](#get%5Fquery-parameters)Parameters

Query Parameters

| Name             | Description                                                    | Schema                          |
| ---------------- | -------------------------------------------------------------- | ------------------------------- |
| **body**required | Specify the parameters in the query URL in URL-encoded format. | [Query Parameters](#Parameters) |

#### [](#get%5Fquery-responses)Responses

| HTTP Code | Description                                               | Schema                        |
| --------- | --------------------------------------------------------- | ----------------------------- |
| 200       | The operation was successful.                             | [Query Responses](#Responses) |
| 400       | Bad request. A parameter has an incorrect value.          | [Query Responses](#Responses) |
| 401       | Unauthorized. The user name or password may be incorrect. | [Query Responses](#Responses) |

#### [](#get%5Fquery-security)Security

| Type         | Name                                                                            |
| ------------ | ------------------------------------------------------------------------------- |
| http (basic) | [Analytics Manage / Analytics Select](#security-AnalyticsManageAnalyticsSelect) |

### [](#get%5Fservice)Read-Only Query Service

GET /analytics/service

#### [](#get%5Fservice-description)Description

Enables you to execute a SQL++ for Analytics statement. This method only allows you to run queries and specify query parameters. It does not allow you to run modifying statements.

This is intended for situations where use of the `POST` method is restricted.

Produces

* application/json

#### [](#get%5Fservice-parameters)Parameters

Query Parameters

| Name             | Description                                                    | Schema                          |
| ---------------- | -------------------------------------------------------------- | ------------------------------- |
| **body**required | Specify the parameters in the query URL in URL-encoded format. | [Query Parameters](#Parameters) |

#### [](#get%5Fservice-responses)Responses

| HTTP Code | Description                                               | Schema                        |
| --------- | --------------------------------------------------------- | ----------------------------- |
| 200       | The operation was successful.                             | [Query Responses](#Responses) |
| 400       | Bad request. A parameter has an incorrect value.          | [Query Responses](#Responses) |
| 401       | Unauthorized. The user name or password may be incorrect. | [Query Responses](#Responses) |

#### [](#get%5Fservice-security)Security

| Type         | Name                                                                            |
| ------------ | ------------------------------------------------------------------------------- |
| http (basic) | [Analytics Manage / Analytics Select](#security-AnalyticsManageAnalyticsSelect) |

#### [](#example-http-request)Example HTTP Request

The example below uses a URL-encoded query parameter. The SQL++ statement is `SELECT "hello, beer!" AS greeting`.

curl request

```sh
curl -v -u Administrator:password \
http://localhost:8095/analytics/service?statement=SELECT%20%22hello%2C%20beer%21%22%20AS%20greeting
```

#### [](#example-http-response)Example HTTP Response

Response 200

```json
{
  "requestID": "bbf382b1-4335-4a10-9eca-3b5d1a70b562",
  "signature": {
    "*": "*"
  },
  "results": [ { "greeting": "hello, beer!" }
 ]
  ,
  "plans":{},
  "status": "success",
  "metrics": {
    "elapsedTime": "56.893471ms",
    "executionTime": "51.615165ms",
    "resultCount": 1,
    "resultSize": 31,
    "processedObjects": 0
  }
}
```

### [](#post%5Fquery)Query Service (Alternative)

POST /query/service

#### [](#post%5Fquery-description)Description

An alternative endpoint for the [Query Service](#post%5Fservice), provided for tools compatibility.

Consumes

* application/json
* application/x-www-form-urlencoded

Produces

* application/json

#### [](#post%5Fquery-parameters)Parameters

By default, the API accepts parameters using the `application/x-www-form-urlencoded` MIME type. You can specify the `application/json` MIME type using the `Content-Type` header of the POST request.

Body Parameter

| Name             | Description                                        | Schema                          |
| ---------------- | -------------------------------------------------- | ------------------------------- |
| **Body**required | An object specifying one or more query parameters. | [Query Parameters](#Parameters) |

#### [](#post%5Fquery-responses)Responses

| HTTP Code | Description                                               | Schema                        |
| --------- | --------------------------------------------------------- | ----------------------------- |
| 200       | The operation was successful.                             | [Query Responses](#Responses) |
| 400       | Bad request. A parameter has an incorrect value.          | [Query Responses](#Responses) |
| 401       | Unauthorized. The user name or password may be incorrect. | [Query Responses](#Responses) |

### [](#post%5Fservice)Query Service

POST /analytics/service

#### [](#post%5Fservice-description)Description

Enables you to execute a SQL++ for Analytics statement. This method allows you to run queries and modifying statements, and specify query parameters.

Consumes

* application/json
* application/x-www-form-urlencoded

Produces

* application/json

#### [](#post%5Fservice-parameters)Parameters

By default, the API accepts parameters using the `application/x-www-form-urlencoded` MIME type. You can specify the `application/json` MIME type using the `Content-Type` header of the POST request.

Body Parameter

| Name             | Description                                        | Schema                          |
| ---------------- | -------------------------------------------------- | ------------------------------- |
| **Body**required | An object specifying one or more query parameters. | [Query Parameters](#Parameters) |

#### [](#post%5Fservice-responses)Responses

| HTTP Code | Description                                               | Schema                        |
| --------- | --------------------------------------------------------- | ----------------------------- |
| 200       | The operation was successful.                             | [Query Responses](#Responses) |
| 400       | Bad request. A parameter has an incorrect value.          | [Query Responses](#Responses) |
| 401       | Unauthorized. The user name or password may be incorrect. | [Query Responses](#Responses) |

#### [](#post%5Fservice-security)Security

| Type         | Name                                                                            |
| ------------ | ------------------------------------------------------------------------------- |
| http (basic) | [Analytics Manage / Analytics Select](#security-AnalyticsManageAnalyticsSelect) |

#### [](#example-http-requests)Example HTTP Requests

The example below uses URL-encoded data.

curl request

```sh
curl -v -u Administrator:password \
     --data-urlencode "statement=select 1;" \
     http://localhost:8095/analytics/service
```

The example below posts the same query statement as data of type `application/json` and adds a client context ID.

curl request

```sh
curl -v -u Administrator:password -H "Content-Type: application/json" -d '{
    "statement":"select 1;",
    "pretty":true,
    "client_context_id":"xyz"
}' http://localhost:8095/analytics/service
```

#### [](#example-http-response-2)Example HTTP Response

Response 200

```json
{
  "requestID": "c1984db0-f135-48ee-aea0-39dfe02d55ea",
  "clientContextID": "xyz",
  "signature": {
    "*": "*"
  },
  "results": [ {
    "$1" : 1
  } ]
  ,
  "plans":{},
  "status": "success",
  "metrics": {
    "elapsedTime": "41.969099ms",
    "executionTime": "31.36645ms",
    "resultCount": 1,
    "resultSize": 15,
    "processedObjects": 0
  }
}
```

## [](#models)Definitions

This section describes the properties consumed and returned by this REST API.

[Query Parameters](#Parameters)  
[Common Parameters](#ParametersCommon)  
[Analytics Parameters](#ParametersLocal)  
[Query Responses](#Responses)  
[Common Responses](#ResponsesCommon)  
[Errors](#ResponsesCommonErrors)  
[Warnings](#ResponsesCommonWarnings)  
[Common Metrics](#ResponsesCommonYardsticks)  
[Analytics Responses](#ResponsesLocal)  
[Plans](#ResponsesLocalPlans)  
[Analytics Metrics](#ResponsesLocalYardsticks)

### [](#Parameters)Query Parameters

 Composite Schema

| All of …​                                 |                                               | Schema                                   |
| ----------------------------------------- | --------------------------------------------- | ---------------------------------------- |
| Parameters common with the Query Service. | [Common Parameters](#ParametersCommon)        |                                          |
| and                                       | Parameters specific to the Analytics Service. | [Analytics Parameters](#ParametersLocal) |

#### Common Parameters

 Object

| Property                            |                                                                                                                                                                                                                                                                                                                                             | Schema         |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| **statement**required               | Specifies at least one valid SQL++ for Analytics statement to run.                                                                                                                                                                                                                                                                          | String         |
| **client\_context\_id**optional     | An identifier passed by the client that is returned verbatim in the query response. Useful for matching a particular query to a specific caller.                                                                                                                                                                                            | String         |
| **format**optional                  | Desired format for the query results. Note that the only possible format is JSON. **Values:** "JSON" **Default:** "JSON"                                                                                                                                                                                                                    | String         |
| **pretty**optional                  | If true, the result is indented. **Default:** false                                                                                                                                                                                                                                                                                         | Boolean        |
| **query\_context**optional          | A scope for the statement. The value of this parameter must start with default:, followed by an Analytics scope name. The default: prefix is a dummy and is ignored when resolving an Analytics collection name or synonym name. **Default:** "default:Default"                                                                             | String         |
| **readonly**optional                | If true, then DDL statements are not allowed. **Default:** false                                                                                                                                                                                                                                                                            | Boolean        |
| **scan\_consistency**optional       | The consistency guarantee constraint for index scanning. If not\_bounded, the query is executed immediately. If request\_plus, the required datasets are updated with data available from the Data service at the time of the request before the query is executed. **Values:** "not\_bounded", "request\_plus" **Default:** "not\_bounded" | String         |
| **scan\_wait**optional              | The maximum time to wait for datasets to be updated before the query is executed. The format includes an amount and a unit: ns, us, ms, s, m, or h. The default is "" (no timeout). **Default:** ""                                                                                                                                         | String         |
| **timeout**optional                 | Maximum time to spend on the request before timing out. The format includes an amount and a unit: ns, us, ms, s, m, or h. The default is "" (no timeout). **Default:** ""                                                                                                                                                                   | String         |
| **args**optional                    | An array of positional parameter values.                                                                                                                                                                                                                                                                                                    | Any Type array |
| **<$identifier>**additionalproperty | A named parameter value. **Nullable:** yes                                                                                                                                                                                                                                                                                                  | Any Type       |

#### Analytics Parameters

 Object

| Property                              |                                                                                                                   | Schema          |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | --------------- |
| **plan-format**optional               | The plan format. **Values:** "JSON", "STRING" **Default:** "JSON"                                                 | String          |
| **logical-plan**optional              | If true, the logical plan is included in the query response. **Default:** false                                   | Boolean         |
| **optimized-logical-plan**optional    | If true, the optimized logical plan is included in the query response. **Default:** true                          | Boolean         |
| **expression-tree**optional           | If true, the expression tree is included in the query response. **Default:** false                                | Boolean         |
| **rewritten-expression-tree**optional | If true, the rewritten expression tree is included in the query response. **Default:** false                      | Boolean         |
| **job**optional                       | If true, the job details are included in the query response. **Default:** false                                   | Boolean         |
| **max-warnings**optional              | An integer specifying the maximum number of warning messages to be included in the query response. **Default:** 0 | Integer (int32) |

### [](#Responses)Query Responses

 Composite Schema

| All of …​                                |                                              | Schema                                 |
| ---------------------------------------- | -------------------------------------------- | -------------------------------------- |
| Responses common with the Query Service. | [Common Responses](#ResponsesCommon)         |                                        |
| and                                      | Responses specific to the Analytics Service. | [Analytics Responses](#ResponsesLocal) |

#### Common Responses

 Object

| Property                    |                                                                                                                                                                                                                                                                                                                                                                                                                                 | Schema                                       |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| **requestID**optional       | A unique identifier for the response.                                                                                                                                                                                                                                                                                                                                                                                           | UUID (UUID)                                  |
| **clientContextID**optional | The client context ID of the request, if one was supplied — refer to client\_context\_id in [Query Parameters](#Parameters).                                                                                                                                                                                                                                                                                                    | String                                       |
| **signature**optional       | The schema of the results. Present only when the query completes successfully.                                                                                                                                                                                                                                                                                                                                                  | Object                                       |
| **results**optional         | An array of all the objects returned by the query. An object can be any JSON value.                                                                                                                                                                                                                                                                                                                                             | Any Type array                               |
| **status**optional          | The status of the request. **Values:** "success", "running", "failed", "timeout", "fatal"                                                                                                                                                                                                                                                                                                                                       | String                                       |
| **errors**optional          | An array of error objects. Present only if 1 or more errors are returned during processing of the request. Each error is represented by an object in this list.                                                                                                                                                                                                                                                                 | [Errors](#ResponsesCommonErrors) array       |
| **warnings**optional        | An array of warning objects. Present only if 1 or more warnings are returned during processing of the request. Each warning is represented by an object in this list. Note that you can specify the maximum number of warning messages to be returned in the query response — refer to max-warnings in [Query Parameters](#Parameters). By default, no warnings are returned, even if warnings have occurred during processing. | [Warnings](#ResponsesCommonWarnings) array   |
| **metrics**optional         | An object containing metrics about the request.                                                                                                                                                                                                                                                                                                                                                                                 | [Common Metrics](#ResponsesCommonYardsticks) |

#### Errors

 Object

| Property         |                                                                                                           | Schema  |
| ---------------- | --------------------------------------------------------------------------------------------------------- | ------- |
| **code**optional | A number that identifies the error.                                                                       | Integer |
| **msg**optional  | A message describing the error in detail. Refer to [Error Codes](/server/8.0/analytics/error-codes.html). | String  |

#### Warnings

 Object

| Property         |                                             | Schema  |
| ---------------- | ------------------------------------------- | ------- |
| **code**optional | A number that identifies the warning.       | Integer |
| **msg**optional  | A message describing the warning in detail. | String  |

#### Common Metrics

 Object

| Property                  |                                                                                                                                      | Schema             |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------ |
| **elapsedTime**optional   | The total time taken for the request, that is the time from when the request was received until the results were returned.           | String             |
| **executionTime**optional | The time taken for the execution of the request, that is the time from when query execution started until the results were returned. | String             |
| **resultCount**optional   | The total number of objects in the results.                                                                                          | Integer (unsigned) |
| **resultSize**optional    | The total number of bytes in the results.                                                                                            | Integer (unsigned) |
| **errorCount**optional    | The number of errors that occurred during the request.                                                                               | Integer (unsigned) |
| **warningCount**optional  | The number of warnings that occurred during the request.                                                                             | Integer (unsigned) |

#### Analytics Responses

 Object

| Property            |                                                     | Schema                                         |
| ------------------- | --------------------------------------------------- | ---------------------------------------------- |
| **plans**optional   | An object containing the query plans, if requested. | [Plans](#ResponsesLocalPlans)                  |
| **metrics**optional | An object containing metrics about the request.     | [Analytics Metrics](#ResponsesLocalYardsticks) |

#### Plans

 Object

| Property                            |                                | Schema |
| ----------------------------------- | ------------------------------ | ------ |
| **logicalPlan**optional             | The logical plan.              | Object |
| **optimizedLogicalPlan**optional    | The optimized logical plan.    | Object |
| **rewrittenExpressionTree**optional | The rewritten expression tree. | String |
| **expressionTree**optional          | The expression tree.           | String |
| **job**optional                     | The job details.               | Object |

|  | The structure and content of query plans is expected to change as development of the query processor progresses. |
|  | ---------------------------------------------------------------------------------------------------------------- |

#### Analytics Metrics

 Object

| Property                     |                                                    | Schema       |
| ---------------------------- | -------------------------------------------------- | ------------ |
| **processedObjects**optional | Number of processed tuples during query execution. | Long (int64) |

## [](#security)Security

The Analytics Service REST API supports HTTP basic authentication. Pass your credentials through HTTP headers.

### [](#security-AnalyticsManageAnalyticsSelect)Analytics Manage / Analytics Select

Users must have one of the following RBAC roles:

* Full Admin
* Cluster Admin
* Analytics Manager
* Analytics Reader
* Analytics Select
* Analytics Admin

**Type:** http

For more information, see [Roles](../learn/security/roles.md).