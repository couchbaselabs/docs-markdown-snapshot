---
title: Analytics Query Parameters
description: A description of query parameters for Couchbase Analytics.
editUrl: https://github.com/couchbase/docs-analytics/edit/release/8.0/modules/analytics/pages/query-params.adoc
pubDate: 2026-06-12T16:31:57.907Z
link: xref:server:analytics:query-params.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/analytics/query-params.html)

# Analytics Query Parameters

To specify request-level parameters for the Analytics Service, do one of the following:

* In the [Analytics Workbench](run-query.md#Using%5Fanalytics%5Fworkbench), click the cog icon  to display the Run-Time Preferences window.
* Use the `\SET` command in the [cbq Shell](../n1ql/n1ql-intro/cbq.md#cbq-parameter-manipulation).
* Use the [Service API](../analytics-rest-service/index.md#post%5Fservice).

## [](#common-parameters)Common Parameters

The Analytics Service supports the following parameters in common with the Query Service.

For more information on these common parameters, refer to [Request-Level Parameters](../n1ql/n1ql-manage/query-settings.md#section%5Fnnj%5Fsjk%5Fk1b).

| Property                            |                                                                                                                                                                                                                                                                                                                                             | Schema         |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| **statement**required               | Specifies at least one valid SQL++ for Analytics statement to run.                                                                                                                                                                                                                                                                          | String         |
| **client\_context\_id**optional     | An identifier passed by the client that's returned verbatim in the query response. Useful for matching a particular query to a specific caller.                                                                                                                                                                                             | String         |
| **format**optional                  | Desired format for the query results. The only possible format is JSON. **Values:** "JSON" **Default:** "JSON"                                                                                                                                                                                                                              | String         |
| **pretty**optional                  | If true, the result is indented. **Default:** false                                                                                                                                                                                                                                                                                         | Boolean        |
| **query\_context**optional          | A scope for the statement. The value of this parameter must start with default:, followed by an Analytics scope name. The default: prefix is a dummy and is ignored when resolving an Analytics collection name or synonym name. **Default:** "default:Default"                                                                             | String         |
| **readonly**optional                | If true, then DDL statements are not allowed. **Default:** false                                                                                                                                                                                                                                                                            | Boolean        |
| **scan\_consistency**optional       | The consistency guarantee constraint for index scanning. If not\_bounded, the query is executed immediately. If request\_plus, the required datasets are updated with data available from the Data service at the time of the request before the query is executed. **Values:** "not\_bounded", "request\_plus" **Default:** "not\_bounded" | String         |
| **scan\_wait**optional              | The maximum time to wait for datasets to be updated before the query is executed. The format includes an amount and a unit: ns, us, ms, s, m, or h. The default is "" (no timeout). **Default:** ""                                                                                                                                         | String         |
| **timeout**optional                 | Maximum time to spend on the request before timing out. The format includes an amount and a unit: ns, us, ms, s, m, or h. The default is "" (no timeout). **Default:** ""                                                                                                                                                                   | String         |
| **args**optional                    | An array of positional parameter values.                                                                                                                                                                                                                                                                                                    | Any Type array |
| **<$identifier>**additionalproperty | A named parameter value. **Nullable:** yes                                                                                                                                                                                                                                                                                                  | Any Type       |

> [!IMPORTANT]
> The Analytics Service API does not support the `prepared` parameter.

> [!NOTE]
> The Analytics Service API does not support the `at_plus` or `statement_plus` settings for scan consistency.

## [](#analytics-parameters)Analytics Parameters

In addition, the Service API supports the following parameters which are unique to Analytics.

| Property                              |                                                                                                                   | Schema          |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | --------------- |
| **plan-format**optional               | The plan format. **Values:** "JSON", "STRING" **Default:** "JSON"                                                 | String          |
| **logical-plan**optional              | If true, the logical plan is included in the query response. **Default:** false                                   | Boolean         |
| **optimized-logical-plan**optional    | If true, the optimized logical plan is included in the query response. **Default:** true                          | Boolean         |
| **expression-tree**optional           | If true, the expression tree is included in the query response. **Default:** false                                | Boolean         |
| **rewritten-expression-tree**optional | If true, the rewritten expression tree is included in the query response. **Default:** false                      | Boolean         |
| **job**optional                       | If true, the job details are included in the query response. **Default:** false                                   | Boolean         |
| **max-warnings**optional              | An integer specifying the maximum number of warning messages to be included in the query response. **Default:** 0 | Integer (int32) |