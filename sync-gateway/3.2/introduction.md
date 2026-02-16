[View original HTML](/sync-gateway/3.2/introduction.html)

Sync Gateway is a secure, high-performance gateway designed for cloud-to-edge data synchronization. It serves as the synchronization server in a Couchbase Mobile deployment, enabling mobile, web, and IoT applications to view and sync data with Couchbase Server.

You can use Sync Gateway in conjunction with Couchbase Lite for full Bi-directional sync between edge devices and the cloud. It provides fine-grained access control, RESTful API, and secure sync capabilities.

![cbm architecture](_images/cbm-architecture.png) 

Figure 1\. Couchbase Mobile — Deployment Architecture

As you can see from [Figure 1](#fig-mobile-server) Sync Gateway synchronizes changes made by web clients through its REST API, Couchbase Lite mobile-device applications, and Couchbase Server buckets.

You can read more about the Data Synchronization process in [Sync with Couchbase Server](sync-with-couchbase-server.md). Some of its most central, and commonly used features, are those used to secure [Access Control](access-control-model.md).

Sync Gateway assures secure access control using:

* **User authentication**, which ensures that only authorized users can connect to Sync Gateway. For more information see the [Users](users.md), [Roles](roles.md) and [User Authentication](authentication-users.md) content.
* **Data Routing**, which ensures that authorized users can only access documents in those [Channels](channels.md) assigned to them and only in accordance with their assigned privileges. You can set those privileges to confer [Read Access](access-control-how-control-document-access.md#lbl-read-access) and-or [Write Access](access-control-how-control-document-access.md#lbl-write-access) as required.

The business logic behind the validation and authorization of document access is provided by the customizable [Sync Function](sync-function.md).

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

|  | For more information about the latest changes to Sync Gateway, see [New In 3.2](whatsnew.md). |
|  | --------------------------------------------------------------------------------------------- |

## Get Started

Get started with Sync Gateway, from preparing your environment to installing and verifying your installation.

* [Prepare your environment](get-started-prepare.md)
* [Install Sync Gateway](get-started-install.md)
* [Verify your installation](get-started-verify-install.md)

## Data Modeling

Learn how to design and structure your data buckets and documents using Sync Gateway.

* [Data Modelling](data-modeling.md)

## Configuration

Learn how to configure Sync Gateway for cloud to edge synchronization including bootstrap, database settings, security, and more.

* [Bootstrap Configuration](configuration-schema-bootstrap.md)
* [Database Configuration](configuration-schema-database.md)
* [Database Security](configuration-schema-db-security.md)
* [Access Control Configuration](configuration-schema-access-control.md)
* [Import Filter Configuration](configuration-schema-import-filter.md)
* [Inter-Sync Gateway Replication Configuration](configuration-schema-isgr.md)
* [Using External Javascript Functions](configuration-javascript-functions.md)
* [Configuration Environment Variables](configuration-environment-variables.md)

## Security

Implement comprehensive security measures to protect your data and control access to Sync Gateway.

* [Secure Sync Gateway Access](secure-sgw-access.md)
* [User Authentication](authentication-users.md)
* [TLS Certificate Authentication](authentication-certs.md)
* [Audit Logging](audit-logging.md)

## Access Control

Configure fine-grained access control with users, roles, channels, and sync functions.

* [Access Control Concepts](access-control-concepts.md)
* [Sync Function](sync-function.md)
* [How to](#access-contrlol-how.adoc)
* [Auto-Purge on Channel Access Revocation](auto-purge-channel-access-revocation.md)

## REST API

Interact with Sync Gateway programmatically using comprehensive REST API interfaces.

* [Secure API Access](rest-api-access.md)
* [Admin REST API](rest-api-admin.md)
* [Metrics REST API](rest-api-metrics.md)
* [Public REST API](rest-api.md)
* [RBAC Role — Endpoint Cross-reference](rest-api-access-rbac-roles.md)

## Sync

Synchronize data between Sync Gateway and your applications, servers, and other Sync Gateway instances.

* [Sync with Couchbase Server](sync-with-couchbase-server.md)
* [Sync with Couchbase Lite](sync-using-app.md)
* [inter-syncgateway-overview.adoc](#inter-syncgateway-overview.adoc)
* [Delta Sync](delta-sync.md)
* [Import Processing](import-processing.md)

## Manage

Perform administrative and operational tasks to maintain and monitor Sync Gateway.

* [Revisions](revisions.md)
* [Tombstones](managing-tombstones.md)
* [Resync](resync.md)
* [View Statistics and Metrics](stats-monitoring.md)
* [Take Database Offline/Online](database-offline.md)
* [Logging](logging.md)

## Deploy

Deploy Sync Gateway in production environments with scalability and reliability considerations.

* [Using the Command Line](command-line-options.md)
* [Load Balancer](load-balancer.md)
* [Webhooks](webhooks.md)
* [Integrate Prometheus](stats-prometheus.md)
* [Indexes versus Views](indexing.md)
* [Deploying a Sync Gateway Cluster](deploy-cluster-to-kubernetes.md)

## Server Compatibility

Understand Sync Gateway compatibility with Couchbase Server features and services.

* [Buckets](server-compatibility-buckets.md)
* [Collections](server-compatibility-collections.md)
* [Eventing](server-compatibility-eventing.md)
* [Transactions](server-compatibility-transactions.md)
* [XDCR](server-compatibility-xdcr.md)
* [Backup and Restore](server-compatibility-backups.md)