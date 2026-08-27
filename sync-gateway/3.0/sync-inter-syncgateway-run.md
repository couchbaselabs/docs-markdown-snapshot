---
title: Initialize Inter-Sync Gateway Replications
description: Initializing and running inter-Sync Gateway replication
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.0/modules/ROOT/pages/sync-inter-syncgateway-run.adoc
  xref: xref:3.0@sync-gateway::sync-inter-syncgateway-run.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.0/sync-inter-syncgateway-run.html)

# Initialize Inter-Sync Gateway Replications

> Initializing and running inter-Sync Gateway replication  

_Related topics_: [Overview](sync-inter-syncgateway-overview.md) | Run | [Manage](sync-inter-syncgateway-manage.md) | [Monitor](sync-inter-syncgateway-monitor.md) | [Conflict](sync-inter-syncgateway-conflict-resolution.md)

_Other Topics_: [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md) | [Admin REST API](rest-api-admin.md)

> [!IMPORTANT]
> Context Clarification
> 
> This content relates only to inter-Sync Gateway replication in Sync Gateway 2.8+. For documentation on pre-2.8 inter-Sync Gateway replication (also known as SG Replicate) — see the documentation for the appropriate release.

## [](#introduction)Introduction

Replications are initialized by submitting a [replication definition![glossary icon](_images/icons/glossaryIconImage2.png)](glossary.md#replication-definition) using either:

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

  * Reset — a [checkpoint![glossary icon](_images/icons/glossaryIconImage2.png)](glossary.md#checkpoint) can be reset to zero
  * Updated — only the parameter values provided in the PUT request body will be updated
* Persistent and ad hoc replications can be:

  * Removed — only the replication\_id is needed to delete ongoing continuous or one-shot replications.
* [ENTERPRISE EDITION](https://www.couchbase.com/products/editions) only:

  * Replications can use delta-sync mode, whereby only the changed data-items are replicated.

* Multiple identical replicators can be initiated on a Sync Gateway node provided each has a unique `replication_Id`.
* inter-Sync Gateway replications introduced in Sync Gateway 2.8 as well as SG-Replicate can run on the same node, but you must ensure that they each have a different `replication_id`.
* The user under which replication is being run must have read and write access to the data being replicated.
* Exponential backoff when connection lost; this can be customized using the [max\_backoff\_time](configuration-schema-database.md#database-replications-this%5Frep-max%5Fbackoff%5Ftime) configuration setting.
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

Both scenarios are covered in [Example 2](#replication-properties). It summarizes the [replication definition![glossary icon](_images/icons/glossaryIconImage2.png)](glossary.md#replication-definition) elements\[[2](#%5Ffootnotedef%5F2 "View footnote.")\], which are covered in more detail in [Database Configuration](configuration-schema-database.md).

### [](#database-level-settings)Database-level Settings

A number of database-level options are also especially relevant to Inter-Sync Gateway Replication, including:

* [sgreplicate\_enabled](configuration-schema-database.md#database-sgreplicate%5Fenabled) — use this [ENTERPRISE EDITION](https://www.couchbase.com/products/editions) setting to allow the database to participate in Inter-Sync Gateway Replications.
* [database.delta\_sync](configuration-schema-database.md#database-delta%5Fsync) — use this setting to enable delta-sync replication on the database, it must be set if you want to use delta-sync in your _replication definition_.
* [sgreplicate\_websocket\_heartbeat\_secs](configuration-schema-database.md#database-sgreplicate%5Fwebsocket%5Fheartbeat%5Fsecs) — use this setting to override the default (5 minute) heartbeat interval for websocket ping frames for this database.
* [database.sync](configuration-schema-database.md#database-sync) — use this setting to specify the sync function logic — this is an essential part of access-control.
* [unsupported.sgr\_tls\_skip\_verify](configuration-schema-database.md#database-unsupported-sgr%5Ftls%5Fskip%5Fverify) — use this unsupported option to make development an testing easier by skipping verification of TLS certificates.

### [](#replication-level-settings)Replication-level Settings

Example 2\. Replication Definition

* Summary of Parameters
* Configured Example
* REST API Example

This table summarize all the available configurable items.

Data schema for the replication model

Name

Description

Schema

**adhoc**  
_optional_

" **About**

Use the Admin REST API's `adhoc` parameter to specify that a replication is ad hoc rather than persistent.

**Behavior**

Ad hoc replications behave the same as normal replications, but they are automatically removed when their status changes to stopped. This will usually be on completion, but may also be as a result of user action.

**Constraints**

This parameter is **NOT** available to configured replications; only those initialized using the Admin REST API."  
**Default** : `false`

boolean

**batch\_size**  
_optional_

**About**

Use the optional `batch_size` property to specify the number of changes to be included in a single batch during replication.

integer

**cancel**  
_optional_

**About**

Use this parameter on,y when you want to want to cancel an existing active replication.

**Constraints**

\* This parameter is **NOT** available in configured replications; only those initialized using the Admin REST API.

\* **NOTE** that the body of the request must be the same as the replication's replication definition for the cancellation request to be honoured. For example, if you requested continuous replication, the cancellation request must also contain the continuous field.  
**Default** : `false`

boolean

**conflict\_resolution\_type**  
_optional_

**About**

The **`conflict_resolution_type`** property defines the conflict resolution policy that Sync Gateway applies when resolving conflicting revisions.

The default behavior is that automatic conflict resolution policy is applied.

**Valid options**\- `default`\- `localWins`\- `remoteWins`\- `custom`

**Behavior**

\* _default_ \- Selecting `default` applies the following conflict resolution policy \* Deletes always win (the delete with longest revision history wins if both revisions are deletes) \* The revision with the longest revision history wins (so, the one with most changes and consequently the highest revision Id). \* _localWins_ \- Selecting `localWins` will result in local revisions always being the winner in any conflict.

\* _remoteWins_ \- Selecting `remoteWins` will result in remote revisions always being the winner in any conflict. \* _custom_ \- Selecting `custom` specifies that you want to handle conflict resolution with your own application logic. You **must** provide this logic as a Javascript function by specifying it in using the custom-conflict-resolver parameter.

**Example**

\---- "conflict\_resolution\_type":"remoteWins" ----

**Constraints**

\* Replications created prior to version 2.8 will default to `default`.  
**Default** : `"default"`

string

**continuous**  
_optional_

**About**

The `continuous` property specifies whether this replication will run in continuous mode.

**Behavior**

\* `continuous=true`– In continuous mode, changes are immediately synced in accordance with the replication definition. \* `continuous=false`– Detected changes are synced in accordance with the replication definition. The replication ceases once all revisions are processed.

**Constraints**

\* Optional for stops and removes  
**Default** : `false`

boolean

**custom\_conflict\_resolver**  
_optional_

**About**

The optional `custom_conflict_resolver` property specifies the Javascript function that will be used to resolve conflicts, if the custom conflict resolution type is specified in the `conflict_resolution_type`.

**Options**

The property is _mandatory_ when `conflict_resolution_type=custom` and will be ignored in all other cases.

**Using**

Provide the required logic in a Javascript function, as a string within backticks (see also the description for the `sync` function\`.

The function takes one parameter `struct` representing the conflict and comprising - the document id - the local document - the remote document

The function returns a document `struct` representing the winning revision.

**Example**

\---- "custom\_conflict\_resolver":\` function(conflict) { console.log("full remoteDoc doc: "+JSON.stringify(conflict.RemoteDocument)); return conflict.RemoteDocument; }\` ----

**Constraints**

Using complex `custom_conflict_resolver` functions can noticeably degrade performance. Use a built-in resolver whenever possible.  
**Default** : `"none"`

string

**direction**  
_optional_

**About**

The mandatory `direction` property specifies whether the replication is _push_, _pull_ or _pushAndPull_ relative to this node.

The property value is referenced by the [remote](rest-api-admin.html#database-this%5Fdb-replications-remote) property.

**Behavior**

\* `pull` \- changes are pulled from the `remote` database \* `push` \- changes are pushed to the `remote` database \* `pushAndPull` \- changes are both pushed-to and pulled-from the `remote` database

**Constraints**

Replications created prior to version 2.8 derive their _direction_ from the source/target url of the replication.

string

**enable\_delta\_sync**  
_optional_

**About**

The optional `enable_delta_sync` parameter turns on delta sync for a replication. It works in conjunction with the database level setting `delta_sync.enabled`.

**Options**

\* `"enable_delta_sync": true`, the replication can use delta sync (depending on `delta_sync.enabled` setting) \* `"enable_delta_sync": false`, the replication cannot use delta sync

**Behavior**

The optional `enable_delta_sync` parameter works in conjunction with the database level `delta_sync.enabled` setting, to determine whether this replication uses delta sync.

\* **If** `"delta_sync.enabled": true` for both databases involved in the replication, then this parameter enables or disables its use for this specific replication. \* In all other cases it has no effect and the replication runs without delta-sync.

**Constraints**

\* Applies **ONLY** to Enterprise Edition deployments. \* Depends upon the setting of the database level parameter `delta_sync.enabled`\* Replications created prior to version 2.8 must run with `"enable_delta_sync": false`\* Push replications will not use Delta Sync when pushing to a pre-2.8 target  
**Default** : `false`

boolean

**filter**  
_optional_

**About**

Use the optional filter\`property to defines the function to be used to filter documents. 

**Options**

A common value used when replicating from Sync Gateway is \`sync\_gateway/bychannel. This option limits the pull replication to a specific set of channels. You can specify the required channels using `query_params`.

**Behavior**

Works in conjunction with `query_params` to control the documents processed by the replication.

**Example**

\---- "filter":"sync\_gateway/bychannel" ----

**Constraints**

OPTIONAL for stops and removes (even if defined during creation)

string

**initial\_state**  
_optional_

**About**

The optional `initial_state` property is used to specify that the replication must be launched in 'Stopped' mode

**Behavior**

All replications are configured to start on Sync Gateway launch. So, if omitted, the state defaults to 'Running'.

Constraints\* 

Replications created prior to version 2.8 will all default to a state of 'Running'.  
Default\*\* : `"Running"`

string

**max\_backoff\_time**  
_optional_

The \*max\_backoff\_time\*property specifies the time-period (in minutes) during which Sync Gateway will attempt to reconnect lost or unreachable _remote_ targets.

On disconnection, Sync Gateway will do an exponential backoff up to the specified value, after which it will attempt to reconnect indefinitely every _max\_backoff\_time_ minutes.

If a zero value is specified, then Sync Gateway will do an exponential backoff up to an interval of five minutes before stopping the replication.

NOTE - this value defaults to five minutes for replications created prior to version 2.8.

integer

**password**  
_optional_

**About**

Use `password` to provide the login password value for the accredited user running this replication.

**Behavior**

These details are used to authenticate credentials and approve access to data.

Once provided and recorded, the password data is redacted and will not be displayed in either the configuration file or Admin REST API. A string of ****\* will be displayed in its place.** 
**Default**\* : `"mandatory"` 

string

**purge\_on\_removal**  
_optional_

**About**

The optional `purge_on_removal` property specifies, per replication, whether the removal of a `channel` triggers a purge.

**Options**\- `true` or `false`\- Default = false - Document removals are ignored by receiving end

**Behavior**

If `purge_on_removal=false`, then the removal of channels is ignored (not purged) by the receiving end.

**Constraints**

\* Applies only to PULL replications, including the PULL portion of a PUSHANDPULL replication.

\* Replications created prior to version 2.8 _must_ be run with `purge_on_removal=false`.  
**Default** : `false`

boolean

**query\_params**  
_optional_

**About**

The `query_params` property defines a set of key/value pairs used in the query string of the replication.

**Behavior**

This property works in conjunction with `filters` and `channels` to provide routing.

**Using**

You can use `` query_params’ _channels_ function to _pull_ from a specific set of `channels ``. To do so, you would also need to set the `filter` to `sync_gateway/bychannels`.

**Example**

\[source,json\] ---- "filter":"sync\_gateway/bychannel", "query\_params": { "channels":\["channel.user1"\] }, ----

**Constraints**

OPTIONAL for stops and removes (even if defined during creation)

< string > array

**remote**  
_optional_

**About**

The **remote** property represents the endpoint of a database for the remote Sync Gateway. That is, it identifies the remote Sync Gateway database that is the subject of this replication's push, pull or pushAndPull action.

Typically the endpoint will include URI, Port and Database name elements.

You can also include user credentials in the URL, in the form `<username>:<password>`. The credentials relate to an existing Sync Gateway user on the remote server.

**Example**\`"remote": "<http://user:password@example.com:4985/db1-remote">; \`

**Format**

\* a string containing a valid URL for a (remote) Sync Gateway database. \* an object whose url property contains the Sync Gateway database URL.

**Behavior**

Dependent upon setting of **direction**.

If **direction** is : - _pull_, 'remote' defines the remote cluster _from_ which data is pulled - _push_, 'remote' defines the remote cluster _to_ which data is pushed - _pushAndPull_, 'remote' defines the _push_ configuration.

**Example**

\[source,json\] ---- "remote": "http://www.example.com:4984/sample-database", ----

string

**replication\_id**  
_optional_

**About**

The _replication\_id_ property specifies either:

\* For NEW replications, the ID to be assigned to the the replication. If no _replication\_id_ is specified, Sync Gateway will assign a random UUID to new replications.

\* For existing replications, this is the ID of the required replication.

\* If **cancel=true**, this is the id of the active replication task to be cancelled.

**Constraints**

If this is specified in the body of a POST or PUT request then it must be the same value as specified in the request URL.

string

**username**  
_optional_

**About**

Use `username` to provide the name of the accredited user running this replication.

**Behavior**

These details are used to authenticate credentials and approve access to data

Once provided and recorded, the username data is redacted and will not be displayed in either the configuration file or Admin REST API. A string of ****\* will be displayed in its place.** 
**Default**\* : `"Mandatory"` 

string

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

Replications in the configuration file start automatically whenever Sync Gateway is (re)started. Unless you inhibit this by adding an `"initial_state": "stopped"` parameter to the replication definition — see: [initial\_state](configuration-schema-database.md#database-replications-this%5Frep-initial%5Fstate). You can manually start 'stopped' replication using [Starting a replication](sync-inter-syncgateway-manage.md#starting-a-replication).

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
| **2** | The remote URL can also include the credentials for an existing Sync Gateway user on the remote server.                                                                                                                 |

```json
//. . . other configuration entries
"db1-rep-id3-pull-oneshot":
"replication_id": "db1-rep-id3-pull-oneshot", (1)
"direction": "pull",
"remote": "http://user1:password@example.com:4985/db1-remote", (2)
"filter": "sync_gateway/bychannel",
"query_params": { "channels": ["channel1.user1"] }
//  . . . other configuration entries
```

| **1** | This a a one-shot replication because the continuous parameter defaults to false.                       |
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

The replication will run once, after a short delay to allow the Rest API to start. It will then run once after each Sync Gateway restart and-or when manually initiated using the `_replicationStatus` endpoint — see [Inter Sync Gateway Sync - Manage](sync-inter-syncgateway-manage.md).

```json
curl --location --request POST 'http://localhost:4985/db1-local/_replication/' \
--header 'Content-Type: application/json' \
--dataraw '{
"replication_id": "db1-rep-id3-pull-oneshot", (1)
"direction": "pull",
"remote": "http://user1:password@example.com:4985/db1-remote", (2)
"filter": "sync_gateway/bychannel",
"query_params": { "channels": ["channel1.user1"] }
}'
```

| **1** | This a a one-shot replication because the continuous parameter defaults to false.                       |
| ----- | ------------------------------------------------------------------------------------------------------- |
| **2** | The remote URL can also include the credentials for an existing Sync Gateway user on the remote server. |

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

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Learn more …​

* [Inter Sync Gateway Sync - Overview](sync-inter-syncgateway-overview.md)
* [Sync with Couchbase Server](sync-with-couchbase-server.md)

###### [](#-3)

Reference material …​

* [Bootstrap](configuration-schema-bootstrap.md)
* [Database](configuration-schema-database.md)
* [Database Security](configuration-schema-db-security.md)
* [Access Control](configuration-schema-access-control.md)
* [Import Filter](configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)
* [Public REST API](rest-api.md)
* [Admin REST API](rest-api-admin.md)
* [Metrics REST API](rest-api-metrics.md)

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