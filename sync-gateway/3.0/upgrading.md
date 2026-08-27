---
title: Upgrading Sync Gateway
description: This page documents various implementation details and
  functionalities to consider when performing an upgrade to Sync Gateway 3.0.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.0/modules/ROOT/pages/upgrading.adoc
  xref: xref:3.0@sync-gateway::upgrading.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.0/upgrading.html)

# Upgrading Sync Gateway

> This page documents various implementation details and functionalities to consider when performing an upgrade to Sync Gateway 3.0.  

Related _Application Deployment_ topics: [Prepare](get-started-prepare.md) | [Install](get-started-install.md) | [Release Notes](release-notes.md)

## [](#upgrade-approaches)Upgrade Approaches

A rolling upgrade is the recommended method to upgrade a Sync Gateway cluster. At a high level, a rolling upgrade consists of the following steps:

1. The load balancer configuration is updated to stop any HTTP traffic going to the node that will be upgraded.
2. The upgrade is performed on the given node
3. The load balancer configuration is updated to re-balance the HTTP traffic across all nodes.

Those steps are then repeated for each node in the sync gateway cluster.

## [](#upgrade-to-3-0)Upgrade to 3.0

### [](#use-persistent-configuration)Use Persistent Configuration

The use of 3.0's Persistent Configuration feature is strongly recommended. It is the default operational mode when starting sync gateway.

The feature provides a smooth upgrade path for existing users by automatically converting their existing configuration files to the new persistent configuration format.

