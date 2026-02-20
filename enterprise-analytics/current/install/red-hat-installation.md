---
title: Install Enterprise Analytics on Red Hat Enterprise
description: Enterprise Analytics can be installed on Red Hat Enterprise Linux
  for production and development use-cases.
editUrl: https://github.com/couchbaselabs/docs-enterprise-analytics/edit/release/2.1/modules/install/pages/red-hat-installation.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:enterprise-analytics:install:red-hat-installation.adoc[]
---

[View original HTML](/enterprise-analytics/current/install/red-hat-installation.html)

# Install Enterprise Analytics on Red Hat Enterprise

> Enterprise Analytics can be installed on Red Hat Enterprise Linux for production and development use-cases. Root installations are supported. 

Use the instructions on this page to install Enterprise Analytics on Red Hat Enterprise Linux using Couchbase-provided RPM packages.

## [](#before-you-install)Before You Install

Enterprise Analytics works out-of-the-box with most OS configurations. However, the procedures on this page assume the following:

* Your system meets the [minimum requirements](sys-resource-req.md) and your operating system version is [supported](supported-platform.md).
* You’re working from a clean system.  
For production deployments, make sure to follow the [deployment guidelines](deploy-guidelines.md) so that your systems and environment are properly sized and configured before installation.

## [](#basic-installation)Basic Installation

You must log in as root (superuser) or use `sudo` to run the installation commands.

### [](#install-using-yum)Install Using Yum

The Red Hat package manager (`yum`) provides the simplest and most comprehensive way to install Enterprise Analytics on Red Hat Enterprise. This method involves downloading and installing a small meta package from Couchbase, which `yum` uses to automatically download and install Enterprise Analytics and dependencies.

1. Download the meta package.  
```console  
curl -O https://packages.couchbase.com/releases/couchbase-release/couchbase-release-1.0.noarch.rpm  
```
2. Install the meta package.  
```console  
sudo rpm -i ./couchbase-release-1.0.noarch.rpm  
```  
The meta package installs the necessary information for `yum` to retrieve all of the necessary Enterprise Analytics installation packages and dependencies.
3. Install the latest release or a specific release of Enterprise Analytics.

  * To install the latest release:  
  ```console  
  sudo yum install enterprise-analytics  
  ```  
  You’ll be prompted to start the download of Enterprise Analytics, plus any dependencies, as well as import several GPG keys.
  * To install a specific release:

    * List the available releases.  
      ```console  
      yum list --showduplicates enterprise-analytics  
      ```  
      Available releases are listed with their full `version-build` number:  
      enterprise-analytics.x86_64   **2.0.0-1060**
    * Specify a release to install it.  
      ```console  
      sudo yum install enterprise-analytics-version-build  
      ```  
      Using the example listing from the previous step, the resulting installation command would be:  
      sudo yum install enterprise-analytics-**2.0.0-1060**  
      You’ll be prompted to start the download of Enterprise Analytics (plus any dependencies), as well as import several GPG keys. For each of these prompts, type `y` to accept and continue.  
      Once installation is complete, Enterprise Analytics starts automatically. It starts automatically at run levels 2, 3, 4, and 5\. It explicitly shuts down at run levels 0, 1, and 6\. You can use the `systemctl` command to start and stop Enterprise Analytics, and check the current status. On earlier operating systems, use `service`. For more information, see [Enterprise Analytics Startup and Shutdown](start-stop-cb-enterprise-analytics.md).

### [](#install-using-rpm-package)Install Using RPM Package

Install Enterprise Analytics on Red Hat Enterprise using a full RPM package provided by Couchbase.

1. Download the appropriate package from the Couchbase [downloads page](https://www.couchbase.com/downloads).
2. Install Enterprise Analytics.  
```console  
sudo yum upgrade ./package-name.rpm  
```  
If any Enterprise Analytics dependencies are missing on your system, `yum` automatically downloads and installs them as part of the installation process.  
Once installation is complete, Enterprise Analytics starts automatically. It starts automatically at run levels 2, 3, 4, and 5\. It explicitly shuts down at run levels 0, 1, and 6\. You can use the `systemctl` command to start and stop Enterprise Analytics, and check the current status. On earlier operating systems, use `service`. For more information, see [Enterprise Analytics Startup and Shutdown](start-stop-cb-enterprise-analytics.md).

## [](#setting-max-process-limits)Setting Max Process Limits

On Red Hat Enterprise, Couchbase recommends that you increase the maximum process limits for Couchbase.

TTo set the process limits, create a `.conf` file in the `/etc/security/limits.d` directory. For example, `91-couchbase.conf`. Add the following values:

```console
couchbase soft nproc 4096
couchbase hard nproc 16384
```

## [](#next-steps)Next Steps

Following installation and start-up of Enterprise Analytics, you must initialize and provision a node.

* If it’s the first node in a deployment, initialization and provisioning happens all at once when you create a cluster of one.  
For more information, see [Create a Cluster](../manage/manage-nodes/create-cluster.md).
* If you already have an existing cluster, you must initialize and provision a node when you add it to the cluster.  
For more information, see [Add a Node and Rebalance](../manage/manage-nodes/add-node-and-rebalance.md).
* Optionally, you can perform initialization explicitly and independently of provisioning, as a prior process, to establish certain configurations, such as custom disk-paths.  
For more information, see [Initialize a Node](../manage/manage-nodes/initialize-node.md).