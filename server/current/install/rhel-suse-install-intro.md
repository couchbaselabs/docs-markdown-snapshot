---
title: Install Couchbase Server on Red Hat Enterprise Linux, Oracle Linux, or
  Amazon Linux 2023
description: Couchbase Server can be installed on Red Hat Enterprise Linux,
  Oracle Linux, or Amazon Linux 2023 for production and development use cases.
editUrl: https://github.com/couchbase/docs-server/edit/release/8.0/modules/install/pages/rhel-suse-install-intro.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:server:install:rhel-suse-install-intro.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/current/install/rhel-suse-install-intro.html)

# Install Couchbase Server on Red Hat Enterprise Linux, Oracle Linux, or Amazon Linux 2023

> Couchbase Server can be installed on Red Hat Enterprise Linux, Oracle Linux, or Amazon Linux 2023 for production and development use cases. 

Couchbase Server supports both root and non-root installations of Red Hat Enterprise Linux, Oracle Linux, and Amazon Linux 2023.

Use the instructions on this page to install Couchbase Server on Red Hat Enterprise Linux, Oracle Linux, or Amazon Linux 2023 using Couchbase-provided RPM packages. The instructions support both Enterprise and Community [editions](https://www.couchbase.com/products/editions).

If you’re upgrading an existing Couchbase Server instance, see [Upgrading Couchbase Server](upgrade.md).

## [](#prerequisites-for-installation)Prerequisites for Installation

Couchbase Server works out of the box with most OS configurations. However, the following are the prerequisites for installation:

* Your system meets the [minimum requirements](pre-install.md) and that your operating system version is [supported](install-platforms.md).
* You’re working from a clean system and that you have [uninstalled](install-uninstalling.md) any previous versions of Couchbase Server.  
If you’re upgrading an existing installation of Couchbase Server, see [Upgrading Couchbase Server](upgrade.md).
* For Oracle Linux, only the Red Hat Compatible Kernel (RHCK) is supported. The Unbreakable Enterprise Kernel (UEK) is not supported.
* For production deployments, make sure to follow the [deployment guidelines](install-production-deployment.md) so that your systems and environment are properly sized and configured before installation.

## [](#basic-installation)Basic Installation

> [!IMPORTANT]
> * You must be logged in as root user (superuser) or use `sudo` to run the installation commands.
> * `dnf` is the default package manager on Red Hat Enterprise Linux 8 and later versions, the corresponding Oracle Linux releases, and Amazon Linux 2023\. On earlier versions where only `yum` is available, you can replace `dnf` with `yum` in all commands.

This section explains the following installations using the `dnf` or `yum` package managers, and RPM package methods:

* [Install Using Dnf or Yum](#install-using-dnf-yum).
* [Install Using RPM Package](#install-using-rpm).

### [](#install-using-dnf-yum)Install Using Dnf or Yum

The Red Hat package managers `dnf` and `yum` provide the simplest and most comprehensive way to install Couchbase Server on Red Hat Enterprise Linux or Oracle Linux. This method involves downloading and installing a small meta package from Couchbase, which `dnf` or `yum` can then use to automatically download and install Couchbase Server and all of its dependencies.

> [!NOTE]
> All commands in this section use `dnf` for Red Hat Enterprise Linux 8 and later versions, the corresponding Oracle Linux releases, and Amazon Linux 2023\. On earlier versions where only `yum` is available, you can replace `dnf` with `yum` in all commands.

1. Download the meta package.  
```console  
curl -O https://packages.couchbase.com/releases/couchbase-release/couchbase-release-1.0.noarch.rpm  
```
2. Install the meta package.  
```console  
sudo rpm -i ./couchbase-release-1.0.noarch.rpm  
```  
The meta package installs the necessary information for `dnf` or `yum` to retrieve all necessary Couchbase Server installation packages and dependencies.
3. Install Couchbase Server.

  * Enterprise
  * Community  
To install the latest release  
Run the following command:  
```console  
sudo dnf install couchbase-server  
```  
You’ll be prompted to start the download of Couchbase Server (plus any dependencies), as well as import several GPG keys. For each of these prompts, type `y` to accept and continue.  
To install a specific release

  1. List the available releases.  
  ```console  
  dnf list --showduplicates couchbase-server  
  ```  
  Available releases are listed with their complete `version-build` number:  
  couchbase-server.x86_64 <version_number>-<build_number>  
  The following is an example of the listing:  
  couchbase-server.x86_64 **8.0.0-3777**
  2. Specify a release to install it.  
  ```console  
  sudo dnf install couchbase-server-<version_number>-<build_number>  
  ```  
  The following is an example of the installation command:  
  sudo dnf install couchbase-server-**8.0.0-3777**  
  You’ll be prompted to start the download of Couchbase Server and its dependencies, and import several GPG keys. For each of these prompts, type `y` to accept and continue.  
To install the latest release  
Run the following command:  
```console  
sudo dnf install couchbase-server-community  
```  
You’ll be prompted to start the download of Couchbase Server and its dependencies, and import several GPG keys. For each of these prompts, type `y` to accept and continue.  
To install a specific release

  1. List the available releases.  
  ```console  
  dnf list --showduplicates couchbase-server-community  
  ```  
  Available releases are listed with their full `version-build` number:  
  couchbase-server-community.x86_64 <version_number>-<build_number>  
  The following is an example of the listing:  
  couchbase-server-community.x86_64 **8.0.0-3777**
  2. Specify a release to install it.  
  ```console  
  sudo dnf install couchbase-server-community-<version_number>-<build_number>  
  ```  
  The following is an example of the installation command:  
  sudo dnf install couchbase-server-community-**8.0.0-3777**  
  You’ll be prompted to start the download of Couchbase Server and its dependencies, and import several GPG keys. For each of these prompts, type `y` to accept and continue.  
After the installation is complete, Couchbase Server starts automatically. Couchbase Server continues to start automatically at run levels 2, 3, 4, and 5, and explicitly shuts down at run levels 0, 1, and 6\. You can use the `systemctl` command, a `service` on older operating systems, to start and stop the Couchbase Server service, and to verify the current status. For more information, see [Couchbase Server Startup and Shutdown](startup-shutdown.md).
4. Open the Couchbase Web Console in a browser to [verify](testing.md) that the installation was successful and that the node is available.

### [](#install-using-rpm)Install Using RPM Package

Install Couchbase Server on Red Hat Enterprise Linux or Oracle Linux or Amazon Linux 2023 using a full RPM package provided by Couchbase.

> [!NOTE]
> All commands in this section use `dnf` for Red Hat Enterprise Linux 8 and later versions, the corresponding Oracle Linux releases, and Amazon Linux 2023\. On earlier versions where only `yum` is available, you can replace `dnf` with `yum` in all commands.

1. Download the appropriate package from the Couchbase [downloads page](https://www.couchbase.com/downloads).
2. Install Couchbase Server.

  * For Red Hat Enterprise Linux, use the following command:  
  ```console  
  sudo dnf upgrade ./package-name.rpm  
  ```
  * For Oracle Linux, use the following command:  
  ```console  
  sudo dnf install ./package-name.rpm  
  ```
  * For Amazon Linux 2023, use the following command:  
  ```console  
  sudo rpm --install package-name.rpm  
  ```  
  If any Couchbase Server dependencies are missing on your system, `dnf` or `yum` automatically downloads and installs them as part of the installation process.  
  After the installation is complete, Couchbase Server starts automatically. Couchbase Server starts automatically at run levels 2, 3, 4, and 5, and explicitly shuts down at run levels 0, 1, and 6\. You can use the `systemctl` command, a `service` on older operating systems, to start and stop the Couchbase Server service, and to verify the current status. For more information, see [Couchbase Server Startup and Shutdown](startup-shutdown.md).
3. Open the Couchbase Web Console in a browser to [verify](testing.md) that the installation was successful and that the node is available.

## [](#rh-nonroot-nonsudo-)Installing as Non-Root

The non-root installation process is identical for all supported Linux distributions, including Red Hat Enterprise Linux, Oracle Linux, and Amazon Linux 2023\. For instructions, see [Non-Root Install and Upgrade](non-root.md).

## [](#setting-max-process-limits)Setting Max Process Limits

Couchbase recommends that, on Red Hat Enterprise Linux, you increase the maximum process limits for Couchbase.

To set the process limits, create a `.conf` file in the `/etc/security/limits.d` directory such as `91-couchbase.conf`, and add the following values:

```console
couchbase soft nproc 4096
couchbase hard nproc 16384
```

For more information about non-root installation and upgrade, see [Establish Limits for User Processes and File Descriptors](non-root.md#establish-limits-for-user-processes-and-file-descriptors).

## [](#next-steps)Next Steps

After you install and start Couchbase Server, initialize and provision a node.

* If it’s the first node in a deployment, initialization and provisioning happens all at once when you create a cluster of one.  
For more information, see [Create a Cluster](../manage/manage-nodes/create-cluster.md).
* If you already have an existing cluster, the node is initialized and provisioned when you add it to the cluster.

For more information, see [Add a Node and Rebalance](../manage/manage-nodes/add-node-and-rebalance.md).

* Optionally, you can initialize a node explicitly and independently of provisioning, as a prior process. This is to establish configurations such as custom disk-paths.

For more information, see [Initialize a Node](../manage/manage-nodes/initialize-node.md).