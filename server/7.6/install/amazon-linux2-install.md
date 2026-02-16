[View original HTML](/server/7.6/install/amazon-linux2-install.html)

> Couchbase Server can be installed on Amazon Linux 2 for production and development use-cases. Root and non-root installations are supported. 

Amazon Linux 2 is supported with Couchbase Server 6.0.1+. See [Supported Operating Systems](install-platforms.md) for details.

Use the instructions on this page to install Couchbase Server on Amazon Linux 2 using Couchbase-provided RPM packages. The instructions support both Enterprise and Community [editions](https://www.couchbase.com/products/editions).

If you’re upgrading an existing installation of Couchbase Server, refer to [Upgrading Couchbase Server](upgrade.md).

## [](#before-you-install)Before You Install

Couchbase Server works out-of-the-box with most OS configurations. However, the procedures on this page assume the following:

* Your system meets the [minimum requirements](pre-install.md) and that your operating system version is [supported](install-platforms.md).
* You’re working from a clean system and that you’ve [uninstalled](install-uninstalling.md) any previous versions of Couchbase Server.  
If you’re upgrading an existing installation of Couchbase Server, refer to [Upgrading Couchbase Server](upgrade.md).

For production deployments, make sure to follow the [deployment guidelines](install-production-deployment.md) so that your systems and environment are properly sized and configured before installation.

## [](#basic-installation)Basic Installation

You must be logged in as root (superuser) or use `sudo` to run the installation commands.

### [](#install-using-rpm-package)Install Using RPM Package

Install Couchbase Server on Amazon Linux 2 using a full RPM package provided by Couchbase.

1. Download the appropriate package from the Couchbase [downloads page](https://www.couchbase.com/downloads).
2. Install Couchbase Server.  
```console  
sudo rpm --install package-name.rpm  
```  
Once installation is complete, Couchbase Server will start automatically (and will continue to start automatically at run levels 2, 3, 4, and 5, and explicitly shut down at run levels 0, 1, and 6). You can use the `systemctl` command (`service` on older operating systems) to start and stop the Couchbase Server service, as well as check the current status. Refer to [Couchbase Server Startup and Shutdown](startup-shutdown.md) for more information.
3. Open a web browser and access the Couchbase Web Console to [verify](testing.md) that the installation was successful and the node is available.

## [](#amzn-lnx2-nonroot-nonsudo-)Installing as Non-Root

Non-root installation is performed identically for all supported Linux distributions, including Amazon Linux 2\. For instructions, see [Non-Root Install and Upgrade](non-root.md).

## [](#next-steps)Next Steps

Following installation and start-up of Couchbase Server, a node must be _initialized_ and _provisioned_.

* If it is the first node in a deployment, initialization and provisioning happens all at once when you create a _cluster of one_.  
Refer to [Create a Cluster](../manage/manage-nodes/create-cluster.md)
* If you already have an existing cluster, the node is initialized and provisioned when you add it to the cluster.  
Refer to [Add a Node and Rebalance](../manage/manage-nodes/add-node-and-rebalance.md)
* Optionally, initialization can be performed explicitly and independently of provisioning, as a prior process, in order to establish certain configurations, such as custom disk-paths.  
Refer to [Initialize a Node](../manage/manage-nodes/initialize-node.md)