---
title: Upgrade App Services
description: Scheduling for Capella App Services.
editUrl: https://github.com/couchbaselabs/docs-capella-app-services/edit/main/modules/ROOT/pages/maintenance/upgrading-app-services.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/app-services/maintenance/upgrading-app-services.html)

# Upgrade App Services

> Scheduling for Capella App Services. 

> [!IMPORTANT]
> From App Services 3.1.8, all configurations previously defined in bucket mode will now be under the **\_default** scope and collection. For example, Access Control functions or Import Filters created in bucket mode prior to App Services 3.1.8 will be listed under the **\_default** scope and collection.

The underlying framework used by App Services will require periodic upgrading as new versions are rolled out. These upgrade maintenance jobs can be scheduled on a per-App Service basis to ensure that they occur at the time best suited to maintain high availability for your App Services. You can also log incidents and maintenance requests.

## [](#app-services-version-support)App Services Version Support

You can deploy and upgrade clusters to new versions of the App Services framework as they become available.

In general, releases follow this pattern:

| Release   | Introduces                            |
| --------- | ------------------------------------- |
| **Major** | Major new features and functionality. |
| **Minor** | Some new features or improvements.    |
| **Patch** | Essential fixes and improvements.     |

The App Service framework versions offered in Capella are supported until they reach the end of maintenance. This support typically aligns with the full maintenance lifespan of the major or minor version provided by Couchbase.

To provide secure and reliable service, the version of the App Service framework deployed will be the latest available patch version. You can expect to be upgraded to the latest patch version shortly after it becomes available on Capella.

When maintenance or an upgrade is scheduled, you can choose to upgrade your App Service framework at any time before the scheduled date. When the scheduled time is reached, the framework is upgraded automatically. The notice that Capella aims to provide varies depending on the nature of the upgrade.

## [](#app-services-upgrade-timeframes)App Services Upgrade Timeframes

Similar to cluster maintenance jobs, App Service maintenance jobs have 2 different kinds of timeframes:

