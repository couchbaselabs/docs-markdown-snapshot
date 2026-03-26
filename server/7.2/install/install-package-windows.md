---
title: Install Couchbase Server on Windows
description: Couchbase Server can be installed on Windows Server for production
  use-cases, and Windows Desktop for development use-cases.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/install/pages/install-package-windows.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:7.2@server:install:install-package-windows.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/server/7.2/install/install-package-windows.html)

# Install Couchbase Server on Windows

> Couchbase Server can be installed on Windows Server for production use-cases, and Windows Desktop for development use-cases. 

Use the instructions on this page to install Couchbase Server on Windows platforms using Couchbase-provided MSI packages. The instructions support both Enterprise and Community [editions](https://www.couchbase.com/products/editions).

If you're upgrading an existing installation of Couchbase Server, refer to [Upgrading Couchbase Server](upgrade.md).

## [](#before-you-install)Before You Install

Couchbase Server works out-of-the-box with most OS configurations. However, the procedures on this page assume the following:

* You have _administrator privileges_. These are required, for installing Couchbase Server on Windows.
* Your system meets the [minimum requirements](pre-install.md) and that your operating system version is [supported](install-platforms.md).  
Windows Server is fully supported for production use-cases, while Windows Desktop is only supported for development use-cases.
* You're working from a clean system and that you've [uninstalled](install-uninstalling.md) any previous versions of Couchbase Server.  
If you're upgrading an existing installation of Couchbase Server, refer to [Upgrade](upgrade.md).
* You're not running any third-party anti-virus software during the installation process.
* The Windows 10 Universal CRT is installed.  
The Windows 10 Universal CRT is required to run Couchbase Server on Windows. This component is not included by default in versions of Windows earlier than Windows 10\. Make sure to download and install the [Update for Universal C Runtime in Windows](https://support.microsoft.com/en-us/help/2999226/update-for-universal-c-runtime-in-windows) if you are using one of these earlier versions of Windows.

For production deployments, make sure to follow the [Deployment Guidelines](install-production-deployment.md) so that your systems and environment are properly sized and configured before installation.

## [](#basic-installation)Basic Installation

Couchbase Server uses an interactive wizard, for basic installations on Windows systems. You must be logged into a local user account that has administrator privileges, in order to perform the installation. Proceed as follows:

1. Download the appropriate package from the Couchbase [downloads page](https://www.couchbase.com/downloads). Note that Couchbase Server for Windows is packaged in a standard MSI file.
2. In the **Type here to search** field, which is to the immediate right of the **Start** button, at the lower left of the screen, type `cmd`:  
![typeCmd](_images/typeCmd.png)
3. When the **Command Prompt** icon appears in the search results, right-click on it, to display the pull-down menu; then, select **Run as administrator**:  
![runAsAdmin](_images/runAsAdmin.png)  
Next, a dialog appears, asking whether you wish to allow the **Windows Command Processor** to make changes to your system. Click **Yes**, on the dialog.
4. The **Command Prompt** now appears. Against the prompt, change directory to **Downloads**, by entering the following command.  
```shell  
cd C:\Users\customer\Downloads  
```
5. Start the Couchbase-Server install wizard; by using the `call` command, and specifying the `.msi` file that you have downloaded:  
```shell  
call couchbase-server-enterprise_7.1.0-windows_amd64.msi  
```  
The install wizard now appears:  
![wizardScreen](_images/wizardScreen.png)
6. On the initial, **Welcome** screen of the install wizard, click **Next**; to start configuring the installation.
7. On the License Agreement screen, make sure to read the entire End-User License Agreement.  
If you accept the license agreement, check the box next to **I accept the terms in the License Agreement**.  
Click **Next** to continue.
8. On the Destination Folder screen, choose the folder where you want the Couchbase Server application to be installed.  
You can change the folder by clicking the **Change…​** button, or click **Next** to use the default folder.  
> [!NOTE]  
> The destination folder will only contain the Couchbase Server application. Couchbase Server stores database files and other persistent data in `C:\Program Files\Couchbase`.
9. Enterprise Edition: On the IP Version Selection screen, you can choose to configure Couchbase Server to use IPv6.  
Unless you're sure that you need to use IPv6, you should keep the default configuration (IPv4). Refer to the [IPv6 documentation](../manage/manage-nodes/manage-address-families.md) for more information.  
Click **Next** to continue.
10. Once you're ready, click **Install** to begin the installation.  
Some parts of the installation may cause Windows User Account Control to prompt for your explicit permission to install certain components. These are required components, so you must click **Yes** in order to successfully complete the installation.
11. Once the installation completes, a web browser and access the Couchbase Web Console to [verify](testing.md) that the installation was successful and that the node is available.

## [](#unattended-installation)Unattended Installation

If you need to install Couchbase Server using the command line, you can perform an unattended installation (also known as a silent or headless installation). For a completely unattended installation, you must run each command from an Administrator command prompt.

1. Download the appropriate package from the Couchbase [downloads page](https://www.couchbase.com/downloads).  
Couchbase Server for Windows is packaged in a standard MSI file.
2. Install Couchbase Server.  
To install Couchbase Server in the default directory:  
```console  
start /wait msiexec /i package-name.msi /qn  
```  
To install Couchbase Server to a non-standard directory:  
```console  
start /wait msiexec /i package-name.msi /qn INSTALLDIR=C:\ my-install-dir  
```  
> [!NOTE]  
> If you don't prepend `start /wait` to the command, `msiexec` immediately returns control to the command prompt and doesn't wait for the installation to complete or report any errors. In this case, you may have to wait a minute or two for the actual installation to complete.
3. Once the installation completes, a web browser and access the Couchbase Web Console to [verify](testing.md) that the installation was successful and that the node is available.

## [](#next-steps)Next Steps

Following installation and start-up of Couchbase Server, a node must be _initialized_ and _provisioned_.

* If it is the first node in a deployment, initialization and provisioning happens all at once when you create a _cluster of one_.  
Refer to [Create a Cluster](../manage/manage-nodes/create-cluster.md)
* If you already have an existing cluster, the node is initialized and provisioned when you add it to the cluster.  
Refer to [Add a Node and Rebalance](../manage/manage-nodes/add-node-and-rebalance.md)
* Optionally, initialization can be performed explicitly and independently of provisioning, as a prior process, in order to establish certain configurations, such as custom disk-paths.  
Refer to [Initialize a Node](../manage/manage-nodes/initialize-node.md)