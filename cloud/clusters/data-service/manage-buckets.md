---
title: Manage Buckets
description: Create, edit, and delete buckets to manage your data storage in a
  Capella operational cluster.
editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/data-service/manage-buckets.adoc
pubDate: 2026-03-26T05:14:31.984Z
link: xref:cloud:clusters:data-service/manage-buckets.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/clusters/data-service/manage-buckets.html)

# Manage Buckets

> Create, edit, and delete buckets to manage your data storage in a Capella operational cluster. 

A **bucket** is the named container in which you save your data. You may have up to 30 buckets in your cluster. You may organize the data within a bucket into different **collections**, according to content-type. A bucket's data may be [replicated](../xdcr/xdcr.md) across the cluster, to make sure that the data exists in multiple copies, and is highly available. A bucket's data may also be replicated across different clusters, potentially in different geographic locations.

The Capella UI defines buckets with default settings that support rapid prototyping and pre-production experimentation. For the subsequent design of sophisticated production systems, multiple configuration options are provided, to ensure heightened performance, integrity, and availability.

## [](#bucket-types)Bucket Types

Capella has two distinct bucket types:

* **Memory and Disk**: The bucket holds data in-memory and persists it to disk.
* **Memory Only**: The bucket holds data in-memory but does not persist it to disk.

For a detailed overview of buckets, see [Buckets](../../../server/current/learn/buckets-memory-and-storage/buckets.md) in the Couchbase Server documentation.

> [!WARNING]
> **Memory Only** buckets lose data during cluster restarts, whether planned or unplanned, and may also lose data due to concurrent failure of multiple nodes.

## [](#buckets-storage)Buckets and Storage

Couchbase Capella operational clusters store document data and metadata in append-only files. This format ensures consistent updates to files and reduces the risk of corruption. Every file change, including additions, modifications, or deletions, creates a new entry at the end of the file. Even when document deletion removes user data, the file temporarily grows in size because of the append-only format.

Capella periodically reduces file sizes through automated compaction. Automated compaction purges metadata items and runs other necessary maintenance tasks. During compaction, Capella removes any item marked as a deleted item, or tombstone, when its age exceeds a set purge age. The delay for deleting tombstones is necessary for replication consistency.

