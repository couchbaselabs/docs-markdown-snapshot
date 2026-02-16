[View original HTML](/server/7.6/rest-api/logs-rest-api.html)

> REST API endpoints are provided for retrieving log and diagnostic information, for collecting logs for upload and review, and for logging client-side errors. 

## [](#apis-in-this-section)APIs in this Section

The Couchbase-Server _Logging_ facility records important events, and saves the details to log files, on disk. REST API endpoints are provided for retrieving log and diagnostic information, for logging client-side errors, and for collecting logs for upload and review.

The APIs are as follows.

| HTTP Method | URI                              | Documented at                                                 |
| ----------- | -------------------------------- | ------------------------------------------------------------- |
| POST        | /controller/startLogsCollection  | [Collecting Logs](rest-manage-log-collection.md)              |
| POST        | /controller/cancelLogsCollection | [Collecting Logs](rest-manage-log-collection.md)              |
| GET         | /pools/default/tasks             | [Getting Cluster Tasks](rest-get-cluster-tasks.md)            |
| GET         | /diag                            | [Retrieving Diagnostic and Log Information](rest-logs-get.md) |
| GET         | /sasl\_logs                      | [Retrieving Diagnostic and Log Information](rest-logs-get.md) |
| POST        | /logClientError                  | [Logging Client-Side Errors](rest-client-logs.md)             |