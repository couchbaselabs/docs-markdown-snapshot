---
title: Deploy Couchbase Server Using GCP Marketplace
description: Couchbase partners with Google to provide a packaged solution on
  GCP Marketplace.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/cloud/pages/couchbase-gcp-cloud-launcher.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/cloud/couchbase-gcp-cloud-launcher.html)

# Deploy Couchbase Server Using GCP Marketplace

> Couchbase partners with Google to provide a packaged solution on GCP Marketplace. This solution is based on Google Deployment Manager templates that incorporate the latest features and best practices for deploying Couchbase Server on Google Cloud Platform. 

Couchbase Server on GCP Marketplace provides one of the fastest and easiest ways to get up and running on Google Cloud Platform. Google Deployment Manager templates are developed in close collaboration with Google in order to adopt the latest features and best practices. These templates leverage Google’s globally flat network for extremely secure geographical replication.

Couchbase is available through GCP Marketplace with hourly pricing, or through a Bring Your Own License (BYOL) model.

## [](#before-you-begin)Before You Begin

* You need a Google account with access to Google Cloud Platform. If you don’t have one, [sign up](https://console.cloud.google.com/getting-started) for one before proceeding.
* You should review the [best practices](couchbase-cloud-deployment.md#gcp-best-practices) for deploying Couchbase Server on GCP.  
> [!NOTE]  
> The free trial version of GCP has limits on the number of resources that can be be deployed. You can proactively request quota adjustments from the [Quotas](https://console.cloud.google.com/projectselector/iam-admin/quotas) page in the Cloud Platform Console.

## [](#deploying-couchbase-enterprise)Deploying Couchbase Enterprise

> [!IMPORTANT]
> The templates are provided as a starting point and may be customized as needed. Note that additional post deployment setup may be required.

1. Log in to your Google Cloud Platform account and navigate to the Google Cloud Launcher page for [Couchbase Enterprise Edition](https://console.cloud.google.com/launcher/details/couchbase-public/couchbase-enterprise-edition). If you wish to bring your own license, navigate to [Couchbase Enterprise Editon - BYOL](https://console.cloud.google.com/launcher/details/couchbase-public/couchbase-enterprise-edition-byol) instead.  
![gcp cloud launcher couchbase enterprise](_images/gcp/deploying/gcp-cloud-launcher-couchbase-enterprise.png)
2. Click **Launch on Compute Engine**. On the **New Couchbase Enterprise Edition deployment** screen, configure the VM settings.  
![gcp new couchbase ee deploy config regions](_images/gcp/deploying/gcp-new-couchbase-ee-deploy-config-regions.png)  
![gcp new couchbase ee deploy config vm](_images/gcp/deploying/gcp-new-couchbase-ee-deploy-config-vm.png)  

| Field Name                                    | Description                                                                                                                                                                                                                                               |
| --------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Deployment name                               | Provide a deployment name. We recommend using a shorter name as the deployment name has a character limit and the template will truncate longer names automatically.                                                                                      |
| Regions                                       | Google Cloud Platform has a wide range of locations available. Pick a location where you want your cluster to be deployed.                                                                                                                                |
| Couchbase Server                              |                                                                                                                                                                                                                                                           |
| Couchbase Server Node Count                   | Enter the number of Server Nodes to deploy.                                                                                                                                                                                                               |
| Couchbase Server Node Type                    | Select the machine type for your server nodes. You can choose to customize your machine type using the Customize link.                                                                                                                                    |
| Couchbase Server pd-ssd disk size in GB       | Enter the disk size for each of the server nodes.                                                                                                                                                                                                         |
| Couchbase Server Version                      | Choose the Couchbase Server version to deploy. The [Compatibility Matrix](https://developer.couchbase.com/documentation/mobile/current/installation/index.html#story-h2-1) summarizes the compatible versions of Sync Gateway and Couchbase Server.       |
| Couchbase Sync Gateway                        |                                                                                                                                                                                                                                                           |
| Couchbase Sync Gateway Node Count             | Enter the number of Sync Gateway Nodes to deploy.                                                                                                                                                                                                         |
| Couchbase Sync Gateway Node Type              | Select the machine type for your sync gateway nodes. You can choose to customize your machine type using the Customize link.                                                                                                                              |
| Couchbase Sync Gateway pd-ssd disk size in GB | Enter the disk size for each of the sync gateway nodes.                                                                                                                                                                                                   |
| Couchbase Sync Gateway Version                | Choose the Couchbase Sync Gateway version to deploy. The [Compatibility Matrix](https://developer.couchbase.com/documentation/mobile/current/installation/index.html#story-h2-1) summarizes the compatible versions of Sync Gateway and Couchbase Server. |
3. Click Deploy. Deployment begins and you will be redirected to the Deployment Manager where the deployment status is displayed.  
![gcp new couchbase ee deploy inprogress](_images/gcp/deploying/gcp-new-couchbase-ee-deploy-inprogress.png)
4. You should see a green check mark once deployment completes successfully.  
> [!IMPORTANT]  
> Note the Couchbase Username and Password displayed on the screen.  
![gcp new couchbase ee deploy done](_images/gcp/deploying/gcp-new-couchbase-ee-deploy-done.png)

That’s it! It may take a short while for Couchbase to be up and running.

At this point a number of Instance Group Managers have been deployed. It may take several minutes for the VMs that the Instance Group Managers manage to start, and for their start-up scripts to complete installing and configuring Couchbase.

## [](#logging-in)Logging in to Your Couchbase Cluster

You can log in to the Couchbase cluster and explore the items created.

1. To inspect the resources that have been deployed and log in to Couchbase Server:

  1. Click the Products & services icon ![gcp icon prdt services](_images/gcp/deploying/gcp-icon-prdt-services.png) at the top left of the screen to pull down the sidebar and select **Compute Engine** \> **Instance Groups**. You can see a list of all the Instance groups being deployed. Depending on how quickly you get to this step after starting deployment, the instance groups may still be deploying.  
  ![gcp instance groups](_images/gcp/logging-in/gcp-instance-groups.png)
  2. Click a server instance group to view details such as CPU utilization and the VM instances in that group. Note the **External IP** of one of the deployed VMs.  
  ![gcp server igm details](_images/gcp/logging-in/gcp-server-igm-details.png)
  3. Open a browser tab and enter the copied External IP along with port 8091 as _<external-ip>:8091_ to open the Couchbase Server Web Console.  
  ![gcp web console login](_images/gcp/logging-in/gcp-web-console-login.png)
  4. Enter the user name and password noted when deployment completed.  
  > [!TIP]  
  > If you forgot to note the credentials, you can retrieve them by examining the Custom metadata > startup-script for the server instance template.  
  >  
  > ![gcp instance template startup script](_images/gcp/logging-in/gcp-instance-template-startup-script.png)  
  The dashboard shows the current view of the cluster. If you’ve gotten to this step quickly, the cluster may still be adding nodes and rebalance may be in progress. Once the process complete, the dashboard will look something like the following screen capture.  
  ![gcp web console dashboard](_images/gcp/logging-in/gcp-web-console-dashboard.png)  
  Click the Servers tab to explore the server nodes that have been created.  
  ![gcp web console servers](_images/gcp/logging-in/gcp-web-console-servers.png)  
You can click around to explore, load sample buckets and run queries from the Query Workbench. You can also setup XDCR links between the different clusters created by the deployment.
2. To log in to the Sync Gateway Admin portal:

  1. Click the Products & services icon ![gcp icon prdt services](_images/gcp/deploying/gcp-icon-prdt-services.png) at the top left of the screen to pull down the sidebar and select **Compute Engine** \> **Instance Groups**. You can see a list of all the Instance groups being deployed. Depending on how quickly you get to this step after starting deployment, the instance groups may still be deploying.  
  ![gcp instance groups](_images/gcp/logging-in/gcp-instance-groups.png)
  2. Click a sync gateway instance group to view details such as CPU utilization and the VM instances in that group. Note the **External IP** of one of the deployed VMs.  
  ![gcp sync gateway igm details](_images/gcp/logging-in/gcp-sync-gateway-igm-details.png)
  3. Open a browser tab and enter the copied External IP along with port 4984 as _<external-ip>:4984_. This opens the interface for Couchbase Sync Gateway which is already setup and configured to connect to an empty bucket on the cluster.
  4. Open another browser tab and enter _<external-ip>:4984/\_admin/_ to open the Couchbase Sync Gateway Admin Portal.  
  ![gcp sync gateway admin portal](_images/gcp/logging-in/gcp-sync-gateway-admin-portal.png)

## [](#scaling)Scaling Your Couchbase Cluster

Scaling Couchbase is simplified greatly on Google Cloud Platform. This section describes how to scale up your cluster up in three simple steps.

1. Log in to Google Cloud Platform and navigate to **Compute Engine** \> **Instance Groups** and select the server instance that you want to scale.  
![gcp server instance group members](_images/gcp/scaling/gcp-server-instance-group-members.png)
2. On the **Details** tab, click **Edit Group** and edit the number of instances.  
![gcp server instance group details](_images/gcp/scaling/gcp-server-instance-group-details.png)  
![gcp server instance group edit number](_images/gcp/scaling/gcp-server-instance-group-edit-number.png)
3. Click **Save**. You’ll see a notification that the group is being updated.  
![gcp server instance updating](_images/gcp/scaling/gcp-server-instance-updating.png)  
Once updated, you can see the updated number of instances reflected on the server Instance group Details tab.  
![gcp server instance updated](_images/gcp/scaling/gcp-server-instance-updated.png)  
On a different browser tab, you can log in to the Couchbase Server Web Console to see the additional server nodes that were added to your cluster.  
![gcp web console servers rebalance](_images/gcp/scaling/gcp-web-console-servers-rebalance.png)