---
title: Manage Buckets
description: Create, edit, and delete buckets to manage your data storage in a
  Capella operational cluster.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-capella/edit/main/modules/clusters/pages/data-service/manage-buckets.adoc
  xref: xref:cloud:clusters:data-service/manage-buckets.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/cloud/clusters/data-service/manage-buckets.html)

# Manage Buckets

> Create, edit, and delete buckets to manage your data storage in a Capella operational cluster. 

A **bucket** is the named container in which you save your data. You may have up to 30 buckets in your cluster. You may organize the data within a bucket into different **collections**, according to content-type. A bucket's data may be [replicated](../xdcr/xdcr.md) across the cluster, to make sure that the data exists in multiple copies, and is highly available. A bucket's data may also be replicated across different clusters, potentially in different geographic locations. For more information, see [Buckets, Scopes, and Collections](about-buckets-scopes-collections.md).

The Capella UI defines buckets with default settings that support rapid prototyping and pre-production experimentation. For the subsequent design of sophisticated production systems, multiple configuration options are provided, to ensure heightened performance, integrity, and availability.

## [](#prerequisites)Prerequisites

> [!NOTE]
> Free Tier Limitations
> 
> If you're using a free tier operational cluster, you cannot create a bucket with advanced settings. Free tier clusters can create buckets only with the memory and disk bucket type, and the Magma 128 vBucket storage backend option.

To create, modify, or delete buckets in a project, you need:

