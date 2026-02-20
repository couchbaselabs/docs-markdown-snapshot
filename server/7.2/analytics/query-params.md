---
title: Analytics Query Parameters
description: A description of query parameters for Couchbase Analytics.
editUrl: https://github.com/couchbase/docs-analytics/edit/release/7.2/modules/analytics/pages/query-params.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:analytics:query-params.adoc[]
---

[View original HTML](/server/7.2/analytics/query-params.html)

# Analytics Query Parameters

## [](#common-parameters)Common Parameters

The Couchbase Analytics [Service API](rest-service.md#%5Fpost%5Fservice)supports the following parameters in common with the SQL++ for Query REST API.

For more information on these common parameters, refer to [Request-Level Parameters](../settings/query-settings.md#section%5Fnnj%5Fsjk%5Fk1b).

### [](#%5Fcommon%5Fparameters)Common Parameters

| Name                               | Description                                                                                                                                                                                                                                                                                      | Schema                             |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------- |
| **statement** _required_           | Specifies at least one valid SQL++ for Analytics statement to run.                                                                                                                                                                                                                               | string                             |
| **client\_context\_id** _optional_ | An identifier passed by the client that is returned verbatim in the query response. Useful for matching a particular query to a specific caller.                                                                                                                                                 | string                             |
| **format** _optional_              | Desired format for the query results. Note that the only possible format is JSON. **Default** : "JSON"                                                                                                                                                                                           | enum (JSON)                        |
| **pretty** _optional_              | If true, the result is indented. **Default** : false                                                                                                                                                                                                                                             | boolean                            |
| **query\_context** _optional_      | A scope for the statement. The value of this parameter must start with default:, followed by an Analytics scope name. The default: prefix is a dummy and is ignored when resolving an Analytics collection name or synonym name. **Default** : "default:Default"                                 | string                             |
| **readonly** _optional_            | If true, then DDL statements are not allowed. **Default** : false                                                                                                                                                                                                                                | boolean                            |
| **scan\_consistency** _optional_   | The consistency guarantee constraint for index scanning. If not\_bounded, the query is executed immediately. If request\_plus, the required datasets are updated with data available from the Data service at the time of the request before the query is executed. **Default** : "not\_bounded" | enum (not\_bounded, request\_plus) |
| **scan\_wait** _optional_          | The maximum time to wait for datasets to be updated before the query is executed. The format includes an amount and a unit: ns, us, ms, s, m, or h. The default is "" (no timeout). **Default** : ""                                                                                             | string                             |
| **timeout** _optional_             | Maximum time to spend on the request before timing out. The format includes an amount and a unit: ns, us, ms, s, m, or h. The default is "" (no timeout). **Default** : ""                                                                                                                       | string                             |
| **args** _optional_                | An array of positional parameter values.                                                                                                                                                                                                                                                         | < object > array                   |
| **$_identifier_** _optional_       | A named parameter value.                                                                                                                                                                                                                                                                         | string                             |

> [!IMPORTANT]
> The Analytics Service API does not support the `prepared` parameter.

> [!NOTE]
> The Analytics Service API does not support the `at_plus` or `statement_plus` settings for scan consistency.

## [](#analytics-parameters)Analytics Parameters

In addition, the Service API supports the following parameters which are unique to Analytics.

### [](#%5Fanalytics%5Fparameters)Analytics Parameters

| Name                                     | Description                                                                                                        | Schema              |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ------------------- |
| **plan-format** _optional_               | The plan format. **Default** : "JSON"                                                                              | enum (JSON, STRING) |
| **logical-plan** _optional_              | If true, the logical plan is included in the query response. **Default** : false                                   | boolean             |
| **optimized-logical-plan** _optional_    | If true, the optimized logical plan is included in the query response. **Default** : true                          | boolean             |
| **expression-tree** _optional_           | If true, the expression tree is included in the query response. **Default** : false                                | boolean             |
| **rewritten-expression-tree** _optional_ | If true, the rewritten expression tree is included in the query response. **Default** : false                      | boolean             |
| **job** _optional_                       | If true, the job details are included in the query response. **Default** : false                                   | boolean             |
| **max-warnings** _optional_              | An integer specifying the maximum number of warning messages to be included in the query response. **Default** : 0 | integer (int32)     |