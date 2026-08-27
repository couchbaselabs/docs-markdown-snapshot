---
title: Manage Cluster Maintenance Jobs
description: You can use the Capella UI to view self-service or Capella Support
  scheduled maintenance jobs for your cluster at any time.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/manage-maintenance.adoc
  xref: xref:cloud:clusters:manage-maintenance.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/clusters/manage-maintenance.html)

# Manage Cluster Maintenance Jobs

> You can use the Capella UI to view self-service or Capella Support scheduled maintenance jobs for your cluster at any time. 

You can also schedule or cancel your self-service maintenance jobs, or set a preferred time for all future maintenance.

## [](#prerequisites)Prerequisites

* To schedule maintenance jobs on a cluster, you must have the [Organization Owner](../organizations/organization-user-roles.md#organization-role-organization-owner) or [Project Owner](../projects/project-roles.md#project-owner-role) role.
* To schedule a new maintenance job, an upgrade must be available:

  * On the **Operational** tab, look for the upgrade icon ![arrow circle up](_images/arrow_circle_up.png) next to the cluster you want to upgrade. This indicates an upgrade is available.
  * The cluster you want to upgrade must have a [Healthy](scale-database.md#cluster-status) scaling status and be [turned on](off-on-database.md#turn-cluster-onoff) to immediately run an upgrade job.
* You have followed [upgrade best practices](upgrade-best-practices.md) before upgrading your cluster.
* To reschedule or cancel a maintenance job, an upgrade must not currently be **Running** on your cluster.

## [](#view-current-maintenance)View Current and Scheduled Maintenance Jobs

To view current and scheduled maintenance jobs for your cluster:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  * Click your organization name and go to **Operational**.
  * Click your current project name or search for a project and go to **Operational**.
  * Expand the cluster breadcrumb and search for a cluster.
2. Select your cluster.
3. Go to **Settings** **Maintenance**.

Upgrade maintenance job statuses are pending, running, completed, and cancelled.

The **Created By** field indicates whether the maintenance job was scheduled by a user or by the Capella Support team.

## [](#view-past-maintenance)View Past Maintenance Jobs

To view past maintenance jobs for your cluster:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  * Click your organization name and go to **Operational**.
  * Click your current project name or search for a project and go to **Operational**.
  * Expand the cluster breadcrumb and search for a cluster.
2. Select your cluster.
3. Go to **Settings** **Maintenance**.
4. In **Past Maintenance Jobs**, click **Go to Past Maintenance Jobs**.

Capella displays details about all completed or cancelled maintenance jobs on your cluster. The **Created By** field indicates whether the maintenance job was scheduled by a user or by the Capella Support team.

## [](#schedule-maintenance-jobs)Schedule a Maintenance Job

> [!NOTE]
> You cannot self-schedule all maintenance jobs for your operational cluster. Some maintenance jobs can only be scheduled by Capella Support.

Prior to any maintenance job, follow maintenance best practices for a safe and effective cluster upgrade. This may include backing up your cluster and verifying SDK compatibility. For more information, see [Upgrading Best Practices](upgrade-best-practices.md).

To schedule a maintenance job for your cluster:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  * Click your organization name and go to **Operational**.
  * Click your current project name or search for a project and go to **Operational**.
  * Expand the cluster breadcrumb and search for a cluster.
2. Do 1 of the following:

  * Go to **More Options (︙)** **Upgrade Cluster** and click **Upgrade Cluster**.
  * Go to your cluster's **Data Tools** page and click **Cluster Upgrade**.
3. Select the upgrade version for your cluster.
4. Do 1 of the following to schedule an available maintenance job:

  * To schedule a maintenance job to start within the next 10 minutes, click **Upgrade Now**.
  * To schedule a maintenance job for a later time, click **Schedule Upgrade**.  
  Enter a date and time and click **Save**.

## [](#reschedule-maintenance-job)Reschedule a Maintenance Job

When an maintenance job is scheduled, you can choose to reschedule it for any time before the scheduled date or within the upgrade window. Rescheduling is possible up to the end date, which is the latest possible upgrade schedule date specified in the upgrade window. However, maintenance jobs cannot be deferred indefinitely because each maintenance job has a latest possible upgrade date.

Depending on the type of upgrade and the target start time, you can schedule a new date. This is a new target start time. When the scheduled time is reached, the cluster is automatically upgraded.

You cannot reschedule a maintenance job while it's **Running**.

> [!NOTE]
> You can create a support ticket to ask for an extension if there are exceptional circumstances. Extensions are not guaranteed.

To reschedule your maintenance job:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  * Click your organization name and go to **Operational**.
  * Click your current project name or search for a project and go to **Operational**.
  * Expand the cluster breadcrumb and search for a cluster.
2. Select your cluster.
3. Go to **Settings** **Maintenance**.
4. Find the maintenance job you want to reschedule in **Scheduled Maintenance Jobs**.
5. Do 1 of the following to reschedule your maintenance job:

  * To schedule the maintenance job to start within the next 10 minutes, click **Run Now**.
  * To schedule the maintenance job for a later time, go to **More Options (︙)** **Change Upgrade Schedule**.  
  Enter a new date and time and click **Save**.  
  If another job is in progress, then the selected job will be queued to run at a later time.

> [!NOTE]
> When you create a new upgrade schedule for your cluster, you're overriding the existing one. This cancels the previous upgrade and applies the new schedule you set.

## [](#cancelled-maintenance-job)Cancel a Maintenance Job

You can cancel maintenance jobs that you have scheduled. You cannot cancel a maintenance job while it's **Running**.

You cannot cancel maintenance jobs scheduled by Capella Support. When Support schedules a mandatory upgrade for your cluster, they cancel your previously scheduled maintenance upgrade. You can reschedule your maintenance job once the mandatory upgrade is complete. To cancel a support-initiated upgrade, [Create a Support Ticket](../support/manage-support.md#create-support-ticket).

To cancel a maintenance job you have scheduled:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  * Click your organization name and go to **Operational**.
  * Click your current project name or search for a project and go to **Operational**.
  * Expand the cluster breadcrumb and search for a cluster.
2. Select your cluster.
3. Go to **Settings** **Maintenance**.
4. Find the maintenance job you want to cancel in **Scheduled Maintenance Jobs**.
5. Go to **More Options (︙)** **Cancel Scheduled Upgrade**.
6. Confirm that you want to cancel the maintenance job and click **Cancel Scheduled Upgrade**.

To view canceled maintenance jobs, see [View Past Maintenance Jobs](#view-past-maintenance).

## [](#set-preferred-time)Set a Preferred Time for all Maintenance Jobs

You can set a preferred time and day of the week for future maintenance jobs to be scheduled. This does not reschedule maintenance jobs that are already scheduled on the **Maintenance** page.

When an upgrade or maintenance becomes available, Capella attempts to schedule the maintenance job at your preferred time and day of the week. The preferred time is not a guarantee. If it's not possible to schedule the maintenance job at your preferred time, the cluster is scheduled at any time within the upgrade window.

To set a preferred maintenance day and time for all upcoming jobs:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  * Click your organization name and go to **Operational**.
  * Click your current project name or search for a project and go to **Operational**.
  * Expand the cluster breadcrumb and search for a cluster.
2. Select your cluster.
3. Go to **Settings** **Maintenance**.
4. Click **Set Maintenance Schedule**.
5. Click **Enable a preferred start time for cluster maintenance**.
6. In the **Day of the Week** list, select the day you want scheduled maintenance to occur.
7. In the **Time** field, enter the time you want scheduled maintenance to occur.  
Your upgrade time is local to you. Enter a time in the HH:mm format. For example: `14:30`.
8. Click **Save**.

## [](#next-steps)Next Steps

For more information about managing your cluster, see:

* [Turn Clusters Off or On](off-on-database.md)
* [Schedule Cluster On or Off](off-on-schedule.md)
* [Back Up and Restore An Entire Cluster](cloud-snapshots.md)
* [Modify a Paid Cluster](modify-database.md)
* [Cluster Scaling](scale-database.md)