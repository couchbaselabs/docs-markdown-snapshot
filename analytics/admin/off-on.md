---
title: Turn a Cluster Off or On
description: You can turn a Capella Analytics services cluster off to save costs.
editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/admin/pages/off-on.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:analytics:admin:off-on.adoc[]
---

[View original HTML](/analytics/admin/off-on.html)

# Turn a Cluster Off or On

> You can turn a Capella Analytics services cluster off to save costs. To resume operations, turn it back on. 

## [](#overview)Overview

Turning off your cluster turns off the compute for your cluster but the storage remains. All of your data, schema (buckets, scopes, and collections), and indexes remain, as well as your cluster configuration, including users and allow lists.

When you turn your cluster off, you will be charged the OFF amount shown in the Capella UI for the cluster.

Variable backup and data transfer costs still apply when your cluster is off.

Private endpoint charges still apply when your cluster is off. To avoid charges, delete your endpoints and turn off Private Endpoints before you turn off your cluster.

You can turn your cluster off for a maximum of 30 days. Capella will notify you by email and automatically turn on your cluster after 30 days.

You can [create a schedule](#schedule-a-cluster-to-turn-onoff) to turn your cluster on or off.

## [](#when-a-cluster-is-turned-off)When a Cluster is Turned Off

| **Remote links and running queries**   | Remote links are disconnected. Any currently running queries are canceled.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Application and client connections** | Application and client connections will be disconnected. You cannot connect to or read/write from your cluster. You will receive an authentication error if you try to connect to a cluster that’s off. [Verify the cluster status](#check-cluster-status) if the application returns an authentication error.                                                                                                                                                                                                                                                                       |
| **Backups and scheduled backups**      | Backups cannot run, be downloaded, or restored - even to another cluster. Backups can expire. Download backups you want to keep before turning off your cluster, or do not turn your cluster off past the expiration dates of your existing backups. If the cluster is scheduled to turn off while a backup or restore operation is running, Capella waits for the operation to complete before turning off the cluster. If you try to manually turn off the cluster while a backup or restore operation is running, Capella will return an error and the cluster will not turn off. |
| **Maintenance**                        | If the cluster is running maintenance or due to run maintenance in the next hour, the cluster cannot be turned off manually or through a schedule. If the cluster is turned back on, it might need maintenance. Avoid scheduling an off soon after turning your cluster back on.                                                                                                                                                                                                                                                                                                     |

## [](#managing-on-demand-cluster-on-and-off)Managing On-Demand Cluster On and Off

You can turn your cluster on or off on-demand, and check the status of your cluster at any time.

### [](#prerequisites)Prerequisites

* You have created a Capella Analytics services cluster.
* You have logged in to the Couchbase Capella UI.
* You have [disconnected any remote links](../sources/connect-link.md).

### [](#turn-a-cluster-on-or-off)Turn a Cluster On or Off

To turn your cluster on or off:

1. Go to **Capella Analytics**.
2. In the list of Capella Analytics clusters, find your cluster.
3. Go to **More Options (⋮)** **Turn Cluster Off/Turn Cluster On**.
4. In the confirmation window, type `yes` to confirm, and click **Yes, Proceed**.

or

1. Go to **Capella Analytics**.
2. In the list of Capella Analytics clusters, click your cluster name.
3. Go to **Settings** **General**.
4. Under **Cluster On/Off**, click **Turn Off Cluster** or **Turn On Cluster**.
5. In the confirmation window, type `yes` to confirm, and click **Yes, Proceed**.  
Turning your cluster on or off will take a few minutes.  
If a cluster backup is running or if maintenance is scheduled within 1 hour, Capella will not turn off your cluster.

### [](#check-cluster-status)Check Cluster Status

To check the status of your cluster:

1. Go to **Capella Analytics**.
2. In the list of Capella Analytics clusters, find your cluster.
3. Check the status in the **Status** column.

| Status      | Description                                                                                                               |
| ----------- | ------------------------------------------------------------------------------------------------------------------------- |
| OFF         | Your cluster is OFF.                                                                                                      |
| Turning Off | Your cluster is turning OFF. Wait for the status to change to **OFF** before trying to turn on.                           |
| Turning On  | Your cluster is turning on. This may take a few minutes. You can use your cluster when the status changes to **Healthy**. |
| Healthy     | Your cluster is operational.                                                                                              |

## [](#schedule-a-cluster-to-turn-onoff)Schedule a Cluster to Turn On/Off

Set a schedule to automatically turn your cluster on and off at set times.

### [](#prerequisites-2)Prerequisites

* You have created a Capella Analytics services cluster.
* You have logged in to the Couchbase Capella UI.
* Before your cluster turns off, you have [disconnected any remote links](../sources/connect-link.md).

### [](#create-a-new-cluster-schedule)Create a New Cluster Schedule

1. Go to **Capella Analytics**.
2. In the list of Capella Analytics clusters, click your cluster name.
3. Go to **Settings** **Schedule On/Off**.
4. Choose the timezone to use for your schedule from the list.
5. Choose the day and time ranges you want your cluster to be on.  
Capella turns your cluster on at the specified **From** time, until the **To** time, for each selected day.
6. To add a new time range for a different set of days, click **Add Scheduling Row**.
7. To save and start your schedule, click **Start Schedule**.

> [!NOTE]
> Capella will not turn off the cluster if a cluster backup is running, if maintenance is running, or if maintenance is scheduled within 1 hour. If a cluster that’s off requires maintenance, the maintenance begins when it turns on.

### [](#edit-cluster-schedule)Edit Cluster Schedule

To edit your cluster schedule:

1. Go to **Capella Analytics**.
2. In the list of Capella Analytics clusters, click your cluster name.
3. Go to **Settings** **Schedule On/Off**.
4. Click **Edit Schedule**.
5. Edit your timezone, day, and time ranges as needed.  
To add a new time range for a different set of days, click **Add Scheduling Row**.
6. Click **Start Schedule**.

### [](#delete-cluster-schedule)Delete Cluster Schedule

> [!NOTE]
> You cannot recover a deleted schedule.

To delete your cluster schedule:

1. Go to **Capella Analytics**.
2. In the list of Capella Analytics clusters, click your cluster name.
3. Go to **Settings** **Schedule On/Off**.
4. Click **Delete Schedule**.
5. Type `delete` to confirm and click **Delete Schedule**.