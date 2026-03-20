---
title: Upgrading a Cluster
description: Maintenance jobs are scheduled to run upgrades on your cluster.
  Capella upgrades help provide a reliable service with the latest features.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/upgrade-database.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:cloud:clusters:upgrade-database.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/clusters/upgrade-database.html)

# Upgrading a Cluster

> Maintenance jobs are scheduled to run upgrades on your cluster. Capella upgrades help provide a reliable service with the latest features. 

This page walks you through support, timeframes, and maintenance jobs for cluster upgrades in Couchbase Capella. Use the procedures on this page to view, schedule, and reschedule maintenance jobs. These maintenance jobs apply upgrades to your clusters.

When a [maintenance job](#maintenance-jobs) is scheduled to upgrade your operational cluster, Capella sends you [email notifications](#upgrade-email-notifications).

## [](#server-version-support)Couchbase Server Version Support

Capella makes maintenance jobs available for the following types of Couchbase Server releases:

| Release                  | Introduces                            |
| ------------------------ | ------------------------------------- |
| **Major**                | Major new features and functionality. |
| **Minor**                | Some new features or improvements.    |
| **Maintenance or Patch** | Essential fixes and improvements.     |

By carefully managing the upgrade process, Capella tries to make upgrading as easy as possible. For maintenance and patch releases, you can expect none to minimal impact.

The notice that Capella aims to provide varies depending on the nature of the upgrade. For example, major version upgrades often require [application testing](upgrade-best-practices.md#test-application). The upgrade window for major versions is longer than for maintenance, patch, and minor version upgrades. For more information, see [Cluster Upgrade Timeframes](#database-upgrade-timeframes).

Couchbase Capella supports the following Couchbase Server versions for new clusters:

| Status         | Available Version                                                      |
| -------------- | ---------------------------------------------------------------------- |
| Latest release | [Couchbase Server 8.0](../../server/current/release-notes/relnotes.md) |

> [!IMPORTANT]
> Maintenance Best Practice
> 
> Before running any patch, minor, or major cluster upgrades, review the [Upgrade Best Practices](upgrade-best-practices.md). Use this page to review the best practice recommendations for your cluster upgrades.

In addition to Couchbase Server upgrades, Capella may schedule routine maintenance jobs that do not upgrade the Couchbase Server version, but apply essential updates to the systems your cluster runs on.

## [](#database-upgrade-timeframes)Cluster Upgrade Timeframes

When planning for cluster upgrades, it’s important to understand the upgrade timeframes:

* **Notice period**: the timeframe between when the maintenance job is scheduled (and maintenance notifications are sent) and the scheduled upgrade date (target start time). You receive notification emails when Capella schedules a maintenance job. For more information, see [Manage Maintenance Email Notifications](#upgrade-email-notifications).
* **Upgrade window**: the timeframe during which the maintenance job can begin. This time is dependent on the upgrade type and begins after the notice period ends, allowing you to adjust the maintenance schedule as needed. For more information, see [Reschedule a Maintenance Job](#reschedule-maintenance-job).

> [!NOTE]
> You can click the maintenance job name in the Capella UI to see the full details of the upgrade and set a preferred time and day of the week for these maintenance jobs. You can also see options that allow you to change when the upgrade maintenance job runs.

For more details about the different types of maintenance jobs and the timeframes to complete the upgrade, see the following table:

| Upgrade or Maintenance Type                       | Description                                                                                                                                 | Timeframe                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Critical Upgrade**                              | Capella schedules critical upgrades in response to an urgent bug, vulnerability, or other issue that impacts cluster health or performance. | Capella can schedule these upgrades on the same date as the maintenance job creation and the upgrade maintenance notification. You might have a 0-day notice of a pending upgrade maintenance job before Capella automatically upgrades your cluster.                                                                                                                                                                                                                                                                                                                                                                             |
| **Routine Maintenance or Couchbase Server Patch** | A new Couchbase Server maintenance, patch version, or routine image upgrades.                                                               | A typical maintenance job has a 1-2 week notice period. It includes an upgrade window of 2 to 4 weeks after the notice period ends, allowing customers to adjust the upgrade schedule as needed.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Couchbase Server Minor Release**                | A new Couchbase Server minor version release.                                                                                               | The timeframes for notice periods and upgrade windows vary based on the actual features and improvements included in the Couchbase Server minor release version, and how these features and improvements might impact Capella users. If the service impact is similar to a Server maintenance or patch release, the typical notice and maintenance job dates for Capella are the same as the Server maintenance or patch release. A maximum of 2 minor versions are available as options during cluster creation.                                                                                                                 |
| **Couchbase Server Major Release**                | A new Couchbase Server major release version.                                                                                               | Upgrade timeframes vary. Since major version upgrades often require [application testing](upgrade-best-practices.md#test-application), the upgrade window for major versions is longer than for maintenance and minor version upgrades. When the upgrade window is announced for a major version upgrade, Capella provides you with a suitable notice period to allow for application testing. You can defer major version upgrades until 12 months have passed since the initial release of the cluster’s major version, or until 3 months have passed since the latest minor version release under the cluster’s major version. |

## [](#maintenance-jobs)Maintenance Jobs

All maintenance jobs have a target start time. Capella aims to start your cluster upgrade at this time. However, maintenance jobs are sometimes delayed when the cluster cannot be upgraded. For more information, see [Maintenance and Cluster Status](#maintenance-cluster-status).

When a maintenance job runs, the cluster is moved to a redeploying state while nodes are rebalanced to apply the maintenance changes. Maintenance redeployments are not time-bound, and the time taken varies depending on the size of the cluster, volume of data, and load. Couchbase Capella clusters are designed to remain available throughout the upgrade. Cluster reconfiguration options are not available during an upgrade, though data tools remain accessible in the Capella UI.

> [!CAUTION]
> Single Node clusters may experience downtime during upgrades. Since there are no data replicas, any failure during the upgrade process can lead to service disruption. It’s recommended to use Single Node clusters for prototyping or learning purposes. For production use cases, configure a Multi-Node cluster. To scale out your Single Node cluster, see [Modify a Paid Cluster](modify-database.md).

For each individual maintenance job, you can:

* Create and change the job schedule.
* View the maintenance job type, status, and scheduled upgrade time.
* Review the new features or changes for the maintenance job.

You can review all scheduled maintenance jobs that have run on the cluster. For more information, see [Activity Log](monitoring/activity-log.md).

> [!IMPORTANT]
> Maintenance and Cluster Status
> 
> Keep the following in mind while using scheduled or on-demand on/off operations on your cluster:
> 
> * Your cluster must have a [Healthy](scale-database.md#cluster-status) scaling status and be [turned on](off-on-database.md#turn-cluster-onoff) to run an upgrade.
> * If your cluster is turned off or in an unhealthy state when a maintenance job is set to run an upgrade, Capella automatically reschedules the maintenance job for an hour later. The maintenance is repeatedly rescheduled until the cluster is on and healthy.
> * Even when your cluster is turned off, you can schedule a maintenance job to run an upgrade once the cluster is turned on. [Manually turn your cluster back on](off-on-database.md#turn-cluster-onoff) if you want to **Upgrade Now**.
> * If you have [scheduled your cluster to turn off](off-on-schedule.md) and the cluster is running or due to run an upgrade within the next hour, Capella does not turn off the cluster. The cluster will not turn off until the next scheduled off event in your schedule.
> * If you try to [turn your cluster off on-demand](off-on-database.md#turn-cluster-onoff) and the cluster is running or due to run an upgrade within the next hour, Capella returns an error and the cluster does not turn off.

### [](#view-individual-maintenance-jobs)View Individual Maintenance Jobs

You can view current and scheduled maintenance jobs for your clusters:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select your cluster.
3. Go to **Settings** **Maintenance**.
4. View your maintenance jobs in **Scheduled Maintenance Jobs**.

Upgrade maintenance job statuses are pending, running, completed, and cancelled.

The **Created By** field indicates whether the maintenance job was scheduled by a user or by the Capella Support team.

### [](#schedule-maintenance-jobs)Schedule a Maintenance Job

When certain upgrade maintenance jobs become available, if you have the [Organization Owner](../organizations/organization-user-roles.md#organization-role-organization-owner) or [Project Owner](../projects/project-roles.md#project-owner-role) role, you can schedule these jobs for your cluster.

> [!NOTE]
> Scheduling Upgrades
> 
> You cannot self-schedule all maintenance jobs for your operational cluster. Some maintenance jobs can only be scheduled by Capella Support.
> 
> To see if a maintenance job is available for you to schedule:
> 
> 1. Go to **Operational Clusters** and find the name of the cluster you’re working with.
> 2. In the **Cluster Activity** column, look for the upgrade icon ![arrow circle up](_images/arrow_circle_up.png). This indicates an upgrade is available.

Prior to any maintenance job, follow maintenance best practices for a safe and effective cluster upgrade. This may include backing up your cluster and verifying SDK compatibility. For more information, see [Upgrading Best Practices](upgrade-best-practices.md).

To schedule a maintenance job for your cluster:

1. Go to **Operational Clusters** and find your cluster.
2. Choose one of the following options:

  1. Go to **More Options (︙)** **Upgrade Cluster** and click **Upgrade Cluster**.
  2. Go to your cluster’s **Data Tools** page and click **Cluster Upgrade**.
3. Select the upgrade version for your cluster.
4. Select one of the following options:

  1. To schedule a maintenance job to start within the next 10 minutes, click **Upgrade Now**.
  2. To schedule a maintenance job for a later time, click **Schedule Upgrade**.  
  Enter a date and time and click **Save**.

### [](#reschedule-maintenance-job)Reschedule a Maintenance Job

When an maintenance job is scheduled, you can choose to reschedule it for any time before the scheduled date or within the upgrade window. Rescheduling is possible up to the end date, which is the latest possible upgrade schedule date specified in the upgrade window. However, maintenance jobs cannot be deferred indefinitely because each maintenance job has a latest possible upgrade date.

Depending on the type of upgrade and the target start time, you can schedule a new date. This is a new target start time. When the scheduled time is reached, the cluster is automatically upgraded.

You cannot reschedule a maintenance job while it’s **Running**.

> [!NOTE]
> You can create a support ticket to ask for an extension if there are exceptional circumstances. Extensions are not guaranteed.

To reschedule your maintenance job:

1. Go to **Settings** **Maintenance**
2. Find the maintenance job in **Scheduled Maintenance Jobs**.
3. Choose one of the following options:

  1. To schedule a maintenance job to start within the next 10 minutes, click **Run Now**.
  2. To schedule a maintenance job for a later time, go to **More Options (︙)** **Change Upgrade Schedule**.  
  Enter a new date and time and click **Save**.  
  If another job is in progress, then the selected job will be queued to run at a later time.

> [!NOTE]
> When you create a new upgrade schedule for your cluster, you’re overriding the existing one. This cancels the previous upgrade and applies the new schedule you set.

### [](#cancelled-maintenance-job)Cancel a Maintenance Job

You can cancel maintenance jobs that you have scheduled. You cannot cancel a maintenance job while it’s **Running**.

You cannot cancel maintenance jobs scheduled by Capella Support. When Support schedules a mandatory upgrade for your cluster, they cancel your previously scheduled maintenance upgrade. You can reschedule your maintenance job once the mandatory upgrade is complete. To cancel a support-initiated upgrade, [Create a Support Ticket](../support/manage-support.md#create-support-ticket).

To cancel a maintenance job you have scheduled:

1. Go to **Settings** **Maintenance**.
2. Find the maintenance job in **Scheduled Maintenance Jobs**.
3. Go to **More Options (︙)** **Cancel Scheduled Upgrade**.
4. Confirm that you want to cancel the maintenance job and click **Cancel Scheduled Upgrade**.

To view canceled maintenance jobs:

1. Go to **Settings** **Maintenance**.
2. In **Past Maintenance Jobs**, click **Go to Past Maintenance Jobs**.

### [](#set-preferred-time)Set a Preferred Time for all Maintenance Jobs

You can set a preferred time and day of the week for future maintenance jobs to be scheduled. This does not reschedule maintenance jobs that are already scheduled on the Maintenance tab.

When an upgrade or maintenance becomes available, Capella attempts to schedule the maintenance job at your preferred time and day of the week. The preferred time is not a guarantee. If it is not possible to schedule the maintenance job at your preferred time, the cluster is scheduled at any time within the upgrade window.

To set a preferred maintenance day and time for all upcoming jobs:

1. Go to **Settings** **Maintenance**.
2. Click **Set Maintenance Schedule**.
3. Click **Enable a preferred start time for cluster maintenance**.
4. In the **Day of the Week** list, select the day you want scheduled maintenance to occur.
5. In the **Time** field, enter the time you want scheduled maintenance to occur.  
Your upgrade time is local to you. Enter a time in the HH:mm format. For example: `14:30`.
6. Click **Save**.

### [](#upgrade-email-notifications)Manage Maintenance Email Notifications

When a maintenance job is scheduled, email notifications are sent to:

* [Organization Owners](../organizations/organization-user-roles.md#organization-role-organization-owner) where one or more clusters in their organization is scheduled for maintenance.
* [Project Owners](../projects/project-roles.md#project-owner-role) and [Cluster Managers](../projects/project-roles.md#project-cluster-manager-role) where at least one cluster in a project they have access to is scheduled for maintenance.

Capella sends these emails when the maintenance job is scheduled and, when applicable, 1 week, 24 hours, and 1 hour prior to the target start time. These notifications include details about the cluster, the upgrade, and the upgrade schedule.

> [!NOTE]
> Those with notifications turned off will not receive these emails. For more information about how to turn your email notifications on or off, see [Get Alerts through Email](monitoring/alerts.md#get-alerts-through-email).

## [](#see-also)See Also

See the following pages for more information about managing clusters:

* [Upgrade App Services](../../app-services/maintenance/upgrading-app-services.md).
* [Modify a Paid Cluster](modify-database.md)
* [Cluster Scaling](scale-database.md)
* [Sizing a Cluster](sizing.md)