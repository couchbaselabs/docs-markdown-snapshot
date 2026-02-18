---
title: Analytics Settings REST API
description: A description of the Settings REST API for Couchbase Analytics.
editUrl: https://github.com/couchbaselabs/cb-swagger/edit/release/8.0/docs/modules/analytics-rest-settings/pages/index.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/current/analytics-rest-settings/index.html)

# Analytics Settings REST API

## [](#overview)Overview

The Analytics Settings REST API is provided by the Analytics service. This API enables you to view or set cluster-level Analytics settings.

### Version information

**Version:** 8.0

### Host information

{scheme}://{host}:{port}

The URL scheme, host, and port are as follows.

| Component  | Description                                                                                                                                                                                                      |
| ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **scheme** | The URL scheme. Use https for secure access. **Values:** http, https                                                                                                                                             |
| **host**   | The host name or IP address of a node running the Analytics Service. **Example:** localhost                                                                                                                      |
| **port**   | The Cluster administration REST port. Use 18091 for secure access. Note that the port numbers for this REST API are different to the port numbers used by the other Analytics REST APIs. **Values:** 8091, 18091 |

## [](#resources)Resources

This section describes the operations available with this REST API.

[View Analytics Settings](#get%5Fsettings)  
[Modify Analytics Settings](#post%5Fsettings)

### [](#get%5Fsettings)View Analytics Settings

GET /settings/analytics

#### [](#get%5Fsettings-description)Description

Retrieves cluster-level Analytics settings. Note that only one setting is available: `numReplicas`.

You can also retrieve the number of Analytic replicas using the [Couchbase Web Console](../manage/manage-settings/general-settings.md#analytics-replicas) or the [CLI](../manage/manage-settings/general-settings.md#analytics-settings-via-cli). For more information about Analytics replicas, see [Rebalance](../learn/clusters-and-availability/rebalance.md#rebalancing-the-analytics-service) and [Hard Failover](../learn/clusters-and-availability/hard-failover.md#hard-failover-and-the-analytics-service).

Produces

* application/json

#### [](#get%5Fsettings-responses)Responses

| HTTP Code | Description                                               | Schema                |
| --------- | --------------------------------------------------------- | --------------------- |
| 200       | The operation was successful.                             | [Settings](#Settings) |
| 401       | Unauthorized. The user name or password may be incorrect. | Object                |

#### [](#get%5Fsettings-security)Security

| Type         | Name                                                        |
| ------------ | ----------------------------------------------------------- |
| http (basic) | [Cluster Read / Pools Read](#security-ClusterReadPoolsRead) |

#### [](#example-http-request)Example HTTP Request

The example below retrieves the current number of Analytics replicas.

curl request

```sh
curl -X GET -u Administrator:password \
http://localhost:8091/settings/analytics
```

#### [](#example-http-response)Example HTTP Response

Response 200

```json
{"numReplicas": 1}
```

### [](#post%5Fsettings)Modify Analytics Settings

POST /settings/analytics

#### [](#post%5Fsettings-description)Description

Sets cluster-level Analytics settings. Note that only one setting is available: `numReplicas`.

You can also set the number of Analytic replicas using the [Couchbase Web Console](../manage/manage-settings/general-settings.md#analytics-replicas) or the [CLI](../manage/manage-settings/general-settings.md#analytics-settings-via-cli). For more information about Analytics replicas, see [Rebalance](../learn/clusters-and-availability/rebalance.md#rebalancing-the-analytics-service) and [Hard Failover](../learn/clusters-and-availability/hard-failover.md#hard-failover-and-the-analytics-service).

> [!NOTE]
> A rebalance is required for a new `numReplicas` value to take effect.

Consumes

* application/x-www-form-urlencoded

Produces

* application/json

#### [](#post%5Fsettings-parameters)Parameters

Form Parameters

| Name                    | Description                                                                                   | Schema  |
| ----------------------- | --------------------------------------------------------------------------------------------- | ------- |
| **numReplicas**optional | Specifies the number of replicas for Analytics. **Minimum:** 0 **Maximum:** 3 **Example:** 56 | Integer |

#### [](#post%5Fsettings-responses)Responses

| HTTP Code | Description                                               | Schema                |
| --------- | --------------------------------------------------------- | --------------------- |
| 200       | The operation was successful.                             | [Settings](#Settings) |
| 400       | Bad request. A parameter has an incorrect value.          | Object                |
| 401       | Unauthorized. The user name or password may be incorrect. | Object                |

#### [](#post%5Fsettings-security)Security

| Type         | Name                                                        |
| ------------ | ----------------------------------------------------------- |
| http (basic) | [Cluster Read / Pools Read](#security-ClusterReadPoolsRead) |

#### [](#example-http-request-2)Example HTTP Request

The example below changes the current number of Analytics replicas to 2.

curl request

```sh
curl -X POST -u Administrator:password \
http://localhost:8091/settings/analytics \
-d numReplicas=2
```

#### [](#example-http-response-2)Example HTTP Response

Response 200

```json
{"numReplicas": 2}
```

## [](#models)Definitions

This section describes the properties consumed and returned by this REST API.

### [](#Settings)Settings

 Object

| Property                |                                                                                              | Schema  |
| ----------------------- | -------------------------------------------------------------------------------------------- | ------- |
| **numReplicas**optional | Specifies the number of replicas for Analytics. **Minimum:** 0 **Maximum:** 3 **Example:** 3 | Integer |

## [](#security)Security

The Analytics Settings REST API supports HTTP basic authentication. Pass your credentials through HTTP headers.

### [](#security-ClusterReadPoolsRead)Cluster Read / Pools Read

Users must have one of the following RBAC roles:

* Full Admin
* Cluster Admin
* Read-Only Admin
* Analytics Admin

**Type:** http

For more information, see [Roles](../learn/security/roles.md).