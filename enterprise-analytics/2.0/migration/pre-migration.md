---
title: Pre-Migration Planning &amp; Preparation
description: This section provides a comprehensive checklist and best practices
  to help you prepare for migration from Couchbase Server Analytics Service or
  Capella Operational Analytics Service to Capella Analytics or Enterprise
  Analytics.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/migration/pages/pre-migration.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:2.0@enterprise-analytics:migration:pre-migration.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.0/migration/pre-migration.html)

# Pre-Migration Planning &amp; Preparation

> This section provides a comprehensive checklist and best practices to help you prepare for migration from Couchbase Server Analytics Service or Capella Operational Analytics Service to Capella Analytics or Enterprise Analytics. 

Before you migrate, make sure that you do the following:

* Discovery & Assessment: Understand the current Couchbase environment, including cluster topology, data models, application dependencies (SDKs used), and workload characteristics.
* Capacity Planning: Determine the resource requirements for the new Couchbase cluster based on anticipated growth and performance needs.
* Environment Setup: Provision and configure the new Couchbase cluster, ensuring all necessary hardware and software prerequisites are met.

## [](#prerequisites)Prerequisites

* You must have an existing Couchbase Capella account with an Analytics Service deployed on a Capella cluster, OR an existing self-managed Couchbase Server environment. For more information, see [Analyze the Source System](#analyzesourcesystem).
* You must have an existing Couchbase Capella account (for Capella Analytics cluster deployment), OR compatible server infrastructure for Enterprise Analytics on-premise deployments, OR an account with your the cloud provider for self-managed Enterprise Analytics deployments. For more information, see [Target System Configuration](#targetsystemconfiguration).

## [](#analyzesourcesystem)Analyze the Source System

You must complete a detailed analysis of the source system for migration. This encompasses a comprehensive understanding of everything within the current database system that you need to consider for the move.

### [](#capella-operational-analytics-service)Capella Operational Analytics Service:

* Configuration
* Data Sources
* Database Inventory
* Integrations
* Security and Compliance requirements
* Performance Requirements

* Number of Analytics Nodes and their configuration
* Preferred cloud service provider

* Capella operational data
* External sources such as Amazon S3
* Additional Remote Links

* Scopes and Collection (hierarchy)
* Indexes

* Applications
* PySpark/Spark Connectors
* BI tools (power BI, Tableau)

A key implication of this migration is that applications/connectors using the Couchbase SDK need to upgrade to the new Enterprise Analytics SDK which is purpose built for Enterprise Analytics and Capella Analytics. For more information, see [SDK Migration](migration-process.md#sdk-migration).

* Role-Based Access Control applied to Capella Operational Analytics Service For more information, see [Eventing Role-Based Access Control (RBAC)](../manage/manage-security/rbac-overview.md).
* For information about Capella Analytics and Enterprise Analytics, [Assign Roles for UI Access](../../../analytics/admin/auth/auth-ui.md) and [Role-Based Access Control (RBAC)](../../current/reference/rbac.md).

1. Performance requirement expected from Capella Analytics (for example, Query Latency, Concurrent users etc.)

### [](#couchbase-server-analytics-service)Couchbase Server Analytics Service:

* Configuration
* Data Sources
* Database Inventory
* Integrations
* Security and Compliance requirements
* Performance Requirements

* Operating System
* Object Storage
* Virtualization Platform details

  * Hypervisor
  * Guest operating system
  * VM configuration (VCPUs, RAM, SSD)
* Current server configuration

* Couchbase Server data
* Remote Links
* External sources such as Amazon S3

* Scopes and Collection (hierarchy)
* Indexes

* Applications
* REST APIs
* PySpark/Spark Connectors
* BI tools (power BI, Tableau)

If you use applications or connectors using the Couchbase SDK, you need to upgrade to the new Enterprise Analytics SDK. For more information, see [Migration](migration-process.md).

* Role-based Access Control applied to Capella Operational Analytics Service For more information, see [Eventing Role-Based Access Control (RBAC)](../manage/manage-security/rbac-overview.md).
* For information about Capella Analytics and Enterprise Analytics, [Assign Roles for UI Access](../../../analytics/admin/auth/auth-ui.md) and [Role-Based Access Control (RBAC)](../../current/reference/rbac.md).

1. Expected Performance from Enterprise Analytics (e.g. Query Latency, Concurrent users etc.)

## [](#targetsystemconfiguration)Target System Configuration

Before migrating, make sure that the target system is provisioned and configured to meet your performance, scalability, and security requirements.

Review hardware, software, and network prerequisites to guarantee a smooth transition and optimal operation post-migration.

### [](#capella-analytics)Capella Analytics

You can configure Capella Analytics with the same number of analytics nodes and similar specifications (or a config that translates to similar capacity) as the existing Couchbase Operational Analytics Service and Couchbase Server Analytics Service.

> [!NOTE]
> You must perform a sanity check post-migration.

For more information about Capella Analytics cluster creation, see [Create a Cluster](../../../analytics/admin/prepare-project.md).

#### [](#connection-management)Connection Management:

The following table summarizes client connection options for Enterprise Analytics clusters, node addition steps, and the resulting impact on SDK connectivity.

| Option                                                                           | SDK Impact                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| -------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Using Load Balancer (Couchbase recommended approach for production environments) | If you bootstrap an HTTP(S)-based connection with load balancers, it simplifies client connectivity by directing all requests to a well-known load-balanced endpoint. When a client connects, it sends an HTTP(S) request to this endpoint which is managed by a load balancer distributing traffic across multiple cluster nodes. In this setup, the SDK client sends all requests to load balancer’s endpoint.                                                                                                                                                                                                             |
| Using DNS/HTTP(S) (without Load Balancer)                                        | In HTTP(S)-based connection bootstrapping without load balancers, the SDK client relies on keeping DNS records updated to discover cluster nodes dynamically. When a client connects, it queries the DNS entries associated with the cluster’s hostname and returns IP addresses with which you can contact the cluster nodes. SDK relies on DNS A records and randomly chooses a node to send its requests. If a failure or timeout occurs, the SDK may attempt to connect to another available DNS A record. After a user-configurable number of retries, the SDK throws an exception if it cannot establish a connection. |

#### [](#enterprise-analytics)Enterprise Analytics

Couchbase recommends that you use load balancers for the Enterprise Analytics clusters to make it easier to connect clients and SDKs. SDKs connect to Enterprise Analytics clusters using an HTTP(S) endpoint, similar to how you would use `curl`.

For information about Linux installation, see [Install Enterprise Analytics on Linux](../install/linux-installation.md).

#### [](#operating-systems)Operating Systems

Enterprise Analytics supports deployment on a range of operating systems to provide flexibility and compatibility with your existing infrastructure.

For information about operating systems, see [Supported Operating Systems](../install/supported-platform.md)

#### [](#server-requirement)Server Requirement

* You can configure Enterprise Analytics with the similar server specifications as the existing Couchbase Server Analytics Service. You should be able to achieve the desired performance SLAs. However, you should perform a sanity validation post-migration.
* Although resource requirements depend on the size and resource demands of the customer’s Couchbase deployment, there are some minimum and recommended specifications.

For more information, see [System Requirements](../install/system-requirements.md)

#### [](#object-storage)Object Storage

Enterprise Analytics on-prem supports the NetApp StorageGRID on-prem storage, and Enterprise Analytics self managed supports Amazon S3 compatible object storage.

Enterprise Analytics requires S3-based object storage. Supported options include Amazon S3 and S3-compatible object stores certified against NetApp StorageGRID.

For more information, see [Setting Up With Object Storage](../manage/manage-nodes/object-storage.md).

#### [](#virtualization-platform)Virtualization Platform

You can deploy Enterprise Analytics on a variety of virtualization platforms to meet your infrastructure and scalability needs.

1. Hypervisor Support: Enterprise Analytics is compatible with leading hypervisors such as VMware vSphere and Kernel-based Virtual Machine (KVM), allowing flexible deployment options based on your infrastructure preferences.
2. Virtual Machine Requirements: For optimal performance of Enterprise Analytics, configure your virtual machines with resources comparable to your existing Couchbase Server Analytics Service. At a minimum, Couchbase recommends the following specifications:

  1. 4 vCPUs
  2. 32 GB RAM
  3. 950 GB SSD storage

Adjust these requirements based on your workload and anticipated growth. For production environments, consider allocating additional resources to meet higher performance and scalability needs.

1. Supported Guest Operating Systems:

Enterprise Analytics supports deployment on Red Hat Enterprise Linux (RHEL), Ubuntu, and Debian guest operating systems. Make sure that you use supported versions as listed in the official documentation. For more information, see [Supported Operating Systems](../install/supported-platform.md).