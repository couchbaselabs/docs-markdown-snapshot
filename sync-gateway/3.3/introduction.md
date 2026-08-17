---
title: Sync Gateway
description: Sync Gateway is a secure, high-performance gateway designed for
  cloud-to-edge data synchronization.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/3.3/modules/ROOT/pages/introduction.adoc
  xref: xref:3.3@sync-gateway::introduction.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/3.3/introduction.html)

# Sync Gateway

Sync Gateway is a secure, high-performance gateway designed for cloud-to-edge data synchronization. It serves as the synchronization server in a Couchbase Mobile deployment, enabling mobile, web, and IoT applications to view and sync data with Couchbase Server.

You can use Sync Gateway in conjunction with Couchbase Lite for full Bi-directional sync between edge devices and the cloud. It provides fine-grained access control, RESTful API, and secure sync capabilities.

![cbm architecture](_images/cbm-architecture.png) 

Figure 1\. Couchbase Mobile — Deployment Architecture

As you can see from [Figure 1](#fig-mobile-server) Sync Gateway synchronizes changes made by web clients through its REST API, Couchbase Lite mobile-device applications, and Couchbase Server buckets.

You can read more about the Data Synchronization process in [Sync with Couchbase Server](sync/sync-with-couchbase-server.md). Some of its most central, and commonly used features, are those used to secure [Access Control](access-control/access-control-model.md).

Sync Gateway assures secure access control using:

* **User authentication**, which ensures that only authorized users can connect to Sync Gateway. For more information see the [Users](access-control/users.md), [Roles](access-control/roles.md) and [User Authentication](security/authentication-users.md) content.
* **Data Routing**, which ensures that authorized users can only access documents in those [Channels](access-control/channels.md) assigned to them and only in accordance with their assigned privileges. You can set those privileges to confer [Read Access](access-control/access-control-how-control-document-access.md#lbl-read-access) and-or [Write Access](access-control/access-control-how-control-document-access.md#lbl-write-access) as required.

The business logic behind the validation and authorization of document access is provided by the customizable [Sync Function](access-control/sync-function/sync-function.md).

## Why Use Sync Gateway?

* Bi-directional synchronization: Sync data between Couchbase Lite clients and Couchbase Server with real-time updates.
* Secure access control: Supports RBAC, channels, and sync functions.
* RESTful API: Public, Admin and Metric REST API interfaces for data and configuration access.
* Scalable architecture: Designed for high-throughput, cloud-to-edge synchronization.

## Key Capabilities

* Fine-grained data distribution using channels for efficient synchronization.
* Sync Function support: Customizable business logic for validation, transformation, and access control.
* Role-Based Access Control.
* RESTful API: Public, Admin and Metric REST API interfaces for data and configuration access.
* Integration with Couchbase Lite and Couchbase Server.
* Supports peer-to-peer, cloud, and hybrid sync topologies.

# 

> [!TIP]
> For more information about the latest changes to Sync Gateway, see [New In 3.3](whatsnew.md).

## Get Started

Get started with Sync Gateway, from preparing your environment to installing and verifying your installation.

* [Prepare your environment](start-here/get-started-prepare.md)
* [Install Sync Gateway](start-here/get-started-install.md)
* [Verify your installation](start-here/get-started-verify-install.md)

## Data Modeling

Learn how to design and structure your data buckets and documents using Sync Gateway.

* [Data Modelling](data-modeling.md)

## Configuration

Learn how to configure Sync Gateway for cloud to edge synchronization including bootstrap, database settings, security, and more.

* [Bootstrap Configuration](configuration/configuration-schema-bootstrap.md)
* [Database Configuration](configuration/configuration-schema-database.md)
* [Database Security](configuration/configuration-schema-db-security.md)
* [Access Control Configuration](configuration/configuration-schema-access-control.md)
* [Import Filter Configuration](configuration/configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication Configuration](configuration/configuration-schema-isgr.md)
* [Using External Javascript Functions](configuration/configuration-javascript-functions.md)
* [Configuration Environment Variables](configuration/configuration-environment-variables.md)

## Security

Implement comprehensive security measures to protect your data and control access to Sync Gateway.

* [Secure Sync Gateway Access](security/secure-sgw-access.md)
* [User Authentication](security/authentication-users.md)
* [TLS Certificate Authentication](security/authentication-certs.md)
* [Audit Logging](security/audit-logging.md)

## Access Control

Configure fine-grained access control with users, roles, channels, and sync functions.

* [Access Control Concepts](access-control/access-control-concepts.md)
* [Sync Function](access-control/sync-function/sync-function.md)
* [How to](access-control/access-control-how.md)
* [Auto-Purge on Channel Access Revocation](access-control/auto-purge-channel-access-revocation.md)

## REST API

Interact with Sync Gateway programmatically using comprehensive REST API interfaces.

* [Secure API Access](rest-api/rest-api-access.md)
* [Admin REST API](rest-api/rest-api-admin.md)
* [Metrics REST API](rest-api/rest-api-metrics.md)
* [Public REST API](rest-api/rest-api.md)
* [RBAC Role — Endpoint Cross-reference](rest-api/rest-api-access-rbac-roles.md)

## Sync

Synchronize data between Sync Gateway and your applications, servers, and other Sync Gateway instances.

* [Sync with Couchbase Server](sync/sync-with-couchbase-server.md)
* [Sync with Couchbase Lite](sync/sync-using-app.md)
* [Inter-Sync Gateway Replication](sync/sync-inter-syncgateway-overview.md)
* [Delta Sync](sync/delta-sync.md)
* [Import Processing](sync/import-processing.md)

## Manage

Perform administrative and operational tasks to maintain and monitor Sync Gateway.

* [Revisions](manage/revisions.md)
* [Tombstones](manage/managing-tombstones.md)
* [Resync](manage/resync.md)
* [View Statistics and Metrics](manage/stats-monitoring.md)
* [Take Database Offline/Online](manage/database-offline.md)
* [Logging](manage/logging.md)

## Deploy

Deploy Sync Gateway in production environments with scalability and reliability considerations.

* [Using the Command Line](deploy/command-line-options.md)
* [Load Balancer](deploy/load-balancer.md)
* [Webhooks](deploy/webhooks.md)
* [Integrate Prometheus](deploy/stats-prometheus.md)
* [Indexing](deploy/indexing.md)
* [Deploying a Sync Gateway Cluster](use-kubernetes/deploy-cluster-to-kubernetes.md)

## Server Compatibility

Understand Sync Gateway compatibility with Couchbase Server features and services.

* [Buckets](server-compatibility/server-compatibility-buckets.md)
* [Collections](server-compatibility/server-compatibility-collections.md)
* [Eventing](server-compatibility/server-compatibility-eventing.md)
* [Transactions](server-compatibility/server-compatibility-transactions.md)
* [XDCR](server-compatibility/server-compatibility-xdcr.md)
* [Backup and Restore](server-compatibility/server-compatibility-backups.md)