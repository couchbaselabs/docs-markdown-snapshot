---
title: Query Admin REST API
editUrl: https://github.com/couchbaselabs/cb-swagger/edit/release/7.6/docs/modules/n1ql-rest-admin/pages/index.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.6@server:n1ql-rest-admin:index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/n1ql-rest-admin/index.html)

# Query Admin REST API

## [](#overview)Overview

The Query Admin REST API is a secondary API provided by the Query service. This API enables you to retrieve statistics about the clusters and nodes running the Query service; view or specify node-level settings; and view or delete requests.

### Version information

**Version:** 7.6

### Host information

{scheme}://{host}:{port}

The URL scheme, host, and port are as follows.

| Component  | Description                                                                             |
| ---------- | --------------------------------------------------------------------------------------- |
| **scheme** | The URL scheme. Use https for secure access. **Values:** http, https                    |
| **host**   | The host name or IP address of a node running the Query Service. **Example:** localhost |
| **port**   | The Query Service REST port. Use 18093 for secure access. **Values:** 8093, 18093       |

## [](#resources)Resources

This section describes the operations available with this REST API. The operations are grouped in the following categories.

[Active Requests](#tag-ActiveRequests)  
[Completed Requests](#tag-CompletedRequests)  
[Configuration](#tag-Configuration)  
[Default](#tag-Default)  
[Prepared Statements](#tag-PreparedStatements)  
[Settings](#tag-Settings)  
[Statistics](#tag-Statistics)

### [](#tag-ActiveRequests)Active Requests

**Table of Contents**

[Delete an Active Request](#delete%5Factive%5Frequest)  
[Retrieve Active Index Requests](#get%5Factive%5Findexes)  
[Retrieve an Active Request](#get%5Factive%5Frequest)  
[Retrieve All Active Requests](#get%5Factive%5Frequests)

#### [](#delete%5Factive%5Frequest)Delete an Active Request

DELETE /admin/active_requests/{request}

##### [](#delete%5Factive%5Frequest-description)Description

Terminates the specified active query request.

Produces

* application/json

##### [](#delete%5Factive%5Frequest-parameters)Parameters

Path Parameters

| Name                | Description                                                                                                  | Schema |
| ------------------- | ------------------------------------------------------------------------------------------------------------ | ------ |
| **request**required | The name of a request. This is the requestID that was assigned automatically when the statement was created. | String |

##### [](#delete%5Factive%5Frequest-responses)Responses

| HTTP Code | Description                                                        | Schema |
| --------- | ------------------------------------------------------------------ | ------ |
| 200       | The active request was successfully terminated.                    |        |
| 500       | Returns an error message if the active request could not be found. | Object |

##### [](#delete%5Factive%5Frequest-security)Security

| Type         | Name                         |
| ------------ | ---------------------------- |
| http (basic) | [Default](#security-Default) |

##### [](#example-http-request)Example HTTP Request

For examples, see [Terminate an Active Request](../n1ql/n1ql-manage/monitoring-n1ql-query.md#sys-active-delete).

#### [](#get%5Factive%5Findexes)Retrieve Active Index Requests

GET /admin/indexes/active_requests

##### [](#get%5Factive%5Findexes-description)Description

Returns all active index requests.

* Use [Retrieve an Active Request](#get%5Factive%5Frequest) to get information about an active index request.
* Use [Delete an Active Request](#delete%5Factive%5Frequest) to terminate an active index request.

Produces

* application/json

##### [](#get%5Factive%5Findexes-responses)Responses

| HTTP Code | Description                                                                     | Schema       |
| --------- | ------------------------------------------------------------------------------- | ------------ |
| 200       | An array of strings, each of which is the requestID of an active index request. | String array |

##### [](#get%5Factive%5Findexes-security)Security

| Type         | Name                         |
| ------------ | ---------------------------- |
| http (basic) | [Default](#security-Default) |

#### [](#get%5Factive%5Frequest)Retrieve an Active Request

GET /admin/active_requests/{request}

##### [](#get%5Factive%5Frequest-description)Description

Returns the specified active query request.

Produces

* application/json

##### [](#get%5Factive%5Frequest-parameters)Parameters

Path Parameters

| Name                | Description                                                                                                  | Schema |
| ------------------- | ------------------------------------------------------------------------------------------------------------ | ------ |
| **request**required | The name of a request. This is the requestID that was assigned automatically when the statement was created. | String |

##### [](#get%5Factive%5Frequest-responses)Responses

| HTTP Code | Description                                                          | Schema                |
| --------- | -------------------------------------------------------------------- | --------------------- |
| 200       | An object containing information about the specified active request. | [Requests](#Requests) |

##### [](#get%5Factive%5Frequest-security)Security

| Type         | Name                         |
| ------------ | ---------------------------- |
| http (basic) | [Default](#security-Default) |

##### [](#example-http-request-2)Example HTTP Request

For examples, see [Get Active Requests](../n1ql/n1ql-manage/monitoring-n1ql-query.md#sys-active-get).

#### [](#get%5Factive%5Frequests)Retrieve All Active Requests

GET /admin/active_requests

##### [](#get%5Factive%5Frequests-description)Description

Returns all active query requests.

Produces

* application/json

##### [](#get%5Factive%5Frequests-responses)Responses

| HTTP Code | Description                                                                       | Schema                      |
| --------- | --------------------------------------------------------------------------------- | --------------------------- |
| 200       | An array of objects, each of which contains information about one active request. | [Requests](#Requests) array |

##### [](#get%5Factive%5Frequests-security)Security

| Type         | Name                         |
| ------------ | ---------------------------- |
| http (basic) | [Default](#security-Default) |

##### [](#example-http-request-3)Example HTTP Request

For examples, see [Get Active Requests](../n1ql/n1ql-manage/monitoring-n1ql-query.md#sys-active-get).

### [](#tag-CompletedRequests)Completed Requests

**Table of Contents**

[Delete a Completed Request](#delete%5Fcompleted%5Frequest)  
[Retrieve Completed Index Requests](#get%5Fcompleted%5Findexes)  
[Retrieve a Completed Request](#get%5Fcompleted%5Frequest)  
[Retrieve All Completed Requests](#get%5Fcompleted%5Frequests)

#### [](#delete%5Fcompleted%5Frequest)Delete a Completed Request

DELETE /admin/completed_requests/{request}

##### [](#delete%5Fcompleted%5Frequest-description)Description

Purges the specified completed request.

Produces

* application/json

##### [](#delete%5Fcompleted%5Frequest-parameters)Parameters

Path Parameters

| Name                | Description                                                                                                  | Schema |
| ------------------- | ------------------------------------------------------------------------------------------------------------ | ------ |
| **request**required | The name of a request. This is the requestID that was assigned automatically when the statement was created. | String |

##### [](#delete%5Fcompleted%5Frequest-responses)Responses

| HTTP Code | Description                                                           | Schema |
| --------- | --------------------------------------------------------------------- | ------ |
| 200       | The completed request was successfully purged.                        |        |
| 500       | Returns an error message if the completed request could not be found. | Object |

##### [](#delete%5Fcompleted%5Frequest-security)Security

| Type         | Name                         |
| ------------ | ---------------------------- |
| http (basic) | [Default](#security-Default) |

##### [](#example-http-request-4)Example HTTP Request

For examples, see [Purge the Completed Requests](../n1ql/n1ql-manage/monitoring-n1ql-query.md#sys-completed-delete).

#### [](#get%5Fcompleted%5Findexes)Retrieve Completed Index Requests

GET /admin/indexes/completed_requests

##### [](#get%5Fcompleted%5Findexes-description)Description

Returns all completed index requests.

* Use [Retrieve a Completed Request](#get%5Fcompleted%5Frequest) to get information about a completed index request.
* Use [Delete a Completed Request](#delete%5Fcompleted%5Frequest) to purge a completed index request.

Produces

* application/json

##### [](#get%5Fcompleted%5Findexes-responses)Responses

| HTTP Code | Description                                                                       | Schema       |
| --------- | --------------------------------------------------------------------------------- | ------------ |
| 200       | An array of strings, each of which is the requestID of a completed index request. | String array |

##### [](#get%5Fcompleted%5Findexes-security)Security

| Type         | Name                         |
| ------------ | ---------------------------- |
| http (basic) | [Default](#security-Default) |

#### [](#get%5Fcompleted%5Frequest)Retrieve a Completed Request

GET /admin/completed_requests/{request}

##### [](#get%5Fcompleted%5Frequest-description)Description

Returns the specified completed request.

Produces

* application/json

##### [](#get%5Fcompleted%5Frequest-parameters)Parameters

Path Parameters

| Name                | Description                                                                                                  | Schema |
| ------------------- | ------------------------------------------------------------------------------------------------------------ | ------ |
| **request**required | The name of a request. This is the requestID that was assigned automatically when the statement was created. | String |

##### [](#get%5Fcompleted%5Frequest-responses)Responses

| HTTP Code | Description                                                             | Schema                |
| --------- | ----------------------------------------------------------------------- | --------------------- |
| 200       | An object containing information about the specified completed request. | [Requests](#Requests) |

##### [](#get%5Fcompleted%5Frequest-security)Security

| Type         | Name                         |
| ------------ | ---------------------------- |
| http (basic) | [Default](#security-Default) |

##### [](#example-http-request-5)Example HTTP Request

For examples, see [Get Completed Requests](../n1ql/n1ql-manage/monitoring-n1ql-query.md#sys-completed-get).

#### [](#get%5Fcompleted%5Frequests)Retrieve All Completed Requests

GET /admin/completed_requests

##### [](#get%5Fcompleted%5Frequests-description)Description

Returns all completed requests.

Produces

* application/json

##### [](#get%5Fcompleted%5Frequests-responses)Responses

| HTTP Code | Description                                                                          | Schema                      |
| --------- | ------------------------------------------------------------------------------------ | --------------------------- |
| 200       | An array of objects, each of which contains information about one completed request. | [Requests](#Requests) array |

##### [](#get%5Fcompleted%5Frequests-security)Security

| Type         | Name                         |
| ------------ | ---------------------------- |
| http (basic) | [Default](#security-Default) |

##### [](#example-http-request-6)Example HTTP Request

For examples, see [Get Completed Requests](../n1ql/n1ql-manage/monitoring-n1ql-query.md#sys-completed-get).

### [](#tag-Configuration)Configuration

Operations for cluster and node configuration.

[Read a Cluster](#get%5Fcluster)  
[Read All Clusters](#get%5Fclusters)  
[Read Configuration](#get%5Fconfig)  
[Read a Node](#get%5Fnode)  
[Read All Nodes](#get%5Fnodes)

#### [](#get%5Fcluster)Read a Cluster

GET /admin/clusters/{cluster}

##### [](#get%5Fcluster-description)Description

Returns information about the specified cluster.

Produces

* application/json

##### [](#get%5Fcluster-parameters)Parameters

Path Parameters

| Name                | Description            | Schema |
| ------------------- | ---------------------- | ------ |
| **cluster**required | The name of a cluster. | String |

##### [](#get%5Fcluster-responses)Responses

| HTTP Code | Description                                               | Schema                           |
| --------- | --------------------------------------------------------- | -------------------------------- |
| 200       | An object giving information about the specified cluster. | [Cluster Information](#Clusters) |

##### [](#get%5Fcluster-security)Security

| Type         | Name                         |
| ------------ | ---------------------------- |
| http (basic) | [Default](#security-Default) |

#### [](#get%5Fclusters)Read All Clusters

GET /admin/clusters

##### [](#get%5Fclusters-description)Description

Returns information about all clusters.

Produces

* application/json

##### [](#get%5Fclusters-responses)Responses

| HTTP Code | Description                                                             | Schema                                 |
| --------- | ----------------------------------------------------------------------- | -------------------------------------- |
| 200       | An array of objects, each of which gives information about one cluster. | [Cluster Information](#Clusters) array |

##### [](#get%5Fclusters-security)Security

| Type         | Name                         |
| ------------ | ---------------------------- |
| http (basic) | [Default](#security-Default) |

#### [](#get%5Fconfig)Read Configuration

GET /admin/config

##### [](#get%5Fconfig-description)Description

Returns the configuration of the query service on the cluster.

Produces

* application/json

##### [](#get%5Fconfig-responses)Responses

| HTTP Code | Description                                            | Schema                     |
| --------- | ------------------------------------------------------ | -------------------------- |
| 200       | An object giving information about the specified node. | [Node Information](#Nodes) |

##### [](#get%5Fconfig-security)Security

| Type         | Name                         |
| ------------ | ---------------------------- |
| http (basic) | [Default](#security-Default) |

#### [](#get%5Fnode)Read a Node

GET /admin/clusters/{cluster}/nodes/{node}

##### [](#get%5Fnode-description)Description

Returns information about the specified node in the specified cluster.

Produces

* application/json

##### [](#get%5Fnode-parameters)Parameters

Path Parameters

| Name                | Description            | Schema |
| ------------------- | ---------------------- | ------ |
| **cluster**required | The name of a cluster. | String |
| **node**required    | The name of a node.    | String |

##### [](#get%5Fnode-responses)Responses

| HTTP Code | Description                                            | Schema                     |
| --------- | ------------------------------------------------------ | -------------------------- |
| 200       | An object giving information about the specified node. | [Node Information](#Nodes) |

##### [](#get%5Fnode-security)Security

| Type         | Name                         |
| ------------ | ---------------------------- |
| http (basic) | [Default](#security-Default) |

#### [](#get%5Fnodes)Read All Nodes

GET /admin/clusters/{cluster}/nodes

##### [](#get%5Fnodes-description)Description

Returns information about all nodes in the specified cluster.

Produces

* application/json

##### [](#get%5Fnodes-parameters)Parameters

Path Parameters

| Name                | Description            | Schema |
| ------------------- | ---------------------- | ------ |
| **cluster**required | The name of a cluster. | String |

##### [](#get%5Fnodes-responses)Responses

| HTTP Code | Description                                                          | Schema                           |
| --------- | -------------------------------------------------------------------- | -------------------------------- |
| 200       | An array of objects, each of which gives information about one node. | [Node Information](#Nodes) array |

##### [](#get%5Fnodes-security)Security

| Type         | Name                         |
| ------------ | ---------------------------- |
| http (basic) | [Default](#security-Default) |

### [](#tag-Default)Default

Other operations.

[Run Garbage Collector](#get%5Fgc)  
[Ping](#get%5Fping)  
[Run Garbage Collector and Release Memory](#post%5Fgc)

#### [](#get%5Fgc)Run Garbage Collector

GET /admin/gc

##### [](#get%5Fgc-description)Description

Runs the garbage collector.

A message is written to `query.log` whenever the garbage collector endpoint is invoked.

Produces

* application/json

##### [](#get%5Fgc-responses)Responses

| HTTP Code | Description                                                                            | Schema                         |
| --------- | -------------------------------------------------------------------------------------- | ------------------------------ |
| 200       | Indicates that the garbage collector was invoked.                                      | [Garbage Collection](#Garbage) |
| 401       | Error 10000: authentication failure. The invoking user is not a valid full-admin user. | Object                         |

##### [](#get%5Fgc-security)Security

| Type         | Name                         |
| ------------ | ---------------------------- |
| http (basic) | [Default](#security-Default) |

##### [](#get%5Fgc-ex-response)Example HTTP Response

Response 200

```json
{
  "freed" : 123456,
  "status" : "GC invoked"
}
```

#### [](#get%5Fping)Ping

GET /admin/ping

##### [](#get%5Fping-description)Description

Returns a minimal response, indicating that the service is running and reachable.

Produces

* application/json

##### [](#get%5Fping-responses)Responses

| HTTP Code | Description      | Schema |
| --------- | ---------------- | ------ |
| 200       | An empty object. | Object |

##### [](#get%5Fping-security)Security

No authentication is required for this endpoint.

##### [](#example-http-response)Example HTTP Response

Response 200

```json
{}
```

#### [](#post%5Fgc)Run Garbage Collector and Release Memory

POST /admin/gc

##### [](#post%5Fgc-description)Description

Run the garbage collector and attempts to return freed memory to the OS.

A message is written to `query.log` whenever the garbage collector endpoint is invoked.

Produces

* application/json

##### [](#post%5Fgc-responses)Responses

| HTTP Code | Description                                                                            | Schema                         |
| --------- | -------------------------------------------------------------------------------------- | ------------------------------ |
| 200       | Indicates that the garbage collector was invoked.                                      | [Garbage Collection](#Garbage) |
| 401       | Error 10000: authentication failure. The invoking user is not a valid full-admin user. | Object                         |

##### [](#post%5Fgc-security)Security

| Type         | Name                         |
| ------------ | ---------------------------- |
| http (basic) | [Default](#security-Default) |

##### [](#post%5Fgc-ex-response)Example HTTP Response

Response 200

```json
{
  "freed" : 109304,
  "released" : 835584,
  "status" : "GC invoked and memory released"
}
```

### [](#tag-PreparedStatements)Prepared Statements

**Table of Contents**

[Delete a Prepared Statement](#delete%5Fprepared)  
[Retrieve a Prepared Statement](#get%5Fprepared)  
[Retrieve Prepared Index Statements](#get%5Fprepared%5Findexes)  
[Retrieve All Prepared Statements](#get%5Fprepareds)

#### [](#delete%5Fprepared)Delete a Prepared Statement

DELETE /admin/prepareds/{name}

##### [](#delete%5Fprepared-description)Description

Deletes the specified prepared statement.

Produces

* application/json

##### [](#delete%5Fprepared-parameters)Parameters

Path Parameters

| Name             | Description                                                                                                                                             | Schema |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **name**required | The name of a prepared statement. This may be a UUID that was assigned automatically, or a name that was user-specified when the statement was created. | String |

##### [](#delete%5Fprepared-responses)Responses

| HTTP Code | Description                                                            | Schema |
| --------- | ---------------------------------------------------------------------- | ------ |
| 200       | The prepared statement was successfully deleted.                       |        |
| 500       | Returns an error message if the prepared statement could not be found. | Object |

##### [](#delete%5Fprepared-security)Security

| Type         | Name                         |
| ------------ | ---------------------------- |
| http (basic) | [Default](#security-Default) |

##### [](#example-http-request-7)Example HTTP Request

For examples, see [Delete Prepared Statements](../n1ql/n1ql-manage/monitoring-n1ql-query.md#sys-prepared-delete).

#### [](#get%5Fprepared)Retrieve a Prepared Statement

GET /admin/prepareds/{name}

##### [](#get%5Fprepared-description)Description

Returns the specified prepared statement.

Produces

* application/json

##### [](#get%5Fprepared-parameters)Parameters

Path Parameters

| Name             | Description                                                                                                                                             | Schema |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **name**required | The name of a prepared statement. This may be a UUID that was assigned automatically, or a name that was user-specified when the statement was created. | String |

##### [](#get%5Fprepared-responses)Responses

| HTTP Code | Description                                                              | Schema                             |
| --------- | ------------------------------------------------------------------------ | ---------------------------------- |
| 200       | An object containing information about the specified prepared statement. | [Prepared Statements](#Statements) |

##### [](#get%5Fprepared-security)Security

| Type         | Name                         |
| ------------ | ---------------------------- |
| http (basic) | [Default](#security-Default) |

##### [](#example-http-request-8)Example HTTP Request

For examples, see [Get Prepared Statements](../n1ql/n1ql-manage/monitoring-n1ql-query.md#sys-prepared-get).

#### [](#get%5Fprepared%5Findexes)Retrieve Prepared Index Statements

GET /admin/indexes/prepareds

##### [](#get%5Fprepared%5Findexes-description)Description

Returns all prepared index statements.

* Use [Retrieve a Prepared Statement](#get%5Fprepared) to get information about a prepared index statement.
* Use [Delete a Prepared Statement](#delete%5Fprepared) to delete a prepared index statement.

Produces

* application/json

##### [](#get%5Fprepared%5Findexes-responses)Responses

| HTTP Code | Description                                                                   | Schema       |
| --------- | ----------------------------------------------------------------------------- | ------------ |
| 200       | An array of strings, each of which is the name of a prepared index statement. | String array |

##### [](#get%5Fprepared%5Findexes-security)Security

| Type         | Name                         |
| ------------ | ---------------------------- |
| http (basic) | [Default](#security-Default) |

#### [](#get%5Fprepareds)Retrieve All Prepared Statements

GET /admin/prepareds

##### [](#get%5Fprepareds-description)Description

Returns all prepared statements.

Produces

* application/json

##### [](#get%5Fprepareds-responses)Responses

| HTTP Code | Description                                                                           | Schema                                   |
| --------- | ------------------------------------------------------------------------------------- | ---------------------------------------- |
| 200       | An array of objects, each of which contains information about one prepared statement. | [Prepared Statements](#Statements) array |

##### [](#get%5Fprepareds-security)Security

| Type         | Name                         |
| ------------ | ---------------------------- |
| http (basic) | [Default](#security-Default) |

##### [](#example-http-request-9)Example HTTP Request

For examples, see [Get Prepared Statements](../n1ql/n1ql-manage/monitoring-n1ql-query.md#sys-prepared-get).

### [](#tag-Settings)Settings

Operations for query settings.

[Retrieve Node-Level Query Settings](#get%5Fsettings)  
[Update Node-Level Query Settings](#post%5Fsettings)

#### [](#get%5Fsettings)Retrieve Node-Level Query Settings

GET /admin/settings

##### [](#get%5Fsettings-description)Description

Returns node-level query settings.

Produces

* application/json

> [!NOTE]
> For more information, see [Configure Queries](../n1ql/n1ql-manage/query-settings.md).

##### [](#get%5Fsettings-responses)Responses

| HTTP Code | Description                                 | Schema                |
| --------- | ------------------------------------------- | --------------------- |
| 200       | An object giving node-level query settings. | [Settings](#Settings) |

##### [](#get%5Fsettings-security)Security

| Type         | Name                         |
| ------------ | ---------------------------- |
| http (basic) | [Default](#security-Default) |

#### [](#post%5Fsettings)Update Node-Level Query Settings

POST /admin/settings

##### [](#post%5Fsettings-description)Description

Updates node-level query settings.

Consumes

* application/json
* application/x-www-form-urlencoded

Produces

* application/json

> [!NOTE]
> For more information, see [Configure Queries](../n1ql/n1ql-manage/query-settings.md).

##### [](#post%5Fsettings-parameters)Parameters

Body Parameter

| Name             | Description                                     | Schema                |
| ---------------- | ----------------------------------------------- | --------------------- |
| **Body**optional | An object specifying node-level query settings. | [Settings](#Settings) |

##### [](#post%5Fsettings-responses)Responses

| HTTP Code | Description                                                               | Schema                |
| --------- | ------------------------------------------------------------------------- | --------------------- |
| 200       | An object giving node-level query settings, including the latest changes. | [Settings](#Settings) |

##### [](#post%5Fsettings-security)Security

| Type         | Name                         |
| ------------ | ---------------------------- |
| http (basic) | [Default](#security-Default) |

### [](#tag-Statistics)Statistics

Operations for query statistics.

[Get Debug Variables](#get%5Fdebug%5Fvars)  
[Retrieve a Statistic](#get%5Fstat)  
[Retrieve All Statistics](#get%5Fstats)  
[Retrieve Vitals](#get%5Fvitals)

#### [](#get%5Fdebug%5Fvars)Get Debug Variables

GET /debug/vars

##### [](#get%5Fdebug%5Fvars-description)Description

Currently unused.

Produces

* text/html

##### [](#get%5Fdebug%5Fvars-responses)Responses

| HTTP Code | Description                                                        | Schema             |
| --------- | ------------------------------------------------------------------ | ------------------ |
| 302       | Redirects to the [Retrieve All Statistics](#get%5Fstats) endpoint. | String (text/html) |

##### [](#get%5Fdebug%5Fvars-security)Security

No authentication is required for this endpoint.

##### [](#get%5Fdebug%5Fvars-ex-response)Example HTTP Response

Response 302

```html
<a href="/admin/stats">Found</a>.
```

#### [](#get%5Fstat)Retrieve a Statistic

GET /admin/stats/{stat}

##### [](#get%5Fstat-description)Description

Returns the specified statistic.

Produces

* application/json

##### [](#get%5Fstat-parameters)Parameters

Path Parameters

| Name             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Schema |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **stat**required | The name of a statistic. Only top-level statistic names can be used. You cannot specify a metric. **Values:** "active\_requests", "at\_plus", "audit\_actions", "audit\_actions\_failed", "audit\_requests\_filtered", "audit\_requests\_total", "cancelled", "deletes", "errors", "index\_scans", "inserts", "invalid\_requests", "mutations", "prepared", "primary\_scans", "queued\_requests", "request\_time", "request\_timer", "requests", "requests\_1000ms", "requests\_250ms", "requests\_5000ms", "requests\_500ms", "result\_count", "result\_size", "scan\_plus", "selects", "service\_time", "unbounded", "updates", "warnings" | String |

##### [](#get%5Fstat-responses)Responses

| HTTP Code | Description                                                                                                  | Schema              |
| --------- | ------------------------------------------------------------------------------------------------------------ | ------------------- |
| 200       | An object containing all metrics for the specified statistic. Each statistic has a different set of metrics. | [Metrics](#Metrics) |

##### [](#get%5Fstat-security)Security

| Type         | Name                         |
| ------------ | ---------------------------- |
| http (basic) | [Default](#security-Default) |

#### [](#get%5Fstats)Retrieve All Statistics

GET /admin/stats

##### [](#get%5Fstats-description)Description

Returns all statistics.

Produces

* application/json

##### [](#get%5Fstats-responses)Responses

| HTTP Code | Description                                                                                                                                                  | Schema                    |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------- |
| 200       | An object containing all statistics. Each statistic consists of a top-level statistic name and a metric name. Each statistic has a different set of metrics. | [Statistics](#Statistics) |

##### [](#get%5Fstats-security)Security

| Type         | Name                         |
| ------------ | ---------------------------- |
| http (basic) | [Default](#security-Default) |

#### [](#get%5Fvitals)Retrieve Vitals

GET /admin/vitals

##### [](#get%5Fvitals-description)Description

Returns data about the running state and health of the query engine. This information can be very useful to assess the current workload and performance characteristics of a query engine, and hence load-balance the requests being sent to various query engines.

Produces

* application/json

##### [](#get%5Fvitals-responses)Responses

| HTTP Code | Description                                | Schema                      |
| --------- | ------------------------------------------ | --------------------------- |
| 200       | An object containing all vital statistics. | [Vital Statistics](#Vitals) |

##### [](#get%5Fvitals-security)Security

| Type         | Name                         |
| ------------ | ---------------------------- |
| http (basic) | [Default](#security-Default) |

##### [](#example-http-request-10)Example HTTP Request

For examples, see [Get System Vitals](../n1ql/n1ql-manage/monitoring-n1ql-query.md#vitals).

## [](#models)Definitions

This section describes the properties consumed and returned by this REST API.

[Cluster Information](#Clusters)  
[Garbage Collection](#Garbage)  
[Logging Parameters](#Logging%5FParameters)  
[Metrics](#Metrics)  
[Node Information](#Nodes)  
[Requests](#Requests)  
[Settings](#Settings)  
[Prepared Statements](#Statements)  
[Statistics](#Statistics)  
[Vital Statistics](#Vitals)

### [](#Clusters)Cluster Information

 Object

| Property                 |                              | Schema |
| ------------------------ | ---------------------------- | ------ |
| **name**optional         | The name of the cluster.     | String |
| **datastore**optional    | The URL of the datastore.    | String |
| **configstore**optional  | The URL of the configstore.  | String |
| **accountstore**optional | The URL of the accountstore. | String |
| **version**optional      |                              | String |

### [](#Garbage)Garbage Collection

 Object

| Property             |                                                                            | Schema  |
| -------------------- | -------------------------------------------------------------------------- | ------- |
| **freed**required    | The amount of memory freed.                                                | Integer |
| **released**optional | Only returned by the POST method. The amount of memory released to the OS. | Integer |
| **status**required   | The status of the garbage collector.                                       | String  |

#### Logging Parameters

 Object

| Property              |                                                                                                                                                                                                                                                                     | Schema          |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| **aborted**optional   | If true, all requests that generate a panic are logged. **Default:** null **Nullable:** yes **Example:** true                                                                                                                                                       | Boolean         |
| **client**optional    | The IP address of the client. If specified, all completed requests from this IP address are logged. **Default:** "" **Example:** "172.1.2.3"                                                                                                                        | String          |
| **context**optional   | The opaque ID or context provided by the client. If specified, all completed requests with this client context ID are logged. Refer to the [request-level](../n1ql-rest-query/index.html#client%5Fcontext%5Fid) client\_context\_id parameter for more information. | String          |
| **error**optional     | An error number. If specified, all completed queries returning this error number are logged. **Default:** null **Nullable:** yes **Example:** 12003                                                                                                                 | Integer (int32) |
| **tag**optional       | A unique string which tags a set of qualifiers. Refer to [Configure Completed Requests](../n1ql/n1ql-manage/monitoring-n1ql-query.html#sys-completed-config) for more information. **Default:** "" **Example:** "both\_user\_and\_error"                            | String          |
| **threshold**optional | A duration in milliseconds. If specified, all completed queries lasting longer than this threshold are logged. This is another way of specifying the completed-threshold setting. **Default:** 1000 **Example:** 7000                                               | Integer (int32) |
| **user**optional      | A user name, as given in the request credentials. If specified, all completed queries with this user name are logged. **Default:** "" **Example:** "marco"                                                                                                          | String          |
| **errors**optional    | The number of errors. If specified, all completed queries that return at least this many errors are logged. Queries with fewer errors are not logged. **Example:** 5                                                                                                | Integer (int32) |

### [](#Metrics)Metrics

 Object

| Property              |                                                   | Schema     |
| --------------------- | ------------------------------------------------- | ---------- |
| **count**optional     | A single value that represents the current state. | Integer    |
| **15m.rate**optional  | 15-minute exponentially weighted moving average.  | BigDecimal |
| **1m.rate**optional   | 1-minute exponentially weighted moving average.   | BigDecimal |
| **5m.rate**optional   | 5-minute exponentially weighted moving average.   | BigDecimal |
| **mean.rate**optional | Mean rate since the query service started.        | BigDecimal |
| **max**optional       | The maximum value.                                | Integer    |
| **mean**optional      | The mean value.                                   | BigDecimal |
| **median**optional    | The median value.                                 | BigDecimal |
| **min**optional       | The minimum value.                                | Integer    |
| **stddev**optional    | The standard deviation.                           | BigDecimal |
| **75%**optional       | The 75th percentile.                              | BigDecimal |
| **95%**optional       | The 95th percentile.                              | BigDecimal |
| **99%**optional       | The 99th percentile.                              | BigDecimal |
| **99.9%**optional     | The 99.9th percentile.                            | BigDecimal |

### [](#Nodes)Node Information

 Object

| Property                  |                                             | Schema |
| ------------------------- | ------------------------------------------- | ------ |
| **cluster**optional       | The name of the cluster.                    | String |
| **name**optional          | The URL of the node, including port number. | String |
| **queryEndpoint**optional | The HTTP URL of the query endpoint.         | String |
| **adminEndpoint**optional | The HTTP URL of the admin endpoint.         | String |
| **querySecure**optional   | The HTTPS URL of the query endpoint.        | String |
| **adminSecure**optional   | The HTTPS URL of the admin endpoint.        | String |
| **options**optional       |                                             | String |

### [](#Requests)Requests

 Object

| Property                    |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Schema            |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| **clientContextID**optional | The opaque ID or context provided by the client. Refer to the [request-level](../n1ql-rest-query/index.html#client%5Fcontext%5Fid) client\_context\_id parameter for more information.                                                                                                                                                                                                                                                                                                                                  | String            |
| **elapsedTime**optional     | The time taken from when the request was acknowledged by the service to when the request was completed. It includes the time taken by the service to schedule the request.                                                                                                                                                                                                                                                                                                                                              | String (duration) |
| **errorCount**optional      | Total number of errors encountered while executing the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Integer           |
| **memoryQuota**optional     | The memory quota for the request, in MB. This property is only returned if a memory quota is set for the query.                                                                                                                                                                                                                                                                                                                                                                                                         | Integer           |
| **node**optional            | IP address and port number of the node where the query is executed.                                                                                                                                                                                                                                                                                                                                                                                                                                                     | String            |
| **phaseCounts**optional     | Count of documents processed at selective phases involved in the query execution, such as authorize, index scan, fetch, parse, plan, run, etc. For active requests, this property is dynamic, depending on the documents processed by various phases up to this moment in time. Polling the active requests again may return different values. **Example:** {"fetch":16,"indexScan":187}                                                                                                                                | Object            |
| **phaseOperators**optional  | Indicates the numbers of each kind of query operator involved in different phases of the query processing. For instance, a non-covering index path might involve one index scan and one fetch operator. A join would probably involve two or more fetches, one per keyspace. A union select would have twice as many operator counts, one per each branch of the union. **Example:** {"authorize":1,"fetch":1,"indexScan":2}                                                                                            | Object            |
| **phaseTimes**optional      | Cumulative execution times for various phases involved in the query execution, such as authorize, index scan, fetch, parse, plan, run, etc. For active requests, this property is dynamic, depending on the documents processed by various phases up to this moment in time. Polling the active requests again may return different values. **Example:** {"authorize":"823.631µs","fetch":"656.873µs","indexScan":"29.146543ms","instantiate":"236.221µs","parse":"826.382µs","plan":"11.831101ms","run":"16.892181ms"} | Object            |
| **remoteAddr**optional      | IP address and port number of the client application, from where the query is received.                                                                                                                                                                                                                                                                                                                                                                                                                                 | String            |
| **requestId**optional       | Unique request ID internally generated for the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | UUID (uuid)       |
| **requestTime**optional     | Timestamp when the query is received.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Date (date-time)  |
| **resultCount**optional     | Total number of documents returned in the query result.                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Integer           |
| **resultSize**optional      | Total number of bytes returned in the query result.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Integer           |
| **scanConsistency**optional | The value of the query setting Scan Consistency used for the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                     | String            |
| **serviceTime**optional     | Total amount of calendar time taken to complete the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                              | String (duration) |
| **state**optional           | The state of the query execution, such as completed, running, cancelled. Note that the completed state means that the request was started and completed by the Query service, but it does not mean that it was necessarily successful. The request could have been successful, or completed with errors. To find requests that were successful, use this field in conjunction with the errorCount field: search for requests whose state is completed and whose error count is 0.                                       | String            |
| **statement**optional       | The query statement being executed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | String            |
| **useCBO**optional          | Whether the cost-based optimizer is enabled for the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Boolean           |
| **usedMemory**optional      | The amount of document memory used to execute the request. This property is only returned if a memory quota is set for the query.                                                                                                                                                                                                                                                                                                                                                                                       | Integer           |
| **userAgent**optional       | Name of the client application or program that issued the query.                                                                                                                                                                                                                                                                                                                                                                                                                                                        | String            |
| **users**optional           | Username with whose privileges the query is run.                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | String            |

### [](#Settings)Settings

 Object

| Property                            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Schema                                      |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------- |
| **atrcollection**optional           | Specifies the collection where [active transaction records](/server/7.6/learn/data/transactions.html#active-transaction-record-entries) are stored. The collection must be present. If not specified, the active transaction record is stored in the default collection in the default scope in the bucket containing the first mutated document within the transaction. The value must be a string in the form "bucket.scope.collection" or "namespace:bucket.scope.collection". If any part of the path contains a special character, that part of the path must be delimited in backticks \`\`. The [request-level](../n1ql-rest-query/index.html#atrcollection%5Freq) atrcollection parameter specifies this property per request. If a request does not include this parameter, the node-level atrcollection setting will be used. **Default:** "" **Example:** "default:\`travel-sample\`.transaction.test"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | String                                      |
| **auto-prepare**optional            | Specifies whether the query engine should create a prepared statement every time a SQL++ request is submitted, whether the PREPARE statement is included or not. Refer to [Auto-Prepare](../n1ql/n1ql-language-reference/prepare.html#auto-prepare) for more information. **Default:** false **Example:** true                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Boolean                                     |
| **cleanupclientattempts**optional   | When enabled, the Query service preferentially aims to clean up just transactions that it has created, leaving transactions for the distributed cleanup process only when it is forced to. The [cluster-level](../n1ql-rest-settings/index.html#queryCleanupClientAttempts) queryCleanupClientAttempts setting specifies this property for the whole cluster. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. **Default:** true **Example:** false                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Boolean                                     |
| **cleanuplostattempts**optional     | When enabled, the Query service takes part in the distributed cleanup process, and cleans up expired transactions created by any client. The [cluster-level](../n1ql-rest-settings/index.html#queryCleanupLostAttempts) queryCleanupLostAttempts setting specifies this property for the whole cluster. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. **Default:** true **Example:** false                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Boolean                                     |
| **cleanupwindow**optional           | Specifies how frequently the Query service checks its subset of [active transaction records](/server/7.6/learn/data/transactions.html#active-transaction-record-entries) for cleanup. Decreasing this setting causes expiration transactions to be found more swiftly, with the tradeoff of increasing the number of reads per second used for the scanning process. The value for this setting is a string. Its format includes an amount and a mandatory unit, e.g. 10ms (10 milliseconds) or 0.5s (half a second). Valid units are: ns (nanoseconds) us (microseconds) ms (milliseconds) s (seconds) m (minutes) h (hours) The [cluster-level](../n1ql-rest-settings/index.html#queryCleanupWindow) queryCleanupWindow setting specifies this property for the whole cluster. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. **Default:** "60s" **Example:** "30s"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | String (duration)                           |
| **completed**optional               | A nested object that sets the parameters for the completed requests catalog. All completed requests that match these parameters are tracked in the completed requests catalog. Refer to [Configure Completed Requests](../n1ql/n1ql-manage/monitoring-n1ql-query.html#sys-completed-config) for more information and examples.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | [Logging Parameters](#Logging%5FParameters) |
| **completed-limit**optional         | Sets the number of requests to be logged in the completed requests catalog. As new completed requests are added, old ones are removed. Increase this when the completed request keyspace is not big enough to track the slow requests, such as when you want a larger sample of slow requests. Refer to [Configure Completed Requests](../n1ql/n1ql-manage/monitoring-n1ql-query.html#sys-completed-config) for more information and examples. The [cluster-level](../n1ql-rest-settings/index.html#queryCompletedLimit) queryCompletedLimit setting specifies this property for the whole cluster. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. **Default:** 4000 **Example:** 7000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Integer (int32)                             |
| **completed-max-plan-size**optional | A plan size in bytes. Limits the size of query execution plans that can be logged in the completed requests catalog. Values larger than the maximum limit are silently treated as the maximum limit. Queries with plans larger than this are not logged. You must obtain execution plans for such queries via profiling or using the EXPLAIN statement. Refer to [Configure Completed Requests](../n1ql/n1ql-manage/monitoring-n1ql-query.html#sys-completed-config) for more information. The [cluster-level](../n1ql-rest-settings/index.html#queryCompletedMaxPlanSize) queryCompletedMaxPlanSize setting specifies this property for the whole cluster. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. **Default:** 262144 **Minimum:** 0 **Maximum:** 20840448                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Integer (int32)                             |
| **completed-stream-size**optional   | Couchbase Server 7.6.4 A file size in MiB. When specified, completed requests are saved to the Couchbase Server logs directory. Completed requests are saved to GZIP archives with the prefix local\_request\_log. The value of this property determines the size of the data to retain, per node. Specify 0 (the default) to disable completed request streaming. Completed request streaming is available in Couchbase Server 7.6.4 and later. Refer to [Stream Completed Requests](../n1ql/n1ql-manage/monitoring-n1ql-query.html#sys-history) for more information and examples.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Integer (int32)                             |
| **completed-threshold**optional     | A duration in milliseconds. All completed queries lasting longer than this threshold are logged in the completed requests catalog. Specify 0 to track all requests, independent of duration. Specify any negative number to track none. Refer to [Configure Completed Requests](../n1ql/n1ql-manage/monitoring-n1ql-query.html#sys-completed-config) for more information and examples. The [cluster-level](../n1ql-rest-settings/index.html#queryCompletedThreshold) queryCompletedThreshold setting specifies this property for the whole cluster. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. **Default:** 1000 **Example:** 7000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Integer (int32)                             |
| **controls**optional                | Specifies if there should be a controls section returned with the request results. When set to true, the query response document includes a controls section with runtime information provided along with the request, such as positional and named parameters or settings. NOTE: If the request qualifies for caching, these values will also be cached in the completed\_requests system keyspace. The [request-level](../n1ql-rest-query/index.html#controls%5Freq) controls parameter specifies this property per request. If a request does not include this parameter, the node-level controls setting will be used. **Default:** false **Example:** true                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Boolean                                     |
| **cpuprofile**optional              | The absolute path and filename to write the CPU profile to a local file. The output file includes a controls section and performance measurements, such as memory allocation and garbage collection, to pinpoint bottlenecks and ways to improve your code execution. NOTE: If cpuprofile is left running too long, it can slow the system down as its file size increases. To stop cpuprofile, run with the empty setting of "". **Default:** "" **Example:** "/tmp/info.txt"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | String                                      |
| **debug**optional                   | Use debug mode. When set to true, extra logging is provided. **Default:** false **Example:** true                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Boolean                                     |
| **distribute**optional              | This field is only available with the POST method. When specified alongside other settings, this field instructs the node that is processing the request to cascade those settings to all other query nodes. The actual value of this field is ignored. **Example:** true                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Boolean                                     |
| **functions-limit**optional         | Maximum number of user-defined functions. **Default:** 16384 **Example:** 7000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Integer (int32)                             |
| **keep-alive-length**optional       | Maximum size of buffered result. **Default:** 16384 **Example:** 7000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Integer (int32)                             |
| **loglevel**optional                | Log level used in the logger. All values, in descending order of data: DEBUG — For developers. Writes everything. TRACE — For developers. Less info than DEBUG. INFO — For admin & customers. Lists warnings & errors. WARN — For admin. Only abnormal items. ERROR — For admin. Only errors to be fixed. SEVERE — For admin. Major items, like crashes. NONE — Doesn't write anything. The [cluster-level](../n1ql-rest-settings/index.html#queryLogLevel) queryLogLevel setting specifies this property for the whole cluster. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. **Values:** "DEBUG", "TRACE", "INFO", "WARN", "ERROR", "SEVERE", "NONE" **Default:** "INFO" **Example:** "DEBUG"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | String                                      |
| **max-index-api**optional           | Max index API. This setting is provided for technical support only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Integer (int32)                             |
| **max-parallelism**optional         | Specifies the maximum parallelism for queries on this node. If the value is zero or negative, the maximum parallelism is restricted to the number of allowed cores. Similarly, if the value is greater than the number of allowed cores, the maximum parallelism is restricted to the number of allowed cores. (The number of allowed cores is the same as the number of logical CPUs. In Community Edition, the number of allowed cores cannot be greater than 4\. In Enterprise Edition, there is no limit to the number of allowed cores.) Refer to [Max Parallelism](../n1ql/n1ql-language-reference/index-partitioning.html#max-parallelism) for more information. The [cluster-level](../n1ql-rest-settings/index.html#queryMaxParallelism) queryMaxParallelism setting specifies this property for the whole cluster. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. In addition, there is a [request-level](../n1ql-rest-query/index.html#max%5Fparallelism%5Freq) max\_parallelism parameter. If a request includes this parameter, it will be capped by the node-level max-parallelism setting. NOTE: To enable queries to run in parallel, you must specify the cluster-level queryMaxParallelism parameter, or specify the node-level max-parallelism parameter on all Query nodes. **Default:** 1 **Example:** 0                                                                                                                                                                                                                                       | Integer (int32)                             |
| **memory-quota**optional            | Specifies the maximum amount of memory a request may use on this node, in MB. Specify 0 (the default value) to disable. When disabled, there is no quota. This parameter enforces a ceiling on the memory used for the tracked documents required for processing a request. It does not take into account any other memory that might be used to process a request, such as the stack, the operators, or some intermediate values. Within a transaction, this setting enforces the memory quota for the transaction by tracking the delta table and the transaction log (approximately). The [cluster-level](../n1ql-rest-settings/index.html#queryMemoryQuota) queryMemoryQuota setting specifies this property for the whole cluster. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. In addition, the [request-level](../n1ql-rest-query/index.html#memory%5Fquota%5Freq) memory\_quota parameter specifies this property per request. If a request includes this parameter, it will be capped by the node-level memory-quota setting. **Default:** 0 **Example:** 4                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Integer (int32)                             |
| **memprofile**optional              | Filename to write the diagnostic memory usage log. NOTE: If memprofile is left running too long, it can slow the system down as its file size increases. To stop memprofile, run with the empty setting of "". **Default:** "" **Example:** "/tmp/memory-usage.log"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | String                                      |
| **mutexprofile**optional            | Mutex profile. This setting is provided for technical support only. **Default:** false                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Boolean                                     |
| **n1ql-feat-ctrl**optional          | SQL++ feature control. This setting is provided for technical support only. The value may be an integer, or a string representing a hexadecimal number. The [cluster-level](../n1ql-rest-settings/index.html#queryN1QLFeatCtrl) queryN1QLFeatCtrl setting specifies this property for the whole cluster. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. **Default:** 76 **Example:** 16460                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Integer (int32)                             |
| **node-quota**optional              | Sets the soft memory limit for the Query service on this node, in MB. The garbage collector tries to keep below this target. It is not a hard, absolute limit, and memory usage may exceed this value. When set to 0 (the default), the Query service sets a default soft memory limit for the node. To do this, the Query service calculates the difference between the total system RAM and 90% of the total system RAM: Total System RAM - (0.9 \* Total System RAM) If the difference is greater than 8 GiB, the default soft memory limit is set to the total system RAM minus 8 GiB. If the difference is 8 GiB or less, the default soft memory limit is set to 90% of the total system RAM. The [cluster-level](../n1ql-rest-settings/index.html#queryNodeQuota) queryNodeQuota setting specifies this property for the whole cluster. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. **Default:** 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Integer (int32)                             |
| **node-quota-val-percent**optional  | The percentage of the node-quota that is dedicated to tracked value content memory across all active requests on this node. (The memory-quota setting specifies the maximum amount of document memory an individual request may use on this node.) The [cluster-level](../n1ql-rest-settings/index.html#queryNodeQuotaValPercent) queryNodeQuotaValPercent setting specifies this property for the whole cluster. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. **Default:** 67 **Minimum:** 0 **Maximum:** 100                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Integer (int32)                             |
| **num-cpus**optional                | The number of CPUs the Query service can use on this node. Note that this setting requires a restart of the Query service to take effect. When set to 0 (the default), the Query service can use all available CPUs, up to the limits described below. The number of CPUs can never be greater than the number of logical CPUs. In Community Edition, the number of allowed CPUs cannot be greater than 4\. In Enterprise Edition, there is no limit to the number of allowed CPUs. The [cluster-level](../n1ql-rest-settings/index.html#queryNumCpus) queryNumCpus setting specifies this property for the whole cluster. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. **Default:** 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Integer (int32)                             |
| **numatrs**optional                 | Specifies the total number of [active transaction records](/server/7.6/learn/data/transactions.html#active-transaction-record-entries). The [cluster-level](../n1ql-rest-settings/index.html#queryNumAtrs) queryNumAtrs setting specifies this property for the whole cluster. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | String                                      |
| **pipeline-batch**optional          | Controls the number of items execution operators can batch for Fetch from the KV. The [cluster-level](../n1ql-rest-settings/index.html#queryPipelineBatch) queryPipelineBatch setting specifies this property for the whole cluster. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. In addition, the [request-level](../n1ql-rest-query/index.html#pipeline%5Fbatch%5Freq) pipeline\_batch parameter specifies this property per request. The minimum of that and the node-level pipeline-batch setting is applied. **Default:** 16 **Example:** 64                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Integer (int32)                             |
| **pipeline-cap**optional            | Maximum number of items each execution operator can buffer between various operators. The [cluster-level](../n1ql-rest-settings/index.html#queryPipelineCap) queryPipelineCap setting specifies this property for the whole cluster. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. In addition, the [request-level](../n1ql-rest-query/index.html#pipeline%5Fcap%5Freq) pipeline\_cap parameter specifies this property per request. The minimum of that and the node-level pipeline-cap setting is applied. **Default:** 512 **Example:** 1024                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Integer (int32)                             |
| **plus-servicers**optional          | The number of service threads for transactions where the scan consistency is request\_plus or at\_plus. The default is 16 times the number of logical cores. **Example:** 16                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Integer (int32)                             |
| **prepared-limit**optional          | Maximum number of prepared statements in the cache. When this cache reaches the limit, the least recently used prepared statements will be discarded as new prepared statements are created. The [cluster-level](../n1ql-rest-settings/index.html#queryPreparedLimit) queryPreparedLimit setting specifies this property for the whole cluster. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. **Default:** 16384 **Example:** 65536                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Integer (int32)                             |
| **pretty**optional                  | Specifies whether query results are returned in pretty format. The [request-level](../n1ql-rest-query/index.html#pretty%5Freq) pretty parameter specifies this property per request. If a request does not include this parameter, the node-level setting is used, which defaults to false. **Default:** false **Example:** true                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Boolean                                     |
| **profile**optional                 | Specifies if there should be a profile section returned with the request results. The valid values are: off — No profiling information is added to the query response. phases — The query response includes a profile section with stats and details about various phases of the query plan and execution. Three phase times will be included in the system:active\_requests and system:completed\_requests monitoring keyspaces. timings — Besides the phase times, the profile section of the query response document will include a full query plan with timing and information about the number of processed documents at each phase. This information will be included in the system:active\_requests and system:completed\_requests keyspaces. NOTE: If profile is not set as one of the above values, then the profile setting does not change. Refer to [Monitoring and Profiling Details](../n1ql/n1ql-manage/monitoring-n1ql-query.html#monitor-profile-details) for more information and examples. The [request-level](../n1ql-rest-query/index.html#profile%5Freq) profile parameter specifies this property per request. If a request does not include this parameter, the node-level profile setting will be used. **Values:** "off", "phases", "timings" **Default:** "off" **Example:** "phases"                                                                                                                                                                                                                                                                                                                     | String                                      |
| **request-size-cap**optional        | Maximum size of a request. **Default:** 67108864 **Example:** 70000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Integer (int32)                             |
| **scan-cap**optional                | Maximum buffered channel size between the indexer client and the query service for index scans. This parameter controls when to use scan backfill. Use 0 or a negative number to disable. Smaller values reduce GC, while larger values reduce indexer backfill. The [cluster-level](../n1ql-rest-settings/index.html#queryScanCap) queryScanCap setting specifies this property for the whole cluster. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. In addition, the [request-level](../n1ql-rest-query/index.html#scan%5Fcap%5Freq) scan\_cap parameter specifies this property per request. The minimum of that and the node-level scan-cap setting is applied. **Default:** 512 **Example:** 1024                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Integer (int32)                             |
| **servicers**optional               | The number of service threads for the query. The default is 4 times the number of cores on the query node. **Default:** 32 **Example:** 8                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Integer (int32)                             |
| **timeout**optional                 | Maximum time to spend on the request before timing out (ns). The value for this setting is an integer, representing a duration in nanoseconds. It must not be delimited by quotes, and must not include a unit. Specify 0 (the default value) or a negative integer to disable. When disabled, no timeout is applied and the request runs for however long it takes. The [cluster-level](../n1ql-rest-settings/index.html#queryTimeout) queryTimeout setting specifies this property for the whole cluster. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. In addition, the [request-level](../n1ql-rest-query/index.html#timeout%5Freq) timeout parameter specifies this property per request. The minimum of that and the node-level timeout setting is applied. **Default:** 0 **Example:** 500000000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | Long (int64)                                |
| **txtimeout**optional               | Maximum time to spend on a transaction before timing out (ns). This setting only applies to requests containing the BEGIN TRANSACTION statement, or to requests where the [tximplicit](../n1ql-rest-query/index.html#tximplicit) parameter is set. For all other requests, it is ignored. The value for this setting is an integer, representing a duration in nanoseconds. It must not be delimited by quotes, and must not include a unit. Specify 0 (the default value) to disable. When disabled, no timeout is applied and the transaction runs for however long it takes. The [cluster-level](../n1ql-rest-settings/index.html#queryTxTimeout) queryTxTimeout setting specifies this property for the whole cluster. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. In addition, the [request-level](../n1ql-rest-query/index.html#txtimeout%5Freq) txtimeout parameter specifies this property per request. The minimum of that and the node-level txtimeout setting is applied. **Default:** 0 **Example:** 500000000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Long (int64)                                |
| **use-cbo**optional                 | Specifies whether the cost-based optimizer is enabled. The [cluster-level](../n1ql-rest-settings/index.html#queryUseCBO) queryUseCBO setting specifies this property for the whole cluster. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. In addition, the [request-level](../n1ql-rest-query/index.html#use%5Fcbo%5Freq) use\_cbo parameter specifies this property per request. If a request does not include this parameter, the node-level setting is used, which defaults to true. **Default:** true **Example:** false                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Boolean                                     |
| **use-replica**optional             | Specifies whether a query can fetch data from a replica vBucket if active vBuckets are inaccessible. The possible values are: off — read from replica is disabled for all queries and cannot be overridden at request level. on — read from replica is enabled for all queries, but can be disabled at request level. unset — read from replica is enabled or disabled at request level. Do not enable read from replica when you require consistent results. Only SELECT queries that are not within a transaction can read from replica. Reading from replica is only possible if the cluster uses Couchbase Server 7.6.0 or later. Note that KV range scans cannot currently be started on a replica vBucket. If a query uses sequential scan and a data node becomes unavailable, the query might return an error, even if read from replica is enabled for the request. The [cluster-level](../n1ql-rest-settings/index.html#queryUseReplica) queryUseReplica setting specifies the default for this property for the whole cluster. When you change the cluster-level setting, the node-level setting is overwritten for all nodes in the cluster. In addition, the [request-level](../n1ql-rest-query/index.html#use%5Freplica%5Freq) use\_replica parameter specifies this property per request. If a request does not include this parameter, or if the request-level parameter is unset, the node-level setting is used. If the request-level parameter and the node-level setting are both unset, read from replica is disabled for that request. **Values:** "off", "on", "unset" **Default:** "unset" **Example:** "on" | String                                      |

### [](#Statements)Prepared Statements

 Object

| Property                    |                                                                                                                                                                                                                                                                                                                                                                                                                     | Schema            |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| **encoded\_plan**required   | The full prepared statement in encoded format.                                                                                                                                                                                                                                                                                                                                                                      | String            |
| **featureControls**optional | This property is provided for technical support only. It is only returned when retrieving a specific prepared statement, not when retrieving all prepared statements.                                                                                                                                                                                                                                               | Integer           |
| **indexApiVersion**optional | This property is provided for technical support only. It is only returned when retrieving a specific prepared statement, not when retrieving all prepared statements.                                                                                                                                                                                                                                               | Integer           |
| **name**required            | The name of the prepared statement. This may be a UUID that was assigned automatically, or a name that was user-specified when the statement was created.                                                                                                                                                                                                                                                           | String            |
| **namespace**optional       | The namespace in which the prepared statement is stored. Currently, only the default namespace is available.                                                                                                                                                                                                                                                                                                        | String            |
| **node**optional            | The node on which the prepared statement is stored.                                                                                                                                                                                                                                                                                                                                                                 | String            |
| **statement**required       | The text of the query.                                                                                                                                                                                                                                                                                                                                                                                              | String            |
| **uses**required            | The count of times the prepared statement has been executed.                                                                                                                                                                                                                                                                                                                                                        | Integer           |
| **avgElapsedTime**optional  | The mean time taken from when the request to execute the prepared statement was acknowledged by the service, to when the request was completed. It includes the time taken by the service to schedule the request. This property is only returned when the prepared statement has been executed. It is only returned when retrieving a specific prepared statement, not when retrieving all prepared statements.    | String (duration) |
| **avgServiceTime**optional  | The mean amount of calendar time taken to complete the execution of the prepared statement. This property is only returned when the prepared statement has been executed. It is only returned when retrieving a specific prepared statement, not when retrieving all prepared statements.                                                                                                                           | String (duration) |
| **lastUse**optional         | Date and time of last use. This property is only returned when the prepared statement has been executed.                                                                                                                                                                                                                                                                                                            | Date (date-time)  |
| **maxElapsedTime**optional  | The maximum time taken from when the request to execute the prepared statement was acknowledged by the service, to when the request was completed. It includes the time taken by the service to schedule the request. This property is only returned when the prepared statement has been executed. It is only returned when retrieving a specific prepared statement, not when retrieving all prepared statements. | String (duration) |
| **maxServiceTime**optional  | The maximum amount of calendar time taken to complete the execution of the prepared statement. This property is only returned when the prepared statement has been executed. It is only returned when retrieving a specific prepared statement, not when retrieving all prepared statements.                                                                                                                        | String (duration) |
| **minElapsedTime**optional  | The minimum time taken from when the request to execute the prepared statement was acknowledged by the service, to when the request was completed. It includes the time taken by the service to schedule the request. This property is only returned when the prepared statement has been executed. It is only returned when retrieving a specific prepared statement, not when retrieving all prepared statements. | String (duration) |
| **minServiceTime**optional  | The minimum amount of calendar time taken to complete the execution of the prepared statement. This property is only returned when the prepared statement has been executed. It is only returned when retrieving a specific prepared statement, not when retrieving all prepared statements.                                                                                                                        | String (duration) |

### [](#Statistics)Statistics

 Object

| Property                                    |                                                                                                                                                                                                            | Schema     |
| ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| **active\_requests.count**optional          | Total number of active requests.                                                                                                                                                                           | Integer    |
| **at\_plus.count**optional                  | Total number of query requests with at\_plus index consistency.                                                                                                                                            | Integer    |
| **audit\_actions.count**optional            | The total number of audit records sent to the server. Some requests cause more than one audit record to be emitted. Records in the output queue that have not yet been sent to the server are not counted. | Integer    |
| **audit\_actions\_failed.count**optional    | The total number of audit records sent to the server that failed.                                                                                                                                          | Integer    |
| **audit\_requests\_filtered.count**optional | The number of potentially auditable requests that cause no audit action to be taken.                                                                                                                       | Integer    |
| **audit\_requests\_total.count**optional    | The total number of potentially auditable requests sent to the query engine.                                                                                                                               | Integer    |
| **cancelled.count**optional                 | Total number of cancelled requests.                                                                                                                                                                        | Integer    |
| **deletes.count**optional                   | Total number of DELETE operations.                                                                                                                                                                         | Integer    |
| **errors.count**optional                    | The total number of query errors returned so far.                                                                                                                                                          | Integer    |
| **index\_scans.count**optional              | Total number of secondary index scans.                                                                                                                                                                     | Integer    |
| **inserts.count**optional                   | Total number of INSERT operations.                                                                                                                                                                         | Integer    |
| **invalid\_requests.count**optional         | Total number of requests for unsupported endpoints.                                                                                                                                                        | Integer    |
| **mutations.count**optional                 | Total number of document mutations.                                                                                                                                                                        | Integer    |
| **prepared.count**optional                  | Total number of prepared statements executed.                                                                                                                                                              | Integer    |
| **primary\_scans.count**optional            | Total number of primary index scans.                                                                                                                                                                       | Integer    |
| **queued\_requests.count**optional          | Total number of queued requests.                                                                                                                                                                           | Integer    |
| **request\_time.count**optional             | Total end-to-end time to process all queries (ns).                                                                                                                                                         | Integer    |
| **request\_timer.15m.rate**optional         | Number of query requests processed per second. 15-minute exponentially weighted moving average.                                                                                                            | BigDecimal |
| **request\_timer.1m.rate**optional          | Number of query requests processed per second. 1-minute exponentially weighted moving average.                                                                                                             | BigDecimal |
| **request\_timer.5m.rate**optional          | Number of query requests processed per second. 5-minute exponentially weighted moving average.                                                                                                             | BigDecimal |
| **request\_timer.75%**optional              | End-to-end time to process a query (ns). The 75th percentile.                                                                                                                                              | BigDecimal |
| **request\_timer.95%**optional              | End-to-end time to process a query (ns). The 95th percentile.                                                                                                                                              | BigDecimal |
| **request\_timer.99%**optional              | End-to-end time to process a query (ns). The 99th percentile.                                                                                                                                              | BigDecimal |
| **request\_timer.99.9%**optional            | End-to-end time to process a query (ns). The 99.9th percentile.                                                                                                                                            | BigDecimal |
| **request\_timer.count**optional            | Total number of query requests.                                                                                                                                                                            | Integer    |
| **request\_timer.max**optional              | End-to-end time to process a query (ns). The maximum value.                                                                                                                                                | Integer    |
| **request\_timer.mean**optional             | End-to-end time to process a query (ns). The mean value.                                                                                                                                                   | BigDecimal |
| **request\_timer.mean.rate**optional        | Number of query requests processed per second. Mean rate since the query service started.                                                                                                                  | BigDecimal |
| **request\_timer.median**optional           | End-to-end time to process a query (ns). The median value.                                                                                                                                                 | BigDecimal |
| **request\_timer.min**optional              | End-to-end time to process a query (ns). The minimum value.                                                                                                                                                | Integer    |
| **request\_timer.stddev**optional           | End-to-end time to process a query (ns). The standard deviation.                                                                                                                                           | BigDecimal |
| **requests.count**optional                  | Total number of query requests.                                                                                                                                                                            | Integer    |
| **requests\_1000ms.count**optional          | Number of queries that take longer than 1000ms.                                                                                                                                                            | Integer    |
| **requests\_250ms.count**optional           | Number of queries that take longer than 250ms.                                                                                                                                                             | Integer    |
| **requests\_5000ms.count**optional          | Number of queries that take longer than 5000ms.                                                                                                                                                            | Integer    |
| **requests\_500ms.count**optional           | Number of queries that take longer than 500ms.                                                                                                                                                             | Integer    |
| **result\_count.count**optional             | Total number of results (documents) returned by the query engine.                                                                                                                                          | Integer    |
| **result\_size.count**optional              | Total size of data returned by the query engine (bytes).                                                                                                                                                   | Integer    |
| **scan\_plus.count**optional                | Total number of query requests with request\_plus index consistency.                                                                                                                                       | Integer    |
| **selects.count**optional                   | Total number of SELECT requests.                                                                                                                                                                           | Integer    |
| **service\_time.count**optional             | Time to execute all queries (ns).                                                                                                                                                                          | Integer    |
| **unbounded.count**optional                 | Total number of query requests with not\_bounded index consistency.                                                                                                                                        | Integer    |
| **updates.count**optional                   | Total number of UPDATE requests.                                                                                                                                                                           | Integer    |
| **warnings.count**optional                  | The total number of query warnings returned so far.                                                                                                                                                        | Integer    |

### [](#Vitals)Vital Statistics

 Object

| Property                               |                                                                                                                                                                                                    | Schema            |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| **bucket.IO.stats**optional            | The number of reads and retries for each bucket.                                                                                                                                                   | Object            |
| **uptime**optional                     | The uptime of the query engine.                                                                                                                                                                    | String (duration) |
| **local.time**optional                 | The local time of the query engine.                                                                                                                                                                | Date (date-time)  |
| **version**optional                    | The version of the query engine.                                                                                                                                                                   | String            |
| **total.threads**optional              | The number of active threads used by the query engine.                                                                                                                                             | Integer           |
| **cores**optional                      | The maximum number of logical cores available to the query engine.                                                                                                                                 | Integer           |
| **ffdc.total**optional                 | The total number of times FFDC has been invoked since the last restart.                                                                                                                            | Integer           |
| **gc.num**optional                     | The target heap size of the next garbage collection cycle.                                                                                                                                         | Long (int64)      |
| **gc.pause.time**optional              | The total time spent pausing for garbage collection since the query engine started (ns).                                                                                                           | String (duration) |
| **gc.pause.percent**optional           | The percentage of time spent pausing for garbage collection since the last time the statistics were checked.                                                                                       | Long (int64)      |
| **healthy**optional                    | False when either the unbounded or plus request queues are full; true otherwise.                                                                                                                   | Boolean           |
| **host.memory.free**optional           | Amount of free memory on the host.                                                                                                                                                                 | Long (int64)      |
| **host.memory.quota**optional          | The host memory quota. This reflects the node-quota setting.                                                                                                                                       | Long (int64)      |
| **host.memory.total**optional          | Total memory on the host.                                                                                                                                                                          | Long (int64)      |
| **host.memory.value\_quota**optional   | This the total document memory quota on the node.                                                                                                                                                  | Long (int64)      |
| **load**optional                       | A calculation for how busy the server is.                                                                                                                                                          | Integer           |
| **loadfactor**optional                 | The moving 15 minute average of the load calculation.                                                                                                                                              | Integer           |
| **memory.usage**optional               | The amount of memory allocated for heap objects (bytes). This increases as heap objects are allocated, and decreases as objects are freed.                                                         | Long (int64)      |
| **memory.total**optional               | The cumulative amount of memory allocated for heap objects (bytes). This increases as heap objects are allocated, but does not decrease when objects are freed.                                    | Long (int64)      |
| **memory.system**optional              | The total amount of memory obtained from the operating system (bytes). This measures the virtual address space reserved by the query engine for heaps, stacks, and other internal data structures. | Long (int64)      |
| **node**optional                       | The name or IP address and port of the node.                                                                                                                                                       | String            |
| **node.allocated.values**optional      | The total number of values allocated to contain documents or computations around documents. (This is only of relevance internally.)                                                                | Integer           |
| **node.memory.usage**optional          | The currently allocated document memory on the node.                                                                                                                                               | Integer           |
| **cpu.user.percent**optional           | CPU usage. The percentage of time spent executing user code since the last time the statistics were checked.                                                                                       | Long (int64)      |
| **cpu.sys.percent**optional            | CPU usage. The percentage of time spent executing system code since the last time the statistics were checked.                                                                                     | Long (int64)      |
| **process.memory.usage**optional       | Current process memory use.                                                                                                                                                                        | Integer           |
| **process.percore.cpupercent**optional | Average CPU usage per core.                                                                                                                                                                        | BigDecimal        |
| **process.rss**optional                | Process RSS (bytes)                                                                                                                                                                                | Integer           |
| **process.service.usage**optional      | The number of active servicers for the dominant workload — unbound queue servicers or plus queue servicers.                                                                                        | Integer           |
| **request.completed.count**optional    | Total number of completed requests.                                                                                                                                                                | Integer           |
| **request.active.count**optional       | Total number of active requests.                                                                                                                                                                   | Integer           |
| **request.per.sec.1min**optional       | Number of query requests processed per second. 1-minute exponentially weighted moving average.                                                                                                     | BigDecimal        |
| **request.per.sec.5min**optional       | Number of query requests processed per second. 5-minute exponentially weighted moving average.                                                                                                     | BigDecimal        |
| **request.per.sec.15min**optional      | Number of query requests processed per second. 15-minute exponentially weighted moving average.                                                                                                    | BigDecimal        |
| **request.queued.count**optional       | Number of queued requests.                                                                                                                                                                         | Integer           |
| **request.quota.used.hwm**optional     | High water mark for request quota use.                                                                                                                                                             | Integer           |
| **request\_time.mean**optional         | End-to-end time to process a query. The mean value.                                                                                                                                                | String (duration) |
| **request\_time.median**optional       | End-to-end time to process a query. The median value.                                                                                                                                              | String (duration) |
| **request\_time.80percentile**optional | End-to-end time to process a query. The 80th percentile.                                                                                                                                           | String (duration) |
| **request\_time.95percentile**optional | End-to-end time to process a query. The 95th percentile.                                                                                                                                           | String (duration) |
| **request\_time.99percentile**optional | End-to-end time to process a query. The 99th percentile.                                                                                                                                           | String (duration) |
| **request.prepared.percent**optional   | Percentage of requests that are prepared statements.                                                                                                                                               | Integer           |
| **servicers.paused.count**optional     | Number of servicers temporarily paused due to memory pressure. (Applies to serverless environments only.)                                                                                          | Integer           |
| **servicers.paused.total**optional     | Number of times servicers have been temporarily paused. (Applies to serverless environments only.)                                                                                                 | Integer           |
| **temp.hwm**optional                   | High water mark for temp space use directly by query. (Doesn't include use by the GSI and Search clients.)                                                                                         | Integer           |
| **temp.usage**optional                 | Current Query temp space use. (Doesn't include use by the GSI and Search clients.)                                                                                                                 | Integer           |

## [](#security)Security

### [](#security-Default)Default

The Admin API supports admin credentials. Credentials can be passed via HTTP headers (HTTP basic authentication).

**Type:** http

### [](#none)None

No authentication is required for the [Ping](#get%5Fping) or [Get Debug Variables](#get%5Fdebug%5Fvars) endpoints.

## [](#see-also)See Also

* For cluster-level settings, see the [Query Settings REST API](../n1ql-rest-settings/index.md#Settings).
* For request-level parameters, see the [Query Service REST API](../n1ql-rest-query/index.md#Request).