---
title: Add a GCP Private Service Connection
description: Add a GCP Private Service Connection that connects your GCP network
  with a Capella cluster using GCP as its cloud provider. This connection can
  reduce latency and egress costs for applications hosted in the same region.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/security/pages/add-gcp-private-link.adoc
  xref: xref:cloud:security:add-gcp-private-link.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/security/add-gcp-private-link.html)

# Add a GCP Private Service Connection

> Add a GCP Private Service Connection that connects your GCP network with a Capella cluster using GCP as its cloud provider. This connection can reduce latency and egress costs for applications hosted in the same region. 

> [!IMPORTANT]
> XDCR and Prometheus Metrics
> 
> GCP Private Service Connections can support [Cross Datacenter Replication (XDCR)](../clusters/xdcr/xdcr.md) or [Prometheus metrics](../clusters/monitoring/prometheus.md). These features are only available upon request and are subject to specific conditions.
> 
> For more information about the XDCR conditions, see [Replicate Data Across a Private Endpoint Connection](../clusters/xdcr/manage-xdcr-security.md#private-endpoints). For more information about the Prometheus conditions, see [Prometheus metrics](../clusters/monitoring/prometheus.md).

## [](#prerequisites)Prerequisites

To use [GCP Private Service Connect](https://cloud.google.com/vpc/docs/private-service-connect) with Capella, you need:

* A project in your organization.  
For more information about projects in Capella, see [Projects Overview](../projects/projects.md).
* The [Project Owner](../projects/project-roles.md#project-owner-role) role assigned to your user account.
* A cluster in your project with:

  * GCP as its cloud provider.
  * The region set to the same region as your GCP VPC.
  * The **Developer Pro** or **Enterprise** plan.
* Information about your GCP VPC, including:

  * The **Network** name.
  * The **Subnetwork** name.
* 1 of the following:

  * A BASH-like shell environment with the [Google Cloud Command Line Interface (CLI)](https://cloud.google.com/sdk/docs/install) installed and configured.
  * The Terraform command-line tool downloaded and installed. For more information, see the [Install Terraform Documentation](https://developer.hashicorp.com/terraform/downloads).

> [!NOTE]
> Couchbase Capella automatically manages load balancers for each node in GCP. You do not need to open ports for GCP when configuring a firewall.

## [](#procedure)Procedure

To add a GCP Private Service Connection, you need to:

1. [Enable private endpoints](#enable-pe).
2. [Add a private endpoint](#add-pe).
3. [Verify the connection](#verify-connection).

To get started, open the Capella UI and the Google Cloud CLI or Google Terraform Provider.

### [](#enable-pe)Enable Private Endpoints

In Capella, enable Private Endpoints:

> [!IMPORTANT]
> Enabling private endpoints bills your account hourly for GCP Private Service Connect until you turn off this option. As this feature is resource-intensive, it can result in increased costs.

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**. Select the cluster where you want to add a GCP Private Service Connection.
  2. Click your current project name or search for a project and go to **Operational**. Select the cluster where you want to add a GCP Private Service Connection.
  3. Expand the cluster breadcrumb and search for or select a cluster where you want to add a GCP Private Service Connection.
2. Go to **Settings** **Private Endpoints**.
3. Click **Enable Private Endpoint Service**.  
It can take several minutes for Capella to enable private endpoints. When private endpoints are available, the page shows all the controls you need to manage private endpoints in Capella. You can leave and return to the **Private Endpoints** page at any time.

### [](#add-pe)Add a Private Endpoint

To add a private endpoint:

1. Click **Add Private Endpoint**.
2. In the **Provide Private Endpoint Details** section, add the following information about your GCP network:

| Field                      | Value                                                          |
| -------------------------- | -------------------------------------------------------------- |
| Virtual Private Cloud Name | Enter the GCP network name.                                    |
| Subnet Name                | Enter the GCP subnet name. Your VM must reside in this subnet. |
3. Click **Next**.
4. Choose 1 of the following options:

  * Shell Script
  * Google Terraform Provider  
Use a shell script to create the private endpoint:

  1. Download and run the configuration shell script provided by Capella.  
  This script contains commands to create the required related resources in your chosen GCP network. When successful, the provisioning details are output. It can take several minutes for this script to complete.  
  > [!CAUTION]  
  > If you add a subnet to your network after completing this procedure in GCP, you must re-run the configuration shell script to provision all the required resources in your network.  
Use Google Terraform Provider commands to create the private endpoint:  
> [!NOTE]  
> The Google Terraform configuration files are not available for download through Capella.

  1. Create 2 Terraform configuration files:

    1. A `variables.tfvars` file to assign values to the input variables.
    2. A `main.tf` file to define the input variables and create the related resources.
  2. Copy the following variables in your `variables.tfvars` file. Update the values to match your environment, then save the file.  
  ```tfvars  
  project                      = "YOUR_PROJECT_NAME"  
  region                       = "YOUR_REGION"  
  network                      = "YOUR_VPC_NETWORK_NAME"  
  subnet                       = "YOUR_SUBNET_NAME"  
  cluster                      = "YOUR_CLUSTER_ID"  
  base_dns_name                = "YOUR_BASE_DNS_NAME."  #Include the trailing period ( . )  
  service_attachment           = "SERVICE_ATTACHMENT_URI"  
  bootstrap_service_attachment = "BOOTSTRAP_SERVICE_ATTACHMENT_URI"  
  ```  
  > [!TIP]  
  > You can download the `script.sh` configuration shell script provided through Capella and use it as a reference for these value inputs.
  3. Copy and save the following Terraform configuration into your `main.tf` file. Do not make any modifications.  
  ```tf  
  terraform {  
    required_providers {  
      google = {  
        source  = "hashicorp/google"  
        version = ">= 6.38.0"  
      }  
    }  
  }  
  provider "google" {  
    project = var.project  
    region  = var.region  
  }  
  variable "project" {}  
  variable "region" {}  
  variable "network" {}  
  variable "subnet" {}  
  variable "cluster" {}  
  variable "base_dns_name" {}  
  variable "service_attachment" {}  
  variable "bootstrap_service_attachment" {}  
  locals {  
    network_short = substr(var.network, 0, 15)  
    cluster_short = substr(var.cluster, 0, 15)  
    zone_name     = "${local.network_short}-${local.cluster_short}"  
  }  
  resource "google_compute_address" "pe" {  
    name         = "pe-address-${local.zone_name}"  
    region       = var.region  
    subnetwork   = var.subnet  
    address_type = "INTERNAL"  
    purpose      = "GCE_ENDPOINT"  
  }  
  resource "google_compute_address" "bootstrap" {  
    name         = "pe-address-bootstrap-${local.zone_name}"  
    region       = var.region  
    subnetwork   = var.subnet  
    address_type = "INTERNAL"  
    purpose      = "GCE_ENDPOINT"  
  }  
  resource "google_compute_forwarding_rule" "pe" {  
    name       = "endpoint-${local.zone_name}"  
    region     = var.region  
    network    = var.network  
    ip_address = google_compute_address.pe.self_link  
    target     = var.service_attachment  
    load_balancing_scheme = ""  
  }  
  resource "google_compute_forwarding_rule" "bootstrap" {  
    name       = "endpoint-bootstrap-${local.zone_name}"  
    region     = var.region  
    network    = var.network  
    ip_address = google_compute_address.bootstrap.self_link  
    target     = var.bootstrap_service_attachment  
    load_balancing_scheme = ""  
  }  
  resource "google_dns_managed_zone" "pe_zone" {  
    name        = local.zone_name  
    dns_name    = var.base_dns_name  
    description = "Private Endpoint for Capella cluster"  
    visibility  = "private"  
    private_visibility_config {  
      networks {  
        network_url = "projects/${var.project}/global/networks/${var.network}"  
      }  
    }  
  }  
  resource "google_dns_record_set" "pe" {  
    name         = "pe.${var.base_dns_name}"  
    type         = "A"  
    ttl          = 300  
    managed_zone = google_dns_managed_zone.pe_zone.name  
    rrdatas      = [google_compute_address.pe.address]  
  }  
  resource "google_dns_record_set" "bootstrap" {  
    name         = "private-endpoint.${var.base_dns_name}"  
    type         = "A"  
    ttl          = 300  
    managed_zone = google_dns_managed_zone.pe_zone.name  
    rrdatas      = [google_compute_address.bootstrap.address]  
  }  
  ```
  4. Run the Google Terraform Provider commands:

    1. Initialize Terraform to set up your configuration:  
      ```console  
      terraform init  
      ```
    2. Review the Terraform plan to see what changes will be made to the private endpoint:  
      ```console  
      terraform plan -var-file="variables.tfvars" -out=tfplan  
      ```
    3. Apply the Terraform configuration to create the private endpoint:  
      ```console  
      terraform apply "tfplan"  
      ```
5. Once complete, verify the creation of the related endpoints by visiting Private Service Connect in the Google Cloud Console. These endpoints show a **Pending** status until you accept the connection.
6. In Capella, enter the `gcp-project-id` for your project and accept the connection.  
The acceptance process takes several minutes when you accept a connection to your project for the first time.

> [!IMPORTANT]
> When connecting an SDK to a cluster with a GCP Private Service Connection, you must add `?network=external` to the end of the private endpoint in the connection string.
> 
> For example, `couchbases://private-endpoint.<RANDOM>.cloud.couchbase.com?network=external`.
> 
> This is only required for Java, Scala, Kotlin, C++, Node.js, Python, Ruby, and PHP SDKs.

### [](#verify-connection)Verify the Connection

To verify that the connection is complete:

* In Capella, open the **Private Endpoints** page and review the connection status for the new private endpoint.
* In the GCP console, check that the endpoints for this new Private Server Connection show an **Accepted** status.

### [](#disable-private-endpoints)Disable Private Endpoints

Disabling private endpoints deletes all private endpoints in a cluster. At the bottom of the **Private Endpoints** page, turn off private endpoints for your cluster by clicking **Disable Private Endpoints**.

It can take several minutes for Capella to complete this process.

> [!CAUTION]
> Disabling private endpoints only cleans up the infrastructure deployed in Capella. You must manually clean up any resources deployed to your GCP VPC that were supporting private endpoints.
> 
> Do not remove GCP resources until the disabling process in Capella is complete.

#### [](#delete-private-endpoints-with-terraform)Delete Private Endpoints with Terraform

If you want to delete the private endpoint infrastructure with Google Terraform Provider, run the command:

```console
terraform destroy -var-file="variables.tfvars"
```