Automated compaction tasks and purging automatically run on Capella buckets. When database fragmentation reaches 30% for Couchstore buckets and 50% for Magma buckets, Capella triggers its automated compaction. Capella purges any items marked for deletion, or tombstones, that are more than 3 days old. A dedicated purge task also runs [purging](#buckets-storage) for Memory-Only buckets.

If the cluster links to an App Service, deleted or tombstoned documents remain in buckets for 60 days. This allows disconnected clients to sync deleted documents when they come back online within the 60 day window.

> [!TIP]
> The **Memory Only** bucket must be provisioned with enough memory to be able to restore from backups. For more information about backup and restore, see [Backup and Restore Data](../backup-restore.md).

## [](#access-bucket)Accessing Bucket Information

To create, modify, or delete buckets from the Capella UI, you must have the [Project Owner](../../projects/project-roles.md#project-owner-role) or [Cluster Manager](../../projects/project-roles.md#project-cluster-manager-role) role for the cluster's project. If you have the [Organization Owner](../../organizations/organization-user-roles.md#organization-role-organization-owner) role, you have `Project Owner` access.

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select your cluster.
3. Go to **Buckets**.

If you have not yet created a bucket, the **Create Bucket** button is displayed in the middle of the page, allowing you to create your first bucket. See [Create a Bucket](#add-bucket).

If you have already created one or more buckets, the **Buckets Summary** is displayed.

### [](#buckets-summary)Buckets Summary

The **Buckets Summary** is a table that lists all buckets in the cluster. It includes the following information about each bucket:

Bucket Name

Documents

Bucket Type

Storage Backend

Ops/Sec

Disk

Memory/Quota

Clicking on the name of a bucket opens the **Edit Bucket** page for that bucket. The page shows information about the bucket's current configuration. These details include conflict resolution, minimum durability level, replication, flush, and time to live settings. For more information, see [Modify a Bucket](#edit-bucket).

## [](#add-bucket)Prerequisites

> [!NOTE]
> Free Tier Limitations
> 
> If you're using a free tier operational cluster, you cannot create a bucket with advanced options. Free tier clusters can create only buckets with the memory and disk bucket type, and the Magma 128 vBucket storage backend option.

To create, modify, or delete buckets in a project, you need:

* The [Project Owner](../../projects/project-roles.md#project-owner-role) or [Cluster Manager](../../projects/project-roles.md#project-cluster-manager-role) role for your cluster's project. If you have the [Organization Owner](../../organizations/organization-user-roles.md#organization-role-organization-owner) role, you have `Project Owner` access.

## [](#create-a-bucket)Create a Bucket

> [!IMPORTANT]
> XDCR between Magma and Couchstore
> 
> Only Couchbase Server 8.0 and later supports XDCR replication between buckets with different numbers of vBuckets.
> 
> Couchstore buckets use 1024 vBuckets, while Magma buckets can use either 128 or 1024 vBuckets. To create an XDCR replication from a bucket on a cluster using Couchbase Server 7.6 or earlier, you must use Magma with 1024 vBuckets or Couchstore.

To create a bucket, choose 1 of the following options:

1. Go to **Data Tools** for a quick bucket setup with no advanced settings.
2. Go to **Buckets** to configure a bucket with advanced settings such as storage backends, durability, and replica count.

* Data Tools
* Buckets

1. Go to **Operational** and click your cluster name.
2. Go to **Data Tools**.
3. Click **Bucket, Scope, Collection**.
4. In the **Bucket** field:

  1. Select **New**.
  2. Enter a name for the new bucket. A bucket name can only contain upper or lower case letters, numbers, underscores (`_`), periods (`.`), dashes (`-`), and percentages (`%`). You cannot set a bucket name that exceeds 100 characters in length. You cannot change a bucket name after you create a bucket.
  3. Enter a memory quota for the bucket.  
  > [!IMPORTANT]  
  > Default storage backend  
  >  
  > When using Couchbase Server 8.0 or later, the default storage backend is Magma, which needs 100 MiB with 128 vBuckets or 1 GiB with 1024 vBuckets. Couchstore needs a minimum of 100 MiB. For help with choosing the right storage backend for your bucket, see [Storage Engines](storage-engines.md).  
  Use the memory allocation graph to view the memory allocated to other buckets in the cluster, and the total amount of memory you can allocate to a new bucket.  
  > [!NOTE]  
  > The total memory quota for a bucket equals the number of data nodes in its Service Group multiplied by the memory quota you specify. If you change the number of data nodes in your Service Group, the total memory allocated to the bucket changes as well. For example, if you deploy the Data Service on 3 nodes and create a bucket with a 100 MiB memory quota, each node has 100 MiB. This gives the bucket a total of 300 MiB memory. [Scaling your cluster](../scale-database.md) up to 6 nodes with 100 MiB per node increases the bucket's maximum memory to 600 MiB. Scaling a cluster down to reduce the number of nodes, also reduces the total memory quota for the bucket. If you do not have enough memory allocated to a bucket for your data, you can encounter performance issues.  
  For more information about memory management in Capella, see [Buckets and Storage](#buckets-storage).
  4. In the **Scope** and **Collection** fields, enter names for the bucket's first scope and collection, or select **Use system generated \_default for scope and collection**.
  5. Click **Create**.

You can [modify your bucket settings](#edit-bucket) at any time.

1. Go to **Operational** and click your cluster name.
2. Go to **Buckets**.
3. Click **Create Bucket**.
4. In the **Bucket Name** field, enter a name for the new bucket. A bucket name can only contain upper or lower case letters, numbers, underscores (`_`), periods (`.`), dashes (`-`), and percentages (`%`). You cannot set a bucket name that exceeds 100 characters in length. You cannot change a bucket name after you create a bucket.
5. In the **Memory Quota (MiB)** field, enter a memory quota for the bucket.  
> [!IMPORTANT]  
> Default storage backend  
>  
> When using Couchbase Server 8.0 or later, the default storage backend is Magma, which needs 100 MiB with 128 vBuckets or 1 GiB with 1024 vBuckets. Couchstore needs a minimum of 100 MiB. For help with choosing the right storage backend for your bucket, see [Storage Engines](storage-engines.md).  
Use the memory allocation graph to view the memory allocated to other buckets in the cluster, and the total amount of memory you can allocate to a new bucket.  
> [!NOTE]  
> The total memory quota for a bucket equals the number of data nodes in its Service Group multiplied by the memory quota you specify. If you change the number of data nodes in your Service Group, the total memory allocated to the bucket changes as well. For example, if you deploy the Data Service on 3 nodes and create a bucket with a 100 MiB memory quota, each node has 100 MiB. This gives the bucket a total of 300 MiB memory. [Scaling your cluster](../scale-database.md) up to 6 nodes with 100 MiB per node increases the bucket's maximum memory to 600 MiB. Scaling a cluster down to reduce the number of nodes, also reduces the total memory quota for the bucket. If you do not have enough memory allocated to a bucket for your data, you can encounter performance issues.  
For more information about memory management in Capella, see [Buckets and Storage](#buckets-storage).
6. (Optional) Configure advanced settings for your bucket, or accept the default values. For more information about advanced bucket settings, see [Configure Advanced Bucket Settings](#advanced-settings).  
> [!NOTE]  
> You cannot configure any advanced settings for a bucket on a free tier operational cluster. [Upgrade your account](../../billing/upgrade-account.md) to access all bucket customization options.
7. Click **Create Bucket**.

### [](#advanced-settings)Configure Advanced Bucket Settings

> [!NOTE]
> You can only configure advanced settings if you create a bucket through the **Buckets** tab.

To configure advanced settings:

1. Expand **Show Advanced Settings**.
2. Choose a **Bucket Type**:

  * (Default) **Memory and Disk**: Best if you need to persist your data to disk.
  * **Memory Only**: Best if your data does not require disk-persistence and you can maintain it in-memory only.  
> [!NOTE]  
> Memory-Only Limitations  
>  
> You cannot use a memory only bucket with [App Endpoints](../../../app-services/app-endpoints/creating-an-app-endpoint.md). You also cannot [turn off a cluster](../off-on-database.md) with a memory only bucket, or [use a cluster on or off schedule](../off-on-schedule.md).  
You cannot change your bucket type after you create a bucket. For more information about bucket types, see [Bucket Types](../../../server/current/learn/buckets-memory-and-storage/buckets.md#bucket-types) in the Couchbase Server documentation.
3. For a memory and disk bucket, choose a **Storage Backend**:

  * (Default) **Magma**: Best if your dataset is large in relation to available memory. When using Magma, you must choose the number of vBuckets for the bucket. If you can allocate at least 1 GiB memory per node to your bucket, choose 1024 vBuckets for Magma for better performance at scale.

    * (Default) **128 vBuckets**: For datasets that require a minimum of 100 MiB memory.
    * **1024 vBuckets**: For datasets that require a minimum of 1 GiB memory.
  * **Couchstore**: Best if your dataset is small and fits into memory.  
You cannot change your storage backend after you create a bucket.  
For more information about the differences between Couchstore and Magma, see [Storage Engines](storage-engines.md).  
> [!NOTE]  
> Capella allocates the memory quota specified for a bucket on a per-node basis. The total memory quota for the bucket equals the number of data nodes in the Service Group multiplied by the specified memory quota. If the number of Data Service nodes in the cluster changes, the total memory allocated to the bucket changes based on the new number of data nodes.  
>  
> **Example:**When Data Services deploy on 3 nodes in a Capella cluster and Capella creates a new bucket, the bucket memory quota defaults to 100 MiB. This setting means Capella allocates 100 MiB to each node, giving the bucket a total of 300 MiB memory. When the cluster scales to run Data Services on 6 nodes at 100 MiB, this gives 600 MiB maximum memory for the bucket.  
> [!IMPORTANT]  
> XDCR between Magma and Couchstore  
>  
> Only Couchbase Server 8.0 and later supports XDCR replication between buckets with different numbers of vBuckets.  
>  
> Couchstore buckets use 1024 vBuckets, while Magma buckets can use either 128 or 1024 vBuckets. To create an XDCR replication from a bucket on a cluster using Couchbase Server 7.6 or earlier, you must use Magma with 1024 vBuckets or Couchstore.
4. Choose the **Conflict Resolution** method for the bucket:

  * Select **Sequence Number** to use the document with the higher sequence number in case of a conflict between documents.
  * Select **Timestamp** to use the document with the most recent timestamp.  
  Document conflicts occur during [XDCR](../xdcr/xdcr.md#conflict-resolution) when a document has been modified differently in different locations, requiring one version of the document to be kept and the other discarded. You cannot change your conflict resolution method after you create a bucket. For more information about conflict resolution, see [XDCR Conflict Resolution](../xdcr/xdcr.md#conflict-resolution).
5. (**Memory Only Buckets** Only) Choose an **Ejection Policy** for the bucket:

  * Select **NRU** (Not Recently Used) to make Capella remove documents with the lowest access frequency when the bucket's memory reaches capacity. This reclaims memory for saving new documents.
  * Select **No Ejection** to make Capella keep all documents when the bucket's memory reaches capacity, and force new document save attempts to fail.  
  You cannot change your ejection policy after you create a bucket. For more information about ejection, see [Ejection Policy](../../../server/current/learn/buckets-memory-and-storage/storage-settings.md#storage-settings-ejection-policy) in the Couchbase Server documentation.
6. Choose the **Minimum Durability Level** for each write to the bucket:

  * **None**: Apply no durability level. This option is available for **Memory and Disk** and **Memory Only** buckets.
  * **Replicate to Majority**: Mutations replicate to a majority of the Data Service nodes, without persistence. This option is available for **Memory and Disk** and **Memory Only** buckets.
  * **Majority and Persist to Active**: Mutations replicate to a majority of the Data Service nodes. They're also persisted—​written and synchronized to disk—​on the node hosting the active vBucket for the data. This option is available for **Memory and Disk** buckets only.
  * **Persist to Majority**: Mutations replicate to a majority of the Data Service nodes. They're also persisted—​written and synchronized to disk—​on all nodes. This option is available for **Memory and Disk** buckets only.  
  Durability helps to improve data integrity during failures. For more information about durability in Couchbase clusters, see [Durability](../../../server/current/learn/data/durability.md) in the Couchbase Server documentation.  
> [!NOTE]  
> Limitations  
>  
> For single node operational clusters, the **Minimum Durability Level** is automatically set to **None**. You cannot change this setting.
7. Set the **Number of Replicas**. Based on the number nodes in your cluster, you can choose to create 1 to 3 replica copies of the data stored in this bucket. If you do not have the required number of nodes for a specific number of replicas, that option is unavailable.  
> [!NOTE]  
> Limitations  
>  
> For single node operational clusters, the **Number of Replicas** is automatically set to 0\. You cannot change this setting.
8. Turn **Cross Cluster Versioning** (CCV) on or off. Cross Cluster Versioning enables advanced XDCR capabilities, including mobile active replication. When enabled, XDCR stores additional metadata, called the Hybrid Logical Vector (HLV), in the document extended attributes (XATTRs) for each document it processes.  
CCV enables the following advanced replication scenarios when App Services Endpoints link to buckets:

  * **Bi-directional and uni-directional XDCR** when both buckets are linked with an App Endpoint.
  * **Bi-directional XDCR** when either bucket is linked with an App Endpoint.  
CCV is automatically enabled when setting up mobile active replication. You cannot turn off CCV after enabling it.
9. Turn **Flush** on or off. Flushing a bucket deletes all of its data permanently.  
> [!CAUTION]  
> To protect against inadvertent data loss, turn off Flush on production clusters.
10. Turn **Time to Live** (TTL) on or off.  
Enabling TTL allows you to set a maximum amount of time for which a document can exist before it's automatically deleted. When enabled, this setting allows you to specify the time-period in seconds, minutes, hours, days, or weeks. This setting applies to all collections in the bucket unless you configure a collection's TTL to a non-zero value.
11. Choose a backup schedule for the bucket according to the relative importance of the workload and data.

  1. Select **Do Not Backup** to not schedule any backups.  
  > [!WARNING]  
  > **Do Not Backup** is not recommended for production clusters. To avoid data loss, you should regularly back up a production cluster.  
  To set a weekly incremental schedule:
  2. Choose **Set Weekly Schedule**.
  3. Choose the **Day of the week** when you want Capella to take the full backup. The default value is `Sunday`.
  4. Set the **Start at** time of day for the full backup.  
  Select a **Start at** time when your application isn't using Capella heavily unless you've chosen a cluster configuration with more capacity than you need.
  5. Use the **Incremental Every** list to set the frequency of incremental backups.  
  > [!TIP]  
  > If you change the **Start at** time, the next incremental backup might happen at a different time than you expect. Capella calculates the **Incremental Value** backward from the configured **Start at** time.  
  >  
  > For example, **Incremental Every** is `8 hours`, and the **Start at** time is 4 AM. If the current time is 9 PM, Capella takes an incremental backup at 8 PM, an eight-hour interval backward from 4 AM. If you change the **Start at** to 6 AM, you would see another incremental backup at 10 PM, two hours after the last backup. The backup occurs at this time because Capella recalculates the eight-hour backup interval back from the new 6 AM **Start at** time.
  6. Select **Cost Optimized Retention**. When selected, the cost optimized retention policy applies to your bucket backup. For more information, see [Cost Optimized Retention Policy](../backup-restore.md#cost-optimized-retention-policy).
  7. Set a **Retention Time** in line with your data retention policy.  
  If you selected Cost Optimized Retention, the **Retention Time** applies only to the monthly restore point.  
  Capella preserves each backup from `30 Days` to `5 Years`. After the retention time lapses, Capella schedules the backup for deletion.  
  > [!NOTE]  
  > The **Retention Time** setting applies to all future backups for a bucket. Changes to this setting do not affect previous backups.
12. To create the bucket with your chosen settings, click **Create Bucket**.

## [](#edit-bucket)Modify a Bucket

> [!NOTE]
> Limitations
> 
> For single node operational clusters, you cannot modify the **Storage Backend**, **Minimum Durability Level**, and **Number of Replicas** settings for a bucket. Capella automatically configures buckets on a single node cluster with a Couchstore backend, no minimum durability level, and no replicas. To modify these settings, you need to either [scale out your existing single node cluster](#clusters/modify-database.adoc#add-remove-nodes) or deploy a new multi-node operational cluster.

To modify a bucket, you need the [Project Owner](../../projects/project-roles.md#project-owner-role) or [Cluster Manager](../../projects/project-roles.md#project-cluster-manager-role) role for the cluster's project. If you have the [Organization Owner](../../organizations/organization-user-roles.md#organization-role-organization-owner) role, you have `Project Owner` access. NOTE: You cannot change the **Bucket Name**, **Bucket Type**, **Storage Backend**, or **Conflict Resolution** settings for an existing bucket.

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select your cluster.
3. Go to **Buckets**.
4. In the **Buckets** table, click the name of the bucket you want to modify.
5. Expand **Show Advanced Settings** to show all available settings. You can change the following settings:

  * **Memory Quota (MiB)**: Edit the amount of memory allocated to the bucket. A minimum of 100 MiB is required for a Couchstore storage backend bucket, and 1 GiB for a Magma bucket. Couchstore needs a minimum of 100 MiB, while Magma needs 100 MiB with 128 vBuckets or 1 GiB with 1024 vBuckets.
  * **Minimum Durability Level**: Choose a new minimum durability level. For more information, see the [durability](#durability) configuration instructions.
  * **Number of Replicas**: Choose the number of copies of this bucket's data that Capella creates and maintains.
  * **Flush**: Choose to turn on or turn off flush. For more information, see the [flush](#flush) configuration instructions.
  * **Time to Live**: Choose to turn on or turn off time to live. For more information, see the [time to live](#time-to-live) configuration instructions.
  * **Backup Schedule**: Change the backup schedule for the bucket. For more information about how to change a bucket's backup schedule, see the [backup schedule](#backup-schedule) instructions.
6. Click **Save**.

## [](#delete-bucket)Delete a Bucket

> [!WARNING]
> Deleting a bucket deletes all of its contents. Backups for a deleted bucket might be available for a restore operation, based on the bucket's previous **Backup** configuration.

You can delete a bucket when it's no longer needed, or when you need to replace all items within a bucket. Deleting and recreating a bucket is faster than deleting each document in a bucket.

> [!IMPORTANT]
> If the bucket is the source of a [replication](../xdcr/xdcr.md), bucket deletion fails. You must delete all destination replication buckets before you can delete a source bucket.
> 
> You can delete a destination replication bucket without deleting the source. Any configured replications, from the **Replications** page in your cluster settings, are automatically deleted after you delete a bucket.

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select your cluster.
3. Go to **Buckets**.
4. In the **Buckets Summary** table, click the name of the bucket you want to delete.
5. Click **Delete Bucket**.
6. Verify that you have chosen the correct bucket and then type `delete` into the provided field.
7. Click **Delete Bucket**.

Upon successful deletion, the bucket and all its data are deleted from the cluster.