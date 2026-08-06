---
title: Rolling Upgrade
description: Step-by-step procedures for performing a rolling upgrade of a Sync
  Gateway cluster for each supported version.
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.1/modules/ROOT/pages/rolling-upgrade.adoc
pubDate: 2026-08-06T05:31:06.200Z
link: xref:sync-gateway::rolling-upgrade.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/current/rolling-upgrade.html)

# Rolling Upgrade

> Step-by-step procedures for performing a rolling upgrade of a Sync Gateway cluster for each supported version.  

Related _Application Deployment_ topics: [Prepare](start-here/get-started-prepare.md) | [Release Notes](product-notes/release-notes.md)

## [](#about-rolling-upgrades)About Rolling Upgrades

A rolling upgrade is the recommended method to upgrade a Sync Gateway cluster. You upgrade nodes one at a time while the cluster continues serving traffic, avoiding downtime.

At a high level, a rolling upgrade consists of the following steps:

1. Remove the node from the load balancer or stop HTTP traffic to the node.
2. Run the upgrade on that node.
3. Re-add the node to the load balancer or resume traffic to the node.

Repeat these steps for each node in the Sync Gateway cluster.

> [!NOTE]
> Sync Gateway 4.1 introduces cluster compatibility version, which lets you perform a rolling upgrade with a safe rollback path and without reducing cluster capacity. See [Cluster Compatibility Version](cluster-compatibility-version.md).

## [](#upgrade-to-syncgateway-4-1)Upgrade to Sync Gateway 4.1

### [](#prerequisites)Prerequisites

1. Verify your Couchbase Server cluster is running 7.6.0 or later. Bi-directional XDCR features require 7.6.6 or later.
2. Verify all Couchbase Server nodes are operational before starting the Sync Gateway upgrade.
3. Check your existing Sync Gateway configuration files and remove any unsupported settings:

  * `shared_bucket_access=false`
  * `allow_conflicts=true`
  * `enable_star_channel=false`  
Databases configured with these settings do not start on Sync Gateway 4.1.

### [](#procedure)Procedure

For each node in the cluster, repeat the following steps:

1. Remove the node from the load balancer or stop HTTP traffic to the node.
2. Install Sync Gateway 4.1 on the node.
3. Start the Sync Gateway service.
4. Verify the node is healthy using the [GET /](rest-api/rest%5Fapi%5Fadmin.md#tag/Server/operation/get%5F-) endpoint on the Admin REST API.
5. Verify all databases on the node are online.
6. Re-add the node to the load balancer or resume HTTP traffic to the node.

> [!NOTE]
> Downgrading from Sync Gateway 4.1 to an earlier version is not supported after the full cluster has been upgraded. If you require a rollback path during the upgrade window, use [Cluster Compatibility Version](cluster-compatibility-version.md) before starting.

## [](#upgrade-to-syncgateway-4-0)Upgrade to Sync Gateway 4.0

### [](#prerequisites-2)Prerequisites

1. Verify your Couchbase Server cluster is running 7.6.0 or later. Bi-directional XDCR features require 7.6.6 or later.
2. Verify all Couchbase Server nodes are operational before starting the Sync Gateway upgrade.
3. Check your existing Sync Gateway configuration files and remove any unsupported settings:

  * `shared_bucket_access=false`
  * `allow_conflicts=true`
  * `enable_star_channel=false`  
Databases configured with these settings do not start on Sync Gateway 4.0.

### [](#procedure-2)Procedure

For each node in the cluster, repeat the following steps:

1. Remove the node from the load balancer or stop HTTP traffic to the node.
2. Update the configuration file if it contains any unsupported settings listed in the prerequisites.
3. Install Sync Gateway 4.0 on the node.
4. Start the Sync Gateway service.
5. Verify the node is healthy using the [GET /](rest-api/rest%5Fapi%5Fadmin.md#tag/Server/operation/get%5F-) endpoint on the Admin REST API.
6. Verify all databases on the node are online.
7. Re-add the node to the load balancer or resume HTTP traffic to the node.

> [!NOTE]
> Downgrading from Sync Gateway 4.0 to earlier versions is not supported.

## [](#upgrade-to-syncgateway-3-1)Upgrade to Sync Gateway 3.1

### [](#about-persistent-configuration)About Persistent Configuration

Sync Gateway 3.1 uses Persistent Configuration as its default operational mode. When you start a Sync Gateway 3.1 node with an existing configuration file, Sync Gateway automatically converts the configuration to the persistent format.

> [!CAUTION]
> Migration to the 3.x Persistent Configuration is a one-way process. You cannot downgrade to a previous version after upgrading to 3.1.

Before starting the upgrade, confirm the following:

* Sync Gateway has write access to the directory containing the existing configuration file. Sync Gateway creates a backup of the existing configuration before writing the upgraded version.
* If your configuration file contains multiple databases, all `server` fields used to connect to Couchbase Server must match. Sync Gateway uses the first set of credentials for the bootstrap configuration.  
> [!NOTE]  
> Sync Gateway cannot automatically upgrade configurations with multiple distinct `server` fields. You must create the bootstrap configuration manually in this case.

Consider the following before starting:

* Configuration groups: most deployments use the default group. If you require custom node groupings, add the `bootstrap_group_id` value to your configuration file before startup. See [bootstrap.group\_id](configuration/configuration-schema-bootstrap.md#bootstrap-group%5Fid).
* TLS: Sync Gateway 3.0 and later enables secure TLS connections to Couchbase Server by default. To use a non-secure connection in a test environment, set [bootstrap.use\_tls\_server](configuration/configuration-schema-bootstrap.md#bootstrap-use%5Ftls%5Fserver) to `false`. See [Secure Sync Gateway Access](security/secure-sgw-access.md).
* Admin API authentication: Secure Administration requires Couchbase Server RBAC users for Admin and Metrics API access. Configure the appropriate users before upgrading. See [REST API Access](rest-api/rest-api-access.md).

### [](#procedure-3)Procedure

1. Start a Sync Gateway 3.1 node using your existing configuration properties file.  
Sync Gateway takes the appropriate upgrade path based on the current configuration state:

| Configuration status                      | Inference                                                                     | Outcome                                                                                                                        |
| ----------------------------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| No configuration exists                   | This is the first node in the default group, or with this group ID, to start. | Sync Gateway uses the configuration file to derive and persist a configuration for this node.                                  |
| Configuration exists in the server bucket | A node in the default group, or with this group ID, has already started.      | Sync Gateway ignores the configuration file and uses the configuration associated with the default group or group ID provided. |
2. Verify the node is healthy using the [GET /](rest-api/rest%5Fapi%5Fadmin.md#tag/Server/operation/get%5F-) endpoint on the Admin REST API.
3. Re-add the node to the load balancer or resume traffic to the node.
4. Repeat for each remaining node in the cluster.

---

##### 

## [](#related-content)Related Content

###### [](#-2)

Getting Started

* [Prepare](start-here/get-started-prepare.md)
* [Install](start-here/get-started-install.md)
* [Configure](start-here/get-started-configure.md)

###### [](#-3)

Product Information

* [Release Notes](product-notes/release-notes.md)
* [Compatibility Matrix](product-notes/compatibility.md)
* [Supported OS](product-notes/supported-environments.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)