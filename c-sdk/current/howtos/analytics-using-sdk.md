[View original HTML](/c-sdk/current/howtos/analytics-using-sdk.html)

> Parallel data management for complex queries over many records, using a familiar SQL++ syntax. 

This page covers using our operational C SDK to connect to the Analytics Service of a Capella Operational or self-managed Couchbase Server cluster. As well as this row-based analytics service, a speedy, column-based analytics database is available for real-time analytics.

|  | Analytics SDKs SDKs for [Enterprise Analytics](../../../enterprise-analytics/current/intro/intro.md) — Couchbase’s analytical database for real time apps and operational intelligence (RT-OLAP) — are available for the .NET, Go, Java, Node.js, and Python platforms. See the [Enterprise Analytics SDK pages](#home::analytics-sdk.adoc) for more information. Currently, different SDKs are needed to connect to [Capella Analytics](../../../analytics/intro/intro.md) — as this service does not have Enterprise Analytics' load balancer, and uses a different connection protocol. Capella Analytics SDKs (also known as Columnar SDKs) are available for the Go, Java, Node.js, and Python platforms. See the [Capella Analytics SDK pages](#home::columnar-sdk.adoc) for more information. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

For complex and long-running queries, involving large ad hoc join, set, aggregation, and grouping operations, Couchbase Data Platform offers the [Couchbase Analytics Service (CBAS)](../../../server/current/analytics/introduction.md). This is the analytic counterpart to our [operational data focussed Query Service](n1ql-queries-with-sdk.md).

The analytics service is available in [Capella operational](../../../cloud/clusters/analytics-service/analytics-service.md)or the Enterprise Edition of self-managed Couchbase Server.

## [](#getting-started)Getting Started

After familiarizing yourself with our [introductory primer](../../../server/current/analytics/primer-beer.md), in particular creating a dataset and linking it to a bucket to shadow the operational data, try Couchbase Analytics using the Go SDK. Intentionally, the API for analytics is very similar to that of the query service. In these examples we will be using an `airports` dataset created on the `travel-sample` bucket.

In C SDK 2.x, Analytics was only available on the `Bucket` object; in C SDK 3.x, Analytics queries are submitted using the Cluster reference, not a Bucket or Collection:

|  | When using a Couchbase version < 6.5 you must create a valid Bucket connection using cluster.Bucket(name) before you can use Analytics. |
|  | --------------------------------------------------------------------------------------------------------------------------------------- |

Here is an example of doing an analytics query :

```c
const char *stmt = "SELECT * FROM breweries LIMIT 2";
lcb_CMDANALYTICS *cmd;
int idx = 0;
lcb_cmdanalytics_create(&cmd);
lcb_cmdanalytics_callback(cmd, row_callback);
lcb_cmdanalytics_statement(cmd, stmt, strlen(stmt));
lcb_cmdanalytics_deferred(cmd, 1);
check(lcb_analytics(instance, &idx, cmd), "schedule analytics query");
std::cout << "----> " << stmt << "\n";
lcb_cmdanalytics_destroy(cmd);
lcb_wait(instance, LCB_WAIT_DEFAULT);
```

For a full example, see the [API documentation](https://docs.couchbase.com/sdk-api/couchbase-c-client-3.3.18/example%5F2analytics%5F2analytics%5F8c-example.html).

## [](#analytics-result)Analytics Result

When performing an analytics query, `lcb_RESPANALYTICS` is delivered in the `lcb_ANALYTICS_CALLBACK` function for each result row received.

```c
int *idx;
const char *row;
size_t nrow;
lcb_STATUS rc = lcb_respanalytics_status(resp);

lcb_respanalytics_cookie(resp, reinterpret_cast<void **>(&idx));
lcb_respanalytics_row(resp, &row, &nrow);
if (rc != LCB_SUCCESS) {
    const lcb_RESPHTTP *http;
    std::cout << lcb_strerror_short(rc);
    lcb_respanalytics_http_response(resp, &http);
```

## [](#analytics-options)Analytics Options

The analytics service provides an array of options to customize your query. The following table lists them :

__Table 1\. Available Analytics options__
| Name                                                                                               | Description                                                                    |
| -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| lcb\_cmdanalytics\_reset(command)                                                                  | Reset the structure so that it may be reused for a subsequent analytics query. |
| lcb\_cmdanalytics\_encoded\_payload(command,query,query length)                                    | Get the JSON-encoded analytics query payload.                                  |
| lcb\_cmdanalytics\_payload(command, query, query length)                                           | Sets the JSON-encodes analytics query payload to be executed.                  |
| lcb\_cmdanalytics\_statement(command, statement, statement length )                                | Sets the actual statement to be executed.                                      |
| lcb\_cmdanalytics\_scope\_name(command, scope name, scope length)                                  | Associate scope name with the analytics query.                                 |
| lcb\_cmdanalytics\_named\_param(command, argument name, name length, argument value, value length) | Sets a named argument for the analytics query.                                 |
| lcb\_cmdanalytics\_positional\_param(command, argument value, argument length)                     | Adds a positional argument for the analytics query.                            |
| lcb\_cmdanalytics\_readonly(command, readonly)                                                     | Marks analytics query as read-only ( set readonly value to non zero ).         |

## [](#additional-resources)Additional Resources

To learn more about using SQL++ for Analytics — see our [Tutorial Introduction to SQL++ for SQL users](https://sqlplusplus-tutorial.couchbase.com/tutorial/#1).