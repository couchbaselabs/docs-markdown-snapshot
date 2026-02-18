---
title: Analytics Query Responses
description: A description of query responses for Couchbase Analytics.
editUrl: https://github.com/couchbase/docs-analytics/edit/release/8.0/modules/analytics/pages/query-responses.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/current/analytics/query-responses.html)

# Analytics Query Responses

When you use [Analytics Workbench](run-query.md#Using%5Fanalytics%5Fworkbench), the Analytics Service returns a JSON array containing just the query results, separate from the query metrics or the query plan.

When you use the [Service API](../analytics-rest-service/index.md#post%5Fservice) or the [cbq Shell](../n1ql/n1ql-intro/cbq.md), the Analytics Service returns a JSON object, which includes the query results, query metrics, any warnings or errors, and the query plan. These are described on this page.

## [](#common-responses)Common Responses

The Analytics Service returns the following responses in common with the Query Service.

For more information on these common responses, refer to the [Response Body](../n1ql-rest-query/index.md#Response)section on the SQL++ for Query REST API page.

| Property                    |                                                                                                                                                                                                                                                                                                                                                                                                                                       | Schema                                       |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| **requestID**optional       | A unique identifier for the response.                                                                                                                                                                                                                                                                                                                                                                                                 | UUID (UUID)                                  |
| **clientContextID**optional | The client context ID of the request, if one was supplied — refer to client\_context\_id in [Query Parameters](query-params.html).                                                                                                                                                                                                                                                                                                    | String                                       |
| **signature**optional       | The schema of the results. Present only when the query completes successfully.                                                                                                                                                                                                                                                                                                                                                        | Object                                       |
| **results**optional         | An array of all the objects returned by the query. An object can be any JSON value.                                                                                                                                                                                                                                                                                                                                                   | Any Type array                               |
| **status**optional          | The status of the request. **Values:** "success", "running", "failed", "timeout", "fatal"                                                                                                                                                                                                                                                                                                                                             | String                                       |
| **errors**optional          | An array of error objects. Present only if 1 or more errors are returned during processing of the request. Each error is represented by an object in this list.                                                                                                                                                                                                                                                                       | [Errors](#ResponsesCommonErrors) array       |
| **warnings**optional        | An array of warning objects. Present only if 1 or more warnings are returned during processing of the request. Each warning is represented by an object in this list. Note that you can specify the maximum number of warning messages to be returned in the query response — refer to max-warnings in [Query Parameters](query-params.html). By default, no warnings are returned, even if warnings have occurred during processing. | [Warnings](#ResponsesCommonWarnings) array   |
| **metrics**optional         | An object containing metrics about the request.                                                                                                                                                                                                                                                                                                                                                                                       | [Common Metrics](#ResponsesCommonYardsticks) |

### [](#ResponsesCommonErrors)Errors

| Property         |                                                                                                           | Schema  |
| ---------------- | --------------------------------------------------------------------------------------------------------- | ------- |
| **code**optional | A number that identifies the error.                                                                       | Integer |
| **msg**optional  | A message describing the error in detail. Refer to [Error Codes](/server/8.0/analytics/error-codes.html). | String  |

### [](#ResponsesCommonWarnings)Warnings

| Property         |                                             | Schema  |
| ---------------- | ------------------------------------------- | ------- |
| **code**optional | A number that identifies the warning.       | Integer |
| **msg**optional  | A message describing the warning in detail. | String  |

### [](#ResponsesCommonYardsticks)Common Metrics

| Property                  |                                                                                                                                      | Schema             |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------ |
| **elapsedTime**optional   | The total time taken for the request, that is the time from when the request was received until the results were returned.           | String             |
| **executionTime**optional | The time taken for the execution of the request, that is the time from when query execution started until the results were returned. | String             |
| **resultCount**optional   | The total number of objects in the results.                                                                                          | Integer (unsigned) |
| **resultSize**optional    | The total number of bytes in the results.                                                                                            | Integer (unsigned) |
| **errorCount**optional    | The number of errors that occurred during the request.                                                                               | Integer (unsigned) |
| **warningCount**optional  | The number of warnings that occurred during the request.                                                                             | Integer (unsigned) |

## [](#analytics-responses)Analytics Responses

In addition, the Analytics Service returns the following responses which are unique to Analytics.

| Property            |                                                     | Schema                                         |
| ------------------- | --------------------------------------------------- | ---------------------------------------------- |
| **plans**optional   | An object containing the query plans, if requested. | [Plans](#ResponsesLocalPlans)                  |
| **metrics**optional | An object containing metrics about the request.     | [Analytics Metrics](#ResponsesLocalYardsticks) |

### [](#ResponsesLocalPlans)Plans

| Property                            |                                | Schema |
| ----------------------------------- | ------------------------------ | ------ |
| **logicalPlan**optional             | The logical plan.              | Object |
| **optimizedLogicalPlan**optional    | The optimized logical plan.    | Object |
| **rewrittenExpressionTree**optional | The rewritten expression tree. | String |
| **expressionTree**optional          | The expression tree.           | String |
| **job**optional                     | The job details.               | Object |

> [!NOTE]
> The structure and content of query plans is expected to change as development of the query processor progresses.

### [](#ResponsesLocalYardsticks)Analytics Metrics

| Property                     |                                                    | Schema       |
| ---------------------------- | -------------------------------------------------- | ------------ |
| **processedObjects**optional | Number of processed tuples during query execution. | Long (int64) |