---
title: Admin REST API
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/n1ql/pages/n1ql-rest-api/admin.adoc
  xref: xref:7.2@server:n1ql:n1ql-rest-api/admin.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/n1ql/n1ql-rest-api/admin.html)

# Admin REST API

## [](#%5Foverview)Overview

The Admin REST API is a secondary API provided by the Query service. This API enables you to retrieve statistics about the clusters and nodes running the Query service; view or specify node-level settings; and view or delete requests.

The API schemes and host URLs are as follows:

* <http://node:8093/>
* <https://node:18093/> (for secure access)

where `node` is the host name or IP address of a computer running the Query service.

### [](#version-information)Version information

_Version_ : 7.2

### [](#tags)Tags

* configuration : Operations for cluster and node configuration.
* prepared statements : Operations for prepared statements.
* active requests : Operations for active requests.
* completed requests : Operations for completed requests.
* statistics : Operations for query statistics.
* settings : Operations for query settings.
* default : Other operations.

### [](#consumes)Consumes

* `application/x-www-form-urlencoded`
* `application/json`

### [](#produces)Produces

* `application/json`

## [](#%5Fpaths)Resources

This section describes the operations available with this REST API.

**Table of Contents**

* [Configuration](#%5Fconfiguration%5Fresource)
* [Prepared Statements](#%5Fprepared%5Fstatements%5Fresource)
* [Active Requests](#%5Factive%5Frequests%5Fresource)
* [Completed Requests](#%5Fcompleted%5Frequests%5Fresource)
* [Statistics](#%5Fstatistics%5Fresource)
* [Settings](#%5Fsettings%5Fresource)
* [Default](#%5Fdefault%5Fresource)

### [](#%5Fconfiguration%5Fresource)Configuration

Operations for cluster and node configuration.

* [Read All Clusters](#%5Fget%5Fclusters)
* [Read a Cluster](#%5Fget%5Fcluster)
* [Read All Nodes](#%5Fget%5Fnodes)
* [Read a Node](#%5Fget%5Fnode)
* [Read Configuration](#%5Fget%5Fconfig)

#### [](#%5Fget%5Fclusters)Read All Clusters

GET /admin/clusters

##### [](#description)Description

Returns information about all clusters.

##### [](#responses)Responses

| HTTP Code | Description                                                             | Schema                              |
| --------- | ----------------------------------------------------------------------- | ----------------------------------- |
| **200**   | An array of objects, each of which gives information about one cluster. | < [Clusters](#%5Fclusters) \> array |

##### [](#security)Security

| Type      | Name                       |
| --------- | -------------------------- |
| **basic** | **[Default](#%5Fdefault)** |

#### [](#%5Fget%5Fcluster)Read a Cluster

GET /admin/clusters/{cluster}

##### [](#description-2)Description

Returns information about the specified cluster.

##### [](#parameters)Parameters

| Type     | Name                   | Description            | Schema |
| -------- | ---------------------- | ---------------------- | ------ |
| **Path** | **cluster** _required_ | The name of a cluster. | string |

##### [](#responses-2)Responses

| HTTP Code | Description                                               | Schema                   |
| --------- | --------------------------------------------------------- | ------------------------ |
| **200**   | An object giving information about the specified cluster. | [Clusters](#%5Fclusters) |

##### [](#security-2)Security

| Type      | Name                       |
| --------- | -------------------------- |
| **basic** | **[Default](#%5Fdefault)** |

#### [](#%5Fget%5Fnodes)Read All Nodes

GET /admin/clusters/{cluster}/nodes

##### [](#description-3)Description

Returns information about all nodes in the specified cluster.

##### [](#parameters-2)Parameters

| Type     | Name                   | Description            | Schema |
| -------- | ---------------------- | ---------------------- | ------ |
| **Path** | **cluster** _required_ | The name of a cluster. | string |

##### [](#responses-3)Responses

| HTTP Code | Description                                                          | Schema                        |
| --------- | -------------------------------------------------------------------- | ----------------------------- |
| **200**   | An array of objects, each of which gives information about one node. | < [Nodes](#%5Fnodes) \> array |

##### [](#security-3)Security

| Type      | Name                       |
| --------- | -------------------------- |
| **basic** | **[Default](#%5Fdefault)** |

#### [](#%5Fget%5Fnode)Read a Node

GET /admin/clusters/{cluster}/nodes/{node}

##### [](#description-4)Description

Returns information about the specified node in the specified cluster.

##### [](#parameters-3)Parameters

| Type     | Name                   | Description            | Schema |
| -------- | ---------------------- | ---------------------- | ------ |
| **Path** | **cluster** _required_ | The name of a cluster. | string |
| **Path** | **node** _required_    | The name of a node.    | string |

##### [](#responses-4)Responses

| HTTP Code | Description                                            | Schema             |
| --------- | ------------------------------------------------------ | ------------------ |
| **200**   | An object giving information about the specified node. | [Nodes](#%5Fnodes) |

##### [](#security-4)Security

| Type      | Name                       |
| --------- | -------------------------- |
| **basic** | **[Default](#%5Fdefault)** |

#### [](#%5Fget%5Fconfig)Read Configuration

GET /admin/config

##### [](#description-5)Description

Returns the configuration of the query service on the cluster.

##### [](#responses-5)Responses

| HTTP Code | Description                                            | Schema             |
| --------- | ------------------------------------------------------ | ------------------ |
| **200**   | An object giving information about the specified node. | [Nodes](#%5Fnodes) |

##### [](#security-5)Security

| Type      | Name                       |
| --------- | -------------------------- |
| **basic** | **[Default](#%5Fdefault)** |

### [](#%5Fprepared%5Fstatements%5Fresource)Prepared Statements

Operations for prepared statements.

* [Retrieve All Prepared Statements](#%5Fget%5Fprepareds)
* [Retrieve a Prepared Statement](#%5Fget%5Fprepared)
* [Delete a Prepared Statement](#%5Fdelete%5Fprepared)
* [Retrieve Prepared Index Statements](#%5Fget%5Fprepared%5Findexes)

#### [](#%5Fget%5Fprepareds)Retrieve All Prepared Statements

GET /admin/prepareds

##### [](#description-6)Description

Returns all prepared statements.

> [!NOTE]
> Refer to [Get Prepared Statements](../../manage/monitor/monitoring-n1ql-query.md#sys-prepared-get) for examples.

##### [](#responses-6)Responses

| HTTP Code | Description                                                                           | Schema                                  |
| --------- | ------------------------------------------------------------------------------------- | --------------------------------------- |
| **200**   | An array of objects, each of which contains information about one prepared statement. | < [Statements](#%5Fstatements) \> array |

##### [](#security-6)Security

| Type      | Name                       |
| --------- | -------------------------- |
| **basic** | **[Default](#%5Fdefault)** |

#### [](#%5Fget%5Fprepared)Retrieve a Prepared Statement

GET /admin/prepareds/{name}

##### [](#description-7)Description

Returns the specified prepared statement.

> [!NOTE]
> Refer to [Get Prepared Statements](../../manage/monitor/monitoring-n1ql-query.md#sys-prepared-get) for examples.

##### [](#parameters-4)Parameters

| Type     | Name                | Description                                                                                                                                             | Schema |
| -------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **Path** | **name** _required_ | The name of a prepared statement. This may be a UUID that was assigned automatically, or a name that was user-specified when the statement was created. | string |

##### [](#responses-7)Responses

| HTTP Code | Description                                                              | Schema                       |
| --------- | ------------------------------------------------------------------------ | ---------------------------- |
| **200**   | An object containing information about the specified prepared statement. | [Statements](#%5Fstatements) |

##### [](#security-7)Security

| Type      | Name                       |
| --------- | -------------------------- |
| **basic** | **[Default](#%5Fdefault)** |

#### [](#%5Fdelete%5Fprepared)Delete a Prepared Statement

DELETE /admin/prepareds/{name}

##### [](#description-8)Description

Deletes the specified prepared statement.

> [!NOTE]
> Refer to [Delete Prepared Statements](../../manage/monitor/monitoring-n1ql-query.md#sys-prepared-delete) for examples.

##### [](#parameters-5)Parameters

| Type     | Name                | Description                                                                                                                                             | Schema |
| -------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **Path** | **name** _required_ | The name of a prepared statement. This may be a UUID that was assigned automatically, or a name that was user-specified when the statement was created. | string |

##### [](#responses-8)Responses

| HTTP Code | Description                                                            | Schema  |
| --------- | ---------------------------------------------------------------------- | ------- |
| **200**   | True if the prepared statement was successfully deleted.               | boolean |
| **500**   | Returns an error message if the prepared statement could not be found. | object  |

##### [](#security-8)Security

| Type      | Name                       |
| --------- | -------------------------- |
| **basic** | **[Default](#%5Fdefault)** |

#### [](#%5Fget%5Fprepared%5Findexes)Retrieve Prepared Index Statements

GET /admin/indexes/prepareds

##### [](#description-9)Description

Returns all prepared index statements.

> [!TIP]
> * Use [Retrieve a Prepared Statement](#%5Fget%5Fprepared) to get information about a prepared index statement.
> * Use [Delete a Prepared Statement](#%5Fdelete%5Fprepared) to delete a prepared index statement.

##### [](#responses-9)Responses

| HTTP Code | Description                                                                   | Schema           |
| --------- | ----------------------------------------------------------------------------- | ---------------- |
| **200**   | An array of strings, each of which is the name of a prepared index statement. | < string > array |

##### [](#security-9)Security

| Type      | Name                       |
| --------- | -------------------------- |
| **basic** | **[Default](#%5Fdefault)** |

### [](#%5Factive%5Frequests%5Fresource)Active Requests

Operations for active requests.

* [Retrieve All Active Requests](#%5Fget%5Factive%5Frequests)
* [Retrieve an Active Request](#%5Fget%5Factive%5Frequest)
* [Delete an Active Request](#%5Fdelete%5Factive%5Frequest)
* [Retrieve Active Index Requests](#%5Fget%5Factive%5Findexes)

#### [](#%5Fget%5Factive%5Frequests)Retrieve All Active Requests

GET /admin/active_requests

##### [](#description-10)Description

Returns all active query requests.

> [!NOTE]
> Refer to [Get Active Requests](../../manage/monitor/monitoring-n1ql-query.md#sys-active-get) for examples.

##### [](#responses-10)Responses

| HTTP Code | Description                                                                       | Schema                              |
| --------- | --------------------------------------------------------------------------------- | ----------------------------------- |
| **200**   | An array of objects, each of which contains information about one active request. | < [Requests](#%5Frequests) \> array |

##### [](#security-10)Security

| Type      | Name                       |
| --------- | -------------------------- |
| **basic** | **[Default](#%5Fdefault)** |

#### [](#%5Fget%5Factive%5Frequest)Retrieve an Active Request

GET /admin/active_requests/{request}

##### [](#description-11)Description

Returns the specified active query request.

> [!NOTE]
> Refer to [Get Active Requests](../../manage/monitor/monitoring-n1ql-query.md#sys-active-get) for examples.

##### [](#parameters-6)Parameters

| Type     | Name                   | Description                                                                                                  | Schema |
| -------- | ---------------------- | ------------------------------------------------------------------------------------------------------------ | ------ |
| **Path** | **request** _required_ | The name of a request. This is the requestID that was assigned automatically when the statement was created. | string |

##### [](#responses-11)Responses

| HTTP Code | Description                                                          | Schema                   |
| --------- | -------------------------------------------------------------------- | ------------------------ |
| **200**   | An object containing information about the specified active request. | [Requests](#%5Frequests) |

##### [](#security-11)Security

| Type      | Name                       |
| --------- | -------------------------- |
| **basic** | **[Default](#%5Fdefault)** |

#### [](#%5Fdelete%5Factive%5Frequest)Delete an Active Request

DELETE /admin/active_requests/{request}

##### [](#description-12)Description

Terminates the specified active query request.

> [!NOTE]
> Refer to [Terminate an Active Request](../../manage/monitor/monitoring-n1ql-query.md#sys-active-delete) for examples.

##### [](#parameters-7)Parameters

| Type     | Name                   | Description                                                                                                  | Schema |
| -------- | ---------------------- | ------------------------------------------------------------------------------------------------------------ | ------ |
| **Path** | **request** _required_ | The name of a request. This is the requestID that was assigned automatically when the statement was created. | string |

##### [](#responses-12)Responses

| HTTP Code | Description                                                        | Schema  |
| --------- | ------------------------------------------------------------------ | ------- |
| **200**   | True if the active request was successfully terminated.            | boolean |
| **500**   | Returns an error message if the active request could not be found. | object  |

##### [](#security-12)Security

| Type      | Name                       |
| --------- | -------------------------- |
| **basic** | **[Default](#%5Fdefault)** |

#### [](#%5Fget%5Factive%5Findexes)Retrieve Active Index Requests

GET /admin/indexes/active_requests

##### [](#description-13)Description

Returns all active index requests.

> [!TIP]
> * Use [Retrieve an Active Request](#%5Fget%5Factive%5Frequest) to get information about an active index request.
> * Use [Delete an Active Request](#%5Fdelete%5Factive%5Frequest) to terminate an active index request.

##### [](#responses-13)Responses

| HTTP Code | Description                                                                     | Schema           |
| --------- | ------------------------------------------------------------------------------- | ---------------- |
| **200**   | An array of strings, each of which is the requestID of an active index request. | < string > array |

##### [](#security-13)Security

| Type      | Name                       |
| --------- | -------------------------- |
| **basic** | **[Default](#%5Fdefault)** |

### [](#%5Fcompleted%5Frequests%5Fresource)Completed Requests

Operations for completed requests.

* [Retrieve All Completed Requests](#%5Fget%5Fcompleted%5Frequests)
* [Retrieve a Completed Request](#%5Fget%5Fcompleted%5Frequest)
* [Delete a Completed Request](#%5Fdelete%5Fcompleted%5Frequest)
* [Retrieve Completed Index Requests](#%5Fget%5Fcompleted%5Findexes)

#### [](#%5Fget%5Fcompleted%5Frequests)Retrieve All Completed Requests

GET /admin/completed_requests

##### [](#description-14)Description

Returns all completed requests.

> [!NOTE]
> Refer to [Get Completed Requests](../../manage/monitor/monitoring-n1ql-query.md#sys-completed-get) for examples.

##### [](#responses-14)Responses

| HTTP Code | Description                                                                          | Schema                              |
| --------- | ------------------------------------------------------------------------------------ | ----------------------------------- |
| **200**   | An array of objects, each of which contains information about one completed request. | < [Requests](#%5Frequests) \> array |

##### [](#security-14)Security

| Type      | Name                       |
| --------- | -------------------------- |
| **basic** | **[Default](#%5Fdefault)** |

#### [](#%5Fget%5Fcompleted%5Frequest)Retrieve a Completed Request

GET /admin/completed_requests/{request}

##### [](#description-15)Description

Returns the specified completed request.

> [!NOTE]
> Refer to [Get Completed Requests](../../manage/monitor/monitoring-n1ql-query.md#sys-completed-get) for examples.

##### [](#parameters-8)Parameters

| Type     | Name                   | Description                                                                                                  | Schema |
| -------- | ---------------------- | ------------------------------------------------------------------------------------------------------------ | ------ |
| **Path** | **request** _required_ | The name of a request. This is the requestID that was assigned automatically when the statement was created. | string |

##### [](#responses-15)Responses

| HTTP Code | Description                                                          | Schema                   |
| --------- | -------------------------------------------------------------------- | ------------------------ |
| **200**   | An object containing information about the specified active request. | [Requests](#%5Frequests) |

##### [](#security-15)Security

| Type      | Name                       |
| --------- | -------------------------- |
| **basic** | **[Default](#%5Fdefault)** |

#### [](#%5Fdelete%5Fcompleted%5Frequest)Delete a Completed Request

DELETE /admin/completed_requests/{request}

##### [](#description-16)Description

Purges the specified completed request.

> [!NOTE]
> Refer to [Purge the Completed Requests](../../manage/monitor/monitoring-n1ql-query.md#sys-completed-delete) for examples.

##### [](#parameters-9)Parameters

| Type     | Name                   | Description                                                                                                  | Schema |
| -------- | ---------------------- | ------------------------------------------------------------------------------------------------------------ | ------ |
| **Path** | **request** _required_ | The name of a request. This is the requestID that was assigned automatically when the statement was created. | string |

##### [](#responses-16)Responses

| HTTP Code | Description                                                           | Schema  |
| --------- | --------------------------------------------------------------------- | ------- |
| **200**   | True if the completed request was successfully purged.                | boolean |
| **500**   | Returns an error message if the completed request could not be found. | object  |

##### [](#security-16)Security

| Type      | Name                       |
| --------- | -------------------------- |
| **basic** | **[Default](#%5Fdefault)** |

#### [](#%5Fget%5Fcompleted%5Findexes)Retrieve Completed Index Requests

GET /admin/indexes/completed_requests

##### [](#description-17)Description

Returns all completed index requests.

> [!TIP]
> * Use [Retrieve a Completed Request](#%5Fget%5Fcompleted%5Frequest) to get information about a completed index request.
> * Use [Delete a Completed Request](#%5Fdelete%5Fcompleted%5Frequest) to purge a completed index request.

##### [](#responses-17)Responses

| HTTP Code | Description                                                                       | Schema           |
| --------- | --------------------------------------------------------------------------------- | ---------------- |
| **200**   | An array of strings, each of which is the requestID of a completed index request. | < string > array |

##### [](#security-17)Security

| Type      | Name                       |
| --------- | -------------------------- |
| **basic** | **[Default](#%5Fdefault)** |

### [](#%5Fstatistics%5Fresource)Statistics

Operations for query statistics.

* [Retrieve Vitals](#%5Fget%5Fvitals)
* [Retrieve All Statistics](#%5Fget%5Fstats)
* [Retrieve a Statistic](#%5Fget%5Fstat)
* [Get Debug Variables](#%5Fget%5Fdebug%5Fvars)

#### [](#%5Fget%5Fvitals)Retrieve Vitals

GET /admin/vitals

##### [](#description-18)Description

Returns data about the running state and health of the query engine. This information can be very useful to assess the current workload and performance characteristics of a query engine, and hence load-balance the requests being sent to various query engines.

> [!NOTE]
> Refer to [Get System Vitals](../../manage/monitor/monitoring-n1ql-query.md#vitals) for examples.

##### [](#responses-18)Responses

| HTTP Code | Description                                | Schema               |
| --------- | ------------------------------------------ | -------------------- |
| **200**   | An object containing all vital statistics. | [Vitals](#%5Fvitals) |

##### [](#security-18)Security

| Type      | Name                       |
| --------- | -------------------------- |
| **basic** | **[Default](#%5Fdefault)** |

#### [](#%5Fget%5Fstats)Retrieve All Statistics

GET /admin/stats

##### [](#description-19)Description

Returns all statistics.

##### [](#responses-19)Responses

| HTTP Code | Description                                                                                                                                                  | Schema                       |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------- |
| **200**   | An object containing all statistics. Each statistic consists of a top-level statistic name and a metric name. Each statistic has a different set of metrics. | [Statistics](#%5Fstatistics) |

##### [](#security-19)Security

| Type      | Name                       |
| --------- | -------------------------- |
| **basic** | **[Default](#%5Fdefault)** |

#### [](#%5Fget%5Fstat)Retrieve a Statistic

GET /admin/stats/{stat}

##### [](#description-20)Description

Returns the specified statistic.

##### [](#parameters-10)Parameters

| Type     | Name                | Description                                                                                       | Schema                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| -------- | ------------------- | ------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Path** | **stat** _required_ | The name of a statistic. Only top-level statistic names can be used. You cannot specify a metric. | enum (active\_requests, at\_plus, audit\_actions, audit\_actions\_failed, audit\_requests\_filtered, audit\_requests\_total, cancelled, deletes, errors, index\_scans, inserts, invalid\_requests, mutations, prepared, primary\_scans, queued\_requests, request\_time, request\_timer, requests, requests\_1000ms, requests\_250ms, requests\_5000ms, requests\_500ms, result\_count, result\_size, scan\_plus, selects, service\_time, unbounded, updates, warnings) |

##### [](#responses-20)Responses

| HTTP Code | Description                                                                                                  | Schema                 |
| --------- | ------------------------------------------------------------------------------------------------------------ | ---------------------- |
| **200**   | An object containing all metrics for the specified statistic. Each statistic has a different set of metrics. | [Metrics](#%5Fmetrics) |

##### [](#security-20)Security

| Type      | Name                       |
| --------- | -------------------------- |
| **basic** | **[Default](#%5Fdefault)** |

#### [](#%5Fget%5Fdebug%5Fvars)Get Debug Variables

GET /debug/vars

##### [](#description-21)Description

Currently unused.

##### [](#responses-21)Responses

| HTTP Code | Description                                                           | Schema    |
| --------- | --------------------------------------------------------------------- | --------- |
| **302**   | Redirects to the [Retrieve All Statistics](#%5Fget%5Fstats) endpoint. | text/html |

##### [](#produces-2)Produces

* `text/html`

##### [](#security-21)Security

| Type      | Name                 |
| --------- | -------------------- |
| **basic** | **[None](#%5Fnone)** |

##### [](#example-http-response)Example HTTP response

Response 302

```html
<a href="/admin/stats">Found</a>.
```

### [](#%5Fsettings%5Fresource)Settings

Operations for query settings.

* [Retrieve Node-Level Query Settings](#%5Fget%5Fsettings)
* [Update Node-Level Query Settings](#%5Fpost%5Fsettings)

#### [](#%5Fget%5Fsettings)Retrieve Node-Level Query Settings

GET /admin/settings

##### [](#description-22)Description

Returns node-level query settings.

> [!NOTE]
> Refer to [Query Settings](../../settings/query-settings.md) for more information.

##### [](#responses-22)Responses

| HTTP Code | Description                                 | Schema                   |
| --------- | ------------------------------------------- | ------------------------ |
| **200**   | An object giving node-level query settings. | [Settings](#%5Fsettings) |

##### [](#security-22)Security

| Type      | Name                       |
| --------- | -------------------------- |
| **basic** | **[Default](#%5Fdefault)** |

#### [](#%5Fpost%5Fsettings)Update Node-Level Query Settings

POST /admin/settings

##### [](#description-23)Description

Updates node-level query settings.

> [!NOTE]
> Refer to [Query Settings](../../settings/query-settings.md) for more information.

##### [](#parameters-11)Parameters

| Type     | Name                    | Description                                     | Schema                   |
| -------- | ----------------------- | ----------------------------------------------- | ------------------------ |
| **Body** | **Settings** _optional_ | An object specifying node-level query settings. | [Settings](#%5Fsettings) |

##### [](#responses-23)Responses

| HTTP Code | Description                                                               | Schema                   |
| --------- | ------------------------------------------------------------------------- | ------------------------ |
| **200**   | An object giving node-level query settings, including the latest changes. | [Settings](#%5Fsettings) |

##### [](#security-23)Security

| Type      | Name                       |
| --------- | -------------------------- |
| **basic** | **[Default](#%5Fdefault)** |

### [](#%5Fdefault%5Fresource)Default

Other operations.

* [Ping](#%5Fget%5Fping)

#### [](#%5Fget%5Fping)Ping

GET /admin/ping

##### [](#description-24)Description

Returns a minimal response, indicating that the service is running and reachable.

##### [](#responses-24)Responses

| HTTP Code | Description      | Schema |
| --------- | ---------------- | ------ |
| **200**   | An empty object. | object |

##### [](#security-24)Security

| Type      | Name                 |
| --------- | -------------------- |
| **basic** | **[None](#%5Fnone)** |

##### [](#example-http-response-2)Example HTTP response

Response 200

```json
{}
```

## [](#%5Fdefinitions)Definitions

This section describes the properties consumed and returned by this REST API.

**Table of Contents**

* [Clusters](#%5Fclusters)
* [Nodes](#%5Fnodes)
* [Requests](#%5Frequests)
* [Statements](#%5Fstatements)
* [Vitals](#%5Fvitals)
* [Statistics](#%5Fstatistics)
* [Metrics](#%5Fmetrics)
* [Settings](#%5Fsettings)

### [](#%5Fclusters)Clusters

| Name                        | Description                  | Schema |
| --------------------------- | ---------------------------- | ------ |
| **accountstore** _optional_ | The URL of the accountstore. | string |
| **configstore** _optional_  | The URL of the configstore.  | string |
| **datastore** _optional_    | The URL of the datastore.    | string |
| **name** _optional_         | The name of the cluster.     | string |
| **version** _optional_      |                              | string |

### [](#%5Fnodes)Nodes

| Name                         | Description                                 | Schema |
| ---------------------------- | ------------------------------------------- | ------ |
| **adminEndpoint** _optional_ | The HTTP URL of the admin endpoint.         | string |
| **adminSecure** _optional_   | The HTTPS URL of the admin endpoint.        | string |
| **cluster** _optional_       | The name of the cluster.                    | string |
| **name** _optional_          | The URL of the node, including port number. | string |
| **options** _optional_       |                                             | string |
| **queryEndpoint** _optional_ | The HTTP URL of the query endpoint.         | string |
| **querySecure** _optional_   | The HTTPS URL of the query endpoint.        | string |

### [](#%5Frequests)Requests

| Name                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Schema             |
| ------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| **clientContextID** _optional_ | The opaque ID or context provided by the client. Refer to the [request-level](index.md#client%5Fcontext%5Fid) client\_context\_id parameter for more information.                                                                                                                                                                                                                                                                                                                 | string             |
| **elapsedTime** _optional_     | The time taken from when the request was acknowledged by the service to when the request was completed. It includes the time taken by the service to schedule the request.                                                                                                                                                                                                                                                                                                        | string (duration)  |
| **errorCount** _optional_      | Total number of errors encountered while executing the query.                                                                                                                                                                                                                                                                                                                                                                                                                     | integer            |
| **memoryQuota** _optional_     | The memory quota for the request, in MB. This property is only returned if a memory quota is set for the query.                                                                                                                                                                                                                                                                                                                                                                   | integer            |
| **node** _optional_            | IP address and port number of the node where the query is executed.                                                                                                                                                                                                                                                                                                                                                                                                               | string             |
| **phaseCounts** _optional_     | Count of documents processed at selective phases involved in the query execution. Refer to [Attribute Profile in Query Response](../../manage/monitor/monitoring-n1ql-query.md#profile) for more details and examples.                                                                                                                                                                                                                                                            | object             |
| **phaseOperators** _optional_  | Indicates the number of each kind of query operators involved in different phases of the query processing. Refer to [Attribute Profile in Query Response](../../manage/monitor/monitoring-n1ql-query.md#profile) for more details and examples.                                                                                                                                                                                                                                   | object             |
| **phaseTimes** _optional_      | Cumulative execution times for various phases involved in the query execution. Refer to [Attribute Profile in Query Response](../../manage/monitor/monitoring-n1ql-query.md#profile) for more details and examples.                                                                                                                                                                                                                                                               | object             |
| **remoteAddr** _optional_      | IP address and port number of the client application, from where the query is received.                                                                                                                                                                                                                                                                                                                                                                                           | string             |
| **requestId** _optional_       | Unique request ID internally generated for the query.                                                                                                                                                                                                                                                                                                                                                                                                                             | string (uuid)      |
| **requestTime** _optional_     | Timestamp when the query is received.                                                                                                                                                                                                                                                                                                                                                                                                                                             | string (date-time) |
| **resultCount** _optional_     | Total number of documents returned in the query result.                                                                                                                                                                                                                                                                                                                                                                                                                           | integer            |
| **resultSize** _optional_      | Total number of bytes returned in the query result.                                                                                                                                                                                                                                                                                                                                                                                                                               | integer            |
| **scanConsistency** _optional_ | The value of the query setting Scan Consistency used for the query.                                                                                                                                                                                                                                                                                                                                                                                                               | string             |
| **serviceTime** _optional_     | Total amount of calendar time taken to complete the query.                                                                                                                                                                                                                                                                                                                                                                                                                        | string (duration)  |
| **state** _optional_           | The state of the query execution, such as completed, running, cancelled. Note that the completed state means that the request was started and completed by the Query service, but it does not mean that it was necessarily successful. The request could have been successful, or completed with errors. To find requests that were successful, use this field in conjunction with the errorCount field: search for requests whose state is completed and whose error count is 0. | string             |
| **statement** _optional_       | The query statement being executed.                                                                                                                                                                                                                                                                                                                                                                                                                                               | string             |
| **useCBO** _optional_          | Whether the cost-based optimizer is enabled for the query.                                                                                                                                                                                                                                                                                                                                                                                                                        | boolean            |
| **usedMemory** _optional_      | The amount of document memory used to execute the request. This property is only returned if a memory quota is set for the query.                                                                                                                                                                                                                                                                                                                                                 | integer            |
| **userAgent** _optional_       | Name of the client application or program that issued the query.                                                                                                                                                                                                                                                                                                                                                                                                                  | string             |
| **users** _optional_           | Username with whose privileges the query is run.                                                                                                                                                                                                                                                                                                                                                                                                                                  | string             |

### [](#%5Fstatements)Statements

| Name                           | Description                                                                                                                                                                                                                                                                                                                                                                                                         | Schema             |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| **avgElapsedTime** _optional_  | The mean time taken from when the request to execute the prepared statement was acknowledged by the service, to when the request was completed. It includes the time taken by the service to schedule the request. This property is only returned when the prepared statement has been executed. It is only returned when retrieving a specific prepared statement, not when retrieving all prepared statements.    | string (duration)  |
| **avgServiceTime** _optional_  | The mean amount of calendar time taken to complete the execution of the prepared statement. This property is only returned when the prepared statement has been executed. It is only returned when retrieving a specific prepared statement, not when retrieving all prepared statements.                                                                                                                           | string (duration)  |
| **encoded\_plan** _required_   | The full prepared statement in encoded format.                                                                                                                                                                                                                                                                                                                                                                      | string             |
| **featureControls** _optional_ | This property is provided for technical support only. It is only returned when retrieving a specific prepared statement, not when retrieving all prepared statements.                                                                                                                                                                                                                                               | integer            |
| **indexApiVersion** _optional_ | This property is provided for technical support only. It is only returned when retrieving a specific prepared statement, not when retrieving all prepared statements.                                                                                                                                                                                                                                               | integer            |
| **lastUse** _optional_         | Date and time of last use. This property is only returned when the prepared statement has been executed.                                                                                                                                                                                                                                                                                                            | string (date-time) |
| **maxElapsedTime** _optional_  | The maximum time taken from when the request to execute the prepared statement was acknowledged by the service, to when the request was completed. It includes the time taken by the service to schedule the request. This property is only returned when the prepared statement has been executed. It is only returned when retrieving a specific prepared statement, not when retrieving all prepared statements. | string (duration)  |
| **maxServiceTime** _optional_  | The maximum amount of calendar time taken to complete the execution of the prepared statement. This property is only returned when the prepared statement has been executed. It is only returned when retrieving a specific prepared statement, not when retrieving all prepared statements.                                                                                                                        | string (duration)  |
| **minElapsedTime** _optional_  | The minimum time taken from when the request to execute the prepared statement was acknowledged by the service, to when the request was completed. It includes the time taken by the service to schedule the request. This property is only returned when the prepared statement has been executed. It is only returned when retrieving a specific prepared statement, not when retrieving all prepared statements. | string (duration)  |
| **minServiceTime** _optional_  | The minimum amount of calendar time taken to complete the execution of the prepared statement. This property is only returned when the prepared statement has been executed. It is only returned when retrieving a specific prepared statement, not when retrieving all prepared statements.                                                                                                                        | string (duration)  |
| **name** _required_            | The name of the prepared statement. This may be a UUID that was assigned automatically, or a name that was user-specified when the statement was created.                                                                                                                                                                                                                                                           | string             |
| **statement** _required_       | The text of the query.                                                                                                                                                                                                                                                                                                                                                                                              | string             |
| **uses** _required_            | The count of times the prepared statement has been executed.                                                                                                                                                                                                                                                                                                                                                        | integer            |

### [](#%5Fvitals)Vitals

| Name                                      | Description                                                                                                                                                                                        | Schema             |
| ----------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ |
| **cores** _optional_                      | The maximum number of logical cores available to the query engine.                                                                                                                                 | integer            |
| **cpu.sys.percent** _optional_            | CPU usage. The percentage of time spent executing system code since the last time the statistics were checked.                                                                                     | integer (int64)    |
| **cpu.user.percent** _optional_           | CPU usage. The percentage of time spent executing user code since the last time the statistics were checked.                                                                                       | integer (int64)    |
| **gc.num** _optional_                     | The target heap size of the next garbage collection cycle.                                                                                                                                         | integer (int64)    |
| **gc.pause.percent** _optional_           | The percentage of time spent pausing for garbage collection since the last time the statistics were checked.                                                                                       | integer (int64)    |
| **gc.pause.time** _optional_              | The total time spent pausing for garbage collection since the query engine started (ns).                                                                                                           | string (duration)  |
| **local.time** _optional_                 | The local time of the query engine.                                                                                                                                                                | string (date-time) |
| **memory.system** _optional_              | The total amount of memory obtained from the operating system (bytes). This measures the virtual address space reserved by the query engine for heaps, stacks, and other internal data structures. | integer (int64)    |
| **memory.total** _optional_               | The cumulative amount of memory allocated for heap objects (bytes). This increases as heap objects are allocated, but does not decrease when objects are freed.                                    | integer (int64)    |
| **memory.usage** _optional_               | The amount of memory allocated for heap objects (bytes). This increases as heap objects are allocated, and decreases as objects are freed.                                                         | integer (int64)    |
| **request.active.count** _optional_       | Total number of active requests.                                                                                                                                                                   | integer            |
| **request.completed.count** _optional_    | Total number of completed requests.                                                                                                                                                                | integer            |
| **request.per.sec.15min** _optional_      | Number of query requests processed per second. 15-minute exponentially weighted moving average.                                                                                                    | number             |
| **request.per.sec.1min** _optional_       | Number of query requests processed per second. 1-minute exponentially weighted moving average.                                                                                                     | number             |
| **request.per.sec.5min** _optional_       | Number of query requests processed per second. 5-minute exponentially weighted moving average.                                                                                                     | number             |
| **request.prepared.percent** _optional_   | Percentage of requests that are prepared statements.                                                                                                                                               | integer            |
| **request\_time.80percentile** _optional_ | End-to-end time to process a query. The 80th percentile.                                                                                                                                           | string (duration)  |
| **request\_time.95percentile** _optional_ | End-to-end time to process a query. The 95th percentile.                                                                                                                                           | string (duration)  |
| **request\_time.99percentile** _optional_ | End-to-end time to process a query. The 99th percentile.                                                                                                                                           | string (duration)  |
| **request\_time.mean** _optional_         | End-to-end time to process a query. The mean value.                                                                                                                                                | string (duration)  |
| **request\_time.median** _optional_       | End-to-end time to process a query. The median value.                                                                                                                                              | string (duration)  |
| **total.threads** _optional_              | The number of active threads used by the query engine.                                                                                                                                             | integer            |
| **uptime** _optional_                     | The uptime of the query engine.                                                                                                                                                                    | string (duration)  |
| **version** _optional_                    | The version of the query engine.                                                                                                                                                                   | string             |

### [](#%5Fstatistics)Statistics

| Name                                           | Description                                                                                                                                                                                                | Schema  |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| **active\_requests.count** _optional_          | Total number of active requests.                                                                                                                                                                           | integer |
| **at\_plus.count** _optional_                  | Total number of query requests with at\_plus index consistency.                                                                                                                                            | integer |
| **audit\_actions.count** _optional_            | The total number of audit records sent to the server. Some requests cause more than one audit record to be emitted. Records in the output queue that have not yet been sent to the server are not counted. | integer |
| **audit\_actions\_failed.count** _optional_    | The total number of audit records sent to the server that failed.                                                                                                                                          | integer |
| **audit\_requests\_filtered.count** _optional_ | The number of potentially auditable requests that cause no audit action to be taken.                                                                                                                       | integer |
| **audit\_requests\_total.count** _optional_    | The total number of potentially auditable requests sent to the query engine.                                                                                                                               | integer |
| **cancelled.count** _optional_                 | Total number of cancelled requests.                                                                                                                                                                        | integer |
| **deletes.count** _optional_                   | Total number of DELETE operations.                                                                                                                                                                         | integer |
| **errors.count** _optional_                    | The total number of query errors returned so far.                                                                                                                                                          | integer |
| **index\_scans.count** _optional_              | Total number of secondary index scans.                                                                                                                                                                     | integer |
| **inserts.count** _optional_                   | Total number of INSERT operations.                                                                                                                                                                         | integer |
| **invalid\_requests.count** _optional_         | Total number of requests for unsupported endpoints.                                                                                                                                                        | integer |
| **mutations.count** _optional_                 | Total number of document mutations.                                                                                                                                                                        | integer |
| **prepared.count** _optional_                  | Total number of prepared statements executed.                                                                                                                                                              | integer |
| **primary\_scans.count** _optional_            | Total number of primary index scans.                                                                                                                                                                       | integer |
| **queued\_requests.count** _optional_          | Total number of queued requests.                                                                                                                                                                           | integer |
| **request\_time.count** _optional_             | Total end-to-end time to process all queries (ns).                                                                                                                                                         | integer |
| **request\_timer.15m.rate** _optional_         | Number of query requests processed per second. 15-minute exponentially weighted moving average.                                                                                                            | number  |
| **request\_timer.1m.rate** _optional_          | Number of query requests processed per second. 1-minute exponentially weighted moving average.                                                                                                             | number  |
| **request\_timer.5m.rate** _optional_          | Number of query requests processed per second. 5-minute exponentially weighted moving average.                                                                                                             | number  |
| **request\_timer.75%** _optional_              | End-to-end time to process a query (ns). The 75th percentile.                                                                                                                                              | number  |
| **request\_timer.95%** _optional_              | End-to-end time to process a query (ns). The 95th percentile.                                                                                                                                              | number  |
| **request\_timer.99%** _optional_              | End-to-end time to process a query (ns). The 99th percentile.                                                                                                                                              | number  |
| **request\_timer.99.9%** _optional_            | End-to-end time to process a query (ns). The 99.9th percentile.                                                                                                                                            | number  |
| **request\_timer.count** _optional_            | Total number of query requests.                                                                                                                                                                            | integer |
| **request\_timer.max** _optional_              | End-to-end time to process a query (ns). The maximum value.                                                                                                                                                | integer |
| **request\_timer.mean** _optional_             | End-to-end time to process a query (ns). The mean value.                                                                                                                                                   | number  |
| **request\_timer.mean.rate** _optional_        | Number of query requests processed per second. Mean rate since the query service started.                                                                                                                  | number  |
| **request\_timer.median** _optional_           | End-to-end time to process a query (ns). The median value.                                                                                                                                                 | number  |
| **request\_timer.min** _optional_              | End-to-end time to process a query (ns). The minimum value.                                                                                                                                                | integer |
| **request\_timer.stddev** _optional_           | End-to-end time to process a query (ns). The standard deviation.                                                                                                                                           | number  |
| **requests.count** _optional_                  | Total number of query requests.                                                                                                                                                                            | integer |
| **requests\_1000ms.count** _optional_          | Number of queries that take longer than 1000ms.                                                                                                                                                            | integer |
| **requests\_250ms.count** _optional_           | Number of queries that take longer than 250ms.                                                                                                                                                             | integer |
| **requests\_5000ms.count** _optional_          | Number of queries that take longer than 5000ms.                                                                                                                                                            | integer |
| **requests\_500ms.count** _optional_           | Number of queries that take longer than 500ms.                                                                                                                                                             | integer |
| **result\_count.count** _optional_             | Total number of results (documents) returned by the query engine.                                                                                                                                          | integer |
| **result\_size.count** _optional_              | Total size of data returned by the query engine (bytes).                                                                                                                                                   | integer |
| **scan\_plus.count** _optional_                | Total number of query requests with request\_plus index consistency.                                                                                                                                       | integer |
| **selects.count** _optional_                   | Total number of SELECT requests.                                                                                                                                                                           | integer |
| **service\_time.count** _optional_             | Time to execute all queries (ns).                                                                                                                                                                          | integer |
| **unbounded.count** _optional_                 | Total number of query requests with not\_bounded index consistency.                                                                                                                                        | integer |
| **updates.count** _optional_                   | Total number of UPDATE requests.                                                                                                                                                                           | integer |
| **warnings.count** _optional_                  | The total number of query warnings returned so far.                                                                                                                                                        | integer |

### [](#%5Fmetrics)Metrics

| Name                     | Description                                       | Schema  |
| ------------------------ | ------------------------------------------------- | ------- |
| **15m.rate** _optional_  | 15-minute exponentially weighted moving average.  | number  |
| **1m.rate** _optional_   | 1-minute exponentially weighted moving average.   | number  |
| **5m.rate** _optional_   | 5-minute exponentially weighted moving average.   | number  |
| **75%** _optional_       | The 75th percentile.                              | number  |
| **95%** _optional_       | The 95th percentile.                              | number  |
| **99%** _optional_       | The 99th percentile.                              | number  |
| **99.9%** _optional_     | The 99.9th percentile.                            | number  |
| **count** _optional_     | A single value that represents the current state. | integer |
| **max** _optional_       | The maximum value.                                | integer |
| **mean** _optional_      | The mean value.                                   | number  |
| **mean.rate** _optional_ | Mean rate since the query service started.        | number  |
| **median** _optional_    | The median value.                                 | number  |
| **min** _optional_       | The minimum value.                                | integer |
| **stddev** _optional_    | The standard deviation.                           | number  |

### [](#%5Fsettings)Settings

| Name                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Schema                                               |
| ------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| **atrcollection** _optional_         | Specifies the collection where [active transaction records](../../learn/data/transactions.md#additional-storage-use) are stored. The collection must be present. If not specified, the active transaction record is stored in the default collection in the default scope in the bucket containing the first mutated document within the transaction. The value must be a string in the form "bucket.scope.collection" or "namespace:bucket.scope.collection". If any part of the path contains a special character, that part of the path must be delimited in backticks \`\`. The [request-level](index.md#atrcollection%5Freq) atrcollection parameter specifies this property per request. If a request does not include this parameter, the node-level atrcollection setting will be used. **Default** : "" **Example** : "default:\`travel-sample\`.transaction.test"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | string                                               |
| **auto-prepare** _optional_          | Specifies whether the query engine should create a prepared statement every time a N1QL request is submitted, whether the PREPARE statement is included or not. Refer to [Auto-Prepare](../n1ql-language-reference/prepare.md#auto-prepare) for more information. **Default** : false **Example** : true                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | boolean                                              |
| **cleanupclientattempts** _optional_ | When enabled, the Query service preferentially aims to clean up just transactions that it has created, leaving transactions for the distributed cleanup process only when it is forced to. The [cluster-level](../../rest-api/rest-cluster-query-settings.md#queryCleanupClientAttempts) queryCleanupClientAttempts setting specifies this property for the whole cluster. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. **Default** : true **Example** : false                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | boolean                                              |
| **cleanuplostattempts** _optional_   | When enabled, the Query service takes part in the distributed cleanup process, and cleans up expired transactions created by any client. The [cluster-level](../../rest-api/rest-cluster-query-settings.md#queryCleanupLostAttempts) queryCleanupLostAttempts setting specifies this property for the whole cluster. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. **Default** : true **Example** : false                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | boolean                                              |
| **cleanupwindow** _optional_         | Specifies how frequently the Query service checks its subset of [active transaction records](../../learn/data/transactions.md#additional-storage-use) for cleanup. Decreasing this setting causes expiration transactions to be found more swiftly, with the tradeoff of increasing the number of reads per second used for the scanning process. The value for this setting is a string. Its format includes an amount and a mandatory unit, e.g. 10ms (10 milliseconds) or 0.5s (half a second). Valid units are: ns (nanoseconds) us (microseconds) ms (milliseconds) s (seconds) m (minutes) h (hours) The [cluster-level](../../rest-api/rest-cluster-query-settings.md#queryCleanupWindow) queryCleanupWindow setting specifies this property for the whole cluster. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. **Default** : "60s" **Example** : "30s"                                                                                                                                                                                                                                                                                                                                                                                                                                          | string (duration)                                    |
| **completed** _optional_             | A nested object that sets the parameters for the completed requests catalog. All completed requests that match these parameters are tracked in the completed requests catalog. Refer to [Configure the Completed Requests](../../manage/monitor/monitoring-n1ql-query.md#sys-completed-config) for more information and examples. **Example** : { "user" : "marco", "error" : 12003 }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | [Logging parameters](#%5Flogging%5Fparameters)       |
| **completed-limit** _optional_       | Sets the number of requests to be logged in the completed requests catalog. As new completed requests are added, old ones are removed. Increase this when the completed request keyspace is not big enough to track the slow requests, such as when you want a larger sample of slow requests. Refer to [Configure the Completed Requests](../../manage/monitor/monitoring-n1ql-query.md#sys-completed-config) for more information and examples. The [cluster-level](../../rest-api/rest-cluster-query-settings.md#queryCompletedLimit) queryCompletedLimit setting specifies this property for the whole cluster. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. **Default** : 4000 **Example** : 7000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | integer (int32)                                      |
| **completed-threshold** _optional_   | A duration in milliseconds. All completed queries lasting longer than this threshold are logged in the completed requests catalog. Specify 0 to track all requests, independent of duration. Specify any negative number to track none. Refer to [Configure the Completed Requests](../../manage/monitor/monitoring-n1ql-query.md#sys-completed-config) for more information and examples. The [cluster-level](../../rest-api/rest-cluster-query-settings.md#queryCompletedThreshold) queryCompletedThreshold setting specifies this property for the whole cluster. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. **Default** : 1000 **Example** : 7000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | integer (int32)                                      |
| **controls** _optional_              | Specifies if there should be a controls section returned with the request results. When set to true, the query response document includes a controls section with runtime information provided along with the request, such as positional and named parameters or settings. If the request qualifies for caching, these values will also be cached in the completed\_requests system keyspace. The [request-level](index.md#controls%5Freq) controls parameter specifies this property per request. If a request does not include this parameter, the node-level controls setting will be used. **Default** : false **Example** : true                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | boolean                                              |
| **cpuprofile** _optional_            | The absolute path and filename to write the CPU profile to a local file. The output file includes a controls section and performance measurements, such as memory allocation and garbage collection, to pinpoint bottlenecks and ways to improve your code execution. To stop cpuprofile, run with the empty setting of "". If cpuprofile is left running too long, it can slow the system down as its file size increases. **Default** : "" **Example** : "/tmp/info.txt"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | string                                               |
| **debug** _optional_                 | Use debug mode. When set to true, extra logging is provided. **Default** : false **Example** : true                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | boolean                                              |
| **distribute** _optional_            | This field is only available with the POST method. When specified alongside other settings, this field instructs the node that is processing the request to cascade those settings to all other query nodes. The actual value of this field is ignored. **Example** : true                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | boolean                                              |
| **functions-limit** _optional_       | Maximum number of user-defined functions. **Default** : 16384 **Example** : 7000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | integer (int32)                                      |
| **keep-alive-length** _optional_     | Maximum size of buffered result. **Default** : 16384 **Example** : 7000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | integer (int32)                                      |
| **loglevel** _optional_              | Log level used in the logger. All values, in descending order of data: DEBUG — For developers. Writes everything. TRACE — For developers. Less info than DEBUG. INFO — For admin & customers. Lists warnings & errors. WARN — For admin. Only abnormal items. ERROR — For admin. Only errors to be fixed. SEVERE — For admin. Major items, like crashes. NONE — Doesn't write anything. The [cluster-level](../../rest-api/rest-cluster-query-settings.md#queryLogLevel) queryLogLevel setting specifies this property for the whole cluster. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. **Default** : "INFO" **Example** : "DEBUG"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | enum (DEBUG, TRACE, INFO, WARN, ERROR, SEVERE, NONE) |
| **max-index-api** _optional_         | Max index API. This setting is provided for technical support only.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | integer (int32)                                      |
| **max-parallelism** _optional_       | Specifies the maximum parallelism for queries on this node. If the value is zero or negative, the maximum parallelism is restricted to the number of allowed cores. Similarly, if the value is greater than the number of allowed cores, the maximum parallelism is restricted to the number of allowed cores. (The number of allowed cores is the same as the number of logical CPUs. In Community Edition, the number of allowed cores cannot be greater than 4\. In Enterprise Edition, there is no limit to the number of allowed cores.) The [cluster-level](../../rest-api/rest-cluster-query-settings.md#queryMaxParallelism) queryMaxParallelism setting specifies this property for the whole cluster. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. In addition, there is a [request-level](index.md#max%5Fparallelism%5Freq) max\_parallelism parameter. If a request includes this parameter, it will be capped by the node-level max-parallelism setting. To enable queries to run in parallel, you must specify the cluster-level queryMaxParallelism parameter, or specify the node-level max-parallelism parameter on all Query nodes. Refer to [Max Parallelism](../n1ql-language-reference/index-partitioning.md#max-parallelism) for more information. **Default** : 1 **Example** : 0 | integer (int32)                                      |
| **memory-quota** _optional_          | Specifies the maximum amount of memory a request may use on this node, in MB. Note that the overall node memory quota is this setting multiplied by the [node-level](#servicers) servicers setting. Specify 0 (the default value) to disable. When disabled, there is no quota. This parameter enforces a ceiling on the memory used for the tracked documents required for processing a request. It does not take into account any other memory that might be used to process a request, such as the stack, the operators, or some intermediate values. Within a transaction, this setting enforces the memory quota for the transaction by tracking the delta table and the transaction log (approximately). The [cluster-level](../../rest-api/rest-cluster-query-settings.md#queryMemoryQuota) queryMemoryQuota setting specifies this property for the whole cluster. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. In addition, the [request-level](index.md#memory%5Fquota%5Freq) memory\_quota parameter specifies this property per request. If a request includes this parameter, it will be capped by the node-level memory-quota setting. **Default** : 0 **Example** : 4                                                                                                                     | integer (int32)                                      |
| **memprofile** _optional_            | Filename to write the diagnostic memory usage log. To stop memprofile, run with the empty setting of "". If memprofile is left running too long, it can slow the system down as its file size increases. **Default** : "" **Example** : "/tmp/memory-usage.log"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | string                                               |
| **mutexprofile** _optional_          | Mutex profile. This setting is provided for technical support only. **Default** : false                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | boolean                                              |
| **n1ql-feat-ctrl** _optional_        | SQL++ feature control. This setting is provided for technical support only. The [cluster-level](../../rest-api/rest-cluster-query-settings.md#queryN1QLFeatCtrl) queryN1QLFeatCtrl setting specifies this property for the whole cluster. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. **Default** : 76                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | integer (int32)                                      |
| **numatrs** _optional_               | Specifies the total number of [active transaction records](../../learn/data/transactions.md#additional-storage-use). The [cluster-level](../../rest-api/rest-cluster-query-settings.md#queryNumAtrs) queryNumAtrs setting specifies this property for the whole cluster. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | string                                               |
| **pipeline-batch** _optional_        | Controls the number of items execution operators can batch for Fetch from the KV. The [cluster-level](../../rest-api/rest-cluster-query-settings.md#queryPipelineBatch) queryPipelineBatch setting specifies this property for the whole cluster. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. In addition, the [request-level](index.md#pipeline%5Fbatch%5Freq) pipeline\_batch parameter specifies this property per request. The minimum of that and the node-level pipeline-batch setting is applied. **Default** : 16 **Example** : 64                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | integer (int32)                                      |
| **pipeline-cap** _optional_          | Maximum number of items each execution operator can buffer between various operators. The [cluster-level](../../rest-api/rest-cluster-query-settings.md#queryPipelineCap) queryPipelineCap setting specifies this property for the whole cluster. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. In addition, the [request-level](index.md#pipeline%5Fcap%5Freq) pipeline\_cap parameter specifies this property per request. The minimum of that and the node-level pipeline-cap setting is applied. **Default** : 512 **Example** : 1024                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | integer (int32)                                      |
| **plus-servicers** _optional_        | The number of service threads for transactions where the scan consistency is request\_plus or at\_plus. The default is 16 times the number of logical cores. **Example** : 16                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | integer (int32)                                      |
| **prepared-limit** _optional_        | Maximum number of prepared statements in the cache. When this cache reaches the limit, the least recently used prepared statements will be discarded as new prepared statements are created. The [cluster-level](../../rest-api/rest-cluster-query-settings.md#queryPreparedLimit) queryPreparedLimit setting specifies this property for the whole cluster. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. **Default** : 16384 **Example** : 65536                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | integer (int32)                                      |
| **pretty** _optional_                | Specifies whether query results are returned in pretty format. The [request-level](index.md#pretty%5Freq) pretty parameter specifies this property per request. If a request does not include this parameter, the node-level setting is used, which defaults to false. **Default** : false **Example** : true                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | boolean                                              |
| **profile** _optional_               | Specifies if there should be a profile section returned with the request results. The valid values are: off — No profiling information is added to the query response. phases — The query response includes a profile section with stats and details about various phases of the query plan and execution. Three phase times will be included in the system:active\_requests and system:completed\_requests monitoring keyspaces. timings — Besides the phase times, the profile section of the query response document will include a full query plan with timing and information about the number of processed documents at each phase. This information will be included in the system:active\_requests and system:completed\_requests keyspaces. If profile is not set as one of the above values, then the profile setting does not change. Refer to [Monitoring and Profiling Details](../../manage/monitor/monitoring-n1ql-query.md#monitor-profile-details) for more information and examples. The [request-level](index.md#profile%5Freq) profile parameter specifies this property per request. If a request does not include this parameter, the node-level profile setting will be used. **Default** : "off" **Example** : "phases"                                                                                                                             | enum (off, phases, timings)                          |
| **request-size-cap** _optional_      | Maximum size of a request. **Default** : 67108864 **Example** : 70000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | integer (int32)                                      |
| **scan-cap** _optional_              | Maximum buffered channel size between the indexer client and the query service for index scans. This parameter controls when to use scan backfill. Use 0 or a negative number to disable. Smaller values reduce GC, while larger values reduce indexer backfill. The [cluster-level](../../rest-api/rest-cluster-query-settings.md#queryScanCap) queryScanCap setting specifies this property for the whole cluster. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. In addition, the [request-level](index.md#scan%5Fcap%5Freq) scan\_cap parameter specifies this property per request. The minimum of that and the node-level scan-cap setting is applied. **Default** : 512 **Example** : 1024                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | integer (int32)                                      |
| **servicers** _optional_             | The number of service threads for the query. The default is 4 times the number of cores on the query node. **Default** : 32 **Example** : 8                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | integer (int32)                                      |
| **timeout** _optional_               | Maximum time to spend on the request before timing out (ns). The value for this setting is an integer, representing a duration in nanoseconds. It must not be delimited by quotes, and must not include a unit. Specify 0 (the default value) or a negative integer to disable. When disabled, no timeout is applied and the request runs for however long it takes. The [cluster-level](../../rest-api/rest-cluster-query-settings.md#queryTimeout) queryTimeout setting specifies this property for the whole cluster. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. In addition, the [request-level](index.md#timeout%5Freq) timeout parameter specifies this property per request. The minimum of that and the node-level timeout setting is applied. **Default** : 0 **Example** : 500000000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | integer (int64)                                      |
| **txtimeout** _optional_             | Maximum time to spend on a transaction before timing out (ns). This setting only applies to requests containing the BEGIN TRANSACTION statement, or to requests where the [tximplicit](index.md#tximplicit) parameter is set. For all other requests, it is ignored. The value for this setting is an integer, representing a duration in nanoseconds. It must not be delimited by quotes, and must not include a unit. Specify 0 (the default value) to disable. When disabled, no timeout is applied and the transaction runs for however long it takes. The [cluster-level](../../rest-api/rest-cluster-query-settings.md#queryTxTimeout) queryTxTimeout setting specifies this property for the whole cluster. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. In addition, the [request-level](index.md#txtimeout%5Freq) txtimeout parameter specifies this property per request. The minimum of that and the node-level txtimeout setting is applied. **Default** : 0 **Example** : 500000000                                                                                                                                                                                                                                                                                                         | integer (int64)                                      |
| **use-cbo** _optional_               | Specifies whether the cost-based optimizer is enabled. The [cluster-level](../../rest-api/rest-cluster-query-settings.md#queryUseCBO) queryUseCBO setting specifies this property for the whole cluster. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. In addition, the [request-level](index.md#use%5Fcbo%5Freq) use\_cbo parameter specifies this property per request. If a request does not include this parameter, the node-level setting is used, which defaults to true. **Default** : true **Example** : false                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | boolean                                              |

**Logging parameters**

| Name                     | Description                                                                                                                                                                                                                                                | Schema          |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- |
| **aborted** _optional_   | If true, all requests that generate a panic are logged. **Example** : true                                                                                                                                                                                 | boolean         |
| **client** _optional_    | The IP address of the client. If specified, all completed requests from this IP address are logged. **Default** : "" **Example** : "172.1.2.3"                                                                                                             | string          |
| **context** _optional_   | The opaque ID or context provided by the client. If specified, all completed requests with this client context ID are logged. Refer to the [request-level](index.md#client%5Fcontext%5Fid) client\_context\_id parameter for more information.             | string          |
| **error** _optional_     | An error number. If specified, all completed queries returning this error number are logged. **Example** : 12003                                                                                                                                           | integer (int32) |
| **tag** _optional_       | A unique string which tags a set of qualifiers. Refer to [Configure the Completed Requests](../../manage/monitor/monitoring-n1ql-query.md#sys-completed-config) for more information. **Default** : "" **Example** : "both\_user\_and\_error"              | string          |
| **threshold** _optional_ | A duration in milliseconds. If specified, all completed queries lasting longer than this threshold are logged. This is another way of specifying the [node-level](#completed-threshold) completed-threshold setting. **Default** : 1000 **Example** : 7000 | integer (int32) |
| **user** _optional_      | A user name, as given in the request credentials. If specified, all completed queries with this user name are logged. **Default** : "" **Example** : "marco"                                                                                               | string          |

## [](#%5Fsecurityscheme)Security

### [](#%5Fdefault)Default

The Admin API supports admin credentials. Credentials can be passed via HTTP headers (HTTP basic authentication).

_Type_ : basic

### [](#%5Fnone)None

No authentication is required for the [Ping](#%5Fget%5Fping) or [Get Debug Variables](#%5Fget%5Fdebug%5Fvars) endpoints.

_Type_ : basic