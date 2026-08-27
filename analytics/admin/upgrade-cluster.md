---
title: Upgrading a Cluster
description: Upgrades are scheduled as needed on Capella Analytics clusters to
  provide a reliable service with the latest features.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-columnar/edit/main/modules/admin/pages/upgrade-cluster.adoc
  xref: xref:analytics:admin:upgrade-cluster.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/analytics/admin/upgrade-cluster.html)

# Upgrading a Cluster

> Upgrades are scheduled as needed on Capella Analytics clusters to provide a reliable service with the latest features. 

This page walks you through maintenance jobs for Capella Analytics cluster upgrades in Couchbase Capella. Use the procedures on this page to view and reschedule upgrade maintenance jobs for your clusters.

## [](#database-upgrade-timeframes)Cluster Upgrade Timeframes

When planning for cluster upgrades, it's important to understand the upgrade timeframes:

* **Notice period**: the timeframe between when the maintenance job is scheduled (and maintenance notifications are sent) and the scheduled upgrade date (target start time). You receive notification emails when Capella schedules a maintenance job. For more information, see [Manage Maintenance Email Notifications](#upgrade-email-notifications).
* **Upgrade window**: the timeframe during which the maintenance job can begin. This time is dependent on the upgrade type and begins after the notice period ends, allowing you to adjust the maintenance schedule as needed. For more information, see [Reschedule an Individual Maintenance Job](#reschedule-maintenance-job).

> [!NOTE]
> You can click the upgrade maintenance job name in the Capella Analytics UI to see the [full details of the upgrade](#view-maintenance-job) and [set a preferred time and day of the week](#set-preferred-time) for these maintenance jobs. You can also see options that allow you to change when the upgrade [maintenance job](#maintenance-jobs) runs.

For more details about the different types of upgrade maintenance jobs and the timeframes to complete the upgrade, see the following table:

| Upgrade or Maintenance Type | Description                                                                                                                                           | Timeframe                                                                                                                                                                                                                                                                                                                                                                                                         |
| --------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Critical Upgrade**        | Capella Analytics schedules critical upgrades in response to an urgent bug, vulnerability, or other issue that impacts cluster health or performance. | Capella Analytics can schedule these upgrades on the same date as the maintenance job creation and the upgrade maintenance notification. You might have a 0-day notice of a pending upgrade maintenance job before Capella automatically upgrades your cluster.                                                                                                                                                   |
| **Maintenance Release**     | A new Capella Analytics maintenance release.                                                                                                          | Upgrade timeframes vary based on the actual features and improvements included in the Capella Analytics release version and how these features and improvements might impact Capella Analytics users. A typical upgrade maintenance job has a 1-2 week notice period. It can include an upgrade window of 2 to 4 weeks after the notice period ends, allowing customers to adjust the upgrade schedule as needed. |

## [](#maintenance-jobs)Maintenance Jobs

All maintenance jobs have a target start time. Capella Analytics aims to start the maintenance of your cluster at this time. However, maintenance jobs are sometimes delayed when the cluster cannot be upgraded. For more information, see [Maintenance and Cluster Status](#maintenance-cluster-status).

When a maintenance job runs, the cluster is moved to a redeploying state while nodes are rebalanced to apply the maintenance changes. Maintenance redeployments are not time-bound, and the time taken varies depending on the size of the cluster, volume of data, and load. Analytics clusters remain available throughout the upgrade. Cluster reconfiguration options are not available during an upgrade, though data tools remain accessible in the Capella UI.

For each individual maintenance job, you can:

* View the maintenance job type, status, and scheduled upgrade time.
* Review the new features or changes for the maintenance job.
* Set a preferred time to upgrade.
* Reschedule the maintenance to upgrade at a different time.
* Create a support ticket to cancel the maintenance job.

You can review all scheduled maintenance jobs that have run on the cluster. For more information, see [Activity Log](../../cloud/clusters/monitoring/activity-log.md).

> [!IMPORTANT]
> Maintenance and Cluster On/Off
> 
> Keep the following in mind while using scheduled or on-demand on/off operations on your cluster:
> 
> * If you have [scheduled your cluster to turn off](../../cloud/clusters/off-on-schedule.md) and the cluster is running or due to run maintenance within the next hour, Capella does not turn off the cluster. The cluster will not turn off until the next scheduled off event in your schedule.
> * If you try to [turn your cluster off on-demand](../../cloud/clusters/off-on-database.md) and the cluster is running or due to run maintenance within the next hour, Capella returns an error and the cluster does not turn off.
> * If your cluster is already turned off when a maintenance job is set to run, Capella automatically reschedules the maintenance job for an hour later. The maintenance can be repeatedly rescheduled until the cluster is on.

### [](#view-maintenance-job)View Individual Maintenance Jobs

To view scheduled maintenance upgrade jobs for your clusters:

1. Go to the **Analytics** tab and click your cluster name.
2. Go to **Settings** **Maintenance**.
3. View your maintenance jobs in **Scheduled Jobs**.

Upgrade maintenance job statuses are pending, running, completed, and cancelled.

### [](#reschedule-maintenance-job)Reschedule an Individual Maintenance Job

When an upgrade maintenance job is scheduled, you can choose to reschedule your upgrade for any time before the scheduled date or within the upgrade window. Rescheduling is possible up to the end date, which is the latest possible upgrade schedule date specified in the upgrade maintenance job window. However, maintenance jobs cannot be deferred indefinitely because each maintenance job has a latest possible upgrade date.

Depending on the type of upgrade and the target start time, you can schedule a new date. This is a new target start time. When the scheduled time is reached, the cluster is automatically upgraded.

> [!NOTE]
> You can create a support ticket to ask for an extension if there are exceptional circumstances. Extensions are not guaranteed.

To reschedule your maintenance job:

1. On your Capella Analytics cluster's **Maintenance** page, click on the job name in the **Maintenance Jobs** list.
2. Select one of the following:

  * **Keep current schedule**.
  * **Change time**.  
  Click the date picker and set the preferred date and start time.
  * **Run now**.
3. Click **Save**.

### [](#cancelled-maintenance-job)Cancel a Maintenance Job

You cannot cancel maintenance jobs scheduled by Capella Support using the Capella UI. To cancel a support-initiated upgrade, [Create a Support Ticket](../../cloud/support/manage-support.md#create-support-ticket).

To view canceled maintenance jobs:

1. Go to **Settings** **Maintenance**.
2. In **Past Maintenance Jobs**, click **Go to Past Maintenance Jobs**.

### [](#set-preferred-time)Set a Preferred Time for all Maintenance Jobs

You can set a preferred time and day of the week for future maintenance jobs to be scheduled. This does not reschedule maintenance jobs that are already scheduled on the Maintenance tab.

When an upgrade or maintenance becomes available, Capella Analytics attempts to schedule the maintenance at your preferred time and day of the week. The preferred time is not a guarantee. If it's not possible to schedule the maintenance at your preferred time, the cluster is scheduled at any time within the maintenance window.

To set a preferred maintenance day and time for all upcoming jobs:

1. Click **Set Time**.
2. Select **Enable a preferred start time for cluster maintenance**.
3. In the **Day of the Week** list, select the day you want scheduled maintenance to occur.
4. In the **Time** field, enter the time you want scheduled maintenance to occur.  
This time is local to you, and you enter it using the HH:mm format. For example: `14:30`.
5. Click on **Save**.

### [](#upgrade-email-notifications)Manage Maintenance Email Notifications

When a maintenance job is scheduled, email notifications are sent to:

* [Organization Owners](../../cloud/organizations/organization-user-roles.md) where one or more clusters in their organization is scheduled for maintenance.
* [Project Owners](../../cloud/projects/project-roles.md) and Project managers where at least one cluster in a project they have access to is scheduled for maintenance.

Capella sends these emails when the maintenance job is scheduled and, when applicable, 1 week, 24 hours, and 1 hour prior to the target start time. These notifications include details about the cluster, the upgrade, and the upgrade schedule.

> [!NOTE]
> Those with notifications turned OFF will not receive these emails. For more information about how to turn your email notifications on or off, see [Get Alerts through Email](../../cloud/clusters/monitoring/alerts.md#get-alerts-through-email).