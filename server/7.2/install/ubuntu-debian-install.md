---
title: Install Couchbase Server on Ubuntu and Debian
description: Couchbase Server can be installed on Ubuntu Linux and Debian Linux
  for production and development use-cases. Root and non-root installations are
  supported.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/install/pages/ubuntu-debian-install.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:install:ubuntu-debian-install.adoc[]
---

[View original HTML](/server/7.2/install/ubuntu-debian-install.html)

# Install Couchbase Server on Ubuntu and Debian

> Couchbase Server can be installed on Ubuntu Linux and Debian Linux for production and development use-cases. Root and non-root installations are supported. 

Use the instructions on this page to install Couchbase Server on Ubuntu and Debian platforms using Couchbase-provided _deb_ packages. The instructions support both Enterprise and Community [editions](https://www.couchbase.com/products/editions).

If you’re upgrading an existing installation of Couchbase Server, refer to [Upgrading Couchbase Server](upgrade.md).

## [](#before-you-install)Before You Install

Couchbase Server works out-of-the-box with most OS configurations. However, the procedures on this page assume the following:

* Your system meets the [minimum requirements](pre-install.md) and that your operating system version is [supported](install-platforms.md).
* You’re working from a clean system and that you’ve [uninstalled](install-uninstalling.md) any previous versions of Couchbase Server.  
If you’re upgrading an existing installation of Couchbase Server, refer to [Upgrading Couchbase Server](upgrade.md).

For production deployments, make sure to follow the [deployment guidelines](install-production-deployment.md) so that your systems and environment are properly sized and configured before installation.

## [](#basic-installation)Basic Installation

You must be logged in as root (superuser) or use `sudo` to run the installation commands.

### [](#install-using-apt)Install Using Apt

The Advanced Package Tool (`apt`) provides the simplest and most comprehensive way to install Couchbase Server on Ubuntu and Debian platforms. This method involves downloading and installing a small meta package from Couchbase, which `apt` can then use to automatically download and install Couchbase Server and all of its dependencies.

1. Download the meta package.  
```console  
curl -O https://packages.couchbase.com/releases/couchbase-release/couchbase-release-1.0-noarch.deb  
```
2. Install the meta package.  
```console  
sudo apt install ./couchbase-release-1.0-noarch.deb  
```  
The meta package installs the necessary information for `apt` to be able to retrieve all of the necessary Couchbase Server installation packages and dependencies.
3. Reload the local package database.  
```console  
sudo apt-get update  
```
4. Install Couchbase Server.

  * Enterprise
  * Community  
To install the latest release  
```console  
sudo apt-get install couchbase-server  
```  
To install a specific release

  1. List the available releases.  
  ```console  
  apt list -a couchbase-server  
  ```  
  Available releases are listed with their full `version-build` number:  
  couchbase-server/xenial **6.0.0-1693-1** amd64
  2. Specify a release to install it.  
  ```console  
  sudo apt-get install couchbase-server=version-string  
  ```  
  Using the example listing from the previous step, the resulting installation command would be:  
  sudo apt-get install couchbase-server=**6.0.0-1693-1**  
To install the latest release  
```console  
sudo apt-get install couchbase-server-community  
```  
To install a specific release

  1. List the available releases.  
  ```console  
  apt list -a couchbase-server-community  
  ```  
  Available releases are listed with their full `version-build` number:  
  couchbase-server-community/xenial **6.0.0-1693-1** amd64
  2. Specify a release to install it.  
  ```console  
  sudo apt-get install couchbase-server-community=version-string  
  ```  
  Using the example listing from the previous step, the resulting installation command would be:  
  sudo apt-get install couchbase-server-community=**6.0.0-1693-1**  
The `apt-get` command automatically downloads and installs the latest version of Couchbase Server, along with all of its dependencies.  
Once installation is complete, Couchbase Server will start automatically (and will continue to start automatically at run levels 2, 3, 4, and 5, and explicitly shut down at run levels 0, 1, and 6). You can use the `systemctl` command (`service` on older operating systems) to start and stop the Couchbase Server service, as well as check the current status. Refer to [Couchbase Server Startup and Shutdown](startup-shutdown.md) for more information.
5. Open a web browser and access the Couchbase Web Console to [verify](testing.md) that the installation was successful and that the node is available.

### [](#install-using-deb-package)Install Using Deb Package

Install Couchbase Server on Ubuntu and Debian using a full _deb_ package provided by Couchbase.

1. Download the appropriate package from the Couchbase [downloads page](https://www.couchbase.com/downloads).
2. Reload the local package database.  
```console  
sudo apt-get update  
```
3. Install Couchbase Server.  
```console  
sudo dpkg -i ./package-name.deb  
```  
If `dpkg` reports any errors about missing dependencies, issue the following command to download and install those dependencies from the internet:  
```console  
sudo apt-get -f install  
```  
Once installation is complete, Couchbase Server will start automatically (and will continue to start automatically at run levels 2, 3, 4, and 5, and explicitly shut down at run levels 0, 1, and 6). You can use the `systemctl` command (`service` on older operating systems) to start and stop the Couchbase Server service, as well as check the current status. Refer to [Couchbase Server Startup and Shutdown](startup-shutdown.md) for more information.
4. Open a web browser and access the Couchbase Web Console to [verify](testing.md) that the installation was successful and that the node is available.

## [](#deb-nonroot-nonsudo)Installing as Non-Root

Non-root installation is performed identically for all supported Linux distributions, including Ubuntu and Debian. For instructions, see [Non-Root Install and Upgrade](non-root.md).

## [](#next-steps)Next Steps

Following installation and start-up of Couchbase Server, a node must be _initialized_ and _provisioned_.

* If it is the first node in a deployment, initialization and provisioning happens all at once when you create a _cluster of one_.  
Refer to [Create a Cluster](../manage/manage-nodes/create-cluster.md)
* If you already have an existing cluster, the node is initialized and provisioned when you add it to the cluster.  
Refer to [Add a Node and Rebalance](../manage/manage-nodes/add-node-and-rebalance.md)
* Optionally, initialization can be performed explicitly and independently of provisioning, as a prior process, in order to establish certain configurations, such as custom disk-paths.  
Refer to [Initialize a Node](../manage/manage-nodes/initialize-node.md)