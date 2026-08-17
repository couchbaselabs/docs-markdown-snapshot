---
title: Schedule Cluster On or Off
description: You can schedule when your cluster is on and off to save costs.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/off-on-schedule.adoc
  xref: xref:cloud:clusters:off-on-schedule.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/clusters/off-on-schedule.html)

# Schedule Cluster On or Off

> You can schedule when your cluster is on and off to save costs. 

Turning off your cluster turns off the compute for your cluster but the storage remains. All of your data, schema (buckets, scopes, and collections), and indexes remain, as well as your cluster configuration, including users and allow lists.

When you turn your cluster off, you will be charged the OFF amount for the cluster

Private endpoint charges still apply when your cluster is off. To avoid charges, delete your endpoints and turn off Private Endpoints before you turn off your cluster.

> [!NOTE]
> Variable backup and data transfer costs still apply when your cluster is off.

> [!TIP]
> Public API
> 
> You can also schedule your cluster to turn on or off using the [Capella Operational Management API Reference](../management-api-reference/index.md):
> 
> * [Get Cluster On/Off Schedule](../management-api-reference/index.md#tag/OnOff-Schedule/operation/getOnOffSchedule)
> * [Update Cluster On/Off Schedule](../management-api-reference/index.md#tag/OnOff-Schedule/operation/putOnOffSchedule)
> * [Delete Cluster On/Off Schedule](../management-api-reference/index.md#tag/OnOff-Schedule/operation/deleteOnOffSchedule)

## [](#when-a-cluster-is-turned-off)When a Cluster is Turned Off

| **Linked App Services**                | Linked App Services will be turned off.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Application and client connections** | Application and client connections will be disconnected. You cannot connect to or read/write from your cluster. You'll receive an authentication error if you try to connect to a cluster that's off. [Verify the cluster status](off-on-database.md#verify-database-status) if the application returns an authentication error.                                                                                                                                                                                                                                                                                   |
| **Replications**                       | Replications will be deleted. For more information about XDCR, see [Cross Data Center Replication (XDCR)](xdcr/xdcr.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Backups and scheduled backups**      | Scheduled or on-demand backups cannot run if a cluster is off. Restores cannot run, even if the destination cluster is on, if the cluster that contains the backup is off. Backups will continue to expire when a cluster is off. Backups cannot be downloaded if a cluster is off. If the cluster is scheduled to turn off while a backup or restore operation is running, Capella waits for the operation to complete before turning off the cluster If you try to manually turn off the cluster while a backup or restore operation is running, Capella will return an error and the cluster will not turn off. |
| **Maintenance**                        | If the cluster is running maintenance or due to run maintenance in the next hour, the cluster cannot be turned off manually or through a schedule. When the cluster is turned back on, it might need maintenance. Avoid scheduling an off soon after turning your cluster back on. If your cluster is already turned off when a maintenance job is set to run, Capella automatically reschedules the maintenance job for an hour later. The maintenance can be repeatedly rescheduled until the cluster is on.                                                                                                     |

## [](#when-a-cluster-is-turned-on)When a Cluster is Turned On

| **Linked App Services** | Linked App Services will automatically be turned on.                                                                                                                                                                                                            |
| ----------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Private Endpoints**   | You can use any private endpoints that you did not delete before turning off your cluster. If you deleted private endpoints, you must recreate them.                                                                                                            |
| **Replications**        | Replications will not be recreated. You must manually recreate your replications on your source and target clusters to continue cross datacenter replication (XDCR). For more information about XDCR, see [Cross Data Center Replication (XDCR)](xdcr/xdcr.md). |
| **Maintenance**         | When the cluster is turned back on, it might need maintenance. Avoid scheduling an off soon after turning your cluster back on.                                                                                                                                 |

## [](#schedule-cluster-onoff)Schedule Cluster On/Off

To schedule your cluster:

1. Log in to your account and click **Operational**.
2. Choose your cluster.
3. Click on the **Settings** tab.
4. In the navigation menu, click **Schedule On/Off**.
5. Choose your timezone for your schedule from the drop-down list.
6. Choose the day and time ranges you want your cluster to be on.  
To add different time ranges for different days, click **\+ Add Scheduling Row** to add new rows.
7. Click **Start Schedule**.

> [!NOTE]
> Capella will not turn off the cluster if a cluster backup is running, if maintenance is running, or if maintenance is scheduled within 1 hour. If a cluster that is off requires maintenance, the maintenance begins when it turns on.

## [](#edit-cluster-schedule)Edit Cluster Schedule

To edit your cluster schedule:

1. Log in to your account and click **Operational**.
2. Choose your cluster to go to your cluster page.
3. Click on the **Settings** tab.
4. In the navigation menu, click **Schedule On/Off**.
5. Click **Edit Schedule**.
6. Edit your timezone, day, and time ranges as needed.  
To add different time ranges for different days, click **\+ Add Scheduling Row** to add new rows.
7. Click **Start Schedule**.

## [](#pause-cluster-schedule)Pause Cluster Schedule

Pause your cluster schedule to temporarily stop your cluster from automatically turning on or off according to your set schedule. Pausing a cluster schedule preserves your schedule settings, eliminating the need to delete and recreate your schedule when you need it again.

You can resume your cluster schedule at any time.

> [!NOTE]
> You can still manually turn your cluster on or off when your schedule is paused. The status of your cluster will remain in that state until you decide to change it or reactivate the schedule.

To pause your schedule:

1. Log in to your account and click **Operational**.
2. Choose your cluster to go to your cluster page.
3. Click on the **Settings** tab.
4. In the navigation menu, click **Schedule On/Off**.
5. Find the schedule you want to pause and click **Paused**.

To reactivate your cluster schedule, click **Active**.

> [!CAUTION]
> If you pause your On/Off schedule, your cluster can be continuously OFF for only a maximum of 30 days. After 30 days, Capella automatically turns your cluster back on, and you can manually turn it off again as needed.

## [](#delete-cluster-schedule)Delete Cluster Schedule

> [!NOTE]
> You cannot recover a deleted schedule.

To delete your cluster schedule:

1. Log in to your account and click **Operational**.
2. Choose your cluster.
3. Click on the **Settings** tab.
4. In the navigation menu, click **Schedule On/Off**.
5. Click **Delete Schedule**.
6. Type "delete" to confirm and click **Delete Schedule**.