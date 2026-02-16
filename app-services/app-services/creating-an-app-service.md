[View original HTML](/app-services/app-services/creating-an-app-service.html)

> Using the Capella UI, you can create an App Service for your mobile apps to connect to. 

App Services are available on [AWS](#reference:aws.adoc), [GCP](#reference:gcp.adoc), and [Azure](#reference:azure.adoc), in supported regions.

## [](#prerequisites)Prerequisites

The cluster connected to the App Service:

* MUST have Data, Index, and Query services running.
* Must NOT yet have an App Service linked to it.
* Must NOT have XDCR with another Cluster.
* You must set the Sync Gateway bucket durability setting to `None` as Sync Gateway does not support non-default [durability settings](../../server/current/learn/data/durability.md).
* The Sync Gateway `maxTTL` value must be set to `0` as Sync Gateway does not support bucket-level non-zero `maxTTL` values.

You may subsequently enable XDCR on clusters linked with App Services, as long as:

* You’re setting up unidirectional XDCR between the clusters.
* The other cluster does not have App Services linked to it.

## [](#basics)Create an App Service with Basic Settings

To create an App Service with default deployment configuration:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name or expand and select the organization where you want to work with App Services.
  2. Click your current project name or search for the project where you want to work with App Services.
2. Go to **App Services**.
3. Select your App Service from the list.
4. Go to **App Endpoint**.
5. Click **Create App Endpoint**.
6. Click the **Create App Service** button.
7. Enter a name for the App Service.
8. Choose the cluster you want to connect to.
9. Click the **Create App Service** button to instantiate the service.

|  | Azure App Services deployments can take an average of 15-20 minutes. Deployments on AWS and GCP will take around 5 minutes. |
|  | --------------------------------------------------------------------------------------------------------------------------- |

## [](#deployment-configuration)Deployment Configuration

The provided default should be fine to get you started for development. According to your requirements, you may customize the following parameters:

App Service Nodes

Select the number of nodes, between 1 and 12; default 2.

Compute

Choose the size of each node. The options offered vary depending on which cloud service you have chosen for the cluster.

You can scale an application after it’s deployed by changing its configuration. For more information, see [Scale a Deployed App Service](scaling-a-deployed-app-service.md).

|  | If you want to connect App Services to a [Single Node cluster](../../cloud/clusters/databases.md#option), you can choose to deploy App Services on a single node. Single Node App Services only support the following Compute configurations: 2vCPU with 4 GB RAM 4vCPU with 8 GB RAM You cannot scale a Single Node App Service to add more nodes later. |
|  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#service-cluster-size-implications)Service Cluster Size Implications

When linking App Services to a cluster, bear in mind that an App Service generates some additional sync-related metadata documents during the normal course of its operation. The metadata is stored in the backing server bucket.

In addition to this, when you link App Services to a cluster, deleted documents ("tombstoned" documents) remain in the bucket for 60 days following the deletion. This provides the opportunity for disconnected clients to sync deleted documents through App Services when they come back online anytime within the 60-day partition window.

## [](#linked-database-plan)Linked Cluster Plan

When you deploy a new App Service, Capella confirms the plan selected for the linked cluster. The plan associated with App Services is the same as that of the linked cluster.

The summary shows the services costs separated between the cluster linked to the App Service and the App Service itself. The total cost of the deployment is also shown.

## [](#deletion-protection)App Services and Linked Cluster Deletion Protection

Cluster deletion protection also stops accidental deletion of an App Service from the Capella UI, the [Management API](../../cloud/management-api-reference/index.md#tag/App-Services/operation/deleteAppService), or any other external tools, such as Terraform. [Turn on deletion protection for your linked cluster](../../cloud/clusters/modify-database.md#deletion-protection) to automatically turn on deletion protection for your linked App Service.

You can change this setting even when you have [turned off an App Service](turn-on-off.md).

For more information about how to change deletion protection for your linked cluster, see [Change Your Deletion Protection](../../cloud/clusters/modify-database.md#deletion-protection). You cannot turn off deletion protection for your App Service independently of deletion protection for your cluster.

## [](#see-also)See Also

Learn more about [Billing of App Services](../billing/billing.md).