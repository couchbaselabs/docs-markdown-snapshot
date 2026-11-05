---
title: Logging
description: REST API endpoints are provided for retrieving log and diagnostic
  information, for collecting logs for upload and review, and for logging
  client-side errors.
pubDate: 2026-11-05T15:16:13.118Z
meta:
  component:
    title: Couchbase Server
    version: "7.6"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/rest-api/pages/logs-rest-api.adoc
  xref: xref:7.6@server:rest-api:logs-rest-api.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/rest-api/logs-rest-api.html)

# Logging

> [!IMPORTANT]
> Couchbase Server Enterprise Edition 7.6 reaches End of Life on March 31, 2027\. Please upgrade to 8.0.x by following [Upgrade](https://docs.couchbase.com/server/current/install/upgrade.html), or contact [Couchbase Support](https://support.couchbase.com/hc/en-us).

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