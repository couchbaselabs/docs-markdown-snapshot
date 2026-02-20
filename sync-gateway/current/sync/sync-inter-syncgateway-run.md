---
title: Initialize Inter-Sync Gateway Replications
description: Initializing and running inter-Sync Gateway replication
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.0/modules/sync/pages/sync-inter-syncgateway-run.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:sync-gateway:sync:sync-inter-syncgateway-run.adoc[]
---

[View original HTML](/sync-gateway/current/sync/sync-inter-syncgateway-run.html)

# Initialize Inter-Sync Gateway Replications

> Initializing and running inter-Sync Gateway replication  

_Related topics_: [Overview](sync-inter-syncgateway-overview.md) | [Run](sync-inter-syncgateway-run.md) | [Manage](sync-inter-syncgateway-manage.md) | [Monitor](sync-inter-syncgateway-monitor.md) | [Conflict](sync-inter-syncgateway-conflict-resolution.md)

_Other Topics_: [Legacy Pre-3.0 Configuration](../configuration/configuration-properties-legacy.md) | [Admin REST API](../rest-api/rest-api-admin.md)

> [!IMPORTANT]
> Context Clarification
> 
> This content relates only to inter-Sync Gateway replication in Sync Gateway 2.8+. For documentation on pre-2.8 inter-Sync Gateway replication (also known as SG Replicate) — see the documentation for the appropriate release.

## [](#introduction)Introduction

