---
title: Analytics Settings REST API
description: A description of the Settings REST API for Couchbase Analytics.
editUrl: https://github.com/couchbase/docs-analytics/edit/release/7.2/modules/analytics/pages/rest-settings.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.2@server:analytics:rest-settings.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/analytics/rest-settings.html)

# Analytics Settings REST API

## [](#%5Foverview)Overview

The Analytics Settings REST API is provided by the Analytics service. This API enables you to view or set cluster-level Analytics settings.

The API schemes and host URLs are as follows:

* <http://node:8091/>
* <https://node:18091/> (for secure access)

where `node` is the host name or IP address of a node running the Analytics service. (Note that the port numbers for this REST API are different to the port numbers used by the other Analytics REST APIs.)

### [](#version-information)Version information

_Version_ : 7.2

### [](#consumes)Consumes

* `application/x-www-form-urlencoded`

### [](#produces)Produces

* `application/json`

## [](#%5Fpaths)Paths

This section describes the operations available with this REST API.

* [View Analytics Settings](#%5Fget%5Fsettings)
* [Modify Analytics Settings](#%5Fpost%5Fsettings)

### [](#%5Fget%5Fsettings)View Analytics Settings

GET /settings/analytics

#### [](#description)Description

Retrieves cluster-level Analytics settings. Note that only one setting is available: `numReplicas`.

You can also retrieve the number of Analytic replicas using the [Couchbase Web Console](../manage/manage-settings/general-settings.md#analytics-replicas) or the [CLI](../manage/manage-settings/general-settings.md#analytics-settings-via-cli). For further details about Analytics replicas, refer to [Rebalance](../learn/clusters-and-availability/rebalance.md#rebalancing-the-analytics-service) and [Hard Failover](../learn/clusters-and-availability/hard-failover.md#hard-failover-and-the-analytics-service).

#### [](#responses)Responses

| HTTP Code | Description                                               | Schema                   |
| --------- | --------------------------------------------------------- | ------------------------ |
| **200**   | The operation was successful.                             | [Settings](#%5Fsettings) |
| **401**   | Unauthorized. The user name or password may be incorrect. | object                   |

#### [](#security)Security

| Type      | Name                                                               |
| --------- | ------------------------------------------------------------------ |
| **basic** | **[Cluster Read / Pools Read](#%5Fcluster%5Fread%5Fpools%5Fread)** |

#### [](#example-http-request)Example HTTP request

The example below retrieves the current number of Analytics replicas.

Curl request

```sh
curl -X GET -u Administrator:password \
http://localhost:8091/settings/analytics
```

#### [](#example-http-response)Example HTTP response

Response 200

```json
{"numReplicas": 1}
```

### [](#%5Fpost%5Fsettings)Modify Analytics Settings

POST /settings/analytics

#### [](#description-2)Description

Sets cluster-level Analytics settings. Note that only one setting is available: `numReplicas`.

You can also set the number of Analytic replicas using the [Couchbase Web Console](../manage/manage-settings/general-settings.md#analytics-replicas) or the [CLI](../manage/manage-settings/general-settings.md#analytics-settings-via-cli). For further details about Analytics replicas, refer to [Rebalance](../learn/clusters-and-availability/rebalance.md#rebalancing-the-analytics-service) and [Hard Failover](../learn/clusters-and-availability/hard-failover.md#hard-failover-and-the-analytics-service).

> [!NOTE]
> A rebalance is required for a new `numReplicas` value to take effect.

#### [](#parameters)Parameters

| Type         | Name                       | Description                                     | Schema  |
| ------------ | -------------------------- | ----------------------------------------------- | ------- |
| **FormData** | **numReplicas** _optional_ | Specifies the number of replicas for Analytics. | integer |

#### [](#responses-2)Responses

| HTTP Code | Description                                               | Schema                   |
| --------- | --------------------------------------------------------- | ------------------------ |
| **200**   | The operation was successful.                             | [Settings](#%5Fsettings) |
| **400**   | Bad request. A parameter has an incorrect value.          | object                   |
| **401**   | Unauthorized. The user name or password may be incorrect. | object                   |

#### [](#security-2)Security

| Type      | Name                                                               |
| --------- | ------------------------------------------------------------------ |
| **basic** | **[Cluster Read / Pools Read](#%5Fcluster%5Fread%5Fpools%5Fread)** |

#### [](#example-http-request-2)Example HTTP request

The example below changes the current number of Analytics replicas to 2.

Curl request

```sh
curl -X POST -u Administrator:password \
http://localhost:8091/settings/analytics \
-d numReplicas=2
```

#### [](#example-http-response-2)Example HTTP response

Response 200

```json
{"numReplicas": 2}
```

## [](#%5Fdefinitions)Definitions

This section describes the properties returned by this REST API.

### [](#%5Fsettings)Settings

| Name                       | Description                                                                                                 | Schema  |
| -------------------------- | ----------------------------------------------------------------------------------------------------------- | ------- |
| **numReplicas** _required_ | Specifies the number of replicas for Analytics. **Minimum value** : 0 **Maximum value** : 3 **Example** : 3 | integer |

## [](#%5Fsecurityscheme)Security

### [](#%5Fcluster%5Fread%5Fpools%5Fread)Cluster Read / Pools Read

The Analytics Settings REST API supports HTTP basic authentication. Credentials can be passed via HTTP headers.

Users must have one of the following RBAC roles:

* Full Admin
* Cluster Admin
* Read-Only Admin
* Analytics Admin

Refer to [Roles](../learn/security/roles.html) for more details.

_Type_ : basic