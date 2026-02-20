---
title: XDCR Conflict Logging
description: During Active-Active replication, XDCR detects and logs concurrent
  conflicts created by locally connected applications making independent
  modifications, in different clusters but on the same document version. The
  conflict logs are for your information only. The best practice in
  Active-Active systems is that application environments must be designed to
  avoid conflicts.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/learn/pages/clusters-and-availability/xdcr-conflict-logging-feature.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:server:learn:clusters-and-availability/xdcr-conflict-logging-feature.adoc[]
---

[View original HTML](/server/current/learn/clusters-and-availability/xdcr-conflict-logging-feature.html)

# XDCR Conflict Logging

> During Active-Active replication, XDCR detects and logs concurrent conflicts created by locally connected applications making independent modifications, in different clusters but on the same document version. The conflict logs are for your information only. The best practice in Active-Active systems is that application environments must be designed to avoid conflicts. 

During XDCR Active-Active replication, a conflict can occur if different applications connected locally to 2 different clusters, independently modify the same version of the document at around the same time. These simultaneous modifications happen within the convergence window\*, so the changes made in one document are not reflected in the history of the other.

If conflict logging is enabled, XDCR logs these conflict events in a conflict log collection, specified by you, for your information. The conflict logging does not change conflict resolution.

XDCR performs conflict resolution and replicates the documents whether conflicts are logged or not. Conflict logging is informational only, so that you can review the conflict log record documents and the copies of the documents that were in conflict. Use this information when designing your applications to prevent conflicts.

\*A convergence window is a period during which multiple actors, such as users, applications, or clusters, can modify the same document in an active-active topology, before the changes have fully converged across all clusters.

## [](#xdcr-conflict-logger-overview)XDCR Conflict Logger Overview

* Conflict logging is asynchronous and done on a best-effort basis, meaning, not all conflicts may be logged.
* Conflicts are expected to be rare during XDCR replication. If there is an upsurge of conflicts, so that logging conflicts may cause replication issues, XDCR stops logging conflicts temporarily to prioritize replication.
* XDCR may need to pause or stop the logging process due to resource issues or a delay when writing to the log collection. When it needs to pause or stop logging, XDCR reports the error type for the pipeline and continues replication to avoid High Availability issues.
* [Conflict Resolution](xdcr-conflict-resolution.md) process remains unchanged.

> [!IMPORTANT]
> Even if conflict logging fails, XDCR continues with conflict resolution to make sure of High Availability. Conflict resolution is not changed by conflict logging. Conflict logging is informational only.

## [](#using-of-xdcr-conflict-logging)Using the XDCR Conflict Logging Feature

This section summarizes the prerequisites, and how to enable, configure, and use conflict logging in an XDCR replication.

> [!CAUTION]
> Before enabling conflict logging, make sure that the Eventing functions deployed in replicated buckets do not cause excessive conflicts in an XDCR Active-Active environment. The following can cause conflicts:
> 
> * If you’re using the Eventing functions triggered by both replicated and local mutations, and then the Eventing functions update the same document.
> * If the same Eventing functions are deployed in other replication environments.
> 
> To prevent the conflicts caused by Eventing updates to the replicated documents, design Eventing functions with appropriate logic. Make sure the Eventing functions avoid updating the same documents (document IDs) at around the same time in different replication locations.

To log conflicts during an XDCR, follow these steps:

