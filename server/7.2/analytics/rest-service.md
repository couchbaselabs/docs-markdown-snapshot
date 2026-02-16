[View original HTML](/server/7.2/analytics/rest-service.html)

## [](#%5Foverview)Overview

The Analytics Service REST API is provided by the Analytics service. This API enables you to run Analytics queries and set request-level parameters.

The API schemes and host URLs are as follows:

* <http://node:8095/>
* <https://node:18095/> (for secure access)

where `node` is the host name or IP address of a node running the Analytics service.

### [](#version-information)Version information

_Version_ : 7.2

### [](#consumes)Consumes

* `application/x-www-form-urlencoded`
* `application/json`

### [](#produces)Produces

* `application/json`

## [](#%5Fpaths)Paths

This section describes the operations available with this REST API.

* [Query Service](#%5Fpost%5Fservice)
* [Read-Only Query Service](#%5Fget%5Fservice)
* [Query Service (Alternative)](#%5Fpost%5Fquery)
* [Read-Only Query Service (Alternative)](#%5Fget%5Fquery)

### [](#%5Fpost%5Fservice)Query Service

POST /analytics/service

#### [](#description)Description

Enables you to execute a SQL++ for Analytics statement. This method allows you to run queries and modifying statements, and specify query parameters.

#### [](#parameters)Parameters

By default, the API accepts parameters using the `application/x-www-form-urlencoded` MIME type. You can specify the `application/json` MIME type using the `Content-Type` header of the POST request.

| Type     | Name                      | Description                                        | Schema                                     |
| -------- | ------------------------- | -------------------------------------------------- | ------------------------------------------ |
| **Body** | **Parameters** _required_ | An object specifying one or more query parameters. | [Query Parameters](#%5Fquery%5Fparameters) |

#### [](#responses)Responses

| HTTP Code | Description                                               | Schema                                   |
| --------- | --------------------------------------------------------- | ---------------------------------------- |
| **200**   | The operation was successful.                             | [Query Responses](#%5Fquery%5Fresponses) |
| **400**   | Bad request. A parameter has an incorrect value.          | [Query Responses](#%5Fquery%5Fresponses) |
| **401**   | Unauthorized. The user name or password may be incorrect. | [Query Responses](#%5Fquery%5Fresponses) |

#### [](#security)Security

| Type      | Name                                                                                   |
| --------- | -------------------------------------------------------------------------------------- |
| **basic** | **[Analytics Manage / Analytics Select](#%5Fanalytics%5Fmanage%5Fanalytics%5Fselect)** |

#### [](#example-http-request)Example HTTP request

The example below uses URL-encoded data.

Curl request

```sh
curl -v -u Administrator:password \
     --data-urlencode "statement=select 1;" \
     http://localhost:8095/analytics/service
```

The example below posts the same query statement as data of type `application/json` and adds a client context ID.

Curl request

```sh
curl -v -u Administrator:password -H "Content-Type: application/json" -d '{
    "statement":"select 1;",
    "pretty":true,
    "client_context_id":"xyz"
}' http://localhost:8095/analytics/service
```

#### [](#example-http-response)Example HTTP response

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

### [](#%5Fget%5Fservice)Read-Only Query Service

GET /analytics/service

#### [](#description-2)Description

Enables you to execute a SQL++ for Analytics statement. This method only allows you to run queries and specify query parameters. It does not allow you to run modifying statements.

This is intended for situations where use of the `POST` method is restricted.

#### [](#parameters-2)Parameters

| Type      | Name                                     | Description                                                                                                                                                                                                                                                         | Schema                             | Default           |
| --------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- | ----------------- |
| **Query** | **statement** _required_                 | Specifies at least one valid SQL++ for Analytics statement to run.                                                                                                                                                                                                  | string                             |                   |
| **Query** | **client\_context\_id** _optional_       | An identifier passed by the client that is returned verbatim in the query response. Useful for matching a particular query to a specific caller.                                                                                                                    | string                             |                   |
| **Query** | **format** _optional_                    | Desired format for the query results. Note that the only possible format is JSON.                                                                                                                                                                                   | enum (JSON)                        | "JSON"            |
| **Query** | **pretty** _optional_                    | If true, the result is indented.                                                                                                                                                                                                                                    | boolean                            | "false"           |
| **Query** | **query\_context** _optional_            | A scope for the statement. The value of this parameter must start with default:, followed by an Analytics scope name. The default: prefix is a dummy and is ignored when resolving an Analytics collection name or synonym name.                                    | string                             | "default:Default" |
| **Query** | **readonly** _optional_                  | If true, then DDL statements are not allowed.                                                                                                                                                                                                                       | boolean                            | "false"           |
| **Query** | **scan\_consistency** _optional_         | The consistency guarantee constraint for index scanning. If not\_bounded, the query is executed immediately. If request\_plus, the required datasets are updated with data available from the Data service at the time of the request before the query is executed. | enum (not\_bounded, request\_plus) | "not\_bounded"    |
| **Query** | **scan\_wait** _optional_                | The maximum time to wait for datasets to be updated before the query is executed. The format includes an amount and a unit: ns, us, ms, s, m, or h. The default is "" (no timeout).                                                                                 | string                             | ""                |
| **Query** | **timeout** _optional_                   | Maximum time to spend on the request before timing out. The format includes an amount and a unit: ns, us, ms, s, m, or h. The default is "" (no timeout).                                                                                                           | string                             | ""                |
| **Query** | **args** _optional_                      | An array of positional parameter values.                                                                                                                                                                                                                            | < string (URL-encoded) > array     |                   |
| **Query** | **$_identifier_** _optional_             | A named parameter value.                                                                                                                                                                                                                                            | string                             |                   |
| **Query** | **plan-format** _optional_               | The plan format.                                                                                                                                                                                                                                                    | enum (JSON, STRING)                | "JSON"            |
| **Query** | **logical-plan** _optional_              | If true, the logical plan is included in the query response.                                                                                                                                                                                                        | boolean                            | "false"           |
| **Query** | **optimized-logical-plan** _optional_    | If true, the optimized logical plan is included in the query response.                                                                                                                                                                                              | boolean                            | "true"            |
| **Query** | **expression-tree** _optional_           | If true, the expression tree is included in the query response.                                                                                                                                                                                                     | boolean                            | "false"           |
| **Query** | **rewritten-expression-tree** _optional_ | If true, the rewritten expression tree is included in the query response.                                                                                                                                                                                           | boolean                            | "false"           |
| **Query** | **job** _optional_                       | If true, the job details are included in the query response.                                                                                                                                                                                                        | boolean                            | "false"           |
| **Query** | **max-warnings** _optional_              | An integer specifying the maximum number of warning messages to be included in the query response.                                                                                                                                                                  | integer (int32)                    | 0                 |

#### [](#responses-2)Responses

| HTTP Code | Description                                               | Schema                                   |
| --------- | --------------------------------------------------------- | ---------------------------------------- |
| **200**   | The operation was successful.                             | [Query Responses](#%5Fquery%5Fresponses) |
| **400**   | Bad request. A parameter has an incorrect value.          | [Query Responses](#%5Fquery%5Fresponses) |
| **401**   | Unauthorized. The user name or password may be incorrect. | [Query Responses](#%5Fquery%5Fresponses) |

#### [](#security-2)Security

| Type      | Name                                                                                   |
| --------- | -------------------------------------------------------------------------------------- |
| **basic** | **[Analytics Manage / Analytics Select](#%5Fanalytics%5Fmanage%5Fanalytics%5Fselect)** |

#### [](#example-http-request-2)Example HTTP request

The example below uses a URL-encoded query parameter. The SQL++ statement is `SELECT "hello, beer!" AS greeting`.

Curl request

```sh
curl -v -u Administrator:password \
http://localhost:8095/analytics/service?statement=SELECT%20%22hello%2C%20beer%21%22%20AS%20greeting
```

#### [](#example-http-response-2)Example HTTP response

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

### [](#%5Fpost%5Fquery)Query Service (Alternative)

POST /query/service

#### [](#description-3)Description

An alternative endpoint for the [Query Service](#%5Fpost%5Fservice), provided for tools compatibility.

### [](#%5Fget%5Fquery)Read-Only Query Service (Alternative)

GET /query/service

#### [](#description-4)Description

An alternative endpoint for the [Read-Only Query Service](#%5Fget%5Fservice), provided for tools compatibility.

## [](#%5Fdefinitions)Definitions

This section describes the properties consumed and returned by this REST API.

* [Query Parameters](#%5Fquery%5Fparameters)
* [Query Responses](#%5Fquery%5Fresponses)

### [](#%5Fquery%5Fparameters)Query Parameters

_Polymorphism_ : Composition

| Name                                     | Description                                                                                                                                                                                                                                                                                      | Schema                             |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------- |
| **statement** _required_                 | Specifies at least one valid SQL++ for Analytics statement to run.                                                                                                                                                                                                                               | string                             |
| **client\_context\_id** _optional_       | An identifier passed by the client that is returned verbatim in the query response. Useful for matching a particular query to a specific caller.                                                                                                                                                 | string                             |
| **format** _optional_                    | Desired format for the query results. Note that the only possible format is JSON. **Default** : "JSON"                                                                                                                                                                                           | enum (JSON)                        |
| **pretty** _optional_                    | If true, the result is indented. **Default** : false                                                                                                                                                                                                                                             | boolean                            |
| **query\_context** _optional_            | A scope for the statement. The value of this parameter must start with default:, followed by an Analytics scope name. The default: prefix is a dummy and is ignored when resolving an Analytics collection name or synonym name. **Default** : "default:Default"                                 | string                             |
| **readonly** _optional_                  | If true, then DDL statements are not allowed. **Default** : false                                                                                                                                                                                                                                | boolean                            |
| **scan\_consistency** _optional_         | The consistency guarantee constraint for index scanning. If not\_bounded, the query is executed immediately. If request\_plus, the required datasets are updated with data available from the Data service at the time of the request before the query is executed. **Default** : "not\_bounded" | enum (not\_bounded, request\_plus) |
| **scan\_wait** _optional_                | The maximum time to wait for datasets to be updated before the query is executed. The format includes an amount and a unit: ns, us, ms, s, m, or h. The default is "" (no timeout). **Default** : ""                                                                                             | string                             |
| **timeout** _optional_                   | Maximum time to spend on the request before timing out. The format includes an amount and a unit: ns, us, ms, s, m, or h. The default is "" (no timeout). **Default** : ""                                                                                                                       | string                             |
| **args** _optional_                      | An array of positional parameter values.                                                                                                                                                                                                                                                         | < object > array                   |
| **$_identifier_** _optional_             | A named parameter value.                                                                                                                                                                                                                                                                         | string                             |
| **plan-format** _optional_               | The plan format. **Default** : "JSON"                                                                                                                                                                                                                                                            | enum (JSON, STRING)                |
| **logical-plan** _optional_              | If true, the logical plan is included in the query response. **Default** : false                                                                                                                                                                                                                 | boolean                            |
| **optimized-logical-plan** _optional_    | If true, the optimized logical plan is included in the query response. **Default** : true                                                                                                                                                                                                        | boolean                            |
| **expression-tree** _optional_           | If true, the expression tree is included in the query response. **Default** : false                                                                                                                                                                                                              | boolean                            |
| **rewritten-expression-tree** _optional_ | If true, the rewritten expression tree is included in the query response. **Default** : false                                                                                                                                                                                                    | boolean                            |
| **job** _optional_                       | If true, the job details are included in the query response. **Default** : false                                                                                                                                                                                                                 | boolean                            |
| **max-warnings** _optional_              | An integer specifying the maximum number of warning messages to be included in the query response. **Default** : 0                                                                                                                                                                               | integer (int32)                    |

### [](#%5Fquery%5Fresponses)Query Responses

_Polymorphism_ : Composition

| Name                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                | Schema                                          |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------- |
| **requestID** _optional_       | A unique identifier for the response.                                                                                                                                                                                                                                                                                                                                                                                                      | string (UUID)                                   |
| **clientContextID** _optional_ | The client context ID of the request, if one was supplied — refer to client\_context\_id in [Query Parameters](#%5Fquery%5Fparameters).                                                                                                                                                                                                                                                                                                    | string                                          |
| **signature** _optional_       | The schema of the results. Present only when the query completes successfully.                                                                                                                                                                                                                                                                                                                                                             | object                                          |
| **results** _optional_         | An array of all the objects returned by the query. An object can be any JSON value.                                                                                                                                                                                                                                                                                                                                                        | < object > array                                |
| **status** _optional_          | The status of the request.                                                                                                                                                                                                                                                                                                                                                                                                                 | enum (success, running, failed, timeout, fatal) |
| **errors** _optional_          | An array of error objects. Present only if 1 or more errors are returned during processing of the request. Each error is represented by an object in this list.                                                                                                                                                                                                                                                                            | < [Errors](#%5Ferrors) \> array                 |
| **warnings** _optional_        | An array of warning objects. Present only if 1 or more warnings are returned during processing of the request. Each warning is represented by an object in this list. Note that you can specify the maximum number of warning messages to be returned in the query response — refer to max-warnings in [Query Parameters](#%5Fquery%5Fparameters). By default, no warnings are returned, even if warnings have occurred during processing. | < [Warnings](#%5Fwarnings) \> array             |
| **plans** _optional_           | An object containing the query plans, if requested.                                                                                                                                                                                                                                                                                                                                                                                        | [Plans](#%5Fplans)                              |
| **metrics** _optional_         | An object containing metrics about the request.                                                                                                                                                                                                                                                                                                                                                                                            | [Metrics](#%5Fmetrics)                          |

### [](#%5Ferrors)Errors

| Name                | Description                                                                         | Schema  |
| ------------------- | ----------------------------------------------------------------------------------- | ------- |
| **code** _optional_ | A number that identifies the error.                                                 | integer |
| **msg** _optional_  | A message describing the error in detail. Refer to [Error Codes](error-codes.html). | string  |

### [](#%5Fwarnings)Warnings

| Name                | Description                                 | Schema  |
| ------------------- | ------------------------------------------- | ------- |
| **code** _optional_ | A number that identifies the warning.       | integer |
| **msg** _optional_  | A message describing the warning in detail. | string  |

### [](#%5Fplans)Plans

| Name                                   | Description                    | Schema |
| -------------------------------------- | ------------------------------ | ------ |
| **logicalPlan** _optional_             | The logical plan.              | object |
| **optimizedLogicalPlan** _optional_    | The optimized logical plan.    | object |
| **rewrittenExpressionTree** _optional_ | The rewritten expression tree. | string |
| **expressionTree** _optional_          | The expression tree.           | string |
| **job** _optional_                     | The job details.               | object |

|  | The structure and content of query plans is expected to change as development of the query processor progresses. |
|  | ---------------------------------------------------------------------------------------------------------------- |

### [](#%5Fmetrics)Metrics

_Polymorphism_ : Composition

| Name                            | Description                                                                                                                          | Schema             |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------ |
| **elapsedTime** _optional_      | The total time taken for the request, that is the time from when the request was received until the results were returned.           | string             |
| **executionTime** _optional_    | The time taken for the execution of the request, that is the time from when query execution started until the results were returned. | string             |
| **resultCount** _optional_      | The total number of objects in the results.                                                                                          | integer (unsigned) |
| **resultSize** _optional_       | The total number of bytes in the results.                                                                                            | integer (unsigned) |
| **errorCount** _optional_       | The number of errors that occurred during the request.                                                                               | integer (unsigned) |
| **warningCount** _optional_     | The number of warnings that occurred during the request.                                                                             | integer (unsigned) |
| **processedObjects** _optional_ | Number of processed tuples during query execution.                                                                                   | integer (int64)    |

## [](#%5Fsecurityscheme)Security

### [](#%5Fanalytics%5Fmanage%5Fanalytics%5Fselect)Analytics Manage / Analytics Select

The Analytics Service REST API supports HTTP basic authentication. Credentials can be passed via HTTP headers.

Users must have one of the following RBAC roles:

* Full Admin
* Cluster Admin
* Analytics Manager
* Analytics Reader
* Analytics Select
* Analytics Admin

Refer to [Roles](../learn/security/roles.html) for more details.

_Type_ : basic