[View original HTML](/server/current/manage/manage-buckets/edit-bucket.html)

> Full, Cluster, and Bucket Administrators can edit some settings of an existing bucket. This section explains how to make changes to existing bucket settings using the Couchbase Web Console and the REST API. It also explains the possible consequences of these configuration changes. 

## [](#edit-an-existing-bucket)Edit an Existing Bucket

To edit an existing bucket configuration using the Couchbase Web Console:

1. Click **Buckets** in the vertical navigation bar.  
The **Buckets** page appears, listing the buckets in the cluster:  
![bucketsViewInitialEdit](../_images/manage-buckets/bucketsViewInitialEdit.png)
2. Click the row containing the bucket that you want to edit. This expands the row to display additional information:  
![bucketsViewWithExpandedBucketRow](../_images/manage-buckets/bucketsViewWithExpandedBucketRow.png)  
Underneath the bucket’s name are the bucket’s configuration settings. Next to this information are the memory use and disk use if the bucket is a Couchbase bucket. This row also contains links to examine and manage the bucket’s [Documents](../manage-ui/manage-ui.md#console-documents) and [Scopes and Collections](../../learn/data/scopes-and-collections.md).  
At the bottom are buttons to drop, compact (for Couchbase buckets only), and edit the bucket. If your bucket has flushing enabled, a **Flush** button also appears. See [Flush](#flush) for more information about flushing a bucket.
3. Click **Edit** to edit the bucket’s settings. The **Edit Bucket Settings** dialog appears.  
![bucket edit dialog initial](../_images/manage-buckets/bucket-edit-dialog-initial.png)  
This dialog lets you change a subset of existing settings. The next section explains the settings you can change.

## [](#making-changes)Making Changes

Many of the settings for buckets are in the **Advanced Settings** section that you need to expand to be able to edit. This displays the **Edit Bucket Settings** dialog, which permits changes to be made to a subset of existing settings. All the settings contained here are described in detail for the **Add Data Bucket** dialog, on the page [Create a Bucket](create-bucket.md).

![bucket edit dialog expanded](../_images/manage-buckets/bucket-edit-dialog-expanded.png) 

Not all the settings that appear in the dialog are editable. The settings you can edit are:

Storage Backend [ENTERPRISE EDITION](https://www.couchbase.com/products/editions)

This setting is only available for Couchbase buckets on Couchbase Server Enterprise Edition. It allows you to change the storage backend used by the bucket. Changing this setting does not immediately migrate the bucket to the new storage backend. See [Migrate a Bucket’s Storage Backend](migrate-bucket.md) for more information about migrating a bucket to a different storage backend.

Number of vBuckets [ENTERPRISE EDITION](https://www.couchbase.com/products/editions)

For Couchbase buckets using the Magma storage backend, you can change the number of vBuckets.

Memory Quota

Sets the amount of RAM allocated per node to this bucket. You cannot lower this value to be less than the current amount of memory the bucket is using on any node in your cluster. Changes you make to this setting have an immediate effect.

Replicas

The number of replicas of the bucket to be maintained by the cluster. You can change this number at any time for either type of bucket. However, you must rebalance the cluster to redistribute the replicas across the cluster.

|  | You cannot change the **Replica view indexes** setting after you have created the bucket. |
|  | ----------------------------------------------------------------------------------------- |

Bucket Max Time to Live

Sets the amount of time Couchbase Server keeps a document in this bucket before deleting it. Changes to this setting only affect documents created or mutated after the change. Other settings also affect document expiration. For more information, see [Expiration](../../learn/data/expiration.md).

Compression Mode

Whether and how Couchbase Server compresses the bucket’s data. For information on available modes and the effect of changing the mode of an existing bucket, see [Compression](../../learn/buckets-memory-and-storage/compression.md).

Ejection Method

Controls how the bucket removes documents from memory when the bucket’s memory use approaches its memory quota. You can only change this setting for Couchbase buckets. See [Ejection](../../learn/buckets-memory-and-storage/memory.md#ejection) for more information about ejection policies and [change-ejection-policy.adoc](#change-ejection-policy.adoc) for steps to change a bucket’s ejection policy.

Minimum Durability Level

Allows an appropriate durability level to be assigned to the bucket. Levels are accessed by means of a pull-down menu. The options are **none**, **majority**, **majorityAndPersistActive**, and **persistToMajority**. For information, see [Durability](../../learn/data/durability.md).

Auto-Compaction

Overrides the cluster-wide default setting for compacting the bucket’s data. See [Auto-Compaction](../manage-settings/configure-compact-settings.md) for more information. The auto-compation settings you see depend on the type of bucket you are editing. For Couchbase buckets, you must first select **Override the default auto-compaction settings?** to be able to edit the settings. The available settings are:

* **Database Fragmentation**: The percentage of data fragmentation that triggers database compaction. Only settable on Couchbase buckets.
* **Metadata Purge Interval**: The number of days between purges of the metadata for deleted items from the bucket. Settable for both Couchbase and Ephemeral buckets.

Encryption At Rest [ENTERPRISE EDITION](https://www.couchbase.com/products/editions)

Enables or disables encryption of data at rest for Couchbase buckets. This setting is only available for Couchbase buckets on Couchbase Server Enterprise Edition. See [Encryption at Rest](#learn:buckets-memory-and-storage/encryption-at-rest.adoc) for an overview of encryption at rest and [Manage Native Encryption at Rest](../manage-security/manage-native-encryption-at-rest.md) for steps you need to take in order to enable encryption at rest.

Enable Cross Cluster Versioning

Use this setting to enable the [XDCR enableCrossClusterVersioning](../../learn/clusters-and-availability/xdcr-enable-crossclusterversioning.md) bucket property. When you enable the bucket setting **Enable Cross Cluster Versioning**, for each document processed by XDCR, XDCR stores additional metadata for the document in the extended attributes. This metadata is called, [Hybrid Logical Vector (HLV)](../../learn/clusters-and-availability/xdcr-enable-crossclusterversioning.md#hlv-data-maintained-in-xattr) or a version vector.

|  | Once enabled, the Enable Cross Cluster Versioning bucket setting cannot be disabled. |
|  | ------------------------------------------------------------------------------------ |

To use the following features, enable the bucket setting **Enable Cross Cluster Versioning** on all buckets that are a part of the XDCR topology:

* [XDCR Conflict Logging](../../learn/clusters-and-availability/xdcr-conflict-logging-feature.md).
* [XDCR Active-Active with Sync Gateway](../../learn/clusters-and-availability/xdcr-active-active-sgw.md).

Flush

This setting enables or disables the [Flush](flush-bucket.md) command for the current bucket. It can be changed at any time for all types of buckets. When you enable flushing for a bucket, a **Flush** button appears on the bucket’s row in the Buckets view:

![flushBucketButton](../_images/manage-buckets/flushBucketButton.png) 

If you leave flushing turned off, the **Flush** button does not appear. See [Flush a Bucket](flush-bucket.md) for more information about flushing a bucket.

## [](#changing-bucket-settings-with-the-cli-and-rest-api)Changing Bucket-Settings with the CLI and REST API

You can change bucket-settings using the CLI command [bucket-edit](../../cli/cbcli/couchbase-cli-bucket-edit.md); or the REST [Buckets API](../../rest-api/rest-bucket-intro.md).