1. As a prerequisite, to enable the conflict logging feature, [Enable the Cross Cluster Versioning](xdcr-enable-crossclusterversioning.md) setting on each bucket of the XDCR topology. Do this by setting the bucket property `enableCrossClusterVersioning` to `true` on all the buckets in the XDCR topology clusters. As a result, additional metadata called, [Hybrid Logical Vector (HLV)](xdcr-enable-crossclusterversioning.md#hlv-data-maintained-in-xattr), also known as version vector, is added to the documents and updated as the documents replicate.  
To enable the bucket property `enableCrossClusterVersioning`:

  * Using the REST API, see [Example: Turning on enableCrossClusterVersioning, when Editing](../../rest-api/rest-bucket-create.md#example-enablecrossclusterversioning-edit).
  * From the UI, see [Edit a Bucket to Enable Cross Cluster Versioning](../../manage/manage-buckets/edit-bucket.md#edit-bucket-for-eccv).  
  > [!NOTE]  
  > * Once `enableCrossClusterVersioning` is enabled, it cannot be disabled. As a result, HLV also cannot be disabled.  
  > * The conflict logging feature detects and logs conflicts only when the property `enableCrossClusterVersioning` is set to `true` for all the buckets in the replication topology. Make sure you set `enableCrossClusterVersioning` to `true` in the bucket properties when adding new buckets or new clusters to the existing replication topology.
2. When creating or updating the XDCR replication, configure and enable conflict logging. You configure conflict logging by specifying the conflict log collections to store the conflict logs and the conflict logging rules. You must specify at least 1 conflict log collection, which is the default.  
When you do not specify any conflict logging rules, all conflicts detected during the replication are logged into the default conflict log collection. The conflict logging rules allow granular configuration of conflict log collections for specific scopes and collections in the replication. You can override the default conflict log collection by either specifying which scopes and collections must have their conflicts logged, or assigning different conflict log collections for each.  
For detailed information about how to enable and configure the conflict logging feature while creating or updating a replication, see the following:

  * [Replication Settings for XDCR Conflict Logging](../../manage/manage-xdcr/create-xdcr-replication.md#xdcr-ui-settings-for-conflict-logging  
  ), to set from the UI.
  * [Creating a Replication](../../rest-api/rest-xdcr-create-replication.md) by [Enabling and Configuring Conflict Logging](#configure-conflictlogging-settings), to set through the REST API.  
  > [!NOTE]  
  > Because conflicts result from race conditions, you must enable conflict logging on all legs of the replications in an XDCR topology. This ensures that at least 1 leg detects and logs the conflict.  
  >  
  > * In a bi-directional replication, configure and enable conflict logging on both legs.  
  > * In a 3-cluster XDCR ring topology, configure and enable conflict logging on all 6 legs.
3. When XDCR logs a conflict, it creates 3 related documents in the conflict log collection specified by you. The 3 documents together is referred to as the [Conflict Record](#conflict-record). As the conflict log collections are regular collections, you can programmatically access and review the documents. For examples about different ways to query or process the conflict log information, see [Viewing Conflict Logs](xdcr-viewing-conflict-logs.md).

## [](#conflict-collection)Conflict Log Collection

A conflict log collection, or conflict collection, is the collection you specify to store conflict event messages and conflicting documents when you configure conflict logging for XDCR replication. Each conflict event creates 3 documents in the conflict log collection; 1 conflict event message document and 2 documents that caused the conflict. Together, these 3 documents form a [Conflict Record](#conflict-record).

For information about how to configure conflict collections, see [Enabling and Configuring Conflict Logging](#configure-conflictlogging-settings).

You can specify any regular collection in the cluster as a conflict log collection, including a collection in the bucket that’s being replicated. The conflict record documents are not replicated.

After XDCR creates conflict record documents in the conflict collection, you are responsible for managing them. XDCR does not update or remove these documents. As these documents are also copies of your application documents, you must use RBAC to make sure of appropriate access to the documents. Make sure to monitor the disk storage use for the conflict log collections and delete documents when they’re no longer needed.

> [!NOTE]
> XDCR adds a system extended attribute (xattrs) called `_xdcr_conflict` into each of the 3 documents in the [Conflict Record](#conflict-record), which prevents XDCR from replicating these 3 documents.

### [](#conflict-record)Conflict Record

A conflict record consists of the following 3 documents:

* **Conflict Record Document (CRD)**: This is a JSON document that records details about the conflict event along with the `docId` of the affected document and the CRD creation timestamp in the ISO 8601 format. The CRD document ID is in the format `crd_<unix_timestamp>_<SHA>`.
* **Source document**: This is a copy of the source document (body and xattrs) that caused the conflict. The Source document ID is in the format `src_<unix_timestamp>_<SHA>`. You can find this document ID in the `srcDoc.id` path of the CRD document.
* **Target document**: This is a copy of the target document (body and xattrs) that caused the conflict. The Target document ID is in the format `tgt_<unix_timestamp>_<SHA>`. You can find this document ID in the `tgtDoc.id` path of the CRD document.

In the description of the conflict record documents, the source and the target indicate replication direction.

The generated `<SHA>` in the ID of the conflict record documents ensures that each conflict event, for the same document or the same document ID, is logged uniquely.

XDCR adds a system extended attribute (xattrs) called `_xdcr_conflict` into each of the 3 documents in the Conflict Record, which prevents XDCR from replicating them.

For query examples to view the conflict record documents, see [Viewing Conflict Logs](xdcr-viewing-conflict-logs.md).

### [](#conflict-record-document-format)Conflict Record Document Format

This is an example of the Conflict Record Document.

```json
{
 "docId": "ae03ecde-203c-4a3b-a6d0-36b60f627c8a",
 "id": "crd_1749454000005461807_e2f416ed317beb4f16a3587656b3d3450e1bec893cabebd3b9bb857d63824da4",
 "replId": "d976db26a5ce512a243db65a3026073f/bucket1/bucket1-nhuUKw2mOVPRiDvcoF4hJg==",
 "srcDoc": {
   "bucketUUID": "fada12469f1027ecb078d2c19a2802fb",
   "cas": 1749453999768928300,
   "clusterUUID": "1bc375a26b7f822ebe91288c58a6c614",
   "collection": "_default",
   "expiry": 0,
   "flags": 0,
   "id": "src_1749454000005461807_e2f416ed317beb4f16a3587656b3d3450e1bec893cabebd3b9bb857d63824da4",
   "isDeleted": false,
   "nodeId": "10.0.32.102",
   "revSeqno": 2,
   "scope": "_default",
   "xattrs": {
     "_mou": "",
     "_sync": "",
     "_vv": ""
   }
 },
 "tgtDoc": {
   "bucketUUID": "6cd3a35ba2d337d84d4fcd30c3a46fb9",
   "cas": 1749453999840231400,
   "clusterUUID": "d976db26a5ce512a243db65a3026073f",
   "collection": "_default",
   "expiry": 0,
   "flags": 0,
   "id": "tgt_1749454000005461807_e2f416ed317beb4f16a3587656b3d3450e1bec893cabebd3b9bb857d63824da4",
   "isDeleted": false,
   "nodeId": "10.0.25.110",
   "revSeqno": 2,
   "scope": "_default",
   "xattrs": {
     "_mou": "",
     "_sync": "",
     "_vv": "{\"cvCas\":\"0x00003dca244f4718\",\"src\":\"ntR6bcR9VHcjcPpQ5osEiw\",\"ver\":\"0x00003dca244f4718\"}"
   }
 },
 "timestamp": "2025-06-09T07:26:40.005Z"
}
```

Some of the key-value pairs in the CRD are as follows:

| Key                    | Value                                                                                                                                                         |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| timestamp              | Date and time of the event in the UTC ISO 8601 format: YYYY-MM-DDThh:mm:ss:SSSZ The timestamp is the system time of the node that noted the conflict.         |
| id/srcDoc.id/tgtDoc.id | CRD document ID prefixed with crd\_. A copy of conflict source document ID prefixed with src\_. A copy of conflict target document ID prefixed with tgt\_.    |
| docId                  | Document ID of the actual document in conflict.                                                                                                               |
| replId                 | Replication ID.                                                                                                                                               |
| srcDoc and tgtDoc      | These JSON Objects have the IDs of the source and target document copies in the conflict collection. The document IDs are located in srcDoc.id and tgtDoc.id. |
| nodeId                 | Node identification, which can be the Hostname or IP address and a port.                                                                                      |
| bucketUUID             | Source/target bucket unique ID.                                                                                                                               |
| cas                    | Source/target document CAS.                                                                                                                                   |
| clusterUUID            | Source/target cluster unique ID.                                                                                                                              |
| isDeleted              | True or false for - is the source/target document deleted?                                                                                                    |
| scope and collection   | Name of the scope and collection where the conflict source/target documents exist.                                                                            |
| revSeqno               | Source/target document’s revision sequence number.                                                                                                            |
| expiry                 | Source/target document’s expiry time.                                                                                                                         |
| flags                  | Source/target document’s flag.                                                                                                                                |
| xattrs                 | System xattributes.                                                                                                                                           |
| \_vv                   | Document version vector. HLV metadata.                                                                                                                        |

### [](#conflict-logger)Conflict Logger

The XDCR Conflict Logger logs conflicts continuously and is designed to minimize the impact on replication performance and system resources.

Conflict logging is performed on a best-effort basis. If system resources are limited or errors occur while writing to the conflict log collection, XDCR prioritizes replication and High Availability. In these cases, conflict logging may be stopped temporarily, meaning that some conflicts will not be logged.

By default, the Conflict Logger is tuned to handle a low percentage of conflicts.

`xdcr_clog_status` is a Prometheus stat, which indicates the status of the Conflict Logger. The status can be one of the following:

* **Hibernated**: The logger is temporarily disabled due to persistent errors or resource constraints.  
> [!NOTE]  
> Hibernation prevents the degradation of the replication performance. Logging is re-enabled after a set interval, or after the errors are manually resolved and the logger is manually restarted.
* **Running**: The logger is actively processing conflict events.
* **DNE**: The logger does not exist; conflict logging is not enabled.

## [](#tunable-replication-settings)Conflict Log Settings

By default, the [Conflict Logger](#conflict-logger) is tuned to handle a low percentage of conflicts.

You can retrieve the conflict logging settings for a replication using the REST API `GET /settings/replications/`. For more information, see [Retrieve Conflict Logging Settings](../../rest-api/rest-xdcr-adv-settings.md#rest-api-conflict-logging-replication-tunables). The conflict logger settings start with the prefix `cLog`.

> [!CAUTION]
> Couchbase recommends that you must not adjust the conflict logger settings unless advised to do so by the Couchbase Support.

The following table explains the conflict logger settings. The `conflictLogging` setting, used to enable and configure logging of conflicts, is explained in [Enabling and Configuring Conflict Logging](#configure-conflictlogging-settings).

| Setting                    | Description                                                                                                                                                                                       | Default  |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| conflictLogging            | The main setting, which when non-empty and valid, enables logging of conflicts. For more information, see [Replication Setting conflictLogging key](#conflictlogging-key).                        |          |
| cLogSetTimeoutMs           | Sets the timeout for SetMeta operation for conflict writing.                                                                                                                                      | 5000ms   |
| cLogPoolGetTimeoutMs       | Timeout for getting connection from connection pool                                                                                                                                               | 5000ms   |
| cLogNetworkRetryCount      | Number of attempts for a single doc when there is a network error                                                                                                                                 | 5        |
| cLogNetworkRetryIntervalMs | Time interval to sleep between attempts to write the conflict doc on network error                                                                                                                | 2000ms   |
| cLogWorkerCount            | Number of workers used by the conflict logger, which write the conflict documents.                                                                                                                | 20       |
| cLogQueueCapacity          | Queue capacity for the conflict logger.                                                                                                                                                           | 6000     |
| cLogMaxErrorCount          | Max number of errors encountered by conflict logger in an Error Window after which the conflict logger is hibernated. For information about hibernation, see [Conflict Logger](#conflict-logger). | 10       |
| cLogErrorTimeWindowMs      | This is the time window in which the number of errors in the conflict logger will be checked.                                                                                                     | 120000ms |
| cLogReattemptDurationMs    | This is the duration for which the conflict logger will be hibernated and after this the logger will be active again. For information about hibernation, see [Conflict Logger](#conflict-logger). | 600000ms |

## [](#configure-conflictlogging-settings)Enabling and Configuring Conflict Logging

The XDCR Conflict Logging feature can be configured and enabled per replication using the advanced replication setting `conflictLogging`. You can use the `conflictLogging` key to specify the storage location for conflict records, and to enable or disable conflict logging.

Configuring `conflictLogging` allows you to define a default conflict collection and, optionally, granular logging rules for scopes and collections via the `loggingRules` object. For more information, see the examples and formats in this section.

To log conflicts, when creating an XDCR replication use the following settings, which accepts a key and a corresponding JSON object as the value.

* [conflictLogging](#conflictlogging-key) is the key.
* [loggingRules](#logging-rules) is a JSON object as the value.

You can also update an existing replication’s conflict logging settings by updating the `conflictLogging` value, which is a part of the [Manage Advanced Settings](../../rest-api/rest-xdcr-adv-settings.md) in XDCR replication.

To configure the key and value:

* From the UI, see [Create a Replication](../../manage/manage-xdcr/create-xdcr-replication.md). For reference, see [Replicate Using Scopes and Collections](../../manage/manage-xdcr/replicate-using-scopes-and-collections.md).
* Using the REST API, when [Creating a Replication](../../rest-api/rest-xdcr-create-replication.md), you need to configure the [conflictLogging key](#conflictlogging-key) and if necessary, the [loggingRules](#logging-rules).

When configuring conflict logging, you must always specify a default conflict log collection. All conflicts from the replication are logged into the default conflict log collection. If the `loggingRules` are specified, then the `loggingRules` override the default setting.

### [](#conflictlogging-key)Replication Setting conflictLogging key

The types of values for the `conflictLogging` key are as follows:

* [Enabled for all conflicts](#enabled-for-all-conflicts)
* [Disabled](#disabled-conflict-logging)
* [Enabled with logging rules](#enabled-with-special-logging-rules)
* [Disabled with logging rules configured](#disabled-with-stored-logging-rules)

> [!NOTE]
> The conflict log collections, or conflict collections, can be any collection in the cluster, including a collection in the bucket that’s being replicated. However, the conflict logs are never replicated. XDCR adds a system extended attribute or xattrs called `_xdcr_conflict` into each of the 3 documents in the [Conflict Records](#conflict-record), which prevents these documents, the conflict logs, from being replicated.

The following examples show how to use `conflictLogging` with the `curl` command option `--data-urlencode`. This demonstrates how to specify the conflict logging settings when creating or updating an XDCR replication using the REST API.

#### [](#enabled-for-all-conflicts)Enabled for all conflicts

To log all conflicts to the same collection for the entire replication:

1. Enable conflict logging by setting `disabled` to `false`.
2. Designate a default conflict collection by specifying the conflict log bucket and the conflict log collection in `bucket` and `collection`.

> [!NOTE]
> You can designate any regular collection as the conflict collection, including collections that are a part of the replication.

**Format**:

```json
--data-urlencode conflictLogging= '{
                        "disabled": false,
                        "bucket": [bucketName],
                        "collection": [scope].[collection],
                        }'
```

**Example**: The conflict logging is enabled and the default conflict collection is `conflictlogsbucket.myappscope.log1collection`. All conflicts in the replication will be logged to the default conflict collection.

```json
--data-urlencode conflictLogging= '{
                        "disabled": false,
                        "bucket": "conflictlogsbucket",
                        "collection": "myappscope.log1collection"
                        }'
```

#### [](#disabled-conflict-logging)Disabled

To disable conflict logging and clear all the `conflictLogging` configuration values, set `--data-urlencode conflictLogging='{}'`.

#### [](#enabled-with-special-logging-rules)Enabled with logging rules

To specify different conflict collection rules for different scopes and collections in your replication, define `loggingRules` in the `conflictLogging` settings.

You can use `loggingRules` to specify, for any scope or collection in the replication, whether the conflicts from that scope or collection must be logged to a different conflict collection or not. If you do not specify the logging rules, then by default, the conflicts from all collections are logged to the default conflict collection.

**Format**:

```json
--data-urlencode conflictLogging= '{
                    "disabled": false,
                    "bucket": [bucketName],
                    "collection": [scope].[collection],
                    "loggingRules": {[logging_rules]},
                    }'
```

**Example**: The conflict logging is enabled. The default conflict collection is the same as in the 1st example, however, `loggingRules` is added. The `conflictLogging` setting defines the following rules:

* Conflict logs for the collection `agents.partners` must be logged to a different collection called `conflictlogsbucket2.myappscope.partnerlogs`
* Conflicts must not be logged for the collection `agents.retailers`.
* Conflict logs for the `inventory` scope must be logged to a collection called `conflictlogsbucket2.myappscope.inventorylogs`.
* Conflict logs for the scopes and collections unaffected by `loggingRules` are stored in the default conflict log collection `conflictlogsbucket1.myappscope.log1collection`.

```json
--data-urlencode conflictLogging= '{
                    "disabled": false,
                    "bucket": "conflictlogsbucket1",
                    "collection": "myappscope.log1collection",
                    "loggingRules": {
                          "agents.partners": {
                                  "bucket": "conflictlogsbucket2",
                                  "collection": "myappscope.partnerlogs"
                                            },
                          "agents.retailers": null,
                          "inventory": {
                                  "bucket": "conflictlogsbucket2",
                                  "collection": "myappscope.inventorylogs"
                                      }
                      }
}'
```

#### [](#disabled-with-stored-logging-rules)Disabled with logging rules configured

You can configure `conflictLogging` (specify the default conflict collection and the `loggingRules`) but not enable `conflictLogging` by setting `disabled` to `true`.

> [!NOTE]
> You can update the replication and set the `conflictLogging` status `disabled` to `true` or `false` at any time.

When you set `"disabled": true` and have specified other configurations, then the specified values are retained.

**Format**:

```json
--data-urlencode conflictLogging= '{
                    "bucket": [bucketName],
                    "collection": [scope].[collection],
                    "loggingRules": {[logging_rules]},
                    "disabled": true,
}'
```

**Example**: Conflict logging is disabled, but the default conflict collection and the logging rules are retained.

```json
--data-urlencode conflictLogging= '{
                    "disabled": true,
                    "bucket": "conflictlogsbucket1",
                    "collection": "myappscope.log1collection",
                    "loggingRules": {
                        "agents.partners": {
                        "bucket": "conflictlogsbucket2",
                        "collection": "myappscope.partnerlogs"
                    },
                    "agents.retailers": null,
                    "inventory": {
                        "bucket": "conflictlogsbucket2",
                        "collection": "myappscope.inventorylogs"
                    }
            }
}'
```

### [](#logging-rules)loggingRules in conflictLogging

Use `loggingRules` to override the [default conflict logging settings](#enabled-for-all-conflicts).

> [!NOTE]
> Conflict logging rules can be saved without enabling the `conflictLogging` setting. However, the logging rules come into effect only when the `conflictLogging` setting is enabled.

You can use the `loggingRules` JSON object to define granular conflict logging rules for specific scopes and collections within a replication.

* You can assign a custom conflict log collection to a specific scope or collection.
* If you set a custom conflict log collection for a scope, all collections within that scope will use the specified collection for conflict records. However, for a collection under the scope, you can do one of the following:

  * Assign a different custom conflict log collection.
  * Specify that the conflict records be put in the default conflict log collection and not in the parent scope’s custom conflict log collection.
* You can specify that conflicts from a scope or a collection must not be logged.

The assigned `loggingRules` override the default setting of putting the conflict records into the default conflict log collection specified for `conflictLogging`. For examples about using loggingRules, see the [Enabled with logging rules example](#enabled-with-special-logging-rules).

The following section explains the key-value formats of the `loggingRules`.

| Key                  | Value                                                                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| -------------------- | -------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \[scope\]            | {} Empty JSON object.                                                            | All conflicts will be logged in the conflict collection defined by bucket and collection in the conflictLogging key.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| \[scope\]            | null                                                                             | All conflicts from the specified scope will not be logged.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| \[scope.collection\] | {}                                                                               | All conflicts from the specified collection will be logged in the conflict collection defined by bucket and collection in the conflictLogging key. You may use this option if the parent scope of the collection has a custom conflict collection, and you want the conflicts from this collection to be logged in the default conflict collection, and not in the parent scope’s custom conflict collection. The default behavior, when you define a custom conflict collection for a scope, is that all the conflicts for the collections in that scope are logged into the scope’s custom conflict collection. |
| \[scope.collection\] | null                                                                             | All conflicts from the specified collection will not be logged.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| \[scope\]            | { “bucket”: \[otherBucket\], “collection”: \[otherScope\].\[otherCollection\]” } | All conflicts from the chosen scope will be logged in the specific conflict collection defined by otherBucket, otherScope, and otherCollection; instead of the original location mentioned in the conflictLogging key.                                                                                                                                                                                                                                                                                                                                                                                            |
| \[scope.collection\] | { “bucket”: \[otherBucket\], “collection”: \[otherScope\].\[otherCollection\]” } | All conflicts from the chosen collection will be logged in the specific conflict collection defined by otherBucket, otherScope, and otherCollection; instead of the original location mentioned in the conflictLogging key.                                                                                                                                                                                                                                                                                                                                                                                       |

## [](#disable-conflict-logging)Disable Conflict Logging

This section explains disabling XDCR Conflict Logging feature.

* **HLV**: The prerequisite to using the XDCR Conflict Logging feature is to enable the bucket property `enableCrossClusterVersioning` on all the buckets of the replication topology. This enables adding or updating the Hybrid Logical Vector (HLV) metadata when the documents are replicated. As the bucket property `enableCrossClusterVersioning` cannot be disabled after it has been enabled, the update and maintenance of HLV metadata by XDCR cannot be disabled.  
For more information, see [XDCR enableCrossClusterVersioning](xdcr-enable-crossclusterversioning.md).
* **Disabling Conflict Logging**: Update the replication setting `conflictLogging` value to `{}` or `{ "disabled": true }` to disable `conflictLogging` and remove previous configuration.  
To keep the other `conflictLogging` configuration settings and only update `"disabled"` to `true`, make sure not to remove the other configuration values. For example, `{"disabled": true, …​}`.  
For configuration information, see [Enabling and Configuring Conflict Logging](#configure-conflictlogging-settings). When `conflictLogging` is disabled, any conflict documents previously created by XDCR in the conflict collections remain in place.
* **Deleting a Replication**: When you delete a replication, conflict record documents in the conflict collection remain until you manually delete them. After XDCR writes the conflict record documents into the conflict collection, you manage the documents. As you can change the conflict collection multiple times during the lifecycle of a replication, XDCR will not clean up or delete previously created conflict record documents.