Replications are initialized by submitting a [replication definition![glossary icon](../_images/icons/glossaryIconImage2.png)](../glossary.md#replication-definition) using either:

* A 'JSON' configuration file (`sync-gateway-config.json`)
* The Admin REST API, using a utility such as `curl`, or an application such as _Postman_.

Wherever they are defined, the elements of a replication definition are the same, with the exception of the `adhoc` Admin REST API endpoint used to specify that the replication is ad hoc \[[1](#%5Ffootnotedef%5F1 "View footnote.")\].

Example 1\. Replication Characteristics Highlights

* Replication highlights
* Running highlights

* There are two types of replication: persistent and ad hoc (REST API only).
* Replications of both types can run in one-shot or continuous replications modes.
* All replications involve at least one local database.
* Replications can be configured to purge documents when channel access is revoked (a removal notification is received).
* Persistent continuous replications can be:

  * Reset — a [checkpoint![glossary icon](../_images/icons/glossaryIconImage2.png)](../glossary.md#checkpoint) can be reset to zero
  * Updated — only the parameter values provided in the PUT request body will be updated
* Persistent and ad hoc replications can be:

  * Removed — only the replication\_id is needed to delete ongoing continuous or one-shot replications.
* [ENTERPRISE EDITION](https://www.couchbase.com/products/editions) only:

  * Replications can use delta-sync mode, whereby only the changed data-items are replicated.

* Multiple identical replicators can be initiated on a Sync Gateway node provided each has a unique `replication_Id`.
* inter-Sync Gateway replications introduced in Sync Gateway 2.8 as well as SG-Replicate can run on the same node, but you must ensure that they each have a different `replication_id`.
* The user under which replication is being run must have read and write access to the data being replicated.
* Exponential backoff when connection lost; this can be customized using the [max\_backoff\_time](../configuration/configuration-schema-database.md#database-replications-this%5Frep-max%5Fbackoff%5Ftime) configuration setting.
* replications will continue trying to connect for 30 minutes following authentication failure (including user-invalid/doesn’t exist).
* Running replications can be stopped. Stopped replications can be (re)Started.
* If ALL the Sync Gateway nodes in a source or target Sync Gateway cluster go down in the middle of continuous replication, by default, the system should pick up from the last document that was successfully processed by both sides when the replication/cluster is restarted
* REST ONLY

  * POST databases/{db}/\_replication creates a replication using the replication ID specified in the body or if none specified, a unique UUID.
  * PUT databases/{db}/\_replication/{replicationID} upserts the replication with the specified ID.
* [ENTERPRISE EDITION](https://www.couchbase.com/products/editions) only:

  * Replications are distributed even across all available Sync Gateway nodes and so are not guaranteed to run on their originating node.
  * If a multi-node Sync Gateway cluster loses a subset of sync gateway nodes, the remaining nodes continue replication uninterrupted IF they have been configured to handle the replication (continuous and one-shot replications).

## [](#replication-definition)Replication Definition

All replications are 'initialized' by a [replication definition![glossary icon](../_images/icons/glossaryIconImage2.png)](../glossary.md#replication-definition) in the configuration file or Admin REST API and operate within the context of a local database.

* Configured replications use the `database.{db-name}.replications` property to add a replication definition to a local database.
* REST API replications specify the local database and replication identity in the API POST/PUT request. Providing the replication definition parameters in the request body as a JSON string.

Both scenarios are covered in [Example 2](#replication-properties). It summarizes the [replication definition![glossary icon](../_images/icons/glossaryIconImage2.png)](../glossary.md#replication-definition) elements\[[2](#%5Ffootnotedef%5F2 "View footnote.")\], which are covered in more detail in [Database Configuration](../configuration/configuration-schema-database.md).

### [](#database-level-settings)Database-level Settings

A number of database-level options are also especially relevant to Inter-Sync Gateway Replication, including:

* [sgreplicate\_enabled](../configuration/configuration-schema-database.md#database-sgreplicate%5Fenabled) — use this [ENTERPRISE EDITION](https://www.couchbase.com/products/editions) setting to allow the database to participate in Inter-Sync Gateway Replications.
* [database.delta\_sync](../configuration/configuration-schema-database.md#database-delta%5Fsync) — use this setting to enable delta-sync replication on the database, it must be set if you want to use delta-sync in your _replication definition_.
* [sgreplicate\_websocket\_heartbeat\_secs](../configuration/configuration-schema-database.md#database-sgreplicate%5Fwebsocket%5Fheartbeat%5Fsecs) — use this setting to override the default (5 minute) heartbeat interval for websocket ping frames for this database.
* [database.sync](../configuration/configuration-schema-database.md#database-sync) — use this setting to specify the sync function logic — this is an essential part of access-control.
* [unsupported.sgr\_tls\_skip\_verify](../configuration/configuration-schema-database.md#database-unsupported-sgr%5Ftls%5Fskip%5Fverify) — use this unsupported option to make development an testing easier by skipping verification of TLS certificates.

### [](#replication-level-settings)Replication-level Settings

This table summarizes all the available configurable items.

__Table 1\. Summary of Parameters__
| Property                                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Schema       |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| **adhoc** _optional_                      | Set to true to run the replication as an adhoc replication instead of a persistent one. This means that the replication will only last the period of the replication until the status is changed to stopped and then it will be removed automatically. It will also be removed if Sync Gateway restarts or if removed due to user action.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Boolean      |
| **batch\_size** _optional_                | The amount of changes to be sent in one batch of replications. Changing this is an Enterprise Edition only feature.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Integer      |
| **collections\_enabled** _optional_       | If true, the replicator will run with collections, and will replicate all collections, unless otherwise limited by collections\_local. If false, the replicator will only replicate the default collection.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Boolean      |
| **collections\_local** _optional_         | Limits the set of collections replicated to those listed in this array. The replication will use all collections defined on the database if this list is empty.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | String array |
| **collections\_remote** _optional_        | Remaps the local collection name to the one specified in this array when replicating with the remote. If only a subset of collections need remapping, elements in this array can be specified as null to preserve the local collection name. The same index is used for both collections\_remote and collections\_local, and both arrays must be the same length.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | String array |
| **conflict\_resolution\_type** _optional_ | This defines what conflict resolution policy Sync Gateway should use to apply when resolving conflicting revisions. Changing this is an Enterprise Edition only feature. **Values:** "default", "remoteWins", "localWins", "custom"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | String       |
| **continuous** _optional_                 | If true, changes will be immediately synced when they happen. This is known as a continuous replication. If false, all changes will be synced until they have been processed. The replication will then cease and not process any future changes (unless started again by the user). This is known as a one-shot replication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Boolean      |
| **custom\_conflict\_resolver** _optional_ | This specifies the Javascript function to use to resolve conflicts between conflicting revisions. This **must** be used when conflict\_resolution\_type=custom. This property will be ignored when conflict\_resolution\_type is not custom. The Javascript function to provide this property should be in backticks (like the sync function). The function takes 1 parameter which is a struct that represents the conflict. This struct has 2 properties: LocalDocument \- The local document. This contains the document ID under the \_id key. RemoteDocument \- The remote document The function should return the new document's body. This can be the winning revision (for example, return conflict.LocalDocument), a new body, or nil to resolve as a delete. Example: function(conflict) {   console.log("Doc ID: "+conflict.LocalDocument.\_id);   console.log("Full remote doc: "+JSON.stringify(conflict.RemoteDocument));   return conflict.RemoteDocument; } Using complex custom\_conflict\_resolver functions can noticeably degrade performance. Use a built-in resolver whenever possible. If a document merge is being done, the \_rev and \_cv properties should not be included in the returned document body as Sync Gateway will generate new values for these. This is an Enterprise Edition only feature. | String       |
| **direction** _required_                  | This specifies which direction the replication will be replicating with the remote replicator. **Values:** "push", "pull", "pushAndPull"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | String       |
| **enable\_delta\_sync** _optional_        | This will turn on delta-sync for the replication. In order to enable delta-sync for a replication, the database level setting delta\_sync.enabled must also be set to true. Using delta-sync is an Enterprise Edition only feature.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | Boolean      |
| **filter** _optional_                     | This defines whether to filter documents. **Values:** "sync\_gateway/bychannel", ""                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | String       |
| **initial\_state** _optional_             | This is what state to start the replication in when creating a new replication. This allows you to control if the replication starts in a stopped start or running state. Replications prior to Sync Gateway 2.8 will run in the default state running. **Values:** "running", "stopped"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | String       |
| **max\_backoff\_time** _optional_         | Specifies the maximum time-period (in minutes) that Sync Gateway will attempt to reconnect to a lost or unreachable remote. When a disconnection happens, Sync Gateway will do an exponential backoff up to this specified value. When this value is met, it will attempt to reconnect indefinitely every max\_backoff\_time minutes. If this is set to 0, Sync Gateway will do the normal exponential backoff after the disconnect happens but then attempting 10 minutes and stop the replication. Note: this defaults to 5 minutes for replications created prior to Sync Gateway 2.8.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Integer      |
| **purge\_on\_removal** _optional_         | Specifies whether to purge a document if the remote user loses access to all of the channels on the document when attempting to pull it from the remote. If false, documents will not be replicated and not be purged when the user loses access.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Boolean      |
| **query\_params** _optional_              | This is a set of key/value pairs used in the query string of the replication. If filters=sync\_gateway/bychannel then this can be used to set the channels to filter by in a pull replication. To do this, set the channels key to a string array of the channels to filter by. For example: "filter":"sync\_gateway/bychannel", "query\_params": {   "channels":\["chanUser1"\] },                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | String array |
| **remote** _optional_                     | This is the endpoint of the database for the remote Sync Gateway that is the subject of this replication's push, pull, or pushAndPull action. Typically this would include the URI, port, and database name. For example, https://localhost:4985/db.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | String       |
| **remote\_password** _optional_           | The password to use to authenticate with the remote. This password will be redacted in the replication config.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | String       |
| **remote\_username** _optional_           | The username to use to authenticate with the remote.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | String       |
| **replication\_id** _optional_            | This is the ID of the replication. When creating a new replication using a POST request, this will be set to a random UUID if not explicitly set. When the replication ID is specified in the URL, this must be set to the same replication ID if specifying it at all.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | String       |
| **run\_as** _optional_                    | This is used if you want to specify a user to run the replication as. This means that the replication will only be able to replicate what the user access to what the user has access to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | String       |
| **password** _optional_                   | **This has been deprecated in favour of remote\_password.** This is the password to use to authenticate with the remote. This password will be redacted in the replication config.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | String       |
| **username** _optional_                   | **This has been deprecated in favour of remote\_username.** This is the username to use to authenticate with the remote.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | String       |

Example 2\. Replication Definition

* Configured Example
* REST API Example

This is an example of a replication definition. Its purpose is to illustrate configurable items in use, and so should not be considered a working example.

It creates a replication with the replication\_ID of `db1-rep-id1-pull-oneshot` on a local database `db1-local`, pulling data from a remote database `remote-db1`.

```json
{
  "db1": {                                                (1)
    "bucket":"db1",
    "server": "couchbase://cb-server",
    // ... other DB config ..
    "sgreplicate_enabled": true,                          (2)
    "replications": {
      "db1-rep-id1-pull-oneshot": {                       (3)
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
        "query_params": ["channel.user1"],                (12)
        "max_backoff_time": 5,                            (13)
        "purge_on_removal": false,                        (14)
        "initial_state": "running",                       (15)
        // ... other replication config ...
      }
    }
  }
}
```

| **1**  | All replications are defined at database level within the context of a local database, for example db1.                              |
| ------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| **2**  | Opt in to replication.                                                                                                               |
| **3**  | Define the replication\_id.                                                                                                          |
| **4**  | Pull changes from the remote database at the specified url.                                                                          |
| **5**  | Authenticate with the provided credentials. This user must have read and write access to both the local and remote databases.        |
| **6**  | Batch together up to 1000 revisions at a time. This improves replication performance but consumes more memory resources.             |
| **7**  | Apply a custom conflict resolution policy.                                                                                           |
| **8**  | Provide a working Javascript function to apply the required resolution policy.                                                       |
| **9**  | By setting continuous=false, this creates a one-shot replication. You could omit this parameter as it defaults to false.             |
| **10** | Don’t use delta-sync; the default behavior.                                                                                          |
| **11** | Filter documents by channel.                                                                                                         |
| **12** | Replicate only those documents tagged with the channel names "user1".                                                                |
| **13** | Wait no more than 5 minutes between retries after network failure; default behavior.                                                 |
| **14** | Don’t purge following removal of a channel; the default behavior.                                                                    |
| **15** | Start the replicator immediately and on Sync Gateway node re(start);. You could omit this parameter as this is the default behavior. |

This is an example of a replication definition as you might submit it to the Admin REST API.using `curl`. Its purpose is to illustrate configurable items in use, and so should not be considered a working example.

It creates a replication with the replication\_ID of `db1-rep-id1-pull-oneshot` on a local database `db1-local_`, pulling data from a remote database `db1-remote`.

```bash
curl --location --request POST \
'http://localhost:4985/db1-local/_replication/db1-rep-id1-pull-oneshot' \ (1)
--header 'Content-Type: application/json' \
--dataraw '{
  "replication_id": "db1-rep-id1-pull-oneshot",     (2)
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
  "query_params": ["channel.user1"],                (11)
  "max_backoff_time": 5,                            (12)
  "purge_on_removal": false,                        (13)
  "initial_state": "running",                       (14)
  "adhoc": false,                                   (15)
  "cancel": false                                   (16)
}'
```

| **1**  | All replications take place at database level and in the context of a local database. This sets the replication in the context of db1-local.                                |
| ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2**  | Define the replication\_id.                                                                                                                                                 |
| **3**  | Pull changes from the remote database at the specified url.                                                                                                                 |
| **4**  | Authenticate with the provided credentials. This user must have read and write access to both the local and remote databases.                                               |
| **5**  | Batch together up to 1000 revisions at a time. This improves replication performance but consumes more memory resources.                                                    |
| **6**  | Apply a custom conflict resolution policy.                                                                                                                                  |
| **7**  | Provide a working Javascript function to apply the required resolution policy.                                                                                              |
| **8**  | By setting continuous=false, this creates a one-shot replication. You could omit this parameter as it defaults to false.                                                    |
| **9**  | Don’t use delta-sync; the default behavior.                                                                                                                                 |
| **10** | Filter documents by channel.                                                                                                                                                |
| **11** | Replicate only those documents tagged with the channel names "user1".                                                                                                       |
| **12** | Wait no more than 5 minutes between retries after network failure; default behavior.                                                                                        |
| **13** | Don’t purge following removal of a channel; the default behavior.                                                                                                           |
| **14** | Start the replicator immediately and on Sync Gateway node re(start);. You could omit this parameter as this is the default behavior.                                        |
| **15** | Setting adhoc=false marks this as a persistent replication. The definition will survive Sync Gateway node restarts. This the default behavior if this parameter is omitted. |
| **16** | Set cancel=true to cancel an initialized replication; otherwise you can omit this parameter.                                                                                |

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

Replications in the configuration file start automatically whenever Sync Gateway is (re)started. Unless you inhibit this by adding an `"initial_state": "stopped"` parameter to the replication definition — see: [initial\_state](../configuration/configuration-schema-database.md#replications-replication%5Fid-initial%5Fstate). You can manually start 'stopped' replication using [Starting a replication](sync-inter-syncgateway-manage.md#starting-a-replication).

Example 3\. Configured Replications — Continuous and One-shot

* Continuous
* One-shot

```json
{
//  . . . other configuration entries
  "db1-rep-id1-pull-cont": {
    "replication_id": "db1-rep-id1-pull-cont",
    "direction": "pull",
    "continuous": true, (1)
    "purge-on-removal": true,
    "remote": "http://user:password@example.com:4985/db1-remote", (2)
    "filter":"sync_gateway/bychannel",
    "query_params": {
      "channels": ["channel1.user1"]
    }
  }
//  . . . other configuration entries
}
```

| **1** | Make this a continuous replication that remains running, listening for changes to process. Because it is also persistent, it will start automatically following Sync Gateway node restarts (state defaults to running). |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | The remote URL can also include the credentials for an existing Sync Gateway user on the remote server.                                                                                                                 |

```json
{
//  . . . other configuration entries
  "db1-rep-id3-pull-oneshot": {
    "replication_id": "db1-rep-id3-pull-oneshot", (1)
    "direction": "pull",
    "remote": "http://user1:password@example.com:4985/db1-remote", (2)
    "filter": "sync_gateway/bychannel",
    "query_params": {
      "channels": ["channel1.user1"]
    }
  }
//  . . . other configuration entries
}
```

| **1** | This a one-shot replication because the continuous parameter defaults to false.                         |
| ----- | ------------------------------------------------------------------------------------------------------- |
| **2** | The remote URL can also include the credentials for an existing Sync Gateway user on the remote server. |

## [](#running-admin-rest-api-replications)Running Admin REST API Replications

Replications initialized by sending a `POST`, or `PUT`, request to the `_replication` endpoint will start running automatically, unless the `"initial_state": "stopped"` parameter is specified. with a JSON object defining the replication parameters — as shown in [Example 4](#submitting-api-requests).

You can run multiple replications simultaneously with different replication topologies, provided both databases being synchronized have the same sync function.

You can submit requests using the `curl` utility (as in these examples) or an application such as _Postman_.

Example 4\. Submitting API Requests

* Continuous Pull Replication
* One-shot
* Ad-hoc

This example initializes a persistent, continuous, replication between a local database and one on a remote Sync Gateway instance.

```bash
curl --location --request POST 'http://localhost:4985/db1-local/_replication/' \
--header 'Content-Type: application/json' \
--dataraw '{
  "replication_id": "db1-rep-id1-pull-cont",
  "direction": "pull",
  "continuous": true, (1)
  "purge-on-removal": true,
  "remote": "http://user:password@example.com:4985/db1-remote", (2)
  "filter":"sync_gateway/bychannel",
  "query_params": {
    "channels": ["channel1.user1"]
  }
}'
```

| **1** | Make this a continuous replication that remains running, listening for changes to process. Because it is also persistent, it will start automatically following Sync Gateway node restarts (state defaults to running). |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | The remote URL can also include the credentials for an existing Sync Gateway user on the remote server.                                                                                                                 |

This example initializes a persistent, one-shot, replication between a local database and one on a remote Sync Gateway instance.

The replication will run once, after a short delay to allow the Rest API to start. It will then run once after each Sync Gateway restart and-or when manually initiated using the `_replicationStatus` endpoint — see [Inter Sync Gateway Sync - Manage](sync-inter-syncgateway-manage.md).

```bash
curl --location --request POST 'http://localhost:4985/db1-local/_replication/' \
--header 'Content-Type: application/json' \
--dataraw '{
  "replication_id": "db1-rep-id3-pull-oneshot", (1)
  "direction": "pull",
  "remote": "http://user1:password@example.com:4985/db1-remote", (2)
  "filter": "sync_gateway/bychannel",
  "query_params": {
    "channels": ["channel1.user1"]
  }
}'
```

| **1** | This a one-shot replication because the continuous parameter defaults to false.                         |
| ----- | ------------------------------------------------------------------------------------------------------- |
| **2** | The remote URL can also include the credentials for an existing Sync Gateway user on the remote server. |

```bash
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

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Inter Sync Gateway Sync - Overview](sync-inter-syncgateway-overview.md)
* [Sync with Couchbase Server](sync-with-couchbase-server.md)

###### [](#-3)

Reference material …​

* [Bootstrap](../configuration/configuration-schema-bootstrap.md)
* [Database](../configuration/configuration-schema-database.md)
* [Database Security](../configuration/configuration-schema-db-security.md)
* [Access Control](../configuration/configuration-schema-access-control.md)
* [Import Filter](../configuration/configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](../configuration/configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](../configuration/configuration-properties-legacy.md)
* [Public REST API](../rest-api/rest-api.md)
* [Admin REST API](../rest-api/rest-api-admin.md)
* [Metrics REST API](../rest-api/rest-api-metrics.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)

Conflict Related Blogs

* [Automatic Conflict Resolution](https://blog.couchbase.com/document-conflicts-couchbase-mobile/)
* [Demystifying Conflict Resolution](https://blog.couchbase.com/conflict-resolution-couchbase-mobile/)
* [Conflict Resolution (category)](https://blog.couchbase.com/tag/conflict-resolution/)

---

[1](#%5Ffootnoteref%5F1). This parameter is not available in the configuration file. 

[2](#%5Ffootnoteref%5F2). The definitions apply to configured and API replications).