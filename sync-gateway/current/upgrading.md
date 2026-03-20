---
title: Upgrading Sync Gateway
description: This page documents various implementation details and
  functionalities to consider when performing an upgrade to Sync Gateway 4.0.
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.0/modules/ROOT/pages/upgrading.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:sync-gateway::upgrading.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/current/upgrading.html)

# Upgrading Sync Gateway

> This page documents various implementation details and functionalities to consider when performing an upgrade to Sync Gateway 4.0.  

Related _Application Deployment_ topics: [Prepare](start-here/get-started-prepare.md) | [Install](start-here/get-started-install.md) | [Release Notes](product-notes/release-notes.md)

## [](#upgrade-approaches)Upgrade Approaches

A rolling upgrade is the recommended method to upgrade a Sync Gateway cluster. At a high level, a rolling upgrade consists of the following steps:

1. The load balancer configuration stops any HTTP traffic to the node you’re upgrading.
2. The upgrade runs on the given node.
3. The load balancer configuration resumes traffic to the upgraded node.

Those steps are then repeated for each node in the sync gateway cluster.

## [](#upgrade-to-4-0)Upgrade to 4.0

### [](#upgrade-requirements)Upgrade Requirements

1. Couchbase Server 7.6.6 or later for bi-directional XDCR features.
2. `shared_bucket_access=false` is no longer supported - databases do not start with `shared_bucket_access=false`.
3. `allow_conflicts=true` no longer supported - databases do not start with this setting.
4. `enable_star_channel=false` is no longer supported - databases do not start with this setting.

> [!NOTE]
> As with all major version upgrades, downgrading from 4.0 to earlier versions is not supported.

#### [](#process)Process

Prerequisites

1. Upgrade Couchbase Server cluster to 7.6.0 or later and verify all server nodes are operational.
2. Test Sync Gateway connectivity with existing version to verify compatibility.

Step 1

1. Remove a node from the load balancer or stop traffic to the node.
2. Update the configuration file, if using unsupported settings:

  * Remove `shared_bucket_access=false`.
  * Remove `allow_conflicts=true`.
  * Remove `enable_star_channel=false`.
