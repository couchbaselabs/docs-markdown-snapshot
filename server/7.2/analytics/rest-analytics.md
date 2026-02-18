---
title: Analytics REST API
description: A description of the Analytics REST API.
editUrl: https://github.com/couchbase/docs-analytics/edit/release/7.2/modules/analytics/pages/rest-analytics.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/analytics/rest-analytics.html)

# Analytics REST API

Analytics provides REST APIs that a client application can use to invoke services using simple HTTP methods. A catalog of available REST resources and requests is provided below.

The Analytics REST APIs can be called on any node running the analytics service. By default, the Analytics REST endpoints below listen on port 8095, or 18095 for secure access. Note that the Settings API listens on port 8091, or 18091 for secure access.

For the examples, we assume that:

* You’re running a Couchbase node with the Analytics service using the default port on localhost.
* You authenticate as a user with the "Full Administrator" role with the user name "Administrator" and the password "password".

## [](#apis-in-this-section)APIs in this Section

For a list of the methods and URIs covered in these pages, see the tables below.

### [](#analytics-query-api)Analytics Query API

| HTTP Method | URI                | Documented at                                                           |
| ----------- | ------------------ | ----------------------------------------------------------------------- |
| POST        | /analytics/service | [Query Service](rest-service.md#%5Fpost%5Fservice)                      |
| GET         | /analytics/service | [Read-Only Query Service](rest-service.md#%5Fget%5Fservice)             |
| POST        | /query/service     | [Query Service (Alternative)](rest-service.md#%5Fpost%5Fquery)          |
| GET         | /query/service     | [Read-Only Query Service (Alternative)](rest-service.md#%5Fget%5Fquery) |

### [](#analytics-admin-api)Analytics Admin API

| HTTP Method | URI                               | Documented at                                             |
| ----------- | --------------------------------- | --------------------------------------------------------- |
| DELETE      | /analytics/admin/active\_requests | [Request Cancellation](rest-admin.md#%5Fcancel%5Frequest) |
| GET         | /analytics/cluster                | [Cluster Status](rest-admin.md#%5Fcluster%5Fstatus)       |
| POST        | /analytics/cluster/restart        | [Cluster Restart](rest-admin.md#%5Frestart%5Fcluster)     |
| POST        | /analytics/node/restart           | [Node Restart](rest-admin.md#%5Frestart%5Fnode)           |
| GET         | /analytics/status/ingestion       | [Ingestion Status](rest-admin.md#%5Fingestion%5Fstatus)   |

### [](#analytics-config-api)Analytics Config API

| HTTP Method | URI                       | Documented at                                                      |
| ----------- | ------------------------- | ------------------------------------------------------------------ |
| GET         | /analytics/config/service | [View Service-Level Parameters](rest-config.md#%5Fget%5Fservice)   |
| PUT         | /analytics/config/service | [Modify Service-Level Parameters](rest-config.md#%5Fput%5Fservice) |
| GET         | /analytics/config/node    | [View Node-Specific Parameters](rest-config.md#%5Fget%5Fnode)      |
| PUT         | /analytics/config/node    | [Modify Node-Specific Parameters](rest-config.md#%5Fput%5Fnode)    |

### [](#analytics-settings-api)Analytics Settings API

| HTTP Method | URI                 | Documented at                                                    |
| ----------- | ------------------- | ---------------------------------------------------------------- |
| GET         | /settings/analytics | [View Analytics Settings](rest-settings.md#%5Fget%5Fsettings)    |
| POST        | /settings/analytics | [Modify Analytics Settings](rest-settings.md#%5Fpost%5Fsettings) |

### [](#analytics-links-api)Analytics Links API

| HTTP Method | URI                            | Documented at                                     |
| ----------- | ------------------------------ | ------------------------------------------------- |
| POST        | /analytics/link/{scope}/{name} | [Create Link](rest-links.md#%5Fpost%5Flink)       |
| GET         | /analytics/link/{scope}/{name} | [Query Link](rest-links.md#%5Fget%5Flink)         |
| PUT         | /analytics/link/{scope}/{name} | [Edit Link](rest-links.md#%5Fput%5Flink)          |
| DELETE      | /analytics/link/{scope}/{name} | [Delete Link](rest-links.md#%5Fdelete%5Flink)     |
| GET         | /analytics/link                | [Query All Links](rest-links.md#%5Fget%5Fall)     |
| GET         | /analytics/link/{scope}        | [Query Scope Links](rest-links.md#%5Fget%5Fscope) |

### [](#analytics-library-api)Analytics Library API

| HTTP Method | URI                                  | Documented at                                                   |
| ----------- | ------------------------------------ | --------------------------------------------------------------- |
| GET         | /analytics/library                   | [Read All Libraries](rest-library.md#%5Fget%5Fcollection)       |
| POST        | /analytics/library/{scope}/{library} | [Create or Update a Library](rest-library.md#%5Fpost%5Flibrary) |
| DELETE      | /analytics/library/{scope}/{library} | [Delete a Library](rest-links.md#%5Fdelete%5Flibrary)           |

## [](#legacy-apis)Legacy APIs

The following methods are deprecated, and will be removed in a future release.

| HTTP Method | URI                                 | Documented at                                                     |
| ----------- | ----------------------------------- | ----------------------------------------------------------------- |
| GET         | /analytics/node/agg/stats/remaining | [Pending Mutations (Deprecated)](rest-admin.md#%5Fmonitor%5Fnode) |
| POST        | /analytics/link                     | [Create Link (Alternative)](rest-links.md#%5Fpost%5Falt)          |
| PUT         | /analytics/link                     | [Edit Link (Alternative)](rest-links.md#%5Fput%5Falt)             |
| DELETE      | /analytics/link                     | [Delete Link (Alternative)](rest-links.md#%5Fdelete%5Falt)        |