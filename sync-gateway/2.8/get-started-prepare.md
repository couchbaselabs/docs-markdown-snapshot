---
title: Prepare to Install Sync Gateway
description: Prerequisites for installing <em>Sync Gateway</em>; to synchronize
  your data from cloud to edge.
editUrl: https://github.com/couchbase/docs-sync-gateway/edit/release/2.8/modules/ROOT/pages/get-started-prepare.adoc
pubDate: 2026-03-25T08:25:24.097Z
link: xref:2.8@sync-gateway::get-started-prepare.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/sync-gateway/2.8/get-started-prepare.html)

# Prepare to Install Sync Gateway

> Prerequisites for installing _Sync Gateway_; to synchronize your data from cloud to edge.  
> This is **Step 2** in the _Start Here!_ topic group. It introduces the prerequisites for the installation of _Sync Gateway_

Related _Start Here!_ topics: [Introduction](../current/introduction.md) | [Install](#sync-gateway::get-started-install.adoc) | [Verify](#sync-gateway::get-started-verify-install.adoc)

## [](#introduction)Introduction

Steps in Getting Started

[Introduction](../current/introduction.md)| **Prepare**| [Install](#sync-gateway::get-started-install.adoc)| [Verify](#sync-gateway::get-started-verify-install.adoc)

In this Getting Started topic we will discuss the prerequisites you need to have in place before you begin installing the Sync Gateway package.

On completion of this page you should:

* Know whether your set-up meets the [Minimum Requirements](#lbl-req-minim) and [Compatibility Requirements](#lbl-req-compat) for running Sync Gateway
* Know how to install and or [Configure Server for Sync Gateway](#configure-server)
* Have a working Couchbase Server deployment configured for Sync Gateway, including an RBAC user, ready for Sync Gateway’s use
* Have appropriate network credentials and [Network Access](#lbl-set-netw-access)

Your next step will be covered in [Install](#sync-gateway::get-started-install.adoc)

## [](#lbl-req-minim)Couchbase Requirements

Before you can usefully use Sync Gateway, you will need an operational Couchbase Server installation. You should ensure that you are using compatible versions of Couchbase Server and Sync Gateway — see: [Compatibility Requirements](#lbl-req-compat).

> [!TIP]
> You can get Couchbase Server from our [Downloads](https://www.couchbase.com/downloads/?family=mobile) page

You will then need to configure Couchbase Server by adding a Bucket and an RBAC User for Sync Gateway — see: [Configure Server for Sync Gateway](#configure-server).

> [!NOTE]
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

> [!NOTE]
> Users of Couchbase Server 6.0 should ensure they have addressed the known issue ([MB-41255](https://issues.couchbase.com/browse/MB-41255)) by upgrading to one of the recommended Couchbase Server versions (6.0.5, 6.5.2, or 6.6.1).
> 
> The known issue can cause re-balance failures and/or failed replica writes of deleted or expired documents that use Xattrs.
> 
> This impacts Sync Gateway deployments running with shared bucket access enabled, which use Xattrs for metadata storage.

__Table 2\. Sync Gateway/Couchbase Server Compatibility Matrix__
| Sync Gateway ↓                                                                 | Couchbase Server →                               |                                                  |                                                  |     |     |         |   |
| ------------------------------------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | --- | --- | ------- | - |
| 4.0\[[1](#%5Ffootnotedef%5F1 "View footnote.")\]                               | 4.1\[[1](#%5Ffootnotedef%5F1 "View footnote.")\] | 4.5\[[1](#%5Ffootnotedef%5F1 "View footnote.")\] | 4.6\[[1](#%5Ffootnotedef%5F1 "View footnote.")\] | 5.0 | 5.1 | 5.5-7.1 |   |
| 1.3\[[2](#%5Ffootnotedef%5F2 "View footnote.")\] feed\_type: "DCP"             | ✖                                                | ✖                                                | ✖                                                | ✖   | ✔   | ✔       | ✔ |
| 1.4\[[2](#%5Ffootnotedef%5F2 "View footnote.")\] feed\_type: "DCP"             | ✖                                                | ✖                                                | ✖                                                | ✖   | ✔   | ✔       | ✔ |
| 1.5\[[3](#%5Ffootnotedef%5F3 "View footnote.")\] shared\_bucket\_access: false | ✔                                                | ✔                                                | ✔                                                | ✔   | ✔   | ✔       | ✔ |
| 1.5\[[3](#%5Ffootnotedef%5F3 "View footnote.")\] shared\_bucket\_access: true  | ✖                                                | ✖                                                | ✖                                                | ✖   | ✔   | ✔       | ✔ |
| 2.0 shared\_bucket\_access: false                                              | ✔                                                | ✔                                                | ✔                                                | ✔   | ✔   | ✔       | ✔ |
| 2.0 shared\_bucket\_access: true                                               | ✖                                                | ✖                                                | ✖                                                | ✖   | ✔   | ✔       | ✔ |
| 2.1 shared\_bucket\_access: false use\_views: true                             | ✔                                                | ✔                                                | ✔                                                | ✔   | ✔   | ✔       | ✔ |
| 2.1 shared\_bucket\_access: true                                               | ✖                                                | ✖                                                | ✖                                                | ✖   | ✔   | ✔       | ✔ |
| 2.1 use\_views: false                                                          | ✖                                                | ✖                                                | ✖                                                | ✖   | ✖   | ✖       | ✔ |
| 2.5-2.8 shared\_bucket\_access: false use\_views: true                         | ✔                                                | ✔                                                | ✔                                                | ✔   | ✔   | ✔       | ✔ |
| 2.5-2.8 shared\_bucket\_access: true                                           | ✖                                                | ✖                                                | ✖                                                | ✖   | ✔   | ✔       | ✔ |
| 2.5-2.8 use\_views: false                                                      | ✖                                                | ✖                                                | ✖                                                | ✖   | ✖   | ✖       | ✔ |

> [!NOTE]
> Couchbase Server Bucket Types
> 
> Use only **Couchbase** bucket types in _Couchbase for Mobile and Edge_. We do not support the use of Couchbase Server’s **Ephemeral** or **Memcached** bucket types — for more on bucket types see: Couchbase Server [bucket types](../../server/current/learn/buckets-memory-and-storage/buckets.md).

## [](#compatibility-with-couchbase-lite)Compatibility with Couchbase Lite

The table below summarizes the compatible versions of Couchbase Lite with Sync Gateway.

> [!IMPORTANT]
> The beta version of Couchbase Lite 4.0 is only compatible with Sync Gateway 4.0

__Table 3\. Sync Gateway and Couchbase Lite Compatibility Matrix__
| Sync Gateway Versions ↓                                                                                         | Couchbase Lite →     |                      |                      |                      |                      |                      |                      |                      |
| --------------------------------------------------------------------------------------------------------------- | -------------------- | -------------------- | -------------------- | -------------------- | -------------------- | -------------------- | -------------------- | -------------------- |
| 1.4 **\[[4](#%5Ffootnotedef%5F4 "View footnote.")\]**                                                           | 2.0                  | 2.1                  | 2.5 - 2.8            | 3.0.0                | 3.1.0                | 3.2.0                | 4.0.0                |                      |
| 1.4 **\[[2](#%5Ffootnotedef%5F2 "View footnote.")\]** and 1.5 **\[[3](#%5Ffootnotedef%5F3 "View footnote.")\]** | ![yes](ROOT:yes.png) | ![no](ROOT:no.png)   | ![no](ROOT:no.png)   | ![no](ROOT:no.png)   | ![no](ROOT:no.png)   | ![no](ROOT:no.png)   | ![no](ROOT:no.png)   | ![no](ROOT:no.png)   |
| 2.0 and 2.1                                                                                                     | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![no](ROOT:no.png)   |
| 2.5 to 2.8with delta sync disabled                                                                              | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![no](ROOT:no.png)   |
| 2.5 to 2.8with delta sync enabled                                                                               | ![no](ROOT:no.png)   | ![no](ROOT:no.png)   | ![no](ROOT:no.png)   | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![no](ROOT:no.png)   |
| 3.0.0                                                                                                           | ![no](ROOT:no.png)   | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![no](ROOT:no.png)   |
| 3.1.0                                                                                                           | ![no](ROOT:no.png)   | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![no](ROOT:no.png)   |
| 3.2.0                                                                                                           | ![no](ROOT:no.png)   | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![no](ROOT:no.png)   |
| 4.0.0                                                                                                           | ![no](ROOT:no.png)   | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) | ![yes](ROOT:yes.png) |

## [](#supported-operating-systems)Supported Operating Systems

__Table 4\. Supported Operating Systems for Development, Testing, and Production__
| Operating System                | Supported Versions                                          |
| ------------------------------- | ----------------------------------------------------------- |
| Red Hat Enterprise Linux (RHEL) | 7.x and 8.x                                                 |
| CentOS                          | 7.x and 8.x                                                 |
| Ubuntu                          | 16.04 LTS and 18.04                                         |
| Debian                          | 8.x and 9.x                                                 |
| Windows Server                  | 2012 (64-bit) DEPRECATED at Sync Gateway 2.8+ 2016 (64-bit) |

__Table 5\. Supported Operating Systems for Development and Testing Only__
| Operating System | Supported Versions            |
| ---------------- | ----------------------------- |
| macOS            | 10.15(Catalina)10.14 (Mojave) |
| Windows Desktop  | 2010                          |

__Table 6\. Supported Cloud Environments for Development, Testing, and Production__
| Platform                  | Operating System | Supported Versions |
| ------------------------- | ---------------- | ------------------ |
| AWS                       | Amazon Linux AMI | 2017.092018.03     |
| Azure                     | Ubuntu           | 16.04              |
| Google Cloud              | Ubuntu           | 16.04              |
| Docker (Docker Hub)       | CentOS           | 7                  |
| OpenShift (RedHat Portal) | RHEL             | 7.2                |

## [](#configure-server)Configure Server for Sync Gateway

### [](#lbl-create-bucket)STEP 1 — Create a Bucket

We will use this bucket to test the deployment of Sync Gateway, later in the Getting Started section.

1. Login to Couchbase Server’s Admin Console

  1. Go to `http://localhost:8091`
  2. Enter your administrator credentials
2. Within the Admin Console’s toolbar,

  1. Select the **Buckets** tab
  2. **Add Bucket** to continue  
  ![cb create bucket](_images/cb-create-bucket.png)
  3. In the pop-up window, enter **get-started-bucket** for the **name** and click **Add Bucket**. You can leave the other options to their defaults.  
  > [!NOTE]  
  > Couchbase Server Bucket Types  
  >  
  > Use only **Couchbase** bucket types in _Couchbase for Mobile and Edge_. We do not support the use of Couchbase Server’s **Ephemeral** or **Memcached** bucket types — for more on bucket types see: Couchbase Server [bucket types](../../server/current/learn/buckets-memory-and-storage/buckets.md).  
![cb create bucket popup](_images/cb-create-bucket-popup.png)

### [](#lbl-create-rbac-user)STEP 2 — Create RBAC User

To connect to Couchbase Server, you must create an RBAC user. These user credentials are used in a later section to start Sync Gateway.

1. Open the **Security** tab and click the **Add User** button.  
![create user](_images/create-user.png)
2. Create the RBAC user with appropriate access roles.  
The steps to do this are shown in [Example 1](#rbac-roles). Note that they differ, depending on your Couchbase Server version.  
Example 1\. Select RBAC roles

  * Couchbase Server 6.6+ (Enterprise)
  * Couchbase Server 5.5 - 6.x
  * Couchbase Server 5.1  
> [!IMPORTANT]  
> This content relates only to [ENTERPRISE EDITION](https://www.couchbase.com/products/editions)

  1. In the pop-up window, provide

    * A Username (`sync_gateway`)
    * A Password (`password`).
  2. Assign the _Sync Gateway_ role to the user  
  [Sync Gateway RBAC Role Description](../../server/current/learn/security/roles.md#sync-gateway)  
  ![user settings 6 6](_images/user-settings-6-6.png)  
  > [!NOTE]  
  > Users are encouraged to move away from using the _Application Access_ and _Read-Only Admin_ roles for this purpose.

  1. In the pop-up window, provide:

    * A Username (`sync_gateway`)
    * A Password (`password`).
  2. Assign these RBAC roles to the user(as shown on the image below):

    * Application Access
    * Read Only Admin  
      ![user settings 5 5](_images/user-settings-5-5.png)

  1. In the pop-up window, provide:

    * A Username (`sync_gateway`)
    * A Password\* (`password`).
  2. Assign these RBAC roles to the user:

    * Bucket Full Access
    * Read Only Admin  
![user settings](_images/user-settings.png)

### [](#lbl-set-netw-access)STEP 3 — Set-up Network Access

When installing Couchbase Server on the cloud, ensure that network permissions (or firewall settings) allow incoming connections to Couchbase Server ports.

For mobile deployment on premise or in the cloud (for example, AWS or Red Hat) open the following ports on the host to enable Couchbase Server to operate correctly:

* Unencrypted: 8091-8093, 11210
* Encrypted: 18091-18093, 11207

Check that any firewall configuration allows communication on the specified ports.

If this is not done, the Couchbase Server node can experience difficulty joining a cluster.

You can refer to the [Couchbase Server Ports](../../server/current/install/install-ports.md) guide to see the full list of available ports and their associated services.

## [](#related-content)Related Content

###### [](#)

Getting Started

* [Prepare](#sync-gateway::get-started-prepare.adoc)
* [Install](#sync-gateway::get-started-install.adoc)
* [Verify](#sync-gateway::get-started-verify-install.adoc)

###### [](#-2)

Product Information

* [Release Notes](../current/product-notes/release-notes.md)
* [Compatibility Matrix](#sync-gateway::compatibility.adoc)
* [Supported OS](#sync-gateway::pn-supported-os.adoc)

###### [](#-3)

Community

* [Forum](https://forums.couchbase.com/c/mobile/14) **|** [Blog](https://blog.couchbase.com/) **|** [Tutorials](https://docs.couchbase.com/tutorials/index.html)

---

[1](#%5Ffootnoteref%5F1). This Couchbase Server version is End of Support 

[2](#%5Ffootnoteref%5F2). This Sync Gateway version is End of Support 

[3](#%5Ffootnoteref%5F3). This Sync Gateway version is End of Life 

[4](#%5Ffootnoteref%5F4). This Couchbase Lite version is End of Support