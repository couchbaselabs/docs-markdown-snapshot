---
title: Upgrading a Cluster
description: Maintenance jobs are scheduled to run upgrades on your cluster.
  Capella upgrades help provide a reliable service with the latest features.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/upgrade-database.adoc
  xref: xref:cloud:clusters:upgrade-database.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/clusters/upgrade-database.html)

# Upgrading a Cluster

> Maintenance jobs are scheduled to run upgrades on your cluster. Capella upgrades help provide a reliable service with the latest features. 

[Maintenance jobs](#maintenance-jobs) can be optional and run through self-service, or mandatory and initiated by Capella Support.

When a maintenance job is scheduled to upgrade your operational cluster, Capella sends you [email notifications](#upgrade-email-notifications).

## [](#server-version-support)Couchbase Server Version Support

Couchbase Capella supports the following Couchbase Server versions for new clusters:

| Status           | Available Version                                                      |
| ---------------- | ---------------------------------------------------------------------- |
| Latest release   | [Couchbase Server 8.0](../../server/current/release-notes/relnotes.md) |
| Previous release | [Couchbase Server 7.6](../../server/7.6/release-notes/relnotes.md)     |

## [](#database-upgrade-timeframes)Cluster Upgrade Policy

Couchbase Capella runs the following types of [maintenance jobs](#maintenance-jobs) on your cluster:

* [Couchbase Server Version Upgrades](#server-release)
* [Critical Upgrades](#critical)

These maintenance jobs might be scheduled by you through self-service, or scheduled by Couchbase Support. Maintenance jobs scheduled by Couchbase Support are mandatory. Mandatory maintenance jobs have both a notice period and an upgrade window:

* **Notice period**: the timeframe between when the maintenance job is scheduled (and maintenance notifications are sent) and the scheduled upgrade date (target start time). You receive notification emails when Capella schedules a maintenance job. For more information, see [Maintenance Email Notifications](#upgrade-email-notifications).
* **Upgrade window**: the timeframe during which the maintenance job can begin. This time is dependent on the upgrade type and begins after the notice period ends. NOTE: Your free tier operational cluster will receive Couchbase Server version upgrades at Couchbase's convenience. Free tier upgrades might not follow the same upgrade timeframe as paid operational clusters.

### [](#server-release)Couchbase Server Version Upgrades

Couchbase Server version maintenance jobs for new releases can be 1 of the following types of release:

| Release                  | Introduces                            |
| ------------------------ | ------------------------------------- |
| **Major**                | Major new features and functionality. |
| **Minor**                | Some new features or improvements.    |
| **Maintenance or Patch** | Essential fixes and improvements.     |

All major and minor Couchbase Server releases on Capella clusters receive regular maintenance patches for 36 months (3 years) from their general availability (GA) date. You'll be notified 6 months before your cluster's Couchbase Server version is no longer supported, to give you time to upgrade to the next supported version. When a cluster's Couchbase Server version is no longer supported, Couchbase Support works with you to upgrade your cluster to the latest major or minor version.

After a Couchbase Server version has reached the end of its support period, you can no longer deploy new clusters with that Server version. The version no longer receives OS upgrades or security patches, and there's no SLA guarantee for clusters running that version.

Major and minor version maintenance jobs often introduce new features or functionality to your cluster. Couchbase recommends [testing your application](upgrade-best-practices.md#test-application) with new major and minor versions to make sure your application stays compatible with your cluster.

Most patch release maintenance jobs can be scheduled by you at a time that works best for your needs. Couchbase recommends always scheduling any available optional self-service maintenance jobs for a Couchbase Server version upgrade as soon as possible. For more information, see [Schedule a Maintenance Job](manage-maintenance.md#schedule-maintenance-jobs).

### [](#critical)Critical Upgrades

The Couchbase Support team schedules maintenance jobs for any critical updates, including security patches, OS patches, fixes, or version compliance upgrades. These upgrades are required, but can be rescheduled to any time within the provided upgrade window. By default, Capella chooses a maintenance time during your [preferred maintenance time](manage-maintenance.md#set-preferred-time).

Couchbase aims to provide a 1-2 week notice period for critical upgrades, before providing an upgrade window of 2-4 weeks. Couchbase reserves the right to adjust notice periods and upgrade windows based on how critical the upgrade maintenance job is to your cluster's health, security, and stability.

## [](#maintenance-jobs)Maintenance Jobs

All maintenance jobs have a target start time. Capella aims to start your cluster upgrade at this time. However, maintenance jobs are sometimes delayed when the cluster cannot be upgraded. For more information, see [Maintenance and Cluster Status](#maintenance-cluster-status).

When a maintenance job runs, the cluster is moved to a redeploying state while nodes are rebalanced to apply the maintenance changes. Maintenance redeployments are not time-bound, and the time taken varies depending on the size of the cluster, volume of data, and load. Couchbase Capella clusters are designed to remain available throughout the upgrade. Cluster reconfiguration options are not available during an upgrade, though data tools remain accessible in the Capella UI.

> [!CAUTION]
> Single Node clusters may experience downtime during upgrades. Since there are no data replicas, any failure during the upgrade process can lead to service disruption. It's recommended to use Single Node clusters for prototyping or learning purposes. For production use cases, configure a Multi-Node cluster. To scale out your Single Node cluster, see [Modify a Paid Cluster](modify-database.md).

For each individual maintenance job, you can:

* Create and change the job schedule.
* View the maintenance job type, status, and scheduled upgrade time.
* Review the new features or changes for the maintenance job.

You can review all current and past scheduled maintenance jobs that have run on the cluster. For more information, see [View Past Maintenance Jobs](manage-maintenance.md#view-past-maintenance) or [View Current and Scheduled Maintenance Jobs](manage-maintenance.md#view-current-maintenance). Events related to maintenance jobs on your cluster are also recorded in the [Activity Log](monitoring/activity-log.md).

For more information about how to manage maintenance on your cluster, see [Manage Cluster Maintenance Jobs](manage-maintenance.md).

### [](#maintenance-cluster-status)Maintenance and Cluster Status

[Turning your cluster on and off on-demand](off-on-database.md) or [on a schedule](off-on-schedule.md) can affect maintenance jobs for your cluster.

Keep the following in mind while using scheduled or on-demand on/off operations on your cluster:

* Your cluster must have a [Healthy](scale-database.md#cluster-status) scaling status and be [turned on](off-on-database.md#turn-cluster-onoff) to run an upgrade.
* If your cluster is turned off or in an unhealthy state when a maintenance job is set to run an upgrade, Capella automatically reschedules the maintenance job for an hour later. The maintenance is repeatedly rescheduled until the cluster is on and healthy.
* Even when your cluster is turned off, you can schedule a maintenance job to run an upgrade once the cluster is turned on. [Manually turn your cluster back on](off-on-database.md#turn-cluster-onoff) if you want to **Upgrade Now**.
* If you have [scheduled your cluster to turn off](off-on-schedule.md) and the cluster is running or due to run an upgrade within the next hour, Capella does not turn off the cluster. The cluster will not turn off until the next scheduled off event in your schedule.
* If you try to [turn your cluster off on-demand](off-on-database.md#turn-cluster-onoff) and the cluster is running or due to run an upgrade within the next hour, Capella returns an error and the cluster does not turn off.

### [](#upgrade-email-notifications)Maintenance Email Notifications

When a maintenance job is scheduled, email notifications are sent to:

* [Organization Owners](../organizations/organization-user-roles.md#organization-role-organization-owner) where one or more clusters in their organization is scheduled for maintenance.
* [Project Owners](../projects/project-roles.md#project-owner-role) and [Cluster Managers](../projects/project-roles.md#project-cluster-manager-role) where at least 1 cluster in a project they have access to is scheduled for maintenance.

Capella sends these emails when the maintenance job is scheduled and, when applicable, 1 week, 24 hours, and 1 hour prior to the target start time. These notifications include details about the cluster, the upgrade, and the upgrade schedule.

> [!NOTE]
> Those with notifications turned off will not receive these emails. For more information about how to turn your email notifications on or off, see [Get Alerts through Email](monitoring/alerts.md#get-alerts-through-email).

## [](#see-also)See Also

* [Manage Cluster Maintenance Jobs](manage-maintenance.md)
* [Turn Clusters Off or On](off-on-database.md)
* [Schedule Cluster On or Off](off-on-schedule.md)
* [Upgrade App Services](../../app-services/maintenance/upgrading-app-services.md)
* [Modify a Paid Cluster](modify-database.md)
* [Cluster Scaling](scale-database.md)
* [Sizing a Cluster](sizing.md)