* The [Project Owner](../../projects/project-roles.md#project-owner-role) or [Cluster Manager](../../projects/project-roles.md#project-cluster-manager-role) role for your cluster's project. If you have the [Organization Owner](../../organizations/organization-user-roles.md#organization-role-organization-owner) role, you have `Project Owner` access.

## [](#add-bucket)Create a Bucket

> [!IMPORTANT]
> XDCR between Magma and Couchstore
> 
> Only Couchbase Server 8.0 and later supports XDCR replication between buckets with different numbers of vBuckets. Couchstore buckets use 1024 vBuckets, while Magma buckets can use either 128 or 1024 vBuckets.
> 
> To create an XDCR replication from a bucket on a cluster using Couchbase Server 7.6 or earlier, you must use Magma with 1024 vBuckets or Couchstore.

To create a bucket:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select your cluster.
3. Go to **Data Tools** for a quick setup, or go to **Buckets** to configure advanced settings.

  * Data Tools
  * Buckets

  1. Click **Create** **Bucket** **Scope** **Collection**.
  2. In the **Bucket** field:

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
      For more information about memory management in Capella, see [Buckets and Storage](about-buckets-scopes-collections.md#buckets-storage).
    4. In the **Scope** and **Collection** fields, enter names for the bucket's first scope and collection, or select **Use system generated \_default for scope and collection**.
    5. Click **Create**.  
You can [modify your bucket's settings](#edit-bucket) at any time.

  1. Click **Create Bucket**.
  2. In the **Bucket Name** field, enter a name for the new bucket. A bucket name can only contain upper or lower case letters, numbers, underscores (`_`), periods (`.`), dashes (`-`), and percentages (`%`). You cannot set a bucket name that exceeds 100 characters in length. You cannot change a bucket name after you create a bucket.
  3. In the **Memory Quota (MiB)** field, enter a memory quota for the bucket.  
  > [!IMPORTANT]  
  > Default storage backend  
  >  
  > When using Couchbase Server 8.0 or later, the default storage backend is Magma, which needs 100 MiB with 128 vBuckets or 1 GiB with 1024 vBuckets. Couchstore needs a minimum of 100 MiB. For help with choosing the right storage backend for your bucket, see [Storage Engines](storage-engines.md).  
  Use the memory allocation graph to view the memory allocated to other buckets in the cluster, and the total amount of memory you can allocate to a new bucket.  
  > [!NOTE]  
  > The total memory quota for a bucket equals the number of data nodes in its Service Group multiplied by the memory quota you specify. If you change the number of data nodes in your Service Group, the total memory allocated to the bucket changes as well. For example, if you deploy the Data Service on 3 nodes and create a bucket with a 100 MiB memory quota, each node has 100 MiB. This gives the bucket a total of 300 MiB memory. [Scaling your cluster](../scale-database.md) up to 6 nodes with 100 MiB per node increases the bucket's maximum memory to 600 MiB. Scaling a cluster down to reduce the number of nodes, also reduces the total memory quota for the bucket. If you do not have enough memory allocated to a bucket for your data, you can encounter performance issues.  
  For more information about memory management in Capella, see [Buckets and Storage](about-buckets-scopes-collections.md#buckets-storage).
  4. (Optional) Configure advanced settings for your bucket, or accept the default values. For more information about advanced bucket settings, see [Configure Advanced Bucket Settings](#advanced-settings).  
  > [!NOTE]  
  > You cannot configure any advanced settings for a bucket on a free tier operational cluster. [Upgrade your account](../../billing/upgrade-account.md) to access all bucket customization options.
  5. Click **Create Bucket**.

### [](#advanced-settings)Configure Advanced Bucket Settings

> [!NOTE]
> You can only configure advanced settings if you create a bucket through the **Buckets** tab.

To configure advanced settings:

1. Expand **Show Advanced Settings**.
2. Choose a [**Bucket Type**](about-buckets-scopes-collections.md#bucket-types). Select **Memory and Disk** to persist data to disk, or **Memory Only** for in-memory storage only.  
> [!NOTE]  
> You cannot change your bucket type after you create a bucket. For more information about bucket types, see [Bucket Types](../../../server/current/learn/buckets-memory-and-storage/buckets.md#bucket-types) in the Couchbase Server documentation.

  * Memory and Disk
  * Memory-Only

  1. Choose a **Storage Backend**:  
  > [!IMPORTANT]  
  > XDCR between Magma and Couchstore  
  >  
  > Only Couchbase Server 8.0 and later supports XDCR replication between buckets with different numbers of vBuckets. Couchstore buckets use 1024 vBuckets, while Magma buckets can use either 128 or 1024 vBuckets.  
  >  
  > To create an XDCR replication from a bucket on a cluster using Couchbase Server 7.6 or earlier, you must use Magma with 1024 vBuckets or Couchstore.

    * **Couchstore**: Best if your dataset is small and fits into memory. Choose this for datasets that require a minimum of 100 MiB memory.
    * **Magma**: Best if your dataset is large in relation to available memory.  
      When using Magma with Couchbase Server 8.0, you must choose the number of vBuckets for the bucket. If you can allocate at least 1 GiB memory per node to your bucket, choose 1024 vBuckets for Magma for better performance at scale.

      * **128 vBuckets**: For datasets that require a minimum of 100 MiB memory.
      * **1024 vBuckets**: For datasets that require a minimum of 1 GiB memory.  
      You cannot change your storage backend after you create a bucket. For more information about the differences between Couchstore and Magma, see [Storage Engines](storage-engines.md).  
  > [!NOTE]  
  > Capella allocates the memory quota specified for a bucket on a per-node basis. The total memory quota for the bucket equals the number of data nodes in the Service Group multiplied by the specified memory quota. If the number of Data Service nodes in the cluster changes, the total memory allocated to the bucket changes based on the new number of data nodes.  
  >  
  > For example, when Data Services deploy on 3 nodes in a Capella cluster and Capella creates a new bucket, the bucket memory quota defaults to 100 MiB. This setting means Capella allocates 100 MiB to each node, giving the bucket a total of 300 MiB memory. When the cluster scales to run Data Services on 6 nodes at 100 MiB, this gives 600 MiB maximum memory for the bucket.
  2. Choose the **Conflict Resolution** method for the bucket:

    * **Sequence Number**: Use the document with the higher sequence number in case of a conflict between documents.
    * **Timestamp**: Use the document with the most recent timestamp.  
  Document conflicts occur during [XDCR](../xdcr/xdcr.md#conflict-resolution) when a document has been modified differently in different locations, requiring one version of the document to be kept and the other discarded. You cannot change your conflict resolution method after you create a bucket. For more information about conflict resolution, see [XDCR Conflict Resolution](../xdcr/xdcr.md#conflict-resolution).
  3. Choose the **Minimum Durability Level** for each write to the bucket:

    * **None**: Apply no durability level.
    * **Replicate to Majority**: Mutations replicate to a majority of the Data Service nodes, without persistence.
    * **Majority and Persist to Active**: Mutations replicate to a majority of the Data Service nodes. They're also persisted—​written and synchronized to disk—​on the node hosting the active vBucket for the data.
    * **Persist to Majority**: Mutations replicate to a majority of the Data Service nodes. They're also persisted—​written and synchronized to disk—​on all nodes.  
      Durability helps to improve data integrity during failures. For more information about durability in Couchbase clusters, see [Durability](../../../server/current/learn/data/durability.md) in the Couchbase Server documentation.  
  > [!NOTE]  
  > Limitations  
  >  
  > For single node operational clusters, the **Minimum Durability Level** is automatically set to **None**. You cannot change this setting.  
> [!WARNING]  
> Memory Only buckets lose data during cluster restarts, whether planned or unplanned, and may also lose data due to concurrent failure of multiple nodes.  
> [!NOTE]  
> Memory-Only Limitations  
>  
> You cannot use a memory only bucket with [App Endpoints](../../../app-services/app-endpoints/creating-an-app-endpoint.md). You also cannot [turn off a cluster](../off-on-database.md) with a memory only bucket, or [use a cluster on or off schedule](../off-on-schedule.md).

  1. Choose the **Conflict Resolution** method for the bucket:

    * **Sequence Number**: Use the document with the higher sequence number in case of a conflict between documents.
    * **Timestamp**: Use the document with the most recent timestamp.  
  Document conflicts occur during [XDCR](../xdcr/xdcr.md#conflict-resolution) when a document has been modified differently in different locations, requiring one version of the document to be kept and the other discarded. You cannot change your conflict resolution method after you create a bucket. For more information about conflict resolution, see [XDCR Conflict Resolution](../xdcr/xdcr.md#conflict-resolution).
  2. Choose an **Ejection Policy** for the bucket:

    * **NRU** (Not Recently Used): Make Capella remove documents with the lowest access frequency when the bucket's memory reaches capacity. This reclaims memory for saving new documents.
    * **No Ejection**: Make Capella keep all documents when the bucket's memory reaches capacity, and force new document save attempts to fail.  
  You cannot change your ejection policy after you create a bucket. For more information about ejection, see [Ejection Policy](../../../server/current/learn/buckets-memory-and-storage/storage-settings.md#storage-settings-ejection-policy) in the Couchbase Server documentation.
  3. Choose the **Minimum Durability Level** for each write to the bucket:

    * **None**: Apply no durability level.
    * **Replicate to Majority**: Mutations replicate to a majority of the Data Service nodes, without persistence.  
      Durability helps to improve data integrity during failures. For more information about durability in Couchbase clusters, see [Durability](../../../server/current/learn/data/durability.md) in the Couchbase Server documentation.  
  > [!NOTE]  
  > Limitations  
  >  
  > For single node operational clusters, the **Minimum Durability Level** is automatically set to **None**. You cannot change this setting.
3. Set the **Number of Replicas**. Based on the number nodes in your cluster, you can choose to create 1 to 3 replica copies of the data stored in this bucket. If you do not have the required number of nodes for a specific number of replicas, that option is unavailable.  
> [!NOTE]  
> Limitations  
>  
> For single node operational clusters, the **Number of Replicas** is automatically set to 0\. You cannot change this setting.
4. Enable or disable **Flush**. Flushing a bucket deletes all of its data permanently.  
> [!CAUTION]  
> To protect against inadvertent data loss, disable Flush on production clusters.
5. Enable or disable **Time to Live** (TTL).  
Enabling TTL allows you to set a maximum amount of time for which a document can exist before it's automatically deleted. When enabled, this setting allows you to specify the time-period in seconds, minutes, hours, days, or weeks. This setting applies to all collections in the bucket unless you configure a collection's TTL to a non-zero value.
6. Choose a backup schedule for the bucket according to the relative importance of the workload and data.

  * **Do Not Backup**: Do not schedule any backups.  
  > [!WARNING]  
  > **Do Not Backup** is not recommended for production clusters. To avoid data loss, you should regularly back up a production cluster.
  * **Set Weekly Schedule**: Set a weekly incremental schedule.

    1. Choose the **Day of the week** when you want Capella to take the full backup. The default value is `Sunday`.
    2. Set the **Start at** time of day for the full backup.  
      Select a **Start at** time when your application isn't using Capella heavily unless you've chosen a cluster configuration with more capacity than you need.
    3. Use the **Incremental Every** list to set the frequency of incremental backups.  
      > [!TIP]  
      > If you change the **Start at** time, the next incremental backup might happen at a different time than you expect. Capella calculates the **Incremental Value** backward from the configured **Start at** time.  
      >  
      > For example, **Incremental Every** is `8 hours`, and the **Start at** time is 4 AM. If the current time is 9 PM, Capella takes an incremental backup at 8 PM, an eight-hour interval backward from 4 AM. If you change the **Start at** to 6 AM, you would see another incremental backup at 10 PM, two hours after the last backup. The backup occurs at this time because Capella recalculates the eight-hour backup interval back from the new 6 AM **Start at** time.
    4. Set a **Retention Time** in line with your data retention policy.  
      If you enabled **Cost Optimized Retention**, the **Retention Time** applies only to the monthly restore point.  
      Capella preserves each backup from `30 Days` to `5 Years`. After the retention time lapses, Capella schedules the backup for deletion.  
      > [!NOTE]  
      > The **Retention Time** setting applies to all future backups for a bucket. Changes to this setting do not affect previous backups.
    5. Enable or disable **Cost Optimized Retention**. When enabled, the cost optimized retention policy applies to your bucket backup. For more information, see [Cost Optimized Retention Policy](../backup-restore.md#cost-optimized-retention-policy).
7. To create the bucket with your chosen settings, click **Create Bucket**.

## [](#access-bucket)View a Bucket

To view your cluster's buckets:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select your cluster.
3. Go to **Buckets**.

You can view the **Buckets Summary** to see all the buckets in your cluster. It includes the following information about each bucket:

* Bucket Name
* Documents
* Bucket Type
* Storage Backend
* Ops/Sec
* Disk
* Memory/Quota

To view more details about a bucket's configuration, click your bucket's **Name**. You can view conflict resolution, minimum durability level, replication, flush, and time to live settings. For more information, see [Modify a Bucket](#edit-bucket).

## [](#edit-bucket)Modify a Bucket

> [!NOTE]
> Limitations
> 
> * For single node operational clusters, you cannot modify the **Storage Backend**, **Minimum Durability Level**, and **Number of Replicas** settings for a bucket. Capella automatically configures buckets on a single node cluster with a Couchstore backend, no minimum durability level, and no replicas. To modify these settings, you need to either [scale out your existing single node cluster](#clusters/modify-database.adoc#add-remove-nodes) or deploy a new multi-node operational cluster.
> * For all cluster types, you cannot change the **Bucket Name**, **Bucket Type**, **Storage Backend**, or **Conflict Resolution** settings for an existing bucket.

To modify a bucket:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select your cluster.
3. Go to **Buckets**.
4. In the **Buckets** table, click the name of the bucket you want to modify.
5. Expand **Show Advanced Settings** to show all available settings. You can change the following settings:

  * **Memory Quota (MiB)**: Edit the amount of memory allocated to the bucket. A minimum of 100 MiB is required for a Couchstore storage backend bucket, and 1 GiB for a Magma bucket. Couchstore needs a minimum of 100 MiB, while Magma needs 100 MiB with 128 vBuckets or 1 GiB with 1024 vBuckets.
  * **Cross Cluster Versioning (CCV)**: Choose to enable or disable. Cross Cluster Versioning enables advanced XDCR capabilities, including mobile active replication. When enabled, XDCR stores additional metadata, called the Hybrid Logical Vector (HLV), in the document extended attributes (XATTRs) for each document it processes. For more information, see [XDCR enableCrossClusterVersioning](../../../server/current/learn/clusters-and-availability/xdcr-enable-crossclusterversioning.md).  
  CCV is automatically enabled when setting up mobile active replication. You cannot turn off CCV after enabling it.  
  CCV enables the following advanced replication scenarios when App Services Endpoints link to buckets:

    * **Bi-directional and uni-directional XDCR** when both buckets are linked with an App Endpoint.
    * **Bi-directional XDCR** when either bucket is linked with an App Endpoint.
  * **Minimum Durability Level**: Choose a new minimum durability level. For more information, see the [durability](#durability) configuration instructions.
  * **Number of Replicas**: Choose the number of copies of this bucket's data that Capella creates and maintains.
  * **Flush**: Choose to turn on or turn off flush. For more information, see the [flush](#flush) configuration instructions.
  * **Time to Live**: Choose to turn on or turn off time to live. For more information, see the [time to live](#time-to-live) configuration instructions.
  * **Backup Schedule**: Change the backup schedule for the bucket. For more information about how to change a bucket's backup schedule, see the [backup schedule](#backup-schedule) instructions.
6. Click **Save**.

## [](#delete-bucket)Delete a Bucket

> [!WARNING]
> Deleting a bucket deletes all of its contents. Backups for a deleted bucket might be available for a restore operation, based on the bucket's previous [Backup](../manage-backup.md) configuration.

You can delete a bucket when it's no longer needed, or when you need to replace all items within a bucket. Deleting and recreating a bucket is faster than deleting each document in a bucket.

> [!IMPORTANT]
> If the bucket is the source of a [replication](../xdcr/xdcr.md), bucket deletion fails. You must delete all destination replication buckets before you can delete a source bucket.
> 
> You can delete a destination replication bucket without deleting the source. Any configured replications, from the **Replications** page in your cluster settings, are automatically deleted after you delete a bucket.

To delete a bucket:

1. In the navigation breadcrumbs in the Capella UI, do 1 of the following:

  1. Click your organization name and go to **Operational**.
  2. Click your current project name or search for a project and go to **Operational**.
  3. Expand the cluster breadcrumb and search for a cluster.
2. Select your cluster.
3. Go to **Buckets**.
4. In the **Buckets Summary** table, click the name of the bucket you want to delete.
5. Click **Delete Bucket**.
6. Confirm that you want to delete this bucket and click **Delete Bucket**.

Upon successful deletion, the bucket and all its data are deleted from the cluster.

## [](#see-also)See Also

* [Buckets, Scopes, and Collections](about-buckets-scopes-collections.md)
* [Manage Scopes and Collections](scopes-collections.md)
* [Manage Documents with the Capella UI](manage-documents.md)
* [Storage Engines](storage-engines.md)
* [Manage Replications](../xdcr/manage-xdcr-replications.md)
* [Manage Bucket Backups](../manage-backup.md)