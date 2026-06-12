---
title: Upgrade Best Practices
description: Each Capella cluster runs a specific version of Couchbase Server.
  Upgrading a cluster means upgrading its underlying Server version, which may
  include enhancements or changes to performance and compatibility. These best
  practices help ensure a secure and smooth upgrade process.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/upgrade-best-practices.adoc
pubDate: 2026-06-12T16:31:57.907Z
link: xref:cloud:clusters:upgrade-best-practices.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/clusters/upgrade-best-practices.html)

# Upgrade Best Practices

> Each Capella cluster runs a specific version of Couchbase Server. Upgrading a cluster means upgrading its underlying Server version, which may include enhancements or changes to performance and compatibility. These best practices help ensure a secure and smooth upgrade process. 

Use this page as a reference for methods and more information about how to apply best practices to your cluster upgrades.

Before upgrading your operational cluster with a patch, minor, or major release version, [back up your entire production cluster](#backup-cluster) and [review SDK compatibility](#sdk-compatibility).

For minor and major cluster upgrades, [test your application](#test-application) in a controlled staging environment. A [staging environment](#create-staging-cluster) lets you verify performance and compatibility while not disrupting your production workflow.

> [!NOTE]
> For any problems that occur during the testing and upgrade process of your staging or production cluster, [create a support ticket](../support/manage-support.md#create-support-ticket). For clusters that are community-supported only, use the Couchbase [forums](https://www.couchbase.com/forums/tag/couchbase-capella), [Discord channel](https://discord.com/invite/K7NPMPGrPk?utm%5Fsource=forums&utm%5Fmedium=pinnedpost&utm%5Fcampaign=discord) and [documentation](../get-started/intro.md) for support and feedback.

## [](#backup-cluster)Back Up Your Cluster

Before upgrading your operational cluster, you should [back up your entire cluster](cloud-snapshots.md). With a cluster backup, you can back up and restore an entire cluster and all of its buckets in a single backup. For more information, see [Back Up and Restore An Entire Cluster](cloud-snapshots.md).

Backups are a good security measure, minimizing the risk associated with the upgrade process. In a disaster recovery scenario, you'd have the option to restore your cluster backup and have backwards compatibility with the cluster versioning.

If you do not use scheduled cluster backups, manually take an on-demand cluster backup using the [Capella UI](take-cloud-snapshot.md#on-demand) or the [REST API](../management-api-reference/index.md#tag/Cloud-Snapshot-Backups-and-Restore).

## [](#sdk-compatibility)Review SDK Compatibility

SDK compatibility is necessary for upgrading your applications without encountering errors or downtime after the upgrade process.

For more information about SDK compatibility, see the [Couchbase Server Release Notes](../../server/current/release-notes/relnotes.md) of the maintenance release version you're upgrading your cluster to.

For minor or major version upgrades, you can test your current SDK with the new cluster release in a [staging environment](#create-staging-cluster). Deploy the same workflows or applications that use the SDK in your staging environment and make sure they work as expected with the new version of the cluster.

> [!NOTE]
> You should update the Couchbase SDK that your application uses to the latest patched version, and validate after upgrading.

## [](#test-application)Test Your Application

For minor and major release versions, test your application with the new upgrade on a staging cluster before applying it to production. This allows you to test how your application behaves before and after the upgrade, helping you identify potential issues in a controlled environment.

Use a staging cluster to mirror your production setup as closely as possible. Staging clusters can also be known as:

* QA clusters
* Test clusters
* Non-production clusters
* Lower clusters

[Upgrade](manage-maintenance.md#schedule-maintenance-jobs) your staging cluster to the minor or major release version available and test your application within this staging environment. If you do not have a staging cluster or need to update your staging environment, see [Create a Staging Cluster](#create-staging-cluster).

Run the necessary security, performance, compatibility, and operational tests with your application. Testing the upgrade allows you to verify if your application continues to function as expected in the new environment and does not introduce any regressions or unexpected behaviors.

If the tests are successful and you can confirm your application performs as expected with the upgrade, you can [upgrade your production cluster](manage-maintenance.md#schedule-maintenance-jobs).

### [](#create-staging-cluster)Create a Staging Cluster

Using a separate staging environment allows you to test new features and changes in a production-like setting, reducing the risk of unexpected errors after an upgrade.

Set up a staging cluster ahead of time. Run the same application, SDK, and Couchbase Server version as your production environment. This ensures that when a new minor or major release version becomes available on your cluster, you can go through the full upgrade process and verify your application's behavior before, during, and after the upgrade.

> [!CAUTION]
> If you wait to create your staging cluster until after a new release is available, you may only be able to deploy with the latest version of Couchbase Server. This means your staging environment will not match your current production version, making it difficult to accurately test how your application behaves throughout the upgrade process.
> 
> If you have any problems with testing an upgrade, [create a support ticket](../support/manage-support.md#create-support-ticket).

To create a staging environment:

1. [Create a cluster](create-database.md) and [configure its settings](databases.md) to mirror your production cluster as closely as possible.  
The settings you choose affect your staging environment's performance. The goal is to have it mimic the performance of your production environment.  
> [!TIP]  
> Your node and Service Group configurations should align with the volume of data you plan to replicate in your staging cluster.
2. Transfer your production cluster's data to your staging cluster. Do one of the following:

  1. Use the `cbbackupmgr` CLI tool to back up and restore data at the bucket level. This method does not restore a full cluster backup from your production cluster to your staging cluster. You must back up each individual bucket from your production cluster and restore them into pre-created buckets on your staging cluster. For more information, see [Back Up and Restore with Command Line Tools](cli-backup-restore.md)
  2. Restore a full cluster backup to your new staging cluster. For more information, see [Restore a Cluster Backup](restore-cloud-snapshot.md).  
> [!NOTE]  
> If you need your staging cluster to stay in sync with your production cluster, create a [one way XDCR replication](#clusters:xdcr:manage-xdcr-replications.adoc) to migrate your data between the clusters.
3. Connect your application to your staging cluster:

  * Connect your application from [SDK, cbsh, CLI, or IDE](../get-started/connect.md).
  * Connect your mobile and IoT applications with [App Services](#app-services:index.adoc).  
Test the application connection by verifying that you can read and write data to the staging cluster.

When a minor or major release version becomes available, use this staging cluster to [test the upgrade with your application](#test-application).

## [](#see-also)See Also

* [Upgrading a Cluster](upgrade-database.md)
* [Manage Cluster Maintenance Jobs](manage-maintenance.md)