[View original HTML](/server/current/rest-api/rest-statistics.html)

> The REST API allows cluster statistics to be retrieved; either individually, or in bulk. 

## [](#apis-in-this-section)APIs in this Section

Metrics are provided for all Couchbase Services, the Cluster Manager, and XDCR. All metrics can be queried by means of the REST API.

Couchbase Server stores up to 365 days or 1GB of stats, whichever limit occurs first.

For a complete list of available metrics that can be queried, see the [Metrics Reference](../metrics-reference/metrics-reference.md).

The APIs described in this section are listed below.

| HTTP Method | URI                                                               | Documented at                                              |
| ----------- | ----------------------------------------------------------------- | ---------------------------------------------------------- |
| GET         | /prometheus\_sd\_config                                           | [Prometheus Discovery API](rest-discovery-api.md)          |
| GET         | /pools/default/stats/range/<metric\_name>/\[function-expression\] | [Getting a Single Statistic](rest-statistics-single.md)    |
| POST        | /pools/default/stats/range                                        | [Getting Multiple Statistics](rest-statistics-multiple.md) |