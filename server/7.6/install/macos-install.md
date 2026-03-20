---
title: Install Couchbase Server on macOS
description: Couchbase Server can be installed on macOS for development use-cases.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.6/modules/install/pages/macos-install.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:7.6@server:install:macos-install.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.6/install/macos-install.html)

# Install Couchbase Server on macOS

> Couchbase Server can be installed on macOS for development use-cases. 

Use the instructions on this page to install Couchbase Server on macOS platforms using Couchbase-provided application packages. The instructions support both Enterprise and Community [editions](https://www.couchbase.com/products/editions).

If you’re upgrading an existing installation of Couchbase Server, refer to [Upgrading Couchbase Server](upgrade.md).

## [](#before-you-install)Before You Install

Couchbase Server works out-of-the-box with most OS configurations. However, the procedures on this page assume the following:

* Your system meets the [minimum requirements](pre-install.md) and that your operating system version is [supported](install-platforms.md).
* You’re working from a clean system and that you’ve [uninstalled](install-uninstalling.md) any previous versions of Couchbase Server.  
If you’re upgrading an existing installation of Couchbase Server, refer to [Upgrading Couchbase Server](upgrade.md).

Although macOS is not supported for production deployments, you should still review the [deployment guidelines](install-production-deployment.md) for more information about best practices.

## [](#basic-installation)Basic Installation

1. Download the appropriate package from the Couchbase [downloads page](https://www.couchbase.com/downloads).  
Couchbase Server for macOS is packaged as a standalone application in a compressed disk image.
2. Mount the the downloaded `.dmg` file.  
Locate the downloaded Couchbase Server `.dmg` file (typically located in the default `~/Downloads` folder) and double-click it. Opening the file will automatically mount a volume in Finder containing the `Couchbase Server.app` application file.
3. Drag-and-drop the `Couchbase Server.app` file into the system `/Applications` folder.  
> [!NOTE]  
> macOS has a security policy that requires downloaded software to be run directly from the `/Applications` folder. Attempting to open `Couchbase Server.app` from any other folder or sub-folder will result in a "Problem Running Couchbase" error.  
>  
> ![Problem Running Couchbase](_images/error-macos-problem-running.png)
4. Double-click `Couchbase Server.app` to start Couchbase Server.  
A macOS Gatekeeper [dialogue](https://support.apple.com/en-us/HT202491) will appear asking if you want to open `Couchbase Server.app`. Click **Open** to continue.  
Couchbase Server runs as a background application. When Couchbase Server starts, the Couchbase Server icon ![Couchbase Server menu bar icon](_images/macos-menu-bar-icon-light.png) will appear in the menu bar.
5. Open a web browser and access the Couchbase Web Console to [verify](testing.md) that the installation was successful and the node is available.  
You can open the Couchbase Web Console by clicking ![Couchbase Server menu bar icon](_images/macos-menu-bar-icon-light.png) and then selecting **Open Admin Console**.

Although the Couchbase Server software resides in the `/Applications` folder, the Couchbase data files are stored in other folders. For more information, refer to [Uninstalling Couchbase Server](install-uninstalling.md).

### [](#terminal-based-installation)Terminal-based Installation

As an alternative to the UI-based installation, you can install Couchbase Server using the Terminal.

1. Download the appropriate package from the Couchbase [downloads page](https://www.couchbase.com/downloads).  
Couchbase Server for macOS is packaged as a standalone application in a compressed disk image.
2. Mount the the downloaded `.dmg` file.  
```console  
hdiutil attach couchbase-download.dmg  
```  
The image will mount a volume in containing the `Couchbase Server.app` application file.
3. Copy the `Couchbase Server.app` file into the system `/Applications` folder.  
```console  
cp -R /Volumes/volume-name/Couchbase\ Server.app /Applications  
```
4. Remove the Gatekeeper [quarantine flag](https://en.wikipedia.org/wiki/Gatekeeper%5F%28macOS%29#Quarantine) from `Couchbase Server.app`.  
```console  
sudo xattr -d -r com.apple.quarantine /Applications/Couchbase\ Server.app  
```
5. Start Couchbase Server.  
```console  
open -a Couchbase\ Server.app  
```  
Couchbase Server runs as a background application. When Couchbase Server starts, the Couchbase Server icon ![Couchbase Server menu bar icon](_images/macos-menu-bar-icon-light.png) will appear in the menu bar of the macOS UI.
6. Open a web browser and access the Couchbase Web Console to [verify](testing.md) that the installation was successful and the node is available.

Although the Couchbase Server software resides in the `/Applications` folder, the Couchbase data files are stored in other folders. For more information, refer to [Uninstalling Couchbase Server](install-uninstalling.md).

## [](#accessing-the-cli-tools)Accessing the CLI Tools

On macOS, the Couchbase Server command line interface (CLI) tools are included in the `Couchbase Server.app` application directory:

/Applications/Couchbase\ Server.app/Contents/Resources/couchbase-core/bin

To browse the commands in Finder, right-click on `Couchbase Server.app`, select **Show Package Contents**, and then go to `/Contents/Resources/couchbase-core/bin`.

## [](#next-steps)Next Steps

Following installation and start-up of Couchbase Server, a node must be _initialized_ and _provisioned_.

* If it is the first node in a deployment, initialization and provisioning happens all at once when you create a _cluster of one_.  
Refer to [Create a Cluster](../manage/manage-nodes/create-cluster.md)
* If you already have an existing cluster, the node is initialized and provisioned when you add it to the cluster.  
Refer to [Add a Node and Rebalance](../manage/manage-nodes/add-node-and-rebalance.md)
* Optionally, initialization can be performed explicitly and independently of provisioning, as a prior process, in order to establish certain configurations, such as custom disk-paths.  
Refer to [Initialize a Node](../manage/manage-nodes/initialize-node.md)