* **Notice period**: the interval of time between when the maintenance job is created (and maintenance notifications are sent) and the scheduled upgrade date (target start time). You receive notification emails when Capella schedules an upgrade maintenance job. For more information, see [Manage Upgrade Email Notifications](#upgrade-email-notifications).
* **Upgrade window**: the interval of time during which the maintenance job can begin. This time is dependent on the upgrade type and begins after the notice periods ends, allowing customers to adjust the maintenance schedule as needed. For more information, see [Reschedule a Maintenance Job](#reschedule-maintenance-job).

For more details about the different types of App Service maintenance jobs and their respective timeframes, see the following table:

| Upgrade or Maintenance Type                             | Description                                                                                                          | Timeframe                                                                                                                                                                                            |
| ------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Critical Upgrade**                                    | An upgrade done in response to an urgent bug, vulnerability, or other issue impacting cluster health or performance. | None.                                                                                                                                                                                                |
| **Routine Maintenance or App Services Framework Patch** | A new App Services patch version or routine image upgrades.                                                          | A typical App Service maintenance job has a 1 week notice period. It includes an upgrade window of 1 week after the notice period ends, allowing customers to adjust the upgrade schedule as needed. |
| **App Services Framework Minor Release**                | A new App Services minor version release.                                                                            | From launch on Capella to end of support on Capella.                                                                                                                                                 |
| **App Services Framework Major Release**                | A new App Services major release version.                                                                            | From launch on Capella to end of support on Capella.                                                                                                                                                 |

> [!NOTE]
> A shorter than best practice period might apply depending on particular circumstances.

## [](#maintenance-jobs)Maintenance Jobs

All upgrades and maintenance patches have a target start time. Capella aims to start the maintenance of your App Services at this time. However, maintenance jobs are sometimes delayed when the App Service cannot be upgraded. For more information, see [Maintenance and App Service Status](#maintenance-App-Service-status).

For each individual maintenance job, you can:

* Create and change the job schedule.
* View the maintenance job type, status, and scheduled upgrade time.
* Review the new features or changes for the maintenance job.
* Create a support ticket.

When a maintenance job runs, the App Service is moved to a `pending` state. Maintenance redeployments are not time-bound, and the time taken varies depending on the size of framework upgrade.

> [!IMPORTANT]
> Maintenance and App Service Status
> 
> Keep the following in mind while using your App Service:
> 
> * Your App Service must be in a **Healthy** state and [turned on](../app-services/turn-on-off.md#turn-app-services-onoff) to run an upgrade.
> * If your App Service is turned off or in an unhealthy state when a maintenance job is set to run, Capella automatically reschedules the maintenance job for an hour later. The maintenance can be repeatedly rescheduled until the App Service is turned on and healthy.
> * If you try to [turn your App Service off on-demand](../app-services/turn-on-off.md) and the App Service is running or due to run maintenance within the next hour, Capella returns an error and the App Service does not turn off.
> * You cannot schedule a maintenance job when your App Service is turned off. Turn your App Service back on to schedule an upgrade maintenance job.

### [](#view-individual-maintenance-jobs)View Individual Maintenance Jobs

You can view current and scheduled maintenance jobs for your App Service:

1. Go to **App Services** and select your App Service.
2. Click through **Settings** **Maintenance**.
3. View your maintenance jobs in **Scheduled Maintenance Jobs**.

Maintenance job statuses are pending, running, completed, and cancelled.

The **Created By** field indicates whether the maintenance job was scheduled by a user or by the Capella Support team.

### [](#schedule-maintenance-jobs)Schedule a Maintenance Job

When certain upgrade maintenance jobs become available, if you have the [Organization Owner](../../cloud/organizations/organization-user-roles.md#organization-role-organization-owner) or [Project Owner](../../cloud/projects/project-roles.md#project-owner-role) role, you can schedule these jobs for your App Service.

> [!NOTE]
> Scheduling Upgrades
> 
> You cannot self-schedule all maintenance jobs for your App Service. Some maintenance jobs can only be scheduled by Capella Support.
> 
> To see if a maintenance job is available for you to schedule:
> 
> 1. Go to **App Services** and find your App Service.
> 2. In the **Activities** column, look for the upgrade icon ![arrow circle up](../_images/maintenance/arrow_circle_up.png). This indicates an upgrade is available.

To schedule a maintenance job for your App Service:

1. Go to **App Services** and find your App Service.
2. Choose one of the following options:

  1. Go to **More Options (︙)** **Upgrade App Service** and click **Upgrade App Service**.
  2. Select your App Service and click **App Service Upgrade**.
3. Select the upgrade version for your App Service.
4. Choose one of the following options:

  1. To start the maintenance job to start within the next 10 minutes, click **Upgrade Now**.
  2. To schedule your maintenance job for a later time, click **Schedule Upgrade**.  
  Enter a date and time and click **Save**.

### [](#reschedule-maintenance-job)Reschedule a Maintenance Job

You can reschedule any job that you have scheduled or any maintenance jobs in the list that are `Pending`.

You can reschedule the target start time for an individual maintenance job or choose to run the maintenance job immediately. However, maintenance jobs cannot be deferred indefinitely because each maintenance job has a latest possible upgrade date.

To reschedule your maintenance job:

1. Go to **Settings** **Maintenance**
2. Find the maintenance job in **Scheduled Maintenance Jobs**.
3. Choose one of the following options:

  1. To schedule a maintenance job to start within the next 10 minutes, click **Run Now**.
  2. To schedule a maintenance job for a later time, go to **More Options (︙)** **Change Upgrade Schedule**.  
  Enter a new date and time and click **Save**.  
  If another job is in progress, then the selected job will be queued to run at a later time.

You cannot reschedule a maintenance job while it’s **Running**.

> [!NOTE]
> When you create a new maintenance schedule for your App Service, you’re overriding the existing one. This cancels the previous maintenance job and applies the new schedule you set.

### [](#cancelled-maintenance-job)Cancel a Maintenance Job

You can cancel maintenance jobs that you have scheduled. You cannot cancel a maintenance job while it’s **Running**.

You cannot cancel maintenance jobs scheduled by Capella Support. When Couchbase Support schedules a mandatory upgrade for your App Service, they cancel your previously scheduled maintenance upgrade. You can reschedule your upgrade once the mandatory upgrade is complete. To cancel a support-initiated upgrade, [Create a Support Ticket](#support:manage-support.adoc#create-support-ticket).

To cancel a maintenance job that you have scheduled:

1. Go to **Settings** **Maintenance**.
2. Find the maintenance job in **Scheduled Maintenance Jobs**.
3. Go to **More Options (︙)** **Cancel Scheduled Upgrade**.
4. Confirm that you want to cancel the maintenance job and click **Cancel**.

To view canceled maintenance jobs:

1. Go to **Settings** **Maintenance**.
2. In **Past Maintenance Jobs**, click **Go to Past Maintenance Jobs**.

### [](#set-the-day-and-time-for-future-maintenance-updates)Set the Day and Time for Future Maintenance Updates

You can set a preferred time and day of the week for future maintenance jobs to be scheduled. This does not reschedule maintenance jobs that are already scheduled on the Maintenance tab.

When an upgrade or maintenance becomes available, Capella attempts to schedule the maintenance at your preferred time and day of the week. The preferred time is not a guarantee. If it’s not possible to schedule the maintenance at your preferred time, the job is scheduled at any time within the maintenance window.

To set a preferred maintenance day and time for all upcoming jobs:

1. Go to **Settings** **Maintenance**.
2. Click **Set Maintenance Schedule**.
3. Click **Enable a preferred start time for App Service maintenance**.
4. Set the date and time you want scheduled maintenance to occur.  
Your upgrade time is local to you. Enter a time in the HH:mm format. For example: `14:30`.
5. Click **Save**.

### [](#upgrade-email-notifications)Manage Upgrade Email Notifications

When a maintenance job is scheduled, email notifications are sent to:

* [Organization Owners](../../cloud/organizations/organization-user-roles.md#organization-role-organization-owner) where one or more App Services in their organization is scheduled for maintenance.
* [Project Owners](../../cloud/projects/project-roles.md#project-owner-role) and [Cluster Managers](../../cloud/projects/project-roles.md#project-cluster-manager-role) where at least one App Service linked to a cluster they have access to is scheduled for maintenance.

Capella sends these emails when the maintenance job is scheduled and, when applicable, 1 week, 24 hours, and 1 hour prior to the target start time. These notifications include details about the App Service, the upgrade, and the upgrade schedule.

> [!NOTE]
> Those with notifications turned OFF will not receive these emails. For more information about how to turn your email notifications on or off, see [Get Alerts through Email](../../cloud/clusters/monitoring/alerts.md#get-alerts-through-email).

### [](#create-support-tickets)Create Support Tickets

You can create a support ticket for any App Services upgrade:

1. Go to **Settings** **Maintenance**.
2. Find the maintenance job in **Scheduled Maintenance Jobs**.
3. Go to **More Options (︙)** **Create Support Ticket**.

Fill in as much detail as possible as to the nature of the problem, including the name of the project and cluster linked to your App Service. If you have any information held in files, such as service logs, then drop them into the `Choose a File` box for uploading.

## [](#access-app-services-maintenance-activity-logs)Access App Services Maintenance Activity Logs

Log entries for App Services maintenance are listed in the cluster activity logs for the cluster running your App Services.

Select the cluster running your App Service and navigate to the **Activity Log** page.

You can select a log entry to see more details, and raise a support ticket if required.

To learn more about activity logs, see [Activity Logs](../../cloud/clusters/monitoring/activity-log.md)