---
title: Request Prompt Action for Cluster Recovery
description: You can choose to authorize Couchbase Capella Support to
  automatically take remedial actions to a specific cluster, in case a failure
  is detected.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/billing/pages/support-pre-auth.adoc
  xref: xref:cloud:billing:support-pre-auth.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/billing/support-pre-auth.html)

# Request Prompt Action for Cluster Recovery

> You can choose to authorize Couchbase Capella Support to automatically take remedial actions to a specific cluster, in case a failure is detected. 

## [](#about-cluster-recovery-authorization)About Cluster Recovery Authorization

Use the **Request prompt action for cluster recovery** feature from the **Settings** tab of a deployed cluster This authorization allows the Capella Support Team to take any necessary, time-sensitive actions to recover a failed or failing cluster as soon as possible.

If you enable this setting, Capella Support does not wait for your explicit permission to try and recover your cluster and any linked App Services. If you have not deployed App Services with your cluster, this authorization still applies to any future App Services deployments.

> [!NOTE]
> This setting is enabled by default when you create a new cluster.

Capella Support will only make changes to your cluster if you enable the cluster recovery authorization, and a delay in action might result in severe consequences to your cluster App Services. You can [Review Actions Taken By Capella Support](#review-support) at any time.

For more information about how to change the authorization on an existing cluster, see <<change-auth,Enable Cluster Recovery Authorization for a Cluster.

### [](#example-actions-capella-support-can-take-on-a-cluster)Example Actions Capella Support Can Take On A Cluster

If you enable the cluster recovery authorization, Couchbase Capella support may do any of the following to try and recover your cluster and any linked App Services:

* Increase storage size on disks.
* Increase compute resources (CPU and RAM) on nodes.
* Add a new node.
* Add a new disk.
* Create another cluster with the same topology, restored from the last known backup.
* Create another cluster with increased storage and compute resources, restored from the last known backup.

> [!NOTE]
> Adding storage or compute resources to your cluster could result in additional costs to you.

### [](#what-actions-capella-support-cannot-take-on-a-cluster)What Actions Capella Support Cannot Take On A Cluster

If you enable the cluster recovery authorization, the Capella Support team still cannot view or change the data on your cluster

## [](#change-auth)Enable Cluster Recovery Authorization for a Cluster

> [!NOTE]
> You must have the `Organization Owner`, `Project Owner`, or `Cluster Manager` role to change the cluster recovery authorization for a cluster

You must set this permission for each cluster in your organization. This setting also applies to any current or future App Services linked to the cluster.

To change the cluster recovery authorization for an existing cluster

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select the cluster where you want to make changes.
3. Go to **Settings** **General**.
4. Under **Request prompt action for cluster recovery**, choose **Yes**.
5. Click **Save**.

## [](#review-support)Review Actions Taken By Capella Support

All actions taken by Capella Support create a record in the Capella Activity Log.

For more information about how to view the Activity Log, see [View Activity Logs](../clusters/monitoring/activity-log.md).

## [](#see-also)See Also

* [Create a Database](../clusters/create-database.md)
* [Modify a Database](../clusters/modify-database.md)
* [View Activity Logs](../clusters/monitoring/activity-log.md)