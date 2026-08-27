---
title: Cluster Query Settings API
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/rest-api/pages/rest-cluster-query-settings.adoc
  xref: xref:7.2@server:rest-api:rest-cluster-query-settings.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/rest-api/rest-cluster-query-settings.html)

# Cluster Query Settings API

## [](#%5Foverview)Overview

The Query Settings REST API is provided by the Query service. This API enables you to view or specify cluster-level Query settings.

The API schemes and host URLs are as follows:

* <http://node:8091/>
* <https://node:18091/> (for secure access)

where `node` is the host name or IP address of a node running the Query service.

### [](#version-information)Version information

_Version_ : 7.2

### [](#consumes)Consumes

* `application/x-www-form-urlencoded`

### [](#produces)Produces

* `application/json`

## [](#%5Fpaths)Paths

**Table of Contents**

* [Retrieve Cluster-Level Query Settings](#%5Fget%5Fsettings)
* [Update Cluster-Level Query Settings](#%5Fpost%5Fsettings)
* [Retrieve CURL Access List](#%5Fget%5Faccess)
* [Update CURL Access List](#%5Fpost%5Faccess)

### [](#%5Fget%5Fsettings)Retrieve Cluster-Level Query Settings

GET /settings/querySettings

#### [](#description)Description

Returns all cluster-level query settings, including the CURL access settings.

#### [](#responses)Responses

| HTTP Code | Description                                    | Schema                   |
| --------- | ---------------------------------------------- | ------------------------ |
| **200**   | An object giving cluster-level query settings. | [Settings](#%5Fsettings) |

#### [](#security)Security

| Type      | Name                       |
| --------- | -------------------------- |
| **basic** | **[Default](#%5Fdefault)** |

#### [](#example-http-request)Example HTTP request

The example below gets the current cluster-level query settings.

Curl request

```sh
curl -v -u Administrator:password \
http://localhost:8091/settings/querySettings
```

#### [](#example-http-response)Example HTTP response

Response 200

```json
{
  "queryTmpSpaceDir": "/opt/couchbase/var/lib/couchbase/tmp",
  "queryTmpSpaceSize": 5120,
  "queryPipelineBatch": 16,
  "queryPipelineCap": 512,
  "queryScanCap": 512,
  "queryTimeout": 0,
  "queryPreparedLimit": 16384,
  "queryCompletedLimit": 4000,
  "queryCompletedThreshold": 1000,
  "queryLogLevel": "info",
  "queryMaxParallelism": 1,
  "queryN1QLFeatCtrl": 76,
  "queryTxTimeout": "0ms",
  "queryMemoryQuota": 0,
  "queryUseCBO": true,
  "queryCleanupClientAttempts": true,
  "queryCleanupLostAttempts": true,
  "queryCleanupWindow": "60s",
  "queryNumAtrs": 1024,
  "queryCurlWhitelist": {
    "all_access": false,
    "allowed_urls": [],
    "disallowed_urls": []
  }
}
```

### [](#%5Fpost%5Fsettings)Update Cluster-Level Query Settings

POST /settings/querySettings

#### [](#description-2)Description

Updates cluster-level query settings, including the CURL access settings.

#### [](#parameters)Parameters

| Type     | Name                    | Description                                        | Schema                   |
| -------- | ----------------------- | -------------------------------------------------- | ------------------------ |
| **Body** | **Settings** _optional_ | An object specifying cluster-level query settings. | [Settings](#%5Fsettings) |

#### [](#responses-2)Responses

| HTTP Code | Description                                                                  | Schema                   |
| --------- | ---------------------------------------------------------------------------- | ------------------------ |
| **200**   | An object giving cluster-level query settings, including the latest changes. | [Settings](#%5Fsettings) |
| **400**   | Returns an error message if a parameter or value is incorrect.               | object                   |

#### [](#security-2)Security

| Type      | Name                       |
| --------- | -------------------------- |
| **basic** | **[Default](#%5Fdefault)** |

#### [](#example-http-request-2)Example HTTP request

The example below changes the temp file directory to `/tmp` and the temp file size to 2048 MB.

Curl request

```sh
curl -v -X POST -u Administrator:password \
http://localhost:8091/settings/querySettings \
-d 'queryTmpSpaceDir=/tmp' \
-d 'queryTmpSpaceSize=2048'
```

#### [](#example-http-response-2)Example HTTP response

Response 200

```json
{
  "queryTmpSpaceDir": "/tmp",
  "queryTmpSpaceSize": 2048,
  "queryPipelineBatch": 16,
  "queryPipelineCap": 512,
  "queryScanCap": 512,
  "queryTimeout": 0,
  "queryPreparedLimit": 16384,
  "queryCompletedLimit": 4000,
  "queryCompletedThreshold": 1000,
  "queryLogLevel": "info",
  "queryMaxParallelism": 1,
  "queryN1QLFeatCtrl": 76,
  "queryTxTimeout": "0ms",
  "queryMemoryQuota": 0,
  "queryUseCBO": true,
  "queryCleanupClientAttempts": true,
  "queryCleanupLostAttempts": true,
  "queryCleanupWindow": "60s",
  "queryNumAtrs": 1024,
  "queryCurlWhitelist": {
    "all_access": false,
    "allowed_urls": [],
    "disallowed_urls": []
  }
}
```

### [](#%5Fget%5Faccess)Retrieve CURL Access List

GET /settings/querySettings/curlWhitelist

#### [](#description-3)Description

Returns the cluster-level CURL access settings only.

#### [](#responses-3)Responses

| HTTP Code | Description                                                              | Schema               |
| --------- | ------------------------------------------------------------------------ | -------------------- |
| **200**   | An object determining which URLs may be accessed by the CURL() function. | [Access](#%5Faccess) |

#### [](#security-3)Security

| Type      | Name                       |
| --------- | -------------------------- |
| **basic** | **[Default](#%5Fdefault)** |

#### [](#example-http-request-3)Example HTTP request

The example below gets the current cluster-level CURL access settings.

Curl request

```sh
curl -v -u Administrator:password \
http://localhost:8091/settings/querySettings/curlWhitelist
```

#### [](#example-http-response-3)Example HTTP response

Response 200

```json
{
  "all_access": false,
  "allowed_urls": [],
  "disallowed_urls": []
}
```

### [](#%5Fpost%5Faccess)Update CURL Access List

POST /settings/querySettings/curlWhitelist

#### [](#description-4)Description

Updates the cluster-level CURL access settings only.

#### [](#parameters-2)Parameters

| Type     | Name                    | Description                                                              | Schema               |
| -------- | ----------------------- | ------------------------------------------------------------------------ | -------------------- |
| **Body** | **Settings** _optional_ | An object determining which URLs may be accessed by the CURL() function. | [Access](#%5Faccess) |

#### [](#responses-4)Responses

| HTTP Code | Description                                                                                            | Schema               |
| --------- | ------------------------------------------------------------------------------------------------------ | -------------------- |
| **200**   | An object determining which URLs may be accessed by the CURL() function, including the latest changes. | [Access](#%5Faccess) |
| **400**   | Returns an error message if a parameter or value is incorrect.                                         | object               |

#### [](#security-4)Security

| Type      | Name                       |
| --------- | -------------------------- |
| **basic** | **[Default](#%5Fdefault)** |

#### [](#example-http-request-4)Example HTTP request

The example below specifies that `https://company1.com` is allowed, and `https://company2.com` is disallowed.

Curl request

```sh
curl -v -X POST -u Administrator:password \
http://localhost:8091/settings/querySettings/curlWhitelist \
-d '{"all_access": false,
     "allowed_urls": ["https://company1.com"],
     "disallowed_urls": ["https://company2.com"]}'
```

#### [](#example-http-response-4)Example HTTP response

Response 200

```json
{
  "all_access": false,
  "allowed_urls": [
    "https://company1.com"
  ],
  "disallowed_urls": [
    "https://company2.com"
  ]
}
```

## [](#%5Fdefinitions)Definitions

**Table of Contents**

* [Settings](#%5Fsettings)
* [Access](#%5Faccess)

### [](#%5Fsettings)Settings

| Name                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Schema                                               |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------- |
| **queryCleanupClientAttempts** _optional_ | When enabled, the Query service preferentially aims to clean up just transactions that it has created, leaving transactions for the distributed cleanup process only when it is forced to. The [node-level](../n1ql/n1ql-rest-api/admin.md#cleanupclientattempts) cleanupclientattempts setting specifies this property for a single node. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. **Default** : true **Example** : false                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | boolean                                              |
| **queryCleanupLostAttempts** _optional_   | When enabled, the Query service takes part in the distributed cleanup process, and cleans up expired transactions created by any client. The [node-level](../n1ql/n1ql-rest-api/admin.md#cleanuplostattempts) cleanuplostattempts setting specifies this property for a single node. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. **Default** : true **Example** : false                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | boolean                                              |
| **queryCleanupWindow** _optional_         | Specifies how frequently the Query service checks its subset of [active transaction records](../learn/data/transactions.md#additional-storage-use) for cleanup. Decreasing this setting causes expiration transactions to be found more swiftly, with the tradeoff of increasing the number of reads per second used for the scanning process. The value for this setting is a string. Its format includes an amount and a mandatory unit, e.g. 10ms (10 milliseconds) or 0.5s (half a second). Valid units are: ns (nanoseconds) us (microseconds) ms (milliseconds) s (seconds) m (minutes) h (hours) The [node-level](../n1ql/n1ql-rest-api/admin.md#cleanupwindow) cleanupwindow setting specifies this property for a single node. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. **Default** : "60s" **Example** : "30s"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | string (duration)                                    |
| **queryCompletedLimit** _optional_        | Sets the number of requests to be logged in the completed requests catalog. As new completed requests are added, old ones are removed. Increase this when the completed request keyspace is not big enough to track the slow requests, such as when you want a larger sample of slow requests. Refer to [Configure the Completed Requests](../manage/monitor/monitoring-n1ql-query.md#sys-completed-config) for more information and examples. The [node-level](../n1ql/n1ql-rest-api/admin.md#completed-limit) completed-limit setting specifies this property for a single node. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. **Default** : 4000 **Example** : 7000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | integer (int32)                                      |
| **queryCompletedThreshold** _optional_    | A duration in milliseconds. All completed queries lasting longer than this threshold are logged in the completed requests catalog. Specify 0 to track all requests, independent of duration. Specify any negative number to track none. Refer to [Configure the Completed Requests](../manage/monitor/monitoring-n1ql-query.md#sys-completed-config) for more information and examples. The [node-level](../n1ql/n1ql-rest-api/admin.md#completed-threshold) completed-threshold setting specifies this property for a single node. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. **Default** : 1000 **Example** : 7000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | integer (int32)                                      |
| **queryLogLevel** _optional_              | Log level used in the logger. All values, in descending order of data: DEBUG — For developers. Writes everything. TRACE — For developers. Less info than DEBUG. INFO — For admin & customers. Lists warnings & errors. WARN — For admin. Only abnormal items. ERROR — For admin. Only errors to be fixed. SEVERE — For admin. Major items, like crashes. NONE — Doesn't write anything. The [node-level](../n1ql/n1ql-rest-api/admin.md#loglevel) loglevel setting specifies this property for a single node. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. **Default** : "INFO" **Example** : "DEBUG"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | enum (DEBUG, TRACE, INFO, WARN, ERROR, SEVERE, NONE) |
| **queryMaxParallelism** _optional_        | Specifies the maximum parallelism for queries on all Query nodes in the cluster. If the value is zero or negative, the maximum parallelism is restricted to the number of allowed cores. Similarly, if the value is greater than the number of allowed cores, the maximum parallelism is restricted to the number of allowed cores. (The number of allowed cores is the same as the number of logical CPUs. In Community Edition, the number of allowed cores cannot be greater than 4\. In Enterprise Edition, there is no limit to the number of allowed cores.) The [node-level](../n1ql/n1ql-rest-api/admin.md#max-parallelism-srv) max-parallelism setting specifies this property for a single node. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. In addition, there is a [request-level](../settings/query-settings.md#max%5Fparallelism%5Freq) max\_parallelism parameter. If a request includes this parameter, it will be capped by the node-level max-parallelism setting. To enable queries to run in parallel, you must specify the cluster-level queryMaxParallelism parameter, or specify the node-level max-parallelism parameter on all Query nodes. Refer to [Max Parallelism](../n1ql/n1ql-language-reference/index-partitioning.md#max-parallelism) for more information. **Default** : 1 **Example** : 0 | integer (int32)                                      |
| **queryMemoryQuota** _optional_           | Specifies the maximum amount of memory a request may use on any Query node in the cluster, in MB. This parameter enforces a ceiling on the memory used for the tracked documents required for processing a request. It does not take into account any other memory that might be used to process a request, such as the stack, the operators, or some intermediate values. Within a transaction, this setting enforces the memory quota for the transaction by tracking the delta table and the transaction log (approximately). The [node-level](../n1ql/n1ql-rest-api/admin.md#memory-quota-srv) memory-quota setting specifies this property for a single node. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. In addition, there is a [request-level](../settings/query-settings.md#memory%5Fquota%5Freq) memory\_quota parameter. If a request includes this parameter, it will be capped by the node-level memory-quota setting. **Default** : 0 **Example** : 4                                                                                                                                                                                                                                                                                                                                                          | integer (int32)                                      |
| **queryN1QLFeatCtrl** _optional_          | SQL++ feature control. This setting is provided for technical support only. The [node-level](../n1ql/n1ql-rest-api/admin.md#n1ql-feat-ctrl) n1ql-feat-ctrl setting specifies this property for a single node. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | integer (int32)                                      |
| **queryNumAtrs** _optional_               | Specifies the total number of [active transaction records](../learn/data/transactions.md#additional-storage-use) for all Query nodes in the cluster. The [node-level](../n1ql/n1ql-rest-api/admin.md#numatrs-srv) numatrs setting specifies this property for a single node. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. **Default** : 1024 **Minimum value (exclusive)** : 0 **Example** : 512                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | integer (int32)                                      |
| **queryPipelineBatch** _optional_         | Controls the number of items execution operators can batch for Fetch from the KV. The [node-level](../n1ql/n1ql-rest-api/admin.md#pipeline-batch-srv) pipeline-batch setting specifies this property for a single node. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. In addition, the [request-level](../settings/query-settings.md#pipeline%5Fbatch%5Freq) pipeline\_batch parameter specifies this property per request. The minimum of that and the node-level pipeline-batch setting is applied. **Default** : 16 **Example** : 64                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | integer (int32)                                      |
| **queryPipelineCap** _optional_           | Maximum number of items each execution operator can buffer between various operators. The [node-level](../n1ql/n1ql-rest-api/admin.md#pipeline-cap-srv) pipeline-cap setting specifies this property for a single node. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. In addition, the [request-level](../settings/query-settings.md#pipeline%5Fcap%5Freq) pipeline\_cap parameter specifies this property per request. The minimum of that and the node-level pipeline-cap setting is applied. **Default** : 512 **Example** : 1024                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | integer (int32)                                      |
| **queryPreparedLimit** _optional_         | Maximum number of prepared statements in the cache. When this cache reaches the limit, the least recently used prepared statements will be discarded as new prepared statements are created. The [node-level](../n1ql/n1ql-rest-api/admin.md#prepared-limit) prepared-limit setting specifies this property for a single node. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. **Default** : 16384 **Example** : 65536                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | integer (int32)                                      |
| **queryScanCap** _optional_               | Maximum buffered channel size between the indexer client and the query service for index scans. This parameter controls when to use scan backfill. Use 0 or a negative number to disable. Smaller values reduce GC, while larger values reduce indexer backfill. The [node-level](../n1ql/n1ql-rest-api/admin.md#scan-cap-srv) scan-cap setting specifies this property for a single node. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. In addition, the [request-level](../settings/query-settings.md#scan%5Fcap%5Freq) scan\_cap parameter specifies this property per request. The minimum of that and the node-level scan-cap setting is applied. **Default** : 512 **Example** : 1024                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | integer (int32)                                      |
| **queryTimeout** _optional_               | Maximum time to spend on the request before timing out (ns). The value for this setting is an integer, representing a duration in nanoseconds. It must not be delimited by quotes, and must not include a unit. Specify 0 (the default value) or a negative integer to disable. When disabled, no timeout is applied and the request runs for however long it takes. The [node-level](../n1ql/n1ql-rest-api/admin.md#timeout-srv) timeout setting specifies this property for a single node. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. In addition, the [request-level](../settings/query-settings.md#timeout%5Freq) timeout parameter specifies this property per request. The minimum of that and the node-level timeout setting is applied. **Default** : 0 **Example** : 500000000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | integer (int64)                                      |
| **queryTxTimeout** _optional_             | Maximum time to spend on a transaction before timing out. This setting only applies to requests containing the BEGIN TRANSACTION statement, or to requests where the [tximplicit](../settings/query-settings.md#tximplicit) parameter is set. For all other requests, it is ignored. The value for this setting is a string. Its format includes an amount and a mandatory unit, e.g. 10ms (10 milliseconds) or 0.5s (half a second). Valid units are: ns (nanoseconds) us (microseconds) ms (milliseconds) s (seconds) m (minutes) h (hours) Specify 0ms (the default value) to disable. When disabled, no timeout is applied and the transaction runs for however long it takes. The [node-level](../n1ql/n1ql-rest-api/admin.md#txtimeout-srv) txtimeout setting specifies this property for a single node. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. In addition, there is a [request-level](../settings/query-settings.md#txtimeout%5Freq) txtimeout parameter. If a request includes this parameter, it will be capped by the node-level txtimeout setting. **Default** : "0ms" **Example** : "0.5s"                                                                                                                                                                                                                 | string (duration)                                    |
| **queryTmpSpaceDir** _optional_           | The path to which the indexer writes temporary backfill files, to store any transient data during query processing. The specified path must already exist. Only absolute paths are allowed. The default path is var/lib/couchbase/tmp within the Couchbase Server installation directory. **Example** : "/opt/couchbase/var/lib/couchbase/tmp"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | string                                               |
| **queryTmpSpaceSize** _optional_          | The maximum size of temporary backfill files (MB). Setting the size to 0 disables backfill. Setting the size to \-1 means the size is unlimited. The maximum size is limited only by the available disk space. **Default** : 5120 **Example** : 2048                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | integer (int32)                                      |
| **queryUseCBO** _optional_                | Specifies whether the cost-based optimizer is enabled. The [node-level](../n1ql/n1ql-rest-api/admin.md#use-cbo-srv) use-cbo setting specifies this property for a single node. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. In addition, the [request-level](../settings/query-settings.md#use%5Fcbo%5Freq) use\_cbo parameter specifies this property per request. If a request does not include this parameter, the node-level setting is used, which defaults to true. **Default** : true **Example** : false                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | boolean                                              |
| **queryCurlWhitelist** _optional_         | An object which determines which URLs may be accessed by the CURL() function.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | [Access](#%5Faccess)                                 |

### [](#%5Faccess)Access

| Name                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                             | Schema           |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| **all\_access** _required_      | Defines whether the user has access to all URLs, or only URLs specified by the access list. This field set must be set to false to enable the allowed\_urls and disallowed\_urls fields. Setting this field to true enables access to all endpoints. **Default** : false                                                                                                                                                                                | boolean          |
| **allowed\_urls** _optional_    | An array of strings, each of which is a URL to which you wish to grant access. Each URL is a prefix match. The CURL() function will allow any URL that starts with this value. For example, if you wish to allow access to all Google APIs, add the URL https://maps.googleapis.com to the array. To allow complete access to localhost, use http://localhost. Note that each URL must include the port, protocol, and all other components of the URL. | < string > array |
| **disallowed\_urls** _optional_ | An array of strings, each of which is a URL that will be restricted for all roles. Each URL is a prefix match. The CURL() function will disallow any URL that starts with this value. If both allowed\_urls and disallowed\_urls fields are populated, the disallowed\_urls field takes precedence over allowed\_urls. Note that each URL must include the port, protocol, and all other components of the URL.                                         | < string > array |

## [](#%5Fsecurityscheme)Security

The Query Settings REST API supports HTTP basic authentication. Credentials can be passed via HTTP headers.

### [](#%5Fdefault)Default

Users must have one of the following RBAC roles:

* Full Admin
* Cluster Admin

_Type_ : basic

Refer to [Roles](../learn/security/roles.md) for more details.