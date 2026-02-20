---
title: Enterprise Analytics REST API
description: A description of the Enterprise Analytics REST API.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/reference/pages/rest-analytics.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:2.0@enterprise-analytics:reference:rest-analytics.adoc[]
---

[View original HTML](/enterprise-analytics/2.0/reference/rest-analytics.html)

# Enterprise Analytics REST API

Enterprise Analytics provides REST APIs that a client application can use to invoke services using simple HTTP methods. A catalog of available REST resources and requests is provided below.

The Enterprise Analytics REST APIs can be called on any node running Couchbase Enterprise Analytics. By default, the Enterprise Analytics REST endpoints below listen on port 8095, or 18095 for secure access. Note that the Settings API listens on port 8091, or 18091 for secure access.

For the examples, we assume that:

* You’re running a Couchbase Enterprise Analytics node using the default port on localhost.
* You authenticate as a user with the "Full Administrator" role with the user name "Administrator" and the password "password".

## [](#apis-in-this-section)APIs in this Section

For a list of the methods and URIs covered in these pages, see the tables below.

### [](#enterprise-analytics-service-api)Enterprise Analytics Service API

| HTTP Method | URI             | Documented at                                                                           |
| ----------- | --------------- | --------------------------------------------------------------------------------------- |
| POST        | /api/v1/request | [Request Service](../analytics-rest-service/index.md#operation/post%5Fservice)          |
| GET         | /api/v1/request | [Read-Only Request Service](../analytics-rest-service/index.md#operation/get%5Fservice) |

### [](#enterprise-analytics-admin-api)Enterprise Analytics Admin API

| HTTP Method | URI                         | Documented at                                                                            |
| ----------- | --------------------------- | ---------------------------------------------------------------------------------------- |
| GET         | /api/v1/active\_requests    | [Active Requests](../analytics-rest-admin/index.md#operation/return%5Factive%5Frequests) |
| DELETE      | /api/v1/active\_requests    | [Request Cancellation](../analytics-rest-admin/index.md#operation/cancel%5Frequest)      |
| GET         | /api/v1/completed\_requests | [Completed Requests](../analytics-rest-admin/index.md#operation/completed%5Frequests)    |
| GET         | /api/v1/status/service      | [Service Status](../analytics-rest-admin/index.md#operation/service%5Fstatus)            |
| POST        | /api/v1/service/restart     | [Service Restart](../analytics-rest-admin/index.md#operation/restart%5Fservice)          |
| POST        | /api/v1/node/restart        | [Node Restart](../analytics-rest-admin/index.md#operation/restart%5Fnode)                |
| GET         | /api/v1/status/ingestion    | [Ingestion Status](../analytics-rest-admin/index.md#operation/ingestion%5Fstatus)        |

### [](#enterprise-analytics-config-api)Enterprise Analytics Config API

| HTTP Method | URI                    | Documented at                                                                                |
| ----------- | ---------------------- | -------------------------------------------------------------------------------------------- |
| GET         | /api/v1/config/service | [View Service-Level Parameters](../analytics-rest-config/index.md#operation/get%5Fservice)   |
| PUT         | /api/v1/config/service | [Modify Service-Level Parameters](../analytics-rest-config/index.md#operation/put%5Fservice) |
| GET         | /api/v1/config/node    | [View Node-Specific Parameters](../analytics-rest-config/index.md#operation/get%5Fnode)      |
| PUT         | /api/v1/config/node    | [Modify Node-Specific Parameters](../analytics-rest-config/index.md#operation/put%5Fnode)    |

### [](#enterprise-analytics-settings-api)Enterprise Analytics Settings API

| HTTP Method | URI                 | Documented at                                                                                         |
| ----------- | ------------------- | ----------------------------------------------------------------------------------------------------- |
| GET         | /settings/analytics | [View Enterprise Analytics Settings](../analytics-rest-settings/index.md#operation/get%5Fsettings)    |
| POST        | /settings/analytics | [Modify Enterprise Analytics Settings](../analytics-rest-settings/index.md#operation/post%5Fsettings) |

### [](#enterprise-analytics-links-api)Enterprise Analytics Links API

| HTTP Method | URI                 | Documented at                                                                              |
| ----------- | ------------------- | ------------------------------------------------------------------------------------------ |
| POST        | /api/v1/link/{name} | [Create Link](../analytics-rest-links/index.md#tag/Single-Links/operation/post%5Flink)     |
| GET         | /api/v1/link/{name} | [Query Link](../analytics-rest-links/index.md#tag/Single-Links/operation/get%5Flink)       |
| PUT         | /api/v1/link/{name} | [Edit Link](../analytics-rest-links/index.md#tag/Single-Links/operation/put%5Flink)        |
| DELETE      | /api/v1/link/{name} | [Delete Link](../analytics-rest-links/index.md#tag/Single-Links/operation/delete%5Flink)   |
| GET         | /api/v1/link        | [Query All Links](../analytics-rest-links/index.md#tag/Multiple-Links/operation/get%5Fall) |