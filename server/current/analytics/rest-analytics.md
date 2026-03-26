---
title: Analytics REST API
description: A description of the Analytics REST API.
editUrl: https://github.com/couchbase/docs-analytics/edit/release/8.0/modules/analytics/pages/rest-analytics.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:server:analytics:rest-analytics.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/analytics/rest-analytics.html)

# Analytics REST API

Analytics provides REST APIs that a client application can use to invoke services using simple HTTP methods. A catalog of available REST resources and requests is provided below.

The Analytics REST APIs can be called on any node running the analytics service. By default, the Analytics REST endpoints below listen on port 8095, or 18095 for secure access. Note that the Settings API listens on port 8091, or 18091 for secure access.

For the examples, we assume that:

* You're running a Couchbase node with the Analytics service using the default port on localhost.
* You authenticate as a user with the "Full Administrator" role with the user name "Administrator" and the password "password".

## [](#apis-in-this-section)APIs in this Section

For a list of the methods and URIs covered in these pages, see the tables below.

### [](#analytics-query-api)Analytics Query API

| HTTP Method | URI                | Documented at                                                                           |
| ----------- | ------------------ | --------------------------------------------------------------------------------------- |
| POST        | /analytics/service | [Query Service](../analytics-rest-service/index.md#post%5Fservice)                      |
| GET         | /analytics/service | [Read-Only Query Service](../analytics-rest-service/index.md#get%5Fservice)             |
| POST        | /query/service     | [Query Service (Alternative)](../analytics-rest-service/index.md#post%5Fquery)          |
| GET         | /query/service     | [Read-Only Query Service (Alternative)](../analytics-rest-service/index.md#get%5Fquery) |

### [](#analytics-admin-api)Analytics Admin API

| HTTP Method | URI                                  | Documented at                                                                  |
| ----------- | ------------------------------------ | ------------------------------------------------------------------------------ |
| GET         | /analytics/admin/active\_requests    | [Active Requests](../analytics-rest-admin/index.md#return%5Factive%5Frequests) |
| DELETE      | /analytics/admin/active\_requests    | [Request Cancellation](../analytics-rest-admin/index.md#cancel%5Frequest)      |
| GET         | /analytics/admin/completed\_requests | [Completed Requests](../analytics-rest-admin/index.md#completed%5Frequests)    |
| GET         | /analytics/cluster                   | [Cluster Status](../analytics-rest-admin/index.md#cluster%5Fstatus)            |
| POST        | /analytics/cluster/restart           | [Cluster Restart](../analytics-rest-admin/index.md#restart%5Fcluster)          |
| POST        | /analytics/node/restart              | [Node Restart](../analytics-rest-admin/index.md#restart%5Fnode)                |
| GET         | /analytics/status/ingestion          | [Ingestion Status](../analytics-rest-admin/index.md#ingestion%5Fstatus)        |

### [](#analytics-config-api)Analytics Config API

| HTTP Method | URI                       | Documented at                                                                      |
| ----------- | ------------------------- | ---------------------------------------------------------------------------------- |
| GET         | /analytics/config/service | [View Service-Level Parameters](../analytics-rest-config/index.md#get%5Fservice)   |
| PUT         | /analytics/config/service | [Modify Service-Level Parameters](../analytics-rest-config/index.md#put%5Fservice) |
| GET         | /analytics/config/node    | [View Node-Specific Parameters](../analytics-rest-config/index.md#get%5Fnode)      |
| PUT         | /analytics/config/node    | [Modify Node-Specific Parameters](../analytics-rest-config/index.md#put%5Fnode)    |

### [](#analytics-settings-api)Analytics Settings API

| HTTP Method | URI                 | Documented at                                                                    |
| ----------- | ------------------- | -------------------------------------------------------------------------------- |
| GET         | /settings/analytics | [View Analytics Settings](../analytics-rest-settings/index.md#get%5Fsettings)    |
| POST        | /settings/analytics | [Modify Analytics Settings](../analytics-rest-settings/index.md#post%5Fsettings) |

### [](#analytics-links-api)Analytics Links API

| HTTP Method | URI                            | Documented at                                                     |
| ----------- | ------------------------------ | ----------------------------------------------------------------- |
| POST        | /analytics/link/{scope}/{name} | [Create Link](../analytics-rest-links/index.md#post%5Flink)       |
| GET         | /analytics/link/{scope}/{name} | [Query Link](../analytics-rest-links/index.md#get%5Flink)         |
| PUT         | /analytics/link/{scope}/{name} | [Edit Link](../analytics-rest-links/index.md#put%5Flink)          |
| DELETE      | /analytics/link/{scope}/{name} | [Delete Link](../analytics-rest-links/index.md#delete%5Flink)     |
| GET         | /analytics/link                | [Query All Links](../analytics-rest-links/index.md#get%5Fall)     |
| GET         | /analytics/link/{scope}        | [Query Scope Links](../analytics-rest-links/index.md#get%5Fscope) |

### [](#analytics-library-api)Analytics Library API

| HTTP Method | URI                                  | Documented at                                                                   |
| ----------- | ------------------------------------ | ------------------------------------------------------------------------------- |
| GET         | /analytics/library                   | [Read All Libraries](../analytics-rest-library/index.md#get%5Fcollection)       |
| POST        | /analytics/library/{scope}/{library} | [Create or Update a Library](../analytics-rest-library/index.md#post%5Flibrary) |
| DELETE      | /analytics/library/{scope}/{library} | [Delete a Library](../analytics-rest-links/index.md#delete%5Flibrary)           |

## [](#legacy-apis)Legacy APIs

The following methods are deprecated, and will be removed in a future release.

| HTTP Method | URI                                 | Documented at                                                                     |
| ----------- | ----------------------------------- | --------------------------------------------------------------------------------- |
| GET         | /analytics/node/agg/stats/remaining | [Pending Mutations (Deprecated)](../analytics-rest-admin/index.md#monitor%5Fnode) |
| POST        | /analytics/link                     | [Create Link (Alternative)](../analytics-rest-links/index.md#post%5Falt)          |
| PUT         | /analytics/link                     | [Edit Link (Alternative)](../analytics-rest-links/index.md#put%5Falt)             |
| DELETE      | /analytics/link                     | [Delete Link (Alternative)](../analytics-rest-links/index.md#delete%5Falt)        |