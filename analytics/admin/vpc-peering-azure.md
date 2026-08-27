---
title: VNet Peering with Azure
description: Use this procedure to create a VNet Peering connection between
  Capella Analytics hosted on Azure and your application's virtual network on
  Azure.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/admin/pages/vpc-peering-azure.adoc
  xref: xref:analytics:admin:vpc-peering-azure.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/analytics/admin/vpc-peering-azure.html)

# VNet Peering with Azure

> Use this procedure to create a VNet Peering connection between Capella Analytics hosted on Azure and your application's virtual network on Azure. 

> [!NOTE]
> For the equivalent procedure in Capella Operational, see [Peer an Azure VNet](https://docs.couchbase.com/cloud/clouds/vpc-peering/peer-azure.html) in the Capella documentation.

## [](#prerequisites)Prerequisites

To configure Capella Analytics VNet peering with Azure, you need:

* A [Global Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-administrator) role in your Azure account to authorize the connection between the application and Capella Analytics.
* One of the following Capella Analytics roles:

  * [Organization Owner](../../cloud/organizations/organization-user-roles.md#organization-role-organization-owner)
  * [Project Owner](../../cloud/projects/project-roles.md#project-owner-role)
* The [Azure Command Line Interface (CLI)](https://learn.microsoft.com/en-us/cli/azure/) installed and configured.
* The following Azure network information:

  * Azure Tenant ID
  * Azure Subscription ID
  * Resource Group Name
  * Virtual Network Name

## [](#procedure)Procedure

Complete the following steps to set up VNet peering between Capella Analytics and your Azure virtual network.

### [](#step-1-start-peering-in-capella)Step 1: Start Peering in Capella

1. In the Capella UI, select the **Capella Analytics** tab and then select a cluster.
2. Select the **Settings** tab.
3. In the navigation pane, under **Networking**, click **VNet Peering**.
4. Click **Set Up VNet Peering**.
5. Review the prerequisites and confirm that you have a [Global Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-administrator) role in your Azure account, then click **Next**.

### [](#step-2-grant-capella-access-to-azure)Step 2: Grant Capella Access to Azure

1. In the **Azure Configuration Details** section, enter the following information to allow Capella to access your Azure account for peering:  
Azure Tenant ID  
Enter your Azure Tenant ID. To find your tenant ID, see [How to find your Microsoft Entra tenant ID](https://learn.microsoft.com/en-us/entra/fundamentals/how-to-find-tenant) in the Azure documentation.  
Azure Subscription ID  
Enter your Azure Subscription ID. To find your subscription ID, see [Get subscription and tenant IDs in the Azure portal](https://learn.microsoft.com/en-us/azure/azure-portal/get-subscription-tenant-id) in the Azure documentation.  
Resource Group Name  
Enter the name of the Azure resource group that holds the virtual network you're connecting with Capella.  
Virtual Network Name  
Enter the name of the target virtual network in Azure.
2. Click **Allow Peering Access**.  
A new browser tab opens. Sign in to Azure if you have not already, then accept Capella's permissions request.  
After accepting the permissions, you're automatically returned to the Capella VNet Peering page. A notice confirms that peering access was successful, and the **Enterprise Application Object ID** is displayed.  
> [!NOTE]  
> You can also find this ID in the Azure portal by navigating to **Microsoft Entra ID** \> **Enterprise applications** and selecting the Capella application name. The object ID is in the **Object ID** box.

### [](#step-3-assign-the-network-contributor-role)Step 3: Assign the Network Contributor Role

To allow Capella to configure the peering connection, you must grant it permissions within your Azure environment.

1. On the Capella VNet Peering page, copy the provided Azure CLI command.
2. Open your terminal and run the command using the Azure CLI.  
This command assigns the [Network Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles/networking#network-contributor) role to the Capella enterprise application on your virtual network, which allows Capella to configure the peering connection.

### [](#step-4-finalize-network-details-in-capella)Step 4: Finalize Network Details in Capella

1. In the **Provide Network Details** section, enter the following information:  
VNet Peering Name  
Enter a descriptive name for the VNet peering connection.  
CIDR Block  
Enter the CIDR block from the virtual network you created in Azure.  
> [!CAUTION]  
> This value cannot overlap with your Capella CIDR block.
2. Click **Set Up VNet Peering**.  
Capella Analytics sets up the peering connection. If successful, the new peering connection appears in the list of VNet peering connections.

## [](#next-steps)Next Steps

After VNet Peering is set up, your applications in the peered Azure virtual network can access your Capella Analytics cluster over the private network.

To verify the connection, navigate to **Settings** **VNet Peering** and confirm the peering connection shows a **Complete** status.

For more information about VNet Peering in the Azure environment, see [Virtual network peering](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-network-peering-overview) in the Azure documentation.