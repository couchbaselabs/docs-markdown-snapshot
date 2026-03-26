---
title: Install Couchbase Server on Red Hat Enterprise
description: Couchbase Server can be installed on Red Hat Enterprise Linux for
  production and development use-cases.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/install/pages/rhel-suse-install-intro.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:7.2@server:install:rhel-suse-install-intro.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/install/rhel-suse-install-intro.html)

# Install Couchbase Server on Red Hat Enterprise

> Couchbase Server can be installed on Red Hat Enterprise Linux for production and development use-cases. Root and non-root installations are supported. 

Use the instructions on this page to install Couchbase Server on Red Hat Enterprise Linux using Couchbase-provided RPM packages. The instructions support both Enterprise and Community [editions](https://www.couchbase.com/products/editions).

If you're upgrading an existing installation of Couchbase Server, refer to [Upgrading Couchbase Server](upgrade.md).

## [](#before-you-install)Before You Install

Couchbase Server works out-of-the-box with most OS configurations. However, the procedures on this page assume the following:

* Your system meets the [minimum requirements](pre-install.md) and that your operating system version is [supported](install-platforms.md).
* You're working from a clean system and that you've [uninstalled](install-uninstalling.md) any previous versions of Couchbase Server.  
If you're upgrading an existing installation of Couchbase Server, refer to [Upgrading Couchbase Server](upgrade.md).

For production deployments, make sure to follow the [deployment guidelines](install-production-deployment.md) so that your systems and environment are properly sized and configured before installation.

## [](#basic-installation)Basic Installation

You must be logged in as root (superuser) or use `sudo` to run the installation commands.

### [](#install-using-yum)Install Using Yum

The Red Hat package manager (`yum`) provides the simplest and most comprehensive way to install Couchbase Server on Red Hat Enterprise. This method involves downloading and installing a small meta package from Couchbase, which `yum` can then use to automatically download and install Couchbase Server and all of its dependencies.

1. Download the meta package.  
```console  
curl -O https://packages.couchbase.com/releases/couchbase-release/couchbase-release-1.0.noarch.rpm  
```
2. Install the meta package.  
```console  
sudo rpm -i ./couchbase-release-1.0.noarch.rpm  
```  
The meta package installs the necessary information for `yum` to be able to retrieve all of the necessary Couchbase Server installation packages and dependencies.
3. Install Couchbase Server.

  * Enterprise
  * Community  
To install the latest release  
```console  
sudo yum install couchbase-server  
```  
You'll be prompted to start the download of Couchbase Server (plus any dependencies), as well as import several GPG keys. For each of these prompts, type `y` to accept and continue.  
To install a specific release

  1. List the available releases.  
  ```console  
  yum list --showduplicates couchbase-server  
  ```  
  Available releases are listed with their full `version-build` number:  
  couchbase-server.x86_64   **6.0.0-1693**
  2. Specify a release to install it.  
  ```console  
  sudo yum install couchbase-server-version-build  
  ```  
  Using the example listing from the previous step, the resulting installation command would be:  
  sudo yum install couchbase-server-**6.0.0-1693**  
  You'll be prompted to start the download of Couchbase Server (plus any dependencies), as well as import several GPG keys. For each of these prompts, type `y` to accept and continue.  
To install the latest release  
```console  
sudo yum install couchbase-server-community  
```  
You'll be prompted to start the download of Couchbase Server (plus any dependencies), as well as import several GPG keys. For each of these prompts, type `y` to accept and continue.  
To install a specific release

  1. List the available releases.  
  ```console  
  yum list --showduplicates couchbase-server-community  
  ```  
  Available releases are listed with their full `version-build` number:  
  couchbase-server-community.x86_64   **6.0.0-1693**
  2. Specify a release to install it.  
  ```console  
  sudo yum install couchbase-server-community-version-build  
  ```  
  Using the example listing from the previous step, the resulting installation command would be:  
  sudo yum install couchbase-server-community-**6.0.0-1693**  
  You'll be prompted to start the download of Couchbase Server (plus any dependencies), as well as import several GPG keys. For each of these prompts, type `y` to accept and continue.  
Once installation is complete, Couchbase Server will start automatically (and will continue to start automatically at run levels 2, 3, 4, and 5, and explicitly shut down at run levels 0, 1, and 6). You can use the `systemctl` command (`service` on older operating systems) to start and stop the Couchbase Server service, as well as check the current status. Refer to [Couchbase Server Startup and Shutdown](startup-shutdown.md) for more information.
4. Open a web browser and access the Couchbase Web Console to [verify](testing.md) that the installation was successful and that the node is available.

### [](#install-using-rpm-package)Install Using RPM Package

Install Couchbase Server on Red Hat Enterprise using a full RPM package provided by Couchbase.

1. Download the appropriate package from the Couchbase [downloads page](https://www.couchbase.com/downloads).
2. Install Couchbase Server.  
```console  
sudo yum upgrade ./package-name.rpm  
```  
If any Couchbase Server dependencies are missing on your system, `yum` will automatically download and install them as part of the installation process.  
Once installation is complete, Couchbase Server will start automatically (and will continue to start automatically at run levels 2, 3, 4, and 5, and explicitly shut down at run levels 0, 1, and 6). You can use the `systemctl` command (`service` on older operating systems) to start and stop the Couchbase Server service, as well as check the current status. Refer to [Couchbase Server Startup and Shutdown](startup-shutdown.md) for more information.
3. Open a web browser and access the Couchbase Web Console to [verify](testing.md) that the installation was successful and the node is available.

## [](#rh-nonroot-nonsudo-)Installing as Non-Root

Non-root installation is performed identically for all supported Linux distributions, including Red Hat Enterprise. For instructions, see [Non-Root Install and Upgrade](non-root.md).

## [](#setting-max-process-limits)Setting Max Process Limits

On Red Hat Enterprise, it's recommended that you increase the maximum process limits for Couchbase.

To set the process limits, create a `.conf` file in the `/etc/security/limits.d` directory (such as `91-couchbase.conf`), and add the following values:

```console
couchbase soft nproc 4096
couchbase hard nproc 16384
```

For more information (provided in the context of _non-root_ install and upgrade), see [Establish Limits for User Processes and File Descriptors](non-root.md#establish-limits-for-user-processes-and-file-descriptors).

## [](#next-steps)Next Steps

Following installation and start-up of Couchbase Server, a node must be _initialized_ and _provisioned_.

* If it is the first node in a deployment, initialization and provisioning happens all at once when you create a _cluster of one_.  
Refer to [Create a Cluster](../manage/manage-nodes/create-cluster.md)
* If you already have an existing cluster, the node is initialized and provisioned when you add it to the cluster.  
Refer to [Add a Node and Rebalance](../manage/manage-nodes/add-node-and-rebalance.md)
* Optionally, initialization can be performed explicitly and independently of provisioning, as a prior process, in order to establish certain configurations, such as custom disk-paths.  
Refer to [Initialize a Node](../manage/manage-nodes/initialize-node.md)