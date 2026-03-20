---
title: Query Service API
description: The Query Service provides REST APIs for executing SQL++
  statements, administering Query Service nodes, configuring the Query Service,
  and managing the JavaScript libraries used to create SQL++ user-defined
  functions.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/n1ql/pages/n1ql-rest-api/intro.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:server:n1ql:n1ql-rest-api/intro.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/n1ql/n1ql-rest-api/intro.html)

# Query Service API

> The Query Service provides REST APIs for executing SQL++ statements, administering Query Service nodes, configuring the Query Service, and managing the JavaScript libraries used to create SQL++ user-defined functions. 

## [](#apis-in-this-section)APIs in this Section

For a list of the methods and URIs covered in these pages, see the tables below.

### [](#sql-statement-execution)Query Service REST API

Use the Query Service REST API to execute SQL++ statements. This REST API uses ports `8093` and `18093`.

| HTTP Method | URI            | Documented at                                                           |
| ----------- | -------------- | ----------------------------------------------------------------------- |
| POST        | /query/service | [Query Service](../../n1ql-rest-query/index.md#post%5Fservice)          |
| GET         | /query/service | [Read-Only Query Service](../../n1ql-rest-query/index.md#get%5Fservice) |

### [](#query-service-administration)Query Admin REST API

Use the Query Administration REST API to administer the Query Service at the node level. This REST API uses ports `8093` and `18093`.

| HTTP Method | URI                                    | Documented at                                                                                 |
| ----------- | -------------------------------------- | --------------------------------------------------------------------------------------------- |
| GET         | /admin/clusters                        | [Read All Clusters](../../n1ql-rest-admin/index.md#get%5Fclusters)                            |
| GET         | /admin/clusters/{cluster}              | [Read a Cluster](../../n1ql-rest-admin/index.md#get%5Fcluster)                                |
| GET         | /admin/clusters/{cluster}/nodes        | [Read All Nodes](../../n1ql-rest-admin/index.md#get%5Fnodes)                                  |
| GET         | /admin/clusters/{cluster}/nodes/{node} | [Read a Node](../../n1ql-rest-admin/index.md#get%5Fnode)                                      |
| GET         | /admin/config                          | [Read Configuration](../../n1ql-rest-admin/index.md#get%5Fconfig)                             |
| GET         | /admin/prepareds                       | [Retrieve All Prepared Statements](../../n1ql-rest-admin/index.md#get%5Fprepareds)            |
| GET         | /admin/prepareds/{name}                | [Retrieve a Prepared Statement](../../n1ql-rest-admin/index.md#get%5Fprepared)                |
| DELETE      | /admin/prepareds/{name}                | [Delete a Prepared Statement](../../n1ql-rest-admin/index.md#delete%5Fprepared)               |
| GET         | /admin/indexes/prepareds               | [Retrieve Prepared Index Statements](../../n1ql-rest-admin/index.md#get%5Fprepared%5Findexes) |
| GET         | /admin/active\_requests                | [Retrieve All Active Requests](../../n1ql-rest-admin/index.md#get%5Factive%5Frequests)        |
| GET         | /admin/active\_requests/{request}      | [Retrieve an Active Request](../../n1ql-rest-admin/index.md#get%5Factive%5Frequest)           |
| DELETE      | /admin/active\_requests/{request}      | [Delete an Active Request](../../n1ql-rest-admin/index.md#delete%5Factive%5Frequest)          |
| GET         | /admin/indexes/active\_requests        | [Retrieve Active Index Requests](../../n1ql-rest-admin/index.md#get%5Factive%5Findexes)       |
| GET         | /admin/completed\_requests             | [Retrieve All Completed Requests](../../n1ql-rest-admin/index.md#get%5Fcompleted%5Frequests)  |
| GET         | /admin/completed\_requests/{request}   | [Retrieve a Completed Request](../../n1ql-rest-admin/index.md#get%5Fcompleted%5Frequest)      |
| DELETE      | /admin/completed\_requests/{request}   | [Delete a Completed Request](../../n1ql-rest-admin/index.md#delete%5Fcompleted%5Frequest)     |
| GET         | /admin/indexes/completed\_requests     | [Retrieve Completed Index Requests](../../n1ql-rest-admin/index.md#get%5Fcompleted%5Findexes) |
| GET         | /admin/vitals                          | [Retrieve Vitals](../../n1ql-rest-admin/index.md#get%5Fvitals)                                |
| GET         | /admin/stats                           | [Retrieve All Statistics](../../n1ql-rest-admin/index.md#get%5Fstats)                         |
| GET         | /admin/stats/{stats}                   | [Retrieve a Statistic](../../n1ql-rest-admin/index.md#get%5Fstat)                             |
| GET         | /admin/settings                        | [Retrieve Node-Level Query Settings](../../n1ql-rest-admin/index.md#get%5Fsettings)           |
| POST        | /admin/settings                        | [Update Node-Level Query Settings](../../n1ql-rest-admin/index.md#post%5Fsettings)            |
| GET         | /admin/ping                            | [Ping](../../n1ql-rest-admin/index.md#get%5Fping)                                             |
| GET         | /admin/gc                              | [Run Garbage Collector](../../n1ql-rest-admin/index.md#get%5Fgc)                              |
| POST        | /admin/gc                              | [Run Garbage Collector and Release Memory](../../n1ql-rest-admin/index.md#post%5Fgc)          |

### [](#query-service-settings)Query Settings REST API

Use the Query Settings REST API to configure the Query Service at the cluster level. This REST API uses ports `8091` and `18091`.

| HTTP Method | URI                                   | Documented at                                                                             |
| ----------- | ------------------------------------- | ----------------------------------------------------------------------------------------- |
| GET         | /settings/querySettings               | [Retrieve Cluster-Level Query Settings](../../n1ql-rest-settings/index.md#get%5Fsettings) |
| POST        | /settings/querySettings               | [Update Cluster-Level Query Settings](../../n1ql-rest-settings/index.md#post%5Fsettings)  |
| GET         | /settings/querySettings/curlWhitelist | [Retrieve CURL Access List](../../n1ql-rest-settings/index.md#get%5Faccess)               |
| POST        | /settings/querySettings/curlWhitelist | [Update CURL Access List](../../n1ql-rest-settings/index.md#post%5Faccess)                |

### [](#javascript-management)Query Functions REST API

Use the Query Functions REST API to manage the JavaScript libraries and objects used to create SQL++ user-defined functions. This REST API uses ports `8093` and `18093`.

| HTTP Method | URI                               | Documented at                                                                   |
| ----------- | --------------------------------- | ------------------------------------------------------------------------------- |
| GET         | /evaluator/v1/libraries           | [Read All Libraries](../../n1ql-rest-functions/index.md#get%5Fcollection)       |
| GET         | /evaluator/v1/libraries/{library} | [Read a Library](../../n1ql-rest-functions/index.md#get%5Flibrary)              |
| POST        | /evaluator/v1/libraries/{library} | [Create or Update a Library](../../n1ql-rest-functions/index.md#post%5Flibrary) |
| DELETE      | /evaluator/v1/libraries/{library} | [Delete a Library](../../n1ql-rest-functions/index.md#delete%5Flibrary)         |

## [](#see-also)See Also

For an explanation of how cluster-level settings, node-level settings, and request-level parameters interact, see [Configure Queries](../n1ql-manage/query-settings.md).