---
title: Create a VNet Peering Connection with Azure
description: Use this procedure to create a VNet Peering connection between
  Capella hosted with Azure and your application's VNet on Azure.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clouds/pages/vpc-peering/peer-azure.adoc
pubDate: 2026-06-24T05:48:50.601Z
link: xref:cloud:clouds:vpc-peering/peer-azure.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/clouds/vpc-peering/peer-azure.html)

# Create a VNet Peering Connection with Azure

> Use this procedure to create a VNet Peering connection between Capella hosted with Azure and your application's VNet on Azure. 

## [](#prerequisites)Prerequisites

To configure Couchbase Capella VNet peering with Microsoft Azure, you need:

* An Azure user with 1 of the following roles:

  * [Global Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-administrator)
  * [Cloud Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#cloud-application-administrator)
  * [Application Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#application-administrator)
* 1 of the following Capella roles:

  * [Organization Owner](../../organizations/organization-user-roles.md#organization-role-organization-owner)
  * [Project Owner](../../projects/project-roles.md#project-owner-role)
* The [Azure Command Line Interface (CLI)](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) installed and configured.

## [](#procedure)Procedure

1. In Capella, start the VNet peering configuration:

  1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

    1. Click your organization name and go to **Operational**.
    2. Click your current project name or search for a project and go to **Operational**.
    3. Expand the cluster breadcrumb and search for a cluster.
  2. Select the cluster where you want to configure VNet peering.
  3. Go to **Settings** **VNet Peering**.
  4. Click **Setup VNet Peering**.
2. Confirm that you have a user with the [Global Administrator Role](https://learn.microsoft.com/en-us/azure/active-directory/roles/permissions-reference#global-administrator).
3. Add your Azure configuration details to allow peering access:  
Azure Tenant ID  
Enter your tenant ID. To find your tenant ID, see [How to find your Azure Active Directory tenant ID](https://learn.microsoft.com/en-us/azure/active-directory/fundamentals/active-directory-how-to-find-tenant).  
Azure Subscription ID  
Enter your subscription ID. To find your subscription ID, see [Find your Azure subscription](https://learn.microsoft.com/en-us/azure/azure-portal/get-subscription-tenant-id#find-your-azure-subscription).  
Resource Group Name  
Enter the resource group name holding the resource you're connecting with Capella.  
Virtual Network Name  
Enter the name of the virtual network in Azure.
4. Click **Allow Peering Access**.  
A new browser tab opens. Sign in to Azure if you have not already.
5. In Azure, accept Capella's permissions request:  
The Azure permissions request page is open in the new browser tab. Make a note of the application name and consent to the new permissions request. Consenting to this permission request creates a service principal that grants Capella access to the Azure tenant to perform VNet peering.  
> [!NOTE]  
> If you previously set up VNet peering with the same Azure tenant, you wont see the permissions request page as you already granted permission.  
On accepting the new permission, you automatically return to the Capella VNet peering page. The Capella VNet peering page shows a notice indicating that peering access is successful.
6. In Capella, add the **Enterprise Application Object ID**:  
With consent now granted, find and add the enterprise application object ID for the Capella service principal. You can find the enterprise application object ID in Azure by selecting **Azure Active Directory** **Enterprise applications**. Next, select the application name—​the same name shown when accepting the Azure permissions request. The object ID is in the **Object ID** box.
7. Click **Next**.
8. Copy the role assignment command on this page and run it using Azure CLI.  
This command assigns a new network contributor role. It scopes only to your specified subscription and the virtual network within that subscription. On success, the details of the role assignment are output in JSON.
9. Provide network details:  
VNet Peering Name  
Enter a descriptive VNet peering name of your choice.  
CIDR Block  
> [!CAUTION]  
> The virtual network CIDR block cannot overlap the CIDR that the cluster uses.  
Enter the CIDR block from the virtual network that you created in Azure. You can find the CIDR block in Azure by viewing the page for the virtual network and selecting **Subnets**.
10. Click **Set Up VNet**.  
> [!CAUTION]  
> Do not refresh the browser while Capella configures the peering connection.  
Capella sets up the VNet peering connection, which can take several minutes. When successful, the new VNet peering connection is on the VNet peering list.

## [](#next-steps)Next Steps

* [Verify VPC Peering Connectivity](verify-troubleshoot.md)