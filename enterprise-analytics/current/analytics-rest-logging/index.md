---
title: Analytics Logging REST API
description: A description of the Logging REST API for Couchbase Enterprise Analytics.
pubDate: 2026-10-02T04:29:37.653Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.2/modules/analytics-rest-logging/pages/index.adoc
  xref: xref:enterprise-analytics:analytics-rest-logging:index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/current/analytics-rest-logging/index.html)

# Analytics Logging REST API

* getView Configured Loggers
* putModify Logger Levels
* delReset All Loggers
* getList Available Loggers
* getView Logger Level
* putModify Logger Level
* delReset Logger Level

[API docs by Redocly](https://redocly.com/redoc/)

# Enterprise Analytics Logging REST API (2.2)

Download OpenAPI specification:

This API enables you to view and modify the log levels of individual Enterprise Analytics loggers at runtime, without restarting the service.

Changes made through this API are applied immediately, broadcast to all active nodes in the cluster, and persisted so that they survive node restarts. They override the default log level configured by the `logLevel` service-level parameter (see the [Configuration REST API](/enterprise-analytics/current/analytics-rest-config/index.html)) for the affected loggers.

The root logger cannot be modified through this API.

## [](#operation/get%5Floggers)View Configured Loggers 

Returns the loggers that have been explicitly configured (i.e., whose level differs from that of their parent logger), along with their current levels.

##### Authorizations:

_AnalyticsManage_

### Responses

**200** 

Success. Returns the configured loggers and their levels.

**401** 

Unauthorized. The user name or password may be incorrect.

get/api/v1/cluster/logging

The URL scheme, host, and port are as follows.

{scheme}://{host}:{port}/api/v1/cluster/logging

### Response samples 

* 200
* 401

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "loggers": [
  * {
    * "name": "com.couchbase.analytics",
    * "level": "DEBUG"  
  }  
]
}`

## [](#operation/put%5Floggers)Modify Logger Levels 

Sets the log level for one or more loggers. Any logger included in the request that does not yet exist is created. The root logger (empty name) cannot be modified.

##### Authorizations:

_AnalyticsManage_

##### Request Body schema: application/json

required

| loggersrequired | Array of objects The list of loggers and their levels. |
| --------------- | ------------------------------------------------------ |

### Responses

**200** 

The operation was successful.

**400** 

Bad request. The request was malformed, the level was invalid, or an attempt was made to modify the root logger.

**401** 

Unauthorized. The user name or password may be incorrect.

put/api/v1/cluster/logging

The URL scheme, host, and port are as follows.

{scheme}://{host}:{port}/api/v1/cluster/logging

### Request samples 

* Payload

Content type

application/json

Copy

 Expand all  Collapse all 

`{
* "loggers": [
  * {
    * "name": "com.couchbase.analytics",
    * "level": "DEBUG"  
  }  
]
}`

### Response samples 

* 400
* 401

Content type

application/json

Copy

`{
* "error": "string"
}`

## [](#operation/delete%5Floggers)Reset All Loggers 

Restores all loggers to their default configuration, discarding any levels previously set through this API. The default level is determined by the `logLevel` service-level parameter.

##### Authorizations:

_AnalyticsManage_

### Responses

**200** 

The operation was successful.

**401** 

Unauthorized. The user name or password may be incorrect.

delete/api/v1/cluster/logging

The URL scheme, host, and port are as follows.

{scheme}://{host}:{port}/api/v1/cluster/logging

### Response samples 

* 401

Content type

application/json

Copy

`{ }`

## [](#operation/get%5Fall%5Floggers)List Available Loggers 

Returns the names of all known loggers, one per line, as plain text.

##### Authorizations:

_AnalyticsManage_

### Responses

**200** 

Success. Returns a newline-delimited list of logger names.

**401** 

Unauthorized. The user name or password may be incorrect.

get/api/v1/cluster/logging/all

The URL scheme, host, and port are as follows.

{scheme}://{host}:{port}/api/v1/cluster/logging/all

### Response samples 

* 200
* 401

Content type

text/plain

Copy

org.apache.hyracks
org.apache.asterix
com.couchbase.analytics

## [](#operation/get%5Flogger)View Logger Level 

Returns the current effective log level of the specified logger, as plain text.

##### Authorizations:

_AnalyticsManage_

##### path Parameters

| loggerrequired | string Example: com.couchbase.analyticsThe name of the logger. |
| -------------- | -------------------------------------------------------------- |

### Responses

**200** 

Success. Returns the logger's current level.

**400** 

Bad request. The request was malformed, the level was invalid, or an attempt was made to modify the root logger.

**401** 

Unauthorized. The user name or password may be incorrect.

get/api/v1/cluster/logging/{logger}

The URL scheme, host, and port are as follows.

{scheme}://{host}:{port}/api/v1/cluster/logging/{logger}

### Response samples 

* 400
* 401

Content type

application/json

Copy

`{
* "error": "string"
}`

## [](#operation/put%5Flogger)Modify Logger Level 

Sets the log level for the specified logger, creating it if it does not yet exist. The root logger cannot be modified.

##### Authorizations:

_AnalyticsManage_

##### path Parameters

| loggerrequired | string Example: com.couchbase.analyticsThe name of the logger. |
| -------------- | -------------------------------------------------------------- |

##### Request Body schema: text/plain

required

string

A log level. Common values, from least to most verbose, are: `OFF`, `FATAL`, `ERROR`, `WARN`, `INFO`, `DEBUG`, `TRACE`, `ALL`.

### Responses

**200** 

The operation was successful.

**400** 

Bad request. The request was malformed, the level was invalid, or an attempt was made to modify the root logger.

**401** 

Unauthorized. The user name or password may be incorrect.

put/api/v1/cluster/logging/{logger}

The URL scheme, host, and port are as follows.

{scheme}://{host}:{port}/api/v1/cluster/logging/{logger}

### Response samples 

* 400
* 401

Content type

application/json

Copy

`{
* "error": "string"
}`

## [](#operation/delete%5Flogger)Reset Logger Level 

Removes the level previously set for the specified logger through this API, so that it reverts to inheriting its level from its parent logger. The root logger cannot be modified.

##### Authorizations:

_AnalyticsManage_

##### path Parameters

| loggerrequired | string Example: com.couchbase.analyticsThe name of the logger. |
| -------------- | -------------------------------------------------------------- |

### Responses

**200** 

The operation was successful.

**400** 

Bad request. The request was malformed, the level was invalid, or an attempt was made to modify the root logger.

**401** 

Unauthorized. The user name or password may be incorrect.

delete/api/v1/cluster/logging/{logger}

The URL scheme, host, and port are as follows.

{scheme}://{host}:{port}/api/v1/cluster/logging/{logger}

### Response samples 

* 400
* 401

Content type

application/json

Copy

`{
* "error": "string"
}`