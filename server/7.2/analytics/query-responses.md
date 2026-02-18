---
title: Analytics Query Responses
description: A description of query responses for Couchbase Analytics.
editUrl: https://github.com/couchbase/docs-analytics/edit/release/7.2/modules/analytics/pages/query-responses.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/analytics/query-responses.html)

# Analytics Query Responses

## [](#common-responses)Common Responses

The Couchbase Analytics [Service API](rest-service.md#%5Fpost%5Fservice)returns the following responses in common with the SQL++ for Query REST API.

For more information on these common responses, refer to the [Response](../n1ql/n1ql-rest-api/index.md#response)section on the SQL++ for Query REST API page.

### [](#%5Fcommon%5Fresponses)Common Responses

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
| **metrics** _optional_         | An object containing metrics about the request.                                                                                                                                                                                                                                                                                                                                                                                            | [Common Metrics](#%5Fcommon%5Fmetrics)          |

For information about query parameters, see [Analytics Query Parameters](query-params.md).

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

### [](#%5Fcommon%5Fmetrics)Common Metrics

| Name                         | Description                                                                                                                          | Schema             |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------ |
| **elapsedTime** _optional_   | The total time taken for the request, that is the time from when the request was received until the results were returned.           | string             |
| **executionTime** _optional_ | The time taken for the execution of the request, that is the time from when query execution started until the results were returned. | string             |
| **resultCount** _optional_   | The total number of objects in the results.                                                                                          | integer (unsigned) |
| **resultSize** _optional_    | The total number of bytes in the results.                                                                                            | integer (unsigned) |
| **errorCount** _optional_    | The number of errors that occurred during the request.                                                                               | integer (unsigned) |
| **warningCount** _optional_  | The number of warnings that occurred during the request.                                                                             | integer (unsigned) |

## [](#analytics-responses)Analytics Responses

In addition, the Service API returns the following responses which are unique to Analytics.

### [](#%5Fanalytics%5Fresponses)Analytics Responses

_Polymorphism_ : Composition

| Name                   | Description                                         | Schema                                       |
| ---------------------- | --------------------------------------------------- | -------------------------------------------- |
| **plans** _optional_   | An object containing the query plans, if requested. | [Plans](#%5Fplans)                           |
| **metrics** _optional_ | An object containing metrics about the request.     | [Analytics Metrics](#%5Fanalytics%5Fmetrics) |

### [](#%5Fplans)Plans

| Name                                   | Description                    | Schema |
| -------------------------------------- | ------------------------------ | ------ |
| **logicalPlan** _optional_             | The logical plan.              | object |
| **optimizedLogicalPlan** _optional_    | The optimized logical plan.    | object |
| **rewrittenExpressionTree** _optional_ | The rewritten expression tree. | string |
| **expressionTree** _optional_          | The expression tree.           | string |
| **job** _optional_                     | The job details.               | object |

> [!NOTE]
> The structure and content of query plans is expected to change as development of the query processor progresses.

### [](#%5Fanalytics%5Fmetrics)Analytics Metrics

| Name                            | Description                                        | Schema          |
| ------------------------------- | -------------------------------------------------- | --------------- |
| **processedObjects** _optional_ | Number of processed tuples during query execution. | integer (int64) |