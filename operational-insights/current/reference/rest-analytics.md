---
title: Service APIs
description: "The Service APIs run requests and manage the Operational Insights
  service: querying, administration, configuration, links, Iceberg catalogs, and
  logging."
pubDate: 2026-10-19T14:21:08.937Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: reference
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/reference/pages/rest-analytics.adoc
  xref: xref:enterprise-analytics:reference:rest-analytics.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/reference/rest-analytics.html)

# Service APIs

The Service APIs let a client application run requests and manage the service using simple HTTP methods. A catalog of available REST resources and requests is provided below.

You can call the Service APIs on any node in the cluster. By default, they listen on port 8095, or 18095 for secure access.

For the APIs that manage the cluster itself, such as nodes, rebalance, security, and service settings, see [Cluster Management APIs](rest-cluster-management.md).

## [](#apis-in-this-section)APIs in this Section

For a list of the methods and URIs covered in these pages, see the tables below.

### [](#request-api)Request API

| HTTP Method | URI                                            | Documented at                                                                                    |
| ----------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| POST        | /api/v1/request                                | [Request Service](../analytics-rest-service/index.md#operation/post%5Fservice)                   |
| GET         | /api/v1/request                                | [Read-Only Request Service](../analytics-rest-service/index.md#operation/get%5Fservice)          |
| GET         | /api/v1/request/status/{request\_id}/{job\_id} | [Request Status](../analytics-rest-service/index.md#operation/get%5Frequest%5Fstatus)            |
| GET         | /api/v1/request/result/{request\_id}/{job\_id} | [Retrieve Request Result](../analytics-rest-service/index.md#operation/get%5Frequest%5Fresult)   |
| DELETE      | /api/v1/request/result/{request\_id}/{job\_id} | [Discard Request Result](../analytics-rest-service/index.md#operation/delete%5Frequest%5Fresult) |

### [](#administration-api)Administration API

| HTTP Method | URI                         | Documented at                                                                            |
| ----------- | --------------------------- | ---------------------------------------------------------------------------------------- |
| GET         | /api/v1/active\_requests    | [Active Requests](../analytics-rest-admin/index.md#operation/return%5Factive%5Frequests) |
| DELETE      | /api/v1/active\_requests    | [Request Cancellation](../analytics-rest-admin/index.md#operation/cancel%5Frequest)      |
| GET         | /api/v1/completed\_requests | [Completed Requests](../analytics-rest-admin/index.md#operation/completed%5Frequests)    |
| GET         | /api/v1/open\_requests      | [Open Requests](../analytics-rest-admin/index.md#operation/open%5Frequests)              |
| GET         | /api/v1/status/service      | [Service Status](../analytics-rest-admin/index.md#operation/service%5Fstatus)            |
| POST        | /api/v1/service/restart     | [Service Restart](../analytics-rest-admin/index.md#operation/restart%5Fservice)          |
| POST        | /api/v1/node/restart        | [Node Restart](../analytics-rest-admin/index.md#operation/restart%5Fnode)                |
| GET         | /api/v1/status/ingestion    | [Ingestion Status](../analytics-rest-admin/index.md#operation/ingestion%5Fstatus)        |
| GET         | /api/v1/health              | [Health Check](../analytics-rest-admin/index.md#operation/health%5Fcheck)                |

### [](#configuration-api)Configuration API

| HTTP Method | URI                    | Documented at                                                                                |
| ----------- | ---------------------- | -------------------------------------------------------------------------------------------- |
| GET         | /api/v1/config/service | [View Service-Level Parameters](../analytics-rest-config/index.md#operation/get%5Fservice)   |
| PUT         | /api/v1/config/service | [Modify Service-Level Parameters](../analytics-rest-config/index.md#operation/put%5Fservice) |
| GET         | /api/v1/config/node    | [View Node-Specific Parameters](../analytics-rest-config/index.md#operation/get%5Fnode)      |
| PUT         | /api/v1/config/node    | [Modify Node-Specific Parameters](../analytics-rest-config/index.md#operation/put%5Fnode)    |

### [](#links-api)Links API

| HTTP Method | URI                 | Documented at                                                                              |
| ----------- | ------------------- | ------------------------------------------------------------------------------------------ |
| POST        | /api/v1/link/{name} | [Create Link](../analytics-rest-links/index.md#tag/Single-Links/operation/post%5Flink)     |
| GET         | /api/v1/link/{name} | [Query Link](../analytics-rest-links/index.md#tag/Single-Links/operation/get%5Flink)       |
| PUT         | /api/v1/link/{name} | [Edit Link](../analytics-rest-links/index.md#tag/Single-Links/operation/put%5Flink)        |
| DELETE      | /api/v1/link/{name} | [Delete Link](../analytics-rest-links/index.md#tag/Single-Links/operation/delete%5Flink)   |
| GET         | /api/v1/link        | [Query All Links](../analytics-rest-links/index.md#tag/Multiple-Links/operation/get%5Fall) |

### [](#iceberg-api)Iceberg API

| HTTP Method | URI                                                                  | Documented at                                                                                           |
| ----------- | -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| GET         | /api/v1/iceberg/catalog                                              | [List Catalogs](../analytics-rest-iceberg/index.md#tag/Iceberg/operation/list%5Ficeberg%5Fcatalogs)     |
| GET         | /api/v1/iceberg/catalog/{catalogName}/namespace                      | [List Namespaces](../analytics-rest-iceberg/index.md#tag/Iceberg/operation/list%5Ficeberg%5Fnamespaces) |
| GET         | /api/v1/iceberg/catalog/{catalogName}/namespace/{namespace}/table    | [List Tables](../analytics-rest-iceberg/index.md#tag/Iceberg/operation/list%5Ficeberg%5Ftables)         |
| GET         | /api/v1/iceberg/snapshot/{databaseName}/{scopeName}/{collectionName} | [List Snapshots](../analytics-rest-iceberg/index.md#tag/Iceberg/operation/list%5Ficeberg%5Fsnapshots)   |

### [](#logging-api)Logging API

| HTTP Method | URI                              | Documented at                                                                              |
| ----------- | -------------------------------- | ------------------------------------------------------------------------------------------ |
| GET         | /api/v1/cluster/logging          | [View Configured Loggers](../analytics-rest-logging/index.md#operation/get%5Floggers)      |
| PUT         | /api/v1/cluster/logging          | [Modify Logger Levels](../analytics-rest-logging/index.md#operation/put%5Floggers)         |
| DELETE      | /api/v1/cluster/logging          | [Reset All Loggers](../analytics-rest-logging/index.md#operation/delete%5Floggers)         |
| GET         | /api/v1/cluster/logging/all      | [List Available Loggers](../analytics-rest-logging/index.md#operation/get%5Fall%5Floggers) |
| GET         | /api/v1/cluster/logging/{logger} | [View Logger Level](../analytics-rest-logging/index.md#operation/get%5Flogger)             |
| PUT         | /api/v1/cluster/logging/{logger} | [Modify Logger Level](../analytics-rest-logging/index.md#operation/put%5Flogger)           |
| DELETE      | /api/v1/cluster/logging/{logger} | [Reset Logger Level](../analytics-rest-logging/index.md#operation/delete%5Flogger)         |