> [!CAUTION]
> One Way Upgrade
> 
> The migration to 3.0 configuration is a ONE WAY process; to continue using legacy-mode configuration see: [Use Legacy-mode Configuration](#lbl-3-0-upgrade-opt-out)

#### [](#considerations)Considerations

Before commencing your upgrade consider your requirements for [Configuration Groups](#lbl-3-0-config-grps) although most users will likely find the default group sufficient, [Secure Server Connection](#lbl-3-0-config-tls) and [Secure Administration](#lbl-3-0-config-adm).

You should also:

* Ensure Sync Gateway has write access to the directory containing the existing configuration (the one to be converted). It will be used to backup the existing configuration, and to write the upgraded config.
* Ensure that, if your existing configuration has multiple databases, all of the **server** fields used to connect to _Couchbase Server_ match.  
Although the connection credentials used may differ between databases, Sync Gateway will only use the **first** set of credentials for the bootstrap configuration file.  
> [!NOTE]  
> Automatic upgrade cannot be done if you have multiple distinct server fields within the configuration file and you will need to manually create their own bootstrap configuration.

#### [](#process)Process

Just start up a sync gateway node using your existing configuration properties file.

On starting, Sync Gateway will take the appropriate upgrade path as shown in [Table 1](#tbl-enhancedcfg).

__Table 1\. Upgrade Paths__
| Configuration Status                      | Inference                                                                 | Outcome                                                                                                                           |
| ----------------------------------------- | ------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| No configuration exists                   | This is first node in the default group or with this _group ID_ to start  | Sync gateway uses the configuration file to derive and persist a configuration for this node.                                     |
| Configuration exists in the Server bucket | A node in the default group, or with this _group ID_, has already started | Sync gateway ignores the configuration file and uses the configuration associated with the default group, or _group ID_ provided. |

#### [](#lbl-3-0-config-grps)Configuration Groups

Whilst the provided default group will suffice for most deployments sync gateway does allow for the configuration of more complex node groupings.

So, before commencing your upgrade consider your requirements for grouping sync gateway nodes within your sync gateway cluster — see: [Configuration Groups](configuration-overview.md#lbl-config-grp)

If you want the sync gateway to associate with a specific configuration group Id, you must add the `bootstrap_group_id` value to the configuration file prior to startup — see: [bootstrap.group\_id](configuration-schema-bootstrap.md#bootstrap-group%5Fid)

Failing to do so may result in the configuration being overridden by one configured on a different sync gateway node that has already started and registered its own configuration.

### [](#lbl-3-0-config-tls)Secure Server Connection

Secure TLS Connection to Couchbase Server is enabled out-of-the-box in 3.0.

If you wish to use non-secure connection, perhaps in a test environment, you need to run sync gateway with [bootstrap.use\_tls\_server](configuration-schema-bootstrap.md#bootstrap-use%5Ftls%5Fserver) set to `false` — see: [Secure Sync Gateway Access](secure-sgw-access.md)

#### [](#lbl-3-0-config-adm)Secure Administration

Secure Administration is under-pinned by the use of Couchbase Server RBAC-users to authenticate and authorize access to Admin (and Metrics) API functionality. This requires you set-up and configure appropriate users — see: [REST API Access](rest-api-access.md).

To opt out of this, you can configure [api.api.admin\_interface\_authentication](configuration-schema-bootstrap.md#api-admin%5Finterface%5Fauthentication) and-or [api.metrics\_interface\_authentication](configuration-schema-bootstrap.md#api-metrics%5Finterface%5Fauthentication) as `false`

### [](#lbl-3-0-upgrade-opt-out)Use Legacy-mode Configuration

To continue using legacy Pre-3.0 configuration you should start sync gateway with [disable-persistent-config](configuration-properties-legacy.md#disable%5Fpersistent%5Fconfig) set `true` either in the configuration file or in [Command Line Options](command-line-options.md).

## [](#1-x-to-2-x-no-views)1.x to 2.x No Views

From: **Sync Gateway 1.x, 2.0**  
To: **Sync Gateway 2.1+ (`use_views: false`)**  
Downtime: No — a rolling upgrade  

### [](#steps)Steps

1. Upgrade one node in the cluster, and wait for it to be reachable via the REST API (for example, at http://localhost:4985/).
2. Upgrade the rest of the nodes in the cluster.
3. Clean up obsolete views:

  * **Optional** Issue a call to `/_post_upgrade?preview=true` on any node to preview which design documents will be removed.
  * Issue a call to `/post_upgrade` to remove the obsolete design documents. The response should indicate that "sync\_gateway" and "sync\_housekeeping" were removed.

### [](#upgrade-notes)Upgrade Notes

The upgrade, from using views to using Global Secondary Indexes and N1QL, happens automatically when starting a Sync Gateway 2.1 or above node in a cluster that was previously using views.

By default, Sync Gateway requires the Couchbase Server cluster to be running Couchbase Server 5.5, with at least two nodes running the Index and Query Services. If this is not the case, users must configure the `use_views` and/or `num_index_replicas` properties in their Sync Gateway configuration during upgrade.

Installation follows the same general approach used in 2.0\. On startup, Sync Gateway will check for the existence of the required indexes, and only attempt to create them if they do not already exist.

Then, Sync Gateway will wait until indexes are available before starting to serve requests.

### [](#tidy-up)Tidy-up

Sync Gateway 2.1 or above will **not** automatically remove the previously used design documents.

Removal of the obsolete design documents is done via a call to the [/\_post\_upgrade](rest-api-admin.md#/server/post%5F%5Fpost%5Fupgrade) endpoint in Sync Gateway's Admin REST API. This endpoint can be run in preview mode (`?preview=true`) to see which design documents would be removed.

## [](#1-x-to-2-x-using-views)1.x to 2.x Using Views

From: **Sync Gateway 1.x**  
To: **Sync Gateway 2.x (`use_views: true`)**  
Downtime: No — a rolling upgrade

### [](#steps-2)Steps

1. Upgrade one node in the cluster to 2.0, and wait for it to be reachable via the REST API (for example at http://localhost:4985/).
2. Upgrade the rest of the nodes in the cluster.
3. Clean up obsolete views:

  * **Optional** Issue a call to `_post_upgrade?preview=true` on any node to preview which design documents will be removed. To upgrade to 2.0, expect to see "sync\_gateway" and "sync\_housekeeping" listed.
  * Issue a call to `_post_upgrade` to remove the obsolete design documents. The response should indicate that "sync\_gateway" and "sync\_housekeeping" were removed.

### [](#notes)Notes

In 2.0, Sync Gateway's design documents include the version number in the design document name. In this release for example, the design documents are named `_design/sync_gateway_2.0` and `_design/sync_housekeeping_2.0`.

On startup, Sync Gateway will check for the existence of these design documents, and only attempt to create them if they do not already exist. Then, Sync Gateway will wait until views are available and indexed before starting to serve requests. To evaluate this, Sync Gateway will issue a `stale=false&limit=1` query against the Sync Gateway views (channels, access and role\_access).

If the view request exceeds the default timeout of 75s (which would be expected when indexing large buckets), Sync Gateway will log additional messages and retry — see [Example 1](#log-output).

Example 1\. Logging output

```bash
14:26:41.039-08:00 Design docs for current SG view version (2.0) found.
14:26:41.039-08:00 Verifying view availability for bucket default...
14:26:42.045-08:00 Timeout waiting for view "access" to be ready for bucket "default" - retrying...
14:26:42.045-08:00 Timeout waiting for view "channels" to be ready for bucket "default" - retrying...
14:26:42.045-08:00 Timeout waiting for view "role_access" to be ready for bucket "default" - retrying...
14:26:44.065-08:00 Timeout waiting for view "access" to be ready for bucket "default" - retrying...
14:26:44.065-08:00 Timeout waiting for view "role_access" to be ready for bucket "default" - retrying...
14:26:44.065-08:00 Timeout waiting for view "channels" to be ready for bucket "default" - retrying...
14:26:44.072-08:00 Views ready for bucket default.
```

### [](#tidy-up-2)Tidy-up

Sync Gateway 2.0 will **not** automatically remove the previous design documents.

Removal of the obsolete design documents is done via a call to the new [\_post\_upgrade](rest-api-admin.md#/server/post\%5F%5Fpost%5Fupgrade) endpoint in Sync Gateway's Admin REST API. This endpoint can be run in preview mode (`?preview=true`) to see which design documents would be removed.

## [](#1-x-to-1-5)1.x to 1.5

From: **Sync Gateway 1.1, 1.2, 1.3, 1.4**  
To: **Sync Gateway 1.5**  
Downtime: Possible downtime in a rolling upgrade; follow the steps below to avoid any downtime.

### [](#steps-3)Steps

### [](#upgrade-notes-2)Upgrade Notes

In this upgrade path, the upgrade process will trigger views in Couchbase Server to be re-indexed. During the re-indexing, operations that are dependent on those views will not be available. The main operations relying on views to be indexed are:

* A user requests data that doesn't reside in the [channel cache](configuration-properties-legacy.md#databases-this%5Fdb-cache-channel%5Fcache%5Fmax%5Flength).
* A new channel or role is granted to a user in the [Sync Function](sync-function.md).

The unavailability of those operations may result in some requests not being processed. The duration of the downtime will depend on the data set and frequency of replications with mobile clients. To avoid this downtime, it is possible to pre-build the view index before directing traffic to the upgraded node.

Sync Gateway uses Couchbase Server views to index and query documents. When Sync Gateway starts, it will publish a Design Document which contains the View definitions (map/reduce functions) — see [Example 2](#des-doc).

Example 2\. Design Document

```json
{
   "views":{
      "access":{
         "map":"function (doc, meta) { ... }"
      },
      "channels":{
         "map":"function (doc, meta) { ... }"
      },
      ...
   },
   "index_xattr_on_deleted_docs":true
}
```

### [](#avoiding-downtime)Avoiding Downtime

**Potential Downtime**: Following the Design Document creation, it must run against all the documents in the Couchbase Server bucket to build the index. An index rebuild may also be required during a Sync Gateway upgrade, if the Design Document definition has changed.

To avoid this downtime, you can publish the Design Document and build the index before starting Sync Gateway by using the Couchbase Server REST API. The following curl commands refer to a Sync Gateway 1.3 → Sync Gateway 1.4 upgrade but they apply to any upgrade of Sync Gateway or Accelerator.

1. Start Sync Gateway 1.4 with Couchbase Server instance that **isn't** your production environment. Then, copy the Design Document to a file with the following.  
```bash  
$ curl localhost:8092/<BUCKET_NAME>/_design/sync_gateway/ > ddoc.json  
```
2. Create a Development Design Document on the cluster where Sync Gateway is going to be upgraded from 1.3:  
```bash  
$ curl -X PUT http://localhost:8092/<BUCKET_NAME>/_design/dev_sync_gateway/ -d @ddoc.json -H "Content-Type: application/json"  
```  
This should return:  
```bash  
{"ok":true,"id":"_design/dev_sync_gateway"}  
```
3. Run a View Query against the Development Design Document. By default, a Development Design Document will index one vBucket per node, however we can force it to index the whole bucket using the `full_set` parameter:  
```bash  
$ curl "http://localhost:8092/sync_gateway/_design/dev_sync_gateway/_view/role_access_vbseq?full_set=true&stale=false&limit=1"  
```  
This may take some time to return, and you can track the index's progress in the Couchbase Server UI. Note that this will consume disk space to build an almost duplicate index until the switch is made.
4. Upgrade Sync Gateway. When Sync Gateway 1.4 starts, it will publish the new Design Document to Couchbase Server. This will match the Development Design Document we just indexed, so will be available immediately.

## [](#couchbase-server-upgrade-paths)Couchbase Server Upgrade Paths

> [!NOTE]
> When upgrading your Couchbase Server from 4.x to 5.x, remember to create a Sync Gateway RBAC user on the server — see: [Configure Server for Sync Gateway](get-started-prepare.md#configure-server.html) — and to include the user's credentials username/password in you Sync-Gateway-Config.json file.

All of the different upgrade paths mentioned above assume that you are running a compatible Couchbase Server version — see [Compatibility Matrix](compatibility.md).

There are three commonly used upgrade approaches for Couchbase Server. Depending on the one you choose, there may be additional consideration to keep in mind when using Sync Gateway:

| Approach                                     | Downtime                       | Additional Machine Requirements | Impact when using Sync Gateway                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| -------------------------------------------- | ------------------------------ | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Rolling Online Upgrade                       | None                           | Low                             | **Potential transient connection errors:** The Couchbase Server re-balance operations can result in transient connection errors between Couchbase Server and Sync Gateway, which could result in Sync Gateway performance degradation. **Potential for unexpected server errors during re-balance:** There is an increased potential to lose in-flight ops during a fail-over.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Upgrade Using Inter-Sync Gateway Replication | Small amount during switchover | High - duplicate entire cluster | Using an XDCR (Cross Data Center Replication) approach will incur some Sync Gateway downtime, but less than other approaches where Sync Gateway is shutdown during the entire Couchbase Server upgrade. It's important to note that the XDCR replication must be a **one way** replication from the existing (source) Couchbase Server cluster to the new (target) Couchbase Server cluster, and that no other writes can happen on the new (target) Couchbase Server cluster other than the writes from the XDCR replication, and no Sync Gateway instances should be configured to use the new (target) Couchbase Server cluster until the last step in the process. Start XDCR to do a one way replication from the existing (source) Couchbase Server cluster to the new (target) Couchbase Server cluster running the newer version. Wait until the target Couchbase Server has caught up to all the writes in the source Couchbase Server cluster. Shutdown Sync Gateway to prevent any new writes from coming in. Wait until the target Couchbase Server has caught up to all the writes in the source Couchbase Server cluster — this should happen very quickly, since it will only be the residual writes in transit before the Sync Gateway shutdown. Reconfigure Sync Gateway to point to the target cluster. Restart Sync Gateway. Caveats: **Small amount of downtime during switchover:** Since there may be writes still in transit after Sync Gateway has been shutdown, there will need to be some downtime until the target Couchbase Server cluster is completely caught up. **XDCR should be monitored:** Make sure to monitor the XDCR relationship as per [XDCR docs](../../server/current/manage/manage-xdcr/xdcr-management-overview.md). |
| Offline Upgrade                              | During entire upgrade          | None                            | Take Sync Gateway offline Upgrade Couchbase Server using any of the options mentioned in the [Upgrading Couchbase Server](../../server/current/install/upgrade.md) documentation. Bring Sync Gateway online                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

## [](#sg-replicate-to-inter-sync-gateway)SG Replicate to Inter-Sync Gateway

### [](#out-of-the-box-behavior)Out of the box behavior

Any [replications](configuration-properties-legacy.md#databases-this%5Fdb-replications-this%5Frep) ([continuous](configuration-properties-legacy.md#databases-this%5Fdb-replications-this%5Frep-continuous) or ad-hoc) pre-configured in the configuration file's [databases](configuration-properties-legacy.md#databases) section will run using the SG Replicate protocol. This is subject to any compatibility constraints defined in the [Compatibility Matrix](compatibility.md).

Existing replications implementing custom conflict resolution strategies (via the REST endpoint) will continue to function in the same manner as for SG Replicate replications after upgrade

### [](#upgrading-existing-replications)Upgrading existing replications

To upgrade existing SG Replicate replications to Inter-Sync Gateway Replication, reconfigure them using Inter-Sync Gateway Replication's [replications](configuration-properties-legacy.md#databases-this%5Fdb-replications-this%5Frep) property in the configuration file or the REST API — see [Upgrade Scenarios](#upgrade-strategies) for more.

### [](#post-upgrade-behavior)Post-upgrade behavior

General

* The system supports a rolling upgrade from SG Replicate to inter-Sync Gateway replication.
* One-shot replications configured at database level will continue as SG Replicate replications.
* Any configured SG Replicate replications that you want to upgrade to Inter-Sync Gateway must be re-configured using the Inter-Sync Gateway configuration (at database rather than global level) or REST API endpoint (`_replication`).
* An pre-2.8 systems using their own custom resolution strategy (via the REST endpoint) will function as they did for SG Replicate replications after upgrading.

Restarting Replications

The `replicationId` is used to ensure that any replications previously setup with SG Replicate, automatically restart using inter-Sync Gateway replication. The restart point will be the last checkpoint used, unless over-ridden.

Over-riding restart point

To restart a sync from zero: After the upgrade reconfigure the inter-Sync Gateway replication [replications](configuration-properties-legacy.md#databases-this%5Fdb-replications-this%5Frep) to use a different [replication\_id](configuration-properties-legacy.md#databases-this%5Fdb-replications-this%5Frep-replication%5Fid)

### [](#constraints)Constraints

Minimum Version for Inter-Sync Gateway Replication

In order to support Inter-Sync Gateway Replication, all active nodes in active cluster must be running Sync Gateway 2.8+.

Replication between two remote databases

Replication between two remote databases is no longer supported.

Sync Gateway will log an error and fail to start if a replication defined at the configuration's root level does not involve at least one local database (source or target).

Pushing to SG Replicate targets

* Push replications do not support SG Replicate targets with `"allow_conflicts": false` set; the target must use `"allow_conflicts": true` for a replication to work.
* Push replications do not use Delta Sync when pushing to a SG Replicate targets

### [](#upgrade-strategies)Upgrade Scenarios

This section describes recommended upgrade strategies for implementing Inter-Sync Gateway Replication

* [Scenario 1](#sc1) — Continue with SG Replicate (no conflict resolution)
* [Scenario 2](#sc2) — Continue with SG Replicate (custom conflict resolution)
* [Scenario 3](#sc3) — Change to SGR-Replicate 2.0 (default conflict resolution)
* [Scenario 4](#sc4) — Change to SGR-Replicate 2.0 (custom conflict resolution)

* [Scenario 1](#sc1)
* [Scenario 2](#sc2)
* [Scenario 3](#sc3)
* [Scenario 4](#sc4)

Scenario 1\. Continue with SG Replicate (no conflict resolution)

From

* Source Cluster — Active peer running Sync Gateway 2.x or 1.5 (Pre-2.8)
* Target Cluster — Passive peer running Sync Gateway 2.x or 1.5 (Pre-2.8)
* Replication - SG Replicate configured in continuous or one-shot mode
* Conflict resolution — Not implemented

To

* Source Cluster — Active node running Sync Gateway 2.8+
* Target Cluster — Passive node running Sync Gateway 2.8+
* Replication — SG Replicate configured in continuous or one-shot mode
* Conflict resolution — Not implemented

Strategy

* Upgrade sequence — Either cluster can be upgraded first
* Restart point — When the active node restarts it will use SG Replicate and will continue from where it last left off
* Upgrade Constraint — Replication will be down for the duration of the active node restart

Scenario 2\. Continue with SG Replicate (custom conflict resolution)

From

* Source Cluster — Active peer running Sync Gateway 2.x or 1.5 (Pre-2.8)
* Target Cluster — Passive peer running Sync Gateway 2.x or 1.5 (Pre-2.8)
* Replication — SG Replicate configured in continuous or one-shot mode
* Conflict resolution — Custom conflict resolution with `allow_conflicts=true`

To

* Source Cluster — Active node running Sync Gateway 2.8+
* Target Cluster — Passive node running Sync Gateway 2.8+
* Replication — SG Replicate configured in continuous or one-shot mode
* Conflict resolution — Custom conflict resolution with `allow_conflicts=true`

Strategy

* Upgrade sequence — Either cluster can be upgraded first
* Restart point — When the active node restarts it will use SG Replicate and will continue from where it last left off
* Conflict Resolution — Will continue to be handled by the app
* Upgrade Constraints

  * Replication will be down for the duration of the active node restart
  * The `allow_conflicts` flag is ignored for any inter-Sync Gateway replication replications configured.

Scenario 3\. Change to SGR-Replicate 2.0 (default conflict resolution)

From

* Source Cluster — Active peer running Sync Gateway 2.x or 1.5 (Pre-2.8)
* Target Cluster — Passive peer running Sync Gateway 2.x or 1.5 (Pre-2.8)
* Replication — SG Replicate configured in continuous or one-shot mode
* Conflict resolution — Not implemented

To

* Source Cluster — Active node running Sync Gateway 2.8+
* Target Cluster — Passive node running Sync Gateway 2.8+
* Replication — Inter-Sync Gateway replication configured in continuous or one-shot mode
* Conflict resolution — Not implemented

Strategy

* Upgrade sequence

  1. Stop SG Replicate replications
  2. Upgrade each cluster to 2.8.
* Restart Outcomes

  * When The active cluster is restarted it will automatically switch to Inter-Sync Gateway Replication
  * Replication will continue from the last checkpoint, unless over-ridden.
  * [ENTERPRISE EDITION](https://www.couchbase.com/products/editions) The replication will distribute automatically
* Conflict resolution — Default
* Upgrade Constraint — The `allow_conflicts` flag is ignored for any inter-Sync Gateway replication replications configured.

Scenario 4\. {sc4-title}

From

* Source Cluster — Active peer running Sync Gateway 2.x or 1.5 (Pre-2.8)
* Target Cluster — Passive peer running Sync Gateway 2.x or 1.5 (Pre-2.8)
* Replication — SG Replicate configured in continuous or one-shot mode
* Conflict resolution — Custom conflict resolution with `allow_conflicts=true`

To

* Source Cluster — Active node running Sync Gateway 2.8+
* Target Cluster — Passive node running Sync Gateway 2.8+
* Replication — inter-Sync Gateway replication configured in continuous or one-shot mode
* Conflict resolution — Apply custom conflict resolution

Strategy

* Upgrade sequence

  1. Stop SG Replicate replications
  2. Add the Inter-Sync Gateway replication configuration, including Javascript function as [custom\_conflict\_resolver](configuration-properties-legacy.md#databases-this%5Fdb-replications-this%5Frep-custom%5Fconflict%5Fresolver)
  3. Upgrade each cluster to 2.8
* Restart Outcomes

  * When the active cluster is restarted it will automatically switch to Inter-Sync Gateway Replication
  * Replication will continue from the last checkpoint, unless over-ridden.
  * [ENTERPRISE EDITION](https://www.couchbase.com/products/editions) The replication will distribute automatically
* Conflict resolution — Conflicts will be handled by the function specified as the as [custom\_conflict\_resolver](configuration-properties-legacy.md#databases-this%5Fdb-replications-this%5Frep-custom%5Fconflict%5Fresolver)
* Upgrade Constraint — The `allow_conflicts` flag is ignored for any inter-Sync Gateway replication replications configured.

### [](#re-using-sg-replicate-checkpoints)Re-using SG Replicate Checkpoints

You are able to use SG Replicate [checkpoint![glossary icon](_images/icons/glossaryIconImage2.png)](glossary.md#checkpoint) as a starting point for Inter-Sync Gateway replications. This can save time on larger buckets by avoiding re-processing documents that have previously been replicated.

To be eligible for re-use use in this way

* These replication parameters MUST match:

  * Replication ID
  * Direction (push or pull only)
  * Previous Source/Target URLs match Remote URL
  * Channel filters
  * DocID filters
* The new replication must be configured to be unidirectional (there was no bidirectional support prior to 2.8)

### [](#upgrade-steps)Upgrade Steps

1. Have both SG Replicate and Inter-Sync Gateway replications defined in the same config file.
2. Ensure prerequisites from previous slide are fulfilled (matching IDs, params, etc.)
3. On startup, Sync Gateway will determine if replications match, and log:  
```none  
[DBG] Replicate+: Matched replication IDs for SGR1 checkpoint fallback: &{...}  
[INF] Replicate: Got SGR1 checkpoint ID for fallback in replication "repl1-push": b8da8486df3093141f7ed225eb2b2afae88ca9ce  
```
4. This prevents the SG Replicate replication from running, even though it's configured.  
```none  
[INF] Replicate: Replication "repl1-push" was upgraded, preventing startup of SG Replicate replication.  
[INF] Replicate: Replication "repl1-pull" was upgraded, preventing startup of SG Replicate replication.  
[INF] Replicate: Starting sg-replicate replications...  
```
5. When the Inter-Sync Gateway replication is assigned (even on a different node), the SG Replicate checkpoint is used if no Inter-Sync Gateway checkpoint can be found. Logs:  
```none  
[DBG] SGCluster+: Replication repl1-pull is assigned to node debbc9ed92243c01 (local node is debbc9ed92243c01)  
[INF] Replicate: Initializing replication repl1-pull  
[INF] Replicate: Attempting to fetch SGR1 checkpoint as fallback: 58782a013091ffc0e7e4ae3c4b6abd8baa7149c6  
[INF] Replicate: c:repl1-pull-pull using checkpointed seq from SGR1: "3"  
```
6. Once the SG Replicate checkpoint is used, it is deleted to ensure it cannot be used as a fallback again in the event Inter-Sync Gateway replication [checkpoints![glossary icon](_images/icons/glossaryIconImage2.png)](glossary.md#checkpoint) are removed.

## [](#upgrade-from-views-to-gsi)Upgrade from Views to GSI

Prior to 2.1, Sync Gateway used system views for a variety of internal operations, including authentication and replication. Starting in 2.1, Sync Gateway will use GSI and N1QL to perform those tasks.

The upgrade, from using views to using Global Secondary Indexes and N1QL, happens automatically when starting a Sync Gateway 2.1 or above node in a cluster that was previously using views.

Use of GSI requires Couchbase Server 5.5, with at least one node running the Query and Index Services. Users wanting to run Sync Gateway 2.1 or above with an older version of Couchbase Server will need to continue to use views, by setting the `use_views` property.

## [](#upgrade-to-shared-bucket)Upgrade to Shared Bucket

### [](#implementation-notes-for-xattrs)Implementation notes for XATTRs:

Mobile applications require additional metadata in order to manage security and replication. In previous versions of Sync Gateway, this information has always been stored in the document body. Sync Gateway 1.5 utilizes a new feature of Couchbase Server 5.0 called XATTRs (x-attributes) to store that metadata into an external document fragment.

Extended attributes (xattrs) are JSON objects that can be associated with Couchbase documents. Each document can be associated with zero or more extended attributes. There are currently three types (user, system, virtual). Mobile Convergence uses a system extended attribute, which has the following characteristics central to convergence:

* Shares lifetime with the document metadata - when a document is deleted, system xattrs are preserved with the tombstone.
* Allocated 1MB of storage, independent of the 20MB available for the document

Extended attributes are stored as part of the document, and are replicated with the document (both intra-cluster replication and XDCR).

Extended attributes can be accessed via the SDKs using the sub-document API, via command-line tools, and via views.

They are also accessible from N1QL in Couchbase Server 5.5 or above with the `().xattrs` property. For example, `SELECT meta().xattrs._sync from travel-sample where Meta().id = "user::demo";`.

> [!WARNING]
> The sync metadata is maintained internally by Sync Gateway and its structure can change at any time. It should not be used to drive business logic of applications. The direct use of the N1QL query is unsupported and must not be used in production environments.

The [raw](rest-api-admin.md#/document/get<em>db</em><em>raw%5F%5Fdoc</em>)endpoint on Sync Gateway's Admin REST API returns both the document and its associated mobile metadata.

### [](#configuration-changes)Configuration Changes

| Before                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | After                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------ |
| **Sync Gateway 1.5 or above** shared\_bucket\_access: false                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | **Sync Gateway 1.5 or above** shared\_bucket\_access: true   |
| After restarting Sync Gateway with the updated configuration file, the mobile metadata for existing documents is automatically migrated. To enable shared bucket on incoming documents, one Sync Gateway node in the cluster must also have the import\_docs: continuous property in the configuration file. Enabling shared bucket access on your existing deployment is **not** reversible. It is recommended to test the upgrade on a staging environment before upgrading the production environment. The known issue [CBG-394](release-notes.md#2-5-0), means that the upgrade will **require downtime** when enabling shared bucket access on an existing deployment that is running with GSI indexing. This is to allow all documents to migrate, using index-based data requests whilst migration is in progress could result in an incomplete data set being returned (containing only those docs migrated at the time of the request). You are advised to schedule a maintenance window to allow time for migration to complete. |                                                              |
| **Sync Gateway 2.1 or above** num\_index\_replicas: 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | **Sync Gateway 2.1 or above** num\_index\_replicas: 2 (or n) |
| After restarting Sync Gateway with the updated configuration file, the number of Index Replicas in the Couchbase Server cluster is automatically updated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |                                                              |

## [](#migrating-from-bucket-shadowing)Migrating from Bucket Shadowing

As of Sync Gateway 1.5, the Bucket Shadowing feature is deprecated and no longer supported. The following steps outline a recommended method for migrating from Bucket Shadowing to the latest version with interoperability between Couchbase Server SDKs and Couchbase Mobile.

1. Follow the recommendations in the [Couchbase Server documentation](#server:install:upgrade-online.adoc) to upgrade all instances to 5.0.
2. Create a new bucket on Couchbase Server (**bucket 2**).
3. Install Sync Gateway 1.5 on a separate node with shared access enabled and connect it to the new bucket (**bucket 2**).
4. Setup a push replication from the Sync Gateway instance used for Bucket Shadowing to the Sync Gateway 1.5 instance.
5. Once the replication has completed, test your application is performing as expected.
6. Update the load balancer to direct incoming traffic to the Sync Gateway 1.5 instance when you are ready to upgrade.
7. Delete the first bucket (**bucket 1**).

![bucket shadowing migration](_images/bucket-shadowing-migration.png)

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Getting Started

* [Prepare](get-started-prepare.md)
* [Install](get-started-install.md)
* [Verify](get-started-verify-install.md)

###### [](#-3)

Product Information

* [Release Notes](release-notes.md)
* [Compatibility Matrix](compatibility.md)
* [Supported OS](supported-environments.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)