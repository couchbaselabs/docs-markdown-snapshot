---
title: Query Settings REST API
editUrl: https://github.com/couchbaselabs/cb-swagger/edit/release/8.0/docs/modules/n1ql-rest-settings/pages/index.adoc
pubDate: 2026-06-12T16:31:57.907Z
link: xref:server:n1ql-rest-settings:index.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/n1ql-rest-settings/index.html)

# Query Settings REST API

## [](#overview)Overview

The Query Settings REST API is provided by the Query Service. This API enables you to view or specify cluster-level Query settings.

### Version information

**Version:** 8.0

### Host information

{scheme}://{host}:{port}

The URL scheme, host, and port are as follows.

| Component  | Description                                                                                                                                                                                        |
| ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **scheme** | The URL scheme. Use https for secure access. **Values:** http, https                                                                                                                               |
| **host**   | The host name or IP address of any node in the Couchbase cluster. **Example:** localhost                                                                                                           |
| **port**   | The Cluster administration REST port. Use 18091 for secure access. The port numbers for this REST API are different to the port numbers used by the other Query REST APIs. **Values:** 8091, 18091 |

### Examples on this page

In the HTTP request examples:

* `$BASEPATH` is the URL scheme, host, and port for any node in the Couchbase cluster.
* `$USER` is the user name of an authorized user — see [Security](#security).
* `$PASSWORD` is the password to connect to Couchbase Server.

## [](#resources)Resources

This section describes the operations available with this REST API.

[Retrieve curl Access List](#get%5Faccess)  
[Retrieve Cluster-Level Query Settings](#get%5Fsettings)  
[Update curl Access List](#post%5Faccess)  
[Update Cluster-Level Query Settings](#post%5Fsettings)

### [](#get%5Faccess)Retrieve curl Access List

GET /settings/querySettings/curlWhitelist

#### [](#get%5Faccess-description)Description

Returns the cluster-level curl access settings only.

Produces

* application/json

#### [](#get%5Faccess-responses)Responses

| HTTP Code | Description                                                              | Schema            |
| --------- | ------------------------------------------------------------------------ | ----------------- |
| 200       | An object determining which URLs may be accessed by the CURL() function. | [Access](#Access) |

#### [](#get%5Faccess-security)Security

| Type         | Name                         |
| ------------ | ---------------------------- |
| http (basic) | [Default](#security-Default) |

#### [](#get%5Faccess-ex-curl)Example HTTP Request

This example gets the current cluster-level curl access settings.

```sh
curl -v -u $USER:$PASSWORD \
  $BASEPATH/settings/querySettings/curlWhitelist
```

#### [](#get%5Faccess-ex-response)Example HTTP Response

Response 200

```json
{
  "all_access" : false,
  "allowed_urls" : [ ],
  "disallowed_urls" : [ ]
}
```

### [](#get%5Fsettings)Retrieve Cluster-Level Query Settings

GET /settings/querySettings

#### [](#get%5Fsettings-description)Description

Returns all cluster-level query settings, including the curl access settings.

Produces

* application/json

#### [](#get%5Fsettings-responses)Responses

| HTTP Code | Description                                    | Schema                |
| --------- | ---------------------------------------------- | --------------------- |
| 200       | An object giving cluster-level query settings. | [Settings](#Settings) |

#### [](#get%5Fsettings-security)Security

| Type         | Name                         |
| ------------ | ---------------------------- |
| http (basic) | [Default](#security-Default) |

#### [](#get%5Fsettings-ex-curl)Example HTTP Request

This example gets the current cluster-level curl query settings.

```sh
curl -v -u $USER:$PASSWORD \
  $BASEPATH/settings/querySettings
```

#### [](#get%5Fsettings-ex-response)Example HTTP Response

Response 200

```json
{
  "queryTmpSpaceDir" : "/opt/couchbase/var/lib/couchbase/tmp",
  "queryTmpSpaceSize" : 5120,
  "queryPipelineBatch" : 16,
  "queryPipelineCap" : 512,
  "queryScanCap" : 512,
  "queryTimeout" : 0,
  "queryPreparedLimit" : 16384,
  "queryCompletedLimit" : 4000,
  "queryCompletedThreshold" : 1000,
  "queryLogLevel" : "info",
  "queryMaxParallelism" : 1,
  "queryTxTimeout" : "0ms",
  "queryMemoryQuota" : 0,
  "queryUseCBO" : true,
  "queryCleanupClientAttempts" : true,
  "queryCleanupLostAttempts" : true,
  "queryCleanupWindow" : "60s",
  "queryNumAtrs" : 1024,
  "queryNodeQuota" : 0,
  "queryUseReplica" : "unset",
  "queryNodeQuotaValPercent" : 67,
  "queryNumCpus" : 0,
  "queryCompletedMaxPlanSize" : 262144,
  "queryN1QLFeatCtrl" : 76,
  "queryCurlWhitelist" : {
    "all_access" : false
  }
}
```

### [](#post%5Faccess)Update curl Access List

POST /settings/querySettings/curlWhitelist

#### [](#post%5Faccess-description)Description

Updates the cluster-level curl access settings only.

Consumes

* application/json
* application/x-www-form-urlencoded

Produces

* application/json

#### [](#post%5Faccess-parameters)Parameters

Body Parameter

| Name             | Description                                                              | Schema            |
| ---------------- | ------------------------------------------------------------------------ | ----------------- |
| **Body**optional | An object determining which URLs may be accessed by the CURL() function. | [Access](#Access) |

#### [](#post%5Faccess-responses)Responses

| HTTP Code | Description                                                                                            | Schema            |
| --------- | ------------------------------------------------------------------------------------------------------ | ----------------- |
| 200       | An object determining which URLs may be accessed by the CURL() function, including the latest changes. | [Access](#Access) |
| 400       | Returns an error message if a parameter or value is incorrect.                                         | Object            |

#### [](#post%5Faccess-security)Security

| Type         | Name                         |
| ------------ | ---------------------------- |
| http (basic) | [Default](#security-Default) |

#### [](#post%5Faccess-ex-curl)Example HTTP Request

This example specifies that `<https://company1.com>` is allowed, and `<https://company2.com>` is disallowed.

```sh
curl -v -X POST -u $USER:$PASSWORD \
  $BASEPATH/settings/querySettings/curlWhitelist \
  -H 'Content-Type: application/json' \
  -d '{"all_access": false,
       "allowed_urls": ["https://company1.com"],
       "disallowed_urls": ["https://company2.com"]}'
```

#### [](#post%5Faccess-ex-request)Example Request Body

```json
{
  "all_access" : false,
  "allowed_urls" : [ "https://company1.com" ],
  "disallowed_urls" : [ "https://company2.com" ]
}
```

#### [](#post%5Faccess-ex-response)Example HTTP Response

Response 200

```json
{
  "all_access" : false,
  "allowed_urls" : [ "https://company1.com" ],
  "disallowed_urls" : [ "https://company2.com" ]
}
```

### [](#post%5Fsettings)Update Cluster-Level Query Settings

POST /settings/querySettings

#### [](#post%5Fsettings-description)Description

Updates cluster-level query settings, including the curl access settings.

Consumes

* application/json
* application/x-www-form-urlencoded

Produces

* application/json

#### [](#post%5Fsettings-parameters)Parameters

Body Parameter

| Name             | Description                                        | Schema                |
| ---------------- | -------------------------------------------------- | --------------------- |
| **Body**optional | An object specifying cluster-level query settings. | [Settings](#Settings) |

#### [](#post%5Fsettings-responses)Responses

| HTTP Code | Description                                                                  | Schema                |
| --------- | ---------------------------------------------------------------------------- | --------------------- |
| 200       | An object giving cluster-level query settings, including the latest changes. | [Settings](#Settings) |
| 400       | Returns an error message if a parameter or value is incorrect.               | Object                |

#### [](#post%5Fsettings-security)Security

| Type         | Name                         |
| ------------ | ---------------------------- |
| http (basic) | [Default](#security-Default) |

#### [](#post%5Fsettings-ex-curl)Example HTTP Request

This example changes the temp file directory to `/tmp` and the temp file size to 2048 MB.

```sh
curl -v -X POST -u $USER:$PASSWORD \
  $BASEPATH/settings/querySettings \
  -d 'queryTmpSpaceDir=/tmp' \
  -d 'queryTmpSpaceSize=2048'
```

#### [](#post%5Fsettings-ex-request)Example Request Body

Partial Settings

```json
{
  "queryTmpSpaceDir" : "/tmp",
  "queryTmpSpaceSize" : 2048,
  "queryCurlWhitelist" : {
    "all_access" : false
  }
}
```

All Settings

```json
{
  "queryTmpSpaceDir" : "/tmp",
  "queryTmpSpaceSize" : 2048,
  "queryPipelineBatch" : 16,
  "queryPipelineCap" : 512,
  "queryScanCap" : 512,
  "queryTimeout" : 0,
  "queryPreparedLimit" : 16384,
  "queryCompletedLimit" : 4000,
  "queryCompletedThreshold" : 1000,
  "queryLogLevel" : "info",
  "queryMaxParallelism" : 1,
  "queryTxTimeout" : "0ms",
  "queryMemoryQuota" : 0,
  "queryUseCBO" : true,
  "queryCleanupClientAttempts" : true,
  "queryCleanupLostAttempts" : true,
  "queryCleanupWindow" : "60s",
  "queryNumAtrs" : 1024,
  "queryNodeQuota" : 0,
  "queryUseReplica" : "unset",
  "queryNodeQuotaValPercent" : 67,
  "queryNumCpus" : 0,
  "queryCompletedMaxPlanSize" : 262144,
  "queryN1QLFeatCtrl" : 76,
  "queryCurlWhitelist" : {
    "all_access" : false
  }
}
```

#### [](#post%5Fsettings-ex-response)Example HTTP Response

Response 200

```json
{
  "queryTmpSpaceDir" : "/tmp",
  "queryTmpSpaceSize" : 2048,
  "queryPipelineBatch" : 16,
  "queryPipelineCap" : 512,
  "queryScanCap" : 512,
  "queryTimeout" : 0,
  "queryPreparedLimit" : 16384,
  "queryCompletedLimit" : 4000,
  "queryCompletedThreshold" : 1000,
  "queryLogLevel" : "info",
  "queryMaxParallelism" : 1,
  "queryTxTimeout" : "0ms",
  "queryMemoryQuota" : 0,
  "queryUseCBO" : true,
  "queryCleanupClientAttempts" : true,
  "queryCleanupLostAttempts" : true,
  "queryCleanupWindow" : "60s",
  "queryNumAtrs" : 1024,
  "queryNodeQuota" : 0,
  "queryUseReplica" : "unset",
  "queryNodeQuotaValPercent" : 67,
  "queryNumCpus" : 0,
  "queryCompletedMaxPlanSize" : 262144,
  "queryN1QLFeatCtrl" : 76,
  "queryCurlWhitelist" : {
    "all_access" : false
  }
}
```

## [](#models)Definitions

This section describes the properties consumed and returned by this REST API.

[Access](#Access)  
[Settings](#Settings)

### [](#Access)Access

 Object

| Property                     |                                                                                                                                                                                                                                                                                                                                                                                                                                               | Schema       |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| **all\_access**required      | Defines whether the user has access to all URLs, or only URLs specified by the access list. This field set must be set to false to enable the allowed\_urls and disallowed\_urls fields. Setting this field to true enables access to all endpoints.                                                                                                                                                                                          | Boolean      |
| **allowed\_urls**optional    | An array of strings, each of which is a URL to which you wish to grant access. Each URL is a prefix match. The CURL() function will allow any URL that starts with this value. For example, if you wish to allow access to all Google APIs, add the URL https://maps.googleapis.com to the array. To allow complete access to localhost, use http://localhost. Each URL must include the port, protocol, and all other components of the URL. | String array |
| **disallowed\_urls**optional | An array of strings, each of which is a URL that will be restricted for all roles. Each URL is a prefix match. The CURL() function will disallow any URL that starts with this value. If both allowed\_urls and disallowed\_urls fields are populated, the disallowed\_urls field takes precedence over allowed\_urls. Each URL must include the port, protocol, and all other components of the URL.                                         | String array |

### [](#Settings)Settings

 Object

| Property                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Schema            |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| **queryCleanupClientAttempts**optional | When enabled, the Query Service preferentially aims to clean up just transactions that it has created, leaving transactions for the distributed cleanup process only when it's forced to. The [node-level](../n1ql-rest-admin/index.html#cleanupclientattempts) cleanupclientattempts setting specifies this property for a single node. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. **Default:** true **Example:** false                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Boolean           |
| **queryCleanupLostAttempts**optional   | When enabled, the Query Service takes part in the distributed cleanup process, and cleans up expired transactions created by any client. The [node-level](../n1ql-rest-admin/index.html#cleanuplostattempts) cleanuplostattempts setting specifies this property for a single node. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. **Default:** true **Example:** false                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Boolean           |
| **queryCleanupWindow**optional         | Specifies how frequently the Query Service checks its subset of [active transaction records](/server/8.0/learn/data/transactions.html#active-transaction-record-entries) for cleanup. Decreasing this setting causes expiration transactions to be found more swiftly, with the tradeoff of increasing the number of reads per second used for the scanning process. The value for this setting is a string. Its format includes an amount and a mandatory unit, e.g. 10ms (10 milliseconds) or 0.5s (half a second). Valid units are: ns (nanoseconds) us (microseconds) ms (milliseconds) s (seconds) m (minutes) h (hours) The [node-level](../n1ql-rest-admin/index.html#cleanupwindow) cleanupwindow setting specifies this property for a single node. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. **Default:** "60s" **Example:** "30s"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | String (duration) |
| **queryCompletedLimit**optional        | Sets the number of requests to be logged in the completed requests catalog. As new completed requests are added, old ones are removed. Increase this when the completed request keyspace is not big enough to track the slow requests, such as when you want a larger sample of slow requests. For more information and examples, see [Configure the Completed Requests](../n1ql/n1ql-manage/monitoring-n1ql-query.html#sys-completed-config). The [node-level](../n1ql-rest-admin/index.html#completed-limit) completed-limit setting specifies this property for a single node. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. **Default:** 4000 **Example:** 7000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Integer (int32)   |
| **queryCompletedMaxPlanSize**optional  | A plan size in bytes. Limits the size of query execution plans that can be logged in the completed requests catalog. Values larger than the maximum limit are silently treated as the maximum limit. Queries with plans larger than this are not logged. You must obtain execution plans for such queries via profiling or using the EXPLAIN statement. For more information, see [Configure the Completed Requests](../n1ql/n1ql-manage/monitoring-n1ql-query.html#sys-completed-config). The [node-level](../n1ql-rest-admin/index.html#completed-max-plan-size) completed-max-plan-size setting specifies this property for a single node. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. **Default:** 262144 **Minimum:** 0 **Maximum:** 20840448                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Integer (int32)   |
| **queryCompletedThreshold**optional    | A duration in milliseconds. All completed queries lasting longer than this threshold are logged in the completed requests catalog. Specify 0 to track all requests, independent of duration. Specify any negative number to track none. For more information and examples, see [Configure the Completed Requests](../n1ql/n1ql-manage/monitoring-n1ql-query.html#sys-completed-config). The [node-level](../n1ql-rest-admin/index.html#completed-threshold) completed-threshold setting specifies this property for a single node. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. **Default:** 1000 **Example:** 7000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Integer (int32)   |
| **queryLogLevel**optional              | Log level used in the logger. All values, in descending order of data: DEBUG — For developers. Writes everything. TRACE — For developers. Less info than DEBUG. INFO — For admin & customers. Lists warnings & errors. WARN — For admin. Only abnormal items. ERROR — For admin. Only errors to be fixed. SEVERE — For admin. Major items, like crashes. NONE — Does not write anything. The [node-level](../n1ql-rest-admin/index.html#loglevel) loglevel setting specifies this property for a single node. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. **Values:** "DEBUG", "TRACE", "INFO", "WARN", "ERROR", "SEVERE", "NONE" **Default:** "INFO" **Example:** "DEBUG"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | String            |
| **queryMaxParallelism**optional        | Specifies the maximum parallelism for queries on all Query nodes in the cluster. If the value is zero or negative, the maximum parallelism is restricted to the number of allowed cores. Similarly, if the value is greater than the number of allowed cores, the maximum parallelism is restricted to the number of allowed cores. (The number of allowed cores is the same as the number of logical CPUs. In Couchbase Server Community Edition, the number of allowed cores cannot be greater than 4\. In Couchbase Server Enterprise Edition, there is no limit to the number of allowed cores.) For more information, see [Max Parallelism](../n1ql/n1ql-language-reference/index-partitioning.html#max-parallelism). The [node-level](../n1ql-rest-admin/index.html#max-parallelism-srv) max-parallelism setting specifies this property for a single node. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. In addition, there is a [request-level](../n1ql-rest-query/index.html#max%5Fparallelism%5Freq) max\_parallelism parameter. If a request includes this parameter, it will be capped by the node-level max-parallelism setting. NOTE: To enable queries to run in parallel, you must specify the cluster-level queryMaxParallelism parameter, or specify the node-level max-parallelism parameter on all Query nodes. **Default:** 1 **Example:** 0                                                                                                                                                          | Integer (int32)   |
| **queryMemoryQuota**optional           | Specifies the maximum amount of memory a request may use on any Query node in the cluster, in MB. This parameter enforces a ceiling on the memory used for the tracked documents required for processing a request. It does not take into account any other memory that might be used to process a request, such as the stack, the operators, or some intermediate values. Within a transaction, this setting enforces the memory quota for the transaction by tracking the delta table and the transaction log (approximately). The [node-level](../n1ql-rest-admin/index.html#memory-quota-srv) memory-quota setting specifies this property for a single node. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. In addition, there is a [request-level](../n1ql-rest-query/index.html#memory%5Fquota%5Freq) memory\_quota parameter. If a request includes this parameter, it will be capped by the node-level memory-quota setting. **Default:** 0 **Example:** 4                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Integer (int32)   |
| **queryN1QLFeatCtrl**optional          | SQL++ feature control. This setting is provided for technical support only. The [node-level](../n1ql-rest-admin/index.html#n1ql-feat-ctrl) n1ql-feat-ctrl setting specifies this property for a single node. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Integer (int32)   |
| **queryNodeQuota**optional             | Sets the soft memory limit for the Query Service on every Query node in the cluster, in MB. The garbage collector tries to keep below this target. It's not a hard, absolute limit, and memory usage may exceed this value. When set to 0 (the default), the Query Service sets a default soft memory limit for every node. To do this, the Query Service calculates the difference between the total system RAM and 90% of the total system RAM: Total System RAM - (0.9 \* Total System RAM) If the difference is greater than 8 GiB, the default soft memory limit is set to the total system RAM minus 8 GiB. If the difference is 8 GiB or less, the default soft memory limit is set to 90% of the total system RAM. The [node-level](../n1ql-rest-admin/index.html#node-quota) node-quota setting specifies this property for a single node. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. **Default:** 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Integer (int32)   |
| **queryNodeQuotaValPercent**optional   | The percentage of the queryNodeQuota that's dedicated to tracked value content memory across all active requests for every Query node in the cluster. (The queryMemoryQuota setting specifies the maximum amount of document memory an individual request may use on any Query node in the cluster.) The [node-level](../n1ql-rest-admin/index.html#node-quota-val-percent) node-quota-val-percent setting specifies this property for a single node. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. **Default:** 67 **Minimum:** 0 **Maximum:** 100                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Integer (int32)   |
| **queryNumAtrs**optional               | Specifies the total number of [active transaction records](/server/8.0/learn/data/transactions.html#active-transaction-record-entries) for all Query nodes in the cluster. The [node-level](../n1ql-rest-admin/index.html#numatrs-srv) numatrs setting specifies this property for a single node. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. **Default:** 1024 **Minimum:** 0 (exclusive) **Example:** 512                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Integer (int32)   |
| **queryNumCpus**optional               | The number of CPUs the Query Service can use on any Query node in the cluster. This setting requires a restart of the Query Service to take effect. When set to 0 (the default), the Query Service can use all available CPUs, up to the limits described below. The number of CPUs can never be greater than the number of logical CPUs. In Couchbase Server Community Edition, the number of allowed CPUs cannot be greater than 4\. In Couchbase Server Enterprise Edition, there is no limit to the number of allowed CPUs. The [node-level](../n1ql-rest-admin/index.html#num-cpus) num-cpus setting specifies this property for a single node. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. **Default:** 0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Integer (int32)   |
| **queryPipelineBatch**optional         | Controls the number of items execution operators can batch for Fetch from the KV. The [node-level](../n1ql-rest-admin/index.html#pipeline-batch-srv) pipeline-batch setting specifies this property for a single node. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. In addition, the [request-level](../n1ql-rest-query/index.html#pipeline%5Fbatch%5Freq) pipeline\_batch parameter specifies this property per request. The minimum of that and the node-level pipeline-batch setting is applied. **Default:** 16 **Example:** 64                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Integer (int32)   |
| **queryPipelineCap**optional           | Maximum number of items each execution operator can buffer between various operators. The [node-level](../n1ql-rest-admin/index.html#pipeline-cap-srv) pipeline-cap setting specifies this property for a single node. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. In addition, the [request-level](../n1ql-rest-query/index.html#pipeline%5Fcap%5Freq) pipeline\_cap parameter specifies this property per request. The minimum of that and the node-level pipeline-cap setting is applied. **Default:** 512 **Example:** 1024                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Integer (int32)   |
| **queryPreparedLimit**optional         | Maximum number of prepared statements in the cache. When this cache reaches the limit, the least recently used prepared statements will be discarded as new prepared statements are created. The [node-level](../n1ql-rest-admin/index.html#prepared-limit) prepared-limit setting specifies this property for a single node. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. **Default:** 16384 **Example:** 65536                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Integer (int32)   |
| **queryScanCap**optional               | Maximum buffered channel size between the indexer client and the Query Service for index scans. This parameter controls when to use scan backfill. Use 0 or a negative number to disable. Smaller values reduce GC, while larger values reduce indexer backfill. The [node-level](../n1ql-rest-admin/index.html#scan-cap-srv) scan-cap setting specifies this property for a single node. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. In addition, the [request-level](../n1ql-rest-query/index.html#scan%5Fcap%5Freq) scan\_cap parameter specifies this property per request. The minimum of that and the node-level scan-cap setting is applied. **Default:** 512 **Example:** 1024                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Integer (int32)   |
| **queryTimeout**optional               | Maximum time to spend on the request before timing out (ns). The value for this setting is an integer, representing a duration in nanoseconds. It must not be delimited by quotes, and must not include a unit. Specify 0 (the default value) or a negative integer to disable. When disabled, no timeout is applied and the request runs for however long it takes. The [node-level](../n1ql-rest-admin/index.html#timeout-srv) timeout setting specifies this property for a single node. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. In addition, the [request-level](../n1ql-rest-query/index.html#timeout%5Freq) timeout parameter specifies this property per request. The minimum of that and the node-level timeout setting is applied. **Default:** 0 **Example:** 500000000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | Long (int64)      |
| **queryTxTimeout**optional             | Maximum time to spend on a transaction before timing out. This setting only applies to requests containing the BEGIN TRANSACTION statement, or to requests where the [tximplicit](../n1ql-rest-query/index.html#tximplicit) parameter is set. For all other requests, it's ignored. The value for this setting is a string. Its format includes an amount and a mandatory unit, e.g. 10ms (10 milliseconds) or 0.5s (half a second). Valid units are: ns (nanoseconds) us (microseconds) ms (milliseconds) s (seconds) m (minutes) h (hours) Specify 0ms (the default value) to disable. When disabled, no timeout is applied and the transaction runs for however long it takes. The [node-level](../n1ql-rest-admin/index.html#txtimeout-srv) txtimeout setting specifies this property for a single node. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. In addition, there is a [request-level](../n1ql-rest-query/index.html#txtimeout%5Freq) txtimeout parameter. If a request includes this parameter, it will be capped by the node-level txtimeout setting. **Default:** "0ms" **Example:** "0.5s"                                                                                                                                                                                                                                                                                                                                                                                                                 | String (duration) |
| **queryTmpSpaceDir**optional           | The path to which the Index Service writes temporary backfill files, and the Query Service writes spill files, to store any transient data during query processing. The specified path must already exist. Only absolute paths are allowed. The default path is var/lib/couchbase/tmp within the Couchbase Server installation directory. **Example:** "/opt/couchbase/var/lib/couchbase/tmp"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | String            |
| **queryTmpSpaceSize**optional          | In MiB, the maximum size of temporary backfill files for each indexer, and the maximum size of temporary files for spilled sorting and other operations. In a cluster with both secondary indexing and full text search, the limit for disk space use is three times this setting. Setting the size to 0 disables backfill. Setting the size to \-1 means the size is unlimited. The maximum size is limited only by the available disk space. **Default:** 5120 **Example:** 2048                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Integer (int32)   |
| **queryUseCBO**optional                | Specifies whether the cost-based optimizer is enabled. The [node-level](../n1ql-rest-admin/index.html#use-cbo-srv) use-cbo setting specifies this property for a single node. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. In addition, the [request-level](../n1ql-rest-query/index.html#use%5Fcbo%5Freq) use\_cbo parameter specifies this property per request. If a request does not include this parameter, the node-level setting is used, which defaults to true. **Default:** true **Example:** false                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Boolean           |
| **queryUseReplica**optional            | Specifies whether a query can fetch data from a replica vBucket if active vBuckets are inaccessible. The possible values are: off — read from replica is disabled for all queries and cannot be overridden at request level. on — read from replica is enabled for all queries, but can be disabled at request level. unset — read from replica is enabled or disabled at request level. Do not enable read from replica when you require consistent results. Only SELECT queries that are not within a transaction can read from replica. Reading from replica is only possible if the cluster uses Couchbase Server 7.6.0 or later. You cannot currently start KV range scans on a replica vBucket. If a query uses sequential scan and a data node becomes unavailable, the query might return an error, even if read from replica is enabled for the request. The [node-level](../n1ql-rest-admin/index.html#use-replica-srv) use-replica setting specifies this property for a single node. When you change the cluster-level setting, the node-level setting is over-written for all nodes in the cluster. In addition, the [request-level](../n1ql-rest-query/index.html#use%5Freplica%5Freq) use\_replica parameter specifies this property per request. If a request does not include this parameter, or if the request-level parameter is unset, the node-level setting is used. If the request-level parameter and the node-level setting are both unset, read from replica is disabled for that request. **Values:** "off", "on", "unset" **Default:** "unset" **Example:** "on" | String            |
| **queryCurlWhitelist**optional         | An object which determines which URLs may be accessed by the CURL() function.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | [Access](#Access) |

## [](#security)Security

The Query Settings REST API supports HTTP basic authentication. Pass your credentials through HTTP headers.

### [](#security-Default)Default

Users must have one of the following RBAC roles:

* Full Admin
* Cluster Admin

**Type:** http

For more information, see [Roles](../learn/security/roles.md).

## [](#see-also)See Also

* For node-level settings, see the [Query Admin REST API](../n1ql-rest-admin/index.md#Settings).
* For request-level parameters, see the [Query Service REST API](../n1ql-rest-query/index.md#Request).