3. Install Sync Gateway 4.0
4. Start the Sync Gateway service.
5. Verify node health via [REST API](rest-api/rest%5Fapi%5Fpublic.md#tag/Server/operation/get%5F-).

Step 2

1. Verify all databases are online.
2. Re-add the node to the load balancer or resume traffic to the node.

## [](#upgrade-to-3-1)Upgrade to 3.1

### [](#use-persistent-configuration)Use Persistent Configuration

The use of 3.x’s Persistent Configuration feature is strongly recommended. It’s the default operational mode when starting sync gateway.

The feature provides a smooth upgrade path for existing users by automatically converting their existing configuration files to the new persistent configuration format.

> [!CAUTION]
> One Way Upgrade
> 
> The migration to 3.x configuration is a ONE WAY process. You cannot downgrade to previous versions after upgrading to 3.1\. To continue using legacy-mode configuration see: [\[lbl-3-0-upgrade-opt-out\]](#lbl-3-0-upgrade-opt-out)

#### [](#considerations)Considerations

Before commencing your upgrade consider your requirements for [Configuration Groups](#lbl-3-0-config-grps) although most users find the default group sufficient, [Secure Server Connection](#lbl-3-0-config-tls) and [Secure Administration](#lbl-3-0-config-adm).

You should also:

* Ensure Sync Gateway has write access to the directory containing the existing configuration (the one you want to convert). It backups the existing configuration and write the upgraded configuration.
* Verify that, if your existing configuration has multiple databases, all of the **server** fields used to connect to **Couchbase Server** match.  
Although the connection credentials used may differ between databases, Sync Gateway only uses the **first** set of credentials for the bootstrap configuration file.  
> [!NOTE]  
> Sync Gateway cannot automatically upgrade configurations that have multiple distinct server fields within the configuration file, and you’ll need to manually create their own bootstrap configuration.

#### [](#process-2)Process

Just start a sync gateway node using your existing configuration properties file.

On starting, Sync Gateway takes the appropriate upgrade path as shown in [Table 1](#tbl-enhancedcfg).

__Table 1\. Upgrade Paths__
| Configuration Status                      | Inference                                                                   | Outcome                                                                                                                             |
| ----------------------------------------- | --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| No configuration exists                   | This is first node in the default group or with this **group ID** to start  | Sync gateway uses the configuration file to derive and persist a configuration for this node.                                       |
| Configuration exists in the Server bucket | A node in the default group, or with this **group ID**, has already started | Sync gateway ignores the configuration file and uses the configuration associated with the default group, or **group ID** provided. |

#### [](#lbl-3-0-config-grps)Configuration Groups

Whilst the provided default group suffices for most deployments sync gateway does allow for the configuration of more complex node groupings.

Before commencing your upgrade consider your requirements for grouping sync gateway nodes within your sync gateway cluster — see: [Configuration Groups](configuration/configuration-overview.md#lbl-config-grp)

If you want the sync gateway to associate with a specific configuration group Id, you must add the `bootstrap_group_id` value to the configuration file prior to startup — see: [bootstrap.group\_id](configuration/configuration-schema-bootstrap.md#bootstrap-group%5Fid)

Failing to do so may result in the configuration being overridden by one configured on a different sync gateway node that has already started and registered its own configuration.

### [](#lbl-3-0-config-tls)Secure Server Connection

Sync Gateway 3.0 enables secure TLS connection to Couchbase Server out-of-the-box.

If you wish to use non-secure connection, perhaps in a test environment, you need to run sync gateway with [bootstrap.use\_tls\_server](configuration/configuration-schema-bootstrap.md#bootstrap-use%5Ftls%5Fserver) set to `false` — see: [Secure Sync Gateway Access](security/secure-sgw-access.md)

#### [](#lbl-3-0-config-adm)Secure Administration

Secure Administration is under-pinned by the use of Couchbase Server RBAC-users to authenticate and authorize access to Admin and Metrics API feature. This requires you set-up and configure appropriate users — see: [REST API Access](rest-api/rest-api-access.md).

To opt-out of this, you can configure [api.api.admin\_interface\_authentication](configuration/configuration-schema-bootstrap.md#api-admin%5Finterface%5Fauthentication) and-or [api.metrics\_interface\_authentication](configuration/configuration-schema-bootstrap.md#api-metrics%5Finterface%5Fauthentication) as `false`

## [](#couchbase-server-upgrade-paths)Couchbase Server Upgrade Paths

> [!NOTE]
> When upgrading your Couchbase Server from 4.x to 5.x, remember to create a Sync Gateway RBAC user on the server — see: [Configure Server for Sync Gateway](start-here/get-started-prepare.md#configure-server.html) — and to include the user’s credentials username/password in you Sync-Gateway-Config.json file.

All of the different upgrade paths mentioned above assume that you’re running a compatible Couchbase Server version — see [Compatibility Matrix](product-notes/compatibility.md).

Three commonly used upgrade approaches exist for Couchbase Server. Depending on the one you choose, there may be additional consideration to keep in mind when using Sync Gateway:

| Approach                                     | Downtime                       | Additional Machine Requirements | Impact when using Sync Gateway                                                                                                                                                                                                                                                                                                                                                        |
| -------------------------------------------- | ------------------------------ | ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Rolling Online Upgrade                       | None                           | Low                             | **Potential transient connection errors:** The Couchbase Server re-balance operations can result in transient connection errors between Couchbase Server and Sync Gateway, which could result in Sync Gateway performance degradation. **Potential for unexpected server errors during re-balance:** In-flight ops are lost during a fail-over due to increased potential for errors. |
| Upgrade Using Inter-Sync Gateway Replication | Small amount during switchover | High - duplicate entire cluster | Using an XDCR (Cross Data Center Replication) approach incurs some Sync Gateway downtime, but less than other approaches where Sync Gateway is shutdown during the entire Couchbase Server upgrade.                                                                                                                                                                                   |
| Offline Upgrade                              | During entire upgrade          | None                            | Take Sync Gateway offline Upgrade Couchbase Server using any of the options mentioned in the [Upgrading Couchbase Server](../../server/current/install/upgrade.md) documentation. Bring Sync Gateway online                                                                                                                                                                           |

The XDCR replication must be a **one way** replication from the existing (source) Couchbase Server cluster to the new (target) Couchbase Server cluster. No other writes can happen on the new (target) Couchbase Server cluster other than the writes from the XDCR replication. Do not configure any Sync Gateway instances to use the new (target) Couchbase Server cluster until the last step in the process.

1. Start XDCR to do a one way replication from the existing (source) Couchbase Server cluster to the new (target) Couchbase Server cluster running the earlier version.
2. Wait until the target Couchbase Server has caught up to all the writes in the source Couchbase Server cluster.
3. Shutdown Sync Gateway to prevent any new writes from coming in.
4. Wait until the target Couchbase Server has caught up to all the writes in the source Couchbase Server cluster — this should happen quickly, since it will only be the residual writes in transit before the Sync Gateway shutdown.
5. Reconfigure Sync Gateway to point to the target cluster.
6. Restart Sync Gateway.

Caveats:

* **Small amount of downtime during switchover:** Since there may be writes still in transit after Sync Gateway has been shutdown, there will need to be some downtime until the target Couchbase Server cluster is caught up.
* **XDCR should be monitored:** Make sure to monitor the XDCR relationship as per [XDCR docs](../../server/current/manage/manage-xdcr/xdcr-management-overview.md).

## [](#upgrade-to-shared-bucket)Upgrade to Shared Bucket

### [](#implementation-notes-for-xattrs)Implementation notes for XATTRs:

Mobile applications require additional metadata to manage security and replication. Sync Gateway has always stored this information in the document body in previous versions. Sync Gateway 1.5 utilizes a new feature of Couchbase Server 5.0 called XATTRs (x-attributes) to store that metadata into an external document fragment.

Couchbase documents can have associated JSON objects called extended attributes (xattrs). You can associate each document with zero or more extended attributes. Three types currently exist (user, system, virtual). Mobile Convergence uses a system extended attribute, which has the following characteristics central to convergence:

* System xattrs share lifetime with the document metadata - when you delete a document, the system preserves system xattrs with the tombstone.
* The system allocates 1MB of storage, independent of the 20MB available for the document

Couchbase Server stores extended attributes as part of the document and replicates them with the document (both intra-cluster replication and XDCR).

You can access extended attributes via the SDKs using the sub-document API, via command-line tools, and via views.

They’re also accessible from SQL++ in Couchbase Server 5.5 or above with the `().xattrs` property. For example, `SELECT meta().xattrs._sync from travel-sample where Meta().id = "user::demo";`.

> [!WARNING]
> Sync Gateway maintains the sync metadata internally and its structure can change at any time. Applications should not use it to drive business logic. Sync Gateway does not support the direct SQL++ query in production environments.

The [raw](rest-api/rest%5Fapi%5Fadmin.md#tag/Document/operation/get%5Fkeyspace-%5Fraw-docid)endpoint on Sync Gateway’s Admin REST API returns both the document and its associated mobile metadata.

### [](#configuration-changes)Configuration Changes

| Before                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | After                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------- |
| **Sync Gateway 1.5 or above** shared\_bucket\_access: false                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | **Sync Gateway 1.5 or above** shared\_bucket\_access: true  |
| After you restart Sync Gateway with the updated configuration file, Sync Gateway automatically migrates the mobile metadata for existing documents when you set import\_docs to true. To enable shared bucket access on incoming documents, set the import\_docs: true property on at least one Sync Gateway node in the cluster. Enabling shared bucket access on your existing deployment is **not** reversible. We recommend testing the upgrade on a staging environment before upgrading the production environment. The known issue [CBG-394](product-notes/release-notes.md#2-5-0), means that the upgrade will **require downtime** when enabling shared bucket access on an existing deployment that is running with GSI indexing. This is to allow all documents to migrate, using index-based data requests whilst migration is in progress could result in an incomplete data set being returned (containing only those docs migrated at the time of the request). You are advised to schedule a maintenance window to allow time for migration to complete. |                                                             |
| **Sync Gateway 2.1 to 3.2** num\_index\_replicas: 2 (or n)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | **Sync Gateway 3.3 or later** index.num\_replicas: 2 (or n) |
| After you restart Sync Gateway with the updated configuration file, Sync Gateway automatically updates the number of Index Replicas in the Couchbase Server cluster. As of Sync Gateway 3.3, num\_index\_replicas still works, but this option has been deprecated in favor of index.num\_replicas.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |                                                             |

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Getting Started

* [Prepare](start-here/get-started-prepare.md)
* [Install](start-here/get-started-install.md)
* [Verify](start-here/get-started-verify-install.md)

###### [](#-3)

Product Information

* [Release Notes](product-notes/release-notes.md)
* [Compatibility Matrix](product-notes/compatibility.md)
* [Supported OS](product-notes/supported-environments.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)