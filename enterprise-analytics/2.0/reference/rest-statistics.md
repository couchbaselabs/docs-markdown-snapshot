[View original HTML](/enterprise-analytics/2.0/reference/rest-statistics.html)

> The REST API allows cluster statistics to be retrieved; either individually, or in bulk. 

## [](#apis-in-this-section)APIs in this Section

Metrics are provided for all Couchbase Services, and also for the Cluster Manager. All metrics can be queried by means of the REST API.

For a complete list of available metrics that can be queried, see the [Metrics Reference](../metrics-reference/metrics-reference.md).

The APIs described in this section are listed below.

| HTTP Method | URI                                                               | Documented at                                              |
| ----------- | ----------------------------------------------------------------- | ---------------------------------------------------------- |
| GET         | /pools/default/stats/range/<metric\_name>/\[function-expression\] | [Getting a Single Statistic](rest-statistics-single.md)    |
| POST        | /pools/default/stats/range                                        | [Getting Multiple Statistics](rest-statistics-multiple.md) |