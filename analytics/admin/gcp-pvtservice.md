[View original HTML](/analytics/admin/gcp-pvtservice.html)

|  | Limited availabilityAdding a GCP Private Service Connection is available only on request. For more information, [contact Couchbase Support](../../cloud/support/manage-support.md#create-support-ticket). |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

> Add a Google Coud Platform (GCP) Private Service Connection that peers your GCP network with a Capella Analytics cluster using GCP as its cloud provider. This connection can reduce latency and egress costs for applications hosted in the same region. 

GCP Private Service Connections do not support [Prometheus metrics](../metrics-reference/metrics-reference.md). If you require Prometheus metrics, use [VPC Peering](create%5Fvpc%5Fpeering%5Fconnection.md).

## [](#prerequisites)Prerequisites

To use [GCP Private Service Connect](https://cloud.google.com/vpc/docs/private-service-connect) with Capella Analytics, you need:

* A project in your organization.  
For more information about projects in Capella Analytics, see [Projects Overview](../../cloud/projects/projects.md).
* The [Project Owner](../../cloud/projects/project-roles.md#project-owner-role) role assigned to your user account.
* A cluster in your project with GCP as its cloud provider and the region set to the same region as your GCP VPC. This cluster must use the **Developer Pro** or **Enterprise** plan.

|  | You cannot have more than 3 GCP clusters with private endpoints enabled in the same region. Additionally, in an organization, you cannot have more than 6 GCP clusters with private endpoints enabled. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
* Information about your GCP VPC, including:

  * The **Network** name.
  * The **Subnetwork** name.
* A BASH-like shell environment with the [Google Cloud Command Line Interface (CLI)](https://cloud.google.com/sdk/docs/install) installed and configured.

## [](#procedure)Procedure

To add a GCP Private Service Connection, you need the Capella Analytics UI and the Google Cloud CLI.

1. In Capella Analytics, enable private endpoints:

|  | Enabling private endpoints bills your account hourly for GCP Private Service Connect unless you turn off this option. As this feature is resource-intensive, it can result in increased costs. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

  1. Open the cluster where you want to add a GCP Private Service Connection.
  2. Go to **Settings** **Private Endpoints**.
  3. Click **Enable Private Endpoints Services**.  
  It can take 10 or more minutes for Capella Analytics to enable private endpoints. You can leave and return to the **Private Endpoints** page at any time.
2. Click **Add Private Endpoint**.
3. In the **Provide Private Endpoint Details** section, add the following information about your GCP network:

| Field                | Value                                                          |
| -------------------- | -------------------------------------------------------------- |
| Virtual Network Name | Enter the GCP network name.                                    |
| Subnet Name          | Enter the GCP subnet name. Your VM must reside in this subnet. |
4. Click **Next**.
5. Download and run the configuration shell script provided by Capella Analytics.

|  | If you add a subnet to your network after completing this procedure in GCP, you must re-run the configuration shell script to provision all the required resources in your network. |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |  
This script contains commands to create the required related resources in your chosen GCP network, including 50 endpoints for each subnet in your VPC. When successful, the provisioning details are output. It can take several minutes for this script to complete.
6. Once complete, verify the creation of the related endpoints by visiting Private Service Connect in the Google Cloud Console. These endpoints show a **Pending** status until you accept the connection.
7. In Capella Analytics, enter the `gcp-project-id` for your project and accept the connection.  
The acceptance process takes several minutes when you accept a connection to your project for the first time.

|  | When connecting an SDK to a cluster with a GCP Private Service Connection, you must add ?network=external to the end of the private endpoint in the connection string. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

### [](#verifying-the-connection)Verifying the Connection

To verify that the connection is complete:

* In Capella Analytics, open the **Private Endpoints** page and review the connection status for the new private endpoint.
* In the GCP console, check that the endpoints for this new Private Server Connection show an **Accepted** status.

### [](#disable-private-endpoints)Disable Private Endpoints

Disabling private endpoints deletes all private endpoints in a cluster. At the bottom of the **Private Endpoints** page, turn off private endpoints for your cluster by clicking **Disable Private Endpoints**.

It can take several minutes for Capella Analytics to complete this process.

|  | Disabling private endpoints only cleans up the infrastructure deployed in Capella Analytics. You must manually clean up any resources deployed to your GCP VPC that were supporting private endpoints. Do not remove GCP resources until the disabling process in Capella Analytics is complete. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |