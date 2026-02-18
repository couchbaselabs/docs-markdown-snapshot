---
title: Add an Azure Private Link Connection
description: Add an Azure Private Link connection that peers your Azure network
  with a Capella cluster using Azure as its cloud provider. This connection can
  reduce latency and egress costs for applications hosted in the same region.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/security/pages/add-azure-private-link.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/cloud/security/add-azure-private-link.html)

# Add an Azure Private Link Connection

> Add an Azure Private Link connection that peers your Azure network with a Capella cluster using Azure as its cloud provider. This connection can reduce latency and egress costs for applications hosted in the same region. 

> [!IMPORTANT]
> Azure Private Link connections do not support [cross data center replication (XDCR)](../clusters/xdcr/xdcr.md) or [Prometheus metrics](../clusters/monitoring/prometheus.md). If you require XDCR or Prometheus metrics, use [VPC Peering](../clouds/private-network.md).

## [](#prerequisites)Prerequisites

To add an [Azure Private Link](https://learn.microsoft.com/en-us/azure/private-link/private-link-overview) connection, you need:

* The [Project Owner](../projects/project-roles.md#project-owner-role) role assigned to your user account.
* A project in your organization.  
For more information about projects in Capella, see [Projects Overview](../projects/projects.md).
* A cluster in your project with:

  * Microsoft Azure as its cloud provider.
  * The **Developer Pro** or **Enterprise** Support Plan.  
For more information about how to create a cluster, see [Create A Paid Cluster](../clusters/create-database.md).
* Information about your Azure network:

  * The Azure **Resource Group** name.
  * The Azure **Virtual Network/Subnet** name.
* A BASH-like shell.
* The [Azure Command-Line Interface (CLI)](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) installed and configured.
* When configuring firewalls for Couchbase Capella and an Azure Private Link connection, open and allow traffic through port ranges `18091-18203` and `11207-11308`. These port ranges are consistent across the cloud service providers that Capella supports.

> [!TIP]
> The Microsoft Azure portal can also help you monitor your progress and find resource information.

## [](#procedure)Procedure

To add an Azure Private Link connection, you need to:

1. [Enable private endpoints](#enable-pe).
2. [Add a private endpoint](#add-pe).
3. [Verify the connection](#verify-connection).

To get started, open the Capella UI and the Azure CLI.

### [](#enable-pe)Enable Private Endpoints

In Capella, enable Private Endpoints:

> [!NOTE]
> Enabling Private Endpoints bills your account hourly for Azure Private Link until you turn off this option.

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**. Select the cluster where you want to add an Azure Private Link connection.
  2. Click your current project name or search for a project and go to **Operational**. Select the cluster where you want to add an Azure Private Link connection.
  3. Expand the cluster breadcrumb and search for or select a cluster where you want to add an Azure Private Link connection.
2. Go to **Settings** **Private Endpoints**.
3. Click **Enable Private Endpoint Service**.  
It can take several minutes for Capella to enable private endpoints. When private endpoints are available, the page shows all the controls you need to manage private endpoints in Capella. You can leave and return to the **Private Endpoints** page at any time.

### [](#add-pe)Add a Private Endpoint

To add a private endpoint:

1. Click **Add Private Endpoint**.
2. In the **Provide Private Endpoint Details** section, add the following information:

| Field                  | Value                                                                                                        |
| ---------------------- | ------------------------------------------------------------------------------------------------------------ |
| Resource Group Name    | Enter your Azure resource group name                                                                         |
| Virtual Network/Subnet | Enter your Azure virtual network and subnet in the following format: example-virtual-network/default-subnet. |
3. Click **Next**.
4. Download and run the shell script provided by Capella:  
> [!NOTE]  
> This script is only compatible with BASH-like shells.

  1. In the **Run the following script** area, click **Download Script**.
  2. With Azure CLI installed and signed in, run the downloaded script in your terminal.  
  This script contains commands to create the private endpoint and related resources in your chosen Azure resource group. When successful, the provisioning details are output. It can take a few minutes to complete.
5. In Capella, the new interface endpoint is now shown and has a **Pending Acceptance** status. Click **Accept**.  
Returning to the **Private Endpoints** page in Capella, the new private endpoint shows a **Linked** status once the connection is accepted. This process can take a few minutes.

### [](#verify-connection)Verify the Connection

You can verify this connection in the Azure portal by opening the private endpoint resource. The overview page shows an **Approved** connection status when the configuration is successful.