---
title: Azure Private Endpoint Connection
description: Add an Azure Private Link connection that peers your Azure network
  with a Capella Analytics cluster using Azure as its cloud provider.
editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/admin/pages/azure-private-endpoint.adoc
pubDate: 2026-07-20T13:54:32.914Z
link: xref:analytics:admin:azure-private-endpoint.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/analytics/admin/azure-private-endpoint.html)

# Azure Private Endpoint Connection

> Add an Azure Private Link connection that peers your Azure network with a Capella Analytics cluster using Azure as its cloud provider. 

This connection can reduce latency and egress costs for applications hosted in the same region.

## [](#prerequisites)Prerequisites

To use Azure Private Link with Capella Analytics, you need:

* One of the following Capella roles:

  * Organization Owner
  * Project Owner
* A Capella Analytics cluster on Azure in your project.
* Access to the [Azure portal](https://portal.azure.com) and information about your Azure network, including:

  * Azure Resource Group Name
  * Virtual Network and Subnet (in the format `<virtual-network-name>/<subnet-name>`)
* The [Azure Command Line Interface (CLI)](https://learn.microsoft.com/en-us/cli/azure/) installed and configured.

## [](#set-up-the-private-endpoint)Set Up the Private Endpoint

> [!NOTE]
> Enabling private endpoints bills your account hourly for Azure Private Link until you disable this option.

To add a connection using Azure Private Link, you use both the Capella UI and the Azure CLI.

1. In the Capella UI, select the **Capella Analytics** tab and then select a cluster.
2. Select **Settings** **Private Endpoints**.
3. Click **Enable Private Endpoints**.  
A warning modal explains that enabling this service is billed hourly. Confirm to proceed.  
It can take several minutes for Capella to enable private endpoints. When private endpoints are available, the page shows all the controls you need to manage private endpoints.
4. Click **Add Private Endpoint**.
5. In the **Provide Private Endpoint Details** section, complete the following fields:  
Resource Group Name  
Enter your Azure resource group name.  
Virtual Network/Subnet  
Enter your Azure virtual network and subnet in the following format:  
`<virtual-network-name>/<subnet-name>`  
For example: `example-virtual-network/default-subnet`
6. Click **Next**.
7. Download the connection shell script provided by Capella:

  1. In the **Run the following script** area, click **Download Script**.
  2. With the Azure CLI installed and signed in, run the downloaded script in your terminal.  
  This script contains commands to create the private endpoint and related resources in your chosen Azure resource group. The script can take a few minutes to complete. When successful, the provisioning details are output to the terminal.
8. In the Capella UI, the new private endpoint appears with a **Pending Acceptance** status. Click **Accept**.

## [](#next-steps)Next Steps

Returning to the **Private Endpoints** page in Capella Analytics, the new private endpoint shows a **Linked** status once the connection is accepted. This status change can take several minutes after completing the configuration procedure.

## [](#disable-private-endpoints)Disable Private Endpoints

To disable private endpoints, navigate to **Settings** **Private Endpoints**. The **Disable Private Endpoints** option appears only after private endpoints have been enabled.

> [!NOTE]
> Disabling private endpoints removes the Private Link Service from the Capella Analytics cluster and stops hourly billing for Azure Private Link.