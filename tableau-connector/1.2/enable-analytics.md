---
title: Enable Couchbase Analytics Service
description: To use Tableau with Couchbase Server or Capella Operational, you
  must enable the Analytics Service on the target node.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-tableau/edit/release/1.2/modules/ROOT/pages/enable-analytics.adoc
  xref: xref:1.2@tableau-connector::enable-analytics.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/tableau-connector/1.2/enable-analytics.html)

# Enable Couchbase Analytics Service

> To use Tableau with Couchbase Server or Capella Operational, you must enable the Analytics Service on the target node. 

You can enable the Analytics Service either on an existing cluster or a new cluster.

> [!NOTE]
> To enable the Analytics Service on Capella Operational, see [Using the Analytics Service](../../cloud/clusters/analytics-service/analytics-service.md).

## [](#enable-analytics-service-on-an-existing-cluster)Enable Analytics Service on an Existing Cluster

To enable the Analytics Service on an existing cluster, use one of the following methods:

### [](#option-1-add-a-new-node-and-rebalance)Option 1: Add a New Node and Rebalance

Use this option to add a new node to an existing cluster and enable the Analytics Service on that node.

> [!NOTE]
> Before you begin, start the node you want to add and note its IP address.

1. Log in to the Couchbase Web Console of your existing cluster as an administrator.
2. In the left-hand menu, select **Servers**.
3. Click **Add Server**.
4. In **Add Server Node** dialog, enter the **IP address** of the node you want to add.
5. Select the authentication method as **Username/Password**.

  * The **Username** field is pre-populated with your admin username.
  * Enter a **Password**. You can use a placeholder value and change it later after the node is added to the cluster.
6. In **Services**, select **Data** and **Analytics**. Clear all other services.
7. Click **Add Server**. The new node appears in the **Servers** list.
8. Next, click **Rebalance** to rebalance the cluster.

For more information, see [Add a Node](../../server/current/manage/manage-nodes/add-node-and-rebalance.md).

### [](#option-2-join-a-cluster-and-rebalance)Option 2: Join a Cluster and Rebalance

Use this option to add an uninitialized, unprovisioned node to an existing cluster and enable the Analytics Service on that node.

1. Open the Couchbase Web Console of the uninitialized node.
2. Click **Join Existing Cluster**.
3. Enter the **Cluster Host Name / IP address** of the existing cluster.
4. Enter the **Username** and **Password** of the existing cluster. Use the Cluster Admin or Full Admin credentials.
5. Click **Configure Services & Settings For This Node** for more options.
6. Enter the **IP address** of the node.
7. Select **Data** and **Analytics** and clear all other services.
8. Click **Join Cluster**. The cluster dashboard appears.
9. In the left-hand menu, select **Servers**.
10. Next, click **Rebalance** to rebalance the cluster.

For more information, see [Join a Cluster](../../server/current/manage/manage-nodes/join-cluster-and-rebalance.md).

## [](#enable-analytics-service-on-a-new-cluster)Enable Analytics Service on a New Cluster

You can enable the Analytics Service while creating a new cluster.

To create a new cluster, see [Create a Cluster](../../server/current/manage/manage-nodes/create-cluster.md).

* When configuring the cluster, select **Finish With Defaults** to automatically enable the Analytics Service.
* If you want to configure the service memory quota for the Analytics Service, select **Configure Disk, Memory, Services**.