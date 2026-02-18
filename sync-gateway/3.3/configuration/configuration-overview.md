---
title: Configuration Overview
description: How to configure <em>Sync&#160;Gateway</em> for secure cloud-to-edge data sync
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.3/modules/configuration/pages/configuration-overview.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/sync-gateway/3.3/configuration/configuration-overview.html)

# Configuration Overview

> How to configure _Sync Gateway_ for secure cloud-to-edge data sync  

_Related topics_: [Overview](configuration-overview.md) | [Bootstrap](configuration-schema-bootstrap.md) | [Database](configuration-schema-database.md) | [Database Security](configuration-schema-db-security.md) | [Access Control](configuration-schema-access-control.md) | [Import](configuration-schema-import-filter.md) | [Inter-Sync Gateway Replication](configuration-schema-isgr.md)

## [](#introduction)Introduction

_Sync Gateway_ 3.0 introduces _Centralized Persistent Modular Configuration_, to better suit its use in increasingly prevalent multi-node, multi-cluster deployments. Centralized persistent modular configuration replaces the established, file-based configuration method \[[1](#%5Ffootnotedef%5F1 "View footnote.")\], supporting the move away from a reliance on increasingly monolithic central configuration files. It enables simpler, more agile configuration updates and encompasses:

* **Bootstrap Startup**  
A minimal configuration file is used to bootstrap a sync gateway node and attach it to its Couchbase Server cluster; these files and their settings are node-specific — see the [Bootstrap Configuration](configuration-schema-bootstrap.md)
* **Dynamic Configuration**  
The ability to make remote in-flight configuration changes to database settings, access-control policies and inter-sync gateway replications, enables simpler and more agile maintenance.
* **Cluster-aware Updates**  
Configuration changes made to a node through the API endpoints are propagated to other sync gateway nodes belonging to the same cluster (or to a user-defined subset of nodes) — [Configuration Groups](#lbl-config-grp)
* **Persistent Updates**  
Any database changes made using the API endpoints are persisted and survive sync gateway node restarts (this does not apply when running in file-based configuration mode).
* **Secure REST API**  
by default the REST API requires authentication and authorization using Couchbase Server RBAC-user credentials — see [Secure Sync Gateway Access](../security/secure-sgw-access.md). This can be disabled for test purposes only.
* **Automatic upgrade path**  
Your existing legacy Pre-3.0 configuration files will (optionally) be automatically converted, on start-up, to the new format for centralized persistent modular configuration.

## [](#workflow)Workflow

In the _Centralized Persistent Modular Configuration_ ecosphere you provide a minimal bootstrap configuration to get Sync Gateway started, then add users, roles, database and replications using the REST API.

![persistent config](../_images/persistent-config.png) 

Figure 1\. Configuration Workflow

1. Set up a user for the Admin REST API on Couchbase Server  
Alternatively, you can disable authentication of REST API user(s) — for test purposes **only**
2. Provide a [bootstrap configuration file](configuration-schema-bootstrap.md), in JSON format, which defines the sync gateway node’s run time behavior. This configuration is node-specific. Any changes require a sync gateway restart.
3. Add or amend configuration items in-flight using the Admin Rest API.  
All changes are persisted across sync gateway restarts. Auto restarts will be initiated for ny change that requires one. You will need to configure and maintain:

  1. Databases  
  Use the Admin REST API endpoint [Database Configuration](configuration-schema-database.md) endpoints to add required databases.
  2. Database Security  
  Use the [Database Security](configuration-schema-db-security.md) endpoints to configure users and roles.
  3. Access Control  
  Use the [Access Control](configuration-schema-access-control.md) endpoints to configure your Sync Function.
  4. Inter-Sync Gateway replications  
  Use the [inter-sync gateway replication](configuration-schema-isgr.md) endpoints to configure required replications.

### [](#opt-out)Opt-out

To continue using legacy Pre-3.0 configuration you should start sync gateway with [disable-persistent-config](configuration-properties-legacy.md#disable%5Fpersistent%5Fconfig) set `true` either in the configuration file or in [Command Line Options](../deploy/command-line-options.md).

This ensures you can use the [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md). Note that no Admin REST API changes are persisted across sync gateway restarts.

## [](#key-terms)Key Terms

| Term                             | Description                                                                                                                                                  |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Sync Gateway Cluster             | A collection of sync gateway nodes connected to a common Couchbase Server cluster                                                                            |
| Homogeneous Sync Gateway Cluster | A sync gateway cluster where every node in cluster shares common configuration                                                                               |
| Sync Gateway Config Group        | A group of sync gateway nodes within a sync gateway cluster sharing common configuration. Each node in the group will continue to have node-specific config. |

## [](#configuration-levels)Configuration Levels

All the configuration properties, whether defined in the bootstrap configuration file or by the Admin REST API endpoint belong to one of two core 'levels': _node_ or _database_ — see [Table 1](#tbl-cfg-levels)

__Table 1\. Configuration levels in centralized persistent modular configuration__
| Level                  | Use                                                                                                | Scope                                                                                                                                    | Changeable?                                                           |                                                   |
| ---------------------- | -------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- | ------------------------------------------------- |
| Node                   | Couchbase Server connection                                                                        | Minimal set of configuration properties required for connection to Couchbase Server bucket, for example server credentials, and group id | Node-specific; unshared                                               | Yes, file-editRestart required                    |
| System properties      | Node level system properties including, for example, api.tls.cert\_path and max\_file\_descriptors | Node-specific; unshared                                                                                                                  | Yes, file-editRestart required                                        |                                                   |
| Logging properties     | Logging-related properties                                                                         | Node-specific; unshared                                                                                                                  | Yes by the Admin REST APINo restart, but **not persisted**            |                                                   |
| Database               | DB properties                                                                                      | Database configuration properties including, for example, bucket, or access control policies such as users and sync                      | May be node-specific, but typically shared across nodes in same group | Yes, by Admin REST APIRestart initiated as needed |
| Replication properties | inter-sync gateway replication properties                                                          | Shared across all participating replication nodes                                                                                        | Yes, by Admin REST APIRestart initiated as needed                     |                                                   |

## [](#lbl-auth)Secure Administration

Secure Administration is **on** by default.

In order to submit Admin or Metrics REST API requests you should create specific Couchbase Server users for that purpose. You will then provide a valid set of Couchbase Server credentials for these RBAC-users in each API request.

Authenticated users will have access to Admin and-or Metrics API functionality, application data and configuration settings.

For more see: [REST API Access](../rest-api/rest-api-access.md)

## [](#lbl-config-grp)Configuration Groups

You can group sync gateway nodes into homogenous clusters using the `Config-Group-ID` property ([bootstrap.group\_id](configuration-schema-bootstrap.md#bootstrap-group%5Fid)). This defines the database configuration group to which a node belongs.

All nodes in a group share the same database configuration. Changes made from one node are propagated to other nodes in the group automatically.

All nodes in a cluster belong, by default, to a common shared group `default`.

If you move a sync gateway node to a new group, it will inherit the configuration associated with that group. This applies also if you move a group (back) into the `default` group.

---

##### 

## [](#related-content)Related Content

###### [](#-2)

API Topics

* [Public REST API](../rest-api/rest-api.md)
* [Admin REST API](../rest-api/rest-api-admin.md)
* [Metrics REST API](../rest-api/rest-api-metrics.md)

###### [](#-3)

Reference

* [Bootstrap](configuration-schema-bootstrap.md)
* [Database](configuration-schema-database.md)
* [Database Security](configuration-schema-db-security.md)
* [Access Control](configuration-schema-access-control.md)
* [Import Filter](configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication](configuration-schema-isgr.md)
* [Legacy Pre-3.0 Configuration](configuration-properties-legacy.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)

---

[1](#%5Ffootnoteref%5F1). You can continue using file-based configuration by using the CLI option `-disable_persistent_config` when starting Sync Gateway