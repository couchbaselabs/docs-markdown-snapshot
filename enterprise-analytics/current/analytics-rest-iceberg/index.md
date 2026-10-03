---
title: Analytics Iceberg REST API
description: A description of the Iceberg REST API for Couchbase Analytics.
pubDate: 2026-10-03T04:27:21.374Z
meta:
  component:
    title: Enterprise Analytics
    version: "2.2"
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/analytics-rest-iceberg/pages/index.adoc
  xref: xref:enterprise-analytics:analytics-rest-iceberg:index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/analytics-rest-iceberg/index.html)

# Analytics Iceberg REST API

* Iceberg
  * getList Catalogs
  * getList Namespaces
  * getList Tables
  * getList Snapshots

[API docs by Redocly](https://redocly.com/redoc/)

# Enterprise Analytics Iceberg REST API (2.2)

Download OpenAPI specification:

This API enables you to browse Iceberg catalogs and metadata used by Enterprise Analytics.

## [](#tag/Iceberg)Iceberg

Operations for listing Iceberg catalogs, namespaces, tables, and snapshots.

## [](#tag/Iceberg/operation/list%5Ficeberg%5Fcatalogs)List Catalogs 

Returns all Iceberg catalogs created in Enterprise Analytics.

##### Authorizations:

_AnalyticsManageAnalyticsAccess_

### Responses

**200** 

Success. Returns an array of Iceberg catalog names.

**401** 

Unauthorized. The user name or password may be incorrect.

**500** 

Internal Server Error. Unexpected processing error while fetching Iceberg metadata.

**503** 

Service unavailable. The Analytics cluster is not in ACTIVE state.

get/api/v1/iceberg/catalog

The URL scheme, host, and port are as follows.

{scheme}://{host}:{port}/api/v1/iceberg/catalog

### Response samples 

* 200
* 401
* 500
* 503

Content type

application/json

Copy

 Expand all  Collapse all 

`[
* {
  * "catalog": "string"  
}
]`

## [](#tag/Iceberg/operation/list%5Ficeberg%5Fnamespaces)List Namespaces 

Returns all namespaces in the specified Iceberg catalog.

##### Authorizations:

_AnalyticsManageAnalyticsAccess_

##### path Parameters

| catalogNamerequired | string The Iceberg catalog name. |
| ------------------- | -------------------------------- |

### Responses

**200** 

Success. Returns an array of namespace names.

**400** 

Bad request. The URI or parameters are malformed, or the resource is not a supported Iceberg target.

**401** 

Unauthorized. The user name or password may be incorrect.

**404** 

Not found. The path may be incorrect, or the catalog/collection does not exist.

**500** 

Internal Server Error. Unexpected processing error while fetching Iceberg metadata.

**503** 

Service unavailable. The Analytics cluster is not in ACTIVE state.

get/api/v1/iceberg/catalog/{catalogName}/namespace

The URL scheme, host, and port are as follows.

{scheme}://{host}:{port}/api/v1/iceberg/catalog/{catalogName}/namespace

### Response samples 

* 200
* 400
* 401
* 404
* 500
* 503

Content type

application/json

Copy

 Expand all  Collapse all 

`[
* {
  * "namespace": "string"  
}
]`

## [](#tag/Iceberg/operation/list%5Ficeberg%5Ftables)List Tables 

Returns all iceberg tables in the specified namespace.

##### Authorizations:

_AnalyticsManageAnalyticsAccess_

##### path Parameters

| catalogNamerequired | string The Iceberg catalog name.                             |
| ------------------- | ------------------------------------------------------------ |
| namespacerequired   | string The Iceberg namespace. URL-encode special characters. |

### Responses

**200** 

Success. Returns an array of table names.

**400** 

Bad request. The URI or parameters are malformed, or the resource is not a supported Iceberg target.

**401** 

Unauthorized. The user name or password may be incorrect.

**404** 

Not found. The path may be incorrect, or the catalog/collection does not exist.

**500** 

Internal Server Error. Unexpected processing error while fetching Iceberg metadata.

**503** 

Service unavailable. The Analytics cluster is not in ACTIVE state.

get/api/v1/iceberg/catalog/{catalogName}/namespace/{namespace}/table

The URL scheme, host, and port are as follows.

{scheme}://{host}:{port}/api/v1/iceberg/catalog/{catalogName}/namespace/{namespace}/table

### Response samples 

* 200
* 400
* 401
* 404
* 500
* 503

Content type

application/json

Copy

 Expand all  Collapse all 

`[
* {
  * "table": "string"  
}
]`

## [](#tag/Iceberg/operation/list%5Ficeberg%5Fsnapshots)List Snapshots 

Returns snapshots for the specified iceberg table (Enterprise Analytics iceberg collection).

##### Authorizations:

_AnalyticsManageAnalyticsAccess_

##### path Parameters

| databaseNamerequired   | string The Analytics database name.            |
| ---------------------- | ---------------------------------------------- |
| scopeNamerequired      | string The Analytics scope name.               |
| collectionNamerequired | string The Analytics external collection name. |

### Responses

**200** 

Success. Returns an array of snapshots for the Iceberg table.

**400** 

Bad request. The URI or parameters are malformed, or the resource is not a supported Iceberg target.

**401** 

Unauthorized. The user name or password may be incorrect.

**404** 

Not found. The path may be incorrect, or the catalog/collection does not exist.

**500** 

Internal Server Error. Unexpected processing error while fetching Iceberg metadata.

**503** 

Service unavailable. The Analytics cluster is not in ACTIVE state.

get/api/v1/iceberg/snapshot/{databaseName}/{scopeName}/{collectionName}

The URL scheme, host, and port are as follows.

{scheme}://{host}:{port}/api/v1/iceberg/snapshot/{databaseName}/{scopeName}/{collectionName}

### Response samples 

* 200
* 400
* 401
* 404
* 500
* 503

Content type

application/json

Copy

 Expand all  Collapse all 

`[
* {
  * "id": 0,
  * "timestamp_ms": 0  
}
]`