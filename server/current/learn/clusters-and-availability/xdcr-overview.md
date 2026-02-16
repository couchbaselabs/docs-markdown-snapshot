[View original HTML](/server/current/learn/clusters-and-availability/xdcr-overview.html)

> _Cross Data Center Replication_ (XDCR) allows data to be replicated across clusters that are potentially located in different data centers. 

## [](#introduction-to-xdcr)Introduction to XDCR

Cross data center replication (XDCR) replicates data between a source bucket and a target bucket. The buckets may be located on different clusters, and in different data centers: this provides protection against data-center failure, and also provides high-performance data-access for globally distributed, mission-critical applications.

|  | In Version 7.0, Couchbase made XDCR a commercial-only feature of Enterprise Edition. See [Couchbase Modifies License of Free Community Edition Package](https://blog.couchbase.com/couchbase-modifies-license-free-community-edition-package/), for more information about the license restrictions. Also see [XDCR and Community Edition](../../manage/manage-xdcr/xdcr-management-overview.md#xdcr-and-community-edition), for information about how the new restrictions affect the experience of Community-Edition administrators. |
|  | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

Data from the source bucket is pushed to the target bucket by means of an XDCR agent, running on the source cluster, using the Database Change Protocol. Any bucket (Couchbase or Ephemeral) on any cluster can be specified as a source or a target for one or more XDCR definitions. Note, however, that if an Ephemeral bucket configured to eject data when its RAM-quota is exceeded is used as a source for XDCR, not all data written to the bucket is guaranteed to be replicated by XDCR. (See [Buckets](../buckets-memory-and-storage/buckets.md), for information on ejection.)

Cross Data Center Replication differs from intra-cluster replication in the following, principal ways:

* As indicated by their respective names, _intra-cluster replication_ replicates data across the nodes of a single cluster; while _Cross Data Center Replication_ replicates data across multiple clusters, each potentially in a different data center.
* Whereas intra-cluster replication is configured and performed with reference to only a single bucket (to which all active and replica vBuckets will correspond), XDCR requires _two_ buckets to be administrator-specified, for a replication to occur: one is the bucket on the source cluster, which provides the data to be replicated; the other is the bucket on the target cluster, which receives the replicated data.
* Whereas intra-cluster replication is configured at bucket-creation, XDCR is configured _following_ the creation of both the source and target buckets.

The starting, stopping, and pausing of XDCR all occur independently of whatever intra-cluster replication is in progress on either the source or target cluster. While running, XDCR continuously propagates mutations from the source to the target bucket.

|  | Versions of Couchbase Server before 8.0 do not support XDCR replication between buckets with different numbers of vBuckets. They also do not support Magma buckets with 128 vBuckets. Due to both these limitations, you cannot replicate from a pre-8.0 cluster to a Magma bucket with 128 vBuckets. You can replicate in the opposite direction (from a Magma bucket with 128 vBuckets to a pre-8.0 cluster) because Magma buckets on Couchbase Server 8.0 and later can replicate to buckets with a different number of vBuckets. However, you should avoid doing so because bidirectional replication is impossible in this configuration. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#tools-for-managing-xdcr)Tools and Procedures for Managing XDCR

Prior to XDCR management, source and target clusters should be appropriately prepared, as described in [Prepare for XDCR](../../manage/manage-xdcr/prepare-for-xdcr.md). Then, XDCR is managed in three stages:

1. Define a _reference_ to a remote cluster, which will be the target for Cross Data Center Replication. See [Create a Reference](../../manage/manage-xdcr/create-xdcr-reference.md).
2. Define and start a _replication_, which continuously transfers mutations from a specified source bucket to a specified target bucket. See [Create a Replication](../../manage/manage-xdcr/create-xdcr-replication.md).
3. Monitor the ongoing replication, pausing and resuming the replication if and when appropriate. See [Monitor a Replication](../../manage/manage-xdcr/create-xdcr-replication.md), [Pause a Replication](../../manage/manage-xdcr/pause-xdcr-replication.md), and [Resume a Replication](../../manage/manage-xdcr/resume-xdcr-replication.md).

Couchbase provides three options for managing these stages, which are by means of:

* _Couchbase Web Console_, which provides a graphical user interface for interactive configuration and management of replications.
* _CLI_, which provides commands and flags that allow replications to be managed from the command line.
* _REST API_, which underlies both the Web Console and CLI, and can be expressed either as a `curl` command on the command line, or within a program or script.

For procedures that cover all main XDCR management tasks, performed with all three of the principal tools, see [XDCR Management Overview](../../manage/manage-xdcr/xdcr-management-overview.md).

## [](#xdcr-direction-and-topology)XDCR Direction and Topology

XDCR allows replication to occur between source and target clusters in either of the following ways:

* _Unidirectionally_: The data contained in a specified source bucket is replicated to a specified target bucket. Although the replicated data on the source _could_ be used for the routine serving of data, it is in fact intended principally as a backup, to support disaster recovery.

![unidirectional xdcr](../_images/xdcr/unidirectional-xdcr.png) 

* _Bidirectionally_: The data contained in a specified source bucket is replicated to a specified target bucket; and the data contained in the target bucket is, in turn, replicated back to the source bucket. This allows both buckets to be used for the serving of data, which may provide faster data-access for users and applications in remote geographies.

![bidirectional xdcr](../_images/xdcr/bidirectional-xdcr.png) 

Note that XDCR provides only a single basic mechanism from which replications are built: this is the _unidirectional_ replication. A _bidirectional_ topology is created by implementing two _unidirectional_ replications, in opposite directions, between two clusters; such that a bucket on each cluster functions as both source and target.

Used in different combinations, unidirectional and bidirectional replication can support complex topologies; an example being the _ring_ topology, where multiple clusters each connect to exactly two peers, so that a complete ring of connections is formed:

![ring topology xdcr](../_images/xdcr/ring-topology-xdcr.png) 

### [](#using-xdcr-within-a-single-cluster)Using XDCR within a Single Cluster

XDCR allows a single cluster to be specified as both source cluster and target cluster: the source bucket and target bucket must still be specified as different buckets.

## [](#xdcr-filtering)XDCR Advanced Filtering

_Filtering Expressions_ can be used in XDCR replications. Each is a regular expression that is applied to the document keys on the source cluster: those document keys returned by the filtering process correspond to the documents that will be replicated to the target. For information, See [XDCR Advanced Filtering](xdcr-filtering.md).

Optionally, _deletion filters_ can be applied to a replication: these control whether the deletion of a document at source causes deletion of a replica that has been created. Each filter covers a specific deletion-context. For a description of the individual deletion filters, see [Deletion Filters](../../manage/manage-xdcr/filter-xdcr-replication.md#deletion-filters). For an explanation of the relationship between deletion filters and filters formed with regular and other filtering expressions, see [Using Deletion Filters](xdcr-filtering.md#using-deletion-filters).

### [](#xdcr-filter-binary)Filtering Binary Documents

Every JSON or binary document has a [key](../data/data.md#keys), and also has [Extended Attributes](../data/extended-attributes-fundamentals.md): XDCR filtering expressions can be applied to these. However, a binary document does _not_ have a JSON body: therefore, an XDCR filter that references a JSON body cannot be applied to the body of a binary document. In consequence, administrators must decide whether binary documents should be replicated, when a filter has been configured to refer to a JSON body.

For details on handling binary replications with Couchbase Web Console, see [Filtering Binary Documents](../../manage/manage-xdcr/filter-xdcr-replication.md#filtering-binary-documents). For details on using the REST API’s [filterBinary flag](../../rest-api/rest-xdcr-create-replication.md#filter-binary), see [Creating a Replication](../../rest-api/rest-xdcr-create-replication.md).

## [](#xdcr-payloads)XDCR Payloads

XDCR only replicates data: it does not replicate views or indexes. Views and indexes can only be replicated manually, or by administrator-provided automation: when the definitions are pushed to the target server, the views and indexes are regenerated there.

When encountered on the source cluster, non-UTF-8 encoded document IDs are automatically filtered out of replication: they are therefore not transferred to the target cluster. For each such ID, the warning output `xdcr_error.*` is written to the log files of the source cluster.

## [](#xdcr-using-scopes-and-collections)XDCR Using Scopes and Collections

XDCR supports _scopes_ and _collections_, which are provided with Couchbase Server 7.0 or a later version. Scopes and collections are supported in the following ways:

* Replication based on _implicit mapping_. Whenever a _keyspace_ (i.e. a reference to the location of a collection within its scope, provided as _scope-name_._collection-name_) is identical on source and target clusters, XDCR replicates documents from the source collection to the target collection automatically, when the respective buckets are specified as source and target.
* Replicaton based on _explicit_ mapping. The data in any source collection can be replicated to any target collection, as specified by the administrator.
* _Migration_. Data in the _default_ collection of a source bucket can be replicated to an administrator-defined collection in the target bucket.

|  | Be aware that performing data migration may result in data loss when using XDCR filters to delete data. If you are running filters that remove data, be sure to read [Configuring Deletion Filters to Prevent Data-Loss](xdcr-filtering.md#configuring-deletion-filters-to-prevent-data-loss) before attempting a migration. |
|  | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

In each case, _filtering_ can be applied.

The source-bucket may be:

* A bucket on a cluster with 7.0 or a later version, housing its data in administrator-defined collections. Thus, data can be replicated (optionally using XDCR Advancing Filtering), from one collection to another within the same bucket; or from a collection in one bucket to a collection in another bucket.
* A bucket on a cluster with 7.0 or a later version, housing its data in the `_default` collection, within the `_default` scope (this being the default initial residence for all data in a bucket of a cluster which has been upgraded from a Couchbase Server version earlier than 7.0 to a 7.0 or a later version). Thus, XDCR can subsequently be used to redistribute the data into administrator-defined collections, either within the same or within different buckets (again, optionally using XDCR Advancing Filtering).

Note that whereas _implicit_ replication is available in both Couchbase Server Enterprise and Community Edition, _explicit_ replication and _migration_ are available only in Couchbase Server Enterprise Edition.

For an introduction to scopes and collections, see [Scopes and Collections](../data/scopes-and-collections.md). For more information on how XDCR works with scopes and collections, see [XDCR with Scopes and Collections](xdcr-with-scopes-and-collections.md). Examples of collections-based XDCR are provided in [Replicate Using Scopes and Collections](../../manage/manage-xdcr/replicate-using-scopes-and-collections.md).

## [](#xdcr-process)XDCR Process

When a replication is created, it is stored internally as a _replication specification_. When the replication is started, XDCR reads the specification and creates a _pipeline_, which requests data from the source bucket, and examines every document in turn, to determine whether it is a candidate for replication to the target bucket. A document is only replicated if both of the following requirements are satisfied:

* The document meets whatever filtering criteria may have been configured. For information, See [XDCR Advanced Filtering](xdcr-filtering.md).
* The source collection within which the document resides can be mapped to a collection within the target bucket. For information, see [XDCR with Scopes and Collections](xdcr-with-scopes-and-collections.md#xdcr-with-scopes-and-collections).

If, for a given document, one or both criteria are not satisfied, the document is _dropped_ from the XDCR replication pipeline, and therefore not replicated: however, the attempted replication of other documents is continued.

Subsequent to the initial attempt to replicate all documents in the source bucket, documents are only replicated from the source bucket to the target bucket in the following circumstances:

* The document is _mutated_: which is to say, it is created, modified, deleted, or expired.  
Replication of a deleted or expired document means that the document will be correspondingly deleted or expired on the target. Note that this is the default behavior; although options are provided for _not_ replicating deletion or expiration mutations — so that the replicated documents are not removed. See the reference information for the CLI [xdcr-replicate](../../cli/cbcli/couchbase-cli-xdcr-replicate.md) command.
* On the target bucket, a collection is created that allows a new mapping to occur between a source collection and the new target collection. For information, see [Target-Collection Removal and Addition](xdcr-with-scopes-and-collections.md#target-collection-removal-and-addition).
* The current replication is _restarted_, following the editing of filtering criteria. For more information, see [Filter-Expression Editing](xdcr-filtering.md#filter-expression-editing).
* The current replication is _deleted_, and a new replication is created and started.

## [](#xdcr-priority)XDCR Priority

When throughput is high, multiple simultaneous XDCR replications are likely to compete with one another for system resources. In particular, when a replication starts, its _initial process_ may be highly consumptive of memory and bandwidth, since all documents in the source bucket are being handled.

To manage system resources in these circumstances, each replication can be assigned a priority of _High_, _Medium_, or _Low_:

* _High_. No resource constraints are applied to the replication. This is the default setting.
* _Medium_. Resource constraints are applied to the replication while its _initial process_ is underway, if the replication is in competition with one or more _High_ priority replications. Subsequently, it is treated as a _High_ priority replication.
* _Low_. Resource constraints are applied to the replication whenever it is in competition with one or more _High_ priority replications.

## [](#xdcr-conflict-resolution)XDCR Conflict Resolution

In some cases, especially when bidirectionally replicated data is being modified by applications in different locations, _conflicts_ may arise: meaning that the data of one or more documents has been differently modified more or less simultaneously, requiring resolution. XDCR provides options for _conflict resolution_, based on either _sequence number_ or _timestamp_, whereby conflicted data can be saved consistently on source and target. For more information, See [XDCR Conflict Resolution](xdcr-conflict-resolution.md).

## [](#xdcr-based-data-recovery)XDCR-Based Data Recovery

In the event of data-loss, the **cbrecovery** tool can be used to restore data. The tool accesses remotely replicated buckets, previously created with XDCR, and copies appropriate subsets of their data back onto the original source cluster.

By means of intra-cluster replication, Couchbase Server allows one or more replicas to be created for each vBucket on the cluster. This helps to ensure continued data-availability in the event of node-failure.

However, if multiple nodes within a single cluster fail simultaneously, one or more active vBuckets and all their replicas may be affected; meaning that lost data cannot be recovered locally.

In such cases, provided that a bucket affected by such failure has already been established as a source bucket for XDCR, the lost data may be retrieved from the bucket defined on the remote server as the corresponding replication-target. This retrieval is achieved from the command-line, by means of the Couchbase **cbrecovery** tool.

For a sample step-by-step procedure, see [Recover Data with XDCR](../../manage/manage-xdcr/recover-data-with-xdcr.md).

## [](#xdcr-security)XDCR Security

XDCR configuration requires that the administrator provide a username and password appropriate for access to the target cluster. When replication occurs, the password is automatically supplied, along with the data. By default, XDCR transmits both password and data in non-secure form. Optionally however, a secure connection can be enabled between clusters, in order to secure either password alone, or both password and data. The password received by the destination cluster can be authenticated either locally or externally, as described in [Authentication](../security/authentication.md).

A secure XDCR connection is enabled either by SCRAM-SHA or by TLS — depending on the administrator-specified connection-type, and the server-version of the destination cluster. Use of TLS involves certificate management: for information on preparing and using certificates, see [Manage Certificates](../../manage/manage-security/manage-certificates.md).

Two administrator-specified connection-types are possible:

* _Half_ Secure: Secures the specified password only: it does not secure data. The password is secured by hashing with SCRAM-SHA, when the destination cluster is running Couchbase Enterprise Server 5.5 or later; and by TLS encryption, when the destination cluster is running a pre-5.5 Couchbase Enterprise Server. The root certificate of the destination cluster must be provided, for a successful TLS connection to be achieved.  
Before attempting to enable half-secure replications, see the important information provided in [SCRAM SHA and XDCR](../../manage/manage-xdcr/secure-xdcr-replication.md#scram-sha-and-xdcr).
* _Full_ Secure: Handles both authentication and data-transfer via TLS.

For step-by-step procedures, see [Secure a Replication](../../manage/manage-xdcr/secure-xdcr-replication.md).

## [](#xdcr-advanced-settings)XDCR Advanced Settings

The performance of XDCR can be fine-tuned, by means of configuration-settings, specified when a replication is defined. These settings modify _compression_, source and target _nozzles_ (worker threads), _checkpoints_, _counts_, _sizes_, _network usage limits_, and more. For detailed information, see [XDCR Advanced Settings](../../xdcr-reference/xdcr-advanced-settings.md).

## [](#xdcr-bucket-flush)XDCR Bucket Flush

The **flush** operation deletes data on a local bucket: this operation is disabled if the bucket is currently the source for an ongoing replication. If the target bucket is flushed during replication, the bucket becomes temporarily inaccessible, and replication is suspended.

If either a source or a target bucket needs to be flushed after a replication has been started, the replication must be deleted, the bucket flushed, and the replication then recreated.

## [](#xdcr-and-bucket-expiration)XDCR and Expiration

Buckets, collections, and documents have a TTL setting, which determines the maximum expiration times of individual items. This is explained in detail in [Expiration](../data/expiration.md). For specific information on how TTL is affected by XDCR, see the section [Expiration and XDCR](../data/expiration.md#bucket-expiration-and-xdcr).

## [](#monitoring-xdcr-replication)Monitoring XDCR

Couchbase Server provides the ability to monitor ongoing XDCR replications, by means of the Couchbase Web Console. Detailed information is provided in [Monitor a Replication](../../manage/manage-xdcr/create-xdcr-replication.md).

## [](#xdcr-compatibility)XDCR Compatibility

[ENTERPRISE EDITION](https://www.couchbase.com/products/editions)

The following table indicates XDCR compatibility between different versions of Couchbase Server Enterprise edition, used for source and target clusters.

| **Enterprise Server Version**                                 | **8.0.x**     | **7.6.6 and later versions** | **7.6.5**, **7.6.4**, **7.6.3**, **7.6.2**, **7.6.1**, **7.6.0**, **7.2.x**, **7.1.x**, **7.0.x** |
| ------------------------------------------------------------- | ------------- | ---------------------------- | ------------------------------------------------------------------------------------------------- |
| 8.0.x                                                         | ✓             | ✓\*                          | ✓\*\* No ECCV                                                                                     |
| 7.6.6 and later                                               | ✓\*           | ✓\*                          | ✓\*\* No ECCV                                                                                     |
| 7.6.5, 7.6.4, 7.6.3, 7.6.2, 7.6.1, 7.6.0, 7.2.x, 7.1.x, 7.0.x | ✓\*\* No ECCV | ✓\*\* No ECCV                | ✓                                                                                                 |

|  | XDCR Compatibility with vBucket Configuration (for both \* and \*\*) Starting in Couchbase Server 8.0, Magma storage backend buckets can have either 128 or 1024 vBuckets. In earlier versions, all buckets had 1024 vBuckets, except on macOS. When creating XDCR replications between the Couchbase Server clusters, make sure of the compatibility of number of vBuckets with the Couchbase Server version as follows: From pre-8.0 to 8.0: The source and destination buckets must have the same number of vBuckets. For example, when replicating from a 7.x cluster to an 8.x cluster, create the target 8.x bucket with 1024 vBuckets. From 8.0 to pre-8.0: The vBucket counts do not need to match. However, the vBucket count mismatch, in the source and target buckets of an XDCR topology, does not support the bi-directional replication. Between 8.0 and later versions: Replications are supported even if the buckets have different vBucket counts. For more information about Magma storage, see [Storage Engines](../buckets-memory-and-storage/storage-engines.md). For more information about vBuckets, see [vBuckets](../buckets-memory-and-storage/vbuckets.md). Cross Cluster Versioning (ECCV) Compatibility (for \*\* only) Starting in Couchbase Server 7.6.6, buckets include the enableCrossClusterVersioning (ECCV) property, which is set to false (disabled) by default. If you set ECCV to true (enabled) on a bucket in an XDCR replication topology, then you must set ECCV to true on all buckets participating in the XDCR replication topology. Otherwise, dependent features may not function. As the Couchbase Server versions earlier than 7.6.6 do not support the enableCrossClusterVersioning bucket property, those buckets cannot participate in a replication topology containing ECCV-enabled buckets. XDCR does not automatically validate ECCV property consistency across buckets. If you want to prevent a bucket without ECCV from participating in an XDCR replication topology, then before creating or modifying XDCR replications, you must manually verify that ECCV is disabled for all participating buckets. For more information about ECCV, see [XDCR enableCrossClusterVersioning](xdcr-enable-crossclusterversioning.md). |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |