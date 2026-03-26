---
title: Install Enterprise Analytics on Ubuntu and Debian
description: Enterprise Analytics can be installed on Ubuntu Linux and Debian
  Linux for production and development use-cases. Root installation is
  supported.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.0/modules/install/pages/ubuntu-debian-install.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:2.0@enterprise-analytics:install:ubuntu-debian-install.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/enterprise-analytics/2.0/install/ubuntu-debian-install.html)

# Install Enterprise Analytics on Ubuntu and Debian

> Enterprise Analytics can be installed on Ubuntu Linux and Debian Linux for production and development use-cases. Root installation is supported. 

Use the instructions on this page to install Enterprise Analytics on Ubuntu using Couchbase-provided `deb` packages.

## [](#before-you-install)Before You Install

Enterprise Analytics works out-of-the-box with most OS configurations. The procedures on this page assume that you work from a clean system, your system meets the [system resource requirements](sys-resource-req.md), and your operating system version is a [supported platform](supported-platform.md).

For production deployments, make sure to follow the [deployment guidelines](deploy-guidelines.md) so that your systems and environment are properly sized and configured before installation.

## [](#basic-installation)Basic Installation

You must be logged in as `root` (superuser) or use `sudo` to run the installation commands.

### [](#install-using-apt)Install Using Apt

The Advanced Package Tool (`apt`) provides the simplest and most comprehensive way to install Enterprise Analytics on Ubuntu and Debian. This method involves downloading and installing a small meta package from Couchbase, which `apt` uses to automatically download and install Enterprise Analytics and its dependencies.

1. Download the meta package:  
```console  
curl -O https://packages.couchbase.com/releases/couchbase-release/couchbase-release-1.0-noarch.deb  
```
2. Install the meta package:  
```console  
sudo dpkg -i ./couchbase-release-1.0-noarch.deb  
```  
The meta package installs the necessary information for `apt` to retrieve all the necessary Enterprise Analytics installation packages and dependencies.
3. Reload the local package database:  
```console  
sudo apt-get update  
```
4. Install Enterprise Analytics:

  * To install the latest release  
  ```console  
  sudo apt-get install enterprise-analytics  
  ```
  * To install a specific release

    1. List the available releases.  
      ```console  
      apt list -a enterprise-analytics  
      ```  
      Available releases are listed with their full `version-build` number:  
      enterprise-analytics/xenial **2.0.0-1060** amd64
    2. Specify a release to install it:  
      ```console  
      sudo apt-get install enterprise-analytics=[.var] version-string  
      ```  
      Using the example listing from the previous step, the resulting installation command would be:  
      sudo apt-get install enterprise-analytics=**2.0.0-1060**

### [](#install-using-deb-package)Install Using Deb Package

Install Enterprise Analytics on Ubuntu and Debian using a full `deb` package provided by Couchbase.

1. Download the appropriate package from the Couchbase [downloads page](https://www.couchbase.com/downloads).
2. Reload the local package database:  
```console  
sudo apt-get update  
```
3. Install Enterprise Analytics:  
```console  
sudo dpkg -i ./[.var] package-name.deb  
```  
If `dpkg` reports any errors about missing dependencies, issue the following command to download and install those dependencies from the Internet:  
```console  
sudo apt-get -f install  
```  
Once installation is complete, Enterprise Analytics starts automatically. It continues to start automatically at run levels 2, 3, 4, and 5, and explicitly shut down at run levels 0, 1, and 6\. You can use the `systemctl` command to start and stop Enterprise Analytics, and check the current status. On earlier operating systems, use `service`. For more information, see [Enterprise Analytics Startup and Shutdown](start-stop-cb-enterprise-analytics.md).
4. Open a web browser and open the Enterprise Analytics Web Console to [verify](verify-installation.md) that the installation was successful and that the node is available.

## [](#next-steps)Next Steps

Following installation and start-up of Enterprise Analytics, you must initialize and provision a node.

* If it's the first node in a deployment, initialization and provisioning happens all at once when you create a cluster of one.  
For more information, see [Create a Cluster](../manage/manage-nodes/create-cluster.md).
* If you already have an existing cluster, the node is initialized and provisioned when you add it to the cluster.  
For more information, see [Add a Node and Rebalance](../manage/manage-nodes/add-node-and-rebalance.md).
* Optionally, you can perform initialization explicitly and independently of provisioning, as a prior process, to establish certain configurations, such as custom disk-paths.  
For more information, see [Initialize a Node](../manage/manage-nodes/initialize-node.md).