---
title: Turn Clusters Off or On
description: You can turn your cluster off to save costs. To resume operations,
  turn it back on.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/off-on-database.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/cloud/clusters/off-on-database.html)

# Turn Clusters Off or On

> You can turn your cluster off to save costs. To resume operations, turn it back on. 

## [](#overview)Overview

Turning off your cluster turns off the compute for your cluster but the storage remains. All of your data, schema (buckets, scopes, and collections), and indexes remain, as well as your cluster configuration, including users and allow lists.

When you turn your cluster off, you will be charged the OFF amount for the cluster.

Variable backup and data transfer costs still apply when your cluster is off.

Private endpoint charges still apply when your cluster is off. To avoid charges, delete your endpoints and turn off Private Endpoints before you turn off your cluster.

You can turn your cluster off for a maximum of 30 days. Capella will notify you by email and automatically turn on your cluster after 30 days.

You can [create a schedule](off-on-schedule.md) to turn your cluster on or off.

> [!TIP]
> Public API
> 
> You can also turn your cluster on or off using the [Management API Reference](../management-api-reference/index.md):
> 
> * [Turn On Cluster](../management-api-reference/index.md#tag/Clusters/operation/clusterOn)
> * [Turn Off Cluster](../management-api-reference/index.md#tag/Clusters/operation/clusterOff)

## [](#when-a-cluster-is-turned-off)When a Cluster is Turned Off

| **Linked App Services**                | Linked App Services will be turned off. Log Streaming for those App Services will be turned off, if enabled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Application and client connections** | Application and client connections will be disconnected. You cannot connect to or read/write from your cluster. You’ll receive an authentication error if you try to connect to a cluster that’s off. [Verify the cluster status](#verify-database-status) if the application returns an authentication error.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Replications**                       | Replications will be deleted. Replications are deleted for both source _and_ target clusters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Backups and scheduled backups**      | Scheduled or on-demand backups cannot run if a cluster is off. Restores cannot run, even if the destination cluster is on, if the cluster that contains the backup is off. Backups will continue to expire when a cluster is off. Download backups you want to keep before turning off your cluster, or do not turn your cluster off past the expiration dates of your existing backups. Backups cannot be downloaded if a cluster is off. If the cluster is scheduled to turn off while a backup or restore operation is running, Capella waits for the operation to complete before turning off the cluster. If you try to manually turn off the cluster while a backup or restore operation is running, Capella will return an error and the cluster will not turn off. |
| **Maintenance**                        | If the cluster is running maintenance or due to run maintenance in the next hour, the cluster cannot be turned off manually or through a schedule. If the cluster is turned back on, it might need maintenance. Avoid scheduling an off soon after turning your cluster back on. If your cluster is already turned off when a maintenance job is set to run, Capella automatically reschedules the maintenance job for an hour later. The maintenance can be repeatedly rescheduled until the cluster is on.                                                                                                                                                                                                                                                               |

## [](#when-a-cluster-is-turned-on)When a Cluster is Turned On

| **Linked App Services** | You can choose whether to turn your linked App Services back on with your cluster.                                                                                                                                                                              |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Private Endpoints**   | You can use any private endpoints that you did not delete before turning off your cluster. If you deleted private endpoints, you must recreate them.                                                                                                            |
| **Replications**        | Replications will not be recreated. You must manually recreate your replications on your source and target clusters to continue cross datacenter replication (XDCR). For more information about XDCR, see [Cross Data Center Replication (XDCR)](xdcr/xdcr.md). |
| **Maintenance**         | When the cluster is turned back on, it might need maintenance. Avoid turning your cluster off soon after turning your cluster back on.                                                                                                                          |

## [](#turn-cluster-onoff)Turn Cluster On/Off

> [!NOTE]
> If a cluster that is off requires maintenance, the maintenance begins when it turns on.

To turn your cluster on or off:

1. Log in to your account and click **Operational**.
2. Find your cluster in the cluster list, click the **More options**  icon.
3. Choose **Turn Off**/**Turn On**.
4. In the confirmation window, type "yes" to confirm, and click **Yes, Proceed**.

or

1. Log in to your account and click **Operational**.
2. Click your cluster in the cluster list to go to your cluster page.
3. Click on the **Settings** tab.
4. In the navigation menu, click **General**.
5. Scroll down to **Cluster On/Off** and click **Turn On/Off Cluster**.
6. In the confirmation window, type "yes" to confirm, and click **Yes, Proceed**.  
Turning on or off cluster operations will take a few minutes.  
If a cluster backup is running or if maintenance is scheduled within 1 hour, Capella will not turn off the cluster.

## [](#verify-database-status)Verify Cluster Status

To check the status of your cluster:

1. Log in to your account and click **Operational**.
2. Find your cluster in the cluster list and check the status in the **status** column.

| Status      | Description                                                                                                               |
| ----------- | ------------------------------------------------------------------------------------------------------------------------- |
| OFF         | Your cluster is OFF.                                                                                                      |
| Turning Off | Your cluster is turning OFF. Wait for the status to change to **OFF** before trying to turn on.                           |
| Turning On  | Your cluster is turning on. This may take a few minutes. You can use your cluster when the status changes to **Healthy**. |
| Healthy     | Your cluster is operational.                                                                                              |