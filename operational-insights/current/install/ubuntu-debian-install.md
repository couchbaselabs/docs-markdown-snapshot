---
title: Install on Ubuntu and Debian
description: Operational Insights can be installed on Ubuntu Linux and Debian
  Linux for production and development use-cases. Root installation is
  supported.
pubDate: 2026-10-23T04:31:18.652Z
meta:
  component:
    title: Operational Insights Enterprise
    version: "3.0"
  topic_type: concept
antora:
  editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/3.0/modules/install/pages/ubuntu-debian-install.adoc
  xref: xref:enterprise-analytics:install:ubuntu-debian-install.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operational-insights/current/install/ubuntu-debian-install.html)

# Install on Ubuntu and Debian

> Operational Insights can be installed on Ubuntu Linux and Debian Linux for production and development use-cases. Root installation is supported. 

Use the instructions on this page to install Operational Insights on Ubuntu using Couchbase-provided `deb` packages.

## [](#before-you-install)Before You Install

Operational Insights works out-of-the-box with most OS configurations. The procedures on this page assume that you work from a clean system, your system meets the [system resource requirements](sys-resource-req.md), and your operating system version is a [supported platform](supported-platform.md).

For production deployments, make sure to follow the [deployment guidelines](deploy-guidelines.md) so that your systems and environment are properly sized and configured before installation.

## [](#basic-installation)Basic Installation

You must be logged in as `root` (superuser) or use `sudo` to run the installation commands.

### [](#install-using-apt)Install Using Apt

The Advanced Package Tool (`apt`) provides the simplest and most comprehensive way to install Operational Insights on Ubuntu and Debian. This method involves downloading and installing a small meta package from Couchbase, which `apt` uses to automatically download and install Operational Insights and its dependencies.

1. Download the meta package:  
```console  
curl -O https://packages.couchbase.com/releases/couchbase-release/couchbase-release-1.0-noarch.deb  
```
2. Install the meta package:  
```console  
sudo dpkg -i ./couchbase-release-1.0-noarch.deb  
```  
The meta package installs the necessary information for `apt` to retrieve all the necessary Operational Insights installation packages and dependencies.
3. Reload the local package database:  
```console  
sudo apt-get update  
```
4. Install Operational Insights:

  * To install the latest release  
  ```console  
  sudo apt-get install operational-insights  
  ```
  * To install a specific release

    1. List the available releases.  
      ```console  
      apt list -a operational-insights  
      ```  
      Available releases are listed with their full `version-build` number:  
      operational-insights/xenial **2.0.0-1060** amd64
    2. Specify a release to install it:  
      ```console  
      sudo apt-get install operational-insights=[.var] version-string  
      ```  
      Using the example listing from the previous step, the resulting installation command would be:  
      sudo apt-get install operational-insights=**2.0.0-1060**

### [](#install-using-deb-package)Install Using Deb Package

Install Operational Insights on Ubuntu and Debian using a full `deb` package provided by Couchbase.

1. Download the appropriate package from the Couchbase [downloads page](https://www.couchbase.com/downloads).
2. Reload the local package database:  
```console  
sudo apt-get update  
```
3. Install Operational Insights:  
```console  
sudo dpkg -i ./[.var] package-name.deb  
```  
If `dpkg` reports any errors about missing dependencies, issue the following command to download and install those dependencies from the Internet:  
```console  
sudo apt-get -f install  
```  
Once installation is complete, Operational Insights starts automatically. It continues to start automatically at run levels 2, 3, 4, and 5, and explicitly shut down at run levels 0, 1, and 6\. You can use the `systemctl` command to start and stop Operational Insights, and check the current status. On earlier operating systems, use `service`. For more information, see [Start and Stop Operational Insights](start-stop-cb-operational-insights.md).
4. Open a web browser and open the Operational Insights Web Console to [verify](verify-installation.md) that the installation was successful and that the node is available.

## [](#install-the-python-udf-add-on)Install the Python UDF Add-on

To run [Python user-defined functions](../sqlpp/9b%5Fpython%5Fudf.md), install the optional `operational-insights-udf` add-on on every node, after you install Operational Insights. The add-on requires Docker. See [Install the Python UDF Add-on](install-udf-addon.md).

## [](#next-steps)Next Steps

Following installation and start-up of Operational Insights, you must initialize and provision a node.

* If it's the first node in a deployment, initialization and provisioning happens all at once when you create a cluster of one.  
For more information, see [Create a Cluster](../manage/manage-nodes/create-cluster.md).
* If you already have an existing cluster, the node is initialized and provisioned when you add it to the cluster.  
For more information, see [Add a Node and Rebalance](../manage/manage-nodes/add-node-and-rebalance.md).
* Optionally, you can perform initialization explicitly and independently of provisioning, as a prior process, to establish certain configurations, such as custom disk-paths.  
For more information, see [Initialize a Node](../manage/manage-nodes/initialize-node.md).