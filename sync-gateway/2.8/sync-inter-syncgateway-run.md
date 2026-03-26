---
title: Initialize Inter-Sync Gateway Replications
description: Initializing and running inter-Sync Gateway replication
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/sync-inter-syncgateway-run.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.8@sync-gateway::sync-inter-syncgateway-run.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/sync-inter-syncgateway-run.html)

# Initialize Inter-Sync Gateway Replications

> Initializing and running inter-Sync Gateway replication  

_Related inter-syncgateway topics_: [Overview](../current/sync/sync-inter-syncgateway-overview.md) | Run | [Manage](../current/sync/sync-inter-syncgateway-manage.md) | [Monitor](../current/sync/sync-inter-syncgateway-monitor.md) | [Conflict](../current/sync/sync-inter-syncgateway-conflict-resolution.md)

_Other related topics_: [Configuration Properties](../current/configuration/configuration-properties-legacy.md) | [Admin REST API](../current/rest-api/rest-api-admin.md)

> [!CAUTION]
> Context Clarification
> 
> This content relates only to inter-Sync Gateway replication in Sync Gateway 2.8+. For documentation on pre-2.8 inter-Sync Gateway replication (also known as SG Replicate) — see [SG-Replicate](#sync-gateway::legacy-sg-replicate.adoc)

## [](#introduction)Introduction

Replications are initialized by submitting a [replication definition![glossary icon](_images/icons/glossaryIconImage2.png)](glossary.md#replication-definition) using either:

* A 'JSON' configuration file (`sync-gateway-config.json`)
* The Admin REST API, using a utility such as `curl`, or an application such as _Postman_.

Wherever they are defined, the elements of a replication definition are the same, with the exception of these Admin REST API only elements:

* `adhoc` — Use this to specify that the replication is ad hoc \[[1](#%5Ffootnotedef%5F1 "View footnote.")\].
* `cancel` — Use this to cancel on-going replications \[[1](#%5Ffootnotedef%5F1 "View footnote.")\].

Example 1\. Replication Characteristics Highlights

* Replication highlights
* Running highlights

* There are two types of replication: persistent and ad hoc (REST API only).
* Replications of both types can run in one-shot or continuous replications modes.
* All replications involve at least one local database.
* Replications can be configured to purge documents when channel access is revoked (a removal notification is received).
* Persistent continuous replications can be:

  * Reset — a [checkpoint![glossary icon](_images/icons/glossaryIconImage2.png)](glossary.md#checkpoint) can be reset to zero
  * Updated — only the parameter values provided in the PUT request body will be updated
* Persistent and ad hoc replications can be:

  * Removed — only the replication\_id is needed to delete ongoing continuous or one-shot replications.
* [ENTERPRISE EDITION](https://www.couchbase.com/products/editions) only:

  * Replications can use delta-sync mode, whereby only the changed data-items are replicated.

* Multiple identical replicators can be initiated on a Sync Gateway node provided each has a unique `replication_Id`.
* inter-Sync Gateway replications introduced in Sync Gateway 2.8 as well as SG-Replicate can run on the same node, but you must ensure that they each have a different `replication_id`.
* The user under which replication is being run must have read and write access to the data being replicated.
* Exponential backoff when connection lost; this can be customized using the [max\_backoff\_time](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-replications-this%5Frep-max%5Fbackoff%5Ftime) configuration setting.
* replications will continue trying to connect for 30 minutes following authentication failure (including user-invalid/doesn't exist).
* Running replications can be stopped. Stopped replications can be (re)Started.
* If ALL the Sync Gateway nodes in a source or target Sync Gateway cluster go down in the middle of continuous replication, by default, the system should pick up from the last document that was successfully processed by both sides when the replication/cluster is restarted
* REST ONLY

  * POST databases/{db}/\_replication creates a replication using the replication ID specified in the body or if none specified, a unique UUID.
  * PUT databases/{db}/\_replication/{replicationID} upserts the replication with the specified ID.
* [ENTERPRISE EDITION](https://www.couchbase.com/products/editions) only:

  * Replications are distributed even across all available Sync Gateway nodes and so are not guaranteed to run on their originating node.
  * If a multi-node Sync Gateway cluster loses a subset of sync gateway nodes, the remaining nodes continue replication uninterrupted IF they have been configured to handle the replication (continuous and one-shot replications).

## [](#replication-definition)Replication Definition

All replications are 'initialized' by a [replication definition![glossary icon](_images/icons/glossaryIconImage2.png)](glossary.md#replication-definition) in the configuration file or Admin REST API and operate within the context of a local database.

* Configured replications use the `database.{db-name}.replications` property to add a replication definition to a local database.
* REST API replications specify the local database and replication identity in the API POST/PUT request. Providing the replication definition parameters in the request body as a JSON string.

Both scenarios are covered in [Example 2](#replication-properties). It summarizes the [replication definition![glossary icon](_images/icons/glossaryIconImage2.png)](glossary.md#replication-definition) elements\[[2](#%5Ffootnotedef%5F2 "View footnote.")\], which are covered in more detail in [Configuration Properties](../current/configuration/configuration-properties-legacy.md).

### [](#database-level-settings)Database-level Settings

A number of database-level options are also especially relevant to Inter-Sync Gateway Replication, including:

* [sgreplicate\_enabled](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-sgreplicate%5Fenabled) — use this [ENTERPRISE EDITION](https://www.couchbase.com/products/editions) setting to allow the database to participate in Inter-Sync Gateway Replications.
* [this\_db.delta\_sync](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-delta%5Fsync) — use this setting to enable delta-sync replication on the database, it must be set if you want to use delta-sync in your _replication definition_.
* [sgreplicate\_websocket\_heartbeat\_secs](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-sgreplicate%5Fwebsocket%5Fheartbeat%5Fsecs) — use this setting to override the default (5 minute) heartbeat interval for websocket ping frames for this database.
* [sync](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-sync) — use this setting to specify the sync function logic — this is an essential part of access-control.
* [unsupported.sgr\_tls\_skip\_verify](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-unsupported-sgr%5Ftls%5Fskip%5Fverify) — use this unsupported option to make development an testing easier by skipping verification of TLS certificates.

### [](#replication-level-settings)Replication-level Settings

Example 2\. Replication Definition

* Summary of Parameters
* Configured Example
* REST API Example

This table summarize all the available configurable items. It includes a link to a detailed description of each.

| Name and Link                                                                                                                                                      | Summary                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| [adhoc](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-replications-this%5Frep-adhoc)                                             | REST API ONLYUse the Admin REST API's adhoc parameter to specify that a replication is ad hoc rather than persistent.                                |
| [batch\_size](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-replications-this%5Frep-batch%5Fsize)                                | Use batch\_size to specify the number of changes to be included in a single batch during replication.                                                |
| [cancel](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-replications-this%5Frep-cancel)                                           | REST API ONLYUse the Admin REST API's cancel parameter only when you want to want to cancel an existing active replication.                          |
| [conflict\_resolution\_type](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-replications-this%5Frep-conflict%5Fresolution%5Ftype) | Use conflict\_resolution\_type to specify how Sync Gateway should resolve conflicts. By default the automatic conflict resolution policy is applied. |
| [continuous](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-replications-this%5Frep-continuous)                                   | Use continuous to specify whether this replication will run continuously, or be one-shot.                                                            |
| [custom\_conflict\_resolver](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-replications-this%5Frep-custom%5Fconflict%5Fresolver) | Use custom\_conflict\_resolver to provide the Javascript function used to resolve conflicts if "conflict\_resolution\_type": "custom".               |
| [direction](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-replications-this%5Frep-direction)                                     | Use direction to specify the replication is **push**, **pull** or **pushAndPull** relative to this node.                                             |
| [enable\_delta\_sync](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-replications-this%5Frep-enable%5Fdelta%5Fsync)               | Use enable\_delta\_sync to specify use of delta sync for a replication.                                                                              |
| [filter](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-replications-this%5Frep-filter)                                           | Use filter to specify the name of the function to be used to filter documents.                                                                       |
| [max\_backoff\_time](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-replications-this%5Frep-max%5Fbackoff%5Ftime)                 | Use max\_backoff\_time to specify the number of minutes Sync Gateway will spend trying to reconnect lost or unreachable remote targets.              |
| [purge\_on\_removal](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-replications-this%5Frep-purge%5Fon%5Fremoval)                 | Use purge\_on\_removal to specify (per replication) whether removing a channel should trigger a purge.                                               |
| [query\_params](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-replications-this%5Frep-query%5Fparams)                            | Use query\_params to specify the key/value pairs to be passed to the filter named in filter.                                                         |
| [remote](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-replications-this%5Frep-remote)                                           | Use remote to specify the database endpoint on the remote Sync Gateway custer.                                                                       |
| [replication\_id](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-replications-this%5Frep-replication%5Fid)                        | Use replication\_id to specify an identifying name for the replication.                                                                              |
| [initial\_state](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-replications-this%5Frep-initial%5Fstate)                          | Use initial\_state to specify the state in which to launch the replication.                                                                          |

This is an example of a replication definition. Its purpose is to illustrate all configurable items in use and so should not be considered a working example.

It creates a replication with the replication\_ID of `db1-rep-id1-pull-oneshot` on a local database `db1-local_`, pulling data from a remote database `db1-remote`.

```json
"databases": {
 " db1": {                                                (1)
    "bucket":"db1",
    "server": "couchbase://cb-server",
    // ... other DB config ..
    "sgreplicate_enabled": true,                          (2)
    "replications":
      "db1-rep-id1-pull-oneshot":                         (3)
        "direction": "pull",                              (4)
        "remote": "https://example.com:4984/remote_db1",
        "user": "user1",                                  (5)
        "password": "password",
        "batch_size": 1000,                               (6)
        "conflict_resolution_type": "custom",             (7)
        "custom_conflict_resolver": "",                   (8)
        "continuous": false,                              (9)
        "enable_delta_sync": false,                       (10)
        "filter": "sync_gateway/bychannel",               (11)
        "query_params": ["channel.user1"]                 (12)
        "max_backoff_time": 5,                            (13)
        "purge_on_removal": false                         (14)
        "state": "running"                                (15)
    }
  }
```

| **1**  | All replications are defined at database level within the context of a local database (e.g. DB1)                                                 |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **2**  | Opt in to replication                                                                                                                            |
| **3**  | Define the replication\_id                                                                                                                       |
| **4**  | Pull changes from the remote database at the specified url.                                                                                      |
| **5**  | Authenticate with the provided credentials. This user must have read and write access to both the local and remote databases.                    |
| **6**  | Batch together up to 1000 revisions at a time. This improve replication performance but consumes more memory resources.                          |
| **7**  | Apply a custom conflict resolution policy.                                                                                                       |
| **8**  | Provide a working Javascript function to apply the required resolution policy.                                                                   |
| **9**  | By setting continuous=false, we are creating a one-shot replication. We could also have omitted this parameter as it defaults to false.          |
| **10** | Don't use delta-sync; the default behavior.                                                                                                      |
| **11** | Filter documents by channel.                                                                                                                     |
| **12** | Replicate only those documents tagged with the channel names "user1".                                                                            |
| **13** | Wait no more than 5 minutes between retries after network failure; default behavior.                                                             |
| **14** | Don't purge following removal of a channel; the default behavior.                                                                                |
| **15** | Start the replicator immediately and on Sync Gateway node re(start);. We could also have omitted this parameter as this is the default behavior. |

This is an example of a replication definition as you might submit it to the Admin REST API.using `curl`. Its purpose is to illustrate all configurable items in use and so should not be considered a working example.

It creates a replication with the replication\_ID of `db1-rep-id1-pull-oneshot` on a local database `db1-local_`, pulling data from a remote database `db1-remote`.

```json
curl --location --request POST 'http://localhost:4985/db1-local/_replication/db1-rep-id1-pull-oneshot' \ (1)
--header 'Content-Type: application/json' \
--dataraw '{
"replication_id": "db1-rep-id1-pull-oneshot" (2)
        "direction": "pull",                              (3)
        "remote": "https://example.com:4984/remote_db1",
        "user": "user1",                                  (4)
        "password": "password",
        "batch_size": 1000,                               (5)
        "conflict_resolution_type": "custom",             (6)
        "custom_conflict_resolver": "",                   (7)
        "continuous": false,                              (8)
        "enable_delta_sync": false,                       (9)
        "filter": "sync_gateway/bychannel",               (10)
        "query_params": ["channel.user1"]                 (11)
        "max_backoff_time": 5,                            (12)
        "purge_on_removal": false                         (13)
        "state": "running"                                (14)
  "adhoc": false, (15)
  "cancel": false (16)
}'
```

| **1**  | All replications take place at database level and in the context of a local database. Here we are setting the replication in the context of db1-local                         |
| ------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2**  | Define the replication\_id                                                                                                                                                    |
| **3**  | Pull changes from the remote database at the specified url.                                                                                                                   |
| **4**  | Authenticate with the provided credentials. This user must have read and write access to both the local and remote databases.                                                 |
| **5**  | Batch together up to 1000 revisions at a time. This improve replication performance but consumes more memory resources.                                                       |
| **6**  | Apply a custom conflict resolution policy.                                                                                                                                    |
| **7**  | Provide a working Javascript function to apply the required resolution policy.                                                                                                |
| **8**  | By setting continuous=false, we are creating a one-shot replication. We could also have omitted this parameter as it defaults to false.                                       |
| **9**  | Don't use delta-sync; the default behavior.                                                                                                                                   |
| **10** | Filter documents by channel.                                                                                                                                                  |
| **11** | Replicate only those documents tagged with the channel names "user1".                                                                                                         |
| **12** | Wait no more than 5 minutes between retries after network failure; default behavior.                                                                                          |
| **13** | Don't purge following removal of a channel; the default behavior.                                                                                                             |
| **14** | Start the replicator immediately and on Sync Gateway node re(start);. We could also have omitted this parameter as this is the default behavior.                              |
| **15** | Setting adhoc=false marks this as a persistent replication. The definition will survive Sync Gateway node restarts. This the default behaviour if this parameter is omitted.+ |
| **16** | Set cancel=true to cancel an initialized replication; otherwise you can omit this parameter.                                                                                  |

## [](#generic-constraints)Generic Constraints

> [!CAUTION]
> Replication
> 
> All active nodes in an active cluster must be running Sync Gateway version 2.8+.

[ENTERPRISE EDITION](https://www.couchbase.com/products/editions)

All replications are distributed evenly across available nodes. This means they cannot be guaranteed to run on the node from which they originate.

Access rights

The user running the replication must have read and write access to the data being replicated. This is not enforced by the system. Use your `sync` function to ensure a consistent approach is applied across all clusters.

Mixing Inter-Sync Gateway Replication Versions

Versions of inter-Sync Gateway replications pre- and post-2.8 can legitimately be in use at the same time, especially during transition. However, you should avoid initializing identical pre-2.8 (SG Replicate) and 2.8+ replications.

## [](#running-configured-replications)Running Configured Replications

Replications in the configuration file start automatically whenever Sync Gateway is (re)started. Unless you inhibit this by adding an `"initial_state": "stopped"` parameter to the replication definition — see: [initial\_state](../current/configuration/configuration-properties-legacy.md#databases-this%5Fdb-replications-this%5Frep-initial%5Fstate). You can manually start 'stopped' replication using [Starting a replication](../current/sync/sync-inter-syncgateway-manage.md#starting-a-replication).

Example 3\. Configured Replications — Continuous and One-shot

* Continuous
* One-shot

```json
//  . . . other configuration entries
"db1-rep-id1-pull-cont":
  "replication_id": "db1-rep-id1-pull-cont",
  "direction": "pull",
  "continuous": true (1)
  "purge-on-removal": true,
  "remote": "http://user:password@example.com:4985/db1-remote",
  "filter":"sync_gateway/bychannel",
  "query_params": {
    "channels": ["channel1.user1"]
  }
//  . . . other configuration entries
```

| **1** | Make this a continuous replication that remains running, listening for changes to process. Because it is also persistent, it will start automatically following Sync Gateway node restarts (state defaults to running). |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

```json
//. . . other configuration entries
"db1-rep-id3-pull-oneshot":
"replication_id": "db1-rep-id3-pull-oneshot", (1)
"direction": "pull",
"remote": "http://user:password@example.com:4985/db1-remote",
"filter": "sync_gateway/bychannel",
"query_params": { "channels": ["channel1.user1"] }
//  . . . other configuration entries
```

| **1** | This a a one-shot replication because the continuous parameter defaults to false. |
| ----- | --------------------------------------------------------------------------------- |

## [](#running-admin-rest-api-replications)Running Admin REST API Replications

Replications initialized by sending a `POST`, or `PUT`, request to the `_replication` endpoint will start running automatically, unless the `"initial_state": "stopped"` parameter is specified. with a JSON object defining the replication parameters — as shown in [Example 4](#submitting-api-requests).

* You can run multiple replications simultaneously with different replication topologies, provided both databases being synchronized have the same sync function.

You can submit requests using the `curl` utility (as in these examples) or an application such as _Postman_.

Example 4\. Submitting API Requests

* Continuous Pull Replication
* One-shot
* Ad-hoc

This example initializes a persistent, continuous, replication between a local database and one on a remote Sync Gateway instance.

```json
curl --location --request POST 'http://localhost:4985/db1-local/_replication/' \
--header 'Content-Type: application/json' \
--dataraw '{
  "replication_id": "db1-rep-id1-pull-cont",
  "direction": "pull",
  "continuous": true (1)
  "purge-on-removal": true,
  "remote": "http://user:password@example.com:4985/db1-remote",
  "filter":"sync_gateway/bychannel",
  "query_params": {
    "channels": ["channel1.user1"]
  }
}'
```

This example initializes a persistent, one-shot, replication between a local database and one on a remote Sync Gateway instance.

The replication will run once, after a short delay to allow the Rest API to start. It will then run once after each Sync Gateway restart and-or when manually initiated using the `_replicationStatus` endpoint — see [Manage Inter-Sync Gateway Replications](../current/sync/sync-inter-syncgateway-manage.md).

```json
curl --location --request POST 'http://localhost:4985/db1-local/_replication/' \
--header 'Content-Type: application/json' \
--dataraw '{
"replication_id": "db1-rep-id3-pull-oneshot", (1)
"direction": "pull",
"remote": "http://user:password@example.com:4985/db1-remote",
"filter": "sync_gateway/bychannel",
"query_params": { "channels": ["channel1.user1"] }
}'
```

| **1** | This a a one-shot replication because the continuous parameter defaults to false. |
| ----- | --------------------------------------------------------------------------------- |

```javascript
curl --location --request POST 'http://localhost:4985/db1-local/_replication/' \
--header 'Content-Type: application/json' \
--dataraw '{
  "replication_id": "db1-rep-id1-pull-adhoc",
  "adhoc": true, (1)
  "direction": "pull",
  "purge-on-removal": true,
  "remote": "http://user:password@example.com:4985/db1-remote",
  "filter":"sync_gateway/bychannel",
  "query_params": {
    "channels": ["channel1.user1"]
  }
}'
```

| **1** | Run this replication as an ad hoc one. It will run once only, process all changes but not survive Sync Gateway restarts |
| ----- | ----------------------------------------------------------------------------------------------------------------------- |

## [](#related-content)Related Content

###### [](#)

Learn more …​

* [Inter-Sync Gateway Replication](../current/sync/sync-inter-syncgateway-overview.md)
* [SG-Replicate](#sync-gateway::legacy-sg-replicate.adoc)
* [Sync with Couchbase Server](../current/sync/sync-with-couchbase-server.md)

###### [](#-2)

Reference material …​

* [Configuration Properties](../current/configuration/configuration-properties-legacy.md)
* [Public REST API](../current/rest-api/rest-api.md)
* [Admin REST API](../current/rest-api/rest-api-admin.md)
* [Metrics REST API](../current/rest-api/rest-api-metrics.md)
* [Use the REST API?](#sync-gateway::rest-api-client-app.adoc)

###### [](#-3)

Community

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)

Conflict Related Blogs

* [Automatic Conflict Resolution](https://blog.couchbase.com/document-conflicts-couchbase-mobile/)
* [Demystifying Conflict Resolution](https://blog.couchbase.com/conflict-resolution-couchbase-mobile/)
* [Conflict Resolution (category)](https://blog.couchbase.com/tag/conflict-resolution/)

---

[1](#%5Ffootnoteref%5F1). This parameter is not available in the configuration file. 

[2](#%5Ffootnoteref%5F2). The definitions apply to configured and API replications).