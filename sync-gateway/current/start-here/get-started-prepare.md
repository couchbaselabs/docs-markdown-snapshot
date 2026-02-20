---
title: Prepare to Install Sync Gateway
description: Prerequisites for installing <em>Sync Gateway</em>; to synchronize
  your data from cloud to edge.
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/4.0/modules/start-here/pages/get-started-prepare.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:sync-gateway:start-here:get-started-prepare.adoc[]
---

[View original HTML](/sync-gateway/current/start-here/get-started-prepare.html)

# Prepare to Install Sync Gateway

> Prerequisites for installing _Sync Gateway_; to synchronize your data from cloud to edge.  
> This is **Step 2** in the _Start Here!_ topic group. It introduces the prerequisites for the installation of _Sync Gateway_

Related _Start Here!_ topics: [Introduction](../introduction.md) | [Install](get-started-install.md) | [Verify](get-started-verify-install.md)

Steps in Getting Started

[Introduction](../introduction.md)| [Prepare](get-started-prepare.md)| [Install](get-started-install.md)| [Verify](get-started-verify-install.md)

## [](#what-you-need)What You Need

Here’s what you need in order to install Sync Gateway:

* To know whether your set-up meets the [Minimum Requirements](#lbl-req-minim) and [Compatibility Requirements](#lbl-req-compat) for running Sync Gateway
* To have access to a working Couchbase Server deployment configured for Sync Gateway, or alternatively, to know how to [Deploy Couchbase Server](../../../server/current/install/get-started.md)
* To [Configure Server for Sync Gateway](#configure-server), including creating an appropriate set of RBAC users, ready for use in Sync Gateway and in the REST API
* Have appropriate network credentials and [Network Access](#lbl-set-netw-access)

Once you have all that covered …​ go [Install](get-started-install.md) Sync Gateway.

## [](#lbl-req-minim)Couchbase Server Requirements

To use Sync Gateway you need an operational Couchbase Server installation. Ensure that you use compatible versions of Couchbase Server and Sync Gateway — see: [Compatibility Requirements](#lbl-req-compat).

> [!TIP]
> You can get Couchbase Server from our [Downloads](https://www.couchbase.com/downloads/?family=mobile) page

You will then need to configure Couchbase Server by adding a Bucket and an RBAC User for Sync Gateway — see: [Configure Server for Sync Gateway](#configure-server).

> [!IMPORTANT]
> Users of Couchbase Server 6.0 should ensure they have addressed the known issue ([MB-41255](https://issues.couchbase.com/browse/MB-41255)) by upgrading to one of the recommended Couchbase Server versions (6.0.5, 6.5.2, or 6.6.1).
> 
> The known issue can cause re-balance failures and/or failed replica writes of deleted or expired documents that use Xattrs.
> 
> This impacts Sync Gateway deployments running with shared bucket access enabled, which use Xattrs for metadata storage.

## [](#network-port-requirements)Network Port Requirements

Sync Gateway uses specific ports for communication with the outside world, mostly Couchbase Lite databases replicating to and from Sync Gateway — see [Table 1](#network-ports) for details.

__Table 1\. Sync Gateway Network Port Requirements__
| Port | Description                                                                                                                                                                                                                                                                                                                                                                                 |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 4984 | Public port. External HTTP port used for replication with Couchbase Lite databases and other applications accessing the REST API on the Internet. The Public REST API is used for client replication. The default port for the Public REST API is 4984.                                                                                                                                     |
| 4985 | Admin port. Internal HTTP port for unrestricted access to the database and to run administrative tasks. The Admin REST API is used to administer user accounts and roles. It can also be used to look at the contents of databases in superuser mode. The default port for the Admin REST API is 4985\. By default, the Admin REST API is reachable only from localhost for safety reasons. |
| 4986 | Metrics port. By default 4986 is the internal HTTP port designated for providing access to Sync Gateway’s Metrics REST API. Like the admin port, it is bound to 127.0.0.1 by default. The Metrics REST API returns Sync Gateway metrics, in JSON and-or Prometheus-compatible formats, for performance monitoring and-or diagnostic purposes,                                               |

## [](#couchbase-server-host-ports)Couchbase Server Host Ports

For mobile deployment on premise or in the cloud (for example, AWS or Red Hat) open the following ports on the host to enable Couchbase Server to operate correctly:

* Unencrypted: 8091-8093, 11210
* Encrypted: 18091-18093, 11207

Check that any firewall configuration allows communication on the specified ports.

## [](#lbl-req-compat)Compatibility with Couchbase Server

> [!IMPORTANT]
> Users of Couchbase Server 6.0 should ensure they have addressed the known issue ([MB-41255](https://issues.couchbase.com/browse/MB-41255)) by upgrading to one of the recommended Couchbase Server versions (6.0.5, 6.5.2, or 6.6.1).
> 
> The known issue can cause re-balance failures and/or failed replica writes of deleted or expired documents that use Xattrs.
> 
> This impacts Sync Gateway deployments running with shared bucket access enabled, which use Xattrs for metadata storage.

__Table 2\. Sync Gateway/Couchbase Server Compatibility Matrix__
| Sync Gateway ↓ | Couchbase Server →                             |                            |                            |                            |                            |                            |                            |
| -------------- | ---------------------------------------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- |
| Version        | Scenario                                       | 8.0.0                      | 7.6.5                      | 7.6.4                      | 7.6                        | 7.2                        | 7.1                        |
| 4.0.0          |                                                | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![no](../_images/no.png)   | ![no](../_images/no.png)   |
| 4.0.0          | Bidirectional Active-Active XDCR               | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![no](../_images/no.png)   | ![no](../_images/no.png)   | ![no](../_images/no.png)   | ![no](../_images/no.png)   |
| 3.3.0          |                                                | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 3.2.0          |                                                | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 3.1.0          |                                                | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 3.0.3          |                                                | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 2.5-2.8        | shared\_bucket\_access: false use\_views: true | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 2.5-2.8        | shared\_bucket\_access: true                   | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 2.5-2.8        | use\_views: false                              | ![yes](../_images/yes.png) | ![no](../_images/no.png)   | ![no](../_images/no.png)   | ![no](../_images/no.png)   | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 2.1            | shared\_bucket\_access: false use\_views: true | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 2.1            | shared\_bucket\_access: true                   | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 2.1            | use\_views: false                              | ![yes](../_images/yes.png) | ![no](../_images/no.png)   | ![no](../_images/no.png)   | ![no](../_images/no.png)   | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 2.0            | shared\_bucket\_access: false                  | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |
| 2.0            | shared\_bucket\_access: true                   | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |

> [!WARNING]
> Starting from CBS 7.0, the `use_views` feature is deprecated.
> 
> * SGW 3.1 will only run with `use_views` with a default scope/collection configuration
> * You cannot run `use_views` with a defined scope/collection
> 
> Sync Gateway 4.0 requires CBS 7.6.1+. Active-Active XDCR requires CBS 7.6.5+. Sync Gateway 3.x does not support Active-Active XDCR.

> [!IMPORTANT]
> Couchbase Server Bucket Types
> 
> Use only **Couchbase** bucket types in _Couchbase Mobile_. We do not support the use of Couchbase Server’s **Ephemeral** or **Memcached** bucket types — for more on bucket types see: Couchbase Server [bucket types](../../../server/current/learn/buckets-memory-and-storage/buckets.md).

**Compatibility with Couchbase Server 5.0-7.0**

For Couchbase Server versions 5.0, 5.1, 5.5-6.0, and 6.5-7.0:

* Sync Gateway 4.0.0 is not compatible with these versions
* Sync Gateway 3.x and 2.x versions are fully compatible with these versions

## [](#compatibility-with-couchbase-lite)Compatibility with Couchbase Lite

The table below summarizes the compatible versions of Couchbase Lite with Sync Gateway.

__Table 3\. Sync Gateway and Couchbase Lite Compatibility Matrix__
| Sync Gateway Versions ↓                                                                                         | Couchbase Lite →           |                            |                            |                            |                            |                            |                            |                            |                            |
| --------------------------------------------------------------------------------------------------------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- | -------------------------- |
| 1.4 **\[[1](#%5Ffootnotedef%5F1 "View footnote.")\]**                                                           | 2.0                        | 2.1                        | 2.5 - 2.8                  | 3.0.0                      | 3.1.0                      | 3.2.0                      | 3.3.0                      | 4.0.0                      |                            |
| 1.4 **\[[2](#%5Ffootnotedef%5F2 "View footnote.")\]** and 1.5 **\[[3](#%5Ffootnotedef%5F3 "View footnote.")\]** | ![yes](../_images/yes.png) | ![no](../_images/no.png)   | ![no](../_images/no.png)   | ![no](../_images/no.png)   | ![no](../_images/no.png)   | ![no](../_images/no.png)   | ![no](../_images/no.png)   | ![no](../_images/no.png)   | ![no](../_images/no.png)   |
| 2.0 and 2.1                                                                                                     | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![no](../_images/no.png)   |
| 2.5 to 2.8with delta sync disabled                                                                              | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![no](../_images/no.png)   |
| 2.5 to 2.8with delta sync enabled                                                                               | ![no](../_images/no.png)   | ![no](../_images/no.png)   | ![no](../_images/no.png)   | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![no](../_images/no.png)   |
| 3.0.0                                                                                                           | ![no](../_images/no.png)   | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![no](../_images/no.png)   |
| 3.1.0                                                                                                           | ![no](../_images/no.png)   | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![no](../_images/no.png)   |
| 3.2.0                                                                                                           | ![no](../_images/no.png)   | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![no](../_images/no.png)   |
| 3.3.0                                                                                                           | ![no](../_images/no.png)   | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![no](../_images/no.png)   |
| 4.0.0                                                                                                           | ![no](../_images/no.png)   | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) | ![yes](../_images/yes.png) |

> [!WARNING]
> **Couchbase Lite 4.0 requires Sync Gateway 4.0.**
> 
> Couchbase Lite 4.0 is only compatible with Sync Gateway 4.0\. Connecting Couchbase Lite 4.0 to Sync Gateway versions before 4.0 is not supported due to version vector architecture changes. However, Sync Gateway 4.0 is compatible with all supported Couchbase Lite versions (2.0+), allowing customers to upgrade Sync Gateway first.

## [](#supported-operating-systems)Supported Operating Systems

__Table 4\. Supported Operating Systems for Development, Testing, and Production__
| Operating System                | Supported Versions           |
| ------------------------------- | ---------------------------- |
| Red Hat Enterprise Linux (RHEL) | 10.x                         |
| 9.x                             |                              |
| Alma Linux                      | 9.x                          |
| Rocky Linux                     | 9.x                          |
| Ubuntu                          | 24.04 LTS ARM, 24.04 LTS x86 |
| 22.04 LTS ARM, 22.04 LTS x86    |                              |
| Debian                          | 13.x                         |
| 12.x                            |                              |
| 11.x                            |                              |
| Windows Server                  | 2022                         |

__Table 5\. Supported Operating Systems for Development and Testing Only__
| Operating System    | Supported Versions  |
| ------------------- | ------------------- |
| macOS               | 15 M1 ARM64, 15 x86 |
| 14 M1 ARM64, 14 x86 |                     |
| Windows Desktop     | 11                  |
| 10                  |                     |

__Table 6\. Supported Cloud Environments for Development, Testing, and Production__
| Platform                  | Operating System     | Supported Versions                         |
| ------------------------- | -------------------- | ------------------------------------------ |
| AWS                       | Amazon Linux         | 2023 LTS (ARM, x86)                        |
| Ubuntu                    | 24.04 LTS (ARM, x86) |                                            |
| Azure                     | Ubuntu               | 24.04 LTS (ARM, x86), 22.04 LTS (ARM, x86) |
| Google Cloud              | Ubuntu               | 24.04 LTS (ARM, x86) 22.04 LTS (ARM, x86)  |
| OpenShift (RedHat Portal) | RHEL                 | 10                                         |
| RHEL                      | 9                    |                                            |
| Ubuntu                    |                      | 24.04 LTS, 22.04 LTS                       |

## [](#cluster-configuration-for-sync-gateway)Cluster Configuration for Sync Gateway

Create a new cluster on a fresh Couchbase Server installation.

1. Access the Admin Console at `http://localhost:8091`
2. Select **Setup New Cluster**
3. Fill in the details for the new cluster on the `New Cluster` screen:
4. Then press **Next: Accept Terms**
5. On the `Terms and Conditions` screen, accept the terms and conditions, then Select **Configure Disk, Memory, Services** to configure the cluster.
6. Verify that you have selected `Data`, `Query`, and `Index` before selecting **Save & Finish**

## [](#configure-server)Configure Server for Sync Gateway

### [](#step-1create-a-bucket)Step 1 — Create a Bucket

Use this bucket to test the deployment of Sync Gateway, later in the Getting Started section.

1. Login to Couchbase Server’s Admin Console

  1. Go to `http://localhost:8091`
  2. Enter your administrator credentials.
2. Within the Admin Console’s toolbar,

  1. Select the **Buckets** tab
  2. Select **Add Bucket** to continue
  3. In the pop-up window, enter **get-started-bucket** for the **name** and select **Add Bucket**. You can leave the other options to their defaults.  
  > [!IMPORTANT]  
  > Couchbase Server Bucket Types  
  >  
  > Use only **Couchbase** bucket types in _Couchbase Mobile_. We do not support the use of Couchbase Server’s **Ephemeral** or **Memcached** bucket types — for more on bucket types see: Couchbase Server [bucket types](../../../server/current/learn/buckets-memory-and-storage/buckets.md).

### [](#step-2create-rbac-user)Step 2 — Create RBAC User

You’ll need to create at least one RBAC user in Couchbase Server as sync gateway requires RBAC user credentials to authenticate and authorize access not only to Couchbase Server buckets, but also to its Admin and Metrics API. If you plan to use these API then create at least one user for each of:

* Couchbase Server Access  
Add an RBAC user that Sync Gateway uses to authenticate and authorize access to Couchbase Server. Use the _sync\_gateway_ role.
* Admin API  
Add an RBAC user that administrators can use to authenticate and authorize access to the sync gateway Admin REST API Use the _Full Admin_ role.
* Metrics API  
Add an RBAC user that devops can use to authenticate and authorize access to the sync gateway Metrics REST API Use the _Read-Only Admin_ or _Application Access_ roles.

Enterprise edition users can exert a finer-grained control using additional roles appropriate to the capabilities required for the specific user.

> [!NOTE]
> For more on creating Couchbase Server users see: [Server — Manage Users and Roles](../../../server/current/manage/manage-security/manage-users-and-roles.md).

### [](#lbl-set-netw-access)Step 3 — Set-up Network Access

When installing Couchbase Server on the cloud, ensure that network permissions (or firewall settings) allow incoming connections to Couchbase Server ports.

For mobile deployment on premise or in the cloud (for example, AWS or Red Hat) open the following ports on the host to enable Couchbase Server to operate correctly:

* Unencrypted: 8091-8093, 11210
* Encrypted: 18091-18093, 11207

Check that any firewall configuration allows communication on the specified ports.

If this is not done, the Couchbase Server node can experience difficulty joining a cluster.

You can refer to the [Couchbase Server Ports](../../../server/current/install/install-ports.md) guide to see the full list of available ports and their associated services.

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

* [Release Notes](../product-notes/release-notes.md)
* [Compatibility Matrix](../product-notes/compatibility.md)
* [Supported OS](../product-notes/supported-environments.md)

###### [](#-4)

Community

[Mobile Forum](https://forums.couchbase.com/c/mobile/14) | [Blog](https://blog.couchbase.com/) | [Blog (Mobile)](https://blog.couchbase.com/category/couchbase-mobile/?ref=blog-menu) | [Tutorials](https://docs.couchbase.com/tutorials/)

---

[1](#%5Ffootnoteref%5F1). This Couchbase Lite version is End of Support 

[2](#%5Ffootnoteref%5F2). This Sync Gateway version is End of Support 

[3](#%5Ffootnoteref%5F3). This Sync Gateway version is End of Life